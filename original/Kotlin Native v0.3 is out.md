---
title: Kotlin/Native v0.3 is out
author: Nikolay Igotti
date: 2017-06-22 20:41:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlinnative-v0-3-is-out/
tags: 
categories:  官方动态
---

We’re happy to announce the release of Kotlin/Native v0.3. We are going to the new lands! With the release of version v0.3 Windows is supported as both a compilation host and execution target, and Google Android devices as an execution target with native activities. So Windows API ‘Hello World’ may look as easy as:

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

Android native activity’s event processing:

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

## Debugging

With this release we support source level debugging (single-stepping only). For example, try

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

## Libraries

Last, but surely, not the least, we introduced a new library format, called .klib, which is intended to be the default distribution format for Kotlin/Native libraries. Native libraries and frameworks could be easily interoperated with using .klib and used with Kotlin/Native compiler by just specifying -library library command line flag or library Gradle plugin option. Interop tool already produces .klib format files by default. For more details on library format see here.
## Getting the bits

Binaries could be downloaded below:

* x86-64 Linux
* x86-64 MacOS
* x86-64 Windows

Bugs and issues could be reported using Kotlin bug tracker.
