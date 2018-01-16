---
title: Kotlin 1.2 Released: Sharing Code between Platforms
author: Dmitry Jemerov
date: 2017-11-28 19:52:00
tags: 
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlin-1-2-released/
translator: pye52 & 黄志强
translator_url: https://pye52.github.io/ & https://suima0v0.github.io/

---

今天我们正式发布Kotlin1.2。这是一个意义重大的版本，也是将Kotlin推广到现代化应用的各部件开发的关键一步。

在Kotlin1.1版本，我们正式**将JavaScript纳入支持**，你可以将你的Kotlin代码编译成JS并在浏览器运行。而在Kotlin1.2，你的代码可以**在JavaScript和JVM中复用**。现在只需要编写一次业务逻辑，代码就能在后端、浏览器前端、Android移动app中复用。我们也正努力开发能让你复用更多代码的库，例如跨平台序列化的库。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/cake3-1.png)

Kotlin1.2将集成在本周发布的[IntelliJ IDEA 2017.3](https://www.jetbrains.com/idea/)。如果你正在使用Android Studio或旧版本的IntelliJ IDEA，你可以在Tools | Kotlin | Configure Kotlin Plugin Updates中安装新版本。

本次更新包含了许多外部贡献者的成果，我们也感谢你们反馈和报告的问题，尤其是提交了PR的贡献者。

## 跨平台项目

一个跨平台的项目允许你使用相同的代码库去构建多个层面的应用程序 —— 后端、前端和Android app。这样的项目不仅拥有包含跨平台代码的**通用模块**，还拥有包含特定平台(JVM或JS)代码与能调用依赖于平台的库的**特定平台模块**。 要从通用模块中调用特定平台代码，可以使用**预定义** - 所有特定平台模块都需要提供实际实现的声明。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/MPP.png)

此特性的更多的说明，请查看此[文档](http://kotlinlang.org/docs/reference/multiplatform.html)

正如同前面所说的，我们正致力于开发更多的库，供你将业务逻辑迁移到通用模块：

- [kotlin.test](http://kotlinlang.org/api/latest/kotlin.test/index.html)能直接在Kotlin1.2中使用，只需写一次测试便可在JVM和JS中运行
- [kotlinx.html](https://github.com/kotlin/kotlinx.html)支持-**同构渲染**——使同样的代码在前后端渲染HTML
- [kotlinx.serialization](https://github.com/kotlin/kotlinx.serialization)允许你使用JSON或者ProtoBuf在应用程序的不同层之间序列化Kotlin对象

请注意跨平台项目现在只是一个实验性的特性；这意味着虽然可以正常使用，但我们可能会在后续版本中更改设计（到时我们会提供工具迁移代码的）。

## 编译的性能优化

在1.2版本的开发过程中，我们费尽心思去提升编译的速度。相比于1.1版本，我们达到了接近25%的提升，并且我们看到了能进一步优化的潜力，这将在1.2.x的更新版本中发布。

下图展示了两个使用Kotlin构建的大型JetBrains项目在编译时的时间差异：

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/CompilationSpeed.png)

## 其他在语言和标准库方面的改进

我们还对语言和标准库进行了一些小改进：

- 在注解（常量数组）传递多个参数时[一个更简洁的语法](http://kotlinlang.org/docs/reference/whatsnew12.html#array-literals-in-annotations)；
- `lateinit`现在支持全局或局部变量了，同时检查`lateinit`变量是否已经初始化；
- [智能转换](http://kotlinlang.org/docs/reference/whatsnew12.html#smart-cast-improvements)和[类型推断](http://kotlinlang.org/docs/reference/whatsnew12.html#information-from-explicit-casts-is-used-for-type-inference)在某些情况的改善；
- 标准库现在可以兼容Java9中引入的拆分包限制
- 标准库引入了新的`kotlin.math`包
- 标准库新增了用于处理队列和集合的函数，其中有[一组函数](http://kotlinlang.org/docs/reference/whatsnew12.html#windowed-chunked-zipwithnext)可以将集合或队列分解为可重复固定尺寸的组


更多信息及示例代码，请查看[What's New in Kotlin 1.2](http://kotlinlang.org/docs/reference/whatsnew12.html)文档页面。

## 走向世界的Kotlin

随着今年3月份发布了Kotlin1.1，Kotlin在全世界范围内受到了巨大的关注，这在[KotlinConf](https://kotlinconf.com/)上达到最高峰，这次会议于11月2、3号在旧金山举行，总共有12000名与会者。本次会议我们作了全程记录，视频在[这里](https://kotlinconf.com/talks/)。

Kotlin现在已经受到了Android开发的官方支持，并且集成到Android Studio3.0中，同时Google也提供了[示例](https://developer.android.com/samples/index.html?language=kotlin)和[设计规范](https://android.github.io/kotlin-guides/)。据统计，已有[超过17％的Android Studio 3.0项目](https://android-developers.googleblog.com/2017/11/update-on-kotlin-for-android.html)在使用Kotlin了，其中包括来自热门初创公司和500强公司的许多应用程序。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KotlinConfUsers.jpg)

在服务器端，[Spring Framework 5.0](https://spring.io/blog/2017/09/28/spring-framework-5-0-goes-ga)已经支持许多[Kotlin的特性](https://docs.spring.io/spring/docs/current/spring-framework-reference/languages.html#kotlin)了，[Vert.x](http://vertx.io/)也从3.4.0版本开始[支持Kotlin](http://vertx.io/docs/vertx-core/kotlin/)。此外，Gradle现在也开始支持Kotlin DSL，[Gradle Kotlin DSL](https://github.com/gradle/kotlin-dsl)项目正以可观的速度迈向1.0版本。

GitHub上开源项目的Kotlin代码行数已经超过了2500万。 在Stack Overflow上，[Kotlin是增长最快，也是最少被讨厌的语言之一](https://stackoverflow.blog/2017/10/31/disliked-programming-languages/)。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KotlinAdoption.png)

Kotlin社区的发展速度也快得让人惊叹。现已有100多个用户群体遍布世界各地，除开我们无法追踪到的讨论，就我们所知而绘成的[讨论分布图](http://kotlinlang.org/community/talks.html)能让你了解到世界哪些地方正在使用Kotlin。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KUGmap.png)

同时也有越来越多的[书籍](http://kotlinlang.org/docs/books.html)(包括我们的"Kotlin in Action"已被译成[英语](https://manning.com/books/kotlin-in-action)、[俄语](https://dmkpress.com/catalog/computer/programming/java/978-5-97060-497-7/)、[日语](https://www.amazon.co.jp/Kotlin%E3%82%A4%E3%83%B3%E3%83%BB%E3%82%A2%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3-Dmitry-Jemerov/dp/4839961743/ref=sr_1_2?ie=UTF8&qid=1511539431&sr=8-2&keywords=kotlin)、[中文](https://www.amazon.com/Kotlin%E5%AE%9E%E6%88%98-Svetlana-Isakova-Dmitry-Jemerov/dp/B07568C58F/ref=sr_1_3?s=books&ie=UTF8&qid=1511539582&sr=1-3)、[葡萄牙语](https://novatec.com.br/livros/kotlin-em-acao/))、在线课堂、教程和[其他资料](http://kotlinlang.org/community/)供初学者学习。

## 与开发团队交流：网络研讨会和Reddit AMA

为了分享更多新版本信息，我们计划于12月7日晚上6点举办[Kotlin1.2跨平台项目的网络研讨会](http://kotlinlang.org/community/)。名额有限，请及时注册！

Kotlin团队也会在12月5日在[Kotlin Reddit](https://www.reddit.com/r/Kotlin/)上进行AMA(问答会)，讨论将于中午开始，与你度过接下来的24小时。

## 如何升级

与往常一样，你可以在[try.kotlinlang.org](http://try.kotlinlang.org/)中**尝试新版本**。

- **在Maven，Gradle和npm**：请更新编译版本及标准库版本号到`1.2.0`，详细请查看[文档](http://kotlinlang.org/docs/reference/using-gradle.html)。
- **在Intellij IDEA**：2017.3已集成了1.2版本，旧版本可以通过安装或更新Kotlin插件来获取最新版本。
- **在Android Studio**：请通过*Plugin Manager*安装或更新你的插件。
- **在Eclipse**：通过[Marketplace](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse)安装插件。
- [Github发布页](https://github.com/JetBrains/kotlin/releases/tag/v1.2.0)可下载最新命令行编译器。

**关于兼容性**：Kotlin1.2版本及其标准库是[向前兼容](http://kotlinlang.org/docs/reference/compatibility.html)的，在1.0或1.1版本下成功编译并运行的代码也能运行在1.2上。考虑到一些大型团队需要逐渐推进更新，我们提供了一些编译器开关以便禁用部分新特性。如果遇到问题，请参考[这里](http://kotlinlang.org/docs/reference/compatibility.html#binary-compatibility-warnings)。

*请尽情享受Kotlin！*

