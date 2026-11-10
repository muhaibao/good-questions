#!/usr/bin/env python3
"""从 data/*.yaml 生成静态站点到 site/（含 RSS）。"""
from __future__ import annotations

import shutil
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape as xml_escape

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TPL = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "site"
TZ = timezone(timedelta(hours=8))

# 全站唯一的发布根 URL（不要末尾斜杠，也不要在模板或 workflow 里再写一遍）。
# 页面子路径和 RSS 绝对地址都从这里推导。
# GitHub Pages 项目站形如 https://<owner>.github.io/<repo>
BASE_URL = "https://muhaibao.github.io/good-questions"


def normalize_base_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url.strip())
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise SystemExit(f"BASE_URL 必须是绝对 http(s) 地址，当前为 {url!r}")
    if parsed.query or parsed.fragment:
        raise SystemExit("BASE_URL 不能包含 query 或 fragment")
    path = parsed.path.rstrip("/")
    base = f"{parsed.scheme}://{parsed.netloc}{path}"
    base_path = "/" if path == "" else f"{path}/"
    return base, base_path


def site_meta() -> dict:
    base_url, base_path = normalize_base_url(BASE_URL)
    return {
        "name": "好问题",
        "tagline": "每日搜集世界上最有价值、最有意思的问题",
        "description": "跨领域好问题策展：AI、商业、科学、哲学、心理学。支持 RSS 订阅。",
        "lang": "zh-Hans",
        "base_url": base_url,
        "base_path": base_path,
        "built_at": datetime.now(TZ).strftime("%Y-%m-%d %H:%M"),
        "timezone_label": "Asia/Shanghai",
    }


def load_data():
    cats = yaml.safe_load((DATA / "categories.yaml").read_text(encoding="utf-8"))["categories"]
    questions = yaml.safe_load((DATA / "questions.yaml").read_text(encoding="utf-8"))
    cat_map = {c["id"]: c for c in cats}
    seen = set()
    for q in questions:
        if q["id"] in seen:
            raise SystemExit(f"重复的问题 id: {q['id']}")
        seen.add(q["id"])
        if q["category"] not in cat_map:
            raise SystemExit(f"未知领域 {q['category']}（问题 {q['id']}）")
        q["category_meta"] = cat_map[q["category"]]
    questions.sort(key=lambda q: (q["date"], q["id"]), reverse=True)
    return cats, questions


def rfc822(date_str: str) -> str:
    # date_str YYYY-MM-DD -> RSS pubDate in +0800
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=TZ, hour=8)
    return format_datetime(dt)


def abs_url(base_url: str, rel: str) -> str:
    return f"{base_url}/{rel.lstrip('/')}"


def xml_text(value: str) -> str:
    return xml_escape(value)


def xml_attr(value: str) -> str:
    return xml_escape(value, {'"': "&quot;", "'": "&apos;"})


def cdata(value: str) -> str:
    return value.replace("]]>", "]]]]><![CDATA[>")


def build_rss(site: dict, questions, title, description, page_path: str, self_path: str, out_path: Path):
    base_url = site["base_url"]
    items = []
    for q in questions:
        item_link = abs_url(base_url, f"questions/{q['id']}.html")
        desc = f"<p>{xml_text(q['commentary'])}</p>"
        if q.get("title_en"):
            desc += f"<p><em>{xml_text(q['title_en'])}</em></p>"
        desc += (
            f"<p>来源：<a href=\"{xml_attr(q['source_url'])}\">"
            f"{xml_text(q['source_name'])}</a>"
        )
        if q.get("author"):
            desc += f" · {xml_text(q['author'])}"
        desc += "</p>"
        items.append(
            f"""    <item>
      <title>{xml_text(q['title_zh'])}</title>
      <link>{xml_text(item_link)}</link>
      <guid isPermaLink="true">{xml_text(item_link)}</guid>
      <pubDate>{rfc822(q['date'])}</pubDate>
      <category>{xml_text(q['category_meta']['name'])}</category>
      <description><![CDATA[{cdata(desc)}]]></description>
    </item>"""
        )
    if questions:
        latest = rfc822(questions[0]["date"])
    else:
        latest = format_datetime(datetime.now(TZ))
    self_link = abs_url(base_url, self_path)
    channel_link = abs_url(base_url, page_path) if page_path else f"{base_url}/"
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{xml_text(title)}</title>
    <link>{xml_text(channel_link)}</link>
    <description>{xml_text(description)}</description>
    <language>zh-cn</language>
    <lastBuildDate>{latest}</lastBuildDate>
    <atom:link href="{xml_attr(self_link)}" rel="self" type="application/rss+xml"/>
{chr(10).join(items)}
  </channel>
</rss>
"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(xml, encoding="utf-8")


def main():
    site = site_meta()
    cats, questions = load_data()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "questions").mkdir()
    (OUT / "category").mkdir()
    (OUT / "feeds").mkdir()
    (OUT / "static").mkdir()

    if (STATIC / "css").exists():
        shutil.copytree(STATIC / "css", OUT / "static" / "css", dirs_exist_ok=True)
    if (STATIC / "js").exists() and any((STATIC / "js").iterdir()):
        shutil.copytree(STATIC / "js", OUT / "static" / "js", dirs_exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(TPL)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    by_date = defaultdict(list)
    by_cat = defaultdict(list)
    for q in questions:
        by_date[q["date"]].append(q)
        by_cat[q["category"]].append(q)

    dates = sorted(by_date.keys(), reverse=True)
    today = dates[0] if dates else datetime.now(TZ).strftime("%Y-%m-%d")
    todays = by_date[today]

    ctx_base = {
        "site": site,
        "categories": cats,
        "today": today,
        "all_dates": dates,
        "total": len(questions),
    }

    env.get_template("index.html").stream(
        **ctx_base, questions=todays, recent_dates=dates[:14]
    ).dump(str(OUT / "index.html"), encoding="utf-8")

    env.get_template("archive.html").stream(
        **ctx_base, by_date=dict(sorted(by_date.items(), reverse=True))
    ).dump(str(OUT / "archive.html"), encoding="utf-8")

    env.get_template("about.html").stream(**ctx_base).dump(
        str(OUT / "about.html"), encoding="utf-8"
    )

    for c in cats:
        qs = by_cat.get(c["id"], [])
        env.get_template("category.html").stream(
            **ctx_base, category=c, questions=qs
        ).dump(str(OUT / "category" / f"{c['id']}.html"), encoding="utf-8")

    for q in questions:
        env.get_template("question.html").stream(
            **ctx_base, question=q
        ).dump(str(OUT / "questions" / f"{q['id']}.html"), encoding="utf-8")

    build_rss(
        site,
        questions,
        f"{site['name']} — 全部",
        site["description"],
        "",
        "feed.xml",
        OUT / "feed.xml",
    )
    build_rss(
        site,
        questions,
        f"{site['name']} — 全部",
        site["description"],
        "",
        "feeds/all.xml",
        OUT / "feeds" / "all.xml",
    )

    for c in cats:
        qs = by_cat.get(c["id"], [])
        build_rss(
            site,
            qs,
            f"{site['name']} — {c['name']}",
            c["description"],
            f"category/{c['id']}.html",
            f"feeds/{c['id']}.xml",
            OUT / "feeds" / f"{c['id']}.xml",
        )

    env.get_template("feeds.html").stream(**ctx_base).dump(
        str(OUT / "feeds.html"), encoding="utf-8"
    )

    print(f"built {len(questions)} questions, {len(dates)} days -> {OUT}")
    print(f"base_url={site['base_url']} base_path={site['base_path']}")


if __name__ == "__main__":
    main()
