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
 * 支持缺省包可空性注解  
 * 提升对JAVA 9的支持  
 * 添加@Parcelize注解生成Android Parcelable实现的初始支持(实验性)  
 * 添加用于删除JavaScript无用代码的工具，提升对JS调试源映射的支持，并支持JS单元测试  
 * 生成更高效的字节码
 * IntelliJ IDEA诸多新特性   

本次更新适用于2016.2至2017.2间所有版本的IntellJ IDEA以及Android Studdio 2.3以及3.0 Beta版。

查看完整更新[日志](https://github.com/JetBrains/kotlin/blob/1.1.4/ChangeLog.md)。

{% raw %}
<p><span id="more-5184"></span></p>
{% endraw %}

感谢在本次发布中向我们提交PR的贡献者们[Andrius Semionovas](https://github.com/neworld)，[Bill Collins](https://github.com/mrginglymus)，[Derek Alexander](https://github.com/alexanderdr)，[Dimach](https://github.com/Dimach)，[Ilya Zorin](https://github.com/geralt-encore)，[Kirill Rakhman](https://github.com/cypressious)，[Stuart Kent](https://github.com/stkent)，[takahirom](https://github.com/takahirom)，[Toshiaki Kameyama](https://github.com/t-kameyama)，[Vasily Kirichenko](https://github.com/vasily-kirichenko)，[Vitaly Khudobakhshov](https://github.com/khud)，[Vladimir Koshelev](https://github.com/vedun-z)，[Yoshinori Isogai](https://github.com/shiraji)，[Yuli Fiterman](https://github.com/fitermay)以及[Zoltan Polgar](https://github.com/Pozo)。  

## 包缺省可空性注解

自本次发布的版本开始，Kotlin支持缺省包可空性注解（例如JSR-305的[```@ParametersAreNonnullByDefault```](http://static.javadoc.io/com.google.code.findbugs/jsr305/3.0.1/javax/annotation/ParametersAreNonnullByDefault.html)以及Spring框架5.0中引入的[```@NonNullApi```](https://github.com/spring-projects/spring-framework/blob/master/spring-core/src/main/java/org/springframework/lang/NonNullApi.java)注解）。为了迁移方便，以及避免由于使用精确Java API可空性信息而导致的编译错误，默认情况下此类注解均已关闭，需要向编译器传递```-Xjsr305-annotations = enable```的命令来启用。在Gradle中启用此功能，使用[freeCompilerArgs option](http://kotlinlang.org/docs/reference/using-gradle.html#attributes-common-for-jvm-and-js)； 在Maven构建中使用[args](http://kotlinlang.org/docs/reference/using-maven.html#attributes-common-for-jvm-and-js)；更多详细内容，请参阅[建议规范](https://github.com/Kotlin/KEEP/pull/78)。

## Java 9支持

我们将继续推进Java 9的支持。在本次发布的版本中，Kotlin基于module-info.java的信息执行基于模块的可见性检查。现已支持在JDK 9下运行编译器。

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

Kotlin 1.1.4改进了对JavaScript源代码生成的支持，从而更容易在浏览器调试器（如Chrome DevTools）中调试JS。有关详细信息，请参阅本[教程](https://kotlinlang.org/docs/tutorials/javascript/debugging-javascript/debugging-javascript.html)。
## JavaScript单元测试

本次更新扩展了JavaScript单元测试支持，以便与更多种类的库共同使用。有关更多信息和示例项目的链接，请访问[论坛帖子](https://discuss.kotlinlang.org/t/unit-testing-in-kotlin-js/3943)。
## 字节码质量提升

在本次更新中，我们为生成字节码的质量实施了诸多改进。命名挂起功能的异常现在源于函数本身，这使得它们的堆栈跟踪器更易于阅读，并且字节码在许多情况下表现更好。
## IntelliJ IDEA插件改进

新版本为IntelliJ IDEA插件带来了许多改进：

* 主要业绩改善
* 新的重构？

现在可以使用带有访问器的属性来重构
* 现在支持重命名标签
* 代码样式设置中有许多新的选项
* 数据流分析支持（分析|分析数据流从/到这里）
* 在项目中配置Kotlin？现在支持使用Gradle Kotlin DSL的项目
* 许多新的检查和quickfixes

## 如何更新

要更新插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“淐呵呵更新” - 按钮。此外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本。
像往常一样，如果您遇到新版本的任何问题，欢迎您在论坛上，Slack（在这里获得邀请）请求帮助，或者在问题跟踪器中报告问题。
让檚ot！
