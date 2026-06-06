## Motivate GenAI
[ ] Status

Enhance the `## Motivation` section of the repo's `README.md` 
section to capture the essence of the below section as to 
why you should bother learning about `Gen AI` tooling and why
has it taken over the world by storm.

Review and edit as appropriate the below with a short accompanying example - 
hopefully better than the one laid below:

```text
# Why generative AI?

We will understand the transformative nature of generative AI
using the lense of an example as well as technology. 

## Example
Imagine a you are building an application that helps people 
realize their objective of booking vacation travel for family. 

Typical **activities** that fulfill this objective are:
1. **interact and understand goal**: comprehend where all 
she desires to travel, for how many days, what are the constraints
(eg budget, allergy), etc.
2. **deduce preferences, taste, mood, etc.**: seek explicitly or 
deduce the families' preferred "time", "taste", "mood", etc.
3. **plan**: break the "book vacation travel" goal into a plan, such as
figure out the itinerary, for each place figure out the transportation, 
activities, place to stay, etc.   
4. **search and recommend**: **search** various public/private 
information sites, **recommend** specific flavors once an
activity is chosen (eg good movie to see assuming you want to see
a movie).
5. **reason** around the pros and cons of the various alternatives 
often requiring "judgment" and while factoring in the families'
prefences.
6. **book and pay**: **act** on each step of the plan and information 
gathered by booking and paying.

Legacy apps could only fulfill highly deterministic activity 
steps, such as **book and pay** [step 6] or require you to fill a 
form to gather your goal and/or gather your preferences eg 
do you prefer to visit a beach or a rain forest, do you prefer 
Indian or Chinese cuisine. 

In essence, legacy apps do not "deduce", it just "gathers" 
information based on fixed forms and "acts" based on predictable 
logic.

ML (predictiveAI) apps allows one to automatically 
deducing the families' preferences based on prior choices. 
This includes activities, such as "deduce" preferences [2] 
and search and recommend [4].

Agentic (genAI) apps interact and "understand" 
your goal, "generate" different plan of actions [3], 
"reason" on the various choices with pros and cons even 
allowing multiple turns of interactions if needed, and
generate chain of "actions" that may not be deterministic
but yet are contextually relevant.  

## Software
Most applications are now written as agentic apps. 
They are not only far more capable than predictable fixed 
logic legacy apps, but also highly adaptive thus allowing one 
to cover yet unforeseen scenarios from when the application 
was built. 

## Hardware
AI existed for a long time but its true potential jumped
only only when suffiently capable hardware showed up 
[add reference to PKM session on `Silicon and AI`].

AMD and NVIDIA are now in a race to release GPU/CPU 
enabled processors that puts an `AI Local' laptop 
device on every user [add reference to NVIDIA announcement]. 
Apple has already release AI enabled MAC Mini and Smart Phone
[add reference to Apple announcement].

Just as we saw a wave of use cases and applications were 
unleashed when smart phones were put in the hands of every
person [reference Uber and other examples], we anticipate 
the abundant availability of genAI capable hardware will
unleash a wave of new use cases.
```

### Update HDD

Add to the `## 🧠 The Core Concept` session on `HDD` the following:
1. Principles that drives HDD philosophy are:
* genAI generates code that is "probabilistic and not deterministic" 
(ie same prompt will not generate identical code) by nature. 
Hence, one may not assume that it is **correct by construction**. 
not "guaranteed. 
* Ultimately human is accountable for the outcome for the code. 
No, human can digest accountability of code unless it has been
reviewed at some level.

2. Factors that drives HDD methodology are
* Humans are smarter but AI is faster. 
* AI gets confused unless given limited context - otherwise, you 
see deteoriated quality due to context overflow - that is focused 
and limited in scope at an instance.  
