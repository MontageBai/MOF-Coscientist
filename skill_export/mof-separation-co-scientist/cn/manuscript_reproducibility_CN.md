# 论文写作、复现和评价中文说明

英文对应：

- `references/manuscript_methods_si_template.md`
- `references/reproducibility_reporting_checklist.md`
- `references/co_scientist_evaluation_protocol.md`
- `references/forward_test_protocol.md`

## 论文中的核心定位

推荐表达：

```text
We developed a co-scientist workflow to assist MOF adsorptive separation studies by converting feed composition, adsorbent descriptors, adsorption isotherms, and breakthrough data into functional bed-layer assignments and experimentally testable serial-bed configuration hypotheses.
```

中文理解：

我们开发的是一个共同科研助手工作流，它把进料组成、吸附剂描述符、等温线和穿透数据，转化成功能化床层分配和可实验检验的串联床配置假设。

## 必须避免的论文表述

不要写：

- LLM autonomously discovered the optimal process。
- LLM replaces physical simulation。
- The recommended configuration is globally optimal。
- The process is industrially feasible。

除非真的有闭环自动实验、物理模拟替代证据、全局优化或工艺验证。

## Methods 可以怎么组织

### 1. Co-Scientist Workflow

写七模块：

```text
mixture role analysis
functional bed decomposition
function-compatible sorbent screening
experimental calibration
configuration hypothesis generation
feed/objective perturbation analysis
process validation planning
```

### 2. Mixture Role Analysis

说明如何从进料表确定：

- target recovery mode。
- dominant impurity class。
- specification-limiting impurity。

### 3. Functional Bed Decomposition

说明先分功能再选材料。典型功能：

- 前置分离或出口顺序调控。
- 限制杂质后置精制。
- 保护层。
- 容量支撑层。

### 4. Sorbent Screening

说明材料按功能筛选，不做全局 MOF 排名。描述符包括：

- PLD, LCD, PSD。
- surface area, pore volume。
- OMS。
- functional groups。
- polarity/hydrophobicity。
- stability and availability。

### 5. Experimental Calibration

说明穿透和等温线数据用于校准功能，而不只是验证：

- target breakthrough。
- first impurity breakthrough。
- clean collection window。
- curve broadening。
- dynamic uptake proxy。

### 6. Configuration Hypothesis Generation

说明 LLM 用作配置假设生成器，不是数值优化器。输出包括：

- material set。
- bed order。
- mass ratio。
- collection window。
- expected limiting impurity。
- failure mode。

### 7. Process Validation

说明有希望的配置还要检查：

- regeneration route。
- working-capacity proxy。
- cycle stability。
- shaping/pressure-drop risk。
- material practicality。
- adsorbent cost proxy。

## SI 表格建议

可以做这些 Supporting Information 表：

| 表 | 内容 |
|---|---|
| Table S1 | Feed role table |
| Table S2 | Function-compatible candidate map |
| Table S3 | Evidence-level assignment |
| Table S4 | Configuration hypotheses |
| Table S5 | Iterative decision log |
| Table S6 | Controls and uncertainty |
| Table S7 | Regeneration, scale-up, and TEA proxy |
| Table S8 | Evaluation rubric |

## 审稿人常见质疑和回答方向

### 质疑 1：LLM 是否替代物理模拟？

回答方向：

LLM 不替代物理模拟或穿透实验。它只是结构化推理层，用来组织证据、分配床层功能、生成可测试的配置假设。

### 质疑 2：推荐配置是不是没有全局优化？

回答方向：

把 wording 从 optimized configuration 改成 configuration hypothesis。只有比例/顺序比较或真实优化器支持时，才说优化。

### 质疑 3：指标是不是 proxy？

回答方向：

明确标注 productivity、recovery、purity 的计算口径。如果只有归一化穿透曲线，就写 curve-integral proxy 或 time-window proxy。

## 复现记录

每次 co-scientist run 至少记录：

```text
Co-Scientist Record
- skill_name:
- skill_path_or_repository:
- skill_version_or_date:
- model_name:
- model_provider:
- run_date:
- temperature_or_sampling_setting:
- system_or_skill_prompt_reference:
- additional user prompt:
```

如果模型设置不知道，就明确写 limitation。

## 数据来源记录

```text
Data Provenance
- feed_data_source:
- descriptor_data_source:
- simulation_source:
- isotherm_source:
- breakthrough_source:
- regeneration_cycle_source:
- cost_or_scaleup_source:
- preprocessing_steps:
- excluded_data:
- known_uncertainties:
```

## 人工干预记录

人工判断不是缺点，隐藏才是风险。需要记录：

- 人工假设。
- 手动数据清洗。
- 人工在备选方案中选择。
- 实验可行性限制。
- 专家审阅后的修改。

## Forward Test 是什么

Forward test 是在新上下文中测试 skill 是否真的可迁移，而不是靠记住答案。

测试时只能给 agent-facing prompt，不给 evaluator rubric。

评分维度：

| 维度 | 看什么 |
|---|---|
| data conversion | 是否把原始数据转成表 |
| target role | 是否说明 target recovery mode |
| functional decomposition | 是否先分功能 |
| candidate mapping | 是否按功能映射材料 |
| calibration | 是否用穿透数据更新角色 |
| configuration hypothesis | 是否给出顺序、比例、窗口、风险 |
| metric discipline | 是否标指标口径 |
| claim discipline | 是否避免过度声称 |

通过要求：

- 总分至少 18/24。
- 没有维度为 0。
- configuration hypothesis、metric discipline、claim discipline 都至少 2 分。

## 论文 AI-use statement 中文理解

可以写成英文：

```text
An LLM-based co-scientist workflow was used to structure the adsorption-separation problem, assign functional bed roles, map candidate MOFs to functions, and generate testable serial-bed configuration hypotheses. The LLM output was treated as decision support and was not used as a substitute for physical simulation, adsorption measurements, or breakthrough experiments.
```

中文意思：

我们用 LLM 共同科研助手来结构化吸附分离问题、分配功能床层、按功能映射候选 MOF、生成可实验检验的串联床配置假设。LLM 输出被当作决策支持，而不是替代物理模拟、吸附测量或穿透实验。
