# MOF Co-Scientist · v2.0

面向多组分吸附分离的科研辅助技能：结合等温线、单床穿透、动力学与串联实验，提出可解释的材料组合、床序及质量配比假设。

**v2.0 主技能：[`mof-tandem-bed-co-scientist`](skill_export/mof-tandem-bed-co-scientist/SKILL.md)**。新增可执行的动态容量匹配公式，支持 CSV / Excel 输入、组分负荷分析、实验校准和进料工况迁移。

## v2.0 的工作方式

```text
分离任务与进料 → 分配床层功能 → 单床曲线积分
→ 计算残余杂质负荷与配比基线 → 材料证据修正
→ 串联实验验证 → 更新配置假设
```

对前床 U、后床 D 及后床负责的杂质组分 g：

```text
q_U,i = F_i × ∫[0, x_B](1 − C_i/C_i,0) dx     （按吸附剂质量归一化）
τ_U = Σ(i∈B)q_U,i / Σ(i∈B)L_i
b_g,res = max(0, L_g × τ_U − q_U,g)
m_D/m_U = max(g∈G)[b_g,res / q_D,g]
```

`x_B` 为前床任务杂质中最早达到指定突破阈值的时刻；最严格的后床任务组分控制质量比。普通时间轴的积分结果需要除以床质量；已按质量归一化的时间轴不能重复除质量。详见[公式与单位约定](skill_export/mof-tandem-bed-co-scientist/references/tandem_capacity_matching.md)。

**公式输出是容量匹配基线。** 它不等于全局最优配比，也不自动证明产品纯度或回收率。缺少同进料动态曲线时，输出有明确假设的迁移范围或待验证配置。

## 安装与开始使用

按 [INSTALL.md](INSTALL.md) 安装 `skill_export/mof-tandem-bed-co-scientist`，然后向支持技能的助手发送：

```text
使用 $mof-tandem-bed-co-scientist 分析我的多组分吸附分离任务。
先检查进料、目标产品、单床穿透曲线、床质量、流量和单位是否齐全。
条件允许时计算容量匹配基线，再结合等温线、动力学和实验结果提出床序及配比建议。
请区分实测、计算、推断及待验证预测，并列出下一步最关键的实验。
```

直接运行合成示例（Python 3.10+，CSV 计算无需第三方库）：

```bash
python skill_export/mof-tandem-bed-co-scientist/scripts/tandem_capacity_analysis.py examples/tandem_synthetic/manifest.json
```

示例全部为人为构造的测试数据，不能作为实际材料性能或实验验证证据。

## 仓库内容

| 路径 | 用途 |
|---|---|
| `skill_export/mof-tandem-bed-co-scientist/` | v2.0 通用串联床主技能、公式脚本、协议及中文读本 |
| `skill_export/mof-separation-co-scientist/` | 保留的 2026 年 7 月旧版，便于复现；新任务优先使用 v2.0 |
| `examples/tandem_synthetic/` | 可运行的合成曲线与输入示例 |
| `tests/` | 容量积分、组分控制、质量归一化及输入检查 |
| `private_cases/` | 历史外部评价案例，不属于安装内容；公开仓库中的此目录并非私密存储 |

盲测时只向助手提供当前技能与指定输入；不要让评价案例、预期配置或最终实验结果进入预测输入。

## 检查与版本

```bash
python -m pip install -r skill_export/mof-tandem-bed-co-scientist/requirements.txt
python skill_export/mof-tandem-bed-co-scientist/scripts/validate_skill_structure.py skill_export/mof-tandem-bed-co-scientist
python -m unittest discover -s tests -v
```

结构检查与合成数据测试验证文件完整性和计算行为，不能代替真实串联实验或独立科研评价。版本变化见 [CHANGELOG.md](CHANGELOG.md)；历史记录见 [CHANGELOG_BRIEF.md](CHANGELOG_BRIEF.md)。
