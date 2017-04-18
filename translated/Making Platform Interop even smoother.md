---
title: "[译]Making Platform Interop even smoother"
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

与JVM 100％可互操作，随后使用JavaScript，一直是科特林的首要任务。随着现有代码的数量和丰富的JVM生态系统，具有互操作性和有效性的功能至关重要。<span id =“more-1616”> </ span>
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

尝试将值<em> x </ em>传递给以下函数：

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

在第一种情况下，Kotlin编译器会发出错误。这意味着对<em> nullNotAllowed </ em>的调用将需要：

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

参数<em>输入</ em>不再需要类型为<em> String？</ em>。您可以选择使用<em> String </ em>还是<em> String？</ em>  - 取决于其实际含义。在这个例子中，我们选择<em>输入</ em>不为空，并且<em>数据</ em>为空。
## 使用platformStatic的注释方法

Kotlin有<em>对象声明</ em>，可以看作单身人士。这些都是从Java中消耗的，尽管不是最好的语法。给定：

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

使代码更清洁。同样适用于<em>类对象</ em>。
### 去除包版广告

<em> platformStatic </ em>的另一个好处是在使用某些Java库（例如JUnit）时删除了一些存在的showstoppers。特别地，后者在使用时需要Java中的静态方法 [理论](https://github.com/junit-team/junit/wiki/Theories) 。对此的解决方法相当乏味。幸运的是，情况已经不再如此。我们可以使用<em> platformStatic </ em>注释来解决这个问题 [问题](https://youtrack.jetbrains.com/issue/KT-4861) 。

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

当从Kotlin调用这些可能时，尝试从Java调用它们是由于类型擦除而有问题的。类似于<em> platformStatic </ em>，我们引入了允许重命名该函数的<em> platformName </ em>注释，以便在从Java调用时，使用新的给定名称：

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

请注意，这是 [不是唯一的用例](http://blog.jetbrains.com/kotlin/2014/07/m8-is-out/#platformName)  for <em> platformName </ em>。
## 私人财产存取者

Kotlin的私人私人财产不再生成属性访问器，这意味着 [冲突](http://blog.jetbrains.com/kotlin/2014/07/m8-is-out/#platformName)  使用现有的<em> getXYZ </ em>方法
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

如果我们要在Kotlin中实现这个接口，而我们的类有一个名为<em> bar </ em>的私有属性，在M8和以前的版本中它会引起冲突，我们必须将属性命名为与< em> bar </ em>。从M9开始，情况就不一样了。因此，以下代码完全有效：

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
注意：M9尚未发布，但您可以在<a href="https://teamcity.jetbrains.com/project.html?projectId=Kotlin&amp;tab=projectOverview">夜间版本中找到这些功能</a> </ em>
