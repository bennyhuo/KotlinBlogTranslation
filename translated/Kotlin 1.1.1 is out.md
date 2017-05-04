---
title: "[译]Kotlin 1.1.1 is out"
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
translator: SnakEys
translator_url:
---

今天我们发布了针对**Kotlin 1.1**的第一个 bug 修复更新。此更新的重点是解决导致错误代码生成的回归；我们希望尽可能快地修复此问题。详细内容请查看[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.1/ChangeLog.md) 。
重点更新如下：

* 默认情况下，已启用 Gradle 增量编译。如果需要，您仍然可以按照文档描述禁用此功能。
* Kotlin 插件现已可以通过 Gradle 插件依赖添加使用。详情可参阅相关文档。
* 禁用使用带有接收器的函数类型作为 JavaScript 外部声明的参数类型。在此之前，传递给这些参数的 lambdas 没有被正确的参数调用，并且在这个问题上没有简单的解决方法，所以现在我们决定禁用这个功能。

更新后的 Kotlin [Eclipse](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse) 和 [NetBeans](http://plugins.netbeans.org/plugin/68590/kotlin) 插件将支持 Kotlin 1.1.1，所以您可以尽情享受 Kotlin 新版本的优点而无需关注 IDE。
## 如何更新

要更新 IDEA 插件，在菜单栏中依次选择 Tools | Kotlin | Configure Kotlin Plugin Update，然后点击“Check for updates now”按钮。另外，不要忘记在 Maven 和 Gradle 构建脚本中更新编译器和标准库版本

命令行编译器可以从 [Github 发布页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1.1) 页面下载。
像往常一样，如果您在新版本中遇到任何问题，您可以在 [论坛](https://discuss.kotlinlang.org/) 中寻求帮助，在 Slack([获取邀请](http://kotlinslackin.herokuapp.com/))、或者在[问题追踪器](https://youtrack.jetbrains.com/issues/KT)提出问题 。  
让我们开始吧！
