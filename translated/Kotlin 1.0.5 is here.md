---
title: "[译]Kotlin 1.0.5 is here"
date: 2016-11-08 22:04:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/11/kotlin-1-0-5-is-here/
translator:
translator_url:
---

我们很高兴地宣布，我们刚刚发布了 Kotlin 1.0.5**，它继续了 Kotlin 1.0 的一系列错误修复和工具更新。
我们要感谢我们的外部贡献者，他们的引用请求被包含在这个版本中： [基拉里·拉赫曼](https://github.com/cypressious) ， [弗拉季斯拉夫·戈卢布](https://github.com/ensirius) ， [Vsevolod Tolstopyatov](https://github.com/qwwdfsad) ， [Yoshinori Isogai](https://github.com/shiraji) ， [takahirom](https://github.com/takahirom) 和 [gitreelike](https://github.com/gitreelike) 。感谢所有尝试 EAP 构建的人，并向我们发送反馈意见！
发布中的完整更改列表可以在 [更新日志](https://github.com/JetBrains/kotlin/blob/1.0.5/ChangeLog.md) 。值得强调的一些变化是：
### 循环到λ转换

IntelliJ IDEA 插件现在可以检测许多情况，其中`循环的命令式`可以使用标准库函数（例如`filter`和`map < / code>。作为一个简单的例子，下面的代码段：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val result = arrayListOf<String>()
for (s in list) {
    if (s.isNotEmpty()) {
        result.add(s)
    }
}
```

{% raw %}
<p></p>
{% endraw %}

...将自动转换为：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val result = list.filter { it.isNotEmpty() }
```

{% raw %}
<p></p>
{% endraw %}

要触发转换，将插入符号放在`关键字的`上，然后按<kbd> Alt-Enter </kbd>。<br/>
<span id =“more-4350”> </span>
### 后缀代码完成

IntelliJ IDEA 的 [后缀代码完成](https://blog.jetbrains.com/idea/2014/03/postfix-completion/) 现在支持 Kotlin，拥有大量模板。请注意，该功能取决于 IntelliJ IDEA 2016.2 中进行的平台更改，因此在 Android Studio 2.2 中不可用;它将基于较新的 IntelliJ Platform 版本在较新版本的 Android Studio 中得到支持。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-postfixCompletion.png?ssl=1" rel="attachment wp-att-4358"><img alt="1-0-5-postfixcompletion" class="alignnone size-full wp-image-4358" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-postfixCompletion.png?resize=640%2C465&amp;ssl=1"/></a></p>
{% endraw %}

### 新的重构

Kotlin 插件现在支持“提取界面”和“提取超类”重构，以前只支持 Java 和其他一些语言，以及一个全新的重构“引入类型参数”，提供了一个简单的方法来改变类或功能成为通用的。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-extractInterface.png?ssl=1" rel="attachment wp-att-4359"><img alt="1-0-5-extractinterface" class="alignnone size-full wp-image-4359" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-extractInterface.png?resize=640%2C363&amp;ssl=1"/></a></p>
{% endraw %}

### Android IDE 支持改进

Kotlin 1.0.5 更新了 Kotlin Lint 检查功能，与 Android Studio 2.2 的 Java Lint 检查功能相同，在此过程中修复了很多问题。它还增加了一个期待已久的功能：“提取字符串资源”的意图，允许将硬编码的字符串字面值从 Kotlin 代码移动到字符串资源文件。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-android-extract-string-resource.png?ssl=1" rel="attachment wp-att-4357"><img alt="1-0-5-android-extract-string-resource" class="alignnone size-full wp-image-4357" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-android-extract-string-resource.png?resize=640%2C188&amp;ssl=1"/></a></p>
{% endraw %}

### JavaScript 支持改进

Kotlin 1.0.5 为 JavaScript 后端添加了两个主要的新功能：

* @JsName 注释允许控制从 Kotlin 代码生成的 JavaScript 函数和属性的名称，使得从简单的 JavaScript 调用 Kotlin 编译的代码更容易;
* 现在支持类文字（Foo :: class）。 a :: class 表达式的值不会实现完整的 KClass API;它只定义一个 simpleName 属性来访问类名。

### 如何更新

要更新插件，请使用工具 | Kotlin | 配置 Kotlin 插件更新，然后按“检查更新现在”按钮。另外，别忘了在 Maven 和 Gradle 构建脚本中更新编译器和标准库版本。
像往常一样，如果您遇到新版本的任何问题，欢迎您提供帮助 [论坛](https://discuss.kotlinlang.org/) ，在 Slack（获得邀请） [这里](http://kotlinslackin.herokuapp.com/) ），或报告中的问题 [问题追踪器](https://youtrack.jetbrains.com/issues/KT) 。
让我们来吧！
