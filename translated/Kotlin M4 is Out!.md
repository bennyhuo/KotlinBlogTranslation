---
title: [译]Kotlin M4 is Out!
date: 2012-12-11 09:15:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/12/kotlin-m4-is-out/
---

今天我们推出Kotlin M4（从下雪）。这篇文章概述了这个里程碑带来的新功能和其他内容。
# 这里和那里的改进

Kotlin M4是JDK7友好的：我们仍然生成兼容Java6的字节码，但是与JDK7编译有关的一些问题现在已经修复了。
类型参数推论已经进一步改进，现在更快，加速更多。
代码完成也在许多方面得到了改进。请享用
总的来说，自从M3.1出来以来，已经关闭了128个问题。
# KAnnotator：注释世界

由于M3，您可以使用外部注释来告诉系统您的方法返回/取非空值。即使不使用Kotlin，这种机制也是有用的：你也可以启用Java的可空性检查（我完全建议你这么做）。
关于这个的一个问题曾经是这样的，虽然你可以在编写自己的代码时注释自己的代码（我们一直在JetBrains这样做），但是你最喜爱的库没有注释，它是如此之大，你不能注释它手动。
这里的关键是“手动”。程序员是一个懒惰的生物，凭借我们的懒惰，我们希望尽可能自动化。而今天，与Kotlin M4一起，我们推出了KAnnotator：一种自动注释库的工具（当然这个工具写在Kotlin中）。
简单来说，它的工作原理是：将你的库作为一个jar（或一些jar），你告诉KAnnotator来推断这些jar的注释，然后再回收一堆.xml文件。它们包含方法和字段的注释，例如：
现在，您可以将这些注释附加到项目中，Java IDE和Kotlin编译器都将看到它们。
KAnnotator刚刚开始，它会变得更加智能，但是今天我们已经有了一个完整的JDK注释，可以在新的Kotlin插件中使用。一旦您在编辑器中打开任何Kotlin文件，它将建议将它们添加到您的JDK中：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png"><img alt="" class="aligncenter size-full wp-image-742" data-recalc-dims="1" sizes="(max-width: 610px) 100vw, 610px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?resize=610%2C53&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?resize=300%2C26&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?w=610&amp;ssl=1 610w"/></a></p>
{% endraw %}

# 复制您的数据

Kotlin M3引入了数据类，这是一种很好的方式来表示你的数据。一个受欢迎的请求是能够复制数据类的实例，并选择性地更改其某些属性，同时保持对象不可变。
在Kotlin M4你可以这样做：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Person(val firstName: String, val lastName: String)
 
fun Person.asMarried(newLastName: String)
         = this.copy(lastName = newLastName)
```

{% raw %}
<p></p>
{% endraw %}

每个数据类获取一个具有所有参数的默认值的copy（）函数，以便您只能指定要更改的那些参数。由于Kotlin支持命名参数，所有您需要做的就是'copy（property1 = v1，property3 = v2）'，并且所有其他属性将被复制，而'property1'和'property3'将被更改。
# 声明站点方差... Java

这将有一个单独的职位，但我会在这里给出一个简短的公告。我们都知道Java让你写“List”？只要您不想修改该列表，就会扩展Foo>“。如你所知，Kotlin具有声明位置差异和集合的只读接口，因此'List <String>'可以到达'List <Object>'的地方。现在，当您在Kotlin中有此功能时：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun join(l: List<Any>, separator: String): String = ...
```

{% raw %}
<p></p>
{% endraw %}

你可以传递任何列表，但是如果你想从Java调用它呢？
在M4中，Kotlin为此功能生成以下Java签名：

{% raw %}
<p></p>
{% endraw %}

```kotlin
String join(List<? extends Object>, String separator)
```

{% raw %}
<p></p>
{% endraw %}

这使得甚至可以从Java代码传递一个字符串列表。
如果你永远不会得到这些通配符，那么现在就有一个答案：写一个简单的Kotlin并从Java中调用它
# 支持弃用

一些设计决策是好的，有些不是。有些人很好，当他们来了，但不是那么好了...我们需要能够废弃的东西。 Kotlin M4支持“已弃用”注释，与Java的@Deprecated不同，需要一个字符串参数，告诉您应该做什么，而不是使用此方法/类。
例如，在这个里程碑中，我们在标准库中弃用arrayList（...），hashSet（...）和其他这样的函数，因为我们发现它们令人困惑：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val c: List<Node> = node.getChildren()
ArrayList(c) // a copy of that list
arrayList(c) // a list containing that list, [c]
```

{% raw %}
<p></p>
{% endraw %}

一个字母的情况大大改变了意义。这就是为什么现在arrayList（）被弃用，并且新的arrayListOf（）可用。还有一个新的list（）函数，它也创建一个数组列表，但是通过只读引用返回它。所以现在arrayList（）的声明如下所示：
如果你在某个地方使用，呼叫站点会告诉你有什么问题，你应该做什么：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png"><img alt="" class="aligncenter size-full wp-image-745" data-recalc-dims="1" sizes="(max-width: 617px) 100vw, 617px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?resize=617%2C79&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?resize=300%2C38&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?w=617&amp;ssl=1 617w"/></a></p>
{% endraw %}

# IDE改进

在目录中运行所有测试。现在，IntelliJ IDEA可以发现在Kotlin中编写的测试，以便您可以在目录/包中运行所有测试：Java和Kotlin。
调试器包括扩展函数/属性的接收器的许多修复现在在“变量”视图中可见。
新制作程序。 IntelliJ IDEA 12带来了一个新的make的实现。 Kotlin M4增加了对它的支持，这种支持最终将发展成为Kotlin的增量编译器。
Kotlin Home Page现在具有统一的搜索框，可以汇总文档，论坛，跟踪器，源代码以及其他内容。

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png"><img alt="" class="aligncenter size-full wp-image-747" data-recalc-dims="1" sizes="(max-width: 690px) 100vw, 690px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png?resize=640%2C318&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png?resize=300%2C149&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png?w=690&amp;ssl=1 690w"/></a></p>
{% endraw %}

它每天暂时限制100次搜索，但这个限制将很快被删除。
# 诊断改进

用户提问这是正常的。当不同的用户一遍又一遍地问同一个问题时，有些人写了一个FAQ，但是我们更喜欢更好的方式：我们希望IDE帮助他们找出答案。一个例子是：

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (foo is List) { // ERROR!
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

编译器会抱怨List必须有一个类型参数“List <String>”。但是泛型被删除，我们不能检查是否有字符串列表，我们在运行时知道它是一个列表。编译器也知道：

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (foo is List<String>) { // ERROR: can't check!
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

所以用户被卡住：一个类型的参数不起作用，也没有参数也不起作用。这是IDE来救援的地方：
只需按下Alt + Enter就可以了解错误（因为我确信你总是这么做），并且得到它的修正：你需要一个'星标投影'在这里。
# 下载

Kotlin插件需要IntelliJ IDEA 12，它是几天前发布的，你可以在这里找到（开源社区版可用）。您可以从插件库中下载Kotlin M4，可从IDE访问。
您的反馈非常受欢迎。有一个漂亮的Kotlin！
