# Install Guide

This package contains the current `mof-separation-co-scientist` Codex skill and separated private case files.

## Contents

```text
mof-separation-co-scientist_export_20260713/
├── skill_export/
│   └── mof-separation-co-scientist/
├── private_cases/
│   └── mof-separation-co-scientist_private_cases/
├── INSTALL.md
└── CHANGELOG_BRIEF.md
```

## Install The Active Skill

Copy only the active skill folder into Codex skills:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/mof-separation-co-scientist
cp -R skill_export/mof-separation-co-scientist ~/.codex/skills/
```

Expected path:

```text
~/.codex/skills/mof-separation-co-scientist/SKILL.md
```

## Validate

```bash
cd ~/.codex/skills/mof-separation-co-scientist
python3 scripts/validate_skill_structure.py .
```

Expected output:

```text
mof-separation-co-scientist structure ok
```

If PyYAML is missing:

```bash
python3 -m pip install pyyaml
```

## Private Cases

The folder below is intentionally outside the active skill:

```text
private_cases/mof-separation-co-scientist_private_cases/
```

Do not copy these files into the active skill if you want to preserve held-out or blind-test behavior. Use them only as external validation fixtures or project notes.

## Recommended First Prompt

```text
Use the mof-separation-co-scientist skill.
First inspect the active skill structure and validate it.
Then analyze the provided MOF separation task using the skill workflow.
Do not use private case files unless I explicitly provide them as case evidence.
```
