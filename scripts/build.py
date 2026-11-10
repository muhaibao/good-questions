#!/usr/bin/env python3
"""从 data/*.yaml 生成静态站点到 site/（含 RSS）。"""
from __future__ import annotations

import html
import shutil
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TPL = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "site"
TZ = timezone(timedelta(hours=8))

SITE = {
    "name": "好问题",
    "tagline": "每日搜集世界上最有价值、最有意思的问题",
    "description": "跨领域好问题策展：AI、商业、科学、哲学、心理学。支持 RSS 订阅。",
    "lang": "zh-Hans",
    "base_url": "https://muhaibao.github.io/good-questions",
    "built_at": datetime.now(TZ).strftime("%Y-%m-%d %H:%M"),
    "timezone_label": "Asia/Shanghai",
}


def load_data():
    cats = yaml.safe_load((DATA / "categories.yaml").read_text(encoding="utf-8"))["categories"]
    questions = yaml.safe_load((DATA / "questions.yaml").read_text(encoding="utf-8"))
    cat_map = {c["id"]: c for c in cats}
    for q in questions:
        q["category_meta"] = cat_map[q["category"]]
    questions.sort(key=lambda q: (q["date"], q["id"]), reverse=True)
    return cats, questions


def rfc822(date_str: str) -> str:
    # date_str YYYY-MM-DD -> RSS pubDate in +0800
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=TZ, hour=8)
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


def atom_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=TZ, hour=8)
    return dt.isoformat(timespec="seconds")


def build_rss(questions, title, description, link_self, out_path: Path):
    base = SITE["base_url"].rstrip("/")
    items = []
    for q in questions:
        item_link = f"{base}/questions/{q['id']}.html"
        desc = f"<p>{xml_escape(q['commentary'])}</p>"
        if q.get("title_en"):
            desc += f"<p><em>{xml_escape(q['title_en'])}</em></p>"
        answer = q.get("answer") or {}
        if answer.get("summary"):
            desc += f"<p><strong>解答综述</strong> {xml_escape(answer['summary'])}</p>"
        desc += f"<p>来源：<a href=\"{xml_escape(q['source_url'])}\">{xml_escape(q['source_name'])}</a>"
        if q.get("author"):
            desc += f" · {xml_escape(q['author'])}"
        desc += "</p>"
        items.append(
            f"""    <item>
      <title>{xml_escape(q['title_zh'])}</title>
      <link>{xml_escape(item_link)}</link>
      <guid isPermaLink="false">{xml_escape(q['id'])}</guid>
      <pubDate>{rfc822(q['date'])}</pubDate>
      <category>{xml_escape(q['category_meta']['name'])}</category>
      <description><![CDATA[{desc}]]></description>
    </item>"""
        )
    latest = questions[0]["date"] if questions else datetime.now(TZ).strftime("%Y-%m-%d")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{xml_escape(title)}</title>
    <link>{xml_escape(base + '/')}</link>
    <description>{xml_escape(description)}</description>
    <language>zh-cn</language>
    <lastBuildDate>{rfc822(latest)}</lastBuildDate>
    <atom:link href="{xml_escape(base + '/' + link_self)}" rel="self" type="application/rss+xml"/>
{chr(10).join(items)}
  </channel>
</rss>
"""
    out_path.write_text(xml, encoding="utf-8")


def main():
    cats, questions = load_data()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "questions").mkdir()
    (OUT / "category").mkdir()
    (OUT / "feeds").mkdir()
    (OUT / "static").mkdir()

    # copy static
    if (STATIC / "css").exists():
        shutil.copytree(STATIC / "css", OUT / "static" / "css", dirs_exist_ok=True)
    if (STATIC / "js").exists():
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
        "site": SITE,
        "categories": cats,
        "today": today,
        "all_dates": dates,
        "total": len(questions),
    }

    # index
    env.get_template("index.html").stream(
        **ctx_base, questions=todays, recent_dates=dates[:14]
    ).dump(str(OUT / "index.html"), encoding="utf-8")

    # archive
    env.get_template("archive.html").stream(
        **ctx_base, by_date=dict(sorted(by_date.items(), reverse=True))
    ).dump(str(OUT / "archive.html"), encoding="utf-8")

    # about
    env.get_template("about.html").stream(**ctx_base).dump(
        str(OUT / "about.html"), encoding="utf-8"
    )

    # categories
    for c in cats:
        qs = by_cat.get(c["id"], [])
        env.get_template("category.html").stream(
            **ctx_base, category=c, questions=qs
        ).dump(str(OUT / "category" / f"{c['id']}.html"), encoding="utf-8")

    # question detail
    for q in questions:
        env.get_template("question.html").stream(
            **ctx_base, question=q
        ).dump(str(OUT / "questions" / f"{q['id']}.html"), encoding="utf-8")

    # RSS
    build_rss(
        questions,
        f"{SITE['name']} — 全部",
        SITE["description"],
        "feeds/all.xml",
        OUT / "feeds" / "all.xml",
    )
    # also root feed.xml convenience
    shutil.copy(OUT / "feeds" / "all.xml", OUT / "feed.xml")

    for c in cats:
        qs = by_cat.get(c["id"], [])
        build_rss(
            qs,
            f"{SITE['name']} — {c['name']}",
            c["description"],
            f"feeds/{c['id']}.xml",
            OUT / "feeds" / f"{c['id']}.xml",
        )

    # feeds index page
    env.get_template("feeds.html").stream(**ctx_base).dump(
        str(OUT / "feeds.html"), encoding="utf-8"
    )

    print(f"built {len(questions)} questions, {len(dates)} days -> {OUT}")


if __name__ == "__main__":
    main()
