---
title: [译]Kotlin 1.0 Beta 4 is Out!
date: 2015-12-22 22:25:00
author: Roman Belov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/12/kotlin-1-0-beta-4-is-out/
---

我们很高兴地宣布Kotlin Beta 4，向1.0的另一个步骤！我们现在主要关注基础设施和面向未​​来的变化。完整的更改列表可在此处获得。更多细节如下。
现在是时候让你知道我们将在1.0之前还要做些什么。
## 改进的增量编译（实验）

我们已经推出了一个新的精确的依赖检测算法，使Kotlin的增量编译更快。它仍然是实验性的，但对我们的用例已经很好了。试试看：
设置|构建，执行，部署|编译器| Kotlin编译器|启用精确的增量编译（实验）
很快：同样的增量编译支持来到了Gradle！敬请关注。
## 语言

完整的更改列表中的一些亮点。
### 重载分辨率的变化

由于修复了重载解析算法，Kotlin现在将SAM转换的Java函数更像是成员（以前曾经像之前的扩展名一样）。这个修复很重要，因为编译器会以麻烦的方式解释许多情况。
不幸的是，至少有一个比较常见的情况已经破裂了。但修复很简单。现在编译器抱怨file.listFiles {it.name ==“...”}。
原因很复杂：

* java.io.File中有三个重载的列表文件
* 他们中的两个采取一个SAM接口，我们转换，以便他们可以采取一个lambda
* 所以当传递无参数的lambda时，我们不知道应该选择哪一个
* 之前工作，因为选择旧的图书馆扩展功能（可追溯到SAM之前的时代）而不是SAM转换的成员。

解决方法很简单，只需指定参数，例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
file.listFiles { it -> ... }
 
```

{% raw %}
<p></p>
{% endraw %}

### 属性可以用作无参数的函数对象

示例：在Kotlin中String :: length是一个属性，而不是一个函数，但是可以方便地使用它的功能，例如，

{% raw %}
<p></p>
{% endraw %}

```kotlin
val lengths = strs.map(String::length)
 
```

{% raw %}
<p></p>
{% endraw %}

所以，我们现在允许这个。换句话说，每当一个API期望一个类型（R） - > T的函数时，我们可以使用对返回类型为T的R的属性的引用。
### 保留关键字以备将来使用

我们计划在未来的Kotlin版本中添加新功能，因此我们决定提前预留必要的关键字。我们了解到，人们无法预测未来的全部，但这是我们最好的猜测（没有详细的设计，为将来的功能可用，但我们会尽力使它们有用）

* yield被保留为关键字
* 密封保留在“何时”之前
* typeof被保留为关键字。在JS中，使用jsTypeOf（）
* 异步保留在“{”和“乐趣”之前

所以现在，而不是异步{...}，我们不得不说async（）{...}。我们知道这不是很干净，但是我们没有找到更好的选择。代码完成将自动插入（）。
代码清理将帮助您迁移现有代码。
### Java通配符

有关Kotlin如何翻译变体类型的问题，例如List <Foo>是否应该是List <？在Java中扩展Foo>或简单地列出<Foo>。细节细节，我们做了如下工作：

* 默认情况下，我们不会在返回类型中生成通配符，并且它们没有任何意义
* 当需要通配符时，可以使用类型注释来强制执行其存在：List <@JvmWildcard String>始终是List <？在Java中扩展String>
* 当我们需要摆脱一个通配符时，我们可以使用@JvmSuppressWildcards（这可以在一个类型或包含它的任何声明中使用）

例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(l: List<String>) // in Java: List<String> (String is final)
fun foo(l: List<@JvmWildcard String>) // in Java: List<? extends String>
 
interface Open
fun bar(p: List<Open>) // in Java: List<? extends Open> (Open is not final)
@JvmSuppressWildcards
fun bar(p: List<Open>) // in Java: List<Open>
 
```

{% raw %}
<p></p>
{% endraw %}

注意：这不仅涉及集合，而且涉及涉及声明位置差异的所有类型
## 图书馆更改

我们正在清理标准库，这包括一些重新包装：

* kotlin.test软件包已被移动到单独的jar文件：kotlin-test.jar。可以在IDE中快速修复以自动添加此依赖关系。
* 为了准备在标准库中重新排列包，我们已经创建了新的包，并将所有的功能复制到它们。旧功能保留二进制兼容性。 Kotlin代码不需要迁移，代码清理可用于Java代码。

之后，我们计划从库中再次提取一个JAR：它将包含很少使用的数组实用程序，所以我们希望将它们保留在主JAR之外，以减小其大小。
更多亮点：
Kotlin的Int :: class可能对应于Java的int.class或Integer.class在不同的上下文中（它是有道理的）。为了方便用例，当需要两个特定的一个时，我们引入了两个属性：

* Int :: class.javaPrimitiveType返回Int.class
* Int :: class.javaObjectType返回Integer.class

此外，我们现在可以说如IntArray（5）{it * 3}，即创建初始化的原始数组。
### 未来的变化：集合中的null的含义

JDK的更新版本使得集合越来越不容忍。例如，以下是JavaDoc对java.util.Map.computeIfAbsent的描述：
如果指定的键尚未与值相关联（或映射到null），则尝试使用给定的映射函数计算其值，并将其输入到此映射中，除非为null。
这些合同对于这种操作的原子属性是固有的，所以我们决定我们也必须满足它们，否则当Kotlin的扩展功能在无空闲的并发集合中运行时，我们将无法保证正确的行为。所以，我们要改变getOrPut和其他这样的函数的行为，以便它们将null值与值不存在相同。
要更新您的代码，请遵循废弃警告中给出的建议。
## IDE中的新功能


* 添加了用于重命名未解析引用的快速修复。在将某些代码粘贴到不同的上下文时，可以方便地调整符号的名称：

