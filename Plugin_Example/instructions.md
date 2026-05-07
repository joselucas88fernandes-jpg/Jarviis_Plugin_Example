# JARVIS PLUGIN STANDARD (ABI v1)

This document defines the official structure, rules, and execution model for all plugins compatible with the Jarvis Kernel.

Any plugin that does not follow these rules will be rejected by the loader.

---

# 1. PURPOSE

A Jarvis plugin is a modular execution unit that extends the capabilities of the Jarvis Kernel.

Plugins MUST be:
- deterministic
- isolated in logic
- contract-based
- execution-safe

Plugins are NOT allowed to:
- control the kernel directly
- execute system-level operations without restrictions
- bypass the execution contract
- modify other plugins

---

# 2. REQUIRED STRUCTURE
plugin_name/
│
├── manifest.json
├── main.py
├── instructions.md (optional but recommended)
├── requirements.txt (optional)
└── assets/ (optional folder for static files)


---

# 3. MANDATORY FILES

## 3.1 manifest.json (REQUIRED)

Defines the plugin identity and routing rules.

Must include:

- name (string)
- version (string)
- min_kernel_version (string)
- entry (must be "main.py")
- triggers (list of strings)
- priority (integer)
- type (core | tool | brain | memory | utility)
- description (string)

---

## 3.2 main.py (REQUIRED)

Must expose exactly one function:

```python
def execute(skill_input) -> SkillOutput

Rules:
Must not execute code outside the function scope
Must not access system resources directly
Must return ONLY SkillOutput object
Must not return raw strings or unstructured data
Must be stateless unless memory is explicitly provided
4. EXECUTION CONTRACT
Input Object (SkillInput)

Each plugin receives:

user_input: str
context: dict
memory: dict
Output Object (SkillOutput)

Each plugin MUST return:

success: bool
response: str
actions: list[str]
metadata: dict
5. SECURITY RULES (STRICT)

Plugins MUST NOT:

access filesystem outside their folder
perform network calls without explicit design permission
execute subprocess/system commands
import unsafe or dynamic execution libraries (eval, exec, etc.)
modify kernel state directly

Any violation results in plugin rejection.

6. ROUTING BEHAVIOR

Plugins are triggered via:

exact match triggers
partial match triggers
semantic overlap scoring

The router selects the highest scoring plugin.

7. PRIORITY SYSTEM

Each plugin has a priority field:

Higher priority overrides weak matches
Priority is NOT a guarantee of execution
Only affects scoring weight
8. OPTIONAL COMPONENTS
8.1 instructions.md (this file)

Used by future AI Main Nodes to understand:

intent of plugin
usage conditions
constraints
behavior expectations
8.2 requirements.txt

Defines Python dependencies.

Installed in isolated environment per plugin (future sandbox model).

8.3 assets/

Static resources only:

images
models
config files

No executable code allowed inside assets.

9. VERSIONING RULES

Plugins MUST follow semantic versioning:

MAJOR.MINOR.PATCH

MAJOR: breaking changes
MINOR: new features
PATCH: fixes
10. COMPATIBILITY

Plugins must define:

min_kernel_version

The kernel will reject incompatible plugins.

11. ERROR HANDLING

Plugins MUST never crash the kernel.

All exceptions MUST be caught internally and returned as:

SkillOutput.error("message")

12. DESIGN PHILOSOPHY

The Jarvis system is built on:

modular intelligence
isolated execution
predictable contracts
safe extensibility

Plugins are NOT autonomous systems.

Plugins are controlled execution units.

13. FINAL RULE

If a plugin violates this standard, it is considered invalid and will be rejected by the loader without execution.

Every plugin MUST follow this directory structure:

