---
title: "[译]Kotlin M6 is here!"
date: 2013-08-12 21:09:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/08/kotlin-m6-is-here/
---

我们已经达到了我们的第六个里程碑，在商店方面，在语言改进和工具方面都有一些很好的功能。<span id =“more-1155”> </ span>
## 语言改进


{% raw %}
<p><a name="SAM-conversions"></a></p>
{% endraw %}

### SAM转换

我们已经完成了在M5.2中使用单抽象方法调用Java接口的初始支持。你现在可以简单地做

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater { doItNow() }
```

{% raw %}
<p></p>
{% endraw %}

并且现在在任何SAM接口（即Callable（），Comparator（）等）上。 <em> Runnable </ em>功能仍然适用于需要的情况。
### 注释改进

您现在可以使用<em>枚举</ em>类型的注释，以及使用<em> vararg </ em>传递可变数量的参数的数组。

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class validate(val side: Side, vararg val props: String)
```

{% raw %}
<p></p>
{% endraw %}

其中<em>侧面</ em>可以是枚举

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Side {
   Client
   Server
   Both
}
```

{% raw %}
<p></p>
{% endraw %}

### 静态字段

我们覆盖 [Kotlin中的静态常数](http://blog.jetbrains.com/kotlin/2013/06/static-constants-in-kotlin/)  先前。使用此版本，您现在可以使用类对象，并将其属性表示为Java中的真静态字段，以确保100％的互操作性。
## Maven

对于那些使用Maven的人，您将很高兴知道Kotlin现在可以使用 [Maven Central](http://www.maven.org) 。快照存储库也被移动到oss.sonatype.org。有关Maven支持的更多信息，请参阅文档 [Maven支持](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Maven) 。
## Android Studio支持

几个月后，您可能已经听到这个消息，Google一直在研究一个新的开发IDE [Android Studio](http://developer.android.com/sdk/installing/studio.html)  用于开发基于IntelliJ IDEA社区版的Android应用程序。有了这个里程碑，我们现在为这个IDE提供支持。现在，您还可以在Android Studio中为IntelliJ IDEA中的Kotlin提供所有功能。 <img alt =“Android Studio”border =“0”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image .png？resize = 640％2C477＆amp; ssl = 1“style =”padding-top：0px; padding-left：0px; padding-right：0px; border-width：0px“/>深入了解Android Studio支持，包括如何将Gradle设置为与Kotlin合作，以及在单独的文章中布置该项目。
## 新的重构

除了支持Android Studio，我们还在M6中提供了一些新的IDE重构。
### 内联变量

您可以使用简单的按键使内联变量。 <img alt =“image”border =“0”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image1。 png？resize = 381％2C162＆amp; ssl = 1“style =”padding-top：0px; padding-left：0px; padding-right：0px; border-width：0px“
### 拆分/连接属性声明

如你所知，Kotlin允许在声明上初始化属性。 IntelliJ IDEA现在允许我们使用<em> Split属性声明意图</ em>轻松地将其重构为两个单独的表达式，或者使用<em> Edit | Join Lines </ em>重新连接。 <img alt =“image”border =“0”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image2。 png？resize = 247％2C68＆amp; ssl = 1“style =”padding-top：0px; padding-left：0px; padding-right：0px; border-width：0px“
### 安全删除

您现在可以安全地删除项目中未引用的符号，包括检查注释和字符串中的引用<img alt =“image”border =“0”data-recalc-dims =“1”src =“https：// i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image3.png?resize=189%2C164&amp;ssl=1“style =”padding-top：0px; padding-left：0px; padding -  right：0px; border-width：0px“/>
### 展开/删除表达式

与IDEA中其他语言的支持相同，您现在可以通过<strong>代码|展开/移除</ strong>重构。 <img alt =“image”border =“0”data-recalc-dims =“1”src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image4。 png？resize = 384％2C123＆amp; ssl = 1“style =”padding-top：0px; padding-left：0px; padding-right：0px; border-width：0px“
## 其他功能和改进

除了上述功能之外，这个版本还带来了一些其他的好东西

* 性能改进。我们一直在努力提高性能，包括更快完成和其他一般性能增强。需要更多的工作，但我们在正确的轨道上。
* TestNG。您现在可以右键单击一个类或函数，并使用TestNG运行测试（感谢Jayson Minard）。

<span> <a href="http://plugins.jetbrains.com/plugin?pr=idea&amp;pluginId=6954">立即下载</a> </ span>，并尝试 [如果您有任何问题，请告诉我们](http://youtrack.jetbrains.com/issues/kotlin) 。重要提示：如果您正在使用 [IntelliJ 13 EAP](http://eap.jetbrains.com/idea) 请注意，您需要最新版本才能使用此版本。
