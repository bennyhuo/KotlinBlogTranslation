---
title: "[译]Kotlin M13 is out!"
date: 2015-09-16 18:29:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/kotlin-m13-is-out/
translator:
translator_url:
---

这是一个漫长的夏天，我们有很多告诉你关于Kotlin M13（详情如下）：

* 编译器守护进程可以更快的编译;
* 支持依赖注入和其他框架的后期属性;
* 用于表达封闭层级的密封类;
* 指定和检查注释目标;
* Java get / set对现在被视为Kotlin中的属性;
* 更好的Java互操作的类型安全性：考虑@NotNull注释（参见此博文）;
* 修饰符和注释已经在语法上分开（见本博客文章）;
* 全面功能反思课堂，功能和属性;
* 现在在模块外检查内部访问（详见下文）;
* 用于顶级功能和属性的新的.class文件布局;
* 和更多（见下文）

## 语言变化

我们正在用语言进行包装，并进行必要的更改以完成语法以及添加关键用例缺少的小事情。一些变化正在破裂，像往常一样，我们尽全力帮助您迁移。
请注意，我们正在努力的1.0版本将重点放在JVM支持上。 JavaScript后端将被包含，但它将被视为一个实验功能。因此，在这个版本中，影响JavaScript的变化很少。我们计划在1.0版本发布之后恢复JS的工作。
### Late-init属性

使用Kotlin将框架注入到Java字段（即依赖注入，Mocking，序列化和其他框架）中的最大问题之一是曾经不具有在构造函数中未初始化的非空类型的属性。
现在，我们介​​绍`lateinit`属性：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example {
    @Inject
    lateinit val foo: Foo
    @Inject
    lateinit var bar: Bar
}
 
```

{% raw %}
<p></p>
{% endraw %}

`foo`和`bar`都没有初始化器，但同时声明非空类型。如果我们在初始化之前尝试读取它们，将抛出异常，但是只要它们被DI框架（Guice，Dagger或Spring）初始化，它们就可以作为普通属性读取。
这样的属性也可以用于其他用例（如JUnit `setUp`初始化）。请注意，`val`可以被标记为`lateinit`以及`var`。不同于`var`，它们不能在代码中自由分配，但框架可以将值注入到无障碍中，因为底层JVM字段未标记为`final`。
看到更多的 [语言文档](http://kotlinlang.org/docs/reference/properties.html#late-initialized-properties) 。
### 密封课程

很多人问Kotlin是否支持 [代数数据类型（ADT）](https://en.wikipedia.org/wiki/Algebraic_data_type) 。答案一直是：“是的，ADT可以表示为Kotlin中的类，当`与模式匹配实际上一样好时，可以使用`。现在我们已经添加了一些更安全的类型：使用`密封的`类，我们可以确保在`中列举`时所有的情况都是：

{% raw %}
<p></p>
{% endraw %}

```kotlin
package pets
 
import pets.Pet.*
 
sealed class Pet(val name: String) {
    class Dog(name: String): Pet(name)
    class Cat(name: String): Pet(name)
}
 
fun Pet.saySomething(): String {
    return when (this) {
        is Dog -> "woof"
        is Cat -> "meow"
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

请注意，上述示例中不需要`else`：因为`Pet`是一个密封类，编译器知道除`Dog < / code>和`Cat` </em>。所以我们可以确保所有的情况都被检查，并且不需要`else`。顺便说一下，如果你忘记覆盖某些情况，编译器会报告一个错误，并提醒你这样做，或者诉诸`else`。
现在只有嵌入到密封类中的类可以扩展它，但是我们稍后会放宽这个限制，并允许在同一个源文件中的子类。
有关详细信息，请参阅 [文件](http://kotlinlang.org/docs/reference/classes.html#sealed-classes) 。
### 注释需要“@”

修饰符和注释已经在语法上分离（参见 [博客文章](http://blog.jetbrains.com/kotlin/2015/08/modifiers-vs-annotations/) ）在M13。我们现在需要一个`@`来注释，所有注释类都应该以大写字母开头命名（这使Java具有更好的统一性）。
因此，重命名诸如`@Throws`或`@Volatile`的库注释。我们还将`@platformName`重命名为`@JvmName`和`@platformStatic`到`@JvmStatic`。
一些以前的注释已经成为修饰符：

* 数据
* 内联相关

一致
中午线
crossiniline  - 而不是以前的@inlineOption（ONLY_LOCAL_RETURNS）
* 一致
* 中午线
* crossiniline  - 而不是以前的@inlineOption（ONLY_LOCAL_RETURNS）
* tailrec  - 而不是前@tailRecursive
* 外部 - 而不是以前的@native

对于大多数用户，此更改是透明的，因为未更改其名称的注释看起来像修饰符之前。
旧的语法和类已被弃用。
的 [代码清理IDE操作](http://blog.jetbrains.com/idea/2014/07/try-intellij-idea-14-eap-138-1283-4-with-code-cleanup-android-studio-beta-features-and-more/) 将帮助您迁移代码。
### 注释目标和其他选项

Kotlin现在支持以下注释选项（表示为注释类的注释）：

* @Retention  - 谁可以看到这个注释：RUNTIME（默认），BINARY（.class文件）或SOURCE;
* @Target  - 注释适用的地方;
* @MustBeDocumented  - 一个标记，表示此注释是注释元素的API的一部分，并且必须显示在生成的文档中;
* @Repeatable  - 一个标记，表示该注释可以在同一个元素上多次使用。

看到更多的 [文件](http://kotlinlang.org/docs/reference/annotations.html#annotation-declaration) 。
此外，我们现在可以为使用站点的注释指定可选目标：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example(
    @field:MyFieldAnnotation(...)
    val foo: Foo
)
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>注意：这是一个突破性的变化</strong>。在M13之前，当我们注释主要构造函数的参数时，在它们存储的参数和字段上注释<strong>都是</strong>。现在它们只写在以下一个（第一个适用的）之一：参数，属性，领域。即如果注释适用于字段和参数，则只会在参数上写入。这在使用Jackson时会出现一些问题，但有一个简单的解决方法：使用特殊的 [杰克逊模块为Kotlin](http://mvnrepository.com/artifact/com.fasterxml.jackson.module/jackson-module-kotlin) 。而旧的方式没有一个。
查找更多信息 [文件](http://kotlinlang.org/docs/reference/annotations.html#annotation-use-site-targets) 。
### 可见性

我们重新访问了我们的访问修改器/可见性模型。从现在开始：

* 顶层私有（任何类外）意味着“只能在此源文件内部可见”;
* 我们不需要公开声明的明确的返回类型;
* 默认可见性（无修饰符）从内部更改为public，
* 我们终于启用了拒绝在模块外部使用内部声明的检查。

这可能是有争议的，我们选择`public`作为默认可见性。 Kotlin是一种类型安全的语言，选择最安全的选项，默认情况下，`private`似乎更合乎逻辑。我们完全认识到有利于这一违约的有效论据。但Kotlin也是一种务实的语言。我会尽量简单解释为什么我们认为`public`是正确的默认值。
在真正的Java代码库（公开/私有决策明确地采用）中，`public`比`private`更频繁地出现（代码库中的2.5到5倍）我们检查过， [其中包括Kotlin编译器和IntelliJ IDEA](https://youtrack.jetbrains.com/issue/KT-3240#comment=27-1110881) ）。这意味着我们会让人们在整个地方写出`public`来实现他们的设计，这将使Kotlin更加礼节，我们会失去一些从Java获得的宝贵的成果简洁。在我们的经验中，显式的`public`打破了许多DSL的流程，并且常常是主要构造函数。所以我们决定默认使用它来保持我们的代码清洁。
<strong>注意</strong>：`internal`仍然支持，但现在您需要明确指定。
### 杂项变更


* 支持重载的可调用引用：即使foo重载也可以使用:: foo，但可以根据上下文选择正确的签名;
* 明确的超级可以使用没有尖括号;
* 类型参数严格无效检查;
* 没有默认参数的功能在重载分辨率（API进化有利）中是首选的;
* @HiddenDeclaration注释引入来隐藏来自客户端的声明，同时保持它们在二进制文件中（也为了更平滑的API演进）。

## Java互操作更改

### Java get / set对现在被视为属性

人们一直在要求这个功能很长一段时间，花了我们一段时间才搞清楚。现在，当我们使用通过约定定义属性的Java类（例如，`getFoo（）`，或者可能是`setFoo（）`）时，Kotlin会自动定义相应的扩展属性：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java:
 
class JBean {
    public Foo getFoo() { return ...; }
    public void setFoo(Foo foo) { ... }
}
 
// Kotlin
 
fun demo(bean: JBean) {
    println(bean.foo) // 'foo' is automatically defined
}
 
```

{% raw %}
<p></p>
{% endraw %}

对这些属性的访问进行了优化，以便`bean.foo`编译为`bean.getFoo（）`，无需任何中间调用。
### 顶层声明的.class文件的新布局

几个月前我们宣布了 [这个变化](http://blog.jetbrains.com/kotlin/2015/06/improving-java-interop-top-level-functions-and-properties/) 现在已经完成了：

* 默认情况下，每个Kotlin源文件（例如myFile.kt）生成一个具有相同名称，大小写并后缀为“Kt”的类文件：MyFileKt;
* 该文件中定义的顶级函数和属性可以通过Java类通过此类名来访问（而不是有问题的FooPackage）;
* 因此，同一个包中的两个文件不能具有相同的名称（或类文件会冲突）;
* 您可以在源文件上指定一个@file：JvmName（“CustomName”）注释来更改类的名称;
* 如果额外添加了@file：JvmMultifileClass注释，许多文件可以共享相同的JVM名称。

为了使这个更改工作，我们必须引入一个新的资源文件，这是编译Kotlin代码所需的Kotlin二进制文件。它的名字是`META-INF /＆lt; module_name＆gt; .kotlin_module`。 <strong>确保这些`.kotlin_module`文件不会被包装过程剥离。</strong>另外，确保模块名不会在您的项目中冲突：

* 在Maven中，我们使用groupId和artifactId作为模块名，但可以说


{% raw %}
<p></p>
{% endraw %}

```kotlin
<configuration>
    <moduleName>com.example.mymodule</moduleName>
</configuration>
 
```

{% raw %}
<p></p>
{% endraw %}


* 在Gradle中它的项目名称+构建任务名称，以自定义：


{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin {
    kotlinOptions.moduleName = "com.example.mymodule"    
}
 
```

{% raw %}
<p></p>
{% endraw %}


* 在Ant和命令行中，您应该明确指定模块名称：

<kotlinc modulename =“com.example.mymodule”/>
$ kotlinc-jvm -module-name com.example.mymodule
* <kotlinc modulename =“com.example.mymodule”/>
* $ kotlinc-jvm -module-name com.example.mymodule

更多信息可以找到 [这里](http://kotlinlang.org/docs/reference/java-interop.html#package-level-functions) 。
### Java互操作中的空安全

我们首先宣布这个 [不久以前](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-more-null-safety-for-java/) 。现在我们可以在Java中使用`@NotNull`和`@Nullable`，而Kotlin会认识到这些错误，导致编译错误而不是警告。
因此，使用Java集合变得更加安全：我们不能将`null`放入`ArrayList＆lt; String＆gt;`中。 [平台类型](http://blog.jetbrains.com/kotlin/2014/10/making-platform-interop-even-smoother/) 由于注释常常丢失，有时会出错（例如违反继承规则），因此默认情况下不会对Java代码施加静态空检。
外部注释也不会被使用，所以我们已经为您提供了很多构建配置。
## 图书馆

Kotlin图书馆也在积极发展。 M13带来全功能的反射库：我们现在可以内省课程，他们的成员，参数等。
标准库有很多方便的添加

* +和 - 用于集合和其他集合;
* 改善财产代表。

更多的这是一个单独的职位。
## 工具

<strong>编译器守护进程。</strong>我们宣布 [支持Gradle守护进程](http://blog.jetbrains.com/kotlin/2015/08/gradle-daemon-support-for-faster-compilation/) 前一段时间，您的反馈一直是积极的：编译时间似乎下降到三分之一。我们一直致力于编译性能，因为M13在IntelliJ IDEA中也使用了类似于Gradle的守护进程。此功能现在被标记为“实验性”，因此您需要勾选“首选项”</em>对话框中的一个框，将其打开：
<p>
  构建，执行，部署 - ＆gt;编译器 - ＆gt; Kotlin编译器 - ＆gt;在调用之前保持编译器进程（实验）
</p>
<strong>增量编译</strong>是我们为提高Kotlin编译时间而采取的另一个方向。 M13带来：

* 内联函数的增量编译：现在如果您更改内联函数的主体，则仅重新编译使用它的类;
* 对私有成员的更改不会导致重新编译其他文件。

## IDE

IDE的经验也得到了改善。为了简洁起见，我们仅强调那些不容易发现的功能：

* IDE键入时建议参数的名称和类型：
（提示：将鼠标悬停在图像上以开始动画）

