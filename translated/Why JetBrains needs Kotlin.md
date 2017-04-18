---
title: "[译]Why JetBrains needs Kotlin"
date: 2011-08-02 15:52:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/08/why-jetbrains-needs-kotlin/
---

动机的问题是有人在学习有人正在使用新的编程语言时首先询问的问题。 Kotlin文档提供了关于语言存在的原理的相当详细的概述。尽管如此，我们也希望能够更清楚JetBrains希望从整体上获得的结果。我们显然是长期的，是的，我们意识到需要多年才能达成目标。这就是为什么我们愿意做这个投资。
首先，这是关于我们自己的生产力。虽然我们已经开发了对几种JVM目标编程语言的支持，但是我们仍然将所有的基于IntelliJ的IDE完全用Java编写。 IntelliJ构建系统基于Groovy和Gant，一些Groovy也用于测试，RubyMine中有一些JRuby代码，就是这样。我们希望通过切换到更具表现力的语言来提高生产力。同时，我们不能接受Java互操作性方面的妥协（新语言将逐步引入，需要与现有代码库平滑地进行互操作）或编译速度（我们的代码基础需要足够长的时间来编译javac，我们买不起，要慢一些）。
接下来的事情也是相当直截了当的：我们期望科特林推动IntelliJ IDEA的销售。我们正在开发一种新的语言，但是我们不打算替代为JVM构建的整个生态系统。因此，您可能会在使用Kotlin构建的项目中继续使用Spring和Hibernate或其他类似的框架。虽然Kotlin本身的开发工具将是免费的和开源的，但对企业开发框架和工具的支持仍将是IDE的商业版本IntelliJ IDEA Ultimate的一部分。当然，框架支持也将与科特林完全融合。
最后一点不太明显，但仍然很重要：新的编程语言是许多人真正喜欢谈论的话题，自从我们公布Kotlin以来已经过去的第一天证明了这一点。我们看到已经熟悉JetBrains的人相信公司能够在这个项目中做得很好。因此，我们相信，JetBrains的这种信任和日益增长的社区意识不仅将推动公司的业务发展，而且还将吸引更多的人来构建开发工具，并让他们以快乐的方式发展。
我们想重申，我们对Kotlin的工作并不会影响我们对其他开发工具的投入，特别是Scala插件。如果您已经对Scala感到满意，并且不需要另一种新语言，我们将继续尽力为您提供一流的Scala开发工具。
