---
title: "Kotlin M5.1"
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

There have been enough little improvements since [Kotlin M5](http://blog.jetbrains.com/kotlin/2013/02/kotlin-m5-is-out/) so that we are rolling them out as M5.1 today. Some of them are not so little in fact, like enabling the use of Scala libraries, such as [Akka](http://akka.io/) . This post gives a quick overview of these changes.<span id="more-971"></span>
## Better Support for Scala Classes. Akka

Theoretically, it is very easy for all JVM languages to interoperate. In practice, there appear to be numerous little problems that make it unpleasant or practically impossible.
One of such problems was related to the ambiguous use of “$” signs in class names, which is a well-known issue on the JVM. It being fixed now, allows you to use some Akka classes you couldn’t use before, such as Duration.
To get an impression of what Akka looks like in Kotlin, have a look at [this example](https://gist.github.com/abreslav/5046126) .
## Even More Helpful IDE

With the help of students of Cornell and Jagiellonian universities, we got quite a few quick fixes implemented in M5.1. When the IDE complains about some error or warns you, you can simply press Alt+Enter and get a list of proposed fixes:

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i2.wp.com/www.evernote.com/shard/s171/sh/b504e729-ddda-42b5-b330-e08e9ef3986c/3d16d58b507733588c1037d60d1ed0dc/res/33c7d0fd-b2e0-482a-ad71-aef35d452fb2/skitch.png?w=640&amp;ssl=1"/></p>
{% endraw %}

## Parameters are Immutable

We removed support for mutable parameters, as in

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

The main reason is that this was confusing: people tend to think that this means passing a parameter by reference, which we do not support (it is costly at runtime). Another source of confusion is primary constructors: “val” or “var” in a constructor declaration means something different from the same thing if a function declarations (namely, it creates a property). Also, we all know that mutating parameters is no good style, so writing “val” or “var” infront of a parameter in a function, catch block of for-loop is no longer allowed.
If some of your existing code breaks, you can quick-fix the whole project in one click using the IDE:

{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/JY-Vx8FjtIM?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## Support for Java’s**protected static**methods

Some Java frameworks, like Android, rely on protected static methods to be available in subclasses. Although this seems like a questionable pattern, Kotlin now supports it (only for Java compatibility), i.e. you can access a **protected static**member of a Java class if you extend this class in Kotlin.
## Anonymous Objects

Consider the following code (that uses a Kotlin analog to anonymous inner class):

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = object : A() { ... }
```

{% raw %}
<p></p>
{% endraw %}

What is the type of x? It used to be the anonymous type, but if you use x from the outside, you can not access it: the type is not valid. Now the type will be A. This applies only to properties that can be seen from the outside, i.e. if x is a local variable it will still have the anonymous type, since it is harmless.
## Class Objects are Usable from Java

Kotlin classes do not have static members, but rather have *<a href="http://confluence.jetbrains.com/display/Kotlin/Classes+and+Inheritance#ClassesandInheritance-Classobjects">class objects</a>*:

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

Now, with a few bugs fixed, you can access members of class objects from your Java code:

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

## Compiler

The compiler is being improved too: a few fixes for corner cases of nullable types interacting with generics and optimizations for loops over ranges.
## Requirements

Kotlin M5.1 requires [IntelliJ IDEA 12.0.4](http://www.jetbrains.com/idea/download/index.html) (EAPs of 12.1 are not supported yet), you can download it from the plugin repository.
**Have a nice Kotlin!**
