---
title: "Kotlin M2 is Out!"
date: 2012-06-11 09:55:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-is-out/
---

Some news websites told you that [Kotlin](http://kotlin.jetbrains.org) M2 was out earlier this week. Well, now we make it come true <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
In the [M2 Candidate post](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/) I told you about [JavaScript](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#js) and [Android](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#android) support, as well as new [Language Features](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#language) . Now it’s time for more updates, examples and plans.
Proceed to [Kotlin M2 Installation Instructions](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-is-out/#install) .
## A Little More on The Language

The previous post gave an overview of the new [Language Features](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#language) . Here’s a little more:<span id="more-570"></span>
First, I’d like to remind you that in M1 we added the [“assert not null” operator: !!](http://confluence.jetbrains.net/display/Kotlin/Null-safety#Null-safety-The%7B%7B%5C%21%5C%21%7D%7Doperator) , it replaces the sure() function we used to have in the standard library. Now, we removed sure() from the library, so some of you code might break, but it’s very easy to fix.
People keep asking whether Kotlin has <strong>literals for lists or maps</strong>. The answer is: strictly speaking, no, but we have function in the [library](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/kotlin/package-summary.html) that are good enough for that:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val list = arrayList(1, 2, 3)
val map = hashMap(
    "John" to "Doe",
    "Jane" to "Smith"
)
```

{% raw %}
<p></p>
{% endraw %}

Note that to() is also a function.
Also note that now you can use any type that has a function named invoke() in a callee position:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(x : Method) {
    x(bar)
}
```

{% raw %}
<p></p>
{% endraw %}

You could only use function types in this role before, now you can turn any object into a “function” by providing an invoke() extension or member.
I have to apologize for not all of that being present in the [docs](http://kotlin.jetbrains.org) yet. A little piece of good news is that we are working on making our docs open source as well as the rest of the project. Now you can find the sources (in Confluence wiki format) in our github [repo](https://github.com/JetBrains/kotlin/tree/master/docs/confluence.jetbrains.com/Kotlin) , and thus contribute your corrections/additions in the for of pull-requests.
A little more news on the docs: our KDoc tool is maturing rapidly, thanks to [James Strachan](https://github.com/jstrachan) . Now it supports search and links to github sources of the [libraries](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html) .
## Examples

As I mentioned above, the big things in this milestone were JavaScript support in the IDE and Android. It’s always good to start with examples, so here’s a set of projects you can open in your IDE and play with. Please, find some instructions in the [previous post](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/) .
Examples for <strong>JavaScript</strong>:

* Hello, world!
* Creatures (HTML5 Canvas): see it running
* KotlinPuzzle: see it running
* Traffic Lights: see it running
* Also note koolapp by James Strachan, which deserves a separate post, that I hope will be there soon. For now, refer to the readme file.

Examples for <strong>Android</strong>:

* Hello, world!
* Standard Snake and Wikitionary example re-written to Kotlin can be found here.
* A set of useful utilities by Vlad Likhonos: kotlinAndroidLib

have fun playing with these examples, and contribute more!
## IntelliJ IDEA Plugin

The IntelliJ IDEA plugin is progressing pretty fast. Most of the work is done behind the scenes (performance, tighter integration with the Java IDE), but there’re a few user-facing things to point out, too:

* The IDE now displays error messages formatted in nice HTML-like way, which makes the messages more readable.
* Enjoy the “Specify explicit type” refactoring when you need to add a type to your declaration.
* Cross-language Find Usages and Rename between Kotlin and Java code is now supported.
* Navigation to inheritors is supported. This also works across languages: inside Kotlin, for Kotlin classes extending Java classes, and vice versa.
* Also, we changed the IDE icons, and they are very nice now. More work coming on this topic.

Our priority for the next milestone is IDE performance and improvements to null-safety support for Java classes.
<strong><a name="install">To install the M2 plugin</a></strong>: If you had you M1 installed, it will update automatically from the [plugin repository](http://plugins.intellij.net/plugin/?idea&pluginId=6954) . It checks for updates once a day, so if you don’t want to wait, initiate the check manually:

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Check-For-Updates.png"><img alt="" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Check-For-Updates.png?resize=150%2C150&amp;ssl=1"/></a></p>
{% endraw %}

You will be prompted to update your Kotlin library, since the annotation format has changed a little. If you miss the “Update Kotlin Runtime” balloon, open the message in the Event Log:<br/>
<img alt="" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Outdated-Kotlin-Runtime.png?resize=150%2C129&amp;ssl=1"/><img alt="" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Update-Runtime.png?resize=150%2C150&amp;ssl=1"/>
<strong>Note </strong>that you have to uninstall the M2 Candidate and any nightly builds of the Kotlin plugin or builds installed manually before [installing](http://www.jetbrains.com/idea/plugins/index.html) M2 from the main [plugin repository](http://plugins.intellij.net/plugin/?idea&pluginId=6954) .
## Build Tools: Ant and Maven

Our [build tools integration](http://confluence.jetbrains.net/display/Kotlin/Kotlin+Build+Tools) , including Maven, has improved a little bit fewer repositories, easier set-up process. You may need to update your pom’s. See instructions [here](http://confluence.jetbrains.net/display/Kotlin/Kotlin+Build+Tools) .
## Plans

A little more on what we plan to do next. As mentioned above, the IDE priorities are performance and Java-integration wrt null-safety. The language work will bring the following improvements:

* Kotlin will provide means of defining properties that turn into Java’s static final constants.
* We will support the concept of data classes, that are somewhat similar to Scala’s case classes.
* Kotlin will support a dynamic type, which is needed mostly to accommodate the JavaScript APIs that don’t fit with the statically typed approach.
* We’ll also improve the type inference algorithm tremendously. We owe you this for a long time by now…

Library-wise the plans are as follows:

* Port most of the Kotlin’s standard library to the JS platform.
* Make Kotlin’s collections variant, but preserve the seamless interop with java.util.* collections. This actually deserves a separate post.
* Provide good library support for Android. We suspect that most of Android’s XML files can be replaced with Kotlin’s builders that are much nicer in many ways…

## Have a nice Kotlin!

And don’t forget to give us feedback. Thanks.
