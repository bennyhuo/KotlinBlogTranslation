---
title: "[译]Multiple Inheritance Part 2: Possible directions"
date: 2011-08-31 16:21:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-2-possible-directions/
translator:
translator_url:
---

在里面 [此系列之前的帖子](http://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-1-problems-with-the-existing-design/) 我们讨论了缺点 [我们最初为 Kotlin 计划的继承模式](http://confluence.jetbrains.net/pages/viewpage.action?pageId=41484416) 。今天我们将谈谈替代设计。
请注意，这些帖子旨在引发讨论，以便我们可以从您的反馈中获益，并提出更好的设计。
**什么是**
上一篇文章总结了以下（不完整）的其他语言可用的多重继承问题解决方案列表：

* Java 和 C＃具有类和接口，即多接口继承和单实现继承;
* Scala 具有可以实现方法甚至具有状态的类和特征，但是它们的构造函数不能有参数;
* 一些其他语言，如堡垒，不允许国家的特征;
* <您最喜欢的语言>

我们都知道 Java 的方法是坚实的，但是对代码重用造成了严重的限制，所以我们想放宽这些限制，但是不要陷入困境。放宽限制的“第一学位”将是<无状态特征**（如在 Fortress 和 in [[1]](#Traits) ）：没有状态的特征，没有隐含的覆盖。或者我们可以将状态的遗产交易出来，并获得混合（像在 Ruby 中）。放宽限制，我们得到**Scala 的特征**，它们具有状态，但没有构造函数的参数，一个特征可能会覆盖另一个特征。然后，我们以**要求**到 CZ 的课程（如 [[2]](#CZ) ）。下一步，我猜，已经是不受限制的多重继承，就像在 C ++ 中一样。
我们将略过对这些解决方案的全面分析，只是对状态进行评论
<span id =“more-115”> </span> <br/>
**状态。**一个重要的考虑因素是允许在这个或那个表单中允许**多重继承状态**。一方面，这似乎是非常有用的，但另一方面，它带来了问题。讨论了一个问题 [以前的帖子](http://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-1-problems-with-the-existing-design/#Problem2) 以**问题 2**的名义：
<p>执行 Left 假定它用 3 初始化，但它可能会调用在 Right 中实现的 bar（），并假设所有内容都被初始化为 4.这可能会导致一些不一致的行为。</p>
另一个问题是，以遗传为单位（类或特征或混合）表示在其中具有构造函数，并且构造函数可能具有副作用，并且重要的是以**可预测顺序**。
**问题 2**非常适用于 Scala 在 trait 构造函数中没有参数的方法。不幸的是，构造器副作用的问题仍然存在：改变特征之间的继承关系（例如由图书馆作家完成）可以在创建子类实例时重新排列构造函数的副作用（参见 [这个评论如下](#comment-110) ）。这个问题似乎是不可避免的，无论我们选择多少继承国家的方式，我希望有人能证明我错了！
所有这一切，我会解释一下我们正在考虑的设计。如上所述，本文的目的是开始讨论，所以您的反馈非常受欢迎。
**Kotlin 方式（Attempt＃2）**
首先，我想指出，在这一点上，我们更喜欢保守的解决方案*，所以如果他们提供的功能集是不够的话，我们可以自然地延长它们。
简而言之，目前的设计可以描述如下：

* 无状态特征：没有属性与后备字段，没有构造函数，
* 这可以“需要”类存在于使用特征的具体类的一组超类中，
* 没有自动解决压缩冲突：如果一个类继承了两个实现的东西，它必须重写这个东西，并提供自己的实现（即从继承的实现中选择，或者从头编写它们，或者混合使用它们）。

所以我们现在不再拥有状态*的多重继承。我认为如果我们以这种方式尝试，考虑放宽以后的限制，如果有真正的需求，那么*可以。
**语法**现在，让我们用一些语法来渲染。这里的第一个问题是“我们还应该把这些无国籍人士的班级，还是有一个特殊的任期呢？”他们不同于课堂，施加一些限制，现在他们没有任何状态。如果只有课程，用户将会陷入以下情况：

* 没有什么告诉我，这个班是特别的，所以
* 我加了一块状态，和
* 编译器抱怨没有构造函数，所以
* 我只是添加一个构造函数
* 得到一些其他类的错误告诉我，我打破了一个人的超类型列表，所以
* 在跟踪错误的真正原因之前需要一些时间，这是不好的。

如果我知道这个类别首先有一些限制，那将会更好一些，所以我不会盲目地做出任何改变，如果我做了一个坏的改变，编译器会知道我违反了本地的限制，并会适当地抱怨。所以，最好是在不受限制的类中具有不同的语法特征。所以，让我们在声明前面加上一个关键字**trait**，而不是**class** <sup> <a href="#Footnote1"> 1 </a> </sup >。
所以，我们有类（state 和 all，但是单一继承）和 traits（没有状态，没有构造函数，而是多重继承）。特征可以声明（“require”，是 CZ 术语）一个超级*类*，但不能初始化它：

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class MyClass() {
  fun foo() { ... }
}
 
trait MyTrait : MyClass { // MyClass is not initialized
  fun bar() {
    foo() // calls foo() from MyClass
  }
}
 
class Child : MyClass(), MyTrait { // MyClass is initialized
}
 
class ChildErr : MyTrait { // ERROR: MyClass must be a supertype
}
```

{% raw %}
<p></p>
{% endraw %}

这允许 traits 使用基类的成员，而不会干扰初始化逻辑。
另一个句法问题是我们是否应该有一个单一的同质超类型列表（如上面的例子），或者像 Java 的“扩展”和“实现”子句，或者甚至 Scala 的“扩展类 Trait1 与 Trait2 与 Trait3”语法。使事情明确的想法说明了在超类型列表中的类的一些句法分离，因为它在某种程度上是有特权的，即至少具有像 Java 的“扩展”和“实现”这样的东西。另一方面，我们都知道这个令人讨厌的例子，当我将一个接口变成一个抽象类，并且必须改变所有这些用于实现*接口的子类，现在必须<em >扩展*该类。可能在语法上局部变化的变化是非本地化的。这就是为什么我们倾向于拥有一个同质的超类型列表，如上例所示。
**使用 traits**
现在，我们禁止国家的特质。这当然是一个很大的限制，但是我想指出它不是什么。
**您可以在特征中具有属性。**限制是这些属性不能具有后备字段或初始值设置，但属性本身可能会出现在特征中：

{% raw %}
<p></p>
{% endraw %}

```kotlin
trait Trait {
  val property : Int // abstract
 
  fun foo() {
    print(property)
  }
}
 
class C() : Trait {
  override val property : Int = 239
}
```

{% raw %}
<p></p>
{% endraw %}

我们的特征声明了一个**抽象**属性，该类用有状态的方式覆盖它。现在，trait 可以使用该属性，通过晚期绑定的调用，如果我们在 C 对象上调用 foo（），我们得到 239 打印。
**您可以访问您的 traits 的状态。**上一个示例显示了如何间接地进行排序，通过使子类覆盖您定义的属性，但还有另一种方法。记住一个特征可能声明（需要）一个超类：

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class A(x : Int) {
  val y = x * 2
}
 
trait B : A {
  fun foo() {
    print(y)
  }
}
 
class C() : A(239), B {}
```

{% raw %}
<p></p>
{% endraw %}

在这个例子中，我们有一个基类 A，它定义了一个具体的属性 y 并初始化它。 trait B 扩展了这个类，但是没有传递一个构造函数参数，因为 traits 根本没有初始化代码。请注意，B 可以访问在 A 中定义的属性 y。现在，类 C 扩展 A 并使用 239 进行初始化，并扩展 B.扩展 B 是正确的，因为 B 需要 A，并且我们扩展 A，所有权利。<br/>
现在，当我们在 C 的实例上调用 foo（）时会发生什么？它打印 478（239 * 2），因为 y 的值是从这个实例获得的，C 的构造函数在那里写了 239。
现在，我们来看一下关于 traits 的最后一个例子：
**如何解决压倒一切的冲突。**当我们在超类型列表中声明很多类型时，可能会出现我们继承同一个方法的多个实现。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
trait A {
  fun foo() { print("A") }
  fun bar()
}
 
trait B {
  fun foo() {print("B")}
  fun bar() {print("bar")}
}
 
class C() : A {
  override fun bar() { print("bar") }
}
 
class D() : A, B {
  override fun foo() {
    super<A>.foo()
    super<B>.foo()
  }
}
```

{% raw %}
<p></p>
{% endraw %}

特征 A 和 B 都声明函数 foo（）和 bar（）。他们都实现了 foo（），但只有 B 实现 bar（）（bar（）在 A 中没有标记为**abstract**，因为这是 traits 的默认值，如果函数没有 body）。现在，如果我们从 A 导出一个具体的类 C，我们显然必须重写 bar（）并提供一个实现。如果我们从 A 和 B 导出 D，我们不必重写 bar（），因为我们只继承了它的一个实现。但是我们继承了两个* foo（）的实现，所以编译器不知道哪一个可以选择，并强制我们重写 foo（）并且明确地说出我们想要的内容。
我觉得今天已经够了你的意见是非常欢迎的，像往常一样。
**参考**

0. NathanaelShärli，StéphaneDucasse，Oscar Nierstrasz 和 Andrew Black。特征：可行的行为单位。 ECOOP-2003，pdf 预印本。=== Donna Malayeri 和 Jonathan Aldrich。 CZ：没有钻石的多重继承。 SIGPLAN 不。 44，10（2009 年 10 月），21-40，pdf 预印本。


{% raw %}
<hr/>
{% endraw %}

1 以前这篇文章曾经说过如下：
一个很好的方法是在类声明中设置一个限定符，即**trait class**，而不仅仅是**类**（我们可以说只是**trait < / strong>，但是对它有一些语言的可扩展性考虑，我现在不想深入研究。）</p>
但是我们已经找到了一个简单的解决方案来解决我们的语言扩展性问题，而且问题不再存在。
