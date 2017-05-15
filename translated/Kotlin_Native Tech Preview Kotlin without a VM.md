---
title: "[译]Kotlin/Native Tech Preview: Kotlin without a VM"
date: 2017-04-04 14:42:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/04/kotlinnative-tech-preview-kotlin-without-a-vm/  
translator:SnakEys  
translator_url:https://github.com/SnakeEys  

---

很高兴告诉大家，**Kotlin/Native**的第一个技术预览版已经具备将Kotlin代码编译为机器码的能力了。Kotlin/Native编译器能够生成独立的可执行文件，不需要借助任何虚拟机即可运行。  

尽管目前该版本的功能尚未完善，但这并不妨碍您去尝试使用该技术，还可以在此查看[源代码](https://github.com/JetBrains/kotlin-native/)。编译器基于Apache 2 OSS许可证下使用。

{% raw %}
<p><img alt="KotlinNative" class="alignnone size-full wp-image-4889" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/04/KotlinNative.png" width="800"/><br/>
<span id="more-4862"></span></p>
{% endraw %}

## 任务

Kotlin/Native是让Kotlin贯穿所有应用场景又一大进步。而最终目的则是能够使用Kotlin编写从服务器端到网页甚至移动客户端的每个组件。对此，共享技能是一大激励，另外则是共享实际代码。  

对于平台内部代码重用，我们有着如下愿景：使用Kotlin以平台独立的方式为任何支持的平台编写和编译整个模块（目前包括Kotlin/JVM，Kotlin/JS和即将推出的Kotlin/Native）。我们称之为***通用模块***。通用模块的部分内容可能需要基于具体平台实现，这能够为每个平台进行独立开发，通用模块向所有客户端提供公共API，但其它模块（具体平台）可以扩展这部分API，以在其平台上提供额外独占功能。  

值得一提的是，我们并不打算在Kotlin/Native或Kotlin/JS上运行任何的Kotlin/JVM 程序。这相当于又实现了另一个JVM，因此在程序运行时有着诸多的限制与工作量；所以我们将换了一个思路：提供跨平台语言，同时通过与平台代码无缝互通来创建通用库。
## 技术

Kotlin/Native使用LLVM编译器基础架构生成机器代码。在该预览版本中，我们支持以下[目标平台](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/RELEASE_NOTES.md#supported-platforms) ：

* Mac OS X 10.10及更高版本（x86-64）
* x86-64 Ubuntu Linux（14.04,16.04 及更高版本）及其他Linux版本 
* Apple iOS(arm64)，MacOS X主机交叉编译
* Raspberry Pi，Linux主机交叉编译

只要LLVM支持可用，相对地就可以很方便的添加更多平台，未来我们将尽可能会支持更多的平台。  

与往常一样，互通性是我们的首要任务之一，Kotlin/Native可以有效地调用C函数并与之进行数据传递。您可以在构建时从C语言的头文件中生成Kotlin绑定关系，并获得对目标平台任何原生API的快速安全类型访问。查看[详细文档](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/INTEROP.md) 。
### 内存管理

Kotlin/Native旨在为不同的目标平台提供不同的内存管理解决方案。例如，在未来为服务器/桌面端配置GC跟踪是非常有意义的，而ARC对于iOS意义更为巨大。某些平台可能只需要进行手动内存管理，反过来Kotlin/Native运行时内存则会更小。  

此次预览技术具有自动引用计数的功能，其顶部采用循环收集器，但最终的内存管理解决方案此时尚未确定。
### 局限性

综上所述，Kotlin/Native目前的完成度是非常之低的，所以该项预览技术目前存在不少限制，我们也将在以后的阶段逐步优化：

* 运行性能未优化，所以对Kotlin/Native进行基准测试毫无意义。
* 标准库以及反射支持未完整实现，后续会添加更多的API。
* 更多[版本说明](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/RELEASE_NOTES.md)

## 后续计划

我们目前正在研究Kotlin/Native的核心技术，对于所有支持的目标平台（编译器，运行时核心以及库）而言这项技术是相通的。作为未来目标，我们正在考虑以下应用场景：

* iOS应用程序（复用Android代码）
* 嵌入式系统/IoT（不限于Arduino）
* 数据分析与科学计算
* 服务器端和微服务器（低内存占用可执行文件，利用协同程序的功能）
* 游戏开发

## 试一试

我们准备了两个具有编译器、示例和文档的存档链接：  
[适用于Mac和iOS](http://download.jetbrains.com/kotlin/native/kotlin-native-macos-0.1.tar.gz)  
[适用于Linux和Raspberry Pi](http://download.jetbrains.com/kotlin/native/kotlin-native-linux-0.1.tar.gz)  

从[Github](https://github.com/JetBrains/kotlin-native)上检出代码，查看[版本说明](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/RELEASE_NOTES.md) 。  

您可以在[Slack](https://kotlinlang.slack.com)的#kotlin-native频道告诉我们**您的宝贵意见**（[获得邀请](http://slack.kotl.in)）。
