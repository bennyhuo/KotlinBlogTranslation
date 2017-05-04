---
title: "[译]Anko 0.6 is Released"
date: 2015-04-30 12:31:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/anko-0-6-is-released/
translator:
translator_url:
---

今天我们很高兴地介绍新版本 [安科](https://github.com/JetBrains/anko) - 促进Android应用程序开发的库。我们很高兴收到了很多反馈，以及一些变化 [0.6](https://github.com/JetBrains/anko/releases/tag/v0.6) 实际上是由社区提出的
<span id =“more-2124”> </span>
## 警告：软件包名称已更改

那我们很抱歉由于历史原因，Anko软件包的名称曾经是`kotlinx.android.anko`，我们将它改为0.6中的`org.jetbrains.anko`，以与Maven工件一致名称。
## 新听众

Anko 0.5引入了部分定义的减少代码冗长度的监听器：当我们只需要定义一个多方法监听器的一个方法时，我们就不用实现我们不在乎的方法。根据您的反馈（谢谢， [SalomonBrys](https://github.com/SalomonBrys) ！）此功能已重新设计为0.6：

* 局部定义的听众现在可以在DSL布局外面使用;
* 语法更易于理解;
* “引擎盖”下的逻辑更简单。

这就是现在的样子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
editText {
    textChangedListener {
        onTextChanged { text, start, before, count ->
            toast("New text: $text")
        }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 配置限定符 [限定词](http://developer.android.com/guide/topics/resources/providing-resources.html#AlternativeResources) 用于支持不同设备，区域设置等的不同布局。
Anko的DSL现在支持`configuration（）`函数，该函数指定布局的限定符：

{% raw %}
<p></p>
{% endraw %}

```kotlin
configuration(screenSize = ScreenSize.LARGE, orientation = Orientation.LANDSCAPE) {
    /*
      This code will be only executed
      if the screen is large and its orientation is landscape
    */
}
 
```

{% raw %}
<p></p>
{% endraw %}

此代码相当于将您的XML布局放在`layout-large-land`目录下。在技​​术上，它通过检查指定的限定符并且仅在`configuration（）`中执行代码（如果它们的值匹配）来实现。因此，`configuration（）`的用法不仅限于DSL：例如，您可以安全地使用`配置调用在旧版本的系统中不存在的Android SDK功能（fromSdk =版本＆gt;）{/ * code * /}`。
支持的限定符的完整列表可用 [这里](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#configuration-qualifiers) 。
## 自定义视图创建

将您自己的自定义视图合并到DSL中的最简单的方法是创建自己的视图 [构建器类功能](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#extending-anko) ，但由于它是耗时的，Anko现在支持更快的方式：

{% raw %}
<p></p>
{% endraw %}

```kotlin
frameLayout {
    customView<CustomView> {
        backgroundResource = R.drawable.custom_view_bg
    }.linearLayout(width = matchParent)
}
 
```

{% raw %}
<p></p>
{% endraw %}

它通过Java Reflection实现。虽然它比普通的DSL功能更慢，但是当您进行原型制作时，会更容易。
## appcompat.v7视图和属性

我们已经做出了初步的步骤，以支持`appcompat.v7` Android库。扩展功能为支持包中的`View`类和其属性的扩展属性添加到Anko。 [小部件着色](http://android-developers.blogspot.ru/2014/10/appcompat-v21-material-design-for-pre.html) 不支持，我们希望能在以后的版本中实现。
## 移除简单视图的顶级DSL功能

由于不太可能有简单的非容器视图（如TextView）作为活动的内容视图，因此我们删除了`Activity`和`Fragment`的这些视图的DSL功能，代码>接收器。在不太可能的情况下需要顶级的这种观点，使用`UI（）`包装函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
UI {
    textView(R.string.name)
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 您的反馈是欢迎

安科是根据Apache许可证2.0授权的，该项目是 [在Github上可用](https://github.com/JetBrains/anko) 。<BR/>
欢迎您的反馈和拉动请求！
