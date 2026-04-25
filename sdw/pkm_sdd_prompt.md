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

