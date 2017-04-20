---
title: "[译]为什么 JetBrains 需要 Kotlin"
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

动机是人们在学习或使用新的编程语言时首先要问的问题。 Kotlin 文档对于这门语言为何出现已经做了相当详细的说明。尽管如此，我们还是乐于让大家更加清楚 JetBrains 希望从这门语言上获得什么。这门语言的开发显然是项长期的工作，我们明确意识到需要多年才能达成目标。而以下就是为什么我们愿意做这个投入的原因。

首先，这关乎我们自己的生产力。虽然我们已经为若干门 JVM 语言开发过工具，但都是基于 IntelliJ 的 IDE 完全用 Java 编写的。IntelliJ 构建系统基于 Groovy 和 Gant，同时 Groovy 也用于部分测试，RubyMine 中则有一些 JRuby 代码，这是目前的概况。我们希望通过切换到更具表现力的语言来提高生产力。同时，我们不希望这门语言存在与 Java 交互（新语言将逐步引入，需要与现有代码库顺畅地进行交互）或编译速度（我们的代码库需要使用 javac 编译很长的时间，任何程度的变慢我们都无法接受）方面的问题。

接着这点则十分简单明了：我们期望 Kotlin 推动 IntelliJ IDEA 的销售。我们正在开发一种新的语言，但是不打算让它替代 JVM 构建的整个生态系统。因此，您可以在使用 Kotlin 构建的项目中继续使用 Spring 和 Hibernate 或其他类似的框架。虽然 Kotlin 本身的开发工具将是免费的和开源的，但对企业开发框架和工具的支持仍将是 IDE 的商业版本 IntelliJ IDEA Ultimate 的一部分。所以使用 Kotlin 时也将获得完整的框架支持。

最后一点不太明显，但仍然很重要：新的编程语言是许多人喜欢谈论的话题，而我们公布 Kotlin 的那第一天就证明了这一点。许多熟悉 JetBrains 的人相信我们能够在这个项目中做得很好。因此我们相信对 JetBrains 的这种信任和日益增长的社区意识不仅将推动公司的业务发展，而且还将吸引更多的人来构建开发工具同时获得乐趣。

另外我们想重申：Kotlin 的工作并不会影响我们对其他开发工具的投入，特别是 Scala 插件。如果您已经对 Scala 感到满意，并且不需要另一种新语言，我们将继续尽力为您提供一流的 Scala 开发工具。