---
title: "[译]Upcoming Change: “Class Objects” Rethought"
date: 2015-03-11 16:11:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/upcoming-change-class-objects-rethought/
translator:
translator_url:
---

**Kotlin M11**即将到来，和您中的一些人一样 [表示担忧](https://devnet.jetbrains.com/thread/461012?tstart=0) 关于即将发生的变化，我将介绍M11的一个功能，并要求您提供一些**反馈**。 <span id =“more-1817”> </span>
## 类对象：一个简短的提醒

众所周知，任何Kotlin类都可以有一个关联的 [类对象](http://kotlinlang.org/docs/reference/classes.html#class-objects) ：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    class object {
        fun classObjectMember() {}
    }
 
    fun classMember() {}
}
```

{% raw %}
<p></p>
{% endraw %}

一个*类对象*的成员大概类似于Java / C＃类的*静态成员*，因为它们可以在类名上被调用：

{% raw %}
<p></p>
{% endraw %}

```kotlin
KotlinClass.classObjectMember()
```

{% raw %}
<p></p>
{% endraw %}

（您可以使用`[platformStatic]`注释来使这些成员实际上从Java中看到`static`。）
事实上，Kotlin的*类对象*和Java的静态不一样，因为*类对象是**对象***，即它们可以扩展类，实现traits并在运行时作为*值*：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = KotlinClass // reference to class object of KotlinClass is assigned to x
```

{% raw %}
<p></p>
{% endraw %}

## 术语改变

正如你可能已经注意到的那样，术语“类对象”在英文中听起来有些模糊，这就是为什么很多人倾向于认为`Foo`的类对象必须是一个实例（换句话说，对象）的`Foo`，完全不是这样。这也是为什么我们正在寻找另一个术语和语法。目前的建议如下：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    default object {
        fun defaultObjectMember() {}
    }
 
    fun classMember() {}
}
```

{% raw %}
<p></p>
{% endraw %}

所以，以前被称为“类对象”现在称为“默认对象”。
更多的动力来自于下面，但在这一点上，请注意你对这个变化的感受：现在更好吗？更混乱大概和以前一样？
**请在阅读动机之前，在下面的评论中分享您的意见。非常感谢！**

{% raw %}
<p><a name="why-default-objects"></a></p>
{% endraw %}

## 为什么选择默认对象

**注意**：此处提供的所有语法均为**临时**（我们已实施，但可能会决定在M11之前更改）。
不幸的措辞不是这个变化的唯一原因。事实上，我们重新设计了这个概念，使其与普通物体更为统一。
请注意，类可以（并且总是可以）嵌套到它中的许多对象（通常的，命名的单例）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    object Obj2 { ... }
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

现在，这些对象之一可以使用`默认`修饰符声明，这意味着可以通过类名直接访问其成员，即默认情况下**：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    default object Obj2 { ... }
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

访问`Obj1`的成员需要资格：`KotlinClass.Obj1.foo（）`，对于`Obj2`的成员，对象名称是可选的：`KotlinClass .foo（）`
最后一步：可以省略*默认对象*的名称（在这种情况下，编译器将使用默认名称`Default`）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    default object { ... }
    ...
}
```

{% raw %}
<p></p>
{% endraw %}

现在，您仍然可以通过包含类的名称来引用其成员：`KotlinClass.foo（）`，或通过完整的资格：`KotlinClass.Default.foo（）`。
正如你所看到的，与我们以前使用的*类对象*不同，默认对象*与普通对象完全一致。
另一个重要的好处是，现在每个对象*都有一个名字*（当省略缺省对象*的名称时，再次使用`Default`），为默认对象启用**书写扩展功能**：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun KotlinClass.Default.bar() { ... }
```

{% raw %}
<p></p>
{% endraw %}

这可以称为`KotlinClass.bar（）`。这就是我们为内置类（如`Int`）实现特定于平台的扩展。 `Int.MAX_VALUE`是仅在JVM上定义的`Int.Default`的扩展（JS ony具有浮点数，因此`Int.MAX_VALUE`是没有意义）。
## 概要


* 我们正在改变以前称为“类对象”的语法和概念负载：它们现在是默认对象。

旧的语法将被废弃，并保持一段时间，以便您可以迁移您的代码（IDE将在其中为您提供帮助）。
* 旧的语法将被废弃，并保持一段时间，以便您可以迁移您的代码（IDE将在其中为您提供帮助）。
* 新概念与普通命名对象是一致的。
* 您现在可以将扩展名写入可以在类名上调用的默认对象。

**您的反馈非常受欢迎！**这个变化的很大一部分是关于术语和措词，所以如果你认为新的概念是混乱的话，请在评论中告诉我们。
