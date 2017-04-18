---
title: "[译]Kotlin M12 is out!"
date: 2015-05-29 16:28:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/05/kotlin-m12-is-out/
---

我们很高兴地介绍Kotlin M12，带来一些相当重要的变化和新功能：

* 注释和枚举的新语法
* 更方便的功能类型语义
* 更好的聪明人
* kapt用于Java注释处理支持
* 多个IDE功能
* 和更多…

## 语言

引入语言和核心库的许多更改都是​​弃用。使用 [“代码清理...”操作](http://blog.jetbrains.com/idea/2014/07/try-intellij-idea-14-eap-138-1283-4-with-code-cleanup-android-studio-beta-features-and-more/)  自动修复项目中的所有警告。
### 注释：新语法

和我们一样 [前面提到过](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-syntax-for-annotations) ，我们决定为未来更有效的使用预留方括号，并使Java用户的注释语法更加熟悉。所以，从M12开始，我们写<code> @Foo（args）</ code>而不是<code> [Foo（args）] </ code>。更多细节可以找到 [这里](http://kotlinlang.org/docs/reference/annotations.html)  （甚至更多 - 在 [规格文件](https://github.com/JetBrains/kotlin/blob/spec-at-based-annotations/spec-docs/at-based-annotation-syntax.md) ）。
请注意，在大多数情况下，<code> @ </ code>不需要</ strong>。通常我们编写注释而不进行任何转义：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Foo // `data` is an annotation
 
```

{% raw %}
<p></p>
{% endraw %}

基于<code> [...] </ code>的旧语法已被弃用</ em>，因此编译器将在您的代码上发出警告。要修复这些警告，请按Alt + Enter并运行快速修复（个人或整个项目）。上述“代码清理...”动作也适用于整个项目。
### 标签语法已更改

由于M12 <code> @name </ code>是一个注释，但它之前有一个含义，即它是一个 [标签](http://kotlinlang.org/docs/reference/returns.html#break-and-continue-labels) 。我们不得不为标签找到一些其他语法，现在他们在最后用<code> @ </ code>声明：

{% raw %}
<p></p>
{% endraw %}

```kotlin
loop@ for (i in 1..100) {
  for (j in 1..100) {
    if (...)
      break@loop
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

所以，<code> loop @ </ code> <em>声明一个标签，<code> break @ loop </ code> <em>使用</ em>。
### 注释中的类文字

在M12之前，Kotlin中的注释被允许使用<code> java.lang.Class </ code>，例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class handledBy(val handlerClass: Class<out Handler>)
 
// Usage
handledBy(javaClass<MyHandler>())
class MyEvent {...}
 
```

{% raw %}
<p></p>
{% endraw %}

现在，在Kotlin注释中不推荐使用Java特定的类，我们需要使用Kotlin自己的模型：<code> kotlin.reflect.KClass </ code>而不是<code> java.lang.Class </ code>和<代码> Foo :: class </ code>而不是<code> javaClass＆Foo＆gt;（）</ code>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class handledBy(val handlerClass: KClass<out Handler>)
 
// Usage
handledBy(MyHandler::class)
class MyEvent {...}
 
```

{% raw %}
<p></p>
{% endraw %}

请注意，Kotlin看到Java注释，就像他们引用<code> KClass </ code>而不是<code> java.lang.Class </ code>一样：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
@interface JavaAnnotation {
    Class<?> value();
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p></p>
{% endraw %}

```kotlin
// Kotlin
 
fun introspect(jann: JavaAnnotation) {
    val theClass = jann.value // the type of this expression is KClass<*>
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

现在，当我们需要将一个<code> KClass </ code>转换成一个<code> java.lang.Class </ code>时，我们可以调用它们的<code> .java </ code>。 <code> Foo :: class.java </ code>或<code> jann.value.java </ code>。
### 注释主要构造函数

我们决定使主构造函数的语法更加规则，现在主构造函数的<em>完整表单</ em>包括<code>构造函数</ code>关键字：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class PrivateConstructor private constructor (val x: Int) {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

只有当我们想要注释</ strong>主要构造函数或添加修饰符时，完整的表单才是<strong>。在大多数情况下，旧的熟悉语法仍然有效：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class MyClass(val x: Int) {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 特征现在是接口

由于我们的特征相当有限，Java的接口几乎相同，所以我们已经弃用了<code> trait </ code>关键字，所以请改用<code> interface </ code>。
像往常一样，快速修复和“清理代码...”将帮助您。
### 枚举类：新语法

的 [枚举的新语法](http://kotlinlang.org/docs/reference/enum-classes.html)  非常接近Java所拥有的。枚举条目现在应以逗号分隔：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Foo {
    A, B, C
}
 
```

{% raw %}
<p></p>
{% endraw %}

现在，当你声明一个<code>枚举</ code>类的成员时，它必须在所有条目之后，在最后一个条目之后必须有一个分号：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class FooWithMember {
    FOO,
    BAR,
    BAZ;
 
    fun doIt() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

最后，当<code>枚举</ code>具有构造函数时，可以通过简单地传递条目名称旁边的参数来调用它：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Color(val rgb: Int) {
  RED(0xFF0000),
  GREEN(0x00FF00),
  BLUE(0x0000FF)
  // no members => semicolon is not needed here
}
 
```

{% raw %}
<p></p>
{% endraw %}

旧的语法已弃用。
### 功能类型改写

我们统一了函数类型和扩展函数类型，所以现在它们通常可以互换使用。例如，我们可以传递<code> String :: length </ code>，其中函数<code>'（String） - > Int'</ code>是预期的。

{% raw %}
<p></p>
{% endraw %}

```kotlin
// map() expects `(String) -> Int`
// argument has type `String.() -> Int`
strings.map(String::length)
 
```

{% raw %}
<p></p>
{% endraw %}

更多细节 [这个帖子](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-function-types-reform) 。
如果您在Java代码中使用Kotlin的函数类（例如<code> kotlin.Function1 </ code>），则需要对其进行调整，因为从现在开始，这些类驻留在<code> kotlin.jvm.function </ code>包。您可以通过运行“清除代码...”来迁移所有Java代码，并使用“Java中使用已弃用的函数类”检查。
### 智能铸造更聪明

一个期待已久的功能：Kotlin现在可以智能铸造本地的<code> var </ code>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo = bar()
 
if (foo != null) {
    foo.baz() // no error here
}
 
```

{% raw %}
<p></p>
{% endraw %}

当然，只有当编译器知道自相关检查后才能进行修改，智能转换只能起作用。请注意，循环通常会使图像失真（由于某些技术原因，我们无法使用完整的数据流分析进行智能转换），因此当循环中的<code> var </ code>被突变时，智能转换可能会不行。
公共和受保护的不可变的<code> val </ code>在同一个模块中的使用也可以被智能铸造：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(public val d: D?)
 
fun foo(c: C) {
    if (c.d != null) {
        c.d.foo() // c.d has been smart-cast here
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 功能表达式支持的内联和非本地返回

 [函数表达式](http://kotlinlang.org/docs/reference/lambdas.html#function-expressions)  现在在M11中推出的内联电话支持：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test(list: List<Foo?>) {
    val mapped = list.map(fun (item) = item?.toString() ?: return@test) // non-local return
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 弃用和丢弃的功能

M12删除以前不推荐的一些功能：

* 类对象被放弃赞成对象;
* 在匿名初始化程序块前面需要init。

一些更多的功能已被弃用：

* 打破和继续在何时;
* 扩展类的接口
* 协变型超类型专业化;
* 静态类型断言。

使用快速修复程序和“清理代码...”来迁移程序。
## Java互操作

### jvmOverloads

Kotlin有默认的参数大大地减少了重载中的需求，但是Java客户端不能直接从这个功能中受益
在M12中，我们添加了一个注释<code> jvmOverloads </ code>，指示编译器为具有N个默认参数的Kotlin函数生成N + 1重载。<br/>
例如，

{% raw %}
<p></p>
{% endraw %}

```kotlin
jvmOverloads fun f(a: String, b: Int = 0, c: String = "abc") {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

会产生

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
void f(String a, int b, String c)
void f(String a, int b)
void f(String a)
 
```

{% raw %}
<p></p>
{% endraw %}

### 源地图进行更好的调试（JSR-45）

由于编译器发出的源映射表生成的类文件，我们现在可以逐步通过内联函数体。
一些技术说明：每个类文件都有分配给说明的行号。对于内联函数体，我们分配行数超出文件的实际结尾（例如，如果文件有50行，内联代码的行号以51开头），这些“虚拟”数字将映射到可能的内联代码的实际来源驻留在其他文件中。标准的JVM调试器可以了解源映射，并可以遍历相应的文件和行。唯一的注意事项是，异常堆栈跟踪可能有时包含超出文件结尾的行号。我们正在寻找解决这个问题的办法。
### Java注释：参数排序

在Java中，注释是接口，它们的参数是这些接口的方法。因此，参数的排序是微不足道的，呼叫站点不能依赖它。这就是为什么Java要求所有的参数，但是一个（命名为<code> value </ code>）的命名。
虽然在Kotlin中声明的注释有适当的构造函数允许定位参数甚至是varargs，但是我们在这方面不能依赖Java注释，所以从现在开始，以下内容适用于Java注释：

* 只有名称值的参数才能被传递而不用名字，
* 只有名为value的参数可以是一个vararg（并且自动变为1，如果它是Java中的数组）
* 所有其他参数不能作为位置传递。

## JavaScript

JavaScript后端正赶上JVM。 M12增加了支持

* 模块之间的内联工作
* 验证参数
* 函数表达式
* 次级施工人员

## 工具

### kapt：注释处理（JSR-269）

如前所述 [这个帖子](http://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/) ，M12为Annotation Processing添加了初始支持，因此现在，像Dagger 2这样的框架与Kotlin配合使用。当前实现的主要限制是Kotlin代码不能引用由注解处理器生成的任何声明（因此，对于Dagger，您需要在Java中至少写入一个小类）。
我们将来会通过为Kotlin编译器发出的类生成存根来解决这个限制。详细信息 [上述职位](http://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/) 。
### Gradle：JUnit支持Android

用于Android的Kotlin Gradle插件现在支持JUnit测试。我们需要做的就是遵循 [Java的标准过程](http://tools.android.com/tech-docs/unit-testing-support#TOC-Setting-up-Android-Studio) ，但现在我们可以在Kotlin写我们的测试。
### 类星体支持

科特林最近的一些变化使我们的生态系统得到了很大的发展：现在 [类星体](http://docs.paralleluniverse.co/quasar/)  提供光纤（轻量级线程），Go-like频道，Erlang类演员和其他异步工具Kotlin！见公告 [这里](http://blog.paralleluniverse.co/2015/05/29/quasar-pulsar-0-7-0/) 。
## 标准API已更改

M12为标准库添加了新功能：

* 新的实用程序在kotlin.io包
* 新的文本实用程序
* 正则表达式API通过JVM和JS统一
* 新的收集工具
* 对于JVM和JS的所有数字类型，MIN_VALUE和MAX_VALUE都可用

当我们在Kotlin标准库上工作时，有些事情会被改变和/或不赞成。使用快速修复程序和“清理代码...”操作来迁移代码。 （请确保已将标准库的源附加到项目中。）
完整的更改列表可用 [这里](https://quip.com/Cy9IAkZtvmjm) 。
## IntelliJ IDEA插件

Kotlin IDE现在支持标准的<strong>引用参数</ strong>重构，将将函数内选择的表达式转换为参数：

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/05/parameter.png?fit=640%2C120&amp;ssl=1"/></p>
{% endraw %}

另外，<strong>引入Lambda参数</ strong>可用于提取一段代码作为函数值：

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/05/lambda.png?fit=640%2C120&amp;ssl=1"/></p>
{% endraw %}

<strong>重命名</ strong>还可以重命名相关声明（变量，子类等）：

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/05/rename.png?fit=640%2C85&amp;ssl=1"/></p>
{% endraw %}

由于我们最近添加了很多弃用资料，IDE现在支持<code> ReplaceWith </ code> quick-fix：对于<code>已弃用的</ code>注释，有一个（可选的）额外的参数，我们可以指定一个表达式替换已弃用的调用：

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/05/replace-with.png?fit=640%2C230&amp;ssl=1"/></p>
{% endraw %}

有一个意图是将<code> ReplaceWith </ code>添加到用户不推荐的声明中。
一些更改：

* 新的调试器功能

评估本地功能的表达式
现场观察点（仅适用于具有后备字段的属性）
* 评估本地功能的表达式
* 现场观察点（仅适用于具有后备字段的属性）
* 更改包意图
* 突出显示出口点的功能
* Gutter标记用于递归调用
* 未使用的接收机参数检查
* 导入的代码样式设置（例如，我们现在可以随时使用'*'导入指定的包）
* Java2Kotlin转换器现在提供更新其他文件的用法
* 当完成列表打开时键入'！'插入否定调用（例如！foo.isEmpty（））
* 改变可见度修饰符的意图操作
* 意图行动现在有更好的可用性
* 当超类“构造函数”具有参数时，可以快速修复从基类添加参数

## 还没有做的事情

我们仍在努力解决我们先前宣布的一些变化 [Java的更安全](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-more-null-safety-for-java/) 。一旦他们准备好就会把它们出来。
## 更多公告来了

在最近的将来会出现一些更多与M12有关的材料。敬请关注！
