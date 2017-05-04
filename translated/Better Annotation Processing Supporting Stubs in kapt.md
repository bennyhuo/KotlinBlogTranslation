---
title: "[译]Better Annotation Processing: Supporting Stubs in kapt"
date: 2015-06-22 15:28:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/06/better-annotation-processing-supporting-stubs-in-kapt/
translator:
translator_url:
---

我们宣布 [kapt](http://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/) 之前，Kotlin的注释处理工具，并讨论了其局限性。现在，大部分<strong>限制正在消失，`可以使用`0.1-SNAPSHOT`预览版本的`kapt`更新版本。<span id =“ more-2385“> </span>
## 回顾：kapt如何工作

通过截取注解处理器（例如Dagger 2）和`javac`之间的通信，初始版本的`kapt`工作，并在Java类之上添加了已经编译的Kotlin类，代码> javac`在源中看到自己。这种方法的问题是，由于Kotlin类必须已经被编译，所以没有办法引用处理器生成的任何代码（例如Dagger的模块类）。因此，我们必须在Java中编写Dagger应用程序类。
## 它现在如何工作

如 [在上一篇博文中讨论过](http://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/) 可以通过在运行`javac`之前生成Kotlin类的</em> </em>来克服该问题，然后在`javac`完成后运行真正的编译。存根只包含声明，没有方法体。 Kotlin编译器用于在内存中创建这样的存根（它们用于Java互操作，当Java代码回溯到Kotlin时），所以我们只需要将它们序列化到磁盘上的文件。
## 示例：DBFlow

Stubs支持依赖于注释处理器生成的代码的框架。例如，您现在可以使用 [DBFlow](https://github.com/Raizlabs/DBFlow) 在Kotlin：

{% raw %}
<p></p>
{% endraw %}

```kotlin
public object ItemRepository {
 
    public fun getAll(): MutableList<Item> {
        return Select()
                .from(javaClass<Item>())
                .where()
                .orderBy(false, Item_Table.UPDATED_AT)
                .queryList()
    }
 
}
 
```

{% raw %}
<p></p>
{% endraw %}

由DBFLow库提供类似DSL的功能`Select（）`，（）`等，DBFlow的注释处理器生成`Item_Table`，上面的Kotlin代码可以高兴地参考它！
完整的例子是可用的 [这里](https://github.com/yanex/kotlin-poc) （谢谢 [Mickele Moriconi](https://github.com/mickele) 对于初始代码）。
请注意，生成存根需要相对较多的工作，因为所有声明必须解决，有时候知道返回类型需要分析表达式（函数或属性初始化程序的主体在`=`符号之后）。因此，在`kapt`中使用存根减慢了你的构建。这就是为什么<strong>存根默认情况下关闭</strong>，为了使它们能够在您的 [build.gradle文件](https://github.com/yanex/kotlin-poc/blob/master/app/build.gradle#L41) ：

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

此外，`kapt`现在可以处理传递参数到注释处理器。这是一个例子 [AndroidAnnotations](http://androidannotations.org/) 图书馆：

{% raw %}
<p></p>
{% endraw %}

```kotlin
kapt {
    generateStubs = true
    arguments {
        arg("androidManifestFile", variant.outputs[0].processResourcesTask.manifestFile)
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 源保留注释

正如您可能已经注意到的那样，我们生成二进制代码`.class` -files，而不是作为`.java`源。这更加方便，原因有很多：

* 我们已经为不同的目的生成了必要的字节，
* 在一个类文件中，我们可以简单地跳过一个方法的主体，不需要生成一个将使javac快乐的存根体，
* javac将编译存根源并生成稍后需要删除的类文件，
* 这种方式，旧的（快速）和新（较慢）的kapt模式使用相同的基本机制。

但是二进制存根有自己的缺点：

* 如果注释由@Retention（RetentionPolicy.SOURCE）标记，则它不在二进制文件中，
* javac不会在类层次结构下传播@Inherited注释。

到目前为止，我们还没有解决后一个问题，但前者的源保留注释是绝对关键的，因为许多流行的框架（如 [DBFlow](https://github.com/Raizlabs/DBFlow) ）他们的注释源保留。幸运的是，当`javac`读取二进制文件时，它不会仔细检查注释，如果我们将类保留的注释写入类文件，尽管声明了保留，它会高兴地看到它。这是我们现在所做的<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin /wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em“
## 剩余限制

在`kapt`上还有一些工作尚待处理。
注释处理本身最大的问题是支持 [@继承注释](http://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Inherited.html) 。我们需要解决`javac`，不会将它们传播到二进制类的层次结构中。
但是真正的问题在于外部的`kapt`：许多框架，如 [AndroidAnnotation](http://androidannotations.org/) 并且上述DBFlow想要直接将值注入到字段中，而Kotlin则是关于安全的，并且使这些字段`private`正在阻碍。这就是为什么现在我们必须在Java中编写DBFlow“表类” [Item.java](https://github.com/yanex/kotlin-poc/blob/master/app/src/main/java/mobi/porquenao/poc/kotlin/core/Item.java) 在我们的例子中
所以，我们正在考虑一个选择性功能，使得Kotlin生成的类中的非私有字段。
## 反馈

新的`kapt`尚未发布，但欢迎您尝试并告诉我们您的想法。以下是您如何做的例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
repositories {
    maven { url 'https://raw.github.com/Raizlabs/maven-releases/master/releases' }
    maven { url 'http://oss.sonatype.org/content/repositories/snapshots' }
    jcenter()
}
 
dependencies {
    ...
 
    // DBFlow
    kapt 'com.raizlabs.android:DBFlow-Compiler:2.0.0'
    compile 'com.raizlabs.android:DBFlow-Core:2.0.0'
    compile 'com.raizlabs.android:DBFlow:2.0.0'
 
    // Kotlin
    compile 'org.jetbrains.kotlin:kotlin-stdlib:0.1-SNAPSHOT'
}
 
kapt {
    generateStubs = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

再次参见完整的DBFlow示例 [这里](https://github.com/yanex/kotlin-poc) 。
请告诉我们：

* 有什么对你有用
* 什么没有？
* 你喜欢还是不喜欢什么？
* 任何我们忽视的用例？

谢谢！
