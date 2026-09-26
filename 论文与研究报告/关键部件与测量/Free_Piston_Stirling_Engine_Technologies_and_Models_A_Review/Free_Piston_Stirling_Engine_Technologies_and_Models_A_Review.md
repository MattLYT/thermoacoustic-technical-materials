---
record_category: "论文与研究报告/关键部件与测量"
source_id: "article:energies:2021:perozziello-fpse-review"
title: "Free-Piston Stirling Engine Technologies and Models: A Review"
authors:
  - "Carmela Perozziello"
  - "Lavinia Grosu"
  - "Bianca Maria Vaglieco"
year: 2021
doi: "10.3390/en14217009"
institution:
  - "Università degli Studi di Napoli Parthenope"
  - "University of Paris Nanterre"
  - "Consiglio Nazionale delle Ricerche"
engineering_type: "自由活塞 Stirling 技术及模型综述"
function_boundary: "构型、应用与一维/二维/CFD 模型梳理"
drive_chain: "外部热源→自由活塞 Stirling→直线发电机"
phase_control: "活塞—配气活塞质量弹簧系统与相位"
topology: "单作用、双作用、对置与串联构型"
evidence_grade: "开放获取全文页面；MinerU 全文转换；综述"
source_status: "MinerU-public-page-fulltext"
source_path: "https://www.mdpi.com/1996-1073/14/21/7009"
source_url: "https://www.mdpi.com/1996-1073/14/21/7009"
mineru_method: "crawl public full-text page"
---

Open Access Review

# Free-Piston Stirling Engine Technologies and Models: A Review

by

Carmela Perozziello

Lavinia Grosu

Bianca Maria Vaglieco

<sup>1</sup>

Dipartimento di Ingegneria, Università degli Studi di Napoli “Parthenope”, Centro Direzionale, Isola C4, 80143 Napoli, Italy

<sup>2</sup>

Laboratory of Energetic, Mechanic and Electromagnetism, LEME, University of Paris Nanterre, 50 Rue de Sèvres, 92410 Ville d’Avray, France

<sup>3</sup>

Istituto di Scienze e Tecnologie per l’Energia e la Mobilità Sostenibili, Consiglio Nazionale delle Ricerche, Via G. Marconi, 4, 80125 Napoli, Italy

<sup>*</sup>

Authors to whom correspondence should be addressed.

Energies 2021, 14(21), 7009; https://doi.org/10.3390/en14217009

Submission received: 8 September 2021/ Revised: 20 October 2021/ Accepted: 20 October 2021/ Published: 26 October 2021

(This article belongs to the Collection Women in Energy and Environment)
## Abstract

The Stirling engine is an alternative solution to produce cleaner energy in order to achieve the reduction of the fossil fuel consumption and the CO<sub>2</sub> emissions. It comprises an external combustion engine that can convert any external heat source into mechanical power, through cyclic expansion and compression of a working gas in a closed-regenerative cycle, with or without driving mechanisms. The free-piston Stirling Engine is significantly preferred because of the absence of any mechanical linkage resulting in longer operating life, lower noise pollution, maintenance and vibration free, self-starting and high thermal efficiency. The aim of this paper is to summarize the research works on the free-piston Stirling engine technologies and models. First, the working principles of the free-piston Stirling engine are described, identifying different configurations. Then, several applications are presented. Finally, a detailed review of the models available in literature is given, pointing out the main assumptions and equations.

Keywords:

free piston Stirling engine; applications; renewable energy; micro-CHP; modeling

![](https://pub.mdpi-res.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-ag-550.jpg?1635238722)

Graphical Abstract

## 1. Introduction

The search for alternative sources and sustainable energy production methods is the main target to protect the environment, to maintain natural resources over time reducing the fossil fuel consumption and to decrease the greenhouse gas emissions. In this scenario, the attention has been focused on new cleaner energy production systems based on renewable sources (e.g., solar, wood pellets) and waste heat recovery (i.e., to generate electricity from the lost heat power of the exhaust gas produced by combustion process). Besides the most popular technologies, such as solar photovoltaic and thermal collectors, wind turbines, fuel cells, cogeneration and tri-generation units, the Stirling Engine (SE) has emerged as a new promising technology for its energy source flexibility, low vibrations, operability in a wide range of temperatures, large application possibilities, good efficiency, easy maintenance and compact design [1, 2, 3, 4, 5]. It presents a closed-cycle regenerative heated externally engine that produces mechanical power through cyclic expansion and compression of a working gas (air, helium, nitrogen or hydrogen [6, 7, 8]) between a hot and a cold source named heater and cooler, respectively [9, 10]. The ideal cycle efficiency is equal to that of the Carnot cycle between the same temperatures, that is the maximum thermodynamic efficiency. However, the real thermal performance of the SE is lower than ideal efficiency because of several losses as heat transfer resistance, gas leakage and heat transfer between the sources [8]. Multitudinous heat sources can be used, such as solar [11], biogas [12], natural gas [13], wood pellets [14], waste energy [15] which give the SE a higher adaptability with respect to other energy conversion systems.

Based on the operational mechanisms, Stirling engines can be classified into crank-driven/kinematic and free-piston [16]. In the kinematic SE the variation of the working gas pressure is converted into mechanical power thanks to a connecting rod and crank-shaft system, which connects the alternate moving pistons e.g., the displacer and the working piston, inside the engine. The free-piston Stirling Engine (FPSE) replaces the crankshaft with an interior spring system attached to the respective displacer and working piston. By this way, there are no driving mechanisms and the pistons motion is only based on the variation of the working gas pressure. This results in longer operating life, lower noise pollution, maintenance and vibration free, self-starting and high thermal efficiency [16, 17]. For this reason, the FPSE technology is preferred for several applications, such as solar converters (dish Stirling) [18], cryocoolers [19] and micro combined heat and power (CHP) units. This last system allows to produce electricity and heat power simultaneously from the same energy source and it is available in small units (micro-CHP) for residential applications in the recent years [16, 20].

To analyze FPSE performance, one-dimensional (1D), two-dimensional (2D) computational fluid dynamics (CFD) models are widely used in research works. The thermodynamic equations used for SE analysis are combined with the dynamic relationships, in which the engine is simulated by a mass-spring-damper system. In fact, the thermodynamic analysis would not be sufficient to describe the dynamic behavior of FPSE because of springs dynamic characteristics [16]. Generally, the Newton’s second low is used to describe the motion of the working piston and the displacer, which is assumed harmonic. Most of the studies analyze the overall power output and thermal efficiency, considering the energy losses and the heat-exchangers effectiveness. The results are validated using different FPSE experimental data.

This paper aims to summarize some relevant research works on the Free-Piston Stirling Engines technologies and modeling approach. The general features of FPSE and its different operating configurations are described. Then, a presentation of the commercialized FPSEs for solar and micro-CHP applications are shown. The fundamental hypothesis and equations of the models found in literature are reported. Finally, the object of the paper is harmonizing with respect to other review papers written in the past avoiding the repetition of concepts well known and reaching experts in the field.

## 2. Free-Piston Stirling Engine Configuration

### 2.1. Operation Mode

The FPSE is a reciprocating engine in which the moving pistons are not linked to a crankshaft to extract power. This means that there are no rotating parts, but rather the motion of the two pistons, indicated as working piston and displacer, is coupled via gas pressure dynamics. They are activated only by the relative pressures and the relative motion is determined by their dynamic characteristics. Output power is taken from a linear alternator. Usually a permanent magnet is attached to the working piston, producing electricity directly from the linear stroke of the piston, moving through the alternator field coil [16, 17, 20, 21, 22, 23, 24, 25]. The FPSE works as the kinematic Stirling engine. A schematic working principle of the engine is shown in Figure 1. The heat of the external energy source is transferred by convection to the working gas in the heater. The heated working gas expands, pushing the working piston (expansion and heating processes occurs in the hot volume). Then, the displacer moves the working gas from the hot space to the cold space (hot volume decreases and cold volume increases). The working gas moves towards the regenerator and the cooler, where it transfers the heat to an external coolant, up to the compression space where it is compressed (compression and cooling processes occurs in the cold volume). Then, the working piston moves upwards and the displacer moves downwards resulting the transfer of the gas from the cold volume to the hot volume, through the regenerator. During this process, the gas is heated by the regenerator material. Supposing a perfect regenerator, corresponding to a perfect storage/releasing heat, the gas temperature at the end of this process becomes the hot temperature. Thus, a cyclic pressure- variation resulting in mechanical work is produced and converted in electrical power. The only difference is that the crank-shaft is replaced by an interior spring damping system. In particular, flexure springs are attached to the respective displacer and working piston, releasing mechanical energy as the flywheel in the kinematic Stirling engine. By this way, the movement of the displacer and the piston is independent, only based on the pressure variation of the working gas [16, 17, 20, 21, 22, 23, 24, 25, 26].

![Energies 14 07009 g001](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g001-550.jpg "Energies 14 07009 g001")

Figure 1. Operation mode of a FPSE [26].

### 2.2. Classification

Different types of FPSEs—hybrid, pendulum, diaphragm, duplex, single and double acting—can be identified: [27]. The latter two are divided into several subcategories, as widely reported and described by Zare et al. [16]. A summary of their characteristics was well synthesized in Figure 2. The main features reported in [16] are summarized below. The hybrid FPSE can be considered as a combination of kinematic and dynamic Stirling engines, in which the working piston is usually connected to a crank mechanism through a connecting rod, while the displacer piston is free to move. The pendulum type is characterized by a pendulum mechanism, which is the reason of working piston resonance, while the displacer is free to move. Instead, in the diaphragm engine, the working piston is replaced by a diaphragm which flexes to effect the change of working gas volume [28]. This prevents the gas leakages which occur in conventional FPSE where the displacer’s guiding shaft goes through a clearance seal into a chamber called bounce space [28]. The duplex FPSE is able to work as both engine and refrigerator simultaneously due to two displacers that, with the working piston, serves one as heat engine and one as heat pump. Finally, the FPSE can be single-acting or double-acting. The double-acting type consists of multiple-engine units with one piston per cylinder. The cylinder can be more than two, with linked working chambers. In contrast, in the single-acting FPSE, there are two reciprocating pistons per cylinder. Two spaces are detectable, i.e., the expansion and the compression spaces. The last configuration is the most usable FPSE model. More than one single-acting configuration can be possible, as for example working piston-working piston type with parallel, V or opposed cylinders and working piston-displacer in split cylinders (parallel/orthogonal/opposed) or in tandem mode. However, the single-acting working piston-displacer in tandem engine shown in Figure 3 can be considered as the common model of FPSE [16]. It presents a single cylinder in which both working piston and displacer are placed. This arrangement includes the displacer sprung to working piston, reported in Figure 3 a and displacer piston sprung to ground, reported in Figure 3 b.

![Energies 14 07009 g002](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g002-550.jpg "Energies 14 07009 g002")

Figure 2. Classification of single-acting and double-acting FPSEs.

![Energies 14 07009 g003](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g003-550.jpg "Energies 14 07009 g003")

Figure 3. Two common models of single-acting working piston-displacer in tandem FPSE: (a) displacer sprung to working piston; (b) displacer piston sprung to ground.

## 3. Free-Piston Stirling Engine Applications

The first FPSE was designed by William Beale in 1964, who founded the Sunpower Company in 1974 [16, 27]. Over the years, the engine has gone through several modifications, preserving the same working principles. Currently, FPSE is used in different applications, such as solar converters (dish Stirling), cryocoolers and micro combined heat and power (CHP) units. A description of these systems is given in this section.

### 3.1. Dish Stirling

The SE and specifically the FPSE are used as solar converters in Concentrated solar power (CSP) systems to convert the heat generated by concentrating and absorbing the solar radiation in electricity [29]. In particular, the incident solar radiation is directly concentrated on the heater of the engine through a parabolic dish [18, 29]. The solar applications based on the Stirling cycle, known as dish Stirling, are a valid option to linear Fresnel reflectors, parabolic troughs and power tower because the combination of the parabolic dish (one of the most performant system for solar tracking) and the SE allows a high conversion efficiency [30]. Moreover, the dish Stirling systems are very suitable for distributed generation because they are self-contained power generators which make available an electrical power with high modularity (3–45 kW) [23, 31, 32, 33, 34, 35].

A schematic view of the dish Stirling is reported in Figure 4. It consists in a parabolic dish collector and a FPSE. The collector allows to deliver thermal energy. It has a solar concentrator, i.e., the parabolic dish to direct the solar radiation on the receiver’s aperture, and a thermal receiver, that accepts the solar radiations delivered by the dish and transfers the thermal energy to the working gas of the engine [32]. To achieve the maximum efficiency, the concentrator is placed on a mobile structure to track the sun (tracking system) [2]. The FPSE is usually located at the focal point of the reflector, held up by the engine support [23, 36]. Generally, two methods are used to transfer absorbed solar radiation to the working gas [23]. The directly illuminated tube receiver (i.e., small tubes through which the engine’s working gas flows), can be placed directly where there is the concentrated solar flux (the tubes form the absorber surface) or a liquid metal intermediate heat transfer fluid can be used [23]. The liquid metal is vaporized on the absorber surface and condenses on tubes carrying the engine’s working gas. This second type of receiver is called a heat pipe receiver because the vapor condenses and flows back to be heated again [23]. The thermal receiver is thermally connected to the heater, thus the working gas warms up directly [37].

![Energies 14 07009 g004](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g004-550.jpg "Energies 14 07009 g004")

Figure 4. A schematic view of a Dish Stirling.

Due to the low thermal inertia, a dish Stirling system reacts very quickly on changes in solar thermal input [23]. Thus, steady state operation is achieved within a few minutes after system start. The engines applied for dish Stirling systems use helium or hydrogen at working gas temperatures between 600 and 800 °C. Power output is controlled by varying the working gas mean pressure or piston stroke [23].

Dish Stirling systems are suitable for decentralized applications, even if going for small units increases relative cost for components like electrics, controls and field cabling [23, 31, 32, 33, 34, 35]. Different sizes of dish Stirling systems are commercialized and installed in the world. Most of the present product developments range between some kW and 25 kW, corresponding to dish projected areas of 50–120 m<sup>2</sup> [23]. Infinia Corporation started to commercialize a PowerDish, equipped with a 3.2 kW FPSE, in 2004. Then, the company developed four generations of PowerDish that were installed in Yuma (AZ, USA), Villarrobledo (Spain), and the Tooele Army Depot (UT, USA) [18, 23, 36]. In 2013, after filing for bankruptcy, Infinia knowhow was acquired by Qnergy [36].

### 3.2. Cryocoolers

FPSE cryocoolers are used for high temperature superconducting and gas liquefaction applications because they are able to provide large cooling power reliably and economically [38]. These are of particular interest in the duplex Stirling engine, i.e., one SE receiving heat at high temperature produces the power necessary to drive another SE acting as a refrigerator or heat pump. The FPSE is particularly favorable because the two FPSE can be integrated in a very compact system with a common working piston and two displacers [39]. Qnergy has developed a system with proven flexure bearings to provide the gas clearance seals while eliminating wear as a degradation mechanism. This allows to work over a wide range of conditions (from 50 K up to more than 120 K) with a nominal cooling capacity rating of 650 W at 77 K with an efficiency equal to about 30% that of Carnot cycle [19].

### 3.3. Micro Combined Heat and Power

The micro-CHP units are based on the producing electrical and heat power simultaneously from the same energy source. It takes advantages of the high residual heat contained in the exhaust gas that can be reused for other systems. In the recent years, CHP units are based on different technologies, e.g., internal combustion engine [40], gas turbine [41, 42], organic Rankine cycle (ORC) [43, 44], fuel cells [45]. However, the SE is preferred in residential applications for its low emissions and compact design [6, 17, 46, 47]. Moreover, different companies have focused particular attention on the FPSE solution for micro-CHP systems because no maintenance is necessary. At this time, the commercially available FPSE units are that of Microgen Engine Corporation [48] and Qnergy [49].

Microgen Engine Corporation is a consortium of the gas boiler companies Viessmann, Baxi, Vaillant and Remeha and Sunpower [22, 50]. The most suitable Microgen FPSE for domestic houses produces alternating current (50 Hz) and provides 1 kW of electrical power [51, 52]. The displacer pushes helium through the regenerator from the head to the cooler; the spring on the opposite case at the bottom pushes the piston back upwards; the helium is alternately heated and cooled, and as a result it expands and contracts, creating cyclic pressure waves 50 times per second, generating AC power at 50 Hz [51]. The magnetic working piston is surrounded by a fixed magnetic coil with copper windings, which means that an alternating current is generated (a linear alternator inside the engine is used) [51]. Generally, Microgen FPSE systems use natural gas but other heat sources are tested [53].

Qnergy developed 1 kWe and 3 kWe FPSEs for micro-CHP systems [49, 54]. The hot side of the engine is a vertical tubular heater, which allows more suitability for gas burners [55]. The working gas, that is helium, quickly heats up and expands, meanwhile the displacer moves on. Then, the hot helium passes through the cold side of the engine where it contracts and quickly loses pressure and temperature. A mix of properly tuned gas and mechanical springs sends the displacer back. The displacer movement creates a wave of pressure in the helium which moves a linear magnet inside a coil of wire, with a cyclic motion that is 60° out of phase with the displacer. This generates single-phase alternating current power on both back-and-forth displacer strokes [49, 56]. The latest commercial FPSE for micro-CHP is the PCK80 FPSE [57]. It can provide an electrical power output of 7.1 kW (maximum value) with an electrical efficiency up to 30% and a maximum thermal output of 25 kW, with the temperature of the hot side is between 673 K and 1073 K [58]. Different liquid/gaseous fuels, biogas, wood/paper fuels, solar and waste heat can be employed as heat source [57, 59] to produce electricity.

Microgen and Qnergy FPSE are usually installed on micro-CHP systems commercialized by other companies. Recently, the ÖkoFEN Company [60] proposes the Pellematic Condense and the Pellematic e-max micro-CHP units based on Microgen and Qnergy FPSE, respectively [58]. The Pellematic Condens_e provides 0.6 kW of electric power and a thermal output up to 13 kW [61]. The Pellematic e-max is a pilot-project that consists in a development of electricity generating from wood pellets heating to produce up to 5 kWe and 60 kWth for larger buildings [62].

Experimental results of a Pellematic Condens_e using Microgen FPSE installed in laboratory at Paris Nanterre University presented in Figure 5, are summarized in Table 1. The wood pellet mass is measured about 1.4462 g and the net calorific value is determined experimentally about 5.1 kWh/kg.

![Energies 14 07009 g005](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g005-550.jpg "Energies 14 07009 g005")

Figure 5. Micro-CHP unit installed in laboratory@ Paris Nanterre University.

Table 1. Experimental results of ÖkoFEN micro-CHP units tested in our laboratory (LEME).

![](https://pub.mdpi-res.com/img/table.png)

## 4. Free-Piston Stirling Engine Modeling

Well-established thermodynamic models analyze SE performance in terms of power output and thermal efficiency. These models are classified into different orders, according to the level of their complexity. The order increases as the number of idealizing assumptions decreases [27, 63]. Zero-order, first-order, second-order and third-order models can be considered [2, 52, 58].

The zero-order analysis is based on experiments, i.e., SE power and efficiency are calculated through a semi-empirical expression, in which a power correction factor is applied according to the temperature range. This method has been introduced by Beale and confirmed by West and Organ [2].

The first-order models evaluate the idealized SE performance with no losses, by identifying different control volumes and making some thermodynamic assumptions. In particular, the compression and the expansion spaces can be considered isothermal or adiabatic, resulting in isothermal or adiabatic model, respectively [1]. The first simplest approach has been presented by Schmidt; the second analysis has been reported by Finkelstein, who introduced the concept of conditional temperatures depending on the gas flow direction, and reconsidered by Urieli and Berchowitz [64, 65].

The second-order models study the SE by implementing the first-order ideal analysis with the thermal and power losses [32, 66, 67, 68]. The separated effects of thermal and friction power losses in the heat exchangers allow to estimate closely the real engine power and efficiency [69, 70]. These losses are calculated independently from each other. For this reason, the second-order models are defined also uncoupled [71].

The third-order models evaluate the variation of pressure, temperature and velocity in the working gas using Navier-Stokes and energy conservation equations at each working space. This analysis-type is named coupled approach [72, 73].

More recently, CFD-based models have been set up to study SE, achieving detailed information about SE process and losses in higher computational time and costs [3, 4]. Multi-objective models have been also widely used to optimize SE performance [74, 75, 76].

To model the dynamic behavior of the FPSE, the thermodynamic analysis alone is not sufficient because of spring dynamic characteristics. For this reason, the thermodynamic equations are usually combined with the dynamic relationships [16]. The motion of the working piston and the displacer are generally assumed harmonic according to the D’Alemebert’s principle: $M\stackrel{¨}{x}+\sigma \stackrel{˙}{x}+Kx=F$ that is the general equation to describe a mass-spring-damper system with an applied force $F$ , where x is the mass displacement, $\sigma$ is the damping coefficient and $K$ is the spring stiffness. Thermodynamic parameters of the engine have to be defined prior to any dynamic model of FPSE because the movements of the displacer and working piston are related to the variation of pressure that depends on the fluid temperatures. Due to the complexity of this analysis, the isothermal assumption is usually adopted, given the temperatures inside the engine as input variables. The stroke and the phase angle are fixed by the combined effect of both thermodynamic and dynamic parameters [77]. One-dimensional, two-dimensional Computational Fluid Dynamics, and Sage models are widely used in research works.

Beale presented the first analytical approach for predicting the performance of FPSE based on Schmidt’s theory adopted originally for kinematic Stirling engine [54]. Later, several models have been proposed to simulate also the dynamic effects. These theories can be classified into linear and non-linear analysis [16].

Rogdakis et al. [78] proposed a linearization technique of dynamic balance equation, solving analytically the equations of the angular velocity in terms of the working gas mass and the displacer-piston phase angle of the engine. Linearizing the equations of the motion allowed to obtain a system of linear and homogeneous differential equations with constant coefficient, that could be solved analytically in the time domain. They applied this approach to a typical FPSE, the RE-1000 produced by Sunpower Inc.

It is a single cylinder FPSE with the displacer sprung to ground, connected to a dashpot load device built inside of the bounce space. The gas spring is within the displacer [79]. The main feature of the engine is that the working piston motion is larger than the casing motion, because the piston mass is lighter than that of the casing. The motion of the working piston and the displacer has been assumed harmonic. Generally, according to the Newton’s second low, $F+{F}_{s}+{F}_{d}=M\stackrel{¨}{x}$ , where $F$ is the applied force (that has a component normal to the displacing surface), ${F}_{s}$ is the force due to the spring effects, ${F}_{d}$ is the damping force and $M\stackrel{¨}{x}$ is the inertial force. All the forces are collinear. The forces acting on the working piston and the displacer are reported in Figure 6.

![Energies 14 07009 g006](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g006-550.jpg "Energies 14 07009 g006")

Figure 6. A schematic drawing of the forces acting on the working piston and the displacer (a) and the mass-spring-damper system approximation (b).

In order to easy identify all magnitudes of the equations the volume divisions in the engine with proper notations are reported in Figure 6.

Ignoring the casing oscillation and assuming $\Delta p={p}_{E}-{p}_{C}$

$$
{M}_{p}{\stackrel{¨}{x}}_{p}=\left({p}_{C}-{p}_{B}\right){A}_{p}-\left({C}_{{H}_{pc}}+{C}_{pc}\right){\stackrel{˙}{x}}_{p}
$$

(1)

$$
{M}_{d}{\stackrel{¨}{x}}_{d}={A}_{d}\Delta p+\left({p}_{C}-{p}_{d}\right){A}_{r}-{C}_{{H}_{dc}}{\stackrel{˙}{x}}_{d}
$$

(2)

where $M$ is the mass, $A$ is the cross-section area, $x$ is the displacement, $\stackrel{˙}{x}$ is the velocity, $\stackrel{¨}{x}$ is the acceleration, $p$ is the pressure. The subscripts $p$ and $d$ are referred to the working piston and the displacer, respectively. $B$ denotes the bounce space, ${A}_{r}$ is the displacer rod section. ${C}_{pc}$ is the load damping, while ${C}_{{H}_{pc}}$ and ${C}_{{H}_{dc}}$ are the piston gas and the displacer gas spring damping, respectively. Assuming that ${S}_{ij}$ and ${D}_{ij}$ are the effects of the $j$ -component motion on the $i$

$$
{\stackrel{¨}{x}}_{p}={S}_{pp}{x}_{p}+{S}_{pd}{x}_{d}+{D}_{pp}{\stackrel{˙}{x}}_{p}+{D}_{pd}{\stackrel{˙}{x}}_{d}
$$

(3)

$$
{\stackrel{¨}{x}}_{d}={S}_{dp}{x}_{p}+{S}_{dd}{x}_{d}+{D}_{dp}{\stackrel{˙}{x}}_{p}+{D}_{dd}{\stackrel{˙}{x}}_{d}
$$

(4)

This equations system could be written in matrix form as follows:

$$
\left[\begin{array}{c}{\stackrel{¨}{x}}_{p}\\ \begin{array}{c}{\stackrel{¨}{x}}_{d}\\ {\stackrel{˙}{x}}_{p}\\ {\stackrel{˙}{x}}_{d}\end{array}\end{array}\right]=\left[\begin{array}{cccc}{D}_{pp}& {D}_{pd}& {S}_{pp}& {S}_{pd}\\ {D}_{dp}& {D}_{dd}& {S}_{dp}& {S}_{dd}\\ 1& 0& 0& 0\\ 0& 1& 0& 0\end{array}\right]·\left[\begin{array}{c}{\stackrel{˙}{x}}_{p}\\ \begin{array}{c}{\stackrel{˙}{x}}_{d}\\ {x}_{p}\\ {x}_{d}\end{array}\end{array}\right]
$$

(5)

To resolve this equation system, the Schmidt isothermal model was used to obtain the pressure variations in the working spaces and the gas springs [66]. The engine is considered divided into 5 volumes (compression volume, cold volume, regenerator, hot volume and expansion volume) and the temperature variation of the gas into the regenerator volume is supposed to be linear $\left({T}_{R}=\frac{{T}_{H}-{T}_{K}}{ln\frac{{T}_{H}}{{T}_{K}}}\right)$

$$
p=Mr{\left[\frac{{V}_{C}}{{T}_{K}}+\frac{{V}_{K}}{{T}_{K}}+\frac{{V}_{R}·\mathrm{ln}\left({T}_{H}/{T}_{K}\right)}{\left({T}_{H}-{T}_{K}\right)}+\frac{{V}_{H}}{{T}_{H}}+\frac{{V}_{E}}{{T}_{H}}\right]}^{-1}
$$

(6)

where V<sub>C</sub> is compression volume, V<sub>K</sub> is cooler volume, V<sub>R</sub> is regenerator volume, V<sub>E</sub> is expansion volume, and r is the working gas constant.

Considering the volume variations, linearizing the pressure equations with the binomial expansion and assuming that the mean pressure ${p}_{mean}$ in the working space is the charge pressure, the spring and damping coefficients as a function of the working gas mass $M$ , angular velocity $\omega$ and piston-displacer phase angle ${\alpha }_{xdxp}$

$$
{S}_{pp}\left(M\right)=-\frac{{A}_{p}^{2}}{{M}_{p}}{p}_{mean}\left(M\right)\left(\frac{1}{{T}_{K}S}+\frac{\gamma }{{V}_{B}}\right)
$$

(7)

$$
{S}_{pd}\left(M\right)=-\frac{{A}_{p}^{2}}{{M}_{p}S}{p}_{mean}\left(M\right)\left[\left(1/{T}_{H}\right)-\left(1-\frac{{A}_{R}}{{A}_{p}}\right)/{T}_{K}\right]
$$

(8)

$$
{S}_{dp}\left(M\right)=-\frac{{A}_{p}{A}_{R}{p}_{mean}\left(M\right)}{{M}_{D}{T}_{K}S}
$$

(9)

$$
{S}_{dd}\left(M\right)=-\frac{{A}_{r}{p}_{mean}\left(M\right)}{{M}_{D}}\left[\frac{{A}_{p}}{{T}_{H}S}-\frac{\left({A}_{p}-{A}_{r}\right)}{{T}_{K}S}+\gamma \frac{{A}_{r}}{{V}_{D}}\right]
$$

(10)

$$
{D}_{pp}=-\frac{{C}_{pc}}{{M}_{p}}
$$

(11)

$$
{D}_{pd}=0
$$

(12)

$$
{D}_{dp}\left(M,\omega ,{\alpha }_{xdxp}\right)=\frac{{C}_{p}\left(M,\omega ,{\alpha }_{xdxp}\right)}{{M}_{D}}
$$

(13)

$$
{D}_{dd}\left(M,\omega ,{\alpha }_{xdxp}\right)=\frac{{C}_{d}\left(M,\omega ,{\alpha }_{xdxp}\right)-{C}_{{H}_{dc}}}{{M}_{D}}
$$

(14)

$$
S=\frac{{A}_{P}{C}_{C}}{{T}_{K}}+\frac{{V}_{K}}{{T}_{K}}+\frac{{V}_{R}\mathrm{ln}\left[{T}_{H}/{T}_{K}\right]}{{T}_{H}-{T}_{K}}+\frac{{V}_{H}}{{T}_{H}}+\frac{{A}_{d}{E}_{E}}{{T}_{H}}
$$

(15)

where here S is stiffness coefficient.

Finally, the set of dynamic equations for the angular velocity, the piston-displacer phase angle and the piston-displacer amplitude are obtained as follows:

$$
\omega ={\left[\frac{{D}_{dp}\left(M,\omega ,{\alpha }_{xdxp}\right)·{S}_{pd}\left(M\right)+{S}_{dp}\left(M\right)·{D}_{dp}-{D}_{dd}\left(M,\omega ,{\alpha }_{xdxp}\right)·{S}_{pp}\left(M\right)-{S}_{dd}\left(M\right)·{D}_{pp}}{{D}_{dd}\left(M,\omega ,{\alpha }_{xdxp}\right)+{D}_{pp}}\right]}^{1/2}
$$

(16)

$$
{\alpha }_{xdxp}={\mathrm{tan}}^{-1}\left(\frac{\omega {D}_{pp}}{-\left({S}_{pp}\left(M\right)+{\omega }^{2}\right)}\right)
$$

(17)

$$
\frac{{x}_{d}}{{x}_{p}}=\frac{{\left({\omega }^{2}+{S}_{pp\left(M\right)}\right)}^{2}+{\omega }^{2}{D}_{pp}^{2}}{{S}_{pd}\left(M\right){\left[{\left({\omega }^{2}+{S}_{pp}\left(M\right)\right)}^{2}+{\omega }^{2}{D}_{pp}^{2}\right]}^{1/2}}
$$

(18)

In Table 2 are reported the comparison between the results obtained by Rogdakis et al. by the model exposed above, where differential equations system has been solved parametrically [78], their previous results obtained by resolving equations analytically in terms of stiffness and damping coefficients [80], results from previous works by Urieli et al. [65] and Walker et al. [27] and experimental data [65]. It was evidenced that by linearization, it was obtained a good correspondence with the frequency and slightly improvement with the amplitude ratio and phase angle.

Table 2. Comparison of the stable operation parameters of the RE-1000 obtained by several models.

![](https://pub.mdpi-res.com/img/table.png)

Formosa and Despesse [81] developed a thermodynamic model as a start point to develop a global analysis of the FPSE. This model considered heat losses and irreversibility of the heat exchangers and the regenerator. First, the Schmidt isothermal analysis has been used; then, the heat exchangers and the regenerator efficiency was expressed as a function of fluid flow rates. The results of this model were compared with the experimental data of the General Motor GPU-3 Stirling engine prototype and the model of Urieli and Berchowitz [65] for the same conditions of the GPU-3 demonstrating that a reduction of losses and a notable improvement in the engine performance could be reached even if not a perfect agreement was obtained.

In a later work, Formosa [77] presented a semi-analytical dynamic model, in which both thermodynamic and dynamic evaluations were performed. The results obtained have been compared with experimental data obtained of RE 1000 FPSE and good agreement obtained demonstrated that this model could be used as possible guide line for the improvement of other similar Stirling engines.

The isothermal analysis was applied for the thermodynamic analysis, while the dynamic model evaluated the kinematic results; the global simulation of the FPSE has been made using a coupled iterative technique. The model considered the regenerator efficiency, heat exchanger performance and the conduction losses.

The main target of the dynamic analysis is to evaluate the operating pulsation ( $\omega$ ) and and amplitudes and phase angle of displacer and working piston (s<sub>d</sub>, s<sub>p</sub>) and the phase angle ( ${\alpha }_{xdxp}$

$$
{V}_{E}\left(t\right)=\frac{{V}_{swE}}{2}\left(1+\mathrm{cos}\left(\omega t\right)\right)
$$

(19)

$$
{V}_{C}\left(t\right)=\frac{{V}_{swC}}{2}\left(1+\mathrm{cos}\left(\omega t-\alpha \right)\right)
$$

(20)

where ${V}_{sw}$ is the swept volume for the compression ( $C$ ) and expansion ( $E$ ) spaces and $\alpha$

Assuming that the motion of the working piston and the displacer is harmonic, the instantaneous volumes become:

$$
{V}_{E}\left(t\right)={A}_{de}{x}_{d}\left(t\right)={A}_{de}{s}_{d}\mathrm{cos}\left(\omega t\right)
$$

(21)

$$
{V}_{C}\left(t\right)={A}_{p}{x}_{p}\left(t\right)-{A}_{dc}{x}_{d}\left(t\right)={A}_{p}{s}_{p}\mathrm{cos}\left(\omega t+{\alpha }_{xdxp}\right)-{A}_{dc}{s}_{d}\mathrm{cos}\left(\omega t\right)
$$

(22)

where $A$ is the cross-section area, $s$ is the stroke and $x$ is the moving part position. The subscripts $p$ and $d$ are referred to the working piston and the displacer, respectively. ${A}_{de}$ is the area of the expansion side of the displacer; similarly, ${A}_{dc}$

Comparing the previous equations, it is derived that the swept volumes are:

$$
{V}_{swE}=2{A}_{de}{s}_{d}
$$

(23)

$$
{V}_{swC}=2\sqrt{{\left({A}_{p}{s}_{p}\mathrm{cos}\left({\alpha }_{xdxp}\right)+{A}_{dc}{s}_{d}\right)}^{2}+{\left({A}_{p}{s}_{p}\mathrm{sin}\left({\alpha }_{xdxp}\right)\right)}^{2}}
$$

(24)

$$
\alpha =\pi +arctan\left[\frac{{A}_{p}{s}_{p}\mathrm{sin}\left({\alpha }_{xdxp}\right)}{-{A}_{dc}{s}_{d}+{A}_{p}{s}_{p}\mathrm{cos}\left({\alpha }_{xdxp}\right)}\right]
$$

(25)

Defining the swept volume ratio:

$$
\kappa ={V}_{swC}/{V}_{swE}
$$

(26)

the total swept volume is:

$$
{V}_{sw}={V}_{swE}\sqrt{1+{\kappa }^{2}+2\kappa \mathrm{cos}\left(\alpha \right)}
$$

(27)

As a result, the main engine parameters are obtained as follows:

$$
{p}_{mean}=\frac{Mr}{z}\frac{1}{\sqrt{1-{\beta }^{2}}}
$$

(28)

$$
{P}_{i}={p}_{mean}\frac{\omega }{2\pi }\frac{{V}_{swE}}{2\beta }\frac{\kappa \left(\tau -1\right)\mathrm{sin}\left(\alpha \right)}{\sqrt{{\tau }^{2}+{\kappa }^{2}+2\kappa \mathsf{\tau }\mathrm{cos}\left(\alpha \right)}}\left(1-\sqrt{1-{\beta }^{2}}\right)
$$

(29)

$$
{\eta }_{i}=1-{T}_{C}/{T}_{E}
$$

(30)

where $\beta =\frac{\sqrt{2\tau \kappa \mathrm{cos}\left(\alpha \right)+{\tau }^{2}+{\kappa }^{2}}}{2\nu +\kappa +\tau }$ , $\frac{1}{z}=2\frac{{T}_{E}}{{V}_{swE}}\tau \frac{1}{2\nu +\kappa +\tau },\text{}\tau ={T}_{C}/{T}_{E}$ , $\nu =\frac{{V}_{CC}}{{V}_{swE}}+\frac{{V}_{R}}{{V}_{swE}}\frac{{T}_{C}}{{T}_{R}}+\frac{{V}_{HC}}{{V}_{swE}}\tau$

From the dynamic analysis, the equations of the displacer and the working piston motion are written as follows:

$$
{M}_{d}{\stackrel{¨}{x}}_{d}+{D}_{d}{\stackrel{˙}{x}}_{d}=\left({A}_{Bd}{p}_{Bd}-{A}_{de}{p}_{E}+{A}_{dc}{p}_{C}\right)
$$

(31)

$$
{M}_{p}{\stackrel{¨}{x}}_{p}+{D}_{p}{\stackrel{˙}{x}}_{p}=\left({A}_{p}{p}_{Bp}-{A}_{p}{p}_{C}\right)
$$

(32)

${\stackrel{˙}{x}}_{p}=0$ , ${\stackrel{˙}{x}}_{d}=0$ , ${x}_{d}=0$ , ${x}_{p}=0$ are assumed as initial conditions. $M$ is the mass, $\stackrel{˙}{x}$ is the velocity, $\stackrel{¨}{x}$ is the acceleration, $p$ is the pressure, D is the damping coefficient. $B$ denotes the bounce space. ${D}_{p}$ is the total damping coefficient for the working piston. ${p}_{E}$ and ${p}_{C}$ are the pressure in expansion and compression spaces, respectively. In particular, considering the pressure losses in the heat exchangers, ${p}_{E}=p+\left(\mathsf{\Delta }{p}_{H}+\mathsf{\Delta }{p}_{R}+\mathsf{\Delta }{p}_{K}\right)$ and ${p}_{C}=p$

The thermodynamic and the dynamic equations are coupled to solve the model. First, an evaluation of the chambers temperatures thanks to thermodynamic analysis using kinematic parameters of the RE-1000 FPSE is obtained. Then, these values are input parameters for the dynamic analysis for which the linear viscous damping coefficients are used as calibration variables. They are modified to match the strokes of the piston and the displacer, their phase angle and the operating frequency. After a first iteration, the evaluated kinematic results are parameters for a next iteration of thermodynamic analysis. The resulting temperatures of the expansion and the compression spaces are compared with the previous values. The convergence is achieved when the error is less than 0.5%.

Kwankaomeng et al. [82] assumed harmonic motion of the pistons to describe a FPSE prototype, considering the mass-spring-damper system and the Schmidt theory for thermodynamic analysis.

The equations of motion of the working piston and the displacer used in their model are:

$$
{M}_{p}{\stackrel{¨}{x}}_{p}=\left({p}_{C}-{p}_{atm}\right)·{A}_{p}-{D}_{pd}·\left({\stackrel{˙}{x}}_{p}+{\stackrel{˙}{x}}_{d}\right)
$$

(33)

$$
{M}_{d}{\stackrel{¨}{x}}_{d}={A}_{dr}·{p}_{C}+\left({p}_{E}-{p}_{C}\right)·{A}_{d}-{K}_{d}{x}_{d}-\left({D}_{dp}+{D}_{E}\right)·{\stackrel{˙}{x}}_{p}
$$

(34)

where, as in the previous models $M$ is the mass, $A$ is the cross-section area, $x$ is the displacement, $\stackrel{˙}{x}$ is the velocity, $\stackrel{¨}{x}$ is the acceleration, $p$ is the pressure. The subscripts $p$ denotes the working piston, $d$ is the displacer, while $E$ and $C$ are referred to the expansion and the compression volume, respectively. ${A}_{dr}$ is the cross-section area of the displacer rod; ${D}_{dp}$ , ${D}_{pd}$ , and ${D}_{E}$ are the damping coefficient and K is the spring stiffness.

The sinusoidal displacement $x$ and volume variation $V$

$$
{x}_{d}=\frac{1}{2}·{s}_{d}·\mathrm{sin}\left(\omega t\right)
$$

(35)

$$
{x}_{d}=\frac{1}{2}·{s}_{p}·\mathrm{sin}\left(\omega t-{\alpha }_{xdxp}\right)
$$

(36)

$$
{V}_{E}={A}_{d}·{x}_{d}+{V}_{dh}
$$

(37)

$$
{V}_{C}={A}_{d}·{s}_{d}-{V}_{E}+{A}_{p}·{x}_{p}+{V}_{dc}
$$

(38)

where ${V}_{dh}$ and ${V}_{dc}$ are the dead volume of the hot and cold spaces, respectively, and $s$

The equations derived by the Schmidt analysis are:

$$
p=M·r·{\left[\frac{{V}_{C}}{{T}_{C}}+\frac{{V}_{R}}{{T}_{R}}+\frac{{V}_{E}}{{T}_{E}}\right]}^{-1}
$$

(39)

$$
{p}_{mean}={p}_{max}{\left(\frac{1-\delta }{1+\delta }\right)}^{-1/2}
$$

(40)

where:

$$
\delta ={\left({\tau }^{2}+{\kappa }^{2}+2\tau \kappa \mathrm{cos}{\alpha }_{xdxp}\right)}^{1}{2}}/\left(\tau +\kappa +2\mu \right)
$$

(41)

$$
\mu =\left(2X\tau \right)/\left(\tau +1\right)
$$

(42)

$$
X={V}_{dc}/{V}_{dh}
$$

(43)

$M$ is the total mass of the gas in the engine, $\delta$ and μ are the calculation parameter, $\tau$ is the temperature ratio ${T}_{C}/{T}_{E}$ , $\kappa$ is the swept volume ratio ${V}_{swC}/{V}_{swE}$ , $\alpha$ is the phase angle and $X$

The working piston and displacer motion and the pressure variation diagram have been obtained. Experimental tests have been performed on the prototype to evaluate engine power and efficiency.

Tavakolpour-Saleh et al. [83] have analyzed a FPSE using a model based on perturbation technique (multiple scale method) taking into account non-linear springs behavior, in which the fast-scale and the slow-scale variables were defined in order to solve the problem. In particular, the heater and cooler temperatures were included into two non-linear equations; their values were found numerically through a genetic algorithm.

Sowale et al. [84, 85] presented a quasi-steady model of a gamma-type FPSE. In this model, damping and spring stiffness are calculated at every iteration, defining a properly convergence criteria to achieve the steady state, i.e., the compression and the expansion space temperatures at the beginning of the cycle are the same at the end of the cycle. The engine is divided into five control volumes, that include the heater, the cooler, the regenerator, the expansion and the compression spaces. In particular, the regenerator and its matrix are split in ten parts to give a more realistic behavior. Displacer and piston motions are determined in order to predict their amplitudes, velocities and acceleration, as follows:

$$
{M}_{d}{\stackrel{˙}{x}}_{d}+{K}_{d}{x}_{d}+{C}_{d}\stackrel{˙}{x}={A}_{d}p
$$

(44)

$$
{M}_{p}{\stackrel{˙}{x}}_{p}+{K}_{p}{x}_{p}+{C}_{p}\stackrel{˙}{x}={A}_{p}\left(p-{p}_{B}\right)
$$

(45)

where $M$ is the mass, $K$ is the spring stiffness, $C$ is the dumping load and $A$ is the cross-sectional area. The subscripts $d$ and $p$ denote the displacer and the working piston, respectively. ${p}_{B}$ denotes the bounce space pressure, while $p$

$$
p=\frac{Mr}{\left(\frac{{V}_{c}}{{T}_{CK}}+\frac{{V}_{K}}{{T}_{K}}+\frac{{V}_{R}}{{T}_{R}}+\frac{{V}_{H}}{{T}_{H}}+\frac{{V}_{E}}{{T}_{HE}}\right)}
$$

(46)

The concept of conditional temperatures depending on the gas flow direction is used to determine the temperature of the working gas across the boundary conditions. In addition, contrary to the Rogdakis et al. model [78], the temperature of the working gas on the regenerator is obtained as:

$$
{T}_{R\left(i\right)-R\left(i+1\right)}=\frac{{T}_{R\left(i\right)}+{T}_{R\left(i+1\right)}}{2}
$$

(47)

where $i$

The expansion ( ${V}_{E}$ ) and the compression ( ${V}_{C}$ ) volumes are expressed function of the clearance volume ( ${V}_{cl}$ ) and the pistons position ( $x$

$$
{V}_{E}={V}_{clE}+{x}_{d}{A}_{d}
$$

(48)

$$
{V}_{C}={V}_{clC}+{x}_{p}{A}_{p}-{x}_{d}{A}_{d}
$$

(49)

The heat loss from conduction in the heat exchanger is expressed as:

$$
{Q}_{cond}=\frac{kA}{l\Delta T}
$$

(50)

where k is the thermal conductivity, $l$ is the length and $\Delta T$

For the regenerator, the heat transfer due to the heat conduction form the first to the last part is defined as external conduction heat loss, including also the heat transfer from the part of the regenerator with a higher temperature to the part with a lower temperature. It is estimated as:

$$
{Q}_{Rext}=\left(1-\epsilon \right){h}_{R}{S}_{fs}\left({T}_{m}-{T}_{R}\right)
$$

(51)

where $\epsilon$ is the effectiveness of the regenerator and ${T}_{m}$ and ${T}_{r}$

The provided work per cycle is calculated by:

$$
W={\int }_{0}^{t}\left({p}_{E}\frac{d{V}_{E}}{dt}+{p}_{C}\frac{d{V}_{C}}{dt}\right)
$$

(52)

Finally, the power output is obtaining as a product of the work and the frequency $f$

$$
\stackrel{˙}{W}=Wf
$$

(53)

A good agreement in terms of output power and amplitude ratio of the piston and displacer with experimental data of the RE-1000 FPSE was shown. After validating the model, the authors have optimized the performance of the engine selecting some design parameters, using the genetic algorithm.

Ye et al. [25] conducted a multi-objecting optimization of a 1 kW beta-type FPSE through response surface methodology (RSM), that allowed to determine the optimal combination of engine features. The significant effects of parameters were investigated by ANOVA (analysis of variance), while the optimal combination of the parameters was obtained to maximize the output power, and the thermal and exergy efficiency. The multi-objective optimal results were also validated using Sage simulation results. The Sage software produced by Geodon Associates is a one-dimensional thermodynamic modeling tool that is useful to estimate and optimize SE performance [86]. It has a graphical interface that includes the main components of the SE connected to each other through forces, heat and gas flow interconnections (indicated as boundary connections). In the model [25], a displacer, a piston, a rectangular-fin heater, a regenerator, and a cooler were used with expansion, compression and back spaces. The displacer seal, the shuttle losses, the conductive losses of the regenerator and the displacer, and the heat exchangers friction were added to the model. The flow and heat transfer were considered unsteady and periodic, while the working gas was compressible. Thus, the equations were derived from the integral-form compressible gas dynamic equations for one-dimensional internal flow with space and time-variable flow area. The predicted total power increased linearly with the hot temperature and the error between the SAGE model prediction and experimental result kept less than 5% in the temperature range studied. For the multi-objective optimization, power, thermal and exergy efficiency were set to be maximum with the variation of charge pressure, operating frequency, and hot and cold-end temperatures in the design range. It was found a good agreement between the Sage model results and the predicted values. In particular, the errors were equal to 0.37%, 1.51% and 1.40% for output power, thermal and exergy efficiency, respectively. This means that the RSM method is a valid approach to optimize the FPSE.

Chi et al. [87] proposed a two-dimensional (2D) axisymmetric CFD simulation of a beta-type FPSE in order to investigate the variation of pressure, temperature and velocity of the working gas. Then, a post-processing method was used to track the movement of gas parcel to understand the engine operating characteristics. The reliability of the model is verified by experiments. Some errors between experimental and modeling results probably due to some neglected internal and external losses and conversion efficiency were found.

In addition to the models that consider the FPSE a particular type of kinematic Stirling engine, some studies have used the analogy between the FPSE and the thermo-acoustic engine.

Zhu et al. [54] studied a FPSE-based micro-CHP solving implicitly the frequency and piston displacement by thermo-acoustic theory. Schmidt theory has been adopted to model the mean pressure, while the heat transfer has been implemented with other complementary models. The software Sage developed by Gedeon Associates has been used for thermodynamic and dynamic calculations to take into account the non-linear effects.

In some works [52, 58, 88, 89, 90, 91], Microgen FPSE and similar prototypes have been set as reference to study micro-CHP performance and to verify model’s results. Instead, few works on Qnergy (formerly Infinia) can be found in literature [20, 92, 93], mainly focusing on the past Technology Demonstration Convertor (TDC) designed by the Stirling Technology Company (STC), later Infinia Corporation. The TDC is a gamma-type free-piston Stirling convertor, in which both the working piston and the displacer are supported by flexures. In details, the displacer is coupled by two internal flexure stacks on its rod and the working piston is coupled to the engine casing by two flexures stacks. Helium is used as working gas. Two spaces can be identified: the working space and the pressure vessel, in which the displacer and the working piston move, respectively [92, 93, 94]. A moving iron linear alternator is used to convert the working piston oscillations in electric power [95]. A cheaper monolithic heater head is preferred. The estimated Stirling cycle efficiency is about 45%, while the overall system efficiency is about 38.3% [55].

Qui and Peterson [92] presented a linear dynamic simulation of the STC gamma-type FPSE, useful for Sage modeling. The engine was simulated by a mass-spring-damper system, combining simple thermodynamic models and dynamic analysis.

In a later work [96], a new 3.1 kW Stirling Converter Assembly for European residential combined heat and power market was implemented. Design improvements of dead volumes, components height, flow paths, convertor and alternator were shown.

Li et al. [97, 98] proposed the CFD analysis to identify the best solutions in terms of engine structure and heat exchanger dimensions of a FPSE similar to TDC. A new displacer, piston housing cold heat exchanger and regenerator were designed. A larger cooler surface was conceived with respect to the hot side because of the smaller temperature difference. A foiled regenerator was preferred to the traditional random fiber type as a results of its higher reliability and lower flow losses. In [97], it was shown that the engine could reach an efficiency of 28% with 1.6 MPa of mean pressure and with temperatures equal to 923 K (hot-side) and 353 K (cold-side).

Demko et al. [93] studied the TDC engine via the Sage software, starting from a simple model and adding at each step (totaling six case) some components to reach a more realistic model. Cold and hot-end temperatures, mean pressure and frequency were set as operating conditions. Electrical power, heat input and net efficiency were evaluated and compared to experimental data. Each part of the Stirling engine was identified by components connected by different type of connectors (e.g., heat flow, mass flow, etc.). The first case was the simplest structure, containing constrained working piston and displacer, heat exchangers, expansion and compression spaces. No heat conduction and other losses were included for energy and heat flows evaluation. The predicted efficiency was equal to 40.7%. The second case introduced the Sage bar conductor to simulate heat conduction losses through the displacer shell and cylinder liner. The new efficiency (37.6%) did not change too much, except by the different way in which Sage software made the calculation; thus, the conduction losses did not affect the thermodynamic cycle. The bounce space and the working piston seal were considered in the third case. Piston seal loss, piston shuttle loss, and heat loss from the bounce space were implemented in the energy balance. The efficiency decreased up to 37.2%. Adding the displacer-body seal and the appendix gap in the fourth case, a higher reduction of the total power (4.3 W) and a little decreasing in the efficiency (0.4%) were found. In the fifth case, the variable volume inside of the displacer and the displacer rod seal were introduced. This variation had no effects on the total power, while the efficiency decreased by 1.3%. Finally, the sixth case considered the displacer operation in free mode, that is the free-displacer movement was determined by the displacer mass, spring rate and damping. The spring rate and damping coefficients, that were input parameters for the model, were obtained experimentally. As a result, the power and the efficiency became lower because of a decrease in displacer amplitude. This was determined by parametrically altering the spring rate and damping coefficients. However, the total power and the efficiency decreased from the first to the last case because the losses implemented in the model increased at each step. Comparing the simulation results to experimental data, some calibration parameters were analyzed. In particular, the heat transfer and the regenerator friction-factor multipliers were used to correct the heat transfer correlations and to consider the viscous pressure drop, respectively. Considering the calibration factors for heater and cooler heat transfer, and regenerator friction-factor, a good agreement with the experimental data was found: predicted electric power was high by 1.8 W (3.6%), predicted heat input was high by 9.6 W (5.2%), resulting in a net efficiency that was underestimated by 0.4%. However, the pressure amplitude and the pressure phase angle were not predicted very well. This means that some effects of leakages and components eccentricity in the assembly were not considered.

Recently, a work proposed by Qiu et al. [20] optimized a similarly FPSE configuration for a micro-CHP system with a Sage one-dimensional thermodynamic model, to obtain an electrical power output of 1 kW of electrical power and 1.1 kW of heating at 80 °C.

Authors in their previous work [67], developed a new polytropic model to predict the performance of beta and gamma SE, considering several losses. A bypass was added between the compression and expansion volumes and polytropic processes have been considered in these volumes. Shuttle heat exchange and mass leakage in the gap between the displacer and the cylinder have been considered at the same time step. Various losses have been coupled in the model, including regenerator imperfection, heat conduction, fluid viscosity et al. which interact each other as they are calculated in the same time step. This new model can be adapted to FPSE, in addition with a dynamic model as reported above, and represents a perspective of this work.

A synthesis of the models presented in this section are summarized in Table 3 focusing on the main points and model methods used.

Table 3. Summary of thermodynamic and dynamic models on FPSE from the literature.

![](https://pub.mdpi-res.com/img/table.png)

## 5. Conclusions

A summary of the research works on free-piston Stirling Engine (FPSE), has been presented in this paper. The attention has been focused on the difference with the conventional Stirling engine. In particular, in the FPSE, the crankshaft is replaced by an interior spring system attached to the respective displacer and working piston. This means that there are no driving mechanisms, thus it is preferred for its longer operating life, lower noise pollution, maintenance and vibration free, self-starting and high thermal efficiency. The main application of the FPSE, i.e., solar dish Stirling, cryocoolers and micro combined heat and power (CHP) units, are described in details, with reference to the main manufacturing companies. Finally, the assumptions and the main equations of the models reported in literature are presented. Different types of analysis have been developed by researchers, all the studies being based on a combination of the thermodynamic and the dynamic relationship. Actually, to model the dynamic behavior of the FPSE, the thermodynamic analysis becomes not sufficient because of spring dynamic characteristics. Thus, by this work a synthesis of the knowledge of the main aspect of FPSE, both on technology and models, could be achieved, which is necessary before a new project on a free piston Stirling engine.

## Author Contributions

Conceptualization, L.G. and C.P.; methodology, L.G. and C.P.; data curation, L.G. and C.P.; writing—original draft preparation, L.G and C.P.; writing—review and editing, L.G., C.P. and B.M.V. All authors have read and agreed to the published version of the manuscript.

## Funding

This research received no external funding.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

Not applicable.

## Conflicts of Interest

The authors declare no conflict of interest.

## Nomenclature

<table><tbody><tr><td colspan="2">Acronyms</td></tr><tr><td>1D</td><td>One-dimensional</td></tr><tr><td>2D</td><td>Two-dimensional</td></tr><tr><td>CFD</td><td>Computational Fluid Dynamics</td></tr><tr><td>CHP</td><td>Combined Heat and Power</td></tr><tr><td>CSP</td><td>Concentrated Solar Power</td></tr><tr><td>FPSE</td><td>Free-Piston Stirling Engine</td></tr><tr><td>ORC</td><td>Organic Rankine Cycle</td></tr><tr><td>SE</td><td>Stirling Engine</td></tr><tr><td colspan="2">Symbols</td></tr><tr><td>$A$</td><td>Cross-section area (m<sup>2</sup>)</td></tr><tr><td>C<sub>pc</sub></td><td>Load damping (N$·$ s/m)</td></tr><tr><td>C<sub>Hdc</sub></td><td>Displacer gas spring damping (N$·$ s$·$ m<sup>−1</sup>)</td></tr><tr><td>C<sub>Hpc</sub></td><td>Working piston gas spring damping (N$·$ s$·$ m<sup>−1</sup>)</td></tr><tr><td>$D$</td><td>Damping coefficient</td></tr><tr><td>${D}_{ij}$

${E}_{E}$</td><td>Effect of the $j$ -component motion on the$i$ -component for damping

Expansion clearance space (mm)</td></tr><tr><td>$f$</td><td>Frequency (Hz)</td></tr><tr><td>$F$</td><td>Applied force (N)</td></tr><tr><td>${F}_{d}$</td><td>Damping force (N)</td></tr><tr><td>${F}_{s}$</td><td>Force due to spring effects (N)</td></tr><tr><td>$k$</td><td>Thermal conductivity (W$·$ m<sup>−1</sup>$·$ K<sup>−1</sup>)</td></tr><tr><td>K</td><td>Spring stiffness (N$·$ m<sup>−1</sup>)</td></tr><tr><td>$M$</td><td>Mass (kg)</td></tr><tr><td>$p$</td><td>Pressure (Pa)</td></tr><tr><td>${P}_{i}$</td><td>Indicated power (W)</td></tr><tr><td>p<sub>mean</sub></td><td>Mean pressure (Pa)</td></tr><tr><td>$r$</td><td>Working gas constant (j$·$ kg<sup>−1</sup>$·$ K<sup>−1</sup>)</td></tr><tr><td>$s$</td><td>Stroke (m)</td></tr><tr><td>S</td><td>Heat exchange surface/stiffness coefficient (m<sup>2</sup>)/(s<sup>−2</sup>)</td></tr><tr><td>${S}_{ij}$</td><td>Effect of the $j$ -component motion on the$i$ -component for spring</td></tr><tr><td>$t$</td><td>Time (s)</td></tr><tr><td>$T$</td><td>Temperature (k)</td></tr><tr><td>$V$</td><td>Volume (m<sup>3</sup>)</td></tr><tr><td>${V}_{dc}$</td><td>Dead volume of the cold space (m<sup>3</sup>)</td></tr><tr><td>${V}_{dh}$</td><td>Dead volume of the hot space (m<sup>3</sup>)</td></tr><tr><td>${V}_{sw}$</td><td>Swept volume (m<sup>3</sup>)</td></tr><tr><td>$\stackrel{˙}{W}$</td><td>Mechanical power (w)</td></tr><tr><td>$X$</td><td>Dead volume ratio</td></tr><tr><td>$x$</td><td>Displacement (m)</td></tr><tr><td>$\stackrel{˙}{x}$</td><td>Velocity (m$·$ s<sup>−1</sup>)</td></tr><tr><td>$\stackrel{¨}{x}$</td><td>Acceleration (m$·$ s<sup>−2</sup>)</td></tr><tr><td>$z$</td><td>Amplitude coefficient (m<sup>3</sup>$·$ K<sup>−1</sup>)</td></tr><tr><td colspan="2">Greek Symbols</td></tr><tr><td>$\alpha$</td><td>Swept volume phase angle (rad)</td></tr><tr><td>${\alpha }_{xdxp}$</td><td>Displacer-piston phase angle (rad)</td></tr><tr><td>$\epsilon$</td><td>Heat exchanger effectiveness (%)</td></tr><tr><td>$\kappa$</td><td>Swept volume ratio (-)</td></tr><tr><td>$\sigma$</td><td>Damping coefficient (N$·$ s$·$ m<sup>−1</sup>)</td></tr><tr><td>$\tau$</td><td>Temperature ratio (-)</td></tr><tr><td>$\omega$</td><td>Angular velocity (rad$·$ s<sup>−1</sup>)</td></tr><tr><td colspan="2">Subscripts</td></tr><tr><td>$B$</td><td>Bounce space</td></tr><tr><td>$C$</td><td>Compression space</td></tr><tr><td>$CC$</td><td>Compression chamber dead volume</td></tr><tr><td>$d$</td><td>Displacer</td></tr><tr><td>$dc$</td><td>Compression side of the displacer/dead volume of the cold space</td></tr><tr><td>$de$</td><td>Expansion side of the displacer</td></tr><tr><td>$dr$</td><td>Displacer rod</td></tr><tr><td>$E$</td><td>Expansion space</td></tr><tr><td>$H$</td><td>Heater</td></tr><tr><td>$HC$</td><td>Expansion chamber dead volume</td></tr><tr><td>$K$</td><td>Cooler</td></tr><tr><td>$p$</td><td>Working piston</td></tr><tr><td>$pc$</td><td>Compression side of the working piston</td></tr><tr><td>r</td><td>Rod</td></tr><tr><td>$R$</td><td>Regenerator</td></tr><tr><td>$s$</td><td>Spring effect</td></tr><tr><td>$sw$</td><td>Swept (volume)</td></tr></tbody></table>

## References

1. Walker, G. Stirling Engines ; Clarendon Press: Oxford, UK, 1980. [ Google Scholar ]
2. Hachem, H.; Gheith, R.; Aloui, F.; Ben Nasrallah, S. Technological challenges and optimization efforts of the Stirling machine: A review. Energy Convers. Manag. 2018 , 171 , 1365–1387. [ Google Scholar ] [ CrossRef ] [ Scilit ]
3. Kuban, L.; Stempka, J.; Tyliszczak, A. A 3d-CFD study of a γ–type Stirling engine. Energy 2019 , 169 , 142–159. [ Google Scholar ] [ CrossRef ] [ Scilit ]
4. Alfarawi, S.; Al-Dadah, R.; Mahmoud, S. Influence of phase angle and dead volume on gamma-type Stirling engine power using CFD simulation. Energy Convers. Manag. 2016 , 124 , 130–140. [ Google Scholar ] [ CrossRef ] [ Scilit ]
5. Catapano, F.; Perozziello, C.; Vaglieco, B.M. Heat transfer of a Stirling engine for waste heat recovery application from internal combustion engines. Appl. Therm. Eng. 2021 , 198 , 117492. [ Google Scholar ] [ CrossRef ] [ Scilit ]
6. Chahartaghi, M.; Sheykhi, M. Energy, environmental and economic evaluations of a CCHP system driven by Stirling engine with helium and hydrogen as working gases. Energy 2019 , 174 , 1251–1266. [ Google Scholar ] [ CrossRef ] [ Scilit ]
7. Bert, J.; Chrenko, D.; Sophy, T.; le Moyne, L.; Sirot, F. Simulation, experimental validation and kinematic optimization of a Stirling engine using air and helium. Energy 2014 , 78 , 701–712. [ Google Scholar ] [ CrossRef ] [ Scilit ]
8. Ni, M.; Shi, B.; Xiao, G.; Peng, H.; Sultan, U.; Wang, S.; Luo, Z.; Cen, K. Improved simple analytical model and experimental study of a 100 W β-type Stirling engine. Appl. Energy 2016 , 169 , 768–787. [ Google Scholar ] [ CrossRef ] [ Scilit ]
9. Mou, J.; Li, W.; Li, J.; Hong, G. Gas action effect of free piston Stirling engine. Energy Convers. Manag. 2016 , 110 , 278–286. [ Google Scholar ] [ CrossRef ] [ Scilit ]
10. Xiao, G.; Huang, Y.; Wang, S.; Peng, H.; Ni, M.; Gan, Z.; Luo, Z.; Cen, K. An approach to combine the second-order and third-order analysis methods for optimization of a Stirling engine. Energy Convers. Manag. 2018 , 165 , 447–458. [ Google Scholar ] [ CrossRef ] [ Scilit ]
11. Abbas, M.; Boumeddane, B.; Said, N.; Chikouche, A. Dish Stirling technology: A 100 MW solar power plant using hydrogen for Algeria. Int. J. Hydrogen Energy 2011 , 36 , 4305–4314. [ Google Scholar ] [ CrossRef ] [ Scilit ]
12. Renzi, M.; Brandoni, C. Study and application of a regenerative Stirling cogeneration device based on biomass combustion. Appl. Therm. Eng. 2014 , 67 , 341–351. [ Google Scholar ] [ CrossRef ] [ Scilit ]
13. Magri, G.; di Perna, C.; Serenelli, G. Analysis of electric and thermal seasonal performances of a residential microCHP unit. Appl. Therm. Eng. 2012 , 36 , 193–201. [ Google Scholar ] [ CrossRef ] [ Scilit ]
14. Tavakolpour-Saleh, A.; Zare, S.; Bahreman, H. A novel active free piston Stirling engine: Modeling, development, and experiment. Appl. Energy 2017 , 199 , 400–415. [ Google Scholar ] [ CrossRef ] [ Scilit ]
15. Vuarnoz, D.; Kitanovski, A.; Gonin, C.; Borgeaud, Y.; Delessert, M.; Meinen, M.; Egolf, P.W. Quantitative feasibility study of magnetocaloric energy conversion utilizing industrial waste heat. Appl. Energy 2012 , 100 , 229–237. [ Google Scholar ] [ CrossRef ] [ Scilit ]
16. Zare, S.; Tavakolpour-Saleh, A. Free piston Stirling engines: A review. Int. J. Energy Res. 2020 , 44 , 5039–5070. [ Google Scholar ] [ CrossRef ] [ Scilit ]
17. Park, J.; Ko, J.; Kim, H.; Hong, Y.; Yeom, H.; Park, S.; In, S. The design and testing of a kW-class free-piston Stirling engine for microcombined heat and power applications. Appl. Therm. Eng. 2020 , 164 , 114504. [ Google Scholar ] [ CrossRef ] [ Scilit ]
18. Zhu, S.; Yu, G.; Ma, Y.; Cheng, Y.; Wang, Y.; Yu, S.; Wu, Z.; Dai, W.; Luo, E. A free-piston Stirling generator integrated with a parabolic trough collector for thermal-to-electric conversion of solar energy. Appl. Energy 2019 , 242 , 1248–1258. [ Google Scholar ] [ CrossRef ] [ Scilit ]
19. Penswick, L.; Olan, R.W.; Williford, I.; Draney, S.; Buchholz, G. High-capacity and efficiency Stirling cycle cryocooler. Cryocooler 2014 , 18 , 155–162. [ Google Scholar ]
20. Qiu, S.; Gao, Y.; Rinker, G.; Yanaga, K. Development of an advanced free-piston Stirling engine for micro combined heating and power application. Appl. Energy 2019 , 235 , 987–1000. [ Google Scholar ] [ CrossRef ] [ Scilit ]
21. Breeze, P. Stirling engines and free piston engines. In Piston Engine-Based Power Plants ; Academic Press: London, UK, 2018; pp. 59–70. [ Google Scholar ]
22. Harrison, J.; On, E. Stirling engine systems for small and micro combined heat and power (CHP) applications. In Small and Micro Combined Heat and Power (CHP) Systems ; Woodhead Publishing: Sawston, UK, 2011; pp. 179–205. [ Google Scholar ]
23. Schiel, W.; Keck, T. Parabolic dish concentrating solar power (CSP) systems. Conc. Sol. Power Technol. 2012 , 284–322. [ Google Scholar ] [ CrossRef ] [ Scilit ]
24. De la Bat, B.J.G.; Harms, T.M.; Dobson, R.T.; Eng, M.; Bell, A.J. Derivation and numerical case study of a one-dimensional, compressible-flow model of a novel free-piston Stirling engine. Energy 2020 , 199 , 117404. [ Google Scholar ] [ CrossRef ] [ Scilit ]
25. Ye, W.; Yang, P.; Liu, Y. Multi-objective thermodynamic optimization of a free piston Stirling engine using response surface methodology. Energy Convers. Manag. 2018 , 176 , 147–163. [ Google Scholar ] [ CrossRef ] [ Scilit ]
26. Perozziello, C. Experimental and Numerical Study of a Stirling Engine for Waste Heat Recovery from Internal Combustion Engine ; University of Naples Parthenope: Napoli, Italy, 2020. [ Google Scholar ]
27. Walker, G.; Senft, J. Lecture Notes in Engineering: Free Piston Stirling Engines , 1st ed.; Springer: Berlin/Heidelberg, Germany, 1985. [ Google Scholar ]
28. Caughley, A.; Sellier, M.; Gschwendtner, M.; Tucker, A. A free-piston Stirling cryocooler using metal diaphgrams. Cryogenics 2016 , 80 , 8–16. [ Google Scholar ] [ CrossRef ] [ Scilit ]
29. Py, X.; Azoumah, Y.; Olives, R. Concentrated solar power: Current technologies, major innovative issues and applicability to west African countries. Renew. Sustain. Energy Rev. 2013 , 18 , 306–315. [ Google Scholar ] [ CrossRef ] [ Scilit ]
30. Khosravi, A.; Syri, S.; Pabon, J.J.; Sandoval, O.R.; Caetano, B.C.; Barrientos, M.H. Energy modeling of a solar dish/Stirling by artificial intelligence approach. Energy Convers. Manag. 2019 , 199 , 112021. [ Google Scholar ] [ CrossRef ] [ Scilit ]
31. Mancini, T.; Heller, P.; Butler, B.; Osborn, B.; Schiel, W.; Goldberg, V.; Buck, R.; Diver, R.; Andraka, C.; Moreno, J. Dish-Stirling systems: An overview of development and status. J. Sol. Energy Eng. 2003 , 125 , 135–151. [ Google Scholar ] [ CrossRef ] [ Scilit ]
32. Singh, U.R.; Kumar, A. Review on solar Stirling engine: Development and performance. Therm. Sci. Eng. Prog. 2018 , 8 , 244–256. [ Google Scholar ] [ CrossRef ] [ Scilit ]
33. Ahmadi, M.H.; Sayyaadi, H.; Hosseinzadeh, H. Optimization of output power and thermal efficiency of solar-dish Stirling engine using finite time thermodynamic analysis. Heat Transf.-Asian Res. 2015 , 44 , 347–376. [ Google Scholar ] [ CrossRef ] [ Scilit ]
34. May, J.R.; Brennan, D.J. Sustainability assessment of Australian electricity generation. Process Saf. Environ. Prot. 2006 , 84 , 131–142. [ Google Scholar ] [ CrossRef ] [ Scilit ]
35. Zayed, M.; Zhao, J.; Du, Y.; Kabeel, A.; Shalaby, S. Factors affecting the thermal performance of the flat plate solar collector using nanofluids: A review. Sol. Energy 2019 , 182 , 382–396. [ Google Scholar ] [ CrossRef ] [ Scilit ]
36. Coventry, J.; Andraka, C. Dish systems for CSP. Sol. Energy 2017 , 152 , 140–170. [ Google Scholar ] [ CrossRef ] [ Scilit ]
37. Barreto, G.; Canhoto, P. Modelling of a Stirling engine with parabolic dish for thermal to electric conversion of solar energy. Energy Convers. Manag. 2017 , 132 , 119–135. [ Google Scholar ] [ CrossRef ] [ Scilit ]
38. Zhu, S.; Yu, G.; Li, X.; Dai, W.; Luo, E. Parametric study of a free-piston Stirling cryocooler capable of providing 350 W cooling power at 80 K. Appl. Therm. Eng. 2020 , 174 , 115101. [ Google Scholar ] [ CrossRef ] [ Scilit ]
39. Walker, G.C.; Senft, J.R. Large free-piston Stirling engines. In Lecture Notes in Engineering ; Springer: Berlin/Heidelberg, Germany, 1985; pp. 216–221. [ Google Scholar ]
40. Mikalsen, R. Internal combustion and reciprocating engine systems for small and micro combined heat and power (CHP) applications. Chap.6. In Small and Micro Combined Heat and Power (CHP) Systems ; R Beith Woodhead Publishing: Sawston, UK, 2011; pp. 125–146. [ Google Scholar ]
41. Thu, K.; Saha, B.B.; Chua, K.J.; Bui, T.D. Thermodynamic analysis on the part-load performance of a microturbine system for micro/mini-CHP applications. Appl. Energy 2016 , 178 , 600–608. [ Google Scholar ] [ CrossRef ] [ Scilit ]
42. Rist, J.F.; Dias, M.F.; Palman, M.; Zelazo, D.; Cukurel, B. Economic dispatch of a single micro-gas turbine under CHP operation. Appl. Energy 2017 , 200 , 1–18. [ Google Scholar ] [ CrossRef ] [ Scilit ]
43. Oyewunmi, O.; Kirmse, C.J.; Pantaleo, A.; Markides, C. Performance of working-fluid mixtures in ORC-CHP systems for different heat-demand segments and heat-recovery temperature levels. Energy Convers. Manag. 2017 , 148 , 1508–1524. [ Google Scholar ] [ CrossRef ] [ Scilit ]
44. Dong, L.; Liu, H.; Riffat, S. Development of small-scale and micro-scale biomass fueled CHP systems—A literature review. Appl. Therm. Eng. 2009 , 29 , 2119–2126. [ Google Scholar ] [ CrossRef ] [ Scilit ]
45. Staffell, I.; Green, R. The cost of domestic fuel cell micro-CHP systems. Int. J. Hydrogen Energy 2013 , 38 , 1088–1102. [ Google Scholar ] [ CrossRef ] [ Scilit ]
46. Bartela, Ł.; Kotowicz, J.; Dubiel-Jurgaś, K. Investment risk for biomass integrated gasification combined heat and power unit with an internal combustion engine and a Stirling engine. Energy 2018 , 150 , 601–616. [ Google Scholar ] [ CrossRef ] [ Scilit ]
47. Qiu, S.; Solomon, L.; Rinker, G. Development of an integrated thermal energy storage and free-piston Stirling generator for a concentrating solar power system. Energies 2017 , 10 , 1361. [ Google Scholar ] [ CrossRef ] [ Scilit ]
48. Available online: https://www.microgen-engine.com/ (accessed on 15 September 2020).
49. Available online: https://www.qnergy.com/ (accessed on 15 September 2020).
50. Mahkamov, K. Thermal-engine-based small and micro combined heat and power (CHP) systems for domestic applications: Modelling micro-CHP deployment. Chap.18. In Small and Micro Combined Heat and Power (CHP) Systems ; R BeithWoodhead Publishing: Sawston, UK, 2011; pp. 459–509. [ Google Scholar ]
51. Available online: http://www.oekofen-e.com/en/engine/ (accessed on 15 September 2020).
52. De la Bat, B.J.G.; Dobson, R.T.; Harms, T.M.; Bell, A.J. Simulation, manufacture and experimental validation of a novel single-acting free-piston Stirling engine electric generator. Appl. Energy 2020 , 263 , 114585. [ Google Scholar ] [ CrossRef ] [ Scilit ]
53. Cardozo, E.; Erlich, C.; Malmquist, A.; Alejo, L. Integration of a wood pellet burner and a Stirling engine to produce residential heat and power. Appl. Therm. Eng. 2014 , 73 , 671–680. [ Google Scholar ] [ CrossRef ] [ Scilit ]
54. Zhu, S.; Yu, G.; Jongmin, O.; Xu, T.; Wu, Z.; Dai, W.; Luo, E. Modeling and experimental investigation of a free-piston Stirling engine-based micro-combined heat and power system. Appl. Energy 2018 , 226 , 522–533. [ Google Scholar ] [ CrossRef ] [ Scilit ]
55. Qiu, S.; Solomon, L. Free-piston stirling engine generators. In Energy Conversion—Current Technologies and Future Trends ; IntechOpen: London, UK, 2018; Available online: https://www.intechopen.com/chapters/62541 (accessed on 15 September 2020). [ CrossRef ] [ Scilit ]
56. Mraz, S.J. Infinia Uses Stirling Cycle for Solar Power and Air Conditioning. Available online: http://machinedesign.com/energy/infinia-uses-stirling-cycle-solar-power-and-air-conditioning (accessed on 11 August 2011).
57. Available online: www.qnergy.com/wp-content/uploads/2017/12/Download-the-PCK80-Brochure-SpecSheet.pdf (accessed on 4 October 2020).
58. Ferreira, A.C.; Silva, J.; Teixeira, S.; Teixeira, J.; Nebra, S.A. Assessment of the Stirling engine performance comparing two renewable energy sources: Solar energy and biomass. Renew. Energy 2020 , 154 , 581–597. [ Google Scholar ] [ CrossRef ] [ Scilit ]
59. Mazzetti, A.; Pret, M.G.; Pinarello, G.; Celotti, L.; Piskacev, M.; Cowley, A. Heat to electricity conversion systems for moon exploration scenarios: A review of space and ground technologies. Acta Astronaut. 2019 , 156 , 162–186. [ Google Scholar ] [ CrossRef ] [ Scilit ]
60. Available online: https://www.oekofen.com/ (accessed on 4 October 2020).
61. Available online: http://www.okofen-e.com/en/pellematic_condens_e/ (accessed on 4 October 2020).
62. Available online: http://www.okofen-e.com/en/pellematic_e_max/ (accessed on 4 October 2020).
63. Martini, W.R. Stirling Engine Design Manual ; US Department of Energy: Washington, DC, USA, 1978.
64. Finkelstein, T. Insights into the thermodynamics of Stirling cycle machines. In Proceedings of the Intersociety Energy Conversion Engineering Conference, Monterey, CA, USA, 7–11 August 1994; pp. 1829–1834. [ Google Scholar ]
65. Urieli, I.; Berchowitz, D.M. Stirling Cycle Engine Analysis ; Adam Hilger Ltd.: Bristol, NY, USA, 1984. [ Google Scholar ]
66. Li, R.; Grosu, L.; Queiros-Condé, D. Losses effect on the performance of a gamma type Stirling engine. Energy Convers. Manag. 2016 , 114 , 28–37. [ Google Scholar ] [ CrossRef ] [ Scilit ]
67. Li, R.; Grosu, L.; Li, W. New polytropic model to predict the performance of beta and gamma type Stirling engine. Energy 2017 , 128 , 62–76. [ Google Scholar ] [ CrossRef ] [ Scilit ]
68. Grosu, L.; Dobre, C.; Petrescu, S. Study of a Stirling engine used for domestic micro-cogeneration. Thermodynamic analysis and experiment. Int. J. Energy Res. 2015 , 39 , 1280–1294. [ Google Scholar ] [ CrossRef ] [ Scilit ]
69. Cheng, C.-H.; Yu, Y.-J. Numerical model for predicting thermodynamic cycle and thermal efficiency of a beta-type Stirling engine with rhombic-drive mechanism. Renew. Energy 2010 , 35 , 2590–2601. [ Google Scholar ] [ CrossRef ] [ Scilit ]
70. Araoz, J.A.; Cardozo, E.; Salomon, M.; Alejo, L.; Fransson, T.H. Development and validation of a thermodynamic model for the performance analysis of a gamma Stirling engine prototype. Appl. Therm. Eng. 2015 , 83 , 16–30. [ Google Scholar ] [ CrossRef ] [ Scilit ]
71. Ahmadi, M.H.; Ahmadi, M.-A.; Pourfayaz, F. Thermal models for analysis of performance of Stirling engine: A review. Renew. Sustain. Energy Rev. 2017 , 68 , 168–184. [ Google Scholar ] [ CrossRef ] [ Scilit ]
72. Toghyani, S.; Kasaeian, A.; Hashemabadi, S.H.; Salimi, M. Multi-objective optimization of GPU3 Stirling engine using third order analysis. Energy Convers. Manag. 2014 , 87 , 521–529. [ Google Scholar ] [ CrossRef ] [ Scilit ]
73. Hooshang, M.; Moghadam, R.A.; Nia, S.A.; Masouleh, M.T. Optimization of Stirling engine design parameters using neural networks. Renew. Energy 2015 , 74 , 855–866. [ Google Scholar ] [ CrossRef ] [ Scilit ]
74. Ahmadi, M.H.; Hosseinzade, H.; Sayyaadi, H.; Mohammadi, A.H.; Kimiaghalam, F. Application of the multi-objective optimization method for designing a powered Stirling heat engine: Design with maximized power, thermal efficiency and minimized pressure loss. Renew. Energy 2013 , 60 , 313–322. [ Google Scholar ] [ CrossRef ] [ Scilit ]
75. Li, R.; Grosu, L.; Queiros-Conde, D. Multi-objective optimization of Stirling engine using finite physical dimensions thermodynamics. Energy Convers. Manag. 2016 , 124 , 517–527. [ Google Scholar ] [ CrossRef ] [ Scilit ]
76. Xiao, G.; Sultan, U.; Ni, M.; Peng, H.; Zhou, X.; Wang, S.; Luo, Z. Design optimization with computational fluid dynamic analysis of beta-type Stirling engine. Appl. Therm. Eng. 2017 , 113 , 87–102. [ Google Scholar ] [ CrossRef ] [ Scilit ]
77. Formosa, F. Coupled thermodynamic–dynamic semi-analytical model of free piston Stirling engines. Energy Convers. Manag. 2011 , 52 , 2098–2109. [ Google Scholar ] [ CrossRef ] [ Scilit ]
78. Rogdakis, E.; Bormpilas, N.; Koniakos, I. A thermodynamic study for the optimization of stable operation of free piston Stirling engines. Energy Convers. Manag. 2004 , 45 , 575–593. [ Google Scholar ] [ CrossRef ] [ Scilit ]
79. Benvenuto, G.; de Monte, F. A simple approach to calculate the regenerator effectiveness in Stirling Machines. In Proceedings of the 7th International Conference on Stirling Cycle Machines, Waseda University, Tokyo, Japan, 5–8 November 1995. [ Google Scholar ]
80. Rogdakis, E.D.; Bormpilas, N.A.; Koniakos, I.K. A thermodynamic study of the thermal performance of free piston stirling prime movers. Saf. Eng. Risk Anal. 2002 , 2002 , 19–27. [ Google Scholar ] [ CrossRef ] [ Scilit ]
81. Formosa, F.; Despesse, G. Analytical model for Stirling cycle machine design. Energy Convers. Manag. 2010 , 51 , 1855–1863. [ Google Scholar ] [ CrossRef ] [ Scilit ]
82. Kwankaomeng, S.; Silpsakoolsook, B.; Savangvong, P. Investigation on stability and performance of a free-piston Stirling engine. Energy Procedia 2014 , 52 , 598–609. [ Google Scholar ] [ CrossRef ] [ Scilit ]
83. Tavakolpour-Saleh, A.; Zare, S.; Omidvar, A. Applying perturbation technique to analysis of a free piston Stirling engine possessing nonlinear springs. Appl. Energy 2016 , 183 , 526–541. [ Google Scholar ] [ CrossRef ] [ Scilit ]
84. Sowale, A.; Anthony, E.J.; Kolios, A.J. Optimisation of a quasi-steady model of a free-piston Stirling engine. Energies 2018 , 12 , 72. [ Google Scholar ] [ CrossRef ] [ Scilit ]
85. Available online: https://core.ac.uk/reader/77062392 (accessed on 10 October 2020).
86. Gedeon, D. Sage User’s Guide: Stirling, Pulse-Tube and Low-T Cooler Model Classes , 11th ed.; Gedeon Associates: Athens, Greece, 2016. [ Google Scholar ]
87. Chi, C.; Mou, J.; Lin, M.; Hong, G. CFD simulation and investigation on the operating mechanism of a beta-type free piston Stirling engine. Appl. Therm. Eng. 2020 , 166 , 114751. [ Google Scholar ] [ CrossRef ] [ Scilit ]
88. Prinsloo, G.; Dobson, R.; Mammoli, A. Model based design of a novel Stirling solar micro-cogeneration system with performance and fuel transition analysis for rural African village locations. Sol. Energy 2016 , 133 , 315–330. [ Google Scholar ] [ CrossRef ] [ Scilit ]
89. Hassan, A.; Torres-Perez, A.; Kaczmarczyk, S.; Picton, P. Vibration control of a Stirling engine with an electromagnetic active tuned mass damper. Control. Eng. Pract. 2016 , 51 , 108–120. [ Google Scholar ] [ CrossRef ] [ Scilit ]
90. Remiorz, L.; Kotowicz, J.; Uchman, W. Comparative assessment of the effectiveness of a free-piston Stirling engine-based micro-cogeneration unit and a heat pump. Energy 2018 , 148 , 134–147. [ Google Scholar ] [ CrossRef ] [ Scilit ]
91. González-Pino, I.; Perez-Iribarren, E.; Campos-Celador, A.; Terés-Zubiaga, J. Analysis of the integration of micro-cogeneration units in space heating and domestic hot water plants. Energy 2020 , 200 , 117584. [ Google Scholar ] [ CrossRef ] [ Scilit ]
92. Qiu, S.; Peterson, A. Linear dynamic modeling and numerical simulation of an STC Stirling convertor. In Proceedings of the 1st International Energy Conversion Engineering Conference (IECEC), Portsmouth, VA, USA, 17–21 August 2003. [ Google Scholar ]
93. Demko, R.; Penswick, L. Sage simulation model for technology demonstration convertor by a step-by-step approach. In Proceedings of the 3rd International Energy Conversion Engineering Conference (IECEC), San Francisco, CA, USA, 15–18 August 2005. [ Google Scholar ]
94. Roth, M.E.; Schreiber, J.; Pepper, S. Extended operation of stirling convertors. In Proceedings of the 2nd International Energy Conversion Engineering Conference (IECEC), Providence, RI, USA, 16–19 August 2004. [ Google Scholar ]
95. Bagg, S.D. Linear alternator technologies used for free piston Stirling engine. In Proceedings of the Nuclear and Emerging Technologies for Space, Woodlands, TX, USA, 21–23 March 2012. [ Google Scholar ]
96. Qiu, S.; Redinger, D.; Augenblick, J. The new generation infinia free-piston Stirling engine for micro-CHP and remote power applications. In Proceedings of the 3rd International Energy Conversion Engineering Conference (IECEC), San Francisco, CA, USA, 15–18 August 2005. [ Google Scholar ]
97. Li, R.; Qiu, S.; Gao, Y. Development of an advanced free piston Stirling engine of space power system. In Proceedings of the AIAA Propulsion and Energy 2019 Forum, Indianapolis, IN, USA, 9–22 August 2019. [ Google Scholar ]
98. Li, R.; Gao, Y.; Yanaga, K.; Qiu, S. Design of a free piston Stirling engine power generator. In Proceedings of the ASME International Mechanical Engineering Congress and Exposition, Salt Lake City, UT, USA, 11–14 November 2019. [ Google Scholar ]

Figure 1. Operation mode of a FPSE [26].

![Energies 14 07009 g001](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g001.png "Energies 14 07009 g001")

Figure 2. Classification of single-acting and double-acting FPSEs.

![Energies 14 07009 g002](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g002.png "Energies 14 07009 g002")

Figure 3. Two common models of single-acting working piston-displacer in tandem FPSE: (a) displacer sprung to working piston; (b) displacer piston sprung to ground.

![Energies 14 07009 g003](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g003.png "Energies 14 07009 g003")

Figure 4. A schematic view of a Dish Stirling.

![Energies 14 07009 g004](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g004.png "Energies 14 07009 g004")

Figure 5. Micro-CHP unit installed in laboratory@ Paris Nanterre University.

![Energies 14 07009 g005](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g005.png "Energies 14 07009 g005")

Figure 6. A schematic drawing of the forces acting on the working piston and the displacer (a) and the mass-spring-damper system approximation (b).

![Energies 14 07009 g006](https://www.mdpi.com/energies/energies-14-07009/article_deploy/html/images/energies-14-07009-g006.png "Energies 14 07009 g006")

Table 1. Experimental results of ÖkoFEN micro-CHP units tested in our laboratory (LEME).

| Micro-CHP Unit | FPSE Manufacturer | Heat Source | Thermal Input (kW) | Electric Power (kW) | Thermal Output (kW) | Flame Temperature (K) |
|---|---|---|---|---|---|---|
| Pellematic Condense | Microgen | Wood pellets | 10 | 0.7 | 7.9 | 950 |

Table 2. Comparison of the stable operation parameters of the RE-1000 obtained by several models.

| Parameters | Urieli et al. [65 ] | Walker et al. [27 ] | Rogdakis [80 ] | Rogdakis [78 ] | Exper. [65 ] |
|---|---|---|---|---|---|
| Frequency (Hz) | 33.2 | 32.9 | 32.9 | 30 | 30 |
| Phase angle (°) | −57.9 | −55.1 | −55.1 | −54.8 | −42.5 |
| Amplitude ratio | 0.62 | 0.63 | 0.63 | 0.87 | 1.06 |

Table 3. Summary of thermodynamic and dynamic models on FPSE from the literature.

| Authors | Model Type/Analysis Methods | Main Points |
|---|---|---|
| Rogdakis et al. [78 ] | Thermodynamic model | The dynamic balance equations are solved using a linearization technique. |
| Formosa and Despesse [81 ] | Thermodynamic model | The irreversibility of the heat exchangers and regenerator is expressed as a function of fluid flow rates. |
| Formosa [77 ] | Semi-analytical dynamic model | A coupled iterative technique solves the isothermal and the dynamic analysis. |
| Kwankaomeng et al. [82 ] | Thermodynamic and dynamic model | The isothermal analysis is combined with the approximation of the engine to a mass-spring-damper system, assuming harmonic motion of the pistons. |
| Tavakolpour-Saleh et al. [83 ] | Nonlinear analysis | The multiple-scale method uses two independent variables (fast-scale and slow-scale type), taking into account the nonlinear springs in the engine. |
| Sowale et al. [84 ,85 ] | 1D quasi-steady model | Damping and spring stiffness is calculated at each iteration, until convergence criteria is reached. |
| Ye et al. [25 ] | Multi-objective optimization | The response surface methodology (RSM) determines the optimal combination of the engine parameters. |
| Zhu et al. [54 ] | Thermo-acoustic analogy | The frequency and the piston displacement are solved implicitly using the thermo-acoustic theory. |
| Demko et al. [93 ] | Sage 1D model | The engine is simulated increasing the number of components, until reaching a more real model as possible. |
