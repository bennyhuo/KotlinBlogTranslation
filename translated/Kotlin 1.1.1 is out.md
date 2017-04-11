---
title: [译]Kotlin 1.1.1 is out
date: 2017-03-14 20:29:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/03/kotlin-1-1-1-is-out/
---

今天我们发布了Kotlin 1.1的第一个bug修复。此更新的主要重点是解决导致错误代码生成的回归;我们希望尽可能快地获得这些修复。更改日志中提供了详细信息。
值得强调的具体变化有：

* 默认情况下，已启用Gradle增量编译。如果需要，您仍然可以按照文档中所述将其关闭。
* Kotlin插件现在可以在Gradle插件门户中使用。有关使用说明，请参阅文档。
* 使用带有接收器的函数类型作为JavaScript外部声明的参数类型不再允许。以前，传递给这些参数的lambdas没有被正确的参数调用，并且在这个问题上没有简单的解决方法，所以现在我们决定禁用这个功能。

我们还更新了Kotlin Eclipse和NetBeans插件以包含Kotlin 1.1.1，因此无论IDE选择如何，您都可以享受新Kotlin版本的优势。
## 如何更新

要更新IDEA插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“检查更新现在”按钮。另外，别忘了在Maven和Gradle构建脚本中更新编译器和标准库版本。
命令行编译器可以从Github发行页面下载。
像往常一样，如果您遇到新版本的任何问题，欢迎您在论坛上，Slack（在这里获得邀请）或在问题跟踪器中报告问题，寻求帮助。
让我们来吧！
