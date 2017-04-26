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
---

我们很高兴地宣布发布Kotlin 1.1.2，Kotlin 1.1的第二个修补程序和工具更新。该更新为编译器和IntelliJ IDEA插件，工具中的几个新功能以及所有领域的许多错误修复带来性能改进。 Kotlin 1.1.2还带来了与Android Gradle插件版本2.4.0-alpha的兼容性。
此版本中完整的更改列表可以在 [更新日志](https://github.com/JetBrains/kotlin/blob/1.1.2/ChangeLog.md) 。
我们要感谢我们的外部贡献者，他们的引用请求被包含在这个版本中： [Yoshinori Isogai](https://github.com/shiraji) ， [乔纳森·雷茨楚](https://github.com/JLLeitschuh)  和 [基拉里·拉赫曼](https://github.com/cypressious) 。感谢所有尝试EAP构建的人，并向我们发送反馈意见！
## 迁移说明

Kotlin编译器现在需要运行JDK 8。您不应该注意到任何更改，因为大多数其他Java开发工具（如Gradle和Android工具链）也需要JDK 8，因此您几乎肯定已经安装了。对于由编译器生成的代码，Java 1.6兼容性仍然是默认值，我们没有计划放弃生成Java 1.6兼容字节码的支持。
一个内部类不能再声明一个对象。这样的对象将能够访问外部类实例，这在概念上是不可能的，因为对象始终是单例。内部密封类也被禁止。这是一个暂时的限制，当我们添加在其外部类中声明内部类的内部类的可能性，而不在内部类本身时，这将被删除。 （ [KT-16232](https://youtrack.jetbrains.com/issue/KT-16232) ， [KT-16233](https://youtrack.jetbrains.com/issue/KT-16233) ）
使用一个名称完全由下划线字符组成的声明，现在总是需要反引号。 （ [KT-16264](https://youtrack.jetbrains.com/issue/KT-16264) ）

{% raw %}
<p><span id="more-4945"></span></p>
{% endraw %}

## Maven增量编译

由于Kotlin 1.1.2，以前可用于IntelliJ IDEA和Gradle构建的增量编译现在支持Maven。要启用，请使用-D命令行参数或<code>属性</ code>标记将<code> kotlin.compiler.incremental </ code>属性设置为true：

{% raw %}
<p></p>
{% endraw %}

```kotlin
<properties>
    <kotlin.compiler.incremental>true</kotlin.compiler.incremental>
</properties>
 
```

{% raw %}
<p></p>
{% endraw %}

## Maven注释处理

Kotlin的注释处理工具kapt现在可以从Maven构建中调用。在<code> compile </ code>之前，只需从kotlin-maven-plugin中添加<code> kapt </ code>目标的执行：

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

 [这里](https://github.com/JetBrains/kotlin-examples/blob/master/maven/dagger-maven-example/pom.xml)  是具有Java-Kotlin代码支持和测试的POM文件的完整示例。
请注意，IntelliJ IDEA自己的构建系统仍然不支持<code> kapt </ code>。当您要重新运行注释处理时，从“Maven Projects”工具栏启动构建。
## 内联方法重构

我们终于在Kotlin代码中实现了Inline方法（Function）的支持。
## 其他IDE改进

我们在1.1.x时间范围内的很大一部分工作致力于提高IntelliJ IDEA插件的性能。在1.1.2版本中，我们发布了几项主要的性能改进，主要影响到响应性，我们已经为1.1.3版本提供了额外的重大改进。
除此之外，我们已经在此版本中实施了大量新的检测，quickfix和小型IDE功能。特别值得一提的是，在编辑器中支持折叠Android String资源引用，以及用于处理Android API版本问题的新的quickfix。
## 如何更新

要更新插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“检查更新现在”按钮。另外，别忘了在Maven和Gradle构建脚本中更新编译器和标准库版本。
像往常一样，如果您遇到新版本的任何问题，欢迎您提供帮助 [论坛](https://discuss.kotlinlang.org/) ，在Slack（获得邀请） [这里](http://kotlinslackin.herokuapp.com/) ），或报告中的问题 [问题追踪器](https://youtrack.jetbrains.com/issues/KT) 。
让我们来吧！
