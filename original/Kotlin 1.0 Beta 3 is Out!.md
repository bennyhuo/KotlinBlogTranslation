---
title: "Kotlin 1.0 Beta 3 is Out!"
date: 2015-12-07 15:45:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/12/kotlin-1-0-beta-3-is-out/
---

We are glad to present another update of Kotlin 1.0 Beta. We are working towards finalizing the standard library and getting rid of old deprecated constructs in the language, as well as bug fixes, performance improvements and future-proof checks.
Full list of changes is available  [here](https://youtrack.jetbrains.com/issues/KT?q=%23Major+%23Critical+%23Resolved+-Obsolete+-%7BEclipse+Plugin%7D+resolved+date%3A+2015-11-16+..+2015-11-30) .<br/>

See closed issues  [here](https://youtrack.jetbrains.com/issues/KT?q=%23Major+%23Critical+%23Resolved+-Obsolete+-%7BEclipse+Plugin%7D+resolved+date%3A+2015-11-16+..+2015-11-30) .<span id="more-3263"></span>
## Library Changes

We are working hard on the standard library to get it into the best shape before 1.0. This involves some experimentation, so new deprecations happen and new functions are added. We are planning to make the final clean-up of the standard library in the 1.0 build (or RC): remove all the deprecations and other legacy stuff.
Here we give only one highlight from the  [changes](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-3595) : <code>contains()</code> and other similar extensions now accept supertypes of the element of the collection.

{% raw %}
<p></p>
{% endraw %}

```kotlin
// strs: Collection<String>
// ns: String?
// cs: CharSequence
// i: Int
strs.contains(ns) // accepted now
strs.contains(cs) // accepted now
str.contains(i) // ERROR (in fact, a deprecation warning, but will be an error soon)
 
```

{% raw %}
<p></p>
{% endraw %}

We found that the previously proposed <code>containsRaw</code> approach is inefficient, and opted for making <code>contains()</code> a bit more permissive, while keeping the initially intended safety. Note that the collection interfaces themselves are intact, and all this is done solely through extension functions. Use <em>Code Cleanup</em> to migrate your code.
## Language Changes

Some highlights from the language changes, the full list is available  [here](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-3595) .<br/>

Many things that we deprecated before, have now become errors. Use <em>Code Cleanup</em> to migrate.
### When expressions

This kind of code has proven to be problematic, so we decided to deprecate it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
when {
    foo.isValid(), foo.isReady() -> process(foo)
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

Many people tend to think that the condition “<code>foo.isValid(), foo.isReady()</code>” means that <code>foo</code> is <strong>both</strong> valid <strong>and</strong> ready, while actually the comma means <em>or</em>. The workaround is trivial: simply use <code>||</code> instead:

{% raw %}
<p></p>
{% endraw %}

```kotlin
when {
    foo.isValid() || foo.isReady() -> process(foo)
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

<em>Code Cleanup</em> will migrate it for you.
### Annotations

A bug has been fixed that prevented us from using arrays in default values for annotation parameters:

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class Entry(val value: String)
 
annotation class Example(
        val entries: Array<Entry> = arrayOf(Entry("a"), Entry("b")) // OK now
)
 
```

{% raw %}
<p></p>
{% endraw %}

### Enum.values()

Recently we changed the traditional Java’s <code>Enum.values()</code> to be a property: <code>Enum.values</code>, but now we are rolling this change back, because there’s an unpleasant corner case: a constant in an enum may be named <code>values</code>, and there’s no way to access one of the two then. We considered different options, and decided that changing <code>values</code> back to a function is the cleanest.
So, the <code>values</code> property is now deprecated, and <code>values()</code> function — un-deprecated.
### Visibilities and scoping rules

We are cleaning up and fixing minor issues in visibilities and scoping rules, so

* protected members are allowed in companion objects
* Calls to non-@JvmStatic protected members of companion objects from subclasses are marked as errors (unsupported)
* private setters are now deprecated for open properties
* Local sealed classes are deprecated (never were usable)
* Overriding setter cannot weaken visibility
* Inner classes are no longer allowed inside enum entries
* Use of uninitialized variables in lambdas / object literals / local functions is forbidden

## Android Extensions

We have merged the main Kotlin plugin for IntelliJ IDEA and the <em>Kotlin Extensions For Android</em> plugin. The latter is now obsolete as its functionality is available from the main Kotlin plugin.
Also, we have added support for Android <strong>product flavors</strong>: now properties from different flavours are available in different packages.
For example, if we have two flavors in the <code>build.gradle</code> file:

{% raw %}
<p></p>
{% endraw %}

```kotlin
productFlavors {
    free {
        versionName "1.0-free"
    }
    pro {
        versionName "1.0-pro"
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

We can now use synthetic properties not only for layouts in the <code>main</code> source set, but also for the flavor layouts:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Import synthetic properties for the `activity_free.xml` layout in the `free` flavor
import kotlinx.android.synthetic.free.activity_free.versionMarker
 
class FreeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
 
        setContentView(R.layout.activity_free)
 
        ...
 
        versionMarker.text = "Free version"
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Note that all layouts for the main source set are now located under the <code>kotlinx.android.synthetic.main</code> package, and the old package naming convention is deprecated.
## What’s new in the IDE


* Android Extensions plugin has been merged into the main Kotlin plugin and no longer needs to be installed separately
* We’ve added option to choose Kotlin when creating a new Gradle project:
* Debugger: stacktrace navigation now supports stack frames from inline functions. Also there were a bunch of improvements in a stepping through inline functions.
* Three new property initialization Quick Fixes have been added:
* Introduce Variable (Ctrl+Alt+V / Cmd+Alt+V) now supports multi-declaration expressions:
* Also it allows choosing container for expression in lambda or anonymous functions:
* Beta 3 brings support of Introduce Variable/Parameter/Property/Function from string template fragments
* Finally, one experimental feature has been added — basic support for Kotlin script files (.kts) in the IDE

