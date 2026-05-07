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
