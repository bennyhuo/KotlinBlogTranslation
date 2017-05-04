---
title: "[译]Kotlin 1.1-M04 is here!"
date: 2016-12-21 00:12:00
author: Ilya Chernikov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/12/kotlin-1-1-m04-is-here/
translator:
translator_url:
---

我们很高兴向您呈现即将推出的 Kotlin 发行版的第四个里程碑。我们正在封装版本 1.1 的开发，最终版本计划于 2017 年第一季度进行。大多数功能已经形成了体面，所以现在是尝试它的好时机，并给我们您的反馈。我们会很感激！
与其他里程碑版本一样，我们为新语言和库功能提供**无后向兼容性保证**。在 1.1 版本的里程碑版本中引入的任何内容都将在最终 1.1 版本之前更改**。
请分享您关于新功能或您可能遇到的任何问题的反馈，通过此版本 [YouTrack](https://youtrack.jetbrains.com/issues/KT) ， [论坛](https://discuss.kotlinlang.org) 和 [松弛](http://kotlinlang.slack.com/) 。
这一里程碑对协同语法和语义进行了重大改造，使协同工作更加简单和灵活。它还包含标准库增强功能，新语言功能和编译器插件，JS 后端的许多功能和改进，以及许多其他修补程序和更新。<br/>

新版本还包括所有功能 [Kotlin 1.0.6](https://discuss.kotlinlang.org/t/kotlin-1-0-6-eap/2117/10) ，包括与**Android Studio 2.3 Beta 1**兼容的更新。
完整的更新日志可用 [这里](https://github.com/JetBrains/kotlin/blob/1.1-M04/ChangeLog.md) 以下列出了一些关键变化：
<span id =“more-4405”> </span>
## 协调程序

我们重新思考了协同设计，使其更简单，可组合和更强大：

* 所有挂起和协同构建器的功能现在都具有直观的签名（没有更奇怪的变化要记住）。
* 暂停功能只有一种基本语言概念和相应的挂起功能类型。特殊的协同关键字已被删除。协调程序现在只是一个可暂停计算的实例，它使用标准库中的 startCoroutine 函数启动。
* 复杂的挂起功能可以由更原始的挂起功能组成。在这个版本中，他们可以拖尾调用其他暂停功能，但这个限制在将来会被解除。
* 可以定义挂起的函数来包装任何回调式 API，并且可以在任何异步协同程序中自由使用。控制器不再需要了。使用 @RestrictsSuspension 注解，生成和生成对，构建同步序列限制了生成块内的悬架。
* 现在实现协同程序的类型推断。您可以在大多数用例中省略类似的协同程序构建器，并且类型将自动推断。

经典的`await`暂停功能现在可以通过尾部调用到标准库的一部分的`suspendCoroutine`挂起函数来实现：

{% raw %}
<p></p>
{% endraw %}

```kotlin
suspend fun <T> await(f: CompletableFuture<T>): T =
    suspendCoroutine<T> { c: Continuation<T> ->
        f.whenComplete { result, exception ->
            if (exception == null) // the future has been completed successfully
                c.resume(result)
            else // the future has been completed with an exception
                c.resumeWithException(exception)
        }
    }
```

{% raw %}
<p></p>
{% endraw %}

相应的构建器称为`async`，并通过`startCoroutine`函数实现：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> async(block: suspend () -> T): CompletableFuture<T> {
    val future = CompletableFuture<T>()
    block.startCoroutine(completion = object : Continuation<T> {
        override fun resume(value: T) {
            future.complete(value)
        }
        override fun resumeWithException(exception: Throwable) {
            future.completeExceptionally(exception)
        }
    })
    return future
}
```

{% raw %}
<p></p>
{% endraw %}

他们可以一起使用来编写一个更自然的代码与期货：

{% raw %}
<p></p>
{% endraw %}

```kotlin
async {
    val original = asyncLoadImage("...original...") // creates a Future
    val overlay = asyncLoadImage("...overlay...")   // creates a Future
    ...
    // suspend while awaiting the loading of the images
    // then run `applyOverlay(...)` when they are both loaded
    return applyOverlay(original.await(), overlay.await())
}
```

{% raw %}
<p></p>
{% endraw %}

然而，期货只是协同程序支持的多种用例之一。协调实现的完整概述及其使用示例可在修订版中获得 [KEEP 文件](https://github.com/Kotlin/kotlin-coroutines/blob/master/kotlin-coroutines-informal.md) 。
我们认为现在我们已经有了一个很棒的 Kotlin 协同设计，但是我们意识到它还没有经过足够的测试。因此，我们将在 1.1 中发布选择性孵化标志。从这个里程碑开始，您将在使用协同程序时获得“此功能是实验性的：协同程序”警告。您可以使用`-Xcoroutines = enable`编译器标志关闭此警告，或者使用`-Xcoroutines = error`编译器标志禁用此功能。相应的设置也可以在 IDEA 中的 Kotlin 编译器设置下使用。要为 gradle 项目设置此选项，您可以在项目根目录中添加`kotlin.coroutines = enable`或`kotlin.coroutines = error`到 local.properties 文件。
如果你正在使用 [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) 图书馆请使用更新版本`0.2-alpha-1`，适应协同设计的最新更改。此版本还在生成范围中引入了`yieldAll`方法。请看 [自述文件](https://github.com/Kotlin/kotlinx.coroutines/blob/master/README.md) 详细信息。
## 语言功能

### 属性类型可以从吸气剂推断出来

例如在下面的代码中，属性`foo`的类型将被推断为`String`。看到这个问题 [KT-550](https://youtrack.jetbrains.com/issue/KT-550) 更多的细节。

{% raw %}
<p></p>
{% endraw %}

```kotlin
val foo get() = ""
```

{% raw %}
<p></p>
{% endraw %}

### 浮点相关功能，修复和改进

浮点数比较现在使用 IEEE 754 兼容比较，其中类型是静态地被认为是`Double`或`Float`。对于浮点数范围，我们引入了专门的`ClosedFloatingPointRange`接口，它提供了自己的比较方法，因此使用范围的扩展操作（如`coerceIn`）可以在上面实现的。它的实例是通过在两个`Float`或`Double`值上调用的运算符`..`获得的。看到 [KT-4481](https://youtrack.jetbrains.com/issue/KT-4481) 和 [KT-14651 了解详情。](https://youtrack.jetbrains.com/issue/KT-14651) <br/>
### 
拦截委托属性绑定

现在可以使用`provideDelegate`运算符拦截代理到属性绑定

例如，如果我们要在绑定之前检查属性名称，我们可以这样写：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class ResourceLoader<T>(id: ResourceID<T>) {
    operator fun provideDelegate(thisRef: MyUI, property: KProperty<*>): ReadOnlyProperty<MyUI, T> {
        checkProperty(thisRef, property.name)
        ... // property creation
    }
 
    private fun checkProperty(thisRef: MyUI, name: String) { ... }
}
 
fun <T> bindResource(id: ResourceID<T>): ResourceLoader<T> { ... }
 
class MyUI {
    val image by bindResource(ResourceID.image_id)
    val text by bindResource(ResourceID.text_id)
}
```

{% raw %}
<p></p>
{% endraw %}

这里在`MyUI`的构造函数初始化器中调用方法`provideDelegate`。因此，我们可以在创建时检查物业一致性。早期这种检查只能在呼吸吸气器或吸气器的时候才可以。
不幸的是，该功能尚未正确记录，但可以使用 [本草案文件](https://github.com/orangy/KEEP/blob/fabb56360f2d7a293ac720cace89cd445da3c919/proposals/attach-to-property.md#createdelegate) 作为初始参考。
### 增强了一些 JDK 方法的可空性

JDK 中的一些功能在文档中定义了可空性契约，有些功能不接受 null 值，有些不会返回 null，而其他函数可能会有时返回 null。

不幸的是，JDK 没有使用任何注释来表达这样的合同，并且仅在文档中陈述它们。在 1.0 之前，我们为 JDK 使用了外部注释工件，可以将其提供给编译器来更改 JDK 函数的签名，但是这种方法不够可靠。
现在我们将介绍另一种方法：将所需的信息嵌入到将 JDK 签名直接增加到编译器中。作为第一步，我们涵盖了 API 的一小部分的无效性：

* java.util.Optional 工厂和成员函数：
* of：不允许空值
ofNullable，它需要一个可空值，并返回一个可选的不可空类型。
总是返回不可为空的值。
* of：不允许空值
* ofNullable，它需要一个可空值，并返回一个可选的不可空类型。
* 总是返回不可为空的值。
* java.lang.ref.Reference 及其所有继承者，如 WeakReference 和 SoftReference：
* get 返回一个可空值，因为如果引用的对象被垃圾回收，它可以随时变为 null。
* get 返回一个可空值，因为如果引用的对象被垃圾回收，它可以随时变为 null。
* JDK 的 Iterator，Iterable，Collection，List，Map 的默认方法作为 Kotlin 内置集合接口的平台相关功能而被公开。
* java 功能类型，当它们使用非平台类型构建时，它们在调用方法中具有非平台类型。

在大多数情况下，这些增强功能是安全的。特别地，当增强型在返回位置变得更具体（不可为空）或参数位置更一般（可空）时，它们是安全的。但是当类型改变方向相反时，更改将会被打破

我们努力不引入这种突破性增强，除非不尊重正确的可空性将导致运行时出现异常。所以例如`Optional.of`现在采用一个非限制性的参数，它的限制性更大，但试图将`null`传递给该方法会导致异常。 >

另一方面，我们决定不为`File.listFiles`指定正确的可空性，实际上可以有时返回 null，因为在大多数情况下，除了抛出另一个异常之外，没有有意义的回退。
### 其他变化


* 现在可以使用 @PublishedApi 注释来解决公共内部函数使用非公开成员的问题。当它应用于内部成员时，它变得有效地公开，可以从公共内联函数中调用。有关详细信息，请参见 KT-12215。
* 现在在通话网站内嵌了 const val（见 KT-11734）
* SAM 转换现在与正常成员重载分辨率相同。这修复了 KT-11128 和一样。
* 我们认为我们选择的 mod 名称为％（余数）运算符是一个错误，有一些不太好的后果（参见例如 KT-14650）。因此，我们决定引入 rem 操作符，弃用该模块并提供所有工具使此过渡顺利。

## 标准库

### 字符串到数字转换

在`String`类中有一堆新的扩展，将其转换为一个数字，而不会在无效数字上抛出异常：`String.toIntOrNull（）：Int？`，<code > String.toDoubleOrNull（）：Double？`等

请注意，这些函数将在返回它们之前输入结果数字，因为返回类型假定它。
还有整数转换函数，如`Int.toString（）`，`String.toInt（）`，`String.toIntOrNull（）` `radix`参数，它允许指定转换的基础。
我们要感谢 [丹尼尔·沃多皮](https://github.com/voddan) 为实现这些功能的发展作出了重大贡献。
### 在各个

`onEach`是用于集合和序列的小而有用的扩展函数，它允许在操作链中的集合/序列的每个元素上执行一些可能具有副作用的操作。 />

对于迭代，它的行为类似于`forEach`，而且还可以进一步返回迭代实例。在序列上，它返回一个包装序列，它在元素被迭代时懒惰地应用给定的动作。
谢谢 [ChristianBrüggemann](https://github.com/cbruegg) 为初始原型。
## JavaScript 后端

### `external`，而不是`@native`

从这个里程碑开始，`@native`注释已经弃用了，而你必须使用`external`修饰符。<br/>

与 JVM 目标不同，JS 一个允许使用带有类和属性的`external`修饰符

请注意，您不需要将`external`类的成员标记为`external`：此修饰符

由成员自动继承。所以，而不是

{% raw %}
<p></p>
{% endraw %}

```kotlin
@native fun alert(message: Any?): Unit {}
```

{% raw %}
<p></p>
{% endraw %}

你可以写

{% raw %}
<p></p>
{% endraw %}

```kotlin
external fun alert(message: Any?)
```

{% raw %}
<p></p>
{% endraw %}

### 改进了进口处理

您现在可以更精确地描述应该从 JavaScript 模块导入的声明

如果您在外部声明中添加了`@JsModule（“＆lt; module-name＆gt;”）`注释，则在编译期间将其正确导入到模块系统（CommonJS 或 AMD）。例如，使用 CommonJS，声明将通过`require（...）`函数导入

另外，如果要将声明作为模块或全局 JavaScript 对象导入，可以使用`@JsNonModule`注释
让我们看看下面的完整例子。您可以将 jQuery 库导入 Kotlin 源文件，如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@JsModule("jquery")
@JsNonModule
@JsName("$")
external abstract class JQuery {
    fun toggle(duration: Int = 0): JQuery
    fun click(handler: (Event) -> Unit): JQuery
}
 
@JsModule("jquery")
@JsNonModule
@JsName("$")
external fun JQuery(selector: String): JQuery
```

{% raw %}
<p></p>
{% endraw %}

在这种情况下，JQuery 将被导入为一个名为`jquery`的模块，或者可以用作`$` -object，具体取决于 Kotlin 编译器被配置为使用。
您可以在应用程序中使用这些声明，如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun main(args: Array<String>) {
    JQuery(".toggle-button").click {
        JQuery(".toggle-panel").toggle(300)
    }
}
```

{% raw %}
<p></p>
{% endraw %}

您可以为 CommonJS 和“plain”模块系统检查此代码段生成的 JS 代码 [这里](https://gist.github.com/ligee/50d30ad9bca5ea925ff7d913ff232004) 。
## 如何尝试

**在 Maven / Gradle 中：**添加 [http://dl.bintray.com/kotlin/kotlin-eap-1.1](http://dl.bintray.com/kotlin/kotlin-eap-1.1) 作为构建脚本和项目的存储库;使用 1.1-M04 作为编译器和标准库的版本号。
**在 IntelliJ IDEA 中：**转到<i>工具→Kotlin→配置 Kotlin 插件更新</i>，然后在<i>更新频道</i>下拉列表中选择“早期访问预览 1.1”下拉列表，然后按<i>检查更新</i>。
**命令行编译器**可以从中下载 [Github 发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1-M04) 。
**<a href="http://try.kotlinlang.org"> try.kotlinlang.org </a>**。使用右下角的下拉列表将编译器版本更改为 1.1-M04。
快乐 Kotlin！
