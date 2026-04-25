# Prompt History

This file maintains a chronological ledger of prompts that led to the creation and evolution of the Specification Driven Workbench (SDW).

## Initial Unrecorded Prompts (Reverse Engineered)

**Prompt:** "Act as an expert computer science educator. I want to build a hands-on AI lab for high schoolers and non-CS undergrads. The lab should teach them how to build AI-powered applications, starting from basic prompting to multi-agent server workflows. Help me structure the initial agenda, the overarching 'Group Meetup Organizer' project, and the markdown files needed for the sessions. I want this to be a 'Specification Driven' project where we define the plan in markdown first."

**Context:** This initial thought process led to the creation of the `sdw/` directory and the foundational `plan.md`.

---

## add_embed_RAG_prompt.md

# Embed RAG Plan Prompt

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

## merge_plan_prompt.md

# Merging various Prompts and Specification Plans Prompt

## OBJECTIVE
I am creating an AI workbench for high schoolers and non-CS major 
undergraduates. As part of that I've created a specification
driven workbench (SDW) with the plan driving the creation of the
workbench in `sdw`. 

Please read markdown files in`sdw` and `projects/llm_wiki/` 
directory.

## CONTEXT
Unfortunately, I was not disciplined in collating all the
prompts that led to the creation of the workbench and the 
initial workbench content was not created via a structured 
`plan.md` file.

Along the way I switched to spec driven content creation with a 
first part available in `sdw/sdd_server_workflow_plan.md` and the 
second part in `sdw/plan.md`. The prompts that led tot the plan
itself have a pattern of `sdw/*_prompt.md`.

##TASK

### Best Practices for Specification Plans
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

#### Organization of Plan files:
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

### Executed Project Plans vs Original Project Plans

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

## Trigger Prompt
```markdown
Reference the prompts in `sdw/merge_plan_prompt.md` and offer your 
recommendations. Please offer the updates to specification plans 
in markdown format that if approved can be copied into a markdown 
file and git committed. Please do NOT make any changes to the files
until you have my approval.
```



---

## pkm_design_local_prompt.md

# PKM, Design, and Local Plan Prompt

## PKM - Session Plan

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

## Claude Design - Session Plan

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


## AI Local
What is 'AI Local'? What is the dominant use case for 'AI Local'? 
Does it require laptops with specialized hardware or can be run on 
commodity laptop? May we add a session on the trend of `AI Local` 
with an accompanied exercise that be used to illustrate 'AI Local'?

---

## pkm_sdd_prompt.md

# Specification Driven Activities Plan Prompt

## OBJECTIVES

* Read `sdw/plan.md`, `sessions/claude_design.md`, `sessions/llm_wiki.md`, 
`sessions/instructor.md`, `tools/VM/setup.md`, `tools/ollama/setup.md`

* Suggest an addition or amendment plan to `sdw/plan.md` to incorporate 
the following tasks:

## TASKS:

### `tools/instructor.md`: 
#### VM Setup
Create a section on VM setup - reference `tools/VM/setup.md`
#### SSH Access
Create a section on remote ssh access from your Win/MAC laptop to Docker Server. 
Note the server-IP/name, username, and server-PORT is available as environment
variables passed via 
* DOCKER_SERVER_ID
* DOCKER_SERVER_USERNAME
* DOCKER_SERVER_PORT
* Instructions with snippet to add to .ssh/config as a convenience instead of 
having to type all parameters everytime. 
```bash
ssh -p $DOCKER_SERVER_PORT -i ~/.ssh/your_private_key \
$DOCKER_SERVER_USERNAME@DOCKER_SERVER_ID
```
* Update `projects/group_meetup/labsetup.py` to ensure the above setup for students 
is automated and update `projects/group_meetup/preflight_check.py` to ensure the 
setup is validated, such as SSH access is working as expected.
#### Claude.ai Account Setup
* Add a section or update section that sets up claude.ai account - link to 
`tools/claude/cloud.md` that should have signup instructions for account, 
provider account, provider key, etc. - some of that could be duplicated 
in `tools/claude/cli.md` or `tools/claude/desktop.md` which we should 
clean up.
* Explicitly DISALLOW Claude.ai to learn from your data or use your 
location services: claude.ai ⇒ User Logo ⇒ Settings ⇒ Privacy
```markdown
Allow Claude to use coarse location metadata (city/region) to improve 
product experiences. Learn more.
Help improve Claude
Allow the use of your chats and coding sessions to train and improve Anthropic AI models.
```

### Update `sessions`
#### Specification Driven Workbench


#### Specification Driven Slides and Design - Claude Design


#### Specification Driven Personal Knowledge Management

Centralize the plan for validating the exercise
Obsedian and Claude
* Add a kid friendly exercise to LLM_Wiki - review PKM
* How to update PKM when additional topics not related to Compute or AI is added to raw_sources? Is the idea to keep everything in a single home.md?
Collate all the plans and consolidate into one plan and the prompts that generated the plan into one prompt. What about the prompts through which previous git version content was created - can it be reverse engineered?
Note taking: Recall; Voice: 11labs; Persona: Anum
Replace all ```bash with ```markdown
AI local
Centralize the plan for validating the exercise.
Find appropriate places to graft these sessions in README.md agenda.git a


OUTPUT:
Please generate the changes proposed to the plan in `sdw/plan.md` that will drive the changes to
course content in various folders - `sessions`, `tools`, `projects` etc.


CONSTRAINTS:
Do NOT change the plan in `sdw/plan.md` directly. I'd like to first review your proposes
changes in phases/steps FIRST before we change the plan file.


---

## sdlc_env_prompt.md

# SDLC Environment Plan Prompt

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
