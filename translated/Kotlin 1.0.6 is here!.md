---
title: "[译]Kotlin 1.0.6 is here!"
date: 2016-12-27 20:11:00
author: yanex
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/12/kotlin-1-0-6-is-here/
translator:
translator_url:
---

我们很高兴地宣布发布Kotlin 1.0.6，这是Kotlin 1.0的新bug和工具更新。此版本带来了与IDE插件和Android支持相关的大量改进。
我们要感谢我们的外部贡献者，他们的引用请求被包含在这个版本中： [基拉里·拉赫曼](https://github.com/cypressious) 和 [Yoshinori Isogai](https://github.com/shiraji) 。我们也要感谢我们的EAP用户的反馈。这对我们来说真的很有价值。
您可以在其中找到完整的更改列表 [更新日志](https://github.com/JetBrains/kotlin/blob/1.0.6/ChangeLog.md#106) 。下面将介绍一些值得突出显示的变化。 <span id =“more-4429”> </span>
## 将`try-finally`转换为`use（）`意图

我们继续添加将代码转换为惯用Kotlin的意图。 IDE现在自动地建议用...替换`try-finally`块 [使用（）](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/use.html) 当所有的`finally`块正在关闭资源时调用
“img alt =”“class =”alignnone size-full wp-image-4043“onmouseout =”this.src ='https：//d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/12/try1.png'; “ onmouseover =“this.src ='https：//d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/12/try.gif';” src =“https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/12/try1.png”width =“700”/>
## “添加名称来调用参数”意图

命名的参数有助于增加代码的可读性。使用新的“添加名称来调用参数”意图，您可以轻松地将名称添加到参数中，或者只是替换所有调用参数的名称。

{% raw %}
<p><img alt="" class="alignnone size-full wp-image-4043" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/12/args.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/12/args.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/12/args.png" width="700"/></p>
{% endraw %}

## 其他显着的IDE插件更改


* 清除空二次建设机构的检查/意图，以及空的主要建设者声明;
* “加入申报和转让”意向;
* 修复调试器中的内联函数和性能改进;
* KDoc和Quick Doc的许多修复意图。

## Android支持


* 现在支持Android Studio 2.3 beta 1，以及Android Gradle插件2.3.0-alpha3和更新版本。
* 添加“创建XML资源”意图;
* 只有在build.gradle中启用相应的插件，Android Extensions支持才能在IDE中处于活动状态;
* Android Lint中的大量修复程序。另外还添加了“抑制皮肤”意图。

## Kapt改进

我们继续研究Kotlin注解处理工具（kapt）的实验版本。尽管为了完全支持增量编译，还有一些事情要做，但自Kotlin 1.0.4起，注释处理的性能显着增加。
要启用实验性kapt，只需将以下行添加到您的`build.gradle`：
`应用插件：'kotlin-kapt'`
## 全开编译器插件

<strong>全开</strong>编译器插件使类注释具有特定的注释，并且它们的成员在没有明确的`open`关键字的情况下打开，因此使用框架/库更容易，如Spring AOP或Mockito。您可以阅读相关的全开的详细信息 [保持](https://github.com/Kotlin/KEEP/pull/40) 。
我们为Gradle和Maven以及IDE集成提供全面的插件支持。
### 如何使用全开的Gradle


{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-allopen:$kotlin_version"
    }
}
 
apply plugin: "kotlin-allopen"
 
allOpen {
    annotation("com.your.Annotation")
}
 
```

{% raw %}
<p></p>
{% endraw %}

如果类（或其任何超类）用`com.your.Annotation`注释，则类本身及其所有成员将被打开。它甚至可以使用元注释：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@com.your.Annotation
annotation class MyFrameworkAnnotation
 
@MyFrameworkAnnotation
class MyClass // will be all-open
 
```

{% raw %}
<p></p>
{% endraw %}

我们还提供了已经具有Spring框架所有必需注释的“kotlin-spring”插件：

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-allopen:$kotlin_version"
    }
}
 
apply plugin: "kotlin-spring"
 
```

{% raw %}
<p></p>
{% endraw %}

当然，您可以在同一个项目中同时使用`kotlin-allopen`和`kotlin-spring`。
### 如何使用全部打开与Maven


{% raw %}
<p></p>
{% endraw %}

```kotlin
<plugin>
    <artifactId>kotlin-maven-plugin</artifactId>
    <groupId>org.jetbrains.kotlin</groupId>
    <version>${kotlin.version}</version>
 
    <configuration>
        <compilerPlugins>
            <!-- Or "spring" for the Spring support -->
            <plugin>all-open</plugin>
        </compilerPlugins>
 
        <pluginOptions>
            <!-- Each annotation is placed on its own line -->
            <option>all-open:annotation=com.your.Annotation</option>
            <option>all-open:annotation=com.their.AnotherAnnotation</option>
        </pluginOptions>
    </configuration>
 
    <dependencies>
        <dependency>
            <groupId>org.jetbrains.kotlin</groupId>
            <artifactId>kotlin-maven-allopen</artifactId>
            <version>${kotlin.version}</version>
        </dependency>
    </dependencies>
</plugin>
 
```

{% raw %}
<p></p>
{% endraw %}

## No-arg编译器插件

<b> no-arg </b>编译器插件为具有特定注释的类生成一个额外的零参数构造函数。生成的构造函数是合成的，因此不能从Java或Kotlin直接调用，但可以使用反射来调用它。你可以看到激动人心的讨论 [这里](https://discuss.kotlinlang.org/t/feature-request-a-modifier-annotation-for-data-classes-to-provide-a-non-arg-constructor-on-jvm/1549/4) 。
### 如何在Gradle中使用no-arg

用法非常类似于全开。

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-noarg:$kotlin_version"
    }
}
 
// Or "kotlin-jpa" for the Java Persistence API support
apply plugin: "kotlin-noarg"
 
noArg {
    annotation("com.your.Annotation")
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 如何在Maven中使用无参数


{% raw %}
<p></p>
{% endraw %}

```kotlin
<plugin>
    <artifactId>kotlin-maven-plugin</artifactId>
    <groupId>org.jetbrains.kotlin</groupId>
    <version>${kotlin.version}</version>
 
    <configuration>
        <compilerPlugins>
            <!-- Or "jpa" for the Java Persistence annotation support -->
            <plugin>no-arg</plugin>
        </compilerPlugins>
 
        <pluginOptions>
            <option>no-arg:annotation=com.your.Annotation</option>
        </pluginOptions>
    </configuration>
 
    <dependencies>
        <dependency>
            <groupId>org.jetbrains.kotlin</groupId>
            <artifactId>kotlin-maven-noarg</artifactId>
            <version>${kotlin.version}</version>
        </dependency>
    </dependencies>
</plugin>
 
```

{% raw %}
<p></p>
{% endraw %}

## 如何更新

要更新IDEA插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“检查更新现在”按钮。另外，别忘了在Maven和Gradle构建脚本中更新编译器和标准库版本。
命令行编译器可以从中下载 [Github发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.0.6) 。
像往常一样，如果您遇到新版本的任何问题，欢迎您提供帮助 [论坛](https://discuss.kotlinlang.org/) ，在Slack（获得邀请） [这里](http://kotlinslackin.herokuapp.com/) ），或报告中的问题 [问题追踪器](https://youtrack.jetbrains.com/issues/KT) 。
让我们来吧！
