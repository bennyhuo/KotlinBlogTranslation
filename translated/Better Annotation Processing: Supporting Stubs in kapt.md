---
title: [译]Better Annotation Processing: Supporting Stubs in kapt
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
---

前一段时间，我们发布了kapt，一个Kotlin的注释处理工具，并讨论了它的局限性。现在，大部分的限制都是随着更新版本的kapt而有所改进，可以作为0.1-SNAPSHOT预览。
## 回顾：kapt如何工作

kapt的初始版本通过截取注解处理器（例如Dagger 2）和javac之间的通信来工作，并在javac在源中看到的Java类之上添加了已编译的Kotlin类。这种方法的问题是，由于Kotlin类必须已经被编译，所以没有办法引用处理器生成的任何代码（例如Dagger的模块类）。因此，我们必须在Java中编写Dagger应用程序类。
## 它现在如何工作

如上一篇博客文章所述，可以通过在运行javac之前生成Kotlin类的存根，然后在javac完成后运行真正的编译来克服这个问题。存根只包含声明，没有方法体。 Kotlin编译器用于在内存中创建这样的存根（它们用于Java互操作，当Java代码回溯到Kotlin时），所以我们只需要将它们序列化到磁盘上的文件。
## 示例：DBFlow

Stubs支持依赖于注释处理器生成的代码的框架。例如，您现在可以在Kotlin中使用DBFlow：

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

类似DSL的功能Select（），from（）等由DBFLow库提供，Item_Table由DBFlow的注释处理器生成，上面的Kotlin代码可以高兴地引用它！
完整的例子可以在这里（感谢Mickele Moriconi的初始代码）。
请注意，生成存根需要相对较多的工作，因为所有声明必须解决，有时候知道返回类型需要分析表达式（=符号后的函数或属性初始值的主体）。所以，在kapt中使用存根减慢你的建设有点。这就是为什么stub在默认情况下关闭，为了使它们能够在build.gradle文件中编写以下内容：

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

此外，kapt现在可以将注释处理器的参数传递给它们。以下是AndroidAnnotations库的示例：

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

正如您可能已经注意到的那样，我们将生成存根作为二进制.class文件，而不是.java源。这更加方便，原因有很多：

* 我们已经为不同的目的生成了必要的字节，
* 在一个类文件中，我们可以简单地跳过一个方法的主体，不需要生成一个将使javac快乐的存根体，
* javac将编译存根源并生成稍后需要删除的类文件，
* 这种方式，旧的（快速）和新（较慢）的kapt模式使用相同的基本机制。

但是二进制存根有自己的缺点：

* 如果注释由@Retention（RetentionPolicy.SOURCE）标记，则它不在二进制文件中，
* javac不会在类层次结构下传播@Inherited注释。

我们到目前为止还没有解决后一个问题，但是前面的源保留注释是绝对关键的，因为许多流行的框架（如DBFlow）的注释源保留。幸运的是，当javac读取二进制文件时，它不会仔细检查注释，如果我们将类保留的注释写入类文件，尽管声明了保留，它将很高兴地看到它。这是我们现在所做的
## 剩余限制

在kapt上还有一些工作还在等待。
注释处理本身最大的问题是支持@Inherited注释。我们需要解决javac不会将它们传播到二进制类的层次结构中。
但真正的问题在于kapt之外：许多框架，如AndroidAnnotation和上述的DBFlow都希望将值直接注入到字段中，而Kotlin则是关于安全性的，而这些领域是私有的。这就是为什么现在我们必须在Java中编写DBFlow“表类”，请参阅我们的例子中的Item.java。
所以，我们正在考虑一个选择性功能，使得Kotlin生成的类中的非私有字段。
## 反馈

新的kapt尚未发布，但欢迎您尝试并告诉我们您的想法。以下是您如何做的例子：

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

再次看到这里的完整的DBFlow示例。
请告诉我们：

* 有什么对你有用
* 什么没有？
* 你喜欢还是不喜欢什么？
* 任何我们忽视的用例？

谢谢！
