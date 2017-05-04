---
title: "[译]Kotlin M4 is Out!"
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
translator:
translator_url:
---

今天我们推出了Kotlin M4（从下） [雪](http://www.google.ru/imgres?um=1&hl=en&newwindow=1&sa=N&tbo=d&biw=1320&bih=1106&tbm=isch&tbnid=q5-uJPbVI3jRFM:&imgrefurl=http://mr-stroy.com/news/498/45&docid=hUulWRZZmtitkM&imgurl=http://mr-stroy.com/uploads/images/sneg-spb.jpg&w=784&h=500&ei=sG28UMayC4nZ4QT22IDYCw&zoom=1&iact=hc&vpx=4&vpy=288&dur=1347&hovh=179&hovw=281&tx=179&ty=150&sig=101271244132511519226&page=1&tbnh=139&tbnw=206&start=0&ndsp=36&ved=1t:429,r:6,s:0,i:102) ）。这篇文章概述了这个里程碑带来的新功能和其他内容。<span id =“more-731”> </span>
# 这里和那里的改进

Kotlin M4是**JDK7友好**：我们仍然生成兼容Java6的字节码，但是与JDK7编译相关的一些问题现在已经修复了。
**类型参数推断**已经进一步改进，现在**更快**，更多的加速即将到来。
**代码完成**也在许多方面得到改进。享受<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/ images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“
总体而言 [128个问题](http://youtrack.jetbrains.com/issues/KT?p=0&q=%23Resolved+resolved+date%3A+2012-10-11+..+2012-12-01&f=false) 关闭以来 [M3.1](http://blog.jetbrains.com/kotlin/2012/10/dogfooding-kotlin-and-m3-1/) 不在。
# KAnnotator：注释世界

以来 [M3](http://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/) ， 您可以使用 [外部注释](http://blog.jetbrains.com/kotlin/using-external-annotations/) 告诉系统你的方法返回/取非空值。即使不使用Kotlin，这种机制也是有用的：你可以打开 [Java的可空性检查](http://www.jetbrains.com/idea/documentation/howto.html) （我完全建议你这样做）。
关于这个的一个问题曾经是这样，虽然你可以在编写自己的代码时注释它（我们这样做） [所有](https://github.com/JetBrains/kotlin/blob/master/compiler/frontend/src/org/jetbrains/jet/lang/types/TypeConstructor.java) [的](https://github.com/JetBrains/intellij-community/blob/master/platform/util/src/com/intellij/util/text/CharArrayUtil.java) [时间](https://github.com/JetBrains/la-clojure/blob/master/src/org/jetbrains/plugins/clojure/utils/ClojureUtils.java) 在JetBrains），您最喜欢的库没有注释，它是如此之大，您不能手动注释。
这里的关键是“手动”。程序员是一个懒惰的生物，凭借我们的懒惰，我们希望尽可能自动化。而今天，与Kotlin M4一起，我们推出了**KAnnotator**：一种**自动注释库的工具**（该工具当然是用Kotlin编写的）。
简单来说，你的库是一个罐子（或者是一些罐子），你告诉KAnnotator来推断这些jar的注释，然后再收回一堆.xml文件。它们包含方法和字段的注释，例如：
<img alt =“”class =“aligncenter size-full wp-image-740”data-recalc-dims =“1”sizes =“（max-width：409px）100vw，409px”src =“https：// i0 .wp.com / blog.jetbrains.com / kotlin / files / 2012/12 / annotations.xml_.png？resize = 409％2C149＆amp; ssl = 1“srcset =”https://i0.wp.com/blog。 jetbrains.com/kotlin/files/2012/12/annotations.xml_.png?resize=300%2C109&amp;ssl=1 300w，https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012 /12/annotations.xml_.png?w=409&amp;ssl=1 409w“/>现在，您可以将这些注释附加到项目中，而Java IDE和Kotlin编译器都将看到它们。
KAnnotator刚刚开始**，它会变得更加聪明，但是今天我们已经有了一个完整的JDK注释，可以在新的Kotlin插件中使用。一旦您在编辑器中打开任何Kotlin文件，它将建议将它们添加到您的JDK中：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png"><img alt="" class="aligncenter size-full wp-image-742" data-recalc-dims="1" sizes="(max-width: 610px) 100vw, 610px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?resize=610%2C53&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?resize=300%2C26&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?w=610&amp;ssl=1 610w"/></a></p>
{% endraw %}

# 复制您的数据

Kotlin M3推出 [数据类](http://blog.jetbrains.com/kotlin/2012/09/how-do-you-traverse-a-map/) 一个很好的方式来表示你的数据。一个受欢迎的要求是能够复制数据类的实例，并有选择地**更改**某些属性**，同时保持对象不可变**。
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

每个数据类都获取一个copy（）函数，所有参数都有*默认值*，以便您只能指定要更改的那些。由于Kotlin支持*命名参数*，所有你需要做的就是'copy（property1 = v1，property3 = v2）'，所有的其他属性将被复制，而'property1'和'property3'将会改变
# 声明站点方差... Java

这将有一个单独的职位，但我会在这里给出一个简短的公告。我们都知道Java让你写“List”？扩展Foo>' [每当你不意味着修改该列表](http://www.eecs.qmul.ac.uk/~mmh/APD/bloch/generics.pdf) 。当你 [知道](http://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/) ，Kotlin具有用于集合的声明位置方差和只读接口，因此'List <String>'可以转到'List <Object>'的位置。现在，当您在Kotlin中有此功能时：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun join(l: List<Any>, separator: String): String = ...
```

{% raw %}
<p></p>
{% endraw %}

您可以传递任何列表，但如果您想从Java**将其称为**呢？
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

这使得它可以传递一个字符串列表**甚至从Java代码**。
如果你永远不会得到这些通配符，那么现在有一个答案：写出简单的Kotlin并从Java中调用它<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https ：//i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height： 1em;“/>
# 支持弃用

一些设计决策是好的，有些不是。有些人很好，当他们来了，但不是那么好...我们需要能够**弃用**的东西。 Kotlin M4支持“已弃用”注释，与Java的@Deprecated不同，**需要**一个字符串参数，告诉您应该使用该方法而不是使用此方法/类。
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
<img alt =“”class =“aligncenter size-full wp-image-773”data-recalc-dims =“1”sizes =“（max-width：564px）100vw，564px”src =“https：// i1 .wp.com / blog.jetbrains.com / kotlin / files / 2012/12 / arrayList-1.png？resize = 564％2C42＆amp; ssl = 1“srcset =”https://i1.wp.com/blog。 jetbrains.com/kotlin/files/2012/12/arrayList-1.png?resize=300%2C22&amp;ssl=1 300w，https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012 /12/arrayList-1.png?w=564&amp;ssl=1 564w“/> <br/>
如果你在某个地方使用，呼叫站点会告诉你有什么问题，你应该做什么：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png"><img alt="" class="aligncenter size-full wp-image-745" data-recalc-dims="1" sizes="(max-width: 617px) 100vw, 617px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?resize=617%2C79&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?resize=300%2C38&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?w=617&amp;ssl=1 617w"/></a></p>
{% endraw %}

# IDE改进

**在目录中运行所有测试。**现在，IntelliJ IDEA可以发现在Kotlin中编写的测试，以便您可以在目录/包中运行所有测试：Java和Kotlin。
**调试器。**现在可以在“变量”视图中看到包括扩展函数/属性的接收器在内的许多修复。
**新的制作过程。** IntelliJ IDEA 12带来了一个新的make的实现。 Kotlin M4增加了对它的支持，这种支持最终将发展成为Kotlin的**增量编译器**。
Kotlin主页**现在具有统一的搜索框，可以汇总文档，论坛，跟踪器，源代码以及whatnot。

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

编译器会抱怨List必须有一个类型参数“List <String>”。但是泛型被删除，我们不能检查某些东西是字符串*的列表，所有我们在运行时知道的是它是一个列表。编译器也知道：

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
<img alt =“”class =“aligncenter size-full wp-image-746”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files /2012/12/QuickFix.png?resize=190%2C96&amp;ssl=1"/>只需按Alt + Enter就可以出现错误（因为，我相信你总是这样做），并得到它的修正：你需要一个'明星投影“在这里。
# 下载

Kotlin插件需要IntelliJ IDEA 12，它是在几天前发布的，你可以得到它 [这里](http://www.jetbrains.com/idea/download/index.html) （**开源**社区版可用）。您可以从插件库中下载**Kotlin M4** [可从IDE访问](http://www.jetbrains.com/idea/plugins/index.html) 。
您的反馈非常受欢迎。 **拥有不错的Kotlin！**
