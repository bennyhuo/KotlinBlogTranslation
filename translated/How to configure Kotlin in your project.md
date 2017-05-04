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

Kotlin 可以和 Java 自由混合。这意味着您可以轻松地将 Kotlin 代码添加到现有的 Java 项目中。所有你需要做的是创建一个新的 Kotlin 文件（* .kt），并告诉环境使用 Kotlin。如果您使用 IntelliJ IDEA，则可以自动为您提供此功能。<span id =“more-1247”> </span>
Kotlin 插件会检查包含 Kotlin 文件的所有模块是否正确配置。如果没有，您将在编辑器的左上角看到以下通知：
<img alt =“通知”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/1.jpg?w=640&amp ; ssl = 1“/> <br/>
要配置它们，请根据需要点击通知中的其中一个链接。
## 定位 JVM 字节代码

如果要将 Kotlin 编译为**JVM 字节代码**，请单击**作为 Kotlin（Java）模块。**系统会提示您输入以下对话框：<br/>
<img alt =“创建 Kotlin 运行时库对话框”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/2.jpg ？w = 640＆amp; ssl = 1“/> <br/>
在这里，您可以选择需要配置的模块和将库复制到的目标路径。
您可以选择复制 JAR 库并将其存储在项目文件夹下（可选择将其检入 VCS），或者选择**使用库插件**，这将仅使用 IntelliJ IDEA 中的插件捆绑的 JAR 。但是，后一个选项意味着您的项目将仅适用于安装此插件的计算机。
## 定位 JavaScript

如果要将 Kotlin 编译为**JavaScript**，请在通知中单击**作为 Kotlin（JavaScript）模块**链接。
与上述类似，您可以指定存储运行时文件的位置
<img alt =“创建 JavaScript 库对话框”data-recalc-dims =“1”src =“https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/09/3.jpg？ w = 640＆amp; ssl = 1“/>
有两个路径：第一个指向 Kotlin 运行时文件，这是 Kotlin 库的 JavaScript 实现。第二条路径是指向 Kotlin 图书馆的标题。
## 使用 Maven 或 Gradle

如果您使用**Maven**或**Gradle**，我们也有好消息：Kotlin 插件现在可以使用 pom.xml 或* .gradle 文件配置您的项目。<br/>
<img alt =“Maven Notification”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/09/4.jpg?w= 640＆amp; ssl = 1“/>
再次，您需要点击通知中的链接，选择要配置的模块和 Kotlin 插件的版本（最新的稳定版本或快照）。<br/>
<img alt =“Maven Dialog”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/09/5.jpg?w= 640＆amp; ssl = 1“/> <br/>
所选模块的配置文件将按照所述进行更改 [这里](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools) 。
如果偶然你想念一个通知，你可以随时通过 IntelliJ IDEA 的事件日志访问它
<img alt =“事件日志中的通知”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/09/7.jpg？ w = 640＆amp; ssl = 1“/>另请注意，只有在您的项目中**在源根目录下有 Kotlin 文件**，通知才会出现。
*对于 Gradle 用户*：您的 Kotlin 文件应该在名为“kotlin”的源代码根目录下
