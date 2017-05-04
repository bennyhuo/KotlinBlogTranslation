---
title: "[译]First glimpse of Kotlin 1.1: Coroutines, Type aliases and more"
date: 2016-07-14 19:01:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/07/first-glimpse-of-kotlin-1-1-coroutines-type-aliases-and-more/
translator:
translator_url:
---

虽然Kotlin 1.0.X版本不断提供增量更新和工具功能，但我们正在研究Kotlin 1.1中的新语言功能。今天，我们展示了1.1的第一个预览版本，它远离Beta，但勇敢和好奇的人可以玩新的令人兴奋的事情（希望能给我们提供宝贵的反馈）。
## 兼容性

这不是Kotlin的稳定版本，并且<strong>不兼容性保证</strong>在这里给出：在1.1的未来预览中，语法，API，命令行开关和任何其他可能会更改。如果您需要Kotlin的稳定版本，请留在1.0.X，直至另行通知。
## 反馈

这种暂时缺乏保证的上升空间是我们可以立即使用您提供给我们的所有反馈！告诉我们你认为是什么的最好方式 [保持](https://github.com/Kotlin/KEEP) 请留意您对以下提案中提出的问题的意见。 Kotlin 1.1 M01中的实现是KEEP中描述的功能的原型。
## 概述

1.1 M01的完整更新日期可用 [这里](https://github.com/JetBrains/kotlin/blob/1.1-M1/ChangeLog.md#11-m01-eap-1) <span id =“more-4080”> </span>
## 协调程序

我们都知道，在高负载下阻塞是坏的，轮询是一个不停的，世界正在变得越来越多的基于推动和异步。许多语言（2012年以C＃开头）通过专用语言结构支持异步编程，例如`async` / `等待`关键字。在Kotlin中，我们概括了这个概念，以便库可以定义自己的这样的结构版本，而`async`不是一个关键字，而只是一个函数。
这种设计允许不同异步API的集成：期货/承诺，回调传递等。表达延迟生成器（`yield`）并涵盖其他一些用例也是一般的。
所以，满足Kotlin 1.1的更大功能之一：<em>协同程序</em>。这是一个传统的CS术语，用于“泛化非优先多任务的子程序的程序组件”，但是我们不会在这里介绍理论<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1 “src =”https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em ; max-height：1em;“/>

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun main(args: Array<String>) {
    val future = async<String> {
        (1..5).map {
            await(startLongAsyncOperation(it)) // suspend while the long method is running
        }.joinToString("\n")
    }
 
    println(future.get())
}
 
```

{% raw %}
<p></p>
{% endraw %}

关于协同程序的好处是，他们可以暂停</em>而不阻止线程，但它们看起来像正常的顺序代码。请看一下 [详细说明](https://github.com/Kotlin/kotlin-coroutines/blob/master/kotlin-coroutines-informal.md) 和一个专门的例子 [KEEP存储库](https://github.com/Kotlin/kotlin-coroutines) 并评论 [那里的问题](https://github.com/Kotlin/kotlin-coroutines/issues) 。
我们是基于协同程序的库的原型 [这里](https://github.com/Kotlin/kotlinx.coroutines) ，随后被列入标准库。这包括来自Swing中的UI线程的JDK的`CompletableFuture`，异步IO（NIO），RxJava和卸载任务。这个回购包含了例子以及图书馆本身。要玩，请按照说明进行操作 [自述文件](https://github.com/Kotlin/kotlinx.coroutines/blob/master/README.md) 。
## 键入别名

在Kotlin 1.1中我们可以写

{% raw %}
<p></p>
{% endraw %}

```kotlin
typealias Action<T> = (T) -> Unit
 
```

{% raw %}
<p></p>
{% endraw %}

这意味着我们可以与`（T） - >互换使用`Action＆lt; T＆gt;`单位`，即它是真实的<strong>别名</strong>。类型别名可用于缩写代码中多个位置使用的较长类型：

* 具有复杂签名的函数类型：UserAction =（用户，上下文） - > ActionResponse，
* 复杂的通用类型：Multimap <K，V> = Map <K，List <V >>

预期您的问题：此功能不涵盖别名类型不能分配给原始类型（类似于Haskell中的新的类型）的用例：例如如果我们试图实施测量单位说

{% raw %}
<p></p>
{% endraw %}

```kotlin
typealias Length = Double
typealias Weight = Double
 
```

{% raw %}
<p></p>
{% endraw %}

它不会让我们做得很好，因为`Length`可以自由分配给`Weight`，反之亦然。实际上，它们都可以被分配给一个常规的`Double`。我们了解这种用例的重要性，并计划在未来对其进行覆盖，最有可能通过<em>价值类</em>，但这是另一个故事。现在我们只有类型别名。
阅读更多和评论 [这里](https://github.com/Kotlin/KEEP/issues/4) 。
## 绑定的可引用引用

在Kotlin 1.0中，可以获得对这样的函数（或属性）的引用：`String :: length`，即使用包含类的名称。在1.1中，我们添加了<em>绑定引用</em>：即我们可以说`mystr :: length`其中`mystr`是一个变量表达）。这样的引用被绑定到它们的接收者，因此是部分功能应用的特殊情况（在一般情况下，至少现在我们不支持）。
阅读更多和评论 [这里](https://github.com/Kotlin/KEEP/issues/5) 。
## 本地委托属性和内联属性

委托的属性已被证明是一个非常有用的抽象，现在我们允许它们在函数/代码块中。例如，我们可以说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example(foo: (Bar) -> Foo, bar: Bar) {
    val memoizedFoo by lazy { foo(bar) }
 
    // use memoizedFoo instead of foo to get it computed at most once
    if (someCondition && memoizedFoo.isValid()) {
        memoizedFoo.doSomething()
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

DSL和脚本也将受益于此功能。
阅读更多和评论 [这里](https://github.com/Kotlin/KEEP/issues/25) 。
我们也允许 [内联属性访问器](https://github.com/Kotlin/KEEP/issues/34) 现在。
## 密封类和数据类的放松规则

我们现在解除对数据类和密封类的限制。
数据类现在可以从其他类继承。请注意，自动生成的方法可能会覆盖超类中定义的方法！
对于密封类，我们扩大了可以定义其继承者的范围：在只有密封类本身之前，现在它在同一文件中的任何位置。
阅读更多和评论 [这里](https://github.com/Kotlin/KEEP/issues/31) 和 [这里](https://github.com/Kotlin/KEEP/issues/31) 。
## 脚本

您可能听说过，我们很快就可以在Kotlin中编写Gradle构建脚本，这将大大提高IDE编辑脚本的体验，并通过静态类型检查使其更可靠。这个项目促使我们更多地在Kotlin脚本上进行工作：我们正在开发基础架构，以便在不同工具的上下文中使用Kotln脚本，以及简单的命令行支持。
更多细节在 [提案](https://github.com/Kotlin/KEEP/issues/28) 。
## Java 7/8支持

我们正在努力改进对Java 8：1.1的支持，解决了我们以前使用的Stream API（并减少了支持库）的问题，并增加了在Kotlin接口中生成默认方法的支持，以便Java客户端可以实现它们无缝地阅读和评论 [这里](https://github.com/Kotlin/KEEP/issues/30) 。
要启用版本8类文件的生成，请提供`-jvm-target 1.8`命令行开关。
我们还在标准库中添加新功能，并且依靠Java API版本比1.6更新，我们引入了新的工件：`kotlin-stdlib-jre7`和`kotlin-stdlib-jre8 < / code>具有额外的功能，如`AutoCloseable.use（）`，Regex命名组支持和与流相关的功能。如果您需要他们添加的API，请从Maven / Gradle构建中使用这些工件而不是`kotlin-stdlib`。
阅读并讨论有关stdlib的提案 [这里](https://github.com/Kotlin/KEEP/labels/stdlib) 。
## JavaScript

我们正在积极研究JavaScript后端：1.0中提供的所有语言功能都已覆盖，我们将接近将JavaScript（运行时）模块系统集成到图片中。请注意，Kotlin 1.0.X中也提供了所有这些功能。
查找与JavaScript相关的提案 [这里](https://github.com/Kotlin/KEEP/labels/JS) 。
## 贡献者

我们非常感谢GitHub用户 [dotlin](https://github.com/dotlin) ， [Valdemar0204](https://github.com/Valdemar0204) ， [ensirius](https://github.com/ensirius) 和 [地理位置](https://github.com/geoand) 为他们对这个版本的贡献！
## 如何尝试

<strong>在Maven / Gradle </strong>中。加 [http://dl.bintray.com/kotlin/kotlin-eap-1.1](https://bintray.com/kotlin/kotlin-eap-1.1) （请参阅<em>“设置我！”</em>下的说明）作为项目的存储库。使用版本1.1-M01作为您的Kotlin文物。
<strong>在IDE </strong>中。如果你正在运行 [Kotlin 1.0.3](https://blog.jetbrains.com/kotlin/2016/06/kotlin-1-0-3-is-here/) ，请转到<em>工具→Kotlin→配置Kotlin插件更新</em>，然后在更新频道下拉列表中选择“Early Access Preview 1.1”

{% raw %}
<p><img alt="Configure-Plugin-Updates" class="aligncenter size-small wp-image-4085" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/07/Configure-Plugin-Updates.png?w=400&amp;ssl=1"/></p>
{% endraw %}

在同一对话框中按<em>检查更新</em>，当新版本显示时，<em>安装</em>。
<strong> <a href="http://try.kotlinlang.org/"> try.kotlinlang.org </a> </strong>。使用右下角的下拉列表更改编译器版本：<br/>
“img alt =”屏幕截图2016-07-14在20.23.48“class =”alignnone size-full wp-image-4121“data-recalc-dims =”1“src =”https：//i0.wp。 com / blog.jetbrains.com / kotlin / files / 2016/07 / Screen-Shot-2016-07-14-at-20.23.48.png？resize = 640％2C549＆amp; ssl = 1“/>
<strong>使用SDKMan </strong>。运行`sdk install kotlin 1.1-M01`。
您的反馈非常受欢迎，一如既往。
### 有一个漂亮的Kotlin！

