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

我们很高兴宣布Kotlin 1.1.2正式发布了，这也是Kotlin 1.1的第二次 Bug 修复和工具更新。此次更新不仅提升了编译器和 IntelliJ IDEA 插件的性能，同时也在工具中增加了新的特性，当然还有各方面的问题修复。 此外，Kotlin 1.1.2也提升了与Android Gradle插件版本2.4.0-alpha的兼容性。
本次发布版本的所有更新可在[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.2/ChangeLog.md)中查看。  
在这里要感谢所有外部的贡献者，他们提交的pull request也包含于该版本中：[Yoshinori Isogai](https://github.com/shiraji)，[Jonathan Leitschuh](https://github.com/JLLeitschuh)和[Kirill Rakhman](https://github.com/cypressious) 。感谢所有尝试EAP构建并向我们发送反馈意见的人！
## 迁移说明

Kotlin编译器现在也需要基于JDK 8运行。但您应该不需要在意这一点改变，因为大多数其他Java开发工具（比如Gradle和Android工具）也需要JDK 8，因此您肯定已经安装了JDK 8。对于由编译器生成的代码，仍然默认兼容Java 1.6，而且我们也没有计划要放弃对生成的Java 1.6兼容性字节码的支持。    

内部类当中不能再声明 object，因为这个 object 将能够访问外部类的实例，我们知道 object 始终是一个单例，因此这在理论上是行不通的。同样的，内部密封类也是不被允许的。然而这只是临时方案，在我们添加了在其外部类而非内部类中声明内部密封类的子类的可能性时，将会删除该限制。([KT-16232](https://youtrack.jetbrains.com/issue/KT-16232)，[KT-16233](https://youtrack.jetbrains.com/issue/KT-16233)）    

现在使用一个名称完全由下划线字符组成的声明时将必须使用反引号。([KT-16264](https://youtrack.jetbrains.com/issue/KT-16264)）

{% raw %}
<p><span id="more-4945"></span></p>
{% endraw %}

## Maven增量编译

从Kotlin 1.1.2开始，以前用于IntelliJ IDEA和Gradle构建的增量编译现在也支持Maven。启用该功能时，需要使用-D命令行参数或<code>proterties</code>标记设置<code>kotlin.compiler.incremental</code>属性为true：

```kotlin
<properties>
    <kotlin.compiler.incremental>true</kotlin.compiler.incremental>
</properties>
```

## Maven注解处理

现在可以从Maven构建中调用Kotlin的注解处理工具kapt了，只需要在<code>compile</code>前，从kotlin-maven-plugin中添加<code>kapt</code>的执行目标：

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

在[这里](https://github.com/JetBrains/kotlin-examples/blob/master/maven/dagger-maven-example/pom.xml)查看具有Java-Kotlin代码支持和测试的POM文件完整示例。  

请注意，IntelliJ IDEA自己的构建系统仍然不支持<code>kapt</code>。当您要重新运行注解处理时，需要从“Maven Projects”工具栏中启动构建。
## 内联方法重构

我们终于在Kotlin代码中实现了Inline方法（Function）的支持。
## 其他IDE改进

在1.1.x时间范围内，我们很大一部分的工作是致力于提高IntelliJ IDEA插件的性能。在此次发布的1.1.2版本中，我们对几项主要性能进行了改进，主要涉及输入响应，同时我们也已经为后续1.1.3版本进行了额外的重大改进。  

除此之外，我们还在此版本中进行了大量新的检测，快速解决方案和小型IDE功能。特别值得一提的是，在编辑器中支持折叠Android String资源引用，以及新的用于处理Android API版本问题的问题解决方案。
## 如何更新

要更新IDEA插件，在菜单栏中依次选择 Tools | Kotlin | Configure Kotlin Plugin Update，然后点击“Check for updates now”按钮。另外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本

命令行编译器可以从 [Github发布页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1.1) 页面下载。
像往常一样，如果您在新版本中遇到任何问题，您可以在 [论坛](https://discuss.kotlinlang.org/) 中寻求帮助，在Slack([获取邀请](http://kotlinslackin.herokuapp.com/))、或者在[问题追踪器](https://youtrack.jetbrains.com/issues/KT)提出问题 。  
让我们来吧！
