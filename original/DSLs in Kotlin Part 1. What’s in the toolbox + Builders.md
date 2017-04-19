---
title: "DSLs in Kotlin: Part 1. What’s in the toolbox + Builders"
date: 2011-10-04 13:17:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/10/dsls-in-kotlin-part-1-whats-in-the-toolbox-builders/
---

If you have a <em>very nice</em> API, it is the fashion nowadays to call it an <em>internal DSL</em>, because the code that uses such an API reads almost like a language inside your language of choice. [Fluent interfaces](http://martinfowler.com/bliki/FluentInterface.html) serve as one of the most popular examples.
Many modern languages provide some advanced means for creating internal DSLs, and Kotlin is no exception here. In this post I will briefly list the features that are useful for this purpose.<br/>
<span id="more-181"></span>
Let’s start with [extension functions](http://confluence.jetbrains.net/display/Kotlin/Extension+functions) . We all are familiar with Java’s utility classes, like java.util.Collections and like. Such classes are simply containers for a bunch of static methods, which are intended to be used with such and such classes. So we end up writing code like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
Collection.sort(list);
int index = Collections.binarySearch(list, x);
```

{% raw %}
<p></p>
{% endraw %}

and this does not look very pretty. Static imports make it prettier, but they don’t solve an important problem of <em>discoverability</em>: we all navigate through APIs with IDE’s code completion capability:<br/>
<img alt="Code completion in IDEA" class="alignnone size-full wp-image-220" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2011/09/Screen-shot-2011-10-04-at-15.42.18-.png?resize=582%2C143&amp;ssl=1"/><br/>
And wouldn’t it be cool to discover those utility functions the same way? So we have <em>extension functions</em> that are called in the form “a.foo()” even if foo() is not a member of the class of a. For example, those utility functions from Collections could be defined as extension functions, and be called like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
list.sort();
val index = list.binarySearch(x);
```

{% raw %}
<p></p>
{% endraw %}

These are still statically dispatched utility functions, i.e. the bytecode emitted by the compiler is the same as in Java, but the syntax is better, and code completion works. Note that, unlike members, extension functions cannot be overridden in subclasses, i.e. some special implementation of List could not override sort() to be more efficient.
To define an extension function, we just put a receiver type in front of its name:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T : Comparable<T>> List<T>.sort() {
  Collections.sort(this)
}
```

{% raw %}
<p></p>
{% endraw %}

Note that I can use a ‘this’ reference that represents my receiver object. See more [here](http://confluence.jetbrains.net/display/Kotlin/Extension+functions) .
Now, what do extension functions give us, DSL creators? First of all you can turn any interface into a fluent one. For example, let’s create a new buffered reader with a given charset:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val reader = FileInputStream("mytext.txt").buffered().reader("utf-8")
```

{% raw %}
<p></p>
{% endraw %}

Is it a special class I wrote to be able to get this? No. It’s only two functions:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun InputStream.buffered() = BufferedInputStream(this)
fun InputStream.reader(charset : String) = InputStreamReader(this, charset)
```

{% raw %}
<p></p>
{% endraw %}

Then, they play very well together with [operator overloading](http://confluence.jetbrains.net/display/Kotlin/Operator+overloading) : in Kotlin, most operators, such as plus, minus and so on, are compiled by convention to named function calls. For example, when I say “a + b”, Kotlin reads “a.plus(b)” (see more in our [docs](http://confluence.jetbrains.net/display/Kotlin/Operator+overloading) ). This means that by adding an extension function named “plus” to my type I can have a binary ‘+’ working on it. For example, I could make my own ‘+’ for list concatenation:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun  List.plus(other : List) : List {
  val result = ArrayList(this)
  result.addAll(other)  
  return result
}
```

{% raw %}
<p></p>
{% endraw %}

And call it like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val l1 = list(1, 2, 3)
val l2 = list(4, 5, 6)
val l3 = l1 + l2 // a new list of length 6 is created
```

{% raw %}
<p></p>
{% endraw %}

And there’s more: since indexation is compiled to calls of get() and set() functions, we can have pretty sublists (or “slices”) that look like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val sublist = list[a..b]
```

{% raw %}
<p></p>
{% endraw %}

By defining an extension function get() on a list:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> List<T>.get(range : IntRange<Int>) : List<T>
    = subList(range.start, range.end)
```

{% raw %}
<p></p>
{% endraw %} [Infix function calls](http://confluence.jetbrains.net/display/Kotlin/Functions#Functions-Infixcalls) add more on top of that, because you can say, for example

{% raw %}
<p></p>
{% endraw %}

```kotlin
it hasPrivilege WRITE
```

{% raw %}
<p></p>
{% endraw %}

instead of

{% raw %}
<p></p>
{% endraw %}

```kotlin
it.hasPrivilege(WRITE)
```

{% raw %}
<p></p>
{% endraw %}

And, of course< you get a whole lot of fun with [higher-order functions](http://confluence.jetbrains.net/display/Kotlin/Functions#Functions-Higherorderfunctions) and [function literals (i.e. “closures”)](http://confluence.jetbrains.net/display/Kotlin/Function+literals) . For example, check this out:

{% raw %}
<p></p>
{% endraw %}

```kotlin
lock (myLock) {
  // Do something
}
```

{% raw %}
<p></p>
{% endraw %}

Is this a built-in construct, like Java’s <strong>synchronized</strong> section? No, it’s a function call. It uses a very handy convention: you can pass <em>the last function literal</em> outside the parentheses you put around your argument list. So this call is the same as “lock(myLock, {…})”, but looks prettier.
More about this example can be found [here](http://confluence.jetbrains.net/display/Kotlin/Functions#Functions-Inlinefunctions) .
There’s one other nice convention that makes something very close to LINQ possible:

{% raw %}
<p></p>
{% endraw %}

```kotlin
users
   .filter { it hasPrivilege WRITE }
   .map { it => it.fullName }
   .orderBy { lastName }
```

{% raw %}
<p></p>
{% endraw %}

The convention is: If a function with only one parameter is expected, the parameter declaration may be omitted, and the default name ‘it’ will be used. I.e. “filter {it.foo()}” is the same as “filter {it => it.foo()}”.
And finally, if we put all this (and just a tiny little bit more) together, we can get something really nice. Look at this code:

{% raw %}
<p></p>
{% endraw %}

```kotlin
html {
   head {
     title { +"XML encoding with Kotlin" }
   }
   body {
     h1 { +"XML encoding with Kotlin" }
     p { +"this format is now type-safe" }

     /* an element with attributes and text content */
     a(href="http://jetbrains.com/kotlin") { +"Kotlin" }
   }
}
```

{% raw %}
<p></p>
{% endraw %}

Is it Groovy? No, it’s Kotlin, and, unlike Groovy, it’s statically typed. Yes, we can do builders like Groovy, but better. <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/> I added a detailed explanation of this example to our wiki; you can find it [here](http://confluence.jetbrains.net/display/Kotlin/Type-safe+Groovy-style+builders) .
Have a question? Opinion? Suggestion? We really appreciate your comments!
