---
title: "Upcoming Change: “Class Objects” Rethought"
date: 2015-03-11 16:11:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/upcoming-change-class-objects-rethought/
translator:
translator_url:
---

<strong>Kotlin M11</strong> is coming very soon, and as some of you [expressed concerns](https://devnet.jetbrains.com/thread/461012?tstart=0) about being informed about the upcoming changes, I will describe one of the features of M11 and ask you for some <strong>feedback</strong>. <span id="more-1817"></span>
## Class Objects: a short reminder

As you all know, any Kotlin class can have an associated [class object](http://kotlinlang.org/docs/reference/classes.html#class-objects) :

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    class object {
        fun classObjectMember() {}
    }
 
    fun classMember() {}
}
```

{% raw %}
<p></p>
{% endraw %}

Members of a <em>class object</em> are roughly analogous to <em>static members</em> of Java/C# classes, as they can be called on the class name:

{% raw %}
<p></p>
{% endraw %}

```kotlin
KotlinClass.classObjectMember()
```

{% raw %}
<p></p>
{% endraw %}

(You can even use the `[platformStatic]` annotation to make those member actually `static` when seen from Java.)
In fact, Kotlin’s <em>class objects</em> and Java’s statics are not at all the same, because <em>class objects are <strong>objects</strong></em>, i.e. they can extend classes, implement traits and serve as <em>values</em> at runtime:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = KotlinClass // reference to class object of KotlinClass is assigned to x
```

{% raw %}
<p></p>
{% endraw %}

## Terminology Change

As you might have noticed, the term “class object” sounds a little ambiguous in English, and this is why many people tend to think that class object of `Foo` must be an instance (in other words, object) of `Foo`, which is totally not so. This, among other reasons, is why we are looking for another term and syntax. The current proposal has it as follows:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    default object {
        fun defaultObjectMember() {}
    }
 
    fun classMember() {}
}
```

{% raw %}
<p></p>
{% endraw %}

So, what used to be called “class objects” will now be called “default objects”.
More motivation is coming below, but at this point, please note how you feel about this change: is it better now? more confusing? about the same as before?<br/>
<strong>Please share your opinion in the comments below, now, before reading the motivation. Thanks a lot!</strong>

{% raw %}
<p><a name="why-default-objects"></a></p>
{% endraw %}

## Why Default Objects

<strong>NOTE</strong>: all syntax presented here is <strong>provisional</strong> (we have it implemented, but might decide to change it before M11).
The unfortunate wording is not the only reason for this change. In fact, we redesigned the concept so that it is more uniform with normal objects.
Note that a class can (and always could) have many objects (usual, named singletons) nested into it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    object Obj2 { ... }
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

Now, one of these objects may be declared with the `default` modifier, which means that its members can be accessed directly through class name, i.e. <em>by default</em>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    default object Obj2 { ... }
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

Accessing members of `Obj1` requires qualification: `KotlinClass.Obj1.foo()`, for members of `Obj2` the object name is optional: `KotlinClass.foo()`.
One last step: the name of a <em>default object</em> can be omitted (the compiler will use the default name `Default` in this case):

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    default object { ... }
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

Now you can still refer to its members though the name of the containing class: `KotlinClass.foo()`, or through full qualification: `KotlinClass.Default.foo()`.
As you can see, unlike what we used to have with <em>class objects</em>, <em>default objects</em> are completely uniform with normal objects.
Another important benefit is that now every object <em>has a name</em> (again, `Default` is used when the name of a <em>default object</em> is omitted), which enables <strong>writing extension function for default objects</strong>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun KotlinClass.Default.bar() { ... }
```

{% raw %}
<p></p>
{% endraw %}

This can be called as `KotlinClass.bar()`. This is how we implement platform-specific extensions for built-in classes like `Int`: e.g. `Int.MAX_VALUE` is an extension for `Int.Default` defined only on the JVM (JS ony has floating-point numbers, so `Int.MAX_VALUE` is meaningless there).
## Summary


* We are changing the syntax and conceptual load of what was formerly known as “class objects”: they are now default objects.

The old syntax will be deprecated and kept around for a while, so that you can migrate your code (in which the IDE will assist you).
* The old syntax will be deprecated and kept around for a while, so that you can migrate your code (in which the IDE will assist you).
* The new concept is uniform with normal named objects.
* You can now write extensions to default objects that can be called on class names.

<strong>Your feedback is very welcome!</strong> A large part of this change is about terminology and wording, so if you think the new concept is confusing is some way, please tell us in the comments.
