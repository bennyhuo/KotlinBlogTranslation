---
title: "[译]Kotlin M5.3: IntelliJ IDEA 13, Delegated Properties and more"
date: 2013-06-06 10:48:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/06/kotlin-m5-3-idea-13-delegated-properties-and-more/
---

Kotlin M5.3支持IntelliJ IDEA 13和一些新功能，供您查看。我们正在向强大的运行时支持，包括反射和其他框架启用功能。这个里程碑标志着我们朝这个方向迈出的第一步。 <span id =“more-1060”> </ span>
## IntelliJ IDEA 12.1和13

首次早期访问版本 [IntelliJ IDEA 13](http://blogs.jetbrains.com/idea/2013/05/intellij-idea-13-early-preview-is-out/) 正在出来，我们发行与这些版本兼容的Kotlin插件。记住这是一个EAP，使用它自己承担风险。当然好老了 [IntelliJ IDEA 12.1](http://www.jetbrains.com/idea/download/) 也被支持。
<strong>注意</ strong>：有关Kotlin支持的一些消息 [Android Studio](http://developer.android.com/sdk/installing/studio.html) 即将到来
## 许多改进

像往常一样，M5.3在编译器和IDE中都带来了许多改进。在编译器中，我们仍然主要关注性能，这正在逐渐改善。 IDE会获得新的快速修复和重构，其中一些将在下面介绍。您现在可以导航到覆盖您正在查看的属性（请参见左侧沟槽中的图标）。编辑器识别语法 [KDoc](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Doc) （谢谢 [这个拉请求](https://github.com/JetBrains/kotlin/pull/280) ）...但是首先，让我们谈谈酷的新语言功能，有些期待已久，有些意想不到的（也许）。
## 新语言功能：委派属性

我们经常收到以下功能要求：

* 支持延迟属性：仅在第一次访问时才计算该值。
* 支持可观察属性：听众收到关于此属性更改的通知。
* 支持在地图中存储属性，而不是单独的字段。
* 支持<我最喜欢的属性语义> ...

解决这些要求的一个方法就是说生活是艰难的，用户不得不忍受。另一种方式是在语言层面上支持不同类型的属性。我们不喜欢任何一种方法：一方面太多不愉快的用户，另一方面太多的特别功能。所以，我们采取第三种方法：支持涵盖所有这些请求（或许更多）的统一机制，以便特定类型的属性可以在库中实现，而不会改变语言。
认识<strong>委托属性</ strong>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example {
  var p: String by Delegate()
}
```

{% raw %}
<p></p>
{% endraw %}

有一些新的语法：您可以通过<expression>来表示“val <property name>：<Type>”。 </ strong>之后的表达式是<em>委托</ em>，因为与该属性相对应的get（）和set（）方法将被委派给它。属性委托不必实现任何接口，而是必须提供名为get（）和set（）的方法来调用。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Delegate() {
  fun get(thisRef: Any?, prop: PropertyMetadata): String {
    return "$thisRef, thank you for delegating '${prop.name}' to me!"
  }
 
  fun set(thisRef: Any?, prop: PropertyMetadata, value: String) {
    println("$value has been assigned")
  }
}
```

{% raw %}
<p></p>
{% endraw %}

当我们从p读取时，来自Delegate的get（）函数被调用，所以它的第一个参数是我们从p读取的对象，第二个参数保存p本身的描述（例如你可以使用它的名字）。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val e = Example()
println(e.p)
```

{% raw %}
<p></p>
{% endraw %}

这将打印“示例@ 33a17727，谢谢你委托'p'给我！”同样，当我们分配给p，set（）函数被调用。前两个参数相同，第三个参数保持分配的值：

{% raw %}
<p></p>
{% endraw %}

```kotlin
e.p = "NEW"
```

{% raw %}
<p></p>
{% endraw %}

这将打印“新的已分配给”p“在示例@ 33a17727”。
可能，您已经看到如何使用这种机制来实现懒惰或可观察的东西。尝试一下锻炼，但大部分已经完成了 [标准库](https://github.com/JetBrains/kotlin/blob/build-0.5.742/libraries/stdlib/src/kotlin/properties/Delegation.kt) 。
的 [kotlin.properties.Delegates](https://github.com/JetBrains/kotlin/blob/build-0.5.742/libraries/stdlib/src/kotlin/properties/Delegation.kt#L12) 对象拥有最有用的东西。我们从懒惰开始：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.properties.Delegates
 
class LazySample {
    val lazy: String by Delegates.lazy {
        println("computed!")
        "Hello"
    }
}
```

{% raw %}
<p></p>
{% endraw %}

Delegates.lazy（）是一个函数，它返回一个实现一个延迟属性的委托：第一次调用get（）执行传递给lazy（）的lambda表达式作为参数，并记住结果，后来的get（）调用简单地返回记住的结果。如果你想要<strong>线程安全</ strong>，请改用blockingLazy（）：它保证只在一个线程中计算这些值，并且所有的线程都会看到相同的值。
现在，我们转向观察：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class User {
    var name: String by Delegates.observable("<no name>") {
        d, old, new ->
        println("$old -> $new")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

observable（）函数有两个参数：初始值和修改的处理程序。每当我们分配到'name'时，处理程序被调用，它有三个参数：被赋值的属性，旧值和新值。如果您想要“否决”该作业，请使用否决权（）而不是observable（）。
接下来可能会有点意外：用户经常询问如果您有一个非空的var，但是您没有适当的值在构造函数中分配给它（即必须稍后分配）？您不能在Kotlin中拥有未初始化的非抽象属性：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
  var bar: Bar // error: must be initialized
}
```

{% raw %}
<p></p>
{% endraw %}

您可以使用null初始化它，那么您每次访问它时都必须检查。现在你有一个委托来处理这个：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
  var bar: Bar by Delegates.notNull()
}
```

{% raw %}
<p></p>
{% endraw %}

如果您在写入之前从此属性中读取，则会在第一个赋值之后引发异常，如预期的那样工作。
最后显示的是存储在地图中的属性。这在应用程序中出现了很多解析JSON或进行其他“动态”的东西：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class User(val map: Map<String, Any?>) {
    val name: String by Delegates.mapVal(map)
    val age: Int     by Delegates.mapVal(map)
}
```

{% raw %}
<p></p>
{% endraw %}

在这个例子中，构造函数采用地图：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val user = User(mapOf(
    "name" to "John Doe",
    "age"  to 25
))
```

{% raw %}
<p></p>
{% endraw %}

代表从这个地图获取值（通过字符串键 - 属性名称）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(user.name) // Prints "John Doe"
println(user.age)  // Prints 25
```

{% raw %}
<p></p>
{% endraw %}

当然，您也可以使用var（）和mapVar（）函数），这将在赋值后修改映射（请注意，您需要使用MutableMap而不是只读Map）。
还有其他用例，可能有许多改进。幻想，实验，享受！ 😉

{% raw %}
<p><a name="SAM-conversions"></a></p>
{% endraw %}

## SAM转换的第一步

我们介绍 [SAM构造函数](http://blog.jetbrains.com/kotlin/2013/04/kotlin-m5-2-intellij-idea-12-1-and-gradle/) 上次。当然这还不够，所以我们正在进行全面的SAM转换。该功能尚未完成，但您可以在简单的情况下使用它：

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater {
  button.setVisible(true)
}
```

{% raw %}
<p></p>
{% endraw %}

要提醒您，SAM转换是Java 8用于lambdas的：当您只有一个（抽象）方法（如Comparator或Runnable）的接口时，您可以通过一个lambda来传递此接口的实例（在这个例子我们传递一个lambda而不是一个Runnable）。 Kotlin没有这样的语言功能（因为在一个具有正确的函数类型的语言中不需要这个功能），所以它只适用于Java类。
## “可引用参考”中的第一步

我们正在进行的另一件事是“可调用引用”或“特征文字”，即将命名函数或属性作为值传递的能力。用户经常问“我有一个foo（）函数，我如何作为参数传递？”答案是：“你用'::'”前缀。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun isOdd(x: Int) = x % 2 != 0
 
val numbers = listOf(1, 2, 3)
println(numbers.filter(::isOdd)) // Prints [1, 3]
```

{% raw %}
<p></p>
{% endraw %}

这里“:: isOdd”是函数类型“（Int） - > Boolean”的值，您可以将其作为过滤谓词传递。另一个例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun compose<A, B, C>(f: (B) -> C, g: (A) -> B): (A) -> C {
    return {x -> f(g(x))}
}
```

{% raw %}
<p></p>
{% endraw %}

此函数返回传递给它的两个函数的组合：compose（f，g）= f（g（*））。现在，您可以将其应用于可调用引用：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun length(s: String) = s.size
 
val oddLength = compose(::isOdd, ::length)
val strings = listOf("a", "ab", "abc")
println(strings.filter(oddLength)) // Prints "[a, abc]"
```

{% raw %}
<p></p>
{% endraw %}

如果你想使用一个类的成员，你需要限定它，结果将是类型“扩展功能”，例如。 String :: toCharArray为String提供了一个扩展函数。
请注意，这是早期正在进行的工作</ strong>，所以很多事情都没有起作用，例如重载消歧，类型推断，属性等的支持。最终这个功能将演变成完全类型安全的反射，但是今天我们只是开始工作了。
## 改变签名重构

当您有很多呼叫站点进行更新时，添加/删除/重新排序功能参数可能很乏味。这就是为什么IDEs证明了一个“变更签名”重构。将光标放在一个函数或构造函数上，然后按Ctrl + F6（Mac上的Cmd + F6），你会得到如下对话框：

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s171/sh/b4eb0e6e-b866-4a12-83f9-b94ed3daf8d9/1ec5d8ee74c94a7c6433813dd3c488e9/deep/0/Screenshot%206/5/13%206:42%20PM.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

更改类型，重命名，重新排序或删除参数，并且所有呼叫站点将相应更新。
## 快速修复“类型不匹配”等

感谢贡献 [周杰克](https://github.com/univerio) ， [MichałSapalski](https://github.com/sapal) ， [WojciechŁopata](https://github.com/lopekpl) 和斯坦福大学领导的开源导师计划的其他学生，我们现在得到很多很好的快速修复。例如，当您遇到类型不匹配错误时，按Alt + Enter并获取一些建议来修复代码：

{% raw %}
<p><img alt="" class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s171/sh/ff9bd33c-ecd1-4800-91f2-4a69db761a37/f829b15d7de80df501e39b64f6973754/deep/0/Screenshot%206/5/13%206:51%20PM.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

## 代码转换

另一组有用的IDE操作可在等效的代码形式之间进行转换，如：<br/>
<span class =“embed-youtube”style =“text-align：center; display：block;”> <iframe allowfullscreen =“true”class =“youtube-player”height =“390”src =“https：// www.youtube.com/embed/Cfwq-pYtiDY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent“style =”border：0 ;“ type =“text / html”width =“640”> </ iframe> </ span>
您也可以使用Ctrl + Shift + Up / Down来移动语句或声明：

{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/RRRROZc3-2g?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## 安装

像往常一样，新的插件可以从中安装 [我们的插件库](http://plugins.jetbrains.com/plugin?pr=idea&pluginId=6954) 。
<strong>拥有不错的Kotlin！</ strong>
