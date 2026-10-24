# 20 Before/After Prompt Examples
Categories: Code (1-7), Writing (8-13), Study (14-20). Pattern tags in [brackets].

## CODE
**1. Debugging** [role, task, format]
- Before: `fix my code`
- After: `You are a Python tutor for beginners. Find the bug in the function below, explain it in one sentence, give fixed code and 2 test cases. [paste code]`

**2. Explain code** [role, format]
- Before: `what does this do`
- After: `Explain this C function line by line to a first-year student. Use a table: line | what it does | why. [paste code]`

**3. Write a function** [task, constraints]
- Before: `write a sorting program`
- After: `Write a Python function that sorts a list of tuples by the second element, no built-in sort(). Include docstring and 3 asserts.`

**4. Error message** [context]
- Before: `i got an error`
- After: `Java 17, compiling with javac. Error: "cannot find symbol" on line 12 (code below). Explain the cause in 2 sentences and the fix. [paste]`

**5. Complexity** [chain-of-thought]
- Before: `is this fast`
- After: `Analyze time complexity of this function. Think step by step, count the loops, then state Big-O and one way to improve it.`

**6. Test cases** [few-shot]
- Before: `make tests`
- After: `Write pytest tests for is_prime(n). Style example: def test_two(): assert is_prime(2) is True. Give 6 tests including 0, 1, negatives, a large prime.`

**7. Learn an API safely** [ReAct]
- Before: `how to use pandas merge`
- After: `Using the official pandas docs, explain DataFrame.merge with one inner-join example. First list what you need to look up, then answer, and give the doc link. Flag anything you're unsure about.`

## WRITING
**8. Email** [role, format]
- Before: `write email to professor`
- After: `Write a polite 90-word email from a 2nd-year CSE student asking Prof. [Name] for a 15-minute meeting about my project. Include subject line and 2 time options.`

**9. Resume bullet** [few-shot]
- Before: `improve my resume`
- After: `Rewrite my bullet in action-verb + result style. Example: "Built a Flask app that cut booking time by 30%." My bullet: "I did a college website."  Give 3 versions, no invented numbers.`

**10. Summary** [format]
- Before: `summarize this`
- After: `Summarize the text below in 5 bullets of max 15 words, then one line "Key takeaway". [paste text, not confidential]`

**11. Proofreading** [constraints]
- Before: `fix grammar`
- After: `Proofread this paragraph. Keep my meaning and voice. Return corrected text, then a list of changes made. [paste]`

**12. Project README** [role, format]
- Before: `write readme`
- After: `You are a technical writer. Draft a README with sections: Overview, Features, Setup, Usage, License for a Python weather CLI. Use only the facts I give: [facts]. Mark unknowns as TODO.`

**13. LinkedIn post** [role, constraints]
- Before: `make a post about my workshop`
- After: `Write a 100-word LinkedIn post about attending a prompt-engineering workshop. Friendly, no hashtags spam (max 3), no exaggerated claims.`

## STUDY
**14. Concept explain** [role, format]
- Before: `explain recursion`
- After: `Explain recursion to a first-year student using a real-life analogy, then a 5-line Python factorial example, then 3 common mistakes.`

**15. Quiz me** [task, format]
- Before: `give questions on DBMS`
- After: `Create 5 MCQs on normalization (1NF-3NF), difficulty easy-medium. Give 4 options each; put answers and one-line explanations at the end.`

**16. Study plan** [context, constraints]
- Before: `make study plan`
- After: `Make a 7-day plan for my Data Structures exam. I have 2 hours on weekdays, 4 on weekend. Topics: arrays, linked lists, stacks, queues, trees. Table: day | topic | task | self-test.`

**17. Math reasoning** [chain-of-thought]
- Before: `solve this`
- After: `Solve step by step, showing each rule used, then verify by substituting back: [problem].`

**18. Compare concepts** [format]
- Before: `stack vs queue`
- After: `Compare stack and queue in a table (order, operations, use cases, Python implementation). End with a 2-line memory trick.`

**19. Research with sources** [ReAct]
- Before: `tell me about transformers`
- After: `Find 3 reliable sources on the transformer architecture. For each give title, author, year, link and one-sentence relevance. Say "not found" rather than guessing. I will verify the links.`

**20. Feedback on my answer** [role, constraints]
- Before: `is my answer correct`
- After: `You are an examiner. Grade my answer out of 5 using this rubric: correctness, clarity, example. Don't rewrite it; give 2 specific improvements. Question: [..] My answer: [..]`
