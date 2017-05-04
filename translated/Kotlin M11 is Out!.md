---
title: "[译]Kotlin M11 is Out!"
date: 2015-03-19 17:27:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/kotlin-m11-is-out/
translator:
translator_url:
---

今天，我们发布了一个新的里程碑：Kotlin M11，带来了诸如<strong>次要构造器</strong>等久经久待的功能，第一眼就是对Kotlin的真正反映</strong>支持。 <span id =“more-1836”> </span>
## 语言变化

M11带来了不少语言变化，其中有些则是破坏旧的做事方式的改变和/或弃用。您的某些代码可能会中断，但我们已尽力使您的过渡路径尽可能顺利。
### 多个构造函数

Android开发人员最期待这个功能，因为在Android上分类标准视图类需要有多个构造函数。现在你可以这样做：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class MyView : View {
    constructor(context: Context, attrs: AttributeSet, defStyle: Int) : super(context, attrs, defStyle) {
        // ...
    }
 
    constructor(context: Context, attrs: AttributeSet) : this(context, attrs, 0) {}
}
 
```

{% raw %}
<p></p>
{% endraw %}

请参考 [用户文档](http://kotlinlang.org/docs/reference/classes.html#constructors) 和 [规格文件](https://github.com/JetBrains/kotlin/blob/master/spec-docs/secondary-constructors.md) 更多细节。
### 用于初始化程序块的前缀

另一个改变，也与构造函数有关，它是使用软关键字`init`的初始化程序块前缀。<br/>
这种变化的主要原因是，以前使用的语法（在一个类体中表示为初始化程序块的只是花括号）在初始化程序跟随一个属性声明（这是很常见的））时并没有太好的效果：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    val bar = baz() // ERROR here
 
    {
        // pre-M11 initializer
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

对`baz（）`的调用报告了一个错误，因为初始化器看起来像一个传递给它的尾随的lambda。唯一的解决方法是在属性初始化器之后放一个分号，这在Kotlin看起来很不自然。所以，由于M11，我们在初始化程序块之前需要使用`init`：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    val bar = baz()
 
    init {
        // initializer
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

旧的语法<strong>已弃用</strong>，即您会收到警告，而不是错误。此外，IDE提供了一个Alt + Enter快速修复操作，将旧的语法转换为新的语法，可以批量更新整个项目。
看到 [用户文档](http://kotlinlang.org/docs/reference/classes.html#constructors) 更多细节。
### 伴随对象（类对象重新定位）

大家可能知道，Kotlin类没有静态成员。相反，可能会有一个与类关联的特殊单例`对象`，我们用来调用“class object”＆dash;一个相当不幸的术语。所以，我们有点重新设计了这个概念， [与你的帮助](http://blog.jetbrains.com/kotlin/2015/03/follw-up-new-class-object-syntax/) ，为其选择另一个名称：<strong>伴侣对象</strong>。
不幸的措辞不是这种变化的唯一原因。事实上，我们重新设计了这个概念，使其与普通物体更为统一。
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

由于M11可以使用`companion`修饰符声明其中一个对象，这意味着可以通过类名直接访问其成员：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    companion object Obj2 { ... }
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

访问`Obj1`的成员需要资格：`KotlinClass.Obj1.foo（）`。对于`Obj2`的成员，对象名称是可选的：`KotlinClass.foo（）`。
最后一步：可以省略<em>协同对象</em>的名称（在这种情况下，编译器将使用默认名称`Companion`）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    companion object { ... }
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

现在，您仍然可以通过包含类的名称来引用其成员：`KotlinClass.foo（）`，或通过完整的资格：`KotlinClass.Companion.foo（）`。
正如你所看到的，与我们以前使用的</em>类对象</em>不同，伴随对象</em>与普通对象完全一致。
另一个重要的好处是，现在每个对象<em>都有一个名字</em>（当省略一个<em>协同对象</em>的名称时，再次使用`Companion`），启用协同对象<strong>书写扩展功能</strong>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun KotlinClass.Companion.bar() { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

请参阅用户文档 [这里](http://kotlinlang.org/docs/reference/object-declarations.html#companion-objects) 。
### 函数表达式

Kotlin具有更高阶的功能，这意味着你可以传递一个函数作为一个值。在M11之前，有两种获取这些值的方法：lambda表达式（例如`{x  - ＆gt; x + 1}`）和可调用引用（例如`MyClass :: myFun`） 。 M11引入了一个新的，如果你想到的话，这是非常合乎逻辑的：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val f = fun (x: Int): Int { return x + 1 }
 
```

{% raw %}
<p></p>
{% endraw %}

因此，您可以使用其传统句法形式的函数作为值。看到 [用户文档](http://kotlinlang.org/docs/reference/lambdas.html#function-expressions) 和 [规格文件](https://github.com/JetBrains/kotlin/blob/master/spec-docs/multi-declarations-in-parameters.md#function-expressions) 更多细节。
### Lambda语法限制（用于未来浓缩）

除其他功能外，函数表达式使我们能够在lambdas的参数中支持<em>多声明</em>。最终目标（尚未实现）是能够以下列语法过滤列表：

{% raw %}
<p></p>
{% endraw %}

```kotlin
pairs.filter { (a, b) -> a != b }
 
```

{% raw %}
<p></p>
{% endraw %}

这里，`（a，b）`是一个 [多声明](http://kotlinlang.org/docs/reference/multi-declarations.html) ，即`a`获取每个`Pair`对象的第一个组件，并且`b`获得第二个组件。目前，不支持多声明，但是我们不推荐使用lambdas的一些语法形式将其放在M12中，并使多声明语法成为可能。
什么是不推荐的：

* 指定羔羊的返回类型，例如{（a：Int）：Int  - > a + 1}
* 指定lambdas的接收器类型：{Int。（a：Int） - > this + a}
* 对于lambdas参数名称使用括号：{（a，b） - > a + b}

每当你真的需要其中之一时，请切换到使用函数表达式。
IDE提供了快速修复，自动迁移代码。
### Lambdas的标签退货

长久以来，在lambdas中使用`return`表达式有一个限制：只有当lambda具有显式的返回类型时才允许使用<em> local </em> `return`指定。这是由类型推理算法的限制引起的。现在，限制被删除，我们可以自由地使用本地退货：

{% raw %}
<p></p>
{% endraw %}

```kotlin
list.map {
    if (it < 10) return@map DEFAULT
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 导入语义已更改

导入是IDE用户最不可见的语言功能之一，但它对工具的工作方式以及用户偶尔也有很大的影响。
在M11中，我们将* -imports（也称为“按需导入”）的顺序不重要，并进行了一些其他调整，使我们能够在IDE中实现对导入指令的高效自动管理。
## 反射

实现Kotlin特定的反射（而不是让您在Kotlin类上使用Java反射）是一个长期运行的项目，需要在编译器中进行大量的工作。基本上，我们必须考虑到大部分的编译器，并将其作为运行时的一部分。这包括：从二进制文件中加载Kotlin特定的元数据，将Kotlin符号表示为对象（历史上我们称之为<em>描述符</em>），将Java声明加载为Kotlin（因为Kotlin反射也适用于Java对象）等等。
最后，我们介绍这项工作的第一个结果：通过编译器附带的一个新的kotlin-reflection.jar提供内省属性的能力（即将添加更多的功能）。
### 新反思罐

我们分开运送`kotlin-reflect.jar`（不是`kotlin-runtime.jar`的一部分），因为它现在相当大：大约1.8MB。我们将考虑缩小其大小，但可能总是相当可观，因此让每个人总是运用它的应用程序不是一个选择（特别是对于Android开发人员）。
因此，如果您使用属性文字（`:: propertyName`），则可能需要将此jar添加到类路径中。如果没有，M11编译器会产生错误，但稍后这个要求将会放宽。 IDE将为您提供一个快速修复操作，将jar自动添加到您的项目中。
### 班级文字

要获取Kotlin中的类的反射对象，请使用以下语法：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val c = MyClass::class
 
```

{% raw %}
<p></p>
{% endraw %}

你可以得到一个`KClass＆lt; MyClass＆gt;`的例子。得到它的属性。
看到更多的 [用户文档](http://kotlinlang.org/docs/reference/reflection.html#class-references) 。
### 与Java Reflection API的兼容性

Kotlin反射API适用于Kotlin和Java类，您可以从Kotlin“转换”为Java反射对象并返回。例如，您可以说`kClass.java`并获取一个`java.lang.Class`实例，反之亦然：`jlClass.kotlin`给你一个`KClass`实例。
## @Nullable和@NotNull在Java

和往常一样，Java互操作是我们的首要任务，这一次我们正在改进我们发货的<em>平台类型</em>功能 [M9](http://blog.jetbrains.com/kotlin/2014/10/m9-is-here/) ：现在，编译器发出警告滥用Java值注释为`@Nullable`和`@NotNull`。这并不像以前在M9之前那样严格，但是也不会像往常一样破裂。
下一步是以安全的方式发布Java可空性错误（从而总是可以合理地修复错误），这是为下一个里程碑计划的。
## Android扩展

Android用户的好消息：M11带来了一个有用的扩展，使得Kotlin中的Android开发更容易。
我们都知道`findViewById（）`。这是一个臭名昭着的错误和不愉快的代码，很难阅读和支持。在Java中，解决这个问题的方法是通过库来实现 [牛油刀](http://jakewharton.github.io/butterknife/) 和 [AndroidAnnotations](http://androidannotations.org) ，依靠 [JSR 269](https://jcp.org/aboutJava/communityprocess/mrel/jsr269/index2.html) ，但它是一个`javac`特定的API，并且在Kotlin（尚）中不支持。
自从M11以来，Kotlin有自己的解决方案`findViewById（）`问题，这不需要JSR 269：Kotlin编译器的新的`kotlin-android-extensions`插件允许你使用<strong>零</strong>额外的用户代码（无注释或其他类似的东西）和<strong>不需要运行时库</strong>，以类型安全的方式访问视图。
要使用此扩展，您需要在Gradle构建中启用它，并在IDE中安装扩展插件。查看更多 [这里](http://kotlinlang.org/docs/tutorials/android-plugin.html) 。
## IntelliJ IDEA支持

IntelliJ IDEA的更多改进和功能
### 重构和意图

以下重构和意图现已可用：

* 介绍物业
能够引入属性并定义是否需要初始化程序，getter或lazy属性
* 使用Java Interop创建
现在可以在Kotlin文件中使用的Java类型上调用“从使用创建”。
* 接收机到参数转换
变更签名重构的特殊情况，从而可以将参数重构为接收器，从而允许
将接收到类型T的参数的函数转换为T的扩展函数。它还允许相反，从而可以将接收器转换为参数。

