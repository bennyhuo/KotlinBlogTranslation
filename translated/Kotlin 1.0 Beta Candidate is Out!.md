---
title: "[译]Kotlin 1.0 Beta Candidate is Out!"
date: 2015-10-22 16:54:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/10/kotlin-1-0-beta-candidate-is-out/
translator:
translator_url:
---

我们很高兴地介绍Kotlin <strong> Beta Candidate </strong>。官方的1.0 Beta版将很快推出。到目前为止，二进制格式已经完成，没有规划主要的语言变化，标准库中只有一些变化即将到来。
在这篇文章中，我们描述了自M14以来的变化，包括

* 从对象进口，
* 新的更安全的收集界面，
* 内联Java常量，
* 更好地支持Java静态，
* 和更多。

## 语言变化

我们正在推出一些突破性的变化以及新的重要特征。
### 运算符和中缀功能

由于M14，Kotlin需要使用用于操作符重载的函数的`运算符`修饰符。从现在起，对于中缀函数也是如此：

{% raw %}
<p></p>
{% endraw %}

```kotlin
operator Foo.plus(other: Foo): Foo { ... }
 
fun testPlus() = Foo() + Foo()
 
infix fun Foo.bar(other: Foo): Foo { ... }
 
fun testInfix() = Foo() bar Foo()
```

{% raw %}
<p></p>
{% endraw %}

现在，我们放宽了对Java函数的这一要求：具有合适签名的任何Java函数都可以用作运算符</strong>，但不能作为中缀使用。
一些操作员名称已更改，以避免歧义：

* 我们现在应该使用unaryPlus和unaryMinus，而不是仅仅加上和减去一元函数，即-Foo（）现在是Foo（）。unaryMinus（）;
* 对于委派的属性，应该使用getValue和setValue，而不是仅仅获取和设置。

<em>代码清理</em>操作将帮助您迁移代码。
此外，操作员签名现在由声明站点上的编译器进行检查。这些检查中的一些可能在将来放松，但我们相信现在我们现在是一个很好的起点。
### 从对象导入

Kotlin现在支持通过名称导入对象的个别成员（但不能从对象导入`*`  -  import）

{% raw %}
<p></p>
{% endraw %}

```kotlin
import mypackage.MyObject.foo
 
val test = foo("...")
```

{% raw %}
<p></p>
{% endraw %}

在这个例子中，我们从命名对象`mypackage.MyObject`导入了所有名为`foo`的成员。
要从类的伴随对象导入，我们必须指定其全名：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import mypackage.MyClass.Companion.foo
```

{% raw %}
<p></p>
{% endraw %}

### Rich @已删除

我们最近一直在迁移很多代码<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains。 com / kotlin / wp-includes / images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em;“/>所以Kotlin的`@Deprecated < / code>注释已经变得非常强大：它不仅需要一个消息，并允许通过`ReplaceWith（“...”）`指定替换，它还具有`级别</code > now：`WARNING`，`ERROR`或`HIDDEN`。

* 警告是默认的，可以作为正常的弃用：在呼叫站点会有警告，IDE会将其删除，
* ERROR是一样的，但报告编译错误而不是警告，
* HIDDEN是以前的@HiddenDeclaration：它只是使这个声明在编译时对客户端不可见。

### 用于捕获本地变量的智能转换

即使在lambdas中捕获的本地`var`，即使在这些lambdas中没有突变，智能转换也可以工作：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var a: Any? = ...
 
val mapped = users.map {
    "${it.name}: $a"
}
 
if (a is String) {
    println(a.length) // This works now
}
```

{% raw %}
<p></p>
{% endraw %}

### 多个main（）函数在同一个包中

我们现在可以在每个文件中定义一个带有标准签名的`main（）`函数（除了`@file：JvmMultileClass`）。这在实验代码时非常有用：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// FILE: a.kt
package foo
 
fun main(args: Array<String>) {
    println("a.kt")
}
 
// FILE: b.kt
package foo
 
fun main(args: Array<String>) {
    println("b.kt")
}
```

{% raw %}
<p></p>
{% endraw %}

### Varargs和扩展操作符

要概述：在调用`vararg`函数时，我们可以使用 [传播操作员](https://kotlinlang.org/docs/reference/functions.html#variable-number-of-arguments-varargs) 将数组转换为vararg：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(vararg args: String) { ... }
 
fun bar(vararg args: String) {
    foo(*args) // spread operator
}
```

{% raw %}
<p></p>
{% endraw %}

<em>扩展运算符</em>的语义已被修复，以便始终保证`foo`看到的数组不会被“外部世界”修改或观察。我们可以假设每次使用扩展运算符时都会做出防御性拷贝（实际上，稍后可能会实现一些优化来减少内存流量）。
因此，Kotlin图书馆的作者可以依赖于安全地存储的vararg数组，而无需防御性复制
<strong>注意</strong>：当Kotlin函数从java调用时，由于没有使用任何扩展操作符，因此不能满足此保证。这意味着如果一个函数旨在从Java和Kotlin两者中使用，那么它的Java客户端的合同应该包含一个注释，该数组应该在传递给它之前被复制。
### “sparam”注释目标已重命名为“setparam”

要注释属性的setter参数，请使用`setparam` use-site target而不是`sparam`：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@setparam:Inject
var foo: Foo = ...
```

{% raw %}
<p></p>
{% endraw %}

### @UnsafeVariance注释

有时我们需要压制 [申报站点方差检查](https://kotlinlang.org/docs/reference/generics.html#declaration-site-variance) 在我们的课上例如，为了使`Set.contains`类型安全，同时保持只读集合变量，我们必须这样做：

{% raw %}
<p></p>
{% endraw %}

```kotlin
interface Set<out E> : Collection<E> {
    fun contains(element: @UnsafeVariance E): Boolean
}
```

{% raw %}
<p></p>
{% endraw %}

这对`包含`的实现者负有一定的责任，因为通过这个检查可以抑制`元素`的实际类型在运行时可能是任何东西，但有时候需要实现方便的签名。详细了解下面的集合的类型安全性。
因此，为此，我们为类型引入了`@UnsafeVariance`注释。这是故意长时间，并突出警告再次滥用它。
### 杂项检查和限制

增加了许多支票，其中一些限制可能会在以后解除。
<strong>键入参数声明</strong>。我们决定限制类型参数声明的语法，以便所有这样的声明是一致的，所以

* 有趣的foo <T>（）已被弃用，有利于fun <T> foo（）：
* 类型参数的所有约束都应在“where”或“<...>”内部出现：


{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T: Any> foo() {} // OK
fun <T> foo() where T: Serializable, T: Comparable<T> {} // OK
 
fun <T: Serializable> foo() where T: Comparable<T> {} // Forbidden
```

{% raw %}
<p></p>
{% endraw %}

<strong>数组的动态类型检查</strong>。数组元素类型在Java中被引用，但是它们的Kotlin特定属性（如可空性）不是。因此，我们删除了允许像`a为Array＆lt; String＆gt;`的检查的数组的特殊处理，现在数组作为所有其他通用类工作：我们可以检查`a是Array * ;`和像`a的转换像Array＆lt; String＆gt;`被标记为未选中。我们添加了一个特定于JVM的函数`isArrayOf＆lt; T＆gt;（）`，以确定给定的数组可以包含Java </em>中的`T` <em>类型的元素：

{% raw %}
<p></p>
{% endraw %}

```kotlin
    val a: Any? = ...
 
    if (a is Array<*> && a.isArrayOf<String>()) {
        println((a as Array<String>)[0])
    }
```

{% raw %}
<p></p>
{% endraw %}

<strong>委派属性</strong>。委托属性的约定现在在`getValue`和`setValue`中使用`KProperty * *＆gt;`而不是`PropertyMetadata`

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.getValue(thisRef: Bar, property: KProperty<*>): Baz? {
    return myMap[property.name]
}
```

{% raw %}
<p></p>
{% endraw %}

代码清理</em>将帮助您进行迁移。
<strong>可调用引用</strong>。现在禁止使用`::`的一些用法，稍后在实现绑定引用时启用。最值得注意的是，当`foo`是类的成员时，现在不应该使用`:: foo`应该使用`MyClass :: foo`。对对象成员的引用也暂时不受支持（它们也将作为绑定引用）。我们可以暂时使用lambdas作为解决方法。
<strong> If-expressions </strong>。当`if`用作表达式时，通过要求`else` `if`和`时统一了`的语义。

{% raw %}
<p></p>
{% endraw %}

```kotlin
val foo = if (cond) bar // ERROR: else is required
```

{% raw %}
<p></p>
{% endraw %}

<strong>不返回函数</strong>。当一个函数知道抛出一个异常或循环永远，它的返回类型可能是`Nothing`，这意味着它永远不会正常返回。为了使工具更智能，我们要求这些函数始终显式指定其返回类型：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() = throw MyException() // Must specify return type explicitly
 
fun bar(): Nothing = throw MyException() // OK
fun baz() { throw MyExcepion() } // OK
fun goo(): Goo { throw MyExcepion() } // OK
```

{% raw %}
<p></p>
{% endraw %}

这是一个警告，在我们使用<em>代码清理</em>迁移我们的代码后，这些警告会被提升为错误
<strong>可见性检查</strong>被限制，例如，公共声明不能公开本地，私有或内部类型。访问内部声明在编译器以及IDE中进行检查;
查看更多 [这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-1038) 。
## 集合

该版本的主要变化是我们已经清理了集合和其他核心API，例如，`size`现在是一个属性，`包含`是类型安全的：它需要`E`而不是`Any？`。这是使图书馆感觉像Kotlin一样保持与Java兼容的重大努力。这背后有相当多的编译器魔法，但是我们对结果感到满意。
例：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val strs = setOf("1", "abc")
 
if (1 in strs) { // 'strs' is a set of strings, can't contain an Int
    println("No!")
}
```

{% raw %}
<p></p>
{% endraw %}

类似的代码在Java中起作用，因为`Set＆lt; E＆gt; .contains`（`中的`被编译为）需要`Object`，而不是`/ code>，集合的元素类型。这被证明是容易出错的，所以我们决定让Kotlin收集接口更安全（同时保持与Java集合的完全兼容性）。因此，我们的`包含`需要一个`E`，上面的例子在Kotlin中是不正确的。
目前，Kotlin编译器在上述示例中报告了`中的`的弃用警告，因为我们在标准库中提供了过渡扩展功能，以帮助每个人迁移，但是很快这将是一个错误。 <em>代码清理</em>是我们的朋友：它将用`strs.containsRaw（1）`替换strs`中的`1。 `containsRaw`是标准库中的一个新功能，当我们真正需要</em>类似Java的行为时，我们可以使用它们：我们可以使用< code> containsRaw`。
底线：

* Collection.contains，Map.get和其他一些收集方法现在更安全;
* 我们可以使用containsRaw，getRaw等获取无类型的行为;
* Collection.size，Array.size，String.length，Map.Entry.key等现在属性;
* List.remove（Int）已重命名为removeAt（int），以避免与按照项目而不是索引删除的List <Int> .remove发生冲突。
* 代码清理将迁移所有代码。

所有正常的Java集合都可以正常工作：编译器知道如何在一个`java.util.ArrayList`上找到一个“属性”`size`。
## Java互操作

有很多重要的变化涉及到Kotlin声明如何从Java可见，反之亦然。
### 在库中定义的常量内联

从现在开始，我们在库中引入了Java常量（原始和String类型的公共静态final字段）。这将有助于Android开发人员遇到API不兼容：

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) { ... }
```

{% raw %}
<p></p>
{% endraw %}

现在可以在Android运行时的任何版本上工作（用于在比Lollipop小的运行时崩溃）。
### 较小的运行时间

我们只是从那里开始，但是为减少`kotlin-runtime`库的大小而开发的工作基础。现在它比现在的M14只有200K，但是我们做的更多的事情要做的更少（不会破坏兼容性）。
### 静态方法，字段和类

Kotlin现在对Java静态非常友好：

* 我们可以在其Kotlin子类的Java类中使用继承的嵌套类，静态方法和字段;
* 我们可以通过子类名称访问继承的Java静态方法和字段：SubClass.SUPER_CLASS_CONSTANT;
* 我们可以从Kotlin子类中访问超类的伴侣对象的成员;
* 但唯一的限定名称一个类可以访问的是它的规范名称，即我们不能说SubClass.SupersInnerClass。

这关闭了我们过去使用的大型继承框架（如Android）的许多问题。
### 接口继承规则与Java 8兼容

为了使Kotlin面向未来，我们添加了一些符合Java 8的要求，以便能够以后将Kotlin接口中的函数体编译为Java默认方法。
在某些情况下，它会导致Kotlin需要比以前更加明确的覆盖，可惜的是，不能在接口中实现`Any`的方法（这在Java 8中不起作用）。
旁注：接口方法的默认实现可以从Java访问，作为`MyIntf.DefaultImpls`的静态成员。
### 布鲁塞尔更方便的吸气剂名称

例如，当Kotlin中的一个属性被命名为`isValid`时，它的Java getter现在将是`isValid（）`而不是`getIsVaild（）`。
### @JvmField和对象

我们已经制定了生成纯字段的策略（而不是获取/设置对）更可预测：从现在开始，只注释为`@JvmField`，`lateinit`或`const`作为字段公开给Java客户端。旧版本使用启发式方法，无条件地在对象中创建静态字段，这违反了我们默认情况下具有兼容二进制兼容性的API的初始设计目标。
此外，单例实例现在可以通过名称`INSTANCE`（而不是`INSTANCE $`）访问。
我们不得不禁止在接口中使用`@JvmField`，因为我们不能保证正确的初始化语义。
### Int是可序列化的

现在，类型`Int`和其他基本类型是JVM上的`Serializable`。这应该有助于许多框架。
### 没有“包立面”

类似于`KotlinPackage`等等已经不见了。我们已经完成了转换到新的类文件布局，以前不推荐使用的“程序包外观”现在已被删除。使用`FileNameKt`和/或`@file：JvmName`（使用可选的`@file：JvmMultifileClass`）。
### 内部现在已经被破坏了

由于Java没有`内部`可见性（但是），我们必须调整`内部`声明的名称，以避免在从另一个模块扩展类时，覆盖中出现意外的冲突。在技​​术上，内部成员可用于Java客户端，但是它们看起来很丑，这是我们可以为图书馆进化的可预测性支付的最低价格。
### 其他贬低和限制


* @Synchronized和@Volatile不适用于抽象声明;
* 作为摆脱外部注释的最后一步，@KotlinSignature已被弃用，将被删除;
* 参数包含Nothing的通用类型现在将被编译为原始Java类型，因为Java没有“Nothing”的正确对应项;

## IDE更改


* 现在，参数信息几乎无处不在，包括括号，这个和超级调用

