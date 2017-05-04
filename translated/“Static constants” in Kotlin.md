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
translator: SnakEys
translator_url:
---

“静态成员(static member)” 没有包含在 Kotlin 类的设计中，假设在类中有一个函数，那么该函数只能通过这个类的实例调用。而如果函数与任何类的实例并没有关联，那么就可以在类之外、包级进行定义（我们称之为包级函数 --package-level functions）：

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

然而有时仍需要在类中使用**静态常量**：例如，要符合某些框架的要求或使用序列化，那么在 kotlin 中应该如何实现？Kotlin 中有两种类似于 Java 的静态概念：上述的包级别函数以及[类对象](http://confluence.jetbrains.com/display/Kotlin/Classes+and+Inheritance#ClassesandInheritance-Classobjects) 。下面将简要解释类对象，然后继续讨论静态常量。

## 类对象

一个类(非[inner](http://confluence.jetbrains.com/display/Kotlin/Nested+classes)且非局部)或属性最多可以声明一个相关联的类对象。例如：

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

上例中我们有创建类 Foo，内部声明一个类对象，类对象中又含有成员属性 bar。这意味着我们可以直接通过类名访问 bar(与 JAVA 一样)：

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(Foo.bar)
```

{% raw %}
<p></p>
{% endraw %}

注意我们无法使用 Foo 的*实例*访问 bar：

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

因为 bar 并非 Foo 的成员，而是属于 Foo 的类对象；类对象是与所在的类*相联的*单独实体，并且不与其实例共享成员。因此也不能通过类名直接访问 baz：

{% raw %}
<p></p>
{% endraw %}

```kotlin
prinltn(Foo.baz) // error
```

{% raw %}
<p></p>
{% endraw %}

因为 baz 是 Foo 的成员，不属于它的类对象，所以只能通过 Foo 的*实例*访问 baz。  

现在，我们来看看类对象的工作原理。首先，存在一个为类对象单独生成的 JVM 类，bar 便是该类的成员。假设用 Java 的方式访问类对象：

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

类对象是存储在它定义的类中的静态字段中的一个实例，其属性使用 getter/setter 访问。

## 静态常量

类对象中的属性与静态字段相同（甚至更好），但仅限于 Kotlin。如上所述，对于 Java 而言这是不同的，如果（在 Java 中）框架或约定要求您必须使用静态字段，则可能会引发问题。  

**免责声明**：在 Kotlin M5.3 中，类是不可能存在静态字段的。但最近已经实现，所以只要你去[每日最新版本](http://confluence.jetbrains.com/display/Kotlin/Getting+Started#GettingStarted-UsingtheKotlinnightlybuilds)尝试即可。 

当对类对象使用 public 或 internal 访问修饰符，且不定义 getter 与 setter 时，Kotlin 会自动将其直接存储在附属类中，所以在 Java 中可以用

{% raw %}
<p></p>
{% endraw %}

```kotlin
System.out.println(Foo.bar);
```

{% raw %}
<p></p>
{% endraw %}

这对您的 Kotlin 代码而言没有任何区别：一切都能正常运行。即便在 Java 中老掉牙的 Foo.object$.getBar()，但是现在也可以在你的类中使用真正的静态常量了。  

感谢使用 Kotlin。
