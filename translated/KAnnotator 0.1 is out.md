---
title: [译]KAnnotator 0.1 is out
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
---

我们在12月份宣布了KAnnotator：它可以帮助您抵御Java中的NPE，并使您的Kotlin代码更好。今天，我们很高兴地宣布IntelliJ的0.1版本的KAnnator插件。它可以从插件库中获得。
## 为什么插入注释

从早期的博客文章摘录，解释KAnnotator是什么：
由于Kotlin M3，您可以使用外部注释告诉系统您的方法返回/取非空值。即使不使用Kotlin，这种机制也是有用的：你也可以启用Java的可空性检查（我完全建议你这么做）。
关于这个的一个问题曾经是这样的，虽然你可以在编写自己的代码时注释自己的代码（我们一直在JetBrains这样做），但是你最喜爱的库没有注释，它是如此之大，你不能注释它手动。
这里的关键是“手动”。程序员是一个懒惰的生物，凭借我们的懒惰，我们希望尽可能自动化。 KAnnotator是一种自动注释库的工具（当然这个工具是用Kotlin编写的）。
简单来说，它的工作原理是：将你的库作为一个jar（或一些jar），你告诉KAnnotator来推断这些jar的注释，然后再回收一堆.xml文件。它们包含方法和字段的注释，例如：

现在，您可以将这些注释附加到项目中，Java IDE和Kotlin编译器都将看到它们。
我们使用KAnnotator来推断与Kotlin一起提供的JDK的注释。现在你也可以使用它：注释你自己的库。
## 安装

KAnnotator作为IntelliJ IDEA 12或更高版本的独立插件（12.0.4和12.1都可以工作）。请注意，Kotlin插件不是必需的。要安装插件，请按照此处的说明进行操作。
## 推断

不，您可以调用Analyze  - > Annotate Jar Files ...（从主菜单或上下文菜单）
你会得到一个这样的对话：

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s171/sh/7a64fc28-2eef-4fa5-ab4d-9c76d1e5b743/a39de23030a194a1c353d88bf08c88cf/res/764fc590-59e4-424a-9d63-134b9d15fd9c/skitch.png?w=640&amp;ssl=1"/></p>
{% endraw %}

在那里您指定要分析的JAR文件以及放置结果的位置，即包含注释的XML文件。默认情况下，KAnnotator会将注释附加到您调用的库中。
## 请享用

所以，当你看到Kotlin抱怨Java的可空类型时，你所需要做的就是在该Java库上运行一次KAnnotator，它会使你的红色代码变绿。
如果没有，也许KAnnotator不够聪明，但也许该方法实际上返回null？
