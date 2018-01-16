---
title: Kotlin/Native v0.5 released: calling Kotlin from Swift and C, LLVM 5 and more
author: Nikolay Igotti
date: 2017-12-19 17:16:00
source_url: https://blog.jetbrains.com/kotlin/2017/12/kotlinnative-v0-5-released-calling-kotlin-from-swift-and-c-llvm-5-and-more/
tags: 
categories:  官方动态
---

我们很高兴宣布推出Kotlin / Native v0.5，圣诞版！此版本增加了对使用C，Objective-C和Swift的Kotlin / Native听代码的支持，支持使用iOS模拟器的开发以及LLVM 5支持，以及从Linux和Windows主机创建WebAssembly。

{% raw %}
<p><span id="more-5635"></span></p>
{% endraw %}

# Objective-C和Swift的反向交互

在之前的Kotlin / Native版本中，我们介绍了从Kotlin / Native调用Apple框架，假设他们提供了Objective-C头文件。现在我们换一种方式，添加从Swift和Objective-C调用Kotlin代码的支持。为此，已经实现了一个新的编译器选项-produce框架。它生成一个自包含的框架，可以从应用程序的其他部分使用，就好像它是用Swift编写的一样。让我们来看看这个计算器的例子。它具有用Swift编写的用户界面以及用Kotlin编写的计算器逻辑。 Swift代码与Kotlin混合透明。例如，这行Swift代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
private let parser = KAPPartialParser(composer: KAPCalculator(), partialComposer: PartialRenderer())
```

{% raw %}
<p></p>
{% endraw %}

创建Kotlin类PartialParser的实例，并为其提供实现Kotlin接口ExpressionComposer的Swift类PartialRenderer的实例。
请注意，像数字和字符串这样的基本类型在Swift和Kotlin世界之间是透明映射的。
要构建项目，只需在XCode中打开它，然后将其编译为真实设备或模拟器，请参阅README.md了解详细信息。

{% raw %}
<p><img alt="Screen Shot 2017-12-18 at 18.40.21" class="alignnone size-full wp-image-5638" height="1918" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/12/Screen-Shot-2017-12-18-at-18.40.21.png" width="2804"/></p>
{% endraw %}

IntelliJ IDEA中的Kotlin代码：

{% raw %}
<p><img alt="Screen Shot 2017-12-18 at 19.44.38" class="alignnone size-full wp-image-5643" height="1848" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/12/Screen-Shot-2017-12-18-at-19.44.38.png" width="3508"/></p>
{% endraw %}

# 从C反向交互

对于其他平台，我们也支持反向互操作性，允许从外部调用Kotlin / Native代码。现代语言的最低标准是C，所以这是我们互操作的语言。编译器选项-produce dynamic会生成一个动态库（例如macOS上的.dylib，Linux上的.so和Windows上的.dll），其中包含使用Kotlin / Native代码所需的所有内容。为了使事情变得奇特，我们决定通过创建Python扩展来演示这种互操作性。 Python调用C实现，他们调用Kotlin实现像这样：

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (PyArg_ParseTuple(args, "Lss", &session_arg, &string_arg1, &string_arg2)) {
       T_(Server) server = getServer();
       T_(Session) session = { (void*)(uintptr_t)session_arg };
       const char* string = __ kotlin.demo.Server.concat(server, session, string_arg1, string_arg2);
       result = Py_BuildValue("s", string);
       __ DisposeString(string);
    } else {
        result = Py_BuildValue("s", NULL);
    }
```

{% raw %}
<p></p>
{% endraw %}

Kotlin / Native编译器生成一个动态库，然后Python distutils构建工具生成另一个动态库，具体取决于那个。因此，Python启动器代码通过C桥调用Kotlin / Native对象，并正确转换对象和原始类型。
# 其他改进


* 在Kotlin 1.2中，kotlin.math包被添加到Kotlin标准库中。使用v0.5 Kotlin / Native也支持kotlin.math包中的操作
* 这个版本支持LLVM 5.0.0，因为clang工具链和bitcode codegenerator和优化器都支持
* 现在可以从Linux和Windows主机上生成WebAssembly目标代码（-target wasm32）（仅在支持macOS主机之前）
* 通过允许更容易地使用工作者执行结果和增加从工作者传递原始值的能力，工人API得到了改进
* 漏洞修复和改进

# 获取位

二进制文件可以在下面下载：

* x86-64 macOS主机
* x86-64 Linux主机
* x86-64 Windows主机

# 反馈

请报告Kotlin错误跟踪器中的错误和问题。问题是欢迎的＃kotlin本地听频道在Slack（获得邀请在这里）。
