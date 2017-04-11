---
title: Kotlin Web Demo is out!
date: 2012-01-10 19:16:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/01/kotlin-web-demo-is-out/
---

It’s been a little more than a year since the first commit was pushed to our source control, and we are happy to announce the first public preview of Kotlin.
This preview works as follows:

* You go to http://kotlin-demo.jetbrains.com and it loads a code editor in your browser:
* You check out examples, modify them or even solve our sample toy-problems;
* You run your code on a JVM running on our server, so that you can use familiar JDK classes;
* Or, alternatively, you compile you code to JavaScript and run it in your browser:

Note that the JavaScript back-end is a pre-alpha version, so it may refuse to compile some of your programs.


{% raw %}
<p><span id="more-318"></span></p>
{% endraw %}

Experimental features
By default, you get error highlighting only when you run your program. But you can try out some of the features we are experimenting with and turn on “as-you-type” error highlighting:

If you choose “Server”, the editor starts talking to a type checker service hosted on our server. If you choose “Client”, a type checker is loaded as a (so far rather big) Applet which runs on your machine.
Both “Server” and “Client” options give you code completion as well:
Please, note that these features are experimental and feel free to report any problems to us.
Coming soon
This demo will be developed further for you to have more fun. Among other things we plan to add the following:

* Standard Library of extension functions that make using JDK collections and other common APIs more pleasant (things like map()/filter() and so on);
* Code Challenge: currently we offer a few sample problems in the form of code snippets containing test data. This will be extended to contest-like automated testing system.
* More Examples: There’s always some more to show off

Have fun!
