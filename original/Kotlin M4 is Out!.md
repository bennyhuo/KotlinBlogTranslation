---
title: "Kotlin M4 is Out!"
date: 2012-12-11 09:15:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/12/kotlin-m4-is-out/
translator:
translator_url:
---

Today we roll out Kotlin M4 (from under [snow](http://www.google.ru/imgres?um=1&hl=en&newwindow=1&sa=N&tbo=d&biw=1320&bih=1106&tbm=isch&tbnid=q5-uJPbVI3jRFM:&imgrefurl=http://mr-stroy.com/news/498/45&docid=hUulWRZZmtitkM&imgurl=http://mr-stroy.com/uploads/images/sneg-spb.jpg&w=784&h=500&ei=sG28UMayC4nZ4QT22IDYCw&zoom=1&iact=hc&vpx=4&vpy=288&dur=1347&hovh=179&hovw=281&tx=179&ty=150&sig=101271244132511519226&page=1&tbnh=139&tbnw=206&start=0&ndsp=36&ved=1t:429,r:6,s:0,i:102) ). This post gives an overview of new features and other things this milestone brings.<span id="more-731"></span>
# Improvements Here and There

Kotlin M4 is **JDK7-friendly**: we still generate Java6-compatible byte codes, but some issues related to compiling against JDK7 are now fixed.
**Type argument inference** has been improved even more, it is now **faster**, and more speedups are coming.
**Code completion** has been improved in many ways, too. Enjoy <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
Overall, it is [128 issues](http://youtrack.jetbrains.com/issues/KT?p=0&q=%23Resolved+resolved+date%3A+2012-10-11+..+2012-12-01&f=false) closed since [M3.1](http://blog.jetbrains.com/kotlin/2012/10/dogfooding-kotlin-and-m3-1/) was out.
# KAnnotator: Annotate the world

Since [M3](http://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/) , you can use [external annotations](http://blog.jetbrains.com/kotlin/using-external-annotations/) to tell the system that your methods return/take non-null values. This mechanism is useful even if you don’t use Kotlin: you can turn on [nullability inspections for Java](http://www.jetbrains.com/idea/documentation/howto.html) too (and I totally recommend you to do so).
One problem about this used to be that, while you can annotate your own code while you write it (and we do it [all](https://github.com/JetBrains/kotlin/blob/master/compiler/frontend/src/org/jetbrains/jet/lang/types/TypeConstructor.java) [the](https://github.com/JetBrains/intellij-community/blob/master/platform/util/src/com/intellij/util/text/CharArrayUtil.java) [time](https://github.com/JetBrains/la-clojure/blob/master/src/org/jetbrains/plugins/clojure/utils/ClojureUtils.java) at JetBrains), your favorite library is not annotated, and it is so big, you can’t annotate it manually.
The key thing here is that ‘manually’. A programmer is a lazy creature, and by virtue of our laziness, we want to automate as much as we can. And today, along with Kotlin M4, we roll out **KAnnotator**: a tool that **annotates your libraries automatically** (the tool is written in Kotlin, of course).
How it works, in a nutshell: you have your library as a jar (or a number of jars), you tell KAnnotator to *infer* annotations for these jars, and get a bunch of .xml files back. They contain annotations for methods and fields, for example:
<img alt="" class="aligncenter size-full wp-image-740" data-recalc-dims="1" sizes="(max-width: 409px) 100vw, 409px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png?resize=409%2C149&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png?resize=300%2C109&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/annotations.xml_.png?w=409&amp;ssl=1 409w"/>Now, you can attach these annotations to your project, and both Java IDE and Kotlin compiler will see them.
KAnnotator is **just started**, and it will grow much smarter, but today we already have a full JDK annotated with it, available in the new Kotlin plugin. It will propose to add them to your JDK once you open any Kotlin file in the editor:

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png"><img alt="" class="aligncenter size-full wp-image-742" data-recalc-dims="1" sizes="(max-width: 610px) 100vw, 610px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?resize=610%2C53&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?resize=300%2C26&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/JDK-annotations-1.png?w=610&amp;ssl=1 610w"/></a></p>
{% endraw %}

# Copy Your Data

Kotlin M3 introduced [data classes](http://blog.jetbrains.com/kotlin/2012/09/how-do-you-traverse-a-map/) , a nice way to represent your data. A popular request was to be able to copy an instance of a data class and selectively **change** some of its properties, **while keeping the object immutable**.
In Kotlin M4 you can do this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Person(val firstName: String, val lastName: String)
 
fun Person.asMarried(newLastName: String)
         = this.copy(lastName = newLastName)
```

{% raw %}
<p></p>
{% endraw %}

Every data class gets a copy() function that has *default values* for all parameters, so that you can specify only those ones you want to change. Since Kotlin supports *named arguments*, all you need to do is say ‘copy(property1 = v1, property3 = v2)’, and all the other properties will be copied, while ‘property1’ and ‘property3’ will be changed.
# Declaration-site variance in… Java

There will be a separate post on this, but I’ll give a short announcement here. We all know that Java makes you write ‘List<? extends Foo>’ [whenever you don’t mean to modify that list](http://www.eecs.qmul.ac.uk/~mmh/APD/bloch/generics.pdf) . As you [know](http://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/) , Kotlin has declaration-site variance and read-only interfaces for collections, so that ‘List<String>’ can go where ‘List<Object>’ is expected. Now, when you have this function in Kotlin:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun join(l: List<Any>, separator: String): String = ...
```

{% raw %}
<p></p>
{% endraw %}

you can pass any list in, but what if you want to call it **from Java**?
In M4, Kotlin generates the following Java signature for this function:

{% raw %}
<p></p>
{% endraw %}

```kotlin
String join(List<? extends Object>, String separator)
```

{% raw %}
<p></p>
{% endraw %}

Which makes it possible to pass it a list of strings **even from Java code**.
If you could never get those wildcards right, there’s an answer now: write plain Kotlin and call it from Java <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
# Support for Deprecation

Some design decisions are good and some are not. Some were good when they came about, but are not so good any more… We need to be able to **deprecate** things. Kotlin M4 supports the ‘deprecated’ annotation that, unlike Java’s @Deprecated, **requires** a string parameter that tells you what you should do instead of using this method/class.
For example, in this milestone we deprecate arrayList(…), hashSet(…) and other such functions in the standard library, because we found that they are confusing:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val c: List<Node> = node.getChildren()
ArrayList(c) // a copy of that list
arrayList(c) // a list containing that list, [c]
```

{% raw %}
<p></p>
{% endraw %}

The case of one letter changes the meaning dramatically. That’s why now arrayList() is deprecated, and new arrayListOf() is available. There’s also a new list() function that also creates an array list, but returns it by a read-only reference. So now the declaration of arrayList() looks like this:
<img alt="" class="aligncenter size-full wp-image-773" data-recalc-dims="1" sizes="(max-width: 564px) 100vw, 564px" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/12/arrayList-1.png?resize=564%2C42&amp;ssl=1" srcset="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/12/arrayList-1.png?resize=300%2C22&amp;ssl=1 300w, https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/12/arrayList-1.png?w=564&amp;ssl=1 564w"/><br/>
And if you have it used somewhere, the call site will tell you that something is wrong, and what you should do:

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png"><img alt="" class="aligncenter size-full wp-image-745" data-recalc-dims="1" sizes="(max-width: 617px) 100vw, 617px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?resize=617%2C79&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?resize=300%2C38&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/deprecated.png?w=617&amp;ssl=1 617w"/></a></p>
{% endraw %}

# IDE Improvements

**Run All Tests in a Directory.**Now IntelliJ IDEA can discover tests written in Kotlin, so that you can run all tests in directory/package: Java ones as well as Kotlin ones.
**Debugger.**Many fixes including receivers of extension functions/properties are now visible in the Variables view.
**New Make Procedure.** IntelliJ IDEA 12 brings a new implementation of make. Kotlin M4 adds support for it, and this support will eventually develop into an **incremental compiler** for Kotlin.
**Kotlin Home Page**now features a unified search box that aggregates the docs, forum, tracker, source code and whatnot.

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png"><img alt="" class="aligncenter size-full wp-image-747" data-recalc-dims="1" sizes="(max-width: 690px) 100vw, 690px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png?resize=640%2C318&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png?resize=300%2C149&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/12/Search.png?w=690&amp;ssl=1 690w"/></a></p>
{% endraw %}

It is temporarily limited by 100 searches per day, but this limit will be removed soon.
# Diagnostics improvements

Users ask questions. It’s normal. When different users ask the same question over and over again, some people write a FAQ, but we prefer a better way: we want the IDE to help them figure out the answer. One example there is the following:

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (foo is List) { // ERROR!
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

the compiler complains that List must have a type argument, ‘List<String>’ for example. But generics are erased, and we can’t check if something is a list *of strings*, all we know at runtime is that it is a list. And the compiler knows that too:

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (foo is List<String>) { // ERROR: can't check!
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

So the user is stuck: a type argument doesn’t work, and no argument doesn’t work either. This is where the IDE comes to the rescue:
<img alt="" class="aligncenter size-full wp-image-746" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/12/QuickFix.png?resize=190%2C96&amp;ssl=1"/>Just press Alt+Enter on the error (as, I am sure, you always do), and get it fixed: you need a ‘star projection’ here.
# Download

Kotlin plugin requires IntelliJ IDEA 12, it was released a few days ago, and you can get it [here](http://www.jetbrains.com/idea/download/index.html) (**Open Source** Community Edition is available). You can download **Kotlin M4** from the plugin repository, which is [accessible from your IDE](http://www.jetbrains.com/idea/plugins/index.html) .
Your feedback is very welcome. **Have a nice Kotlin!**
