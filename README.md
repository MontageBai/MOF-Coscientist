# MOF Co-Scientist · v2.0.1

面向多组分吸附分离的科研辅助技能，结合等温线、单床穿透、动力学和串联实验，提出可解释的材料组合、床序及质量配比假设。

主技能：[`mof-tandem-bed-co-scientist`](mof-tandem-bed-co-scientist/SKILL.md)。

## 工作方式

```text
分离任务与进料 → 分配床层功能 → 单床曲线积分
→ 计算残余杂质负荷与配比基线 → 材料证据修正
→ 串联实验验证 → 更新配置假设
```

对于前床 U、后床 D 及后床负责的杂质组分 g：

```text
q_U,i = F_i × ∫[0, x_B](1 − C_i/C_i,0) dx     （按吸附剂质量归一化）
τ_U = Σ(i∈B)q_U,i / Σ(i∈B)L_i
b_g,res = max(0, L_g × τ_U − q_U,g)
m_D/m_U = max(g∈G)[b_g,res / q_D,g]
```

`x_B` 是前床任务杂质最早达到指定突破阈值的时刻，最严格的后床任务组分控制质量比。普通时间轴的积分结果需要除以吸附剂质量；已按质量归一化的时间轴不能重复除质量。详见[公式与单位约定](mof-tandem-bed-co-scientist/references/tandem_capacity_matching.md)。

公式结果是**容量匹配基线**，并不自动证明全局最优配比、产品纯度或回收率。缺少同进料动态曲线时，应明确迁移假设与不确定性。

## 安装

将整个 `mof-tandem-bed-co-scientist` 文件夹复制到 Codex 的技能目录：

- Windows 默认位置：`%USERPROFILE%\.codex\skills\`
- macOS / Linux 默认位置：`~/.codex/skills/`
- 设置过 `CODEX_HOME` 时，使用其下的 `skills/` 目录。

最终入口应为 `skills/mof-tandem-bed-co-scientist/SKILL.md`。已有同名版本时先备份，再更新。安装后新建聊天，并调用 `$mof-tandem-bed-co-scientist`。

```text
使用 $mof-tandem-bed-co-scientist 分析我的多组分吸附分离任务。
先检查进料、目标产品、单床穿透曲线、床质量、流量和单位。
条件允许时计算容量匹配基线，再结合材料证据和串联实验提出床序及配比建议。
请区分实测、计算、推断及待验证预测。
```

## 直接运行计算

需要 Python 3.10+。CSV 计算使用标准库；结构检查需要 PyYAML，Excel 输入还需要 openpyxl。从本仓库根目录运行：

```bash
python -m pip install -r mof-tandem-bed-co-scientist/requirements.txt
python mof-tandem-bed-co-scientist/scripts/validate_skill_structure.py mof-tandem-bed-co-scientist
python mof-tandem-bed-co-scientist/scripts/tandem_capacity_analysis.py /path/to/manifest.json /path/to/result.json
```

将示例路径替换为自己的输入和输出路径。输入字段、曲线列映射和归一化约定见[输入格式](mof-tandem-bed-co-scientist/references/tandem_manifest_schema.md)。曲线文件路径相对于输入 JSON 所在目录解析。

## 文件结构

```text
README.md
mof-tandem-bed-co-scientist/
├── SKILL.md          技能入口与版本信息
├── agents/           技能界面配置
├── references/       计算公式、数据约定与研究协议
├── scripts/          容量匹配及技能检查工具
├── cn/               中文辅助说明
└── requirements.txt  Python 依赖
```

英文 `SKILL.md` 与 `references/` 为正式技能说明，`cn/` 为中文阅读辅助。v2.0.1 精简发布目录，容量匹配计算方法保持 v2.0.0 的实现。
