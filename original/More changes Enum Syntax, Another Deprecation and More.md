---
title: "More changes: Enum Syntax, Another Deprecation and More"
date: 2015-04-07 13:34:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/more-changes-enum-syntax-and-one-deprecation-and-more/
translator:
translator_url:
---


{% raw %}
<p><a name="enum-syntax"></a></p>
{% endraw %}

## Enum Syntax

Currently the syntax for enums with non-trivial constructors is kind of monstrous:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Message(val str: String) {
    ERROR : Message("This is an error")
    WARNING : Message("This is a friendly warning")
    DEBUG : Message("Ignore this")
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-2042"></span></p>
{% endraw %}

We would really like to make it nicer, e.g. something like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Message(val str: String) {
    ERROR("This is an error")
    WARNING("This is a friendly warning")
    DEBUG("Ignore this")
}
 
```

{% raw %}
<p></p>
{% endraw %}

Now, there are some technicalities, namely, enums can have other members:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example(...) {
    A(...)
    B(...)
 
    fun foo() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

The problem is that <code>A</code> and <code>B</code> can be parsed as annotations on <code>foo()</code>. So, we had some options to consider here.
We are leaning toward putting a separator there between entries and other members:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example(...) {
    A(...)
    B(...)
    ; // this is mandatory
 
    fun foo() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

The semicolon is only necessary when some members follow it.
Other options include requiring escaping on all annotations on members (and, possibly, modifiers too):

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example(...) {
    A(...)
    B(...)
 
    @inject fun foo() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

This would be a little inconsistent with normal classes, traits etc.
Or we could prefix enum entries with a (soft-)keyword:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example {
    entry A
    entry B
}
 
```

{% raw %}
<p></p>
{% endraw %}

This looks too verbose.
Another question here is how do we annotate enum entries themselves. Requiring escaping looks reasonable here:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example {
    @Ann1 A
    @Ann2(...) B    
}
 
```

{% raw %}
<p></p>
{% endraw %}

Other options include

* requiring a comma between enum literals (like in Java)
* requiring a newline between enum literals and allowing unescaped annotations on the same line

We have not decided which way to go on this one yet.

{% raw %}
<p><a name="break-continue"></a></p>
{% endraw %}

## Prohibiting break/continue in when-expressions

We are planning to implement <code>continue</code> in <code>when</code>-expressions as a jump to the next <code>when</code>-entry. It is not implemented yet, but we want your code to stay unchanged when we add it, so for the time being, we prohibit using <code>continue</code> in <code>when</code> without a label that points to a loop:

{% raw %}
<p></p>
{% endraw %}

```kotlin
loop@
for (...) {
    when (...) {
        ... -> if (...) continue@loop else ... // OK
        ... -> if (...) continue // ERROR
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

We also prohibit unlabeled <code>break</code> inside <code>when</code>. While it is not decided whether we want to allow it ever, it seems like a better design to keep <code>break</code> and <code>continue</code> symmetric.
NOTE: A simple interpretation of <code>break</code> inside <code>when</code> is “stop matching and jump outside” (as in <code>switch</code> in Java and C), but our <code>when</code> often returns a value, and that would be unknown if we break out of it.

{% raw %}
<p><a name="interfaces"></a></p>
{% endraw %}

## Rename traits to interfaces

Well, we picked the names long time ago, and now what we call “trait” in Kotlin is not so much of a trait, and is exactly like Java’s interface nowadays, so we want to deprecate the usage of the <code>trait</code> keyword, and introduce <code>interface</code> in M12.
Feedback request: Let the flame begin <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
