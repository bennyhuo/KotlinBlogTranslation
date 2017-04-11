---
title: [译]Kotlin M13 is out!
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
现在我们介绍一下晚期的属性：

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

foo和bar都没有初始化器，但同时声明非空类型。如果我们在初始化之前尝试读取它们，将抛出异常，但是只要它们被DI框架（Guice，Dagger或Spring）初始化，它们就可以作为普通属性读取。
此类属性也可用于其他用例（如JUnit setUp初始化）。请注意，val可以标记为lateinit以及var。与var不同，它们不能在代码中自由分配，但是框架可以在没有障碍的情况下向其中注入值，因为底层JVM字段未标记为final。
在语言文档中查看更多内容。
### 密封课程

许多人问Kotlin是否支持代数数据类型（ADT）。答案一直是：“是的，ADT可以表示为Kotlin的类，什么时候几乎和模式匹配一​​样好”。现在我们已经添加了更多的类型安全性：使用密封类，我们可以确保在下列情况下枚举所有的案例：

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

请注意，在上面的示例中不需要其他内容：由于Pet是一个密封类，编译器知道它没有除Dog和Cat之外的子类。所以我们可以确定所有的情况已被检查，否则不需要。顺便说一下，如果你忘记覆盖某些情况，编译器将报告一个错误，并提醒你这样做，或者诉诸于别的。
现在只有嵌入到密封类中的类可以扩展它，但是我们稍后会放宽这个限制，并允许在同一个源文件中的子类。
有关详细信息，请参阅文档。
### 注释需要“@”

在M13中，修饰符和注释已经被语法分离（见本博文）。我们现在需要一个@用于注释，并且所有的注释类都应该以大写字母开头命名（这使得Java具有更好的一致性）。
因此，重命名了@Throws或@Volatile等库注释。我们还将@platformName重命名为@JvmName和@platformStatic到@JvmStatic。
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
代码清理IDE操作将帮助您迁移代码。
### 注释目标和其他选项

Kotlin现在支持以下注释选项（表示为注释类的注释）：

* @Retention  - 谁可以看到这个注释：RUNTIME（默认），BINARY（.class文件）或SOURCE;
* @Target  - 注释适用的地方;
* @MustBeDocumented  - 一个标记，表示此注释是注释元素的API的一部分，并且必须显示在生成的文档中;
* @Repeatable  - 一个标记，表示该注释可以在同一个元素上多次使用。

在文档中查看更多内容。
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

注意：这是一个突破性的变化。在M13之前，当我们注释主要构造函数的参数时，注释是在它们存储的参数和字段上写的。现在它们只写在以下（第一个适用的）之一：参数，属性，字段中。即如果注释适用于字段和参数，则只会在参数上写入。这在使用Jackson时会出现一些问题，但有一个简单的解决方法：使用Kotlin的特殊杰克逊模块。而旧的方式没有一个。
在文档中查找更多信息。
### 可见性

我们重新访问了我们的访问修改器/可见性模型。从现在开始：

* 顶层私有（任何类外）意味着“只能在此源文件内部可见”;
* 我们不需要公开声明的明确的返回类型;
* 默认可见性（无修饰符）从内部更改为public，
* 我们终于启用了拒绝在模块外部使用内部声明的检查。

这可能是有争议的，我们选择公共作为默认可见性。 Kotlin是一种类型安全的语言，选择最安全的选项，默认情况下私有的似乎更合乎逻辑。我们完全认识到有利于这一违约的有效论据。但科特林也是一种务实的语言。我会尽量简单解释为什么我们认为公众是正确的违约。
在真实的Java代码库（公共/私人决策被明确地采用）中，公开发生的频率比私有（在我们检查的代码基础中的频率高出2.5到5倍，包括Kotlin编译器和IntelliJ IDEA）。这意味着我们会让人们在公众场合发表演说来实现他们的设计，这样可以使Kotlin更加礼貌，我们会因为简洁而失去一些从Java获得的宝贵的成果。在我们的经验中，明确的公开打破了许多DSL的流动，并且常常是主要构造函数。所以我们决定默认使用它来保持我们的代码清洁。
注意：内部支持支持，但现在您需要明确指定。
### 杂项变更


* 支持重载的可调用引用：即使foo重载也可以使用:: foo，但可以根据上下文选择正确的签名;
* 明确的超级可以使用没有尖括号;
* 类型参数严格无效检查;
* 没有默认参数的功能在重载分辨率（API进化有利）中是首选的;
* @HiddenDeclaration注释引入来隐藏来自客户端的声明，同时保持它们在二进制文件中（也为了更平滑的API演进）。

## Java互操作更改

### Java get / set对现在被视为属性

人们一直在要求这个功能很长一段时间，花了我们一段时间才搞清楚。现在，当我们使用通过常规定义属性的Java类（例如getFoo（）和可能的setFoo（））时，Kotlin会自动定义相应的扩展属性：

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

对这些属性的访问进行了优化，以便bean.foo无需任何中间调用即可编译成bean.getFoo（）。
### 顶层声明的.class文件的新布局

几个月前，我们宣布了这一变化，现在已经完成了：

* 默认情况下，每个Kotlin源文件（例如myFile.kt）生成一个具有相同名称，大小写并后缀为“Kt”的类文件：MyFileKt;
* 该文件中定义的顶级函数和属性可以通过Java类通过此类名来访问（而不是有问题的FooPackage）;
* 因此，同一个包中的两个文件不能具有相同的名称（或类文件会冲突）;
* 您可以在源文件上指定一个@file：JvmName（“CustomName”）注释来更改类的名称;
* 如果额外添加了@file：JvmMultifileClass注释，许多文件可以共享相同的JVM名称。

为了使这个更改工作，我们必须引入一个新的资源文件，这是编译Kotlin代码所需的Kotlin二进制文件。它的名字是META-INF / <module_name> .kotlin_module。确保这些.kotlin_module文件不会被包装过程剥离。另外，确保模块名称不会在您的项目中冲突：

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

更多信息可以在这里找到。
### Java互操作中的空安全

我们刚才宣布了这个。现在我们可以在Java中使用@NotNull和@Nullable，而Kotlin可以识别它们，以免误用导致编译错误而不是警告。
因此，使用Java集合变得更加安全：我们不能再将一个null放入ArrayList <String>。
平台类型保持原样，因为注释通常会丢失，有时会出错（例如违反继承规则），因此默认情况下不会对Java代码施加静态空检。
外部注释也不会被使用，所以我们已经为您提供了很多构建配置。
## 图书馆

科特林图书馆也在积极发展。 M13带来全功能的反射库：我们现在可以内省课程，他们的成员，参数等。
标准库有很多方便的添加

* +和 - 用于集合和其他集合;
* 改善财产代表。

更多的这是一个单独的职位。
## 工具

编译器守护进程。我们之前宣布支持Gradle Daemon，您的反馈一直是积极的：编译时间似乎下降到三分之一。我们一直致力于编译性能，因为M13在IntelliJ IDEA中也使用了类似于Gradle的守护进程。此功能现在被标记为“实验性”，因此您需要勾选“首选项”对话框中的一个框，将其打开：
构建，执行，部署 - >编译器 - > Kotlin编译器 - >保持编译过程在调用之间生效（实验）
增量编译是我们为提高Kotlin编译时间而采取的另一个方向。 M13带来：

* 内联函数的增量编译：现在如果您更改内联函数的主体，则仅重新编译使用它的类;
* 对私有成员的更改不会导致重新编译其他文件。

## IDE

IDE的经验也得到了改善。为了简洁起见，我们仅强调那些不容易发现的功能：

* IDE键入时建议参数的名称和类型：
（提示：将鼠标悬停在图像上以开始动画）

