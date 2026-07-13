# 早期阶段结构目标协议中文说明

英文对应：

- `references/early_stage_structural_target_protocol.md`
- `references/data_input_contract.md`
- `references/module_3_sorbent_screening_engine.md`
- `references/module_5_configuration_optimizer.md`

## 什么时候用

当用户只给了：

- 分离任务；
- 目标分子；
- 进料组成；
- recovery mode 或 objective；

但还没有给：

- 候选 MOF 列表；
- PLD/LCD/PSD 等描述符表；
- 等温线；
- 穿透曲线；
- 动力学或再生数据；

这时 co-scientist 不应该直接推荐材料，也不应该给床层比例。

## 正确推进顺序

```text
确定任务
-> 确定 recovery mode
-> 分析分离逻辑
-> 定义床层功能
-> 定义结构目标
-> 明确下一步材料搜索需要什么数据
-> 下一轮再找候选材料
```

## 允许输出什么

可以输出：

- 这个分离任务的本质是什么；
- breakthrough product 是否与常规吸附选择性冲突；
- 需要捕获什么杂质，避免滞留什么目标；
- 需要什么结构目标；
- 下一步如何按结构目标找材料。

结构目标可以包括：

- cage-window 结构；
- 合适孔口尺寸；
- 门控或柔性窗口；
- 疏水孔环境；
- 弱/中等极性；
- 是否需要 OMS，或是否要避免强 OMS；
- 对目标分子的低滞留；
- 对限制杂质的扩散或亲和延迟；
- C6 稳定性和可再生性。

## 不允许输出什么

在只有进料组成时，不应该输出：

- 某个最佳 MOF；
- 具体材料组合；
- bed order；
- mass ratio；
- purity/recovery/productivity；
- optimized configuration。

## 推荐表格

```text
Structural Target Profile
| function | desired structure/chemistry | avoid | reason | data needed to search |
|---|---|---|---|---|
```

## 对 C6 breakthrough product 的特别提醒

如果目标是线性烷烃并要求作为 breakthrough product，很多微孔材料可能会更强吸附线性烷烃，所以这是一个逆常规选择性问题。

这时早期目标不是“找最强吸附目标分子的材料”，而是：

```text
找能延迟杂质、同时限制目标滞留的结构类型。
```

也就是说，先找结构靶标，例如 cage-window、门控窗口、疏水低极性孔环境，而不是直接列材料名。

## 安全表述

可以说：

```text
The current stage supports a structural target profile, not a material recommendation.
```

中文：

```text
当前阶段支持结构目标定义，不支持材料推荐。
```
