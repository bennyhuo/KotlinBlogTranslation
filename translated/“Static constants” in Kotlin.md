---
title: "[译]“Static constants” in Kotlin"
date: 2013-06-24 12:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/06/static-constants-in-kotlin/
---

Kotlin被设计成在课堂上没有一个“静态成员”这样的东西。如果你在一个类中有一个函数，它只能在这个类的实例上被调用。如果你需要一些不附加到任何类的实例的东西，你可以在一个包中定义它，在任何类之外（我们称之为package-level functions）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo
 
fun bar() {}
```

{% raw %}
<p></p>
{% endraw %}

但有时您需要在您的课堂中使用<strong>静态常量</ strong>：例如，要符合某些框架的要求或使用序列化。你怎么在Kotlin这样做？ <span id =“more-1101”> </ span> Kotlin中有两件类似于Java的静态：上述的包级别函数和 [类对象](http://confluence.jetbrains.com/display/Kotlin/Classes+and+Inheritance#ClassesandInheritance-Classobjects) 。我将简要解释什么是类对象，然后继续执行静态常量。
## 类对象

一个班（不 [内](http://confluence.jetbrains.com/display/Kotlin/Nested+classes) 而不是本地的）或trait最多可以声明一个与其相关联的类对象。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
  class object {
    val bar = 1
  }
 
  val baz = 2
}
```

{% raw %}
<p></p>
{% endraw %}

这里我们有一个类Foo，它声明一个类对象，它又有一个成员属性栏。这意味着我们可以直接在类名上调用bar（就像在Java中）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(Foo.bar)
```

{% raw %}
<p></p>
{% endraw %}

请注意，我们无法在Foo的<em>实例</ em>上调用bar：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val foo = Foo()
println(foo.bar) // compilation error
```

{% raw %}
<p></p>
{% endraw %}

那是因为吧不是Foo的成员，只是它的类对象。类对象是与该类相关联的单独实体<em> </ em>，并且不与其实例共享成员。我们也不能在班级名称上加上baz：

{% raw %}
<p></p>
{% endraw %}

```kotlin
prinltn(Foo.baz) // error
```

{% raw %}
<p></p>
{% endraw %}

这是因为baz是Foo的成员，不是它的类对象，所以你只能在Foo的<em>实例</ em>上调用baz。
现在，我们来看看类对象的工作原理。首先，为类对象生成一个单独的JVM类，bar是该类的成员。如果你从Java访问类对象，你必须这样说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
/* Java */
Foo.object$.getBar()
```

{% raw %}
<p></p>
{% endraw %}

Class对象是存储在它定义的类中的静态字段中的一个实例，其属性使用getter / setter访问。
## 静态常量

类对象中的属性与静态字段（甚至更好）相同，但仅在Kotlin中。如上所述，对于Java，它看起来是不同的，如果一些框架或约定（在Java中）要求您具有真正的静态字段，这可能会导致问题。
<strong>免责声明</ strong>：在Kotlin M5.3中，您的课堂中没有一个静态字段。它最近实施了，所以你只有在它 [最新的夜间建设](http://confluence.jetbrains.com/display/Kotlin/Getting+Started#GettingStarted-UsingtheKotlinnightlybuilds) 。
当您在类对象中定义公共或内部属性，并且不指定自定义getter和setter时，Kotlin会自动将其直接存储在封闭类中，以便在Java中可以说

{% raw %}
<p></p>
{% endraw %}

```kotlin
System.out.println(Foo.bar);
```

{% raw %}
<p></p>
{% endraw %}

您的Kotlin代码没有任何区别：一切都应该如此。即使在Java中，老式的Foo.object $ .getBar（），但是现在你也可以在你的类中有真正的静态常量。
请享用。
