---
title: "Making Platform Interop even smoother"
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
translator:
translator_url:
---

Being 100% interoperable with the JVM, and subsequently with JavaScript, has always been among Kotlin’s top priorities. With the amount of existing code, and a rich JVM ecosystem, having the ability of interoperating and leveraging these is crucial.<span id="more-1616"></span>
With the upcoming release of M9 we’ve improved on this, making the integration even more seamless.
## Platform Types

Dealing with nulls is one of the biggest issues when it comes to Java  interoperability. Almost any Java method may, potentially, return null, so Kotlin has treated Java types as nullable, and we either need to resort to using the safe-call (?.) operator or notnull-assertion (!!) to avoid compilation errors:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = javaCanReturnNull() // Java call that can return null
```

{% raw %}
<p></p>
{% endraw %}

on trying to pass the value *x* to the following functions:

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

in the first case, Kotlin compiler would issue an error. This means that the call to *nullNotAllowed* would need to be:

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

As of M9 this is no longer the case. This allows for much cleaner code, and avoiding the overuse of ?. and !! operators when interacting with Java.
Much the same way, when implementing Java interfaces, methods that can have potentially null arguments, no longer require these declarations to be declared as nullable in Kotlin. For instance, given:

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

when implementing this in Kotlin:

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

the parameter *input* no longer has to be of type *String?*. You can choose to make it either *String* or *String?* — depending on its actual meaning. In this example we chose *input* to be not-null, and *data* to be nullable.
## Annotating methods with platformStatic

Kotlin has *object declarations* which can be viewed as singletons. And these are consumable from Java, albeit not with the nicest syntax. Given:

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

consuming this from Kotlin, would be:

{% raw %}
<p></p>
{% endraw %}

```kotlin
Foo.bar()
```

{% raw %}
<p></p>
{% endraw %}

whereas from Java it would look like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
Foo.INSTANCE$.bar()
```

{% raw %}
<p></p>
{% endraw %}

With the next release, we’ll be able to call the method from Java the same way as from Kotlin by simply adding an annotation to the function declaration:

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

making the code much cleaner. Same applies to *class objects*.
### Removing roadblocks

Another benefit of *platformStatic* is removing some showstoppers that existed when using certain Java libraries such as JUnit. In particular, the latter requires a static method in Java when using [Theories](https://github.com/junit-team/junit/wiki/Theories) . The workaround for this was quite tedious. Fortunately, this is no longer the case. We can use the *platformStatic* annotation to solve this [issue](https://youtrack.jetbrains.com/issue/KT-4861) .

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

## Leveraging overloaded functions with platformName

When having overloaded methods that use generics such as:

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

While calling these from Kotlin is possible, trying to invoke these from Java is problematic due to type erasure. Similar to *platformStatic*, we’ve introduced the *platformName* annotation that allows to rename the function so that when invoked from Java, the new given name is used:

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

This can now be called from Java as follows:

{% raw %}
<p></p>
{% endraw %}

```kotlin
averageOfInt(numbers)
```

{% raw %}
<p></p>
{% endraw %}

Note that this is [not the only use case](http://blog.jetbrains.com/kotlin/2014/07/m8-is-out/#platformName) for *platformName*.
## Private property accessors

Property accessors are no longer generated for private private properties in Kotlin, which means that [conflicts](http://blog.jetbrains.com/kotlin/2014/07/m8-is-out/#platformName) with existing *getXYZ* methods do<br/>
not occur if unnecessarily. Take the following interface in Java:

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

If we are to implement this interface in Kotlin and our class has a private property named *bar*, in M8 and previous versions it causes a conflict, and we’d have to name the property to something different than *bar*. Starting with M9, this is no longer the case. As such, the code below is perfectly valid:

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

## Summary

With these changes coming in M9 we’ve removed some roadblocks and more importantly aimed at making the interoperability between Java and Kotlin much cleaner. And while these improvements can make consuming existing Java code more pleasant, it also allows for an even better experience of writing new libraries and functionality in Kotlin and consuming these from Java.
As always, we’d love feedback. Let us know what you think.
*Note: M9 has not been released yet, but you can find these features on <a href="https://teamcity.jetbrains.com/project.html?projectId=Kotlin&amp;tab=projectOverview">the nightly builds</a>*
