---
title: "[译]DSLs in Kotlin: Part 1. What’s in the toolbox + Builders"
date: 2011-10-04 13:17:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/10/dsls-in-kotlin-part-1-whats-in-the-toolbox-builders/
translator:
translator_url:
---

如果您有一个非常好的</em> API，那么现在将它叫做“内部DSL”就是时尚，因为使用这样的API的代码几乎就像一种语言中的语言的选择。 [流畅的界面](http://martinfowler.com/bliki/FluentInterface.html) 作为最受欢迎的例子之一。
许多现代语言为创建内部DSLs提供了一些先进的方法，而Kotlin在这里也不例外。在这篇文章中，我将简要列出对此有用的功能
<span id =“more-181”> </span>
我们开始吧 [扩展功能](http://confluence.jetbrains.net/display/Kotlin/Extension+functions) 。我们都熟悉Java的实用工具类，如java.util.Collections等。这些类是一组静态方法的简单容器，这些静态方法旨在与这样的类一起使用。所以我们最终编写如下代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
Collection.sort(list);
int index = Collections.binarySearch(list, x);
```

{% raw %}
<p></p>
{% endraw %}

这看起来不是很漂亮。静态导入使它更漂亮，但它们并不能解决一个重要的可发现性问题</em>：我们都使用IDE编写完整的代码完成功能来浏览API：
<img alt =“IDEA中的代码完成”class =“alignnone size-full wp-image-220”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com /kotlin/files/2011/09/Screen-shot-2011-10-04-at-15.42.18-.png?resize=582%2C143&amp;ssl=1“/>
发现这些效用函数也不是很酷吗？因此，即使foo（）不是a的类的成员，所以我们以“a.foo（）”的形式调用<em>扩展函数</em>。例如，集合中的这些效用函数可以定义为扩展函数，如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
list.sort();
val index = list.binarySearch(x);
```

{% raw %}
<p></p>
{% endraw %}

这些仍然是静态调度的实用程序函数，即编译器发出的字节码与Java相同，但语法更好，代码完成工作。请注意，与成员不同，扩展函数不能在子类中被覆盖，即List的某些特殊实现无法覆盖sort（）以提高效率。
要定义扩展功能，我们只需将接收器类型放在其名称前面：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T : Comparable<T>> List<T>.sort() {
  Collections.sort(this)
}
```

{% raw %}
<p></p>
{% endraw %}

请注意，我可以使用代表我的接收者对象的“this”引用。查看更多 [这里](http://confluence.jetbrains.net/display/Kotlin/Extension+functions) 。
现在，扩展功能给我们带来了什么，DSL创作者？首先你可以将任何界面变成流畅的界面。例如，让我们用一个给定的字符集创建一个新的缓冲阅读器：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val reader = FileInputStream("mytext.txt").buffered().reader("utf-8")
```

{% raw %}
<p></p>
{% endraw %}

这是我写的一个特殊的课程，能够得到这个吗？不，这只有两个功能：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun InputStream.buffered() = BufferedInputStream(this)
fun InputStream.reader(charset : String) = InputStreamReader(this, charset)
```

{% raw %}
<p></p>
{% endraw %}

然后，他们一起玩得很好 [操作员重载](http://confluence.jetbrains.net/display/Kotlin/Operator+overloading) ：在Kotlin中，大多数运算符，如加号，减号等，都按惯例编译为命名函数调用。例如，当我说“a + b”时，Kotlin读取“a.plus（b）”（见我们的更多内容） [文件](http://confluence.jetbrains.net/display/Kotlin/Operator+overloading) ）。这意味着通过在我的类型中添加一个名为“plus”的扩展函数，我可以使用二进制'+'。例如，我可以使自己的'+'用于列表连接：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun  List.plus(other : List) : List {
  val result = ArrayList(this)
  result.addAll(other)  
  return result
}
```

{% raw %}
<p></p>
{% endraw %}

并称之为：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val l1 = list(1, 2, 3)
val l2 = list(4, 5, 6)
val l3 = l1 + l2 // a new list of length 6 is created
```

{% raw %}
<p></p>
{% endraw %}

还有更多：由于索引编译到调用get（）和set（）函数，我们可以有漂亮的子列表（或“片”），如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val sublist = list[a..b]
```

{% raw %}
<p></p>
{% endraw %}

通过在列表上定义扩展函数get（）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> List<T>.get(range : IntRange<Int>) : List<T>
    = subList(range.start, range.end)
```

{% raw %}
<p></p>
{% endraw %} [Infix函数调用](http://confluence.jetbrains.net/display/Kotlin/Functions#Functions-Infixcalls) 加上更多的，因为你可以说，例如

{% raw %}
<p></p>
{% endraw %}

```kotlin
it hasPrivilege WRITE
```

{% raw %}
<p></p>
{% endraw %}

代替

{% raw %}
<p></p>
{% endraw %}

```kotlin
it.hasPrivilege(WRITE)
```

{% raw %}
<p></p>
{% endraw %}

而且，当然，你会有很多乐趣 [高阶函数](http://confluence.jetbrains.net/display/Kotlin/Functions#Functions-Higherorderfunctions) 和 [功能文字（即“封闭”）](http://confluence.jetbrains.net/display/Kotlin/Function+literals) 。例如，请查看：

{% raw %}
<p></p>
{% endraw %}

```kotlin
lock (myLock) {
  // Do something
}
```

{% raw %}
<p></p>
{% endraw %}

这是一个内置的构造，如Java的**同步**部分？不，这是一个函数调用。它使用非常方便的约定：您可以将最后一个函数文字</em>传递到您的参数列表周围的括号之外。所以这个电话与“lock（myLock，{...}”）相同，但看起来更漂亮。
有关这个例子的更多信息可以找到 [这里](http://confluence.jetbrains.net/display/Kotlin/Functions#Functions-Inlinefunctions) 。
还有一个很好的约会，使得非常接近LINQ的东西可能：

{% raw %}
<p></p>
{% endraw %}

```kotlin
users
   .filter { it hasPrivilege WRITE }
   .map { it => it.fullName }
   .orderBy { lastName }
```

{% raw %}
<p></p>
{% endraw %}

约定是：如果期望只有一个参数的函数，则可以省略参数声明，并使用默认名称“it”。即“filter {it.foo（）}”与“filter {it => it.foo（）}”相同。
最后，如果我们把所有这些（和一点点更多）放在一起，我们可以得到一些非常好的东西。看这个代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
html {
   head {
     title { +"XML encoding with Kotlin" }
   }
   body {
     h1 { +"XML encoding with Kotlin" }
     p { +"this format is now type-safe" }

     /* an element with attributes and text content */
     a(href="http://jetbrains.com/kotlin") { +"Kotlin" }
   }
}
```

{% raw %}
<p></p>
{% endraw %}

是Groovy吗不，这是Kotlin，与Groovy不同，它是静态打字的。是的，我们可以像Groovy这样的建设者，但是更好。 <img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images /smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>我将这个例子的详细解释添加到我们的wiki中;你可以找到它 [这里](http://confluence.jetbrains.net/display/Kotlin/Type-safe+Groovy-style+builders) 。
有一个问题？意见？建议？我们非常感谢您的意见！
