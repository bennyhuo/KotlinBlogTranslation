---
title: Kotlin 1.1.3 is out
author: Dmitry Jemerov
date: 2017-06-23 20:19:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlin-1-1-3-is-out/
tags: 
categories:  官方动态
---

我们很高兴地宣布发布Kotlin 1.1.3，这是Kotlin 1.1的一个新的错误修复和工具更新。该更新带来了许多新的IDE功能，编译器和IDE中的性能改进，生成的字节码的效率改进以及许多错误修复。该更新与2016年2月至2017年2月的所有版本的IntelliJ IDEA兼容，以及Android Studio 2.3和3.0 Canary。
注意：Android Studio 3.0 Canary 4有一个问题，可以防止正确加载Kotlin插件更新，因此您可以将该更新安装到Canary 4. Kotlin 1.1.3将捆绑到Android Studio 3.0 Canary 5中。
此版本中的完整更改列表可以在更改日志中找到。

{% raw %}
<p><span id="more-5079"></span></p>
{% endraw %}

我们要感谢我们的外部贡献者，他们的引用要求包括在这个版本中：AJ Alt，Chris Horner，Gaetan Zoritchak，Jonathan Leitschuh，Kirill Rakhman，Marek Langiewicz，Nadia Humbert-Labeaumaz，Shaun Reich，Yoshinori Isogai，尤其是尤里·菲特曼（尤里·菲特曼（尤里·菲特曼），他在此版本中提供了一个主要的新特性之一，参数/类型提示）。感谢所有尝试EAP构建的人，并向我们发送反馈意见！
## JDK 9支持

此版本增加了对Java 9 JDK编译Kotlin代码的初始支持。请注意，将来的1.1.x更新将支持基于模块的可见性检查;截至1.1.3，Kotlin不以任何方式使用module-info.java的信息。
## Maven并行构建

Kotlin Maven插件现在支持并行构建，所以如果您使用-T选项运行Maven，那么现在可以并行编译多个Kotlin模块。
## kapt增量编译

kapt现在逐渐构建Java存根，这使得使用注释处理的构建显着更快。
## TODO突出显示

TODO（）方法的使用现在在编辑器中作为TODO突出显示，并显示在TODO视图中。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-todo.png?ssl=1" rel="attachment wp-att-5080"><img alt="kotlin113-todo" class="alignnone size-full wp-image-5080" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-todo.png?resize=316%2C220&amp;ssl=1"/></a></p>
{% endraw %}

## 语义突出显示

如果您在“颜色和字体”设置中启用语义突出显示，则Kotlin将突出显示具有不同颜色的每个局部变量和参数的定义和所有出现。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-semantic-highlighting.png?ssl=1" rel="attachment wp-att-5081"><img alt="kotlin113-semantic-highlighting" class="alignnone size-full wp-image-5081" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-semantic-highlighting.png?resize=640%2C381&amp;ssl=1"/></a></p>
{% endraw %}

## 参数名称提示

随着IntelliJ IDEA的Java支持，Kotlin现在支持在调用中显示参数名称的编辑器提示，其中参数的含义可能不会从上下文中清除。这对于通过纯Kotlin代码从Kotlin调用Java代码特别有用，这种情况应该通过使用命名参数来解决。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-parameter-name.png?ssl=1" rel="attachment wp-att-5082"><img alt="kotlin113-parameter-name" class="alignnone size-full wp-image-5082" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-parameter-name.png?resize=640%2C34&amp;ssl=1"/></a></p>
{% endraw %}

## 类型提示

与上一个功能类似，Kotlin插件现在支持在编辑器提示中显示推断的变量，函数和参数类型。默认情况下禁用此功能;您可以在编辑器外观设置中启用它。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-type-hints.png?ssl=1" rel="attachment wp-att-5083"><img alt="kotlin113-type-hints" class="alignnone size-full wp-image-5083" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-type-hints.png?resize=640%2C409&amp;ssl=1"/></a></p>
{% endraw %}

## 如何更新

要更新插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“淐呵呵更新” - 按钮。此外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本。
像往常一样，如果您遇到新版本的任何问题，欢迎您在论坛上请求帮助，在Slack（在这里获得邀请）或报告问题跟踪器中的问题。
让檚ot lin！
