# 2-Hour Workshop Plan: "Prompt Like an Engineer"
**Audience:** 1st/2nd-year CSE students (20-40) | **Needs:** laptop/phone, free AI tool (ChatGPT/Gemini/Claude), projector | **Facilitator:** M. Saravanan

## Learning outcomes
By the end, students can (1) write prompts using Role-Task-Context-Format, (2) apply few-shot and step-by-step prompting, (3) verify AI output, (4) follow privacy and citation rules.

## Agenda
| Time | Min | Activity | Output |
|---|---|---|---|
| 0:00 | 10 | Warm-up: "Bad prompt battle" - everyone sends `help me with coding`, compare answers | Realize vague = random |
| 0:10 | 15 | Mini-lecture: prompt anatomy (infographic + slides 1-4) | Notes |
| 0:25 | 20 | **Exercise 1 - Rewrite**: improve 3 weak prompts (code/writing/study) using the checklist | 3 rewrites |
| 0:45 | 10 | Debrief: share best rewrites, score with checklist | Class scoreboard |
| 0:55 | 5 | Break | |
| 1:00 | 15 | Patterns demo: few-shot, chain-of-thought, ReAct (slide 5) | Live demo |
| 1:15 | 20 | **Exercise 2 - Pattern lab** (pairs): classify student feedback with few-shot; debug a loop with step-by-step | 2 prompts + outputs |
| 1:35 | 15 | **Exercise 3 - Hallucination hunt**: find errors in a provided AI answer (fake citation, wrong code, outdated fact) | Error list |
| 1:50 | 10 | Ethics + wrap-up: privacy, verification, credit; save prompts to library | Library entry |
| | | Quiz (5 min inside wrap-up or homework) | Score |

## Exercise sheets
**Ex 1 weak prompts:** (a) `fix my code` (b) `write email` (c) `explain DBMS`. Task: rewrite each; score with checklist; run both versions.
**Ex 2:** Few-shot: give 3 labeled feedback lines (Positive/Negative), classify 5 new ones. Step-by-step: ask AI to trace `for i in range(3): print(i*2)` line by line, then you verify by running it.
**Ex 3:** Facilitator provides an AI answer containing a non-existent library function, an invented paper, and an outdated version claim. Students verify each with official docs/search.

## Discussion questions
1. When did a longer prompt make things worse?
2. How do you know the AI is wrong when you're a beginner?
3. What should never go into a prompt?
4. Is using AI for homework cheating? Where is the line in our college policy?
5. How would you cite AI assistance?

## Answer guidance (for facilitator)
1. Extra irrelevant detail dilutes the task; keep only what changes the output.
2. Run code, check docs, ask for sources then open them, compare two tools.
3. Passwords, API keys, ID numbers, personal chats, others' private data, confidential/unpublished work.
4. Follow the institution's policy: learning aid vs submitting unattributed output; disclose usage.
5. Name tool, date, and purpose (e.g. "Used Claude on 24 Oct 2026 to brainstorm examples; I verified and edited them").

## Assessment
Checklist scores from Ex 1 + quiz (12 Qs) + library entry quality.

## Risk plan
No internet -> offline printed examples. Tool limit reached -> pair up / switch tool. Mixed skill levels -> stretch task: add ReAct-style source checking.
