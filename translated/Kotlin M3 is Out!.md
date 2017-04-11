---
title: [译]Kotlin M3 is Out!
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
---

上一次我在“即将到来的科特林M3”中写了一个新的令人兴奋的功能。今天，Kotlin M3不是“即将到来”，就在这里。这篇文章概述了新的里程碑。
我们重新设计了kotlin.jetbrains.org。目前，这个页面的链接指向我们wiki中熟悉的文档，但这也将随着时间的推移而改善。
## 改进和错误修复

我们在这个里程碑中关闭的近400个问题中有许多是错误修复和小型增强功能，使Kotlin更加整洁，更加光滑。类型论证推理算法已经取得了巨大进步。还没完成，但已经相当好了。
在M3中，我们开始剖析事物并调整IDE的性能以及编译器。这将是很多工作，但最终一切都会快速消耗很少的记忆。这次大部分改进与代码完成有关。
## 多重分配和数据类

这在上周的报道中有所介绍。长篇小说，你可以写这样的东西：

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

并定义数据类，如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Point(val x: Int, val y: Int)
```

{% raw %}
<p></p>
{% endraw %}

这里Point自动获取toString（），equals（）/ hashCode（）和组件函数，使您能够写入：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (x, y) = functionReturningPoint()
```

{% raw %}
<p></p>
{% endraw %}

在上述帖子中查看更多。
这些功能使我们能够废弃元组。它们将在下一个里程碑中完全删除，您可以使用IDE插件自动迁移代码。

{% raw %}
<p><a name="Collections"></a></p>
{% endraw %}

## 集合

静态JVM语言倾向于提出自己的集合库，因为Java集合不会使用这些语言的酷功能。所以我们得到了很酷的集合，不幸的是，它们是不兼容的，这使得我们在使用Java API时封装它们或复制它们。
Kotlin有很多奇特的功能，但是我们渴望与Java平滑地进行互操作，事实证明，我们也可以吃这个蛋糕。认识Kotlin的系列：
正如你所看到的，这里的基本结构非常像java.util给我们的，但有一些重要的区别：

* 存在区分可变集和只读集合的​​特征（“接口”）。
* 只读特征（如List或Set）是共变的（即可以将List <String>分配给List <Any>）。

好的旧的java.util.ArrayList仍然存在，但是Kotlin看起来像是继承自Kotlin的MutableList，后者又继承了List。这样，您可以获得集合的兼容性和良好的类型属性，例如能够传递List <String>，其中List <Any>是预期的。
请注意，由于旧名称（如列表或集合）现在意味着不同，您的某些代码将会中断。对于一个快速而肮脏的解决方案，您可以将所有列表更改为MutableLists等等，但是如果大部分数据都是只读的，则会更好。
另请注意，如果您的旧代码导入了类似java.util.Collection的内容，那么您将收到有关此导入的警告，并需要将其删除。
## 外部注释

Kotlin通过将零安全引入类型系统来使您的程序更安全。由于Java不太在意这一点，我们需要通过断言Java返回的东西不使用'!!'运算符来保护它。

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (file.getName()!!.endsWith(extension)) {...}
```

{% raw %}
<p></p>
{% endraw %}

（BTW，好的旧的sure（）函数已经从库中删除，您可以自动迁移代码。）
许多Java方法从不实际返回null。人们使用注释来让工具知道它，但是如果我使用第三方库呢？
在Kotlin M3中，我们支持外部注释：即使不控制源代码，也可以注释事物。这在IDE中很容易完成。
我们将创建一个自动化工具，从而推断出库代码中的注释。在此之前，我们使用IDE手动添加注释。
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

“Shebang”评论也受到支持。
脚本使我们足够接近有一个REPL，但是我们还没有。请使用网络演示。
## 有一个尼斯科特林！

新的插件需要IntelliJ IDEA 12，它可以作为EAP版本（此版本的IntelliJ IDEA尚未发布，有问题，例如Android的这个问题）。并且不要忘记更新你的kotlin-runitme.jar（IDE会提供你这样做）！
像往常一样，您的反馈非常受欢迎！
