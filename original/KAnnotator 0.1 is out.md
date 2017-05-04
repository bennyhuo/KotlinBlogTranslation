---
title: "KAnnotator 0.1 is out"
date: 2013-03-29 14:42:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/03/kannotator-0-1-is-out/
translator:
translator_url:
---

We announced KAnnotator back [in December](http://blog.jetbrains.com/kotlin/2012/12/kotlin-m4-is-out/) : it helps you against NPEs in Java and [makes your Kotlin code nicer](http://blog.jetbrains.com/kotlin/using-external-annotations/) . Today we are pleased to announce a KAnnotator Plugin for IntelliJ, version 0.1. It is available from the plugin repository.<span id="more-1005"></span>
## Why Infer Annotations

An excerpt from an earlier [blog post](http://blog.jetbrains.com/kotlin/2012/12/kotlin-m4-is-out/) , explaining what KAnnotator is:
<p><span style="font-size: 16px">Since Kotlin M3</span><span style="font-size: 16px">, you can use </span><a href="http://blog.jetbrains.com/kotlin/using-external-annotations/">external annotations</a><span style="font-size: 16px"> to tell the system that your methods return/take non-null values. This mechanism is useful even if you don’t use Kotlin: you can turn on </span><a href="http://www.jetbrains.com/idea/documentation/howto.html">nullability inspections for Java</a><span style="font-size: 16px"> too (and I totally recommend you to do so).</span></p>
<p>One problem about this used to be that, while you can annotate your own code while you write it (and we do it <a href="https://github.com/JetBrains/kotlin/blob/master/compiler/frontend/src/org/jetbrains/jet/lang/types/TypeConstructor.java">all</a> <a href="https://github.com/JetBrains/intellij-community/blob/master/platform/util/src/com/intellij/util/text/CharArrayUtil.java">the</a> <a href="https://github.com/JetBrains/la-clojure/blob/master/src/org/jetbrains/plugins/clojure/utils/ClojureUtils.java">time</a> at JetBrains), your favorite library is not annotated, and it is so big, you can’t annotate it manually.</p>
<p>The key thing here is that ‘manually’. A programmer is a lazy creature, and by virtue of our laziness, we want to automate as much as we can. **KAnnotator**is a tool that **annotates your libraries automatically** (the tool is written in Kotlin, of course).</p>
<p>How it works, in a nutshell: you have your library as a jar (or a number of jars), you tell KAnnotator to *infer* annotations for these jars, and get a bunch of .xml files back. They contain annotations for methods and fields, for example:</p>
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png"><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png?resize=409%2C149&amp;ssl=1"/></a></p>
<p>Now, you can attach these annotations to your project, and both Java IDE and Kotlin compiler will see them.</p>
We used KAnnotator to infer annotations for JDK that ship with Kotlin. Now you can use it as well: to annotate your own libraries.
## Install

KAnnotator ships as a separate plugin for [IntelliJ IDEA 12](http://www.jetbrains.com/idea/) or higher (both 12.0.4 and 12.1 will work). Note that the Kotlin plugin**is not required**.  To install the plugin, follow the instructions from [here](http://www.jetbrains.com/idea/plugins/index.html) .
## Infer

No you can call Analyze -> Annotate Jar Files… (from either Main menu or context menu)  <img alt="" data-recalc-dims="1" src="https://i2.wp.com/www.evernote.com/shard/s171/sh/8242aa4b-939b-416c-9880-6a6b97f748ce/add22424ad329409984c8f1df963bfde/res/902508da-cf33-453b-9790-c2af86cfa407/skitch.png?w=640&amp;ssl=1"/>
You get a dialog like this:

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s171/sh/7a64fc28-2eef-4fa5-ab4d-9c76d1e5b743/a39de23030a194a1c353d88bf08c88cf/res/764fc590-59e4-424a-9d63-134b9d15fd9c/skitch.png?w=640&amp;ssl=1"/></p>
{% endraw %}

There you specify what JAR files you want analyzed and where to put the results, i.e. XML files containing annotations. By default, KAnnotator will attach the annotation to the libraries you call it on.
## Enjoy

So, when you see Kotlin complaining about nullable types coming from Java, all you need to do is run KAnnotator once on that Java library, and it will turn your red code green.
If it does not, maybe KAnnotator is not smart enough, but maybe that method actually returns null?
