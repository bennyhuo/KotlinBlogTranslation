---
title: Kotlin 1.2 Beta2 is out
author: Dmitry Petrov
date: 2017-10-19 13:43:00
source_url: https://blog.jetbrains.com/kotlin/2017/10/kotlin-1-2-beta2-is-out/
tags: 
categories:  官方动态
---

我们很高兴地宣布Kotlin 1.2的第二个Beta版本。在这个版本中，我们一直主要关注较小的内部变化，并在我们的多平台项目故事中增加一些缺失的部分。
感谢Andrey Mischenko，Francesco Vasco，Jake Wharton，Jonathan Leitschuh，Kirill Rakhman，Pap Lorinc，Paul Merlin，Raluca Sauciuc，Toshiaki Kameyama和Yoshinori Isogai对Kotlin 1.2 Beta2的贡献。
自1.2-Beta以来的完整更新日志可以在这里找到，下面列出的重大更改。

{% raw %}
<p><span id="more-5350"></span></p>
{% endraw %}

## 编译器

### 编译器性能改进

自上次公开发布以来，有一系列的编译器性能改进。平均项目建设时间减少了近20％。
### 生成字节码后处理工具的代码规范化

从1.0版开始，Kotlin支持复杂控制流的表达式，如try-catch表达式和内联函数调用。这样的代码根据Java虚拟机规范是有效的。不幸的是，当构造函数调用的参数中存在这样的表达式时，一些字节码处理工具不能很好地处理这些代码。
为了缓解这种字节码处理工具的用户的这个问题，我们添加了一个命令行选项（-Xnormalize-constructor-calls = MODE），告诉编译器为这样的结构生成更多的类Java字节码。这里MODE是以下之一：

* 禁用（默认）“按照Kotlin 1.0和1.1中的相同方式生成字节码;
* 启用“为构造函数调用生成类似Java的字节码。这可以改变类加载和初始化的顺序;
* 保留类初始化 - 为构造函数调用生成类似于Java的字节码，确保保持类初始化顺序。这可能会影响应用程序的整体性能;只有在多个类之间共享一些复杂的状态并在类初始化时更新时才使用它。

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
