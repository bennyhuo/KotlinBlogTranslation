---
title: Kotlin/Native v0.4 released: Objective-C interop, WebAssembly and more
author: Nikolay Igotti
date: 2017-11-16 15:26:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinnative-v0-4-released-objective-c-interop-webassembly-and-more/
tags: 
categories:  官方动态
---

我们很高兴宣布发布Kotlin / Native v0.4，KotlinConf 2017版！此版本增加了对iOS和MacOS，WebAssembly目标平台上Objective-C API的访问支持，同时还介绍了使Kotlin / Native方式的应用程序开发变得更为简单的重大变化。
# 平台库

为了访问底层操作系统接口，Kotlin / Native提供了一套针对特定平台的任何程序可用的特定于平台的库。以前，您需要使用cinterop工具来自己生成库，现在它们是开箱即用的。
以下程序演示了v0.4发行版中新平台库的使用。
导入platform.posix。*
导入kotlinx.cinterop。*
鈥？
fun readFileData（path：String）= memScoped {
    val info = alloc <stat>（）
    if（stat（path，info.ptr）！= 0）return @ memScoped null
    val size = info.st_size.toInt（）
    val结果= ByteArray（大小）
    val file = fopen（path，“rb”）？：return @ memScoped null
    var position = 0
    while（position <size）{
        val toRead = minOf（size  -  position，4096）
        val read = fread（result.refTo（position），1，toRead.signExtend（），file）.toInt（）
        如果（读取<= 0）中断
        位置+ =读取
    }
    FCLOSE（文件）
    结果
}
鈥？
fun main（args：Array <String>）{
  for（file in args）{
      val data = readFileData（file）
      if（data！= null）{
          写（STDOUT_FILENO，data.refTo（0），data.size.signExtend（））
      }
  }
}
它会将文件的内容读入Kotlin ByteArray，然后将其打印到标准输出。所以现在操作系统界面的全部力量就在你的手中，而不需要显式的互斥存根的产生。
请注意，我们可以使用Kotlin对象来存储平台调用fread的结果，请参见下面的“对象定位”部分。
# iOS和macOS听框架的互操作性

在大多数其他平台上，在苹果平台上，以Objective-C API的形式提供对系统框架的访问。为了支持这一点，Kotlin / Native团队实施了一个Objective-C互操作层。例如，以纯Kotlin / Native编写的以下代码将读取iOS上的应用程序资源：
有趣的readResource（资源名称：字符串）：ByteArray {
    val filePath = NSBundle.mainBundle.pathForResource（resourceName，ofType = null）

    val fileData = NSData.dataWithContentsOfFile（filePath !!）
            ？：抛出错误（“失败的阅读资源$资源名称”）

    return fileData.bytes !!。readBytes（fileData.length.toInt（））
}
下面的完整程序将在macOS上呈现顶层窗口。请注意窗口标题是西里尔文，以表明我们在互操作层中执行正确的字符集转换。
导入kotlinx.cinterop。*
导入平台.AppKit。*
导入平台。基础。*
导入platform.objc。*
导入platform.osx。*
鈥？
私人乐趣runApp（）{
    val app = NSApplication.sharedApplication（）
    app.delegate = MyAppDelegate（）
    app.setActivationPolicy（NSApplicationActivationPolicy.NSApplicationActivationPolicyRegular）
    app.activateIgnoringOtherApps（真）
    app.run（）
}
鈥？
私人类MyAppDelegate（）：NSObject（），NSApplicationDelegateProtocol {
    私人val窗口：NSWindow
    在里面 {
        val mainDisplayRect = NSScreen.mainScreen（）!!。frame
        val windowRect = mainDisplayRect.useContents {
            NSMakeRect（
                    origin.x + size.width * 0.25，origin.y + size.height * 0.25，
                    size.width * 0.5，size.height * 0.5
            ）
        }
        val windowStyle = NSWindowStyleMaskTitled或NSWindowStyleMaskMiniaturizable或
                NSWindowStyleMaskClosable或NSWindowStyleMaskResizable
        window = NSWindow（windowRect，windowStyle，NSBackingStoreBuffered，false）.apply {
            title =“袨泻芯褕泻芯港南”
            preferredBackingLocation = NSWindowBackingLocationVideoMemory
            backgroundColor = NSColor.whiteColor（）
            发布时间=关闭=假

            委托=对象：NSObject（），NSWindowDelegateProtocol {
                重写有趣的windowShouldClose（sender：ObjCObject）：Boolean {
                    NSApplication.sharedApplication（）。停止（这种）
                    返回true
                }
            }
        }
    }
    重写有趣的applicationWillFinishLaunching（通知：NSNotification）{
        window.makeKeyAndOrderFront（本）
    }
}
鈥？
fun main（args：Array <String>）{
    autoreleasepool {
        runApp（）
    }
}
请参阅iOS客户端的Kotlin / Native fullstack应用程序，了解iOS完整应用程序的示例。如果您拥有Apple或Android设备，请随时在App Store上和Google Play上观看此应用程序。
# 对象锁定

为了简化在C API中使用Kotlin对象，我们为类型化数组（ByteArray，IntArray，FloatArray等）提供了新的API，即refTo（），pin（）和unpin（）。见Pinning.kt。它们允许确保对象锁定在内存中，并且其数据具有稳定的地址，从而允许直接从C API使用Kotlin对象数据，反之亦然。例如，在上面的readFileData（）函数中，我们将指向ByteBuffer中的数据的指针传递给fread（）调用。
# 改进的调试

使用发行版v0.4进行调试增加了检查，因此大多数变量可以在运行时检查。例如，如果我们让程序从第一部分读取一个文件，并用调试支持（note -g switch）编译它，我们可以执行符号调试和变量检查。

{% raw %}
<p></p>
{% endraw %}

```kotlin
#
# bin/konanc kat.kt  -o kat -g
# lldb kat.kexe
(lldb) target create "kat.kexe"
Current executable set to 'kat.kexe' (x86_64).
(lldb) command script import tools/konan_lldb.py
(lldb) b kfun:main(kotlin.Array&lt;kotlin.String&gt;)
Breakpoint 1: where = kat.kexe`kfun:main(kotlin.Array&lt;kotlin.String&gt;) + 26 at kat.kt:25, address = 0x00000001000023ba
(lldb) print args
(ObjHeader *) $1 = [/etc/groups]
 
```

{% raw %}
<p></p>
{% endraw %}

# WebAssembly

Kotlin / Native v0.4拥有WebAssembly的实验支持（-target wasm32）。由于浏览器支持的限制（主要围绕更加无缝的DOM / HTML5 API访问和执行WASM的虚拟机的性能），WebAssembly的目标主要是为了展示该技术，因为它还没有完全准备好生产。但是，我们非常感兴趣的是来自用户的反馈，了解WASM支持的兴趣。
# IDE支持

最后，我们最近宣布了一个支持Kotlin / Native的实验性CLion插件，请参阅这篇文章了解更多细节。
# 获取位

二进制文件可以在下面下载：
* x86-64 Linux主机
* x86-64 MacOS主机
* x86-64 Windows主机
# 反馈

请报告Kotlin错误跟踪器中的错误和问题。在Slack的＃kotlin-native频道上欢迎您的问题。
