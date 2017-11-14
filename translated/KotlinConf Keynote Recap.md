---
title: KotlinConf Keynote Recap
author: Dmitry Jemerov
date: 2017-11-02 20:51:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinconf-keynote-recap/
tags: 
categories:  官方动态
---

今天是Kotlin社区的好日子。 KotlinConf是首个Kotlin会议，今天开幕，我们留下深刻的印象，大约有1200名来自世界各地的与会者加入了我们的旧金山。在会议主题演讲中，Kotlin的首席设计师Andrey Breslav宣布了Kotlin的一些重大发展，现在我们正在与其他人分享这个消息。
# Kotlin 1.2 RC

主题演讲的第一个重要公告是Kotlin 1.2 Release Candidate的发布。此版本中的新功能包括对多平台项目的实验性支持，允许您在针对JVM和JavaScript的模块之间共享代码，以及多种语言改进，包括支持注释中的数组文字。有关1.2中的新功能的更多信息，请查看Kotlin 1.2 Beta公告博客文章。
编译器现在拒绝使用较早版本的Kotlin 1.2编译的二进制文件;你需要重新编译这个版本。用Kotlin 1.0.x或1.1.x编译的代码当然是完全兼容这个版本的编译器。
尽管协程仍然被标记为一个实验性的特征，但是我们想澄清这个状态的确切含义。协程完全准备好用于生产，我们将它们用在自己的开发中，而且我们不知道有什么实施的重大问题。我们保持实验状态的原因是它使我们有能力重复设计。请注意，即使我们对API进行了更改，当前API仍将受支持，即使它将被标记为已弃用，我们也将提供必要的迁移工具。根据我们目前的计划，Kotlin 1.3将删除协程的实验状态。
现在是我们要求你帮忙的时候了。尽管我们已经在JetBrains内部和其他团队对这个版本进行了大量的测试，但真实世界比我们所访问的要多得多。因此，请给Kotlin 1.2 RC试一下自己的项目，如果遇到任何问题，请告诉我们。您的帮助对于确保顺利的最终版本至关重要。
告诉大家去试试看

{% raw %}
<p><span id="more-5407"></span></p>
{% endraw %}

# Kotlin / Native iOS支持

我们宣布的下一个重大消息是支持Kotlin / Native的iOS开发，作为Kotlin / Native 0.4的一部分发布。这种支持还处于早期阶段，但在这方面，这是我们在所有平台上实现科特林发展的重要一步。
为了展示什么是可能的，我们写了两个应用程序，并将它们发布到App Store：

* Spinner应用程序（GitHub）是使用OpenGL构建的简单游戏。它在iOS和Android上运行（玩商店链接），大部分代码在这两个版本之间共享。 iOS版本还有其他一些功能，如Game Center集成。
* KotlinConf应用程序（GitHub）向您显示本次会议的时间安排，并具有完全原生的UIKit构建的iOS UI。

这两个示例应用程序都是开源的，您可以将它们作为模板在纯Kotlin中构建自己的跨平台移动应用程序。
# Kotlin / Native IDE支持

当然，你需要一个IDE来使用任何语言，从今天开始，Kotlin / Native也有IDE支持。
我们现在正在发布CLion的Kotlin / Native插件的最初预览版本，我们的C / C ++ IDE。该插件支持CMake作为构建系统。它包括IntelliJ IDEA的Kotlin插件的全套代码编辑功能，以及对项目创建，测试和调试的初始支持。

{% raw %}
<p><a href="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/clion-debugger.png" rel="attachment wp-att-5414"><img alt="clion-debugger" class="alignnone size-full wp-image-5414" height="612" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/clion-debugger.png" width="1600"/></a></p>
{% endraw %}

要尝试插件，请安装CLion 2017.3 EAP并在JetBrains插件列表中搜索“otlin / Native”。
在未来的日子里，我们将发布一个单独的博客文章，详细介绍插件及其功能。当然，CLion插件只是我们Kotlin IDE支持故事中的一步。请继续关注明年的进一步公告！
# Ktor 0.9

服务器端开发也是我们多平台故事的关键部分。而现在我们正在宣布我们自己的这一部分：Ktor的0.9版本，这是一个非常棒的基于异步协程的Web框架，从Kotlin开始构建。
Ktor已经在JetBrains内部和社区中的许多项目中使用，现在我们相信它是构建高性能Web应用程序的坚实基础。查看ktor.io上的快速入门指南，试用一下，让我们知道您的想法，以便我们可以在1.0版本中做得更好。
# 使用React和Kotlin创建现代Web应用程序

对于使用Kotlin进行Web前端开发，今天最大的新闻是发布React.js的官方Kotlin包装器，以及使用React.js在Kotlin中创建现代Web应用程序的工具箱create-react-kotlin-app。 。使用create-react-kotlin-app，您可以生成并立即开始在客户端应用程序上工作，而无需担心项目设置和构建配置，使用静态类型语言的好处以及JavaScript生态系统的强大功能。
要开始，请运行npm install -g create-react-kotlin-app并查看入门指南。
# 多平台项目演示

为了展示我们的多平台故事中的所有内容，我们使用我们的技术堆栈的所有最新版本构建了一个应用程序：KotlinConf应用程序。它由以下组件组成：

* 使用Ktor的后端;
* 使用React.js和Kotlin React包装的浏览器应用程序;
* 使用Anko和Android体系结构组件的Android应用程序;
* iOS应用（上面提到）使用UIKit。

后端，浏览器应用程序和Android应用程序使用Kotlin多平台项目技术共享代码。对于异步编程，所有组件都使用协程。为了在服务器和客户端之间交换数据，我们使用全新的kotlinx.serialization库。
您可以从应用程序的源代码中找到技术宝库，您也可以在自己的工作中使用这些宝藏。
# 学习Kotlin

随着Kotlin的各种喧嚣，越来越多的人对学习语言感兴趣。为了使这一点更容易，我们发布了新版本的EduTools插件，允许通过在您喜欢的IDE中解决交互式练习来学习Kotlin。新版本增加了对Android Studio的支持（以前只支持IntelliJ IDEA），并包含用于构建自己的课程的新UI。
# 未来的方向

至于语言的未来发展，我们目前的主要目标是在Kotlin支持的平台之间实现更好，更广泛的代码重用。我们计划使用相同的API扩展在所有平台上可用的库集，以包括I / O，网络，序列化，日期处理等等。
在编译器中，我们关注1.3的主要焦点仍然是内部变化，而不是外部可见的语言特性。内部的改变可以提高性能，改进类型推断，为所有目标平台生成更高效的代码，以及更好的IDE插件响应能力。我们希望我们仍然可以用一些很好的新语言来释放发行版，但是我们现在还没有做出任何承诺。
让科特林！
