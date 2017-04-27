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
---

<div style =“margin：0px; padding：10px; border-color：＃f0f0f0; display：inline-block; border-width：1px; border-style：solid; font-size：10”>我们社区的成员将这篇博文翻译成几种语言：<br/>
<a href="https://medium.com/@walmyrcarvalho/kotlin-1-1-suporte-a-javascript-co-rotinas-e-mais-d84b65ac2f92" title="巴西葡萄牙语"> <img data-recalc -dims =“1”src =“https://i1.wp.com/emojipedia-us.s3.amazonaws.com/cache/82/1a/821aaf51852412ffcf042c2f2a61309e.png?w=25&amp;ssl=1”style =“显示：inline; margin-bottom：-10px“/> </a> <a href="http://www.weibo.com/ttarticle/p/show?id=2309404081257721035952" title="Chinese"> <img data-recalc-dims =“1”src =“https://i1.wp.com/emojipedia-us.s3.amazonaws.com/cache/51/a3/51a3fcf2d2c44c34bd3d4a90fff477f8.png?w=25&amp;ssl=1” style =“display：inline; margin-bottom：-10px”/> </a> <a href =“https://medium.com/@gz_k/kotlin-1-1-javascript-coroutines-et-plus- ce2eb3d7004“title =”French“> <img data-recalc-dims =”1“src =”https://i1.wp.com/emojipedia-us.s3.amazonaws.com/cache/31/7a/317a88ee3fdec119bfbd5f69a6bf35b1。 png？w = 25＆amp; ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> <a href =”https://blog.jetbrains.com/jp/2017/03 / 01/739“title =”Japanese“> <img data-recalc-di ms =“1”src =“https://i2.wp.com/emojipedia-us.s3.amazonaws.com/cache/a4/0d/a40df75ad96b0d143df710080c710f0f.png?w=25&amp;ssl=1”style =“显示：inline; margin-bottom：-10px“/> </a> <a href =”http://kotlin.kr/2017/03/01/kotlin-1-dot-1.html“title =”Korean“ > <img data-recalc-dims =“1”src =“https://i0.wp.com/emojipedia-us.s3.amazonaws.com/cache/f8/e1/f8e14a4d5c26dedc5b0639ca763bc03a.png?w=25&amp;ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> <a href =”https://habrahabr.ru/company/JetBrains/blog/323012/“title =”Russian“ > <img data-recalc-dims =“1”src =“https://i2.wp.com/emojipedia-us.s3.amazonaws.com/cache/80/da/80da132bc3307d3d2ac0729493eb4c26.png?w=25&amp;ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> <a href =”http://kotlin.es/2017/03/1.1.0/“title =”Spanish“ > <img data-recalc-dims =“1”src =“https://i2.wp.com/emojipedia-us.s3.amazonaws.com/cache/77/3e/773e66b858a69ddbade6951fdb012949.png?w=25&amp;ssl = 1“style =”display：inline; margin-bottom：-10px“/> </a> </ div>

今天我们发布了Kotlin 1.1。这是向前迈进的一大进步，可以在许多新的场景中使用Kotlin，我们希望您能享受它。

{% raw %}
<p><img alt="Kotlin 1.1" class="alignnone size-full wp-image-4675" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/Kotlin11blogbanner1.png" width="800"/></p>
{% endraw %}

我们对Kotlin的愿景是在现代应用的所有组件中使用单一的表现力强，性能强的类型语言。 Kotlin 1.1为实现这一目标迈出了两大步骤。

{% raw %}
<p><span id="more-4611"></span></p>
{% endraw %}

首先，JavaScript目标</ em>不再是实验性的，并且支持所有Kotlin语言功能，标准库的大部分以及JavaScript互操作性。这样，您可以将应用程序的浏览器前端迁移到Kotlin，同时继续使用现代JavaScript开发框架（如React）。
其次，我们正在为<em>协调程序</ em>引入支持。作为线程的轻量级替代方案，协同程序可实现更多可扩展的应用程序后端，从而支持单个JVM实例上的大量工作负载。除此之外，协同程序是实现异步行为的非常有表现力的工具，这对于在所有平台上构建响应式用户界面很重要。
下面我们进一步介绍这两个变化。其他消息：我们已经添加 [键入别名](http://kotlinlang.org/docs/reference/whatsnew11.html#type-aliases) ， [绑定的可引用引用](http://kotlinlang.org/docs/reference/whatsnew11.html#bound-callable-references) ， [在兰布斯进行破坏](http://kotlinlang.org/docs/reference/whatsnew11.html#destructuring-in-lambdas)  和更多。看我们的细节 [什么是新的](http://kotlinlang.org/docs/reference/whatsnew11.html)  页面（查看可运行的示例！）。
## 协调程序

Kotlin中的协调程序使非阻塞异步代码与简单的同步代码一样简单。
异步编程正在接管世界，唯一让我们回想的是，非阻塞代码对我们的系统增加了相当大的复杂性。 Kotlin现在提供了通过单一原语：<em>暂停功能</ em>使协调一致的语言公民处于这种复杂性的手段。这样的函数（或lambda）表示可以暂停（不阻塞任何线程）并稍后恢复的计算。
技术上，协同程序是协同多任务的轻量级手段（非常相似 [纤维](https://en.wikipedia.org/wiki/Fiber_(computer_science)) ）。换句话说，他们只是更好的线程</ em>：几乎可以自由地开始和保持，非常便宜的挂起（暂停是协同程序什么阻塞是线程），非常容易组合和自定义。
我们设计协同程序以实现最大的灵活性：语言中固定的很少，而且可以作为一个库来完成。的 [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)  在Rx，CompletableFuture，NIO，JavaFx和Swing之上的项目功能库。可以为Android和JavaScript编写类似的库。即使许多其​​他语言的内置结构现在也可以表示为Kotlin库。这包括来自Python的生成器/收益，来自Go的通道/ select和来自C＃的异步/等待

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

阅读更多在我们的 [文件](http://kotlinlang.org/docs/reference/coroutines.html) 。
<strong>重要的注释</ strong>。凭借所带来的所有好处，Kotlin协同程序是一个相当新的设计，需要大量的战斗测试，才能确定它的100％正确和完整。这就是为什么我们将在“实验” [选择加入标志](http://kotlinlang.org/docs/diagnostics/experimental-coroutines.html) 。我们不希望语言规则发生变化，但API可能需要在Kotlin 1.2中进行一些调整。
## JavaScript支持

如上所述，Kotlin 1.1中的所有语言功能（包括协同程序）都适用于JVM / Android和JavaScript。 （JavaScript的反思不可用，但我们正在研究它）。这意味着一个Web应用程序可以完全写在Kotlin中，而且我们已经在JetBrains中有一些经验。我们将尽快发布教程和其他材料。
Kotlin for JavaScript具有与“native”JavaScript代码进行互操作的动态类型。要通过类型的API使用知名库，可以使用 [ts2kt转换器](http://github.com/kotlin/ts2kt)  连同标题 [绝对命令](http://github.com/DefinitelyTyped/DefinitelyTyped) 。
我们支持Node.js和浏览器。 Kotlin标准库可通过<code> npm </ code>使用。
阅读更多在我们的 [文件](http://kotlinlang.org/docs/reference/js-overview.html) 。
## 模具

Kotlin 1.1不是Kotlin工具的主要版本：我们更喜欢运输工具功能，一旦它们准备就不会影响语言本身，所以您已经看到Kotlin 1.0.x版本中的许多这样的改进。要突出几点：

* 所有主要IDE的Kotlin插件：IntelliJ IDEA，Android Studio，Eclipse和NetBeans
* IntelliJ IDEA和Gradle中的增量编译
* Spring，JPA和Mockito的编译器插件（使类打开并生成无参数构造函数）
* kapt用于注释处理
* Lint支持Android项目
* 许多IDE的意图，检查，快速修复，重构和代码完成改进

我们将继续努力使我们的工具更好，并在1.1.x版本中提供更新。
# 科特林第一年：收养与社区

总之，科特林正在成长。去年，我们看到有超过160,000人使用它。 Github上的OSS项目从2.4M增加到10M Kotlin码（约4x）。我们的Slack社区已经从1 400增长到超过5,700人（超过4倍）。社区组织了众多的聚会和用户组 [在世界各地](http://kotlinlang.org/community/talks.html) 。我们看到越来越多的Kotlin书籍和在线课程出版。

{% raw %}
<p><center><br/>
<img alt="Kotlin GitHub Stats" class="alignnone size-full wp-image-4679" height="375" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/GitHub-Stats-2.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/GitHub-Stats-1.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/03/GitHub-Stats-2.png" width="750"><br/>
</img></center></p>
{% endraw %}

Kotlin与服务器端和Android开发人员一样强大（大约50/50分）。 Spring框架5.0 [介绍了Kotlin的支持](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0) 也是如此 [vert.x 3.4](http://vertx.io/blog/vert-x-3-4-0-beta1-release/) 。 [毕业](https://blog.gradle.org/kotlin-meets-gradle)  和 [TeamCity](https://blog.jetbrains.com/teamcity/2016/11/kotlin-configuration-scripts-an-introduction/)  正在使用Kotlin构建脚本。使用Kotlin的更多项目可以在这里找到 [kotlin.link](http://kotlin.link) 。
许多知名公司正在使用科特林： [Pinterest](https://www.youtube.com/watch?v=mDpnc45WwlI) ， [Coursera](https://building.coursera.org/blog/2016/03/16/becoming-bilingual-coursera/) ， [Netflix](https://twitter.com/robspieldenner/status/708355228832178176) ， [Uber](https://www.reddit.com/r/androiddev/comments/5sihp0/2017_whos_using_kotlin/ddfmkf7/) ， [广场](https://github.com/square/sqldelight) ， [特雷洛](https://twitter.com/danlew42/status/809065097339564032) ， [大本营](https://m.signalvnoise.com/some-of-my-favorite-kotlin-features-that-we-use-a-lot-in-basecamp-5ac9d6cea95) ， 在其他人中。 [科达达](https://github.com/corda/corda) ，由知名银行（如高盛，富国银行，摩根大通，德意志银行，瑞银，汇丰银行，法国巴黎银行，SociétéGénérale）联盟开发的分销账户分类帐有 [超过90％的科特林](https://www.corda.net/2017/01/10/kotlin/)  在其代码库。
我们感谢世界各地的所有用户，贡献者和倡导者。您的支持对我们非常重要！
### 组织您自己的Kotlin 1.1事件

Kotlin 1.1是与当地用户组和朋友见面的好理由。我们已经准备了一些材料来帮助您举办此类活动。 3月23日，我们将以Kotlin团队成员的形式进行现场直播，另外还有一个组织者包，包括一些sw。和未来特征调查。获取更多信息和 [在这里注册你的活动](https://docs.google.com/forms/d/e/1FAIpQLSf6iXcrIpaNIqeeUJI2L6pntS5yy_iI01PbrO9gTMmX0kg5Lw/viewform) 。
# 下一步是什么

为了使Kotlin成为真正的全栈语言，我们将为多个平台编译相同的代码提供工具和语言支持。这将有助于在客户端和服务器之间共享模块。我们将继续致力于改进JavaScript工具和库的支持。除此之外，JavaScript平台的增量编译已经在作品中了。请继续关注1.1.x更新。
Java 9即将推出，我们将在发布之前为其新功能提供支持。
我们期望在未来几个月内对协同程序提供很多反馈意见，并且改进这一领域（在性能和功能方面）是我们的优先事项。
除此之外，我们的下一个版本将主要集中在维护，性能改进，基础架构和错误修复。
美国在多个平台上运行是Kotlin的战略方向。使用1.1，我们可以在服务器，台式机，Android设备和浏览器上运行，但是将来我们将编译Kotlin到本地代码，并在更多平台（包括例如iOS和嵌入式设备）上运行。 JetBrains的一个伟大的团队正在开展这个项目，我们期待很快就会展现出一些有趣的东西。但是，这并不针对任何特定版本。
# 安装说明

和往常一样，您可以<strong>在线尝试Kotlin </ strong> [try.kotlinlang.org](http://try.kotlinlang.org/) 。
<strong>在Maven / Gradle </ strong>中：使用<code> 1.1.0 </ code>作为编译器和标准库的版本号。查看文档 [这里](http://kotlinlang.org/docs/reference/using-gradle.html) 。
<strong>在IntelliJ IDEA </ strong>中：2017.1已将Kotlin 1.1捆绑在早期版本中，将Kotlin插件安装或更新到版本1.1。
<strong>在Android Studio中</ strong>：通过插件管理器</ em>安装或更新插件。
<strong>在Eclipse中</ strong>：使用插件安装 [市场](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse) 。
<strong>命令行编译器</ strong>可以从中下载 [Github发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1) 。
<strong>兼容性</ strong>。在Kotlin 1.1中，语言和标准库是 [向后兼容（模误）](http://kotlinlang.org/docs/reference/compatibility.html) ：如果有一些编译和运行在1.0，它将继续工作在1.1。为了帮助逐渐更新的大型团队，我们提供了一个禁用新功能的编译器开关。 [这里](http://kotlinlang.org/docs/reference/compatibility.html#binary-compatibility-warnings)  是一个涵盖可能陷阱的文件。
有一个漂亮的Kotlin！</ em>
美国参见讨论 [Reddit](https://www.reddit.com/r/programming/comments/5wvpv8/kotlin_11_released_with_javascript_support/)  和 [黑客新闻](https://news.ycombinator.com/item?id=13763483) 
