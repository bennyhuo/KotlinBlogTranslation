---
title: KotlinConf Keynote Recap
author: Dmitry Jemerov
date: 2017-11-02 20:51:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinconf-keynote-recap/
tags: 
categories:  官方动态  
translator: SnakEys  
translator_url: https://github.com/SnakeEys

---

今天对于Kotlin社区来说是意义非凡的一天。1200多名来自世界各地的与会者，齐聚三藩市，共庆KotlinConf——关于Kotlin的首次大会。大会开幕式上，Kotlin首席设计师Andrey Breslav宣布了一系列有关Kotlin的重磅消息以及未来发展。 
# Kotlin 1.2 RC

第一个重磅消息是**Kotlin 1.2候选发布版本**，此版本中的新特性包括对<strong>[多平台项目](http://kotlinlang.org/docs/reference/multiplatform.html)</strong>的实验性支持，因此开发者可在针对JVM和JavaScript的模块之间共享代码；以及几项<strong>语言改进</strong>，包括对注解中数组常量的支持。关于1.2版本中新功能的更多内容，请参考<strong>[Kotlin 1.2 Beta is out](https://github.com/enbandari/KotlinBlogTranslation/blob/master/translated/Kotlin%201.2%20Beta%20is%20out.md)</strong>。  

编译器现在已经无法编译由较早版本的Kotlin 1.2所编译的二进制文件，因此开发者需要重新编译新版本；而Kotlin 1.0或1.1.x版本则不受此影响。  

尽管协程(Coroutines)仍然被标记为实验性，但我们仍然要对此状态进行说明：协程已经**完全准备好用于生产项目中**，在我们自己的开发项目中就有使用，到目前为止尚未发现存在重大问题。目前仍然保留实验性状态的原因仅仅是让我们能够进行迭代设计。但即使我们对API进行了修改，已有的API仍然支持，即便被标记为弃用(deprecated)，我们也会提供必要的**迁移工具**。根据目前的计划，我们会在Kotlin 1.3版本中将协程的实验状态移除。  

而现在我们**需要大家的帮助**，尽管在团队内部以及JetBrains其它团队中进行了大量的长时间测试，但实际情况要比我们想象的复杂的多。如果可以请在您自己的项目中尝试使用1.2RC版本，如果遇到任何问题，请与我们联系。您的反馈对于确保最终版本的顺利发布至关重要。

{% raw %}
<p><span id="more-5407"></span></p>
{% endraw %}

# Kotlin/Native iOS支持

作为Kotlin/Native 0.4的一部分，第二个大新闻是Kotlin/Native支持iOS开发。然而目前还处于早期阶段，但从无到有，让Kotlin在全平台开发的道路上迈出了巨大的一步。  

为此，我们编写了两个应用程序，并发布在了App Store:

* [Spinner App](https://itunes.apple.com/us/app/kotlinconf-spinner/id1291282375?mt=8)([Github](https://github.com/jetbrains/kotlinconf-spinner))是一款使用OpenGL编写的简单游戏。可以同时运行在iOS和Android平台上([Play Sotre链接](https://play.google.com/store/apps/details?id=com.jetbrains.konan_activity2))，两个版本之间的大部分代码是通用的。但在iOS版本中集成了Game Center。
* [KotlinCof App](https://itunes.apple.com/us/app/kotlinconf/id1299196584?mt=8)([Github](https://github.com/jetbrains/kotlinconf-app))是一款可以展示本次大会的时间流程的应用程序，并使用UIKit构建完全原生的iOS界面。

以上两个程序的代码完全开源，开发者可以将其作为模板蓝本，完全使用Kotlin来构建自己的跨平台移动应用程序。

# Kotlin/Native IDE支持

当然，无论任何语言，使用IDE都可以大幅提高效率，从今天开始，Kotlin/Native也开始有IDE支持了。

我们即将为自己的C/C++ IDE——CLion，发布一款Kotlin/Native插件的初始预览版本。插件支持使用CMake作为构建系统，它包括IntelliJ IDEA Kotlin插件的全套代码编辑功能，以及对创建项目，测试和调试的初始支持。

{% raw %}
<p><a href="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/clion-debugger.png" rel="attachment wp-att-5414"><img alt="clion-debugger" class="alignnone size-full wp-image-5414" height="612" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/clion-debugger.png" width="1600"/></a></p>
{% endraw %}

目前插件可在2017.3 EAP版本CLion中的JetBrains插件列表中获取(搜索“Kotlin/Native”)。  

后续我们将单独发布博客文章，详细介绍该插件及其功能。当然CLion插件仅仅只是我们对Kotlin IDE支持故事中的一步。请继续关注来年的更多消息。

# Ktor 0.9

**服务端开发**在我们的多平台项目中也是非常关键的内容之一。现在我们宣布[Ktor](http://ktor.io/) 0.9版本正式面世，这是一款由Kotlin构建的了不起的基于异步协程的**Web端框架**。

Ktor已经应用于JetBrains内部和社区的诸多项目中，而且我们相信它足以成为构建高性能Web应用程序的基石。开发者可以在ktor.io上查看[快速入门手册](http://ktor.io/quickstart/index.html)，尝试一下，告诉我们您的想法，让我们可以在1.0版本中做的更好。

# 使用React和Kotlin创建现代Web应用程序

对于使用Kotlin进行Web前后端的开发者而言，今天最大的消息莫过于为[React.js](https://reactjs.org/)发布的[官方Kotlin包装器](https://github.com/JetBrains/kotlin-wrappers)，以及使用React.js在Kotlin中创建现代Web应用程序的工具箱[create-react-kotlin-app](https://www.npmjs.com/package/create-react-kotlin-app)。有了这个工具箱，开发者可以生成并立即开始进行客户端应用开发，无需关注项目设置和构建配置，享受静态类型语言的好处，以及JavaScript生态系统的强大功能。  

获取组件请运行`npm install -g create-react-kotlin-app`，查看[入门指南](https://github.com/JetBrains/create-react-kotlin-app/)。

# 多平台项目演示

为了充分展示多平台项目中的所有内容，我们应用目前所有技术栈的最新版本构建了KotlinConf应用程序，所使用的组件包括如下内容：

* 后端使用Ktor；
* 浏览器应用程序使用React.js和Kotlin React包装器；
* Android应用程序使用Anko和Android体系结构组件；
* iOS应用（见上文）使用UIKit。

后端，浏览器应用和Android应用程序均使用Kotlin跨平台项目技术共享代码。异步编程均使用协程实现。服务端与客户端数据交互则使用全新的[kotlinx.serialization库](https://github.com/kotlin/kotlinx.serialization)。  

开发者能够从该程序的源代码中获益良多，并可直接应用于实际工作中。

# 学习Kotlin

伴随着Kotlin的喧嚣而上，会有越来越多的人对Kotlin产生兴趣并开始学习。为此，我们发布了新版本的[EduTools插件](https://www.jetbrains.com/education/kotlin-edu/)，让学习Kotlin更轻松，让开发者在自己最爱的IDE中通过解决交互练习掌握Kotlin。新版本增加了对Android Studio的支持(旧版本仅支持IntelliJ IDEA)，并包括用于构建自己课程的新UI。

# 未来的方向

至于语言的未来发展，当下的主要目标是在Kotlin支持的平台之间实现更好和更广泛的代码重用。我们计划使用相同的API扩展在所有平台上可用的库，包括I/O，网络，序列化，日期处理等等。
在编译器中，对于1.3版本我们的主要焦点仍然是关注内部变化，而非外部可见的语言特性。内部的改变可以提高性能，改进类型推断，为所有目标平台生成更高效的代码，以及更好的IDE插件响应能力。我们希望在新版本发布时仍然有不错的新语言特性，但是目前我们对此不做任何承诺。  

Let's Kotlin！
