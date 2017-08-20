---
title: Kotlin 1.2 M2 is out
author: Alexey Sedunov
date: 2017-08-09 17:56:00
source_url: https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-2-m2-is-out/
tags: 
categories:  官方动态
---

我们很高兴地宣布Kotlin 1.2的第二个里程碑版本。此版本的主要重点是Kotlin编译器和工具的稳定性和错误修复以及Kotlin标准库的改进。它还包括即将发布的Kotlin 1.1.4中提供的许多工具功能。
感谢您对新功能的反馈或您可能遇到的任何问题。
完整的变更日志自1.2 M1可以在这里找到，下面列出了一些主要的变化。

{% raw %}
<p><span id="more-5160"></span></p>
{% endraw %}

## 编译器

### 破解更改：Java默认方法调用

到目前为止，Kotlin接口成员覆盖Java默认方法，同时针对JVM 1.6在超级调用中产生了一个警告：在JVM目标1.6中不推荐使用超级调用Java默认方法。用'-jvm-target 1.8'重新编译。在1.2-M2版本中，我们将错误地替换为警告，因此需要使用-jvm-target 1.8选项编译任何此类代码
## 标准库

### 修改窗口/成对操作

我们一直在听取关于分块/窗口/成对功能KEEP-11的反馈意见，这些功能已经在上一个里程碑1.2-M1中发布预览，并且基于此，我们决定对这些功能进行一些更改：

* 窗口函数现在将其步骤参数默认为1。
它还会获得一个额外的可选参数partialWindows，它可以控制到底是不完整的窗口。默认情况下是false，这意味着不完整的窗口被删除。
* 成对的功能名称太混乱，不清楚如何将元素配对在一起。现在它被称为zipWithNext，所以更清楚的是，每个元素都在集合中的下一个元素压缩。

### 标准库中常见的数学运算

在标准库KT-4900中，长期以来一直要求支持数学运算。到目前为止，人们不得不在JVM平台中使用java.lang.Math类中的数学函数和常量，并在JS平台中将kotlin.js.Math暴露给Kotlin代码。
但现在我们在kotlin.math包中引入了以下几组API：

* 常数：PI和E;
* 三角函数：cos，sin，tan和它们的倒数：acos，asin，atan，atan2;
* 双曲：cosh，sinh，tanh;
* 指数：pow（扩展函数），sqrt，hypot，exp，expm1;
* 对数：log，log2，log10，ln，ln1p;
* 四舍五入：

大小，地板，截面，圆（半到偶）的功能;
roundToInt，roundToLong（一半到整数）扩展功能;
* 大小，地板，截面，圆（半到偶）的功能;
* roundToInt，roundToLong（一半到整数）扩展功能;
* 符号和绝对值：

绝对和符号功能;
absoluteValue和sign扩展属性;
withSign扩展功能;
* 绝对和符号功能;
* absoluteValue和sign扩展属性;
* withSign扩展功能;
* max和min两个值;
* 二进制表示法

ulp扩展属性;
nextUp，nextDown，nextTowards扩展功能;
toBits，toRawBits，Double.fromBits（这些都在kotlin包中）。
* ulp扩展属性;
* nextUp，nextDown，nextTowards扩展功能;
* toBits，toRawBits，Double.fromBits（这些都在kotlin包中）。

Float参数也可以使用相同的函数集（但不带常数）。
大多数这些功能（二进制表示组除外）也可以在JS中使用，从而解决了为两个平台编写相同的计算的问题。
## 预发行说明

与其他里程碑版本一样，我们不会为新语言和库功能提供向后兼容性保证。在1.2版本的里程碑版本中引入的任何内容都将在最终1.2版本之前发生变更。当我们到达最终RC时，由发行版本生成的所有二进制文件将被编译器取代：您需要重新编译1.2 x编译的所有内容。
  但是，由1.1.x和更早版本编译的所有代码完全没有重新编译。
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.2作为构建脚本和项目的存储库;使用1.2-M2作为编译器插件和标准库的版本号。
在IntelliJ IDEA：转到工具鈫？Kotlin鈫？配置Kotlin插件更新，然后在更新频道下拉列表中选择“访问预览1.2”，然后按检查更新。
命令行编译器可以从Github发行页面下载。
在try.kotlinlang.org上：使用右下角的下拉列表将编译器版本更改为1.2惭2（即将推出）。
