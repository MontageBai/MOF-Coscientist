# Forward-Test Protocol

Use this file when validating whether the MOF separation co-scientist works in a fresh context. The goal is to test transferable reasoning, not whether an agent can recover an answer from leaked prior discussion.

## Purpose

Forward-testing checks whether the skill can:

- convert raw adsorption-separation data into usable structured inputs;
- assign target recovery mode and bed-layer functions;
- map MOFs to functions rather than global rankings;
- generate one actionable configuration under an experimental budget;
- label evidence levels and metric calculation bases;
- avoid unsupported manuscript claims.

## Test Setup

Use a fresh context whenever possible. Provide:

- the skill path;
- the test fixture prompt;
- raw data or summarized raw observations;
- the expected output format, but not the evaluator rubric or hidden reasoning notes.

Do not provide:

- the intended final configuration;
- previous human interpretation;
- the evaluator's scoring notes;
- suspected weaknesses in the skill.

For fixtures that contain an evaluator section, extract only the agent-facing prompt with:

```text
python scripts/extract_agent_prompt.py <fixture.md>
```

## Standard Forward-Test Prompt

```text
Use the MOF separation co-scientist skill at:
<path-to-mof-tandem-bed-co-scientist-skill>

Analyze the provided MOF adsorption-separation case as a publication-grade co-scientist. Convert the input data into usable tables, run the relevant modules, and give one primary next experiment if the budget is one experiment. Your output must include target recovery mode, functional bed decomposition, function-compatible candidate map, experimental calibration status, configuration hypothesis, metric calculation basis, evidence level, biggest risk, and publication-safe claim boundary.
```

## Evaluation Dimensions

Score each dimension from 0 to 3:

| dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| data conversion | raw data ignored | partial table | usable feed/evidence tables | tables plus missing-data flags |
| target role | missing/wrong | vague target role | target recovery mode stated | target mode plus collection implication |
| functional decomposition | material-first | vague layers | clear bed functions | functions plus falsification criteria |
| candidate mapping | global ranking | partial mapping | per-function candidates | candidates plus evidence/risk |
| calibration | ignores breakthrough | describes data only | updates roles | updates roles plus evidence level |
| configuration hypothesis | many options/no ratio | one option but incomplete | order and ratio | order, ratio, window, risk, overturning result |
| metric discipline | unsupported purity/recovery | vague proxies | metric basis stated | basis plus missing raw-data limits |
| claim discipline | overclaims | weak caveats | safe claims | safe claims plus reviewer risk |

Passing threshold:
- Minimum total score: 18/24.
- No dimension should score 0.
- `configuration hypothesis`, `metric discipline`, and `claim discipline` must each score at least 2.

## Failure Flags

Flag the test as failed if the output:

- recommends a global best MOF without function mapping;
- claims a global optimum from limited evidence;
- reports recovery or purity without metric basis;
- ignores the one-experiment budget;
- fails to state target recovery mode;
- treats LLM reasoning as replacing physical simulation or experiments.

## Test Report Format

```text
Forward-Test Report
- Test fixture:
- Skill path:
- Date:
- Overall score:
- Pass/fail:

Dimension Scores
| dimension | score | evidence from output | issue |

Major Strengths
-

Failure Flags
-

Recommended Skill Fixes
-
```

## Deterministic Scoring Gate

After a forward-test report is written, run:

```text
python scripts/score_forward_test.py <forward-test-report.md>
```

The script checks that all eight rubric dimensions are scored, the total score reaches the passing threshold, no dimension is zero, and critical dimensions pass the minimum gate.

For skill-package integrity, run:

```text
python scripts/validate_skill_structure.py
```

## Paper-Facing Use

Forward-test results can support a manuscript or SI statement such as:

```text
We evaluated the co-scientist workflow using staged case prompts in which the final experimental interpretation was withheld. Outputs were scored for data conversion, target-role assignment, functional decomposition, candidate mapping, experimental calibration, configuration hypothesis quality, metric discipline, and claim discipline.
```

Do not claim autonomous discovery unless the forward test is coupled to actual closed-loop experimental execution.
