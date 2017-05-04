---
title: "Why JetBrains needs Kotlin"
date: 2011-08-02 15:52:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/08/why-jetbrains-needs-kotlin/
translator:
translator_url:
---

The question of motivation is one of the first asked when someone learns that someone else is working on a new programming language. Kotlin documentation offers a fairly detailed overview of why the language exists. Still, we would like to make it clearer what exactly JetBrains expects to gain from the whole endeavor. We’re obviously in it for the long run, and yes, we realize it will take years to reach our goals. And here’s why we are willing to make this investment.
First and foremost, it’s about our own productivity. Although we’ve developed support for several JVM-targeted programming languages, we are still writing all of our IntelliJ-based IDEs almost entirely in Java. The IntelliJ build system is based on Groovy and Gant, some Groovy is also used for tests, there is some JRuby code in RubyMine, and that’s it. We want to become more productive by switching to a more expressive language. At the same time, we cannot accept compromises in terms of either Java interoperability (the new language is going to be introduced gradually, and needs to interoperate smoothly with the existing code base) or compilation speed (our code base takes long enough to compile with javac, and we cannot afford making it any slower).
The next thing is also fairly straightforward: we expect Kotlin to drive the sales of IntelliJ IDEA. We’re working on a new language, but we do not plan to replace the entire ecosystem of libraries that have been built for the JVM. So you’re likely to keep using Spring and Hibernate, or other similar frameworks, in your projects built with Kotlin. And while the development tools for Kotlin itself are going to be free and open-source, the support for the enterprise development frameworks and tools will remain part of IntelliJ IDEA Ultimate, the commercial version of the IDE. And of course the framework support will be fully integrated with Kotlin.
The final point is less obvious but still important: new programming languages is a topic that many people really enjoy talking about, and the first days that have passed since we’ve unveiled Kotlin prove that. We see that people who are already familiar with JetBrains trust the company to be able to do a good job with this project. Thus, we believe that this trust and the increasing community awareness of JetBrains will not only drive the company’s business, but will attract even more people to our approach to building development tools, and let them Develop with Pleasure.
And we’d like to reiterate that our work on Kotlin does not in any way affect our investment into other development tools, and in particular the Scala plugin. If you’re already happy with Scala and have no need for another new language, we’ll continue to do our best providing you with first-class Scala development tooling.
