# Concept & Exercise: Visual Generation with Claude Design

## 🎯 Objective

Learn to bypass the steep learning curve of traditional design software. 
You will use **Claude Design** to convert natural language ideas into 
functional UI prototypes and professional presentation decks, 
completely bypassing the blank canvas.

## 🧠 The Concept: What is Claude Design?

In previous sessions, we used AI to write code and process data. 
**Claude Design** is different—it is a visual engine powered by 
Claude Opus 4.7. Instead of returning text, it returns 
**rendered, interactive visual artifacts**. 
* **For Developers:** It builds functional frontend prototypes - 
buttons that click, sliders that move - that you can hand off 
to your codebase.
* **For Presenters:** It generates formatted, multi-slide pitch 
decks (HTML, PPTX, or Canva exports) based on a simple outline.

---

## 🏃‍♂️ Exercise 1: The Physics App Prototype (UI/UX)
```text
You have written the backend logic for a physics calculator, 
but you need a beautiful interface for students to use it.
```

### Step 1: The Prompt
Go to URL `claude.ai/design` and start a new project. 
Use the following prompt to generate an interactive mockup:
```text
Scenario: I need a mobile app UI prototype for a high school physics 
tool called 'Newton's Apple'. The main screen should have:
1. A clean, dark-mode aesthetic with neon green accents.
2. Three interactive input sliders for Mass (kg), Acceleration (m/s²), 
and Time (s).
3. A large, stylized 'Calculate Force' button.
4. A display area for the result that updates dynamically.

Make the layout modern, with plenty of whitespace, and ensure the UI 
feels tactile.
```

### Step 2: The Refinement
Claude Design allows for "Point-and-Edit" refinement. 
1. Click on the `Calculate Force` button in the generated preview.
2. Ask Claude to change it: 
```text
Make this button look like a glowing 3D pill.
```
3. Test the interactive elements—notice how the sliders actually work.

### Step 3: The Handoff
If you were building this app for real, you would click 
`Send to Claude Code`. This packages the HTML/CSS/JS so your local CLI 
can inject it directly into your Git repository.

---

## 👨‍💼 Exercise 2: The Pitch Deck (Presentations)
```text
You need to pitch 'Newton's Apple' to a panel of judges in 10 minutes.
```

### Step 1: Structural Prompting
Never ask an AI to "make a presentation" all at once. Build the skeleton first.
```text
I need a 5-slide pitch deck for my app 'Newton's Apple'. The audience is a 
high school science department. Outline the 5 slides first.
```

### Step 2: Visual Generation
Once Claude provides the outline, prompt it to build the deck:
```text
Perfect. Now build the full deck. Use a bold, high-contrast design: 
dark navy backgrounds, white text, and orange accents. Add a subtle 
fade transition between the slides. On the 'Market' slide, include an 
animated donut chart showing student engagement.
```

### Step 3: Exporting
The output is a browser-based, interactive presentation. 
To make it portable:
1. Click the **Export** menu.
2. Choose **Canva** (to add your own custom graphics) or 
**PPTX** (for Microsoft PowerPoint).

---

## 🔑 Key Takeaways
1. **Design Systems Matter:** `Claude Design` can ingest a brand document 
and apply those colors and fonts automatically to everything you build.
2. **Interactive over Static:** Always ask for interactive components 
(charts, sliders) rather than static images.
3. **The AI Assembly Line:** You use Claude Design for the *look*, 
and Claude Code for the *logic*.
