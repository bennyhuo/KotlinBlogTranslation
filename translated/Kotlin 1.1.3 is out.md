---
title: Kotlin 1.1.3 is out
author: Dmitry Jemerov
date: 2017-06-23 20:19:00  
translator: SnakEys  
translator_url: https://github.com/SnakeEys
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlin-1-1-3-is-out/
tags: 
categories:  官方动态
---

Kotlin 1.1.3版本发布啦！这也是基于1.1版本以来的又一次Bug修复和工具更新。适用于2016.2到2017.2之间所有版本的IntelliJ IDEA，以及Android Studio 2.3和3.0 Canary版本；本次更新不仅改善了编译器和IDE的性能，还极大提高了生成字节码的效率。  

**注意：**目前在Android Studio 3.0 Canary 4版本中存在不能正确加载Kotlin插件更新的问题，因此在Canary 4的版本中无法安装该更新。Kotlin 1.1.3则会自动打包到Android Studio 3.0 Canary 5版本中。  

此次发布版本的完整更新列表可以在[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.3/ChangeLog.md)中查看。

{% raw %}
<p><span id="more-5079"></span></p>
{% endraw %}

感谢在本次发布中向我们提交pull request的贡献者们：[AJ Alt](https://github.com/ajalt)，[Chris Horner](https://github.com/chris-horner)，[Gaetan Zoritchak](https://github.com/gzoritchak)，[Jonathan Leitschuh](https://github.com/jlleitschuh)，[Kirill Rakhman](https://github.com/cypressious)，[Marek Langiewicz](https://github.com/langara)，[Nadia Humbert-Labeaumaz](https://github.com/nphumbert)，[Shaun Reich](https://github.com/sreich)，[Yoshinori Isogai](https://github.com/shiraji)，特别感谢[Yuli Fiterman](https://github.com/fitermay)（他在此版本中贡献了几大主要新功能之一：参数/类型提示）。同时也感谢所有使用EAP构建以及向我们发送宝贵意见的人！

## JDK 9支持

本次发布增加了对Java 9 JDK编译Kotlin代码的初始支持。但在未来的1.1.x更新将支持基于模块的可见性检查；截至1.1.3，Kotlin尚不能以任何方式使用module-info.java中的信息。
## Maven并行构建

Kotlin Maven插件现在支持[并行构建](https://cwiki.apache.org/confluence/display/MAVEN/Parallel+builds+in+Maven+3)，使用 -T 选项运行Maven即可并行编译多个Kotlin模块。
## kapt增量编译

kapt现已具备增量构建Java存根的能力，因此使用注解处理时构建会显著更快。 
## TODO高亮显示

使用[TODO()](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-t-o-d-o.html)方法会在编辑器中作为TODO高亮显示，并会展示在TODO视图中。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-todo.png?ssl=1" rel="attachment wp-att-5080"><img alt="kotlin113-todo" class="alignnone size-full wp-image-5080" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-todo.png?resize=316%2C220&amp;ssl=1"/></a></p>
{% endraw %}

## 语义突出显示

如果在“颜色和字体 (Colors & Fonts)”设置中启用语义高亮显示，Kotlin则会以不同颜色显示每个局部变量和参数的定义以及使用。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-semantic-highlighting.png?ssl=1" rel="attachment wp-att-5081"><img alt="kotlin113-semantic-highlighting" class="alignnone size-full wp-image-5081" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-semantic-highlighting.png?resize=640%2C381&amp;ssl=1"/></a></p>
{% endraw %}

## 参数名称提示

继[IntelliJ IDEA Java支持](https://blog.jetbrains.com/idea/2016/09/intellij-idea-2016-3-eap-faster-git-log-parameter-hints-and-more/)之后，现在Kotlin支持在上下文参数意义不明的方法调用中为参数名称展示编辑器提示。这一功能在使用Java调用Kotlin代码时尤为有用 —— 而在纯Kotlin代码中，同样的情形则通过命名参数的方式解决。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-parameter-name.png?ssl=1" rel="attachment wp-att-5082"><img alt="kotlin113-parameter-name" class="alignnone size-full wp-image-5082" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-parameter-name.png?resize=640%2C34&amp;ssl=1"/></a></p>
{% endraw %}

## 类型提示

与上一个功能类似，Kotlin插件现在支持在编辑器提示中显示变量，函数和参数的推断类型。默认情况下此功能禁用；若需启用请参考下图设置：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-type-hints.png?ssl=1" rel="attachment wp-att-5083"><img alt="kotlin113-type-hints" class="alignnone size-full wp-image-5083" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2017/06/kotlin113-type-hints.png?resize=640%2C409&amp;ssl=1"/></a></p>
{% endraw %}

## 如何更新

更新插件，请依次在菜单栏中选择 Tools | Kotlin | Configure Kotlin Plugin Updates并点击"Check for updates now"按钮。此外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本。  

像往常一样，如果您在新版本中遇到的任何问题，欢迎您在[论坛](https://discuss.kotlinlang.org/)上寻求帮助，在Slack（[获得邀请](http://slack.kotlinlang.org/)）或在[问题跟踪器](https://youtrack.jetbrains.com/oauth?state=%2Fissues%2FKT)中上报问题。  
Let's Kotlin!
