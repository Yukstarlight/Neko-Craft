# 模组清单

共 16 个模组：12 个来自 Modrinth（按 SHA-512 精确匹配，用户自行下载），4 个为本地适配构建（随发行版提供）。

| 模组 | 版本 | 来源 | 许可证 | 客户端 | 服务端 |
| --- | --- | --- | --- | --- | --- |
| Cardinal Components API | `6.1.3` | [Modrinth](https://modrinth.com/mod/cardinal-components-api) | MIT | optional | required |
| CreativeCore | `2.13.52` | [Modrinth](https://modrinth.com/mod/creativecore) | LGPL-3.0-only | required | optional |
| Fabric Language Kotlin | `1.13.14+kotlin.2.4.20` | [Modrinth](https://modrinth.com/mod/fabric-language-kotlin) | Apache-2.0 | optional | optional |
| Female Gender Mod | `3.2.2` | [Modrinth](https://modrinth.com/mod/female-gender) | LGPL-3.0-only | required | optional |
| Forgified Fabric API | `0.116.15+2.3.6+1.21.1` | [Modrinth](https://modrinth.com/mod/forgified-fabric-api) | Apache-2.0 | required | required |
| Geckolib | `4.8.2` | [Modrinth](https://modrinth.com/mod/geckolib) | MIT | required | optional |
| JustARod | `0.2.2` | 本地适配（[上游仓库](https://github.com/CSneko/JustARod)） | 未声明 | required | optional |
| JustARod Attribute Fix | `1.0.2` | 本地补丁（无公开页面） | 未知 | optional | optional |
| Lazr's Lib | `1.2.1` | [Modrinth](https://modrinth.com/mod/lazrs-lib) | GPL-3.0-only | required | required |
| Leashable Collars | `1.6.0-beta.2+1.21.1` | [Modrinth](https://modrinth.com/mod/leashable-collars) | MIT | required | required |
| Patchouli | `1.21.1-93-neoforge` | [Modrinth](https://modrinth.com/mod/patchouli) | CC-BY-NC-SA-3.0 | required | required |
| playerAnimator | `2.0.4+1.21.1-fabric` | [Modrinth](https://modrinth.com/mod/playeranimator) | MIT | required | required |
| Sinytra Connector | `2.0.0-beta.17+1.21.1` | [Modrinth](https://modrinth.com/mod/connector) | MIT | optional | optional |
| The Art of Stockings | `0.11.0` | 本地构建（无公开页面） | 未知 | required | optional |
| toNeko | `1.9.7` | 本地适配（[上游仓库](https://github.com/CSNeko/toNeko)） | GPL-3.0 | required | optional |
| Trinkets | `3.10.0` | [Modrinth](https://modrinth.com/mod/trinkets) | MIT | required | required |

## 关于本地适配构建

标注为「本地适配」或「本地构建」的 4 个模组，由整合包作者为兼容 Minecraft 1.21.1 / NeoForge 21.1.265 进行修改后打包，仅随本整合包分发。

- `toNeko 1.9.7`：上游 GitHub 最新 Release 为 1.9.6，Modrinth 仅提供服务端构建，本包使用本地 1.9.7 构建。
- `JustARod 0.2.2`：上游 GitHub 有同名 0.2.2，但与本包构建不一致，本包使用本地适配版本。
- `The Art of Stockings 0.11.0`：无公开 Modrinth/CurseForge 页面，作者信息为「寿云」。
- `JustARod Attribute Fix 1.0.2`：本地补丁，作者字段为 `local-patch`。

原始版权与许可证归各自作者所有；如原作者要求下架，将立即从仓库与发行版中移除。适配构建的对应源码可向整合包作者索取。

其余 12 个模组不随仓库或发行版分发，请按各自许可证从 Modrinth 获取。
