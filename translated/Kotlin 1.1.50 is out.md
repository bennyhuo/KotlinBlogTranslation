---
title: Kotlin 1.1.50 is out
author: Dmitry Jemerov
date: 2017-09-22 18:13:00
source_url: https://blog.jetbrains.com/kotlin/2017/09/kotlin-1-1-50-is-out/
tags: 
categories:  官方动态
---

Kotlin1.1.50版本正式发布，本次更新是基于1.1版本的Bug修复及工具更新，包括： 

* 采取新的版本控制方案：使用1.1.5x替代1.1.5-x
* 提升对JSR-305标准注解的支持（可空性问题可作为警告方式进行提示，基于JSR-305标准的类无路径时进行检查）
* 提升生成字节码的性能
* 使原始数组为TypedArray转换，增加源代码映射支持死码消除工具，并对JS后端进行其他改进
* 编译器和IDE的Bug修复
* 在IntelliJ插件中引入新的检查项，性能提升和错误修复
* 支持预览Kotlin序列化插件的扩展点

本次更新兼容2016.3至2017.3版本的IntelliJ IDEA以及Android Studio 2.3和3.0。
此版本中的完整更改列表可在更改日志中找到。

{% raw %}
<p><span id="more-5280"></span></p>
{% endraw %}

我们要感谢我们的外部贡献者，他们的推荐要求包括在这个版本中：Andrius Semionovas，Dimach，Kirill Rakhman，Toshiaki Kameyama，scache，Andr茅奥娅，Daniil Vodopian，Nagesh Susarla和Knize。
## 版本控制方案更改

从本版本开始，而不是使用版本1.1.5,1.1.5-1,1.1.5-2等，将使用1.1.50,1.1.51,1.1.52等。
我们想将版本号与发行版本相同的JS工件发布到NPM。这里的问题是我们使用破折号后面的数字作为修补程序号，而NPM考虑将破折号作为预先释放的版本。这意味着NPM认为Kotlin 1.1.5比1.1.5-1更新，而实际情况恰恰相反。更改版本控制方案可以解决问题。
## JSR-305注释支持改进

Kotlin 1.1.4引入了默认可空性注释的初始支持，例如@ParametersAreNonnullByDefault作为选择加入功能。在Kotlin 1.1.50中，由于这种注释，检测到的无效性问题默认情况下报告为警告。要将它们转换为错误，请添加命令行参数-Xjsr305 = strict。要禁用警告，请使用-Xjsr305 = ignore。 （请注意，现在不推荐使用用于在Kotlin 1.1.4中启用默认可空性注释的命令行参数-Xjsr305-annotations = enable。）
此外，由于此版本，Kotlin不再需要在库的依赖关系中具有JSR-305注释的.jar文件，以便读取此库的可空性信息。
## JavaScript后端改进

Kotlin 1.1.50引入了几个改变，它们破坏了JavaScript后端的二进制向前兼容性。这意味着如果要使用Kotlin / JS 1.1.50编译的库，您应该将编译器更新为1.1.50或更高版本。您仍然可以使用使用旧版本的Kotlin编译器编译的库。
### 内衬改进

将内联函数转换为JS的方式已更改，以避免在内联函数体中使用完全限定名称。这减少了生成的JS文件的大小。
### TypedArrays默认启用

默认情况下，原始数组将转换为TypedArrays。可以通过将-Xtypedarrays = false传递给编译器来禁用此功能。这种变化影响二进制向前兼容性？不建议使用旧的编译器与新的库。
请注意，新的数组表示也可能会影响从Kotlin调用JS代码。要调用一个需要常规数组而不是TypedArray的JS函数，请使用toTypedArray扩展函数将TypedArray转换为常规数组。类似于IntArray的函数可用于将原始数组转换为TypedArray。

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

这种改变也使得可以在运行时区分Array和IntArray等。

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

### DCE中的源地图支持

Kotlin 1.1.50改进了死码消除工具，使其更容易调试其输出。该工具检测现有的源地图并将其与代码一起转换。有关JS调试的更多信息，请参阅本教程。
## IntelliJ IDEA插件改进

IntelliJ IDEA插件在新版本中的改进部分：

* 性能提升
* 支持导入别名的代码完成
* 更好地支持Gradle Kotlin DSL
* 校验代码是否与项目配置的格式以及约定命名相匹配
* 其它新特性及问题修复

## 如何更新

更新插件，请依次在菜单栏中选择 Tools | Kotlin | Configure Kotlin Plugin Updates并点击"Check for updates now"按钮。此外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本。

与往常一样，如果您在新版本中遇到的任何问题，欢迎您在[论坛](https://youtrack.jetbrains.com/issues/KT)上寻求帮助，在Slack（[获得邀请](http://slack.kotlinlang.org/)）或在[问题跟踪器](https://youtrack.jetbrains.com/issues/KT)中上报问题。
Let's Kotlin!
