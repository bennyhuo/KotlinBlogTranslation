---
title: "[译]KAnnotator 0.1 is out"
date: 2013-03-29 14:42:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/03/kannotator-0-1-is-out/
translator:
translator_url:
---

我们宣布 KAnnotator 回来了 [在十二月](http://blog.jetbrains.com/kotlin/2012/12/kotlin-m4-is-out/) ：它可以帮助您抵御 Java 中的 NPE [使您的 Kotlin 代码更好](http://blog.jetbrains.com/kotlin/using-external-annotations/) 。今天，我们很高兴地宣布 IntelliJ 的 0.1 版本的 KAnnator 插件。它可以从插件库中获得。<span id =“more-1005”> </span>
## 为什么插入注释

摘自早期的摘录 [博客文章](http://blog.jetbrains.com/kotlin/2012/12/kotlin-m4-is-out/) 说明 KAnnotator 是什么：
<p> <span style =“font-size：16px”>由于 Kotlin M3 </span> <span style =“font-size：16px”>，可以使用</span> <a href =“http： /blog.jetbrains.com/kotlin/using-external-annotations/">外部注释</a> <span style =“font-size：16px”>告诉系统你的方法返回/取非空值。即使您不使用 Kotlin，此机制也很有用：您可以打开</span> <a href="http://www.jetbrains.com/idea/documentation/howto.html"> Java 的可空性检查< / a> <span style =“font-size：16px”>（我完全建议你这样做）。</span> </p>
<p>一个问题就是这样，虽然你可以在编写代码时注释自己的代码（而且我们这样做<a href =“https://github.com/JetBrains/kotlin/blob/master/compiler /frontend/src/org/jetbrains/jet/lang/types/TypeConstructor.java">所有</a> <a href =“https://github.com/JetBrains/intellij-community/blob/master/platform/ util / src / com / intellij / util / text / CharArrayUtil.java“> </a> <a href =”https://github.com/JetBrains/la-clojure/blob/master/src/org/jetbrains /plugins/clojure/utils/ClojureUtils.java">时间</a>在 JetBrains），您最喜欢的图书馆没有注释，它是如此之大，你不能手动注释。</p>
<p>这里的关键是“手动”。程序员是一个懒惰的生物，凭借我们的懒惰，我们希望尽可能自动化。 **KAnnotator**是一种**自动注释库的工具**（该工具当然是用 Kotlin 编写的）。</p>
简单来说，它是如何工作的：你把你的库作为一个 jar（或一些 jar），你告诉 KAnnotator 来推断这些 jar 的注释，并得到一堆.xml 文件回来它们包含方法和字段的注释，例如：</p>
<p> <a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png"> <img alt =“”class =“aligncenter” data-recalc-dims =“1”src =“https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png?resize=409%2C149&amp;ssl= 1“/> </a> </p>
<p>现在，您可以将这些注释附加到项目中，Java IDE 和 Kotlin 编译器都将看到它们。</p>
我们使用 KAnnotator 来推断与 Kotlin 一起提供的 JDK 的注释。现在你也可以使用它：注释你自己的库。
## 安装

KAnnotator 作为一个单独的插件 [IntelliJ IDEA 12](http://www.jetbrains.com/idea/) 以上（12.0.4 和 12.1 都可以工作）。请注意，Kotlin 插件**不是必需的**。要安装插件，请按照以下说明进行操作 [这里](http://www.jetbrains.com/idea/plugins/index.html) 。
## 推断

不，您可以调用 Analyze  - > Annotate Jar Files ...（从主菜单或上下文菜单）<img alt =“”data-recalc-dims =“1”src =“https://i2.wp.com/www。 eSCSI.com/shard/s171/sh/8242aa4b-939b-416c-9880-6a6b97f748ce/add22424ad329409984c8f1df963bfde/res/902508da-cf33-453b-9790-c2af86cfa407/skitch.png?w=640&amp;ssl=1“/>
你会得到一个这样的对话：

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s171/sh/7a64fc28-2eef-4fa5-ab4d-9c76d1e5b743/a39de23030a194a1c353d88bf08c88cf/res/764fc590-59e4-424a-9d63-134b9d15fd9c/skitch.png?w=640&amp;ssl=1"/></p>
{% endraw %}

在那里您指定要分析的 JAR 文件以及放置结果的位置，即包含注释的 XML 文件。默认情况下，KAnnotator 会将注释附加到您调用的库中。
## 请享用

所以，当你看到 Kotlin 抱怨 Java 的可空类型时，你所需要做的就是在该 Java 库上运行一次 KAnnotator，它会使你的红色代码变绿。
如果没有，也许 KAnnotator 不够聪明，但也许该方法实际上返回 null？
