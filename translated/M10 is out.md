---
title: "[译]M10 is out"
date: 2014-12-17 15:02:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/12/m10-is-out/
---

在庆祝活动开始之前，我们设法发布了Kotlin的下一个里程碑，添加了<strong>动态类型</strong>等等。我们来看看M10带给我们什么。 <span id =“more-1708”> </span>
## 语言增强

语言的一些改进，特别是：
### 内联函数的Reified类型参数

在M10之前，我们有时会写这样的代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> TreeNode.findParentOfType(clazz: Class<T>): T? {
    var p = parent
    while (p != null && !clazz.isInstance(p)) {
        p = p?.parent
    }
    return p as T
}
```

{% raw %}
<p></p>
{% endraw %}

在这里，我们走一棵树，并使用反射来检查节点是否具有某种类型。这一切都很好，但通话网站看起来有点混乱：

{% raw %}
<p></p>
{% endraw %}

```kotlin
myTree.findParentOfType(javaClass<MyTreeNodeType>())
```

{% raw %}
<p></p>
{% endraw %}

我们实际想要的是简单地将类型</em>传递给此功能，即调用如下：

{% raw %}
<p></p>
{% endraw %}

```kotlin
myTree.findParentOfType<MyTreeNodeType>()
```

{% raw %}
<p></p>
{% endraw %}

但是，我们需要使用<em>的泛化泛型</em>来访问一个函数中的类型，而在JVM上，通用的泛型是昂贵的...
幸运的是，Kotlin有 [内联函数](http://kotlinlang.org/docs/reference/lambdas.html#inline-functions) 现在他们支持<strong> reified </strong>类型参数，所以我们可以这样写：

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun <reified T> TreeNode.findParentOfType(): T? {
    var p = parent
    while (p != null && p !is T) {
        p = p?.parent
    }
    return p as T
}
```

{% raw %}
<p></p>
{% endraw %}

我们使用<strong> reified </strong>修饰符对type参数进行限定，现在可以在函数内部访问，几乎就像是普通类一样。由于函数是内联的，因此不需要反射，像<strong>！</strong>这样的正常运算符正在工作。另外，我们可以如上所述调用它：<code> myTree.findParentOfType＆MyTreeNodeType＆gt;（）</code>。
虽然在许多情况下可能并不需要反思，但我们仍然可以使用一个重定义的类型参数：<code> javaClass <t>（）</t> </code>使我们可以访问它：

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun methodsOf<reified T>() = javaClass<T>().getMethods()
 
fun main(s: Array<String>) {
  println(methodsOf<String>().joinToString("\n"))
}
```

{% raw %}
<p></p>
{% endraw %}

正常功能（未标记为<code> inline </code>）不能有参数。不具有运行时表示形式的类型（例如，非引用类型参数或类似于<code> Nothing </code>的虚构类型）不能用作引用类型参数的参数。
此功能旨在简化传统上依赖于反思的框架中的代码，我们的内部实验表明它的工作正常。
### 检查申报地点差异

Kotlin有 [申报地点差异](http://kotlinlang.org/docs/reference/generics.html#declaration-site-variance) 从一开始，但编译器长时间缺少通讯员检查。现在他们放在他们的位置：编译器抱怨如果我们在</strong>或<strong> out </strong>中声明一个类型参数为<strong>，但在类体中滥用它：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C<out T> {
  fun foo(t: T) {} // ERROR
}
```

{% raw %}
<p></p>
{% endraw %}

在这个例子中，由于T在T中被声明为<strong> out </strong>（即类是<em> covariant </em>），我们不允许将它作为<code> foo的参数（）</code>函数，我们只能返回它。
请注意，<strong>私人</strong>声明可以违反方差限制，例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C<out T>(t: T) {
    private var foo: T = t
}
```

{% raw %}
<p></p>
{% endraw %}

虽然<code> foo </code>的设置器将T作为参数，因此违反了<strong> out </strong>限制，编译器允许这样做，并确保只有同一个实例</em> <code> C </code>可以访问<code> foo </code>。这意味着<code> C </code>中的以下函数将无法编译：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// inside the class C
private fun copyTo(other: C<T>) {
    other.foo = foo // ERROR: Can not access foo in another instance of C
}
```

{% raw %}
<p></p>
{% endraw %}

这是一个<strong>破坏变化</strong>：以前编译的一些代码可能会中断，但是不能修复它可能会导致运行时异常，所以编译器错误将对你有一些价值<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/ simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“
### 类型推断支持使用方差

类型参数推断已被改进以适应 [使用方差](http://kotlinlang.org/docs/reference/generics.html#type-projections) 更舒适现在您可以调用通用功能，例如一个投影类型的<code> reverseInPlace（）</code>，例如<code> Array＆lt; out Number＆gt; </code>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example(a: Array<out Number>) {
    a.reverseInPlace()
}
```

{% raw %}
<p></p>
{% endraw %}

其中<code> reverseInPlace </code>定义如下：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> Array<T>.reverseInPlace() {
    fun (i in 0..size() / 2) {
        val tmp = this[i]
        this[i] = this[size - i - 1]
        this[size - i - 1] = tmp
    }
}
```

{% raw %}
<p></p>
{% endraw %}

最初由罗斯·泰特（Ross Tate）提出的基本机制 [“混合场地差异”](http://www.cs.cornell.edu/~ross/publications/mixedsite/) 。
### Varargs转换为投影阵列

另一个<strong>突破性变化</strong>的形式是对一个晦涩的修复，但有时候 [相反](https://youtrack.jetbrains.com/issue/KT-5534) [烦人的](https://youtrack.jetbrains.com/issue/KT-2163) 问题：当我们有一个使用<code> String？</code>的变量的函数时，我们真的希望能够将<code> String </code>的数组传递给它，不是吗？在M10之前是不可能的，因为T的vararg被编译为<code> Array＆lt; T＆gt; </code>，现在它们被编译为<code> Array＆lt; out T＆gt; </code>，并且以下代码工作：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun takeVararg(vararg strings: String?) { ... }
 
val strs = array("a", "b", "c")
takeVararg(*strs)
```

{% raw %}
<p></p>
{% endraw %}

## JavaScript改进和更改

JavaScript在此版本中获得重要更新，支持动态类型。
### 动态支持

有时与动态语言交谈的最佳方式是动态的。这就是为什么我们引入了软键盘<em>动态</em>，这样我们可以将类型声明为动态的。目前，这仅在定位JavaScript而不是JVM时才受支持。
当与JavaScript进行互操作时，我们现在可以使用函数作为参数，或返回动态类型

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun interopJS(obj: dynamic): dynamic {
   ...
   return "any type"
}
```

{% raw %}
<p></p>
{% endraw %}

我们将在单独的博客文章中详细介绍动态更多细节以及使用场景和限制。对于技术性见 [规格文件](https://github.com/JetBrains/kotlin/blob/master/spec-docs/dynamic-types.md) 。
### 新注释

我们添加了一系列注释，使JavaScript互操作更简单，特别是nativeInvoke，nativeGetter </em>和<em> nativeSetter </em>。
如果使用<code> nativeInvoke </code>注释了一个函数<code> bar </code>，它的调用<code> foo.bar（）</code>将被转换为<code> foo（）</code>在JavaScript中。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
   nativeInvoke
   fun invoke(a: Int) {}
}
 
val f = Foo()
f(1) // translates to f(1), not f.invoke(1)
f.invoke(1) // also translates to f(1)
```

{% raw %}
<p></p>
{% endraw %}

同样的方式，我们可以使用NativeGetter </em>和<em> nativeSetter </em>来获取JavaScript中的索引访问权限：

{% raw %}
<p></p>
{% endraw %}

```kotlin
native("Array")
class JsArray<T> {
   nativeGetter
   fun get(i: Int): T = noImpl
   nativeSetter
   fun set(i: Int, v: T): Unit = noImpl
}
```

{% raw %}
<p></p>
{% endraw %}

没有<code> native * </code>注解，调用<code> get </code>和<code> set </code>（包括按惯例完成的那些，例如<code> a [i] = j <代码>与<code> a.set（i，j）</code>相同）被翻译成<code> a.get（...）</code>和<code> a.set（.. 。）</code>，但是注释如上所述，它们在JavaScript中被转换为方括号运算符：

{% raw %}
<p></p>
{% endraw %}

```kotlin
a[0] // translates to a[0], not a.get(0)
a.get("first") // translates to a["first"]
a[2] = 3 // translates to a[2] = 3
```

{% raw %}
<p></p>
{% endraw %}

在以下情况下，我们可以使用这些注释：

* 非扩展成员函数的本机声明，
* 顶级扩展功能。

### Kotlin.js输出突破变化

以前，在创建新项目时，将在名为<em> scripts </em>的文件夹中创建kotlin.js运行时。从M10开始，这个文件是在第一次编译时创建的，并且被放置在输出文件夹（默认为<em> out </em>）中。这提供了一个更容易的部署场景，因为库和项目输出现在位于同一根文件夹下。
### kotlin-js编译器的新no-stdlib选项 - 打破变化

我们现在为kotlin-js编译器提供一个命令行选项，即<em> no-stdlib </em>。没有指定此选项，编译器使用捆绑的标准库。这是M9行为的改变。
### js代码

我们现在可以直接在Kotlin代码中输出JavaScript代码

{% raw %}
<p></p>
{% endraw %}

```kotlin
js("var value = document.getElementById('item')")
```

{% raw %}
<p></p>
{% endraw %}

它将代码提供为参数，并将其直接注入到编译器生成的AST JavaScript代码中。
如您所见，我们在此版本中为JavaScript添加了大量新的改进，我们将在单独的文章中更详细地介绍这些改进。
## Java互操作

### [platformStatic]属性

现在，我们可以将属性标记为<code> [platformStatic] </code>，以便它们的访问者从Java可视为静态方法。
### 对象中的静态字段

任何对象的属性现在都会产生静态字段，以便它们可以轻松地从Java消费，即使不需要使用<em> platformStatic </em>注释进行装饰。
### JNI和[本地]

Kotlin现在通过<code> [native] </code>注释支持JNI，在<code> kotlin.jvm </code>包中定义（参见规范文档 [这里](https://github.com/JetBrains/kotlin/blob/master/spec-docs/jvm-native-flag-support.md) 。）。要声明本机方法，只需将注释放在其上：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.jvm.*
import kotlin.platform.*
 
class NativeExample {
    native fun foo() // native method
 
    class object {
        platformStatic native fun bar() // static native method
    }
}
```

{% raw %}
<p></p>
{% endraw %}

这是一个 [例](https://github.com/ligee/kotlin-ndk-samples/blob/master/hello-jni/src/com/example/hellojni/HelloJni.kt) 使用Android和NDK的原生声明。
## IntelliJ IDEA改进

IntelliJ IDEA领域的一些改进包括：
### 混合项目增量汇编

我们已经增强了增量编译，并且使用M10，它现在支持Kotlin和Java代码之间的依赖。现在，当您更改Java代码时，您的Kotlin代码的相关部分将被重新编译。作为提醒，增量编译在Kotlin编译器选项下激活。
### HotSwap在调试器中固定

现在，当我们在调试的时候重新编译Kotlin代码，它顺利地被重新加载到了难民程序中。
### 评估表达：完成改进

在调试会话期间，在评估表达式时，根据需要自动添加转换。例如，当从<em>任何</em>下载到特定类型时。

{% raw %}
<p><img alt="Completion Casts" class="aligncenter size-full wp-image-1716" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/12/completion.png?resize=564%2C126&amp;ssl=1"/></p>
{% endraw %}

### 复制参考

我们现在可以获得任何Kotlin符号的完整参考，就像我们一样 [IntelliJ IDEA在Java代码中](https://www.jetbrains.com/idea/help/cutting-copying-and-pasting.html) {% raw %}
<p><img alt="Copy Reference" class="aligncenter size-full wp-image-1711" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/12/copy-reference-no-retina.png?resize=457%2C269&amp;ssl=1"/></p>
{% endraw %}

### 


从类和包的使用创建

现在，使用创建可用于类和包，这对TDD工作流程有重大贡献。即使您不在做TDD，它也会减少创建新元素的摩擦。

{% raw %}
<p><img alt="Create Class from Usage" class="aligncenter size-full wp-image-1713" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/12/create-class.png?resize=421%2C108&amp;ssl=1"/></p>
{% endraw %}

### 泛型改变签名

变更签名重构现在在基类功能被提升为使用泛型的情况下支持泛型。实质上，在下面的情况

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class Base<T> {
    open fun baseMethod<K>(t: T, k: K) {}
}
 
class Derived<X>: Base<List<X>> {
    override fun baseMethod<Y>(a: List<X>, b: Y) {}
}
```

{% raw %}
<p></p>
{% endraw %}

如果<em> Base.baseMethod </em>的签名被更改为<em>派生的签名，那么将其更改为<em> baseMethod＆lt; T＆gt;（t：List＆lt; T＆gt;，k：K？）。碱性方法</em>适当地更改为<em>＆gt; baseMethod＆lt; Y＆gt;（a：List＆lt; Y＆gt;，b：List＆lt; X＆gt;？
### 完成改进

完成项目订购已得到改进，现在突出显示立即成员。智能完成现在可以找到预期类型的​​继承者。完成表现严重改善。
### 可运行的对象

现在，您可以为IDE运行一个声明为<code> [platformStatic] </code>主要功能的对象：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.platform.*
 
object Hello {
    platformStatic fun main(args: Array<String>) {
        println("Hello")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

只需右键单击该对象，然后选择<em>运行... </em>
### 编辑器中的代码覆盖率突出显示

如果您运行Kotlin代码与覆盖，编辑器现在标记覆盖和未覆盖的行（仅适用于IntelliJ IDEA 14）。
### JavaScript项目配置

IDE插件现在可以自动配置Maven项目以使用Kotlin / JS。另外，如果您有一个过时的Kotlin版本的运行时库，IDE会要求您进行更新，现在您可以选择使用插件分发中的库，而不是将其复制到项目中。
## 概要

要安装M10，请更新IntelliJ IDEA 14（或更早版本）中的插件，并且一如以往，您可以在我们的插件库中找到该插件。您也可以从中下载独立的编译器 [发行页面](https://github.com/JetBrains/kotlin/releases/tag/build-0.10.4) 。
