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
* `preserve-class-initialization` - 为构造函数调用生成类似Java的字节码，确保类初始化顺序不变。但会影响应用程序的整体性能；仅在多个类之间需要共享复杂状态和类初始化更新时使用。

“手册”的解决方案是将具有控制流的子表达式的值存储在变量中，而非直接在调用参数中进行求值。类似于`Xnormalize-constructor-calls=enable`。

更多详细信息请查阅[KT-19251](https://youtrack.jetbrains.com/issue/KT-19251)。

## 多平台项目
IDE中对多平台项目支持方面有诸多改进，但不限于此。

### 编写多平台单元测试的注解

在常用项目中编写测试并独立在每个平台项目中编译运行已经成为可能。目前在`kotlin-test`包中提供4个注解，用于改进常用代码中的测试：`@Test`，`@Ignore`，`@BeforeTest`，`@AfterTest`。  
在JVM平台这些注解被映射到相应的JUnit 4注解，而在JS中从1.1.4版本便已经支持JS单元测试。

若要使用则需要对通用模块添加`kotlin-test-annotations-common`依赖，在JVM模块中添加`kotlin-test-junit`，在js模块中添加`kotlin-test-js`。

### “implement”更名为“expectedBy”。

在`expect`/`actual`命名之后，Gradle依赖项配置`implement`（由平台项目使用，以指向其相应的公共项目）现在被重命名为`expectedBy`，并且旧的名称已被弃用。


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

### 正确导入多模块的多平台项目
在平台模块中引用通用代码有令人心烦的问题，在多模块多平台项目中仍未解决。现在从Gradle中引入这些项目是固定的，并且不再需要通过额外手动添加依赖来解决这些问题。

## Gradle插件
### “warningsAsErrors错误”更名为“allWarningsAsErrors”。

在Kotlin 1.2 Beta中引入的`warningsAsErrors`标志被重命名为`allWarningsAsErrors`：

{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin.kotlinOptions.allWarningsAsErrors = true
 
```

{% raw %}
<p></p>
{% endraw %}
## 标准库

### “Throwable.addSuppressed”可用时被“Closeable.use”调用
在其它异常关闭资源后抛出异常时，`Closeable.use`函数最终调用`Throwable.addSuppressed`。要启用该功能需添加`kotlin-stdlib-jdk7`依赖项。

### 发布前的注意事项

与其他里程碑版本一样，我们也不会对新语言和库功能提供向后兼容保证。在1.2的里程碑版本中引入的任何内容在最终的1.2版本之前可能会发生变化。当我们达到最后的RC，由预发布版本生成的所有二进制文件将被编译器取缔：你以 - 檒l条需要重新编译，是由1.2鈥惭X，1.2测试版，或1.2的Beta2编译一切。
但是，所有由1.1.x和更早版本编译的代码在没有重新编译的情况下是完全正确的。
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.2作为构建脚本和项目的存储库;使用1.2.0-beta-88作为编译器插件和标准库的版本号。
## 在IntelliJ IDEA的：进入工具鈫科特林鈫配置科特林插件的更新，然后选择鈥淓阿尔利访问预览1.2鈥在更新通道下拉列表，然后按检查更新？？。
命令行编译器可以从GitHub发布页面下载。

在try.kotlinlang.org上：使用右下角的下拉列表将编译器版本更改为1.2（即将推出）。
