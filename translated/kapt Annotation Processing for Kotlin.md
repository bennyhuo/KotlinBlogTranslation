---
title: "[译]kapt: Annotation Processing for Kotlin"
date: 2015-05-21 23:39:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/
translator:
translator_url:
---

**这篇文章大部分已经过时了

请查看<a href="http://blog.jetbrains.com/kotlin/2015/06/better-annotation-processing-supporting-stubs-in-kapt/">更好的注释处理：在kapt中支持存根</a>**
由于有很多要求支持 [Java注释处理](https://www.jcp.org/en/jsr/detail?id=269) ，我们正在努力，第一个结果准备好**进行预览**。这是早期反馈的呼吁。 <span id =“more-2143”> </span>
我们计划在5月底公布对M12的JSR 269注解处理的初步支持。同时，大部分工作已经完成，您可以使用Gradle的Kotlin插件的`SNAPSHOT`版本进行测试。支持是有限的，但是 [匕首2](http://google.github.io/dagger/) 作品<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/ images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“
## 注释处理基础

JSR 269为Java编译器<em>注释处理器</em>定义了一种特殊类型插件的API。这样一个插件可以大致地向编译器询问“使用@Foo注释什么代码元素（类，方法，字段）”？编译器返回一组代表注释元素的对象。然后，处理器可以检查它们，并**生成一些新的代码**，该代码将在与注释代码相同的过程中被编译。诀窍在于，生成的代码可以由手写代码**使用，尽管编译器开始工作时不存在。
为了以Java语言支持注释处理，有一些选项：
**One。**重新实现JSR 269 API。这需要一些工作，但不是很难。问题是在**混合项目**中没有帮助：最终我们需要处理来自**Java和Kotlin代码的**中的注释元素，并且仅支持Kotlin中的JSR 269不是那么多的收获。
**两个。**从Kotlin源生成Java源，然后将其馈送到Java编译器，然后再运行处理器。当然，将Kotlin转换为完全工作的Java代码（方法体的翻译将非常痛苦）太难了，但是真正需要的只是**声明**。这是方式 [Groovy做到了](https://gradle.org/docs/2.4-rc-1/release-notes#support-for-“annotation-processing”-of-groovy-code) ：通过从Groovy代码生成Java“stub”，并将它们提供给Java编译器。这对于Kotlin也是有效的，但需要两个编译器运行：首先生成存根，然后再次编译生成的代码。参考处理器生成的类是可能的，但在某些情况下会出现问题（从使用生成代码的右侧表达式推断属性/函数类型，同时生成存根）。
**三。**假设Kotlin二进制文件**是** Java源代码。通常，Kotlin编译器首先运行，Java编译器将Kotlin代码视为二进制代码.class`文件。当然，源代码和二进制的所有代码元素都在Java编译器中统一表示。因此，处理器可能还没有获得注释的Java源代码，而是获取了注释的Kotlin二进制文件，但并不会注意到可用API的差异。不幸的是，Javac不会自动执行，但是我们可以在Java编译器和注解处理器之间插入，自己找到二进制元素，并将它们添加到通常由`javac`返回的源元素中。一个巨大的优势是，这个解决方案相当容易实现（涉及到一些小的字节代码生成，但是我们很习惯它））。但是有一些重要的限制：Kotlin代码不能引用处理器生成的声明，并且源保留注释通过二进制文件不可见。 （**更新**：两个限制都已解除 [稍后的](http://blog.jetbrains.com/kotlin/2015/06/better-annotation-processing-supporting-stubs-in-kapt/) 。）
现在，我们选择了三个，名称为`kapt`（Kotlin注释处理）。它看起来像是最重要的现实生活用例。不过，我们可以稍后支持选项二。
## 示例：使用匕首2

Gradile插件支持`kapt`，以启用它，添加

{% raw %}
<p></p>
{% endraw %}

```kotlin
dependencies {
    ...
    compile 'com.google.dagger:dagger:2.0'
    kapt 'com.google.dagger:dagger-compiler:2.0'
    provided 'org.glassfish:javax.annotation:10.0-b28'
```

{% raw %}
<p></p>
{% endraw %}

到你的构建脚本。注释将从您的Java和Kotlin代码中获取。
由于`kapt`尚未发布，所以只能从Kotlin的`SNAPSHOT`版本中获得：

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
    repositories {
        ...
        maven {
            url 'http://oss.sonatype.org/content/repositories/snapshots'
        }
    }
    dependencies {
        ...
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:0.1-SNAPSHOT"
    }
}
```

{% raw %}
<p></p>
{% endraw %}

由于上述限制，使用Dagger生成的代码的类必须使用Java编写（通常它的代码很少）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import android.app.Application;
 
public abstract class BaseApplication extends Application {
 
    protected ApplicationComponent createApplicationComponent() {
        return DaggerApplicationComponent.builder()
                .androidModule(new AndroidModule(this)).build();
    }
}
```

{% raw %}
<p></p>
{% endraw %}

一切都可以写在Kotlin。这是一个演示匕首使用的示例项目： [kotlin匕首](https://github.com/JetBrains/kotlin-examples/tree/master/gradle/kotlin-dagger) （您可能需要强制重新下载快照工件）。
## 反馈

如果您在项目中尝试了`kapt`，我们非常感激，并给予我们反馈：

* 你尝试了什么框架？
* 它为你工作吗？
* 你要写多少Java代码？
* 任何其他问题？

