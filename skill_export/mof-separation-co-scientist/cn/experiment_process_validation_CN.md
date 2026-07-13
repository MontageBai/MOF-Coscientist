# 实验控制、不确定性和工艺验证中文说明

英文对应：

- `references/experimental_controls_uncertainty.md`
- `references/regeneration_scaleup_tea_protocol.md`
- `references/module_7_process_validation_engine.md`

## 为什么这部分重要

好的配置假设不等于论文结论。穿透曲线差异可能来自活化、装填、流量、检测器漂移、归一化、死体积或偶然误差。因此必须把控制实验和不确定性写清楚。

## 最低控制实验

### Blank 和系统控制

可行时需要：

- 空管或空柱响应。
- 惰性填料控制。
- 载气基线。
- 检测器基线和漂移检查。
- bypass 或无吸附剂响应。

目的：区分真实吸附延迟和系统死体积、检测器滞后、管路效应。

### 单床控制

串联床里的每个材料，最好都有单床穿透数据：

- 床质量。
- 流速。
- 温度和压力。
- 活化条件。
- 粒径或成型形态。
- 曲线归一化方法。

目的：证明材料确实能完成分配给它的功能。

### 顺序和比例控制

如果要说某个配置更好，至少要考虑：

- 之前最好的 baseline ratio。
- 反向顺序。
- 附近比例扰动。
- 单功能控制。

目的：区分真实顺序/比例效应和总床质量或容量效应。

## 重复性

如果条件允许，最终最佳配置至少做 duplicate。

如果只有一次实验：

- 只能说 single-run observation 或 configuration hypothesis test。
- 不能说 statistical superiority。
- 要说明下一步最需要重复哪个实验。

## 不确定性来源

需要显式记录：

- 流量误差。
- 床质量误差。
- 检测器响应因子。
- 曲线数字化误差。
- 基线漂移。
- 进料组成误差。
- 活化状态差异。
- 粒径和装填差异。
- 温度或压力波动。
- 积分窗口选择。

## Claim 阈值

| 证据 | 可以支持的说法 |
|---|---|
| 单次串联床成功 | promising configuration hypothesis |
| 顺序比较 | sequence-dependent performance |
| 比例系列 | ratio-sensitive performance 或 locally improved ratio |
| 最终配置重复 | reproducible improvement under tested conditions |
| 再生和循环测试 | process-validation outlook |

不要在没有重复统计时说 significant。不要在没有系统搜索时说 global optimum。不要在没有再生/循环和实用材料数据时说 process-ready。

## 再生和放大为什么单独看

穿透性能好，只说明实验室分离有希望。工艺可行还要看：

- 目标或杂质能不能再生出来。
- 再生温度和能耗。
- 多次循环后容量是否保持。
- 材料能否成型。
- 压降是否可接受。
- 合成是否能放大。
- 成本和安全性。

## Process-Relevance Input

```text
Process-Relevance Input
- best_configuration:
- target_recovery_mode:
- adsorption_condition:
- regeneration_condition:
- cycle_count:
- material_form:
- synthesis_batch_size:
- material_cost_or_precursor_proxy:
- moisture_or_contaminant_tolerance:
- pressure_drop_or_particle_size_proxy:
- safety_or_handling_constraint:
```

如果这些字段缺失，就只能说 process-validation outlook。

## Regeneration Record

```text
| material | retained species | regeneration method | temperature | pressure | purge gas | desorption completeness | evidence |
```

要问：

- 再生是否释放目标或杂质？
- 再生温度是否破坏 MOF？
- 强吸附带来纯度好处的同时，是否带来再生能耗惩罚？
- 脱附是否足够完全，可以进入下一循环？

## Working Capacity

理想定义：

```text
working capacity = q_adsorption(condition) - q_regeneration(condition)
```

没有完整等温线时，只能用 feed-relevant uptake 加定性再生惩罚，标为 proxy。

## Cycle Stability

经验边界：

- 1 cycle：只能说再生可行性观察。
- 3 cycles：初步循环稳定性。
- 5+ cycles：更强的实验室循环稳定性。
- 长期过程稳定性需要更多循环和成型材料数据。

## TEA Proxy

没有详细流程模拟时，可以用代理指标：

- 吸附剂成本代理。
- 每 mol 目标再生能耗代理。
- 单位床质量或床体积生产率。
- 循环时间。
- 容量保持或更换频率。
- 合成放大风险。
- 成型和压降风险。

输出：

```text
TEA Proxy Summary
- productivity basis:
- recovery/purity basis:
- regeneration energy proxy:
- adsorbent cost proxy:
- cycle-time proxy:
- material lifetime risk:
- pressure-drop/shaping risk:
- strongest economic advantage:
- largest economic uncertainty:
```
