---
name: explain-code
description: Explains implemented code and design flow across the app. Use when a user asks how something works, why a pattern was chosen, or wants an end-to-end flow traced through the actual code.
---

Explain the system from the implemented code, not from memory or specs:

1. Identify the concrete entry points, files, and runtime path relevant to the question
2. Read the actual implementation before answering — do NOT explain from memory, assumptions, or specification text alone
3. Trace the flow across modules in execution order, including important data transformations, boundaries, and side effects
4. When asked why a pattern was chosen, ground the explanation in the code structure and nearby usage; clearly label any inference that is not explicitly documented
5. Cite the specific files and symbols that support the explanation
6. If the code does not support a complete answer, say what is missing and stop short of guessing
7. Summarize as:
   - **Entry points**: where the flow starts
   - **Flow**: the end-to-end path through the code
   - **Key design choices**: patterns visible in the implementation and why they appear to be used
   - **Evidence**: files, symbols, and code paths inspected
