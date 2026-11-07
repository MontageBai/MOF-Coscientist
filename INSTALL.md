# Install MOF Co-Scientist v2.0

The v2.0 skill is `mof-tandem-bed-co-scientist`. The July export remains available under its original name for reproducing earlier work. Install only the skill folder; examples, tests, and historical evaluation cases are not part of the installed skill.

## Windows / PowerShell

Run from the repository root:

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex\skills' }
$skillTarget = Join-Path $skillRoot 'mof-tandem-bed-co-scientist'
if (Test-Path -LiteralPath $skillTarget) { throw 'The target already exists. Back it up or choose another destination before copying.' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skill_export\mof-tandem-bed-co-scientist' -Destination $skillTarget -Recurse
```

## macOS / Linux

Run from the repository root:

```bash
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
skill_target="$skill_root/mof-tandem-bed-co-scientist"
if [ -e "$skill_target" ]; then
  echo 'The target already exists. Back it up or choose another destination before copying.'
else
  mkdir -p "$skill_root"
  cp -R skill_export/mof-tandem-bed-co-scientist "$skill_target"
fi
```

Start a new chat if the newly installed skill has not appeared. Invoke it with `$mof-tandem-bed-co-scientist`.

## Dependencies and verification

Python 3.10+ is required for the scripts. CSV calculations use the standard library. The structure checker requires PyYAML; Excel input additionally requires openpyxl. Install both with:

```bash
python -m pip install -r skill_export/mof-tandem-bed-co-scientist/requirements.txt
python skill_export/mof-tandem-bed-co-scientist/scripts/validate_skill_structure.py skill_export/mof-tandem-bed-co-scientist
python -m unittest discover -s tests -v
```

After installation, the same structure checker can be run from inside the installed skill with `python scripts/validate_skill_structure.py .`.

## Run a calculation

From the repository root:

```bash
python skill_export/mof-tandem-bed-co-scientist/scripts/tandem_capacity_analysis.py examples/tandem_synthetic/manifest.json
```

To save JSON output, add a positional output path:

```bash
python skill_export/mof-tandem-bed-co-scientist/scripts/tandem_capacity_analysis.py examples/tandem_synthetic/manifest.json result.json
```

The example is synthetic. Replace it with your own feed-matched multicomponent curves and documented mass/flow/coordinate units before interpreting a physical mass ratio. Curve paths resolve relative to the input manifest. Input fields are defined in [`tandem_manifest_schema.md`](skill_export/mof-tandem-bed-co-scientist/references/tandem_manifest_schema.md).

## Migration from the July skill

- Use the new name for tandem-bed calculations and transfer reasoning.
- The old `mof-separation-co-scientist` folder remains unchanged; existing historical records continue to refer to that version.
- Do not copy `private_cases/` into either skill. These are evaluation materials, and the directory name does not make them private on GitHub.
- This repository supplies skill instructions and local calculation helpers. No API key is needed to download the package or run its CSV example.
