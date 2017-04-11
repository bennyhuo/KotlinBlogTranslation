---
title: [译]Kotlin M2 is Out!
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
---

一些新闻网站告诉你，科特林M2本周早些时候出来了。那么现在我们成真了
在M2候选人的帖子中，我向您介绍了JavaScript和Android支持以及新的语言功能。现在是更多更新，示例和计划的时候了。
继续进行Kotlin M2安装说明。
## 更多关于语言

上一篇文章概述了新的语言功能。这里还有一点：
首先，我想提醒一下，在M1中，我们添加了“assert not null”运算符：!!，它替代了在标准库中使用的sure（）函数。现在，我们从库中删除了sure（），所以有些代码可能会中断，但很容易解决。
人们不断询问Kotlin是否有列表或地图的字面值。答案是：严格来说，不，但是我们在图书馆里有这样的功能：

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
我不得不为文档中的所有内容道歉。一个好消息是，我们正在努力使我们的文档开源以及项目的其余部分。现在，您可以在我们的github回购中找到来源（在Confluence wiki格式中），从而为您的拉取请求提供更正/补充。
有关文档的更多消息：我们的KDoc工具快速成熟，感谢James Strachan。现在它支持搜索和链接到图书馆的github源。
## 例子

如上所述，这个里程碑中的大事情是IDE和Android中的JavaScript支持。从示例开始总是很好，所以这里有一组您可以在IDE中打开的项目。请在上一篇文章中找到一些说明。
JavaScript示例：

* 你好，世界！
* 生物（HTML5 Canvas）：看它运行
* Kotlin拼图：看它运行
* 交通信号灯：看到它正在运行
* 还要注意James Strachan的koolapp，值得一个单独的职位，我希望能在那里很快。现在，请参阅自述文件。

Android的示例：

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
要安装M2插件：如果您安装了M1，它将自动从插件库更新。它每天检查一次更新，所以如果你不想等待，手动启动检查：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Check-For-Updates.png"><img alt="" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/06/Check-For-Updates.png?resize=150%2C150&amp;ssl=1"/></a></p>
{% endraw %}

由于注释格式有所改变，系统将提示您更新Kotlin库。如果您错过“更新Kotlin运行时”气球，请在事件日志中打开消息：
请注意，在从主插件存储库安装M2之前，您必须卸载M2候选人和Kotlin插件的任何夜间版本或手动构建。
## 构建工具：Ant和Mave

我们的构建工具集成，包括Maven，已经改进了一点点更少的存储库，更容易的设置过程。您可能需要更新您的pom的。请参阅这里的说明。
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
