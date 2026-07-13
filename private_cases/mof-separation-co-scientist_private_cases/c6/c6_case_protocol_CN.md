# C6 / nHEX 案例中文说明

英文对应：

- `references/case_study_c6_protocol.md`
- `references/forward_test_c6_fixture.md`

## 案例目标

目标分子：

```text
nHEX
```

代表性进料分压：

```text
22DMB / 23DMB / 2MP / 3MP / 1HEX / nHEX
= 1.51 / 1.05 / 0.89 / 0.74 / 1.52 / 18.91 kPa
```

这个案例要做的不是“找最强吸附 nHEX 的 MOF”，而是设计一个串联床配置，让 `nHEX` 产品表现更好，同时考虑生产率、回收率、纯度和实验预算。

## 必须先整理的三张表

### 1. Feed Table

```text
| component | partial pressure kPa | role | expected issue |
```

作用：把混合物从一串组分变成“目标、杂质、潜在限制杂质”的角色表。

### 2. Material Evidence Table

```text
| MOF | data type | component behavior | likely function | evidence level | risk |
```

作用：记录每个 MOF 有什么证据，可能适合哪个床层功能。

### 3. Breakthrough Feature Table

```text
| MOF/configuration | target breakthrough | first impurity | clean window | limiting impurity | metric basis |
```

作用：把穿透行为转成可比较的动态特征，而不是只看曲线长得怎么样。

## C6 中要保留的关键观察

在数据支持时，可以保留这些观察：

- HKUST-1 对 `1HEX` 有较强延迟或去除能力。
- UiO-66 和 UiO-66-NH2 是剩余组分分离的重要候选。
- UiO-66 和 UiO-66-NH2 对剩余组分可能有不同的出口顺序。
- UiO-66-like 层接 HKUST-1-like 层可能是一个有力的串联床假设，但必须用功能解释。
- 如果已有实验显示 `100 mg + 10 mg` 比等质量更好，替换 MOF 时应从这个功能质量分布出发，而不是重新假设 1:1。

注意：这些不是普适真理，只是当前 C6 案例下的证据线索。必须绑定进料、活化、流速、床质量、温度和穿透条件。

## 一次实验预算时怎么推荐

如果只能做一个实验，并且目标是性能优先：

1. 只给一个 primary configuration。
2. 明确 bed order、mass ratio、total mass 和 collection window。
3. 说明每一层的功能。
4. 说明最大风险。
5. 说明什么结果会推翻这个假设。

不要给三四个“都可以试试”的选项。实验只有一次时，回答要有判断力。

## C6 的功能化思路

可以按这个方向理解：

```text
不是：HKUST-1 是不是最佳 MOF？
而是：HKUST-1 适合哪个功能？

不是：UiO-66 和 UiO-66-NH2 谁总体更好？
而是：谁更适合作为前置序列调控层，谁更适合作为后置精制层？

不是：Zn-MOF-74 要不要直接 1:1 替换？
而是：它替代的是哪个功能？容量、选择性、目标滞留和再生风险如何改变比例？
```

## 替换 MOF 时的比例迁移

当替换某一层材料时，必须先问：

- 替换的是哪个功能？
- 新材料对限制组分的动态容量更高还是更低？
- 新材料是否更强烈保留目标分子，从而降低生产率？
- 新材料是否有动力学拖尾、再生或稳定性问题？

输出格式：

```text
Replacement Ratio Hypothesis
- Original best configuration:
- Replaced function:
- Replacement material:
- Proposed new ratio:
- Why this ratio migrates:
- Expected benefit:
- Biggest risk:
- Evidence level:
```

## 指标口径

如果只有归一化穿透曲线，可以使用曲线积分代理指标：

```text
proxy = integral(C_A / C_A0 dt over selected window) / Delta t
```

但这只能叫 curve-integral proxy。没有流量、校准和绝对物质的量时，不能说真实纯度、真实回收率或真实生产率。

如果只有突破时间，没有完整曲线，就叫 time-window proxy。

如果只有定性描述，就叫 qualitative estimate。

## C6 论文图建议

适合做这些图：

1. 进料和分子角色图。
2. 功能床层设计图。
3. 描述符或等温线支持图。
4. 单组分穿透校准图。
5. 串联床配置比较图。
6. one-shot 或 replacement-MOF 预测图。
7. 工艺验证展望图。

## C6 的安全表述

可以说：

- “C6 case-study demonstration”
- “configuration hypothesis”
- “experimentally calibrated function”
- “ratio migration hypothesis”

不要说：

- “global optimum”
- “universally best MOF”
- “replacement MOF will always outperform”
- “process-ready” without regeneration and cycle data
