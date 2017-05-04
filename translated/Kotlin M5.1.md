---
title: "[译]Kotlin M5.1"
date: 2013-02-27 11:03:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/02/kotlin-m5-1/
translator:
translator_url:
---

自从以来，已有足够的改善 [Kotlin M5](http://blog.jetbrains.com/kotlin/2013/02/kotlin-m5-is-out/) 所以我们今天把它们推出 M5.1。其中一些事实上并不那么简单，就像使用 Scala 库一样 [阿卡](http://akka.io/) 。这篇文章快速概述了这些变化。<span id =“more-971”> </span>
## 更好地支持 Scala 类。阿卡

理论上讲，所有 JVM 语言都很容易互操作。在实践中，似乎有许多小问题使它变得不愉快或几乎不可能。
其中一个问题与类名中使用“$”符号的模糊有关，这是 JVM 上众所周知的问题。它现在被修复，允许您使用以前不能使用的一些 Akka 类，如 Duration。
要了解 Akka 在 Kotlin 看起来的印象，请看看 [这个例子](https://gist.github.com/abreslav/5046126) 。
## 甚至更有用的 IDE

在康奈尔大学和耆那教大学的学生的帮助下，我们在 M5.1 中实现了很多快速修复。当 IDE 抱怨某些错误或警告您时，您可以简单地按 Alt + Enter 并获取建议的修复列表：

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i2.wp.com/www.evernote.com/shard/s171/sh/b504e729-ddda-42b5-b330-e08e9ef3986c/3d16d58b507733588c1037d60d1ed0dc/res/33c7d0fd-b2e0-482a-ad71-aef35d452fb2/skitch.png?w=640&amp;ssl=1"/></p>
{% endraw %}

## 参数是不变的

我们删除了对可变参数的支持，如

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(var x: Int) {
  x = 5
}
```

{% raw %}
<p></p>
{% endraw %}

主要的原因是这是令人困惑的：人们往往认为这意味着通过引用传递一个参数，我们不支持（在运行时代价高昂）。混淆的另一个来源是主要构造函数：构造函数声明中的“val”或“var”表示与函数声明（即，它创建一个属性）相同的东西。此外，我们都知道变异参数不是很好的风格，所以在函数中写入一个参数的“val”或“var”infront，不再允许 catch 循环的块。
如果您现有的一些代码中断，您可以使用 IDE 快速修复整个项目：

{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/JY-Vx8FjtIM?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## 支持 Java 的**保护静态**方法

一些 Java 框架（如 Android）依赖于受保护的静态方法在子类中可用。虽然这似乎是一个有问题的模式，但 Kotlin 现在支持它（仅适用于 Java 兼容性），即如果您在 Kotlin 中扩展此类，则可以访问 Java 类的**受保护的静态**成员。
## 匿名对象

考虑以下代码（使用 Kotlin 模拟到匿名内部类）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = object : A() { ... }
```

{% raw %}
<p></p>
{% endraw %}

x 的类型是什么？它曾经是匿名类型，但如果您从外部使用 x，则无法访问它：类型无效。现在该类型将为 A.这仅适用于从外部可以看到的属性，即如果 x 是局部变量，它将仍然具有匿名类型，因为它是无害的。
## 类对象可以从 Java 使用

Kotlin 类没有静态成员，而是<a href="http://confluence.jetbrains.com/display/Kotlin/Classes+and+Inheritance#ClassesandInheritance-Classobjects">类对象</a>*：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class A {
    class object {
        val x = 1
    }
}
```

{% raw %}
<p></p>
{% endraw %}

现在，修复了一些错误，您可以从 Java 代码访问类对象的成员：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public static void main(String[] args) {
    System.out.println(A.object.instance$.getX());
}
```

{% raw %}
<p></p>
{% endraw %}

## 编译器

编译器也在改进：一些修复可空类型的角色与泛型交互的范围和针对范围的循环的优化。
## 要求

Kotlin M5.1 要求 [IntelliJ IDEA 12.0.4](http://www.jetbrains.com/idea/download/index.html) （不支持 12.1 的 EAP），您可以从插件库中下载。
**拥有不错的 Kotlin！**
