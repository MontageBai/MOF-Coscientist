# MOF Tandem-Bed Co-Scientist v2.0 中文读本

v2.0 新增动态容量匹配公式与可执行脚本：先按同进料多组分单床穿透曲线计算前床服务基线、后床残余负荷及质量比，再用材料证据和串联实验修正建议。公式结果是“容量匹配基线”，不是全局最优比例。缺少新进料匹配曲线时，使用实验锚点迁移，并单独标注不确定性。

公式定义见 `../references/tandem_capacity_matching.md`，输入格式见 `../references/tandem_manifest_schema.md`，迁移方法见 `../references/feed_transfer_protocol.md`。执行方式：`python scripts/tandem_capacity_analysis.py MANIFEST.json OUTPUT.json`。

这个目录是给中文阅读用的对照材料。英文 `SKILL.md` 和 `references/` 仍然是正式 skill 文件；这些中文文件只帮助理解，不作为最终发表或正式执行文本。

## 这个 Skill 的一句话目标

它不是让 AI 直接说“哪个 MOF 最好”，而是让 AI 像一个吸附分离方向的共同科研助手一样，把原料组成、MOF 描述符、吸附等温线、穿透实验和实验约束整理成可检验的串联床配置假设。

核心原则：

```text
先分配功能，再选择材料。
把 LLM 当成配置假设生成器，不当成数值优化器。
把实验当成功能模型的校准，而不是一次性验证。
```

## 你应该怎么读

建议顺序：

1. 先读本文件，了解整体思想。
2. 读 `six_module_framework_CN.md`，知道六个模块分别干什么。
3. 如果要整理 Excel、曲线和实验数据，读 `data_metric_evidence_CN.md`。
4. 如果只有任务和进料、还没到找材料阶段，读 `early_stage_structural_target_CN.md`。
5. 如果已经准备从结构目标进入材料推荐，读 `material_recommendation_input_CN.md`。
6. 如果要写论文、SI、答审稿人，读 `manuscript_reproducibility_CN.md`。
7. 如果要判断能不能说“优化”或“显著”，读 `experimental_controls_CN.md`。
8. 如果要保存每一步日志、追溯输入和输出，读 `run_logging_protocol_CN.md`。

## 英文文件对应关系

| 中文文件 | 对应英文文件 | 用途 |
|---|---|---|
| `README_CN.md` | `SKILL.md` | 总体理解 |
| `six_module_framework_CN.md` | `six_module_framework.md`, `module_*.md` | 六模块工作流 |
| `data_metric_evidence_CN.md` | `data_input_contract.md`, `metric_requirements.md`, `research_state_schema.md` | 数据、指标、证据等级 |
| `early_stage_structural_target_CN.md` | `early_stage_structural_target_protocol.md` | 早期任务识别、结构目标定义 |
| `material_recommendation_input_CN.md` | `material_recommendation_input_protocol.md`, `module_3_sorbent_screening_engine.md` | 分子尺寸、数据库路径、PLD/LCD/GLD 匹配 |
| `experimental_controls_CN.md` | `experimental_controls_uncertainty.md` | 控制实验、不确定性和结论阈值 |
| `manuscript_reproducibility_CN.md` | `manuscript_methods_si_template.md`, `reproducibility_reporting_checklist.md`, `co_scientist_evaluation_protocol.md` | 论文写作、复现、评价 |
| `run_logging_protocol_CN.md` | `run_logging_protocol.md`, `research_state_schema.md`, `reproducibility_reporting_checklist.md` | 运行日志、溯源、输出快照 |

## 最重要的写作边界

可以说：

- “configuration hypothesis”：配置假设。
- “function-compatible candidates”：功能匹配候选材料。
- “experimentally calibrated function”：经实验校准的功能。
- “curve-integral proxy”：曲线积分代理指标。

没有充分证据时不要说：

- “global optimum”：全局最优。
- “best MOF”：最佳 MOF。
- “statistically significant”：统计显著。
- “LLM replaces simulation/experiment”：LLM 替代模拟或实验。

## Skill 的标准输出长什么样

默认应该输出：

```text
Research State
- Target:
- Feed condition:
- Target recovery mode:
- Current objective:
- Current best hypothesis:
- Evidence level:
- Weakest evidence link:

Module Outputs
1. Mixture role analysis:
2. Functional decomposition:
3. Sorbent screening map:
4. Experimental calibration status:
5. Configuration hypothesis:
6. Feed/objective perturbation response:

Metric Requirements
- Material screening metrics:
- Experimental calibration metrics:
- Configuration metrics:
- Productivity/recovery/purity calculation basis:
- Missing data that block stronger claims:

Next Experiment
- Experiment budget strategy:
- Primary configuration:
- Hypothesis tested:
- Measurements:
- Success criterion:
- Failure interpretation:

Publication Value
- Central claim enabled:
- Required controls:
- Figure/table plan:
- Reviewer risk:
```

## 我以后使用这个 Skill 时会遵守的规则

- 先把原始数据转成结构化表，再推理。
- 先说分离功能，再说材料。
- 每个强结论都标证据等级。
- 每个纯度、回收率、生产率都标计算口径。
- 只有一组实验时，说“单次实验观察”或“配置假设测试”，不说统计显著。
