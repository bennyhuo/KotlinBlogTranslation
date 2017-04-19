---
title: "The Road Ahead"
date: 2012-01-16 10:10:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/01/the-road-ahead/
---

As you all know, we rolled out our first public release last week: [kotlin-demo.jetbrains.com](http://kotlin-demo.jetbrains.com/) . And while you (7K+ unique visitors) are having fun with it, we keep working on the Kotlin compiler, IDE and standard library.  In this post, I’ll give an overview of our plans.  <span id="more-365"></span> <strong></strong>
<strong>What you can play with today</strong>
Today you can already [try](http://kotlin-demo.jetbrains.com/) many features of Kotlin. Among others, these include:

* Function literals (closures)
* Extension functions and properties
* Traits (code in interfaces)
* Declaration site/Use site variance
* First-class delegation
* Compilation of mixed Java/Kotlin code

See [Kotlin Documentation](http://jetbrains.com/kotlin) for more details.
Using things for real problems reveals limitations, inconsistencies and other downsides of the design, and this is <strong>good</strong>, because then we can [fix them](http://blog.jetbrains.com/kotlin/2012/01/the-great-syntactic-shift/) . The point is to find and fix virtually everything there is <strong>before we release the 1.0 version</strong>. After the release, we won’t be able to introduce backwards incompatible changes, so fixing the language will be difficult. So, please, go try them, and <strong>give us your feedback</strong> in the comments below or in the [issue tracker](http://youtrack.jetbrains.net/issues/KT) .
<strong>What’s keeping us busy</strong>
<strong></strong> Currently we are stabilizing the existing features and work on the IDE and language infrastructure (building etc). The hottest topics of this month are:

* Modules: module = unit of compilation and dependency management;
* Ant and Maven integrations: use your favorite build infrastructure;
* Standard Library: utility functions for JDK collections, IO etc;
* JavaScript back-end: still very early prototype, but it’s improving.

<strong>ToDo</strong>
When playing with Kotlin it’s handy to know what’s not supported yet. The list is long, and some of these features may even wait for 2.0:

* Visibility checks: it’s a pity we don’t have those private, public etc. yet;
* Local functions: a function inside a function can be a very handy thing to have;
* Labeled tuples (aka records): to return many things from a function;
* KotlinDoc: like JavaDoc, but Markdown-based;
* Annotations: customizable metadata to enable compiler extensions;
* Secondary constructors: sometimes you need more than one;
* Enum classes (Algebraic data types): like Java enums, but better;
* Pattern matching: handy conditions over object structures;
* Inline functions: zero-overhead closures for custom control structures;
* Labels: break and continue for outer loops;
* Type aliases: to shorten long generics etc;
* Self-types: never write awkward recursive generics any more;
* Dynamic type: interoperability wi JavaScript and other dynamic languages;
* Eclipse plugin: Kotlin IDE != IntelliJ IDEA;
* LLVM back-end: compile Kotlin to native code…

Even without this stuff, you can have a lot of fun. Try out <strong>extension functions</strong> and <strong>closures</strong>, <strong>traits</strong> and <strong>string templates</strong> and much more. Solve the problems (we wil be adding more over time). [Have a nice Kotlin](http://kotlin-demo.jetbrains.com/) !
