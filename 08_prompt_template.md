# Reusable Prompt Template (RTCFC-V)

```
ROLE:        You are a [role] helping [audience/level].
TASK:        [One clear action verb + goal].
CONTEXT:     [Course/language/version/background/constraints].
INPUT:       [Paste text/code/data. No private information.]
FORMAT:      [Structure, length, tone, e.g. table with 3 columns, max 120 words].
EXAMPLES:    [Optional: 1-3 input -> output pairs].
CONSTRAINTS: [What to avoid; what to assume].
REASONING:   [Optional: "Think step by step, then give the final answer."]
VERIFY:      [Ask: list assumptions and what I should double-check.]
```

## Filled example (code)
```
ROLE: You are a patient Python tutor for first-year CSE students.
TASK: Find and explain the bug in my function.
CONTEXT: Python 3.11, beginner level, we have only learned loops and lists.
INPUT: def avg(xs): total=0; for x in xs: total+=x; return total/len(xs)  # crashes on []
FORMAT: 1) Bug in one sentence 2) Fixed code 3) Two test cases.
CONSTRAINTS: No external libraries.
VERIFY: Tell me what I should test myself.
```
