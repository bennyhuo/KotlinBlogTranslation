---
title: Kotlin M3 is Out!
date: 2012-09-20 15:03:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/
---

Last time I wrote about a new exciting feature in “the upcoming Kotlin M3”. Today, Kotlin M3 is not “upcoming” any more, it’s here. This post gives an overview of the new milestone.
We have redesigned kotlin.jetbrains.org. Currently, links from this page point to the familiar docs in our wiki, but this will also improve over time.
## Improvements and Bug fixes

Many of almost 400 issues we closed in this milestone are bug fixes and small enhancements that make Kotlin neater and shinier. A huge improvement has been made in the type argument inference algorithm. It’s not finished yet, but is rather good already.
In M3 we started to profile things and tune performance of the IDE as well as the compiler. It will be a lot of work, but eventually everything will be fast and consume little memory. This time most improvements are related to code completion.
## Multi-assignment and Data Classes

This is covered in the last week’s entry. Long story short, you can write things like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val map = hashMap("one" to 1, "two" to 2, "three" to 3)
for ((k, v) in map) {
    println("$k -> $v")
}
```

{% raw %}
<p></p>
{% endraw %}

And define data classes like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Point(val x: Int, val y: Int)
```

{% raw %}
<p></p>
{% endraw %}

Here Point automatically gets toString(), equals()/hashCode() and component functions that enable you to write this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (x, y) = functionReturningPoint()
```

{% raw %}
<p></p>
{% endraw %}

See more in the aforementioned post.
These features enabled us to deprecate tuples. They will be removed completely in the next milestone, and you can migrate your code automatically using the IDE plugin.

{% raw %}
<p><a name="Collections"></a></p>
{% endraw %}

## Collections

Static JVM languages tend to come up with their own collections libraries, because Java collections do not make use of the cool features these languages have. So we get really cool collections, that are, unfortunately, incompatible, which makes us wrap them or copy when using Java APIs.
Kotlin has many fancy features, but we are eager to interoperate smoothly with Java, and, it turns out, we can have this cake and eat it too. Meet Kotlin’s collections:
As you can see, the basic structure here is very much like what java.util gives us, but with a few important differences:

* There are traits (“interfaces”) that distinguish between mutable and read-only collections.
* Read-only traits (like List or Set) are covariant (i.e. you can assign a List<String> to a List<Any>).

The good old java.util.ArrayList is still there, but Kotlin sees it as if it inherited from Kotlin’s MutableList, which in turn inherits List. This way you get both compatibility and nice type properties for your collections, like being able to pass a List<String> where List<Any> was expected.
Note that since the old names (like List or Collection) now mean something different, some of your code will break. For a quick and dirty solution, you can change all your Lists to MutableLists and so on, but it would be better if most of your data were read-only.
Also note that if your old code imported something like java.util.Collection, you will get a warning on this import, and will need to remove it.
## External annotations

Kotlin makes your programs safer by incorporating null-safety into the type system. Since Java doesn’t care that much about this, we need to guard against it by asserting that things returned from Java are not null using the ‘!!’ operator:

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (file.getName()!!.endsWith(extension)) {...}
```

{% raw %}
<p></p>
{% endraw %}

(BTW, the good old sure() function has been removed from the library, and you can migrate your code automatically.)
Many Java methods never actually return null. People use annotations to let the tools know about it, but what if I’m using a third-party library?
In Kotlin M3 we support external annotations: you can annotate things even if you don’t control their source code. This is done easily in the IDE.
We’re going to create an automated tool that will infer the annotations from the library code. Until then, we use the IDE to add annotations manually.
## Local Functions and Classes

In addition to local functions, Kotlin M3 support local classes and object declarations:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() {
  class Bar {...}
  val bars = ArrayList<Bar>()
  // ...
}
```

{% raw %}
<p></p>
{% endraw %}

Note that to create a local data class, you need to surround the “data” annotation with square brackets:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() {
    [data] class Data(...)
    // ...
}
```

{% raw %}
<p></p>
{% endraw %}

## Java Interoperability: Enums and Annotations

Support for annotations in Kotlin has been improved greatly. Among other things, Kotlin’s annotations are now fully compatible with Java annotations, one can use enum constants in annotations’ argument lists and so on.
Enums are also much better now: they support valueOf(), name() and ordinal() and play well with Java.
## REPL/Scripts

We have done some work on supporting scripts in Kotlin. Script support is rather preliminary, but you can run something like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// tree.ktscript
import java.io.File
 
fun tree(dir: File, indent: String) {
    val files = dir.listFiles()!!
    for (file in files) {
        println(indent + file!!.getName())
        if (file.isDirectory()) {
            tree(file, indent + "  ")
        }
    }
}
 
tree(File("."), "")
```

{% raw %}
<p></p>
{% endraw %}

By calling it from the command line:

{% raw %}
<p></p>
{% endraw %}

```kotlin
$ kotlinc/bin/kotlinc-jvm -script tree.ktscript
foo
  bar.txt
tree.ktscript
```

{% raw %}
<p></p>
{% endraw %}

“Shebang” comments are supported as well.
Scripts get us close enough to having a REPL, but we are not there yet. Please, use Web Demo instead.
## Have a Nice Kotlin!

The new plugin requires IntelliJ IDEA 12, which is available as an EAP build (this version of IntelliJ IDEA is not released yet, there are problems, e.g. this issue with Android). And don’t forget to update your kotlin-runitme.jar (the IDE will offer you to do so)!
As usual, your feedback is very welcome!
