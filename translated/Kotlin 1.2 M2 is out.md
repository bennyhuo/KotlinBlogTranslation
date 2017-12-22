---
title: Kotlin 1.2 M2 is out
author: Alexey Sedunov
date: 2017-08-09 17:56:00
tags:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-2-m2-is-out/
translator: pye52 & 睡魔的倦意
translator_url: https://pye52.github.io/ & https://suima0v0.github.io/
---

我们很高兴地公布Kotlin 1.2的第二个里程碑版本。该版本的重点在于Kotlin编译器和工具的稳定性与bug修复，以及Kotlin标准库的改进。此外还包含了很多即将发布的Kotlin 1.1.4所具备的工具特性。

如果能有您对新特性或者运行中所遇到的任何问题的反馈，我们将非常感谢。

从1.2 M1开始，完整的更新日志可以在[这里](https://github.com/JetBrains/kotlin/blob/1.2-M2/ChangeLog.md)查看，重要的变更在下面列出：

{% raw %}
<p><span id="more-5160"></span></p>
{% endraw %}

## 编译器

### 重大更改：Java默认方法调用

到目前为止，Kotlin的接口成员在jvm 1.6重写Java默认方法的时候，如果通过super调用父类方法，将会得到一个警告`子类对Java默认方法的调用在JVM target 1.6已被弃用。请使用-jvm-target 1.8重新编译`。在1.2-M2版本中，我们将警告变更为错误，因此此类代码将需要使用`-jvm-target 1.8`编译

## 标准库

- ### 修正windowed/pairwise操作

  我们听取了大家[KEEP-11](https://github.com/Kotlin/KEEP/blob/master/proposals/stdlib/window-sliding.md)中关于chunked/windowed/pairwise函数的反馈，并且在1.2-M1里程碑版中发布了预览功能，在这基础上，我们还进行了如下改动：

- `windowed`函数的自增变量现在默认为1。
  同时还增加了一个额外的可选参数`partialWindows`，用于控制不完整的窗口的结束处理流程。默认值为false，表示不完整的窗口不会保留。

- `pairwise`函数名让人摸不着头脑，不知道它是如何配对元素的。所以我们新命名为`zipWithNext`，这更清楚地表明这函数会把集合中每个元素和下一个元素都压缩一次。

### 标准库中常用的数学运算

在标准库(KT-4900)[https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-4900]中，长期以来一直要求支持数学运算。到目前为止，人们不得不在JVM平台中使用java.lang.Math类中的数学函数和常量，并在JS平台中将kotlin.js.Math暴露给Kotlin代码。
但现在我们在kotlin.math包中引入了以下几组API：

- 常数：PI和E;
- 三角函数：cos，sin，tan和反三角函数：acos，asin，atan，atan2;
- 双曲：cosh，sinh，tanh;
- 指数：pow（扩展函数），sqrt，hypot，exp，expm1;
- 对数：log，log2，log10，ln，ln1p;
- 四舍五入：
  - ceil，floor，truncate，四舍五入(结果是偶数)的函数;
  - 四舍五入到整数、四舍五入到Long的扩展函数;
- 符号和绝对值：
  - 绝对值和符号函数;
  - absoluteValue和sign扩展属性;
  - withSign扩展函数;
- 针对两个值的max和min函数;
- 二进制表示
  - ulp扩展属性;
  - nextUp，nextDown，nextTowards扩展函数;
  - toBits，toRawBits，Double.fromBits（这些都在kotlin包中）。

Float类型也可以使用相同的函数功能（但不带常数）。
大多数这些功能（二进制表示除外）也可以在JS中使用，从而不需要为两个平台编写功能一样的代码。

## 预发行说明

> 与其他里程碑版本一样，我们不会为新的语言和标准库特性提供向后兼容性保证。在1.2版本的里程碑版本中引入的任何内容都将在最终1.2版本之前发生变更。当我们最终RC时，预发行版本的所有二进制文件将被编译器认为不合法：您需要重新编译1.2-Mx编译过的所有内容。
>
> 但是，由1.1.x和更早正式版本编译的所有代码无需重新编译也能正常运行。

## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.2作为构建脚本和项目的存储库;使用1.2-M2作为编译器插件和标准库的版本号。
在IntelliJ IDEA：打开工具 -> Kotlin -> 配置Kotlin插件更新，然后在更新窗口下拉列表中选择“Early Access Preview 1.2”，然后点击*Check for updates*。
命令行编译器可以从(Github版本发布页面)[https://github.com/JetBrains/kotlin/releases/tag/v1.2-M2]下载。
在(try.kotlinlang.org)[https://try.kotlinlang.org/]上：使用右下角的下拉列表将编译器版本更改为1.2-M2（即将推出）。