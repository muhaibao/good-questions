# 好问题（本地原型）

每日策展「最有价值 / 最有意思」的问题。优先领域：AI、商业、科学、哲学、心理学。每题附详细解答（综述、多种观点与可查出处、未决部分）。支持 RSS。

部署地址（待推送）：https://muhaibao.github.io/good-questions

## 技术选型

Python 3 + Jinja2 静态生成（YAML 数据 → `site/`），无构建依赖，便于日后部署到 GitHub Pages / Cloudflare Pages。

## 目录

```
data/
  categories.yaml          # 领域
  questions.yaml           # 已发布问题（成品）
  candidates/YYYY-MM-DD.json  # 每日采集候选池
scripts/
  collect.py               # 从 HN / SE / Manifold / arXiv / MR 拉候选
  build.py                 # 生成静态站 + RSS
templates/  static/        # 模板与样式
site/                      # 构建产物（可离线打开 index.html）
screenshots/               # 预览截图
```

## 常用命令

```bash
cd /workspace/good-questions
python3 scripts/collect.py          # 写入 data/candidates/
# 人工/半自动筛选后编辑 data/questions.yaml
python3 scripts/build.py            # 输出到 site/
```

离线预览：打开 `site/index.html`，或解压上级目录的 `good-questions-preview.zip`。

## RSS

- 总源：`site/feed.xml`（同 `site/feeds/all.xml`）
- 分领域：`site/feeds/{ai,business,science,philosophy,psychology}.xml`

## 许可与抓取边界

摘要改写 + 出处链接；不抓取知乎 / Quora / Reddit。Stack Exchange 内容请遵循各站 CC BY-SA 等声明。
