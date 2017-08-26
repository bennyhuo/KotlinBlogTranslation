---
title: Kotlin 1.1.4 is out
author: Dmitry Jemerov
date: 2017-08-15 10:38:00
source_url: https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-1-4-is-out/
tags: 
categories:  官方动态
---


Kotlin 1.1.4来啦！本次更新主要包括：
  
 * IntelliJ IDEA插件主要性能回归修正  
 * 缺省包可空性注解支持  
 * 提升对JAVA 9的支持  
 * 添加@Parcelize注解生成Android Parcelable实现的初始支持(实验性)  
 * 添加用于删除JavaScript无用代码的工具，提升对JS调试源映射的支持，并支持JS单元测试  
 * 更高效率的字节码
 * IntelliJ IDEA其它新特性   

本次更新适用于2016.2至2017.2所有版本的IntellJ IDEA以及Android Studdio 2.3以及3.0 Beta版。

查看完整[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.4/ChangeLog.md)。

{% raw %}
<p><span id="more-5184"></span></p>
{% endraw %}

感谢在本次发布中向我们提交PR的贡献者们[Andrius Semionovas](https://github.com/neworld)，[Bill Collins](https://github.com/mrginglymus)，[Derek Alexander](https://github.com/alexanderdr)，[Dimach](https://github.com/Dimach)，[Ilya Zorin](https://github.com/geralt-encore)，[Kirill Rakhman](https://github.com/cypressious)，[Stuart Kent](https://github.com/stkent)，[takahirom](https://github.com/takahirom)，[Toshiaki Kameyama](https://github.com/t-kameyama)，[Vasily Kirichenko](https://github.com/vasily-kirichenko)，[Vitaly Khudobakhshov](https://github.com/khud)，[Vladimir Koshelev](https://github.com/vedun-z)，[Yoshinori Isogai](https://github.com/shiraji)，[Yuli Fiterman](https://github.com/fitermay)以及[Zoltan Polgar](https://github.com/Pozo)。  

## 包缺省可空性注解

自本次版本发布开始，Kotlin支持缺省包可空性注解（例如JSR-305的[```@ParametersAreNonnullByDefault```](http://static.javadoc.io/com.google.code.findbugs/jsr305/3.0.1/javax/annotation/ParametersAreNonnullByDefault.html)以及Spring框架5.0中引入的[```@NonNullApi```](https://github.com/spring-projects/spring-framework/blob/master/spring-core/src/main/java/org/springframework/lang/NonNullApi.java)注解）。为了迁移方便，同时避免由于使用精确Java API可空性信息而导致的编译错误，默认情况下此类注解均已关闭，启用时需向编译器传递```-Xjsr305-annotations = enable```命令。在Gradle中启用此功能，请使用[freeCompilerArgs option](http://kotlinlang.org/docs/reference/using-gradle.html#attributes-common-for-jvm-and-js)； 在Maven构建中使用[args](http://kotlinlang.org/docs/reference/using-maven.html#attributes-common-for-jvm-and-js)；更多详细内容，请参阅[建议规范](https://github.com/Kotlin/KEEP/pull/78)。

## Java 9支持

我们将继续推进对Java 9的支持。在本次发布的版本中，Kotlin基于module-info.java的信息执行基于模块的可见性检查。现已支持在JDK 9下运行编译器。

## Android Extensions插件增强

Android Extensions插件现在不仅支持Activities和Fragments，同时还支持自定义控件，甚至支持自定义布局容器（如[ViewHolder](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.ViewHolder.html)）。此外，现已完全支持[Build Variant](https://developer.android.com/studio/build/build-variants.html)。  

更多详细内容请参阅[KEEP建议](https://github.com/Kotlin/KEEP/blob/master/proposals/android-extensions-entity-caching.md)。以上内容目前均为实验性质，因此需要在build.gradle文件中添加如下参数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
androidExtensions {
    experimental = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Parcelable支持

Android Extensions插件包含自动实现[Parcelable](https://developer.android.com/reference/android/os/Parcelable.html)的生成器。在主构造函数中声明序列化属性，添加```@Parcelize```注解后，将自动创建```writeToParcel()/createFromParcel()```方法。

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Parcelize
class User(val firstName: String, val lastName: String) : Parcelable
 
```

{% raw %}
<p></p>
{% endraw %}

Parcelable生成器目前处于实验状态，我们无法确保其兼容性。欢迎您随时向我们反馈API使用情况。更多详细内容，请参阅[建议规范](https://github.com/Kotlin/KEEP/blob/master/proposals/extensions/android-parcelable.md) 。

## JavaScript无用代码删除

Kotlin 1.1.4中新增加了用于删除由Kotlin/JS编译器生成的.js文件中无用代码的工具。目前此工具仅在Gradle构建中受支持；若需启用，在build.gradle中添加```apply plugin: 'kotlin-dce-js'```。有关详细信息，请参阅[文档](https://kotlinlang.org/docs/reference/javascript-dce.html)。
## JavaScript调试

Kotlin 1.1.4优化了对JavaScript源代码生成的支持，从而更容易在浏览器调试器（如Chrome DevTools）中调试JS。有关详细信息，请参阅[本教程](https://kotlinlang.org/docs/tutorials/javascript/debugging-javascript/debugging-javascript.html)。
## JavaScript单元测试

本次更新扩展了JavaScript单元测试支持，以便与更多种类的库共同使用。有关更多信息和示例项目的链接，请访问[论坛](https://discuss.kotlinlang.org/t/unit-testing-in-kotlin-js/3943)。
## 字节码质量提升

在本次更新中，我们为生成字节码的质量实施了诸多优化。命名挂起函数的异常现在由函数本身抛出，更易于阅读和追踪堆栈信息，并且字节码在多数情况下表现更强大。

## IntelliJ IDEA插件优化

新发布的版本对IntelliJ IDEA插件有着显著提升：

* 主要性能提升
* 新的重构“复制类”  
* 含有访问器的属性可使用"inline"重构
* 支持重命名标签
* 更多的代码样式风格设置选项
* [数据流分析支持](https://www.jetbrains.com/help/idea/analyzing-data-flow.html)，在菜单栏中选择(Analyze | Analyze Data Flow from/to Here)
* "配置Kotlin项目"现已支持使用[Gradle Kotlin DSL](https://github.com/gradle/kotlin-dsl)的工程
* 其它新检查和快速修复

## 如何更新

要更新插件，请在菜单栏中选择Tools | Kotlin | Configure Kotlin Plugin Updates，点击"Check for updates now"按钮。当然，不要忘记同步更新编译器以及Maven和Gradle脚本中的标准库版本。  

与往常一样，如果您在新版本中遇到任何问题，欢迎您在[论坛](https://discuss.kotlinlang.org/)、Slack（获得[邀请](http://slack.kotlinlang.org/)）上寻求帮助，或者在[问题跟踪器（issue tracker）](https://youtrack.jetbrains.com/issues/KT)中反馈问题。  

Let's Kotlin!
