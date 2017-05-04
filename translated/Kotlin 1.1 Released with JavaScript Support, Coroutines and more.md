---
title: "[译]Kotlin 1.1 Released with JavaScript Support, Coroutines and more"
date: 2017-03-01 17:12:00
author: Roman Belov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/03/kotlin-1-1/  
translator: SnakEys  
translator_url: https://github.com/SnakeEys
---

<div style =“margin：0px; padding：10px; border-color：＃f0f0f0; display：inline-block; border-width：1px; border-style：solid; font-size：10”>我们社区的成员将这篇博文翻译成几种语言：<br/>
<a href="https://medium.com/@walmyrcarvalho/kotlin-1-1-suporte-a-javascript-co-rotinas-e-mais-d84b65ac2f92" title="巴西葡萄牙语"> <img data-recalc -dims =“1”src =“https://i1.wp.com/emojipedia-us.s3.amazonaws.com/cache/82/1a/821aaf51852412ffcf042c2f2a61309e.png?w=25&amp;ssl=1”style =“显示：inline; margin-bottom：-10px“/> </a> <a href="http://www.weibo.com/ttarticle/p/show?id=2309404081257721035952" title="Chinese"> <img data-recalc-dims =“1”src =“https://i1.wp.com/emojipedia-us.s3.amazonaws.com/cache/51/a3/51a3fcf2d2c44c34bd3d4a90fff477f8.png?w=25&amp;ssl=1” style =“display：inline; margin-bottom：-10px”/> </a> <a href =“https://medium.com/@gz_k/kotlin-1-1-javascript-coroutines-et-plus- ce2eb3d7004“title =”French“> <img data-recalc-dims =”1“src =”https://i1.wp.com/emojipedia-us.s3.amazonaws.com/cache/31/7a/317a88ee3fdec119bfbd5f69a6bf35b1。 png？w = 25＆amp; ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> <a href =”https://blog.jetbrains.com/jp/2017/03 / 01/739“title =”Japanese“> <img data-recalc-di ms =“1”src =“https://i2.wp.com/emojipedia-us.s3.amazonaws.com/cache/a4/0d/a40df75ad96b0d143df710080c710f0f.png?w=25&amp;ssl=1”style =“显示：inline; margin-bottom：-10px“/> </a> <a href =”http://kotlin.kr/2017/03/01/kotlin-1-dot-1.html“title =”Korean“ > <img data-recalc-dims =“1”src =“https://i0.wp.com/emojipedia-us.s3.amazonaws.com/cache/f8/e1/f8e14a4d5c26dedc5b0639ca763bc03a.png?w=25&amp;ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> <a href =”https://habrahabr.ru/company/JetBrains/blog/323012/“title =”Russian“ > <img data-recalc-dims =“1”src =“https://i2.wp.com/emojipedia-us.s3.amazonaws.com/cache/80/da/80da132bc3307d3d2ac0729493eb4c26.png?w=25&amp;ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> <a href =”http://kotlin.es/2017/03/1.1.0/“title =”Spanish“ > <img data-recalc-dims =“1”src =“https://i2.wp.com/emojipedia-us.s3.amazonaws.com/cache/77/3e/773e66b858a69ddbade6951fdb012949.png?w=25&amp;ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> </div>

Kotlin 1.1 今天正式发布了，这让 Kotlin 有能力适用于更多的应用场景，希望大家能够喜欢。


{% raw %}
<p><img alt="Kotlin 1.1" class="alignnone size-full wp-image-4675" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/Kotlin11blogbanner1.png" width="800"/></p>
{% endraw %}

我们希望 Kotlin 能够在应用的任何组件中成为独立的、富有表现力且性能强大的强类型语言，Kotlin1.1 为了实现这一目标迈出了巨大的两步。

{% raw %}
<p><span id="more-4611"></span></p>
{% endraw %}

首先，***JavaScript 支持***的“试验性”标签已被移除，并且支持所有 Kotlin 语言特性、标准库的大部分内容以及 JavaScript 互操作性。这意味着开发者可以完全使用 Kotlin 来编写整个 WEB 应用，同时继续使用 JavaScript 的开发框架（比如 React）。  

其次，我们引入了***协程(coroutines)***的概念。作为线程的轻量级替代方案，协程在应用程序后端可以具有更大可扩展性，从而支持单个 JVM 实例上的大量工作负载。除此之外，协程对于实现异步行为具有强大的表现力，这对于在任何平台上构建响应式用户交互界面而言极其重要。  

下面我们将进一步介绍这两大功能。其他部分如[type aliases](http://kotlinlang.org/docs/reference/whatsnew11.html#type-aliases)，[callable references](http://kotlinlang.org/docs/reference/whatsnew11.html#bound-callable-references)，[destructuring in lambdas](http://kotlinlang.org/docs/reference/whatsnew11.html#destructuring-in-lambdas)等详情可在[最新消息](http://kotlinlang.org/docs/reference/whatsnew11.html)查看，试试完整的可运行示例代码！
## 协程(Coroutines)

在 Kotlin 中协程使非阻塞式异步代码与同步代码一样易于理解。  

异步编程正当风靡，唯一让我们思虑的是，非阻塞式代码大量增加了系统的复杂性。 而 Kotlin 现在提供了简化这种复杂性的方法，通过单原子让协程在语言中成为一等公民：***挂起函数***。这种类型的函数（或 lambda）表示在计算运行中可以被挂起（不阻塞任何线程），而后也能继续恢复运行。  

从技术上说，协程是多任务协作的轻量级解决方案（类似于[fibers](https://en.wikipedia.org/wiki/Fiber_(computer_science))）。换言之，他们只是***更好的线程***：可以任意的启动和保留，且挂起的消耗极其之低（挂起之于协程，如阻塞之于线程），非常易于组合与订制。  

我们对于协程的设计以实现最大的灵活性为目标：在语言中固化的部分少，而且可以作为库来实现很多功能。[kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)项目在 Rx，CompletableFuture，NIO，JavaFx 和 Swing 上均有设计功能库，甚至可以为 Android 和 JavaScript 编写类似的库。即使在其​​他语言中许多内置构建现在也可以用 Kotlin 库来编写。包括 Python 的 generators/yield，来自 Go 的 channels/select 以及 C＃的 async/await:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// runs the code in the background thread pool
fun asyncOverlay() = async(CommonPool) {
    // start two async operations
    val original = asyncLoadImage("original")
    val overlay = asyncLoadImage("overlay")
    // and then apply overlay to both results
    applyOverlay(original.await(), overlay.await())
}
 
// launches new coroutine in UI context
launch(UI) {
    // wait for async overlay to complete
    val image = asyncOverlay().await()
    // and then show it in UI
    showImage(image)
}
```

{% raw %}
<p></p>
{% endraw %}

查看[完整内容](http://kotlinlang.org/docs/reference/coroutines.html)。  

**重要提示**：凭借上述的这些优势，Kotlin 协程近乎全新的设计，在我们能确定这是 100％正确和完整之前，仍然需要大量的实践和测试。因此我们才选择在“实验性”[标志](http://kotlinlang.org/docs/diagnostics/experimental-coroutines.html)下发布。我们不希望语言规则发生变化，但 API 可能需要在 Kotlin 1.2 中进行调整。
## JavaScript 支持

如上所述，Kotlin 1.1 中的所有语言特性（包括协程）都适用于 JVM / Android 和 JavaScript（JavaScript 的反射目前不可用，但我们正在这方面努力）。这意味着 Web 应用程序可以完全使用 Kotlin 编写，而且我们已经在 JetBrains 内部有一些尝试，相信很快就会发布教程和其他资料。  

Kotlin for JavaScript 具有与“源生”JavaScript 代码进行互相操作的动态类型，通过类型 API 可以使用[ts2kt converter](http://github.com/kotlin/ts2kt)以及[DefinitelyTyped](http://github.com/DefinitelyTyped/DefinitelyTyped)等知名库。  

我们支持 Node.js 和浏览器。 Kotlin 标准库可通过`npm`使用。  
[文档链接](http://kotlinlang.org/docs/reference/js-overview.html) 。
## 工具

Kotlin 1.1 并不是 Kotlin 工具发布的主版本：我们更喜欢具有这些功能的工具就绪后，不会对语言本身产生影响，所以我们在 Kotlin 1.0.x 版本中的有许多这样的改进：

* 主流 IDE 的 Kotlin 插件：IntelliJ IDEA，Android Studio，Eclipse 和 NetBeans
* IntelliJ IDEA 和 Gradle 中的增量编译
* Spring，JPA 和 Mockito 的编译器插件（all-open 与 no-arg）
* 注解处理器 kapt
* 对 Android 项目的支持 Lint 检查
* 大量的 IDE 代码预测，检查，快速修复，重构和自动完成提升

我们将继续在 1.1.x 版本中进行更新，努力为开发者们提供更好的工具。
# Kotlin 元年：迁移与社区

总而言之，Kotlin 正在逐渐壮大。去年，我们看到有超过 160,000 人使用，Github 上的 Kotlin 开源项目从 2.4M 增加到 10M（约 4 倍）。我们的 Slack 社区已经从 1,400 人增长到超过 5,700 人（超过 4 倍）。[世界各地](http://kotlinlang.org/community/talks.html)均有社区组织了众多的线下交流以及用户群组，我们也看到越来越多的 Kotlin 书籍和在线课程发布。

{% raw %}
<p><center><br/>
<img alt="Kotlin GitHub Stats" class="alignnone size-full wp-image-4679" height="375" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/GitHub-Stats-2.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/GitHub-Stats-1.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/GitHub-Stats-2.png" width="750"><br/>
</img></center></p>
{% endraw %}

Kotlin 在服务器端和 Android 端（开发人员数量均等）表现异常强大。 [Spring 框架 5.0](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0)和[vert.x 3.4](http://vertx.io/blog/vert-x-3-4-0-beta1-release/)均引入了对 Kotlin 的支持。 [Gradle](https://blog.gradle.org/kotlin-meets-gradle)和[TeamCity](https://blog.jetbrains.com/teamcity/2016/11/kotlin-configuration-scripts-an-introduction/)正在使用 Kotlin 构建脚本。更多使用 Kotlin 的项目可以在[kotlin.link](http://kotlin.link)查看。  

许多知名公司也正在使用 Kotlin：[Pinterest](https://www.youtube.com/watch?v=mDpnc45WwlI)，[Coursera](https://building.coursera.org/blog/2016/03/16/becoming-bilingual-coursera/)，[Netflix](https://twitter.com/robspieldenner/status/708355228832178176)，[Uber](https://www.reddit.com/r/androiddev/comments/5sihp0/2017_whos_using_kotlin/ddfmkf7/)，[Square](https://github.com/square/sqldelight)，[Trello](https://twitter.com/danlew42/status/809065097339564032)，[Basecamp](https://m.signalvnoise.com/some-of-my-favorite-kotlin-features-that-we-use-a-lot-in-basecamp-5ac9d6cea95)；除此之外， 由知名银行（如高盛，富国银行，摩根大通，德意志银行，瑞银，汇丰银行，法国巴黎银行，SociétéGénérale）联盟开发的分销账户分类账户[Corda](https://github.com/corda/corda)，其代码库中有[超过 90％的部分](https://www.corda.net/2017/01/10/kotlin/)使用 Kotlin。我们感谢世界各地的所有用户，贡献者和倡导者。您的支持对我们非常重要！
### 组织您自己的 Kotlin 1.1 活动

Kotlin 1.1 的发布是与当地社区好友线下聚会的好话题。我们已经准备了一些资料来帮助开发者们举办此类活动。3 月 23 日，我们将以 Kotlin 团队成员的形式进行现场直播，发起人均可获得一个背包，里面有一份关于未来特性的调查问卷和一些小礼物，点击[注册](https://docs.google.com/forms/d/e/1FAIpQLSf6iXcrIpaNIqeeUJI2L6pntS5yy_iI01PbrO9gTMmX0kg5Lw/viewform)即可参与。
# 后续

为了使 Kotlin 成为真正的全栈语言，我们将为多个平台编译相同的代码提供工具和语言支持。这将有助于在客户端和服务器之间进行模块共享。我们将继续致力于改进 JavaScript 工具和库的支持。除此之外，JavaScript 平台的增量编译正在进行中。请继续关注 1.1.x 更新。  

Java 9 即将推出，我们将在发布之前为其新功能提供支持。  

我们期望在未来几个月内能够收到许多关于协程反馈意见，改进这一领域（在性能和功能方面）对于我们优先级最高。  
除此之外，下一版本的主要工作将集中在维护，性能改进，基础架构和错误修复方面。
P.S 跨平台运行是 Kotlin 的战略方向，伴随着 1.1 的发布，我们可以在服务器，台式机，Android 设备和浏览器上运行，但是未来我们将把 Kotlin 编译为本地代码，并使之能够在更多平台（例如 iOS 和嵌入式设备等）上运行。 目前在 JetBrains 内部，有一个非常棒的团队正在开展这个项目，我们期待很快就会出现有趣的东西，不过尚未计划为此专门发布任何版本。
# 安装说明

与以往一样，开发者可以使用**Kotlin 线上编辑器** [try.kotlinlang.org](http://try.kotlinlang.org/)。  

**Maven/Gradle**：使用`1.1.0`作为编译器和标准库的版本号([查看文档](http://kotlinlang.org/docs/reference/using-gradle.html))。  

**IntelliJ IDEA**：2017.1 已包含 Kotlin 1.1；旧版本则需要安装 Kotlin 插件或更新到 1.1 版本。  

**Android Studio**：通过***Plugin Manager***安装或更新插件。  

**Eclipse**：使用[Marketplace](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse) 安装插件。  

**命令行编译器**可以从[Github 发布页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1)下载。  

**兼容性**：Kotlin 1.1 语言和标准库[向后兼容(modulo bugs)](http://kotlinlang.org/docs/reference/compatibility.html) ：如果使用 1.0 版本编译运行，1.1 版本仍然可以运行。为了帮助大型团队有规律的更新，我们在编译器中新增禁用新功能的开关。查看[踩坑文档](http://kotlinlang.org/docs/reference/compatibility.html#binary-compatibility-warnings)。  

***请尽情享受 Kotlin！***  

P.S: 在[Reddit](https://www.reddit.com/r/programming/comments/5wvpv8/kotlin_11_released_with_javascript_support/)和[Hacker News](https://news.ycombinator.com/item?id=13763483)上加入讨论吧！
