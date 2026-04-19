Reflection Tree Design

Overview

This reflection tree is designed as a deterministic, structured system that guides users through a daily self-reflection process.
The goal is to translate psychological concepts into a clear decision tree, ensuring consistency, interpretability, and repeatability without relying on any AI at runtime.

The system progresses through three interconnected psychological axes, forming a coherent reflective journey rather than isolated questions.

---

Axis 1: Agency (Locus of Control)

The first stage focuses on how users interpret events in their day.

Users are guided to reflect on:

- Whether outcomes were shaped by their actions
- Or influenced primarily by external circumstances

This axis is grounded in:

- Locus of Control theory (Rotter)
- Growth Mindset (Dweck)

Design intent:
To help users recognize moments of agency without assigning blame.
Even small choices are surfaced to build awareness of control.

---

Axis 2: Contribution (Orientation)

The second stage shifts focus from control → contribution.

Users reflect on:

- What they contributed (effort, help, initiative)
- Versus what they expected (recognition, support)

This axis is inspired by:

- Organizational Citizenship Behavior
- Psychological Entitlement theory

Design intent:
To make contribution visible without moralizing.
The tree encourages users to observe their behavior rather than judge it.

---

Axis 3: Perspective (Radius)

The final stage expands the user’s perspective beyond themselves.

Users reflect on:

- Whether their thinking was self-focused
- Or included others (team, colleagues, customers)

This axis draws from:

- Self-transcendence (Maslow)
- Perspective-taking (Batson)

Design intent:
To widen awareness and reduce self-centered interpretation of events, enabling more meaningful reflection.

---

Flow Design

The tree follows a strictly deterministic structure:

- Each axis builds sequentially (Axis 1 → Axis 2 → Axis 3)
- Each question has fixed answer options (no free text)
- Decision nodes route based on selected answers
- Reflections are predefined and consistent
- Same inputs always produce the same outputs

This ensures:

- Predictability
- Auditability
- Consistency across sessions

---

Design Decisions

1. Fixed Options

All questions use predefined options to eliminate ambiguity and ensure deterministic behavior.

2. Structured Branching

Multiple decision nodes allow nuanced paths while maintaining clarity and traceability.

3. Reflection over Evaluation

Reflections are written as neutral observations, not judgments or scores.

4. Progressive Depth

Each axis builds deeper insight:

- Agency → Contribution → Perspective

---

Trade-offs

- Avoided free-text input to maintain determinism
- Limited number of options per question to balance depth and usability
- Prioritized clarity over excessive branching complexity

---

Future Improvements

With more time, the system could be enhanced by:

- Adding more nuanced branching paths
- Expanding reflection personalization using accumulated signals
- Designing a lightweight UI for better user experience

---

Conclusion

This reflection tree demonstrates how abstract psychological concepts can be translated into a structured, navigable decision system.

By combining deterministic logic with thoughtful question design, the system enables meaningful self-reflection that is:

- Consistent
- Explainable
- Scalable

without relying on AI during execution.
