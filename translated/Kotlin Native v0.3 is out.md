---
title: Kotlin/Native v0.3 is out
author: Nikolay Igotti
date: 2017-06-22 20:41:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlinnative-v0-3-is-out/
tags: 
categories:  官方动态
translator: SnakEys
translator_url: https://github.com/SnakeEys
---

Kotlin/Native 0.3发布啦！此次升级包括支持Windows同时作为编译主机与运行平台，同时也增加了对Google Android设备运行native activities的支持。因此在Windows平台编写['Hello World'](https://github.com/JetBrains/kotlin-native/tree/master/samples/win32)看起来会像下面一样简单：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import win32.*
fun main(args: Array<String>) {
  MessageBoxW(null, "Привет!","标题", MB_YESNOCANCEL or MB_ICONQUESTION)
}
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-5071"></span></p>
{% endraw %}

[Android native activies](https://github.com/JetBrains/kotlin-native/tree/master/samples/androidNativeActivity/src/main/kotlin)事件处理：

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (AInputQueue_getEvent(queue, event.ptr) < 0) {
  logError("Failure reading input event")
  return
}
if (AInputEvent_getType(event.value) == AINPUT_EVENT_TYPE_MOTION) {
  when (AKeyEvent_getAction(event.value) and AMOTION_EVENT_ACTION_MASK) {
    AMOTION_EVENT_ACTION_DOWN -> {
      animating = false
      currentPoint = getEventPoint(event.value, 0)
      startTime = getEventTime(event.value)
      startPoint = currentPoint
    }
    AMOTION_EVENT_ACTION_UP -> {
      val endPoint = getEventPoint(event.value, 0)
      val endTime = getEventTime(event.value)
      ....
   }
   AMOTION_EVENT_ACTION_MOVE -> {
      val numberOfPointers = AMotionEvent_getPointerCount(event.value).toInt()
      for (i in 0 until numberOfPointers)
         move(getEventPoint(event.value, i))
   }
}
AInputQueue_finishEvent(queue, event.value, 1)
```

{% raw %}
<p></p>
{% endraw %}

## 调试

本次发布的版本支持源代码级调试（仅限单步调试）。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
$ bin/konanc string0.kt  -g -o string0
$ lldb ./string0.kexe
(lldb) target create "string0.kexe"
Current executable set to 'string0.kexe' (x86_64).
(lldb) b string0.kt:1
Breakpoint 1: where = string0.kexe`kfun:main(kotlin.Array<kotlin.String>) + 4 at string0.kt:1, address = 0x0000000100001344
(lldb) r
Process 12288 launched: '/Users/jetbrains/kotlin/kotlin-native-release/kotlin-native/string0.kexe' (x86_64)
Process 12288 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x0000000100001344 string0.kexe`kfun:main(kotlin.Array<kotlin.String>) at string0.kt:1
-> 1       fun main(args: Array<String>) {
   2           val str = "hello"
   3           println(str.equals("HElLo", true))
   4           val strI18n = "Привет"
   5           println(strI18n.equals("прИВет", true))
   6           println(strI18n.toUpperCase())
   7           println(strI18n.toLowerCase())
(lldb) s
Process 12288 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = step in
    frame #0: 0x0000000100001354 string0.kexe`kfun:main(kotlin.Array<kotlin.String>) at string0.kt:3
   1       fun main(args: Array<String>) {
   2           val str = "hello"
-> 3           println(str.equals("HElLo", true))
   4           val strI18n = "Привет"
   5           println(strI18n.equals("прИВет", true))
   6           println(strI18n.toUpperCase())
   7           println(strI18n.toLowerCase())
```

{% raw %}
<p></p>
{% endraw %}

## 依赖库

非常值得一提的是，我们引入了一个新的依赖库格式：***.klib***，今后也将作为Kotlin/Native库的默认发行版本。本地库和框架可以轻松地使用 ***.klib*** 进行互操作，并通过指定 ***-library library*** 命令行参数或 ***library*** Gradle插件选项与Kotlin/Native编译器一起使用。Interop工具默认自动生成 ***.klib*** 格式文件。更多详细信息，请参阅[此处](https://github.com/JetBrains/kotlin-native/blob/master/LIBRARIES.md)。
## 下载

* [x86-64 Linux](http://download.jetbrains.8686c.com/kotlin/native/kotlin-native-linux-0.3.tar.gz)
* [x86-64 MacOS](http://download.jetbrains.8686c.com/kotlin/native/kotlin-native-macos-0.3.tar.gz)
* [x86-64 Windows](http://download.jetbrains.8686c.com/kotlin/native/kotlin-native-windows-0.3.zip)

欢迎使用[Kotlin错误跟踪器](https://youtrack.jetbrains.com/oauth?state=%2Fnewissue%3Fproject%3Dkotlin)提交错误和问题。
