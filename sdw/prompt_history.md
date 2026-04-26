# Prompt History

This file maintains a chronological ledger of prompts that led to the creation and evolution of the Specification Driven Workbench (SDW).

## Purpose

**Prompt:** "Act as an expert computer science educator. I want to build a hands-on AI lab for high schoolers and non-CS undergrads. The lab should teach them how to build AI-powered applications, starting from basic prompting to multi-agent server workflows. Help me structure the initial agenda, the overarching 'Group Meetup Organizer' project, and the markdown files needed for the sessions. I want this to be a 'Specification Driven' project where we define the plan in markdown first."

**Context:** This initial thought process led to the creation of the `sdw/` directory and the foundational `plan.md`.

---

## Embed RAG Plan Prompt

### extracted from add_embed_RAG_prompt.md

Reference `README.md` and `sdw/plan.md`

OBJECTIVES
* Review the agenda in `README.md` and suggest any topics that we've missed that we should add or remove sessions or topics that should not be a part of this lab.

TASKS
Consider sessions and exercises that illustrate:
* BERT and how it can be used to do a semantic similarity. For example, when context engineering and deciding whether a context is relevant to the user query OR to search between two paragraphs - a cheap embedding similarity exercise and render to show how Queen and King are directionally similar from Woman and Man in visualization. 
* Small Language Model along with short exercise to pull a model from Hugging Face that can be used to do a simple exercise.
* Any other sessions or exercises that makes sense for the objective of the lesson.

* Review the `sessions/future_advancements.md` and suggest any topics that we've missed.
  * Suggest whether adding a session in Predictive AI and techniques makes sense that offers a short overview of highly effective and used techniques: 
  1. Linear Regression 
  2. Logistic Regression 
  3. Decision Trees 
  4. Recommendation 
  5. Reinforcement learning 
  6. Neural Network. 
  * Does adding an exercise to illustrate Predictive AI, such as hand-written digit recognition or any exercise that very easily illustrates predictive AI.

* Consider whether adding a session `sessions/solution.md` that illustrates how a modern agentic solutions actually ties together techniques of (a) predictive AI (b) generative AI (c) non-AI software
algorithms (d) systems software engineering - in order to build a practical solution. An toy exercise that brings together many of these disciplines to solve a problem.

* Review the `sessions/recap.md` to ensure it reflects the content of all the sessions.  


CONSTRAINTS:
* Keep the overall theme of the exercises cohesive and tight, the session sequencing appropraite, and the exercises in each session that feeds towards the overall theme of the lab. 
* Remove cruft and any session that does *NOT* meet the need. 
* Suggest any new session or edit any existing session that makes sense. 
* Avoid overall bloat of the education lab to ensure students can aborb the overall lab without suffering from indigestion as there is too much unrelated topic and without an overall consistent theme. 
* Conversely, add any session or topic that is vital but has been missed so far.

OUTPUT:
Suggest any changes as an update to the plan in `sdw/plan.md` that meets the above OVJECTIVES, TASKS, and CONSTRAINTS.

---

## Merging various Prompts and Specification Plans Prompt

## extracted from merge_plan_prompt.md

### OBJECTIVE
I am creating an AI workbench for high schoolers and non-CS major 
undergraduates. As part of that I've created a specification
driven workbench (SDW) with the plan driving the creation of the
workbench in `sdw`. 

Please read markdown files in`sdw` and `projects/llm_wiki/` 
directory.

### CONTEXT
Unfortunately, I was not disciplined in collating all the
prompts that led to the creation of the workbench and the 
initial workbench content was not created via a structured 
`plan.md` file.

Along the way I switched to spec driven content creation with a 
first part available in `sdw/sdd_server_workflow_plan.md` and the 
second part in `sdw/plan.md`. The prompts that led tot the plan
itself have a pattern of `sdw/*_prompt.md`.

### TASK

#### Best Practices for Specification Plans
* What are the **best practices** for saving the prompts that lead to the
creation of the plan? That is are the prompts that lead to the creation
of the specifications are to be git stored and versioned OR are they 
to be "treated as disposable scratch pads":

  * **Regarding prompts:**: Do we consolidate the prompts scattered 
  in `sdw/*_prompt.md` files into `sdw/prompt_history.md`?

* What are the **best practices** wrt organizing/storing the different 
plan files? That is are the specifications (aka plan files) that lead
to the workbench content to be git stored and versioned OR are they 
to be "treated as a scratch pads"? 

What would you recommend? Based on your recomendation, please suggest
the plan of changes to `sdw/plan` or a new plan file as appropriate .

##### Organization of Plan files:
Furthermore, even if they are to be stored in git, should they be 
consolidated into a single file or should they be stored in separate files? 

If separate files should they be organized hierarchically? For example, 
should plans for content creation of subprojects be stored in separate 
files under subdirectories OR under a single directory, in separate 
files? 

  * **Regarding plan files:**: Specifically, should we consolidate - if so 
  how - the individual plans in `sdw/*plan.md` are consolidated into 
  `sdw/plan.md` i.e. move contents in `sdw/sdd_server_workflow_plan.md` 
  into `sdw/plan.md`?

  * What about the plan and prompts that we never recorded to the creation 
  of the initial structure of the workbench? Is it possible to reverse engineer 
  those and add it to the prompt history and plan for records?

What would you recommend? Based on your recomendation, please suggest
the plan of changes to `sdw/plan` or a new plan file as appropriate .

#### Executed Project Plans vs Original Project Plans

* Reference an original project plan in `projects/llm_wiki/llm_wiki_plan.md`. 
As an instructor, I executed the plan which resulted in an obsidian cross 
linked markdown file. The plan when executed has phases and steps marked
as done and recorded as such in the file `projects/llm_wiki/plan.md`.

I'd like the original plan to be available for students to execute the 
plan and realize how personal knowledge management is realized. At the
same time, I'd like to record that the instructor (in this case I) have
already executed the plan. 

What are the **best practices** to remembering an executed project plan?
Do we keep both the original plan and the executed plan? Should we 
have a naming convention to distinguish between them? Or should we 
have a single plan file that is updated to reflect the changes made 
during execution?

What would you recommend? Based on your recomendation, please suggest
the plan of changes to `sdw/plan` or a new plan file as appropriate.

### Trigger Prompt
```markdown
Reference the prompts in `sdw/merge_plan_prompt.md` and offer your 
recommendations. Please offer the updates to specification plans 
in markdown format that if approved can be copied into a markdown 
file and git committed. Please do NOT make any changes to the files
until you have my approval.
```

---

##  PKM, Design, and Local Plan Prompt

## extracted from pkm_design_local_prompt.md

### PKM - Session Plan

There is a lot of buzz around Obsedian-Claude use case. Can you shed 
some light as to what is the use case that Claude integration with 
Obsedian unlocks? Please share the blog or you tube where 
Andrej Karpathy talks about how he uses Obsedian in a day of his life 
and how it improve his productivity.



Is this worth adding to my AI Education Lab class as a workbench 
session. Please suggest the contents of that session - topics, 
installation instructions, key take aways, references, etc and 
an accompanying exercise that is both simple and clearly 
illustrates the benefit.

### Claude Design - Session Plan

Claude just released Claude Design released as part of `Pro` 
subscription package. Is it a separate tab in `Claude Desktop` 
or just part of the overall `Claude Code`. Is it generally 
available to a person like me who is a `Pro` subscriber to Claude?

`Claude Design` lets developers (novice designers) to iterate and 
generate Figma akin UX designs and mockups using prompts.
`Claude Design` also lets folks create beautiful brand/logo/template 
based presentation decks.

High schoolers and undergrad kids have to be adept in presenting - 
whether it is to an audience (via slides) or to consumers - 
via websites or product UX. Can you suggest a session structure 
and an accompanied exercise that helps kids familiarize with the 
concepts, benefits, etc. of `Claude Design`?


### AI Local
What is 'AI Local'? What is the dominant use case for 'AI Local'? 
Does it require laptops with specialized hardware or can be run on 
commodity laptop? May we add a session on the trend of `AI Local` 
with an accompanied exercise that be used to illustrate 'AI Local'?

---

## SDLC Environment Plan Prompt

### extracted from sdlc_env_prompt.md

OBJECTIVES
* Read `sdw/plan.md` and `sessions/sdlc_ai.md`
* Suggest an addition or amendment to `sdw/plan.md` to incorporate the following tasks:

TASKS:
1. Pass all the non confidential environment variable names and values (as mentioned in `sessions/intructor.md`) for setting up the AI Lab as a YAML file `projects/group_meetup/labenv.yaml`. 

Examples of the environment variables whose values need to set are:
* DISCORD_SERVER - Discord Server name for the class id
* DOCKER_SERVER_ID - Name of the server that is resolvable to a IP on which an account with username `labuser` is created. 

NOTE that please validate that the few environment variables that must NOT be visible in any git file and only set 'out of band':
* DISCORD_WEBHOOK_URL  - this is a secret and should be removed from `sessions/intructor.md`. It is the webhook URL with name `Meetup Bot` in channel `#meetup-notifications`, where any post appears as message in `#meetup-notifications`.


2. Add a python script `projects/group_meetup/labsetup.py` that parses `projects/group_meetup/labenv.yaml` and sets the environment variables based on the key/values in the YAML file. It also checks that the DISCORD_WEBHOOL_URL is set.

3. Add a simple markdown picture that illustrates SDLC phases.

4. Suggest how tests - specifically unit tests  in `sessions/sdlc_ai.md` - can be run with dependencies on test data i.e. are the data source of truth partitioned into two namespaces:
* Production Data - highly privileged and access available only to production jobs with appropriate IAM controls.
* Dev/Test Data - available in a separate namespace that is exposed for access even from developers running and testing software on their client laptop.
* Exercise that illustrates how data dependent tests can be run without having to create a separate copy of data.

OUTPUT:
Please offer the changes to the plan in `sdw/plan.md` using which we will make the appropriate adjustments to `sessions/intructor.md`, scripts in `projects/group_meetup`, and session content and/or content/exercises in `sessions/sdlc_ai.md` for testing section.

---

## Specification Driven Activities Plan Prompt

### extracted from pkm_sdd_prompt.md

### OBJECTIVES

* Read section `#Purpose`

* Reference `sdw/plan.md`

* Suggest an amendment to `sdw/plan.md` to incorporate the below remaining 
part of this section:

### TASKS:

#### Instructor & Group Meetup Setup

This section covers updates to set up files:
* [Instructor](../sessions/instructor.md)
* [Lab](../projects/group_meetup/labsetup.py) 
* [Preflight](../projects/group_meetup/preflight_check.py)

##### VM Setup
Create a section on instructions with Virtual Machine (VM) setup 
and reference in it a link to `tools/VM/setup.md`

##### SSH Access
1. Create a section on instructions with remote ssh access from your laptop
Windows or MacOS laptop to Docker Server. 

Note the server-IP/name, username, and server-PORT is available as environment
variables passed via 
* DOCKER_SERVER_ID
* DOCKER_SERVER_USERNAME
* DOCKER_SERVER_PORT

2. Add instructions with snippet to add to .ssh/config as a convenience 
instead of having to type all parameters everytime. 
```bash
ssh -p $DOCKER_SERVER_PORT -i ~/.ssh/your_private_key \
$DOCKER_SERVER_USERNAME@DOCKER_SERVER_ID
```

3. Modify Lab Setup file to ensure the SSH setup from students to Docker Server
is updated, automated, and validated i.e. ssh config file is set, environment
variable existence is validated, and ssh is working as expected.  

#### Claude.ai Account Setup

1. Create a file [Claude Cloud Setup](../tools/claude/cloud.md) that has 
* Signup: instructions for every student's claude.ai account
* API: Setting up API key
* API Call Setup: Saving it in a local environment variable ANTHROPIC_API_KEY. 
* Privacy: Explicitly DISALLOW Claude.ai to learn from your data or use your 
location services: claude.ai ⇒ User Logo ⇒ Settings ⇒ Privacy
```bash
Allow Claude to use coarse location metadata (city/region) to improve 
product experiences. Learn more.
Help improve Claude
Allow the use of your chats and coding sessions to train and improve 
Anthropic AI models.
```

2. Reference this claude.ai account setup wherever appropriate.  
Some instructions of `Claude Cloud Setup` maybe duplicated in few files, 
such as:
* [Claude CLI Setup](../tools/claude/cli.md) and 
* [Claude Desktop Setup](../tools/claude/desktop.md)

Ensure the duplications are removed and cross references are added so to 
maintain DRY principle.

#### Update `sessions`

##### Specification Driven **XXX**

Here **XXX** means any useful activity, such as:
* `Workbench`, 
* `Presentation` (`Slides and Design`) 
* `Personal Knowledge Management (PKM)`
* `Development`

Consider adding the below sections as part of an existing session or 
create new sessions as appropriate. Whenever you propose modifying an 
existing session or adding new session, please update the agenda 
in `README.md` so that the content is consistent.

###### Specification Driven Workbench - SDW

This `AI workbench` is itself built using Specifications. Add a 
section referencing the `sdw/plan.md` as an illustration.

###### Specification Driven Presentation - SDP

`Claude Design` can create aesthetically pleasing Slides and Design 
content. Expand the session on [Slides](../sessions/slides.md) 
to include the content and exercises created in 
[Claude Design](../sessions/claude_design.md), rename the 
session on `Slides` to a session on `Presentation`, make the session 
content coherent and consistent with other session by adding appropriate 
sections ie do not just concatenating the session files, and update 
all references as appropriate.

###### Specification Driven Personal Knowledge Management - SDPKM

Karpathy introduced a way for everyone to have their person LLM-Wiki 
using Obsedian and IDE and LLM for cross referencing knowledge graph.

Reference [LLM Wiki](../sessions/llm_wiki.md) and modify an existing
session or create a new session as appropriate. Add a section within 
the exercise section that consolidates content in `Home.md` 
(currently has cross links between `Moore's Law` and `History of AI`) 
clarifying how additonal topics unrelated to the above two 
are coherently factored in `home.md`.


###### Specification Driven Development - SDD

We already have a full `Concept` and `Exercise` session on SDD 
that is also referenced in `README.md` - add a section to links 
other Specification Driven Work, such as SDW, SDP, SDPKM, just
as illustration that SDD is just one field among many feasible via AI


#### AI Local

AI Local allows one to run LLM models locally on client laptops and 
then build, test, and deliver intelligent local apps. 

Reference [AI Local](../sessions/ai_local.md) and create a new session
or modify an existing session as appropriate.

#### Connect execises across sessions where feasible

Explore whether it is feasbile to build over the exercise projects 
proposed in SDP, SDPKM, SDP, AI Local, and optionally from other 
session so that students have a sense of continuity and that they 
are building one over another. 

Of course, if the continuity forces tough or complex exercises or is NOT 
feasible then let us craft exercises as common as possible across the 
above sessions. Reasons we may not attempt a coherent arc for 
exercises across certian sessions may be limitations - say if we find 
that `AI Local` forces simple exercise or `SDPKM` does not easily lend 
to other exercises, etc


#### Hygiene

Make references to all markdowns consistent. 

1. If the markdown encapsulate a terminal command, use:
```bash
...
```

2. If the markdown encapsulates just a special string, use:
```markdown
...
```

#### Consistency

Run a consistent check across content in AI Workbench. Example is 
review README.md, all markdown file references across all subdirectories,
such as `sessions/`, `projects/`, `tools/`, etc. are consistent including
that all session content and project preferences are appropriately placed.

### OUTPUT:
Please generate the changes proposed to the plan in `sdw/plan.md` that 
will drive the changes to workbench content in various folders, such 
as `sessions`, `tools`, `projects` etc.

### CONSTRAINTS:
Propose the change to the plan in `sdw/plan.md` BUT do NOT change the 
plan directly. Propose the change first as a separate markdown file
`sdw/plan.v2.md` that can be reviewed in terms of changes in 
phases/steps to the plan of record `sdw/plan.md` file. Once approved
we can incorporate the changes to `sdw/plan.md` and start executing
to amend the workbench content.

---

## Improve Setup Skill RAG 

### OBJECTIVES

* Read section `#Purpose`

* Reference `sdw/plan.md`

* Suggest an amendment to `sdw/plan.md` to incorporate the below remaining 
part of this section:

### TASKS:

#### Students **Development System** Setup

Review and validate 
[Development Workbench](../sessions/dev_workbench.md) as it is 
what is used to help set up the development workbench 
for learners. Reference this session as the session 
in the agenda immediately after the one after `instructor` 
in README.md. 

#### Move Setup and Install Content to Development System

1. Clean up the instructor.md of any references that are 
meant for students. For example, [Instructor](../sessions/instructor.md)
has Section 0 Provision Docker VM on Server that has a 
reference to VM Setup Guide. That reference should be removed
as [VM Setup Guide](../tools/VM/setup.md) is for provisioning VMs on
student laptops - NOT for provisioning Docker VMs on server side.

2. Review files and identify if we've any session that
dedicates to help students set up the development system
and associated environment. Move those sections to 
[Development Workbench](../sessions/dev_workbench.md).

For example, move sections in [Instructor](../sessions/Instructor.md) for 
students into [Development System](../sessions/development_system.md) 
that are meant for students.


3. If there are files that reference the exact steps to setup and install 
of the below commonly used tools for development into 
[Develoment System](../tools/dev_system) directory.
Specifically move the following files to ../tools/dev_system:
* [GitHub](../tools/github.md)
* [VS Code](../tools/vscode.md) 
* [LLM Provider Cost Management](../tools/provider_cost_control.md)


#### GitHub - Cloud Account and SSH Setup

Review [GitHub](../tools/dev_system/github.md) - validate that 
there is a section that students can reference on how to set up 
github: account setup, provision ssh private/public 
key (just as they did for SSH to DOCKER_SERVER), and upload the ssh 
key to the GitHub account associated with the user. Add the 
corresponding github access key to .ssh/config via 
[Lab Setup](../projects/group_meetup/labsetup.py) and add a test in  
[Preflight Check](../projects/group_meetup/preflight_check.py) 
to ensure git commands are working for the user.

#### MacOS Setup

1. Replace the [VM Setup](../tools/VM/setup.md) for MacOS from 
Parallels VM to Dev Container
2. Add a section on [Instructor](../sessions/Instructor.md) 
that lays out how a student should thinks about the platforms 
used for different tools, VSCode frontend on Win11/MacOS, 
Ubuntu for development, etc. 

#### Update Embedding Skills RAG

The current reference to Embedding, Skills, and RAG in 
[advanced prompting](../sessions/prompting_advanced.md) is NOT 
reinforced in later sessions or sections. 

For example:
1. Any exercises in sessions/ after the Advance Prompting session 
do NOT build on Skills. Please revisit exercises in later sessions
and find opportunities to build Skills. 

2. The [LLM Wiki](../sessions/llm_wiki.md) technique completely 
does away with the need to build RAG tooling. Reinforce this concept
in the LLM Wiki session and reference link to `Advanced Prompting` 
section on RAGs.

3. Explore if there are student friendly exercise to use embeddings 
(BERT?) for similarity to Ollama LLM in [AI Local](../sessions/ai_local.md) 
session. Or scope to use lightweight RAG for an exercise in later sessions?

#### Consistency

Run a consistent check across content in AI Workbench. Example is 
review README.md, all markdown file references across all subdirectories,
such as `sessions/`, `projects/`, `tools/`, etc. are consistent including
that all session content and project preferences are appropriately placed.

### OUTPUT:
Please generate the changes proposed to the plan in `sdw/plan.md` that 
will drive the changes to workbench content in various folders, such 
as `sessions`, `tools`, `projects` etc.

### CONSTRAINTS:
Propose the change to the plan in `sdw/plan.md` BUT do NOT change the 
plan directly. Propose the change first as a separate markdown file
`sdw/plan.v2.md` that can be reviewed in terms of changes in 
phases/steps to the plan of record `sdw/plan.md` file. Once approved
we can incorporate the changes to `sdw/plan.md` and start executing
to amend the workbench content.

---

## Replan Trigger Prompt

Read `sdw/plan.md`.
Reference [Replan Prompt](./sdw/prompt_history.md#improve-setup-skill-rag).
What is the title of the section and key contents?
Once I confirm you have narrowed to the correct section, generate the 
specification plan changes to meet the requirements of that section 
as a markdown file sdw/plan.v2.md. Once the plan change is approved
add the sdw/plan.md starting from Phase 14 and Steps in the phase.
