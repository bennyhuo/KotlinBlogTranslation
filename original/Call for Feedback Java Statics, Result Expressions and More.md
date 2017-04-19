---
title: "Call for Feedback: Java Statics, Result Expressions and More"
date: 2015-09-25 18:27:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-java-statics-result-expressions-and-more/
---

Thank you all for the feedback we got on the [previous call](http://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-upcoming-changes-in-kotlin/) ! Here comes another round of changes and adjustments. Your opinions and use cases are welcome.<span id="more-2707"></span>
## Java Statics and Inheritance

We are going to improve interoperability with Java statics in Kotlin by allowing Kotlin subclasses to access static members of their superclasses: we will now be able to use constants, nested classes and static utilities defined up the inheritance tree. Same for members of companion objects of supertypes.
We will also allow calling Java statics on Java classes that inherit them.
What won’t be allowed is calling an inherited static member on a Kotlin class:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
public class Base {
    public static void foo() {}
}
 
// Kotlin
class Derived : Base() {
    fun test() {
        foo() // OK
        Base.foo() // OK
 
        Derived.foo() // ERROR!
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Lateinit val’s

With the help of our users we found that we have previously missed an unpleasant hole in the design of <code>lateinit val</code>: backing fields for such properties were not final, and thus Java code could modify them freely. That makes the <code>val</code>-ness of such properties vanish, because no code can ever assume any immutability on them, so we decided to take this feature back: from now on, only <code>var</code>s can be marked <code>lateinit</code>. We’ll keep thinking on use cases and improvements of this feature.
## Backing fields and custom setters

An addition to the previously announced  [change]()  in backing field syntax: if a property has a custom setter or is <code>open</code>, the setter may be reading the field before writing it, so there’s no syntax for initializing this property for the first time, unless it’s done upon declaration. So, we now require initializers for such properties:

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo? = makeFoo() // initializer required
    set(v) {
        if (field != null)
            notifyListeners()
        field = v
    }
 
```

{% raw %}
<p></p>
{% endraw %}

If we really need to initialize such a property in the constructor, we’d have to introduce a <em>backing property</em>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
private var _foo: Foo?
var foo: Foo?
    get() = _foo
    set(v) {
        if (_foo != null)
            notifyListeners()
        _foo = v
    }
 
init {
    _foo = ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Type parameter declarations

Historically, Kotlin had two forms of syntax for type parameter declarations for functions:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> T.foo() = ...
 
fun T.foo<T>() = ...
 
```

{% raw %}
<p></p>
{% endraw %}

Two is too many, so we decided to keep only the first one, because it places the declaration of <code>T</code> before its usages, which is easier to read and code completion will be more helpful.
## Visibilities of subclasses and elements of declarations

It’s a technical requirement, but rather intuitive: if something is <code>public</code>, it should not, for example, expose a <code>private</code> type:

{% raw %}
<p></p>
{% endraw %}

```kotlin
private open class Super
 
class Public : Super() {
    private class Private
 
    fun public(p: Private): Private = ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

From now on, public classes can’t extend private ones, and public members can’t expose private types.
More formally: a supertype or an element of a declaration must be (effectively) at least as visible as the declaration/class itself.
## Marking result expressions

This one is not really decided, and very debatable indeed, but it can’t be added after 1.0, so we have been thinking about it for some time:
As some of you [rightfully observed](https://youtrack.jetbrains.com/issue/KT-8695) , it may be difficult at times to see what expressions are used as results of blocks or lambdas.
We are considering prefixing such result expressions with the <code>^</code> symbol (or maybe some other prefix) to make them visible, in the following cases:

* expression is a result of a multi-line block or lambda, AND
* its type is not Unit, nor Nothing.

Example (from the Kotlin code base):

{% raw %}
<p></p>
{% endraw %}

```kotlin
val getter = target.getGetter() ?: run {
    val defaultGetter = DescriptorFactory.createDefaultGetter(target, Annotations.EMPTY)
    defaultGetter.initialize(target.getType())
    ^defaultGetter
}
 
```

{% raw %}
<p></p>
{% endraw %}

or

{% raw %}
<p></p>
{% endraw %}

```kotlin
private fun transformTryCatchBlocks(methodNode: MethodNode, newTryStartLabels: HashMap<LabelNode, LabelNode>) {
     methodNode.tryCatchBlocks = methodNode.tryCatchBlocks.map { tcb ->
         val newTryStartLabel = newTryStartLabels[tcb.start]
         ^if (newTryStartLabel == null)
             tcb
         else
             TryCatchBlockNode(newTryStartLabel, tcb.end, tcb.handler, tcb.type)
     }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Note that simply highlighting result expressions in the IDE is not really a solution:

* It does not prevent accidentally changing results of lambdas or block by adding a harmless-looking println() at the end,
* It doesn’t work on GitHub, in Terminal or anywhere outside the IDE

We did a quick experiment on the Kotlin codebase, and added all the necessary prefixes:
<p>
<a href="https://github.com/JetBrains/kotlin/compare/hats">See diff on github</a>
</p>
The diff above will give you a sense of what such code might look like.
To give you an idea of how often this will occur in the code: we got 493 lines changed out of about 230’000 lines of Kotlin code (0.21%), and 233 files were changed out of 2190 Kotlin files we have in our code base (every 10th file).
