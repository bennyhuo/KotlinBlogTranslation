---
title: Kotlin Future Features Survey Results
author: Andrey Breslav
date: 2017-06-13 21:24:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlin-future-features-survey-results/
tags: 
categories:  官方动态
---

With all the exciting recent events, we had to postpone the publication of the Future Features Survey results. Sorry about that. Better late than never, this blog post summarizes what we learned from the survey.
To recap, the Future Features Survey ran in April and got about 850 replies. We would like to thank everyone who took part in the survey!
## Survey results

The raw (anonymized) data for the survey are available here.
The questions asked were:

* The most expected feature 1, The most expected feature 2, The most expected feature 3
* Nominate one feature that you would like to be banned (optional)

You can see the list of proposed features here.
We received a total of 852 responses (a few of them blank). Most people used up all three slots for positive feature nomination, and some 300+ people skipped the negative nomination.
Here’s the summary chart of all results (sorted by nominations in favour of a feature):

{% raw %}
<p><iframe frameborder="0" height="637" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/pubchart?oid=2077021838&amp;format=interactive" width="790"></iframe></p>
{% endraw %}


{% raw %}
<p><span id="more-5025"></span></p>
{% endraw %}

So, the favorites here are: “Collection literals”, “SAM conversions for Kotlin interfaces” and “Truly immutable data”.
“Private members accessible from tests” seems to be the most controversial feature: 108 people for and 120 against, which is understandable since designing for testability is widely recognized as a good practice.
I’m a bit puzzled over the “Overloadable operators | and &” controversy: 46 for and 50 against, while I see zero harm in this feature. Please share your motivation in the comments to this post.
Here’s the chart of negative nominations:

{% raw %}
<p><iframe frameborder="0" height="483.5" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/pubchart?oid=346107453&amp;format=interactive" width="933"></iframe></p>
{% endraw %}

We shouldn’t have put “Optional commas” and “Optional trailing commas” under the same feature (my mistake, sorry), as it’s actually two features, so the results there are difficult to interpret.
Another mistake (and on my part as well): we forgot to include “Ternary conditional operator” in the survey, and realized that too late in the game. Sorry, folks, we understand that there’s substantial demand for this feature, and will look into it.
Curiously enough, the results of the survey that was conducted at the Kotlin 1.1 Launch Event turned out quite differently:

{% raw %}
<p><iframe frameborder="0" height="580" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1gR1C69Rcmv2szbQJ-mXrhW7KtU4tPSya93Xq9sfE8Y0/pubchart?oid=2043595044&amp;format=interactive" width="1034"></iframe></p>
{% endraw %}

I suspect that the results may have been affected by the fact that people saw previous votes and got biased, but it’s hard to be sure. Other factors may also be relevant, e.g. the audience at the meetups may be a bit different from the online survey audience.
## Conclusion

There are clear leaders:

* Collection literals
* SAM conversions for Kotlin interfaces
* Truly immutable data

The rest of the features got significantly fewer nominations. Truly immutable data is very desirable indeed, but really tough too, so no promises there. The other two seem tractable in the foreseeable future, and multi-catch looks like a good thing to look into as well. Anyway, we will take the results into account while planning our work.
Disclaimer: as announced previously, we are not committing here to implementing any of these features in a particular time frame, or at all. We do care a lot about what our users need, but can’t promise anything upfront. For one thing, there’s significant design work required before we even know if these features can be fit pragmatically (and elegantly) into the language.
