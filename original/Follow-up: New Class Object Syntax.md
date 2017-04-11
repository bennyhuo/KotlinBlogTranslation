---
title: Follow-up: New Class Object Syntax
date: 2015-03-14 10:57:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/follw-up-new-class-object-syntax/
---

In the previous post I explained the rethought design of what used to be called “class objects”: they are now more uniform with normal nested objects, have names (name may be omitted, but a default one will be used by the compiler), and we can write extensions to them.
One of the goals of that post was to gather feedback on the term we proposed, namely “default object”, and many of you rightfully stated in the comments that  the term has a disadvantage: it is easily misread for “a default instance of the class”. Now we are looking for a better term and need some more feedback…
Update: thanks to everyone, with your help, we chose companion.
We are talking about a modifier in front of the word object:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    ??? object {
        fun callMeOnTheClassName() { ... }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Our candidates are:

* default object
* attached object
* companion object
* manifest object

We’d be very grateful if you shared your thoughts about these candidates in the comments.
Thanks!
P.S. There was a proposal of simply using a naming convention instead of a modifier. This comment explains why we decided in favour of a modifier. Also note that this convention would be used a lot more often than others, and others are subject to reconsideration under the upcoming language design review.
