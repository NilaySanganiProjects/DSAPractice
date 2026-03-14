# AXIOM Onboarding — Calibration Questionnaire

Before AXIOM generates your Week 1 Day 1 mission, answer these three questions honestly. Fill in your answers below each question, then read the **What Happens Next** section.

---

## Question 1 — Current Level

**What is your current coding level, honestly?**

Choose one:
- [ ] Beginner who knows syntax (can write loops, functions, basic OOP)
- [ ] Can solve easy LeetCode problems (arrays, strings, basic iteration)
- [ ] Struggle at mediums (know the patterns exist but can't apply them quickly)
- [ ] Comfortable at mediums (can solve most mediums given 30–45 minutes)

**Your answer:**
> (Fill in here)

---

## Question 2 — Target

**What is your target?**

Choose one or more:
- [ ] Product company (mid-tier, solid DSA expected but not LeetCode-hard)
- [ ] FAANG / top-tier (hard LC problems, system design, behavioral)
- [ ] Startup (practical engineering, may not grill on LC but expect strong problem-solving)
- [ ] Just want to be a strong engineer (no specific job target, want depth)

**Your answer:**
> (Fill in here)

---

## Question 3 — Time Commitment

**How many hours per day can you give this realistically?**

Be honest — 1 focused hour beats 3 distracted hours.

Choose one:
- [ ] 30 minutes (minimum viable — one problem per day)
- [ ] 1 hour (one problem + reading the system context)
- [ ] 2 hours (one problem + project work)
- [ ] 3+ hours (full sessions — problem + project + mock interview)

**Your answer:**
> (Fill in here)

---

## What Happens Next

Once you fill in your answers:

1. AXIOM reads your calibration and assigns you a **starting point** in the curriculum.
2. Your **Week 1 Day 1 mission** is loaded from the appropriate week folder.
3. All subsequent sessions follow the structure in [`AXIOM.md`](./AXIOM.md).

### Starting Point Guide

| Level | Starting Week |
|-------|--------------|
| Beginner who knows syntax | Phase 1, Week 1 — start with array fundamentals |
| Can solve easy LC | Phase 1, Week 1 — move faster, skip the very basics |
| Struggle at mediums | Phase 1, Week 1 — focus on pattern recognition |
| Comfortable at mediums | Phase 1, Week 2 — skip warm-up, go straight to pattern drilling |

---

## Week 1 Day 1 Mission (Phase 1, Week 1)

> **Copy your answers above and proceed to [`phase-1/week-1/README.md`](./phase-1/week-1/README.md) for your first mission.**

### Context: Why Arrays First?

Before you write a single line of code, here is the real-world context:

**Instagram's feed deduplication** uses a two-pointer technique on a sorted array of post IDs to remove duplicates in O(n) instead of O(n²). The same pattern is in your Day 3 problem. You are not solving a LeetCode problem — you are learning the move that Instagram's backend engineers make.

**Google's search suggestion ranking** uses frequency maps (hashmaps) to count and rank query prefixes. That is your Day 2 problem.

Every problem this week is mapped to a real system. Check the `real-world-context` section in each problem file.

---

## Session Template

At the start of every session, open [`templates/SESSION_TEMPLATE.md`](./templates/SESSION_TEMPLATE.md) and fill it in. This keeps AXIOM's feedback engine calibrated.
