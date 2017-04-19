---
title: "Kotlin 1.1 Beta 2 is here"
date: 2017-02-02 23:24:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/02/kotlin-1-1-beta-2-is-here/
---

We’re happy to announce the second beta of Kotlin 1.1. Please give the new version a try – your feedback is essential for ensuring that we can deliver a quality release.
Since the first beta release, we’ve mostly been focused on stability, bugfixes, and improving the key focus areas of this release: coroutine support and the JavaScript backend. The full list of changes since 1.1 Beta can be found in the [changelog](https://github.com/JetBrains/kotlin/blob/0e1b61b422bd0d006158d8b68fa34e960853c5c6/ChangeLog.md) . And if you’re interested in a recap of everything added in version 1.1, check out our [what’s new page](https://kotlinlang.org/docs/reference/whatsnew11.html) .

{% raw %}
<p><span id="more-4562"></span></p>
{% endraw %}

## Migration Notes

For JavaScript projects, we’ve changed the name of the artifact for the standard library. Instead of <code>kotlin-js-library</code>, it is now <code>kotlin-stdlib-js</code>. You’ll need to update your Maven and Gradle scripts accordingly when you update to 1.1 beta 2 or a newer build.
In addition to that, testing support classes (in the package <code>kotlin.test</code>) for JavaScript are now packaged as a separate artifact, as it was previously done for the Java version. If you’re using kotlin.test in your JS project, add a dependency on <code>kotlin-test-js</code>.
The coroutines APIs in the Kotlin standard library have been moved to the <code>kotlin.coroutines.experimental</code> package; you need to update your imports if you’ve used these APIs in your code. See [Andrey’s forum post](https://discuss.kotlinlang.org/t/experimental-status-of-coroutines-in-1-1-and-related-compatibility-concerns/2236) for the background on this change.
We’ve also made it easier to enable the experimental coroutine support in your Gradle projects. Instead of editing gradle.properties, you can add the following snippet to your build.gradle:

{% raw %}
<p></p>
{% endraw %}

```kotlin
kotlin {
    experimental {
        coroutines 'enable'
    }
}
```

{% raw %}
<p></p>
{% endraw %}

If you’re using the [kotlinx.coroutines library](https://github.com/kotlin/kotlinx.coroutines) , please update your dependency to version <code>0.6-beta</code>. Earlier versions of the library are incompatible with this Kotlin update.
## New Features

We did add a few last-minute features in this beta. Here are the most important ones:

* The compiler now reports a warning if you declare an extension that has the same signature as a member of the same class and will always be shadowed (for example, String.length())
* Type inference for member references passed to generic functions is now much improved (KT-10711)
* The minus operator can now be used with maps, returning a copy of the map with the given keys removed. The -= operator can be used on mutable maps to remove the given keys from the map.
* It is now possible to access the delegate instance of a delegated property using KPropertyN.getDelegate() (see KT-8384 for details);
* Intention (contributed by Kirill Rakhman) to merge two nested if statements;
* Support for building Android projects when the Jack toolchain is enabled (jackOptions { true });
* Intention (contributed by Kirill Rakhman) to generate View constructors in Android applications.

## Source Compatibility with Kotlin 1.0

Another area to which we paid a lot of attention in this update is <strong>source compatibility with Kotlin 1.0</strong>. This allows you to try Kotlin 1.1, even if your team is using Kotlin 1.0, without worrying that you’ll break the build by using some of the features added in the new release.
To enable the compatibility mode:

* For Maven, Ant and the command-line compiler, set the -language-version compiler argument to 1.0.
* In a Gradle build, add kotlinOptions { languageVersion = "1.0" } to your compileKotlin task.
* In the IDE, specify the language version in the Kotlin facet settings or in Settings | Build, Execution, Deployment | Compiler | Kotlin Compiler

## How to try it

<strong>In Maven/Gradle:</strong> Add <code>http://dl.bintray.com/kotlin/kotlin-eap-1.1</code> as a repository for the build script and your projects; use <code>1.1.0-beta-38</code> as the version number for the compiler and the standard library.
<strong>In IntelliJ IDEA:</strong> Go to <em>Tools → Kotlin → Configure Kotlin Plugin Updates</em>, then select “Early Access Preview 1.1” in the <em>Update channel</em> drop-down list, then press <em>Check for updates</em>.
The command-line compiler can be downloaded from the [Github release page](https://github.com/JetBrains/kotlin/releases/tag/v1.1-beta2) .
<strong>On <a href="http://try.kotlinlang.org/">try.kotlinlang.org</a></strong>. Will be available soon.
Let’s Kotlin!
