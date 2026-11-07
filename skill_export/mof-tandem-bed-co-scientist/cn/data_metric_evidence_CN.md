# 数据、指标和证据等级中文说明

英文对应：

- `references/data_input_contract.md`
- `references/metric_requirements.md`
- `references/research_state_schema.md`

## 为什么要先做数据合同

这个 skill 的一个关键要求是：不要从原始笔记直接跳到 MOF 推荐。必须先把数据转成结构化输入，标明缺什么、能支持什么结论、不能支持什么结论。

## Project Block

```text
Project
- project_id:
- target_molecule:
- target_recovery_mode:
- objective_priority:
- experiment_budget:
- total_bed_mass_constraint:
- allowed_materials:
```

重点：

- `target_recovery_mode` 必须明确：breakthrough product、adsorbed product 或 desorption product。
- `objective_priority` 要说明是生产率优先、回收率优先、纯度优先还是鲁棒性优先。

## Feed Composition Block

```text
| component | partial_pressure_kPa | mole_fraction | role | note |
```

最低要求：

- 组分名。
- 分压或摩尔分数。
- 目标分子。
- 总压和温度，如果有。

如果有分压，优先用分压，因为它更接近吸附平衡和进料负担。

## Material Descriptor Block

```text
| material | PLD | LCD | PSD | surface_area | pore_volume | OMS | functional_group | polarity | stability | availability |
```

这些描述符用于材料筛选，但只能支持 Level 0 或部分 Level 1 级别的推理。它们不能直接证明动态穿透性能。

## Isotherm Block

```text
| material | component | temperature | pressure_range | uptake_at_feed_pressure | unit | model_or_raw | source |
```

等温线要在 feed-relevant partial pressure 下比较。不同温度、活化条件、单位或压力范围的数据不能直接硬比。

## Breakthrough Block

```text
| material_or_config | component | feed_basis | bed_mass | flow_rate | temperature | t5 | t50 | t95 | outlet_order | source |
```

穿透数据是动态功能判断的核心。

至少要知道：

- 材料或配置。
- 进料条件。
- 床质量。
- 流速。
- 温度。
- 目标或杂质的穿透顺序/穿透时间。

## Serial-Bed Configuration Block

```text
| configuration_id | bed_order | material_1_mass | material_2_mass | total_mass | feed_condition | objective | observed_result |
```

要支持 Level 4 配置比较，至少需要：

- 两个以上顺序或比例配置。
- 可比的进料和操作条件。
- 明确的目标指标或代理指标。

## 数据充分性分类

| 分类 | 含义 |
|---|---|
| complete | 请求的结论所需字段基本完整 |
| usable with proxy | 可以方向性推理，但指标必须标代理 |
| qualitative only | 只有定性观察，只能建议实验，不能强定量 |
| insufficient | 关键信息缺失，强推荐会误导 |

## 指标分三层

### 1. 材料筛选指标

用于判断候选材料是否适合某个功能：

- PLD, LCD, PSD
- 比表面积、孔容、空隙率
- OMS 密度
- 官能团
- 极性/疏水性
- 热稳定、化学稳定
- 合成可得性和安全性

### 2. 实验校准指标

用于判断材料是否完成预期功能：

- `t5/t50/t95`
- 动态吸附量代理
- 传质展宽
- 目标穿透时间
- 第一个杂质
- 限制杂质
- 产品收集窗口
- 曲线积分回收率/纯度代理
- 重复性

### 3. 配置指标

用于判断串联床配置是否有价值：

- 生产率
- 回收率
- 纯度
- 吸附剂利用率
- 床层质量比
- 顺序稳定性
- 进料扰动鲁棒性

## 四种指标口径

每次报告 productivity、recovery 或 purity，都必须标口径：

| 口径 | 什么时候用 |
|---|---|
| measured | 有校准流量、绝对量和真实测量 |
| curve-integral proxy | 有完整归一化曲线，可积分 |
| time-window proxy | 只有突破时间或收集窗口 |
| qualitative estimate | 只有定性描述 |

没有口径标签的纯度/回收率是不合格输出。

## Research State

每轮工作都应该维护一个研究状态：

```text
Research State
- project_id:
- date:
- target:
- feed_condition:
- target_recovery_mode:
- objective_priority:
- experiment_budget:
- available_materials:
- current_best_configuration:
- current_evidence_level:
- weakest_evidence_link:
- current_limiting_impurity:
- metric_basis:
- next_experiment:
- decision_rationale:
- overturning_result:
```

这样做的好处是：之后新实验来了，不会从头乱猜，而是明确记录为什么配置改变、哪个功能被修正、哪个证据推翻了原假设。

## Claim Trace

论文中的每个重要 claim 都应该能追溯：

```text
Claim Trace
- claim:
- supporting_module:
- evidence_level:
- supporting_data:
- metric_basis:
- safe_wording:
- unsupported_extension:
- reviewer_risk:
```

这能防止论文里把“单次实验现象”写成“普遍规律”。
