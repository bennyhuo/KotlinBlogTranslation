---
title: "The Kotlin Language: 1.0 Beta is Here!"
date: 2015-11-02 18:44:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/11/the-kotlin-language-1-0-beta-is-here/
---

We are extremely pleased to present <strong>Kotlin 1.0 Beta</strong> for JVM and Android!
To recap:  [Kotlin](https://kotlinlang.org/)  is a <strong>modern programming language</strong> that  [JetBrains](https://www.jetbrains.com/)  has been working on for quite some time now.
This post gives an overview of where we are and what’s coming next. Changes in this version are listed  [here](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-1103) .
## The story behind Kotlin

Kotlin was conceived in 2010. Ten years of Java development led us to feeling that our productivity at JetBrains could be improved significantly by using a modern JVM language alongside Java. Having evaluated other available options, we decided that a new language was needed there, and we had the expertise and resources to create such a language. Our primary line of business is making tools for developers, and the guiding principle is that the best way to make an awesome product for the users is to make an awesome tool we need ourselves. This worked with IntelliJ IDEA, ReSharper, and many other IDEs, as well as TeamCity and other server products, so we set off to apply the same principle for another developer tool — a programming language. <span id="more-3005"></span>
We designed Kotlin as a <strong>modern language for industry</strong>, and had rather specific requirements for it. First off, our projects live long and grow really big (many millions of lines of code), so we needed <strong>static typing</strong> to be able to reason precisely about huge codebases and maintain them over the years. Then, all our code was written in Java, so we needed a <strong>smooth migration path</strong> where the new language could be <strong>introduced gradually</strong> into an existing Java codebase affecting the rest of the code as little as possible. Also, being JetBrains, we did not want to compromise on the <strong>tooling quality</strong>: we were looking for a new language to make us more productive, and we believe that much of it depends on the tooling. Finally, we needed a language that’s <strong>easy to learn and understand</strong>: in our teams, we do not separate “library writers” from “library users”, and we want all our developers to be equally productive with the language they are using.
Such a project involves making very many decisions, and we knew from the start that it’s impossible to get everything right on the first try. That’s why we allowed a considerable period for experimenting and validation of the core design choices: as it was being used by early adopters both inside and outside JetBrains, we were constantly gathering feedback and making changes (many thanks to our community for all the comments you folks gave us!). This gave us important insights into a wide range of use cases, and now we believe that we can <strong>maintain backward compatibility after 1.0</strong>.
JetBrains has been using Kotlin in production of  [IntelliJ IDEA](https://www.jetbrains.com/idea/) ,  [YouTrack](https://www.jetbrains.com/youtrack/)  and other products for quite a long time now. We have more than <strong>250’000 LOC of Kotlin in production</strong> at the moment (plus about as much in the  [Kotlin project](https://github.com/JetBrains/kotlin)  itself). While some of our projects are entirely written in Kotlin ( [account.jetbrains.com](https://account.jetbrains.com) ), others have introduced it to existing Java codebases, as we planned initially. We reached the level of interoperability where freely putting Kotlin alongside Java is transparent for Java clients: Java can be called from Kotlin and vice versa, sources can be mixed in one project, resulting <code>.class</code> files are totally compatible with Java tooling.
Kotlin is serving us well and we have dedicated a <strong>team of over 20 people</strong> to its development.
Even though it has not reached 1.0 yet, <strong>other companies and individual developers are already using Kotlin in production</strong> from web-service back-ends to Android apps. We’ve got reports from  [Expedia](https://twitter.com/fleurchild/status/636965650536108032) ,  [Prezi.com and many others](https://github.com/JetBrains/kotlin-web-site/blob/master/_data/companies-using-kotlin.yml)  (feel free to add your company to this list by submitting a PR).
The number of lines of Kotlin code in open repositories on GitHub has been growing exponentially so far (JetBrains’ projects are excluded):

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/Kotlin-GitHub-LOC.png"><img alt="Kotlin GitHub LOC" class="alignleft size-full wp-image-3069" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/Kotlin-GitHub-LOC.png?resize=640%2C279&amp;ssl=1"/></a></p>
{% endraw %}

## What Kotlin feels like

From our own experience with the language and from what we hear from many external users here’s what using Kotlin feels like:

* it’s less code,
* better readability,
* more type-safety,
* more expressive power,
* smooth experience with tooling and interop.

## What is Beta?

While being actively used in production, Kotlin is in the Beta status now. What it means to you:

* we are wrapping up the preparations to the official release;
* the binary format is finalized;
* all major language changes have been done.

## Compatibility

Kotlin won’t stay long in Beta, 1.0 is coming rather soon.
We are committed to smooth user experiences, and this includes compatibility of Kotlin versions. After 1.0 all updates to the language and libraries will be <strong>backwards-compatible</strong>:

* a newer compiler will work with older binaries (but older compilers may not understand newer binaries, like javac 1.6 can’t read classes compiled by javac 1.8);
* older binaries will keep working with newer binaries at runtime (newer code may require newer dependencies, though).

Everything stated above applies to the JVM/Android support only. The JavaScript support remains experimental for now and will have its own  release later on.
## A few more facts about Kotlin


* it’s Open Source (under Apache 2.0 License): compiler, runtime libraries and all the tooling, including the IDE;
* it promotes functional style of programming (while being a multi-paradigm language);
* it is statically compiled, and  introduces no runtime overhead compared to Java;
* it supports efficient and safe concurrency through Quasar;
* it’s bundled with IntelliJ IDEA 15 (both Ultimate and the OSS Community Edition) and available out-of-the-box;
* it has plug-ins for Android Studio, Eclipse, Maven, Gradle and Ant (not to mention IntelliJ IDEA and TeamCity);
* it has a REPL;
* it has an active and helpful community that is producing awesome libraries;
* two books are written about it: Kotlin in Action and Kotlin for Android Developers.

## Frameworks, interop and migration

Virtually <strong>any Java or Android framework or library works</strong> smoothly with Kotlin. Among others, this includes <em>Spring MVC</em>, <em>Vaadin</em>, <em>Vert.x</em> and <em>Jackson</em>. Many Android frameworks require annotation processing that is available in Kotlin through  [kapt](http://blog.jetbrains.com/kotlin/2015/06/better-annotation-processing-supporting-stubs-in-kapt/)  that supports <em>Dagger 2</em>, <em>DataBinding</em>, <em>DBFlow</em>, <em>ButterKnife</em>, <em>AndroidAnnotations</em> and others.
Kotlin has its <strong>own frameworks and libraries</strong> developed by JetBrains and the community. Some examples:  [Anko](https://github.com/JetBrains/anko) ,  [RxKotlin](https://github.com/ReactiveX/RxKotlin) ,  [funKtionale](https://github.com/MarioAriasC/funKTionale) ,  [kohesive](https://github.com/kohesive/) ,  [kovenant](https://github.com/mplatvoet/kovenant) , the  [Kobalt](http://beust.com/kobalt)  build tool, and  [much more](https://kotlinlang.org/docs/resources.html) .
A <strong>converter</strong> built-in to the IDE helps migrate the source code from Java to Kotlin.
## Try it


* Learn: Koans/Playground/, Tutorials, Language docs
* Install

IntelliJ IDEA 15 (Ultimate or Community): just create a Kotlin project or a Kotlin file in a Java project
Android Studio: install the plugin through Plugin Manager
Eclipse: install the plugin through Marketplace
Command line: download the compiler here
* IntelliJ IDEA 15 (Ultimate or Community): just create a Kotlin project or a Kotlin file in a Java project
* Android Studio: install the plugin through Plugin Manager
* Eclipse: install the plugin through Marketplace
* Command line: download the compiler here
* Community: Forum, Slack (get invite), StackOverflow, GitHub (PRs welcome)
* News: Blog, Twitter
* Issue tracker

<strong><em>Have a nice Kotlin!</em></strong>
