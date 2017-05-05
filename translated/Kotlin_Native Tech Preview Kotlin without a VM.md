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
translator:  
translator_url:  

---

我们很高兴地宣布**Kotlin/Native**的第一个技术预览版本可以直接将Kotlin编译为机器码。Kotlin/Native编译器生成独立的可执行文件，可以不借助任何虚拟机运行。  

然而目前该版本功能尚未完善，但您已经可以使用该技术，在[这里](https://github.com/JetBrains/kotlin-native/)查看源代码。编译器基于Apache 2 OSS许可证下使用。

{% raw %}
<p><img alt="KotlinNative" class="alignnone size-full wp-image-4889" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/04/KotlinNative.png" width="800"/><br/>
<span id="more-4862"></span></p>
{% endraw %}

## 任务

Kotlin/Native是让Kotlin贯通所有应用场景又一大进步。最终目的是能够使用Kotlin来编写从服务器端到网页甚至移动客户端的每个组件。对此，共享技能是一大激励，另外则是共享实际代码。  

对于平台内部代码重用，我们有着如下愿景：使用Kotlin以平台无关的方式为任何支持的平台编写和编译模块（目前包括Kotlin/JVM，Kotlin/JS 和即将推出的Kotlin/Native），我们称之为***通用模块***。公共模块的一部分可能需要一个平台特定的实现，可以为每个平台单独开发。通用模块为所有客户端提供通用 API，但其他（特定于平台的）模块可以扩展此 API，以在其平台上提供一些独占功能。
请注意，我们不打算在 Kotlin / Native 或 Kotlin / JS 上运行任意的 Kotlin / JVM 程序。这将相当于实现另一个 JVM，这对于运行时来说是很多工作和很多限制。我们将以另一种方式：为所有平台提供通用语言，同时通过与平台代码的无缝互操作来创建通用库。
## 技术

Kotlin / Native 使用 LLVM 编译器基础架构生成机器代码。在这个预览中，我们支持以下内容 [目标平台](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/RELEASE_NOTES.md#supported-platforms) ：

* Mac OS X 10.10 及更高版本（x86-64）
* x86-64 Ubuntu Linux（14.04,16.04 及更高版本），其他 Linux 版本也可以正常工作
* 苹果 iOS（arm64），在 MacOS X 主机上交叉编译
* Raspberry Pi，在 Linux 主机上交叉编译

只要 LLVM 支持可用，可以相对容易地添加更多的平台。我们将来可能会支持更多的平台。
像往常一样，互操作性是我们的首要任务之一，Kotlin / Native 可以有效地调用 C 函数并将数据传递给/从他们获取数据。您可以在构建时从 C 头文件生成 Kotlin 绑定，并获得对目标平台原生的任何 API 的快速类型安全访问。查看详细说明 [这里](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/INTEROP.md) 。
### 内存管理

Kotlin / Native 旨在为不同的目标平台提供不同的内存管理解决方案。例如，在将来，为服务器/桌面平台配置跟踪 GC 可能是有意义的，而 ARC 在 iOS 上更有意义。某些平台可能只需要手动内存管理，并获得一个更小的 Kotlin / Native 运行时。
此技术预览功能具有自动参考计数，顶部采用循环收集器，但最终的内存管理解决方案在此时尚未知。
### 当前局限性

如上所述，Kotlin / Native 是远未完成的，所以这个技术预览有一些限制，将在以后的阶段消除：

* 没有执行性能优化，所以基准测试 Kotlin / Native 在这一点上是没有意义的。
* 标准库和反思支持还远未完成，稍后会添加更多的 API。
* 阅读更多在发行说明。

## 未来的计划

我们目前正在研究 Kotlin / Native 的核心技术，它与所有目标平台（编译器，核心运行时和库）是一样的。作为未来可能的工作，我们正在考虑以下可能的用例：

* iOS 应用程序（使用 Android 重用代码）
* 嵌入式系统/ IoT（例如，Arduino 及其以外）
* 数据分析与科学计算
* 服务器端和微服务器（低可用性可执行文件，利用协同程序的功能）
* 游戏开发

## 如何尝试

我们已经准备了两个具有编译器，样本和文档的档案： [适用于 Mac 和 iOS](http://download.jetbrains.com/kotlin/native/kotlin-native-macos-0.1.tar.gz) 和 [对于 Linux 和 Raspberry Pi](http://download.jetbrains.com/kotlin/native/kotlin-native-linux-0.1.tar.gz) 。
看看 [Github 项目](https://github.com/JetBrains/kotlin-native) 和 [发行说明](https://github.com/JetBrains/kotlin-native/blob/v0.1.0/RELEASE_NOTES.md) 为了指示。
**我们非常欢迎您的反馈意见**在＃kotlin 本机频道 [公共松弛](https://kotlinlang.slack.com) （获取您的邀请 [这里](http://slack.kotl.in) 。
