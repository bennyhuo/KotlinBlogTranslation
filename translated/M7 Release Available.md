---
title: "[译]M7 Release Available"
date: 2014-03-20 00:00:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/03/m7-release-available/
translator:
translator_url:
---

Kotlin M7在这里和它一些期待已久的功能。
## 编译器和语言变化

### 内联支持

M7的最大特点之一是支持内联功能。 Kotlin鼓励使用高阶函数（有些人称之为“功能性样式”），这需要大量使用lambda表达式。从M7开始，您可以将更高阶的函数声明为“内联”，这意味着它的正文将在调用站点以及传递给它的任何lambdas内联。这意味着使用这些功能的性能损失是无关紧要的。例如，使用**循环而不是使用*forEach*并传递一个lambda在速度方面几乎没有区别。
<span id =“more-1439”> </span> <br/>
内联提供的优点包括生成的类的数量，字节码大小，更少的分配和更少的变形调用，所有这些都有助于这些性能提升。
Kotlin标准库的许多功能现在已经被列入了。
注意：如果内联中断代码（例如由于编译器错误），可以通过将<i> -inline off </i>命令行选项传递给编译器来关闭它（请参阅首选项 - >编译器 - > Kotlin编译器）：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/inline1.png"><img alt="inline" class="alignnone size-full wp-image-1462" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/inline1.png?resize=381%2C115&amp;ssl=1"/></a></p>
{% endraw %}

### toString（），equals（）和hashCode（）需要override指令

当声明*toString（）*，*equals（）*和*hashCode（）*时，我们现在需要使用*覆盖*关键词。这是以前版本中的**突破性变化**，适用于所有类。使用IDE中提供的快速修复（Alt + Enter错误）快速添加“覆盖”到项目中的所有这些方法。
### “jet”包更名为“kotlin”

核心类已被重命名为“kotlin”，这也意味着，是的，你猜到了，Kotlin现在是Kotlin的官方和最终名字。这也是一个潜在的**破坏性变化**。大多数进口将自动发生。如果遇到任何问题，请手动重命名导入。
### 参考本地功能

在Kotlin中，您可以使用*:: functionName*语法通过名称引用函数。这也适用于本地功能

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() {
 
    fun bar() {
 
    }
 
    fun biz(func: () -> Unit) {
 
    }
 
    biz(::bar)
}
```

{% raw %}
<p></p>
{% endraw %}

## 互操作性

### *[throws]*注释

现在，您可以使用*throws*注释来装饰函数，以指示当编译为JVM时该函数应声明哪些异常。

{% raw %}
<p></p>
{% endraw %}

```kotlin
[throws(javaClass<SocketException>()]
fun connect(host: String) {
...
}
```

{% raw %}
<p></p>
{% endraw %}

将被翻译成

{% raw %}
<p></p>
{% endraw %}

```kotlin
void connect(String host) throws SocketException {
...
}
```

{% raw %}
<p></p>
{% endraw %}

在Java中。
### JavaScript增强功能

您现在可以提供重载函数并将其编译为JavaScript。 Kotlin使用后缀_1，_2等创建新的函数。

{% raw %}
<p></p>
{% endraw %}

```kotlin
    foo: function () {
    },
    foo_1: function (param) {
    },
    foo_2: function (param, anotherParam) {
    }
```

{% raw %}
<p></p>
{% endraw %}

此外，JavaScript本机功能还允许将扩展文字作为参数传递。
## 标准库

标准图书馆正在重新加工。这包括引入*流*（除其他外，这将有助于更好地与Java 8的兼容性）和某些功能的弃用。
某些重新设计已导致库API破坏****。大多数功能仍然可用，但您可能需要稍微修复现有代码。
## IntelliJ IDEA增强功能

### 现在复制/粘贴插入导入

当从一个文件复制和粘贴代码到另一个文件时，IntelliJ IDEA将自动导入所需的任何软件包。
### 查找用途改进

查找用途现在涵盖本地课程。此外，您现在可以看到覆盖以及这些的分层视图。
### 智能完成

增强代码完成功能，支持枚举，Java静态成员以及匿名对象。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/smartcompletion1.gif"><img alt="smartcompletion1" class="alignnone size-full wp-image-1479" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/smartcompletion1.gif?resize=557%2C206&amp;ssl=1"/></a></p>
{% endraw %}

### 重构支持

某些重命名重构（如局部变量）现在可以在现场完成，而无需使用对话框。

{% raw %}
<p><img alt="In-Place Rename Refactoring" class="alignnone wp-image-1452" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/inplacerename1.gif?resize=312%2C89&amp;ssl=1"/></p>
{% endraw %}

### 安全删除

您现在可以安全地删除整个项目中未使用的符号，并使用安全删除重构
### 重新包装

现在支持所有导入的软件包重命名和相应的更新

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/renamepackage.png"><img alt="Rename Package" class="alignnone wp-image-1453" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/renamepackage.png?resize=321%2C116&amp;ssl=1"/></a></p>
{% endraw %}

### 与Java的移动重构集成

当执行Java代码的移动重构时，它现在更新Kotlin代码中的相应用法。
### 意图

此版本还为IntelliJ IDEA带来了一系列意向，其中包括：
#### 替换Elvis操作符如果有条件

安全访问操作员或者elvis操作员现在可以用更明确的方式替换，如果需要，只需简单地使用意图即可。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/elvis3.gif"><img alt="elvis3" class="alignnone size-full wp-image-1482" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/elvis3.gif?resize=473%2C116&amp;ssl=1"/></a></p>
{% endraw %}

#### Infix呼叫点限制呼叫

Infix呼叫可以转换为点限呼叫

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/infix.gif"><img alt="infix" class="alignnone size-full wp-image-1471" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/infix.gif?resize=473%2C90&amp;ssl=1"/></a></p>
{% endraw %}

#### 转换为表达体

能够使用简单的return语句将函数转换为表达式

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/convertbody.gif"><img alt="convertbody" class="alignnone size-full wp-image-1472" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/convertbody.gif?resize=473%2C90&amp;ssl=1"/></a></p>
{% endraw %}

#### 从字符串模板中的简单变量名称中添加和删除大括号

当我们在字符串模板中有变量名时，我们可以轻松添加或删除大括号

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/stringtemplates.gif"><img alt="stringtemplates" class="alignnone size-full wp-image-1473" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/stringtemplates.gif?resize=473%2C90&amp;ssl=1"/></a></p>
{% endraw %}

除了上述之外，还有

* 支持IntelliJ IDEA 13.1和Android Studio
* 通过懒惰分析进行性能改进，导致与Java的更好的互操作速度。
* 改进的Java2Kotlin转换器，导致更清晰的代码，并包括更好的复制/粘贴行为。
* 代码格式化程序的改进

## 其他改进

另外还有一些其他错误修复和功能

* 改进的控制流分析导致修复一些现有的错误。
* 更多的bootstrapping。我们在Kotlin使用越来越多的Kotlin。
* 对Kotlin标准库进行了一些改进。

我们可以找到编译器和插件 [GitHub上的发行页面](https://github.com/JetBrains/kotlin/releases/tag/build-0.7.270) 。<BR/>
如果您使用IntelliJ IDEA，您可以从中下载最新的插件 [我们的存储库](http://plugins.jetbrains.com/plugin?pr=idea&pluginId=6954) 或者通过IntelliJ IDEA中的插件直接更新。 Kotlin M7需要IntelliJ IDEA 13.1。
