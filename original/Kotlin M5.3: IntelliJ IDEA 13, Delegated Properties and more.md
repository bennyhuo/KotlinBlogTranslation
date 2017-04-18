---
title: "Kotlin M5.3: IntelliJ IDEA 13, Delegated Properties and more"
date: 2013-06-06 10:48:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/06/kotlin-m5-3-idea-13-delegated-properties-and-more/
---

Kotlin M5.3 brings support for IntelliJ IDEA 13 and some new features for you to check out. We are moving towards powerful runtime support, including reflection and other framework-enabling features. This milestone marks our first steps in that direction.  <span id="more-1060"></span>
## IntelliJ IDEA 12.1 and 13

First early access versions of  [IntelliJ IDEA 13](http://blogs.jetbrains.com/idea/2013/05/intellij-idea-13-early-preview-is-out/)  are coming out, and we ship a Kotlin plugin compatible with these versions. Remember it’s an EAP, use it at your own risk. Of course, good old  [IntelliJ IDEA 12.1](http://www.jetbrains.com/idea/download/)  is supported as well.
<strong>Note</strong>: Some news about Kotlin support in  [Android Studio](http://developer.android.com/sdk/installing/studio.html)  are coming soon.
## Many Improvements

As usual M5.3 brings many improvements both in the compiler and the IDE. In the compiler we are still mostly concerned with performance, which is gradually improving. The IDE gets new quick fixes and refactorings, some of which are described below. You can now navigate to properties overriding the one you are looking at (see icons in the left gutter). The editor recognizes the syntax of  [KDoc](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Doc)  (thanks to  [this pull request](https://github.com/JetBrains/kotlin/pull/280) )… But first, let’s talk about cool new language features, some long awaited, some unexpected (maybe).
## New Language Feature: Delegated Properties

We often get feature requests like:

* Support lazy properties: the value gets computed only upon first access.
* Support observable properties: listeners get notified about changes to this property.
* Support storing properties in a map, not in separate field each.
* Support <my favorite kind of property semantics>…

One way of addressing these requests would be to say that life is tough and users have to suffer. Another way would be to support different kinds of properties on the language level. We do not like either of these approaches: too many unhappy users on the one hand, too many ad hoc features on the other hand. So, we take a third approach: support a unified mechanism that covers all these requests (and probably more), so that particular kinds of properties can be implemented in libraries, without altering the language.
Meet <strong>delegated properties</strong>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example {
  var p: String by Delegate()
}
```

{% raw %}
<p></p>
{% endraw %}

There’s some new syntax: you can say “val <property name>: <Type> by <expression>”. The expression after <strong>by</strong> is the <em>delegate</em>, because get() and set() methods corresponding to the property will be delegated to it.  Property delegates don’t have to implement any interface, but they have to provide methods named get() and set() to be called. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Delegate() {
  fun get(thisRef: Any?, prop: PropertyMetadata): String {
    return "$thisRef, thank you for delegating '${prop.name}' to me!"
  }
 
  fun set(thisRef: Any?, prop: PropertyMetadata, value: String) {
    println("$value has been assigned")
  }
}
```

{% raw %}
<p></p>
{% endraw %}

When we read from p, the get() function from Delegate is called, so that its first parameter is the object we read p from and the second parameter holds a description of p itself (e.g. you can take its name). For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val e = Example()
println(e.p)
```

{% raw %}
<p></p>
{% endraw %}

This prints “Example@33a17727, thank you for delegating ‘p’ to me!” Similarly, when we assign to p, the set() function is called. The first two parameters are the same, and the third hold the value being assigned:

{% raw %}
<p></p>
{% endraw %}

```kotlin
e.p = "NEW"
```

{% raw %}
<p></p>
{% endraw %}

This prints “NEW has been assigned to ‘p’ in Example@33a17727”.
Probably, you already see how to implement things like lazy or observable with this mechanism. Try it as a metter of exercise, but most of it is already done in the  [standard library](https://github.com/JetBrains/kotlin/blob/build-0.5.742/libraries/stdlib/src/kotlin/properties/Delegation.kt) .
The  [kotlin.properties.Delegates](https://github.com/JetBrains/kotlin/blob/build-0.5.742/libraries/stdlib/src/kotlin/properties/Delegation.kt#L12)  object holds the most useful stuff. Let’s start with lazy:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.properties.Delegates
 
class LazySample {
    val lazy: String by Delegates.lazy {
        println("computed!")
        "Hello"
    }
}
```

{% raw %}
<p></p>
{% endraw %}

Delegates.lazy() is a function that returns a delegate that implements a lazy property: the first call to get() executes the lambda expression passed to lazy() as an argument and remembers the result, subsequent calls to get() simply return the remembered result. If you want <strong>thread safety</strong>, use blockingLazy() instead: it guarantees that the values will be computed only in one thread, and that all threads will see the same value.
Now, let’s turn to observable:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class User {
    var name: String by Delegates.observable("<no name>") {
        d, old, new ->
        println("$old -> $new")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

The observable() function takes two arguments: initial value and a handler for modifications. The handler gets called every time we assign to ‘name’, it has three parameters: a property being assigned to, the old value and the new one. If you want to be able to ‘veto’ the assignment, use vetoable() instead of observable().
Next may be somewhat unexpected: users frequently ask what to do when you have a non-null var, but you don’t have an appropriate value to assign to it in constructor (i.e. it must be assigned later)? You can’t have an uninitialized non-abstract property in Kotlin:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
  var bar: Bar // error: must be initialized
}
```

{% raw %}
<p></p>
{% endraw %}

You could initialize it with null, bit then you’d have to check every time you access it. Now you have a delegate to handle this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
  var bar: Bar by Delegates.notNull()
}
```

{% raw %}
<p></p>
{% endraw %}

If you read from this property before writing to it, it throws an exception, after the first assignment it works as expected.
The last thing to show is properties stored in a map. This comes up a lot in applications like parsing JSON or doing other “dynamic” stuff:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class User(val map: Map<String, Any?>) {
    val name: String by Delegates.mapVal(map)
    val age: Int     by Delegates.mapVal(map)
}
```

{% raw %}
<p></p>
{% endraw %}

In this example, the constructor takes a map:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val user = User(mapOf(
    "name" to "John Doe",
    "age"  to 25
))
```

{% raw %}
<p></p>
{% endraw %}

Delegates take values from this map (by the string keys – names of properties):

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(user.name) // Prints "John Doe"
println(user.age)  // Prints 25
```

{% raw %}
<p></p>
{% endraw %}

Of course, you can have var’s as well (with mapVar() function), that will modify the map upon assignment (note that you’d need MutableMap instead of read-only Map).
There are other use cases, and probably numerous improvements to these ones. Fantasize, experiment, enjoy! 😉

{% raw %}
<p><a name="SAM-conversions"></a></p>
{% endraw %}

## First Steps in SAM Conversions

We introduced  [SAM constructors](http://blog.jetbrains.com/kotlin/2013/04/kotlin-m5-2-intellij-idea-12-1-and-gradle/)  last time. Of course, this is not enough, so we are working on full SAM conversions. The feature is not finished yet, but you can already use it in simple case like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater {
  button.setVisible(true)
}
```

{% raw %}
<p></p>
{% endraw %}

To remind you, SAM conversions is what Java 8 uses for lambdas: when you have an interface with only one (abstract) method, like Comparator or Runnable, you are allowed to pass in a lambda where an instance of this interface is expected (in this example we pass a lambda instead of a Runnable). Kotlin does not have this as a language feature (for it is not needed in a language with proper function types), so it will only work for Java classes.
## First Steps in “Callable References”

Another thing we are working on is “Callable References” or “Feature Literals”, i.e. an ability to pass named functions or properties as values. Users often ask “I have a foo() function, how do I pass it as an argument?”. The answer is: “you prefix it with a ‘::'”. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun isOdd(x: Int) = x % 2 != 0
 
val numbers = listOf(1, 2, 3)
println(numbers.filter(::isOdd)) // Prints [1, 3]
```

{% raw %}
<p></p>
{% endraw %}

Here “::isOdd” is a value of function type “(Int) -> Boolean”, and you can pass it as a filtering predicate. Another example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun compose<A, B, C>(f: (B) -> C, g: (A) -> B): (A) -> C {
    return {x -> f(g(x))}
}
```

{% raw %}
<p></p>
{% endraw %}

This function return a composition of two functions passed to it: compose(f, g) = f(g(*)). Now, you can apply it to callable references:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun length(s: String) = s.size
 
val oddLength = compose(::isOdd, ::length)
val strings = listOf("a", "ab", "abc")
println(strings.filter(oddLength)) // Prints "[a, abc]"
```

{% raw %}
<p></p>
{% endraw %}

If you want to use a member of a class, you need to qualify it, and the result will be of type “extension function”,  e.g. String::toCharArray gives you an extension function for type String.
Note that this is <strong>early work in progress</strong>, so many things do not work yet, for example, overload disambiguation, type inference, support for properties etc. Eventually this feature will evolve into full type-safe reflection, but today we are only starting working on it.
## Change Signature Refactoring

Adding/removing/reordering function parameters may be tedious when you have a lot of call sites to update. That’s why IDEs prove a “Change Signature” refactoring. Place your cursor on a function or a constructor and hit Ctrl+F6 (Cmd+F6 on Mac), and you’ll get a dialog like this:

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s171/sh/b4eb0e6e-b866-4a12-83f9-b94ed3daf8d9/1ec5d8ee74c94a7c6433813dd3c488e9/deep/0/Screenshot%206/5/13%206:42%20PM.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

Change type, rename, reorder or delete parameters and all your call sites will be updates accordingly.
## Quick Fixes for “Type Mismatch” etc

Thanks to contributions by  [Jack Zhou](https://github.com/univerio) ,  [Michał Sapalski](https://github.com/sapal) ,  [Wojciech Łopata](https://github.com/lopekpl)  and other students of Open Source Mentorship program led by Stanford University, we now get many cool quick fixes. For example, when you get a type mismatch error, hit Alt+Enter and get some proposals to fix your code:

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s171/sh/ff9bd33c-ecd1-4800-91f2-4a69db761a37/f829b15d7de80df501e39b64f6973754/deep/0/Screenshot%206/5/13%206:51%20PM.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

## Code Transformations

Another group of useful IDE actions to convert between equivalent forms of code, like:<br/>
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/Cfwq-pYtiDY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span>
You can also use Ctrl+Shift+Up/Down to move statements or declarations:

{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/RRRROZc3-2g?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## Installation

As usual, the new plugin can be installed from  [our plugin repository](http://plugins.jetbrains.com/plugin?pr=idea&pluginId=6954) .
<strong>Have a nice Kotlin!</strong>
