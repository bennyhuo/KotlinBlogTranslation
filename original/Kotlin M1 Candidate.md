---
title: Kotlin M1 Candidate
date: 2012-03-30 14:57:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/03/kotlin-m1-candidate/
---

IntelliJ IDEA 11.1 has been recently released, and we are happy to announce a milestone candidate build for Kotlin IDE plugin, too. This post gives an overview of what happened over the last month.
## Milestone Candidate Build is Ready for Your Evaluation

To install on IntelliJ IDEA 11.1 (Free Community Edition is available here), please follow the instructions from the Getting Started guide. In short:

* Use this plugin repository: http://www.jetbrains.com/kotlin/eap-plugin-repository/updatePlugins.xml
* Or download a zipped plugin from here.

You can always download nightly builds of Kotlin from our build server or build it yourself from sources.
Now we proceed to a short overview of the New and Noteworthy. Please refer to this blog post for the previously implemented features.
## Little Things that Matter

First of all, we did very many bugfixes, improvements and other important things that are hard to demo. See the commit history on github and the closed issues in YouTrack.
## Library

With the power of extension functions, Kotlin makes existing Java APIs better. In particular, we provide enhancements for JDK collections so that you can say things like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun main(args : Array<String>) {
    val list = arrayList(1, 2, 3)
    val odds = list.filter {it % 2 == 1}
    println(odds.join(", "))
}
```

{% raw %}
<p></p>
{% endraw %}

Here, filter() and join() are extension functions.
Implementation-wise, extension functions are just static utility functions, like “good old” Java’s Collecions.*, but with the “receiver.function()” call syntax, the IDE makes them much better: there is code completion that helps you browse through the API and learn it (just as if the extensions were normal class members):

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png"><img alt="" class="alignnone size-medium wp-image-483" data-recalc-dims="1" sizes="(max-width: 259px) 100vw, 259px" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?resize=259%2C300&amp;ssl=1" srcset="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?resize=259%2C300&amp;ssl=1 259w, https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?w=663&amp;ssl=1 663w"/></a></p>
{% endraw %}

You can navigate to sources of library functions:

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png"><img alt="" class="alignnone size-full wp-image-485" data-recalc-dims="1" sizes="(max-width: 501px) 100vw, 501px" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?resize=501%2C144&amp;ssl=1" srcset="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?resize=300%2C86&amp;ssl=1 300w, https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?w=501&amp;ssl=1 501w"/></a></p>
{% endraw %}

And see the doc comments there:

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png"><img alt="" class="alignnone size-full wp-image-486" data-recalc-dims="1" sizes="(max-width: 476px) 100vw, 476px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?resize=476%2C297&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?resize=300%2C187&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?w=476&amp;ssl=1 476w"/></a></p>
{% endraw %}

The HTML version of the library docs is available here.
## GitHub Support

Kotlin highlighting is now supported by github, including gist.
## Annotations

Kotlin now supports annotations. Here’s a small example that relies on JUnit 4:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import org.junit.Test as test
import org.junit.Assert.*
 
class Tests {
    test fun simple() {
        assertEquals(42, getTheAnswer())
    }
}
```

{% raw %}
<p></p>
{% endraw %}

Read more here.
## String Templates

Now you can use multi-line string templates, for example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
println("""
  First name: $first
  Last name: $last
  Age: $age
""")
```

{% raw %}
<p></p>
{% endraw %}

## Simple Enums

Simple cases of enum classes are now supported. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Color {
  RED
  GREEN
  BLUE
}
```

{% raw %}
<p></p>
{% endraw %}

## Local Functions

Functions can be declared inside other functions:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun count() : Int {
  fun count(parent : Entity) : Int {
    return 1 + parent.children.sum { count(it) }
  }
  return count(this.root)
}
```

{% raw %}
<p></p>
{% endraw %}

## Nullability

Kotlin now recognizes the @Nullable and @NotNull annotations). If the Java code says:

{% raw %}
<p></p>
{% endraw %}

```kotlin
@NotNull String foo() {...}
```

{% raw %}
<p></p>
{% endraw %}

Kotlin will trat foo() as returning a non-nullable String.
A short-hand operator (!!) for converting a nullable value into a non-nullable one is added:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val foo = getSomethingThatMayBeNull()
foo!!.bar() // throw NPE if foo is null, run bar() otherwise
```

{% raw %}
<p></p>
{% endraw %}

## Byte Code Unveiled

Click on the Kotlin button on the right edge of the IDEA window, and choose the “Bytecode” tab. You’ll see the byte-code Kotlin generates for your program!

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Bytecode-1.png"><img alt="" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Bytecode-1.png?resize=640%2C312&amp;ssl=1"/></a></p>
{% endraw %}

## Your feedback is very welcome. Have a nice Kotlin!

