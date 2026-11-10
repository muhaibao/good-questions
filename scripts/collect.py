#!/usr/bin/env python3
"""每日采集候选好问题：HN Ask、Stack Exchange、Manifold、arXiv、Marginal Revolution。

用法:
  python3 scripts/collect.py
  python3 scripts/collect.py --out data/candidates/YYYY-MM-DD.json

不抓取知乎 / Quora / Reddit。输出为候选池，需人工或后续评分筛选后写入 data/questions.yaml。
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
TZ = timezone(timedelta(hours=8))  # Asia/Shanghai

UA = "GoodQuestionsBot/0.1 (+local prototype; polite fetch)"


def fetch_json(url: str, timeout: int = 30):
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_text(url: str, timeout: int = 30) -> str:
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", s.lower()).strip("-")
    return s[:60] or "item"


# --- sources ---

def collect_hn_ask(limit: int = 40) -> list[dict]:
    url = (
        "https://hn.algolia.com/api/v1/search_by_date?"
        + urlencode({"tags": "ask_hn", "hitsPerPage": str(limit)})
    )
    data = fetch_json(url)
    out = []
    for h in data.get("hits", []):
        title = h.get("title") or ""
        if not title.lower().startswith("ask hn"):
            continue
        points = h.get("points") or 0
        oid = h.get("objectID")
        out.append(
            {
                "title_en": title,
                "source_name": "Hacker News — Ask HN",
                "source_url": f"https://news.ycombinator.com/item?id={oid}",
                "author": h.get("author") or "",
                "source_type": "hackernews",
                "score": points,
                "category_guess": "ai" if re.search(r"\bAI\b|LLM|GPT", title, re.I) else "business",
                "collected_from": "hn_algolia",
            }
        )
    out.sort(key=lambda x: -x["score"])
    return out


def collect_stackexchange(site: str, category: str, pagesize: int = 20) -> list[dict]:
    url = (
        "https://api.stackexchange.com/2.3/questions?"
        + urlencode(
            {
                "order": "desc",
                "sort": "votes",
                "site": site,
                "pagesize": str(pagesize),
            }
        )
    )
    data = fetch_json(url)
    out = []
    for q in data.get("items", []):
        title = html.unescape(q.get("title") or "")
        owner = (q.get("owner") or {}).get("display_name") or ""
        out.append(
            {
                "title_en": title,
                "source_name": f"{site} Stack Exchange",
                "source_url": q.get("link") or "",
                "author": owner,
                "source_type": "stackexchange",
                "score": q.get("score") or 0,
                "category_guess": category,
                "collected_from": f"se_{site}",
            }
        )
    return out


def collect_manifold(term: str, category: str, limit: int = 15) -> list[dict]:
    url = (
        "https://api.manifold.markets/v0/search-markets?"
        + urlencode({"term": term, "limit": str(limit), "sort": "liquidity"})
    )
    data = fetch_json(url)
    out = []
    for m in data if isinstance(data, list) else []:
        q = m.get("question") or ""
        if not q.endswith("?"):
            # prediction markets often are yes/no propositions; keep if question-like
            if "?" not in q:
                continue
        out.append(
            {
                "title_en": q,
                "source_name": "Manifold Markets",
                "source_url": m.get("url") or "",
                "author": (m.get("creator") or {}).get("username")
                if isinstance(m.get("creator"), dict)
                else str(m.get("creatorUsername") or ""),
                "source_type": "manifold",
                "score": m.get("uniqueBettorCount") or 0,
                "category_guess": category,
                "collected_from": f"manifold_{term}",
            }
        )
    return out


def collect_arxiv_ai(limit: int = 15) -> list[dict]:
    """从 arXiv cs.AI 摘要标题生成「开放问题」候选（保留论文链接）。"""
    try:
        import feedparser
    except ImportError:
        print("feedparser missing; skip arxiv", file=sys.stderr)
        return []
    feed = feedparser.parse("https://rss.arxiv.org/rss/cs.AI")
    out = []
    for e in feed.entries[:limit]:
        title = re.sub(r"\s+", " ", (e.get("title") or "").replace("\n", " ")).strip()
        link = e.get("link") or ""
        # Frame as a research question without fabricating claims
        q = f"这篇工作提出的问题是否站得住：{title}？"
        out.append(
            {
                "title_en": title,
                "title_zh_draft": q,
                "source_name": "arXiv cs.AI",
                "source_url": link,
                "author": e.get("author") or "",
                "source_type": "arxiv",
                "score": 0,
                "category_guess": "ai",
                "collected_from": "arxiv_cs_ai",
                "note": "候选：需编辑改写成独立好问题，勿直接当成品发布",
            }
        )
    return out


def collect_marginal_revolution(limit: int = 10) -> list[dict]:
    try:
        import feedparser
    except ImportError:
        return []
    feed = feedparser.parse("https://marginalrevolution.com/feed")
    out = []
    for e in feed.entries[:limit]:
        title = e.get("title") or ""
        link = e.get("link") or ""
        out.append(
            {
                "title_en": title if "?" in title else f"What interesting question does this raise: {title}?",
                "source_name": "Marginal Revolution",
                "source_url": link,
                "author": "Tyler Cowen / Alex Tabarrok",
                "source_type": "rss",
                "score": 0,
                "category_guess": "business",
                "collected_from": "marginal_revolution",
                "note": "博客帖；需提炼真正的问题句",
            }
        )
    return out


def heuristic_filter(items: list[dict], min_score: int = 0) -> list[dict]:
    """轻量启发式：标题含问号或 Ask、长度适中、排除纯公告。"""
    skip = re.compile(r"down\?$|outage|merry christmas|thank hn: thank", re.I)
    kept = []
    for it in items:
        t = it.get("title_en") or ""
        if skip.search(t):
            continue
        if it["source_type"] == "hackernews" and it.get("score", 0) < 2 and min_score == 0:
            # keep low-score recent for inspection but mark
            it["weak"] = True
        if len(t) < 12 or len(t) > 280:
            continue
        kept.append(it)
    # prefer higher score
    kept.sort(key=lambda x: (-(x.get("score") or 0), x.get("title_en") or ""))
    return kept


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="", help="输出 JSON 路径")
    args = ap.parse_args()

    today = datetime.now(TZ).strftime("%Y-%m-%d")
    out_path = Path(args.out) if args.out else ROOT / "data" / "candidates" / f"{today}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    candidates: list[dict] = []
    errors: list[str] = []

    collectors = [
        ("HN Ask", lambda: collect_hn_ask()),
        ("SE philosophy", lambda: collect_stackexchange("philosophy", "philosophy")),
        ("SE psychology", lambda: collect_stackexchange("psychology", "psychology")),
        ("SE ai", lambda: collect_stackexchange("ai", "ai")),
        ("SE economics", lambda: collect_stackexchange("economics", "business")),
        ("Manifold AI", lambda: collect_manifold("AI", "ai")),
        ("Manifold science", lambda: collect_manifold("science", "science")),
        ("arXiv cs.AI", lambda: collect_arxiv_ai()),
        ("Marginal Revolution", lambda: collect_marginal_revolution()),
    ]

    for name, fn in collectors:
        try:
            got = fn()
            print(f"[ok] {name}: {len(got)}")
            candidates.extend(got)
        except Exception as e:
            msg = f"[err] {name}: {e}"
            print(msg, file=sys.stderr)
            errors.append(msg)

    filtered = heuristic_filter(candidates)
    # de-dupe by URL
    seen = set()
    unique = []
    for it in filtered:
        u = it.get("source_url") or it.get("title_en")
        if u in seen:
            continue
        seen.add(u)
        unique.append(it)

    payload = {
        "collected_at": datetime.now(TZ).isoformat(timespec="seconds"),
        "timezone": "Asia/Shanghai",
        "count": len(unique),
        "errors": errors,
        "candidates": unique,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(unique)} candidates -> {out_path}")


if __name__ == "__main__":
    main()
