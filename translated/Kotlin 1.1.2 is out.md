---
title: "[译]Kotlin 1.1.2 is out"
date: 2017-04-25 21:19:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/04/kotlin-1-1-2-is-out/
translator:
translator_url:
---

我们很高兴宣布 Kotlin 1.1.2 正式发布了，这也是 Kotlin 1.1 的第二次 Bug 修复和工具更新。此次更新不仅提升了编译器和 IntelliJ IDEA 插件的性能，同时也在工具中增加了新的特性，当然还有各方面的问题修复。 此外，Kotlin 1.1.2 也提升了与 Android Gradle 插件版本 2.4.0-alpha 的兼容性。
本次发布版本的所有更新可在[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.2/ChangeLog.md)中查看。  
在这里要感谢所有外部的贡献者，他们提交的 pull request 也包含于该版本中：[Yoshinori Isogai](https://github.com/shiraji)，[Jonathan Leitschuh](https://github.com/JLLeitschuh)和[Kirill Rakhman](https://github.com/cypressious) 。感谢所有尝试 EAP 构建并向我们发送反馈意见的人！
## 迁移说明

Kotlin 编译器现在也需要基于 JDK 8 运行。但您应该不需要在意这一点改变，因为大多数其他 Java 开发工具（比如 Gradle 和 Android 工具）也需要 JDK 8，因此您肯定已经安装了 JDK 8。对于由编译器生成的代码，仍然默认兼容 Java 1.6，而且我们也没有计划要放弃对生成的 Java 1.6 兼容性字节码的支持。    

内部类当中不能再声明 object，因为这个 object 将能够访问外部类的实例，我们知道 object 始终是一个单例，因此这在理论上是行不通的。同样的，内部密封类也是不被允许的。然而这只是临时方案，在我们添加了在其外部类而非内部类中声明内部密封类的子类的可能性时，将会删除该限制。([KT-16232](https://youtrack.jetbrains.com/issue/KT-16232)，[KT-16233](https://youtrack.jetbrains.com/issue/KT-16233)）    

现在使用一个名称完全由下划线字符组成的声明时将必须使用反引号。([KT-16264](https://youtrack.jetbrains.com/issue/KT-16264)）

{% raw %}
<p><span id="more-4945"></span></p>
{% endraw %}

## Maven 增量编译

从 Kotlin 1.1.2 开始，以前用于 IntelliJ IDEA 和 Gradle 构建的增量编译现在也支持 Maven。启用该功能时，需要使用 -D 命令行参数或`proterties`标记设置`kotlin.compiler.incremental`属性为 true：

```kotlin
<properties>
    <kotlin.compiler.incremental>true</kotlin.compiler.incremental>
</properties>
```

## Maven 注解处理

现在可以从 Maven 构建中调用 Kotlin 的注解处理工具 kapt 了，只需要在`compile`前，从 kotlin-maven-plugin 中添加`kapt`的执行目标：

{% raw %}
<p></p>
{% endraw %}

```kotlin
<execution>
    <id>kapt</id>
    <goals>
        <goal>kapt</goal>
    </goals>
    <configuration>
        <sourceDirs>
            <sourceDir>src/main/kotlin</sourceDir>
            <sourceDir>src/main/java</sourceDir>
        </sourceDirs>
        <annotationProcessorPaths>
            <!-- Specify your annotation processors here. -->
            <annotationProcessorPath>
                <groupId>com.google.dagger</groupId>
                <artifactId>dagger-compiler</artifactId>
                <version>2.9</version>
            </annotationProcessorPath>
        </annotationProcessorPaths>
    </configuration>
</execution>


```

{% raw %}
<p></p>
{% endraw %}

在[这里](https://github.com/JetBrains/kotlin-examples/blob/master/maven/dagger-maven-example/pom.xml)查看具有 Java-Kotlin 代码支持和测试的 POM 文件完整示例。  

请注意，IntelliJ IDEA 自己的构建系统仍然不支持`kapt`。当您要重新运行注解处理时，需要从“Maven Projects”工具栏中启动构建。
## 内联方法重构

我们终于在 Kotlin 代码中实现了 Inline 方法（Function）的支持。
## 其他 IDE 改进

在 1.1.x 时间范围内，我们很大一部分的工作是致力于提高 IntelliJ IDEA 插件的性能。在此次发布的 1.1.2 版本中，我们对几项主要性能进行了改进，主要涉及输入响应，同时我们也已经为后续 1.1.3 版本进行了额外的重大改进。  

除此之外，我们还在此版本中进行了大量新的检测，快速解决方案和小型 IDE 功能。特别值得一提的是，在编辑器中支持折叠 Android String 资源引用，以及新的用于处理 Android API 版本问题的问题解决方案。
## 如何更新

要更新 IDEA 插件，在菜单栏中依次选择 Tools | Kotlin | Configure Kotlin Plugin Update，然后点击“Check for updates now”按钮。另外，不要忘记在 Maven 和 Gradle 构建脚本中更新编译器和标准库版本

命令行编译器可以从 [Github 发布页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1.1) 页面下载。
像往常一样，如果您在新版本中遇到任何问题，您可以在 [论坛](https://discuss.kotlinlang.org/) 中寻求帮助，在 Slack([获取邀请](http://kotlinslackin.herokuapp.com/))、或者在[问题追踪器](https://youtrack.jetbrains.com/issues/KT)提出问题 。  
让我们来吧！
