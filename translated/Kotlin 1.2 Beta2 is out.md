---
title: Kotlin 1.2 Beta2 is out
author: Dmitry Petrov
date: 2017-10-19 13:43:00
source_url: https://blog.jetbrains.com/kotlin/2017/10/kotlin-1-2-beta2-is-out/
tags: 
categories:  官方动态
translator: SnakEys  
translator_url: https://github.com/SnakeEys

---

Kotlin1.2的第二个Beta版本发布了。在该版本中，我们把注意力主要放在较小的内部变化上，并对多平台项目中的缺失部分进行了增补。  

非常感谢Andrey Mischenko，Francesco Vasco，Jake Wharton，Jonathan Leitschuh，Kirill Rakhman，Pap Lorinc，Paul Merlin，Raluca Sauciuc，Toshiaki Kameyama和Yoshinori Isogai对Kotlin 1.2 Beta2所做出的贡献。

查看1.2 Beta发布以来的[完整更新日志](https://github.com/JetBrains/kotlin/blob/1.2-Beta2/ChangeLog.md)，重要变更如下。

{% raw %}
<p><span id="more-5350"></span></p>
{% endraw %}

## 编译器

### 编译器性能提升

自上次公开版本发布后我们对编译器的性能进行了一系列的改进，项目构建的平均时间节省近20%。

### 字节码后处理工具生成代码规范化

从1.0版本开始，Kotlin就支持复杂控制流的表达式，如try-catch表达式和内联函数(inline fun)调用。这些代码是符合Java虚拟机规范的。然而不幸的是，部分字节码处理工具并不能较好的处理这些代码，尤其是当调用构造函数的参数中存在此类表达式时。

为了缓解这个问题，用户在使用此类字节码处理工具时，可以通过添加命令行选项(`-Xnormalize-constructor-calls=MODE`)，告诉编译器为此类构造函数生成更类似Java的字节码。`MODE`参数可以是如下之一：


* `disable`（默认）- 以Kotlin 1.0和1.1版本同样的方式生成字节码；
* `enable` - 为构造函数调用生成更类似Java的字节码。但会改变类加载和初始化的顺序；
* `preserve-class-initialization` - 为构造函数调用生成类似Java的字节码，确保类初始化顺序不变。但会影响应用程序的整体性能；仅在多个类之间需要共享复杂状态和类初始化更新时使用。

上述“手动”的解决方案是将具有控制流的子表达式的值存储在变量中，而非直接在调用参数中进行求值。类似于`Xnormalize-constructor-calls=enable`。

更多详细信息请查阅[KT-19251](https://youtrack.jetbrains.com/issue/KT-19251)。

## 多平台项目
对于多平台项目的支持有着难以数计的改进，大多集中在IDE方面，但远不止如此。而最值得注意的有如下内容：

### 编写多平台单元测试的注解

在通用项目中编写测试并独立在每个平台项目中编译运行已经成为可能。目前在`kotlin-test`包中提供4个注解：`@Test`，`@Ignore`，`@BeforeTest`，`@AfterTest`，用于提升通用代码的测试。  
在JVM平台这些注解被映射到相应的JUnit 4注解，JS从1.1.4版本已经开始支持JS单元测试。

使用时需要对通用模块添加`kotlin-test-annotations-common`依赖，在JVM模块中添加`kotlin-test-junit`，在js模块中添加`kotlin-test-js`。

### “implement”更名为“expectedBy”。

伴随着`expect`/`actual`命名之后，Gradle依赖项配置`implement`（由平台项目使用，以指向其相应的公共项目）现已被重命名为`expectedBy`，并且旧的名称已被弃用。


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
在平台模块中引用通用代码有令人心烦的问题，这一情况在多模块多平台项目中并未得到改善。现在从Gradle中引入这些项目已然固定，且不再需要额外手动添加依赖来解决这些问题。

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

### 发布前注意事项
*与其它里程碑式发布版本相似，我们对新语言以及特征库<strong>无法提供向后兼容性保证</strong>。任何在1.2里程碑版本中引入的内容都将以最终的1.2版本<strong>变更为准</strong>。在最后的RC版本中，编译器会将所有预发布版本生成的二进制文件当作非法文件：开发者可能需要重新将之前由1.2-Mx，1.2-Beta或者1.2-Beta2编译的内容重新进行编译。*  
*但是，由1.1.x以及更早版本编译的代码无需重新编译亦可完美运行。*

## 如何尝试
**Maven/Gradle：**添加`http://dl.bintray.com/kotlin/kotlin-eap-1.2`作为构建脚本和项目的仓库；修改编译器插件以及标准库版本号为`1.2.0-beta-88`。  

**IntelliJ IDEA：**在菜单栏中依次选择***Tools → Kotlin → Configure Kotlin Plugin Updates***， 并在***Update Channel***下拉列表中选择“Early Access Preview 1.2”，点击***Check for updates***。  
命令行编译器可在[Github页面](https://github.com/JetBrains/kotlin/releases/tag/v1.2-beta2)下载。


**[try.kotlinlang.org](https://try.kotlinlang.org/)：**可在右下角的下拉列表将编译器版本更改为1.2Beta2（即将推出）。
