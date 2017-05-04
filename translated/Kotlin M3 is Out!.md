---
title: "[译]Kotlin M3 is Out!"
date: 2012-09-20 15:03:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/
translator:
translator_url:
---

上次我写了一个新的令人兴奋的 [特征](http://blog.jetbrains.com/kotlin/2012/09/how-do-you-traverse-a-map/) 在“即将到来的KotlinM3”。今天，Kotlin M3不是“即将到来”，就在这里。这篇文章概述了新的里程碑。<span id =“more-663”> </span>
我们重新设计了**<a href="http://kotlin.jetbrains.org"> kotlin.jetbrains.org </a>。**目前，此页面的链接指向我们wiki中熟悉的文档，但随着时间的推移，这也会有所改善。
## 改进和错误修复

许多 [我们关闭了近400个问题](http://youtrack.jetbrains.com/issues/KT?q=%23Kotlin+%23Resolved+resolved+date%3A+2012-07-11+..+2012-09-20) 在这个里程碑是bug修复和小的增强，使Kotlin更整洁和更亮。在**类型参数推论**算法中已经取得了巨大的进步。还没完成，但已经相当好了。
在M3中，我们开始剖析IDE并调整IDE的性能**以及编译器。这将是很多工作，但最终一切都会快速消耗很少的记忆。这次大部分改进与代码完成有关。
## 多重分配和数据类

这覆盖了 [上周入场](http://blog.jetbrains.com/kotlin/2012/09/how-do-you-traverse-a-map/) 。长篇小说，你可以写这样的东西：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val map = hashMap("one" to 1, "two" to 2, "three" to 3)
for ((k, v) in map) {
    println("$k -> $v")
}
```

{% raw %}
<p></p>
{% endraw %}

并定义**数据**类：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Point(val x: Int, val y: Int)
```

{% raw %}
<p></p>
{% endraw %}

这里Point自动获取toString（），equals（）/ hashCode（）和*组件函数*，使您能够写入：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (x, y) = functionReturningPoint()
```

{% raw %}
<p></p>
{% endraw %}

看到更多的 [上述职位](http://blog.jetbrains.com/kotlin/2012/09/how-do-you-traverse-a-map/) 。
这些功能使我们能够**不推荐使用元组**。他们将在下一个里程碑中被完全删除，你可以 [自动迁移代码](http://blog.jetbrains.com/kotlin/migrating-tuples/) 使用IDE插件。

{% raw %}
<p><a name="Collections"></a></p>
{% endraw %}

## 集合

静态JVM语言倾向于提出自己的集合库，因为Java集合不会使用这些语言的酷功能。所以我们得到非常酷的集合，不幸的是，不兼容的*，这使得我们在使用Java API时封装它们或复制。
Kotlin有很多奇特的功能，但是我们渴望与Java平滑地进行互操作，事实证明，我们也可以吃这个蛋糕。认识Kotlin的系列：
<img alt =“”class =“aligncenter size-full wp-image-665”data-recalc-dims =“1”sizes =“（max-width：723px）100vw，723px”src =“https：// i0 .wp.com / blog.jetbrains.com / kotlin / files / 2012/09 / Collections.png？resize = 640％2C335＆amp; ssl = 1“srcset =”https://i0.wp.com/blog.jetbrains。 com / kotlin / files / 2012/09 / Collections.png？resize = 300％2C157＆amp; ssl = 1 300w，https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/09/Collections .png？w = 723＆amp; ssl = 1 723w“/>正如你所看到的，这里的基本结构非常像**java.util**给我们，但有一些重要的区别：

* 存在区分可变集和只读集合的​​特征（“接口”）。
* 只读特征（如List或Set）是共变的（即可以将List <String>分配给List <Any>）。

好的旧的**java.util.ArrayList**仍然存在，但是Kotlin看起来像是继承自Kotlin的MutableList，后者又继承了List。这样，您可以获得集合的兼容性和良好的类型属性，例如能够传递List <String>，其中List <Any>是预期的。
**注意**，因为旧名称（如列表或集合）现在意味着不同，您的一些代码将会中断。对于一个快速而肮脏的解决方案，您可以将所有列表更改为MutableLists等等，但是如果大部分数据都是只读的，则会更好。
**另请注意**：如果您的旧代码导入了类似**java.util.Collection**的内容，那么您将收到关于此导入的警告，并需要将其删除。
## 外部注释

Kotlin通过整合使您的程序更安全 [零安全](http://confluence.jetbrains.net/display/Kotlin/Null-safety) 进入类型系统。由于Java不太在意这一点，我们需要通过断言Java返回的东西不使用'!!'运算符来保护它。

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (file.getName()!!.endsWith(extension)) {...}
```

{% raw %}
<p></p>
{% endraw %}

（BTW，好的旧的sure（）函数已经从库中删除，你可以 [自动迁移代码](http://blog.jetbrains.com/kotlin/migrating-sure/) 。）
许多Java方法从不实际返回null。人们使用注释来让 [工具](http://www.jetbrains.com/idea/documentation/howto.html) 知道它，但是如果我使用第三方库呢？
在Kotlin M3中，我们支持**外部注释**：即使您不控制其源代码，您也可以对其进行注释。这样做很容易 [在IDE中](http://blog.jetbrains.com/kotlin/using-external-annotations/) 。
我们将创建一个自动化工具，从而强调**来自库代码的注释。在此之前，我们使用IDE手动添加注释。
## 本地功能和类

除了本地功能，Kotlin M3支持本地类和对象声明：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() {
  class Bar {...}
  val bars = ArrayList<Bar>()
  // ...
}
```

{% raw %}
<p></p>
{% endraw %}

请注意，要创建本地数据类，需要用方括号括起“数据”注释：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() {
    [data] class Data(...)
    // ...
}
```

{% raw %}
<p></p>
{% endraw %}

## Java互操作性：枚举和注释

支持Kotlin的注释已大大改善。除此之外，Kotlin的注释现在与Java注释完全兼容，可以在注释参数列表中使用枚举常量等等。
枚举现在也好多了：它们支持valueOf（），name（）和ordinal（），并且可以很好地与Java一起使用。
## REPL /脚本

我们在Kotlin的支持脚本方面做了一些工作。脚本支持相当初步，但您可以运行这样的操作：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// tree.ktscript
import java.io.File
 
fun tree(dir: File, indent: String) {
    val files = dir.listFiles()!!
    for (file in files) {
        println(indent + file!!.getName())
        if (file.isDirectory()) {
            tree(file, indent + "  ")
        }
    }
}
 
tree(File("."), "")
```

{% raw %}
<p></p>
{% endraw %}

通过从命令行调用它：

{% raw %}
<p></p>
{% endraw %}

```kotlin
$ kotlinc/bin/kotlinc-jvm -script tree.ktscript
foo
  bar.txt
tree.ktscript
```

{% raw %}
<p></p>
{% endraw %}

“ [Shebang](http://en.wikipedia.org/wiki/Shebang_(Unix)) “评论也受到支持。
脚本使我们足够接近 [REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) ，但我们还没有。请用 [网络演示](http://kotlin-demo.jetbrains.com) 代替。
## 有一个尼斯Kotlin！

新插件需要IntelliJ IDEA **12**，可以使用 [EAP构建](http://eap.jetbrains.com/idea) （此版本的IntelliJ IDEA尚未发布，有问题，例如 [这个问题与Android](http://youtrack.jetbrains.com/issue/KT-2763) ）。并且不要忘记更新你的kotlin-runitme.jar（IDE会提供你这样做）！
像往常一样，您的**反馈非常受欢迎**！
