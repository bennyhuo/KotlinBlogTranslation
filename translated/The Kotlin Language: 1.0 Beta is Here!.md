---
title: [译]The Kotlin Language: 1.0 Beta is Here!
date: 2015-11-02 18:44:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/11/the-kotlin-language-1-0-beta-is-here/
---

我们非常高兴地介绍Kotlin 1.0 Beta for JVM和Android！
总结：Kotlin是JetBrains现在已经进行了一段时间的现代编程语言。
这篇文章概述了我们在哪里和接下来会发生什么。此版本中列出了更改。
## Kotlin背后的故事

Kotlin是在2010年设想的。十年的Java开发使我们感到，JetBrains的生产力可以通过与Java一起使用现代的JVM语言来显着提高。在评估了其他可用选项后，我们决定在那里需要一种新的语言，我们有专门知识和资源来创建这样一种语言。我们的主要业务是为开发人员制作工具，其指导原则是，为用户制作出令人敬畏的产品的最佳方式是制作一个我们需要的真棒工具。这与IntelliJ IDEA，ReSharper和许多其他IDE以及TeamCity和其他服务器产品配合使用，因此我们开始将另一个开发工具 - 一种编程语言应用于相同的原理。
我们将科特林设计为工业的现代语言，并对此有相当的具体要求。首先，我们的项目活得很长，成长真的很大（数百万行代码），所以我们需要静态打字，以便能够准确地说明巨大的代码库并保持这些年。然后，我们的所有代码都是用Java编写的，所以我们需要一个顺利的迁移路径，可以将新的语言逐渐引入现有的Java代码库，尽可能少地影响其余的代码。另外，作为JetBrains，我们不想在工具质量方面妥协：我们正在寻找一种新的语言来使我们更有成效，我们相信这大部分取决于工具。最后，我们需要一种易于学习和理解的语言：在我们的团队中，我们不会将“图书馆用户”与“图书馆用户”分开，我们希望所有开发人员使用他们所使用的语言同样有效。
这样的一个项目涉及做出很多决定，从一开始就知道，第一次尝试是不可能的。这就是为什么我们允许相当长的时间进行核心设计选择的实验和验证：由于JetBrains内部和外部的早期采用者正在使用它们，我们不断收集反馈并进行更改（非常感谢我们的社区对您的所有评论人们给了我们！）。这给了我们对广泛使用案例的重要见解，现在我们认为，我们可以在1.0之后保持向后兼容性。
JetBrains已经使用Kotlin生产IntelliJ IDEA，YouTrack等产品了很长时间了。目前，我们有超过250'000的科特林LOC（加上Kotlin项目本身）。虽然我们的一些项目完全是在Kotlin（account.jetbrains.com）中编写的，但是其他项目已经按照我们最初的计划将其引入了现有的Java代码库。我们达到了互操作性水平，自由地将Kotlin与Java一起放在Java客户端是透明的：Java可以从Kotlin调用，反之亦然，源可以混合在一个项目中，因此.class文件与Java工具完全兼容。
科特林正在为我们服务，我们致力于一个20多人的团队的发展。
尽管尚未达到1.0，但其他公司和个人开发人员已经在使用Kotlin从Web服务后端到Android应用程序。我们有来自Expedia，Prezi.com等许多报告（可以随时通过提交PR将您的公司添加到此列表）。
到目前为止，GitHub开放存储库中的Kotlin代码行数量呈指数级增长（JetBrains的项目被排除在外）：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/Kotlin-GitHub-LOC.png"><img alt="Kotlin GitHub LOC" class="alignleft size-full wp-image-3069" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/Kotlin-GitHub-LOC.png?resize=640%2C279&amp;ssl=1"/></a></p>
{% endraw %}

## 什么Kotlin感觉像

从我们自己的语言经验和从我们听到的许多外部用户这里是什么使用Kotlin感觉像：

* 它的代码较少，
* 更好的可读性，
* 更安全，
* 更具表现力，
* 平滑的工具和互操作经验。

## 什么是测试版？

在生产中积极使用时，Kotlin现在处于Beta状态。这对你意味着什么

* 我们正在把准备工作正式发布;
* 二进制格式定稿;
* 所有主要的语言变化都已经完成。

## 兼容性

科特林将不会停留在Beta版，1.0即将来临。
我们致力于平滑用户体验，这包括Kotlin版本的兼容性。 1.0之后，语言和库的所有更新将向后兼容：

* 较新的编译器将使用较旧的二进制文件（但较旧的编译器可能不了解较新的二进制文件，如javac 1.6无法读取由javac 1.8编译的类）;
* 较旧的二进制文件将在运行时继续使用较新的二进制文件（尽管更新的代码可能需要较新的依赖关系）。

上述所有内容仅适用于JVM / Android支持。 JavaScript支持现在仍然是实验性的，稍后会有自己的发行版。
## 关于科特林的几个事实


* 它是开放源代码（在Apache 2.0许可证下）：编译器，运行库和所有工具，包括IDE;
* 它促进编程的功能风格（同时是多范式语言）;
* 它是静态编译的，与Java相比，不会引入运行时开销;
* 它通过Quasar支持高效和安全的并发;
* 它与IntelliJ IDEA 15（Ultimate和OSS社区版）捆绑在一起，可以开箱即用;
* 它具有Android Studio，Eclipse，Maven，Gradle和Ant的插件（更不用说IntelliJ IDEA和TeamCity）;
* 它有一个REPL;
* 它有一个积极和有益的社区，正在生产令人敬畏的图书馆;
* 写了两本书：Kotlin in Action和Kotlin for Android Developers。

## 框架，互操作和迁移

几乎任何Java或Android框架或库可以与Kotlin顺利工作。其中包括Spring MVC，Vaadin，Vert.x和Jackson。许多Android框架需要通过支持Dagger 2，DataBinding，DBFlow，ButterKnife，AndroidAnnotations等的kapt的Kotlin可用的注释处理。
Kotlin有自己的框架和图书馆由JetBrains和社区开发。一些例子：Anko，RxKotlin，funktionale，kohesive，kovenant，Kobalt构建工具等等。
内置IDE的转换器有助于将源代码从Java迁移到Kotlin。
## 尝试一下


* 学习：Koans / Playground /，教程，语言文档
* 安装

IntelliJ IDEA 15（终极或社区）：只需在Java项目中创建Kotlin项目或Kotlin文件
Android Studio：通过插件管理器安装插件
Eclipse：通过Marketplace安装插件
命令行：在这里下载编译器
* IntelliJ IDEA 15（终极或社区）：只需在Java项目中创建Kotlin项目或Kotlin文件
* Android Studio：通过插件管理器安装插件
* Eclipse：通过Marketplace安装插件
* 命令行：在这里下载编译器
* 社区：论坛，Slack（获取邀请），StackOverflow，GitHub（欢迎公关）
* 新闻：博客，Twitter
* 问题追踪器

有一个漂亮的Kotlin！
