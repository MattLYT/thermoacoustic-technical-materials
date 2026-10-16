---
title: 附录、索引与参考文献 · Swift热声学中文译本
record_role: machine-transcription
---

# 附录、索引与参考文献

[[热声学_统一方法_Swift著_罗二仓译|教程入口]] · [[Swift热声学_07_测量|上一部分]]

> [!info] 来源与核对
> [[热声学-中文版(1).pdf#page=233|原 PDF 第 233–254 页]]。本稿整理阅读结构；公式及数字仍需核对原页。

> [!contents]- 本部分目录
> - [[#^sec-01|驻波发动机]]
> - [[#^sec-02|驻波制冷机]]
> - [[#^sec-03|热声斯特林发动机]]
>   - [[#^sec-04|A]]
>   - [[#^sec-05|B]]
>   - [[#^sec-06|C]]
>   - [[#^sec-07|D]]
>   - [[#^sec-08|E]]
>   - [[#^sec-09|G]]
>   - [[#^sec-10|H]]
>   - [[#^sec-11|I]]
>   - [[#^sec-12|J]]
>   - [[#^sec-13|L]]
>   - [[#^sec-14|M]]
>   - [[#^sec-15|N]]
>   - [[#^sec-16|O]]
>   - [[#^sec-17|Q]]
>   - [[#^sec-18|R]]
>   - [[#^sec-19|S]]
>   - [[#^sec-20|T]]
>   - [[#^sec-21|V]]
>   - [[#^sec-22|W]]
> - [[#^sec-23|参考文献]]

在第 1章的“例子”一节贯穿本书其它部份，以下是关于这些范例硬件的部份DeltaE文件。

## 驻波发动机

^sec-01

这个驻波发动机的部件模型从图 1.10 中的右端开始并积分到左端，通过分支到制冷机，并在谐振管中央的压力节点结束。采用在这个特定文件中的目的是：为了使这个制作的硬件在到制冷机的支路运行在 $p _ { 1 } { = } 2 9 7 \mathrm { k P a }$ ，并且提供 1000W的声功给制冷机，那么在热端热交换器需要多少温度和多少加热功率，这个系统将共振在什么样的频率？（在这个简化的模型中，我们假设在左边的发动机能提供 500W的声功，但在 Los Alamos 我们通常完全地包括了左边发动机的细节在模型中）。

## 驻波制冷机

^sec-02

这个驻波制冷机的模型从图1.12 中制冷机一侧的驱动器开始，向下通过热声堆和它相邻的热交换器积分，到谐振管下部支撑腿的中央的压力节点结束。在这个特定文件中的目的是：为了使制作的硬件在靠近驱动器的部件运行在 $p _ { 1 } { = } 6 4 6 7 \mathrm { k P a }$ ，并达到一个实验观察到的冷端温度 285.6K, 那么 $U _ { 1 } ,$ ,f和冷端热交换的热负荷应发生什么情况？

## 热声斯特林发动机

^sec-03

整个热声斯林的模型似乎很复杂，但是在Los Alamos，它事实上是一个在经过很多月份的实验和计算的进展后一个典型的情况。这个模型从图 1.14 的上部开始，即室温热交换器的上部。它从上积分，到左边、再向下、通过声容，到连接处的惯性管，它然后又正好从室温热交换器的上部开始，向下通过回热器、热缓冲管，并第二次到达连接处，这里复数压力 $p _ { 1 }$ 必须匹配。然后积分通过谐振管向前推进。

微损失在这里作为声阻而进入模型，其值根据类似于方程5.33 中的一些东西而计算（在进行至 RPNTARC）。我们对这些现象的理解仍十分不完善，且进展迅速，因此在这个文件的一些细节是不可信的。

（页数和书的数目请参考Backhaus 的实验计录本）

小孔脉冲管制冷机

Cryenco 目前不愿意公开地共享图 1.15 中小孔脉冲管制冷机的制作细节，因此，这个模型仅包括了图 1.16 上部的 LRC 网络。这个模型从气库开始，并正好在脉冲管上部的热交换器结束。这个文件制作的硬件要达到的目的是：为了达到在气库中的 $p _ { 1 }$ （幅度和相位）以及在实验中观察脉冲管上部的压力，那么两个阀门的流动阻力必须为多少？这些阻力中有一个为负值，表明在这个模型中有错误，也许DeltaE对惯性管中湍流的估计是不准确的。

索 引（以单词的外文字母为顺序）

### A

^sec-04

Acoustic approximation (声学近似) 26,37,55 Acoustic impedance (声阻抗) 40,46,50 specific\~ (比声阻抗) 69 Acoustic power (声功) 73 \~measurement (声功测量) 197 \~dissipation (声功耗散) Amplitude (幅度) 27 Aneurysm ( ) 181 Angular frequency (角频率) 14 Animation (动画) 32 Oscwall\~(壁面振荡动画) 69 Ptr\~（脉冲管动画） 81,87,89 Standing \~(驻波动画) 53,82,89 Tashe \~(行波动画) 8,66,79 Thermal\~ (热的动画) 49,53,78,95 Viscous\~ (粘性的动画) 45,69,77 Wave\~ (波的动画) 28, 41,75 Attenuation constant (衰减常数) 16 Bulk\~ (体衰减常数) Availability (可用性) 103 Average (平均的) 45 Spatial\~ (空间平均的) Temporal\~(时间平均的) 67

### B

^sec-05

Blunders (谬误) 25 Boundary layers (边界层) \~approximation (边界层近似) \~dissipation (边界层耗散) 77 \~intergrals (边界层积分) 45 \~temperature (边界层温度) 49，53 \~velocit (边界层速度) 44

### C

^sec-06

Carnot cycle (卡诺循环) 8 Cavity (洞穴) Accident\~ (偶然的空腔) 181 Coefficient of performance (性能系数) 8 Carnot\~ (卡诺性能系数) 8，97 Complex conjugate (复数共轭) 67 Compliance (声容) 37，50，60 Accidental\~ (偶然的声容) 181， \~example (声顺的例子) 46，48，51，63 Compressibility (压缩性) 38，58 Computation (计算) 29，90，223 Conductance (传导) Thermal-relaxation\~ (热松弛传导) Constants (常数) 16 Continuity equation (连续性方程) 28，115 Acoustic\~ (声学连续性方程) 50，57 Lossless acoustic\~ (无损声学的连续性方程) 13，28，37 Thermoacoustic\~ (热声学连续性方程) 57

Control volume (控制容积) 83 Convection (对流) Critical temperature gradient (临界温度梯度) 53,82,89,106

### D

^sec-07

DeltaE (基于声学近似的一个计算程序) 31, 90, 223Discontinuities (突变)Displacement amplitude (位移幅度) 44Dissipation of acoustic power (声功耗散)Accidental cavity\~ (由偶然的空腔引起的声功耗散) 182

Boundary-layer\~ (边界层产生的声功耗散) 77Thermal-relaxation (热驰豫产生的声功耗散) 76Valve\~ (阀门引起的声功耗散) 128Viscous\~(粘性引起的声功耗散) 76

### E

^sec-08

Efficiency (效率) 8 Carnot\~(卡诺效率) 8，97 Electric circuit analog (电路模拟) 38 Energy equation (能量方程) 115 Engine (发动机) 7 Enthalpy (焓) 85 Entrance effects (入口效应) 130 Entropy (熵) 7，87，97，136 Equation of motion (运动方方程) Eulerian and Lagrangian viewpoints (欧拉和拉格朗日观点) 53 Examples (例子) Exergy (火用) 103,117 First law of thermodynamics (热力学第一定律) 7 Flow availability (流动可用能) 103 Fluidyne engine (液体发动机) 119，120 Friction factor (摩擦因子) 119，120

### G

^sec-09

Gas (气体) 165\~constants and identities (常数和恒等式) 16Gouy-Stodoca therorem (GS 定理) 100Acoustic\~ (声学形式的 GS 定理) 103

### H

^sec-10

Harmonics (谐波) 156，184Heat (热量) 7，84，88\~measurement (热的测量) 200

\~capacity (热容) 15 \~engine (热发动机) 7 \~exchanger (热交换器) 84，174 \~pump (热泵) 35 Heat-transfer equation (传热方程) 49 Acoustic\~ (声学形式的传热方程) 52，56 Helmholt resonator (亥姆霍兹共振器) 40 Hydraulic radius (水力半径) 44 Screen\~ (丝网的水利半径) 118

### I

^sec-11

Impedance (阻抗) 40，46，50 Inertance (声感) 46，59 Associated compliance\~(相连空腔的声感) 67 \~example (声感的例子) 46，48，63 Interface condition (接口条件) 131

### J

^sec-12

Jet (引射器) 141，147Joint condition (连接条件) 131

### L

^sec-13

Lagrangian and Eulerian viewpoints (拉格朗日和欧拉观点) 53 Linear motor-alternator (线性电动机-发电机) 184，199 Liquid-piston (液体活塞发动机) 10 Lost work (损失功) 97 Loudspeaker (扬声器) 184，99

### M

^sec-14

Mass flow (质量流出) 138Mass-flux density (质量流密度) 13，138，143Measurements (测量) 193

Mechanical impedance (机械阻抗) 187 Minor loss (微损失) 126 Momentum equation (动量方程) 115 Acoustic\~ (声学动量方程) 44，46，45 Inviscid acoustic\~ (无粘声学动量) 11，38 Thermoacoustic\~(热声学动量方程) 55，59

### N

^sec-15

Navier-Stokes (N-S)Nonlinear acoustics (非线性声学) 115，184Notation (记号) 27Numerical integration (数值积分) 29，90，223

### O

^sec-16

Orifice pulse-tube refrigerator (小孔脉冲管制冷机) \~extended example (延伸例子) \~acoustic power (声功) 81，92 \~acoustic-impedance network (声阻抗网络)46，52，77，78，181 \~animation (动画) 81，107 \~exergy (阻抗图) 66 \~impedance diagram (测量) 211 \~orifice resistance (小孔阻力) 46 \~overview (观点) 147 \~pulse tube (脉冲管) 21，66，92，107 \~Rayleigh streaming (瑞利声流) 147 \~regenerator (回热器) 81 \~thermal-relaxation resistance (热驰豫阻力) 52 \~total power (总功) 92 Penetration depth (穿透深度) 15 \~animation (穿透深度动画) 45，49，53，69 Phase (相位) 27 Phasors (相图) 28 Pitfall (易犯的错误) 23 Porous media (多孔介质) 117，172

Power (功率)Prantl (普朗特数) 15Pressure transducer (压力传感器) 194Pressure vessel (压力容器) 183Prime mover (原动机) 7Pulse tube (脉冲管) 89，131，147，180\~streaming (脉冲管中的声流) 137\~tapered (锥形的脉冲管) 143

### Q

^sec-17

Quality factor (品质因子) 94，190

### R

^sec-18

Refrigerator (制冷机) 7Regenerator (回热器) 80，117，166，172Stacked-screen\~ (丝网填充的回热器) 58，118Resonator (谐振器) 37，68，181\~example (例子) 63Half-wavelength\~ (半波长的谐振器) 43Helmholtz\~ (亥姆豁兹谐振器) 40Reynolds number (雷诺数)Acoustic\~ (声学雷诺数) 118DC-flow\~ (直流雷诺数) 120

### S

^sec-19

Safety (安全) 183 Scale model (比例模型) 161 Screen (丝网) 117，172 Second law of thermodynamics (热力学第二定律) 7 Shock wave (激波) 158 Source/sink, volume-flow-rate (源/汇，体积流率) 60，76 Spatial average (空间平均) 45，56 Specific acoustic impedance (比声阻) 69

Specific heat (比热) 15Speed of sound (声速) 13Stack (热声堆) 82，166Standing-wave engine (驻波发动机) 54，82\~animation (动画) 82\~extended example (扩展例)\~acoustic power (声功) 83，91\~DetaE file (DeltaE 文件) 223\~exergy (无用能) 107\~heat exchanger (热交换器) 176，178\~impedance diagram (阻抗图) 63\~measurement (测量) 204\~overview (小结) 18，63，107\~resonator (谐振管) 45，51，125，129，181，184\~stack (热声堆) 63，83，168\~thermal-relaxation resistance (热驰豫阻力) 51，78\~total power (总能量) 91Standing-wave refrigerator (驻波制冷机) 54，83\~animation (动画) 83\~extended example (扩展例)\~DeltaEfile (DeltaE 文件) 226\~impedance diagram (阻抗图) 66\~measurements (测量) 205\~overview (小结) 18，66，154\~resonator (谐振管) 42，48，184\~resonator resistance (谐振管阻力) 77\~stack (热声堆) 170Stirling engine (斯特林发动机) 8Streaming (声流) 137Gedeon\~ (Gedeon 声流) 138, 196Jet-driven\~(引射驱动的声流) 147Rayleigh\~ (瑞利声流) 143, 196Regenerator\~ (回热器中的声流) 137，148Surface roughness (表面粗糙度) 121

### T

^sec-20

Thermal buffer tube (热缓冲管) 89，131，147，180 \~streaming (热缓冲管中的声流) 137 Thermal conductivity (热导率) 15，56 Thermal expansion coefficient (热膨胀系数) 34 Thermal-relaxation resistance (热驰豫阻力) 51,60,76,77,102,106 \~example (热驰豫阻力的例子) 51，52，78 Thermoacoustic engine and refrigerator (热声发动机和制冷机) 32 Thermoacoustic-Stirling heat engine (热声斯特林发动机) 11 \~animation (动画) 66 \~extended example (扩展的例子) \~acoustic power (声功) 80 \~DeltaE file (DeltaE 文件) 230 \~Gedeon streaming (Gedeon 声流) 143 \~heat exchanger (热交换器) 177 \~impedance diagram (阻抗图) 65 \~interface (界面) 182 \~joining condition (连接条件) 137 \~measurements (测量) 207 \~overview (小结) 20，65 \~regenerator (回热器) 129，184 \~resonator (谐振管) 129，184 Thermocouples (热电偶) 196 Thermal-viscous function (热粘函数) 56 Time average of a product (乘积的时均值) 67 Total power (总功) 116 Transducer, electroacoustic (传感器，电声的) 184，199 Total power (总功) 116 Temperature (温度) 196 Traveling-wave engine (行波发动机) Traveling-wave refrigerator (行波制冷机) Turbulence (湍流) 120，125

### V

^sec-21

Valve floe impedance (阀门流动阻力) 128

Viscous (粘性) 15，55

Viscous resistance (粘性阻力) 46,59,76,102,120 \~example (粘性阻力的例子) 48,63,77

Volume flow rate (体积流率) 37

Volume velocity (体积速度) 37

Wave equation (波动方程) Lossless\~ (无损失的波动方程) 13 Rott’s\~ (Rott 的波动方程) 13，58

Wavelenghth (波长) 14

Waves (波) 11，28，37，75

Wavevectors (波矢) 28，

### W

^sec-22

Website (网址) 6，31

Work (功) 7，84

## 参考文献

^sec-23

[1] R. S. Reid, W. C. Ward, and G. W. Swift. Cyclic thermodynamics with open flow. Phys. Rev. Lett., 80:4617-4620, 1998.

[2] G. W. Swift and P. S. Spoor. Thermal diffusion and mixture separation in the acoustic boundary layer. J. Acoust. Soc. Am., 106:1794-1800, 1999.

[3] L. E. Kinsler, A. R. Prey, A. B. Coppens, and J. V. Sanders. Fundamentals of Acoustics. John Wiley and Sons, 1982.

[4] G. J. Van Wylen and R. E. Sonntag. Fundamentals of Classical Thermodynamics. Wiley, 1965.

[5] E. Kreyszig. Advanced Engineering Mathematics. Wiley, 1979.

[6] H. B. Callen. Thermodynamics and an Introduction to Thermostatistics. Wiley, 1985.

[7] P. M. Morse. Thermal Physics. Benjamin, 1969.

[8] G. Walker. Stirling Engines. Clarendon, Oxford, 1960.

[9] G. Walker. Cryocoolers. Plenum, New York, 1983.

[10] Ivo Kolin. The Evolution of the Heat Engine. Longman, London, 1972.

[11] J. R. Senft. Ringbom Stirling Engines. Oxford University Press, 1993.

[12] I. Urieli and D. M. Berchowitz. Stirling Cycle Engine Analysis. Adam Hilger, Bristol UK, 1984.

[13] C. D. West. Liquid Piston Stirling Engines. Van Nostrand Reinhold, 1983.

[14] P. H. Ceperley. A pistonless Stirling engine-the traveling wave heat engine. J. Acoust. Soc. Am., 66:1508-1513, 1979.

[15] P. H. Ceperley. Gain and efficiency of a short traveling wave heat engine. J. Acoust. Soc. Am., 77:1239\~-1244, 1985.

[16] A. D. Pierce. Acoustics: An Introduction to Its Physical Principles and Applications. Acoustical Society of America, Woodbury, New York, 1989.

[17] N. Rott. Damped and thermally driven acoustic oscillations in wide

and narrow tubes. Z. Angew. Math. Phys., 20:230-243, 1969.

[18] N. Rott. Thermoacoustics. Adv. Appl. Mech., 20:135-175, 1980. and references therein.

[19] K. M. Godshalk, C. Jin, Y. K. Kwong, E. L. Hershberg, G. W. Swift, and R. Radebaugh. Characterization of 350 Hz thermoacoustic driven orifice pulse tube refrigerator with measurements of the phase of the mass how and pressure. Adv. Cryogenic Eng., 41:1411-1418, 1996.

[20] S. Backhaus and G. W. Swift. A thermoacoustic-Stirling heat engine. Nature, 399:335338, 1999.

[21] S. Backhaus and G. W. Swift. A thermoacoustic-Stirling heat engine: Detailed study. submitted to J. Acoust. Soc. Am., ??:??, 1999?

[22] Cryenco manufactures large-scale cryogenic hardware, such as cryogenic tank trucks, storage tanks, and cryogenic vessels for MRI systems. 3811 Joliet, Denver CO 80239.

[23] G. W. Swift. Thermoacoustic natural gas liquefier. 1997. In proceedings of the DOE Natural Gas Conference, Houston TX, March 1997. Also available at http://lib-www.lanl.gov/la-pubs/00412 750.pdf.

[24] W. C. Ward and G. W. Swift. Design environment for low amplitude thermoacoustic engines (DeltaE). J. Acoust. Soc. Am., 95:3671-3672, 1994. Fully tested software and user's guide available from Energy Science and Technology Software Center, US Department of Energy, Oak Ridge, Tennessee. To review DeltaE's capabilities, visit the Los Alamos thermoacoustics web site at www.lanl.gov/thermoacoustics/. For a beta-test version, contact www.lanl.gov (Bill Ward) or swift.lanl.gov (Greg Swift) by email.

[25] D. Gedeon. A globally implicit Stirling cycle simulation. In Proceedings of the 2\~st Intersociety Energy Conversion Engineering Conference, page 550. American Chemical Society, 1986.

[26] A. Tominaga, Institute of Physics, University of Tsukuba, Tsukuba 305, Japan.

[27] J. Gary, A. O'Gallagher, and R. Radebaugh. A numerical model for regenerator performance. Technical report, NIST-Boulder, 1994. Also known as REGEN 3.1 Users Guide.

[28] W. P. Amott, H. E. Bass, and R. Raspet. General formulation of thermoacoustics for stacks having arbitrarily shaped pore cross sections. J. Acoust. Soc. Am., 90:32283237, 1991.

[29] E. S. Jeong and J. L. Smith. An analytic model of heat transfer with oscillating pressure. In M. Jensen, R. Mahajan, E. McAssey, M. F. Modest, D. Pepper, M. Sohal, and A. Lavine, editors, General Papers in Heat Transfer, pages 97-104, 1992. ASMEHTD, Vol. 204.

[30] L. D. Landau and E. M. Lifshitz. Fluid Mechanics. Pergamon, 1982.

[31] R. W. Fox and A. T. McDonald. Introduction to Fluid Mechanics. Wiley, 1985.

[32] A. Bejan. Entropy Generation Minimization: The Method of Thermodynamic Optimization of Finite-Size Systems and Finite-Time Processes. CRC press, 1995.

[33] A. Bejan. Advanced Engineering Thermodynamics, Wiley, second edition, 1997.

[34] P. M. Morse and K. U. Ingard. Theoretical Acoustics. McGraw-Hill, 1968.

[35] A. Tominaga. Fundamental Thermoacoustics. ISBN4-7536-5079-0, 1998. In Japanese.

[36] G. W. Swift. Thermoacoustic engines. J. Acoust. Soc. Am., 84:1145-1180, 1988.

[37] G. W. Swift. Thermoacoustic engines and refrigerators. Physics Today, pages 22-28, July 1995.

[38] G. W. Swift. Encyclopedia of Applied Physics, volume 21, chapter Thermoacoustic engines and refrigerators, pages 245-264. Wiley, for American Institute of Physics, 1997.

[39] A. J. Organ. Thermodynamics and Gas Dynamics of the Stirling Cycle Machine. Cambridge University Press, 1992.

[40] R. Radebaugh. A review of pulse tube refrigeration. Adv. Cryogenic Eng., 35:1191 1205, 1990.

[41] P. P. Steijaert. Thermodynamical aspects of pulse-tube refrigerators. Ph.D thesis, Technische Universiteit Eindhoven (Netherlands), 1999.

[42] G. Walker, L. Bauwens, and E. Bingham. Pulse-tube refrigerators: An introduction. ??, 1996. Available through Stirling Machine World, stirmach@juno.com.

[43] G. W. Swift and R. M. Keolian. Thermoacoustics in pin-array stacks. J. Acoust. Soc. Am., 94:941-943, 1993.

[44] G. W. Swift and W. C. Ward. Simple harmonic analysis of regenerators. J. Thermophysics and Heat Transfer, 10:652-g62, 1996.

[45] W. M. Kays and A. L. London. Compact Heat Exchangers. McGraw-Hill, New York, 1964.

[46] M. Greenspan and F. N. Wimenitz. An acoustic viscometer for gases--I. Technical report, US National Bureau of Standards (now known as National Institute of Standards and Technology), 1953. NBS Report 2658.

[47] G. Huelsz and E. Ramos. On the phase difference of the temperature and pressure waves in the thermoacoustic effect. Int. Comm. Heat Mass Transfer, 22:71-80, 1995.

[48] P. Merkli and H. Thomann. Thermoacoustic effects in a resonance tube. J. Fluid Mech., 70:161-177, 1975.

[49] H. Thomann. Acoustical streaming and thermal effects in pipe how with high viscosity. Z. Angew. Math. Phys, 27:709, 1976.

[50] N. Rott. Thermally driven acoustic oscillations, part III: Second-order heat Aux. Z. Angew. Math. Phys., 26:43, 1975.

[51] R. C. Tolman and P. C. Fine. On the irreversible production of entropy. Rev. Mod. Phys., 20:51-77, 1948.

[52] J. C. Wheatley, T. Hofler, G. W. Swift, and A. Migliori. An intrinsically irreversible thermoacoustic heat engine. J. Acoust. Soc. Am., 74:153-170, 1983.

[53] A. Migliori and G. W. Swift. Liquid sodium thermoacoustic engine. Appl. Phys. Lett., 53:355-357. 1988.

[54] G. W. Swift, D. L. Gardner, and S. Backhaus. Acoustic recovery of lost power in pulse tube refrigerators. J. Acoust. Soc. Am., 105:711-724, 1999.

[55] A. T. A. M. de Waele, P. P. Steijaert, and J. Gijzen. Thermodynamical aspects of pulse tubes. Cryogenics, 37:313-324, 1997.

[56] A. T. A. M. de Waele, P. P. Steijaert, and J. J. Koning. Thermodynamical aspects of pulse tubes II. Cryogenics, 38:32\~335, 1998.

[57] M. A. Lewis, T. Kuriyama, F. Kuriyama, and R. Radebaugh. Measurement of heat conduction through stacked screens. Adv. Cryogenic Eng., 43:1611-1618, 1998.

[58] R. Yaron, S. Shokralla, J. Yuan, P. E. Bradley, and R. Radebaugh. Etched foil regenerator. Adv. Cryogenic. Eng., 41:1339-1346, 1996.

[59] J. R. Womersley. Method for the calculation of velocity, rate of flow, and viscous drag in arteries when the pressure gradient is known. J. Physiology, 127:553-563, 1955.

[60] M. Iguchi, M. Ohmi, and K. Maegawa. Analysis of free oscillating flow in a U-shaped tube. Bull. JSME, 25:1398, 1982.

[61] U. H. Kurzweg, E. R. Lindgren, and B. Lothrop. Onset of turbulence in oscillating flow at lo7N Womersley number. Phys. Fluids A, 1:1972-1975, 1989. and references therein.

[62] S. M. Hino, M. Sawamoto, and S. Takasu. Experiments on transition to turbulence in an oscillatory pipe flow. J. Fluid Mech., 75:193-207, 1976.

[63] M. Ohmi and M. Iguchi. Critical Reynolds number in an oscillating pipe flow. Bulletin of the JSIME, 25:165, 1982.

[64] M. Ohmi, M. Iguchi, K. Kakehashi, and M. Tetsuya. Transition to turbulence and velocity distribution in an oscillating pipe flow. Bulletin of the JSME, 25:365, 1982.

[65] M. Ohmi, M. Iguchi, and I. Urahata. Flow patterns and frictiona losses in an oscillating pipe flow. Bull. JSME, 25:536-543, 1982.

[66] J. R. Olson and G. W. Swift. Acoustic streaming in pulse tube refrigerators: Tapered pulse tubes. Cryogenics, 37:769-776, 1997.

[67] G. W. Swift, M. S. Alien, and J. J. Wollan. Performance of a tapered pulse tube. In R. G. Ross Jr., editor, Cryocoolers 11, pages 315-320. Plenum, New York, 1999.

[68] V. L. Streeter. Handbook of Fluid Dynamics. McGraw-Hill, 1961.

[69] I. E. Idelchik. Handbook of Hydraulic Resistance. Begell House, New York, 3rd edition, 1994.

[70] M. Hino, M. Kashiwayanagi, A. Nakayama, and T. Hara.--Experiments on the turbulence statistics and the structure of reciprocating oscillatory flow. J. Fluid Mech., 131:363-400, 1983.

[71] A. S. Worlikar and 0. M. Knio. Numerical simulation of a thermoacoustic refrigerator I: Unsteady adiabatic flow around the

stack. J. Comp. Phys., 127:424-451, 1996.

[72] A. S. Worlikar, O. M. Knio, and R. Klein. Numerical simulation of a thermoacoustic refrigerator II: Stratified flow around the stack. J. Comp. Phys., 144:299-324, 1998.

[73] N. Cao, J. R. Olson, G. W. Swift, and S. Chen. Energy flux density in a thermoacoustic couple. J. Acoust. Soc. Am., 99:3456-3464, 1996.

[74] P. J. Storch, R. Radebaugh, and J. E. Zimmerman. Analytical model for the refrigeration power of the orifice pulse tube refrigerator. Technical note 1343, National Institute of Standards and Technology, 1990.Conference, pages 5.529-5.532. Society of Automotive Engineers, 1992.

[75] G. W. Swift. Analysis and Performance of a Large Thermoacoustic Engine, J.Acoust. Soc. Am., 92,1552-1563,1992

[76] N. Rott and G. Zououlas. Thermally Driven Acoustic Oscillation: Tube with variable cross section. Z. Angew. Math. Phys. 27,197-224,1976

[77] J. L. Smith and M. Romm. Thermodynamic Loss at Component Interface in Stirling Cycle. In Proceedings of $2 7 ^ { \mathrm { t h } }$ Intersociety of Energy Conversion Engineering Conference. Page 5:529-532. Society of Automotive Engineer, 1992.

[78] P. Kittel. Temperature profile within pulse tubes. Adv. Cryogenic Eng., 43:1927-1932, 1998.

[79] L. Bauwens. Interface loss in the small amplitude orifice pulse tube model. Adv. Cryogenic. Eng., 43:1933-1940, 1998.

[80] M. J. Romm and J. L. Smith. Stirling engine loss in dead volumes between components. In Proceedings of the 28th Intersociety Energy Conversion Engineering Conference, pages 751-758, 1993.

[81] G. W. Swift. A Stirling engine with a liquid working substance. J. Appl. Phys., 65:4157-4172, 1989.

[82] W. L. h/l. Nyborg. Acoustic streaming. In W. P. Mason, editor, Physical Acoustics, Volume IIB, pages 265-331. Academic Press, 1965.

[83] David Gedeon. DC gas flows in Stirling and pulse-tube cryocoolers. In R. G. Ross, editor, Cryocoolers 9, pages 385-392. Plenum, New York, 1997.

[84] C. Wang, G. Thummes, and C. Heiden. Effects of DC gas flow on performance of two-stage 4 K pulse tube coolers. Cryogenics, 38:689-695, 1998.

[85] Lord Rayleigh. Theory of Sound. Dover, New York, 1945. Section 352.

[86] J. R. Olson and G. W. Swift. Suppression of acoustic streaming in tapered pulse tubes. In R. G. Ross Jr., editor, Cryocoolers 11, pages 307-313. Plenum, New York, 1999.

[87] S. Zhu, P. Wu, and Z. Chen. Double inlet pulse tube refrigerators: An important improvement. Cryogenics, 30:514, 1990.

[88] C. E. Bradley. Acoustic streaming field structure: The influence of the radiator. J. Acoust. Soc. Am., 100:1399-1408, 1996.

[89] X. Zhao, Z. Zhu, and G. Du. A note about acoustic streaming: Comparison of C. E. Bradley's and W. L. Nyborg's theories. J. Acoust. Soc. Am., 104:583-584, 1998.

[90] J. M. Lee, P. Kittel, K. D. Timmerhaus, and R. Radebaugh. Flow patterns intrinsic to the pulse tube refrigerator. In Proceedings of the rth International Cryocooler Conference, page 125, Kirtland AFB, NM 87117-5776, 1993. Phillips Laboratory. Phys, 25:417, 1974.

[91] N.Rott. The Influence of Heat Conduction on Acoustic Streaming. Z. Angew. Math. Phys. 25:417,1974.

[92] C. S. Kirkconnell. Experimental investigation of a unique pulse tube expander design. In R. G. Ross Jr., editor, Cryocoolers 10, pages 239-247. Plenum, New York, 1999.

[93] V. Kotsubo, P. Huang, and T. C. Nast. Observation of DC flows in a double inlet pulse tube. In R. G. Ross Jr., editor, Cryocoolers 10, pages 299-305. Plenum, New York, 1999.

[94] R. S. Reid. ?? Ph.D. thesis, Georgia Institute of Technology, Department of Mechanical Engineering, 1999. Almost complete, as of June 1999.

[95] B. Zinn. Pulsating combustion. In F. J. Weinberg, editor, Advanced Combustion Methods, pages 113-181. Academic, London, 1986.

[96] C. C. Lawrenson, B. Lipkens, T. S. Lucas, D. K. Perkins, and T. W. Van Doren. Measurements of macrosonic standing waves in oscillating closed cavities. J. Acoust. Soc. Am., 104:623-636, 1998.

[97] Y. Il'inskii, B. Lipkens, T. Lucas, T. W. Van Doren, and E;. Zabolotskaya. Nonlinear standing waves in an acoustical resonator. J. Acoust. Soc. Am., 104:2664-2674, 1998.

[98] E. Buckingham. On physically similar systems: Illustrations of the use of dimensional equations. Phys. Rev., 4:345, 1914. See also any introductory fluid mechanics textbook.

[99] J. R. Olson and G. W. Swift. Similitude in thermoacoustics. J. Acoust. Soc. Am., 95:1405-1412. 1994.

[100] F. Reif. Fundamentals of Statistical and Thermal Physics. McGraw-Hill, 1965.

[101] F. W. Giacobbe. Estimation of Prandtl numbers in binary mixtures of helium and other noble gases. J. Acoust. Soc. Am., 96:3568-3580, 1994.

[102] S. L. Garrett, D. K. Perkins, and A. Gopinath. Thermoacoustic refrigerator heat exchangers: Design, analysis, and fabrication; In G. F. Hewitt, editor, Heat Transfer 1994: Proc. 10th Int. Heat Transfer Conf., pages 375-380. Inst. Chem. Eng., Rugby UK, 1994.

[103] C. Wang, G. Thummes, and C. Heiden. Experimental study of staging method for two-stage pulse tube refrigerators for liquid 4He temperatures. Cryogenics, 37:857-863, 1997.

[104] T. J. Hofler. Thermoacoustic refrigerator design and performance. Ph.D. thesis, Physics department, University of California, San Diego, 1986.

[105] T. J. Hofler. Concepts for thermoacoustic refrigeration and a practical device. In Chairman Paul Lindquist, editor, Proceedings of the 5th International Cryocoolers Conference, pages 93-101, Wright-Patterson AFB, OH, August 1988. Wright-Patterson Air Force Base. Monterey, California.

[106] \~laster's thesis, US Naval Postgraduate School, Monterey CA, 1996.

[107] lllllll

[108] M. S. Reed and T. J. Hofler. Measurements with wire mesh stacks in thermoacoustic prime movers. J. Acoust. Soc. Am., page 2559, 1996.

[109] J. A. Adeff, T. J. Hofler, A. A. Atchley, and W. C. Moss. Measurements with reticulated vitreous carbon stacks in

thermoacoustic prime movers and refrigerators. J. Acoust. Soc. Am., 104:32-38, 1998.

[110] J. Bijsel, Ch. Trepp, and F. Fourie. An alternative stack arrangement for thermoacoustic heat pumps and refrigerators. J. Acoust. Soc. Am., 106:707-715, 1999.

[111] J. Bosel. Unterszlchungen zllr Erhiihzlng der Leistungsdichte thermoalcustischer Maschinen. PhD thesis, Swiss Federal Institute of Technology, 1998. Dissertation ETH 12530.

[112] W. A. Marrison. U.S. Patent No. 2,836,033 (1958).

[113] D. Gedeon and J. G. Wood. Oscillating-flow regenerator test rig: Hardware and theory with derived correlation for screens and felts. Technical Report 198442, NASA Lewis Research Center, 1996.

[114] J. Gerster, J. Krause, S. Wunderlich, L. Doerrer, F. Schmidl, R. Weidl, M. Thiirk, and P. Seidel. Operation of a high-T, SQUID gradiometer in a nonmetallic one-stage pulse tube cryocooler. In Book Abstracts of the Low Power Cryocooler III Workshop, 3\~ May - 2 June 1999, Venlo, The Netherlands, page 27, 1999.

[115] W. Rawlings, K. D. Timmerhaus, R. Radebaugh, and D. E. Daney. Measurement of performance of a spiral wound polyamide regenerator in a pulse tube refrigerator. In R. W. Fast, editor, Advances in Cryogenic Engineering, page 947. Plenum, New York, 1992.

[116] Mitchell Stirling, Berkeley CA.

[117] F. P. Incropera and D. P. DeWitt. Introduction to Heat Transfer. Wiley, 2nd edition, 1990.

[118] W. M. Rohsenow, J. P. Hartnett, and Y. I. Cho. Handbook of Heat Transfer. McGraw Hill, 1998.

[119] T. W. Simon and J. R. Seume. A survey of oscillating flow in Stirling engine heat exchangers. Technical Report 182108, NASA Lewis Research Center, 1988.

[120] Progressive Technology, Auburn CA.

[121] E. F. hlegyesy. Pressure Vessel Handbook. Pressure Vessel Handbook Publishing Inc., Tulsa, Oklahoma, ninth edition, 1992.

[122] Ht.H:\~Bednar,Pressure Vessel Design Handbook. Van Nostrand Reinhold, New Yor gineers. ASME Boiler and Pressure Vessel Code. American Society of Mechanical Engineers, New York,

1998.

[123] llll

[124] D. F. Gaitan and A. A. Atchley. Finite-amplitude standing waves in harmonic and anharmonic tubes. J. Acoust. Soc. Am., 93:2489-2495, 1993.

[125] A. B. Coppens and J. V. Sanders. Finite-amplitude standing waves within real cavities. J. Acoust. Soc. Am., 58:1133-1140, 1975.

[126] W. P. Arnott, J. A. Lightfoot, R. Raspet, and H. Moosmiiller. Radial wave thermoacoustic engines: Theory and examples for refrigerators and high-gain narrow bandwidth photo-acoustic spectrometers. J. Acoust. Soc. Am., 99:734-745, 1996.

[127] J. A. Lightfoot, W. P. Arnott, H. E. Bass, and R. Raspet. Experimental study of a radial mode thermoacoustic prime mover. J. Acoust. Soc. Am., 105:2652-2662, 1999.

[128] J. A. Corey and G. A. Yarr. HOTS.to WATTS: The LPSE linear alternator system re-invented. In Proceedings of the 27th Intersociety Energy Conversion Engineering Conference, pages 5.289-5.294, Warrendale PA, 1992. Society of Automotive Engineers. No editor; general chairman Buryl McFadden.

[129] A. K. de Jonge and A. Sereny. Analysis and optimization of a linear motor for the compressor of a cryogenic refrigerator. Adv. Cryogenic Eng., 27:631-640, 1982.

[130] R. S. Wadceland. Use of electrodynamic drivers in thermoacoustic refrigerators. J. Acoust. Soc. Am., ??:??, 1999. (submitted).

[131] L. Marton and C. Marton, Editors in Chief. Methods of Experimental Physics: Fluid Dynamics, volume 18. Academic Press, 1981.

[132] L. L. Beranek. Acoustic Measurements. Wiley, 1949.

[133] Jacob Fraden. A\~P Handbook of Modern Sensors: Physics, Designs, and Applications. American Institute of Physics, New York, 1993.

[134] P. R. Bevington. Data Reduction and Error Analysis for the Physical Sciences. McGraw-Hill, 1969.

[135] Endevco, San Juan Capistrano, California.

[136] Ray Radebaugh, personal communication.

[137] Omega Engineering, Stanford Connecticut. www.omega.com.

[138] A. M. Fusco, W. C. Ward, and G. W. Swift. Two-sensor power measurements in lossy ducts. J. Acoust. Soc. Am., 91:2229-2235, 1992.

[139] T. J. Hofler. Accurate acoustic power measurements with a high-intensity driver. J. Acoust. Soc. Am., 83:777-786, 1988.

[140] J. L. Martin, J. A. Corey, and C. hi. Martin. A pulse tube cryocooler for telecommunications applications. In R. G. Ross, editor, Cryocoolers 11, pages 181-189. Plenum, 1999.

---

[[热声学_统一方法_Swift著_罗二仓译|教程入口]] · [[Swift热声学_07_测量|上一部分]]
