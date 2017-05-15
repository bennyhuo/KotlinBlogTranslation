---
title: "[译]Kotlin 1.1: What’s coming in the standard library"
date: 2017-01-25 00:15:00
author: ilya.gorbunov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-whats-coming-in-the-standard-library/
translator:
translator_url:
---

## Java 9 准备工作

Java 9 即将到来 [项目拼图](http://openjdk.java.net/projects/jigsaw/spec/sotms/) 到桌面 -  Java 平台模块系统。它所施加的约束之一是没有两个模块可以在同一个包中声明公共 API。当有两个有助于同一个软件包的模块时，这种情况称为“拆分”软件包。
我们在运行时工具中使用拆分包面临这个问题：首先，kotlin-runtime 和 kotlin-stdlib 模块共享很多 kotlin。* packages，第二，kotlin-runtime 和 kotlin-reflect share kotlin.reflect 包。我们要做的是使我们的工件对模块系统更加友好：

0. 我们将 kotlin-runtime 和 kotlin-stdlib 合并到单个工件 kotlin-stdlib 中。此外，我们将将编译器分发中的 kotlin-runtime.jar 重命名为 kotlin-stdlib.jar，以减少在不同构建系统中使用不同名称的标准库引起的混淆。

这个重命名将分两个阶段进行：在 1.1 中，编译器分发中的 kotlin-runtime.jar 和 kotlin-stdlib.jar 都将具有相同的内容，而在 1.2 中，前者将被删除。

