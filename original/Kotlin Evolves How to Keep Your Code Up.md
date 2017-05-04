---
title: "Kotlin Evolves: How to Keep Your Code Up"
date: 2015-06-17 16:46:00
author: ilya.gorbunov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/06/kotlin-evolves-how-to-keep-your-code-up/
translator:
translator_url:
---

Kotlin is undergoing finalization, and as part of the process we are **cleaning up**: revising the language and its libraries. The biggest changes have been made in [M12](http://blog.jetbrains.com/kotlin/2015/05/kotlin-m12-is-out/) , but some more are coming. The point is to perform all the necessary breaking changes before we release 1.0, so that we can keep the language and libraries **backwards-compatible** after the release.
The trick is both we, ourselves, and you, our users, have quite a bit of code written in Kotlin already, and we don’t want all that code broken hopelessly on each update (some breakages are inevitable, unfortunately, but we are doing our best). The general scheme of making changes in a user-friendly way is “deprecate-release-remove”, for example:

* in M12 we deprecated quite a few language constructs and library classes/functions,
* then we released M12, so that whenever you use those to-be-removed language and library features, the compiler issues warnings,
* in the next milestone we will remove those deprecated things completely, so that the compiler will issue errors instead of warnings.

So, if you have any deprecation warnings in your code, **now is just the right time to get rid of them**: the next major update will make all that code red, and your build will break.
## Getting rid of deprecation warnings

As mentioned above, there are two kinds of deprecation warnings: language deprecations and library deprecations. To get rid of them we provide several options.<br/>
<span id="more-2358"></span>
### Quick Fixes

With a *Quick Fix* you can fix a deprecation warning when you press `Alt+Enter` on it: available options will appear that fix an individual warning or all such warnings in the entire project. Deprecated language constructs and library functions will be replaced by newer versions.
Please note that for the quick fix to work correctly on library functions, **the sources of the standard library must be attached to your project**.
### Project-Wide Code Cleanup

Quick fixes are good when you have located the deprecated usage already, but since we have deprecated a lot of things recently, it may not be a viable option to look for each individual usage. In such a case, you can apply these fixes in bulk with an IDE action “*Analyze | Code Cleanup*“.
We provide an inspection named “*Usage of redundant or deprecated syntax or deprecated symbols*“. During the Cleanup, this inspection automatically replaces usages of obsolete language features or unnecessarily verbose code constructs with compact and up-to-date syntax, and usages of deprecated symbols — with their proposed substitutions.
### Manual Rewrite

In rare cases some deprecated usages can not be fixed automagically. These include usages of language constructs and library symbols that will be dropped without alternatives or can’t be rewritten without breaking the code, or when there are several options of rewriting the code, so that explicit choice is required.
**Bottom line**. How to get ready for Kotlin M13:<br/>
– install Kotlin M12 (ensure you have latest update of M12 installed),<br/>
– get rid of the deprecation warnings by means described above.
## Which API’s will definitely be dropped in M13

We’d like to share some of our plans about the API to be dropped in M13. This is not an exhaustive list of what will be dropped, but nevertheless.
### Streams

The big problem with Kotlin streams is that they conflict (by names) with streams in Java 8, and we can’t rely on Java 8 streams, because Kotlin targets earlier JDKs as well (think Android). So, sequences were introduced in M11 instead of streams, and streams are to be dropped.
### Iterator Utilities

Utility functions for iterators and some iterator classes were deprecated in favor of streams in M8, but streams are deprecated now too, so the ultimate inheritor of such functionality is `Sequence`.
### Sequence implementations

We have a bunch of sequence implementations in the Standard Library required to implement sequence operations, for example, `FilteringSequence` for `sequence.filter { predicate }`, `TransformingSequence` for `sequence.map { transform }` and so on. These implementation classes do not make much sense as part of the public API of the library, so we have deprecated them in M12 and are making them private in M13 (or dropping, from the user’s point of view :)).
### String.split and String.replaceFirst

Prior to M12 we had extension methods on string inherited from JDK: `split`, `replaceAll`/`replaceFirst`, `matches`. What they all have in common is that they take a string parameter and interpret it as a regular expression. This approach has two disadvantages.
Firstly, it requires compilation to a `Pattern` under the hood, which may have performance implications when used in a tight loop. This is explained in detail an article named [“Hidden evils of Java’s String.split() and replace()”](http://chrononsystems.com/blog/hidden-evils-of-javas-stringsplit-and-stringr) . We want to make every effort to avoid having articles named “Hidden evils of Kotlin’s something…” written in the future, so we decided, as usual, to make things explicit and introduced overloads of these functions that take `Regex` as a parameter where a regular expression is expected.
Secondly, it makes it difficult to introduce an overload taking a string and interpreting it as a literal. Willing to introduce such overloads in M12 for `split` and `replaceFirst`, we had to name them `splitBy` and `replaceFirstLiteral` respectively. But as soon as we drop the original deprecated overloads in M13, we’re going to rename these new methods back to `split` and `replaceFirst` (of course we’ll leave `splitBy` and `replaceFirstLiteral` deprecated and provide a substitution in their `deprecated` annotation).
It is also worth noting that the return type of `split` method has been changed: it now returns a `List&lt;String&gt;` instead of `Array&lt;String&gt;`, and the change of its behavior regarding removing empty substrings in the end. Following the principle of the least surprise we have relieved `split` from this inappropriate responsiblity, and nowinstead of `split(regex: String)` we should say `split(regex.toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()`. The IDE will help you migrate.
## Conclusion

We are going to make more changes in the Standard Library, but we have you covered with the code cleanup and quick fixes. Performing the code cleanup as described above for each Kotlin milestone before release will keep your code up to date.
