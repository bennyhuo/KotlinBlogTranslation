---
title: "An Interview with Andy Selvig, Author of Kara Web Framework"
date: 2013-01-31 10:12:00
author: Robert Demmer
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/01/an-interview-with-andy-selvig-author-of-kara-web-framework/
translator:
translator_url:
---

<strong><img alt="" class="alignright size-medium wp-image-806" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/01/headshot.jpg?resize=210%2C158&amp;ssl=1"/>1. Hello Andy, thank you for taking the time to join us. Can you tell us a bit about yourself? </strong>

{% raw %}
<p><strong> </strong></p>
{% endraw %}

I’m co-owner of [Tiny Mission](http://tinymission.com/) , a small web and mobile development company based in Minnesota, USA. In addition to my work at Tiny Mission, I teach a course in mobile application development at the University of Minnesota.

{% raw %}
<p><span id="more-804"></span></p>
{% endraw %}

<strong>2.  As the author of Kara, please give us a bit of background on the project, how it came about and its goals.</strong>
I do a lot of web development, mainly in Ruby on Rails and ASP.NET MVC. I guess you could look at Kara as an attempt to find the best of both of those worlds.

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/01/commandline-usage.png" target="_blank"><img alt="" class="size-medium wp-image-808 alignleft" data-recalc-dims="1" sizes="(max-width: 180px) 100vw, 180px" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/01/commandline-usage.png?resize=180%2C146&amp;ssl=1" srcset="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/01/commandline-usage.png?resize=300%2C243&amp;ssl=1 300w, https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/01/commandline-usage.png?w=626&amp;ssl=1 626w"/></a></p>
{% endraw %}

I like the expressiveness of Rails but often I think could be more productive with some static typing and a compiler. I know this goes against common wisdom about the productivity of a dynamic language like Ruby, but in large-scale applications the compiler is your friend. The idea that it can be replaced by writing hundreds of unit tests seems unpragmatic.
I enjoy developing in C#/.NET but ASP.NET MVC has some pain points, like the poor templating system (Razor might be okay if it had proper IDE support) and reliance on the Microsoft development ecosystem.
<strong>3.  What makes Kara different from existing web frameworks?</strong>
<strong> </strong><img alt="" class="alignright size-medium wp-image-811" data-recalc-dims="1" sizes="(max-width: 211px) 100vw, 211px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/a-kara-stylesheet.png?resize=211%2C300&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/a-kara-stylesheet.png?resize=211%2C300&amp;ssl=1 211w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/a-kara-stylesheet.png?w=381&amp;ssl=1 381w"/>The primary thing that makes Kara stand out is that all parts of your application are written in the same language. This means that you get statically typed, expressive application code, views, and style sheets. I don’t know of any other framework that offers this level of integration.
In the end, Kara is intended to be a true developer’s framework. Instead of writing traditional HTML and CSS we rely on the power and expressiveness of Kotlin. This might be a turnoff to some web designers, but I think that most developers will “just get it”, and see a framework that works with them instead of against them.
<strong>4.  Why did you choose to write Kara in Kotlin and what were the other alternatives?</strong>
When I set out to write Kara, I evaluated a number of different languages: Kotlin, Scala, Gosu, Nemerle, Groovy, and a couple of others. The primary determining feature was the ability to define custom DSLs for HTML and CSS generation with an elegant syntax. The only two languages that fit the bill at the time were Kotlin and Groovy. However, it was before the release of Groovy 2.0 so it was entirely a dynamic language, which really wasn’t what I was looking for.

{% raw %}
<p><img alt="" class="alignleft size-medium wp-image-815" data-recalc-dims="1" sizes="(max-width: 240px) 100vw, 240px" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/01/a-kara-view.png?resize=240%2C152&amp;ssl=1" srcset="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/01/a-kara-view.png?resize=300%2C190&amp;ssl=1 300w, https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/01/a-kara-view.png?w=381&amp;ssl=1 381w"/></p>
{% endraw %}

Kotlin and Scala obviously have many similarities, but there are some minor differences in the way they scope anonymous functions that make it impossible to create the same type of DSL in Scala. Plus, some commonly used syntax patterns in Scala makes me feel like I’m solving a math problem, not writing code. Kotlin’s syntax just clicks with me better.
<strong>5.  Kara is currently in an Alpha stage, how has your experience with Kotlin been so far?</strong>
<strong> </strong>Overall, Kotlin has been a joy to use. It follows the path of least surprise and implements all the features I’m looking for: type inference, nullability, properties, optional semicolons, and a great capacity for making builder DSLs. In addition to my work on Kara, Kotlin is now my default language when starting a new Android project.
<strong>6.  Kotlin is a fairly young project. What’s your impression of the infrastructure available to you as a language user? Did the IDE help you? How’s tooling support with regards to other tasks, such as building?</strong>
The infrastructure was a huge selling point for me when picking the language. I use several JetBrains IDEs (IntelliJ IDEA, RubyMine, WebStorm) and love them. The Kotlin plugin for IDEA usually works well and the overall developer experience is nice. There have been some instabilities in the plugin, but I know I’m an early adopter and Kotlin is actively being developed, so it comes with the territory.
<strong>7.  What value have you gained by using Kotlin and where are the shortcomings?</strong>
Besides the specific language features mentioned above, the overall value of Kotlin is clearly in productivity. Generally speaking, Kotlin is a replacement for Java, and it accomplishes this task well. I can write code much quicker in Kotlin than Java, while maintaining type safety and performance of the JVM.
Kotlin’s main shortcoming, currently, is the lack of large community and a good set of Kotlin-specific libraries. You can obviously use any old Java library in Kotlin, but the real power of the language shines when you leverage its unique features. Hopefully, Kara will be a part of this ecosystem and draw contributors to more projects.
<strong>8.  You are obviously vested in Kotlin. How do you feel about its viability and its future?</strong>
I think Kotlin is very viable as a common JVM language (for server-side web and Android programming) as well as a platform for writing JavaScript applications. In order for this to be the case, the Kotlin community needs to establish a clear message for how it differentiates itself from Scala – its closest (and arguably more popular) competitor. To me, this differentiation is in having a focus on productivity and a set of first-class tools and libraries to support it.
<strong>9.  What’s next for Kara? What can we expect down the road?</strong>
There are two primary goals for upcoming Kara releases:

0. Right now Kara is basically a stand-alone framework that gives you a bunch of tools for creating websites. We need to develop an ecosystem of libraries, plugins, and middleware that provide a rich toolset for application developers. It should be easy for someone starting a new Kara project to select the various components needed to build a complete application, like a persistence layer, authentication mechanism, CSS framework, UI library, etc. This is an area where Rails really shines, and hopefully we can create that sort of ecosystem.
1. Kara ships with a built-in Jetty server for development, but we don’t really have anything in place for large-scale deployments. I think there’s a lot of interesting room for improvement in this area. It could mean simply providing a mechanism to package Kara apps as servlets, or more innovative methods like being able to host an app on top of Vert.x.


{% raw %}
<p style="text-align: center"><span style="font-size: small"><span style="line-height: 24px"><a href="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2013/01/kara-routes.png" target="_blank"><br/>
</a><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/kara-routes.png" target="_blank"><img alt="" class="aligncenter size-full wp-image-819" data-recalc-dims="1" sizes="(max-width: 774px) 100vw, 774px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/kara-routes.png?resize=640%2C201&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/kara-routes.png?resize=300%2C94&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/01/kara-routes.png?w=774&amp;ssl=1 774w"/></a> </span></span></p>
{% endraw %}

<strong><span style="font-size: 16px">10.   The Kara Web Framework is open source so people can contribute. Where can we learn more and what types of contributions would be helpful right now? </span></strong>
<span style="font-size: 16px">We are absolutely looking for more contributors. Anyone interested can check out our <a href="http://youtrack.codebetter.com/issues/Kara" target="_blank" title="Kara on YouTrack">YouTrack page</a>. There are a bunch of features that need to be implemented there.</span>
<strong>11. Thank you for taking the time to chat with us Andy. Is there anything else that you would like to share with our readers?</strong>
<img alt="" class="alignright size-medium wp-image-822" data-recalc-dims="1" sizes="(max-width: 300px) 100vw, 300px" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/01/karaframework.com_.png?resize=300%2C236&amp;ssl=1" srcset="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/01/karaframework.com_.png?resize=300%2C236&amp;ssl=1 300w, https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/01/karaframework.com_.png?w=962&amp;ssl=1 962w"/>I hope everyone will check out Kara and see what we have to offer. I’ve had a great experience with the Kotlin community so far, and would love to build on that to make Kotlin and Kara a great way to make modern web applications.
<em>For more information, visit <a href="http://www.karaframework.com" target="_blank" title="Kara Web Framework">KaraFramework.com</a>.</em>
