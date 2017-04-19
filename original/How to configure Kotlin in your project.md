---
title: "How to configure Kotlin in your project"
date: 2013-10-07 14:34:00
author: Natalia Ukhorskaya
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/10/how-to-configure-kotlin-in-your-project/
---

Kotlin can be freely mixed with Java. That means that you can easily add Kotlin code to an existing Java project. All you need to do is create a new Kotlin file (*.kt) and tell the environment to use Kotlin. If you’re using IntelliJ IDEA, it can do this for you automatically.<span id="more-1247"></span>
The Kotlin plugin checks that all your modules containing Kotlin files are configured correctly. If they’re not, you will see the following notification in the upper left corner of the editor:
<img alt="Notification" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/1.jpg?w=640&amp;ssl=1"/><br/>
To configure them, click one of the links in the notification, based on what you need.
## Targeting JVM Byte Code

If you want to compile Kotlin to <strong>JVM byte code</strong>, click on <strong>as Kotlin (Java) module. </strong>You’ll be prompted with the following dialog:<br/>
<img alt="Create Kotlin Runtime Library Dialog" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/2.jpg?w=640&amp;ssl=1"/><br/>
Here  you can choose which modules need to be configured and a destination path to copy the library to.
You can either choose to copy the JAR library and store it under your project folder (optionally checking it in to VCS) or select <strong>Use library from plugin </strong>which will merely use the JAR bundled with the plugin in IntelliJ IDEA. However, the latter option means that your project will only work on machines where this plugin is installed.
## Targeting JavaScript

If you want to compile Kotlin to <strong>JavaScript</strong>, click <strong>as Kotlin (JavaScript) module </strong>link in the notification.
Similar to above, you can then specify where you want the runtime files stored.<br/>
<img alt="Create JavaScript library Dialog" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/09/3.jpg?w=640&amp;ssl=1"/>
There are two paths: the first points  to the Kotlin Runtime files, which are a JavaScript implementation of Kotlin library. The second path is a points to the headers of the Kotlin library.
## Using Maven or Gradle

If you use <strong>Maven</strong> or <strong>Gradle</strong> we have also great news: the Kotlin plugin now can configure your project using pom.xml or *.gradle files.<br/>
<img alt="Maven Notification" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/09/4.jpg?w=640&amp;ssl=1"/>
Once again, you need click the link in the notification, choose the modules to configure and the version of the Kotlin plugin (latest stable version or snapshot).<br/>
<img alt="Maven Dialog" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/5.jpg?w=640&amp;ssl=1"/><br/>
Configuration files for selected modules will be changed as described [here](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools) .
If by chance you miss a notification, you can always access it via the Event Log in IntelliJ IDEA.<br/>
<img alt="Notification in Event Log" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/09/7.jpg?w=640&amp;ssl=1"/>Also please note that the notification will appear only if you <strong>have Kotlin files under source root</strong> in your project.
<em>For Gradle Users</em>: Your Kotlin files should be under a source root named ‘kotlin’
