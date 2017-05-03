---
title: "[译]Kotlin’s Android Roadmap"
date: 2016-03-30 16:40:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/03/kotlins-android-roadmap/
---

## 介绍

Google最近发布的最有趣的消息之一是Google宣布 [（有限）Java 8支持Android N](http://developer.android.com/preview/j8-jack.html) 与Java的杰克编译器。当然，我们的用户对这些消息如何影响他们很好奇，而这篇博客文章根据Google的公告，概述了我们的计划和我们对Kotlin在Android开发领域的看法。
<span id =“more-3784”> </span>
### Kotlin的Android路线图

我们非常重视使Kotlin成为Android开发的好工具。在接下来的几个版本（1.0.X）中，我们将继续改进我们的工具链和库。我们目前的努力主要集中在三个主要领域：加快开发工作流程，减少运行时库的大小，并提供更完整的工具支持。
#### 开发工作流程

为了加快开发工作流程，<b>增量编译</b>来到Kotlin的Gradle插件。这将大大改善构建时间：当源文件更改时，我们只会重新编译这个特定文件，这些文件真的取决于它，而不是整个模块。
我们接下来要做的是提高Android构建性能，这是提供与Android新的<b> <a href="http://tools.android.com/tech-docs/jackandjill">杰克和吉尔工具链< a> </b>。现在有一些问题阻止杰克正确处理Kotlin生成的字节码（ [196084年](https://code.google.com/p/android/issues/detail?id=196084) 和 [203531](https://code.google.com/p/android/issues/detail?id=203531) ），但是我们计划与Google团队一起解决问题或提供解决方案。一旦完成，我们将能够在增量编译期间仅使用Jill翻译已更改的类文件，而不是每次翻译所有类文件（这是旧版Android工具中唯一可能的行为）。
最后但并非最不重要的：<b>即时运行</b>。目前，冷交换对于Kotlin来说是正常的，但暖和热交换需要进一步调查。我们将竭尽全力尽快解决问题。同时， [适用于Android的JRebel](https://zeroturnaround.com/software/jrebel-for-android/) Kotlin已经很好了。
#### 运行时大小

我们正在计划对<b>减少kotlin-stdlib的方法计数</b>的几项改进。我们目前的结果是7'191：<img src =“https://img.shields.io/badge/Methods count-core：6289 | deps：902-e91e63.svg”style =“

    显示：inline;

    填充：0;

    margin：0px 0px -4px 15px;

“/>
在多文件外观类中优化顶级函数表示，并将仅内联函数从运行时可用的二进制文件中移出将会赢得我们几千种方法。
#### 模具支持

Kotlin 1.0的Android支持故事中缺少的主要内容是<b> Lint Checks </b>，我们很高兴地宣布他们来到Kotlin。我们已经实施了Android Studio 1.5中可用的所有支票（计划在Kotlin 1.0.2中发布），新的2.0检查正在进行中。我们的Lint检查是建立在Kotlin和Java代码的常见表示之上的，我们计划将该表示贡献给Android SDK，以便在未来版本的Android SDK中添加新的检查将与Kotlin开箱即用。
随着1.0.X版本的发布，还将逐渐添加更多Android特定的IDE支持，例如新的Kotlin活动</i>动作，代码洞察和导航功能等。
### Kotlin和Java 8

Java 8已经存在了很长一段时间，因此我们的许多用户，那些没有做Android开发的用户，已经选择了Kotlin的Java 8，并对此感到高兴。现在，Android已经对Java 8语言功能提供了正式的支持，那么如何改变Kotlin和Java之间的选择呢？
首先，虽然Java 8将lambdas引入Android，但Android工具链在现有平台版本（不运行N版本）上支持lambdas的方式与Kotlin支持lambdas的方式之间存在重大差异。要了解不同之处，请看下面简单的代码片段如何编译：
Kotlin：<code> list.forEach {process（it）} </code> <br/>

Java 8：<code> list.forEach（it  - ＆gt; process（it））</code>
Java的版本稍微长了一些，但是我们不会专注于这一点。相反，让我们看看引擎盖下会发生什么。从Java开始：

* 在Android的Java 8中，每个lambda都被编译成一个类，它有两种方法：构造函数和实体（影响应用程序的方法计数）;
* 这个类在运行时稍后实例化，在许多情况下 - 每次调用forEach（在垃圾收集器上产生压力）;
* 并且要访问它，Java使用对Consumer.accept的多态调用，这可能在紧密循环的每次迭代中发生（影响性能，因为运行时并不总是内联这样的调用）。

在一般情况下，Kotlin以完全相同的方式实施羊羔。然而，在许多情况下，包括大多数收集操作（例如<code> forEach </code>），Kotlin通过使用<i>内联函数</i>生成更高效的字节码。当您使用带有lambda的内联函数时，函数的主体和lambda都将在调用站点内联。结果是：

* lambda的字节码直接插入到调用方法的字节码中，所以方法计数不增加;
* 执行代码不分配任何对象，所以没有垃圾收集器的压力;
* 生成的字节码不包含任何多态方法调用，以确保运行时可能的最佳执行速度。

Bottomline：Android上的Java 8中的lambdas并不是免费的，每个人都可能会考虑两次，并选择良好的代码和性能。在Kotlin，对这种妥协的需求大大减少，您可以使用lambdas尽可能多地在代码中表达想法。
当然，Kotlin还有许多其他语言功能，在任何Java版本中都不可用。只是列举几个：

* 支持空安全防止代码中的大部分NullPointerException问题，可以让您从可怕的“不幸的是，应用程序已停止”消息;
* 属性，主构造函数和数据类大大减少了代表应用程序数据模型的代码中的样板数量：
数据类User（val name：String，val groupId：String =“default”）
* 委派属性允许提取属性getter和setter中的常见逻辑，并将其放入库中：
val imageData by lazy {loadData（imageFile）}

而且，Kotlin的DSL构造功能使您在构建您的应用程序方面具有全新的灵活性，这在Java中根本不可用。例如，它可以让您选择使用嵌入式DSL替换XML布局，并以与其余代码相同的语言来描述应用程序的UI，并可完全访问该语言的抽象功能。这是怎么实现的 [安科图书馆](https://github.com/kotlin/anko) ：

{% raw %}
<p></p>
{% endraw %}

```kotlin
verticalLayout {
    val name = editText()
    button("Say Hello") {
        onClick { toast("Hello, ${name.text}!") }
    }
}
```

{% raw %}
<p></p>
{% endraw %}

正如你所看到的，Kotlin提供了很多很多的东西来提高你的工作效率，超出Java 8可以为Java 6开发人员提供的。而且也很容易学习 [综合文件](https://kotlinlang.org/docs/reference/) ， [互动练习](http://blog.jetbrains.com/kotlin/2016/03/kotlin-educational-plugin/) 和书籍涵盖两者 [Kotlin一般](https://www.manning.com/books/kotlin-in-action) 和使用 [Kotlin为Android开发](https://leanpub.com/kotlin-for-android-developers) 。所以如果你还没有尝试过Kotlin，现在和任何时候一样好！
