---
title: Kotlin/Native v0.5 released: calling Kotlin from Swift and C, LLVM 5 and more
author: Nikolay Igotti
date: 2017-12-19 17:16:00
tags: 
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/12/kotlinnative-v0-5-released-calling-kotlin-from-swift-and-c-llvm-5-and-more/
translator: pye52 & 黄志强
translator_url: https://pye52.github.io/ & https://suima0v0.github.io/
---

我们很高兴地宣布Kotlin / Native 迎来了0.5圣诞版！该版本支持将Kotlin / Native嵌入到C，Objective-C和Swift代码中，同时可以使用iOS模拟器开发了，LLVM 5也被纳入到支持中，以及可以在Linux和Windows的主机中创建WebAssembly。

# Objective-C和Swift的reverse interop

我们曾经在之前的版本中提及过，如何在Kotlin / Native中调用Apple框架，但前提是存在Objective-C头文件。现在我们换了一种方式，以支持从Swift和Objective-C调用Kotlin的代码。为此我们提供了一个新的编译器选项`-produce framework`。它将生成一个独立的框架，可以从应用程序的其他地方调用，就好像它本身就是用Swift编写的一样。下面让我们来看看这个[计算器例子](https://github.com/JetBrains/kotlin-native/tree/master/samples/calculator)。它的界面采用的是[Swift编写](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/calculator/calculator/ViewController.swift#L12)，而计算逻辑则采用[Kotlin编写](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/calculator/src/main/kotlin/org/konan/arithmeticparser/Parser.kt#L17)。Swift代码与Kotlin完美混合。例如，这行Swift代码：

```kotlin
private let parser = KAPPartialParser(composer: KAPCalculator(), partialComposer: PartialRenderer())
```

创建Kotlin类[PartialParser](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/calculator/src/main/kotlin/org/konan/arithmeticparser/Parser.kt#L143)的实例，并将实现了Kotlin接口[ExpressionComposer](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/calculator/src/main/kotlin/org/konan/arithmeticparser/Parser.kt#L42)的Swift类[PartialRenderer](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/calculator/calculator/ViewController.swift#L115)实例赋予给它。
请注意，像numbers和strings这样的基本类型在Swift和Kotlin中的映射是透明的。
若要构建项目，只需在XCode中打开，然后设置为真实设备或模拟器进行编译，请参阅[README.md](https://github.com/JetBrains/kotlin-native/blob/master/samples/calculator/README.md)了解更加详细的信息。

<img alt="Screen Shot 2017-12-18 at 18.40.21" class="alignnone size-full wp-image-5638" height="1918" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/12/Screen-Shot-2017-12-18-at-18.40.21.png" width="2804"/>

IntelliJ IDEA中的Kotlin代码：

<img alt="Screen Shot 2017-12-18 at 19.44.38" class="alignnone size-full wp-image-5643" height="1848" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/12/Screen-Shot-2017-12-18-at-19.44.38.png" width="3508"/>

# Reverse interop from C

我们也对其他平台提供reverse interop的特性，允许从外部调用Kotlin / Native代码。现代底层语言的标准是C，所以这是我们需要进行互操作的语言。开启编译器选项`-produce dynamic`将会生成一个动态库（如同macOS上的`.dylib`，Linux上的`.so`和Windows上的`.dll`），其中包含调用Kotlin / Native代码所需的所有内容。为了更容易理解，我们决定通过[Python扩展](https://github.com/JetBrains/kotlin-native/tree/master/samples/python_extension)来演示这种互操作性。Python调用C的实现，而C调用[Kotlin的实现](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/python_extension/src/main/kotlin/Server.kt#L23)，参考以下[例子](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/python_extension/src/main/c/kotlin_bridge.c#L87)：

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

Kotlin / Native编译器将生成一个动态库，而Python distutils[构建工具](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/python_extension/src/main/python/setup.py#L19)生成另一个起决定作用的动态库。Python[起始代码](https://github.com/JetBrains/kotlin-native/blob/6ee6f5907d808f21af06436e6c44b6fe2b9bb6b5/samples/python_extension/src/main/python/main.py#L19)通过C来桥接Kotlin / Native转换的对象和原始类型。
# 其他改进


* 在Kotlin 1.2中，`kotlin.math`包被添加到Kotlin标准库中。Kotlin / Native v0.5版也支持`kotlin.math`包中的函数
* 得益于对clang工具链、bitcode codegenerator和优化器的支持，LLVM 5.0.0也在这个版本中得到支持。
* 现在可以在Linux和Windows系统的主机上生成WebAssembly目标代码（`-target wasm32`）（在这之前只支持macOS系统）
* Workers API得到了这些改进：允许更方便地使用worker的执行结果和允许与worker交互初始值
* 其他bug的改进及性能提升

# 获取二进制包

可以在以下链接下载二进制包：

* [x86-64 for macOS](download.jetbrains.com/kotlin/native/kotlin-native-macos-0.5.tar.gz)
* [x86-64 for Linux](download.jetbrains.com/kotlin/native/kotlin-native-linux-0.5.tar.gz)
* [x86-64 for Windows](download.jetbrains.com/kotlin/native/kotlin-native-windows-0.5.zip)

# 反馈

若遇到问题请向[Kotlin bug 跟踪器](kotl.in/issue)提交报告。欢迎在[Slack](http://slack.kotlinlang.org/)的*kotlin本地*频道上讨论。（获得[邀请](https://kotl.in/slack)）
