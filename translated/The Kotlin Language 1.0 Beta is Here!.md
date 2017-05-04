---
title: "[译]The Kotlin Language: 1.0 Beta is Here!"
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
translator:
translator_url:
---

我们非常高兴为JVM和Android提供**Kotlin 1.0 Beta**！
总结： [Kotlin](https://kotlinlang.org/) 是一种**现代编程语言** [JetBrains](https://www.jetbrains.com/) 现在已经有一段时间了。
这篇文章概述了我们在哪里和接下来会发生什么。列出了此版本中的更改 [这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-1103) 。
## Kotlin背后的故事

Kotlin是在2010年设想的。十年的Java开发使我们感到，JetBrains的生产力可以通过与Java一起使用现代的JVM语言来显着提高。在评估了其他可用选项后，我们决定在那里需要一种新的语言，我们有专门知识和资源来创建这样一种语言。我们的主要业务是为开发人员制作工具，其指导原则是，为用户制作出令人敬畏的产品的最佳方式是制作一个我们需要的真棒工具。这与IntelliJ IDEA，ReSharper和许多其他IDE以及TeamCity和其他服务器产品配合使用，因此我们开始将另一个开发工具 - 一种编程语言应用于相同的原理。 <span id =“more-3005”> </span>
我们将Kotlin设计为行业的**现代语言**，并且具有相当的具体要求。首先，我们的项目活得很长，成长真的很大（数百万行代码），所以我们需要**静态打字**，以便能够准确地说明巨大的代码库并保持这些年。然后，我们的所有代码都是用Java编写的，所以我们需要一个**平滑的迁移路径**，其中新语言可以**逐渐引入现有的Java代码库，影响其他代码尽可能少。另外，作为JetBrains，我们不想在**工具质量**上妥协：我们正在寻找一种新的语言来使我们更有效率，而且我们相信这大部分取决于工具。最后，我们需要一种易于学习和理解的语言**：在我们的团队中，我们不会将“图书馆用户”与“图书馆用户”分开，我们希望我们所有的开发人员能够与他们正在使用的语言
这样的一个项目涉及做出很多决定，从一开始就知道，第一次尝试是不可能的。这就是为什么我们允许相当长的时间进行核心设计选择的实验和验证：由于JetBrains内部和外部的早期采用者正在使用它们，我们不断收集反馈并进行更改（非常感谢我们的社区对您的所有评论人们给了我们！）。这给了我们对广泛使用案例的重要见解，现在我们相信我们可以在1.0**后保持向后兼容性。
JetBrains一直在使用Kotlin生产 [IntelliJ IDEA](https://www.jetbrains.com/idea/) ， [YouTrack](https://www.jetbrains.com/youtrack/) 和其他产品现在相当长的时间。我们现在有超过**250'000 LOC的Kotlin LOC（**）（加上大约在 [Kotlin项目](https://github.com/JetBrains/kotlin) 本身）。虽然我们的一些项目完全是写在Kotlin（ [account.jetbrains.com](https://account.jetbrains.com) ），其他人已经将其引入现有的Java代码库，正如我们最初计划的。我们达到了互操作性水平，自由地将Kotlin与Java一起放在Java客户端是透明的：Java可以从Kotlin调用，反之亦然，源可以混合在一个项目中，从而导致`.class`文件完全兼容使用Java工具。
Kotlin正在为我们服务，我们致力于发展超过20人的**团队。
尽管尚未达到1.0，但其他公司和个人开发人员已经将Kotlin从生产中使用，从网络服务后端到Android应用。我们有报告 [Expedia](https://twitter.com/fleurchild/status/636965650536108032) ， [Prezi.com等等](https://github.com/JetBrains/kotlin-web-site/blob/master/_data/companies-using-kotlin.yml) （请随时通过提交PR将您的公司添加到此列表中）。
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

Kotlin将不会停留在Beta版，1.0即将来临。
我们致力于平滑用户体验，这包括Kotlin版本的兼容性。 1.0之后，所有对语言和库的更新将是**向后兼容**：

* 较新的编译器将使用较旧的二进制文件（但较旧的编译器可能不了解较新的二进制文件，如javac 1.6无法读取由javac 1.8编译的类）;
* 较旧的二进制文件将在运行时继续使用较新的二进制文件（尽管更新的代码可能需要较新的依赖关系）。

上述所有内容仅适用于JVM / Android支持。 JavaScript支持现在仍然是实验性的，稍后会有自己的发行版。
## 关于Kotlin的几个事实


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

任何Java或Android框架或图书馆几乎可以与Kotlin平滑地工作**。其中包括Spring MVC </em>，Vaadin </em>，</em>和<em>杰克逊</em>。许多Android框架需要通过Kotlin可用的注释处理 [kapt](http://blog.jetbrains.com/kotlin/2015/06/better-annotation-processing-supporting-stubs-in-kapt/) 它支持<em> Dagger 2 </em>，<em> DataBinding </em>，<em> DBFlow </em>，</em> ButterKnife </em>，<em> AndroidAnnotations </em>等。
Kotlin拥有由JetBrains和社区开发的**自己的框架和库**。一些例子： [安科](https://github.com/JetBrains/anko) ， [RxKotlin](https://github.com/ReactiveX/RxKotlin) ， [funKtionale](https://github.com/MarioAriasC/funKTionale) ， [kohesive](https://github.com/kohesive/) ， [约柜](https://github.com/mplatvoet/kovenant) ， [科巴尔特](http://beust.com/kobalt) 构建工具和 [多得多](https://kotlinlang.org/docs/resources.html) 。
内置IDE的**转换器**有助于将源代码从Java迁移到Kotlin。
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

**<em>有一个漂亮的Kotlin！</em>**
