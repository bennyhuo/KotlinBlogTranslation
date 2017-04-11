---
title: [译]Working with Kotlin in Android Studio
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
---

随着M6的发布，我们宣布支持Android Studio。我们来深入了解如何通过Android Studio和Kotlin开始运行。
## 安装Kotlin插件

很像IntelliJ IDEA，要安装Kotlin插件，您需要单击首选项（设置）并选择插件条目。最简单的方法是在对话框弹出时立即开始输入插件。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image5.png?resize=640%2C441&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

虽然我们可以从磁盘下载插件并安装，但最简单的方法是单击安装JetBrains插件，然后从列表中选择Kotlin。右键单击并选择“下载并安装”

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image6.png?resize=640%2C524&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

按照说明重新启动IDE。
# 设立项目

Android Studio使用Gradle作为其构建系统，并且支持这种环境的部分工作正在为Kotlin添加Gradle支持。
## 为Kotlin添加源文件夹

典型的Android项目具有以下布局

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image7.png?resize=476%2C480&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;margin: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

项目的源代码位于文件夹main / java下。由于我们想使用Kotlin（我们可以混合和匹配Java和Kotlin相同的项目），我们需要在main下创建一个名为kotlin的新文件夹。在Gradle脚本中，我们稍后将此文件夹定义为源根。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image8.png?resize=279%2C170&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}


{% raw %}
<p> </p>
{% endraw %}

## 配置Gradle

我们需要在Gradle配置中设置一些依赖项和源文件夹。打开build.gradle文件并复制以下内容

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        <strong>classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:0.6.+'</strong>
        classpath 'com.android.tools.build:gradle:0.5.+'
    }
}
 
apply plugin: 'android'
<strong>apply plugin: 'kotlin-android'</strong>
 
repositories {
    mavenCentral()
}
 
dependencies {
    <strong>compile 'org.jetbrains.kotlin:kotlin-stdlib:0.6.+'</strong>
}
 
android {
    compileSdkVersion 17
    buildToolsVersion "17.0.0"
 
    defaultConfig {
        minSdkVersion 7
        targetSdkVersion 16
    }
    <strong>sourceSets {
        main.java.srcDirs += 'src/main/kotlin'
    }</strong>
}
```

{% raw %}
<p></p>
{% endraw %}

更新：将“0.6。+”替换为您安装的Kotlin插件版本。
相对于Kotlin的部分以粗体突出显示：

* 选择Gradle的Kotlin插件和我们正在使用的版本。 M6版本对应于0.6.69。
* 应用kotlin-android插件
* 导入Kotlin的标准库
* 指定源代码文件所在的位置

指定sourceSet将自动将我们以前创建的文件夹（main / kotlin）标记为Android Studio中的源根。
一旦我们更新了Gradle文件，我们应该能够成功构建用Kotlin编写的Android项目。
## Kotlin的Hello World

尝试使用Android的Kotlin最简单的方法是创建一个默认的Android项目，并将代码转换为Kotlin，IDE可以为我们做。

0. 创建一个新的Android项目（我们将省略创建新的Android项目的步骤）。

