---
title: Kotlin/Native v0.4 released: Objective-C interop, WebAssembly and more
author: Nikolay Igotti
date: 2017-11-16 15:26:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinnative-v0-4-released-objective-c-interop-webassembly-and-more/
tags: 
categories:  官方动态
---

We’re happy to announce the release of Kotlin/Native v0.4, KotlinConf 2017 edition! This release adds support for accessing Objective-C APIs on iOS and macOS, WebAssembly target platform, as well as introduces major changes making app development in Kotlin/Native way easier.
# Platform libraries

To enable access to underlying operating system interfaces, Kotlin/Native provides a set of platform-specific libraries available to any program targeting a particular platform. Previously, you needed to use the cinterop tool to generate the libraries yourself, and now they’re available out of the box.
The following program demonstrates the use of the new platform libraries in the v0.4 release.
import platform.posix.*
import kotlinx.cinterop.*
 
fun readFileData(path: String) = memScoped {
    val info = alloc<stat>()
    if (stat(path, info.ptr) != 0) return@memScoped null
    val size = info.st_size.toInt()
    val result = ByteArray(size)
    val file = fopen(path, "rb") ?: return@memScoped null
    var position = 0
    while (position < size) {
        val toRead = minOf(size - position, 4096)
        val read = fread(result.refTo(position), 1, toRead.signExtend(), file).toInt()
        if (read <= 0) break
        position += read
    }
    fclose(file)
    result
}
 
fun main(args: Array<String>) {
  for (file in args) {
      val data = readFileData(file)
      if (data != null) {
          write(STDOUT_FILENO, data.refTo(0), data.size.signExtend())
      }
  }
}
It will read the contents of a file into a Kotlin ByteArray and then will print it to standard output. So now the full power of operating system interfaces is at your hands without the need of explicit interop stubs generation.
Note that we can use Kotlin objects for storing a result of platform call fread, see below in ‘Object Pinning’ section.
# iOS and macOS framework interoperability

On Apple platforms, unlike most other platforms, access to system frameworks is provided in the form of Objective-C APIs. To support that, the Kotlin/Native team has implemented an Objective-C interoperability layer. For example, the following code, written in pure Kotlin/Native, will read an application’s resource on iOS:
fun readResource(resourceName: String): ByteArray {
    val filePath = NSBundle.mainBundle.pathForResource(resourceName, ofType = null)

    val fileData = NSData.dataWithContentsOfFile(filePath!!)
            ?: throw Error("failed reading resource $resourceName")

    return fileData.bytes!!.readBytes(fileData.length.toInt())
}
And the following complete program will render a top-level window on macOS. Note that the window title is in Cyrillic, to show that we perform correct character set conversion in the interoperability layer.
import kotlinx.cinterop.*
import platform.AppKit.*
import platform.Foundation.*
import platform.objc.*
import platform.osx.*
 
private fun runApp() {
    val app = NSApplication.sharedApplication()
    app.delegate = MyAppDelegate()
    app.setActivationPolicy(NSApplicationActivationPolicy.NSApplicationActivationPolicyRegular)
    app.activateIgnoringOtherApps(true)
    app.run()
}
 
private class MyAppDelegate() : NSObject(), NSApplicationDelegateProtocol {
    private val window: NSWindow
    init {
        val mainDisplayRect = NSScreen.mainScreen()!!.frame
        val windowRect = mainDisplayRect.useContents {
            NSMakeRect(
                    origin.x + size.width * 0.25, origin.y + size.height * 0.25,
                    size.width * 0.5, size.height * 0.5
            )
        }
        val windowStyle = NSWindowStyleMaskTitled or NSWindowStyleMaskMiniaturizable or
                NSWindowStyleMaskClosable or NSWindowStyleMaskResizable
        window = NSWindow(windowRect, windowStyle, NSBackingStoreBuffered, false).apply {
            title = "Окошко Konan"
            preferredBackingLocation = NSWindowBackingLocationVideoMemory
            backgroundColor = NSColor.whiteColor()
            releasedWhenClosed = false

            delegate = object : NSObject(), NSWindowDelegateProtocol {
                override fun windowShouldClose(sender: ObjCObject): Boolean {
                    NSApplication.sharedApplication().stop(this)
                    return true
                }
            }
        }
    }
    override fun applicationWillFinishLaunching(notification: NSNotification) {
        window.makeKeyAndOrderFront(this)
    }
}
 
fun main(args: Array<String>) {
    autoreleasepool {
        runApp()
    }
}
See Kotlin/Native fullstack application iOS client for an example of a complete application for iOS. If you own an Apple or Android device, feel free to see this application in action on App Store and on Google Play.
# Object pinning

To simplify using Kotlin objects with C APIs we provide new APIs for typed arrays (ByteArray, IntArray, FloatArray etc.), namely refTo(), pin() and unpin(). See Pinning.kt. They allow to ensure an object is locked in memory, and its data has a stable address, thus allowing to use Kotlin object data directly from C APIs and vice versa. For example, in readFileData() function above we pass pointer to data in ByteBuffer to fread() call.
# Improved debugging

Debugging with release v0.4 adds improved inspections, so most variables could be inspected in runtime. For example, if we take the program to read a file from the first section, and compile it with the debugging support (note -g switch), we can perform symbolic debugging and variables inspections.

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

Kotlin/Native v0.4  have an experimental support of WebAssembly (-target wasm32). WebAssembly target is mostly intended to showcase the technology, as it is still not fully production ready due to browser support limitations (mainly around more seamless DOM/HTML5 APIs access and performance of virtual machines executing WASM). However, we’re very interested in feedback from our users, to know how much interest in WASM support is there.
# IDE Support

Last, but not the least, we have recently announced an experimental CLion plugin supporting Kotlin/Native, see this post for more details.
# Getting the bits

Binaries could be downloaded below:
* x86-64 Linux hosts
* x86-64 MacOS hosts
* x86-64 Windows hosts
# Feedback

Please report bugs and issues in the Kotlin bug tracker. Questions are welcome on #kotlin-native channel on Slack.
