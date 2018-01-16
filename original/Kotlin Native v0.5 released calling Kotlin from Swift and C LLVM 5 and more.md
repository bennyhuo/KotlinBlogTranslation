---
title: Kotlin/Native v0.5 released: calling Kotlin from Swift and C, LLVM 5 and more
author: Nikolay Igotti
date: 2017-12-19 17:16:00
source_url: https://blog.jetbrains.com/kotlin/2017/12/kotlinnative-v0-5-released-calling-kotlin-from-swift-and-c-llvm-5-and-more/
tags: 
categories:  官方动态
---

We’re happy to announce the release of Kotlin/Native v0.5, Christmas edition! This release adds support for using Kotlin/Native code from C, Objective-C and Swift, supports development using iOS simulator, along with LLVM 5 support and creating WebAssembly from Linux and Windows hosts.

{% raw %}
<p><span id="more-5635"></span></p>
{% endraw %}

# Reverse interop from Objective-C and Swift

In the previous release of Kotlin/Native we introduced calling Apple frameworks from Kotlin/Native, assuming they provide Objective-C headers. Now we go another way around, and add support for calling Kotlin code from Swift and Objective-C. For that, a new compiler option, -produce framework, has been implemented. It generates a self-contained framework, which could be used from other parts of your application, as if it was written in Swift. Let’s take a look at the calculator example. It has UI written in Swift along with calculator logic written in Kotlin. Swift code intermixes with Kotlin transparently. For example, this line of Swift code:

{% raw %}
<p></p>
{% endraw %}

```kotlin
private let parser = KAPPartialParser(composer: KAPCalculator(), partialComposer: PartialRenderer())
```

{% raw %}
<p></p>
{% endraw %}

creates an instance of the Kotlin class PartialParser, and gives it an instance of a Swift class PartialRenderer implementing a Kotlin interface ExpressionComposer.
Note, that basic types like numbers and strings are transparently mapped between Swift and Kotlin worlds.
To build the project, just open it in XCode and compile it for either a real device or the simulator, see the README.md for details.

{% raw %}
<p><img alt="Screen Shot 2017-12-18 at 18.40.21" class="alignnone size-full wp-image-5638" height="1918" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/12/Screen-Shot-2017-12-18-at-18.40.21.png" width="2804"/></p>
{% endraw %}

And Kotlin code in IntelliJ IDEA:

{% raw %}
<p><img alt="Screen Shot 2017-12-18 at 19.44.38" class="alignnone size-full wp-image-5643" height="1848" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/12/Screen-Shot-2017-12-18-at-19.44.38.png" width="3508"/></p>
{% endraw %}

# Reverse interop from C

For other platforms we also support reverse interoperability, allowing to call Kotlin/Native code from the outside world. The lowest common denominator of modern languages is C, so this was the language we interoperate with. Compiler option -produce dynamic produces a dynamic library (such as .dylib on macOS, .so on Linux and .dll on Windows) containing everything needed to work with Kotlin/Native code. To make things fancy we decided to demonstrate this interoperability by creating Python extension. Python calls to C implementations and they call Kotlin implementation like this:

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

The Kotlin/Native compiler produces a dynamic library, and then Python distutils build tool produces another dynamic library, depending on that one. So Python launcher code calls Kotlin/Native objects via C bridge and gets both object and primitive types properly converted.
# Other improvements


* In Kotlin 1.2, the kotlin.math package was added to the Kotlin standard library. With v0.5 Kotlin/Native supports operations available in kotlin.math package as well
* LLVM 5.0.0 is supported with this release, as both clang toolchain and bitcode codegenerator and optimizer
* Code for WebAssembly targets (-target wasm32) now can be produced from Linux and Windows hosts (before only macOS hosts were supported)
* Workers API was improved by allowing easier consumption of worker execution result and adding ability to pass primitive values from and to worker
* Bugfixes and improvements

# Getting the bits

Binaries could be downloaded below:

* x86-64 macOS hosts
* x86-64 Linux hosts
* x86-64 Windows hosts

# Feedback

Please report bugs and issues in the Kotlin bug tracker. Questions are welcome on #kotlin-native channel on Slack (get invite here).
