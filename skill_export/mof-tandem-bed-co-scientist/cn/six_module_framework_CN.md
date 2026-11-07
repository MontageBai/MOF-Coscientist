# 六模块 Co-Scientist 工作流中文说明

英文对应：

- `references/six_module_framework.md`
- `references/module_1_mixture_role_analyzer.md`
- `references/module_2_functional_decomposer.md`
- `references/module_3_sorbent_screening_engine.md`
- `references/module_4_experimental_calibration_loop.md`
- `references/module_5_configuration_optimizer.md`
- `references/module_6_feed_objective_perturbation.md`

## 总流程

```text
混合物角色分析
-> 床层功能分解
-> 按功能筛选 MOF
-> 用实验校准功能模型
-> 生成串联床配置假设
-> 分析进料/目标扰动
-> 回到下一轮实验校准
```

这不是材料排行榜，而是“任务—功能—材料—实验—配置”的闭环。

## Module 1：混合物角色分析

确定目标回收模式、主要杂质负荷、限制产品窗口的杂质，以及尺寸、亲和力和竞争吸附等核心困难。

## Module 2：床层功能分解

在指定材料之前，先定义前置分离、序列调控、后置精制、保护或容量支撑等功能，并为每个功能写明证伪条件。

## Module 3：功能匹配型 MOF 筛选

根据分子尺寸、PLD/LCD/GLD、孔道、OMS、化学环境、模拟和实验依据建立每个功能的候选空间。先做硬过滤，再在功能内部排序，不做全局“最佳 MOF”排名。

## Module 4：实验校准

从等温线和穿透曲线提取 `t5/t50/t95`、穿透顺序、收集窗口、展宽、拖尾和动态容量代理。实验结果用于修正材料功能、限制杂质和失败模式。

## Module 5：配置假设生成

在实验约束下提出材料组合、床层顺序、质量比和收集窗口，并说明指标口径、最大风险和推翻假设的结果。没有系统比较时使用“配置假设”，不使用“全局最优”。

## Module 6：进料与目标扰动

当进料组成或研究目标变化时，重新判断限制杂质、功能分配、材料组合、比例迁移和顺序稳定性，并把建议送回下一轮实验校准。

## 三个反馈回路

1. 配置假设 -> 下一实验 -> 实验校准。
2. 实验校准 -> 修正床层功能和候选角色。
3. 新进料或新目标 -> 重新进行混合物角色分析。

## 证据等级

| 等级 | 含义 |
|---|---|
| Level 0 | 描述符或一般化学假设 |
| Level 1 | 单组分等温线支持 |
| Level 2 | 单床穿透支持 |
| Level 3 | 多组分或串联床穿透支持 |
| Level 4 | 比例、顺序或重复配置比较支持 |
