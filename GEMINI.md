# Agent Development Guidelines (Gemini)

This gemini-style document describes rules, workflow, and suggestions for developing an agent from files you will provide. Save this file in the project root as `agent-guidelines.gmi`.

## 1. Ground rules (must be respected)

* **Explicit permission required for all operations.** The agent must request confirmation before *any* action: analysis, proposing patches, generating files, suggesting refactors, or offering improvements.

* **No deletion of files or code without explicit permission.** If any file or code must be removed, record the request in writing and wait for explicit confirmation.

* **No Git operations by the agent or assistant.** The agent must not commit, push, pull, or modify repository history. All source-control operations are the user's responsibility.

* **User-owned files.** You (the user) will provide files and datasets. The agent may read, analyze, and propose changes, but must never remove originals.

* **Local edits only.** Any automatic edits must be created as separate patch files or suggested diffs (e.g. `.patch` or `.diff`) so originals are preserved.

## 2. How you'll hand me files

When you upload files, please include:

* File path relative to project root.
* Brief description of purpose and responsibilities of each file.
* Any runtime or build commands needed to run/test code.

Example (paste with your upload):

```
/path/to/file.py  — main agent logic
/path/to/config.yaml — runtime config
npm run test        — runs unit tests
```

## 3. Development workflow (safe-by-default)

1. **Inspect**: Agent reads files and builds a file map (no file modification).
2. **Report**: Agent lists syntax issues, missing dependencies, and suggested improvements as a non-destructive report.
3. **Patch**: For any change, the agent outputs a patch file or suggested diff and a human-readable explanation.
4. **Verify**: Run static checks and tests locally (instructions provided by you). Agent reports results.
5. **Iterate**: Repeat until you're satisfied. Agent never pushes changes to git or deletes files.

## 4. Patch format (required)

When proposing changes, the agent should output one of the following formats, never apply changes directly:

* Unified diff (`.diff` / `git diff --no-index` style)
* A new file named `<original>.suggested` with the proposed full contents
* A `.patch` file with metadata and instructions

Each patch must include a short how-to-apply note and tests or commands to validate the patch.

## 5. Automatic features to suggest / implement

These are recommended enhancements to the development process and to the agent itself:

* **Code autocompletion**: Provide inline completion suggestions for functions and classes. Prefer snippets that include types and docstrings.
* **Syntax fixer**: Produce suggested fixes for syntax errors with a clear diff and explanation.
* **Static analysis**: Run linters (e.g., `ruff`, `flake8`, `eslint`) and summarize findings with severity levels.
* **Type checking**: Suggest `mypy` (Python) or TypeScript `tsc` checks and include a minimal `mypy.ini` or `tsconfig.json` suggestion.
* **Unit tests scaffold**: Generate minimal unit tests for uncovered modules with clear instructions how to run them.
* **Local sandbox runner**: Provide commands to run the agent in a sandbox environment (container or venv) without altering user files.
* **Interactive mode**: Provide a read-only interactive walkthrough of code paths so the user can inspect how the agent reasons about behavior.

## 6. Rules for fixing syntax or obvious bugs

* The agent **may** propose fixes for syntax errors, undefined names, and trivial refactors, but must output fixes as diffs or `.suggested` files.
* Include a short explanation for each fix: why it was wrong, why the fix works, and any edge-cases.
* If a fix could change runtime behavior or data, label it `BREAKING` and require explicit approval.

## 7. Security & privacy cautions

* The agent will not transmit sensitive files or secrets. If it detects environment secrets (e.g., keys in `.env`), it reports their paths and suggests secure handling.
* The agent should suggest rotating credentials and moving secrets to a secrets manager when discovered.

## 8. Suggested tools & example commands

These are suggestions — install and run locally as needed.

```
# Python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ruff check .
mypy --strict src/
pytest

# Node
npm ci
npm run lint
npm test
```

## 9. Templates (diff + suggested file example)

**Unified diff example**:

```
*** a/src/agent.py
--- b/src/agent.py
@@ -10,7 +10,7 @@
-def run(agent, config):
-    print('running')
+def run_agent(agent, config):
+    print('running agent')
```

**Suggested full-file example**: create `src/agent.py.suggested` containing the full corrected file; include tests in `tests/test_agent.py`.

## 10. Agent responsibilities checklist (for each iteration)

* [ ] Read-only file map generated
* [ ] List of syntax errors / exceptions encountered
* [ ] Suggested diffs / `.suggested` files created
* [ ] Test commands to run, and expected output
* [ ] Security issues reported (if any)

## 11. Best-practice suggestions I will offer while developing

### Additional Best Practices

* **Permission-first workflow** — always pause and ask before analyzing, reading, suggesting, or generating anything.

* **Immutable originals** — never modify or override original files; always use `.suggested` or diff outputs.

* **Small, logical increments** — propose improvements in small sections to keep reviews simple and safe.

* **Traceability** — always explain the motivation, reasoning, and expected impact of any suggestion.

* **Agent transparency** — whenever the agent proposes something, it must show intermediate reasoning steps at a high level (but never reveal confidential or internal chain-of-thought).

* **Configuration isolation** — if changes require configs, propose separate config files instead of editing existing ones.

* **Fail-safe mode** — if uncertainty exists about a file or command, the agent defaults to asking clarifying questions.

* **Reproducible steps** — provide repeatable validation commands so the user can verify each suggestion.

* **Non-destructive refactoring** — suggest structural improvements without altering behavior unless explicitly approved.

* **Testing-first approach** — encourage adding minimal tests before proposing larger code changes.

* Auto-complete & inline documentation for all exported functions.

* Add small, focused unit tests for each public function before large refactors.

* Prefer small diffs — one logical change per patch.

* Include type hints and docstrings to improve maintainability.

* Where appropriate, suggest CI checks as *suggestions only* (never configure or enable CI or commit changes).

## 12. How to request changes from the agent

When asking the agent to act, include the following in your prompt:

* Exact file path(s) to operate on.
* The kind of change you want (read-only analysis, propose patch, generate tests, or refactor suggestion).
* Any runtime constraints (python version, node version, frameworks used).

Example: `Analyze /src/handler.py for syntax errors and propose patches; do not apply anything.`

## 13. Frequently asked questions (short)

*Q: Can the agent commit changes?*
A: No. Agent cannot perform git operations.

*Q: Can the agent delete or overwrite files?*
A: Not without explicit permission; instead it will output suggested patch files.

*Q: Will the agent fix syntax errors automatically?*
A: It will propose fixes as diffs or suggested files, with explanations. Minor formatting suggestions may be provided inline.

---

If you want, I can now create a starter checklist and a sample `src/agent.py.suggested` based on one of your files. Upload the files (or paste them) and tell me which operation you want first.
