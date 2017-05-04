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
translator:
translator_url:
---

As mentioned before, we are wrapping up with the language design, and this post is a head-up for the upcoming changes + request for your feedback.<span id="more-2657"></span>
## Backing fields

I mentioned some time ago that we are not happy with the present syntax of backing fields, which is `$propertyName`:

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

Note that `field` is just an implicitly defined variable (very much like `it` in lambdas).
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

This has been debated a lot in the past, and we finally decided that we want to introduce some more discipline into how operator overloading and infix function calls work in Kotlin. At the moment any function named `plus` that can be called as `a.plus(b)` can also be called as `a + b`. We will require such functions to be marked with the `operator` modifier, otherwise the operator notation will not be available for them. This makes operator use more disciplined and eliminates the possibility of random punctuation creeping into APIs. The most common example would be having a method called `get` but totally not intending it for use as square brackets.
Same for infix function calls: we will require a function to be marked as `infix`. This will reduce the unintended diversity of styles in common APIs:

* list add 1 vs list.add(1)
* list map {...} vs list.map {...}
* etc

Infix functions will be still callable with the old standard syntax `x.or(y)`, but the tooling will be hinting to you that the intended syntax is infix.
Note that common functions in the standard library (e.g. `map` or `filter`) will not be marked as `infix`, because using them as such sometimes causes cryptic errors if such an expression is followed by a dot:

{% raw %}
<p></p>
{% endraw %}

```kotlin
list map {...}.toSet() // Error: toSet() is not applicable to a lambda
```

{% raw %}
<p></p>
{% endraw %}

If some Java method is not marked as `operator` or `infix`, we can always define an extension that is, and the standard library will provide such extensions for most popular cases.
## Constants

Compile-time constants are important when it comes to annotations: only they can be used as arguments (along with very few extra expressions, namely arrays and annotation constructors). So far we took the same “implicit” approach to detecting them as Java does: if a `val` in an `object` or on the top level only has only constants in its initializer, it is a compile-time constant. This is fragile and presents a possibility of breaking APIs without knowing, so we decided to require the `const` modifiers on such `val`s:

{% raw %}
<p></p>
{% endraw %}

```kotlin
const val SCREEN_WIDTH = 2048
```

{% raw %}
<p></p>
{% endraw %}

Note: `const` values can only have the following types: “primitives”, `String`, enums, class literals.
## invokeExtension() convention

This has been pretty obscure so far, but we are going to change it anyways. For now if a value needs to be callable as an extension function, it has to have a member that is an extension and is named `invoke`:

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

Internal members are compiled to `public` at the moment, which may lead to accidental overrides:

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

The compiler will not require `override` on `Derived::foo` because the parent function is not visible, but in the byte code these have the same signature, and the runtime will bind them as overrides, which was not intended by the authors. The problem is most painful when modules X and Y evolve independently (e.g. one is a library and the other — user’s project), so that when Y is compiled `foo` was not yet present in `X`.
To avoid this, we decided to mangle names of internal members so that they do not clash with superclass members.
<strong>Update</strong>: mangling will likely cause this members to be impossible to call from Java. This seems to be hard to fix, but the workaround is straightforward: just make it `public` or `protected`.
## Other changes


* Default implementation classes for interfaces on Java 6 will be named Foo.DefaultImpls instead of Foo$$TImpl
* _, __, ___ will be forbidden as an identifiers, i.e. we can use _foo, but not _ alone (reserved for future use)
* We are going to drop final, protected and internal in interfaces: these can not be expressed on the JVM, so we postpone their implementation until later
* We are going to drop identityEquals() function in favor of ===

## Feedback

Your opinions and use cases are most welcome!
