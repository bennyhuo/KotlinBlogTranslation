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
---

今天我们发布了针对<strong> Kotlin 1.1 </strong>的第一个bug修复更新。此更新的主要重点是解决导致错误代码生成的回归；我们希望尽可能快地获得这些修复。详细内容请查看[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.1/ChangeLog.md) 。
重点更新如下：

* 默认情况下，已启用Gradle增量编译。如果需要，您仍然可以按照文档描述将其关闭。
* Kotlin插件现在可以在Gradle插件门户中使用。详情使用请参阅文档。
* 禁用使用带有接收器的函数类型作为JavaScript外部声明的参数类型。在此之前，传递给这些参数的lambdas没有被正确的参数调用，并且在这个问题上没有简单的解决方法，所以现在我们决定禁用这个功能。

更新后的Kotlin [Eclipse](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse) 和 [NetBeans](http://plugins.netbeans.org/plugin/68590/kotlin) 插件将支持Kotlin 1.1.1，所以您可以尽情享受Kotlin新版本的优点而无需关注IDE。
## 如何更新

要更新IDEA插件，在菜单栏中依次选择 Tools | Kotlin | Configure Kotlin Plugin Update，然后点击“Check for updates now”按钮。另外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本

命令行编译器可以从 [Github发布页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1.1) 页面下载。
像往常一样，如果您在新版本中遇到任何问题，您可以在 [论坛](https://discuss.kotlinlang.org/) 中寻求帮助，在Slack(在[这里](http://kotlinslackin.herokuapp.com/)获取邀请)，或者在[问题追踪器](https://youtrack.jetbrains.com/issues/KT)提出问题 。
让我们来吧！
