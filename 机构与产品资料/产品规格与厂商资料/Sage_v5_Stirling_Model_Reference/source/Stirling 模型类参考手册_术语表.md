# Sage v5 用户指南 —— 中英术语表（Terminology Glossary）

> 适用范围：`Sage Manual (User's Guide, Sage v5 Edition)` 及其配套模型类手册  
> 领域：斯特林循环机械 / 脉管制冷机 / 低温制冷机的工程建模与数值优化  
> 编制原则：**术语按行业标准；软件中组件的专有英文名称保留原形**

---

## 0. 体例说明（Conventions）

| 类别                          | 处理方式                        | 示例                                                     |
| --------------------------- | --------------------------- | ------------------------------------------------------ |
| 软件专有名称 / 组件名 / 模型类名         | **保留英文原形**，首次出现可附中文说明       | `Gizmo`、`Stirling Root`、`Matrix Gas Domain`、`PropBase` |
| 菜单路径 / 对话框 / 按钮             | **保留英文原形**（用 `\|` 连接层级）     | `Process\|Solve`、`Options\|Model Class`                |
| 通用技术术语                      | **中文（English）** 首次标注，后续仅用中文 | 回热器（Regenerator）、熵产（Entropy Generation）                |
| 变量符号 / 函数名 / 文件名 / 扩展名 / 单位 | **完全保留原样**                  | `Xddot`、`gizmo.ini`、`.stl`、`∂F/∂V`                     |
| 数学公式                        | 保留原公式形式，公式编号保留              | 式 (13.17)                                              |
| 人名 / 文献                     | 保留原文，不音译                    | Powell、Goldfarb & Idnani、Richtmyer & Morton            |

---

## 1. 软件与模型架构（Software & Model Architecture）

| 英文                          | 中文                            | 备注          |
| --------------------------- | ----------------------------- | ----------- |
| Sage                        | Sage                          | 软件名，保留      |
| model class                 | 模型类                           |             |
| model component             | 模型组件                          |             |
| composite model component   | 复合模型组件                        |             |
| model instance / model      | 模型实例 / 模型                     |             |
| submodel                    | 子模型                           |             |
| container                   | 容器                            |             |
| parallel container          | 并联容器（Parallel Container）      | 组件名，保留      |
| multi-length container      | 多长度容器（Multi-Length Container） | 组件名，保留      |
| child model                 | 子模型                           |             |
| parent component            | 父组件                           |             |
| sibling component           | 同级组件                          |             |
| root component              | 根组件                           |             |
| component palette           | 组件面板                          |             |
| edit form                   | 编辑窗体                          |             |
| display form                | 显示窗体                          |             |
| icon                        | 图标                            |             |
| model tree                  | 模型树                           |             |
| boundary connection         | 边界连接                          |             |
| boundary connector          | 边界连接器                         |             |
| connector level             | 连接器层级                         |             |
| Gizmo                       | Gizmo                         | 谐振系统模型类名，保留 |
| resonant-system model class | 谐振系统模型类                       |             |
| spring-mass-damper          | 弹簧-质量-阻尼                      |             |
| Smart Variables             | 智能变量（Smart Variables）         | Sage 架构概念   |
| Smart Models                | 智能模型（Smart Models）            |             |
| solution grid               | 解网格                           |             |
| computational grid          | 计算网格                          |             |
| spatial grid                | 空间网格                          |             |
| time grid / time ring       | 时间网格 / 时间环（Time Ring）         |             |
| staggered grid              | 交错网格                          |             |
| control volume              | 控制体                           |             |
| grid node                   | 网格节点                          |             |
| basis function              | 基函数                           |             |

## 2. 变量与数据类型（Variables & Data Types）

| 英文                                  | 中文                 | 备注 |
| ----------------------------------- | ------------------ | -- |
| variable                            | 变量                 |    |
| input variable                      | 输入变量               |    |
| output variable                     | 输出变量               |    |
| user variable                       | 用户变量               |    |
| mapped variable                     | 映射变量               |    |
| optimized variable                  | 优化变量               |    |
| implicit variable                   | 隐式变量               |    |
| dependent variable                  | 因变量                |    |
| independent variable                | 自变量                |    |
| constant                            | 常量                 |    |
| drivable variable                   | 可驱动变量              |    |
| tag / tagged variable               | 标记 / 标记变量          |    |
| variable scope                      | 变量作用域              |    |
| qualifier                           | 限定符                |    |
| referenceable variable              | 可引用变量              |    |
| identifier                          | 标识符                |    |
| integer                             | 整数                 |    |
| real                                | 实数                 |    |
| complex                             | 复数                 |    |
| phasor                              | 相量                 |    |
| Fourier series                      | 傅里叶级数              |    |
| discrete representation             | 离散表示               |    |
| data pair                           | 数据对                |    |
| cubic spline                        | 三次样条               |    |
| log spline                          | 对数样条               |    |
| enumerated                          | 枚举型                |    |
| algebraic expression                | 代数表达式              |    |
| built-in function                   | 内置函数               |    |
| model-specific function             | 模型专用函数             |    |
| operator                            | 运算符                |    |
| evaluation function                 | 求值函数               |    |
| normalisation / normalization value | 归一化 / 归一化值         |    |
| invalidation                        | 失效（invalidate：使失效） |    |

## 3. 求解、映射与优化（Solving, Mapping & Optimizing）

| 英文                                               | 中文                 | 备注              |
| ------------------------------------------------ | ------------------ | --------------- |
| solve / solving                                  | 求解                 |                 |
| map / mapping                                    | 映射（Mapping）        | Sage 功能名，保留括号英文 |
| optimize / optimization                          | 优化                 |                 |
| nonlinear solver                                 | 非线性求解器             |                 |
| optimization driver                              | 优化驱动器              |                 |
| iterative solution                               | 迭代求解               |                 |
| equation system                                  | 方程组                |                 |
| Jacobian matrix                                  | 雅可比矩阵              |                 |
| sparse matrix                                    | 稀疏矩阵               |                 |
| partial derivative                               | 偏导数                |                 |
| Newton's method                                  | 牛顿法                |                 |
| Powell's method                                  | Powell 法           |                 |
| sequential quadratic programming                 | 序列二次规划（SQP）        |                 |
| quadratic sub-problem                            | 二次子问题              |                 |
| convex method                                    | 凸方法                |                 |
| Goldfarb & Idnani                                | Goldfarb & Idnani  | 文献作者，保留         |
| objective function                               | 目标函数               |                 |
| constraint                                       | 约束                 |                 |
| extreme point                                    | 极值点                |                 |
| line search                                      | 线搜索（Line Search）   |                 |
| variable step limit                              | 变量步长限值             |                 |
| ill-conditioned problem                          | 病态问题               |                 |
| convergence                                      | 收敛                 |                 |
| tolerance                                        | 容差                 |                 |
| residual                                         | 残差                 |                 |
| search direction                                 | 搜索方向               |                 |
| solver diagnostics                               | 求解器诊断              |                 |
| Lagrange polynomial interpolation                | 拉格朗日多项式插值          |                 |
| Neville's recursive algorithm                    | Neville 递推算法       |                 |
| central difference                               | 中心差分               |                 |
| backward differencing                            | 向后差分               |                 |
| Euler's rule                                     | 欧拉法                |                 |
| Richtmyer & Morton                               | Richtmyer & Morton | 文献作者，保留         |
| Kronecker delta                                  | 克罗内克 δ 函数          |                 |
| numerical differencing / integration / averaging | 数值差分 / 积分 / 平均     |                 |
| global conservation property                     | 全局守恒性              |                 |
| harmonic                                         | 谐波                 |                 |

## 4. 斯特林循环与制冷机部件（Stirling Cycle & Cryocooler Components）

| 英文                                              | 中文                                 | 备注              |
| ----------------------------------------------- | ---------------------------------- | --------------- |
| Stirling cycle                                  | 斯特林循环                              |                 |
| stirling-cycle machine                          | 斯特林循环机械                            |                 |
| Stirling Root (component)                       | Stirling Root                      | 组件名，保留          |
| pulse tube                                      | 脉管                                 |                 |
| pulse-tube cooler                               | 脉管制冷机                              |                 |
| thermoacoustic device                           | 热声器件                               |                 |
| low-T cooler                                    | 低温制冷机（Low-T Cooler）                | 模型类名，保留         |
| Joule-Thomson cooler                            | 焦耳-汤姆逊制冷机（J-T 制冷机）                 |                 |
| regenerator                                     | 回热器                                |                 |
| regenerative displacer                          | 回热式排出器                             |                 |
| regenerator matrix                              | 回热器填料                              |                 |
| displacer                                       | 排出器                                |                 |
| displacer appendix                              | 排出器附加间隙                            |                 |
| appendix gap                                    | 附加间隙                               |                 |
| cylinder                                        | 气缸                                 |                 |
| piston                                          | 活塞                                 |                 |
| free piston                                     | 自由活塞                               |                 |
| constrained piston                              | 约束活塞                               |                 |
| simple crank piston                             | 简式曲柄活塞                             |                 |
| crank                                           | 曲柄                                 |                 |
| moving part                                     | 运动部件                               |                 |
| reciprocating mass                              | 往复质量                               |                 |
| heat exchanger                                  | 换热器                                |                 |
| isothermal heat exchanger                       | 等温换热器                              |                 |
| internally-finned heat exchanger                | 内翅片换热器                             |                 |
| matrix heat exchanger                           | 填料式换热器                             |                 |
| woven screen matrix                             | 编织丝网填料                             |                 |
| random fiber matrix                             | 随机纤维填料                             |                 |
| packed sphere matrix                            | 堆积球填料                              |                 |
| wrapped foil matrix                             | 卷绕箔片填料                             |                 |
| tube bundle                                     | 管束                                 |                 |
| rectangular channel                             | 矩形通道                               |                 |
| rectangular fin                                 | 矩形翅片                               |                 |
| canister                                        | 壳体 / 套筒（Canister）                  | 见组件名说明          |
| tubular canister                                | 管式壳体（Tubular Canister）             |                 |
| annular canister                                | 环式壳体（Annular Canister）             |                 |
| tubular-cone canister                           | 管锥式壳体（Tubular-Cone Canister）       |                 |
| annular-cone canister                           | 环锥式壳体（Annular-Cone Canister）       |                 |
| gas domain                                      | 气体域                                |                 |
| matrix gas domain                               | 填料气体域（Matrix Gas Domain）           | 组件名，保留          |
| duct gas domain                                 | 管道气体域（Duct Gas Domain）             | 组件名，保留          |
| variable-volume gas domain                      | 变容积气体域（Variable-Volume Gas Domain） | 组件名，保留          |
| combustion-space gas domain                     | 燃烧室气体域                             |                 |
| thermal solid                                   | 固体域 / 热固体                          |                 |
| solid material                                  | 固体材料                               |                 |
| heat source                                     | 热源                                 |                 |
| point heat source                               | 点热源                                |                 |
| line heat source                                | 线热源                                |                 |
| isothermal surface                              | 等温面                                |                 |
| floating isothermal surface                     | 悬浮等温面                              |                 |
| quasi-adiabatic surface                         | 准绝热面                               |                 |
| thick surface / thin surface / rigorous surface | 厚壁面 / 薄壁面 / 精确壁面                   |                 |
| heat conductor                                  | 导热体                                |                 |
| bar conductor                                   | 条形导热体                              |                 |
| distributed conductor                           | 分布导热体                              |                 |
| conductive surface                              | 导热面                                |                 |
| external conduction path                        | 外部导热通路                             |                 |
| busbar                                          | 母线 / 汇流条                           |                 |
| compliance duct                                 | 气库管（Compliance Duct）               | 组件名，保留          |
| compliance tube                                 | 气库管                                |                 |
| tapered compliance tube                         | 锥形气库管                              |                 |
| thermal buffer tube                             | 热缓冲管                               |                 |
| flow restrictor                                 | 流阻器（Flow Restrictor）               | 组件名，保留          |
| sharp-edged orifice                             | 锐边孔板                               |                 |
| asymmetric sharp-edged orifice                  | 非对称锐边孔板                            |                 |
| sintered powder plug                            | 烧结粉末塞                              |                 |
| check valve                                     | 单向阀                                |                 |
| time-dependent valve                            | 时变阀                                |                 |
| DC flow blocking restrictor                     | 直流阻流器                              |                 |
| mass-flow pump                                  | 质量流泵                               |                 |
| mass-flow driver                                | 质量流驱动器                             |                 |
| flow reverser                                   | 流向切换器（Flow Reverser）               |                 |
| flow separator                                  | 流量分离器（Flow Separator）              |                 |
| adiabatic compressor                            | 绝热压缩机                              |                 |
| pressure-regulated compressor                   | 压力调节压缩机                            |                 |
| pressure source                                 | 压力源                                |                 |
| annulus                                         | 环隙                                 |                 |
| shuttle heat loss                               | 穿梭热损失                              |                 |
| seal leakage                                    | 密封泄漏                               |                 |
| radiation transport path                        | 辐射传热路径                             |                 |
| parasitics                                      | 寄生损失（Parasitics）                   | Sage 章节名，保留括号英文 |
| flexure spring                                  | 柔性弹簧                               |                 |
| flexure stack                                   | 柔性弹簧组（Flexure Stack）               | 组件名，保留          |
| flexure-stack couple                            | 柔性弹簧组力偶（Flexure-Stack Couple）      | 组件名，保留          |
| nonlinear spring                                | 非线性弹簧                              |                 |
| relative nonlinear spring                       | 相对非线性弹簧                            |                 |
| linear motor                                    | 直线电机                               |                 |
| phasor motor                                    | 相量电机（Phasor Motor）                 | 组件名，保留          |
| time-ring motor                                 | 时间环电机（Time-Ring Motor）             | 组件名，保留          |
| generic spring / damper                         | 通用弹簧 / 通用阻尼器                       |                 |
| damper                                          | 阻尼器                                |                 |

## 5. 热力学与流体力学（Thermodynamics & Fluid Mechanics）

| 英文                           | 中文                         | 备注       |
| ---------------------------- | -------------------------- | -------- |
| working gas                  | 工质气体                       |          |
| ideal gas                    | 理想气体                       |          |
| Redlich-Kwong gas            | Redlich-Kwong 气体           | 状态方程名，保留 |
| tabular gas                  | 表格化气体                      |          |
| equation of state            | 状态方程                       |          |
| tables of state              | 状态数据表                      |          |
| conductivity k(T)            | 导热系数 k(T)                  |          |
| viscosity μ(T)               | 黏度 μ(T)                    |          |
| entropy generation           | 熵产                         |          |
| lost available energy        | 可用能损失                      |          |
| second-law balance           | 第二定律平衡                     |          |
| first law / second law       | 第一定律 / 第二定律                |          |
| isothermal                   | 等温                         |          |
| adiabatic                    | 绝热                         |          |
| quasi-adiabatic              | 准绝热                        |          |
| compression space            | 压缩腔                        |          |
| expansion space              | 膨胀腔                        |          |
| swept volume                 | 行程容积                       |          |
| dead volume                  | 死容积                        |          |
| pressure drop                | 压降                         |          |
| mass flow rate               | 质量流量                       |          |
| volumetric displacement      | 容积位移                       |          |
| positional displacement      | 位置位移                       |          |
| momentum flow                | 动量流                        |          |
| energy flow                  | 能量流                        |          |
| heat flux                    | 热流密度                       |          |
| axial conduction             | 轴向导热                       |          |
| axial-conduction enhancement | 轴向导热增强                     |          |
| film heat transfer           | 膜换热                        |          |
| combustion heating           | 燃烧加热                       |          |
| conduction                   | 导热                         |          |
| convection                   | 对流                         |          |
| free convection              | 自然对流                       |          |
| boundary convection          | 边界对流                       |          |
| streaming convection         | 声流对流（Streaming Convection） |          |
| turbulent conduction         | 湍流导热                       |          |
| turbulence model             | 湍流模型                       |          |
| turbulence transition        | 湍流转捩                       |          |
| numerical diffusion          | 数值扩散                       |          |
| Bernoulli's law              | 伯努利定律                      |          |
| energy continuity            | 能量连续性                      |          |
| viscous pressure gradient    | 黏性压力梯度                     |          |
| friction factor              | 摩擦因数                       |          |
| Nusselt number               | 努塞尔数                       |          |
| Reynolds number              | 雷诺数                        |          |
| Prandtl number               | 普朗特数                       |          |
| hydraulic diameter           | 水力直径                       |          |
| porosity                     | 孔隙率                        |          |
| tortuosity                   | 迂曲度                        |          |
| solid tortuosity             | 固体迂曲度                      |          |
| characteristic length        | 特征长度                       |          |
| refrigeration power          | 制冷功率                       |          |
| pressure wave                | 压力波                        |          |
| oscillating flow             | 交变流动                       |          |
| time-periodic                | 时间周期性的                     |          |
| time-averaged                | 时间平均的                      |          |

## 6. 菜单命令与界面（Menu Commands & UI）

| 英文                                                                                     | 中文   | 备注   |
| -------------------------------------------------------------------------------------- | ---- | ---- |
| File|New / Open / Save / Save As                                                       | 保留原样 | 菜单路径 |
| File|Save Listing / Print Listing                                                      | 保留原样 |      |
| File|Listing Preview                                                                   | 保留原样 |      |
| File|Save Solution Grid                                                                | 保留原样 |      |
| File|Save Tagged Variables                                                             | 保留原样 |      |
| Display|Show Window / Add Page / Remove Page / Remove All / Print Display              | 保留原样 |      |
| Edit|Up Connector / Down Connector                                                     | 保留原样 |      |
| Edit|Cut Model / Copy Model / Paste Model / Delete Model                               | 保留原样 |      |
| Edit|Print Form                                                                        | 保留原样 |      |
| Scan|Input Variables / Mapped Variables / Optimized Variables / Constraints / Comments | 保留原样 |      |


| Specify|Input Variables / User Variables / Mapped Variables / Optimized Variables / Constraints / Objective Function / Component Name / Comment / Child-Model Order | 保留原样 | |  
| Process|Solve / Map / Optimize | 保留原样 | |  
| Process|Explore Optimization / Explore User Variables | 保留原样 | |  
| Process|Parse Solution / Parse Mapping / Parse Optimization | 保留原样 | |  
| Process|Reinitialize | 保留原样 | |  
| Options|Sage / Model Class | 保留原样 | |  
| listing | 列表（Listing） | |  
| listing preview | 列表预览 | |  
| solution grid | 解网格 | |  
| data file | 数据文件 | |  
| initialization file | 初始化文件 | |  
| display monitor | 显示监视器 | |  
| dialog | 对话框 | |  
| textbox / listbox / checkbox | 文本框 / 列表框 / 复选框 | |  
| prompt | 提示 | |  
| keyboard shortcut | 快捷键 | |

## 7. 材料物性数据库（Material Property Databases）

| 英文                    | 中文               | 备注     |
| --------------------- | ---------------- | ------ |
| PropBase              | PropBase         | 工具名，保留 |
| material property     | 材料物性             |        |
| solid property        | 固体物性             |        |
| gas property          | 气体物性             |        |
| Redlich-Kwong fitting | Redlich-Kwong 拟合 |        |
| log spline            | 对数样条             |        |
| property data base    | 物性数据库            |        |

## 8. 通用学术与技术用语（General Technical Usage）

| 英文                            | 中文             | 备注 |
| ----------------------------- | -------------- | -- |
| upstream / downstream         | 上游 / 下游        |    |
| steady-state                  | 稳态             |    |
| transient                     | 瞬态             |    |
| hierarchy                     | 层级 / 层次结构      |    |
| interface                     | 接口             |    |
| data structure                | 数据结构           |    |
| software object               | 软件对象           |    |
| encapsulated                  | 封装的            |    |
| method / function / procedure | 方法 / 函数 / 过程   |    |
| pointer                       | 指针             |    |
| debug                         | 调试             |    |
| dynamic-link library (DLL)    | 动态链接库（DLL）     |    |
| executable                    | 可执行文件          |    |
| source code                   | 源代码            |    |
| distribution                  | 发行版            |    |
| default value                 | 缺省值            |    |
| run-time                      | 运行时            |    |
| registry                      | 注册表            |    |
| Borland Delphi                | Borland Delphi | 保留 |
| object-oriented               | 面向对象           |    |
| inheritance (inherit)         | 继承             |    |

---

## 9. 数值符号与约定（Symbols & Notational Conventions）

| 符号                | 含义                      | 保留方式 |
| ----------------- | ----------------------- | ---- |
| `F`               | 待置零函数分量 / 力             | 原样   |
| `V`               | 隐式变量 / 体积               | 原样   |
| `J`               | 雅可比（偏导）矩阵               | 原样   |
| `ΔV`              | 求解步长                    | 原样   |
| `Gx`, `Gt`, `Gxt` | 一维空间网格 / 周期时间环 / 二维时空网格 | 原样   |
| `Q(T)`            | 热流边界连接器标记               | 原样   |
| `P(ΔV)`           | 压力边界连接器标记               | 原样   |
| `ρ(P)`            | 密度边界连接器标记               | 原样   |
| `ṁ(s)`            | 气体质量流量边界连接器标记           | 原样   |
| `F(ΔX)`           | 力边界连接器标记                | 原样   |
| `∂f/∂x`, `∂f/∂t`  | 空间 / 时间导数               | 原样   |
| `Δτ`              | 无量纲时间步                  | 原样   |
| `βk`              | 时间差分系数                  | 原样   |
| `Xddot`           | 加速度状态变量                 | 原样   |

---

## 10. 模型类清单（Model Classes）

| 英文（保留原形）       | 中文说明              | 许可      |
| -------------- | ----------------- | ------- |
| `Gizmo`        | 谐振系统模型类（弹簧-质量-阻尼） | 所有发行版通用 |
| `Stirling`     | 斯特林循环模型类          | 单独许可    |
| `Pulse-Tube`   | 脉管模型类             | 单独许可    |
| `Low-T Cooler` | 低温制冷机模型类          | 单独许可    |

---

*术语表版本 v1.0 ｜ 覆盖 Sage v5 User's Guide 全文术语 ｜ 编制依据：原文实际用词 + 中文工程标准译法*

---

## 11. 斯特林模型类专有术语补充（Stirling Model-Class Terms）

> 本节为 Stirling Manual 新增条目，是对前文的补充。

| 英文 | 中文 | 备注 |
|---|---|---|
| Stirling Root | Stirling Root | 组件名，保留 |
| Stirling Cycle Model Class | 斯特林循环模型类 | 第一部分 |
| Pulse-Tube Model-Class Supplement | 脉管模型类补充 | 第二部分 |
| Low-T Cooler Model-Class Supplement | 低温制冷机模型类补充 | 第三部分 |
| case of the root model / root model | 根模型 | |
| NTnode | NTnode | 时间节点数，保留 |
| Lnorm / FreqNorm / Pnorm / Tnorm / Qnorm | 归一化常量（长度/频率/压力/温度/热流） | 保留符号 |
| Pcharge | 充气压力 | |
| Working Gas | 工质气体 | |
| ideal gas object | 理想气体对象 | |
| Redlich-Kwong gas object | Redlich-Kwong 气体对象 | |
| tabular gas object | 表格化气体对象 | |
| TBSpline2Gas / TBSpline3Gas | 二维/三维表格样条气体（保留原名） | 组件名，保留 |
| compressibility Z | 压缩因子 Z | |
| second virial coefficient | 第二维里系数 | |
| critical temperature / pressure | 临界温度 / 临界压力 | |
| virial expansion | 维里展开 | |
| thermal penetration depth | 热渗透深度 | δs / δ |
| sonic velocity | 声速 | |
| surge angular frequency | 浪涌角频率 | |
| flexure spring | 柔性弹簧 | |
| Flexure Stack / Flexure-Stack Couple | 柔性弹簧组 / 柔性弹簧组力偶 | 组件名，保留 |
| spiral arm | 螺旋臂 | |
| elastic modulus | 弹性模量 | |
| angular stiffness | 角刚度 | |
| peak torsional stress | 峰值扭转应力 | |
| effective reciprocating mass | 有效往复质量 | |
| simple crank piston | 简式曲柄活塞 | |
| crank-throw radius | 曲柄半径 | |
| connecting-rod | 连杆 | |
| nonlinear spring | 非线性弹簧 | |
| relative nonlinear spring | 相对非线性弹簧 | |
| linear motor | 直线电机 | |
| Phasor Motor / Time-Ring Motor | 相量电机 / 时间环电机 | 组件名，保留 |
| force coefficient | 力系数 | |
| Thermal Solid | 固体域 | |
| entropy generation | 熵产 | |
| availability / available energy | 可用能 / 可用度 | |
| point / line heat source | 点热源 / 线热源 | |
| Bar / Distributed Conductor | 条形导热体 / 分布导热体 | 组件名，保留 |
| Conductive Surface | 导热面 | 组件名，保留 |
| Quasi-Adiabatic Surface | 准绝热面 | |
| Thick / Thin / Rigorous Surface | 厚壁面 / 薄壁面 / 精确壁面 | 组件名，保留 |
| Floating Isothermal Surface | 悬浮等温面 | 组件名，保留 |
| thermal busbar | 热母线 | |
| skin thickness | 表层厚度 | |
| Gas Domain | 气体域 | |
| Matrix / Duct / Variable-Volume Gas Domain | 填料 / 管道 / 变容积气体域 | 组件名，保留 |
| combustion-space gas domain | 燃烧室气体域 | |
| Pressure Source | 压力源 | 组件名，保留 |
| Canister | 壳体 | |
| Tubular / Annular / Tubular-Cone / Annular-Cone Canister | 管式 / 环式 / 管锥式 / 环锥式壳体 | 组件名，保留 |
| nested canister | 嵌套壳体 | |
| active diameter | 有效直径 | |
| Heat Exchanger | 换热器 | |
| Woven Screen Matrix | 编织丝网填料 | 组件名，保留 |
| Random Fiber Matrix | 随机纤维填料 | 组件名，保留 |
| Packed Sphere Matrix | 堆积球填料 | 组件名，保留 |
| Wrapped Foil Matrix | 卷绕箔片填料 | 组件名，保留 |
| Tube Bundle | 管束 | 组件名，保留 |
| Rectangular Channels / Rectangular Fins | 矩形通道 / 矩形翅片 | 组件名，保留 |
| Generic Cylinder / Generic Matrix | 通用气缸 / 通用填料 | 组件名，保留 |
| wetted perimeter | 润湿周长 | |
| hydraulic diameter | 水力直径 | |
| tortuosity | 迂曲度 | |
| porosity | 孔隙率 | |
| Nusselt number | 努塞尔数 | |
| friction factor | 摩擦因数 | |
| Reynolds / Valensi / Prandtl number | 雷诺数 / Valensi 数 / 普朗特数 | |
| Annulus (Shuttle/Seal/Appendix) | 环隙（穿梭/密封/附加间隙） | 组件名，保留 |
| shuttle heat transfer | 穿梭传热 | |
| clearance seal | 间隙密封 | |
| appendix gap | 附加间隙 | |
| Radiation Transport Path | 辐射传热路径 | 组件名，保留 |
| gray-body emissivity | 灰体发射率 | |
| Piston-Cylinder Composite | 活塞-气缸复合组件 | 组件名，保留 |
| free-piston / free-cylinder | 自由活塞 / 自由气缸 | |
| constrained piston | 约束活塞 | |
| cylinder liner / piston shell | 气缸套 / 活塞壳体 | |
| Submodel / Container | 子模型 / 容器 | 组件名，保留 |
| Parallel Container | 并联容器 | 组件名，保留 |
| Multi-Length Container | 多长度容器 | 组件名，保留 |
| Heat-Flux Transformer | 热流变换器 | 组件名，保留 |
| PropBase | PropBase | 工具名，保留 |
| log spline | 对数样条 | |
| Compliance Duct | 气库管 | 组件名，保留 |
| Compliance Tube / Tapered Compliance Tube | 气库管 / 锥形气库管 | 组件名，保留 |
| thermal buffer tube | 热缓冲管 | |
| Flow Restrictor | 流阻器 | 组件名，保留 |
| Sintered Powder Plug | 烧结粉末塞 | 组件名，保留 |
| Sharp-Edged Orifice | 锐边孔板 | 组件名，保留 |
| Asymmetric Sharp-Edged Orifice | 非对称锐边孔板 | 组件名，保留 |
| Check Valve | 单向阀 | 组件名，保留 |
| Time-Dependent Valve | 时变阀 | 组件名，保留 |
| DC Flow Blocking Restrictor | 直流阻流器 | 组件名，保留 |
| Mass-Flow Pump / Mass-Flow Driver | 质量流泵 / 质量流驱动器 | 组件名，保留 |
| Flow Reverser | 流向切换器 | 组件名，保留 |
| Flow Separator | 流量分离器 | 组件名，保留 |
| Adiabatic Compressor | 绝热压缩机 | 组件名，保留 |
| Pressure-Regulated Compressor | 压力调节压缩机 | 组件名，保留 |
| streaming convection | 声流对流 | |
| turbulent conduction | 湍流导热 | |
| numerical diffusion | 数值扩散 | |
| Joule-Thomson (J-T) cooler | 焦耳-汤姆逊（J-T）制冷机 | |
| heat lift | 制冷量 | |
| charge pressure | 充气压力 | |
| tables of state | 状态数据表 | |

---

## 12. 气体域、换热器与湍流模型术语补充（Gas-Domain / Heat-Exchanger / Turbulence Terms）

> 本节为第 8、10 章新增条目。

| 英文 | 中文 | 备注 |
|---|---|---|
| gas domain / matrix / duct / variable-volume gas domain | 气体域 / 填料型 / 管道型 / 变容积气体域 | 组件名，保留 |
| charge line | 充气管路 | |
| pressure source | 压力源 | 组件名，保留 |
| flow inlet / flow connector | 流动进口 / 流动连接器 | |
| volume displacement | 容积位移 | |
| dead-ended / through passage | 死端通道 / 贯通通道 | |
| entropy generation (external / internal) | 熵产（外部 / 内部） | |
| conductive / viscous entropy generation | 导热熵产 / 黏性熵产 | |
| film heat transfer | 膜传热 | |
| thermal dispersion | 热弥散 | |
| axial-conduction enhancement ratio | 轴向导热增强比 | Nk |
| effective / molecular conductivity | 有效导热系数 / 分子导热系数 | ke / kg |
| tortuosity (factor / function) | 迂曲度（因子 / 函数） | fs |
| wetted perimeter | 润湿周长 | Sx |
| hydraulic diameter | 水力直径 | dh |
| Valensi number | Valensi 数 | Va |
| Prandtl / Peclet / Nusselt number | 普朗特数 / 贝克来数 / 努塞尔数 | |
| Darcy friction factor | Darcy 摩擦因数 | f |
| local loss coefficient | 局部损失系数 | K |
| momentum thickness | 动量厚度 | δ |
| momentum-thickness Reynolds number | 动量厚度雷诺数 | Rδ |
| turbulence intensity | 湍流强度 | T（第 8 章） |
| turbulent / enhanced axial conductivity ratio | 湍流（增强）轴向导热比 | Nk |
| relaminarization | 再层流化 | |
| convective triggering | 对流触发 | |
| weight function | 权重函数 | W |
| staggered grid | 交错网格 | |
| control volume | 控制体积 | |
| upwind / central differencing | 迎风差分 / 中心差分 | |
| mean-pressure constraint | 平均压力约束 | |
| time ring | 时间环 | |
| upwind fraction | 迎风比例 | UpwindFrac |
| Bernoulli's law | 伯努利定律 | |
| stagnation enthalpy flow | 滞止焓流 | |
| mixed density | 混合密度 | ρm |
| endpoint solution / extrapolation | 端点解 / 外推 | |
| Woven Screen / Random Fiber / Packed Sphere / Wrapped Foil Matrix | 编织丝网 / 随机纤维 / 堆积球 / 卷绕箔片填料 | 组件名，保留 |
| Tube Bundle / Rectangular Channels / Rectangular Fins | 管束 / 矩形通道 / 矩形翅片 | 组件名，保留 |
| Generic Matrix / Generic Cylinder | 通用填料 / 通用气缸 | 组件名，保留 |
| Ergun equation | Ergun 方程 | |
| Blasius friction factor | Blasius 摩擦因数 | |
| Colebrook formula (Altshul approximation) | Colebrook 公式（Altshul 近似） | |
| wall-shear-stress function | 壁面剪应力函数 | s = sr + i·si |
| viscous penetration depth | 黏性穿透深度 | δν |
| complex Nusselt number (compression-driven / advection-driven) | 复努塞尔数（压缩驱动 / 对流驱动） | Nuc / Nua |
| combustion-space gas domain | 燃烧室气体域 | 组件名，保留 |
| firing rate | 放热率 | FQcombust |
| Prandtl mixing length | Prandtl 混合长度 | ℓm |
| tidal amplitude / tidal displacement | 潮汐振幅 / 潮汐位移 | |

## 13. 脉管与低温模型类术语补充（Pulse-Tube / Low-T Terms）

> 本节为第 13、14、16–21 章新增条目。

| 英文 | 中文 | 备注 |
|---|---|---|
| compliance duct / compliance tube | 气库管 | 组件名，保留 |
| tapered compliance tube | 锥形气库管 | 组件名，保留 |
| thermal buffer tube | 热缓冲管 | |
| streaming convection | 声流对流 | |
| boundary convection | 边界对流 | |
| free convection (cells) | 自然对流（胞） | |
| adverse gravitational field | 逆向重力场 | |
| Grashof / Rayleigh number | 格拉晓夫数 / 瑞利数 | |
| horizontal wave number | 水平波数 | |
| numerical diffusion | 数值扩散 | |
| flow restrictor | 流阻器 | 组件名，保留 |
| Sintered Powder Plug | 烧结粉末塞 | 组件名，保留 |
| Sharp-Edged Orifice | 锐边孔板 | 组件名，保留 |
| Asymmetric Sharp-Edged Orifice | 非对称锐边孔板 | 组件名，保留 |
| Check Valve / Time-Dependent Valve | 单向阀 / 时变阀 | 组件名，保留 |
| DC Flow Blocking Restrictor | 直流阻流器 | 组件名，保留 |
| Mass-Flow Pump / Mass-Flow Driver | 质量流泵 / 质量流驱动器 | 组件名，保留 |
| Adiabatic Compressor | 绝热压缩机 | 组件名，保留 |
| Pressure-Regulated Compressor | 压力调节压缩机 | 组件名，保留 |
| Flow Reverser / Flow Separator | 流向切换器 / 流量分离器 | 组件名，保留 |
| discharge coefficient | 流量系数 | Cd |
| pressure recovery diffuser | 压力恢复扩压段 | |
| quality (vapor mass fraction) | 干度（蒸气质量分数） | X |
| submodel / container | 子模型 / 容器 | 组件名，保留 |
| Parallel Container | 并联容器 | 组件名，保留 |
| Multi-Length Container | 多长度容器 | 组件名，保留 |
| Heat-Flux Transformer | 热流变换器 | 组件名，保留 |
| PropBase (property database editor) | PropBase（物性数据库编辑器） | 工具名，保留 |
| log spline | 对数样条 | |
| state table / table of state | 状态数据表 | |
| guard row (temperature) | 温度保护行 | |
| TBSpline2Gas / TBSpline3Gas | 二维 / 三维表格样条气体 | 组件名，保留 |
| saturated vapor / liquid specific volume | 饱和蒸气 / 液体比容 | vv / vl |
| two-phase (saturation) zone | 两相（饱和）区 | |
| RefPropToBSpline3Gas | RefPropToBSpline3Gas | 工具名，保留 |
| J-T (Joule-Thomson) cooler | 焦耳-汤姆逊（J-T）制冷机 | |
| Gifford-McMahon cooler | Gifford-McMahon 制冷机 | |
| heat lift | 制冷量 | |
| puised / pulsatile flow | 脉动流 | |
| isenthalpic flow stream | 等焓流动 | |
| expansion / compression work | 膨胀功 / 压缩功 | |
