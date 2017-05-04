---
title: "[译]Improving Java Interop: Top-Level Functions and Properties"
date: 2015-06-23 14:56:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/06/improving-java-interop-top-level-functions-and-properties/
translator:
translator_url:
---

Kotlin从第一天起就具有顶级的职能和财产。它们在许多情况下非常方便：从基本实用程序到标准API的扩展。
但是，Kotlin代码不是唯一的客户端，今天我要解释一下在调用顶级函数和属性时，我们如何计划改进Java互操作。<span id =“more-2398”> < / span>
## 基本

顶级功能是编译成静态方法的字节码，这样就可以了

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar
 
fun demo() { ... }
```

{% raw %}
<p></p>
{% endraw %}

成为

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar;
 
public class BarPackage {
    public static void demo() { ... }
}
```

{% raw %}
<p></p>
{% endraw %}

或者至少你可以这样想到。 <img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images /smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>
属性非常相似，只将它们转换为字段和访问器：

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar
 
val prop: String = ...
```

{% raw %}
<p></p>
{% endraw %}

成为

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar;
 
public class BarPackage {
    static String prop = ...;
 
    public static String getProp() { return prop; }
}
```

{% raw %}
<p></p>
{% endraw %}

注意类的名称：`BarPackage`。它源于包的简短名称：`bar`。其余的很简单：静态方法。所以我们可以从Java引用它们：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public static void main(String[] args) {
    System.out.println(BarPackage.getProp());
}
```

{% raw %}
<p></p>
{% endraw %}

## 包装件和外墙

实际上，这是一个更棘手的事情：顶级的功能和属性成为Java类中的静态，我们可以通过一个名为package的类来访问它们，但是，这个类只是一个**facade** 。代码的实际布局如下：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/PackageFacade.png"><img alt="PackageFacade" class="alignleft size-full wp-image-2400" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/PackageFacade.png?resize=640%2C309&amp;ssl=1"/></a></p>
{% endraw %}

每个源文件被编译成一个<em>独立的类文件</em>。即使他们在同一个包裹。那些每个源文件类被称为**package-parts**。它们包含方法的所有实际字节码，并声明所有字段。所以，所有实现都驻留在包零件</em>中。
然后，生成一个单独的**package-facade**类，声明所有顶级函数和属性（再次），并将实现委托给包部件。
## 为什么

**为什么有一个门面**。这是我们将要改变的一个方面，但是我们在几年前就做出了这样一个决定的原因，就是为Java客户端提供一个单一的入门点类似于它的简单。另外，将功能从一个文件移动到另一个文件不会破坏任何东西，因为我们仅通过立面来引用它们，不是吗？**不是吗？**嗯，实际上并不是这样，但是我们稍后会介绍一下，现在只需解释剩下的设计，就需要一个立面授予
**为什么是零件包**。主要原因是静态字段的初始化顺序。确实，考虑这两个文件：
<em> file1.kt </em>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar
 
val a = computeA()
```

{% raw %}
<p></p>
{% endraw %}

<em> file2.kt </em>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar
 
val b = computeB()
```

{% raw %}
<p></p>
{% endraw %}

当我们从Java访问`a`或`b`时，应该以什么顺序调用它们的初始化程序？事实上，这可能是一个非常复杂的问题，因为`computeA（）`和`computeB（）`可能彼此依赖（直接或间接地通过其他代码）。他们可能会有副作用，所以这真的很重要。
所以，Kotlin的答案是：

* 里面一个文件属性都是从上到下初始化的，
* 第一次访问此文件中的任何代码。

循环可能发生（并导致错误），但这是不可避免的，Java与静态方法相同，不是吗？因此，实现对Java静态类初始化器的语义搭载：每个文件都有自己的包部分，它声明所有的字段，并在`＆lt; clinit＆gt;`方法（对应于<代码> static {...}`初始化器在Java语言中）。因此，在第一次访问时对字段进行初始化。我们可以免费获得线程安全，这是一个很大的优势。如果不是包装件，我们不能使其工作。
## 软件包名称

正如您在上图中可能已经注意到的，程序包部分往往具有奇怪的名称，例如`BarPackage $ file1 $ 0fbe61c7.class`。这显然是包含一个包的外观名称（`BarPackage`），源文件（`file1`）的短名称和绝对的哈希码源文件的路径</em>。是的，一个绝对的路径。没有其他方法可以确保两个包装部件名称不会冲突。
如果你从Kotlin程序中看到一个异常堆栈跟踪，你可能会注意到这些哈希值，它们只是丑陋。更大的问题是，当项目在另一台机器上构建时，它们可能会改变</em>（不太可能将源代码树放在另一个目录中）。这可能会造成麻烦，而且它做了几次。
## 包 - 门面名称，再次

现在是时候谈论真正的麻烦，不断地一直在咬我们和我们的用户。让我们面对它：**包立面名称做冲突**。
通常情况如何：您有两个模块，`a`和`b`，而在`a`中，您有一个顶级的函数在<code > foo.bar`包。一切都很好，直到您在另一个模块**，`b`中的相同`foo.bar`软件包**中添加另一个顶级功能。一旦你这样做，两个模块都会生成具有相同完全限定名称的类文件：`foo.bar.BarPackage`，并且运行时没有机会区分它们。并且您得到一个`NoSuchMethodError`，因为在运行时只加载了两个外观中的一个，而另一个外部的函数不在那里。
（编译也可能会打破，但并不是那么糟糕。）
## 新设计

那么我花了一段时间来解释现在的事情如何运作。但是这只是告诉你，我们要改变它<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com /blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>
所以上述设计有一些问题：

* 包装外立面的冲突是很痛苦的，很可能在相当大的项目中，
* 包装零件名称因为散列而丑陋，
* Java API并不是很棒的BarPackage全部：这些名字不是很丰富。

为了减轻这些问题，我们决定：

* 摆脱单立面范式，
* 命名包文件名后的文件（Foo.kt  - > Foo.class），
* 提供文件级注释来定制Java类名称，
* 允许多个文件具有与外墙实际相关的情况相同的自定义名称。

所以：

* 如果声明同一个软件包的成员（例如，两者都包含顶部的foo.bar），则不能使用相同名称的文件。
* 您可以通过文件名（File1.foo（））引用Java中的顶级函数，
* 重命名文件需要重新编译客户端，除非您已使用注释自定义类名。

**示例1**。默认情况下，每个文件被编译为一个以它命名的类：
<em> file1.kt </em>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar
 
fun foo() {...}
```

{% raw %}
<p></p>
{% endraw %}

成为

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar;
 
public class File1 {
    public static void foo() {...}
}
```

{% raw %}
<p></p>
{% endraw %}

**示例2**。我们可以通过提供文件级注释来更改类的名称：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@file:jvmName("Utils")
package foo.bar
 
fun foo() {...}
```

{% raw %}
<p></p>
{% endraw %}

成为

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar;
 
public class Utils {
    public static void foo() {...}
}
```

{% raw %}
<p></p>
{% endraw %}

无论源文件名称如何。
**示例3**。通过为许多文件指定相同的JVM名称，我们可以隐藏为立面后面的单个文件生成的许多软件包部分：
<em> file1.kt </em>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@file:jvmName("Utils")
package foo.bar
 
fun foo() {...}
```

{% raw %}
<p></p>
{% endraw %}

<em> file2.kt </em>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@file:jvmName("Utils")
package foo.bar
 
fun bar() {...}
```

{% raw %}
<p></p>
{% endraw %}

生成包含实现和外观的`File1.class`和`File2.class`

{% raw %}
<p></p>
{% endraw %}

```kotlin
package foo.bar;
 
public class Utils {
    public static void foo() { File1.foo(); }
    public static void bar() { File2.bar(); }
}
```

{% raw %}
<p></p>
{% endraw %}

## 元数据的一小部分

当我们有一个单一的外观，我们可以查看它，并一次查找包的所有成员。现在没有一个地方可以研究，这可能会影响编译性能，因此，对于每个模块，编译器将生成一个特殊文件`META-INF /＆lt;模块名称＆gt; .kotlin_module`并存储从包到包的零件映射。这将有助于快速发现顶级成员。
## 结论

新计划使我们摆脱了旧的问题。类名冲突仍然是可能的，但不会比正常课程更可能。
这篇博文描述了我们即将实施的设计
**如果您有反馈意见，非常欢迎！**
