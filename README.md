# 好问题

每日策展「最有价值 / 最有意思」的问题。优先领域：AI、商业、科学、哲学、心理学。支持 RSS。

线上地址：<https://muhaibao.github.io/good-questions/>

## 站点根 URL

只改 `scripts/build.py` 顶部的 `BASE_URL`（无末尾斜杠）。页面里的子路径链接（`/good-questions/...`）和 RSS 里的绝对地址都从这一处推导，模板和 GitHub Actions 不再另写一份。

## 本地构建

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
```

产物在 `site/`（已加入 `.gitignore`）。按 GitHub Pages 项目站的子路径预览：

```bash
mkdir -p /tmp/gq-preview
ln -sfn "$(pwd)/site" /tmp/gq-preview/good-questions
python3 -m http.server 8765 --directory /tmp/gq-preview
```

然后打开 <http://127.0.0.1:8765/good-questions/>。

采集候选（不会发布）：

```bash
python3 scripts/collect.py
```

候选写入 `data/candidates/`。筛选后手工编辑 `data/questions.yaml`，再重新构建。

## 发布

推送到 `main` 后，`.github/workflows/pages.yml` 会安装依赖、运行 `scripts/build.py`，并用 GitHub Pages 官方 action 部署 `site/`。`collect.py` 不在 CI 中运行，也不会自动把候选写进已发布问题。

若仓库还没开通过 Pages，需要仓库管理员在 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。默认的 `GITHUB_TOKEN` 通常没有创建 Pages 站点的权限。

## 目录

```
data/
  categories.yaml             # 领域
  questions.yaml              # 已发布问题（手工维护）
  candidates/YYYY-MM-DD.json  # 每日采集候选池
scripts/
  collect.py                  # 从 HN / SE / Manifold / arXiv / MR 拉候选
  build.py                    # 生成静态站 + RSS（BASE_URL 在这里）
templates/  static/           # 模板与样式
site/                         # 构建产物
```

## RSS

- 总源：`feed.xml`（`feeds/all.xml` 是同一批条目、各自的 self 链接）
- 分领域：`feeds/{ai,business,science,philosophy,psychology}.xml`

条目的 `<link>`、`<guid>` 和 `<atom:link rel="self">` 都是基于 `BASE_URL` 的绝对 URL。

## 许可与抓取边界

摘要改写 + 出处链接；不抓取知乎 / Quora / Reddit。Stack Exchange 内容请遵循各站 CC BY-SA 等声明。
