# Draft - Plan

## Drafting Process
Crafting a plan (plan.md) generally follows the **Intent → Plan → Iterate** 
process where Plan part follows the following sequence: 
* Context → 
* Features → 
* Data Schema → 
* Implementation Checklist → 
* Technical Blockers

## Intent
Social coordination application

## Plan
- Context
- Task
- Constraints
- Output format

### Context
Creating a lightweight web dashboard that automates the coordination 
of any recurring group meetup — a study group, a social gathering, a
community club — eliminating messy group chat threads and the overhead
of scheduling, venue selection, and logistics.

### Task
* Automate the weekly [Thursday] [evening]" social gathering coordination 
  among friends. Note that for another event, the [frequency],  
  [day], [region], and [time] is settable. For now, we will event 
  coordination on this "Thursady evening social gathering" event.
* The web site should offer the following features: 
  * Onboarding [Events]: 
    * [Event]: Existing members have privileges to create, read, 
      update, or unsubscribe) to [Event].
    * Note: 
      * The [Event] is auto subscribed to the [Member], 
        who created the event.
      * [Event] Deletion: If an [Event] is not subscribed by any member 
        for [DeleteAfterWeeks] weeks, it is removed from system.
  * Onboarding [Member]: 
    * Members have privilege to self onboard. 
    * Note: Region is auto-selected based on the nearest one to the
      member's city.
    * Members have privileges to subscribe to and unsubscribe from 
      list of [events].
  * Meet Up Scheduling:
    * Consensus Poll: Automatically initiated [ConsensusByDays] days
      before the next [Event] by sending a Consensus Poll email to 
      all subscribed members of the event. 
    * [Availability] and [Venue Preference] Selection: Members mark
      "free" (or "busy") for the coming event and choose a preferred
      venue type: "Library", "Coffee Shop", "Online/Video Call",
      "Study Room", "Restaurant", "Bar", or other.
    * Consensus to meet is realized when at least ConsensusThreshold 
      (default All) of the members mark themselves "available" to meet 
      for the upcoming meetup.
    * Meet up Location and Venue Selection: The City of the meetup is
      chosen based on rotation of the City of each attending member.
      The venue is chosen from options in the selected city that match
      the preference of the majority of attendees and are available for
      the meetup date.
    * Final Confirmation: An email with calendar invite with the final location 
      and meet-up time is sent to all "free" members. If the meet up is cancelled
      due to lack of consensus, that email is sent as well.
    * Cancellation: A member may cancel the meet up by sending 
      an email after full confirmation. The cancellation may lead to event 
      cancellation if ConsensusThreshold is not met. Nonetheless, the 
      cancellation is notified to other confirmed attendees receiving which 
      other attendees may also request cancelation via email. 

### Data Schema
* [Event] attributes:
  * Name: "[Group] Meetup" e.g. "Study Squad", "Chess Club" - required
  * Description: "Regular meetup for [group description]" - optional
  * Frequency: Week - DropDown [Week, BiWk, Month, Qtr, HalfYr, Yr]
  * WeekDay: Thu - DropDown [Mon, Tue, Wed, Thu, Fri, Sat, Sun] 
    When Frequency is Month (or Qtr, ...) we choose the first 
    occurrence of WeekDay on that Month (or Qtr, ...)
  * Time: Evening - DropDown [Morning, Noon, Evening]
  * ConsensusByDays: 4 - DropDown [1, 2, 4, 8, 16] 
    Unless consensus is realized within ConsensusByDays, the next event 
    is automatically cancelled and another scheduling round is initiated.
  * ConsensusThreshold: All - DropDown [All, ButOne, ...] - default All
  * Region: e.g. "SFO-SouthBay" - DropDown [configurable per deployment]
  * Subscribers: List of Subscribed Members for the event - default []
  * DeleteAfterWeeks: 2 - DropDown [1, 2, 4, 8, 16] - default 2
    for [DeleteAfterWeeks] weeks, it is garbage collected and removed.
* [Member] attributes:
  * Name: e.g. "Alex Kim"
  * Email: e.g. alex@email.com - used as unique identity
  * City: e.g. "Palo Alto" - DropDown [configurable per deployment]
  * Cell: "123-456-7890" - used for notifications
  * Events: [Events] - List of events selected from DropDown.
  * Availability: ["busy", "free"] - default "busy" 

### Implementation Checklist
- [ ] Step 1: UI Scaffold—Create a simple dashboard based on user login 
      with a "Meetup status" ie list of upcoming event meetups, meet up  
      status - confirmed members, final location, chosen restaurant, etc. 
- [ ] Step 2: Availability Logic—Enable users to toggle their status and 
      show a live "Count of Free Friends."
- [ ] Step 3: Neighborhood Logic—Implement a simple round-robin for the 
      City associated with the event.
- [ ] Step 4: Cancellation Toggle that marks a user "Busy" for that week
      and turns the dashboard red for that week.

### Constraints
- Authentication: Need a user login and onboarding.
- Database: Ensure the state (who is free) resets after each event 
  so old data doesn't clutter the dashboard.