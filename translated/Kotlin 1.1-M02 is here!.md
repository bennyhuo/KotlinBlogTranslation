---
title: [译]Kotlin 1.1-M02 is here!
date: 2016-10-20 14:04:00
author: Denis Zharkov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/10/kotlin-1-1-m02-is-here/
---

我们很高兴地宣布Kotlin 1.1的第二个里程碑版本。此版本带来了一个期待已久的新语言功能，在lambdas中进行解构，以及对1.1-M1中引入的功能的许多改进，包括类型别名，协程和绑定引用。新版本还包括Kotlin 1.0.4和1.0.5-eap-66中引入的所有工具功能，并且与IntelliJ IDEA 2016.3 EAP和Android Studio 2.2完全兼容。
与Kotlin 1.1-M01一样，我们对新的语言和库功能不提供向后兼容性保证。在1.1版本的里程碑版本中引入的任何内容都将在最终1.1版本之前发生变更。
再次：请通过YouTrack，论坛和Slack，分享您关于新语言功能或您可能遇到的任何问题的反馈。
1.1-M02的完整更新日期在这里。

{% raw %}
<p><span id="more-4312"></span></p>
{% endraw %}

## 兰布达的破坏

Kotlin 1.0支持破解声明 - 这个功能允许您“解包”复合值（如数据类），并将其组件分配给多个不同的变量。 Kotlin 1.1将其扩展为lambda参数，让您解压缩传递给lambda的复合变量，并以不同的名称访问其组件。例如，您可以使用它来遍历对列表：

{% raw %}
<p></p>
{% endraw %}

```kotlin
listOfPairs.map {
    (a, b) -> a + b
}
 
```

{% raw %}
<p></p>
{% endraw %}

你可以在KEEP中找到更多的细节。请注意，该功能目前仅支持JVM后端。嵌套解析以及传递给常规函数和构造函数的参数的解构目前不受支持。
## 标准库

Kotlin 1.1-M02为标准库添加了几个新的API：

* 不同的AbstractCollection和AbstractMutableCollection层次结构用作实现新Kotlin集合类（KEEP-53）的基类;
* 用于复制地图的Map.toMap（）和Map.toMutableMap（）扩展功能（KEEP-13）

## 反射

反思图书馆已经获得了大量新功能。您现在可以从KType实例获取更多有用的信息，并创建自定义KType实例，声明上的内省修饰符，获取超类或检查子类型等。要查看新功能，可以扫描以下提交。
## IDE

IntelliJ IDEA插件已经扩展到支持新的1.1语言功能，新的重构“引入类型别名”和“内联类型别名”，一种意图操作，用于从使用中创建一个类型别名，以及在lambdas中应用解构的quickfix自动。
## 脚本

从这个版本开始，Kotlin支持JSR-223（javax.script API），允许您从应用程序轻松运行Kotlin脚本，并使用Kotlin作为嵌入式脚本语言。它还继续支持在Gradle构建文件中支持Kotlin脚本的工作。
## JavaScript

1.1-M02中的JavaScript支持已经扩展到支持类别别名和类文字（Foo :: class）。
除此之外，我们正在努力在多平台项目中提供更多的Kotlin API。为此，我们已经定义了kotlin包中的所有标准异常类。当定位到JVM时，Kotlin异常被定义为相应Java异常的类型别名，JS后端提供了其完整的实现。我们还为标准集合类提供了一个完整的Kotlin实现，现在用于JS项目。 （Kotlin在JVM上仍然使用标准的Java集合类。）
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.1作为构建脚本和项目的存储库;使用1.1-M02作为编译器和标准库的版本号。
在IntelliJ IDEA：转到工具→Kotlin→配置Kotlin插件更新，然后在更新频道下拉列表中选择“早期访问预览1.1”，然后按检查更新。
在try.kotlinlang.org。使用右下角的下拉列表将编译器版本更改为1.1-M02。
用SDKMan运行sdk安装kotlin 1.1-M02。
如果您正在使用kotlinx.coroutines库，请使用更新版本的0.1-alpha-2，它几乎是一样的，但是它与1.1-M02编译器重新编译。您可以按照自述文件中的更新。
有一个漂亮的Kotlin！
