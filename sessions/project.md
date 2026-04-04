## Project Preliminary Draft

### Plan Creation
Crafting a plan - plan.md - generally follows the **Intent → Plan → Iterate** framework where the Plan steps follows the **Objective → Features → Data Schema → Implementation Checklist → Technical Blockers** sequence.

### Intent
Social coordination application

### Plan

#### Objective
To create a lightweight web dashboard that automates the coordination of a weekly Thursday social gathering for local friends, eliminating messy group chat threads.

#### Features
- Weekly Consensus Poll: Automatically resets every Sunday. Friends mark "Free & Local" for the coming Thursday.
- Mood Selector: Once consensus is reached, users vote: "Food & Drinks" or "Just Food."
- Location Recommendation: Based on neighborhood rotation (Palo Alto, Menlo Park, Mountain View, Cupertino) and mood choice.
- Final Confirmation Note: Generates a clean text/WhatsApp snippet with the final location and meet-up time.
- One-Click Cancellation: A "Cancel This Week" button that notifies everyone if the core group can no longer make it.

#### Data Schema
- Users: Name, Neighborhood, Availability (Boolean).
- Events: Date, Status (Planned/Confirmed/Cancelled), Mood (Enum: Drinks/Food).
- Locations: Name, Neighborhood, Category (Bar/Restaurant).

#### Implementation Checklist
- [ ] Step 1: UI Scaffold—Create a simple dashboard with a "This Thursday" status card.
- [ ] Step 2: Availability Logic—Enable users to toggle their status and show a live "Count of Free Friends."
- [ ] Step 3: Neighborhood Logic—Implement a simple round-robin or manual selector for the four neighborhoods.
- [ ] Step 4: Notification Generator—Create a button that copies a summary to the clipboard (e.g., "We are meeting! Venue: [Place], Time: 7:00 PM").
- [ ] Step 5: Cancellation Toggle—Add a global "Cancel" flag that turns the dashboard red for that week.

#### Technical Blockers
- Authentication: Do we need a login, or can we just use a "Select Your Name" dropdown for simplicity?
- Database: Ensure the state (who is free) resets every week so old data doesn't clutter the dashboard.