---
title: [译]Upcoming Change: “Class Objects” Rethought
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
---

Kotlin M11即将到来，由于有些人对即将发生的变更通知表示担忧，我将介绍M11的功能之一，并要求您提供一些反馈。
## 类对象：一个简短的提醒

众所周知，任何Kotlin类都可以有一个关联的类对象：

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

类对象的成员大致类似于Java / C＃类的静态成员，因为它们可以在类名上被调用：

{% raw %}
<p></p>
{% endraw %}

```kotlin
KotlinClass.classObjectMember()
 
```

{% raw %}
<p></p>
{% endraw %}

（甚至可以使用[platformStatic]注释来使这些成员实际上是静态的。
事实上，Kotlin的类对象和Java的静态不是一样的，因为类对象是对象，即它们可以扩展类，实现traits，并在运行时用作值：

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

正如你可能已经注意到的那样，术语“类对象”在英语中听起来有点模糊，这就是为什么许多人倾向于认为Foo的类对象必须是Foo的一个实例（换句话说，对象），这完全是不是这样这也是为什么我们正在寻找另一个术语和语法。目前的建议如下：

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
更多的动力来自于下面，但在这一点上，请注意你对这个变化的感受：现在更好吗？更混乱和以前一样吗？
在阅读动机之前，请在下面的评论中分享您的意见。非常感谢！

{% raw %}
<p><a name="why-default-objects"></a></p>
{% endraw %}

## 为什么选择默认对象

注意：这里提供的所有语法都是临时的（我们已经实现了，但可能会决定在M11之前更改它）。
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

现在，这些对象之一可以使用默认修饰符声明，这意味着它的成员可以通过类名直接访问，即默认情况下：

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

访问Obj1的成员需要资格：KotlinClass.Obj1.foo（），对于Obj2的成员，对象名称是可选的：KotlinClass.foo（）。
最后一步：可以省略默认对象的名称（在这种情况下，编译器将使用默认名称Default）：

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

现在，您仍然可以通过包含类的名称来引用其成员：KotlinClass.foo（），或通过完整的资格：KotlinClass.Default.foo（）。
可以看到，与类对象不同，默认对象与普通对象完全一致。
另一个重要的好处是，现在每个对象都有一个名称（同样，当省略默认对象的名称时，使用默认值），这样可以为默认对象写入扩展功能：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun KotlinClass.Default.bar() { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

这可以称为KotlinClass.bar（）。这就是我们如何为Int内置的类实现平台特定的扩展：例如Int.MAX_VALUE是仅在JVM上定义的Int.Default的扩展（JS ony具有浮点数，因此Int.MAX_VALUE无意义）。
## 概要


* 我们正在改变以前称为“类对象”的语法和概念负载：它们现在是默认对象。

旧的语法将被废弃，并保持一段时间，以便您可以迁移您的代码（IDE将在其中为您提供帮助）。
* 旧的语法将被废弃，并保持一段时间，以便您可以迁移您的代码（IDE将在其中为您提供帮助）。
* 新概念与普通命名对象是一致的。
* 您现在可以将扩展名写入可以在类名上调用的默认对象。

您的反馈非常受欢迎！这个变化的很大一部分是关于术语和措词，所以如果你认为这个新概念是混乱的话，请在评论中告诉我们。
