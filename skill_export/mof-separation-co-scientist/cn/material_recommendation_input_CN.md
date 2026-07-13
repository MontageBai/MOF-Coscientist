# 材料推荐输入协议中文说明

英文对应：

- `references/material_recommendation_input_protocol.md`
- `references/module_3_sorbent_screening_engine.md`
- `references/data_input_contract.md`

## 什么时候用

当已经完成早期结构目标定义，准备进入“找材料”阶段时使用。

这一步不能凭记忆列常见 MOF，而应该基于：

1. 分子三维尺寸表；
2. 用户或项目指定的 MOF 数据库路径；
3. 数据库中 PLD、LCD、GLD 等字段的映射；
4. 功能层需求；
5. 先生成候选材料空间；
6. 需要时再做软排序或 shortlist。

## 推荐流程

```text
结构目标
-> 分子尺寸表
-> MOF 描述符数据库路径
-> 字段映射
-> 几何硬筛
-> 按功能生成候选材料空间
-> 人工选择或按实验预算再收敛
-> 标出证据等级和下一步实验
```

## 分子尺寸表

你可以给所有目标和杂质分子的三维尺寸。

```text
Molecule Size Table
| component | role | length_A | width_A | thickness_A | limiting_dimension_A | source_or_method | note |
|---|---|---:|---:|---:|---:|---|---|
```

说明：

- 通常中间尺寸或限制尺寸最适合与孔口匹配。
- 尺寸来源要写清楚，比如 DFT 优化、力场优化、动力学直径、范德华包围盒、文献值。
- 不同来源的尺寸不能混着当成同一精度。

## MOF 数据库路径

数据库应该因项目而异，由用户配置。

```text
MOF Descriptor Database
- database_path:
- file_format: csv / xlsx / parquet / sqlite / json / other
- material_id_field:
- descriptor_fields:
  - PLD:
  - LCD:
  - GLD:
  - pore_size_distribution:
  - surface_area:
  - pore_volume:
  - topology:
  - dimensionality:
  - OMS:
  - functional_groups:
  - polarity_or_charge:
  - hydrophobicity:
  - stability:
  - availability:
- units:
- source:
- filters_or_exclusions:
```

注意：

- `PLD/LCD/GLD` 的定义以数据库为准，必须先确认字段含义和单位。
- 如果数据库没有 `GLD`，可以用等价的 transport/path descriptor，但必须标注替代关系。
- 不要把数据库字段名写死，因为不同人数据库列名会不一样。

## 硬筛选逻辑

先硬筛，再排序。

硬筛包括：

- 孔口或路径尺寸是否允许目标/杂质进入；
- cavity 是否能容纳相关分子；
- 是否满足 cage-window、门控、柔性、疏水性等结构目标；
- 是否明显强滞留目标，违反 breakthrough-product 目标；
- 材料是否稳定、可获得、可再生。

## Descriptor Match Plan

在候选材料列表之前，先输出这个表：

```text
Descriptor Match Plan
| function | molecule dimension constraint | PLD/LCD/GLD logic | chemistry requirement | hard exclusions | soft priorities |
|---|---|---|---|---|---|
```

## Candidate Material Space

Module 3 默认应该先输出候选材料空间，不要一开始就筛到只剩两三个。

```text
Candidate Material Space
| function | candidate | inclusion_reason | matching_features | evidence_type | evidence_level | uncertainty | human_selection_note |
|---|---|---|---|---|---:|---|---|
```

这个表的目的不是替人做最终选择，而是把可能可行的都按功能归类，让人再结合手头材料、合成难度、实验成本和论文故事来选。

## Candidate Shortlist

只有当用户要求排序，或者实验预算很紧时，再输出 shortlist：

```text
Candidate Shortlist
| function | material_id | matched_descriptors | why_candidate | evidence_level | risk | next_validation |
|---|---|---|---|---:|---|---|
```

## 关键纪律

- 先建立候选材料空间，再按需要排序。
- 只在同一个功能内排序，不做全局 MOF 排名。
- 几何匹配、吸附亲和力、动力学、再生、实用性要分列，不要揉成一个总分。
- 只有描述符时是 Level 0。
- 有 feed-relevant 等温线时可以到 Level 1。
- 有穿透数据时才可能到 Level 2 或更高。

## 缺数据时怎么办

如果没有分子尺寸表：

- 先要求用户给尺寸表；
- 或说明将采用哪种尺寸估计方法；
- 不要偷偷做几何匹配。

如果没有数据库路径：

- 先要求用户给项目数据库路径；
- 或输出数据库 schema；
- 不要凭记忆编材料列表。

如果用户给的是 markdown 笔记：

- 从笔记里提取材料名、孔尺寸、结构类型、OMS 状态、已知吸附行为和风险；
- 把这些作为 note-derived evidence；
- 先放入候选材料空间，不要因为证据还不完整就直接丢掉。

如果 PLD/LCD/GLD 定义不清：

- 先要求数据库说明或字段定义；
- 筛选只能标 preliminary。
