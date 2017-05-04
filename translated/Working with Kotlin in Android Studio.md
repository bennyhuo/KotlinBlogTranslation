---
title: "[译]Working with Kotlin in Android Studio"
date: 2013-08-26 18:49:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/08/working-with-kotlin-in-android-studio/
translator:
translator_url:
---

随着 M6 的发布， [我们宣布支持 Android Studio](http://blog.jetbrains.com/kotlin/?p=1155) 。我们来深入了解如何使用 Android Studio 和 Kotlin 开始运行。<span id =“more-1234”> </span>
## 安装 Kotlin 插件

很像 IntelliJ IDEA，要安装 Kotlin 插件，您需要单击首选项（设置）并选择插件条目。最简单的方法是在对话框弹出时立即开始输入*插件*。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image5.png?resize=640%2C441&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

虽然我们可以从磁盘下载插件并进行安装，但最简单的方法是单击安装 JetBrains 插件...*，然后从列表中选择 Kotlin。右键单击并选择*下载并安装*

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image6.png?resize=640%2C524&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

按照说明重新启动 IDE。
# 设立项目

Android Studio 使用 Gradle 作为其构建系统，并且支持这种环境的部分工作正在为 Kotlin 添加 Gradle 支持。
## 为 Kotlin 添加源文件夹

典型的 Android 项目具有以下布局

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image7.png?resize=476%2C480&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;margin: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

其中项目的源代码位于文件夹*main / java*之下。由于我们想使用 Kotlin（我们可以将 Java 和 Kotlin 混合使用在同一个项目中），因此我们需要在*main*下创建一个名为“kotlin”的新文件夹。*在 Gradle 脚本中，我们稍后将此文件夹定义为源代码。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image8.png?resize=279%2C170&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}


{% raw %}
<p> </p>
{% endraw %}

## 配置 Gradle

我们需要在 Gradle 配置中设置一些依赖项和源文件夹。打开*build.gradle*文件并复制以下内容

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        **classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:0.6.+'**
        classpath 'com.android.tools.build:gradle:0.5.+'
    }
}
 
apply plugin: 'android'
**apply plugin: 'kotlin-android'**
 
repositories {
    mavenCentral()
}
 
dependencies {
    **compile 'org.jetbrains.kotlin:kotlin-stdlib:0.6.+'**
}
 
android {
    compileSdkVersion 17
    buildToolsVersion "17.0.0"
 
    defaultConfig {
        minSdkVersion 7
        targetSdkVersion 16
    }
    **sourceSets {
        main.java.srcDirs += 'src/main/kotlin'
    }**
}
```

{% raw %}
<p></p>
{% endraw %}

**更新**：将“**0.6。+**”替换为已安装的 Kotlin 插件版本。
相对于 Kotlin 的部分以粗体突出显示：

* 选择 Gradle 的 Kotlin 插件和我们正在使用的版本。 M6 版本对应于 0.6.69。
* 应用 kotlin-android 插件
* 导入 Kotlin 的标准库
* 指定源代码文件所在的位置

指定*sourceSet*将自动将我们之前创建的文件夹（*main / kotlin*）标记为 Android Studio 中的源根。
一旦我们更新了 Gradle 文件，我们应该能够成功构建用 Kotlin 编写的 Android 项目。
## Kotlin 的 Hello World

尝试使用 Android 的 Kotlin 最简单的方法是创建一个默认的 Android 项目，并将代码转换为 Kotlin，IDE 可以为我们做。

0. 创建一个新的 Android 项目（我们将省略创建新的 Android 项目的步骤）。

