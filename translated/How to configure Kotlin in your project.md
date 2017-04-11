---
title: [译]How to configure Kotlin in your project
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

Kotlin可以和Java自由混合。这意味着您可以轻松地将Kotlin代码添加到现有的Java项目中。所有你需要做的是创建一个新的Kotlin文件（* .kt），并告诉环境使用Kotlin。如果您使用IntelliJ IDEA，则可以自动为您提供此功能。
Kotlin插件会检查包含Kotlin文件的所有模块是否正确配置。如果没有，您将在编辑器的左上角看到以下通知：
要配置它们，请根据需要点击通知中的其中一个链接。
## 定位JVM字节代码

如果要将Kotlin编译为JVM字节码，请单击Kotlin（Java）模块。将出现以下对话框提示：

在这里，您可以选择需要配置的模块和将库复制到的目标路径。
您可以选择复制JAR库并将其存储在项目文件夹下（可选择将其检入VCS），或者从IntelliJ IDEA中选择仅使用与该插件捆绑在一起的JAR的插件。但是，后一个选项意味着您的项目将仅适用于安装此插件的计算机。
## 定位JavaScript

如果要将Kotlin编译成JavaScript，请在​​通知中单击Kotlin（JavaScript）模块链接。
与上述类似，您可以指定希望运行时文件存储在哪里。
有两个路径：第一个指向Kotlin运行时文件，这是Kotlin库的JavaScript实现。第二条路径是指向Kotlin图书馆的标题。
## 使用Maven或Gradle

如果您使用Maven或Gradle，我们也有一个好消息：Kotlin插件现在可以使用pom.xml或* .gradle文件配置您的项目。
再次，您需要点击通知中的链接，选择要配置的模块和Kotlin插件的版本（最新的稳定版本或快照）。

所选模块的配置文件将按照此处所述进行更改。
如果偶然你错过了一个通知，你可以随时通过IntelliJ IDEA的事件日志来访问它。
另请注意，只有您的项目中有源根目录下的Kotlin文件，通知才会出现。
对于Gradle用户：您的Kotlin文件应该在名为“kotlin”的源根下
