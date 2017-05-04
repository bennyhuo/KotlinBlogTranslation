---
title: "[译]Kotlin M2 is Out!"
date: 2012-06-11 09:55:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-is-out/
translator:
translator_url:
---

一些新闻网站告诉你 [Kotlin](http://kotlin.jetbrains.org) M2本周早些时候出来。那么现在我们让它成真了<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com /kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em“
在里面 [M2候选人](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/) 我告诉过你 [JavaScript](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#js) 和 [Android](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#android) 支持，以及新的 [语言特点](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#language) 。现在是更多更新，示例和计划的时候了。
继续 [Kotlin M2安装说明](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-is-out/#install) 。
## 更多关于语言

上一篇文章概述了新的 [语言特点](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/#language) 。这里还有一点：<span id =“more-570”> </span>
首先，我想提醒你，在M1我们加了 [“assert not null”运算符：!!](http://confluence.jetbrains.net/display/Kotlin/Null-safety#Null-safety-The%7B%7B%5C%21%5C%21%7D%7Doperator) ，它取代了我们在标准库中使用的sure（）函数。现在，我们从库中删除了sure（），所以有些代码可能会中断，但很容易解决。
人们不断询问Kotlin是否有列表或地图的**文字**。答案是：严格来说，不，但我们有功能 [图书馆](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/kotlin/package-summary.html) 这对于那个还不错：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val list = arrayList(1, 2, 3)
val map = hashMap(
    "John" to "Doe",
    "Jane" to "Smith"
)
```

{% raw %}
<p></p>
{% endraw %}

注意to（）也是一个函数。
另请注意，现在，您可以在被调用者的位置使用具有名为invoke（）的函数的任何类型：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(x : Method) {
    x(bar)
}
```

{% raw %}
<p></p>
{% endraw %}

您只能在此角色中使用此角色中的函数类型，现在可以通过提供一个invoke（）扩展名或成员将任何对象转换为“function”。
我不得不为在场的所有人道歉 [文件](http://kotlin.jetbrains.org) 然而。一个好消息是，我们正在努力使我们的文档开源以及项目的其余部分。现在，您可以在我们的github中找到源（Confluence wiki格式） [回购](https://github.com/JetBrains/kotlin/tree/master/docs/confluence.jetbrains.com/Kotlin) ，从而为您的拉取请求提供更正/补充。
有关文档的更多消息：我们的KDoc工具快速成熟，感谢 [詹姆斯·斯特拉坎](https://github.com/jstrachan) 。现在它支持搜索和链接到github源 [图书馆](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html) 。
## 例子

如上所述，这个里程碑中的大事情是IDE和Android中的JavaScript支持。从示例开始总是很好，所以这里有一组您可以在IDE中打开的项目。请，找到一些说明 [上一篇文章](http://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/) 。
**JavaScript**的示例：

* 你好，世界！
* 生物（HTML5 Canvas）：看它运行
* Kotlin拼图：看它运行
* 交通信号灯：看到它正在运行
* 还要注意James Strachan的koolapp，值得一个单独的职位，我希望能在那里很快。现在，请参阅自述文件。

**Android**的示例：

* 你好，世界！
* 标签蛇和维基重写的例子可以在这里找到Kotlin。
* Vlad Likhonos的一组有用的工具：kotlinAndroidLib

玩这些例子玩得开心，贡献更多！
## IntelliJ IDEA插件

IntelliJ IDEA插件进度非常快。大部分工作都是在幕后完成的（性能更好，与Java IDE集成更紧密），但还有一些用户面临的问题也要指出：

* IDE现在显示以类似HTML的方式格式化的错误消息，这使得消息更易读。
* 当您需要在声明中添加类型时，请享受“指定显式类型”重构。
* 现在支持跨语言查找Kotlin和Java代码之间的用法和重命名。
* 支持导航到继承者。这也适用于各种语言：Kotlin内部，用于扩展Java类的Kotlin类，反之亦然。
* 此外，我们更改了IDE图标，现在他们非常好。更多关于这个话题的工作。

我们在下一个里程碑上的优先事项是IDE性能和改进对Java类的零安全支持。
**<a name="install">安装M2插件</a>**：如果您安装了M1，则会自动从 [插件库](http://plugins.intellij.net/plugin/?idea&pluginId=6954) 。它每天检查一次更新，所以如果你不想等待，手动启动检查：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Check-For-Updates.png"><img alt="" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Check-For-Updates.png?resize=150%2C150&amp;ssl=1"/></a></p>
{% endraw %}

由于注释格式有所改变，系统将提示您更新Kotlin库。如果您错过了“更新Kotlin Runtime”气球，请在事件日志中打开消息：<br/>
<img alt =“”data-recalc-dims =“1”src =“https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Outdated-Kotlin-Runtime.png？ resize = 150％2C129＆amp; ssl = 1“/> <img alt =”“data-recalc-dims =”1“src =”https://i0.wp.com/blog.jetbrains.com/kotlin/files/ 2012/06 / Update-Runtime.png？resize = 150％2C150＆amp; ssl = 1“/>
**注意**，您必须卸载M2候选人和任何夜间构建的Kotlin插件或手动构建之前 [安装](http://www.jetbrains.com/idea/plugins/index.html) M2主要 [插件库](http://plugins.intellij.net/plugin/?idea&pluginId=6954) 。
## 构建工具：Ant和Maven

我们的 [构建工具集成](http://confluence.jetbrains.net/display/Kotlin/Kotlin+Build+Tools) ，包括Maven，改进了一点点的存储库，更容易的设置过程。您可能需要更新您的pom的。参见说明 [这里](http://confluence.jetbrains.net/display/Kotlin/Kotlin+Build+Tools) 。
## 计划

再多一点我们打算下一步做什么。如上所述，IDE的优先级是性能和Java集成wrt零安全性。语言工作将带来以下改进：

* Kotlin将提供定义属性转换为Java静态最终常量的方法。
* 我们将支持数据类的概念，这与Scala的案例类有些相似。
* Kotlin将支持一种动态类型，这主要是为了适应不符合静态类型方法的JavaScript API。
* 我们还将极大地改进类型推理算法。现在我们欠你这么长时间了

图书馆的计划如下：

* 将大多数Kotlin的标准库端口连接到JS平台。
* 使Kotlin的集合变体，但保留与java.util。*集合的无缝互操作。这实际上值得一个单独的职位。
* 为Android提供良好的图书馆支持。我们怀疑Android的大部分XML文件都可以被Kotlin的建设者所替代，而这些构建者在很多方面都是更好的...

## 有一个漂亮的Kotlin！

不要忘了给我们反馈。谢谢。
