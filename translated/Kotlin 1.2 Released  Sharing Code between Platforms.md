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

自从今年3月份发布Kotlin1.1以来，Kotlin在全球范围内获得了巨大的成功。这是第一次全球会议[KotlinConf](https://kotlinconf.com)中的高潮，在11月2日至3日约有1200名与会者在旧金山聚会。 我们全程记录，并且视频在[这里](https://kotlinconf.com/talks/)。

现在Kotlin是Android开发中官方支持的语言，并且集成在Android Studio 3.0中了，Google官方也提供了[示例](https://developer.android.com/samples/index.html?language=kotlin)和[指南](https://android.github.io/kotlin-guides/)。也因此在[Android Studio 3.0报告](https://android-developers.googleblog.com/2017/11/update-on-kotlin-for-android.html)中超过17％的项目在使用Kotlin了，其中包括许多来自最热门初创公司和500强公司的应用程序。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KotlinConfUsers.jpg)

在服务器端，[Spring Framework 5.0](https://spring.io/blog/2017/09/28/spring-framework-5-0-goes-ga)正式版已经支持了很多Kotlin的[特性](https://docs.spring.io/spring/docs/current/spring-framework-reference/languages.html#kotlin)了，而[Vert.x](http://vertx.io/)自3.4.0版本开始也已经[支持Kotlin](http://vertx.io/docs/vertx-core/kotlin/)了。 此外，Gradle现在也支持Kotlin DSL了，[Gradle Kotlin DSL](https://github.com/gradle/kotlin-dsl)项目以相当可观的速度迈向1.0版本。

GitHub上开源项目的Kotlin代码行数已经超过了2500万。 在Stack Overflow上，Kotlin既是增长最快，也是最不受欢迎的语言之一。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KotlinAdoption.png)

围绕Kotlin的社区也发展得非常迅速。 世界各地有超过100个user groups，还有很多相关的讨论我们无法记录，但下面这个[分布地图](http://kotlinlang.org/community/talks.html)可以让你看到Kotlin现在有多流行。

![](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KUGmap.png)

对于想开始学习Kotlin的人来说，将会有越来越多的[书籍](http://kotlinlang.org/docs/books.html)（包括我们自己的“Kotlin in Action”，现在有[英文](https://www.manning.com/books/kotlin-in-action)，[俄文](https://dmkpress.com/catalog/computer/programming/java/978-5-97060-497-7/)，[日文](https://www.amazon.co.jp/Kotlin%E3%82%A4%E3%83%B3%E3%83%BB%E3%82%A2%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3-Dmitry-Jemerov/dp/4839961743/ref=sr_1_2?ie=UTF8&qid=1511539431&sr=8-2&keywords=kotlin)，[中文](https://www.amazon.com/Kotlin%E5%AE%9E%E6%88%98-Svetlana-Isakova-Dmitry-Jemerov/dp/B07568C58F/ref=sr_1_3?s=books&ie=UTF8&qid=1511539582&sr=1-3)和[葡萄牙](https://novatec.com.br/livros/kotlin-em-acao/)文版本），在线课程，教程和[其他资源](http://kotlinlang.org/community/)。

## 团队会面：网络研讨会和Reddit AMA

为了给大家分享新版本的更多信息，我们计划于12月7日18:00 CET举办Kotlin 1.2[跨平台项目网络研讨会](https://info.jetbrains.com/Kotlin-Webinar-December2017.html)。名额有限请及时注册！

Kotlin团队也将于12月5日在[Kotlin Reddit](https://www.reddit.com/r/Kotlin/)上进行AMA（Ask Me Anything）。 我们将在中午四点开始，我们会在接下来的24小时与您同在。