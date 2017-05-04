---
title: "[译]Multiple Inheritance Part 1: Problems with the existing design"
date: 2011-08-23 12:59:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-1-problems-with-the-existing-design/
translator:
translator_url:
---

我从假期回来，现在是在会议演示文稿和文档评论中收到的反馈中指出的最大问题之一。我在谈论继承。
我打算在这个主题上写一连串的帖子。这些帖子旨在引发讨论，以便我们可以从您的反馈中获益，并提出更好的设计。
这是系列中的第一篇文章，我讨论了我们的设计 [于2011年7月提交](http://confluence.jetbrains.net/download/attachments/40702623/JVMLS_workshop_2011.pdf?version=1&modificationDate=1311201781543) 。它具有以下继承方法：

* 没有接口，只有类;
* 每个类可以有多个超类;
* 如果一些非抽象成员（属性或方法）从两个超类型继承，则编译器要求用户覆盖它，并手动指定要运行的代码。

（有关更多详情，请参阅我们的 [维基](http://confluence.jetbrains.net/pages/viewpage.action?pageId=41484416) 截至2011年7月20日）
这是基本上是臭名昭着的**多重继承**的故事，我们记得从C ++时代来看，这是一个坏的。让我们看看更近
**这是关于初始化**
我们来看下面的例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
abstract class Base(x : Int) { ... }
 
open class Left(x : Int) : Base(x) { ... }
open class Right(x : Int) : Base(x) { ... }
 
class Child : Left(3), Right(4) { ... }
```

{% raw %}
<p></p>
{% endraw %}

所以，我们有一个 [钻石](http://en.wikipedia.org/wiki/Diamond_problem) ：底部位于顶部，左侧和右侧以及底部的“儿童”。有一件事看起来可疑：孩子初始化其超类通过不同的数字两个：3到左和从4到右。现在，他们反过来用这些数字初始化Base ...什么是基本初始化？

{% raw %}
<p><span id="more-74"></span></p>
{% endraw %}

实际上，创建了Base的两个“实例”：一个用3初始化，被隐藏在Left（3）内部，另一个用Right（4）内部的4进行初始化。即它像C ++中的非虚拟继承一样工作。 （在Java平台上，我们通过授权来实现，这对用户来说是不可见的）。
现在，当您调用在Base中定义的函数时会发生什么？例如，我们假设Base定义了两个抽象函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
abstract class Base(x : Int) {
  fun foo()
  fun bar()
}
```

{% raw %}
<p></p>
{% endraw %}

现在，让Left覆盖foo（）和Right override Bar：

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class Left(x : Int) : Base(x) {
  override fun foo() { print(x) }
}
open class Right(x : Int) : Base(x) {
  override fun bar() { print(x) }
}
```

{% raw %}
<p></p>
{% endraw %}

在这种情况下，孩子继承了foo（）和两个<em>声明</em> bar（）的两个<em>声明</em>，但同时它继承<em>只有一个实现</em>每个这些功能，所以它的确定，行为是确定的。所以，当我们说

{% raw %}
<p></p>
{% endraw %}

```kotlin
val c = Child(0)
c.foo()
c.bar()
```

{% raw %}
<p></p>
{% endraw %}

输出是

{% raw %}
<p></p>
{% endraw %}

```kotlin
3
4
```

{% raw %}
<p></p>
{% endraw %}

因为foo（）被调用为Left，而bar（）被调用为Right。
如果孩子继承了比例如foo（）的一个实现<em>，那么编译器会抱怨直到我们在Child中覆盖foo（），并明确指定行为。所以，当调用Child的功能时，我们保证没有歧义。
到目前为止，这么好，但是这种方法还有什么问题吗？
**问题1：**当我们创建一个Child的实例时，Base的构造函数被调用两次。这是坏的，因为如果它有副作用，它们是重复的，并且Child类的作者可能不知道它，因为有人更改继承图将其变成以前不存在的钻石。
<br/>
**问题2：** Left的实现假定它是用3初始化的，但它可能会调用在Right中实现的bar（），并假设所有内容都被初始化为4.这可能会导致一些不一致的行为。
**问题3：**由授权执行，深层层次将通过长期的代理链来降低性能。
**（Im）可能的修复方法**
现在，我们如何解决我们的设计？ C ++通过拥有**问题1**和**3** [虚拟继承](http://en.wikipedia.org/wiki/Virtual_inheritance) 。在Java平台上，考虑到单独的编译，当类<em>从两个来源继承状态</em>时，我不认为我们可以摆脱委托，所以**问题3**代表无论如何有两种继承的味道不是很好，正如我们从C ++中学到的...
虚拟继承不会修复**问题2**：初始化不同，部分继承的实现可能会对对象的整体状态产生不一致的假设。这个问题在一般情况下似乎是棘手的，但让我们准确，并确实是真的。
我们可以尝试保证一切都被一致地初始化。在一般情况下，当我们将任意表达式传递给Left和Right时，无法确定它们产生相同的结果，即使它们在文本上相同。那么我们可以在这里施加一些限制。例如：只允许将编译时常量或不可变变量传递给超类构造函数。在这种情况下，编译器可以检查整个类的层次结构，并确保每个基类都被一致地初始化。然而，有一个问题：如果一个超类更改了其初始化逻辑，子类可能会变得不一致，所以这将是一个很大的进化问题，例如对于库。
当然，对所有类施加这些限制也是太限制了。所以我们最终得到两种口味的课程
那么似乎“只有类（即没有接口或类似的）”方法没有奏效。现在是考虑其他方法的时候了。
**什么是**
不同的语言不同地管理多个继承，我总结了这里的一些方法。

* Java和C＃具有类和接口，即多接口继承和单实现继承;
* Scala具有可以实现方法甚至具有状态的类和特征，但是它们的构造函数不能有参数;
* 一些其他语言，如堡垒，不允许国家的特征;
* <您最喜欢的语言>

在里面 [下一篇文章](http://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-2-possible-directions/) 在本系列中，我们将详细讨论选项。
现在是你的评论的时候了他们非常的欢迎。
