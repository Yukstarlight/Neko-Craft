# 猫娘工艺（Neko-Craft）

> **内容提示**：本项目包含成人向 / 恋物向模组与相关配置，仅面向成年用户，请勿向未成年人分发。

猫娘工艺是面向 Minecraft Java 版 **1.21.1** 的 **NeoForge** 客户端整合包，通过 **Sinytra Connector** 在 NeoForge 上加载 Fabric 模组，围绕猫娘角色、角色外观与互动内容组织。仓库保存整合包配置、语言文件、模组清单与发行版构建脚本；模组按来源分别处理：可从 Modrinth 获取的 12 个模组不随仓库分发，4 个本地适配构建随发行版提供。

## 1. 项目定位

- 面向单人游戏与小规模联机的角色扮演、外观向整合包。
- 以 NeoForge 21.1 + Connector 兼容 Fabric 生态。
- 配置与模组版本可复现；本地适配构建单独列出来源与授权声明。

## 2. 版本与依赖

| 组件 | 版本 |
| --- | --- |
| Minecraft | 1.21.1 |
| NeoForge | 21.1.265 |
| Sinytra Connector | 2.0.0-beta.17+1.21.1 |
| Java | 21 及以上（实测 22） |
| 整合包 | 1.0.0 |

## 3. 内容组成

共 16 个模组，分为三类：

- **角色与互动**：toNeko（猫娘实体、AI 对话、好感度、日记）、Leashable Collars（项圈与牵引）、The Art of Stockings（丝袜外观）、Female Gender Mod（角色模型）。
- **框架与依赖**：Sinytra Connector、Forgified Fabric API、Fabric Language Kotlin、Cardinal Components API、Trinkets、GeckoLib、Lazr's Lib、Patchouli、CreativeCore、playerAnimator、JustARod 及属性修复补丁。
- **说明**：完整清单、版本、许可证与来源见 [docs/MODS.md](docs/MODS.md)。

## 4. 安装

### 4.1 准备

1. 安装 Minecraft 1.21.1。
2. 安装 NeoForge 21.1.265，使用 Java 21 及以上。
3. 下载 [Releases](https://github.com/Yukstarlight/Neko-Craft/releases) 中的 `Neko-Craft-1.0.0.zip`。

### 4.2 部署

1. 将发行版解压到游戏目录，合并 `config/`、`ctlib/`、`mods/`。
2. 按 [docs/MODS.md](docs/MODS.md) 从 Modrinth 下载 12 个模组，放入 `mods/`。
3. 启动游戏，首次启动会生成默认配置。

### 4.3 联机

本整合包以客户端为主。部署到服务端前，请先确认各模组的服务端支持（见清单中的 server 列），并自行承担兼容性风险。

## 5. 配置说明

- `config/toneko.json`：toNeko 主配置。AI 对话默认关闭（`ai.enable=false`）；启用需自行填写 `ai.key`、`ai.base_url`、`ai.model`，仓库与发行版**不包含任何密钥**。`ai.prompt`、好感度、日记、动作等参数可按需调整。
- `config/WildfireGender/client.toml`：Female Gender Mod 的客户端设置。
- `config/connector.json`：Connector 的模组别名与 Mixin 保护开关。
- `ctlib/toneko/lang/`：toNeko 的中文、英文、日文、韩文与繁体语言文件，随包提供。

## 6. 已知限制

- Sinytra Connector 仍处于 beta，Fabric 模组在 NeoForge 上的兼容性由上游实现决定。
- 4 个本地适配构建针对 1.21.1 / NeoForge 21.1.265 调整，上游更新后可能失效，请勿与其他版本混用。
- 本项目不承诺具体性能或稳定性；出现崩溃请附 `logs/latest.log`、模组列表与复现步骤提交 Issue。
- 成人向内容：请在符合当地法律与平台规则的前提下使用与分发。

## 7. 仓库结构

```
config/                   NeoForge 与模组配置
ctlib/                    toNeko 语言文件
docs/MODS.md              16 个模组清单、来源与许可证
tools/build_release.py    构建发行版
LICENSE                   GNU GPL v3.0
```

## 8. 构建发行版

```bash
python tools/build_release.py "路径/到/模组目录"
```

脚本从指定目录读取 4 个本地适配构建，与 `config/`、`ctlib/`、文档和许可证一起打包为 `dist/Neko-Craft-1.0.0.zip`。缺少任一 jar 时会直接报错，避免产出不完整的发行版。

## 9. 许可证与第三方声明

本仓库的配置、文档与脚本以 **GNU GPL v3.0** 发布，全文见 [LICENSE](LICENSE)。

发行版内含 4 个本地适配构建：

| 文件 | 上游 / 说明 |
| --- | --- |
| `toneko-fabric-1.9.7.jar` | 上游 [CSNeko/toNeko](https://github.com/CSNeko/toNeko)，上游许可证 GPL-3.0 |
| `JustARod-0.2.2.jar` | 上游 [CSneko/JustARod](https://github.com/CSneko/JustARod)，上游许可证未声明 |
| `theartofstockings-0.11.0.jar` | 作者「寿云」，无公开页面 |
| `justarod-attrfix-neoforge-1.0.2.jar` | 本地补丁，无公开页面 |

上述构建由整合包作者为兼容当前游戏与加载器版本进行修改后打包，仅随本整合包分发。**原始版权与许可证仍归各自作者所有**；如原作者要求下架，将立即从仓库与发行版中移除。适配构建的对应源码可向整合包作者索取。

其余 12 个模组不随仓库或发行版分发，请按各自许可证从 Modrinth 获取。

Minecraft 是 Mojang Studios / Microsoft 的商标，本项目与其无隶属关系，亦不提供游戏本体或账号。

## 10. 反馈

提交 Issue 时请附上：整合包版本、Minecraft / NeoForge / Java 版本、完整模组列表、`logs/latest.log` 与复现步骤。涉及第三方模组本身的问题，请优先向上游项目反馈。
