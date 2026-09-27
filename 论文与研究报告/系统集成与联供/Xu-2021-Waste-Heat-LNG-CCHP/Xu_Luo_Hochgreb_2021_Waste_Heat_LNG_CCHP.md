---
title: "A thermoacoustic combined cooling, heating, and power (CCHP) system for waste heat and LNG cold energy recovery"
authors: ["Jingyuan Xu", "Ercang Luo", "Simone Hochgreb"]
year: 2021
record_category: "论文与研究报告/系统集成与联供"
original_filename: "Xu_Luo_Hochgreb_2021_Waste_Heat_LNG_CCHP.pdf"
source_sha256: "6912a831cf20b7f454e5d65d368dc8cddea907bdfc27e7111ad53520dbc89720"
source_status: "online-fulltext"
source_url: "https://doi.org/10.1016/j.energy.2021.120341"
source_version: "Energy 227, 120341；剑桥机构库作者接受稿，封面注明2021-03-08接收，PDF38页"
source_pages: 38
institution: ["University of Cambridge", "中国科学院理化技术研究所"]
evidence_status: "理论/数值研究与应用测算；不是三联供整机或装船实测报告。"
reading_status: "已核对引言、§2.1构型、图1、图18及相邻应用讨论；未逐条审核全部计算曲线。"
doi: "10.1016/j.energy.2021.120341"
download_url: "https://api.repository.cam.ac.uk/server/api/core/bitstreams/26b7147c-b221-4409-893f-8cd875fca241/content"
input_energy_final_function: "热能→热（冷）电联供"
pressure_wave_generator: "行波热声发动机"
output_device: ["直线发电机", "热声热泵"]
engineering_type: "利用余热与LNG冷能的热声冷热电联供系统"
topology: "四单元闭合环路"
---

# Xu、Luo与Hochgreb 2021：余热和LNG冷能三联供

## 研究对象与能源边界

本研究同时利用废气热源和已有液化天然气的低温资源。LNG流经热机低温侧换热器并升温，回收其再气化过程的冷能；它是输入侧已有资源，不是该系统制得的产品。热声子系统与直线发电机匹配，同时提供电、供热与制冷服务。

这与库内TANGL报告的任务相反：TANGL用燃烧热驱动热声发动机和脉管制冷器，把天然气冷却液化。两者都涉及LNG，但不能放进同一个“液化性能”指标表。

## 原稿核读定位

- 作者接受稿PDF第7–8页，§2.1及图1：四单元环路、发动机、发电机和热泵的连接。放大图明确标出LNG与废气入口，以及电、热和制冷输出。
- 第10页图2：不同外部资源与系统工作条件；应先辨认冷热资源，再解释模型的性能。
- 第28页图15：联供模式比较；不同输出任务的评价函数不能互相替代。
- 第32页图18及相邻讨论：船舶使用方案示意，是应用设想与计算分析，不是已安装实物照片或现场示范记录。

## 证据状态

原文明确为理论分析。源温条件、阻抗匹配、可供产品组合、费用及减排均依赖设定；不能据此宣称已达到商业整机冷/热/电输出或年度收益。本次主要核对资源边界与拓扑，未逐条复算全部参数扫描和经济测算。

## 原件与来源

仓库保留文献核读入口，完整PDF从下列公开来源获取；以下页数与哈希对应已核验的原件。

- [公开来源完整PDF](https://api.repository.cam.ac.uk/server/api/core/bitstreams/26b7147c-b221-4409-893f-8cd875fca241/content)
- [原始发布来源或论文记录](https://doi.org/10.1016/j.energy.2021.120341)
- 已核验原PDF共38页；SHA-256：`6912a831cf20b7f454e5d65d368dc8cddea907bdfc27e7111ad53520dbc89720`。

## 库内相关来源

- [TANGL_Development](../../../论文与研究报告/系统集成与联供/Wollan-2002-Thermoacoustic-NG-Liquefier/TANGL_Development.md)：相关但不同来源，不标记为同源副本。
- [2024_Hu_thermoacoustic_micro_CHP_residential](../../../论文与研究报告/系统集成与联供/Hu-2024-Thermoacoustic-Micro-CHP/2024_Hu_thermoacoustic_micro_CHP_residential.md)：相关但不同来源，不标记为同源副本。
