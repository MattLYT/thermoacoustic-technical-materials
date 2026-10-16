# 热声技术资料库

本库保存热声及相邻回热式热机的原始资料与阅读版。实体目录先按资料性质、再按主要研究对象归档；装置功能、驱动链、工程型式和证据状态通过元数据分别检索。

本页统一维护资料类别、检索方法、分类与证据规则、交流资料来源规则和待补原文；历史版本通过项目Git查看。

## 阅读入口

- [[资料主题.base|资料主题]]：按资料类别、机构、输入与功能、工程型式、证据状态、年份和同源副本浏览阅读版；
- 教材《热声技术》的 36 项文献编号与核读记录随教材维护，位于项目中的 `教材/源文件/references.json`（教材在项目内单独维护）；
- 交流与原始素材的来源登记与归档规则见本页[交流资料](#交流资料)。

资料的引用追溯：已保存原件的 `source_path` 指向包内 `source/`；只有公开网页来源的阅读版保留其 URL 和取得状态。`same_source_as` 标记同源副本，统计时按唯一来源计数。只有来源、只有阅读版或尚未取得全文的条目，按实际取得状态保存，不强制补造另一半。

### 热声优化与脉管论文

| 论文 | 期刊与题录 | 原文状态 |
|---|---|---|
| [[机器学习辅助热声装置设计与优化综述_Wang_2026|机器学习辅助热声装置设计与优化综述]] | Renewable and Sustainable Energy Reviews 241 (2026), 117255；[DOI](https://doi.org/10.1016/j.rser.2026.117255) | 已核对题录；待补PDF |
| [[直列式脉管制冷机CO2污染物迁移与沉积数值研究_Zhu_2026|直列式脉管制冷机CO₂污染物迁移与沉积]] | Frontiers in Heat and Mass Transfer 24(1) (2026), 3；[DOI](https://doi.org/10.32604/fhmt.2026.076127) | 已保存18页PDF、MinerU全文与图片；数值研究 |
| [[氦氮混合工质排出器式脉管制冷机性能研究_Wang_2026|氦氮混合工质排出器式脉管制冷机]] | Applied Thermal Engineering **289, Part 1** (2026), 129788；[DOI](https://doi.org/10.1016/j.applthermaleng.2026.129788) | 已核对题录；待补PDF |
| [[声功回收脉管热泵性能研究_Zhu_2026|声功回收脉管热泵]] | International Journal of Refrigeration 189 (2026), 107009；[DOI](https://doi.org/10.1016/j.ijrefrig.2026.107009) | 已核对题录；待补PDF |

各资料包保存取得状态与出版社元数据。题录级条目在取得PDF后再转换全文；机器阅读版的公式、图题与性能数字须回原PDF核对。

## 实体目录

| 一级 | 二级 | 状态 | 收录依据 |
|---|---|---|---|
| 论文与研究报告 | 原理与综述；热声发动机与发电；制冷机与热泵；关键部件与测量；系统集成与联供 | 现有 | 论文、学位论文、机构技术报告；二级按题名、摘要和正文的主要研究对象判定 |
| 专利 | 整机与流程 | 现有 | 按主要权利要求判定；申请与授权版本记录为同一专利族的不同来源 |
| 专利 | 部件与控制 | 现有 | 气浮轴承、节流器及气浮活塞等部件专利，按权利要求对象收录 |
| 机构与产品资料 | 科研项目与示范；产品规格与厂商资料 | 现有 | 机构成果与项目页面、样机示范、厂商规格和宣传材料 |
| 交流与原始素材 | 截图与音视频；软件与模型 | 现有 | 一手音视频、用户提供的软件包及工程模型；记录来源、版本与核验状态 |
| 交流与原始素材 | 访谈与纪要 | 预留 | 收到可标注对象、日期与核验状态的记录前不建空目录 |

预留目录在收到符合收录边界的资料前不建空目录。每份资料在二级目录下有一个独立资料包：`source/` 保存原始文件，唯一文件名的 Markdown 是阅读入口，`images/` 保存其引用的派生图片，`parsed/` 保存机器解析结果。跨类别信息用元数据表示，不复制原文。PDF、HTML、图片、DOCX 等扩展名不决定资料类别；综述、理论、部件或测量方法若未研究完整装置，不强填装置字段。阅读版 frontmatter 的 `title` 缺失时，资料主题视图以文件名回退显示，回退只解决显示、不补全元数据。

## 分类与证据

名称优先采用理化所公开成果及本地论文的原文用语；它不是理化所发布的正式分类标准。原文题名、作者用词和型号始终保留，库内规范词只用于检索字段。

### 装置检索的三级字段

三级是从系统能量链走到工程部件的**阅读路径**，不是实体文件夹，也不是互斥的科学分类树。联供或多单元系统允许多个功能或部件值；某一级没有原文证据时省略该字段。

| 字段 | 要回答的问题 | 规范词示例 |
|---|---|---|
| `input_energy_final_function` | 输入能源和最终用途是什么？ | 热能→声功；热能→电能；热能→制冷；热能→供热；电能→制冷；电能→供热；热能→热（冷）电联供；外接声功→制冷 |
| `pressure_wave_generator` | 哪个装置产生声功或压力波？ | 行波热声发动机；驻波热声发动机；自由活塞斯特林发动机；直线压缩机；扬声器；压电驱动器 |
| `output_device` | 哪个工程装置完成最终功能？ | 直线发电机；行波热声制冷机；驻波热声制冷机；自由活塞斯特林制冷机；脉管制冷机；热声热泵 |

`engineering_type` 继续保存原文支持的**完整装置名称**，例如“双作用自由活塞型热声斯特林超高温热泵”或“双行波环路热驱动室温热声制冷机”。三级字段不能替代这个原名。

### 单独记录的结构属性

| 字段 | 记录内容 | 判定边界 |
|---|---|---|
| `sound_field` | 回热器、谐振管等指定位置的行波为主、驻波为主或混合声场 | 行波不自动等于闭合环路；应写明位置 |
| `topology` | 闭合环路、串联环路、同轴脉管、分置式等原文结构 | 不用“声场”词代替管路拓扑 |
| `phase_control` | 机械调相、声学调相、电调相、惯性管及双向进气等 | 只在原文支持时填写 |
| `coupling_method` | 直接耦合、功流旁通等发动机与负载的连接方式 | 不作为制冷机的工程型式 |
| `source_status` / `evidence_grade` | 原始来源取得和核验状态 | 摘要、公开网页、专利主张、模型及样机实测不能互相升级 |

### 用语对照与边界

| 原文可能用语 | 库内规范词 | 处理 |
|---|---|---|
| 脉冲管制冷机 | 脉管制冷机 | 保留原文题名，作为检索别名；不改写原始 PDF |
| 线性压缩机 | 直线压缩机 | 保留原文用语；与“直线电机”区分，后者只是机电部件 |
| 自由活塞斯特林、热声斯特林 | 各按原文的工程装置完整名称 | 二者不是可无条件互换的机器类别；理论关联另记 |
| 双行波、行波环路 | 各按原文分别记录声场与拓扑 | “双行波”需核对回热器、谐振管的局部声场，不从词面推断两股波或两个活塞 |
| 直接热声制冷核心、气体振荡式 | 不作为规范类别 | 改用热声发动机、热声制冷机、热声热泵、脉管制冷机等有明确对象的名称 |

术语依据：[[具有产业化潜力的新型制冷技术研究进展——热声制冷_罗二仓]]区分压力波发生器、热声制冷机、机械／声学调相及单／双作用；[[双行波环路热驱动室温热声制冷机的理论及实验研究_王慧志]]说明“双行波”的声场位置；理化所[团队研究范围](https://ipc.cas.cn/rcdw/zp/202601/t20260112_8103224.html)、[热泵成果](https://ipc.cas.cn/xwzx/kyjz/202512/t20251208_8023931.html)和[室温制冷成果](https://ipc.cas.cn/xwzx/kyjz/202405/t20240531_7176727.html)提供公开装置名称。术语只据其实际对象使用，不据同一团队归属推断结构或性能。

### 证据规则

- 同一层比较：`COP_ac` 只和 `COP_ac` 比，`COP_unit` 只和 `COP_unit` 比，客户 ROI 还要看 `COP_sys`；
- 电输入按互不重叠的供电支路累计，说明功放、驱动器与辅机边界；功放输入已含驱动器功率时不再重复相加。原量热记录中按体积和密度计算的质量与实测称量区分记录；
- 模型、相对 Carnot、厂商规格、项目目标和宣传材料不自动等于整机实测；
- 历史输入保存在 `source/` 仍保持原有来源角色，不得据此升级为技术 A 级证据；
- 访谈、会议和口述价格必须标注交流对象、日期、记录方式与核验状态；合同、报价、项目现状和人员经历在取得原件或当事人确认前保持 `oral-unverified`；
- 场景有痛点不等于电驱声制冷已经胜出，必须有同边界性能、成本、可靠性或可用率数据。

## 交流资料

每个资料包在阅读入口的元数据中记录来源；用户提供的QQ下载资料使用以下字段：

- `original_download`：原下载文件名；一个包有多份下载文件时按列表记录；
- `original_archive`：来源压缩包名（如 `自由活塞斯特林资料.rar`）；
- `archive_member`：成员文件在原压缩包内的文件名；
- 同哈希来源共用同一归档原件，不重复保存，例如 RE-1000 的单独下载 `RE-1000(2).pdf` 与压缩包成员 `RE-1000.pdf` 哈希一致，共用同一 `source/` 原件。

软件包内安装程序、模型和数据维持原有目录关系，使用前需另行核验。中英对照稿和术语表为用户提供的阅读材料；科学结论与公式须回到英文原件核对。

## 待补原文

下列题录沿用已有检索记录，尚无本地原件，只用于跟踪。取得可验证PDF或公开全文后，按实际状态更新并从此表移入对应资料包。

| 题名 | DOI / 编号 | 当前状态 |
|---|---|---|
| Advances in Pulse Tube Cooler with Dual-opposed Ambient Temperature Displacers | [10.1088/1757-899X/1301/1/012144](https://doi.org/10.1088/1757-899X/1301/1/012144) | 中科力函；全文未取得（2024） |
| Performance of a Highly Integrated Micro Linear Stirling Cooler with Active Vibration Cancellation | [10.1088/1757-899X/1301/1/012143](https://doi.org/10.1088/1757-899X/1301/1/012143) | 中科力函；全文未取得（2024） |
| Investigation of improving cool-down speed of a pulse tube cooler with ambient displacers | [10.1088/1757-899X/755/1/012046](https://doi.org/10.1088/1757-899X/755/1/012046) | 中科力函；全文未取得（2020） |
| Advances in a high efficiency commercial pulse tube cooler | [10.1088/1757-899X/278/1/012138](https://doi.org/10.1088/1757-899X/278/1/012138) | 中科力函；全文未取得（2017） |
| Study on a 20 K two-stage pulse tube cooler with independent ambient displacers | [10.1088/1757-899X/1301/1/012146](https://doi.org/10.1088/1757-899X/1301/1/012146) | 中科力函；全文未取得（2024） |
| Adaptability of an opposed free-piston Stirling heat pump for heating in ultra-cold regions | [10.1016/j.applthermaleng.2026.131910](https://doi.org/10.1016/j.applthermaleng.2026.131910) | 摘要级；无本地原件 |
| Output characteristics and performance comparison on a heat-driven direct-coupled thermoacoustic refrigerator with a single piston | [10.1016/j.applthermaleng.2026.131695](https://doi.org/10.1016/j.applthermaleng.2026.131695) | 摘要级；无本地原件 |
| A heat-driven thermoacoustic refrigerator/heat pump for solar-thermal application | [10.1016/j.apenergy.2025.127334](https://doi.org/10.1016/j.apenergy.2025.127334) | 摘要级；无本地原件 |
| High-power post-positioned gas spring hybrid thermoacoustic electric generator | [10.1016/j.energy.2026.140530](https://doi.org/10.1016/j.energy.2026.140530) | 摘要级；无本地原件 |
| Experimental and numerical investigation of heat transfer characteristics of spirally finned tube heat exchanger in a thermoacoustic Stirling generator | [10.1016/j.energy.2026.141598](https://doi.org/10.1016/j.energy.2026.141598) | 摘要级；无本地原件 |
| A ultra-high-temperature free-piston thermoacoustic Stirling heat pump capable of achieving above 200 °C | [10.1063/5.0292379](https://doi.org/10.1063/5.0292379) | 摘要级；无本地原件 |
| A heat-driven thermoacoustic heat pump supplying heat up to 270 °C | [10.1016/j.energy.2025.138325](https://doi.org/10.1016/j.energy.2025.138325) | 摘要级；无本地原件 |
| Ultra-efficient thermoacoustically-driven refrigeration: Detailed mechanism and optimization analysis | [10.1016/j.energy.2025.135956](https://doi.org/10.1016/j.energy.2025.135956) | 摘要级；无本地原件 |
| Acoustic field and power matching mechanism in looped heat-driven thermoacoustic refrigerators | [10.1016/j.ijrefrig.2024.11.033](https://doi.org/10.1016/j.ijrefrig.2024.11.033) | 摘要级；无本地原件 |
| A highly efficient heat-driven thermoacoustic cooling system: Detailed study | [10.1016/j.energy.2024.130610](https://doi.org/10.1016/j.energy.2024.130610) | 摘要级；无本地原件 |
| A highly efficient eco-friendly heat-driven thermoacoustic refrigerator using nitrogen and water | [10.1016/j.enconman.2024.118251](https://doi.org/10.1016/j.enconman.2024.118251) | 摘要级；无本地原件 |
| An efficient and eco-friendly heat-driven thermoacoustic refrigerator with bypass configuration | [10.1063/5.0181579](https://doi.org/10.1063/5.0181579) | 摘要级；无本地原件 |
