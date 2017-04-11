---
title: Modifiers vs Annotations
date: 2015-08-11 17:47:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/08/modifiers-vs-annotations/
---

This is another heads-up and a call for feedback. We have been discussing options regarding Kotlin’s annotation syntax for quite some time already, rolling out experiments, gathering feedback. As we are finalizing the language now, many pain points that we used to postpone are surfacing. We have to make decisions, and sometimes in a defensive way. In this post I will give an overview of the options we have and the decisions we are provisioning.
## Setting the stage: Some introductory definitions

Kotlin (as well as many other languages) has two kinds of metadata:

* modifiers (such as public, open or abstract), which are built into the language, and
* annotations (such as @Test or @Inject), which are defined in libraries, also they can have parameters.

Unlike many languages, in Kotlin most modifiers are not proper keywords. They have special meaning only where they are applicable, i.e. in front of a declaration. The compiler won’t mind if you call your variable or class public:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val public = "PUBLIC!"
println(public)
 
```

{% raw %}
<p></p>
{% endraw %}

This technique is known as “soft keywords” or “contextual keywords”.
## The dream: Unified metadata

When Kotlin was conceived I personally was fascinated with the idea of unified metadata: I thought that we should reach a point where there’s no distinction between modifiers and annotations. All metadata should be declared explicitly, and treated equally. It is uniform, extensible and otherwise great! Both language designers and users can define annotations and extend the language thereof. In my ideal world there would be no modifiers, only annotations, i.e. public would be an annotation, as well as inline, abstract, enum etc.
Then it turned out that technically it was a lot easier to introduce modifiers (and not annotations) at the early stage of the language implementation, so we did that as a temporary measure.
This is why Kotlin allows annotations without @: I wanted them to look like modifiers to be able to turn modifiers into annotations later. Many things that you might have thought were modifiers are actually annotations: data and inline are the most popular ones.
## The reality: Tooling matters

Now, I have to admit that my dream of unified metadata, while not entirely impossible to implement, turned out to be impractical.
Modifiers have a peculiar property of being available right after the parsing stage. And this is important to some performance-critical tasks (e.g. in the IDE), because they sometimes rely on knowing, for example, what’s public and what’s not in contexts where nothing is ready but a parsed text.
So, modifiers have to stay.
## Annotation syntax

Now, the initial idea is challenged: if we don’t unify modifiers and annotations, is there a point in keeping their syntax so similar?
On the one hand, it looks kind of cool that we can omit the “@” before annotations. One can argue that it reduces the amount of “noise” in the code.
On the other hand, there are a bunch of problems, none of which is really critical, but they are annoying enough:
First, it is not orthogonal: we can either use “@” in front of annotations or not. It’s a matter of convention most of the time. But sometimes we have to use “@”: local classes and functions are the most notorious example.
Then, it complicates error recovery: it’s alright when the code is correct, but when you are typing in the IDE, the parser must be able to recover from errors and recognize the code structure on incomplete code. And random identifiers being parseable as annotations complicate this quite a bit.
Also, it complicates naming conventions: we used to name annotations with the first letter in the lower case, like @inline or @platformStatic. Many people find camel-case multi-word names like the latter one ugly in this context. So, there are proposals to use lowercase only for one-word annotations (that look like modifiers then). And also Java annotations (many of which are used frequently) are still named with the upper case first letter. Altogether, it’s a mess. A small one, but still a mess.
And a more technical, but nevertheless realistic concern: it complicates language evolution. We can’t add a new modifier “foo” to the next version of Kotlin without possibly breaking someone’s code: if some library has an annotation foo, it will clash, and the best the compiler can do is report an error.
So, we think that the benefit is too little for the cost.
## Rich modifiers

Incidentally, we think that it would make sense to allow modifiers to have parameters when needed. It facilitates language evolution (we can add optional parameters to existing modifiers later) and doesn’t seem to introduce any problems. For example, annotation is a modifier (it is critical to know annotation classes before resolving names), but it has parameters:

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation(repeatable = true) class MyRepeatableAnnotation
 
```

{% raw %}
<p></p>
{% endraw %}

## Conclusion

We are going to require all annotations to be prefixed with “@”.
Incidentally, some annotations will be turned into modifiers: for example, data and inline.
Your feedback is welcome: we would like to know if we are missing something here, in your opinion.
Special thanks to the author and contributors to this forum thread.
