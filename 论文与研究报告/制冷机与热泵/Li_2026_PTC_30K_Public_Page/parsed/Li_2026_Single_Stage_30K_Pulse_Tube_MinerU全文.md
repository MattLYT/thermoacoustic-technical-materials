---
title: Li_2026_Single_Stage_30K_Pulse_Tube · MinerU全文
record_role: machine-transcription
parse_method: MinerU
source_sha256: 905ed2b736e39b02db33a928997260d102c8d7fc7ee37bd0352956d3c1998dbf
source_pages: 6
---

# 单级 30 K 低温脉管制冷机的性能优化研究

李严恩 <sup>1,2</sup>，王乃亮 <sup>1\*</sup>，潘明涛 <sup>1,2</sup>，高海朋 <sup>1</sup>，张钰红 <sup>1</sup>，赵密广 <sup>1,2</sup>，王国鹏 <sup>1,2</sup>

（1.中国科学院理化技术研究所  低温科学与技术全国重点实验室，北京 100190；2.中国科学院大学，北京 101408）

摘要：高性能红外探测器（特别是长波红外 HgCdTe探测器）需要深低温以抑制自身的热噪声，提高信噪比和探测灵敏度。30 K脉管制冷机的低振动特性对于空间望远镜、卫星侦察和精确制导等需要极高成像稳定性的平台至关重要。以往为了在 30 K获得制冷量，通常采用两级脉管制冷机。而两级结构带来了相对复杂的结构以及更大的质量，所以单级 30 K高效脉管制冷机的研究对空间长波红外探测器的高效性能具有重要意义。论文介绍了一台单级同轴型脉管制冷机的研制，探究了惯性管和频率对该制冷机性能的影响。在数值计算中，发现惯性管的增长，能够增大制冷机整机中的质量流-压力波的相位差，而频率的增加也能带来类似的整机相位增加的结果，说明通过同时调节惯性管和频率，能够使得制冷机内相位合适的同时，制冷机整机也能工作在一个损失更小的频率。另外，实验中使用双向进气结构使得制冷机获得了更低的温度。在150 W输入电功的条件下，在30 K和40 K能够得到的制冷量分别为1.2 W和2.3 W，相对卡诺效率分别为7%和9.7%。

关键词：30 K脉管制冷机；惯性管；双向进气

中图分类号：TB651<sup>+</sup>.4

文献标志码：A

文章编号：1006-7086（2026）04-0385-06

DOI：10.12446/j.issn.1006-7086.2026.04.005

# Performance Optimization of a Single-stage 30 K Cryogenic Pulse Tube Cryocooler

LI Yanen <sup>1,2</sup>，WANG Nailiang <sup>1\*</sup>，PAN Mingtao <sup>1,2</sup>，GAO Haipeng <sup>1</sup>，ZHANG Yuhong <sup>1</sup>，ZHAO Miguang <sup>1,2</sup>，WANG Guopeng <sup>1</sup> ,2 （1. State Key Laboratory of Cryogenic Science and Technology，Technical Institute of Physics and Chemistry， CAS，Beijing 100190，China；2. University of Chinese Academy of Sciences，Beijing 101408，China）

Abstract：High-performance infrared detectors—particularly long-wave infrared (LWIR) HgCdTe detectors— require lower temperatures to suppress intrinsic thermal noise，thereby enhancing the signal-to-noise ratio and detection sensitivity. For space telescopes，satellite reconnaissance，and precision-guided systems that demand extremely high imaging stability，the low-vibration characteristics of 30 K pulse tube cryocooler are of critical importance. Traditionally，two-stage pulse tube cryocoolers have been employed to achieve cooling power at 30 K. However， such two-stage configurations introduce structural complexity and additional weight. Therefore， the development of a single-stage， high-efficiency 30 K pulse tube cryocooler is of great significance for improving the performance and integration of spaceborne long-wave infrared detectors. In this study，we developed a single-stage coaxial pulse tube cryocooler and systematically investigated the effects of the inertance tube and operating frequency on its cooling performance. In numerical calculations，it was found that the increase in inertance tube length can increase the phase difference between the mass flow and the pressure in the whole refrigerator， and the increase in frequency can also bring about a similar increase. This shows that by adjusting the inertance tube and frequency at the same time，the phase in the refrigerator can be made appropriate，and the whole machine can also be made to work at a frequency with higher efficiency and less loss. Additionally，double inlet configuration was adopted to further reduce the no load temperature. With an input electrical power of 150 W，the PTC delivered a cooling capacity of 1.2 W at 30 K or 2.3 W at 40 K，corresponding to relative Carnot efficiencies of 7.0% and 9.7%，respectively.

Key words：30 K pulse tube cryocooler；inertance tube；double inlet

## 0 引言

空间红外探测器需要工作在低温条件下以降低自身的暗电流，保证其高分辨率和可靠性。当工作温度降低到 30 K的时候，能够有效降低热促隧穿产生的暗电流，为红外探测器芯片的更高性能提供保障<sup>[1]</sup>。

很多学者对 30 K脉管制冷机做出了很多研究，为了能够在 30 K获得制冷量并且高效工作，30 K脉管制冷机大多采用两级结构<sup>[2–7]</sup>。而对于空间使用的制冷机，两级脉管制冷机的结构相对于单级脉管制冷机会复杂很多，如何使用单级脉管制冷机在 30 K获得制冷量成为一个重要的研究方向。随着脉管制冷机技术的不断发展和成熟，单级脉管制冷机也能够达到低于 30 K的无负荷温度并且能够在 30 K获得一定制冷量。1995年，TRW报道了一台单级脉管制冷机<sup>[8]</sup>，该制冷机最低温达到了 29.2 K，能够在200 W输入电功率的情况下在 35 K提供 1 W的制冷量。2010 年，Yang 等<sup>[9]</sup> 在对 30 K 以下温度制冷机的研究中，在输入功率 250 W情况下获得了 26.1 K的最低温度；200 W的输入功率下，制冷机能够在35 K 提供 0.3～0.5 W 的制冷量。2018 年，Chen 等<sup>[10]</sup>在脉管制冷机中采用了多路旁通和双向进气的结构，在246 W的输入功率下得到了 15.5 K的最低温度，并且在 20 K 能得到 386 mW 的制冷量，在 30 K 能够得到 1.5 W的制冷量。在对填料结构改进后，在250 W输入功率的情况下，他们进一步得到了单级13.9 K的最低制冷温度，这是目前为止单级脉管制冷机报道的最低温度，该制冷机在 30 K有 0.8 W的制冷量<sup>[11]</sup>。2018 年，Liu 等<sup>[12]</sup> 研制出了一台单级最低温 24.4 K的脉管制冷机，并在 30 K得到 1 W 的制冷量。类似的，2021 年，Wang 等<sup>[13]</sup> 研制出了最低温23.7 K的单极脉管制冷机，该制冷机在热端温度为293 K 以及 150 W 输入电功率的情况下，在 30 K 能够得到 0.8 W的制冷量，相对卡诺效率为 4.6%。2024 年，Hui 等<sup>[14]</sup> 对使用主动活塞调相的 40 K 制冷机进行了研究，当制冷机的运行频率为 50 Hz、热端温度为 293 K ，以及输入功率为 307 W的时候，在35 K能够得到3 W的制冷量。

在目前研究的效率水平上，为了追求单级脉管制冷机在 30 K温度更高的效率，本文对单级 30 K脉管制冷机展开了研究，并在使用惯性管调相的基础上引入双向进气，以获得更低的制冷温度。在对惯性管调相性能的研究中，通过 Sage数值计算，以及针对制冷机惯性管和运行频率的实验，对惯性管和频率对制冷机性能的影响进行了探究。

## 1 实验与测试系统

脉管制冷机的实验测试示意图和实物图分别 如图1和图2所示。

![[mu_905ed2b7_c4834c6b57fe2eb8b268.jpg]]  
图1 脉管制冷机实验测试示意图  
Fig. 1 Schematic diagram of the PTC mode

![[mu_905ed2b7_6fcb3cd5ede39806909e.jpg]]  
图2 30 K脉管制冷机实物图  
Fig. 2 Photograph of the 30 K PTC

制冷机由四部分组成，包括压缩机、热端换热器、冷指和调相机构。压缩机为动圈式直线压缩机，活塞布置采用对置式结构。热端换热器需要带走制冷机产生的大部分热量，热端换热器采用铜制狭缝式换热器，在热端换热器的外部使用冷却水冷却，冷却水由冷水机组提供。制冷机冷指采用同轴式布置结构，回热器采用环形不锈钢丝网填充，冷端采用铜制狭缝式换热器，制冷量可从此处被取出利用。调相机构采用惯性管气库和双向进气结构，以得到更强的调相能力。

## 2 30 K脉管制冷机的性能优化

使用 Sage软件，计算不同频率和不同惯性管对制冷机性能的影响，并且通过实验测试不同频率下的制冷机性能，验证性能随惯性管和频率变化的规律。在实验中，通过对惯性管的优化实验来寻找实验条件下的最优惯性管，并且找到对应的最优频率。另外，在惯性管调相的基础上，为了使制冷机有更低的制冷温度，双向进气调相被用来优化制冷机的调相能力，以使得制冷机有更好的工作性能。通过这些优化实验，确定了制冷机的最优运行状态并对其进行了性能测试。

## 2.1 制冷机最优惯性管长度与最优频率

为了探究频率和惯性管对制冷机性能的影响，使用 Sage对制冷机在不同频率下的工况进行了数值模拟。图 3所示是制冷机内相位随着频率的变化关系。在一定范围内，可以看出压缩机出口的质量流-压力波相位差会随着频率升高而增大，频率的改变会改变制冷机内部的阻抗关系，从而改变整机的相位关系，另外，频率的改变会显著改变冷指与压缩机的阻抗匹配关系，造成压缩机出口相位的显著变化。对于单个部件分析，可以看到脉管中相位的变化会随着频率升高而更明显， 这是因为当频率升高后，脉管作为一个完全的空体积，其容性作用会增强，导致在脉管内质量流的相角变化会更剧烈。

![[mu_905ed2b7_e4b91d897a82372531c3.jpg]]  
图3 制冷机内相位随频率的变化  
Fig. 3 Phase variation inside the PTC with operating frequency

上述模拟探究了同一惯性管情况下制冷机内相位随频率的变化规律，为进一步探究制冷机内相位随惯性管的变化，模拟中分别采用管径 2 mm、3 mm 和 4 mm 的组合惯性管，通过改变 3 mm 惯性管的长度来探究不同长度惯性管对制冷机性能的影响。在模拟中分别采用了总长度 4 m、5 m和6 m的惯性管，在 36 Hz的操作频率下，不同惯性管下制冷机的整机相位如图 4所示。可以发现，在模拟的几组惯性管中，制冷机内的质量流-压力波相位都会整体升高。这说明，在一定范围内，在固定频率下调节惯性管，可以使制冷机内的整机相位趋向于最优分布。

![[mu_905ed2b7_cc1912caf89e8c50cd6a.jpg]]  
图4 不同惯性管长度下制冷机内相位关系的变化  
Fig. 4 Variation in the phase relationship inside the refrigerator under different inertance tube lengths

另外，制冷机在不同惯性管长度和不同频率下制冷性能如图 5所示，可以看出随着惯性管长度的减小，制冷机的最优频率会随之增大。而针对特定的惯性管，制冷机的 COP会随着制冷机频率的升高先升高后减小，存在最优频率使得制冷机在该惯性管条件下达到相对最优的性能。其中一个很重要的因素是随着频率的升高，惯性管的调相能力发生变化，并且惯性管的改变使得整机的阻抗分配变化，使得回热器内或者整机相位的分布发生改变，进而影响制冷机的性能。

![[mu_905ed2b7_8b10b7486777f30609af.jpg]]  
图5 不同惯性管情况下制冷机性能随频率的变化  
Fig. 5 Performance variation of the PTC with operating frequency under different inertance tubes

在上述模拟的基础上，实验中采用了相同的惯性管条件，输入电功率为 150 W，测量制冷机在制冷量为 2 W条件下的冷头温度，实验结果如图 6所示。在同样的惯性管长度下，随着制冷机频率的升高制冷机的冷头温度会先下降后上升，即存在最优频率使得制冷机能够达到更低的冷头温度。随着惯性管的长度增加，制冷机的最优频率会下降。这些实验规律都和模拟中得到的规律表现出了一致性。对三种惯性管组合下的制冷机性能进行了测试，得到如图 7所示的性能曲线。在单纯使用惯性管调相情况下，选择总长 5 m的惯性管能够达到更好的性能，并且实验条件下得到了 23.3 K的最低温。

通过上述的模拟和实验，能够发现在一定范围内，使用不同的惯性管之后，通过调节频率都可以使得制冷机内的相位达到一个相对合适的角度。但是这时不同惯性管对应的最优频率会随之变化，更长的惯性管对应着更低的最优频率，而制冷机设计的过程中，需要找到合适的频率，以达到压缩机和冷指更好的耦合特性，降低回热器内的总损失，所以就需要寻找到最优的惯性管，以匹配到制冷机

最优的运行频率。

![[mu_905ed2b7_2205195f111511c26dcd.jpg]]  
图6 不同惯性管情况冷头温度随频率的变化

Fig. 6 Variation of cold end temperature with operating frequency under different inertance tubes  
![[mu_905ed2b7_e6743aa9d3d74f62194b.jpg]]  
图7 不同惯性管情况下制冷机性能  
Fig. 7 Performance of the PTC under different inertance tubes

## 2.2 双向进气调相优化

在上述的实验基础上，引入了双向进气调相，在脉管的热端的壁面上开了一个小孔，这样就连通了脉管热端与回热器热端的气体，该小孔孔径为0.4 mm，之后测量了引入双向进气小孔的制冷性能。引入双向进气调相后，重新对惯性管进行了优化，以匹配双向进气的引入。经过实验得到的最优惯性管尺寸为： $\phi 2 { \times } 0 . 5 + \phi 2 . 5 { \times } 0 . 5 + \phi 3 { \times } 2 . 5 + \phi 4 { \times } 2 . 5 \nonumber$ 使用双向进气配合惯性管调相，与单纯使用惯性管性能对比如图8所示。可以看出，使用双向进气后，在相同功率下，制冷机能够得到的无负荷温度从23.3 K 降低到了 19.3 K，在 30 K 和 40 K 的制冷性能也得到了提升，30 K制冷量从 0.7 W提升到了1.2 W，40 K 的制冷量从 1.7 W 提升到了 2.3 W。使用惯性管与双向进气组合调相显著改善了制冷机在低温区的性能。

![[mu_905ed2b7_18c0c9da4c58467933f5.jpg]]  
图8 双向进气调相使用前后性能对比  
Fig. 8 Performance comparison of the PTC before and after using the double-inlet phase shifter

## 2.3 制冷机参数和性能

通过上述的优化，确定了制冷机的基本参数和操作条件，如表 1所列。在制冷机的性能测试中，如图 8所示，当制冷机的热端温度为 285 K，制冷机的输入功率为 150 W时，制冷机得到了 19.3 K的无负荷最低温度，并且在 30 K和 40 K能够分别获得 1.2 W 和

2.3 W的制冷量，相对卡诺效率分别为7%和9.7%。

表 1 30 K脉管制冷机的主要参数  
Tab. 1 Key parameters of the 30 K PTC
<table><tr><td>组件</td><td>参数</td><td>值</td></tr><tr><td rowspan="2"></td><td>活塞直径</td><td>25 mm</td></tr><tr><td>压缩机扫气体积/压比</td><td>9.6 mL/1.27</td></tr><tr><td rowspan="2">传输管</td><td>电功转化效率</td><td>约 84%</td></tr><tr><td>长度/直径</td><td>100 mm/6 mm</td></tr><tr><td rowspan="4">冷指</td><td>回热器长度</td><td>80 mm</td></tr><tr><td>回热器直径</td><td>25 mm</td></tr><tr><td>脉管直径</td><td>10.7 mm</td></tr><tr><td>丝网</td><td>500#不锈钢丝网，孔隙率0.613</td></tr><tr><td rowspan="4">调相机构</td><td></td><td>Φ2×0.5 + Φ2.5×0.5 +</td></tr><tr><td>惯性管直径和长度</td><td>Φ3×2.5 + Φ4×2.5</td></tr><tr><td>双向进气小孔直径</td><td>0.4 mm</td></tr><tr><td>充气压力</td><td>3MPa</td></tr><tr><td rowspan="2">操作条件</td><td></td><td></td></tr><tr><td>频率</td><td>36 Hz</td></tr></table>

分析实验中的测量误差，各参数的测量误差如表2所列。

表 2 实验仪器和测量误差  
Tab. 2 Experimental instruments and measurement errors
<table><tr><td>测量参数</td><td>测量仪器/传感器</td><td>测量值</td><td>误差</td></tr><tr><td>冷头温度</td><td>Lakeshare DT-670 二极管温度计</td><td>30 K</td><td>± 12 mK</td></tr><tr><td>制冷量</td><td>Keithley 2700</td><td>1.2 W</td><td>± 0.006 W</td></tr><tr><td>输入电功</td><td>GW GPM-8213 数字功率计</td><td>150 W</td><td>± 0.15 W</td></tr></table>

## 3 结论

本文通过 Sage软件对制冷机进行了数值计算和分析，模拟计算的结果表明，对于该制冷机，在特定的惯性管情况下，在一定范围内提高频率，可以使制冷机冷指内的质量流-压力波相位整体增大。另外，模拟计算的结果还表明惯性管长度的增长也会对该制冷机产生类似的相位改变效果，惯性管和频率都能改变制冷机内的相位，随着惯性管长度的增加，制冷机的最优频率下降，可以通过调节惯性管的长度，使得制冷机能够工作在设计的频率附近，以和压缩机有更好的负载匹配特性，并且回热器在该频率下损失更小。在惯性管调相的情况下，150 W的输入电功率能够得到 23.3 K无负荷温度。之后，引入了双向进气调相，制冷机的无负荷温度从23.3 K降低至 19.3 K，无负荷温度的降低表明在该制冷机中，双向进气结构的引入，大幅改善了该制冷机在低温区的制冷性能，并且制冷机在 30 K的制冷量由 0.7 W 提升到 1.2 W，40 K 的制冷量由1.7 W 提升到了 2.3 W，制冷机在 30 K 和 40 K 的相对卡诺效率分别为7%和9.7%。

## 参考文献：

KUKKONEN C A，SIRANGELO M N，CHEHAYEB R，et al.[1]Commercialization  of  quantum  well  infrared  photodetectorfocal plane arrays[J]. Infrared Physics & Technology，2001，42（3）：397−405.

REZAEI  M， JAFARIAN  A， KARDGAR  A. Numerical  in-[2]vestigation of real gas effects on a two-stage pulse tube cry-ocooler  performance[J]. International  Journal  of  Refrigera-tion，2017，82：106−118.

[3] PROUVÉ T，CHARLES I，LEENDERS H，et al. Progress on

30  K-50  K  two-stage  EM  PT  cold  finger  for  space  applica-tions[C]//Cryocoolers：Proceeding of International Cryocool-er Conference，2016，19：56−59.

YANG L. Investigation on a thermal-coupled two-stage Stir-[4]ling-type pulse tube cryocooler[J]. Cryogenics，2008，48（11/12）：492−496.

SUN D M，DIETRICH M，THUMMES G. High-power Stir-[5]ling-type pulse tube cooler working below 30 K[J]. Cryogen-ics，2009，49（9）：457−462.

CHARLES  I， COYNEL  A， DUVAL  J  M， et  al.  Develop-[6]ment  of a  two  stage  high  temperature  pulse  tube  cooler  forspace  applications[C]//Proceedings  of  the  15th  InternationalCryocooler Conference，2009：63−70.

GULLY  W  J， GLAISTER D  S， HENDERSHOTT  P， et  al.[7]Ball  aerospace  next  generation  two-stage  35  K  coolers： theSB235 and SB235E[C]//International Cryocooler Conference，2007：49−55.

BURT  W  W， CHAN  C  K.  Demonstration  of a  high  perfor-[8]mance 35 K pulse tube cryocooler[M]//ROSS R G. Cryocool-ers 8. Boston，MA：Springer US，1995：313−319.

[9] YANG L W，XUN Y Q，THUMMES G，et al. Single-stage

high frequency coaxial pulse tube cryocooler with base tem-perature below 30 K[J]. Cryogenics，2010，50（5）：342−346.

CHEN L，ZHOU Q，JIN H，et al. 386 mW/20 K single-stage[10]Stirling-type pulse tube cryocooler[J]. Cryogenics，2013，57：195−199.

ZHOU Q，CHEN L，ZHU X，et al. Development of a high-[11]frequency  coaxial  multi-bypass  pulse  tube  refrigerator  be-low 14 K[J]. Cryogenics，2015，67：28−30.

LIU S S，JIANG Z H，ZHANG A K，et al. Study on high[12]energy  efficiency  30  K  single-stage  pulse  tube  cryocoolerfor a space infrared detector[J]. Journal of Infrared and Milli-meter Waves，2018，37（4）：403−410.

WANG  N， ZHAO  M， CHEN  H， et  al.  24  K  single-stage[13]coaxial  pulse  tube  cryocooler  without  double-inlet  phaseshifter[Z]//Cryocoolers  21， ICC  Press  Boulder， CO， 2021：169−173.

HUI H，SONG J，YIN W，et al. An efficient high cooling-[14] capacity 40 K pulse tube refrigerator using an active dualpiston as phase shifter[J]. Energy，2024，286：129534.

（责任编辑：杨建斌）
