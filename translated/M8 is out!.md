---
title: "[译]M8 is out!"
date: 2014-07-02 00:00:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/07/m8-is-out/
translator:
translator_url:
---

自上次发布以来，这是一个非常忙碌的几个月，我们一直在努力进行实质性改进，特别是在速度方面。我们对这个版本有很多好处。让我们开始吧<span id =“more-1509”> </span>
## JVM

### 物业反思

作为第一次了解 Kotlin 的未来反思功能，您现在可以将属性作为 Kotlin 中的一流对象进行访问：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var x = 1
 
fun main(args: Array<String>) {
    println(::x.get()) // prints "1"
    ::x.set(2)
    println(x)         // prints "2"
}
```

{% raw %}
<p></p>
{% endraw %}

“:: propertyName”语法给出一个属性对象，以便您可以获取或设置其值。您还可以访问该属性的名称（将对各种框架有用）。我们将来会增加更多的功能。
要访问作为课程成员的属性，可以说

{% raw %}
<p></p>
{% endraw %}

```kotlin
class A(val p: Int)
 
fun main(args: Array<String>) {
    val prop = A::p
    println(prop.get(A(1))) // prints "1"
}
```

{% raw %}
<p></p>
{% endraw %}

当然，它也适用于扩展：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val String.lastChar: Char
  get() = this[size - 1]
 
fun main(args: Array<String>) {
  println(String::lastChar.get("abc")) // prints "c"
}
```

{% raw %}
<p></p>
{% endraw %}

Kotlin 反思的另一面是它与 Java 的反思的互操作性。例如，要找到一个支持字段或 Java 方法作为 Kotlin 属性的 getter，您可以这样说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.reflect.jvm.*
 
class A(val p: Int)
 
fun main(args: Array<String>) {
    println(A::p.javaGetter) // prints "public final int A.getP()"
    println(A::p.javaField)  // prints "private final int A.p"
}
```

{% raw %}
<p></p>
{% endraw %}

我们将在未来数月进一步发展反思能力。最终的目标是为框架作者提供真正强大的工具来满足他们的需求。议程上的内容包括适当的 Kotlin 类反省，通过反射使类型可用，将反射功能带入可调用引用（:: functionName）等。敬请关注。
### 内联功能改进

一些增强了内联功能，包括：

* 支持默认参数功能。


* 支持嵌入对象。

为了演示这两个功能，我们来看下面的例子。说，我们有一个 Value 界面：

{% raw %}
<p></p>
{% endraw %}

```kotlin
trait Value<V> {
    fun get() : V
}
```

{% raw %}
<p></p>
{% endraw %}

现在，我们想创建一个计算值被锁定的值：

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun <T> guardedValue(
        lock: Lock = ReentrantLock(),
        compute: () -> T
) : Value<T> {
    return object : Value<T> {
        override fun get(): T {
            return lock.withLock {
                compute()
            }
        }
    }
}
```

{% raw %}
<p></p>
{% endraw %}

我们的 guardedValue（）是一个内联函数。现在，**lock**参数具有默认值（为每个值创建一个新的 ReentrantLock）。然后，此函数内的对象表达式“捕获”**计算**参数，并直接在创建的匿名类内嵌。这导致只有一个类和一个对象每个值发出（并存储），而不是非内联情况的两个类和两个对象。

{% raw %}
<p><a name="platformName"></a></p>
{% endraw %}

### 报表平台签名冲突

编译器现在会发生错误，当它生成的某些 JVM 签名将会在字节码中发生冲突（以前这可能会导致 ClassFormatError 或意外覆盖超类“方法而不知道）。
例如，以下 Kotlin 代码看起来是无害的，但是断开了 JVM：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = 1
fun getX() = 1
```

{% raw %}
<p></p>
{% endraw %}

现在，Kotlin 抱怨这个代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
Error:(1, 1) Kotlin: Platform declaration clash:
The following declarations have the same JVM signature (getX()I):
    fun <get-x>(): kotlin.Int
    fun getX(): kotlin.Int
```

{% raw %}
<p></p>
{% endraw %}

原因是*x*的 getter 具有相同的名称（getX）和签名（不需要参数，返回 Int）作为其旁边声明的函数，JVM 不允许在类文件中使用这样的东西。
另一种情况是*意外覆盖*：

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class Base {
    fun getX() = 1
}
 
class Derived(val x: Int) : Base()
```

{% raw %}
<p></p>
{% endraw %}

这里，x 的 getter 与 getX（）具有相同的签名，但它们现在处于不同的类中，所以 getter 会静​​默地覆盖该函数，以使 Derived（2）.getX（）返回 2 而不是 1。
现在编译器抓住了这个错误

{% raw %}
<p></p>
{% endraw %}

```kotlin
Error:(1, 15) Kotlin: Accidental override:
The following declarations have the same JVM signature (getX()I):
    fun <get-x>(): kotlin.Int
    fun getX(): kotlin.Int
```

{% raw %}
<p></p>
{% endraw %}

人们可能会想知道为什么我们不会自动重命名其中一个功能，而不是发出错误？答案在于 Java 互操作性的领域（没有人喜欢编译器发明的名称）和二进制兼容性（事物的名称绝不能静默地改变，或者所有依赖的代码将意外地破坏）。另一方面，您可以使用*platformName*注释手动指定所需的 JVM 名称：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.platform.platformName
 
val x = 1
[platformName("doGetX")]
fun getX() = 1
```

{% raw %}
<p></p>
{% endraw %}

请注意，对于 Kotlin 客户端，此代码不会更改，但 Java 客户端必须使用平台名称（doGetX）而不是 Kotlin 名称（getX）。
**警告：**这是一个**break**更改，您现有的一些代码可能需要修复。
### 支持瞬态，同步和 strictfp

除了长期可用的**之外。我们现在支持*transient*，*同步*和*strictfp*作为注释。语义与 Java 类似：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class FlagDemo {
  volatile var s = ""
  transient var list = listOf(1, 2, 3)
  strictfp fun math() { /* strict floating-point available here */ }
  synchronized fun sync() { /* synchronized on this */ }
}
```

{% raw %}
<p></p>
{% endraw %}

### 生成的代码加速


* 生成的委托代码的代码现在工作得更快，并减少内存分配。
* 此外，由于现在正在使用专用的字节码指令，常量的语句更快。

## JavaScript 支持


* 您现在可以在 JavaScript 中支持数据类。这意味着您现在可以在使用 JavaScript 中的数据注释以及 Java 中注释类时自动生成 toString，equals 和 hashCode。
* 此外，JavaScript 中还支持 LinkedHashSet 和 LinkedHashMap。

## 语言变化

一些语言变化，所有这些变化都是**破坏变化**，重要的是要注意：

* 私有的一个包现在意味着私有的当前包中的模块。在其他模块中具有相同名称的软件包将不会看到这些定义。请注意，程序包是嵌套的，因此同一个模块中的子包也可以看到 privates。
* 扩展属性不能具有后缀字段。这是从来没有建议过的。
* 如果您发现 Kotlin 允许“@”和“@@”作为标签名称，我们很抱歉告诉您，这不再是这样。

## 添加到标准库

标准库还提供了一些新的功能：

* 添加了 slice（）函数，它可以迭代整数，并返回一个包含所述位置元素的列表。
* join（）适用于字符串的 iterables（数组，列表等），并将它们组合成一个字符串
* joinToString（）适用于任何类型的迭代或数组，并且等效于.map {it.toString（）} .join（）
* 地图现在有重载的函数 contains（）。因此，通过惯例，可以实现像“map in map”这样的功能
* 字符串现在可以利用诸如函数之类的集合
* substringBefore，substringBeforeLast 和 substringAfter，substringAfterLast 允许在某个字符或字符串之前和之后找到字符串。
replaceBefore，replaceBeforeLast 和 replaceAfter，replaceAfterLast 允许在某个字符或字符串之前和之后替换字符串。
appendln 添加到 StringBuilder
一个新的 StringBuilder 函数，它接受一个 String 构建器扩展，允许代码如：


* 
*     val information = StringBuilder {
        附加（“第一个条目”）
        appendln（）
        appendln（“其他一行”）
    }
* 

12345

val information = StringBuilder {append（“A first entry”）appendln（）appendln（“Some other line”）}
* substringBefore，substringBeforeLast 和 substringAfter，substringAfterLast 允许在某个字符或字符串之前和之后找到字符串。
* replaceBefore，replaceBeforeLast 和 replaceAfter，replaceAfterLast 允许在某个字符或字符串之前和之后替换字符串。
* appendln 添加到 StringBuilder
* 一个新的 StringBuilder 函数，它接受一个 String 构建器扩展，允许代码如：

