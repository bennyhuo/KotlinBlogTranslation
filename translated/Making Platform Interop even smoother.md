---
title: [译]Making Platform Interop even smoother
date: 2014-10-06 13:20:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/10/making-platform-interop-even-smoother/
---

与JVM 100％可互操作，随后使用JavaScript，一直是科特林的首要任务。随着现有代码的数量和丰富的JVM生态系统，具有互操作和利用这些功能的能力至关重要。
随着即将发布的M9，我们已经改进了这一点，使集成更加无缝。
## 平台类型

处理空值是涉及Java互操作性的最大问题之一。几乎任何Java方法可能会返回null，所以Kotlin将Java类型视为可以为空的，我们还是要求使用安全调用（？。）运算符或notnull-assertion（!!）来避免编译错误：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = javaCanReturnNull() // Java call that can return null
```

{% raw %}
<p></p>
{% endraw %}

尝试将值x传递给以下函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun nullNotAllowed(value: String) {}
fun nullAllowed(value: String?) {}
```

{% raw %}
<p></p>
{% endraw %}

在第一种情况下，Kotlin编译器会发出错误。这意味着对nullNotAllowed的调用将需要：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = javaCanReturnNull()
nullNotAllowed(x!!)
```

{% raw %}
<p></p>
{% endraw %}

从M9开始，情况就不一样了。这允许更清洁的代码，并避免过度使用？和!!操作员在与Java进行交互时。
同样的方式，在实现Java接口时，可能具有潜在的空参数的方法不再需要在Kotlin中将这些声明声明为可空。例如，给出：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public interface SomeFoo {
    void foo(String input, String data);
}
```

{% raw %}
<p></p>
{% endraw %}

当在科特林实施这个时：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public class SomeInterestingFoo(): SomeFoo {
    override fun foo(input: String, data: String?) { // String? no longer required
    ...
    }
}
```

{% raw %}
<p></p>
{% endraw %}

参数输入不再必须是String？类型。您可以选择使其为String还是String？ - 取决于其实际意义。在这个例子中，我们选择输入不为null，数据为空。
## 使用platformStatic的注释方法

Kotlin有对象声明，可以看作是单身人士。这些都是从Java中消耗的，尽管不是最好的语法。给定：

{% raw %}
<p></p>
{% endraw %}

```kotlin
object Foo {
    fun bar() {
    }
}
```

{% raw %}
<p></p>
{% endraw %}

从科特林消费，将是：

{% raw %}
<p></p>
{% endraw %}

```kotlin
Foo.bar()
```

{% raw %}
<p></p>
{% endraw %}

而从Java它将看起来像这样：

{% raw %}
<p></p>
{% endraw %}

```kotlin
Foo.INSTANCE$.bar()
```

{% raw %}
<p></p>
{% endraw %}

随着下一个版本，我们可以通过简单地向函数声明添加一个注释，从与Kotlin相同的方式从Java调用该方法：

{% raw %}
<p></p>
{% endraw %}

```kotlin
object Foo {
   platformStatic bar() {
   }
}
```

{% raw %}
<p></p>
{% endraw %}

使代码更清洁。同样适用于类对象。
### 去除包版广告

platformStatic的另一个好处是删除了在使用某些Java库（如JUnit）时存在的一些showstoppers。特别地，后者在使用Theories时需要Java中的静态方法。对此的解决方法相当乏味。幸运的是，情况已经不再如此。我们可以使用platformStatic注解来解决这个问题。

{% raw %}
<p></p>
{% endraw %}

```kotlin
RunWith(javaClass<Theories>())
public class TestDoubling {
       class object {
           platformStatic DataPoints
               public fun values(): IntArray {
                    return intArray(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
               }
         }

         Theory
         public fun testDoubling(a: Int?) {
                  Assert.assertThat<Int>(doubling(a!!), `is`<Int>(a * 2))
         }

         public fun doubling(value: Int): Int {
                  return value * 2
         }
}
```

{% raw %}
<p></p>
{% endraw %}

## 利用platformName重载函数

当有重载的方法使用泛型，如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Iterable<Long>.average(): Double {
...
}
 
fun Iterable<Int>.average(): Double {
...
}
```

{% raw %}
<p></p>
{% endraw %}

当从Kotlin调用这些可能时，尝试从Java调用它们是由于类型擦除而有问题的。与platformStatic类似，我们引入了platformName注释，允许重命名该函数，以便从Java调用时，将使用新的给定名称：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Iterable<Long>.average(): Long {
...
}
 
platformName("averageOfInt") fun Iterable<Int>.average(): Int {
...
}
```

{% raw %}
<p></p>
{% endraw %}

现在可以从Java调用如下：

{% raw %}
<p></p>
{% endraw %}

```kotlin
averageOfInt(numbers)
```

{% raw %}
<p></p>
{% endraw %}

请注意，这不是platformName的唯一用例。
## 私人财产存取者

Kotlin不再为私有私有属性生成属性访问器，这意味着与现有的getXYZ方法冲突
不必要地发生。在Java中执行以下界面：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public interface SomeFoo {
    String getBar();
}
```

{% raw %}
<p></p>
{% endraw %}

如果我们要在Kotlin中实现这个界面，而我们的类有一个名为bar的私有属性，在M8和以前的版本中，它会引起冲突，我们必须将属性命名为与bar不同的东西。从M9开始，情况就不一样了。因此，以下代码完全有效：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public class SomeInterestingFoo(private val bar: String): SomeFoo {
    override fun getBar(): String {
          ...
    }
}
```

{% raw %}
<p></p>
{% endraw %}

## 概要

随着M9中的这些变化，我们已经删除了一些障碍，更重要的是使Java和Kotlin之间的互操作性更加清晰。虽然这些改进可以使消费现有的Java代码更加愉快，但它也允许在Kotlin中编写新的库和功能以及从Java中消耗这些库的更好的体验。
和往常一样，我们会喜欢反馈。让我们知道你的想法。
注意：M9尚未发布，但您可以在夜间版本中找到这些功能
