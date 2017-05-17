---
title: "[译]Kotlin/Native v0.2 is out"
date: 2017-05-12 11:08:00
author: Nikolay Igotti
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
translator: bennyhuo
translator_url: https://www.kotliner.cn
source_url: https://blog.jetbrains.com/kotlin/2017/05/kotlinnative-v0-2-is-out/
---

我们很高兴地宣布Kotlin / Native v0.2 发布啦，这是 Kotlin / Native 技术预览版的一次功能更新和 Bug 修复。这次更新增加了对协程和跨模块内联函数的支持，以及整体上的问题修复和优化。
这次更新包括了一个演示如何使用 [并发非阻塞IO协同程序](https://github.com/JetBrains/kotlin-native/tree/master/samples/nonBlockingEchoServer) 的示例， 一个 [使用GTK的GUI应用程序](https://github.com/JetBrains/kotlin-native/tree/master/samples/gtk) ，以及一个由Julius Kunze贡献的[TensorFlow机器学习框架](https://github.com/JetBrains/kotlin-native/tree/master/samples/tensorflow) 客户端。

诸如下面的代码：

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

可用于使用协程处理并发 Socket IO，各个用户的请求将得到并发处理。

下面的这段代码则演示了如何创建一个带有事件监听的GTK按钮：

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

简单地说，Kotlin Native v0.2 能够支持我们编写一些功能完善而精巧的程序了。

另外，Kotlin Native 编译和运行时性能均有明显改善，编译生成的可执行程序体积也进一步得到了缩减。

完整更新内容请参考 [更新日志。](https://github.com/JetBrains/kotlin-native/blob/v0.2.0/CHANGELOG.md)
 
 点击后面的链接即可下载 [Linux](http://download.jetbrains.com/kotlin/native/kotlin-native-linux-0.2.tar.gz)  和 [MacOS](http://download.jetbrains.com/kotlin/native/kotlin-native-macos-0.2.tar.gz) 版本的编译器。
