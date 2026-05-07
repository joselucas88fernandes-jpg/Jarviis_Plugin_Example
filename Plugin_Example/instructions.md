JARVIS PLUGIN STANDARD (ABI v1.1)
⚠️ IMPORTANT RULE

This document defines the official execution contract for all Jarvis plugins.

Any plugin that violates this specification:

will be rejected by the loader
will NOT be executed
will NOT be eligible for marketplace verification

Plugins are not applications.
Plugins are controlled execution modules inside the Jarvis Kernel.

1. PURPOSE

A Jarvis plugin is a modular capability unit that extends the Kernel safely and predictably.

Plugins exist to:

process user input
execute constrained logic
return structured outputs
optionally interact with tools (if explicitly allowed)

Plugins MUST NOT behave as independent systems.

2. CORE DESIGN PRINCIPLES

Every plugin MUST follow:

🔒 Isolation-first execution
📦 Stateless design (unless memory is provided)
⚙️ Deterministic behavior (same input → same output)
🧱 Contract-based communication only
🚫 No uncontrolled side effects
3. REQUIRED DIRECTORY STRUCTURE

Every plugin MUST follow exactly this structure:

plugin_name/
│
├── manifest.json          # REQUIRED
├── main.py                # REQUIRED (entry point)
├── instructions.md        # RECOMMENDED (human + AI usage guide)
├── requirements.txt       # OPTIONAL
└── assets/                # OPTIONAL (static files only)
4. MANDATORY FILES
4.1 manifest.json (REQUIRED)

Defines plugin identity, behavior, and routing rules.

Required fields:
{
  "name": "string",
  "version": "MAJOR.MINOR.PATCH",
  "min_kernel_version": "string",
  "entry": "main.py",
  "type": "core | tool | brain | memory | utility",
  "priority": "integer",
  "triggers": ["string"],
  "description": "string"
}
Rules:
entry MUST be "main.py"
triggers MUST be a non-empty list of strings
priority affects routing score only (not execution guarantee)
type defines plugin classification for future marketplace filtering
4.2 main.py (REQUIRED)

Must expose EXACTLY this function:

def execute(skill_input) -> SkillOutput:
Execution Rules:
MUST NOT execute code outside execute()
MUST NOT use global state unless explicitly designed
MUST return ONLY SkillOutput
MUST NOT return raw strings, dicts, or objects outside contract
5. EXECUTION CONTRACT
Input (SkillInput)

Each plugin receives:

user_input: str
context: dict
memory: dict
Output (SkillOutput)

Must strictly follow:

success: bool
response: str
actions: list[str]
metadata: dict
Rules:
response is the only user-facing output
actions are optional system signals (e.g. ["save_memory"])
metadata is for debugging, logs, tracing
6. SECURITY MODEL (STRICT)

Plugins MUST NOT:

❌ access files outside plugin directory
❌ use eval, exec, or dynamic code execution
❌ spawn subprocesses or system commands
❌ perform network calls unless explicitly allowed in future ABI extension
❌ modify kernel state directly
❌ import unauthorized system-level modules

Any violation = automatic rejection by loader

7. ROUTING SYSTEM

Plugins are selected via scoring engine:

Priority order:

Exact trigger match (highest priority)
Partial match (substring)
Word overlap scoring

Kernel selects the highest scoring plugin only

8. PRIORITY SYSTEM
priority: integer

Rules:

Higher value increases likelihood of selection
Does NOT guarantee execution
Only affects routing score weighting
9. OPTIONAL COMPONENTS
9.1 instructions.md (RECOMMENDED)

Used by:

AI Main Nodes
plugin developers
future auto-documentation systems

Should describe:

plugin behavior
usage examples
constraints
expected outputs
9.2 requirements.txt (OPTIONAL)

Defines Python dependencies.

⚠️ Future rule:
Each plugin will be installed in an isolated environment (sandbox-ready architecture).

9.3 assets/ (OPTIONAL)

Static resources only:

Allowed:

images
configs
models
templates

Not allowed:

executable code
scripts
hidden logic
10. VERSIONING RULES

Plugins MUST follow:

MAJOR.MINOR.PATCH
MAJOR → breaking changes
MINOR → new features
PATCH → bug fixes
11. COMPATIBILITY

Each plugin MUST define:

min_kernel_version

Kernel will reject incompatible plugins automatically.

12. ERROR HANDLING

Plugins MUST NEVER crash the kernel.

All exceptions MUST be handled internally:

SkillOutput.error("message")
13. DESIGN PHILOSOPHY

Jarvis is built on:

modular intelligence
controlled execution
predictable contracts
safe extensibility
marketplace scalability

Plugins are NOT autonomous agents.

They are controlled functional extensions of a deterministic kernel.

14. FINAL RULE

If a plugin violates this standard:

It is INVALID and will be rejected without execution.
