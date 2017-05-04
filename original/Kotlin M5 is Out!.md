---
title: "Kotlin M5 is Out!"
date: 2013-02-04 14:30:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/02/kotlin-m5-is-out/
translator:
translator_url:
---

In two weeks from now it will be one year since Kotlin started out as an open source project. It’s been a lot of hard work over this time, with a huge help of the community: we received [164 pull requests](https://github.com/jetbrains/kotlin/pulls?page=1&sort=created&state=closed) , which means a contribution every other day or so. Today we make another step and roll out **Kotlin M5**. This blog post covers the changes introduced in this release.<span id="more-835"></span>
# Overview

M5 was a short milestone (you should subtract the New Year’s break from its term), but we got rid of [144 issues](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-12-11+..+2013-02-04) in the tracker.
Many IDE subsystems were improved, including JUnit runner, search of Kotlin classes from Java, better diagnostics for invalid external annotations, new icons and support for the [Darcula color scheme](http://www.jetbrains.com/idea/) :

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/02/Darcula.png"><img alt="" class="aligncenter size-medium wp-image-836" data-recalc-dims="1" sizes="(max-width: 300px) 100vw, 300px" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/02/Darcula.png?resize=300%2C224&amp;ssl=1" srcset="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/02/Darcula.png?resize=300%2C224&amp;ssl=1 300w, https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/02/Darcula.png?w=965&amp;ssl=1 965w"/></a></p>
{% endraw %}

Minor changes in the language include better support for Float literals (you can now simply [say 1.0 where Float is expected](http://youtrack.jetbrains.com/issue/KT-1895) ) and ability to mix positioned and named arguments to function calls.
Some of the changes are not so humble and may require you to fix the existing code…
# Package Classes

In the older versions of Kotlin every package that had top-level functions or properties declared was compiled to a class named “namespace”, where the top-level declarations were represented by static methods. When you used more than one of these “namespace” classes in Java, you ran into a name clash: you can not import two classes with the same name into the same compilation unit. With Kotlin M5 package [classes are named after respective packages](http://confluence.jetbrains.com/display/Kotlin/Java+interoperability#Javainteroperability-Packagelevelfunctions) , which gives them different names and fixes this problem.
The naming convention works as follows: package “org.example” gets a class “org.example.ExamplePackage”. I.e., we take the simple name of the package, capitalize it, append “Package” and put that class into the package itself. So far it works pretty well.
NOTE: your older versions of **kotlin-runtime.jar** will not work any more because of this change. The compiler will complain about an “incompatible ABI version”, and the IDE will propose to replace the old runtime jar with a new one.
# Inner Classes

An <em>inner class </em>is a non-static nested class, i.e. it holds a reference to an instance of its outer. In Java nested classes are inner by default, and if you don’t want a reference to the outer, you make your class **static**. Sometimes it leads to memory leaks, when someone is holding a reference to an instance of an inner class without knowing that it also holds an outer instance.
Since M5, Kotlin wants you to [mark inner classes explicitly](http://confluence.jetbrains.com/display/Kotlin/Nested+classes) , and nested classes are “static” by default. This may break your existing code, and in the IDE there’s a handy quick-fix to the rescue (just press Alt+Enter on the error).

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s171/sh/b06bbb46-0577-47f3-a715-f3473e1b4f16/e8cb41d5ccdd6ff192c7647619bf47d5/res/df4fb94b-51ea-4923-8538-ea590dbb5467/Add_inner_modifier-20130204-135715.png.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

# Java Generics and Nullability

Generics are tricky, and their combination with nullable types is trickier still. In Java everything is nullable, for example, consider a Java method foo(ArrayList<String>), Kotlin (before M5) used to see it as ArrayList<String?>?, i.e. the collection may be null, and its elements may be null too. This is the safest thing we can do, but it proved to be very inconvenient: if you have an ArrayList<String> in Kotlin, you can’t pass it to foo(): ArrayList is invariant in its generic parameter and thus ArrayList<String> is not a subtype of ArrayList<String?>. This causes a lot of pain, even when KAnnotator is used.
So we decided to change the default strategy for <em>generic argument types</em>, and load ArrayList<String>? in the case above.
This change may break some of the existing code. Most of it is straightforwardly fixable by removing unneeded question marks. If you want the old type, you can [add an external annotation](http://blog.jetbrains.com/kotlin/using-external-annotations/) to your Java definition.
But what about safety? Now Java code may fool you by giving you a collection of nulls instead of strings, and your Kotlin code will fail. This may happen, but we make it fail helpfully: Kotlin checks data received from Java and fails early and with a detailed error message like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
Exception in thread "main" java.lang.IllegalStateException:
    Method specified as non-null returned null: JavaClass.foo
    at _DefaultPackage.main(hello.kt:4)
```

{% raw %}
<p></p>
{% endraw %}

This is much better than an NPE sometime later, maybe. The same kind of checks is performed for function parameters: if someone calls a Kotlin function illegally passing a null, it will blow up early, blaming the guilty as precisely as possible.
# Varargs and function literals

Kotlin’s [type-safe builders](http://confluence.jetbrains.com/display/Kotlin/Type-safe+Groovy-style+builders) [are](http://karaframework.com/docs/views.html) [awesome](http://karaframework.com/docs/stylesheets.html) , especially if you note that they are not a built-in mechanism, but merely a combination of nice language features (mainly extension functions and higher-order functions). One thing was bothering builder writers in older versions of Kotlin: you could not define a vararg function that could also take a function literal as an argument outside parentheses. Now you can do it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun css(vararg selectors: Selector, body: Element.() -> Unit) {...}
```

{% raw %}
<p></p>
{% endraw %}

can be called as

{% raw %}
<p></p>
{% endraw %}

```kotlin
css(TD, _class("data")) {
    background_color = RED
}
```

{% raw %}
<p></p>
{% endraw %}

You can also use named and positioned arguments together (including varargs):

{% raw %}
<p></p>
{% endraw %}

```kotlin
css(TD, body = foo)
```

{% raw %}
<p></p>
{% endraw %}

# Ranges

Kotlin’s standard library evolves too, and this time we revised ranges. To remind you, ranges are used a lot in loops and conditions:

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (i in 1..10) { /* 1, 2, 3, ..., 10 */ } 
 
if (x in low..high) { /* low <= x <= high */ }
```

{% raw %}
<p></p>
{% endraw %}

The new ranges are more consistent internally and generalize properly to cases with descending iteration, nontrivial increments and so on. We’ll provide more details in a separate blog post this week.
# Default constructors

Kotlin allows only one constructor per class. When modeling our data, we often use default values for constructor parameters (after all, this is what makes having only one constructor practical):

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Bean(val data: Integer = 0)
```

{% raw %}
<p></p>
{% endraw %}

Now, constructors are even more convenient: in the generated byte code this class will get a <em>default constructor</em>, i.e. the one that takes no arguments (uses the default values for them). This case comes up a lot when using Java frameworks like JAXB, so now Kotlin is even more Java-friendly.
# Conclusion

You can download Kotlin M5 from the [plugin repository](http://plugins.jetbrains.com/plugin?pr=idea&pluginId=6954) . It requires [IntelliJ IDEA 12](http://www.jetbrains.com/idea/) (using recently released 12.0.3 is recommended).
**Have a nice Kolin!**
