# Project Memory — yemanzhongting.github.io

## 基本信息
- 网站：giserzhang.xyz，托管于 GitHub Pages
- 框架：Jekyll，主题 Academic Pages（基于 Minimal Mistakes）
- 主题语言：英文；已添加中文双语支持

## 双语方案（2026-06-13 实施）
- 中文页面统一放在 /zh/ 路径下
- front matter 用 `lang: zh` 标记中文页面
- `_data/navigation-zh.yml` 存放中文导航菜单
- `_includes/masthead.html` 根据 page.lang 切换导航，并注入右上角语言切换按钮
- 路由映射在 masthead.html 的 JS routeMap 对象中维护

## 关键目录
- `_pages/` — 静态页面（about, cv, publications, portfolio, markdown, year-archive）
  - 中文版：`*-zh.md` / `*-zh.html`
- `_data/navigation.yml` — 英文导航
- `_data/navigation-zh.yml` — 中文导航
- `_includes/masthead.html` — 顶部导航栏（含语言切换逻辑）

## 作者信息
- 张岩（Yan Zhang），香港中文大学太空与地球信息科学研究所
- 邮箱：sggzhang@whu.edu.cn / yanzhang@cuhk.edu.hk
- 微信公众号：城市感知计算（18k+ followers）
