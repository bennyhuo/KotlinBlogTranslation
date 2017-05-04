---
title: "[译]Kotlin M5.2: IntelliJ IDEA 12.1 and Gradle"
date: 2013-04-04 15:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/04/kotlin-m5-2-intellij-idea-12-1-and-gradle/
translator:
translator_url:
---

另一个更新 [Kotlin](http://kotlin.jetbrains.org/) 今天出来欢迎Kotlin M5.2。 <span id =“more-1038”> </span>
## 支持新的IntelliJ IDEA

Koltin M5.2支持（实际上需要）最近发布 [IntelliJ IDEA 12.1](http://www.jetbrains.com/idea/download/index.html) 。
Kotlin IDE的改进包括：

* 类层次结构视图中的Kotlin类。只需按一下类别名称上的Ctrl + H来查看其后代和/或父母。
* 折叠进口（您不必滚动导入，以获得您的代码）。
* Kotlin库配置的新UI：您现在可以控制库名称和位置，默认情况下，kotlin-runtime.jar不会复制到您的项目中。它只是工作。
* 支持针对JavaScript的模块得到显着改善。
* 实时优化导入：IDE设置 - >编辑器 - >自动导入 - >即时优化导入。
* 新的快速修复：将光标放在错误上，然后按Alt + Enter。


{% raw %}
<p><a name="SAM-constructors"></a></p>
{% endraw %}

## SAM构造函数

当使用Java库时，现在可以通过调用它来创建SAM接口（一个具有**S** ingle **A** bstract **M**方法）的实例命名并传递函数文字。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater(Runnable { doItNow() })
```

{% raw %}
<p></p>
{% endraw %}

**这仅适用于Java类**。事实上，它不是语言的一部分，而是Java类被加载到Kotlin的一个特征：我们定义一个*合成的*函数

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Runnable(body: () -> Unit) = object : Runnable {
    override fun run() {
        body()
    }
<span style="color: #222222;font-family: 'Courier 10 Pitch', Courier, monospace;line-height: 21px">}</span>
```

{% raw %}
<p></p>
{% endraw %}

所以每当你导入Runnable，这个功能就在那里，你可以使用它。
这是Java转换支持Java的第一个块。真正的SAM转换即将到来，您可以简单的说

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater { doItNow(); }
```

{% raw %}
<p></p>
{% endraw %}

## 新毕业插件

从M5.2开始，除了长时间使用的Maven插件，JetBrains还有一个用于Kotlin的Gradle插件。
以下是使用Gradle构建Kotlin模块的示例：

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
  repositories {
    mavenCentral()
    maven {
      url 'http://repository.jetbrains.com/all'
    }
  }
  dependencies {
    classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:0.1-SNAPSHOT'
  }
}
 
apply plugin: "kotlin"
 
repositories {
  mavenCentral()
  maven {
    url 'http://repository.jetbrains.com/all'
  }
}
 
dependencies {
  compile 'org.jetbrains.kotlin:kotlin-stdlib:0.1-SNAPSHOT'
}
```

{% raw %}
<p></p>
{% endraw %}

可以找到更多的例子和文档 [这里](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Gradle) 。
## 提醒：KAnnotator

别忘了你现在有了 [KAnnotator](http://blog.jetbrains.com/kotlin/2013/03/kannotator-0-1-is-out/) 乐意效劳。
**拥有不错的Kotlin！**
