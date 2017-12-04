---
title: Kotlin 1.2 Beta2 is out
author: Dmitry Petrov
date: 2017-10-19 13:43:00
source_url: https://blog.jetbrains.com/kotlin/2017/10/kotlin-1-2-beta2-is-out/
tags: 
categories:  官方动态
---

Kotlin1.2的第二个Beta版本发布了。在该版本中，我们一直对较小的内部变化保持持续关注，并在多平台项目中对缺失部分增补。  

感谢Andrey Mischenko，Francesco Vasco，Jake Wharton，Jonathan Leitschuh，Kirill Rakhman，Pap Lorinc，Paul Merlin，Raluca Sauciuc，Toshiaki Kameyama和Yoshinori Isogai对Kotlin 1.2 Beta2所做出的贡献。

查看1.2 Beta发布以来的[完整更新日志](https://github.com/JetBrains/kotlin/blob/1.2-Beta2/ChangeLog.md)，以下列出的重大更改。

{% raw %}
<p><span id="more-5350"></span></p>
{% endraw %}

## 编译器

### 编译器性能提升

自上次公开版本发布后编译我们对编译器的性能进行一系列的改进，项目构建的平均时间节省近20%。

### 生成字节码后处理工具的代码规范化

从1.0版本开始，Kotlin就支持复杂控制流的表达式，如try-catch表达式和内联函数(inline fun)调用。这些代码是符合Java虚拟机规范的。然而不幸的是，部分字节码处理工具并不能较好的处理这些代码，尤其是当构造函数调用的参数中存在此类表达式时。

为了缓解这个问题，用户在使用此类字节码处理工具时，可以通过添加命令行选项(`-Xnormalize-constructor-calls=MODE`)，告诉编译器为此类构造函数生成更类似Java的字节码。`MODE`参数可以是如下之一：


* `disable`（默认）- 以Kotlin 1.0和1.1版本同样的方式生成字节码；
* `enable` - 为构造函数调用生成更类似Java的字节码。但会改变类加载和初始化的顺序；
* `preserve-class-initialization` - 为构造函数调用生成类似Java的字节码，确保类初始化顺序不变。但会影响应用程序的整体性能；建议只在多个类之间共享复杂状态且在类初始化更新时使用。

“解决方案”的解决方法是将具有控制流的子表达式的值存储在变量中，而不是直接在调用参数中对它们进行求值。它与-Xnormalize-constructor-calls = enable类似。
有关更多详细信息，请参阅KT-19251。
## 多平台项目

在多平台项目支持方面有许多改进，主要是在IDE中，但不仅如此。最值得注意的是以下几个。
### 编写多平台单元测试的注释

现在可以在一个普通的项目中编写测试，以便在每个平台项目中进行编译和运行。在kotlin-test包中提供了4个注释，用于标记常用代码中的测试：@Test，@Ignore，@BeforeTest和@AfterTest。
在JVM平台中，这些注释被映射到相应的JUnit 4注释，而在JS中它们已经可用，从1.1.4开始支持JS单元测试。
为了使用它们，你需要添加一个对通用模块通用的kotlin-test-annotations，对你的JVM模块的kotlin-test-junit，以及对JS模块的kotlin-test-js的依赖。
### “实施”更名为“预计”。




在期望/实际命名之后，Gradle依赖项配置实现（由平台项目使用，以指向其相应的公共项目）现在被重命名为expectedBy，并且旧的名称已被弃用。

正确导入具有多个模块的多平台项目

{% raw %}
<p></p>
{% endraw %}

```kotlin
dependencies {
    expectedBy project(':lib-common')
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 引用平台模块中的通用代码在多模块多平台项目中未解决的问题引起了一个讨厌的问题。现在，从Gradle导入这样的项目是固定的，您不必手动添加额外的依赖关系，以便解决这些引用。

Gradle插件
## “行动错误”更名为“警告错误”。




在Kotlin 1.2 Beta中引入的warningsAsErrors标志被重命名为allWarningsAsErrors：

### 标准库

“可以使用的”，“可用的”，“可以使用的”，“可以使用的”

{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin.kotlinOptions.allWarningsAsErrors = true
 
```

{% raw %}
<p></p>
{% endraw %}

## 最后，Closeable.use函数调用Throwable.addSuppressed，当一些其他异常关闭资源时抛出异常。要启用这种行为，你需要在你的依赖关系中有kotlin-stdlib-jdk7。

### 发布前的注意事项

与其他里程碑版本一样，我们也不会对新语言和库功能提供向后兼容保证。在1.2的里程碑版本中引入的任何内容在最终的1.2版本之前可能会发生变化。当我们达到最后的RC，由预发布版本生成的所有二进制文件将被编译器取缔：你以 - 檒l条需要重新编译，是由1.2鈥惭X，1.2测试版，或1.2的Beta2编译一切。
但是，所有由1.1.x和更早版本编译的代码在没有重新编译的情况下是完全正确的。
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.2作为构建脚本和项目的存储库;使用1.2.0-beta-88作为编译器插件和标准库的版本号。
## 在IntelliJ IDEA的：进入工具鈫科特林鈫配置科特林插件的更新，然后选择鈥淓阿尔利访问预览1.2鈥在更新通道下拉列表，然后按检查更新？？。
命令行编译器可以从GitHub发布页面下载。

在try.kotlinlang.org上：使用右下角的下拉列表将编译器版本更改为1.2（即将推出）。
