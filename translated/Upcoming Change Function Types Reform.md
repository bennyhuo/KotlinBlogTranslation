---
title: "[译]Upcoming Change: Function Types Reform"
date: 2015-04-09 14:26:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-change-function-types-reform/
translator:
translator_url:
---

Kotlin M12可能会带来另一个变化，这对Kotlin实施一个有用的反思库至关重要。简而言之，我们将统一`FunctionX`和`ExtensionFunctionX`在运行时以相同的方式表示，但不会影响我们创建的能力 [类型安全的建设者](http://kotlinlang.org/docs/reference/type-safe-builders.html) 和其他类似DSL的结构。<span id =“more-2062”> </span>
## 为什么

目前，在`kotlin`包`kotlin-runtime.jar`中有与`FunctionX`相关的23 * 2 = 46类文件和46个更多的类文件相关到`ExtensionFunctionX`（`X`是0到22之间的数字）。这是很多类文件，但是在`kotlin.reflect`包（`KFunctionX`，`KMemberFunctionX`中有46 * 3 = 138个类文件>，`KExtensionFunctionX`），这是顶部的<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https：// i2 .wp.com / blog.jetbrains.com / kotlin / wp-includes / images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“ >
所以，一方面，我们真的需要在`kotlin-runtime.jar`中<strong>减少类文件的数量</strong>。
那么，现在，`ExtensionFunctionX`类型与`FunctionX`类型无关，我们不能说`listOfStrings.map（String :: length）`因为参数的类型为`String。（） - ＆gt; Int`，但是`map（）` expects `（String） - ＆gt; Int`，这是悲伤，烦人和不便。
因此，我们希望将扩展功能<strong>强制为正常功能</strong>（带有一个额外的参数）。
在我们这样做的时候，我们也希望<strong>允许具有超过22个参数的功能</strong>，理论上可以是任意数量的参数（在JVM中实际上是255）。
这里的一个重要约束是在Java </strong>中实现Kotlin函数必须保持简单：Java 8 lambdas应该可以工作，在早期版本的Java `新的Function2（）{...}`中只有在代码中的`invoke（）`方法就足够了。
## 怎么样

所有230个功能类文件将被单个接口替代 [功能](https://github.com/JetBrains/kotlin/blob/spec-function-types/spec-docs/function-types.md#function-trait) 这将代表运行时的所有功能（+我们将保留23个接口`kotlin.jvm.FunctionX`，以方便在Java中轻松创建Kotlin函数）。共赢得超过200个类文件。
现在，函数值（“`（A） - ＆gt; B`”）和扩展函数值（“`A.（） - > B`”）在运行时相同的类型，这将允许使用它们几乎可互换。静态类型系统只会区分特征（例如，编译器将为任何X创建虚构的“类”代码FunctionX`，这将仅在编译时才会存在，永远不会作为类文件发布）。
由于编译时类型与运行时类型不完全相同，所以需要在`之类的运算符（`）中进行几个调整，因为`是必需的，但它们不会影响不是静态地知道涉及函数类型。
函数和扩展函数类型之间的语法区别将被保留（通过将`A（）→B`与注释的函数类型相结合）：当lambda是类型时 - 根据预期的类型进行检查，该类型是扩展函数，类型推断会将`这个` -receiver添加到其签名中，而对于正常的函数，它会添加一个参数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Normal function:
fun call(callback: (Foo) -> Unit) { // callback has type `Function1<Foo, Unit>
    ...
}
 
// argument is a lambda with a normal parameter
call { foo -> println(foo) }
 
// Extension function
fun builder(body: Foo.() -> Unit) { // body has type `@extension Function1<Foo, Unit>`
  ...
}
 
// argument is an extension lambda: no parameters, but `this` is available
builder {
    this.bar() // `this` has type Foo
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 后果

这些变化会使功能的反思成为可能（即，`KClass`将最终具有`getFunctions（）`），并且使用函数对象将更加直观。
<strong>除非您直接引用`ExtensionFunctionX`类型（例如，例如`ExtensionFucntion0＆lt; Foo，Unit＆gt;`），否则您不需要更改代码中的任何内容</strong> 。
有关详细信息，请参阅 [规格文件](https://github.com/JetBrains/kotlin/pull/636/files) （您可以对源进行评论，或者按“查看”进行渲染降价）。
