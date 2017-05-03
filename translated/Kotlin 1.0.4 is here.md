---
title: "[译]Kotlin 1.0.4 is here"
date: 2016-09-22 20:18:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/09/kotlin-1-0-4-is-here/
---

我们很高兴地宣布发布Kotlin版本<b> 1.0.4 </b>的新错误修复和工具更新。该版本带来了与IDE和构建工具相关的许多改进，以及JavaScript支持。
我们再次感谢我们的外部贡献者在本版本中实现了一些功能， [基拉里·拉赫曼](https://github.com/cypressious) 和 [Yoshinori Isogai](https://github.com/shiraji) ，以及所有尝试EAP构建1.0.4的用户，并向我们发送反馈。
您可以在其中找到修复和改进的完整列表 [更新日志](https://github.com/JetBrains/kotlin/blob/1.0.4/ChangeLog.md) 。有些更改值得特别提及：
### 语言变化：在try / catch中赋值'val'

在1.0版之前的Kotlin版本中，您可以在<code> try </code>和<code> catch </code>分支中初始化相同的<code> val </code> catch </code>语句。例如，允许以下代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x: Int
try {
    x = 1
}
catch(e: Exception) {
    x = 2
}
 
```

{% raw %}
<p></p>
{% endraw %}

实际上，最后一个变量可以被分配两次，并且可以观察到两个不同的值（例如，如果<code> try </code>语句中的值在lambda中被捕获）。在Java中，不允许使用等效代码。
为了保持一致的语义，在<code> try </code>和<code> catch </code>分支<b>中分配相同的<code> val </code>的代码成为警告</b> Kotlin 1.0.4并将在版本1.0.5中<b>成为错误</b>。在大多数情况下，可以通过将代码转换为表达式来轻松修复代码，IDE将<b>提供一个quickfix </b>来自动转换此代码。上述示例将转换为：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = try {
    1
}
catch(e: Exception) {
    2
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-4275"></span></p>
{% endraw %}

### 新实验注释处理

Kotlin 1.0.4包含了一个新的注解处理API的实验实现。要启用它，请将以下内容添加到您的build.gradle中：
<code>应用插件：'kotlin-kapt'</code>
您还需要<b>删除</b>启用旧注释处理的代码段：

{% raw %}
<p></p>
{% endraw %}

```kotlin
kapt {
    generateStubs = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

新的注解处理仍然存在已知问题，可能与所有注释处理器不兼容。只有当您遇到缺省的<code> kapt </code>注解处理实现问题时，才应启用它。
### JavaScript后端改进

JavaScript后端现在可以将代码编译为与AMD，CommonJS和UMD模块系统兼容的模块。看到 [文件](http://kotlinlang.org/docs/reference/js-modules.html) 更多细节。
此外，现在支持有限形式的反射：您可以使用<code> jsClass </code>属性来访问任何对象的运行时类，并且<code> jsClass＆lt; TypeName＆gt;（）</code>以获取特定类的运行时表示。这是一个更完整的例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class A
class B
class C
 
inline fun <reified T> foo() {
    println(jsClass<T>().name)
}
 
println(A().jsClass.name) // prints "A"
println(jsClass<B>().name) // prints "B"
foo<C>() // prints "C"
 
```

{% raw %}
<p></p>
{% endraw %}

### 编译器改进


* 更好的可调用表达式的类型推断

对于表达式的时候和表达的几种情况，效率更高的字节码

更好的语法错误后解析器恢复

修正了“Cast从不成功”警告错误报告的几种情况
* 对于表达式的时候和表达的几种情况，效率更高的字节码

更好的语法错误后解析器恢复

修正了“Cast从不成功”警告错误报告的几种情况
* 更好的语法错误后解析器恢复

修正了“Cast从不成功”警告错误报告的几种情况
* 修正了“Cast从不成功”警告错误报告的几种情况

### 构建工具改进


* 与Gradle 2.14及更高版本兼容。

Gradle增量编译现在可以跟踪子项目之间的变化。

默认情况下，CLI和Ant构建将Kotlin反射库添加到类路径;使用无反射开关禁用。
* Gradle增量编译现在可以跟踪子项目之间的变化。

默认情况下，CLI和Ant构建将Kotlin反射库添加到类路径;使用无反射开关禁用。
* 默认情况下，CLI和Ant构建将Kotlin反射库添加到类路径;使用无反射开关禁用。

### IDE中的新功能


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/KotlinEvaluate.png?ssl=1" rel="attachment wp-att-4285"><img alt="kotlinevaluate" class="alignnone size-full wp-image-4285" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/KotlinEvaluate.png?resize=640%2C648&amp;ssl=1"/></a></p>
{% endraw %}


* 在Java文件中评估表达式和监视时，现在可以选择使用Kotlin语法

检查“泄漏”的新检查 - 可能由访问未完成初始化的数据导致的NullPointerException异常问题。

意图将lambda转换为函数引用

检查以检测Gradle版本与Kotlin插件版本之间的不匹配

许多其他的新意图，检查和quickfixes
* 检查“泄漏”的新检查 - 可能由访问未完成初始化的数据导致的NullPointerException异常问题。

意图将lambda转换为函数引用

检查以检测Gradle版本与Kotlin插件版本之间的不匹配

许多其他的新意图，检查和quickfixes
* 意图将lambda转换为函数引用

检查以检测Gradle版本与Kotlin插件版本之间的不匹配

许多其他的新意图，检查和quickfixes
* 检查以检测Gradle版本与Kotlin插件版本之间的不匹配

许多其他的新意图，检查和quickfixes
* 许多其他的新意图，检查和quickfixes

### 如何更新

要更新插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“检查更新现在”按钮。另外，别忘了在Maven和Gradle构建脚本中更新编译器和标准库版本。
像往常一样，如果您遇到新版本的任何问题，欢迎您提供帮助 [论坛](https://discuss.kotlinlang.org/) ，在Slack（获得邀请） [这里](http://kotlinslackin.herokuapp.com/) ），或报告中的问题 [问题追踪器](https://youtrack.jetbrains.com/issues/KT) 。
让我们来吧！
