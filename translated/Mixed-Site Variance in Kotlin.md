---
title: "[译]Mixed-Site Variance in Kotlin"
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

<img alt =“”class =“alignleft”data-recalc-dims =“1”src =“https://i2.wp.com/www.geoffwilkins.net/images/feynman/feynman-blackboard.jpg?resize = 360％2C272＆amp; ssl = 1“/>类型系统...我们都知道他们很酷。在静态语言（如Kotlin）中，类型系统是负责早期检测错误的系统。许多工具（例如具有重构能力的IDE）也依赖于类型系统。
我们也知道类型系统是困难的：许多计算机科学家构建了他们的整个职业学习类型系统。然而，我们对主流语言的类型系统知之甚少。<span id =“more-1112”> </span>
例如，提出一个简单的问题：“我们有两种Java类型，比如A和B;我可以将类型A的值分配给类型B的变量吗？“（换句话说，”是A是B的子类型“）对于某些语言（例如C＃），我们知道有一个算法需要A和B，想一会儿，然后终止并给出正确答案：“是”或“否”。换句话说，子类型问题是C＃的可判定问题。对于其他一些语言，我们知道不会有这样的算法：无论你编写什么编译器，都会有一对类型A和B，它给出一个错误的答案，永远不会终止或抛出异常（可以看作是一个错误的答案）换句话说，Scala的子类型是<em>不可判定的</em>（实际上，Scala的类型系统是 [图灵完成](http://michid.wordpress.com/2010/01/29/scala-type-level-encoding-of-the-ski-calculus/) ，即您可以使Scala的类型检查器执行任何计算，包括无限循环）。
Java怎么样？我们不知道（见 [这张纸](http://www.cs.cornell.edu/~ross/publications/tamewild/) ， 例如）。有些人怀疑子类型对于Java来说是不可判定的，但至今尚未得到证实。 **这是一个实际的问题吗？**哦，是的。有些人希望将加入的泛型代码添加到Java中，这意味着**foo instanceof Bar**将检查运行时类型的foo是否是Bar的子类型。如果没有可以决定的算法，我们有麻烦：**instanceof**有时会挂起。
这就是为什么要研究主流语言的类型系统的原因。可惜这么少的研究人员呢。
这就是为什么也要仔细设计你的类型系统的原因。所以我们合作 [罗斯·泰特](http://www.cs.cornell.edu/~ross/) ，康奈尔大学助理教授，是该领域的专家。罗斯帮助我们弄清楚类型系统的棘手部分，避免讨厌的角落，保持清洁。最近他写了一篇关于泛型的文章，包括Kotlin的泛型。这是非常平易近人的，所以我完全推荐它：

* Ross Tate的混合场地差异

您将在文章页面上找到“呼吁行业认可”。这是一件重要的事情：虽然这种研究非常重要（如上所述），学术界并不习惯，但我们需要协调一点，帮助他们意识到这种贡献是一个很好的一。引用该页面：
<p> **为什么要打扰？**我（和许多其他人）希望帮助您解决问题。我们面临的挑战是，很多问题难以科学讨论。事实上，行业倾向于通过反思经验来改进，至少在编程语言发展方面。不幸的是，我们的学者需要在科学会议和期刊上发表，个人经验不是一个科学的过程。我们的审稿人可能非常喜欢我们所说的话，但是他们可能不会很乐意接受一个建立在一个科学场地上的论文。事实上，在阅读正面评论后被拒绝后，通过旁观者渠道，我被告知这一担忧是本文的垮台，我很鼓励尝试非常规渠道。所以，这是一个实验，使行业能够鼓励他们想探索的研究方向，尽管科学支持索赔的困难。换句话说，这是试图让行业经验作为学术环境中的证据，就像在行业环境中一样。</p>
罗斯（和我）将欣赏你的一封赞许电子邮件。
谢谢。
美国在上图中你看到 [理查德·费曼](https://en.wikipedia.org/wiki/Richard_Feynman) 诺贝尔奖获奖物理学家。他不关心类型系统，但他是一个非常有趣的人，可能是最实用的理论家，并通过发明为计算机科学贡献 [量子计算机](https://en.wikipedia.org/wiki/Quantum_computer) 。
