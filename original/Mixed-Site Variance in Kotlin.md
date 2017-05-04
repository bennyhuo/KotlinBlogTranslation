---
title: "Mixed-Site Variance in Kotlin"
date: 2013-06-26 12:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/06/mixed-site-variance-in-kotlin/
translator:
translator_url:
---

<img alt="" class="alignleft" data-recalc-dims="1" src="https://i2.wp.com/www.geoffwilkins.net/images/feynman/feynman-blackboard.jpg?resize=360%2C272&amp;ssl=1"/>Type systems… We all know they are cool. In a static language, like Kotlin, the type system is the one responsible for early detection of errors. Many tools (e.g. an IDE with its refactoring abilities) also rely on the type system.
We also know that type systems are hard: many computer scientists built their entire careers studying type systems. Yet we know rather little about type systems of main-stream languages.<span id="more-1112"></span>
For example, take a simple question: “We have two Java types, say, A and B; can I assign a value of type A to a variable of type B?” (In other words, “Is A a subtype of B?”) For some languages (e.g. C#) we know that there’s an algorithm that takes A and B, thinks for some time, then terminates and gives a correct answer: “Yes” or “No”. In other words, the subtyping problem is <em>decidable</em> for C#. For some other languages we know that there can be no such algorithm: whatever compiler you write, there will be a pair of types A and B on which it either gives a wrong answer, never terminates or throws an exception (which can be viewed as a wrong answer too). In other words, subtyping is <em>undecidable</em> for Scala (in fact, Scala’s type system is [Turing-complete](http://michid.wordpress.com/2010/01/29/scala-type-level-encoding-of-the-ski-calculus/) , i.e. you can make Scala’s type checker perform any computation, including an infinite loop).
What about Java? We don’t know (see [this paper](http://www.cs.cornell.edu/~ross/publications/tamewild/) , for example). Some people suspect that subtyping is undecidable for Java, but this has not been proved to this day. <strong>Is this a practical question?</strong> Oh, yes it is. Some people want to add reified generics to Java, which means that <strong>foo instanceof Bar </strong>would be checking whether the run-time type of foo is a subtype of Bar. And if there’s no algorithm that can decide that, we are in trouble: <strong>instanceof</strong> will hang sometimes.
That’s why it’s important to study type systems of main-stream languages. And it’s a pity that so few researchers do.
That’s why it’s important to design your type systems carefully, too. So we collaborate with [Ross Tate](http://www.cs.cornell.edu/~ross/) , an Assistant Professor at Cornell University, who is an expert in this field. Ross helps us figure out tricky bits of the type system, avoid nasty corner cases and keep it clean altogether. Recently he wrote an article about generics, including generics in Kotlin. It is very approachable and well-written, so I totally recommend it:

* Mixed-Site Variance by Ross Tate

You’ll find a “Call for Industry Endorsement” on the article page. It’s an important thing: although this kind of research is very important (as I explained above), the academic community isn’t really used to it, so we need to coordinate a little to help them realize that this kind of contribution is a good one. To quote that page:
<p><strong>Why should you bother?</strong> I (and many others) would like to help solve your problems. The challenge we face is that many of your problems are hard to discuss scientifically. Indeed, industry tends to improve by reflecting on experiences, at least when it comes to programming-language development. Unfortunately, we academics need to publish in scientific conferences and journals, and personal experience is not a scientific process. Our reviewers may very well like what we have to say, but they may not be comfortable accepting a paper founded on heresay into a scientific venue. Indeed, after reading positive reviews and then being rejected, through side channels I was informed such concerns were this paper’s downfall, and I was encouraged to try unconventional avenues. So, this is an experiment to enable industry to encourage research directions they would like explored despite the difficulty in scientifically backing claims. In other words, this is an attempt to make industry experience admissible as evidence in academic settings, just like they are in industry settings.</p>
Ross (and I) will appreciate an endorsement email from you.
Thanks.
P.S. In the picture above you see [Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman) , a Nobel Prize winning physicist. He did not care about type systems, but he was a really interesting man, probably the most practical theoretician, and contributed to Computer Science by inventing [quantum computers](https://en.wikipedia.org/wiki/Quantum_computer) .
