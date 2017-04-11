---
title: [译]Writing Kotlin in the Browser
date: 2013-10-16 08:00:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/10/writing-kotlin-in-the-browser/
---

你知道Kotlin可以定位到JavaScript和JVM吗？不要太惊讶，如果你不知道，因为我们没有给它太多的覆盖，尽管已经运送一个成功的产品，使用这种能力。但是，这是希望改变事情。
# 基础 - 一个简单的项目

第一步是建立一个新项目。在项目中使用Kotlin时，我们有能力定位到JVM或JavaScript。如果我们在现有项目中添加新的Kotlin文件，Kotlin将提示我们。如果我们开始一个新项目，我们可以在设置向导中选择目标，假设我们使用IntelliJ IDEA。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image.png?resize=610%2C499&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

我们还需要将Kotlin标准库添加到该项目中。点击创建按钮，我们会提示我们要复制这些文件的位置。默认情况下，它的副本是一个名为script的文件夹。我们稍后会介绍，因为它很重要。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image1.png?resize=603%2C157&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

## 项目组织

由此产生的项目结构应该是

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image2.png?resize=350%2C196&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

该项目有两个文件被添加：

* lib文件夹包含头文件，作为开发过程中使用的jar文件。
* 脚本文件夹包含一个kotlin.js，它是Kotlin运行时库。这用于生产。

我们所有的Kotlin源代码都应放在src文件夹中。一旦编译完成，它将生成一些需要随kotlin.js运行时文件一起发送的JavaScript文件。
所有其他源代码，作为这个外部JavaScript库或文件，CSS和HTML文件可以放置在任何地方，最好在同一个项目中，使开发更容易，但不一定。对于我们的例子，我们将把它放在一个名为web的文件夹中，并创建一系列子文件夹来构建我们的代码。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image3.png?resize=344%2C259&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

## 设置工作流程

当我们编写Kotlin代码时，编译器将生成一些需要作为我们应用程序一部分发送的JavaScript。默认情况下，IntelliJ IDEA将将该文件及其源映射输出到名为/ production / {project_name}的文件夹中

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image4.png?resize=275%2C154&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; margin: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

在开发过程中，我们需要最新版本的这些文件，因此我们希望将这些文件放在web / js / app文件夹中。使用IntelliJ IDEA工件或Maven / Gradle可以在很多方面做到这一点。在我们的例子中，我们只是使用一个工件。我们可以设置一个将相应的文件复制到所需的输出位置，另外还将最初复制到脚本文件夹的kotlin.js文件复制到同一个位置*。
*这是一次性操作，所以更好的选择是在设置项目时将此文件的输出位置直接定义到所需的输出文件夹。我们这样做是为了逐步解释事情。
## 与DOM元素交互

现在我们已经准备好项目布局了，我们开始编写一些代码。我们可以做的最基本的事情是操纵一些DOM元素。我们可以创建一个简单的HTML页面（名为index.html），并将其放在Web文件夹下
这个想法是现在使用Kotlin更新输入字段的值。为此，我们可以创建一个名为main.kt的新文件，并将其放在我们的src文件夹下。
## 面向网络的图书馆

Kotlin提供了一系列专门针对网络的图书馆。在我们的例子中，由于我们想操纵DOM，所以我们可以导入js.dom.html来访问文档变量。最终的代码将是
这很简单。我们使用document.getElementById来检索DOM元素，然后使用setAttribute设置它的值。完全一样的方式，我们使用JavaScript，除了这里我们使用Kotlin，并有静态打字的好处，除其他外。
标准库已经支持DOM操作，HTML 5功能（如Canvas和本地存储），以及用于常见库（如jQuery）的包装。我们会在更多的时候添加更多的内容，我们将在未来的帖子中介绍其中的一些内容。
## 运行代码

现在我们已经编译了代码，我们需要实际运行它。为此，我们必须同时参考我们的index.html页面中的kotlin.js以及生成的（basic.js）文件。

{% raw %}
<p> </p>
{% endraw %}

当加载页面时，主函数的代码将自动被调用。
一旦我们加载了我们的index.html页面，我们应该看到结果。

{% raw %}
<p><img alt="image" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image5.png?resize=638%2C283&amp;ssl=1"/></p>
{% endraw %}

## 从JavaScript调用Kotlin

如果我们要在Kotlin中使用JavaScript中的一些代码怎么办？例如，想想需要在客户端和服务器上重复需要重复的某种业务逻辑的场景。所有我们需要做的是写它，然后调用它。这是Kotlin写的一个简单的函数

{% raw %}
<p> </p>
{% endraw %}

这被放置在与应用程序相同的模块内，我们可以通过Kotlin模块名称来引用它*
*这个API不是最终的，未来很可能会发生变化，而且可能会更加紧凑。
# 下一步

这不是所有可能与科特林。我们没有提到的一件事是能够从Kotlin内部调用JavaScript代码，这是我们将在另一个帖子中覆盖的东西，因为这个已经变得太久了！
如果你想玩Kotlin到JavaScript，而不需要安装任何东西，你也可以直接在浏览器中尝试。和往常一样，给我们您的反馈！
