---
title: Kotlin 1.2 Beta is out
author: Roman Belov
date: 2017-09-29 13:51:00
source_url: https://blog.jetbrains.com/kotlin/2017/09/kotlin-1-2-beta-is-out/
tags: 
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/09/kotlin-1-2-beta-is-out/
translator: pye52 & 黄志强
translator_url: https://pye52.github.io/ & https://suima0v0.github.io/
---

我们很高兴地发布Kotlin 1.2的Beta版本。借此发布，我们将揭示Kotlin 1.2的主要新特性——**跨平台项目**的实验性支持。此外，Kotlin native和标准库功能也**开发完毕** - 所有计划于Kotlin 1.2实现的新功能都已完备。现在正是你们**反馈新改动**的绝佳时期 - 因为我们仍然有时间对反馈加以考虑并调整1.2终版的设计。

在工具方面，Kotlin 1.2 Beta包含了与最近发布的[1.1.50](https://github.com/enbandari/KotlinBlogTranslation/blob/master/translated/Kotlin%201.1.50%20is%20out.md)更新相同的一系列特性。该测试版兼容从2016.3至2017.3的所有IntelliJ IDEA版本以及Android Studio 2.3与3.0。

从1.2-M2开始，所有的更新日志都可以在[这里](https://github.com/JetBrains/kotlin/blob/1.2-Beta/ChangeLog.md)找到。以下是重大改动：<img alt="12beta" class="alignnone size-full wp-image-5314" height="750" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/09/12beta.png" width="1500"/>

# 跨平台项目

跨平台项目是Kotlin 1.2的一个新的**实验性**功能，允许你在Kotlin支持的目标平台复用代码-JVM，JavaScript以及(未来会支持的)Native。在跨平台项目中，你提交的平台间的通用代码将放入通用模块，连同平台相关的部分一并放入依赖于平台的特定模块中。当您为一个特定的平台编译项目，公用部分和平台特定部分的代码都会生成出来。

跨平台项目所支持的一个关键特性是通过**预期和实际的声明**来表现通用代码与平台特定部分的依赖关系。预期声明定义API（类，接口，注释，顶层声明等）。实际声明则是该API在平台相依的实现，或是在外部库中引用现有实现的typealias：

```kotlin
// Common code
expect fun hello(world: String)
 
expect class URL(spec: String) {
  open fun getHost(): String
  open fun getPath(): String
}
 
// JVM code
actual fun hello(world: String) {
  println("Hello JVM $world")
}
 
actual typealias URL = java.net.URL
 
```

若想得到更多跨平台项目的信息，请查看此[文档](http://kotlinlang.org/docs/reference/multiplatform.html)。

如果你在发布之前就已经尝试了该功能，也请注意及时更新您的项目：`header`和`impl`关键字已重命名为`expect`和`actual`。若想代码自动更新，请使用IntelliJ IDEA中的Analyze | Cleanup Code。

# 语言和编译器

## 注释中的数组字面值

Kotlin 1.2有一个新的语言特性：对**注释中文字常量数组**的支持。现在，不需要类似`@CacheConfig(cacheNames = arrayOf("books", "default"))`这样的写法了，你只需要这样简单地表示：

`@CacheConfig(cacheNames = ["books", "default"])`

其实早在Kotlin 1.2之前的里程碑版本中你已经可以这样做了。但在1.2 Beta中，我们更加统一了语法并允许使用常量数组和`可变`参数：

`@RequestMapping(value = ["value1", "value2"], path = ["path1", "path2"])`

为了实现这种改动，我们决定对常规方法调用和注释中，使用命名参数和可变参数的语法做一些调整。你可能会感到惊讶，因为在Kotlin 1.1中，当使用命名参数语法调用`可变参数`方法时，可以传递单个参数作为一个立即值：

```kotlin
fun foo(vararg strs: String) { ... }
 
foo(strs = "abc")
 
```

这样将`"abc"`赋值于`strs`是不太恰当的，这导致我们在将整个数组作为命名参数传递时得使用展开运算符：

`foo(strs = *arr)`

我们很想可以写成`foo(strs = arr)`，但考虑到兼容性，它需要一个逐步迁移的过程，所以在1.2版本里面，我们弃用了`foo(strs = "abc")`这样的写法。取而代之的是（这种用法应该很少见到），你可以使用展开和`arrayOf`方法：

`foo(x = *arrayOf("abc"))`

我们计划实现一个[编译器优化方案](https://youtrack.jetbrains.com/issue/KT-20462)来消除在这样的调用下对于数组的分配与复制。

由于注释是一个更受限制的上下文，所以我们可以跳过一步迁移，那样你就可以简单地把值放入一个字面值数组，而不需要扩展运算符：

```kotlin
annotation class Foo(vararg value: String)
 
@Foo(value = "a") // deprecated
@Foo(value = ["a"]) // correct
 
```

在[You Track issue](https://youtrack.jetbrains.com/issue/KT-20171)可以看到更多相关信息。
## lateinit改进

我们添加了一个新的反射API，这允许您检查一个`lateinit`变量是否已被初始化：

```kotlin
lateinit var file: File
 
// ...
 
if (::file.isInitialized) {
  ...
}
 
```

这是[该KEEP提议](https://github.com/Kotlin/KEEP/pull/73/files)的一部分实现，剩下的部分（`析构`的方法）则暂时推迟到1.3。

此外，`lateinit`修饰符现在可以用在[全局属性](https://youtrack.jetbrains.com/issue/KT-15461)和[局部变量](https://youtrack.jetbrains.com/issue/KT-14138)上了。举个例子，当你初始化一个对象图，在图中对象的属性之间有一个循环依赖关系的时候（比如，当lambda作为一个构造函数的参数让一个对象引用另一个对象的时候，必须在传递之后才定义），局部变量便可以使用了：

```kotlin
fun test() {
  lateinit var x: Component
 
  // inject takes a lambda which must return the Component though
  val injector = inject(
    ...,
    componentProvider = { x },
    ...
  )
 
  // Initialization is only possible via injector, once it has been run
  x = injector.createComponent()
}
 
```

更多详细信息，请查看[KEEP](https://github.com/Kotlin/KEEP/blob/master/proposals/local-and-top-level-lateinit-vars.md)。
## 绑定方法引用的改进

现在，你可以把类似`this::foo`这样的引用方法中的`this` 省略掉，直接写成`::foo`。在之前只有全局引用的时候才能省略。更多信息，请查看[YouTrack issue](https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-15667)。

## 类型推断的改进

Kotlin编译器现在可以使用类型推断中的类型转换信息。当调用了一个返回`T`且转换为特定类型`Foo`的泛型方法，编译器现在可以知道这个泛型绑定的是`Foo`类型。这对于Android开发人员十分重要，因为编译器在Android API26中可以正确分析`findViewById`了：

`val button = findViewById（R.id.button）as Button`

由于该方法已被改为`<T extends View> T findViewById(int id)`，因此Kotlin 1.1已不支持在这种调用中推断`T`类型参数。更多信息，请查看[YouTrack issue](https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-13644)。

## 警告视为错误

现在编译器提供了一个将所有警告视为错误的选项。在命令行或下面的Gradle代码片段中使用`-Werror`：

```kotlin
compileKotlin {
  kotlinOptions.warningsAsErrors = true
}
 
```

## Smart cast的改进

Smart cast现在能用在[subjects of safe casts](https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-4565)了：

```kotlin
fun foo(x: Foo?) {
  val b = (x as? SubClass)?.subclassMethod1()
  if (b != null) {
    x.subclassMethod2() // x is smart cast to SubClass
  }
}
 
```

另外，以前只允许在lambda之前修改的的`var`变量[现在能](https://youtrack.jetbrains.com/issue/KT-14486)在其中执行Smart cast了：

```kotlin
var x: String? = null
if (flag) x = "Yahoo!"
 
run {
  if (x != null) {
    println(x.length) // x is smart cast to String
  }
}
 
```

## 枚举中的嵌套类

枚举内的嵌套类现在已经被[弃用](https://youtrack.jetbrains.com/issue/KT-16310)；解决方案为将class标记为inner。
# 标准库

## 分包的兼容性

Kotlin标准库现在完全兼容Java 9的模块系统，Java 9禁止分包（多个jar文件在同一个包中声明类）。为了支持分包，我们创建了新的`kotlin-stdlib-jdk7`和`kotlin-stdlib-jdk8`，取代了旧的`kotlin-stdlib-jre7`和`kotlin-stdlib-jre8`。其中的声明在kotlin的同名包下是可见的，但是由于我们对编译器添加了黑魔法，这在Java的不同名包下也是可见的。因此，这种切换不需要对源代码进行任何更改。

为确保与新模块系统的兼容性，我们做出的另一个改动是从`kotlin-reflect`库中移除`kotlin.reflect`包中已经弃用的声明。这些声明需要在`kotlin.reflect.full`包中使用，这在Kotlin 1.1中就已经支持了。

## kotlin.math

`kotlin.math`是Kotlin 1.2标准库中的一个新包，允许您在跨平台代码中执行数学运算。在1.2-Beta中，我们对它进行了一些改进：

* 现在支持反双曲函数（asinh，acosh，atanh）
* 在[1.2-M2](https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-2-m2-is-out/)中添加的浮点数二进制表示（toBits，nextUp等）相关的函数现在可用于JavaScript
* 对JavaScript中polyfills精确度的改进

# 发布前的注意事项

*与其他里程碑版本一样，我们对新语言和库的相关功能**不保证向后兼容性**。在1.2的里程碑版本中引入的任何内容在1.2终版之前**可能会发生变化**。一旦RC版确定，在此之前版本的编译文件将被编译器清理，你需要重新编译1.2-Mx或1.2-Beta所编译过的文件。*

*但是，这不会影响由1.1.x和之前release版本编译的代码。*

# 如何更新

**通过Maven / Gradle**：在构建脚本和项目仓库中添加`http://dl.bintray.com/kotlin/kotlin-eap-1.2`；使用`1.2.0-beta-31`作为编译器插件和标准库的版本号。

**通过IntelliJ IDEA**：*工具→Kotlin→配置Kotlin插件更新*，在更新下拉列表中选择“Early Access Preview 1.2”，然后点击*检查更新*。命令行编译器可以从[GitHub release page](https://github.com/JetBrains/kotlin/releases/tag/v1.2-beta)下载。

**通过[try.kotlinlang.org](https://try.kotlinlang.org/)**：使用右下角的下拉列表将编译器版本更改为1.2（即将实现）。