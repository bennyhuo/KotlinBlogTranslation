---
title: "Call for Feedback: Upcoming Changes in Kotlin"
date: 2015-09-18 14:06:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-upcoming-changes-in-kotlin/
---

As mentioned before, we are wrapping up with the language design, and this post is a head-up for the upcoming changes + request for your feedback.<span id="more-2657"></span>
## Backing fields

I mentioned some time ago that we are not happy with the present syntax of backing fields, which is <code>$propertyName</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo = ...
    get() { beforeRead(); return $foo }
    set(v) { beforeWrite($foo, v); $foo = v }
 
```

{% raw %}
<p></p>
{% endraw %}

The biggest issue is that this syntax clashes with the syntax of [string templates](http://kotlinlang.org/docs/reference/basic-types.html#string-templates) .
So, we decided to change the rules here:

* the $foo syntax will be deprecated and then dropped
* instead, we can access the backing field by the name field inside getters/setters:


{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo = ...
    get() { beforeRead(); return field }
    set(v) { beforeWrite(field, v); field = v }
 
```

{% raw %}
<p></p>
{% endraw %}

Note that <code>field</code> is just an implicitly defined variable (very much like <code>it</code> in lambdas).
Some use cases are not supported by this approach: we used to be able to access backing fields anywhere in the class, and now it’s only visible in getters/setters. We have examined Kotlin code on GitHub, and realized that only a tiny fraction of use cases were not covered, and for these we can always resort to “backing property”:

{% raw %}
<p></p>
{% endraw %}

```kotlin
private var _foo = ...
public var foo: Foo
    get() = ...
    set(v) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

## Operators and infix functions

This has been debated a lot in the past, and we finally decided that we want to introduce some more discipline into how operator overloading and infix function calls work in Kotlin. At the moment any function named <code>plus</code> that can be called as <code>a.plus(b)</code> can also be called as <code>a + b</code>. We will require such functions to be marked with the <code>operator</code> modifier, otherwise the operator notation will not be available for them. This makes operator use more disciplined and eliminates the possibility of random punctuation creeping into APIs. The most common example would be having a method called <code>get</code> but totally not intending it for use as square brackets.
Same for infix function calls: we will require a function to be marked as <code>infix</code>. This will reduce the unintended diversity of styles in common APIs:

* list add 1 vs list.add(1)
* list map {...} vs list.map {...}
* etc

Infix functions will be still callable with the old standard syntax <code>x.or(y)</code>, but the tooling will be hinting to you that the intended syntax is infix.
Note that common functions in the standard library (e.g. <code>map</code> or <code>filter</code>) will not be marked as <code>infix</code>, because using them as such sometimes causes cryptic errors if such an expression is followed by a dot:

{% raw %}
<p></p>
{% endraw %}

```kotlin
list map {...}.toSet() // Error: toSet() is not applicable to a lambda
 
```

{% raw %}
<p></p>
{% endraw %}

If some Java method is not marked as <code>operator</code> or <code>infix</code>, we can always define an extension that is, and the standard library will provide such extensions for most popular cases.
## Constants

Compile-time constants are important when it comes to annotations: only they can be used as arguments (along with very few extra expressions, namely arrays and annotation constructors). So far we took the same “implicit” approach to detecting them as Java does: if a <code>val</code> in an <code>object</code> or on the top level only has only constants in its initializer, it is a compile-time constant. This is fragile and presents a possibility of breaking APIs without knowing, so we decided to require the <code>const</code> modifiers on such <code>val</code>s:

{% raw %}
<p></p>
{% endraw %}

```kotlin
const val SCREEN_WIDTH = 2048
 
```

{% raw %}
<p></p>
{% endraw %}

Note: <code>const</code> values can only have the following types: “primitives”, <code>String</code>, enums, class literals.
## invokeExtension() convention

This has been pretty obscure so far, but we are going to change it anyways. For now if a value needs to be callable as an extension function, it has to have a member that is an extension and is named <code>invoke</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    operator fun String.invoke() { ... }
}
 
fun test(foo: Foo) {
    "".foo()
}
 
```

{% raw %}
<p></p>
{% endraw %}

This is inconvenient in some cases, so we are going to change this to

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    operator fun invokeExtension(s: String) { ... }
}
 
fun test(foo: Foo) {
    "".foo()
}
 
```

{% raw %}
<p></p>
{% endraw %}

As a side-effect, it will be possible to add such function as an extension:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo
 
operator fun Foo.invokeExtension(s: String) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

## Internal visibility and mangling

Internal members are compiled to <code>public</code> at the moment, which may lead to accidental overrides:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// module X
 
open class Base {
    internal fun foo() {...}
}
 
// module Y
 
class Derived : Base() {
    fun foo() {...}
}
 
```

{% raw %}
<p></p>
{% endraw %}

The compiler will not require <code>override</code> on <code>Derived::foo</code> because the parent function is not visible, but in the byte code these have the same signature, and the runtime will bind them as overrides, which was not intended by the authors. The problem is most painful when modules X and Y evolve independently (e.g. one is a library and the other — user’s project), so that when Y is compiled <code>foo</code> was not yet present in <code>X</code>.
To avoid this, we decided to mangle names of internal members so that they do not clash with superclass members.
<strong>Update</strong>: mangling will likely cause this members to be impossible to call from Java. This seems to be hard to fix, but the workaround is straightforward: just make it <code>public</code> or <code>protected</code>.
## Other changes


* Default implementation classes for interfaces on Java 6 will be named Foo.DefaultImpls instead of Foo$$TImpl
* _, __, ___ will be forbidden as an identifiers, i.e. we can use _foo, but not _ alone (reserved for future use)
* We are going to drop final, protected and internal in interfaces: these can not be expressed on the JVM, so we postpone their implementation until later
* We are going to drop identityEquals() function in favor of ===

## Feedback

Your opinions and use cases are most welcome!
