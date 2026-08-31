# Prompt History

This file maintains a chronological ledger of prompts that led to the creation and evolution of the Specification Driven Workbench (SDW).

## Purpose

**Prompt:** "Act as an expert computer science educator. I want to build a hands-on AI lab for high schoolers and non-CS undergrads. The lab should teach them how to build AI-powered applications, starting from basic prompting to multi-agent server workflows. Help me structure the initial agenda, the overarching 'Group Meetup Organizer' project, and the markdown files needed for the sessions. I want this to be a 'Specification Driven' project where we define the plan in markdown first."

**Context:** This initial thought process led to the creation of the `sdw/` directory and the foundational `plan.md`.

---

## [x] Embed RAG Plan Prompt

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

## [x] Merging various Prompts and Specification Plans Prompt

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

## [x] PKM, Design, and Local Plan Prompt

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

## [x] SDLC Environment Plan Prompt

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

## [x] Specification Driven Activities Plan Prompt

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

## [ ] Improve Setup-Skills-RAG 

### OBJECTIVES

* Read section `#Purpose`

* Reference `sdw/plan.md`

* Suggest an amendment to `sdw/plan.md` to incorporate the below remaining 
part of this section:

### TASKS

#### Students **Development System** Setup

Review and validate 
[Development Workbench](../sessions/dev_workbench.md) as it is 
what is used to help set up the development workbench 
for learners. Reference this session as the session 
in the agenda immediately after the one after `instructor` 
in README.md. 

Reorganize Development Workbench into `Concept` and `Exercise`
section with the `Exercise` section sequenced intuitively so 
that any learner can prescriptive follow the session and links 
in those section to setup the Workbench.

1. [VM Setup](tools/VM/setup.md)
Ensure that the set.up.md has clear instructions on how to provision
and start the WSL (Win11) or DevContainer (MacOS). Example below:
```text
Win11 - WSL
* Provision: Links to set up wsl with distro Ubuntu 24.04 LTS
* Start: wsl --cd ~
MacOS DevContainer
* Provision: ...
* Start Dev: ...
```
2. Claude.ai Setup: [Setup](tools/claude/cloud.md)

3. VSCode Setup: 
* Extensions: `Remote WSL`, `Claude Plugin`, ...
* Start inside Ubuntu: `code .`

3. GitHub Setup: GitHub account, ssh key access setup, ...

4. Linux (Ubuntu) tools Setup: 
* Links to install git
* Links to setup SSH access to git and update to .ssh/config

5. Test commands to run from VSCode to ensure Claude is working. Maybe
Hello World program created via Claude and tested from VSCode terminal.

6. Lab Setup: User side set up needed and run projects/group_meetup/labsetup.py

7. Test all set up working via projects/group_meetup/preflight_check.py
...

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

## [x] Workbench Contribution Guidelines

### Workbench Update Workflow
This is a specification driven workbench. The workflow to update **any**
content for the workbench is to follow the below sequence in strict order:
1. **Append** prompts to [Prompt History](sdw/prompt_history.md). 
The prompt is direct AI to change the [Specification Plan](sdw/plan.md)
by **appending** new phases and new steps in the phases.
2. The objective of only appending to `prompt history` and 
`specification plan` is to create both as system of record for any 
changes to the plan.
3. The `specification plan` changes are then executed to amend or create 
new content while adhering to the operating guidelines of `Claude.md`.
Note that:
* NO direct changes to content are only. Only via `Workbench Update Workflow`
* Strict ADHERENCE to CLAUDE.md `STYLE & HYGIENE` section while generating
content.
4. The contributor commits the latest version of `prompt history`, 
`specification plan` and the workbench content on a branch and submits
a pull request (PR) to main branch. Note contributors are NOT allowed 
to commit to main branch. 
5. Maintainers review the PR request, use AI Code review to enforce simple
checks (e.g. `STYLE & HYGIENE` of `Claude.md` is followed) and then manaully
review the content to either approve the merge or revert back to the
contributor with additional comments.

### BACKGROUND
* Read section `#Purpose`
* Reference `sdw/plan.md`
* Suggest an amendment to `sdw/plan.md` to incorporate the below:

### TASKS

#### Document SDW in README

Add a new or amend an existing section of README.md that clearly calls out 
that the `AI Workbench` repo is a `specification driven workbench (SDW)` with an 
short description defining what SDW means.  

#### Document **Workbench Update Workflow**

Review the `Workbench Update Workflow` section above and suggest updates as 
appropriate to the process. 

For example: shouldn't the Pull Request REQUIRE that the section of 
`specificatin plan` that was executed to generate changes to the content 
also contain:
* `provider:model` used to generate append changes to the `specification plan` 
section. 
* `provider:model` used to execute the `specification plan` section and then
generate the content itself? 

What else do you suggest are **best practices** to manage the contribution and
content of Specification Driven Content? 

Document the process of `workbench update workflow` in the `Contribution Guidelines` 
section of README.md.

#### Style and Hygiene

Use the Claude.md `Style and Hygience` to review content of the entire workbench 
that all lines are less than 80 characters and tabs are implemented as 2 spaces.

We repeatedly see generated content violate the `Claude.md` operating protocol. 
Are there ways to enforce that AI does NOT forget to ignore this manadate and
that henceforth generated content always adheres to this requirement?

### CONSTRAINTS:
Propose the change to the plan in `sdw/plan.md` BUT do NOT change the 
plan directly. Propose the change first as a diff to the markdown file 
in terms of changes in phases/steps to the plan of record `sdw/plan.md. 
Once approved we can incorporate the changes to `sdw/plan.md` and start 
executing to amend the workbench content.

---

## [x] Specification Driven XXX


### Imporve Agenda
Update the agenda section of README.md with another column `Description` that 
offers a one sentence summary for each session describing the essence of 
whatever is the most relevant wrt any of the below reasons:
* why the students should bother attending the session
* what will they learn, what will they get out of doing the session
* basically lay out the motivation of the session.

### Specification Driven Activities

Many activities can be driven via Specifications. 

Add to the table in `sessions/sdd_basics.md` for the section on 
`Specification Driven Beyond Code` rows, where we
illustrate additional use cases, such as:

* Specification Driven Bootstrapping: spec plans can be used to drive, 
orchestrate, manage, et.c many of the key activities that entrepreneurs 
engage as part of bootstrapping start-ups, such as ideation, research, 
GTM, product, and technology i.e. creating mocks, building prototypes, etc.

* Specification Driven Computer Aided Design - 
[Claude on AutoDesk](https://x.com/claudeai/status/2049143438281445811?s=20)

* Specificatin Driven Creative Tooling: 
[Claude on Blender](https://x.com/claudeai/status/2049143438281445811?s=20)

* Specification Driven **XXX**: Do a quick search of what all activities are
already known as being driven by specifications and LLMs and add those to 
the table with reference links to the table.

* At the end of the table, add a new sub-section stating that 
`Specifications` can drive any digital services with authorized interface 
that is LLM readable - MCP or APIs with 
schema, types, description, etc. - and rules of execution are well defined 
i.e. not implicit in human mind but rather explicitly stated. 

Once physical world can be digitally controlled (e.g. robots) then 
LLMs can drive additional activities that span the digital and 
physical world as well. Clarify here that in this case the MCP or API 
are the digital interfaces to the physical world.

### Validate Setup or Install Success

Scan through the repo to ensure all setup or installation of tools is 
followed by a validation command to ensure the exercise succeeded. 
For example, we've a validation step in `tools/dev_workbench/github.com` 
where after setting up the GitHub with public SSH keys, we validate
that the SSH acceess has been provisioned correctly by running
`ssh -T git@github.com` and then expecting a given response. 

This kind of test or validation instruction should follow every setup 
instruction.

### Delete unused files

Please scan the repo to eliminate files whose contents have been absored 
in other files. These files were left behind due to oversigh.
As an example reference `sessions/claude_design.md` - validate that contents
its contents have since been moved to `sessions/presentation_n_design.md`.

---

## [x] Multimodel

The objective is to enhance our developer workbench 
`sessions/dev_workbench` setup where we use

### VSCode

#### VSCode and GitHub Setup

##### GitHub Setup
Reference:
* `sessions/dev_workbench`
* `tools/dev_workbench/github.md`
and related files.

1. Update GitHub setup for a student to clone the repo corresponding
to `ai_workbench` in an appropriate directory, say `~/ws/sw`.

2. Ensure User creates a github branch on which she will execute 
and push/pull all the relevant exercises.

##### VSCode Setup
Reference:
* `sessions/dev_workbench`
* `tools/dev_workbench/vscode.md`
and related files.

1. Install VSCode GitHub extension. Ensure students have the steps to now 
push and pull contents against a branch that they created against which 
they freely make and save changes in GitHub. 

2. Install VSCode GitHub Pull Request extension. Ensure students have the 
steps to raise a pull request (PR) to merge content on their personal branch 
to the main branch. 

#### Test VSCode, GitHub, and Claude Code Setup

Reference `Section 6` of `sessions/dev_workbench.md`

Now that Claude, VScode, and VSCode plugins and extensions for GitHub, Claude Code, etc.
setup, validate the setup by having the student chat to:
1. Use VSCode to `Pull` the latest code (if any) in the repo
2. Use Clauge Extension to prompt Claude to add or update the python code 
`tests/vscode/hello.py` and print the user's GitHub username:
```text
print "hello, <my_github_username>!" 
```
3. Use VSCode to `Push` the latest code to the user's git branch off of main.
4. Submit a `Pull Request (PR)` to merge the user's git branch to main.

### Update SDDP

Reference: 
* `sessions/sdb_basics.md` where `Specification Driven Data Pipeline` 
is offered as one of the examples of `Specification Driven XXX`. 
* `sessions/client_multiagent.md` where we set up a 
`Exercise 2: Mini Data Pipeline` where we set up a plan.

### Update Data Pipeline

Reference link the `Mini Data Pipeline` exercise as an example of the
`Specification Driven Data Pipeline` (SDDP). 

Expand the `Mini Data Pipeline` with additional stages to:
* Unit Test Sample Data: few rows (<100) of the data are sampled and kept in 
`tests/data/pipeline` as a CSV file that then allows data engineers 
to unit test directly in their local sandbox.
* Develop a Skill in `prompts/skill.md`: the skill encodes a repetitive data 
pipeline task within the pipeline with a python script that transforms
data, a resumable prompt with instructions to also test the success of data 
transformation using the Unit Test Sample Data.
* Codify the entire data pipeline as a specification plan of phases and tasks 
dedicated to automate the `data pipeline`. 

### Model Swap and Open Weight Model

1. Add a session before the `AI Local` session. The objective of the session 
is for students to learn
* How to build AI-powered apps with pluggable brains
* Expose them to few `Open Weight` models. 

Name the session `Applications on Pluggable Models` or something more
appropriate.

2. Add set and install in instrcutions for various tools: 
* groq: tools/groq/setup.md
* openrouter: tools/openrouter/openrouter.md
* cline: tools/dev_workbench/cline.md

3. Reference these in the `Setup` section of the `Open Weight` session:
instruction
* [Groq](http://console.groq.com) 
* [OpenRouter](http://openrouter.ai)
* [Cline](reference to dev workbench with cline set up and install)


4. Separate the below section earmarked within >>>--- and <<<--- 
that has install instructions for Cline & OpenRouter, 
the setup and validation instructions, 
recommendations on Usage Model, and Tracking Token Usage 
into appropriate setup files in tools directory. 

Add references to the Setup Directory in the above new session that 
we are createing.

>>>---

1. Install Cline:
Extensions (Ctrl + Shift + X) --> Install Cline

2. Install OpenRouter:
https://openrouter.ai/ --> API Keys or BYOK --> Save Key --> Test

3. Setup Cline to use OPENROUTER
Launch Cline --> Settings --> API Provider, API Key, Model

4. Validate: In Cline `act as a conversational assistant and just say hello`.
If Cline responds setup is complete.

#### Usage Model

* Claude `Pro Subscription` as primary - use Claude extension enabled
conversation for thinking, reasoning, execution, validation, etc.
* OpenRouter as secondary - use for testing, cross checking, or when
rate limited in a session. Examples of cross checking are `plan` validation,
code review, etc.

#### Tracking Token Usage
Tracking is not exposed for subscribers and only enabled for PAYG (API Key) users:
* Anthropic: https://platform.claude.com/workspaces/ --> Workspace --> Analytics
* OpenAI: https://platform.openai.com/usage
* Gemini: Google Cloud Console → Billing
* OpenRouter: https://openrouter.ai/activity - shows requests, tokens, cost

<<<---

5. Separates the below section encloded within >>>--- and <<<--- 
that goes over the content into different sections on 
`concept`, `tools`, `setup`, `exercise`, etc.

>>>---

#### Student Lab: The "Brain Swap" Experiment
**Objective:** Learn to build an AI-powered Python application using **Open-Weight** models and understand how to switch "model brains" without changing your code.

---

##### Phase 1: Environment Setup
We will use the **OpenAI Python Library**, which has become the industry standard for connecting to almost any AI provider (including Open-Weight providers like Groq and OpenRouter).

###### **1. Install Python & Library**
Open your terminal (WSL Ubuntu or macOS Terminal) and run:
```bash
# Ensure your package manager is up to date
pip install --upgrade pip

# Install the OpenAI communication library
pip install openai
```

###### **2. Get Your "Passes" (API Keys)**
For this lab, we will use two providers that offer generous free tiers for students:
1.  **Groq:** Go to [console.groq.com](https://console.groq.com/) and create a free API key.
2.  **OpenRouter:** Go to [openrouter.ai](https://openrouter.ai/) and create a free API key.

---

##### Phase 2: The Code (The "Skeleton")
Create a file named `hello_ai.py`. This code is designed to be **provider-agnostic**, meaning it doesn't care which company is providing the AI, as long as they follow the standard protocol.

```python
import os
from openai import OpenAI

# --- CONFIGURATION AREA ---
# To swap brains, you only change these two variables!

# OPTION A: Groq (Ultra Fast)
# URL = "https://api.groq.com/openai/v1"
# KEY = "your-groq-key-here"
# MODEL = "llama-3.1-8b-instant"

# OPTION B: OpenRouter (Free Choice)
URL = "https://openrouter.ai/api/v1"
KEY = "your-openrouter-key-here"
MODEL = "openrouter/free" 
# --------------------------

client = OpenAI(base_url=URL, api_key=KEY)

def ask_ai(prompt):
    print(f"\n[Sending request to {MODEL}...]")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# The Exercise Task
user_prompt = "Write a 3-line Python script that prints 'Hello World' and the current time."
print("AI Response:", ask_ai(user_prompt))
```

---

##### Phase 3: The Lab Tasks

###### **Task 1: The "Hello World" Test**
Run your script using the **OpenRouter** configuration.
```bash
python3 hello_ai.py
```
*   **Observe:** How long did it take? What model did it actually use? (OpenRouter "Free" usually picks the best available open model like **Qwen 3 Coder** or **Llama 4 Scout**).

###### **Task 2: The "Brain Swap"**
Now, comment out the OpenRouter lines and uncomment the **Groq** lines in your script. Replace `your-groq-key-here` with your actual key and run it again.
*   **Observe:** Did the speed change? Groq uses specialized hardware (LPUs) that is often 10x faster than traditional providers.

###### **Task 3: Identity Check**
Change your `user_prompt` to: *"Who are you, and what is your architecture?"*
*   **Discussion:** Note how **Open-Weight** models (like Llama or Qwen) will often tell you their specific version, unlike "Closed" models that might just say "I am a large language model trained by [Company]."

---

##### Phase 4: Critical Thinking
1.  **Portability:** Why is it useful for a developer to use a library like `openai` even when they aren't using OpenAI's models?
2.  **Economics:** Look at your Groq or OpenRouter dashboard. How much did this lab cost you? (In most cases, it should be **$0.00**).
3.  **The "Open" Advantage:** If a company like Google or OpenAI went offline tomorrow, could you still run your "Hello World" app? 
(Hint: Research "Local LLMs" and **Ollama**).
---

<<<---

---

## Tweak Skills
[x] Status

### Specification Driven

Update `sessions/sdd_basics.md` section `Specification Driven Beyond Code` 
table to update the `Name` column for each row  reference to exercises that 
illustrate the Concept. 

For example, in instead of the Name being just 
vanilla text `SDD`, make it SDD clickable link that referes 
`client_application.md` section:
`Exercise — Group Meetup Organizer (non-agentic version)`

Update the other `Name` field of other rows to clickable links wherever an
exercise exists.

### Improve Exercise on Skills

#### Reference
Simmilarly, `prompting_advanced` session goes over the Concept of Skills, 
Plugins, and `Step 5 - Build a Minii Plugin (3 Skills Combined)` help
students learns Skills better. You could summarize the below:

``` text
EXTRACT PHASE
Help the student identify WHY the correction worked. Extract the structural 
difference between the vague and precise prompt. Name the skill pattern 
(e.g. "scope-bounding", "output-anchoring", "constraint-first").

GENERALIZE PHASE
Help the student rewrite the corrected prompt as a reusable template with 
placeholders — general enough to apply across domains but specific enough 
to prevent the original failure mode.

CATALOG PHASE
Ask the student: which phase type does this skill belong to? 
(e.g. setup, feature build, refactor, integration, testing). 
Add it to our prompts/skill.md - skill libraray: 
skill name, description, template, and one example usage.
```

#### Task

##### Concept
Please add in section in `prompting_advanced.md` where 
we introduce Skills concept: 
1. The general `discovery` best practice process of 
identifying a skill-able prompt. Do folks actually 
prompt the agent periodically and make it identify 
the prompt recipes - sequence of prompts that worked to 
deliver an outcome - and create skills out of it. Or
do humans realize a common pattern to solve problems
and then humans consciously collaborate with the 
agent to templatize and orient the prompt into a Skill?

2. The idea of "Extract ==> Catalog" steps of Skills. 
Reference the `client_multiagent.md` section 
`Exercise 2: "Mini Data Pipeline"` where this concept 
will be brought to life via that Exercise.

##### Exercise

Update step `6. Develop a Skill (Reusable Prompt)` of 
`Exercise 2: “Mini Data Pipeline”` where we help students 
learn building Skills for repetivite tasks. 
Specifically, craft how we extract from the prompt 
a repeatble reusable template version where few fields 
are set as placeholder to ensure it is GENERALIZED.

## [x] Streamline Setup and Install

This section attempts to streamline few sections, specially 
in the Setup and Install areas. 

### GitHub

Reference `tools/dev_workbench/dev_workbench.md`

Restructure the `Section 2 — GitHub Account and SSH Setup` 
just as we did in the `Section 3 — VSCode Setup` i.e. 
keep the concept of what all that Section should 
accomplish. 

BUT the actual termianal commands should 
all be in `tools/dev_workbench/github.md` including 
account setup, git hub config, ssh key upload to 
setup ssh connect, testing github connection, 
clone the repo, create a branch and switch to the
branch, etc.

### LLM Provider

Reference `tools/dev_workbench/dev_workbench.md`

1.  session has sections on `VSCode Setup` and `LLM Provider Setup`. 
Move the LLM Provider section *before* the VSCode Setup 
as we often reference the LLM Provider accounts in VSCode.

2. `tools/claude/cloud.md`: Inside the `Cloud Account Setup`, 
be specific about signing up claud.ai Pro Subscription - 
not free tier. Move the `Privacy Settings Setup` section 
to right after the `Set Up` section.

#### Primary Subscription Backup PAYG

1. Add a sub-section `Claude Multimode` in the `VSCode Setup`
section of `sessions/dev_workbench.md` that refers to 
`Claude Multimode Set Up` in `tools/dev_workbench/vscode.md`. 

2. Add a section `Claude Multimode Set Up` to 
`tools/dev_workbench/vscode.md`that sets up 
VSCode -> Claude Extension to support two 
modes based on how CLAUDE_CONFIG_DIR is set. The two modes
should support `Primary Subscription Backup PAYG`. 

3. Leave CLAUDE_CONFIG_DIR not set or set to `$HOME/.claude`, 
to set up the authentication as Pro Susctiption (defautl mode).
This is invoked simply when starting vscode in Linux as: 
`code .`

4. When CLAUDE_CONFIG_DIR is set to $HOME/.claude-payg to 
set up the authentication as PAYG (API) mode.
This is invoked by starting vscode in Linux as:
`CLAUDE_CONFIG_DIR=$HOME/.claude-payg code .`

5. Test/Validate active auth mode in use by VScode terminal as: 
`cat ${CLAUDE_CONFIG_DIR:-$HOME/.claude}/credentials.json` AND
by running /status inside Claude Chat window of VSCode - it 
should show the appropriate mode.

#### Multi LLM Provider and Multi Model

Add a section in `sessions/dev_workbench.md` that 
covers `Set Up` of `Groq`, `Set Up` of `OpenRouter`, 
`Set Up` of Cline, etc.

The actual terminal commands should reference the relevant 
files is `tools/groq`, `tools/openrouter`, and
`tools/dev_workbench/cline.md` respectively
with the concept of what the `Set Up` does kept in 
the section in `sessions/dev_workbench.md`.

Reference `sessions/pluggable_models.md`.
1. Move the terminal command in `Set Up` section to 
`tools/dev_workbench/multimodel.md` with the `Set Up` section
in `sessions/pluggable_models.md` only keeping the concept of 
what is accomplished in `Set Up`.

2. The `Set Up` section in `tools/dev_workbench/multimodel.md` should
expand the `Install OpenAI Python Library ...` to  install `openai`
and upgrade pip as well.

```bash
pip install --upgrade pip
pip install openai
```  

3. The `Exercise: The Brain Swap Experiment` section 
`sessions/pluggable_models.md` `Phase 1: Environment Setup`
should just have the reference to  `Install OpenAI Python Library ...`
secton that we just added to `tools/dev_workbench/multimodel.md`.


4. Add a small test case to validate Groq, OpenRouter, and cline
is working including (VSCode extension) 


### AI Local

Reference `sessions/dev_workbench.md`, 
`sessions/ai_local.md`, and `tools/ollama/setup.md`.

Assess whether the premature installation of the 
`Ollama` model would ONLY take up disk space or will
ALSO eat into the CPU/memory space and slow down all the
workbench exercise.

If the installation does NOT slow down the next few exercises,
then:
1. Add an `AI Local` section to `sessions/dev_workbench.md`.

2. Add a `Set Up` subsection that goes over the concept and
references `tools/ollama/setup.md` for actual commands.

3. Add a `Test` subsection that runs a quick test to validate the 
installation.

### Overall Objective

Comb through the sessions and keep the actual terminal commands 
for `Set Up` sections in `sessions` into `tools`. The `Set Up` 
section of each `sessions` has the concept of what all 
the `Set Up` should accomplishe.


## [x] LLM Wiki Cleanup
[ ] Status

### Update README.md
Update the column `Tool` in the agenda table of `README.md` 
for all the tools used in each session. For example, for the 
row on session `Developer Workbench` we should also add 
`Claude` to the Tool column.


### Update LLM Wiki Plan

1. The llm_wiki exercise `🏃‍♂️ The Exercise: Compounding Knowledge` 
in `sessions/llm_wiki.md` phase 1 to phase 3 overlaps with
the detailed plan set in `projects/llm_wiki/plan_template.md`.

2. The `sessions/llm_wiki` plan Step 1 to Step 3 should just talk 
about the concept of `Download Source` and `Ingest and Link` and
reference the detailed plan for any prompts or active work.

3. Validate the `Verify links` in Step 3 of LLM Wiki sessions 
is executed as Phase 4 Verification Step 2 of the detailed plan. 
As such, Phase 4 of detailed plan ensures links are correctly set -
`projects/llm_wiki/verify_links.py` does not exist and 
references must be removed. 

4. Step 4 of llm_wiki would only talks about key ideas and concepts
BUT not prompts:

Open **Obsidian Graph View**. Navigate `Home.md` and look for
connections between GPU Computing and the previous topics. Note
which existing notes gained new incoming links — this is where
your knowledge graph compounded.

> **If you chose your own topic:** navigate `Home.md` to discover
> which previous topics your new topic relates to — the cross-links
> reveal the connections. Then form your own synthesis question that
> ties your new topic to at least two existing ones.

5. Remaining part of LLM Wiki sessions can be left alone as they are
building off of the detailed plan. That is leave the two sections 
below as is: 
* `### Coherent Home.md Growth`
* `### Optional Extension — Group Meetup Organizer PKM`

## [x] LLM Wiki Reclean

### LLM Wiki README Summary and Reference from Session
* Add a new subsection right before `The First Ingest` subsection 
in `The Exercise: Compounding Knowledge` section of the session 
`sessions/llm_wiki` that goes over the framework of 
`projects/llm_wiki/README.md`. 


### Knowledge Graph Updates
The overall objective of the exercise 
`The Exercise: Compounding Knowledge` is to cover all 
scenarios of building/updating the personal knowledge 
graph, namely:
* New KG for a new subject, new articles
* Update KG for an existing subject, new article
* Update KG for an existing subject, updated of existing article
* New KG for an unrelated subject, new article.

Please **validate** all the above scenarios is covered by the 
different Phases/Steps mentioned in `sessions/llm_wiki`. 
Specifically, reword per the below suggestions:

* Phase 1 to Phase 3 of `sessions/llm_wiki` should be re-worded 
and re-referenced to make it consistent with the appropriate 
Phases of `projects/llm_wiki/SiliconAndAI/plan.md`. 
Note that the `plan.md` is already executing the Fetch, Ingest, 
Re-Ingest, ReLink of new or updated documents. 

* Remove the option of giving the user of choosing their own
topic in Phase 4 of `sessions/llm_wiki`. It just 
complicates the lesson. 

* Phase 4 of `sessions/llm_wiki` (adds a new source, re-ingests, 
re-links) should be re-worded and re-referenced to make it 
consistent with teh appropriate Phases of `projects/llm_wiki/plan.md`. 

* Reword section `Coherent Home.md Growth` and 
`Optional Extension - Group Meetup Organizer PKM` in the session
`sessions/llm_wiki` to emphasize that addition of completely 
new subjects as this one should be dealt by creating a 
completely different subdirectory inside `sessions/llm_wiki` 
with a parallel and new set of knowledge graph `Home.md`, 
`plan.md`, directories, concepts, topics, raw_sources, etc. 
whereas expansion of an existing subject with a New Topic as 
was done in Phase 4 of `sessions/llm_wiki` should be 
processes JUST as an enhancement of the knowledge graph 
already built for that subject and captured in the 
corresponding `Home.md` inside the directory corresponding to 
that Subject.

## [x] Pristine Plan Reset

Students executing `projects/llm_wiki/SiliconAndAI/plan.md`
start from a plan where all checkboxes are already `[x]`.
They need a clean slate to follow the exercise.

Add a `pristine/` subdirectory to each Subject
(e.g., `projects/llm_wiki/SiliconAndAI/pristine/`) containing:
- `plan.md` — identical to the working plan but with all
  Phase 1–4 checkboxes `[ ]` and `✅ COMPLETED` stripped.
- `articles.md` — all entries reset to `[ ]` (URLs kept).

The `pristine/` directory is committed to git and never
modified during execution — students copy from it; they
never write to it.

In `projects/llm_wiki/SiliconAndAI/plan.md` (working copy),
add `pristine/` to the `## 📁 Required Folder Structure` list.

In `projects/llm_wiki/SiliconAndAI/pristine/plan.md`
(clean copy), the `## 📁 Required Folder Structure` list also
includes `pristine/` so students see it as part of the layout.

Update `projects/llm_wiki/README.md`:
- In `## Repository Layout`, add `pristine/` to the subject
  directory block (after `analysis/`, before `<NextSubject>/`).
- In `### Adding a New Subject`, add a step after copying
  `plan.md` to create `pristine/plan.md` and
  `pristine/articles.md` as clean copies (all boxes `[ ]`)
  so students can reset before each run.

In `sessions/llm_wiki.md`, insert a
`### Before You Begin: Reset to Pristine State` subsection
immediately before `### Phase 1: The First Ingest` with `cp`
commands to restore these files before starting execution.

## [x] Skillify

Exploring if few repetitive and templatized prompts can be 
morphed into skills. Reference below sections.

### Generating Plan Steps

1. Plan changes: After updating the prompt_history.md with ideas 
on our next objective, we do the following to effect the 
associated change to `sdw/plan.md`: 

* Update`sdw/replan.md` where we only change the 
[Replan Prompt](sdw/prompt_history.md#<section>) where the 
<section> is replaced with the last section appened to 
`prompt_history.md`. 

* Prompt Claude chat window to "Execute `sdw/replan.md`"

Could the above workflow be encoded as a skill? 

* If so, where should we store the skill? 

* We should add to README.md on the section 
`Contribution Guidelines` section a subsection on 
* Instructions on how do we invoke the skill?

2. Generate Plan Step: During the generation of 
updates to the plan, each steps had to follow 
a set template as set forth in CLAUDE.md section on 
`Plan Update Protocol`, namely:
`Step N: <step name>` with refenences to 
CONTEXT, ACTION, ...

If the step generation itself should be 
organized as a templatized skill to ensure that 
the plan step generation is guardrailed to strictly 
follows that framework, then please do so and
guide as to where we store that skill and how do 
we ensure plan generation always invoke that 
templatized skill

### Plan-Step Skill Refinement (executed Phase 23)

The `/plan-step` skill template was updated to include a
`[ ] Status` line immediately after the step heading:

```
### Step N.K: <step name>

[ ] Status

CONTEXT: ...
```

This `[ ] Status` line is flipped to `[x] Status` when the
step is executed, providing an at-a-glance tracker inside
`sdw/plan.md` without modifying the five-field template.

## LLM Wiki Update
[x] Status

### Process Article

* Rename `SiliconAndAI` in `projects/llm_wiki/` to `silicon_ai`

* Rename `plan.md` in `projects/llm_wiki/SiliconAndAI/` to 
`proc_article.md`.

* Rename `plan.md` in ``projects/llm_wiki/SiliconAndAI/pristine`

* Rename all references to TEST in CLAUDE.md and other files
to VERIFY that describes a concrete manuual check (link scan, 
orphan check, wiki review), etc. Note that TEST is typically 
limited in its use to only validation of software code, not 
necessarily to content, documents, etc. 
<what to check manually — links resolving, orphan scan, wiki updated>

* Validate skill `/proc-article <subject>` to ensure that it reruns 
the specification plan that processes the contents in `articles.md`
in the <subject> within `projects/llm_wiki`.

* Ensure after all these file and directory rename and skill changes 
all contents and references (e.g. from README.md or CLAUDE.md) are 
consistent.

## Embedding
[x] Status

### Skill Update
Update the /replan skill so that it automatically set the mode to 
`Planning` whenever the skill is run.

### Embedding Session
The objective of this exercise is to 
* Create a session in 'embedding` and introduce the concept with 
visualizations as embedding is the underpinning concept of 
generative AI. Reference:
[embedding](https://www.3blue1brown.com/?topic=neural-networks&lesson=gpt)
* Demonstrate the ability to show multiple plots using matplotlib.pyplot
* Demonstrate how jupyter can be directly executed from VSCode (IDE) to
run through the different use cases.

#### Concept and Exercise
References:
* `.tmp/embedding` for embedding concept and exercises.
* `.tmp/polar_plots` for showing multiple plots and integrating 
`jupyter` and `ipykernel` in python virtual environment.

1. Add a concept and an exercise section that crystallizes the 
concept of embedding. Add toy exercises that visualizes via different 
prompts: 
* embedding: take few example words and see where they land
* clustering: how words cluster around similar words. 
* concept direction: how gender and plurality is captured
* attention: how embedding is influenced via neighborhood words.
* similarity: how similar words have high dot products versus 
orthogonal words have low dot products versus reverse 
words have negative dot products. 

Use matplotlib, jupyter, ipykernel (.venv), etc. from IDE (VSCode).

2. Add to .gitignore to ignore `*.bin` or any data related asset 
created to capture the word and phrase vectors.

3. Craft the workbench session so that we can complete it in 
30-45 mins for high school or undergrad non-CS grads.

4. Add reference to this session in agenda of README.md, and create
the project in projects folder.

5. If there is any setup, please add it to dev_workbench.md and 
reference the link to that setup in the `embedding` session.

### Install and Setup

1. Add a seciton to `dev_workbench.md` for creating python venv 
for the embedding session, installing pip-install, ensuring
requirements.in is compiled and requiremement.txt is pip-sync etc.
The installations instructions of `.tmp/embedding` and 
`.tmp/polar_plots` should be consolidated into one for this session,
such as consolidating the requirements.in and ensuring
`Jupyter` sees the virtual environment as available engine.   

Ensure that all setup steps are completed and the `embedding` session 
`Setup` section references the `dev_workbench.md` section just to 
be consistent with other sessions.

2. Add a section to `dev_workbench.md` for Setup/Install of 
`OpenClaw` - with actual commands in `tools/openclaw/` - 
to ensure that the other sessions (`client_agent.md` 
and `server_multiagent.md`) references are consistent.

## General Skills
[x] Status

We will update the agenda in README.md and add 
few sesions and associated projects.

### Human Driven Development (HDD)

Add a session with `Human Driven Development (HDD)` 
with a Concept and Exercise section as below.

#### Concept

Human conceptualizes the high level plan, drives the 
execution of each phase and step of the plan as well as the 
important activities of the plan. AI is used only as an aide
to fulfill details of each activity. 

This structure builds confidence on use cases with very 
high penalty of mistakes - missile attack system, enterprise
infrastructure - and customers demanding very stringent SLAs.

#### Ownership

* Human Structures Product Definition - conceptualized 
from Top to Down including modules, APIs/interfaces, 
interaction sequence, etc. - all human guided
* Building the meat of the individual modules, test cases, 
etc. are AI driven.

#### Exercise

Create a `Tower of Hanoi` game exercise in python that
accept the number of discs as one argument, and whether
the game should be played one step at a time via keystroke
or just all the moves are displayed at one shot.
The configuration after each move is rendered in ascii. 

### Specification Driven Development (SDD)

* Clarify the concept of SDD in the session on 
`Specification Driven Development (SDD)` as below

#### Concept

Human oversess while AI owns the activity
* Human Structures Specification - built via Plan
  * Human owns structure of specification - multi-phased, multi-step, 
  exit criteria
  * Human and AI cooperate to build specification, execution is AI owned
* Vibe Coded 
  * AI owns delivery with Humans specifying outcome in "free style" 
  conversations

### Update `Personal Knowledge Management (PKM)`

Reference 
1. `projects/llm_wiki/speed-reading/`
2. `experimental/speed_reading/`
3. [The Coming Wave](projects/llm_wiki/speed_reading/TheComingWave.pdf)

* Add the exercise on the session on `Personal Knowledge Management`
to include `Speed Reading` as below.

* In this exercise, we'll go over how to speed read books and create 
mindmaps using different agents specialized on different aspects of 
the work but cooperatively working to get the work done. 

Specifically we'll fill in all the missing pieces by going through 
an exercise that create a mindmap of the book `TheComingWave.pdf`.

Our belief of what the speed reading exercise is activiated is 
in experimental/speed_reading/overview.md - this may or may not be 
accurate and needs validation.

Reference the below steps which we believe is the right way to 
go through the entire mindmap exercise.

### build_mindmap.sh

Create a shell script 
`projects/llm_wiki/speed-reading/build_mindmap.sh`
that accepts as a mandatory argument a URL or a 
filename (qualified with directory) the book. 
Sanity check existence of URL or filename as 
well that the type of the argument are limited
to well known types, such as html, pdf, text, etc.
2. Default filename location is current directory.
3. Another argument is the output filename. 
Default filename location (directory) is current 
directory and default filename if `mindmap.html`  
i.e. filename is `./mindmap.html`.

Then the sequence is as below:
* Convert book to text
  * if in PDF/HTML/.. format → plain text - 
  pdftotext book.pdf book.txt or any PDF-to-markdown tool
* Fill templates/detailed-notes.template.md with the book's 
content - manually or via a pre-processing agent
* invoke `projects/llm_wiki/speed-reading/piper.sh` that 
orchestrates the remaining pipeline as below. 

### piper.sh

The `piper.sh` starts by invoking `Seth` where
`Seth` reads that file and produces mindmap-content.json and then
orchestrates the remaning agents.

piper-pipeline-orchestrator.md is Piper's system prompt 
(it describes what Piper should do). 
* The actual sequencing is a shell script `piper.sh`
* Assess whether we need to create the `piper.sh` using 
`piper-pipeline-orchestrator.md` instead of `piper.sh` 
calling 
`claude --system-prompt-file piper-pipeline-orchestrator.md` 
as its entry point. 
* Assume the workflow steps are executed using `Claude CLI` - 
`claude --print ...` with the next sequential step 
executed checking that the previous step completed 
successfully.
* Once we have made the `piper.sh` work correctly and 
the mindmap is created and reviewed manually, 
create a `README.md` with a very clearly articulated
`usage` section with an example workflow so that a
nyone can use this one to create a mindmap of any 
content.

#### Agents

We've a 3-agent pipeline driven by a shell script piper.sh that turns a 
book into an interactive HTML mindmap. Agents hand off work through 
local files — no network calls.

| Agent | Role | Input → Output |
| :--- | :---: | :---: |
| Seth | Content synthesizer | source notes → mindmap-content.json |
| Leo	| Layout engineer | content JSON → mindmap.html |
| Quinn |	QA reviewer	| HTML → APPROVED or NOT APPROVED with checklist |
| Piper | Orchestrator | sequences Seth→Leo→Quinn; loops on rejection |

#### Reconcile and Consolidate
With the above workflow validated to work, review and validate 
that the contents in 
`experimental/speed_reading/overview.md` is a fair representation of 
the entire pipeline. Absorb the content into 
`projects/llm_wiki/speed-reading/README.md`. Add the conceptual 
description of `build_mindmap.sh` in the `README.md` file as well.
The goal is that any student can read the `README.md` as a 
"usage guide" so that they can take any book or article and 
create a mindmap as a "utility".

#### Validation Test Cases
This section is just meant to be a comment for records as it has 
no bearing on the plan.
We'll *manually* run the `build_mindmap` on the below documents to 
validate that the entire pipeline is working as expected.
* [Company Lifecycle](https://linas.substack.com/p/anthropic-claude-study-ai-startup-playbook)
* [Company Infrastructure](https://x.com/benln/status/2054546806516654263?s=46&t=5Wh9qORxgNovMlyxUN25YA)

### Tower of Hanoi
Reference `projects/tower_of_hanoi/'
* Ensure `toh_prompt.md` and `README.md` is updated 
to reflect: 
  * All source code is in src directory and all 
t   ests are in src/tests and the below are honored. 
  * All test files imports are structured to realize that
    source python files are in src/ whereas tests are in 
    src/tests.
  * Command to actually run main.py.
  * Command to actually run all the test case.
  * All generated files formatted to have all columns no more 
  than 80 files and tabs to be 2 spaces only. 
  * All python files to use Python 3.12+ - ensure 
  `toh_prompt.md` reflects this requirement and `README.md` 
  is updated accordingly. 
  * 
  * For the generated python src and src/tests file do NOT use 
      * `from typing import ...` (use `from collections.abc import ...`)
      * `Optional` (use `type | None`), 
      * `Any` (`object` instead)
    * always use named parameters in methods
* main.py should have a `#!/usr/bin/env python3` starter; end invokes
```markdown
if __name__ == "__main__":
  sys.exit(main()) 

### Update Setup
Reference the below files and ensure that the utility scripts in 
group_meetup that sets up the environment for students are 
updated and consistent to make as much of the setup automated. 
* `sessions/dev_workbench.bd`
* `projects/group_meetup/`:
  * `labsetup.py`
  * `preflight_check.py`


### Dev Workbench Restructure

Material changes requested during Phase 26 execution:

1. **Remove section numbering** — `## Section N — Title` →
   `## Title` throughout `sessions/dev_workbench.md`.
   Rationale: numbered sections require renumbering whenever
   sections are added or removed.

2. **Move Run Lab Setup Script to end** — currently Section 5
   (before the integration test section); move to the very
   last section so students complete all tool-specific setup
   before running `labsetup.py` + `preflight_check.py`.

3. **Add `## PKM` section** — install dependencies
   `poppler-utils` (pdftotext) and `html2text` needed for
   the Speed Reading Mindmap pipeline. `labsetup.py` should
   automate both installs; `preflight_check.py` should
   validate both CLIs.

### Arguments

1. Reference `projects/llm_wiki/speed-reading/`

* Consolidate the contents of `piper.sh` into
`build_mindmap.sh` as it does not make sense creating 
a separate shell just for `piper.sh`

* Add `--help` argument to `build_mindmap.sh` for users
to understand usage, arguments supported, default values, 
etc.

* Comment and Annotate the `build_mindmap.sh` execution
in different phases, named appropriately. Example
names of the phases of the shell just as an example: 
`Argument Sanitizer`, `Utility Setup`, `File Converter`, 
`Seth Synthesizer`, `Leo Renderer`, `Quinn Validator`... 

* Add `--from-phase` to `build_mindmap.sh` for users
to resume activity from a specific phase with a basic
sanity to ensure that prior phase has completed. This is
important as often we run out of tokens trying to complete
work while some workflow was already completed and need
not be redone from scratch. 

For example, say the basic install phase was completed and 
then Seth agent completed the work by generating the
detailed-notes.md. However, Leo agent could
not, then we need not start from the beginning. 

Comment the script and `README.md` accordingly.

* Ensure all intermediate files are created with a 
prefix of book name. For example, for the book
`example/TheComingWave.pdf`, ensure the intermediate file 
detailed-notes.md created in `.tmp/` subfolder 
is created as `example/.tmp/TheComingWave-detailed-notes.md`.
Same prefix holds for the `.json` files created.

* Update contents of `README.md` to reflect the 
consolidation.

* Update the reference to speed-reading in 
`Personal Knowledge Management` session 
(`sessions/llm_wiki.md`) to ensure all references
are consistent. 

2. Reference `projects/tower_of_hanoi`:

* Add `--help` argument to `src/main.py` - 
add appropriate comment to teach students
the general hygiene that every program and script 
that is entrypoint for users should support a 
to understand usage, arguments supported, default values, 
etc.

### Motivation

Add a section `## Motivation` right at the top to main repo 
`README.md` in the form of a table in the form of 5 columns?:
* Domain where generative AI is transforming 
* Example of a legacy approach or company.
* Example of an `AI native` approach and company. 
* Description of why and what is `AI native` approach 
disrupting or transforming.

Few suggested examples below - fill the rows and
columns:

| DOMAIN | LEGACY | AI NATIVE | OBJECTIVE | TRANSFORMATION |
| :--- | :--- | :---: | :--- | :---: |
| Internet Search | Google | Chat GPT | How to best prepare for Multivariable Calculus | Offer knowledge fully reasoned, correlated, and organized rather than bunch of keyword matches | 
| Photograph | Photoshop |  | How to make our event memorable | Make pictures taken from my iphone look awesome |
| Coding | IDE | Claude Code | How to quickly ship my next software products with high quality | Coding agents generates code and tested with browsers and terminal |
| Manufacturing Plans |  |  |  |  | 
| Customer Relationship Management | Sales Force | Auracell | How to sell more and fast, but with less people | Automated Customer Records and Pipeline Management |
| Conversational Intelligence | Gong | 1mind | How can I close the deal with this customer | Offer intelligence, not just analysis | 
| Running Company | https://x.com/benln/status/2054546806516654263/photo/1 |   |   |   |
| AI Startup Playbook | https://linas.substack.com/p/anthropic-claude-study-ai-startup-playbook) |   |   |   |


### Sentinel Phase

Add a `sentinel` final-guard phase to the speed-reading
mindmap pipeline in `build_mindmap.sh`.

The sentinel is an independent verification agent that runs
AFTER Quinn approves the rendered mindmap. Its role:

* Use `agents/sentinel-final-guardian.md` as system prompt.
* Independently review the HTML — overrule Quinn if any
  rendering failure, cramped/overlapping nodes, broken
  layout, or hierarchy violation is present.
* If Sentinel outputs `NOT APPROVED`, retry Leo+Quinn+Sentinel
  (same `MAX_RETRIES=3` cap).
* `--from-phase leo` resumes the full Leo+Quinn+Sentinel loop.

Create `agents/sentinel-final-guardian.md` distilling the
strict verification rules from `piper-pipeline-orchestrator.md`
into a focused final-guard system prompt.

Update `README.md` (speed-reading) phases table to include
the sentinel row. Update `README-mindmap-system.md` workflow
step 8 to reference Sentinel (not Piper).

### Sanitize
* Mark the General Skills complete *after* explicitly documenting 
in `projects/llm_wiki/speed-reading/README.md` as well as in 
`build-pipeline.sh` that it is the representation of the objective 
as set forth in `piper-pipeline-orchestrator.md` - cross reference 
in `piper-pipeline-orchestrator.md` that `build-mindmap.sh` 
represents the mindmap pipeline or implementation of the 
metadata file. 
* Extract the `## Setup` subsection of 
`experimental/speed_reading/overview.md` and record the sanitized 
version of the waterfall ascii diagram into 
`projects/llm_wiki/speed-reading/README.md` subsection 
`## Pipeline Phases` showing the orchestrator as the 
central coordinator that feeds the different phases.
* Extract any ofhter section of 
`experimental/speed_reading/overview.md` and migrate into 
`projects/llm_wiki/speed-reading/README.md`.
* Git rid of `experimental/speed_reading` directory and 
its contents as they is no longer needed

## Speed Reading
[x] Status

## Revamp piper
Reference `projects/llm_wiki/speed-reading`:

* `piper.sh` is about 473 lines which is a lot of lines of code for shell script. 

* Reimplement `projects/llm_wiki/speed-reading/piper.sh` as a python 
program `projects/llm_wiki/speed-reading/src/piper.py` with 
main function and other associated python programs that is 
implemented using python 3.12+ using modern constructs with 
2 tabs a spaces and every line no more than 80 columns.

* `piper.py` should have the `#! /usr/bin/env python3` and
executable mode so that is can be invoked as 
`piper argumets ...`

* Modularize the logic into classes, methods, etc. with 
a main method invoked as 
---
if __name__ == "__main__":
    sys.exit(main())
---
* Ensure that any supporting python/pip utilities are captured 
in requirements.in that is installed inside a .venv in the 
`projects/llm_wiki/speed-reading/` directory. 
These installations can be captured in 
`projects/group_meetup/labsetup.py` and validated in 
`projects/group_meetup/preflight_check.py`.

* Review and update `projects/llm_wiki/speed-reading/README.md` 
to reflect the change from `piper.sh` to `piper.py` as well
as any other reference to `piper.sh` in any other file.

* Reference `projects/llm_wiki/speed-reading/.tmp/` has 
file `detailed-notes.md` - examine why files are still 
created without the `<book>-` prefix. For example, file
created should be `TheComingWave-detailed-notes.md`.

* Update the contents of `sessions/llm_wiki.md` to ensure 
that the exercise summary is taking `TheComingWave.pdf` to build
a mindmap for the book as `TheComingWave-mindmap.html`. 
The mechanisms and commands are captured in 
`projects/llm_wiki/speed-reading/README.md` 

* Run through an actual exercise of invoking the piper 
starting with the validator loop (as the previous
loops have run and are validated) i.e. 
Leo (map-creator) -> Quinn(QA) -> Sentinel (QA Final Gate).

* Once the mindmap creation is validated (as a test case
that the plan execution was success): 
  * Remove any files and content inside 
    `experimental/speed_reading/` as those Are not needed.
  * Remove `piper.sh` as that is not needed anymore.

### Track and Log

Current challenges in `piper.py`is tracking and resuming i.e.
agents may take a long time processing a long book. we may 
run out of token credits while we are in the middle. hence:  
* tracking: agents are run without an option to capture log
  track and understand what has happened. that is add a 
  mechanism to OPTIONALLY allow running agent with
  ability to stream agent (Seth, Leo, Quinn, Sentinel) 
  output to agent specific log. Note that the mechanism
  to show a summarized view of where we are in the waterfall
  agent phase should continue to work and is bare minimum.
  That way if any phase takes a super long time, we can 
  track whether and what it is doing by tailing the log file.
* resuming: we need a way to resume then from wherever 
  we were left hanging once token credits are refreshed
* ensure `--help` of `piper.py` is updated to clearly 
  explain the option to log.

Reference `projects/llm_wiki/speed-reading/README.md`. Update the 
`## Worked example - The Coming Wave (PDF)` section: 
* how the agent can be run with the option to log.
* how the agent's summary output in stdout of seeing the 
  waterfall continues to work without a lot of log output
  in the way.

#### Validate
* Review `projects/llm_wiki/speed-reading/README.md` to validate 
  that the manual way to run the `piper.py` to create a mindmap 
  for a book is accurate.
* Rename `projects/llm_wiki/speed-reading/example` to 
  `projects/llm_wiki/speed-reading/examples`. Run through 
  `piper.py` for URL 
  https://www.dench.com/blog/the-ai-native-company-playbook
  with current working directory as 
  `projects/llm_wiki/speed-reading/examples` to test that mindmap

### Debug, Track and Observe

Running `piper.py` against `the-coming-wave.pdf` exposed three
gaps: (a) agent log files were all 0 bytes despite the pipeline
appearing to run; (b) Leo wrote draft HTML directly to the
output directory, making it impossible to distinguish approved
from unapproved output; (c) when `piper.py` is spawned from
an agent or backgrounded, stdout is unavailable so the
waterfall progress view is lost.

Root cause of (a): `claude --print --output-format stream-json`
requires `--verbose`; without it the CLI exits with an error
that was suppressed (`stderr=subprocess.DEVNULL`), leaving
every log file empty.

Fixes applied (commit b06a4f5, feat/sessions):
* Added `--verbose` to the `claude` invocation in _run_agent.
* Reverted `_html_file` to `.tmp/` so Leo drafts never reach
  the output directory until Sentinel approves; `run()` copies
  the approved file after the validator loop completes.
* Versioned Leo drafts as `.tmp/<book>-mindmap-{N}.html` (N =
  attempt number) so the draft history is preserved across
  retries.
* Added `--waterfall-log <path>` CLI option; `PhaseDisplay`
  appends each waterfall snapshot (stdout mirror) to the file.
* Added **Track / Debug / Troubleshoot** section to README.md
  documenting: `pgrep` for process liveness, `wc -c` on
  `.raw.jsonl` for progress, `read-list.md` as authoritative
  completion signal, 0-byte log diagnosis, and attempt
  numbering convention.
  works end to end.

## Consolidate Agents
[x] Status

Reference `.agent` and `.claude`.

Claude, Codex, Cursor, Antigravity, etc. have different
conventions for operating protocols, skills, rules,
workflows.

### Objectives

* Consolidate into a common framework with references where
  appropriate so that loading the repo in ANY agent gives
  consistent, non-duplicated context.
* Specifically, this repo has `CLAUDE.md`, `.agent/`, and
  `.claude/`. Apply the DRY principle: one authoritative
  source for each policy; all other files reference it.

### DRY Requirements

* **Line-length rule (79 chars):** `.agent/rules/
  always-line-length.md` is the single source of truth.
  Remove the duplicate rule block from `CLAUDE.md` and
  replace with a one-line reference to the rule file.
  Update the rule file with Python/Markdown examples to
  match this repo (replace the Go-centric content).

* **AGENTS.md (Codex + Antigravity loader):** Both Codex
  CLI and Antigravity read `AGENTS.md` from the repo root.
  Create `AGENTS.md` as a **symlink to `CLAUDE.md`** —
  zero duplication; both tools get the same protocol.
  Add a comment at top of `CLAUDE.md` noting the symlink.

* **No new canonical file:** Honor DRY — do not create yet
  another standalone file. Use a symlink so there is one
  file (`CLAUDE.md`) serving multiple tool conventions.

* **Annotate agent-specific directives:** `.agent/workflows/
  ls.md` contains `// turbo-all` — an Antigravity/Gemini-
  CLI fan-out directive — with no explanation. Document it
  inline and in any overview section.

* **CLAUDE.md SESSION REHYDRATION:** Add step 0 instructing
  Claude Code to also read `.agent/rules/*.md` as always-on
  policies at session start.

### README.md Agent Conventions section

Generate a section in `README.md` that anyone can reference
to understand how rules, skills, and workflows apply for
each agent tool:
* Two-layer model: `.agent/` = universal canonical layer;
  `CLAUDE.md` / `AGENTS.md` (symlink) = thin provider
  loader files.
* Table: Construct / Canonical path / Invocation / Read by.
* "Not yet wired" note for Cursor, Windsurf, Copilot with
  their respective paths (`.cursor/rules/`,
  `.windsurfrules`, `.github/copilot-instructions.md`).

## Motivate GenAI
[x] Status

BACKGROUND: 
Enhance the `## 🌐 Motivation` section of the repo's `README.md` 
section that captures why studens should bother learning 
about `Gen AI` tooling and why has it taken over the world.

My current proposed rewrite of the section is below:

```text
# Why Generative AI?

You have probably been in this group chat:

> "Where should we go for the trip?"
> "Idk, somewhere not too expensive?"
> "Beach or mountains?"
> "Beach, but Maya gets seasick so no boats"
> "When is everyone free again?"
> *(47 messages later, nobody has booked anything)*

Planning a family or friends' vacation is messy because it is full of
**judgment calls**, not just calculations. That mess is exactly where
generative AI changes everything. Let's use it as our lens.

---

## The Example: Booking a Vacation

Think about everything that actually goes into "book a trip for the
family." It breaks into six kinds of activity:

1. **Understand the goal** — where do they want to go, for how long,
   what are the constraints (budget, Maya's seasickness)?
2. **Read the room** — figure out the family's taste, mood, and
   preferences, whether they say them out loud or not.
3. **Plan** — turn "book a vacation" into a real itinerary: which
   cities, what transport, where to stay, what to do.
4. **Search and recommend** — look across travel sites and suggest
   specific options ("if it rains, here's a great museum nearby").
5. **Reason** — weigh the pros and cons of each option using
   judgment, while respecting what the family actually wants.
6. **Book and pay** — act on the plan: reserve the flights, confirm
   the hotel, pay.

Now watch how three generations of software handle this list.

### Legacy apps: forms and fixed logic

Old-school apps could really only do **step 6** — book and pay — plus
make *you* do the thinking by filling out forms. "Beach or mountains?
Indian or Chinese? Budget under $2,000?" You do the deducing; the app
just collects answers and follows predictable rules.

They don't *understand* anything. They gather and they act.

### Predictive AI (Machine Learning): learning your taste

Then came ML. By learning from past choices, these apps could finally
handle **step 2** (deduce preferences) and **step 4** (search and
recommend). This is the "because you watched X, you might like Y"
magic. The app starts to *guess* what you want — but it still can't
plan a whole trip or reason through trade-offs on its own.

### Generative AI (Agents): understanding, planning, and acting

Generative AI handles the hard, human parts — **steps 1, 3, and 5**.
An agentic app can *understand* your goal in plain language, *generate*
a full plan from scratch, *reason* about competing options with real
pros and cons, ask follow-up questions across several turns, and then
produce a chain of actions that fit your specific situation — even one
nobody programmed in advance.

The leap: legacy apps follow rules, ML apps spot patterns, and
**generative AI makes judgment calls.**

---

## 🌐 The Same Story, Everywhere

The vacation example isn't a one-off. That same shift — from
*following rules* to *making judgment calls* — is happening in every
industry at once. In each case AI isn't just doing the old job a
little faster; it's changing **what the job even is**.

| Domain | Legacy | AI Native | Objective | Transformation |
| :--- | :--- | :--- | :--- | :--- |
| Internet Search | Google keyword ranking | ChatGPT / Claude | How to best prepare for Multivariable Calculus | Knowledge fully reasoned, correlated, and synthesised — not a list of keyword matches |
| Photography | Photoshop manual editing | Midjourney / Adobe Firefly | Make our event photos look professional | Describe the result in words; AI handles composition, lighting, and style |
| Software Development | IDE + Stack Overflow | Claude Code / Cursor | Ship quality software faster | Coding agents generate, test, and debug code end-to-end across the entire codebase |
| Manufacturing Planning | ERP + spreadsheets | Hadrian / Machina Labs | Optimise production scheduling for custom parts | AI reads CAD files, programs CNC machines, and schedules jobs autonomously |
| Customer Relationships | Salesforce CRM manual entry | Auracell | Sell more with less manual tracking | Automated pipeline management and customer records updated from conversation context |
| Conversational Intelligence | Gong call recording + analytics | 1mind | Close the deal with this customer | Real-time AI agent offers live intelligence and suggested responses, not just post-call analysis |
| Running a Company | Human-in-the-loop for every decision | [Autonomous AI orgs](https://x.com/benln/status/2054546806516654263) | Scale operations without scaling headcount | AI agents own workflows end-to-end; humans set goals and review exceptions |

Read down the "Transformation" column and you'll see the same pattern
as our trip planner: the human used to do the understanding, planning,
and judging — now the AI does, and the human sets the goal and reviews
the result.

The sessions in this workbench are designed to give you hands-on
experience with the tools that make these AI-native approaches
possible.

---

## What This Means for Software

This is why so many new applications are being built as **agents**.
They aren't just more capable than rigid, rule-based apps — they're
**adaptive**. They can handle situations the builder never imagined,
because they reason in the moment instead of replaying a fixed script.

And here's the part that matters for *you*: building these apps no
longer requires years of training. If you can describe what you want
clearly, you can build it. That's what this lab is about.

---

## Why Now? The Hardware Wave

AI ideas have existed for decades. What changed is that the **hardware
finally caught up**. *(Add the reference to the PKM session on "Silicon and AI.")*

NVIDIA and AMD are racing to put AI-capable chips into everyday
laptops, and Apple already ships AI-enabled Macs and iPhones. Powerful
AI is moving from giant data centers into the device in your backpack.

We have seen this movie before. When smartphones landed in everyone's
pocket, an entire wave of new ideas was unleashed — Uber, Instagram,
mobile banking — things that simply weren't possible before. Cheap,
abundant AI hardware is about to do the same thing.

The difference this time: **you can be one of the people who builds
the wave, not just rides it.**

---

> **The takeaway:** Generative AI doesn't just follow instructions —
> it understands, plans, and decides. And for the first time, the
> tools to build with it are in your hands. Let's start.
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
* Humans are incapable of reviewing and authentically standing 
behind their accountability unless they review the code. 
Note that rhe review can be limited to high level 
code constructs to endorse correctness but only feasible
those higher level structure is manageable in code size 
(~200 lines of code) and the code is structured neatly into 
components with separation of concerns.

2. Factors that drives HDD methodology are
* Humans are smarter but AI is faster. 
* AI gets confused unless given limited context - otherwise, you 
see deteoriated quality due to context overflow - that is focused 
and limited in scope at an instance.

## Update TOH
[x] Status

Reference `projects/tower_of_hanoi`. Note that the code base in
`src/` was generated applying the prompt in `toh_prompt.md`. Thus,
if you make any changes to code in `src/` update the `toh_prompt.md`
so that the code in `src/` can be created anytime by applying
the `toh_prompt.md`. 

### Changes to src code
1. Run /always-line-length on all the python code in the src/ directory.
2. Annotate with richer comments in all the classes and methods of the code - 
Specifically ensure the comments in tests/ directory is complete and fully
specified so that while running tests the user knows exactly the purpose 
and motivate of all test cases.
3. Validate the logic of the code in src/tests/. Specifically the 
empty_tower() in tests/test_tower.py seems incorrect as the 
Tower class ctor 2nd argument num_discs=3, shouldn't it be zero?

### Restructure src content
Offer a placeholder in the directory `projects/tower_of_hanoi` where
the modifications to `src/` do not pollute the original code with 
skeletal classes defined so that users can always start from skelete
class definitions.
Possible solutions are:
1. Copy src to src_copy and then fill in the classes in src_copy/
If so, how do we prevent the solution is not git checked in. Do we just
put src_copy/ in .gitignore. 
2. How do we ensure that the following classes are not modified:
* classes in the tests directory.
* classes in the step_write.py or ascii_renderer.py.
3. Possible solutions: 
* Should we just package them somehow that is not
modified? OR 
* In the interest of keeping everything simple, we let 
student duplicate everything user src_original to src/ and modifying?

### Solve
For demonstrating students, we need to show a sample solution. 
Create `projects/tower_of_hanoi/SOLUTION.md` where we document
example prompt we feed to solve the problem: 
* copy the code from `src` to say `src_copy`
* fill in the code in the methods of classes in src_copy/
* run the test in src_copy/tests
* validate all tests pass, validate src_copy is in .gitignore
* git add & commit - note only the SOLUTION.md is committed, not src_copy

### Approved Clarifications (pre-approval addendum)

The following changes were incorporated into Phase 30 before
the plan was approved (recorded per prompt history protocol):
* `SOLUTION.md` renamed to `toh_solution_prompt.md` to mirror
  the naming pattern of `toh_prompt.md` (prompt → output).
* Step 30.5 added: apply `toh_solution_prompt.md` via Claude
  CLI, create `src_copy/`, run `pytest src_copy/tests/` to
  validate all tests pass before marking Phase 30 complete.

---

## Restructure TOH Prompts

[x] Status


Restructure the Tower of Hanoi prompt files to follow a 4-step
HDD (Human-Directed Development) workflow. Replace the two
existing prompt files with four purpose-specific prompts, one
per phase. No section is dropped — every section from the
existing files maps to one of the new files as shown below.

### Section mapping

| Existing section (source file) | → New file |
|---|---|
| Teaching note, Context, Solution Approach, Style Rules (toh_prompt.md) | toh_problem_prompt.md |
| Objective: skeleton classes, utilities, CLI, README (toh_prompt.md) | toh_problem_prompt.md |
| Output: file list (toh_prompt.md) | toh_problem_prompt.md |
| Student Workflow (toh_prompt.md) | toh_problem_prompt.md + README.md |
| Objective: test suite item (toh_prompt.md) | toh_define_tests_prompt.md |
| Test Requirements table (toh_prompt.md) | toh_define_tests_prompt.md |
| Intro context, Steps, Constraints (toh_solution_prompt.md) | toh_complete_prompt.md |

### Four new prompt files

1. **toh_problem_prompt.md** — defines the problem; requests
   architecture: classes with method signatures and
   `raise NotImplementedError` bodies; utilities, CLI, README.

2. **toh_define_tests_prompt.md** — given the class definitions,
   produce the test suite structure: test class and method names
   per class plus integration; no assertions yet.

3. **toh_complete_tests_prompt.md** — given the test structure,
   fill in all test bodies with assertions.

4. **toh_complete_prompt.md** — given class definitions and
   complete tests, fill in class implementations one at a time,
   running tests after each to validate.

### README.md addition

Add a `## Running with a Prompt File` section with a sample
Claude CLI invocation:

  ```bash
  claude -p "$(cat ../toh_problem_prompt.md)" \
    --allowedTools "Bash,Read,Write" 2>&1
  # Add --dangerously-skip-permissions once the prompt is
  # well-vetted to skip per-action approval prompts.
  ```

---

## TOH Reorganize Solution Directory

[x] Status

Move the four HDD prompt files and the reference solution into a
single `solution/` subdirectory to make the project layout
self-explanatory:

  solution/
    prompts/   — four HDD phase prompt files
    src/       — reference solution code (was src_solution/)

Update README.md:
- Add `## Objective` section explaining the HDD exercise and
  its four phases.
- Update `## Project Structure` to reflect the new layout,
  tagging `solution/prompts/` as sample prompts and
  `solution/src/` as sample solution code.
- Update all cross-references (Student Workflow, Running with
  a Prompt File, etc.) to use the new paths.

---

## Update `## 🌐 Motivation`
[x] Status

Reference repo root `README.md`: Weave in a pithy and elegant 
version of the below snippet in the beginning of `## Motivation` 
section:

> You are already using genAI for chatting with chatgpt, claude, 
> gemini, etc. for any and all information. Then what more is 
> left that is worthwhile learning.

## Streamline Sessions
[x] Status

Reference: 
* [Motivation](experimental/motivation/motivation.md)
* [AI Computer](experimental/motivation/ai_computer.md)
* git diff for manual changes

Streamline the repo README.md and developer workbench setup. 

Manual changes
* AGENDA section of README.md is the second one and rewords/moved few 
other sections to later. 
* Updated Developer Workbench session and `## LLM Provider Setup` 
subsection as well as `tools/claude/cloud.md`.

### Objectives
1. Add a `Why learn GenAI` session as the first session in the AGENDA 
table that references the [Why learn GenAI](sessions/motivation.md) session.

2. Create a corresponding `Why learn GenAI` session that consolidates 
the content of `Motivation` and `AI Computer`. One mechanism could be 
to rename the section `## Why Now? The Hardwave Wave` of the 
`Motivation` file to `## Why Now? The AI Computer & AI Local Wave` 
and insert a story and summarized version of the `AI Computer` into 
that section.

3. Review the manual changes for correctness and consistency.

## Assistants and Agents
[x] Status

Reference [README.md](../READEME.md)

### Create a session 
1. Add a **concise** `agents_and_assistants` session in the AGENDA of 
README.md placed after the `Exercise: Embeddings Visualization` session 
with the content structure similar to other concept sessions. 

2. Basic concept of `Assistants vs Agents` are as below:
```text
Assistant is a complete application potentially with a user facing 
interface, one or many LLM(s), Tool(s) with persmissions, 
Knowhow(s) (aka skills), and a master agent to do work and spawn 
additional agents on demand. Example of assistant are 
Claude Desktop, Claude CLI, Antigravity, Claude.ai, Codex, etc.

Agent works by operating on a subset of resources that it has
been granted within assistant. It interacts with an LLM 
which in turn may ask the agent to call Tool(s) or invoke Knowhow. 
The response from the Tool or effect of the KnowHow is fed to the LLM.
This loop continues until the LLM response decides the job is done.   
```

3. Phrase title of the session as: `Concept: Agents and AI assistants`.

4. Ensure the contents of session's remain focused and short. 

5. Add to references section:
[Agents and AI assistants](https://drive.google.com/file/d/1hucHQ0QpD3mWeIofVjgvl2m4Nnej52Nm/view)

## Lab Setup
[x] Status

Reference projects/group_meetup:
* labsetup.py
* preflight_check.py
* labenv.yaml

### Issue
* projects/group_meetup/labsetup.py is not setting up cleanly.
* projects/group_meetup/preflight_check.py is not passing.

### Resolution
Fix in the scripts:
1.  Install ollama requires zstd for extraction
2. SSH to `ai-lab` fails although public key is already posted 
* reason is the destination is ai-lab or ai-lab-int depending on 
whether the user accessing server is inside the lab or accessing 
from the Internet. 
* labenv.yaml should have DOCKER_SERVER_ID as 192.168.4.23 if inside 
lab or 73.202.223.27 if outside lab. The COCKER_SERVER_SSH_PORT is 22 
if internal lab or 22439 if external - suggest a way to handle this cleanly.

3. gh commands may fail if gh is not installed.
* install gh if not installated 
* normalize the commands so that gh commands are handled cleanly

### Validation
* projects/group_meetup/labsetup.py should set up up cleanly.
* projects/group_meetup/preflight_check.py should pass

## Lab Update
[x] Status

Reference projects/group_meetup:
* labsetup.py
* preflight_check.py
* labenv.yaml

### Issue
* projects/group_meetup/labsetup.py is creating only server target ai-lab.
* Students could be accessing the server from the intranet (inside 
the lab) or sometimes from the extranet (via Internet from outside).
* Depending on from where labsetup is run, we would have saved against 
ai-lab the target as an internal private IP address or not.
* Instead, create two targets ai-lab-int and ai-lab in .ssh/config and
then students use the appropriate target depending on whether they are
inside the lab or not.

### Validation
Either ssh to ai-lab-int works or ssh to ai-lab works with the latter used
as default as students would mostly access the server via the Internet.

## Lab Update II
[x] Status

### Claude Multimode Setup

Reference `Claude Multimode Set up` of `tools/dev_workbench/vscode.md`
it seems outdated. 

Setting CLAUDE_CONFIG_DIR to $HOME/.claude or 
$HOME/.claude-payg is old. Remove that section as all we need 
to do to switch modes is set  CLAUDE_CODE_OAUTH_TOKEN - 
it has higher preference than ANTHROPIC_API_KEY.
When CLAUDE_Cecho ODE_OAUTH_TOKEN is unset pay-as-you-go 
ANTHROPIC_API_KEY is activated as long as it is set.

Example convenienece functions used to switch claude modes is
kept in ~/.bashrc:

```text
# MY_CLAUDE_CODE_AUTH_TOKEN is Pro/Max Subscription OAUTH TOKEN
# MY_ANTHROPIC_API_KEY is pay-as-you-go API Key

# Convenience functions to switch claude modes:
claude-subscribe() {
  # optional as CLAUDE_CODE_OAUTH_TOKEN has higher precedence
  unset ANTHROPIC_API_KEY
  export CLAUDE_CODE_OAUTH_TOKEN="$MY_CLAUDE_CODE_OAUTH_TOKEN"
  echo "claude set to - `claude auth status --text` - mode"
}
claude-api() {
  unset CLAUDE_CODE_OAUTH_TOKEN
  export ANTHROPIC_API_KEY="$MY_ANTHROPIC_API_KEY"
  echo "claude set to - `claude auth status --text` - mode"
}
# Default to subscription mode - OAUTH is active when
# both OAUTH and API are set
export CLAUDE_CODE_OAUTH_TOKEN="$MY_CLAUDE_CODE_OAUTH_TOKEN"
```

### MacOS Docker Setup

Reference section `macOS — Dev Container` of `tools/VM/setup.md`
The installation is setting up the user as `vscode` in the 
container. It should pick the username from the OS (eg `whoami`)
rather than `vscode` which may have been picked up from the
VSCode extension.

### Github

1. Reference section `GitHub Account and SSH Setup` of
`sessions/dev_workbench.md`.

Hyperlink the text (3rd bullet) where you "Generate and upload 
an SSH Key ..." with https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

2. Refererence `Test VSCode + GitHub + Claude Code Integration` 
section of `sessions/dev_workbench.md`

ADD Step 0 to "switch" to feature branch that was previously created
by adding the command line snippet below:
```bash
git switch feature/from_$GITHUB_USERNAME
```

### Lab Setup Script
Review `projects/group_meetup/labsetup.py` and
`projects/group_meetup/preflight_check.py`.

Validate that labsetup.py is idempotent. For example, everytime 
we run the script we post the SSH public key in the
discord channel - even if a new one was not generated.


### Claude CLI

Reference `tools/claude/cli.md`

1. Clean up section `Plugin Installs` last line 
`claude plugin update`.
The last line was cleaned up to the below - please validate:

```text
# Step 6 - Update all plugins
# Native plugins are auto-updated, 3rd party require manual updates
claude plugin marketplace update claude-code-plugins
claude plugin marketplace update claude-plugins-official
```

2. Clean up section `Install the VSCode Extension`. Eliminate 
the paragraph section starting `Once Installed` to the `settings.json`
added json example to keep sidebar open.

## Claude Code Native Installer Migration
[x] Status

`tools/VM/setup.md`'s WSL "Suggested workflow" Step 4 installs
Claude Code via `npm install -g @anthropic-ai/claude-code`. This
method is deprecated — Anthropic moved Claude Code to a
self-contained native installer and pulled/froze the npm package
after a packaging incident, so `npm install -g` now yields a
stale, broken CLI.

Fix: replace with the official native installer (already used in
`tools/claude/cli.md`):

```bash
npm uninstall -g @anthropic-ai/claude-code   # remove stale pkg
curl -fsSL https://claude.ai/install.sh | bash
```

Verify with `claude --version` and `which claude` — the binary
should resolve under `~/.local/bin/claude`, not node_modules.

## Lab Update III
[x] Status

Reference 
- `tools/claude/cli.md`
- `tools/claude/cloud.md`
- `tools/dev_workbench/cline.md`
- `tools/dev_workbench/vscode.md`

I manually edited the above file references. 
Please validate the correctness of these files. 
Specifically the below changes:
- vscode.md: WAL is typo for WSL
- vscode.md: GitHub extension is not needed as it is built in
- claude/cli.md, claude/cloud.md is about setting the API KEY
  and OAUTH_TOKEN and saving it in environment variables
- cline.md: about linking it LLM for different choices.

## Environmant Update
[x] Status

### Keys and Tokens
Reference
* tools/claude/cli.md
* tools/claude/cloud.md

### Disable Claude Connectors
Add a section to cloud.md where we save API_KEY and OAUTH_TOKEN to 
disable Claude Connectors - set ENABLE_CLAUDEAI_MCP_SERVERS=false 
env var. Add test to ensure connectors are disabled disabled.
Otherwise, claude will silently inject into every student's 
Claude Code CLI session and eat into context/token budget 
without anyone realizing why.

### Update "Planning"
Reference
* README.md
* sessions/planning.md

The README.md agenda table has "Concept: Planning" session that goes 
over both the Concept of planning and an Exercise. 

1. Update the sessions/planning.md to reference the 
projects/planning/plan.md that students should create.

2. Create an appropriate directory projects/planning that will 
host the solution.

3. Create with an empty plan.md with just the heading. 

4. Create a README.md in projects/planning with a heading 
and description that reflects the exercise section of 
sessions/planning.md. Create a back reference from 
projects/planning/README.md to the exercise section of 
the sessions/planning.md.

### Update Exercise and Projects

Review all sessions in the repo root README.md agenda section. 

Ensure the following: 

1. All sessions with an Exercise section (note sessions 
are in sessions/ directory) has a correspondingly 
appropriate directory in the projects/<project_name> 
directory inside which students can create or generate 
a solution. Note this is already done for the 
"tower_of_hanoi" exercise.

2. All projects/<project_name> has a corresponding 
README.md that has a heading and description with 
backreferences to the exercise section of the 
corresponding session (in sessions directory). 

3. The solution artifact could be inside one or more 
subdirs that has one or more or any of the following:
* plan.md eg planning/
* generated code eg tower_of_hanoi
* wiki knowledge graph (Home.md) eg llm_wiki
* ...

4. In any case the README.md of the 
projects/<project_name> heading and description 
must clearly layout the organization of the 
solution, the artifacts, the backreference to the
session with the Exercise section and the 
forwardreference from the session's Exercise section
to the projects/<project_name> folder where the 
solution is expected.

5. After completion of each exercise, add a small 
comment to git commit and push the solution to the 
corresponding origin branch created by and for the student, 
such as feature/from_john where 'john' is the github 
username environment variable ie $GITHUB_USERNAME='john'.  

6. Every projects/<project_name>/README.md must always
direct the agent to execute that project's plan.md per
the repo root CLAUDE.md operating protocol (Plan Update
Protocol, one step per turn, commit after each step).
The root CLAUDE.md already auto-loads regardless of cwd,
but students need this stated explicitly so they invoke
the agent correctly from inside a project subdirectory.

### Update DevContainer Environment
Reference:
* .devcontainer/Dockerfile
* .devcontainer/devcontainer.json

The linux LTS container is only built and updated in MacOS. 
Windows WSL takes care of Ubuntu-LTS VM creation. However,
whenever VSCode is opened in the repo root, the 
"Create DevContainer" message keeps appearing.

Device a way so that the devcontainer creation or udpate 
is not triggered in Windows/WSL or LinuxOS systems.

## Prescribe Workflow
[x] Status

Reference: README.md

Add a section to README.md that specifies a typical workflow of students 
on every session in the agenda, namely:
* Go through the sessions serially, do not jump ahead.
* Complete the development workbench setup 
* Join the discord channel for online lessons and coordination

## Familiarize with foundational tooling:
Reference: tools/dev_workbench/github_and_git.md

Basic GitHub/Git: Add a cheat sheet of commands that helps a developer 
collaboratively develop solutions with human peers and AI agents. 

Example of cheat sheet of "how to" scenarios and commands are: 
* inspect the history of git changes:
  git log --oneline --graph --decorate --all -10
* checkout a local branch fix/from_john (john is GITHUB_USERNAME)
  off of main. if the local branch is already created switch 
  to local branch.
* track changes made in the branch vs main:
  git log --oneline --graph --decorate --left-right \
  fix/from_john...main
* push, pull, merge, and rebase git branch
* create a pull request to merge the branch changes to main


For each session:
* Branch: Pull in and merge the latest in origin/main to local main. 
* Create a local branch off of local main if not existing OR 
  Switch to local branch if already created and ensure it has the latest
  merged changes from main.
* Grok the concept section
* Design, Develop, and Test the solution for the exercise section using the 
  appropriate AI tools inside the projects subfolder.
* Commit and Tag the changes to the local branch
* Push the validated code in the branch to origin/branch
* Submit a pull request to merge the branch changes to main.
* Send a note on discord channel to instructor letting her know the session 
  that you completed asking for feedback from the pull request submission

### Pre-approval file rename (recorded per prompt history protocol)

Before Phase 42 was planned, the user manually renamed
`tools/dev_workbench/github.md` to
`tools/dev_workbench/github_and_git.md` to match the broadened
scope of this section (GitHub setup + Git cheat sheet, not GitHub
alone). Phase 42 Step 42.1 repoints the 8 markdown links across
`README.md`, `sessions/dev_workbench.md`, and
`sessions/code_review.md` that referenced the old filename.

## Cleanup Repo
[x] Status

### Directories
Students mainly operate with below mentioned directories (any other 
directories are of use but not use regularly):
* setup: machine setup, environment setup, and installation of scripts
* projects: exercises
* sessions: for concepts and exercise descriptions

Work on the below directory reorganization:
* Rename sdw to 'software_defined_workbench'
* Reorganize all directores except projects and sessions under
a 'miscellaneous' directory. 
* Feel free to rename and create more subdirectories or flatten
directories under 'miscellaneous'.

### Setup Directory
'setup' directory should have two subdirectories:
* student: all configs (yaml) and scripts used by students
* instructor: all configs (yaml) and scripts used by instructors

#### Student
Move all the files in 'setup' prior to reorganization is moved inside
'setup/student/'.

#### Instructor
'sessions/instructor.md' has all the instructions for instructor. Move 
that to 'setup/instuctor/'. If there are scripts that better serve setting
up work for instructor (just as we had for student), does 
creating a corresponding labsetup.py and preflight_check.py for instructor 
make sense?

#### README
Update the README.md of the repo appropriately to reflect the reorganization
and any setup files/scripts reference that are relevant and appropriate
for a top level README.md file. 

### Consistency Check
Ensure all links and references to files and directories are 
consistent after the regoranization.

### Deferred: instructor automation scripts
Phase 43 moved `sessions/instructor.md` to
`miscellaneous/setup/instructor/instructor.md` but did not create
`labsetup.py`/`preflight_check.py` equivalents for instructors —
the question above ("does creating a corresponding labsetup.py
and preflight_check.py for instructor make sense?") is left open
for a future phase.

## Consistency
[x] Status

The consistency check in the previous setction ('Cleanup Repo') was not 
thorough and we need to do more.

Reference REPO root README.md

1. README section 'Repository Structure' is NOT readable. 
It does not looks like a repo tree structure with descriptions
annotated against the tree. Clean up.

2. README section 'Instructor Guidelines' is messed up. The
instructo preflight hyperlink points to the wrong location.

3. README subsection 'Contribution Guidelines' of section 
'Instructor Guidelines' referenced SDW_DIR/plan.md before first
defining the location of SDW_DIR.

4. README section 'What Goes Where' has references to 
'Best prompts', 'Failed prompts' and 'Plan frameworks'. We hardly
use those references. Remove them. 
On the other hand, students use 'setup/student/' for setting up 
their machine/VM and environment. Similarly, instructors will use 
'setup/instructor' for setting and validating student set up. 
Add those references in the 'Artifact' table of 'What Goes Where'.

---

## Repo Hygiene Documentation
[x] Status

Documented the existing GitHub branch-protection configuration for
`main` (required_approving_review_count=0,
require_code_owner_reviews=false, dismiss_stale_reviews=true,
required_linear_history=true, enforce_admins=true, no
force-push/deletion) in a new file
`miscellaneous/setup/instructor/repo.md`. Also documented how to
generate CLAUDE_CODE_OAUTH_TOKEN (`claude setup-token`) and
ANTHROPIC_API_KEY (`console.anthropic.com`) and set them as
optional GitHub Actions secrets for the `@claude review` PR
workflow. Cross-referenced `repo.md` from `instructor.md` and
from the README Contribution Guidelines. Mirrored the same doc
and cross-links into the companion `la_workbench` repo.
Marked [x] Status directly — this is a repo hygiene/ops record,
not a curriculum content phase routed through SDW_DIR/plan.md.

---

## Enhancing Sessions
[x] Status

### Update Assistant Family, Assistant, Agents

Reference 
* `sessions/assistant-family_assistant_and_agent.md`
* `miscellaneous/experimental/docs/agent_loop.md`
* Markdown section below describing the mental model of agents with 
3 nested loopsk, skills, subagents, skill execution boundaries, 
subscription vs payg accounts, etc.

```text
The clean mental model: **a skill is a *procedure* (possibly complex, possibly with embedded code and conditional logic) that runs in your context; a subagent is a *delegated reasoner* with its own context and its own loop.** If the work is "follow these steps," a skill suffices. If the work is "go figure this out, I don't want to watch you think, just give me the answer" — that's a subagent, and the value is the isolation, not anything the steps couldn't technically express.

A useful unifying picture: there are **three nested loops** — the outer agent loop (LLM-driven, dynamic, conditional), skills as **fixed sub-programs** that run beneath a single step of it, and subagents as **entire nested copies** of the outer loop with their own context. Your instinct to collapse everything into "one agent + skills" is architecturally coherent for *procedural* work; it breaks specifically where you need **isolated reasoning contexts**, which is a property of the runtime, not of what the steps can express.

- But the **subagent (the runtime construct)** is a place the harness can *attach* a distinct permission boundary. The parent might have filesystem-write; the subagent it spawns is configured by the harness with read-only.

A skill, by contrast, **executes within the parent's runtime and therefore under the parent's permission set** — it has no separate enforcement boundary the harness can independently scope. So "different tool permissions" is correctly stated as: *the harness can enforce a different permission scope on a subagent's context than on the parent's*, because the subagent is a separate runtime construct. It was never a property of the LLM. Your correction stands; the capability lives in the harness binding policy to context, not in the model.

A subagent boundary is *also* a permission boundary the harness controls — which is exactly why "subagent as isolated context" and "least-privilege enforcement" are deeply related. The isolation that gives you the context firewall is the *same* isolation that gives the harness a clean seam to attach a tighter credential scope. One mechanism, two payoffs.
```

#### Add agent loop visual 

Enhance section `### 🔹 Layer 1: The **Agent** — does *one* job well` of 
`assistant-family_assistant_and_agent.md`: 

1. Conceptualize the agent as an 'artificial human' and the LLM as its brain.
  Picturize an ascii art the agent that accepts a 'task' and then executes 
  'three nested loops' with description as laid out below:

2. Add a subsection on subagent as a context firewall with its own set of 
  scoped permissions as handed out by the parent agent's harness instance as 
  called out by referenced `agent_loop.md`
 
3. Add a subsection on skills as a 'fixed sub-program' but within the 
  context of the agent and within the scope of permissions of the agent 
  harness as called out by referenced `agent_loop.md`


#### Assistant

Enhance section `### 🔹 Layer 2: The **Assistant** — the resource manager (an "Agent OS")` 
of `assistant-family_assistant_and_agent.md`: 

Add a subsection on 'agent harness'. Define what 'harnesses' provide and how 
it is distinct from assistants.

State where some of the below example functionalities lie (harness or assistants): 
* managing interaction with users on interactive assistants 
* managing interaction with LLMs including error handling and 
  gathering response when it is trickling in.
* spawning agents/subagents and tracking their lifecycle
* managing interaction with tools including error handlign and
  gathering response from tools when it is streamed
* making skills/plugins and connectors available to agents
* scoping the permissions offered to subagents

---

Review the section below wrt subscription vs PAYG account and reword,
summarize, restate as appropriate.

#### Account

Add a separate section on different types of accounts. 

1. Subscription Account - example claude.ai
2. Pay-As-You-Go (PAYG) Account - example platform.claude.com

##### Table contrasting **Subscrition vs PAYG** account 
Create a table contrasting the `Subscription` account (claude.ai) vs 
`PAYG` (platform.claude.com) account wrt:

1. For Subscription account:

* Credential Generation is user friendly as personal assistants 
redirect the session to a user browser login session using oAuth 
flow. An example trigger is via `claude CLI` command line options 
`claude auth <login | setup >`. 

* Credential Storage is local either inside user's home directory 
(eg. ~/.claude/.credentials.json) or saved in shell's environment 
variables (eg. CLAUDE_CODE_OAUTH_TOKEN).

* Credential Submission is automatic as the personal 
assistant applications are already programmed to look at specific 
file locations or shell environment variables. 

* Resources: Connectors and skills uploaded to claude.ai account are 
automatically synchronized and made available to personal assistants 
that are running on client devices, such as Claude CLI, Desktop, 
Browser extension, Powerpoint extension, etc.

* Token cost: reference below (PAYG account) Tokenomics section to 
compare and contrast the cost.

2. For PAYG account:

* Credential Generation is via specific workflow in the account to 
generate API_KEY.

* Credential Storage: As this is stored in cloud (not user's personal device),
one has to upload and store them in a vault. 

* Resources: Every resource must be separately uplodaed and made availabe 
to the agents. 

* `Tokenomics`: As of now, the price per token for PAYG API KEYS vs subscription 
based is almost 7:1. Thus, for any use case that can be solved by individuls, 
users are encouraged to use subscrition mode.

##### Managed Agents
Add a subsection on `Managed Agents`. 

`Managed Agents` are used in cases where the agent's purpose is not tied 
to a specific user. To relieve one from the DevOps burden of operating
the underlying infrastructure (kubernetes), these agents are run 
on provider's infrastructure ie. NOT on user owned client devices.

Example of use cases where `Managed Agents` are used:

* Non-interactive use cases, such as CI/CD, Pull Request, Cron Jobs, and 
Slack channel initiated tasks.  

* Multiple-player collaboratively executing a goal/task on the same session 
(eg. troubleshooting) where players hand off a session midway to other players 
without losing any context. The multi-player scenario uses claude tags as 
identity for scenarios where user identity does not make sense. An example, 
is a slack channel triggered task with the channel members having 3 engineers 
and one product manager that kick off set of work items.

Since `Managed Agents` are not linked to a specific user, it is only available in 
PAYG account (platform.claude.com) rather than a user's tied subscription account.
Thus, API_KEY is the only supported consumtion mode.

Furthermore, they require a separate manual submission of
* credentials as the underlying task is not necessarily tied 
to a single user and does not inherit user credentials.
* connectors for mcp server tool calls as specific user 
tools aren't appropriate for a groups of users or server tasks. 

### Update Anthropic Auth
Reference:
* `miscellaneous/tools/claude/cloud.md`
* `miscellaneous/tools/claude/cli.md`
* `$HOME/.claude/.credentials.json`

Note `$HOME/.claude/.credentials.json` is for interactive human use 
on a client laptop (personal device) whereas CLAUDE_CODE_OAUTH_TOKEN 
is for automated/headless use (CI/CD job, container service) where you 
accept that we are using for inference trading it off in exchange for 
portability.

Hence, I made changes to `cloud.md` and `cli.md`.

Validate that the isntructions are consistent in the files AND that:
* `miscellaneous/tools/claude/cloud.md` does not set API KEY or OAUTH TOKEN
* `miscellaneous/tools/claude/cli.md` does not set API KEY or OAUTH TOKEN
* `$HOME/.claude/.credentials.json` is used for authenticating.

### Objective

* assistants_agents.md was renamed to assistant-family_assistant_and_agent.md
  Review the rewording of the file, validate correctness, add the examples. Edit
  as appropriate for clarity and simplicity.

* Expand the concept and exercises sections on 'Vibe Agentic' and 
  'Dynamic Agenting' to session 'LLM Wiki' per sections below.

* Expand the exercises on session 'LLM Wiki' with the 
  subsection on 'Optional Extension - Speed Reading Mindmap' to
  elaborate and illustrate the 'Vibe Agenting' and 'Dynamic Agenting'
  concepts with corrresponding exercises per guidelines below.

To elaborate, review (and rephrase as appropriate) to incorporate the 
below concept and exercises. 

### Concept

#### Vibe Agenting - Concept

The model/LLM of the coordinator decides fully on subagents:
* when are they created - dynamically created on demand by parent model
* what is the function - dynamically determined by parent model as to 
the functions each subagent would provide
* what is the permission boundary - determined by the parent harness
and permissions may even be downscoped as the harness spanws the 
subagent. note permissions are never determined by LLM to maintain
separation of concerns and make it deterministic. note scoping is 
not managed via declaration file and scoping subagents are limited
by the ceiling of permissions held by the parent agent.
* observability, tracing, and lifecycle is managed by parent harness

The activation of LLM to 'vibe agent' is automatic and can be explicitly 
triggerd by adding a high level prompt to the assistant
`use subagents as appropriate`.

#### Dynamic Agenting - Concept

The subagent functionality is pre-determined and declared - 
(name, description, and tool surface) and captured in a 
markdown file specification document. 

The discoverability of these child agents and routing is driven 
by the model/LLM of the `coordinator agent`. The parent model 
can see and choose among these subagents. 

The first-class agent definition is also a natural seam to 
attach scoped tool permissions, a distinct system prompt, 
a different model, and audit identity — declaratively, is 
enfored by and is the job of the harness. The subagent 
declaration can also help in customizing the permissions 
boundary to the agent specification.

Platforms treats declared agents as first-class objects with 
per-agent traces, token accounting, rate-limit handling, retries, 
failure isolation, "which agent did what", etc. 

#### Static Agenting - Concept

The model/LLM of the cooridnator is used to drive and execute each 
subagent. That function of each agent is static. The number of 
sub-agents spawned by the 'Coordinating Agent' is predetermined.

The routing decision and judgment of which *specialist* to invoke 
is moved from the model to the code. In addition, the developer is 
responsible for configuring the permissions/scope for each subagent.

Subagent dispatch logic, lifecycle management, retries on errors and 
failures, gathering the result from each subagent, passing appropriate 
permission boundary (picked from declaration or decided directly in 
code), directing the observability stats of each subagent, etc could 
now come from the developer's imperative code - something that offers 
more control but may lead to more mistakes as code audits are harder.

### Exercise

#### Reorganize

I've already done the following:

1. Created sub-directories inside 'projects/llm_wiki/speed-reading' dir:
* static: all the files (except README.md) that was previously in 
 'speed-reading' has been moved to that dir except README.md
* dynamic: 
* vibe: soft link ai-mindmap.md, speed-reading.md, and templates
  in that directory.

2. Moved the contents (webpage and PDF files) to 
   'projects/llm_wiki/speed-reading' directory.

Note that the contents/ folder will be shared by the static, dynamic, 
and vibe agenting exercises.

### Vibe Agenting - Exercise

Confirm that only the ai-mindmap.md, speed-reading.md and templates/
are visible in the vibe directory.

Prompt your AI assistant:
```text
Study the contents of speed_reading directory.
Study a book-pdf placed in any directory
Start drawing a mind map in that directory by descending into layer 1.
Render the drawing built so far. 
Use subagents as appropriate.
```

Note that based on the mindmap drawing you could choose a node <name> 
and prompt your AI assistant: 
```text 
Descend on layer 1 node <name> to layer 2.
Use subagents as appropriate.
```

### Dynamic Agenting - 'Speed Reading' Exercise

This is an exercise similar to 'vibe agenting' except that the 
agent work for a given agent is decided statically ie the prompt
that decides functionality of a given agents (what an agent 
does) is 'pinned' using the corresponding md file. 

Reference 'projects/llm_wiki/speed-reading/dynamic/' directory

1. Ensure that only following files are visible to the assistant:

* ai-mindmap.md
* speed-reading.md
* templates/

Specifically the agents directory should NOT be visible as we 
want claude to do vibe agenting, where we ask AI to create the
Child or Specialist agents based on functions it wants these
Specialists to run as well as when to create these agents.
 
2. Run the 'Claude CLI' inside the 'dynamic' dir.

* In the interest of speed, convenience, and to save yourself 
the pain of approving permissions everytime claude runs a 
command, grant 'full access' by run `/permissions` 
so that it does not ask you again and again when running 
various commands.

* Prompt 'Claude CLI' assistant to create an agent 'plan':

```text
Study the speed reading system in the current directory. 

You be the Orchestrator agent.
Suggest what specialized subagents we create to do the work 
by creating additional subagents. 
In addition, ensure you create a QA subagent to validate 
the work created.

Create an agents sub directory in the subdirectory 
"examples/.tmp/" and make md files for each of these 
sub agents inside the "examples/.tmp/agents" subdirectory.
```

3. Exit the 'Claude CLI' session to start afresh again in the 
'dynamic' directory. 

* The objective is to demonstrate how the agent mindmap
artifact definitions are read and then those agents
run to create a mindmap.

* Prompt 'Claude CLI' assistant:
```text
Study the material in the current directory.

Read the book that is in the examples/ subdirectory.

Create subagents corresponding to the information in 
"examples/.tmp/agents" subdirectory while you be the 
orchestrator.

Produce the mindmap html in the examples/ subdirectory. 

Create any intermediate artifacts, such as json, md, 
logs, jsonl, etc. files in examples/.tmp subdirectory.  

Descend only into layer 1.
```

4. You can exit a 'Claude CLI' session (Ctrl-C) and 
'resume' the last session: `claude --resume`

5. View the mindmap.html in the browser as it builds
over time.

6. Review the layer-1 mindmap and then expand the 
map from a specific node(s) of your choice.

Replace <name> with the name of any specific node 
where you'd like to descend and build mindmap. 
```text
Descend into layer2 for the node <name>
```

#### Static Agenting - Exercise
Reference: 'projects/llm_wiki/speed-reading' dir

Current exercise content illustrates and only focuses on the concept 
of 'Static Agenting' where the agent functions are determined per the 
markdown descriptions of each agent in 
projects/llm_wiki/speed-reading/agents.

##### Update Exercise

1. Modify the piper.py script in source to accept two optional arguments:
* --from-node 'node-name' - node from where we descend; when no argument is 
specified we assume it is start from root.
* --level <int> - the level number that we descend from that node; when
no argument is specified we descend down to all levels from that node.

2. Update README.md that is completely focused on 'Static Agenting' to have 
three sections, one each for the different kinds of agenting.
* Modify the exercise section to only descend till level 1 from root.

### Validation
* README.md in each subdirectory of 
'projects/llm_wiki/speed-reading/', namely vibe, dynamic, static correctly 
captures the purpose and how to execute 'vibe agenting', 'dynamic agenting'
and 'static agenting' respectively. 
* README.md in 'projects/llm_wiki/speed-reading/README.md'
* 'projects/llm_wiki/speed-reading/static' contents was formerly directly 
under 'projects/llm_wiki/speed-reading/'. This reorganization may have
broken the code in src and references in the various directories. Please 
review, validate, and re-reference cross links across files.

### Add Credits
Reference:
* sessions/hdd.md
* sessions/assistants_agent.md
* sessions/llm_wiki.md

#### Credits
* Add a 'References' section to llm_wiki. Add a reference stating 
"Assistant, Agents, and Vibe & Dynamic Agenting" that hyperlinks to 
https://drive.google.com/file/d/1BUnt-rTb0X1Nc93z6by6B5ndFViPu8IH/view?usp=sharing

---

## Modularize

[x] Status

### Replan
Current /replan skill does the planning as well as executes (from Step 4) onwards.
Create a `/execute` skill that executes the plan starting Step 4 and strip those
steps from `/replan`.

### Update README

Reference `projects/llm_wiki/README.md` 

Current `README.md` solely focused on building knowledge
graph that is exhibited in `silicon_ai/` rather than `building knowledge`, 
which could be `creating a knowlege graph wiki`, `building mindmap`, or 
any other exercise that enhances personal knowledge.

Move the content inside README.md that is specific to `silicon_ai/` or 
knowledge graph wiki part into `silicon_ai/`.

Reformat or create the content in the README.md to cover any 
personal knowledge management.

Add references to the subdirectories that supports PKM. Review and reword 
as appropriate - a sample references:
* `silicon_ai`: builds wiki and enhances understanding by supporting 
questions or analysis only relying on the wiki content
* `speed-reading`": builds mindmap that enhances knowledge by 
organizing content in visually intuitive concepts showing relationships 
and organized in layers.  

---

## Contribution Mechanism Reflected from la_workbench
[x] Status

The companion repo `la_workbench` (`../la_workbench/`) added a
student solution submission and completion-report mechanism —
reference its `SDW_DIR/prompt_history.md` `## Contribution` section
(and its "Addendum: Refined Requirements" subsection) for the full
prompt. Mirrored the same mechanism here:

* README.md: new `## 📤 Submitting Exercise Solutions` section
  (after `## 🔁 Student Workflow`) documenting the
  `projects/<project>/<github-userid>/` submission layout, the
  `project/<project>/<github-userid>` PR naming convention, and the
  automatic completion reports that follow a merge.
* `miscellaneous/report/report.py`: scans `projects/*/*/solution.md`
  for bare-userid Contributors and generates two things:
  1. `miscellaneous/report/report.md` — the class-wide topic x
     student completion matrix.
  2. `miscellaneous/report/student/<github-userid>-report.md` — a
     **per-student report generated/updated on every checkin**
     (every merged solution PR), not just the class-wide table.
* Each contributor's **Full Name is resolved from their bare
  GitHub-UserId** via the public GitHub Users API — students no
  longer type their name into `solution.md` by hand.
* `report.py` is **idempotent**: re-running it with no new or
  changed submissions leaves every generated file byte-identical
  (a student's report only changes, and its date only bumps, when
  their actual completions change).
* `.github/workflows/report.yml`: since `main` blocks direct pushes
  even from Actions (`enforce_admins: true`, "restrict who can push:
  no one" — see `miscellaneous/setup/instructor/repo.md`), the
  workflow regenerates both the class-wide and per-student reports
  on every merged solution PR and lands them via its own
  auto-created, auto-merged PR (0 approvals required).

Edits only — left uncommitted pending explicit maintainer
confirmation before `git add`/`commit`/`push` in this repo, per this
repo's own git-hygiene norms.

---

## Cleanup Contribution Reflected from la_workbench
[x] Status

The companion repo `la_workbench` (`../la_workbench/`) ran a
cleanup/rename pass over the contribution mechanism reflected above —
reference its `SDW_DIR/prompt_history.md` `## Cleanup Contribution`
section for the full prompt. Mirrored the same restructure here:

* Moved (would move) each exercise's student subdirectories under a
  `solutions/` folder, e.g.
  `projects/<project>/<github-userid>/` →
  `projects/<project>/solutions/<github-userid>/` — no student
  solutions exist yet in this repo, so there was nothing to move.
* Renamed `miscellaneous/report/` → `miscellaneous/reporting/`,
  `report.py` → `generate_reports.py`, the class-wide `report.md` →
  `summary_report.md`, and `student/` → `for_each_student/`.
* Added a `**Full Name:**` line to each per-student report (the full
  name previously only appeared in the H1 title).
* Generalized `collect_completions` to discover every `solutions/`
  directory anywhere under a project via `rglob("solutions")`,
  instead of assuming it always sits exactly one level down — a
  project's exercise may be split into subparts (e.g.
  `projects/<project>/partA/solutions/`), each with its own
  `solutions/` directory at a different depth.
* Tightened the idempotency guard to compare full per-student report
  content (with only the date line normalized out), not just the
  table body, so schema changes like the `Full Name` addition are
  correctly detected as a one-time rewrite while unrelated re-runs
  stay a no-op.
* `.github/workflows/report.yml`'s changed-file detection switched
  from a fixed-depth pathspec glob to a depth-agnostic regex match
  (`^projects/.*/solutions/[^/]+/solution\.md$`) on the diff output,
  matching the generalized directory discovery above.
* README.md's submission section and the workflow's run
  command/`git add` target updated to match the new paths.

Edits only — left uncommitted pending explicit maintainer
confirmation before `git add`/`commit`/`push` in this repo, per this
repo's own git-hygiene norms.

## Gaussian Elimination Reporting Reflected from la_workbench
[x] Status

The companion repo `la_workbench` (`../la_workbench/`) discovered
that its Systems of Linear Equations session grew two distinct
exercises (`np.linalg.solve` vs. hand-rolled Gaussian elimination)
under one topic, and its completion report was lumping both into a
single topic-level checkmark instead of crediting each separately —
reference its `SDW_DIR/prompt_history.md` `## Gaussian Elimination`
section for the full prompt. Mirrored the reporting fix here, since
this repo shares the same `generate_reports.py` design:

* Added `SOLUTION_TITLE_RE` and `parse_solution_title(solution_md,
  default)`, reading a solution.md's own leading `# Solution:
  <Title>` heading as its exercise identity (falling back to the
  session's topic title if the heading is missing).
* Changed `collect_completions`'s return type from `dict[str,
  set[str]]` (slug → contributors) to `dict[str, dict[str,
  set[str]]]` (slug → exercise title → contributors), built via a
  single `rglob("solution.md")` per slug rather than walking
  `solutions/` directories and assuming a fixed nesting depth.
* `write_class_report` and `student_table` now add an `Exercise`
  column and emit one row per (topic, exercise) pair, so a session
  with multiple exercises shows multiple rows instead of one lumped
  row.
* README.md's submission section now documents that solution.md
  must open with a `# Solution: <Exercise Title>` heading, since
  the report depends on it to label and credit each exercise.
* No student solutions exist yet in this repo, so the regenerated
  `summary_report.md` still shows every topic with a blank
  `Exercise` column — verified the script runs cleanly and stays
  idempotent on a second run.

Edits only — left uncommitted pending explicit maintainer
confirmation before `git add`/`commit`/`push` in this repo, per this
repo's own git-hygiene norms.

## Cleanup Solutioning Reflected from la_workbench
[x] Status

The companion repo `la_workbench` (`../la_workbench/`) ran a
cleanup pass over three loose ends in the contribution mechanism —
reference its `SDW_DIR/prompt_history.md` `## Cleanup Solutioning`
section for the full prompt. Mirrored the applicable changes here:

* Moved `miscellaneous/setup/instructor/repo.md` →
  `miscellaneous/setup/admin/repo.md` (admin-facing content, not
  teaching content) and updated README's link to it.
* Added `miscellaneous/setup/admin/member.md` (`gh api` commands
  to check your own/another's collaborator role and to add/promote/
  demote contributors and maintainers) and
  `miscellaneous/setup/maintainer/pull_request.md` (`gh pr`
  commands to list, approve+merge, request changes, amend, and
  close PRs).
* Created `miscellaneous/reporting/solution_template.md` (a clean,
  ready-to-copy solution.md with the `# Solution: <Title>` heading
  and Contributors/Summary/Solution Manual/Test Cases/Software
  Installs sections already laid out) and replaced README's
  verbose inline section-list under the submission step 3 with a
  pointer to copy this template instead.
* Added `miscellaneous/reporting/validate_solution.py` (imports
  `PROJECTS_DIR`, `SOLUTION_TITLE_RE`, and `parse_contributors`
  from `generate_reports.py` to reject a solution.md missing the
  Solution heading or an empty/placeholder Contributors section)
  and `.githooks/pre-commit`, which runs it against staged
  solution.md files. `labsetup.py` now runs `git config
  core.hooksPath .githooks` automatically (a new `REPO_ROOT`
  constant and `_configure_git_hooks()` call at the top of
  `main()`), and README notes the automatic validation.
* Verified `generate_reports.py` tolerates a malformed solution.md
  without crashing (a scratch test in la_workbench confirmed it
  simply credits no one for that file rather than raising).

Unlike this repo's prior two reflected entries, this phase's
prompt explicitly authorized **committing** these changes here —
push to origin is still left manual, per this repo's own
git-hygiene norms.

## Pull Request Reflected from la_workbench
[x] Status

The companion repo `la_workbench` (`../la_workbench/`) reorganized
its three admin-facing docs around GitHub's three permission roles
— reference its `SDW_DIR/prompt_history.md` `## Pull Request`
section for the full prompt. Mirrored the same restructure here:

* Consolidated `admin/repo.md` + `admin/member.md` into one
  `admin/admin.md`, prefixed with a new "Section 1 — Validate your
  admin role" (`gh auth status` + `.permissions.admin` check) and
  renumbering both files' sections into one flat sequence.
* Renamed `maintainer/pull_request.md` → `maintainer/maintainer.md`
  ("everything a maintainer should know," not just PR review),
  added a "Validate your maintainer role" section
  (`.permissions.maintain` check), and fixed its cross-link from
  the old `admin/repo.md` to `admin/admin.md`.
* Added `contributor/contributor.md` (new): validating contributor
  (`write`) access and submitting a PR named to match this repo's
  `projects/<project>/solutions/<userid>` convention.
* Updated README.md's "🤝 Contribution Guidelines" blockquote to
  link `contributor.md` instead of the now-consolidated `repo.md`,
  added a note distinguishing the "🧑‍🏫 Instructor Guidelines"
  education role from the Contributor/Maintainer/Admin GitHub
  roles, and added new "🧭 Maintainer Guidelines" and "🛠️ Admin
  Guidelines" sections linking `maintainer.md`/`admin.md`.
* Verified no remaining reference to the old `admin/repo.md`,
  `admin/member.md`, or `maintainer/pull_request.md` paths anywhere
  in live content, and that all three files' cross-links resolve.

Per this phase's prompt, these changes are committed here — push
to origin is left manual, per this repo's own git-hygiene norms.

## Model Serving Stack
[x] Status

* Add a session going over the Concept of `Model Serving Stack` -
* The content of the session is based on based on 
/.tmp/model_serving_stack.md
* The structure/template of the session can follow the format of
any other session, say `Spec Driven Development`.
* Insert the session in /README.md section AGENDA before the
session on `AI Local`

## check_pr/merge_pr Migration Reflected from ITDev
[x] Status

The companion repo `ITDev` (`../ITDev/`) asked to test its "review
count 1 except admin" branch protection change by migrating its
latest `check_pr`/`submit_pr`/`approve_pr`/`merge_pr` bazel targets
and `tools/scripts/repo_utils/` scripts here (this repo has no bazel
setup, so ported as plain `python3`-invoked scripts instead), run
the hermetic tests without touching a real PR, commit/push, then
live-test against a real PR. Reference `../ITDev`'s own
`prompt_history.md` for that session's full prompt sequence.

* Added `check_pr.py` (read-only mergeability report) and
  `merge_pr.py` (merges only after explicitly confirming every check
  finished with none failing and any required review is satisfied),
  extracting the shared auth/permission preflight and PR-status
  lookup into a new `_pr_utils.py`.
* `pr_tools_test.py`: 32 hermetic tests, `subprocess.run` fully
  mocked, no real git/gh call made.
* Live-tested against a real PR (#70): `merge_pr.py` initially
  hard-blocked on `reviewDecision=REVIEW_REQUIRED` even for an
  admin, despite this repo's branch protection being configured to
  exempt admins. Fixed to retry with `gh pr merge --admin`
  specifically in that case (discovered live: `gh` refuses to
  exercise a configured admin bypass unless `--admin` is passed
  explicitly) -- `CHANGES_REQUESTED` still hard-blocks regardless of
  permission, since that's an explicit human objection rather than
  "no review yet." Validated end-to-end via PR #71, which the fix
  itself was used to merge.

Both PRs merged live via `merge_pr.py`'s admin-bypass path.

## PR Tooling DRY + pr_merge_plugin Reflected from ITDev
[x] Status

The companion repo `ITDev` (`../ITDev/`) asked to DRY the PR tooling
(`check_pr`/`submit_pr`/`approve_pr`/`merge_pr` and the
`pr_submit_plugin` skill built on them) and propagate the same set
consistently across all sister repos — reference its
`specification_driven_development/prompt_history.md`'s "DRY PR
tooling..." entry for the full prompt. Mirrored the relevant parts
here (this repo has no bazel setup, so the four scripts already
existed as plain `python3`-invoked tools rather than bazel targets;
only `submit_pr.py`/`approve_pr.py` had landed before this session):

* Extracted the branch/clean-tree guard `pr_submit_plugin.py` had a
  near-copy of `submit_pr.py`'s own into `_pr_utils.py`'s
  `check_clean_branch`, fixing a latent bug along the way:
  `pr_submit_plugin.py` hardcoded `"main"` instead of respecting
  `--base`.
* Added `pr_merge_plugin`: a "wait for checks, then merge, then
  confirm" 3-step chain mirroring `pr_submit_plugin`'s pattern,
  deliberately never inspecting `reviewDecision` itself since
  `merge_pr.py` is the sole authority on whether an unsatisfied
  review blocks the merge or is admin-bypassable (see this repo's
  earlier `check_pr`/`merge_pr` migration entry for how that
  admin-bypass logic itself was discovered and validated live
  against this repo's own required-review-except-admin branch
  protection, PRs #70/#71).
* `pr_tools_test.py` grows to 35 tests; `pr_merge_plugin_test.py`
  adds 12 more. Both fully mocked -- no real git/gh call ever made.

Committed and pushed to `origin/fix/27aug26` here; per this phase's
scope decision, no new live PR was opened/merged for this specific
change (the admin-bypass path was already proven live by the prior
check_pr/merge_pr migration entry).

## Update Local
[x] Status

* Create a `Concept` session `AI Local` titled ai_local_model.md
based on the content in /.tmp/model_serving_stack.md 
* The content in /.tmp/model_serving_stack.md should go over all
the examples of local model serving, local models, and functionalities
provided by local model serving, etc. That is all `AI Local` related
content, such as agent harness (Aider, OpenCode) as well as serving 
(eg `Ollama`). No need to duplicate content that is already 
reflected  `Model Serving Stack`.
* Add this session in /README.md subsection AGENDA before the 
`Exercise` session on `AI Local`. 

## Bazel Bootstrap + PR Tooling Reflected from aim
[x] Status

The companion repo `ITDev` (`../ITDev/`) drove a cross-repo
consistency decision: `ai_workbench` should be bootstrapped with the
same minimal bazel scaffold `aim` has (`aim` also started with no
real service code, but was bootstrapped with a full bazel scaffold
anyway — see `aim`'s own bootstrap commit and its subsequent
DRY/check_pr/merge_pr/pr_merge_plugin history), rather than staying
bazel-free. This session mirrors `aim`'s *current* complete state
file-for-file (only the repo name changes, e.g.
`module(name = "aim")` → `module(name = "ai_workbench")`).

* Added the bazel scaffold: `.bazelversion`, `MODULE.bazel`,
  `WORKSPACE`, `.gitignore` additions (`bazel-*`, `external/` —
  `.venv/` was already ignored here), and a stub
  `.github/workflows/pr-validation.yaml` (a placeholder `echo` step)
  so `//:pr_check` (wrapping `act`) has something real-but-trivial
  to validate against.
* Ported `tools/scripts/build_utils/_container_checks.py` and
  `pr_check.py` verbatim from `aim`.
* **Replaced** the bazel-free PR tooling added in the two prior
  entries above ("check_pr/merge_pr Migration Reflected from ITDev"
  and "PR Tooling DRY + pr_merge_plugin Reflected from ITDev") with
  `aim`'s bazel-based equivalents: `_pr_utils.py`, `check_pr.py`,
  `submit_pr.py`, `approve_pr.py`, `merge_pr.py` (all now py_binary
  targets invoked via `bazel run //:<name> -- ...` instead of bare
  `python3 tools/scripts/repo_utils/<name>.py`), plus
  `pr_submit_plugin.py`/`pr_merge_plugin.py` (still run directly via
  `python3`, since they shell out to `bazel` themselves — a bazel
  target re-invoking bazel from its own sandbox is a known
  anti-pattern) and their hermetic test files.
  `pr_submit_plugin.py`'s build+test step mirrors `aim`'s deliberate
  2-command stub (`bazel build //...` / `bazel test //...` only, no
  container-test commands), matching `ai_workbench`'s identical
  "no real bazel-buildable code yet" situation rather than ITDev's
  fuller 4-command version.
* Added root `BUILD.bazel` (`pr_check`/`submit_pr`/`check_pr`/
  `approve_pr`/`merge_pr` py_binary targets) and `tools/BUILD.bazel`
  (`container_checks`/`pr_utils` py_library, `pr_submit_plugin_lib`/
  `pr_merge_plugin_lib` py_library with `deps = [":pr_utils"]`, and
  the three py_test targets), mirroring `aim` exactly.
* Updated `.claude/skills/pr_submit_plugin/skill.md` and
  `pr_merge_plugin/skill.md` from "runs directly via `python3` (this
  repo has no `.venv` or bazel)" wording to the bazel-based
  `aim`-style invocation (`bazel run //:submit_pr -- ...` etc.); the
  existing symlinks under `scripts/` needed no change. Updated
  stale `python3 tools/scripts/repo_utils/...` references in
  `README.md` to the bazel invocation style, and added the missing
  `pr_merge_plugin` row to its skills table.
* Validation: `bazel build //...` succeeded cleanly (first-ever
  bazel build in this repo — downloaded and registered the
  `rules_python` 3.12 toolchain). All 3 hermetic test targets
  (`pr_submit_plugin_test`, `pr_merge_plugin_test`, `pr_tools_test`)
  passed. All four `bazel run //:<name> -- --help` invocations
  printed usage cleanly. `bazel run //:pr_check` correctly invoked
  `act` against the stub workflow but hit a Docker/WSL
  credential-socket gap in this environment (`UtilAcceptVsock`
  accept4 failure) — an expected, pre-existing environment gap, not
  a bug in the ported code.

No real GitHub pull request was opened, approved, or merged during
this session — only `--help`/build/test invocations were run.

---

## Container-test stubs, consistency docs, slash-command wrappers
[x] Status

**Date:** 2026-08-30

**Prompt:** Same session as ITDev's own entry (see its
`specification_driven_development/prompt_history.md` for the full,
unparaphrased prompt text) -- container-test stub targets,
cross-repo consistency documentation, README PR-plugin sections,
three new `/pr_submit_plugin`/`/pr_approve_plugin`/`/pr_merge_plugin`
slash commands, and a branch-protection validation pass -- all done
directly in this repo by the same session (not delegated).

**What changed in this repo:**
- Added `tools/scripts/build_utils/container_tests_stub.py` and stub
  `//:container_tests`/`//:dockerfile_container_tests` `py_binary`
  targets (this repo has no real oci_image/Dockerfile targets yet),
  each printing a placeholder message and exiting 0, so
  `pr_submit_plugin.py`'s build+test chain now runs the same
  4-command sequence as ITDev instead of a 2-command stub.
  `pr_submit_plugin.py`/`pr_submit_plugin_test.py`/
  `pr_submit_plugin/skill.md` are now byte-identical to ITDev's
  copies (verified via `diff -q`); `pr_merge_plugin.py`/`skill.md`
  were left untouched.
- Added a generic "Sync note" to the module docstring of every
  PR-related script (`_pr_utils.py`, `submit_pr.py`, `check_pr.py`,
  `approve_pr.py`, `merge_pr.py`, `pr_submit_plugin.py`,
  `pr_merge_plugin.py`, `pr_check.py`), a "Cross-Repo Consistency"
  section to both skill.md files, and a matching comment above the
  PR-tools `BUILD.bazel` section, explaining this tooling is
  intentionally duplicated (not symlinked) across all 5 sister repos
  and must be kept in sync, with a `diff` spot-check example.
- Added/updated a "PR Workflow Plugins" README section covering
  `check_pr`/`submit_pr`/`approve_pr`/`merge_pr` with example usage.
- Fixed a pre-existing path bug in both skill.md files' "Run it via"
  example: it was missing the `.claude/` prefix
  (`skills/pr_submit_plugin/scripts/...` instead of
  `.claude/skills/pr_submit_plugin/scripts/...`), which would not
  have resolved from the repo root; repointed both to the verified
  `tools/scripts/repo_utils/<script>.py` path instead.
- Added three new slash commands, byte-identical across all 5 repos:
  `.claude/commands/pr_submit_plugin.md` (drafts a title/body from
  the branch's actual `git log`/`git diff` content, confirms with
  the user, then invokes `pr_submit_plugin.py` unchanged),
  `.claude/commands/pr_approve_plugin.md` (thin arg-parsing wrapper
  around `bazel run //:approve_pr`; relevant only to MAINTAIN/ADMIN,
  and fails on self-approval per `approve_pr.py`'s own guard), and
  `.claude/commands/pr_merge_plugin.md` (thin wrapper around
  `pr_merge_plugin.py`; relevant only when checks passed and either
  no review is required, the PR is `APPROVED`, or the caller is
  ADMIN with an exempting branch-protection admin bypass). Added
  matching "Or via `/pr_*_plugin`" cross-references to each
  underlying script's own docstring.
- Branch-protection validation (`gh api`) requested to confirm
  PR-only merges to `main`, `required_approving_review_count` 0 for
  private / 1 for public, and admin bypass everywhere -- findings
  logged centrally in ITDev's own prompt_history.md entry (this
  repo's specific result: see that entry for the private-vs-public,
  Free-plan-vs-Pro breakdown covering all 5 repos).
- Re-ran `bazel build //...` / `bazel test //...` (green) and
  `bazel run //:container_tests` / `//:dockerfile_container_tests`
  (both print the stub message and exit 0) in this repo.

---

---

## act --reuse: durable fix for the container-cleanup timeout
[x] Status

**Date:** 2026-08-30

**Prompt:** Follow-on to the entry above. Full details, including
the diagnostic trail (act upgrade, credential-helper removal, and
why the reboot fixed some symptoms but not this one), are in ITDev's
own `specification_driven_development/prompt_history.md` entry of
the same title -- not re-explained here. Summary: after a full
reboot didn't clear a recurring `act` post-job container-cleanup
timeout, the fix was `act`'s own `--reuse` flag, applied identically
to this repo per: "Yes: please reuse. Don't just use in ITDev but in
the spirit of consistency across all repos, let us duplicate this
across all sister repos," plus "Document at appropriate places the
periodic use of `docker container prune` to ensure we reclaim."

**What changed in this repo:**
- Added `--reuse` to the `act` invocation in
  `tools/scripts/build_utils/pr_check.py`, with the same inline
  comment ITDev's copy carries explaining why (a vsock-forwarded
  `docker.sock` on Docker Desktop's WSL2 backend can exceed `act`'s
  internal context deadline during post-success container removal,
  even though the job itself passed).
- Documented the accompanying `docker container prune` maintenance
  note in this repo's README, in its "PR Workflow Plugins" section.
- `bazel build //...` verified green after the change.

---
