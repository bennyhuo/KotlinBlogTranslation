---
title: "Kotlin 1.0 Released: Pragmatic Language for JVM and Android"
date: 2016-02-15 16:57:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/02/kotlin-1-0-released-pragmatic-language-for-jvm-and-android/
translator:
translator_url:
---

This is it. 1.0 is here!
It’s been a long and exciting road but we’ve finally reached the first big 1.0, and we’re celebrating the release by also presenting you with the new logo:

{% raw %}
<p><center><img alt="Kotlin" class="alignnone size-full wp-image-3688" data-recalc-dims="1" margin-left="auto" margin-right="auto" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/02/1_0_Banner.png?resize=640%2C320&amp;ssl=1"/></center></p>
{% endraw %}

<em>See discussions on <a href="https://www.reddit.com/r/programming/comments/45wcnd/kotlin_10_released_pragmatic_language_for_jvm_and/">Reddit</a> and <a href="https://news.ycombinator.com/item?id=11103087">Hacker News</a></em>

{% raw %}
<p><span id="more-3507"></span></p>
{% endraw %}

## What is Kotlin?

Kotlin is a pragmatic programming language for JVM and Android that combines OO and functional features and is focused on <strong>interoperability</strong>, <strong>safety</strong>, <strong>clarity</strong> and <strong>tooling</strong> support.
Being a general-purpose language, Kotlin <strong>works everywhere where Java works</strong>: server-side applications, mobile applications (Android), desktop applications. It works with all major tools and services such as

* IntelliJ IDEA, Android Studio and Eclipse
* Maven, Gradle and Ant
* Spring Boot (Kotlin support released today!)
* GitHub, Slack and even Minecraft

One of the key focuses of Kotlin has been interoperability and seamless support for <strong>mixed Java+Kotlin projects</strong>, making adoption easier leading to less boilerplate code and more type-safety. Additionally, Kotlin has an <strong>extensive standard library</strong> that makes everyday tasks easy and smooth while keeping the bytecode footprint [low](http://www.methodscount.com/?lib=org.jetbrains.kotlin%3Akotlin-stdlib%3A1.0.0-rc-1036) (TODO). Of course, <strong>any Java library can be used in Kotlin</strong>, too; and vice versa. 
## What does pragmatic mean?

Understanding one’s core values is crucial for any long-running project. If I were to choose one word to describe Kotlin’s design, it would be <strong>pragmatism</strong>. This is why, early on, we said that Kotlin is not so much about invention or research. We ended up inventing quite a few things, but this was never the point of the project. Of course we were building a <strong>type system that prevents bugs</strong>, and <strong>abstraction mechanisms that facilitate code reuse</strong>, as anybody in our position would. But our (pragmatic) way of doing it was through <strong>focusing on use cases</strong> to make the language a <strong>good tool</strong>.
In particular, this approach lead us immediately to the notion that <strong>interoperability with existing code and infrastructure is crucial</strong>. Re-writing the world <em>the right way</em>, all from scratch — who never wished to? I did, quite a few times :) And Kotlin would have been a whole lot easier to design and develop if not for the Java interop, Maven integration, Android compatibility! It would definitely be more elegant in many ways. But elegance, though highly appreciated, is not the primary goal here, <strong>the primary goal is being useful</strong>. And the less our users have to re-learn, re-invent, re-do from scratch, the more they can re-use, the better.
— <em>So, why doesn’t Kotlin have its own package manager, or its own build system?</em><br/>

— Because there’s already Maven and Gradle, and re-using their huge number of plugins is crucial for many projects.<br/>

— <em>Why did we invest a lot of time and effort into making JDK-compatible collection interfaces, when it was so much easier to just redesign collections from scratch?</em><br/>

— Because tons and tons of Java code work with JDK collections, and converting data on the boundary would be a pain.<br/>

— <em>Why does Kotlin support Java 6 byte code?</em><br/>

— Because many people are still running Java 6 (Android, most notably, but not only Android).
For us pragmatism is about <strong>creating user experience</strong>, not a language or a library alone. Many of the language design decisions were made under constraints like “Won’t this impede incremental compilation?”, “What if this increases APK method counts?”, “How will the IDE highlight this as-you-type?”, and many more like these. As a result, we are proud of our <strong>tooling as well as the language</strong>.
## Is it mature enough and ready for production?

Yes. And it has been for quite some time. At JetBrains, we’ve not only been implementing the compiler and tooling but have also been using Kotlin <strong>in real-life projects</strong> on a rather extensive scale over the last two years. In addition to JetBrains, there are quite a few companies that have been using Kotlin <strong>in production</strong> for some time now.
In fact, one of the reasons it took us a long time to reach 1.0 was because we paid extra attention to validating our design decisions in practice. This was and is necessary, because moving forward the compiler will be <strong>backwards compatible</strong> and future versions of Kotlin must not break existing code. As such, whatever choices we’ve made we need to stick with them.
Reaching this milestone was something we couldn’t have done without the valuable <strong>help of early adopters</strong>. We want to thank each any every one of you for your bravery, energy and enthusiasm!
## Who’s behind Kotlin?

First and foremost, Kotlin is an Open Source language

* Developed on GitHub under Apache 2.0 Open-Source license;
* With over 100 contributors to date.

JetBrains is the main backer of Kotlin at the moment: we have invested a lot of effort into developing it and <strong>we are committed to the project for the long run</strong>. We wrote it out of our own need to use in our own products. And we’re happy to say that to date, <strong>close to 10 JetBrains products</strong>, which include IntelliJ IDEA, [JetBrains Rider](https://blog.jetbrains.com/dotnet/2016/01/13/project-rider-a-csharp-ide/) , JetBrains Account & E-Shop, YouTrack as well as some of our smaller IDE’s and some internal projects are using Kotlin. So <strong>it’s here to stay</strong>!
Since 2012 we kept Kotlin’s development very open: talking to the community all the time, gathering and addressing lots of feedback.
Moving forward we are planning to set up a centralized venue for design proposals and discussions, to make the process even more visible and organized. Standardization efforts have not been started for Kotlin so far, but we realize that we’ll need to do it rather sooner than later.
Language design and overall steering of the project is done by the team employed at JetBrains. We currently have <strong>over 20 people working full time</strong> on Kotlin, which also yet another testament to JetBrains’ commitment to Kotlin.
### The numbers

Let’s take a look at some numbers:

* 11K+ people were using Kotlin last month and near 5K last week alone;
* Hundreds of StackOverflow answers;
* Two books: Kotlin in Action and Kotlin for Android Developers;
* About 1400 people on Slack (get an invite);
* Over 500K lines of Kotlin code in projects such as IntelliJ IDEA and Rider.

Talking about lines of code, the number of these in open repositories on GitHub is <strong>growing exponentially over time</strong> (JetBrains’ projects excluded): <center><br/>
<img alt="Kotlin GitHub Adoption" data-recalc-dims="1" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/02/KotlinAdoption.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/02/KotlinAdoption.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/02/KotlinAdoption.png?w=640&amp;ssl=1"/><br/>
</center>
And of course we have a growing list of <strong>companies using Kotlin</strong> including Prezi and Expedia. By the way, if you’re using Kotlin, make sure you send us a [Pull Request](https://github.com/JetBrains/kotlin-web-site/blob/master/_data/companies-using-kotlin.yml) .
## The upcoming roadmap

As of 1.0, we are committed to long-term <strong>backward compatibility</strong> of the language and its standard library (`kotlin-stdlib`):

* a newer compiler will work with older binaries (but older compilers may not understand newer binaries, like javac 1.6 can’t read classes compiled by javac 1.8);
* older binaries will keep working with newer binaries at runtime (newer code may require newer dependencies, though).

This applies to the JVM/Android support only. The JavaScript support remains experimental for now and will have its own release later on.
As for the plans, our nearest goals are (apart from bug fixes):

* Constant performance improvements for the Kotlin toolchain (this includes, for example, incremental compilation in Gradle, that is in the works now);
* JavaScript support (including cross-compilation into both JVM and JS where possible);
* Support generating Java 8 byte code with optimized lambdas, etc (Java 6 will be actively supported as long as Android users need it).

Tooling updates and bug fixes will be released as incremental updates, i.e. 1.0.X. Bigger changes will first go though an Early Access Program (EAP) and then will be released as 1.1.
## How to start

The easiest way to play with the language is through its <strong>online mini-IDE: <a href="https://try.kotlinlang.org">try.kotl.in</a></strong>, including [Koans](http://try.kotlinlang.org/koans) — a set of introductory problems which <strong>guide you through the basics</strong> of the language.
To use Kotlin on your machine (and Koans can be completed [offline](https://kotlinlang.org/docs/tutorials/koans.html) as well):

* IntelliJ IDEA (Ultimate or Community): just create a Kotlin project or a Kotlin file in a Java project;
* Android Studio: install the plugin through Plugin Manager;
* Eclipse: install the plugin through Marketplace.

NOTE: If you are running an older version, you may need to update your Kotlin plugin to 1.0.
To get up to speed with concepts, language <strong>docs and tutorials</strong> are available from the [official web site](https://kotlinlang.org) . Great articles and presentations given by members of our community can be found in the [Digest of 2015](http://blog.jetbrains.com/kotlin/2016/01/kotlin-digest-2015/) .
If you’re introducing Kotlin to your Java project, you can make use of the <strong>Java-to-Kotlin converter</strong> built into the IDE, helping migration easier class by class.
Last but not least, make sure you join the discussions on our [Forum](https://devnet.jetbrains.com/community/kotlin) or [Slack](http://kotlinslackin.herokuapp.com/) .
Once again, <strong>we want to thank everyone</strong>. We couldn’t have done this without the community.
Have a nice Kotlin! <strong>Now</strong> <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
P.S. <em>See discussions on <a href="https://www.reddit.com/r/programming/comments/45wcnd/kotlin_10_released_pragmatic_language_for_jvm_and/">Reddit</a> and <a href="https://news.ycombinator.com/item?id=11103087">Hacker News</a></em>
