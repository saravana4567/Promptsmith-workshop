# Research Report: Using AI to Design a Hands-On Prompt Engineering Workshop
**Author:** M. Saravanan | **Audience:** 1st/2nd-year CSE students | **Length:** 2-hour workshop

## 1. Research question
How can AI help design a hands-on workshop that teaches prompt engineering to junior students?

## 2. Method
| Step | Tool | Purpose |
|---|---|---|
| Pattern research | Perplexity, Claude | Cited overviews of each pattern |
| Paper search | Elicit | Find/confirm primary papers |
| Source reading | NotebookLM | Upload official guides, ask grounded questions |
| Drafting | ChatGPT, Claude, Gemini | Plan, examples, quiz drafts |
| Infographic / slides | Leonardo.ai / Gamma (optional polish) | Visual assets |
| Storage | Notion or GitHub | Prompt library |

> Student note: replace/confirm the tool list with the tools you actually used. Log each in the Prompt Library.

## 3. Prompt patterns (summary)
| Pattern | What it is | When to use | Tiny example |
|---|---|---|---|
| Role | Tell the model who/what perspective to take | Tone, expertise level | "You are a patient C tutor for first-year students." |
| Task | One clear, specific instruction | Always | "Explain why this loop never ends." |
| Format | Specify output structure | Tables, JSON, steps, word limits | "Answer in 3 bullets, max 15 words each." |
| Few-shot | Give 2-5 input/output examples | Classification, style matching | Show 3 labeled examples, then the new one |
| Chain-of-thought | Ask for step-by-step reasoning | Math, logic, debugging | "Work step by step, then give the final answer." |
| ReAct | Alternate Reason -> Act (tool/search) -> Observe | Tasks needing lookups/tools | "Think, search, observe, then answer; cite sources." |

Key ideas: clarity and specificity beat clever wording; examples steer format and style; reasoning prompts help on multi-step problems but can still produce confident wrong reasoning; tool-using patterns need verification of what the tool returned.

## 4. Sources (verify each link before submission)
**Official guides**
1. OpenAI - Prompt engineering guide: https://platform.openai.com/docs/guides/prompt-engineering
2. Google - Gemini API prompting strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies
3. Anthropic - Prompt engineering overview: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview

**Papers (confirm in Elicit; note year and venue)**
4. Brown et al. (2020), *Language Models are Few-Shot Learners*, arXiv:2005.14165
5. Wei et al. (2022), *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*, arXiv:2201.11903
6. Kojima et al. (2022), *Large Language Models are Zero-Shot Reasoners*, arXiv:2205.11916
7. Yao et al. (2022), *ReAct: Synergizing Reasoning and Acting in Language Models*, arXiv:2210.03629

Source reliability rating: official guides = high for practice, but vendor-specific and change often; papers = high for concepts, results may not transfer to newer models.

## 5. How AI helped design the workshop
- Drafted the agenda and timings, then humans trimmed to fit 120 minutes.
- Generated 20 before/after examples; each was checked by running it.
- Produced quiz drafts; answer keys were checked against official guides.
- Built the prompt-anatomy visual and slides from the same outline.
- Limits: AI invented citations, over-confident timings, and generic examples in drafts -> see Verification Report.

## 6. Ethics (taught in the workshop)
1. **Never paste private data** (ID numbers, passwords, API keys, marks, personal chats, unpublished work).
2. **Verify before trusting** - run code, cross-check facts, check dates/versions.
3. **Credit sources** - cite guides/papers; disclose AI assistance per your institution's policy.
4. **Academic integrity** - use AI to learn, not to submit unattributed work.
5. **Safety** - don't act on medical/legal/security advice without a qualified source.

## 7. Conclusion
AI is most useful as a drafting and brainstorming partner for workshop design; the human must own scoping, testing, and verification. Teaching prompt patterns together with a verification habit gives juniors the highest value.
