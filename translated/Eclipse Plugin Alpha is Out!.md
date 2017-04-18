---
title: "[译]Eclipse Plugin Alpha is Out!"
date: 2015-03-31 00:54:00
author: Nikolay Krasko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/eclipse-plugin-alpha-is-out/
---

IntelliJ IDEA中的Kotlin支持一直是我们的首要任务之一，但是我们也一直致力于Eclipse的支持，今天我们很高兴地介绍这一努力的第一个<strong> alpha </ strong>结果。
虽然这只是一个开始，但很多事情会随着时间的推移而改善，它已经具备了

* 建立和运行您的代码
* Java互操作性
* 代码突出显示
* 调试
* 导航
* 基本代码完成（Ctrl +空格）
* 自动导入
* 单元测试

## 安装

要试一试，你需要一个干净的安装 [Eclipse Luna](https://www.eclipse.org/downloads/) 。 Kotlin插件可从Eclipse市场</ em>获得。安装Kotlin插件的最简单方法是将该按钮拖放到正在运行的Eclipse窗口</ strong>中：

{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a><br/>
<span id="more-1945"></span></p>
{% endraw %}

或者，您可以使用<em>帮助 - ＆gt; Eclipse Marketplace ... </ em>菜单或以下更新站点：

{% raw %}
<p></p>
{% endraw %}

```kotlin
https://dl.bintray.com/jetbrains/kotlin/eclipse-plugin/last/
 
```

{% raw %}
<p></p>
{% endraw %}

我们的 [教程](http://kotlinlang.org/docs/tutorials/getting-started-eclipse.html)  更详细地介绍安装过程。
## Eclipse IDE支持

在这里，我们快速概述此版本中提供的功能。
### 建立你的代码

Kotlin编译器集成到Eclipse的构建过程中，因此您可以在一个Eclipse项目中自由地混合Kotlin和Java。
您可以先创建一个新的Kotlin项目或者将Kotlin文件添加到现有的Java项目中。在任一种情况下，Java类都可以从Kotlin访问，反之亦然。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/New-Kotlin-File-in-Context-Menu.png"><img alt="New Kotlin File in Context Menu" class="alignnone size-full wp-image-1957" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/New-Kotlin-File-in-Context-Menu.png?resize=640%2C194&amp;ssl=1"/></a></p>
{% endraw %}

问题视图</ em>显示Kotlin报告的诊断（错误和警告）：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/03/skitch.png"><img alt="Problems View in Action" class="alignnone size-full wp-image-1959" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/03/skitch.png?resize=640%2C241&amp;ssl=1"/></a></p>
{% endraw %}

### 编辑

支持基本编辑器功能，如代码高亮和格式化。还支持基本代码完成，但需要进一步改进。
对于Java和Kotlin的未解决的类，自动导入</ em>已经存在：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.26.27.png"><img alt="Eclipse Auto-Import Feature" class="alignnone size-full wp-image-1965" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.26.27.png?resize=393%2C119&amp;ssl=1"/></a></p>
{% endraw %}

许多 [快速修复](https://github.com/JetBrains/kotlin/tree/master/idea/src/org/jetbrains/kotlin/idea/quickfix)  和 [意图](https://github.com/JetBrains/kotlin/tree/master/idea/src/org/jetbrains/kotlin/idea/intentions)  在编辑Kotlin源时将会很有用，我们将逐渐增加越来越多的来源。我们从简单的开始，用索引运算符（<code> [...] </ code>）替换<code> get（）</ code>调用：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.29.20.png"><img alt="Replace 'get' With Index Operator" class="alignnone size-full wp-image-1966" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.29.20.png?resize=500%2C83&amp;ssl=1"/></a></p>
{% endraw %}

### 导航

<em>开放声明</ em>是此版本中唯一支持的导航操作：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/eclipse-references.png"><img alt="Eclipse References" class="alignnone size-full wp-image-1969" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/eclipse-references.png?resize=592%2C159&amp;ssl=1"/></a></p>
{% endraw %}

此外，您可以使用<em>大纲视图</ em>导航到Kotlin文件中的声明，并在<em>开放资源</ em>窗口中按名称搜索Kotlin文件。
### 调试器

安装了我们的插件后，Eclipse JDT调试器可以初步支持Kotlin。再次，有很多改进，但你可以

* 在Kotlin代码中设置断点
* 使用Step / over / out
* 查看局部变量和Kotlin对象的内容


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-16.39.21.png"><img alt="Eclipse Debug" class="alignnone size-full wp-image-1971" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-16.39.21.png?resize=640%2C176&amp;ssl=1"/></a></p>
{% endraw %}

### 单元测试

如果您在类路径中已经有JUnit 3或JUnit 4，则可以在Kotlin中编写测试。运行 - ＆gt;运行方式 - ＆gt;主菜单中的Kotlin JUnit测试</ em>开始测试，并在<em> JUnit View </ em>中打开结果。

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.29.png"><img alt="Eclipse Tests Demonstation" class="alignnone size-full wp-image-1962" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.29.png?resize=560%2C199&amp;ssl=1"/></a></p>
{% endraw %}


{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.51.png"><img alt="Eclipse Tests Result" class="alignnone size-full wp-image-1961" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.51.png?resize=503%2C172&amp;ssl=1"/></a></p>
{% endraw %}

## 反馈欢迎

我们可以慢慢地继续实现功能，使插件越来越稳定和强大。但是，我们决定显示早期的阿尔法希望<strong>反馈</ strong>。对我们来说非常重要。
我们已经有一些问题和功能要求 [跟踪器](https://youtrack.jetbrains.com/search/Kotlin%20Eclipse-19206) 。请填写免费添加更多。谢谢。
此外，这是一个开放源码的项目，我们期望它比我们的编译器和IntelliJ Plugin更加是一个<strong>社区努力</ strong>，所以你的 [拉请求](https://github.com/JetBrains/kotlin-eclipse/)  非常欢迎
