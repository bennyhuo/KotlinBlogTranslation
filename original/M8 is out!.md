---
title: "M8 is out!"
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

It’s been a really busy couple of months since the last release and we’ve been working hard on making substantial improvements, particularly in terms of speed. We have a lot of goodies for this release. Let’s get started<span id="more-1509"></span>
## JVM

### Reflection for properties

As a first peek into the future reflective capabilities of Kotlin, you can now access properties as first-class objects in Kotlin:

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

The “::propertyName” syntax gives a property object so you can get or set its value. You can also access the name of the property (will be useful for frameworks of all sorts). We will add more capabilities in the future.
To access a property that is a member of a class, you can say

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

And, of course, it works for extensions as well:

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

Another side of Kotlin’s reflection is its interoperability with Java’s reflection. For example, to find a backing field or a Java method that serves as a getter for a Kotlin property, you can say something like this:

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

We will develop reflection capabilities further in the next few months. The ultimate goal is to provide framework writers with really powerful tools for their needs. Things on the agenda include proper Kotlin class introspection, making types available through reflection, bringing reflection capabilities to callable references (::functionName) and more. Stay tuned.
### Inline Function Improvements

Some enhances for inlining functions including:

* Support for functions with default parameters.


* Inlines into objects are supported.

To demonstrate these two features together, let’s look at the following example. Say, we have an Value interface:

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

Now, let’s say we want to create values whose computations are guarded by a lock:

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

Our guardedValue() is an inline function. Now, the <b>lock</b> parameter has a default value (a new ReentrantLock is created for every value). Then, the object expression inside this function “captures” the <b>compute</b> parameter, and inlines it directly inside the anonymous class created. This results in only one class and one object emitted (and stored) per value, instead of two classes and two objects for the non-inline case.

{% raw %}
<p><a name="platformName"></a></p>
{% endraw %}

### Reporting platform signature clashes

The compiler now emits errors when some JVM signatures it generates are going to clash in the byte code (previously this could lead to ClassFormatError’s or to accidentally overriding a superclass’ method without knowing it).
For example, the following Kotlin code looks harmless, but breaks on the JVM:

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

Now, Kotlin complains about this code:

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

The reason is that the getter for <em>x</em> has the same name (getX) and signature (takes no parameters, returns Int) as the function declared next to it and JVM does not allow such things in class files.
Another case is an <em>accidental override</em>:

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

Here, the getter for x again has the same signature as getX(), but they are now in different classes, so the getter would silently override the function, so that Derived(2).getX() would return 2 instead of 1.
Now the compiler catches this and the error is

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

One may wonder why wouldn’t we, say, rename one of the functions automatically instead of emitting an error? The answers lie in the realm of Java interoperability (nobody likes names invented by the compiler) and binary compatibility (names of things must never change silently, or all dependent code will unexpectedly break). On the other hand, you can specify desired JVM names manually with the <em>platformName</em> annotation:

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

Note that nothing changes when for the Kotlin clients of this code, but Java clients must use the platform name (doGetX) instead of Kotlin name (getX).
<b>WARNING:</b> This is a <b>breaking</b> change, some of your existing code may need to be fixed.
### Support for transient, synchronized and strictfp

In addition to the long-available <em>volatile</em>. We now support <em>transient</em>, <em>synchronized</em> and <em>strictfp</em> as annotations. The semantics are exactly like in Java:

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

### Generated code speedup


* Generated code for delegated properties works much faster now, and make a lot fewer memory allocations.
* In addition when statements with constants are faster because of dedicated bytecode instructions now being used.

## JavaScript Support


* You now have Data Classes support in JavaScript. This means that you can now get toString, equals and hashCode generated automatically when annotating classes with the data annotation in JavaScript too, as well as in Java.
* In addition, LinkedHashSet and LinkedHashMap are also supported in JavaScript.

## Language Changes

A few language changes, all of which are <b>breaking changes</b>, so important to take note:

* private in a package now means private to the current package inside the module. Packages with the same name in other modules won’t see these definitions. Note that packages are nested, so privates are also visible to subpackages in the same module.
* Extension Properties cannot have backing fields. This was never recommended anyway.
* If you ever discovered that Kotlin allowed “@” and “@@” as label names, we are sorry to tell you that this is no longer so.

## Additions to Standard Library

The standard library gets some new functionality also:

* slice() function added that takes an iterable of integers and returns a list containing the elements in said positions.
* join() works on iterables (array, lists, etc.) of strings and combines them into one string
* joinToString() works on iterables or arrays of any type and is equivalent to .map { it.toString() }.join()
* Maps now have overloaded functions contains()., thus enabling things like “key in map” by convention
* Strings now can take advantage of collection like functions including


substringBefore, substringBeforeLast and substringAfter, substringAfterLast allowing to find string before and after a certain character or string.
replaceBefore, replaceBeforeLast and replaceAfter, replaceAfterLast allowing to replace strings before and after a certain character or string.
appendln added to StringBuilder
A new StringBuilder function that takes a String builder extensions, allowing for code such as:








    val information = StringBuilder {
        append("A first entry")
        appendln()
        appendln("Some other line")
    }




12345

    val information = StringBuilder {        append("A first entry")        appendln()        appendln("Some other line")    }
* substringBefore, substringBeforeLast and substringAfter, substringAfterLast allowing to find string before and after a certain character or string.
* replaceBefore, replaceBeforeLast and replaceAfter, replaceAfterLast allowing to replace strings before and after a certain character or string.
* appendln added to StringBuilder
* A new StringBuilder function that takes a String builder extensions, allowing for code such as:


* Iterables now have merge function which returns a new list containing elements merged from two collections on which a transformation has been applied

