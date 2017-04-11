---
title: [译]Kotlin M6 is here!
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

我们已经达到了我们的第六个里程碑，在商店方面，在语言改进和工具方面都有一些很棒的功能。
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

并且现在在任何SAM接口（即Callable（），Comparator（）等）上。 Runnable功能仍然适用于需要的情况。
### 注释改进

您现在可以使用枚举类型的参数，以及数组以及使用vararg传递可变数量的参数的可能性。

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class validate(val side: Side, vararg val props: String)
```

{% raw %}
<p></p>
{% endraw %}

哪里可以是一个枚举

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

我们以前在Kotlin中介绍了静态常量。使用此版本，您现在可以使用类对象，并将其属性表示为Java中的真静态字段，以确保100％的互操作性。
## Maven

对于那些使用Maven的人，您将很高兴知道Kotlin现在可以在Maven Central上使用。快照存储库也被移动到oss.sonatype.org。有关Maven支持的更多信息，请参阅有关Maven支持的文档。
## Android Studio支持

几个月后，您可能已经听到这个消息，Google一直在开发基于IntelliJ IDEA社区版的开发Android应用程序的Android开发IDE。有了这个里程碑，我们现在为这个IDE提供支持。现在，您还可以在Android Studio中为IntelliJ IDEA中的Kotlin提供所有功能。我们将进一步深入了解Android Studio的支持，包括如何设置Gradle与Kotlin合作，以及在单独的职位中设计项目。
## 新的重构

除了支持Android Studio，我们还在M6中提供了一些新的IDE重构。
### 内联变量

您可以使用简单的按键使内联变量。
### 拆分/连接属性声明

如你所知，Kotlin允许在声明上初始化属性。 IntelliJ IDEA现在允许我们使用Split属性声明意图轻松地将其重构为两个单独的表达式，或者在单个表达式中使用Edit | Join Lines将它们重新连接起来。
### 安全删除

您现在可以安全地删除项目中未引用的符号，包括检查注释和字符串中的引用
### 展开/删除表达式

与IDEA中其他语言的支持相同，您现在可以通过代码|展开/删除重构。
## 其他功能和改进

除了上述功能之外，这个版本还带来了一些其他的好东西

* 性能改进。我们一直在努力提高性能，包括更快完成和其他一般性能增强。需要更多的工作，但我们在正确的轨道上。
* TestNG。您现在可以右键单击一个类或函数，并使用TestNG运行测试（感谢Jayson Minard）。

立即下载并尝试，如果您有任何问题，请告诉我们。重要提示：如果您使用IntelliJ 13 EAP，请注意，您需要最新版本才能使用此版本。
