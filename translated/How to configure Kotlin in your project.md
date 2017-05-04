---
title: "[译]How to configure Kotlin in your project"
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
translator:
translator_url:
---

Kotlin可以和Java自由混合。这意味着您可以轻松地将Kotlin代码添加到现有的Java项目中。所有你需要做的是创建一个新的Kotlin文件（* .kt），并告诉环境使用Kotlin。如果您使用IntelliJ IDEA，则可以自动为您提供此功能。<span id =“more-1247”> </span>
Kotlin插件会检查包含Kotlin文件的所有模块是否正确配置。如果没有，您将在编辑器的左上角看到以下通知：
<img alt =“通知”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/1.jpg?w=640&amp ; ssl = 1“/> <br/>
要配置它们，请根据需要点击通知中的其中一个链接。
## 定位JVM字节代码

如果要将Kotlin编译为<strong> JVM字节代码</strong>，请单击<strong>作为Kotlin（Java）模块。 </strong>系统会提示您输入以下对话框：<br/>
<img alt =“创建Kotlin运行时库对话框”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/2.jpg ？w = 640＆amp; ssl = 1“/> <br/>
在这里，您可以选择需要配置的模块和将库复制到的目标路径。
您可以选择复制JAR库并将其存储在项目文件夹下（可选择将其检入VCS），或者选择<strong>使用库插件</strong>，这将仅使用IntelliJ IDEA中的插件捆绑的JAR 。但是，后一个选项意味着您的项目将仅适用于安装此插件的计算机。
## 定位JavaScript

如果要将Kotlin编译为<strong> JavaScript </strong>，请在通知中单击<strong>作为Kotlin（JavaScript）模块</strong>链接。
与上述类似，您可以指定存储运行时文件的位置
<img alt =“创建JavaScript库对话框”data-recalc-dims =“1”src =“https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/09/3.jpg？ w = 640＆amp; ssl = 1“/>
有两个路径：第一个指向Kotlin运行时文件，这是Kotlin库的JavaScript实现。第二条路径是指向Kotlin图书馆的标题。
## 使用Maven或Gradle

如果您使用<strong> Maven </strong>或<strong> Gradle </strong>，我们也有好消息：Kotlin插件现在可以使用pom.xml或* .gradle文件配置您的项目。<br/>
<img alt =“Maven Notification”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/09/4.jpg?w= 640＆amp; ssl = 1“/>
再次，您需要点击通知中的链接，选择要配置的模块和Kotlin插件的版本（最新的稳定版本或快照）。<br/>
<img alt =“Maven Dialog”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/5.jpg?w= 640＆amp; ssl = 1“/> <br/>
所选模块的配置文件将按照所述进行更改 [这里](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools) 。
如果偶然你想念一个通知，你可以随时通过IntelliJ IDEA的事件日志访问它
<img alt =“事件日志中的通知”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/09/7.jpg？ w = 640＆amp; ssl = 1“/>另请注意，只有在您的项目中<strong>在源根目录下有Kotlin文件</strong>，通知才会出现。
<em>对于Gradle用户</em>：您的Kotlin文件应该在名为“kotlin”的源代码根目录下
