---
title: [译]Kotlin 1.1-M04 is here!
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
---

我们很高兴向您呈现即将推出的Kotlin发行版的第四个里程碑。我们正在封装版本1.1的开发，最终版本计划于2017年第一季度进行。大多数功能已经形成了体面，所以现在是尝试它的好时机，并给我们您的反馈。我们会很感激！
与其他里程碑版本一样，我们不会为新语言和库功能提供向后兼容性保证。在1.1版本的里程碑版本中引入的任何内容都将在最终1.1版本之前发生变更。
请通过YouTrack，论坛和Slack，分享您关于新功能的反馈或您可能遇到的任何问题。
这一里程碑对协同语法和语义进行了重大改造，使协同工作更加简单和灵活。它还包含标准库增强功能，新语言功能和编译器插件，JS后端的许多功能和改进，以及许多其他修补程序和更新。
新版本还包括Kotlin 1.0.6中引入的所有功能，包括与Android Studio 2.3 Beta 1兼容的更新。
完整的更改日志可在此处进行，一些重要更改如下所示：
## 协调程序

我们重新思考了协同设计，使其更简单，可组合和更强大：

* 所有挂起和协同构建器的功能现在都具有直观的签名（没有更奇怪的变化要记住）。
* 暂停功能只有一种基本语言概念和相应的挂起功能类型。特殊的协同关键字已被删除。协调程序现在只是一个可暂停计算的实例，它使用标准库中的startCoroutine函数启动。
* 复杂的挂起功能可以由更原始的挂起功能组成。在这个版本中，他们可以拖尾调用其他暂停功能，但这个限制在将来会被解除。
* 可以定义挂起的函数来包装任何回调式API，并且可以在任何异步协同程序中自由使用。控制器不再需要了。使用@RestrictsSuspension注解，生成和生成对，构建同步序列限制了生成块内的悬架。
* 现在实现协同程序的类型推断。您可以在大多数用例中省略类似的协同程序构建器，并且类型将自动推断。

经典等待暂停功能现在可以通过对作为标准库一部分的suspendCoroutine挂起函数的尾调用来实现：

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

相应的构建器称为异步并通过startCoroutine函数实现：

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

然而，期货只是协同程序支持的多种用例之一。修订的KEEP文件中提供了协同实现及其使用示例的全面概述。
我们认为现在我们已经有了一个很棒的Kotlin协同设计，但是我们意识到它还没有经过足够的测试。因此，我们将在1.1中发布选择性孵化标志。从这个里程碑开始，您将在使用协同程序时获得“此功能是实验性的：协同程序”警告。您可以使用-Xcoroutines =启用编译器标志关闭此警告，或者使用-Xcoroutines =错误编译器标志禁用此功能。相应的设置也可以在IDEA中的Kotlin编译器设置下使用。要为gradle项目设置此选项，可以在项目根目录中的local.properties文件中添加kotlin.coroutines = enable或kotlin.coroutines = error。
如果您正在使用kotlinx.coroutines库，请使用更新版本0.2-alpha-1，适应协同设计的最新更改。该版本还在generate范围中引入了yieldAll方法。请参阅自述文件了解更多详细信息。
## 语言功能

### 属性类型可以从吸气剂推断出来

例如在下面的代码中，属性foo的类型将被推断为String。有关详细信息，请参阅KT-550的问题。

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

浮点数比较现在使用IEEE 754兼容比较，其中类型是静态地被称为Double或Float。对于浮点数范围，我们引入了专门的ClosedFloatingPointRange接口，它提供了自己的比较方法，因此可以在其上实现采用范围的扩展操作，如coerceIn。它的实例是通过操作符获得的。调用两个Float或Double值。详见KT-4481和KT-14651。
### 拦截委托属性绑定

现在可以使用provideDelegate运算符拦截委托给属性绑定。
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

这里的方法provideDelegate将在MyUI类的构造函数初始化器中被调用。因此，我们可以在创建时检查物业一致性。早期这种检查只能在呼吸吸气器或吸气器的时候才可以。
不幸的是，该功能尚未正确记录，但您可以将此草案文档用作初始参考。
### 增强了一些JDK方法的可空性

JDK中的一些功能在文档中定义了一个可空性契约，有些功能不接受空值，有些不会返回null，有些则不能返回null。
不幸的是，JDK没有使用任何注释来表达这样的合同，并且仅在文档中陈述它们。在1.0之前，我们为JDK使用了外部注释工件，可以将其提供给编译器来更改JDK函数的签名，但是这种方法不够可靠。
现在我们将介绍另一种方法：将所需的信息嵌入到将JDK签名直接增加到编译器中。作为第一步，我们涵盖了API的一小部分的无效性：

* java.util.Optional工厂和成员函数：

of：不允许空值
ofNullable，它需要一个可空值，并返回一个可选的不可空类型。
总是返回不可为空的值。
* of：不允许空值
* ofNullable，它需要一个可空值，并返回一个可选的不可空类型。
* 总是返回不可为空的值。
* java.lang.ref.Reference及其所有继承者，如WeakReference和SoftReference：

get返回一个可空值，因为如果引用的对象被垃圾回收，它可以随时变为null。
* get返回一个可空值，因为如果引用的对象被垃圾回收，它可以随时变为null。
* JDK的Iterator，Iterable，Collection，List，Map的默认方法作为Kotlin内置集合接口的平台相关功能而被公开。
* java功能类型，当它们使用非平台类型构建时，它们在调用方法中具有非平台类型。

在大多数情况下，这些增强功能是安全的。特别地，当增强型在返回位置变得更具体（不可为空）或参数位置更一般（可空）时，它们是安全的。但是当类型在相反方向发生变化时，更改将会中断。
我们努力不引入这种突破性增强，除非不尊重正确的可空性将导致运行时出现异常。所以例如Optional.of现在使用一个非限制性的参数，这个参数更具限制性，但试图将null传递给该方法会导致异常。
另一方面，我们决定不对File.listFiles指定正确的可空性，实际上可能会有时返回null，因为在大多数情况下，除了抛出另一个异常之外，没有任何有意义的回退。
### 其他变化


* 现在可以使用@PublishedApi注释来解决公共内部函数使用非公开成员的问题。当它应用于内部成员时，它变得有效地公开，可以从公共内联函数中调用。有关详细信息，请参见KT-12215。
* 现在在通话网站内嵌了const val（见KT-11734）
* SAM转换现在与正常成员重载分辨率相同。这修复了KT-11128和一样。
* 我们认为我们选择的mod名称为％（余数）运算符是一个错误，有一些不太好的后果（参见例如KT-14650）。因此，我们决定引入rem操作符，弃用该模块并提供所有工具使此过渡顺利。

## 标准库

### 字符串到数字转换

在String类中有一堆新的扩展将其转换为一个数字，而不会在无效数字上抛出异常：String.toIntOrNull（）：Int？，String.toDoubleOrNull（）：Double？等等
请注意，这些函数将在返回它们之前输入结果数字，因为返回类型假定它。
还有整数转换函数，如Int.toString（），String.toInt（），String.toIntOrNull（），每个都使用radix参数进行重载，这允许指定转换的基础。
我们要感谢Daniil Vodopian对这些功能的发展做出了重大贡献。
### 在各个

onEach是一个小而有用的扩展函数，用于集合和序列，它允许在操作链中的集合/序列的每个元素上执行一些可能具有副作用的操作。
在iterable上，它的行为类似于forEach，但是还可以进一步返回iterable实例。在序列上，它返回一个包装序列，它在元素被迭代时懒惰地应用给定的动作。
感谢ChristianBrüggemann的初始原型。
## JavaScript后端

### 外部而不是@native

从这个里程碑@native注释变为不赞成，而您必须使用外部修饰符。
与JVM目标不同，JS一个允许使用带有类和属性的外部修饰符。
请注意，您不需要将外部类的成员标记为external：this modifier
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

您现在可以更精确地描述应该从JavaScript模块导入的声明。
如果在外部声明中添加了@JsModule（“<module-name>”）注释，那么在编译期间它将被正确导入模块系统（CommonJS或AMD）。例如，使用CommonJS，声明将通过require（...）函数导入。
另外，如果要将声明作为模块或全局JavaScript对象导入，可以使用@JsNonModule注释
让我们看看下面的完整例子。您可以将jQuery库导入Kotlin源文件，如下所示：

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

在这种情况下，JQuery将被导入为名为jquery的模块，或者可以将其用作$ -object，具体取决于Kotlin编译器被配置为使用哪个模块系统。
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

您可以在此处查看CommonJS和“plain”模块系统的生成的JS代码。
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.1作为构建脚本和项目的存储库;使用1.1-M04作为编译器和标准库的版本号。
在IntelliJ IDEA：转到工具→Kotlin→配置Kotlin插件更新，然后在更新频道下拉列表中选择“早期访问预览1.1”，然后按检查更新。
命令行编译器可以从Github发行页面下载。
在try.kotlinlang.org。使用右下角的下拉列表将编译器版本更改为1.1-M04。
快乐Kotlin！
