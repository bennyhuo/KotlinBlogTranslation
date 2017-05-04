---
title: "Working with Kotlin in Android Studio"
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

With the release of M6, [we announced support for Android Studio](http://blog.jetbrains.com/kotlin/?p=1155) . Let’s take a deeper look at how to get up and running with Android Studio and Kotlin.<span id="more-1234"></span>
## Installing the Kotlin Plugin

Much like with IntelliJ IDEA, to install the Kotlin plugin you need to click on Preferences (Settings) and select the Plugins entry. Easiest way is to just start typing *plugin*as soon as the dialog pops up.

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image5.png?resize=640%2C441&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

Although we can download the plugin and install from disk, the easiest way is to click on the *Install JetBrains plugin…*and select Kotlin from the list. Right-click and choose *Download and Install*

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image6.png?resize=640%2C524&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

Follow the instructions to restart the IDE.
# Setting up the Project

Android Studio uses Gradle as its build system and part of the effort involved in supporting this environment was adding Gradle support for Kotlin.
## Adding Source folder for Kotlin

A typical Android Project has the following layout

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image7.png?resize=476%2C480&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;margin: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}

where the source code for the project is located under the folder*main/java*. Since we want to use Kotlin (we can mix and match both Java and Kotlin the same project), we need to create a new folder under *main*, named *kotlin.*In the Gradle script we’ll later define this folder as a source root.

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image8.png?resize=279%2C170&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/></p>
{% endraw %}


{% raw %}
<p> </p>
{% endraw %}

## Configuring Gradle

We need to set up some dependencies and source folders in the Gradle configuration. Open the *build.gradle* file and copy the following

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

**Update**: Replace “**0.6.+**” with the version of Kotlin plugin you have installed.
The parts relative to Kotlin are highlighted in bold:

* Select the Kotlin plugin for Gradle and the version we’re using. The M6 release corresponds to 0.6.69.
* Apply the kotlin-android plugin
* Import the Kotlin’s standard library
* Specifiy where the source code files are located

Specifying the *sourceSet*will automatically mark the folder we created previously (*main/kotlin*) as a Source Root in Android Studio.
Once we have the Gradle file updated, we should be able to successfully build Android project written in Kotlin.
## Hello World with Kotlin

The easiest way to try out Kotlin with Android is to create a default Android project and convert the code to Kotlin, which the IDE can do for us.

0. Create a new Android Project (we’ll omit the steps for creating new Android projects).

