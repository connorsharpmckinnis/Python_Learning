Project 2: Build a Stateful Event Processor
One-Sentence Brief

Build a long-running Python program that processes a stream of events and maintains internal state over time.

Not a script that runs and exits. A process that lives.

Concept

You are building an Event Processor.

It receives events (you can simulate these) and updates internal state based on rules.

Examples of event domains (pick one or invent your own):

Task queue system (enqueue, complete, fail)

Bank account simulator (deposit, withdraw, freeze)

Rate limiter (requests allowed/denied over time window)

Room booking engine (reserve, cancel, check availability)

Inventory tracker (add stock, sell stock, backorder)

The domain doesn’t matter. The thinking does.

Core Requirements (Simpler, but Real)
1. It Must Run Continuously

The program should:

Start up

Accept events in a loop (from CLI input, file input, or simulated generator)

Update internal state

Print state changes or summaries

Shut down cleanly

No one-shot execution.

2. State Must Be Explicit

You must define:

What the state is

Where it lives

How it changes

No scattered globals. No mystery mutation.

If I open your code, I should see something like:

“Here is the state object. Here are the only places it changes.”

3. At Least One Invariant

An invariant is a rule that must always be true.

Examples:

Account balance can’t go below zero

Inventory cannot be negative

A room cannot be double-booked

Completed tasks can’t be completed again

You must:

Enforce it in code

Demonstrate it with at least one failing case

4. Error Handling (Basic, Not Bulletproof)

You should:

Gracefully handle invalid events

Reject events that break invariants

Keep running after bad input

You do NOT need:

Industrial-grade validation

Advanced schema systems

Retry frameworks

This is about reasoning, not fortification.

Architecture Expectations

Keep it clean but not baroque.

Suggested structure:

event_processor/
│
├─ main.py
├─ processor.py
├─ models.py
├─ events.py
└─ README.md


The key idea:

models.py → defines state structures

events.py → defines event types

processor.py → contains logic that applies events to state

main.py → handles input loop

But you’re allowed to deviate if you have a reason.

Stretch Goals (Optional, But Interesting)

Pick one if you’re feeling bold:

Add persistence (save state to JSON periodically)

Add timestamps and time-based logic

Add simple logging instead of print

Add a replay mode that replays a list of events

Only do this if the core is clean.

Deliverables

When you bring it back, include:

The code

A short README explaining:

What domain you chose

What your state model looks like

What invariant you enforced

A reflection:

Where state management got tricky

What surprised you

What would break if this had concurrency

That last one is important. You won’t implement concurrency yet. But I want you to think about it.

What I’ll Evaluate

I care about:

Is state centralized?

Is mutation controlled?

Does the invariant actually hold?

Does your structure scale mentally?

I do not care if the CLI is fancy.