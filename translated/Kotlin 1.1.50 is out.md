---
title: Kotlin 1.1.50 is out
author: Dmitry Jemerov
date: 2017-09-22 18:13:00
source_url: https://blog.jetbrains.com/kotlin/2017/09/kotlin-1-1-50-is-out/
tags: 
categories:  官方动态
translator: SnakEys  
translator_url: https://github.com/SnakeEys  

---

Kotlin1.1.50版本正式发布，本次更新是基于1.1版本的Bug修复及工具更新，包括： 

* 采取新的版本控制方案：使用1.1.5x替代1.1.5-x
* 改进对JSR-305标准注解的支持（可空性问题可作为警告方式进行提示，基于JSR-305标准的类无路径时的检查任务）
* 提升生成字节码的性能
* 启用原始数组转换TypedArray，增加废弃代码消除工具的源代码映射支持，其它JS后端改进
* 编译器和IDE的Bug修复
* 在IntelliJ插件中引入新的检查项，性能提升和错误修复
* 支持预览Kotlin序列化插件的扩展点

本次更新兼容2016.3至2017.3版本的IntelliJ IDEA以及Android Studio 2.3和3.0。
本次发布的完整内容请参阅[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.50/ChangeLog.md)。

{% raw %}
<p><span id="more-5280"></span></p>
{% endraw %}

此外特别感谢对本次发布提交PR的外部贡献者们：[Andrius Semionovas](https://github.com/neworld), [Dimach](https://github.com/Dimach), [Kirill Rakhman](https://github.com/cypressious), [Toshiaki Kameyama](https://github.com/t-kameyama), [scache](https://github.com/sckm), [André Oriani](https://github.com/aoriani), [Daniil Vodopian](https://github.com/voddan), [Nagesh Susarla](https://github.com/nageshs)以及[Knize](https://github.com/Knize)。

## 版本控制方案更改

从本次发布的版本开始将使用1.1.50，1.1.51，1.1.52版本号替代旧的1.1.5，1.1.5-1，1.1.5-2版本号。

我们希望使用与发布版本相同的版本号将JS组件发布至NPM，一直以来我们将“-”后面的数字作为补丁号使用，而NPM则将“-”后的数字作为[预发布版本](https://docs.npmjs.com/misc/semver#prerelease-tags)。因此在NPM看来，Kotlin 1.1.5的版本高于1.1.5-1，然而这恰恰与实际情况背道而驰，所以只需变更版本方案即可解决。

## 改进对JSR-305注解的支持

在Kotlin 1.1.4中引入了**默认可空性注解**的试验性支持，例如使用[@ParametersAreNonnullByDefault](http://static.javadoc.io/com.google.code.findbugs/jsr305/3.0.1/javax/annotation/ParametersAreNonnullByDefault.html)作为可选功能。在Kotlin 1.1.50中，由于这种注释，检测到的可空性问题默认情况下**被报告为警告**。若将警告转换为错误报告，需要添加命令行参数`-Xjsr305 = strict`。要禁用警告，请使用`-Xjsr305 = ignore`。 （注意现已不推荐使用在Kotlin 1.1.4中启用默认可空性注释的命令行参数`-Xjsr305-annotations = enable`）。  

此外自本次发布版本开始，Kotlin不再需要在依赖库中添加包含JSR-305注解的.jar文件以用于读取此库的可空性信息。  

请注意编译器对严格模式下的JSR-305支持被标记为**实验性质**。
## JavaScript后端提升

Kotlin 1.1.50新引入的几项变化使得JavaScript后端不再向前兼容，这表明Kotlin/JS 1.1.50编译的库仅支持1.1.50或更高版本的编译器，但仍然可以使用旧版本Kotlin编译器所编译的库。

### 行内函数改进
为了避免在行内函数体中使用全匹配名称，我们对行内函数转换为JS的方式进行了修改，并缩小了生成JS文件的大小。

### TypedArrays默认启用

默认情况下，原始数组将转换为[TypedArrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)，若需要禁用此特性，设置编译参数`-Xtypedarrays = false`即可。该项特性会对旧版本的兼容性有所影响--因此并不建议在旧的编译器下使用新的编译库。

值得注意的是新的数组表示方法也可能会影响Kotlin调用JS代码，若需要从JS函数获取常规数组而非TypedArray时，使用[toTypedArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-typed-array.html)函数将TypedArray转换为常规数组。例如类似[toIntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-int-array.html)的函数可将常规的基础类型数组转换为TypedArray。

{% raw %}
<p></p>
{% endraw %}

```kotlin
val intArray: IntArray = intArrayOf(1, 2, 3) // equivalent to Int32Array.of(1, 2, 3)
val arrayOfInts: Array<Int> = intArray.toTypedArray() // arrayOfInts equals to [1, 2, 3]
val otherIntArray: IntArray = arrayOfInts.toIntArray() // otherIntArray is Int32Array
 
```

{% raw %}
<p></p>
{% endraw %}

这些变化也使得可在运行时对Array和IntArray等类似情况进行区分。


{% raw %}
<p></p>
{% endraw %}

```kotlin
val intArray: Any = intArrayOf(1, 2, 3) // Int32Array.of(1, 2, 3)
intArray is IntArray && intArray !is Array<*> // true
 
val arrayOfInts: Any = arrayOf(1, 2, 3) // [1, 2, 3]
arrayOfInts !is IntArray && arrayOfInts is Array<*> // true
 
```

{% raw %}
<p></p>
{% endraw %}

### DCE源映射支持

Kotlin 1.1.50改进了[废弃代码消除工具](https://kotlinlang.org/docs/reference/javascript-dce.html)，使其更容易调试输出。该工具可检测已有的源并将其与代码同时转换，更多关于JS调试信息可参阅本[教程](https://kotlinlang.org/docs/tutorials/javascript/debugging-javascript/debugging-javascript.html)。
## IntelliJ IDEA插件强化

IntelliJ IDEA插件在新版本中的改进部分：

* 性能提升
* 支持导入别名的代码补全
* 更好地支持Gradle Kotlin DSL
* 校验代码是否与项目配置的格式以及约定命名相匹配
* 其它新特性及问题修复

## 如何更新

更新插件，请依次在菜单栏中选择 Tools | Kotlin | Configure Kotlin Plugin Updates并点击"Check for updates now"按钮。此外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本。

与往常一样，如果您在新版本中遇到的任何问题，欢迎您在[论坛](https://youtrack.jetbrains.com/issues/KT)上寻求帮助，在Slack（[获得邀请](http://slack.kotlinlang.org/)）或在[问题跟踪器](https://youtrack.jetbrains.com/issues/KT)中上报问题。
Let's Kotlin!
