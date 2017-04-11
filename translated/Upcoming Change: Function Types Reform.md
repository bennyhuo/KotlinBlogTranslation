---
title: [译]Upcoming Change: Function Types Reform
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
---

Kotlin M12可能会带来另一个变化，这对Kotlin实施一个有用的反思库至关重要。简而言之，我们将在运行时以相同的方式统一FunctionX和ExtensionFunctionX，但不会影响我们创建类型安全的构建器和其他类DSL构造的能力。
## 为什么

目前，在kotlin包kotlin-runtime.jar中有23 * 2 = 46类与FileX相关的类文件，以及46个与ExtensionFunctionX相关的类文件（X是0到22之间的数字）。这是很多类文件，但是在kotlin.reflect包（KFunctionX，KMemberFunctionX，KExtensionFunctionX）中有46 * 3 = 138个更多的类文件，这是顶部的
所以，一方面，我们真的需要减少kotlin-runtime.jar中的类文件数量。
那么，ExtensionFunctionX类型与FunctionX类型无关，我们不能说listOfStrings.map（String :: length），因为该参数的类型为String。（） - > Int，但是map（）expects（String） - > Int，这是悲伤，烦人和不方便。
所以，我们想使扩展功能对正常的功能（具有额外的参数）是强制的。
当我们在此时，我们也希望允许具有超过22个参数的功能，理论上可以使用任何数量的参数（实际上在JVM中为255）。
这里的一个重要约束是在Java中实现Kotlin函数必须保持简单：Java 8 lambdas应该可以工作，而在早期版本的Java中，新的Function2（）{...}只有在主体中的invoke（）方法应该是足够的。
## 怎么样

所有230个函数类文件将被一个单一的接口Function代替，该函数将在运行时代表所有函数（+我们将保留23个接口kotlin.jvm.FunctionX以便于在Java中轻松创建Kotlin函数）。共赢得超过200个类文件。
现在，函数值（“（A） - > B”）和扩展函数值（“A.（） - > B”）将在运行时由相同的类型表示，这将允许使用它们几乎可互换。静态类型系统将仅区分特征（例如，编译器将为任何X创建虚构的“类”FunctionX，该X仅在编译时才会存在，永远不会作为类文件发布）。
由于编译时类型与运行时类型不完全相同，所以运算符中的一些调整就像需要一样，但不会影响不是静态地涉及函数类型的情况。
函数和扩展函数类型之间的句法区别将被保留（通过将A.（） - > B放到一个带注释的函数类型）：当一个lambda与预期的类型进行类型检查时，它是一个扩展函数，一个这个接收者的签名，而对于正常的功能，它添加一个参数：

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

这些变化会使功能的反思成为可能（即KClass最终会有getFunctions（）），而使用函数对象将更加直观。
除非您直接引用ExtensionFunctionX类型（例如ExtensionFucntion0 <Foo，Unit>），否则不需要更改代码中的任何内容。
有关更多详细信息，请参阅此规范文档（您可以对源进行评论，或按“查看”进行渲染降价）。
