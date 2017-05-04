---
title: "Upcoming Change: Syntax For Annotations"
date: 2015-04-03 13:13:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-change-syntax-for-annotations/
translator:
translator_url:
---

Kotlin’s syntax for annotations was inspired by C#, which surrounds them with square brackets:

{% raw %}
<p></p>
{% endraw %}

```kotlin
[Inject]
fun setFoo(foo: Foo) { ... }
```

{% raw %}
<p></p>
{% endraw %}

But brackets are precious for a language designer, and we would really like to use them later for something else, so we are considering changing the annotation syntax to the more Java-like `@`-based one:

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Inject
fun setFoo(foo: Foo) { ... }
```

{% raw %}
<p></p>
{% endraw %}

<strong>NOTE</strong>: the short syntax that does not require `[...]` nor `@` is going to be kept anyways, so you will still be able to say this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Foo
 
volatile var bar: Bar = ...
```

{% raw %}
<p></p>
{% endraw %}

This change has some implications, though.<span id="more-2021"></span>
## Labels

First of all, the `@`-syntax is already in use, for labels:

{% raw %}
<p></p>
{% endraw %}

```kotlin
@loop
for (i in 1..20) {
    if (enough(i)) break@loop
    println(i)
}
```

{% raw %}
<p></p>
{% endraw %}

Since expressions can be annotated as well as declarations, we need to change something here. The simplest option would be to move the `@` to the end of a label declaration:

{% raw %}
<p></p>
{% endraw %}

```kotlin
loop@
for (i in 1..20) {
    if (enough(i)) break@loop
    println(i)
}
```

{% raw %}
<p></p>
{% endraw %}

Note that the use site (`break@loop`) is not changed, and still looks pretty nice <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
## Targeting

We are also looking into how we could prescribe what an annotation should be attached to in the generated `.class`-file:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@Ann("arg") var foo: Int)
```

{% raw %}
<p></p>
{% endraw %}

We have quite a few options here: the `@Ann` annotation can be put on

* the field where foo is stored
* the property foo itself (not a Java declaration)
* getter of foo
* setter of foo
* parameter foo of the primary constructor of C

Some annotations are only applicable to, say, fields, and for those there’s no question, but some allow many possible targets. To express the intent, some additional syntax is needed.
One option would be to prefix the annotation type name with the target(s):

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@field:Ann("arg") var foo: Int)
```

{% raw %}
<p></p>
{% endraw %}

(many targets can be separated by a comma)
Another option would be to do what Scala does:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@(Ann@field)("arg") var foo: Int)
```

{% raw %}
<p></p>
{% endraw %}


* Downside: too many parentheses
* Upside: @field is also an annotation (yes, Ann is an annotated annotation), which means more extensible syntax and fewer concepts in the language

Yet another option would be to have `@field` annotation whose arguments are annotations for the field:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@field(@Ann("arg")) var foo: Int)
```

{% raw %}
<p></p>
{% endraw %}


* Upside: even fewer language changes than the previous case
* Downside: if the same annotation goes to two targets (e.g. getter and setter), it has to be duplicated

A modification of this approach:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@at(FIELD, @Ann1("arg"), @Ann2) var foo: Int)
class C(@atMany(array(FIELD, PROPERTY), @Ann1("arg"), @Ann2) var foo: Int)
```

{% raw %}
<p></p>
{% endraw %}

Then definitions are as follows:

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class at(val target: AnnotationTarget, vararg val annotations: Annotation)
annotation class atMany(val target: Array<AnnotationTarget>, vararg val annotations: Annotation)
```

{% raw %}
<p></p>
{% endraw %}

And, for completeness, yet another approach involves adding an explicit (optional) syntax for declaring fields (inside properties):

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Ann1("arg") @Ann2
val foo: Int = 1
    @Ann1("arg") @Ann2
    field _foo
    @GetterAnnotation
    get
```

{% raw %}
<p></p>
{% endraw %}


* Downside: There’s no way to mitigate duplication here
* Downside: It is likely to become an obscure piece of syntax (like $backingField) which is used rarely and supported poorly by tools

## Annotations on Local Declarations

Our users seem to often write something like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example() {
    data class Example(val foo: String, val bar: Int) // Error on this line
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

This does not parse correctly, because `data` is not a keyword (neither is `open`, btw), so we need to write it like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example() {
    @data class Example(val foo: String, val bar: Int) // OK
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

Now, what if I want an `open` local class, or `abstract`? Those are <em>modifiers</em>, not annotations, and we can’t say `@open` or `@abstract`.
One option is to allow escaping modifiers with `@` as well as annotations:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example() {
    @open class Example(val foo: String, val bar: Int)
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

Other options include allowing modifiers <em>on the same line</em> with the class, but this does not straightforwardly extend to functions, which are [expressions now](http://kotlinlang.org/docs/reference/lambdas.html#function-expressions) . See more [here](https://github.com/JetBrains/kotlin/blob/spec-at-based-annotations/spec-docs/at-based-annotation-syntax.md#reserving-space-for-future-syntactic-changes) ## Feedback Welcome

What do you think?
P.S. BTW, we are working on a spec document draft [here](https://github.com/JetBrains/kotlin/pull/624) 