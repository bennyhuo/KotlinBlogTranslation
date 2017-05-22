---
title: "[译]Kotlin 1.0.7 is out"
date: 2017-03-15 22:21:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/03/kotlin-1-0-7-is-out/
translator: pye52
translator_url: https://github.com/pye52
---

我们很高兴地宣布Kotlin 1.0.x系列的最后一个更新，Kotlin 1.0.7已经发布了。需要重点关注的是该补丁针对Gradle和annotation processing进行修复，此前无法升级到1.1版本的用户现在可以正常使用了。完整的修复列表可以在[更新日志](https://github.com/JetBrains/kotlin/blob/1.0.7/ChangeLog.md)查看。
要在Maven或Gradle版本中更新版本，只需在构建脚本中更改Kotlin版本号。命令行编译器会在[Github发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.0.7)中下载。
在IntelliJ IDEA和Android Studio中，如果您使用Kotlin 1.0.7构建项目，我们建议使用1.1版本的插件，并将语言版本切换为1.0。如果您确实想要安装1.0.7版本的插件，可以在[Kotlin插件页面](https://plugins.jetbrains.com/plugin/6954-kotlin)下载相应版本，并通过IDE的“从磁盘安装插件...”按钮进行安装。
一如既往，如果您在新版本中遇到任何问题，欢迎您在[讨论组](https://discuss.kotlinlang.org/)或者Slack（在[这里](http://kotlinslackin.herokuapp.com/)获得邀请）里寻求帮助，或在[这里](https://youtrack.jetbrains.com/issues/KT)提交issue。
让我们来享受Kotlin吧！