---
title: Kotlin 1.2 Beta is out
author: Roman Belov
date: 2017-09-29 13:51:00
tags: 
categories:  官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/09/kotlin-1-2-beta-is-out/
translator: pye52 & 睡魔的倦意
translator_url: https://pye52.github.io/ & https://suima0v0.github.io/
---

​	我们很高兴地宣布Kotlin 1.2的Beta版本。我们将于该发布版本揭示Kotlin 1.2的主要新特性——跨平台开发的实验性支持。此外，语言和标准库功能已经完善 - 所有计划于Kotlin 1.2实现的新功能都已完备。是时候将你们的反馈意见告诉我们了，如果需要的话，我们仍然有时间根据反馈去考虑并调整1.2终版的设计。
​	Kotlin 1.2 Beta包含了与最近发布的[1.1.50](https://github.com/enbandari/KotlinBlogTranslation/blob/master/translated/Kotlin%201.1.50%20is%20out.md)更新相同的一系列工具。该测试版兼容2016.3至2017.3的IntelliJ IDEA版本以及Android Studio 2.3和3.0。从1.2-M2开始的完整更新日志可以在[这里](https://github.com/JetBrains/kotlin/blob/1.2-Beta/ChangeLog.md)找到，下面列出的重大更改。

{% raw %}
<p><img alt="12beta" class="alignnone size-full wp-image-5314" height="750" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/09/12beta.png" width="1500"/></p>
{% endraw %}


{% raw %}
<p><span id="more-5287"></span></p>
{% endraw %}

# 多平台项目

​	多平台项目是Kotlin 1.2中一个新的实验性功能，允许您在Kotlin的JVM，JavaScript和未来Native支持的平台中复用代码。在多平台项目中，平台之间的通用代码将放入通用模块中，与平台相关部分放入依赖于平台的特定模块中。当您为特定平台编译这样的项目时，会生成公共平台和平台特定部分的代码。
​	多平台项目支持的一个关键特点是通过预期和实际声明来表现通用代码针对不同平台的依赖关系。预期声明定义API（类，接口，注释，顶层声明等）。实际声明则是该API在平台相关的实现，或者在外部库中引用现有实现的typealias：

{% raw %}
<p></p>
{% endraw %}

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

{% raw %}
<p></p>
{% endraw %}

有关多平台项目的更多信息，请查看[文档](http://kotlinlang.org/docs/reference/multiplatform.html)。
如果您在发布之前已经在尝试该功能，请注意及时更新您的项目：`header`和`impl`关键字已重命名为`expect`和`actual`。要自动更新您的代码，请使用IntelliJ IDEA中的Analyze | Cleanup Code。
# 语言和编译器

## 注释中的数组字面值

​	Kotlin 1.2中语言层面的新功能是对注释中文字常量数组的支持。现在，不需要类似@CacheConfig（cacheNames = arrayOf（“books”，“default”））之类的写法了，你可以简单地使用常量表达式：@CacheConfig（cacheNames = [“books”，“default”]）早在Kotlin 1.2之前的里程碑版本中已经有此功能。但在1.2 Beta中，我们使语法更加一致，并允许使用常量数组和可变参数：@RequestMapping（value = [“value1”，“value2”]，path = [“path1”，“path2”]）
​	为了实现这种改变，我们决定对常规方法调用和注释中使用命名参数和可变参数的语法做一些调整。您可能会感到惊讶，但在Kotlin 1.1中，当使用命名参数语法调用可变参数方法时，可以传递单个参数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(vararg strs: String) { ... }
 
foo(strs = "abc")
 
```

{% raw %}
<p></p>
{% endraw %}

​	将"abc"与"strs"划上等号是不太恰当，而在将整个数组作为命名参数传递时我们得使用展开运算符：`foo（strs = * arr）`。虽然我们很想像`foo（strs = arr）`这样的实现，但为了兼容性，它需要逐步迁移，所以在1.2中，我们弃用了`foo（strs =“abc”）`这样的写法。作为一个替代（这种用法应该很少见到），你可以使用spread运算符和`arrayOf`方法：`foo（x = * arrayOf（“abc”））`
​	我们计划实现一个[编译器优化](https://youtrack.jetbrains.com/issue/KT-20462)来消除在这样的调用下对于数组的分配和拷贝。
​	由于注释是一个更受限制的上下文，所以我们可以跳过一步迁移，所以你可以简单地把值放入一个字面值数组，而不需要扩展运算符：

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class Foo(vararg value: String)
 
@Foo(value = "a") // deprecated
@Foo(value = ["a"]) // correct
 
```

{% raw %}
<p></p>
{% endraw %}

有关更多信息，请参阅[YouTrack](https://youtrack.jetbrains.com/issue/KT-20171)问题。
## lateinit改进

我们添加了一个新的反射API，允许您检查一个lateinit变量是否已经被初始化：

{% raw %}
<p></p>
{% endraw %}

```kotlin
lateinit var file: File
 
// ...
 
if (::file.isInitialized) {
  ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

​	这是该[KEEP提议](https://github.com/Kotlin/KEEP/pull/73/files)的一部分实现。剩下的部分（析构的方法）暂时推迟到1.3。
此外，lateinit修饰符现在可以用[在全局属性](https://youtrack.jetbrains.com/issue/KT-15461)和[局部变量](https://youtrack.jetbrains.com/issue/KT-14138)上。后者可应用于以下的情景，当你初始化一个对象图，并且在图中的对象的属性之间有一个循环依赖关系（例如，作为构造器参数传递给一个对象的lambda引用另一个对象必须在以后定义）：

{% raw %}
<p></p>
{% endraw %}

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

{% raw %}
<p></p>
{% endraw %}

有关更多详细信息，请参阅[KEEP](https://github.com/Kotlin/KEEP/blob/master/proposals/local-and-top-level-lateinit-vars.md)。
## 绑定方法引用的改进

​	你现在可以省略类似于`this::foo`这样方法引用中的`this`，以`::foo`代替。在以前，这种语法只能用于全局的方法引用。有关更多信息，请参阅[YouTrack issue](https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-15667)。
## 类型推断的改进

​	Kotlin编译器现在可以使用类型推断中的类型转换信息。如果调用了返回`T`且转换为特定类型`Foo`的泛型方法，编译器现在可以得知该泛型绑定的是Foo类型。这对于Android开发人员十分重要，因为编译器在Android API26中可以正确分析`findViewById`了：`val button = findViewById（R.id.button）as Button`
​	由于该方法已被改为`<T extends View> T findViewById（int id）`，因此Kotlin 1.1无法在这种调用中推断T的类型参数。有关更多信息，请参阅[YouTrack issue](https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-13644)。
## 警告视为错误

编译器现在提供一个将所有警告视为错误的选项。在命令行或下面的Gradle代码片段中使用-Werror：

{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin {
  kotlinOptions.warningsAsErrors = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Smart cast的改进

Smart cast现在能正确应用于[subjects of safe casts](https://youtrack.jetbrains.com/oauth?state=%2Fissue%2FKT-4565)了：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(x: Foo?) {
  val b = (x as? SubClass)?.subclassMethod1()
  if (b != null) {
    x.subclassMethod2() // x is smart cast to SubClass
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

另外，以前只允许在lambda之前修改的的`var`变量现在能在其中执行Smart cast了：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var x: String? = null
if (flag) x = "Yahoo!"
 
run {
  if (x != null) {
    println(x.length) // x is smart cast to String
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 枚举中的嵌套类

枚举内的嵌套类现在已经被[弃用](https://youtrack.jetbrains.com/issue/KT-16310); 解决方案为将class标记为inner。
# 标准库

## 分包的兼容性

​	Kotlin标准库现在完全兼容Java 9的模块系统，它禁止分包（多个jar文件在同一个包中声明类）。为了支持这一点，我们创建了新的`kotlin-stdlib-jdk7`和`kotlin-stdlib-jdk8`，取代了旧的`kotlin-stdlib-jre7`和`kotlin-stdlib-jre8`。这其中的声明在kotlin相同的包名称下是可见的，但是由于我们对编译器添加的黑魔法，在Java的不同包名下也是可见的。因此，这种切换不需要对源代码进行任何更改。
​	为确保与新模块系统的兼容性，我们做出的另一个更改是从`kotlin-reflect`库中移除`kotlin.reflect`包中已弃用的声明。你需要使用自Kotlin1.1开始在`kotlin.reflect.full`包中的声明来使用它们。
## kotlin.math

`kotlin.math`是Kotlin 1.2标准库中的一个新包，允许您在跨平台代码中执行数学运算。在1.2-Beta中，我们对它进行了一些改进：

* 现在支持反双曲函数（asinh，acosh，atanh）
* 在[1.2-M2](https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-2-m2-is-out/)中添加的与浮点数的二进制表示（toBits，nextUp等）有关的函数现在可用于JavaScript
* 对JavaScript中polyfills的精确度的改进

# 发布前的注意事项

​	与其他里程碑版本一样，我们不保证新语言和库相关功能向后兼容性。在1.2的里程碑版本中引入的任何内容在1.2终版之前可能会发生变化。一旦RC版已确定，则在此之前版本的编译文件将被编译器清理，你需要重新编译1.2-Mx或1.2-Beta所编译过的文件。
​	但是，这不会影响由1.1.x和之前release版本编译的代码。
# 如何尝鲜

​	在Maven / Gradle中：在构建脚本和项目仓库中添加`http://dl.bintray.com/kotlin/kotlin-eap-1.2`; 使用`1.2.0-beta-31`作为编译器插件和标准库的版本号。
​	在IntelliJ IDEA中：工具→Kotlin→配置Kotlin插件更新，然后在更新下拉列表中选择“Early Access Preview 1.2”，然后按检查更新。
​	命令行编译器可以从[GitHub release page](https://github.com/JetBrains/kotlin/releases/tag/v1.2-beta)下载。
在[try.kotlinlang.org](https://try.kotlinlang.org/)上：使用右下角的下拉列表将编译器版本更改为1.2（即将到来）。