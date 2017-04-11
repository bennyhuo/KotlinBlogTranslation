---
title: Kotlin M5.2: IntelliJ IDEA 12.1 and Gradle
date: 2013-04-04 15:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/04/kotlin-m5-2-intellij-idea-12-1-and-gradle/
---

Another update of Kotlin comes out today. Welcome Kotlin M5.2. 
## Support for New IntelliJ IDEA

Koltin M5.2 supports (in fact, requires) the recently released IntelliJ IDEA 12.1.
The Kotlin IDE improvements include:

* Kotlin classes in the Class Hierarchy view. Just hit Ctrl+H on a class name to see its descendants and/or parents.
* Folding for imports (you don’t have to scroll through imports to get to your code any more).
* New UI for Kotlin library configuration: you can now control library names and location, and kotlin-runtime.jar is not copied to your project by default. It just works.
* Support for JavaScript-targeted modules is significantly improved.
* Optimizing imports on the fly: IDE Settings -> Editor -> Auto Import -> Optimize imports on the fly.
* New quick fixes: place the cursor on an error, and hit Alt+Enter.


{% raw %}
<p><a name="SAM-constructors"></a></p>
{% endraw %}

## SAM Constructors

When using Java libraries, you can now create an instance of a SAM interface (one with a Single Abstract Method) by calling its name and passing a function literal. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater(Runnable { doItNow() })
```

{% raw %}
<p></p>
{% endraw %}

This works only for Java classes. In fact, it is not a part of the language, but a feature of how Java classes are loaded into Kotlin: we define a synthesized function

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Runnable(body: () -> Unit) = object : Runnable {
    override fun run() {
        body()
    }
<span style="color: #222222;font-family: 'Courier 10 Pitch', Courier, monospace;line-height: 21px">}</span>
```

{% raw %}
<p></p>
{% endraw %}

So whenever you import Runnable, the function is there too, and you can use it.
This is the first chunk of SAM-conversion support for Java. Real SAM conversions will come soon, and you’ll be able to say simply

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater { doItNow(); }
```

{% raw %}
<p></p>
{% endraw %}

## New Gradle Plugin

Starting with M5.2, in addition to the long-available Maven plugin, there’s a Gradle plugin for Kotlin from JetBrains.
Here’s an example for building a Kotlin module with Gradle:

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
  repositories {
    mavenCentral()
    maven {
      url 'http://repository.jetbrains.com/all'
    }
  }
  dependencies {
    classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:0.1-SNAPSHOT'
  }
}
 
apply plugin: "kotlin"
 
repositories {
  mavenCentral()
  maven {
    url 'http://repository.jetbrains.com/all'
  }
}
 
dependencies {
  compile 'org.jetbrains.kotlin:kotlin-stdlib:0.1-SNAPSHOT'
}
```

{% raw %}
<p></p>
{% endraw %}

More examples & docs can be found here.
## Reminder: KAnnotator

Don’t forget that you now have KAnnotator at your service.
Have a nice Kotlin!
