---
title: "“Static constants” in Kotlin"
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
translator:
translator_url:
---

Kotlin is designed so that there’s no such thing as a “static member” in a class. If you have a function in a class, it can only be called on instances of this class. If you need something that is not attached to an instance of any class, you define it in a package, outside any class (we call it package-level functions):

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

But sometimes you need **static constants** in your class: for example, to comply with requirements of some framework or to use serialization. How do you do this in Kotlin? <span id="more-1101"></span> There are two things in Kotlin that resemble Java’s statics: aforementioned package-level functions and [class objects](http://confluence.jetbrains.com/display/Kotlin/Classes+and+Inheritance#ClassesandInheritance-Classobjects) . I’ll explain briefly what class objects are and then proceed to static constants.
## Class Objects

A class (not [inner](http://confluence.jetbrains.com/display/Kotlin/Nested+classes) and not local) or trait may declare at most one class object associated with it. For example:

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

Here we have a class, Foo, that declares a class object, which in turn has a member property bar. This means that we can call bar directly on a class name (just like in Java):

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(Foo.bar)
```

{% raw %}
<p></p>
{% endraw %}

Note that we can not call bar on an *instance*of Foo:

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

That’s because bar is not a member of Foo, only of its class object. Class object is a separate entity *associated* with the class, and does not share members with its instances. Neither can we call baz on the class name:

{% raw %}
<p></p>
{% endraw %}

```kotlin
prinltn(Foo.baz) // error
```

{% raw %}
<p></p>
{% endraw %}

This is because baz is a member of Foo, not of its class object, so you can only call baz on *instances*of Foo.
Now, let’s look at how class objects work. First, there’s a separate JVM class generated for a class object, and bar is a member of that class. If you access class objects from Java, you have to say something like this:

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

Class object is an instance stored in a static field inside the class it is defined in, and its properties are accessed with getters/setters.
## Static Constants

A property in a class object works as well as a static field (and even better), but only in Kotlin. As we saw above, for Java it looks different, and this may cause problems if some framework or convention (in Java) requires you to have a real static field.
**Disclaimer**: in Kotlin M5.3 there’s no way to have a static field in your class. It was implemented very recently, so you have it only in the [latest nightly build](http://confluence.jetbrains.com/display/Kotlin/Getting+Started#GettingStarted-UsingtheKotlinnightlybuilds) .
When you define a public or internal property in your class object, and do not specify custom getter, nor setter, Kotlin automatically stores it directly in the enclosing class, so that in Java you can say

{% raw %}
<p></p>
{% endraw %}

```kotlin
System.out.println(Foo.bar);
```

{% raw %}
<p></p>
{% endraw %}

There’s no difference for your Kotlin code: everything works as it should. Even in Java the old-fashioned Foo.object$.getBar(), but now you can also have real static constants in your class.
Enjoy.
