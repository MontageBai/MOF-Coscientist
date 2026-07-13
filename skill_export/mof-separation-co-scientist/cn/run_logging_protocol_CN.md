# 运行日志和溯源记录中文说明

英文对应：

- `references/run_logging_protocol.md`
- `references/research_state_schema.md`
- `references/reproducibility_reporting_checklist.md`

## 能不能保存 LLM 每一步？

可以保存“可追溯的每一步”，包括：

- 输入了什么数据。
- 读了哪些文件。
- 用了哪些模块。
- 每个模块为什么用。
- 每个模块的关键判断摘要。
- 每个判断对应什么证据。
- 指标是什么口径。
- 最终输出了什么。
- 人工做了哪些选择或修改。
- 下一步研究状态是什么。

但不要把日志写成“完整内部思考过程”。更安全、也更适合论文的方法是写：

- reasoning summary：推理摘要。
- decision rationale：决策理由。
- traceable decision record：可追溯决策记录。

不要写：

- full chain of thought。
- complete internal thought process。

## 默认保存位置

如果有项目文件夹，建议保存到：

```text
logs/
```

推荐文件名：

```text
co_scientist_run_YYYYMMDD_HHMMSS.md
```

如果是连续研究，还可以维护一个最新状态文件：

```text
logs/research_state_latest.md
```

## 完整日志结构

```text
# Co-Scientist Run Log

## Run Metadata
- run_id:
- date_time:
- skill_name:
- skill_version_or_path:
- model_name_if_available:
- user_request:
- project_folder:
- output_files:

## Input Snapshot
- data_sources:
- files_read:
- tables_or_curves_provided:
- assumptions_from_user:
- missing_information:
- data_sufficiency_class:

## Module Execution Trace
| step | module_or_protocol | why_used | input_used | reasoning_summary | output_summary | evidence_refs | limitations |

## Evidence Log
| evidence_id | data_type | source_file_or_note | condition | observation | supports | evidence_level | limitation |

## Decision Log
| decision_id | decision | alternatives_considered | decision_rationale | evidence_refs | risk | overturning_result |

## Metric Log
| metric | value | unit | calculation_basis | window_or_condition | missing_raw_data | interpretation |

## Claim Trace
| claim | evidence_refs | evidence_level | metric_basis | safe_wording | unsupported_extension | reviewer_risk |

## Final Output Snapshot
<最终给用户或论文的输出>

## Human Intervention And Changes
- human_constraints:
- manual_data_cleaning:
- user_selected_alternative:
- expert_review_changes:

## Next-State Record
- current_best_configuration:
- weakest_evidence_link:
- next_experiment:
- result_that_would_change_the_plan:
```

## 最小日志结构

小任务可以简化，但至少保留：

```text
Run Metadata
Input Snapshot
Module Execution Trace
Decision Log
Final Output Snapshot
Next-State Record
```

如果涉及性能、论文 claim 或实验推荐，不能省略：

- evidence level。
- metric basis。
- missing data limitations。

## 为什么这个日志有发表价值

它能证明：

- AI 使用了什么输入。
- AI 按什么模块做了判断。
- 每个强结论对应哪个证据。
- 哪些地方只是 proxy，不是真实测量。
- 人工干预在哪里发生。
- 最终输出和后续研究状态可以复现。

## 论文里的安全表述

可以写：

```text
Each co-scientist run was documented using a structured run log that captured inputs, module use, evidence references, decision rationales, metric bases, final outputs, and human interventions.
```

中文意思：

每次共同科研助手运行都用结构化日志记录输入、模块使用、证据引用、决策理由、指标口径、最终输出和人工干预。

不要写：

```text
We recorded the complete hidden chain of thought of the model.
```

因为这既不准确，也不适合审稿。
