# 七模块 Co-Scientist 工作流中文说明

英文对应：

- `references/seven_module_framework.md`
- `references/module_1_mixture_role_analyzer.md`
- `references/module_2_functional_decomposer.md`
- `references/module_3_sorbent_screening_engine.md`
- `references/module_4_experimental_calibration_loop.md`
- `references/module_5_configuration_optimizer.md`
- `references/module_6_feed_objective_perturbation.md`
- `references/module_7_process_validation_engine.md`

## 总流程

```text
混合物角色分析
-> 床层功能分解
-> 按功能筛选 MOF
-> 用实验校准功能模型
-> 生成串联床配置假设
-> 分析进料/目标扰动
-> 做工艺验证展望
```

这条线的重点是：不要从“材料排名”开始，而要从“这个分离任务需要哪些床层功能”开始。

## Module 1: Mixture Role Analyzer

中文名：混合物角色分析器。

它回答的问题：

- 目标分子是谁？
- 目标是从出口直接收集，还是先吸附再脱附？
- 哪类杂质最可能影响目标收集窗口？
- 哪个杂质可能是 specification-limiting impurity，即最容易限制产品规格的杂质？

输出应该包括：

```text
Mixture Role Analysis
- Target:
- Feed condition:
- Target recovery mode:
- Collection/desorption implication:
- Dominant impurity class:
- Specification-limiting impurity:
- Main separation challenge:
- Missing information:
```

常见错误：

- 只看浓度最高的杂质，忽略高亲和力低浓度杂质。
- 没有说明 target recovery mode。
- 把平衡吸附选择性直接等同于动态穿透顺序。

## Module 2: Functional Decomposer

中文名：功能分解器。

它回答的问题：

- 床层 A 负责什么功能？
- 床层 B 负责什么功能？
- 有没有必要加 guard layer 或 capacity-support layer？
- 每个功能用什么实验可以证伪？

典型功能包括：

- front separation layer：前置分离层。
- sequence-shaping layer：出口顺序调控层。
- downstream refining layer：后置精制层或出口端精制层。
- guard layer：保护层。
- capacity-support layer：容量支撑层。

注意：不要用含糊的“抛光层”。中文里建议写“后置精制层”或“出口端精制层”。

## Module 3: Sorbent Screening Engine

中文名：吸附剂筛选引擎。

它不是输出一个全局 MOF 排名，也不是一开始就筛到只剩很少材料。更合理的是先输出“每个功能对应的候选材料空间”，把可能可行的都列出来，并标注为什么可能可行、证据等级、风险和下一步验证。之后如果实验预算有限，再在人类选择基础上收敛成 shortlist。

筛选逻辑：

1. 先看硬条件：孔径可达性、扩散可行性、化学稳定性、实验可获得性。
2. 再看软偏好：容量、选择性、动力学、再生难度、成本。
3. 每个材料只在具体功能内排序，不跨功能做“总冠军”。

输出表：

```text
Function-Compatible Candidate Map
| function | required descriptors | candidate MOFs | evidence type | per-function priority | risk |

Candidate Material Space
| function | candidate | inclusion_reason | matching_features | evidence_type | evidence_level | uncertainty | human_selection_note |
```

## Module 4: Experimental Calibration Loop

中文名：实验校准循环。

它回答的问题：

- 穿透曲线说明材料真的完成了预期功能吗？
- first impurity 是谁？
- clean collection window 有多大？
- 失败原因是容量不够、选择性弱、动力学慢、共吸附、目标被过度保留，还是床层顺序不对？

需要从曲线中提取：

- `t5`, `t50`, `t95`
- 目标分子穿透时间
- 第一个杂质穿透时间
- 干净收集窗口
- 曲线展宽或拖尾
- 动态吸附量代理指标

关键理念：实验不是单纯验证，而是更新功能分配。

## Module 5: Configuration Hypothesis Generator

中文名：配置假设生成器。

它给出：

- 材料组合
- 床层顺序
- 质量比
- 总床层质量
- 收集窗口
- 预计限制杂质
- 最大风险
- 什么结果会推翻这个假设

如果实验预算只有一次，要给一个明确的 primary configuration，不要同时给一堆保守备选。

输出：

```text
Configuration Hypothesis
- Objective priority:
- Experiment budget:
- Primary configuration:
- Bed order:
- Mass ratio:
- Total mass:
- Collection/desorption window:
- Expected limiting impurity:
- Productivity expectation:
- Recovery expectation:
- Purity expectation:
- Metric calculation basis:
- Evidence level:
- Single biggest risk:
- Result that would overturn the hypothesis:
```

写作边界：除非有真实优化器或系统 ratio/sequence 比较，否则不要说 optimized result，应该说 configuration hypothesis。

## Module 6: Feed And Objective Perturbation Engine

中文名：进料和目标扰动引擎。

当进料组成或优化目标变化时使用。

它回答：

- 进料变化后，主导杂质变了吗？
- 限制杂质变了吗？
- 材料组合是否还稳定？
- 质量比应该往哪个方向迁移？
- 床层顺序是否仍然合理？

比例迁移规则：

- bulk impurity 负担增加：前置层质量可能要增加。
- downstream limiting impurity 提前泄漏：后置精制层质量可能要增加。
- 目标分子被强吸附导致生产率下降：强吸附层质量可能要减少。

## Module 7: Process Validation Engine

中文名：工艺验证引擎。

它不是证明已经工业可行，而是把有希望的实验配置转化为工艺验证计划。

必须检查：

- 再生方式
- 工作容量
- 循环稳定性
- 材料合成和成本
- 成型、颗粒、压降
- 水汽或污染物耐受性
- TEA proxy，即技术经济代理指标

没有这些证据时，只能说 process-validation outlook，不能说 industrial feasibility。

## 证据等级速查

| 等级 | 含义 |
|---|---|
| Level 0 | 只有描述符或一般化学判断 |
| Level 1 | 有单组分等温线支持 |
| Level 2 | 有单床穿透实验支持 |
| Level 3 | 有多组分或串联床穿透支持 |
| Level 4 | 有比例或顺序比较支持 |
| Level 5 | 有循环、再生、工艺验证支持 |
