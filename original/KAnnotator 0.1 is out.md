---
title: KAnnotator 0.1 is out
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
---

We announced KAnnotator back in December: it helps you against NPEs in Java and makes your Kotlin code nicer. Today we are pleased to announce a KAnnotator Plugin for IntelliJ, version 0.1. It is available from the plugin repository.
## Why Infer Annotations

An excerpt from an earlier blog post, explaining what KAnnotator is:
Since Kotlin M3, you can use external annotations to tell the system that your methods return/take non-null values. This mechanism is useful even if you don’t use Kotlin: you can turn on nullability inspections for Java too (and I totally recommend you to do so).
One problem about this used to be that, while you can annotate your own code while you write it (and we do it all the time at JetBrains), your favorite library is not annotated, and it is so big, you can’t annotate it manually.
The key thing here is that ‘manually’. A programmer is a lazy creature, and by virtue of our laziness, we want to automate as much as we can. KAnnotator is a tool that annotates your libraries automatically (the tool is written in Kotlin, of course).
How it works, in a nutshell: you have your library as a jar (or a number of jars), you tell KAnnotator to infer annotations for these jars, and get a bunch of .xml files back. They contain annotations for methods and fields, for example:

Now, you can attach these annotations to your project, and both Java IDE and Kotlin compiler will see them.
We used KAnnotator to infer annotations for JDK that ship with Kotlin. Now you can use it as well: to annotate your own libraries.
## Install

KAnnotator ships as a separate plugin for IntelliJ IDEA 12 or higher (both 12.0.4 and 12.1 will work). Note that the Kotlin plugin is not required.  To install the plugin, follow the instructions from here.
## Infer

No you can call Analyze -> Annotate Jar Files… (from either Main menu or context menu)
You get a dialog like this:

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s171/sh/7a64fc28-2eef-4fa5-ab4d-9c76d1e5b743/a39de23030a194a1c353d88bf08c88cf/res/764fc590-59e4-424a-9d63-134b9d15fd9c/skitch.png?w=640&amp;ssl=1"/></p>
{% endraw %}

There you specify what JAR files you want analyzed and where to put the results, i.e. XML files containing annotations. By default, KAnnotator will attach the annotation to the libraries you call it on.
## Enjoy

So, when you see Kotlin complaining about nullable types coming from Java, all you need to do is run KAnnotator once on that Java library, and it will turn your red code green.
If it does not, maybe KAnnotator is not smart enough, but maybe that method actually returns null?
