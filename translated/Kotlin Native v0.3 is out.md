---
title: Kotlin/Native v0.3 is out
author: Nikolay Igotti
date: 2017-06-22 20:41:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlinnative-v0-3-is-out/
tags: 
categories:  官方动态
---

我们很高兴地宣布发布Kotlin / Native v0.3。我们要去新的土地！随着版本v0.3的发布，Windows作为编译主机和执行目标以及Google Android设备作为本机活动的执行目标都被支持。所以Windows API“埃洛世界”可能看起来很容易：

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

Android本土活动鈥事件处理：

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

有了这个版本，我们支持源级调试（仅限单步）。例如，尝试

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

## 图书馆

最后，但肯定不是最不重要的，我们引入了一个新的库格式，称为.klib，它将作为Kotlin / Native库的默认分发格式。本地库和框架可以轻松地与.klib进行互操作，并通过指定-library库命令行标志或库Gradle插件选项与Kotlin / Native编译器一起使用。默认情况下，Interop工具已经生成.klib格式文件。有关库格式的更多详细信息，请参阅此处。
## 得到一点

二进制文件可以在下面下载：

* x86-64 Linux
* x86-64 MacOS
* x86-64 Windows

可以使用Kotlin错误跟踪器报告错误和问题。
