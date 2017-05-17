---
title: "Kotlin/Native v0.2 is out"
date: 2017-05-12 11:08:00
author: Nikolay Igotti
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
translator:
translator_url:
source_url: https://blog.jetbrains.com/kotlin/2017/05/kotlinnative-v0-2-is-out/
---

We’re happy to announce the release of Kotlin/Native v0.2, a feature and bugfix update to Kotlin/Native Technology Preview. This update adds support for coroutines and cross-module inline functions support, along with bugfixes and improvements all over the place.
This release includes samples showing how to use  [coroutines for concurrent non-blocking IO](https://github.com/JetBrains/kotlin-native/tree/master/samples/nonBlockingEchoServer) , a  [GUI application using GTK](https://github.com/JetBrains/kotlin-native/tree/master/samples/gtk) , as well as a  [TensorFlow machine learning framework](https://github.com/JetBrains/kotlin-native/tree/master/samples/tensorflow) client contributed by Julius Kunze.
For example, code as easy as

{% raw %}
<p></p>
{% endraw %}

```kotlin
var connectionId = 0
acceptClientsAndRun(listenFd) {
  memScoped {
    val bufferLength = 100L
    val buffer = allocArray<ByteVar>(bufferLength)
    val connectionIdString = "#${++connectionId}: ".cstr
    val connectionIdBytes = connectionIdString.getPointer(this)
    try {
      while (true) {
        val length = read(buffer, bufferLength)
        if (length == 0L) break
        write(connectionIdBytes, connectionIdString.size.toLong())
        write(buffer, length)
      }
    } catch (e: IOException) {
      println("I/O error occurred: ${e.message}")
    }
  }
}
```

{% raw %}
<p></p>
{% endraw %}

can be used to process multiple concurrent socket IO with coroutines and serve each client individually and concurrently.
And to create a GTK button with an event listener, just do:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val button = gtk_button_new_with_label("Click me!")!!
g_signal_connect(button, "clicked",
   staticCFunction { _: CPointer<GtkWidget>?, _: gpointer? -> println("Hi from Kotlin") }
)
```

{% raw %}
<p></p>
{% endraw %}

So v0.2 release allows  to create fully functional small-footprint native applications written in Kotlin.
Both compilation and runtime performance were significantly improved, size of redistributable decreased.
The complete list of changes in this release can be found in the  [changelog.](https://github.com/JetBrains/kotlin-native/blob/v0.2.0/CHANGELOG.md) 
Pre-built binaries for  [Linux](http://download.jetbrains.com/kotlin/native/kotlin-native-linux-0.2.tar.gz)  and  [MacOS](http://download.jetbrains.com/kotlin/native/kotlin-native-macos-0.2.tar.gz)  hosts are available.
