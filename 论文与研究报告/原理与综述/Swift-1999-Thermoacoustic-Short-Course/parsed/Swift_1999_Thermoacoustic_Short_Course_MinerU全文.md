---
title: 'Thermoacoustic engines and refrigerators: A short course · MinerU全文'
record_role: machine-transcription
parse_method: MinerU
source_sha256: ad18d396747856d8e405c355654d4c8aba0dafb34cfc95b0f5da02e70b06ca1a
source_pages: 179
---

<table><tr><td>Title:</td><td>THERMOACOUSTIC ENGINES AND REFRIGERATORS: A SHORT COURSE</td></tr><tr><td>Author(s):</td><td>G.W. Swift RECEIVED AUG 1 9 1999</td></tr><tr><td></td><td>OSTI</td></tr><tr><td>Submitted to:</td><td>Joint 137th Meeting of Acoustical Societies of America and Europe PROCESSED FROM BEST AVAILABLE CO</td></tr></table>

Los Alamos NATIONALLABORATOR

![[mu_ad18d396_5562fb04f07ca06714ed.jpg]]

Los Alamos National Laboratory, an affirmative action/equal opportunity employer, is operated by the University of Califomia for the U.S. Department of Energy under contract W-7405-ENG-36. By acceptance of this article, the publisher recognizes that the U.S. Government retains a nonexclusive, royalty-free Icense to publish or reproduce the published form of this contribution, or to allow others to do so, for U.S. Government purposes. The Los Alamos National Laboratory requests that the publisher identify this article as work performed under the auspices of the U.S. Department of Energy. Form No. 836 R5 Form No 831

## DISCLAIMER

This report was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor any agency thereof, nor any of their employees, make any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately owned rights. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.

## DISCLAIMER

Portions of this document may be illegible in electronic image products. Images are produced from the best available original document.

Thermoacoustic engines and refrigerators

Greg Swift Condensed Matter and Thermal Physics Group Los Alamos National Laboratory Rough draft—-Berlin version

Winter 1999

## CONTENTS

1 Introduction 5   
1.1 Length scales 12   
1.2 Examples 14   
1.3 Thermoacoustics and conventional technology 22   
1.4 Notation. 23   
1.5 Computations (DeltaE). 26   
1.6 Animations 27   
1.7 Outline. 28   
1.8 Exercises. 29   
2 Waves 31   
2.1 Lossless acoustics; ideal resonators . 31   
2.2 Viscous and thermal effects in large channels . 38   
2.2.1 Viscous resistance . 38   
2.2.2 Thermal-relaxation conductance . 42   
2.3 Inviscid boundary-layer thermoacoustics 46   
2.4 General thermoacoustics 48   
2.4.1 The math 49   
2.4.2 The ideas 53   
2.5 Exercises . 62   
3 Power 66   
3.1 Acoustic power 67   
3.1.1 Acoustic power dissipation with dTm/dx = 0. 69   
3.1.2 Acoustic power—general thermoacoustics, with $\mu = 0$ 72   
3.2 Total power 76   
3.2.1 Traveling waves 82   
3.2.2 Standing waves 82   
3.3 A point of view for computations 83   
3.4 Examples 84   
3.5 Exercises . 87   
4 Efficiency 90   
4.1 Lost work and entropy generation . 90   
4.2 Exergy . 95   
4.3 Examples 100   
4.4 Exercises . 104   
5 Beyond Rott's thermoacoustics 107   
5.1 Tortuous porous media . . 110   
5.2 Turbulence. . . 110   
5.2.1 Minor losses 114   
5.3 Entrance effects and joining conditions 118   
5.3.1 Entrance effects . . 118   
5.3.2 Joining conditions . 119   
5.4 Streaming .. 125   
5.4.1 Gedeon streaming . . 127   
5.4.2 Olson streaming . 130   
5.4.3 Jet-driven tube streaming 134   
5.4.4 Streaming within a regenerator or stack 135   
5.4.5 Deliberate streaming. 135   
5.5 Harmonics and shocks 141   
5.6 Dimensionless groups 141   
5.7 Exercises. 141   
6 Hardware 147   
7 Measurements 148   
8 Common pitfalls 149   
9 Appendix 150   
9.1 Standing-wave engine . 150   
9.2 Standing-wave refrigerator 153   
9.3 Traveling-wave engine 157   
9.4 Traveling-wave refrigerator 168   
10 List of Symbols 173   
Bibliography 176

## Preface

I'm excited by the power density and efficiency recently achieved by thermoacoustic engines and refrigerators, and fascinated by new developments in thermoacoustics: deliberate superposition of steady flow, mixture separation via oscillating thermal diffusion. At night I often dream of a future world in which thermoacoustics is widely practiced. One dream had loudspeaker-driven thermoacoustic heat pumps atop the hot-water heaters in half the homes in Phoenix, pumping heat from room air into the hot water—the productión of a little cooling in the homes was a nice by-product. Another dream featured a small thermoacoustic system next to the liquid-nitrogen and liquid-oxygen dewars in back of our local hospital; this system had a gas-fired thermoacoustic engine driving several pulse-tube refrigerators, which provided the cooling necessary to liquefy air, distill it to produce purified nitrogen and oxygen, and reliquefy them for storage in the dewars. A third dream had hundreds of enormous combustion-powered thermoacoustic natural-gas liquefiers arrayed on an offshore platform, using the methane itself as the thermoacoustic working gas and filling a vacuum-insulated supertanker with LNG for transport to distant shores. Yet another dream showed an extensive thermoacoustic apparatus on Mars—a thermoacoustic engine driven by a small nuclear reactor produced 100 kW of acoustic power, which was piped to assorted thermoacoustic mixture separators and refrigerators, splitting atmospheric carbon dioxide and mined frozen water into pure $\mathtt { H _ { 2 } }$ and $0 _ { 2 }$ and liquefying these for use in fuel cells on each of the many robots scooting around building a colony for eventual human habitation.

The dreams are always different, but they have some features in common. First, they all feature low-tech hardware: big pipes and heat exchangers; welded steel, conventional shell-and-tube heat exchangers, molded plastic, etc. Second, I know that this simplicity is deceptive, because the technical challenge of designing this easy-to-build hardware is extreme. Third, there are no people in these dreams...because I know there are few people who are skilled in thermoacoustic engineering today. So I wake $\mathbf { u p } ,$ afraid that none of this will ever happen, afraid that integrated thermoacoustic process engineering is an opportunity that will never have a chance. ${ \bf S o , }$ I get up and I write another few paragraphs of this book, hoping to help newcomers learn basic thermoacoustics quickly, so they can design, build, and debug wonderful thermoacoustic systems of all kinds.

This is an introductory book, not a full review of the current status of the field of thermoacoustics. It is evolving from my March 1999 short course on this subject at the Berlin acoustics méeting. The hardware examples used here to illustrate the elementary principles are thermoacoustics apparatus developed at Los Alamos or with our close collaborators, and the mathematical approach to the gas dynamics and power flows closely follows that pioneered by Nikolaus Rott. (Time pressure induces me to stick with topics most familiar to me! and, indeed, the Los Alamos approach to thermoacoustics has been quite successful.) Many aspects of thermoacoustics will be introduced, in an attempt to help the reader acquire both an intuitive understanding and the ability to design hardware, build it, and diagnose its performance.

At Los Alamos, we have found it most productive to stay focused on experimental and development hardware, while maintaining several abstract points of view including phasor display of acoustic variables, a mental picture of gas motion, and an entropy-generation perspective on the second law of thermodynamics. Intuition is important because it helps us humans organize our thoughts. Mathematics is unavoidable, because it is the common language with which scientists and engineers communicate, and it allows us to interpolate and extend our knowledge quantitatively. But experiment is the source of all real truth, so the experiments are our most important and time-consuming activity at Los Alamos. Weaving intuition, mathematics, and experimental results together in this book, I will at first put the most emphasis on the mathematics, because without this common vocabulary we can get nowhere. Intuition gets second-highest emphasis, as appropriate for an introductory treatment. Experimental results get the least emphasis in this text. But please remember that the mathematical and intuitive discussions presented here are actually distillations of many experiments spanning many decades in many countries.

Many readers will find that they have only part of the background needed to learn thermoacoustics. Mechanical engineers and chemical engineers may have insufficient acoustics background; they should study an introductory treatment like Chapters 5-10 (and perhaps 14) in Fundamentals of Acoustics by Kinsler, Frey, Coppens, and Sanders. Acousticians, on the other hand, may need to study something like the first half of Fundamentals of Classical Thermodynamics by Van Wylen and Sonntag. Someone for whom the expression $i = \sqrt { - 1 }$ is unfamiliar must begin with a review of elementary complex arithmetic in an engineering mathematics text such as Advanced Engineering Mathematics by Kreysig.

The present rough draft of this book can be duplicated freely, and is distributed at no cost from the Los Alamos thermoacoustics web site, http://rott.esa.lanl.gov (maintained by Bill Ward). Be sure to get the animations as well as the book—studying this material without the animations would be as frustrating and ineffective as studying an engineering text without looking at the figures. On the website, the book is in pdf format, which can be viewed and printed using Adobe's free Acrobat Reader software. The photographs in Chapters 1 and 6 are color, so you might want to print at least some pages with a color printer.

## 1. INTRODUCTION

From thermodynamics [1. 2, 3], we know that the heat engine (sometimes known as a prime mover) produces work from high-temperature heat, and the refrigerator (or heat pump) uses work to pump heat. These devices are illustrated in Fig. 1.1, where the central rectangles represent the devices, operating between two thermal reservoirs at different temperatures T. In the heat engine, heat $Q _ { H }$ flows into the device from the reservoir at $T _ { H } ,$ while the device produces work and delivers waste heat $Q _ { 0 }$ into the reservoir at $\pmb { T _ { 0 } } .$ In the refrigerator, work flows into the device, which lifts heat $Q _ { C }$ from the reservoir at $\mathit { \Delta } \mathcal { T } _ { c }$ and rejects waste heat $Q _ { 0 }$ into the reservoir at $\pmb { T _ { 0 } }$

The laws of thermodynamics place bounds on the efficiency of such devices. The first law of thermodynamics is simply energy conservation: If the device is in steady state, what goes in must come out. So the sum of the energies going into the device must equal the sum of the energies going out. For the engine, this implies

$$
Q _ { H } = W + Q _ { 0 } ,\tag{1.1}
$$

while for the refrigerator

$$
\begin{array} { r } { Q _ { 0 } = W + Q _ { c } . } \end{array}\tag{1.2}
$$

The second law of thermodynamics, more subtle, says that the entropy of the universe can only increase or stay the same; it can never decrease. Here, the universe consists of three pieces: the two reservoirs and the device itself. If the device is in steady state then its entropy doesn't change with time, and work carries no entropy, so the universe consists of only the two reservoirs. Hence, for the engine the entropy increase $Q _ { 0 } / T _ { 0 }$ of the cold reservoir has to be greater than or equal to the entropy decrease $Q _ { H } / T _ { H }$ of the hot reservoir

$$
\frac { Q _ { 0 } } { T _ { 0 } } \geq \frac { Q _ { H } } { T _ { H } } ,\tag{1.3}
$$

(a)  
![[mu_ad18d396_1e439bfd8166e1807d20.jpg]]

(b)  
![[mu_ad18d396_e1ef8a6fa9da9899df1f.jpg]]  
Figure 1.1: A heat engine (a) and a refrigerator (b), showing energy flow directions and thermal reservoirs.

and similarly for the refrigerator

$$
{ \frac { Q _ { 0 } } { T _ { 0 } } } \geq { \frac { Q _ { C } } { T _ { C } } } .\tag{1.4}
$$

Combining Eq. (1.1) with Eq. (1.3) by eliminating the uninteresting variable, $Q _ { 0 } ,$ yields an inequality for the efficiency. The efficiency is what you want divided by what you have to spend to get it. For the engine, the efficiency $\eta$ is the work produced by the engine divided by the heat supplied by the hot reservoir:

$$
\eta = \frac { W } { Q _ { H } } \leq \frac { T _ { H } - T _ { 0 } } { T _ { H } } .\tag{1.5}
$$

The temperature ratio on the right is called the Carnot efficiency, which bounds the actual efficiency of all engines. Similarly, for the refrigerator the coefficient of performance COP is the heat of refrigeration divided by the work consumed by the device

$$
C O P = \frac { Q _ { C } } { W } \leq \frac { T _ { C } } { T _ { 0 } - T _ { C } } .\tag{1.6}
$$

The temperature ratio on the right is called the Carnot COP, which bounds the actual COP of all refrigerators.

In the real world, the device of Fig. 1.1a or Fig. 1.1b typically performs its function by taking an ideal gas or other fluid through a thermodynamic cycle or cycles. The Carnot cycle shown in Fig. 1.2 is one such cycle, which Carnot himself used to derive his well-known ultimate efficiency. This cycle is a favorite of textbooks because it is simple to analyze and has this highest possible efficiency. The Stirling cycle also has the Carnot efficiency, but we will not examine the idealized Stirling cycle or other textbook cycles in detail here, because real Stirling engines and refrigerators [4, 5] are so complex that the Stirling cycle itself, like the Carnot cycle, is of only academic interest. Parcels of gas in different parts of real Stirling machines experience totally different thermodynamic cycles, as is shown in Ani. Tashe $/ a .$ This animation shows a two-piston Stirling engine, with moving pistons taking the gas through a cycle of compression, rightward displacement, expansion, and leftward displacement. Between the pistons are two heat exchangers, colored to match the pistons, at temperatures $T _ { H } = 6 0 0 ^ { \circ } \mathrm { C }$ and $T _ { \mathbf { 0 } } = 3 0 ^ { \circ } C .$ Between these is a regenerator. The ellipses above the pistons are “indicator diagrams," which trace pressure vs volume for each piston; the difference between their purple elliptical areas is the net work W done by the gas in each cycle. The red arrows below each of the two heat exchangers show the heats $Q _ { H }$ and $Q _ { C }$ transfered to or from the gas in each cycle. The three moving vertical blue lines within the regenerator mark slices of the moving gas itself; together with the piston faces, these show clearly that the gas motion is small compared to the length of the engine. A typical slice of gas, such as the one indicated by the central blue line, never contacts either heat exchanger, so its cycle can hardly be analyzed by reference to a textbook heat-engine cycle. Furthermore, the smooth time dependences of the motion and pressure in real engines contrasts starkly with the four discrete steps in textbook cycles.

Nevertheless, the presence of four steps in typical thermodynamic cycles suggests the need for proper phasing between two or more phenomena. In the Carnot cycle shown in Fig. 1.2, the relevant phenomena are the pressure changes and the thermal contact to the reservoirs; the mechanism by which the thermal contact to the reservoirs is made and broken is left to our imagination. Conventional heat engines and refrigerators (e.g. Stirling) use piston motion both to cause pressure changes and to push the working gas through the heat exchangers, with the phasing between the pressure changes and the resulting thermal contact in the heat exchangers determined by the phasing of the pistons' motions, as shown in Ani. Tashe /a. Thermoacoustic heat engines and refrigerators also use gas motion to control thermal contact in the heat exchangers, with the phasing between motion and pressure determined by acoustics.

![[mu_ad18d396_12ad6dcc36c90654114f.jpg]]

![[mu_ad18d396_8edd0371eabb83473693.jpg]]  
(a)

![[mu_ad18d396_4abcf8eabf2abc140736.jpg]]

![[mu_ad18d396_85bf47022e9752497ef7.jpg]]

(b)  
![[mu_ad18d396_d48a21ee1c2748be0134.jpg]]

![[mu_ad18d396_669dda84e75af9343da6.jpg]]

![[mu_ad18d396_a3f72062ce8f6f43772b.jpg]]  
(c)

![[mu_ad18d396_de73774cdcbb4455cf85.jpg]]

![[mu_ad18d396_5f3c1c9d5a8c8422e69c.jpg]]  
(d)

![[mu_ad18d396_618a866380abaf0ed315.jpg]]

(e)  
![[mu_ad18d396_2a6cfdb8fc86dab62bda.jpg]]  
Figure 1.2: The Carnot cycle for an engine. (a)—(d) the four individual steps: isothermal compression, isentropic compression, isothermal expansion, isentropic expansion, respectively. (e) the combination of (a) through (d) produces a complete cycle, with the area enclosed on the PV plane equal to the net work produced by the engine. Reproduced from Walker [4].

![[mu_ad18d396_65d2c92aff1db6417fff.jpg]]  
Figure 1.3: Early Stirling engines, Reproduced from Senft [6].

Figure 1.3 shows the layout typical of a Stirling engine of a century ago. There are many moving parts: rotating crankshafts, moving connecting rods, reciprocating pistons. The mechanical parts dominated the thermal parts—in volume, weight, and visual impact—in the early Stirling machines. In the intervening century, engineers have sought to simplify such heat engines and refrigerators by elimination of moving parts. In 1969 William Beale was thinking about resonance effects when moving pistons bounced against gas compressibility in Stirling machines, and he realized that under the correct circumstances the forces on the connecting rods were small while the pistons continued to move correctly. This invention has led to what are called free-piston [7, 4] Stirling engines and refrigerators, as illustrated in Fig. 1.4, in which the moving pistons bounce against gas springs in resonance, and other moving parts such as connecting rods and crankshafts are eliminated. Another method to eliminate moving parts is the liquid-piston Stirling engine, also known as the Fluidyne engine [8], as shown in Fig. 1.5. In Fluidyne engines, liquid in two U tubes serves the function of the two pistons of the ordinary Stirling engine, confining and moving the working gas appropriately; the resonance phenomena are similar to those of the free-piston Stirling engines, but with gravity and liquid density contributing to the effective spring constant of the resonance. More recently, Peter Ceperley [9, 10] realized that the phasing between pressure and velocity in the thermodynamic elements of Stirling machines is the same as the phasing between pressure and velocity in a traveling acoustic wave, so he proposed eliminating everything but the working gas itself, using acoustics to control the gas motion and gas pressure. Figure 1.6 shows such a device, with two heat exchangers and a regenerator but no pistons or any other moving parts.

![[mu_ad18d396_a334abcfd6dcf0669481.jpg]]  
Figure 1.4: A typical free-piston Stirling engine. Reproduced from Walker [4]

Ceperley's work showed the need to consider sound-wave behavior [12, 13] in the working gas of Stirling devices, with variations in important variables such as pressure p and velocity u depending importantly and continuously on the coordinate x along the direction of gas motion, and with these x dependences due to inertial and compressive effects in the gas in addition to the effects of flow resistance.

Basic sound wave behavior is simple to derive. In acoustics, we often express quantities like pressure having sinusoidal time dependence in complex notation,

$$
\begin{array} { r } { p = p _ { m } + \mathrm { R e } \left[ p _ { 1 } \left( x \right) e ^ { i \omega t } \right] , } \end{array}\tag{1.7}
$$

with the pressure p expressed as a mean value pm plus the real part of a complex function of $\dot { p } _ { m }$ x times eiwt. We will use this style of notation throughout the book. The simplest acoustics $e ^ { i \omega t }$ derivation, for sound propagating along the direction x, starts with three simple equations. ${ \pmb x } ,$

![[mu_ad18d396_cd006729b66b2d7068d8.jpg]]  
Figure 1.5: The Fluidyne (liquid piston) Stirling engine. Reproduced from West [11].

![[mu_ad18d396_90ef05c3bc0578ed9398.jpg]]  
Figure 1.6: The traveling-wave engine concept. Reproduced from one of Ceperley's patents.

The first is this version of the momentum equation:

$$
i w { \rho } _ { m } u _ { 1 } = - \frac { d p _ { 1 } } { d x } .\tag{1.8}
$$

The force on the gas is the pressure gradient $d p _ { 1 } / d x ,$ which according to Newton's law must equal the mass density $\rho _ { m }$ times the acceleration ¿ωui. The second is this version of the continuity equation:

$$
\dot { w } \rho _ { 1 } + \rho _ { m } \frac { d u _ { 1 } } { d x } = 0 ,\tag{1.9}
$$

which expresses mass conservation, with the time derivative of mass density at any point, iu ${ \boldsymbol { \rho } } _ { 1 }$ , arising from the gradient of mass flux density $d ( \rho _ { m } u _ { 1 } ) / d x$ at that point. The third is a part of the equation of state of the gas

$$
\frac { p _ { 1 } } { \rho _ { 1 } } = \left( \frac { \partial p } { \partial \rho } \right) _ { s } = a ^ { 2 } ,\tag{1.10}
$$

which gives the proportionality constant $a ^ { 2 }$ —the square of the sound speed-linking pressure changes with density changes under adiabatic conditions. Combining these three equations by eliminating ${ \pmb u } _ { 1 }$ and $\pmb { \rho _ { 1 } }$ gives a simple wave equation

$$
p _ { 1 } + \frac { a ^ { 2 } } { \omega ^ { 2 } } \frac { d ^ { 2 } p _ { 1 } } { d x ^ { 2 } } = 0 .\tag{1.11}
$$

whose solution is sines and cosines of x. (Technically this is a Helmholtz equation, since the time derivatives are written as $\omega ^ { \prime } \mathsf { s } . )$

This simple wave equation is appropriate for plane waves under spatially isothermal, temporally adiabatic conditions—in other words, the gas average temperature is independent of x and the gas exchanges no heat with its surroundings on the time scale of the acoustic oscillations. Amazingly, it was only 20 years ago that anyone was able to derive the correct wave equation for sound waves propagating in a duct with a temperature gradient in the duct along the direction of propagation, and with significant thermal contact between the gas and the side walls of the duct. This equation [14]

$$
\left[ 1 + \left( \gamma - 1 \right) f _ { \kappa } \right] p _ { 1 } + \frac { \rho _ { m } a ^ { 2 } } { \omega ^ { 2 } } \frac { d } { d x } \left( \frac { 1 - f _ { \nu } } { \rho _ { m } } \frac { d p _ { 1 } } { d x } \right) - \frac { a ^ { 2 } } { \omega ^ { 2 } } \frac { f _ { \kappa } - f _ { \nu } } { 1 - \sigma } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \frac { d p _ { 1 } } { d x } = 0\tag{1.12}
$$

was published by Nikolaus Rott in 1969. You can see pieces of Eq. (1.11) in it. The $f _ { \kappa }$ and $f _ { \nu }$ factors in Rott's equation arise from thermal and viscous contact with the walls of the duct.

In this book, we will try to integrate all of the aforementioned threads together into a coherent picture, with physical, mathematical, and intuitive foundations. We will try to develop a vision of these heat engines and refrigerators, using the kind of mathematics that Rott developed, and with many of the features of the work of Beale, West, and especially Ceperley—the elimination of moving parts whenever possible to achieve simplicity and reliability, while maintaining the highest possible efficiency.

![[mu_ad18d396_ca91977ddf0c89ec6e27.jpg]]

![[mu_ad18d396_f7281091b8052d9f65cf.jpg]]  
Figure 1.7: The type of devices under consideration in this book.

As illustrated in Fig. 1.7, this integration will generally involve devices in which the gasenclosing cavity comprises some kind of acoustic resonator that determines the relationship between gas motion and pressure, in which heat exchangers exchange heat with external heat reservoirs, and in which a stack or a regenerator between the heat exchangers make the device function as a thermoacoustic standing-wave device or a Stirling device.

In one respect, thermoacoustic devices are more interesting than crankshaft-based systems, such as that shown in Fig. 1.3, in which hardware motion was determined, by design, and exerted direct control on gas motion. In thermoacoustic systems, including linear-motor, free-piston Stirling systems, oscillating pressure gradients cause the oscillating motion, and the oscillating motion causes the oscillating pressure gradients; analyzing a dynamical system having such interdependent causes and effects is inherently challenging.

## 1.1. Length scales

The important length scales in thermoacoustic engines and refrigerators are illustrated in Fig. 1.8.

Along the wave-propagation direction x (the direction of motion of the gas), the wavelength of sound $\lambda = a / f ,$ where f is the oscillation frequency, is an important length scale. When the gas inertia itself provides the resonance behavior, the whole length of the apparatus may typically be a half wavelength or a quarter wavelength; but when massive mechanical components participate meaningfully in the resonance behavior, as in free-piston Stirling systems, the size of the system is typically much smaller than the wavelength. In all cases, the lengths of heat-exchange components are much shorter than the wavelength.

Another important length scale in the x direction is the gas displacement amplitude |x1, which is the velocity amplitude $\left| u _ { 1 } \right|$ divided by the angular frequency $\omega = 2 \pi f$ of the wave. This displacement amplitude is often a very large fraction of the stack length or regenerator length, and may be larger than the lengths of the heat exchangers at either end of the stack or regenerator. The displacement amplitude is always shorter than the wavelength.

![[mu_ad18d396_a6459d94c6dd184ffb2a.jpg]]  
Figure 1.8: Important length scales in a thermoacoustic device.

Perpendicular to the direction of motion of thé gas, the characteristic lengths are the thermal penetration depth $\delta _ { \kappa } = \sqrt { 2 k / \omega \rho c _ { p } } = \sqrt { 2 \kappa / \omega }$ and the viscous penetration depth $\delta _ { \nu } = \sqrt { 2 \mu / \omega \rho } = \sqrt { 2 \nu / \omega } .$ where k and κ are the thermal conductivity and diffusivity of the $\mathtt { g a s } , \mu$ and ν are its dynamic and kinematic viscosities, and $c _ { p }$ is its specific heat per unit mass at constant pressure. These characteristic lengths tell us how far heat and momentum can diffuse laterally during a time interval of the order of the period of the acoustic oscillation divided by $\pi .$ For gas at distances much greater than these penetration depths from the nearest solid boundary, the sound wave feels no thermal contact or viscous contact with the solid boundaries; in parts of the apparatus whose lateral dimensions are of the order of the viscous and thermal penetration depths, the gas does feel both thermal and viscous effects from the boundaries. Clearly the heat exchange components in thermoacoustic systems must have lateral dimensions of the order of $\delta _ { \kappa }$ or smaller, in order to exchange heat with the working gas.

In the ratio of these two penetration depths,

$$
\frac { \delta _ { \nu } } { \delta _ { \kappa } } = \sqrt { \frac { \mu c _ { p } } { k } } = \sqrt { \sigma } \lesssim 1 ,\tag{1.13}
$$

the frequency and the density cancel out, leaving the ratio of viscosity times heat capacity to thermal conductivity. This ratio is called the Prandtl number σ of the gas. It's close to unity for typical gases, so viscous and thermal penetration depths are comparable. Hence thermoacoustic engines and refrigerators will always suffer from substantial viscous effects.

In ordinary audio acoustics, the displacement amplitude of gas is much smaller than the thermal and viscous penetration depths, which in turn are much smaller than the wavelength. In thermoacoustic engines and refrigerators typically the gas displacement amplitudes are much larger than the penetration depths, but still much smaller than acoustic wavelengths:

$$
\delta _ { \kappa } \ll | x _ { 1 } | \ll \lambda .\tag{1.14}
$$

[Incidentally, the standard expression for bulk attenuation of sound, $\alpha ,$ can easily be expressed in terms of the viscous and thermal penetration depths. From Eq. 7.36 in Kinsler, Frey, Coppens, and Sanders (3rd ed.) [12]:

$$
\alpha = \pi ^ { 2 } \frac { \omega } { a } \left[ \frac { 4 } { 3 } \frac { \delta _ { \nu } ^ { 2 } } { \lambda ^ { 2 } } + \left( \gamma - 1 \right) \frac { \delta _ { \kappa } ^ { 2 } } { \lambda ^ { 2 } } \right] .\tag{1.15}
$$

From this viewpoint, viscous bulk sound attenuation is small if the viscous penetration depth is small compared to the wavelength, and thermal attenuation is small if the thermal penetration depth is small compared to the wavelength. The ratios of penetration depths to wavelength are strongly frequency dependent, because the wavelength is proportional to 1/f while the penetration depths are proportional to ${ \sqrt { 1 / f } } .$ So low frequency, long wavelength sound suffers the least bulk attenuation. The presence of solid boundaries in the resonators and heat-exchange components of thermoacoustic engines and refrigerators has thus far caused boundary-based attentuation to far exceed such bulk attenuation.]

## 1.2. Examples

I will repeat the same four examples of real thermoacoustic hardware in almost every chapter in this book, introducing the examples briefly here and examining various aspects in greater detail at appropriate places in subsequent chapters. Mark these pages (with clips or tape or ...) so you can refer back to them easily. The four examples include two engines and two refrigerators; two standing wave systems and two traveling wave systems; and two research systems and two systems bringing thermoacoustics toward  more practical stage of development. In this chapter, I will just briefly introduce the four examples, discussing their purpose, overall function, and characteristic dimensions.

![[mu_ad18d396_58be84f82e8f55052b9f.jpg]]  
Figure 1.9: Standing-wave engine example: Tektronix researchers with a heat-driven refrigerator, 1995. The resonator, horizontal, has standing-wave engines on each end. The two-stage orifice pulse tube refrigerator stands vertically near the right end. Photo courtesy of Kim Godshalk.

The standing-wave heat engine was part of the heat-driven cryogenic refrigerator [15] assembled at Tektronix in 1994 and shown in Figs. 1.9 and 1.10. This system was under development in order to provide a small amount of cryogenic refrigeration for electronic components, with the system powered by red-hot electric heaters and hence having no moving parts. The resonator lies horizontally in the figures, with standing-wave thermoacoustic engines on each end, and an upward side branch near the right end connecting to the two-stage orifice pulse tube refrigerator. Water cooling lines, seen extending through the tabletop in Fig. 1.9, removed waste heat from the engines and the refrigerator. Our focus in this book will be on the heat-driven engines and the resonator, which delivered up to 1 kW of acoustic power to the pulse tube refrigerator, and delivered 500 W to the pulse tube refrigerator with an efficiency of 23% of the Carnot efficiency. We hoped to make the system as small as possible, and sufficiently efficient that the necessary electrical power could be supplied from an ordinary wall plug. The working gas was helium at a pressure of 30 atmospheres. The sound speed of helium is about 1000 meters per second at room temperature, and the horizontal length of the resonator in Figs. 1.9 and 1.10 is about half a meter, so you would expect that the half-wavelength resonance in this system would be near 500 Hz; and, indeed, the system operated at 350 Hz. At this pressure and frequency, the thermal penetration depth in helium is approximately 0.2 mm; correspondingly, the spacing in the heat exchange components was approximately 1 mm.

![[mu_ad18d396_bded79dc0ba521352f3e.jpg]]  
Figure 1.10: Scale drawing of the Tektronix resonator and its standing-wave engines. The annular spaces around each end are thermal insulation. The spacing in stacks and heat exchangers is not to scale. The upward opening near the right end is the connection to the two-stage pulse tube refrigerator.

The key idea in this and other standing-wave engines is that the gas in the stack must experience thermal expansion when the pressure is high and thermal contraction when the pressure is low. Thus the gas in the stack does work every acoustic cycle, pumping acoustic power into the standing wave. The standing wave in turn provides the oscillating pressure, and the oscillating motion that causes the gas in the stack to experience the oscillating temperature responsible for the thermal expansion and contraction. The velocity of the gas along the stack's temperature gradient is 90° out of phase with the oscillating pressure, so imperfect thermal contact between gas and stack is required to enable the thermal expansion and contraction steps to be in phase with the oscillating pressure. These complex, coupled oscillations appear spontaneously whenever the temperature at the hot ends of the stacks is high enough.

The standing-wave refrigerator shown in Figs. 1.11 and 1.12 was assembled by Bob Reid to investigate the deliberate superposition of steady flow [16] with the oscillating flow of the standing thermoacoustic refrigeration process. The refrigerator was driven by four loudspeakers, enclosed in the obvious aluminum housings shown in Fig. 1.11. The left and right pairs of loudspeakers were driven 180° out of phase, to produce a standing wave in the toroidal resonator having essentially one full wavelength around the circumference of the torus, with pressure nodes centered in the top and bottom sections of the resonator and pressure anti-nodes near the loudspeakers. With the resonator filled with a mixture of 92% helium and 8% argon at three atmospheres of pressure, this resonance occurred at 94 Hz. Slow steady flow of the gas mixture from top to bottom through the heat exchange components, superiposed on the thermoacoustic oscillating flow, produced cold gas leaving the resonator at the bottom pressure node. The spacing in the heat exchange components was-about 1 mm, a few times the thermal penetration depth in this gas.

![[mu_ad18d396_0affe1797f4f343bcf81.jpg]]  
Figure 1.11: Standing-wave refrigerator example: Loudspeaker-driven-research apparatus for investigating the superposition of deliberate steady flow on the oscillatory thermoacoustic flow.

![[mu_ad18d396_2cbf4d3a5ae85c80d454.jpg]]  
Figure 1.12: Schematic of the standing-wave refrigerator example.

The key idea in this and other standing-wave refrigerators is that the gas in the stack experiences partly adiabatic temperature oscillations, in phase with the standing-wave pressure oscillations, and oscillating standing-wave displacements in phase with the pressure oscillations and hence in phase with those temperature oscillations. Thus the gas in the stack cools a little as it is displaced downward in Fig. 1.12, and warms a little as it is displaced upwards. Imperfect thermal contact between gas and stack enables the required heat transfer at the extremes of the motion. (The superimposed steady-flow velocity in this particular apparatus was much smaller than the standing-wave oscillatory velocity, as we will discuss in Chapter 5.)

The traveling-wave engine shown in Figs. 1.13 and 1.14 was built by Scott Backhaus to demonstrate Stirling cycle engine thermodynamics with no moving parts, and to investigate the issues affecting its efficiency [17]. Heat was supplied to the engine electrically, and waste heat was removed by a water stream, delivering acoustic power to the resonator. Some of that acoustic power was dissipated in the resonator, but most was delivered to  variable acoustic load, the small vertical cylinder near the center of Fig. 1.13. This engine has delivered power to the resonator with 40% of the Carnot efficiency. Suppression of steady flow around the small torus containing the heat exchangers is crucial for this high efficiency, as we will discuss in Chapter 5. Thirty-atmosphere helium fills the system, oscillating at 80 Hz. The resonator is essentially half-wavelength, with pressure oscillations 180° degrees out of phase at the right end of the fat portion on the right and in the small torus containing the heat exchangers on the left. The highest velocity occurs in the center of the resonator, at the small end of the long cone.

![[mu_ad18d396_629405c73325d66514e1.jpg]]  
Figure 1.13: Traveling-wave engine example: A research apparatus for initial Los Alamos studies of the performance of a traveling-wave-engine.

The key idea in this and other traveling-wave engines is that the gas in the regenerator experiences thermal expansion when the pressure is high and thermal contraction when the pressure is low. Thus the gas in the regenerator does work every acoustic cycle, pumping acoustic power into the sound wave. The sound wave in turn provides the oscillating pressure, and oscillating motion that causes the gas in the regenerator to experience the oscillating temperature responsible for the thermal expansion and contraction. These complex, coupled oscillations appear spontaneously whenever the temperature at the hot end of the regenerator is high enough. The velocity of the gas along the regenerator's temperature gradient is substantially in phase with the oscillating pressure, so excellent thermal contact between gas and regenerator is required to cause the thermal expansion and contraction steps to be in phase with the oscillating pressure. This thermal contact is achieved by making the channel size in the regenerator much smaller than the thermal penetration depth.

Finąlly, the traveling-wave refrigerator—an orifice pulse-tube refrigerator— shown in Figs. 1.15 and 1.16 was built at Cryenco for liquefaction of natural gas [18, 19]. At about 3 atmospheres, natural gas (methane) liquefies at 120 Kelvin; this refrigerator provided 2 kW of refrigeration at that temperature, with a COP as high as 23% of the Carnot COP. The working gas was helium at a pressure of thirty atmospheres, driven at 40 Hz by a thermoacoustic engine through a resonator, not shown in the figures. The dimensions of the parts shown in the figures are much smaller than the 25 m wavelength of the sound wave, so resonance phenomena are of no concern in this refrigerator.

![[mu_ad18d396_32fd4cf9488660b12a00.jpg]]

![[mu_ad18d396_179f85704ce740ce9dbe.jpg]]  
Figure 1.14: The traveling-wave engine. (a) Overview, as in the photo. (b) The heart of the traveling-wave engine.

![[mu_ad18d396_feda7c21517721b29a59.jpg]]  
Figure 1.15: Traveling-wave refrigerator example: the Cryenco 2 kW orifice pulse-tube refrigerator.

![[mu_ad18d396_9a5c35f20599be9fc13a.jpg]]  
Figure 1.16: Schematic of the Cryenco orifice pulse-tube refrigerator. "P" indicates the location of a pressure sensor.

The key idea in this and other Stirling, pulse-tube, or traveling-wave refrigerators is that gas near the cold heat exchanger must be displaced into the open space of the pulse tube, adiabatically cooled, and displaced back through the cold heat exchanger where it can absorb heat from the load. The sound wave must provide oscillating pressure and oscillating displacement with this required phasing.

## 1.3. Thermoacoustics and conventional technology

With these four examples of thermoacoustic devices in mind, consider what the advantages and disadvantages of thermoacoustic systems might be in comparison to the energy conversion systems that are in widespread use, such as the internal combustion engine, the steam turbine, the reverse Rankine or vapor comipression refrigeration cycle, the gas turbine, etc.

![[mu_ad18d396_770d49b7cab2a84a0e1a.jpg]]  
Figure 1.17: Different technologies exhibit different trade-offs between cost and efficiency.

Those conventional systems have moving parts; from that point of view one might think of them as being less reliable and more expensive than thermoacoustic devices. However, decades of investment in engineering development have given these conventional devices high reliability, and decades of manufacturing experience have given them low cost. Thermoacoustic devices seem to have the immediate potential to have comparable high reliability and low cost, because they use no moving parts, no exotic materials, and no close tolerances. Realizing this potential is one of our challenges.

Decades of investment in the engineering deyelopment of conventional energy-conversion devices has also given them very high efficiencies. Today's automobile engines convert the heat of combustion to shaft work with over 20% efficiency; the largest diesel engines achieve 40%. Vapor-compression refrigeration systems with $C O P \mathbf { s }$ above 50% of Carnot's are common. Thermoacoustic devices haven't yet achieved such high efficiencies; increasing thermoacoustic device efficiency into this range is another of our challenges.

It is important to realize that the efficiency of a new technology need not exceed that of older technologies in order to succeed commercially. This point is illustrated in Fig. 1.17. The Stirling refrigerator is quite old, and in principle it can have Carnot's COP. However, high COP can only be achieved at great expense, as the mass of heat exchange metal, quality of lubricants, etc. is made exceedingly large. For instance, qualitatively, the efficiency vs capital cost of a Stirling refrigerator might resemble the Stirling curve in Fig. 1.17, with very high efficiency possible if you're willing to spend an exponentially large amount of money building the refrigerator. However, in the commercial world, energy costs are currently low enough that no one chooses to invest so much capital to achieve high efficiency. Instead, vapor-compression refrigeration is used for almost all real-world refrigeration systems, because it has lower capital'cost than Stirling refrigeration, even though the COP of vapor compression refrigeration can in principle never approach the ultimate COP of the Stirling cycle. Furthermore, each application requires a different compromise between construction costs and efficiency; for example, the vapor-compression air-conditioning system for a large office building in Phoenix might lie higher on the efficiency-cost curve than the vapor-compression chiller in a soft-drink vending machine in Seattle. If thermoacoustics turns out to have an efficiency-cost curve somewhere to the left of existing technologies, it will succeed in some commercial markets. Whether the terminus of the thermoacoustics curve is higher or lower than that of older technologies is not as important as whether the capital costs will be lower at modest efficiencies.

## 1.4. Notation

We pause now to carefully establish the notation to be used throughout the book for timedependent variables such as pressure. Except in Chapter 5, we will assume that all time dependence is purely sinusoidal, at frequency f and angular frequency $\omega = 2 \pi f$ .Then variables such as pressure could be written

$$
\begin{array} { r } { p ( x , t ) = p _ { m } + C ( x ) \cos \left[ \omega t + \phi ( x ) \right] . } \end{array}\tag{1.16}
$$

Consider this expression carefully. It indicates that we are considering the pressure to be the sum of a mean value $\scriptstyle { p _ { m } } ,$ which is independent of both position x and time $\mathbf { ^ { t } } ,$ and an oscillating part that oscillates in time at angular frequency ω. Both the amplitude A and phase $\phi$ of the time oscillation are functions of position x.

It is much more convenient to rewrite Eq. (1.16) as

$$
\begin{array} { r } { p ( x , t ) = p _ { m } + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] , } \end{array}\tag{1.17}
$$

where $p _ { 1 } ( { \pmb x } )$ is a complex function of x such that

$$
| p _ { 1 } ( x ) | _ { _ { - } } = C ( x ) , _ { _ { - } }\tag{1.18}
$$

$$
\mathrm {  ~ \ p h a s e { \dot { \ p } } _ { 1 } ( x ) ] ~ } = ~ \phi ( x ) .\tag{1.19}
$$

This notation is convenient because a single symbol with subscript 1 stands for both amplitude and phase, and because all the shortcuts of complex arithmetic can be used (with care). In this book, all variables with subscript 1 will be complex.

Sometimes we get lazy or forgetful, and we don't write Re[] explicitly, and we just say that $p _ { 1 } ( x )$ is the oscillating pressure; but of course we really always mean that $\mathtt { R e } [ p _ { 1 } ( x ) e ^ { i \omega t } ]$ is the oscillating pressure, and $p _ { m } + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right]$ is the pressure. Sometimes we abbreviate further to simply ${ \pmb p } _ { 1 }$ , leaving the fact that is depends on x to memory.

One of the reasons that thermoacoustics is at first confusing is that the acoustic variables are wavelike functions of both position and time. Remember that the time dependence is assumed to be exactly sinusoidal in our acoustic approximation; the spatial dependence need not be sinusoidal but sometimes turns out to be nearly so over portions of an apparatus. When talking about the phase of such a wave, it is occasionally necessary to explicitly say temporal phase to identify interest in the phase of the time oscillation, not the x dependence.

To be sure this notation is clear, we will revisit the continuity equation, Eq. (1.9) above. Consider a lossless acoustic wave oscillating adiabatically along the x direction in a gas with no overall temperature gradient along x. We can write the pressure ${ \pmb p } ,$ density $\rho ,$ and velocity u as

$$
\begin{array} { r } { p ( x , t ) \ = \ p _ { m } + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] , } \end{array}\tag{1.20}
$$

$$
\rho ( x , t ) \ = \ \rho _ { m } + \mathrm { R e } \left[ \rho _ { 1 } ( x ) e ^ { i \omega t } \right] ,\tag{1.21}
$$

$$
u ( x , t ) \ = \ \mathrm { R e } \left[ u _ { 1 } ( x ) e ^ { i \omega t } \right] ,\tag{1.22}
$$

with the absence of um in Eq. (1.22) indicating that no steady wind is superimposed on $u _ { m }$ the oscillating flow. Defining $a ^ { 2 }$ as the proportionality constant linking adiabatic density changes and adiabatic pressure changes,

$$
a ^ { 2 } d \rho = d p ,\tag{1.23}
$$

we can simplify the most general continuity equation

$$
{ \frac { \partial \rho } { \partial t } } + \nabla \cdot \left( \rho \mathbf { v } \right) = 0\tag{1.24}
$$

in one dimension, yielding

$$
\frac { \partial p } { \partial t } + a ^ { 2 } \frac { \partial } { \partial x } \left( \rho u \right) = 0 .\tag{1.25}
$$

Substituting our complex notation expressions Eqs. (1.20)-(1.22) into Eq. (1.25), and neglecting the term involving the product of $\pmb { \rho _ { 1 } }$ and ${ \pmb u } _ { 1 }$ , which is smaller than the other surviving terms, yields

$$
\mathrm { R e } \left[ i \omega p _ { 1 } ( x ) e ^ { i \omega t } \right] + \rho _ { m } a ^ { 2 } \frac { \partial } { \partial x } \mathrm { R e } \left[ u _ { 1 } ( x ) e ^ { i \omega t } \right] = 0 .\tag{1.26}
$$

Note the freedom we have to interchange the orders of space and time derivatives, and to interchange the order of derivatives and the “real" operator. Hence, we can always write an equation like Eq. (1.26) in an abbreviated form:

$$
i \omega p _ { 1 } + \rho _ { m } a ^ { 2 } \frac { d u _ { 1 } } { d x } = 0 .\tag{1.27}
$$

This expression is mathematically true, but in terms of physically realistic variables it is an abbreviation of Eq. (1.26).

For further clarification of the complex notation, consider some simple waves. A pure traveling wave, traveling in the positive x direction, as shown in Ani. Wave $/ \mathfrak { t } ,$ is represented in complex notation as

$$
\dot { p } _ { 1 } ( x ) = C e ^ { - i k x } ,\tag{1.28}
$$

where $| C |$ is the amplitude, and the phase of the complex number $\boldsymbol { \sigma }$ defines the overall temporal phasing of the wave relative to our choice of $t = 0$ . A pure standing wave, as shown in $\mathbf { A } \mathbf { n } \mathbf { i } .$ Wave $/ \mathsf { s } ,$ is represented in complex notation as

$$
p _ { 1 } ( x ) = C \cos k x .\tag{1.29}
$$

In a graphical representation of this complex notation known as a phasor diagram, the complex variables are plotted on the complex plane with the real axis horizontal and the imaginary axis vertical. Conventionally, arrows from the origin "point" to each such complex variable, and we will follow this convention here, as shown in Fig. 1.18. If you imagine a phasor $\xi _ { 1 }$ in a phasor diagram rotating counterclockwise at angular frequency $\omega ,$ then the time-dependent variable $\xi ( t ) = \mathbb { R e } \left[ \xi _ { 1 } \overset { \cdot } { e ^ { i \omega t } } \right]$ represented by the phasor is the projection of the phasor on the real axis

(a)  
![[mu_ad18d396_8af2ad871b476b71a147.jpg]]

(b)  
![[mu_ad18d396_4a0e05c6b942fa3806a4.jpg]]  
Figure 1.18: Phasors show complex variables in the complex plane. (a) Two sinusoidally time-dependent variables $p ( t )$ and $U ( t )$ , with U leading $\pmb { p }$ by $\mathfrak { 3 0 ^ { \circ } }$ . (b) The phasor representation of these two variables can be imagined as two vectors whose magnitudes are the amplitudes of $\pmb { p }$ and $\begin{array} { r } { \boldsymbol { U } , } \end{array}$ rotating counterclockwise at angular frequency $\omega .$ The true, timedependent values of the associated variables are the projections on the real axis of these rotating phasors.

Phasor diagrams are extremely useful for indicating the relationships in magnitude and phase among many variables in complicated thermoacoustic systems, as we shall see later. For example, if a second variable is proportional to i times a first variable, the phasor for the second variable will point $9 0 ^ { \circ }$ counter-clockwise from the direction of the phasor for the first variable, and we say that the second variable "leads" the first variable by $9 0 ^ { \circ }$ . We use phasor diagrams so frequently that we usually neglect to label the axes "Real part" and "Imaginary part." Usually we are only illustrating the relative magnitudes and phases of variables—not their actual magnitudes—so we also neglect to provide quantitative scale. In fact, in such cases we often display variables having different units on the same plot, to convey phase information without cluttering the figure with scale information, as in Fig. 1.19 where both ${ \pmb p } _ { 1 }$ and $\pmb { U _ { 1 } }$ are shown for the simple lossless waves of Eqs. (1.28) and (1.29)

![[mu_ad18d396_0f8b5767d96af01b23ee.jpg]]  
Figure 1.19: Phasors at seven locations in standing and traveling waves. The pressure ${ \pmb p } _ { 1 }$ and the volumetric velocity $\pmb { U _ { 1 } }$ are shown. (a) Phasor diagram for Ani. Wave $/ { \mathsf s } ,$ corresponding to Eq.(1.29). (b) Phasor diagram for Ani. Wave $/ \mathfrak { t } ,$ corresponding to Eq. (1.28). The phase of ${ \pmb p _ { 1 } }$ at the left edge of the animation screen is arbitrarily chosen to be zero in both cases.

## 1.5. Computations (DeltaE)

Most of the first half of the book emphasizes the development of intuition, lumped-element impedance estimates, and the promotion of a particular point of view. However, in daily practice of thermoacoustics I spend most of my time working with numerical integrations of the thermoacoustic equations, using DeltaE. It is hard to imagine progress in thermoacoustics today without use of such software.

Any one-dimensional acoustic wave equation, such as Eq. (1.11) or (1.12), is derived from a momentum equation such as Eq. (1.8) and a continuity equation such as Eq. (1.9) with appropriate details added as needed. Noting that the momentum and continuity equations can be solved for $d p _ { 1 } / d x$ and $d U _ { 1 } / d x$ respectively, an easy method of numerical integration suggests itself: ${ p } _ { 1 } ( { \pmb x } )$ can be obtained by integrating the momentum equation with respect to ${ \pmb x } ,$ while simultaneously $\bar { U } _ { 1 } ( x )$ is obtained by integrating the continuity equation with respect to x. We will see in future chapters that the x dependence of mean temperature in stacks is subtle and can be determined by consideration of the conservation of energy flux through the stack, leading to a third fundamental differential equation that can be integrated to obtain $\pmb { T } _ { m } ( \pmb { x } )$ simultaneously with the other two equations.

DeltaE [20] integrates these one-dimensional equations, in a geometry given by the user as a sequence of segments, such as ducts, compliances, transducers, and thermoacoustic stacks or regenerators. In each segment, DeltaE uses locally appropriate momentum, continuity, and energy equations, controlled by local parameters (e.g. area or perimeter) and by global parameters (e.g. frequency and mean pressure). Solutions $p _ { 1 } ( x ) , U _ { 1 } ( x )$ , and $\pmb { T } _ { m } ( \pmb { x } )$ are found for each segment and are matched together at the junctions between segments to piece together $p _ { 1 } ( x ) , U _ { 1 } ( x )$ , and $\mathcal { T } _ { m } ( x )$ for the entire apparatus.

It is clear that this solution $T _ { m } ( x ) , p _ { 1 } ( x ) , U _ { 1 } ( x )$ , is only determined uniquely if one real and two complex boundary conditions are imposed, because the governing equations comprise one real plus two complex coupled first-order equations in one real plus two complex variables. This is true whether considering a single segment or a one-dimensional string of segments with each joined to its neighbor(s) by continuity of $\mathcal { T } _ { m } , p _ { 1 }$ , and $\pmb { U _ { 1 } }$ . If all boundary conditions are known at the intial segment, then the integration is utterly straightforward. But usually some of the boundary conditions are known elsewhere. Under such conditions, DeltaE uses a shooting method, by guessing and adjusting any unknown boundary conditions at the initial segment to achieve desired boundary conditions elsewhere. The user of DeltaE enjoys considerable freedom in choosing which variables are used as boundary conditions and which are computed as part of the solution. For example, in a simple plane-wave resonator, DeltaE can compute the input impedance as a function of frequency, or the resonance frequency for a given geomery and gas, or the length required to give a desired resonance frequency, or even the concentration in a binary gas mixture required to give a desired resonance frequency in a given geometry.

Hoping that the usefulness of this book will greatly outlive version 4 of DeltaE, I have put typical DeltaE i/o files for each·of the four examples that we will re-examine throughout the book in the Appendix. For interested readers, these show how to configure a simple file for DeltaE for each of theșe examples, and may occasionally be consulted to learn a specific dimension of a piece of apparatus. We find that DeltaE and experiment agree best when considerable detail is included in the DeltaE file; often, we have over 50 segments in a file to account for all the little details in hardware as built. To avoid intimidating the newcomer, the first two files in the Appendix are stripped of such details; they use only the key segments necessary to describe the hardware. The third file, for the traveling-wave engine, is fully encumbered with details, typical of what we actually work with; if you àre new to DeltaE or to thermoacoustics, skip it! The fourth file, for the orifice pulse-tube refrigerator, includes only about 25% of the segments actually used to model this refrigerator, in order to hide Cryenco proprietary information.

The user's guide to DeltaE is available at http://rott.esa.lanl.gov, and it might be consulted occasionally while studying this book. A beta version of the code itself can be obtained from Bill Ward at ww@lanl.gov. The use of DeltaE in this book for examples requiring numerical integration is convenient for me, because it's the only thermoacoustics code I routinely use. However, I believe that some other codes, such as Sage by Gedeon [21], Thermoacoustica by Tominaga [22], and Regen3 by Radebaugh's group [23], are also accurate and useful for modeling thermoacoustic devices. Although each code has strengths and weaknesses, the good ones are in agreement on the fundamentals.

## 1.6. Animations

The computer animation “Ani. Wave" discussed above is the first of many animations to be used in this book. Studying them is vital.

These animations run in Windows 95, Windows 98, in full-screen DOS windows in Windows computers, and in raw DOS. They may run'a little jerkily on old 386 computers.

Unless you have a DOS emulator, Macs are not an option.

Remember to use the “filename /option" form of the command line. Example: "wave $/ \mathbf { t } ^ { \mathfrak { N } }$ starts the Wave animation with traveling-wave settings; "wave $/ { \bf s } ^ { \mathfrak { N } }$ starts it with standingwave settings. If you start an animation without typing the option, you may find yourself automatically sequencing through options in the order that I most often use in lectures.

For Windows 95 or 98, keep the same subdirectory structure on your hard disk as you received, so that the shortcuts in folder Win95-98 know where to find the exeçutable files. Open the Win95-98 folder and double-click a shortcut icon to launch the appropriate animation /option. Example: Clicking "Wave\_s (Standing)" executes the DOS command line "Wave $/ \mathbf { s } ^ { \mathfrak { N } }$

For Windows 3.1, execute these the programs from a DOS-box window, or exit windows and run in raw DOS. To run the animations, "cd" to the DOS directory and type the program name with the option character, if any (e.g. /s), as specified here in the text. Either upper or lower case is acceptable.

Warning: If the typed text in the animations looks scrunched or incorrectly located, your DOS window is not using its default font settings or is not sized to the full screen. Edit properties to set font and screen size to defaults, and switch to full-screen DOS window (alt-enter). Better yet, avoid this problem in the first place by never starting an animation from a DOS window that's been modified: If you use Windows 3.1, exit to DOS and change directories to where the animations are; if you use Windows 95 or 98, start a fresh DOS window from “Start...Programs...MS-DOS Prompt" and change directories to where the animations are. These methods apparently cause Windows to open the DOS window in its default state. (This hassle arises because the animations were written in Microsoft Quickasic, which uses DOS settings and fonts for locating and typing text. Hence the coordinate system where text appears on the screen in the animations depends on the DOS font settings.)

## 1.7. Outline

This book will not provide a complete description of how these heat engines and refrigerators work—for that, consult publications specific to each type, such as Refs. [7, 5, 4, 24, 25]. Instead, this book promotes one point of view allowing an understanding of all these devices. This point of view is based firmly on acoustics, with thermodynamics added as necessary.

Chapter 2 —Waves—examines the oscillatory pressure and velocity. This includes the relevant fundamentals of ordinary acoustics, resonance phenomena in resonators, and viscous damping and thermal contact to the side walls of the channel in which the wave propagates. One climax of that chapter is Rott's wave equation, Eq. (1.11) above. After studying the Waves chapter, you should be able to visualize and understand the overall wave behavior of a thermoacoustic apparatus, based on a drawing or description. This process involves thinking about all the dimensions of the apparatus in comparison to $\lambda , \delta _ { \kappa } ,$ and $\delta _ { \nu } ,$ locating the nodes and antinodes of $\pmb { p _ { 1 } }$ and $U _ { 1 }$ , identifying which parts of the wave are inertial and which are compliant, identifying which parts are affected by viscous flow resistance or by thermal relaxation effects, and predicting approximately the relative phases of ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ throughout the apparatus. At a coarse, qualitative level this process can be done by eye and by hand; quantitative results can be obtained by numerical integration of the momentum

and continuity equations.

The power—both thermal and acoustic—is of greatest interest in heat engines and refrigerators, so Chapter 3 —Power—adds these concepts to the pressure and velocity discussion. Acoustic power, the time-averaged product of ${ \pmb p } _ { 1 }$ and $\boldsymbol { \mathcal { U } _ { 1 } }$ , is produced in engines and consumed by refrigerators. Total power, which is the power that is subject to the first law of thermodynamics, is of even greater importance. After studying the Power chapter, you should be able to understand thermoacoustic engines and refrigerators in terms of energyconservation, power flows, and acoustic-power dissipation and production. Quantitative results can be obtained as desired from products of the dynamical variables of Chapter 2.

This completes the portion of the book based closely on the work of Rott.

The second law of thermodynamics, which puts bounds on the performance of thermoacoustic engines and refrigerators, forms the basis of Chapter 4 -Efficiency. Key concepts are entropy generation, which can be subdivided according to location and mechanism, and exergy, which provides a quantitative figure of merit for thermodynamic devices and their interactions with their environment. Together, these concepts provide a standard, formal accounting method for sources of inefficiency. After studying this chapter, you should have an understanding of thermodynamic efficiency that goes beyond what is taught in standard physics courses and undergraduate engineering courses, and you should be able to visualize and understand the locations and mechanisms of irreversibility in a thermoacoustic apparatus, and account quantitatively for the irreversibilities.

Chapter 5 introduces many important issues that go beyond the low-amplitude, monofrequency approximation implicit in Rott's work. These issues include turbulence, entrance effects, superimposed'steady flow, and harmonics. While the first four chapters stand on a firm foundation, these high-amplitude issues are at the. frontier of current knowledge. However, they are of great concern in real devices, which usually operate at high amplitude in order to achieve high power per unit volume.

Chapter 6 presents practical construction techniques we've adopted at Los Alamos, Chapter 7 outlines methods of measurement used to diagnose thermoacoustic behavior, and Chapter 8 describes common pitfalls. An appendix gives some DeltaE files; I may drop this from the final version of the book, because I suspect they will become obsolete quickly.

A symbol table and references are included t the end

(General overview references: fluid dynamics [26, 27], thermodynamics [2, 3, 28, 29, 1], acoustics [12, 13], thermoacoustics [30, 25, 31, 32, 33], Stirling systems [34, 7], pulse-tube refrigeration [24, 35].)

## 1.8. Exercises

1.1 Review the ideal-gas equation of state and other properties of ideal gases: For your favorite working gas, and your favorite temperature and pressure, look up γ, calculate the $\gamma ,$ sound speed, density, and isobaric specific heat. Look up the viscosity and thermal conductivity. Pick your favorite frequency. Calculate λ, $\delta _ { \kappa } ,$ and $\delta _ { \nu }$ . Compare these lengths to various dimensions in your favorite piece of thermoacoustics hardware. Do you know the order of magnitude of $| x _ { 1 } | \}$ Verify that $\delta _ { \nu } / \delta _ { \kappa } = \sqrt { \sigma } .$ (If you don't have a personal favorite gas, etc., then use air at 300 K and atmospheric pressure, 440 Hz, and dimensions in your office. Estimate $\left| x _ { 1 } \right|$ using the fact that conversational acoustics has $\left. p _ { 1 } \right. \simeq 1 0 ^ { - 6 }$ bar.)

1.2 Can you think of any other length scale in simple-harmonic oscillatory motion and thermodynamics in an ideal gas, besides $\lambda , \left| x _ { 1 } \right| , \delta _ { \nu } ,$ and $\delta _ { \kappa } ?$ If you can, when would it be important in thermoacoustics? How can we be sure we haven't forgotten an important length?

1.3 Do you know roughly what a kitchen refrigerator costs, and what is the cost of the electricity it consumes each year? If so, would you expect most people to choose to pay 50% more to buy a refrigerator that uses 50% less electricity?

1.4 A mixture of helium and argon has a sound speed of 500 m/s at 300 Kelvin. What is the concentration of argon in the mixture?

1.5 Thermodynamics review: Show that the ratio of isothermal compressibility to adiabatic compressibility is the same as the ratio γ of isobaric to constant-volume specific heats. Hence, show that $\rho _ { m } a ^ { 2 } = \gamma p _ { m }$

1.6 More thermodynamics review: Derive an expression for isothermal sound speed, instead of the usual adiabatic sound speed. Show that the isothermal sound speed is about 18% lower than the true, adiabatic speed in air, for which $\gamma = 7 / 5$ . Can you think of circumstances in which sound propagates isothermally?

1.7 Review of complex notation: Derive Eq. (1.11) from whatever version of the starting equations (momentum, continuity, and state) you are most familiar with. Express all variables as in Eq. (1.7), and justify the neglect of all terms that you have to throw away to get to the desired answer. Review how the time derivatives in the starting equations become iω in the complex acoustic approximation.

## 2. WAVES

The focus of this chapter will be on the dynamic variables, pressure and velocity, for wave propagation in the x direction in a channel or duct. Adopting increasingly sophisticated perspectives on the continuity equation, we will see how oscillations in pressure are coupled to spatial gradients in velocity. Adopting increasingly sophisticáted perspectives on the momentum equation, we will see how oscillations in velocity are coupled to spatial gradients in pressure. Coupling these pictures together yields wave propagation. Initially, we will examine the lossless concepts of inertia and compressibility, later adding viscous loss to the momentum equation and thermal hysteresis (and gain) to the continuity equation. We'll alternate between formal mathematics, figures, and computer animations, to integrate quantitative tools with intuition. Throughout, we will assume monofrequency, constantamplitude, small oscillations—an approximation that we will, for brevity, refer to simply as "the acoustic approximation."

The principle variables are oscillatory pressure ${ \pmb { p _ { 1 } } }$ and oscillatory volumetric velocity $U _ { 1 } ,$ which is the integral of the x component of the velocity, ${ \pmb u } _ { 1 }$ , over the cross sectional area A of the channel. At the transition between two channels, $\scriptstyle { \bar { U } } _ { 1 }$ and ${ \pmb p } _ { 1 }$ are taken to be continuous. For example, at a transition from a first duct to a second duct, $U _ { 1 }$ out of the first duct has nowhere to go but into the second duct, so $U _ { 1 f } = U _ { 1 s } ,$ and hence if the areas of the ducts are $A _ { f }$ and $A _ { s }$ then the velocity (not volumetric velocity!) changes by the factor $A _ { f } / A _ { s }$ At such a junction between two ducts, ${ \pmb p } _ { 1 }$ must also be continuous, because any pressure discontinuity represents a shock front, outside the realm of the acoustic approximation and today's thermoacoustics.

## 2.1. Lossless acoustics; ideal resonators

The simplest lossless version of the acoustic continuity equation, $\mathtt { E q } .$ (1.9) or (1.27), can be rewritten

$$
p _ { 1 } ~ = ~ - \frac { \gamma p _ { m } } { i \omega A \Delta x } \Delta U _ { 1 }\tag{2.1}
$$

$$
= \mathrm { \Omega } - { \frac { 1 } { i \omega C } } \Delta U _ { 1 }\tag{2.2}
$$

for the short length $\Delta x$ of channel of cross-sectional area A shown in Fig. 2.1a. To arrive at these equations, we have used Eq. (1.10) to express $\pmb { \rho _ { 1 } }$ in terms of ${ \pmb p } _ { 1 }$ , and used the ideal-gas identity $\rho _ { m } a ^ { 2 } = \gamma p _ { m }$ , which is derived in one of the exercises at the end of Chapter 1. In Eq. (2.2),

$$
C = \frac { V } { \gamma p _ { m } }\tag{2.3}
$$

(a)  
![[mu_ad18d396_565e49db9e9d35ce0f30.jpg]]

(b)  
![[mu_ad18d396_d776deb526ac331d6f11.jpg]]

![[mu_ad18d396_bffd39f5f9f4216d6554.jpg]]  
Figure 2.1: (a) A short channel in which the compressibility of the gas is important. (b) Symbolic impedance diagram of the channel. The symbol $\pmb { C }$ indicates compliance. (c) Two possible phasor diagrams for the channel.

is called the compliance of the channel. The compliance is the ratio of the volume $V = A \Delta x$ of the channel to the compressibility $\gamma p _ { m } ;$ larger volume or lower $\big ( \mathfrak { s o f t e r } ^ { 9 9 } \big )$ compressibility means greater compliance. This combination of variables gives us the springy, compressive properties of the gas in the channel.

Similarly, the lossless version of the acoustic momentum equation, Eq. (1.8), can be rewritten

$$
\Delta p _ { 1 } ~ = ~ - { \dot { w } } \frac { \rho _ { m } \Delta x } { A } { U _ { 1 } }\tag{2.4}
$$

$$
\begin{array} { r l } { \mathrm { ~  ~ \lambda ~ } } & { { } = { \bf \Sigma } - i \omega L { \cal U } _ { 1 } , } \end{array}\tag{2.5}
$$

for the short length of channel shown in Fig. 2.2a. Note that the channel illustrated is the same as in Fig. 2.1a; the figures differ only because we're focusing our attention on different properties of this channel in the two situations. In Eq. (2.5),

$$
L = \frac { \rho _ { m } \Delta x } { A }\tag{2.6}
$$

is called the inertance of the channel. It is the product of the gas density $\rho _ { m }$ and the length ∆x divided by the cross-sectional area A of the channel. This combination of variables describes the inertial properties of the gas in the channel.

Writing the continuity and momentum equations in this way allows an accurate analog between acoustic systems and ac electrical circuits, motivating the symbolic "circuit" diagrams of Figs. 2.1b and 2.2b. The analog of oscillating pressure ${ \pmb p } _ { 1 }$ is ac voltage; the analog of oscillating volumetric velocity $U _ { 1 }$ is ac current. The analog of compliance is capacitance to ground, and the analog of inertance is series inductance. (Note that "inertance" sounds a little like the electrical word "inductance" and a little like the mechanical word "inertia.")

![[mu_ad18d396_f985e603afc989af9540.jpg]]  
Figure 2.2: (a) A short channel in which the inertia of the gas is important. (b) Symbolic impedance diagram of the channel. The symbol L signifies the inertance. (c) Two possible phasor diagrams for the channel.

We will rely on this point of view extensively, because I suspect that many readers (especially physicists and electrical engineers) have some prior experience with ac electric circuits. However, I've noticed that other engineers and scientists often gain no intuition from what is to them a totally unfamiliar analog. Such readers, unfamiliar with ac electrical circuits, can take the "circuit diagrams" to be no more than abstract representations of the acoustic impedance networks themselves, and I will try to use nothing but acoustic terminology in referring to these diagrams. When you look at the symbol for inertance in Fig. 2.2b, think of a long, coiled tube through which the dense gas must. accelerate. When you look at the symbol for resistance in figures later in this chapter, think of a kinked tube through which the gas must overcome viscous resistance. When you look at the symbol for compliance in Fig. 2.1b, think of a spongy cushion between the two parallel lines, whose gap changes in response to pressure.

Figures 2.1c and 2.2c show possible phasor diagrams for a compliance and an inertance, respectively. In Fig. 2.1c, note that $| U _ { 1 } + \Delta U _ { 1 } |$ could be either larger or smaller than $| \bar { U } _ { 1 } |$ the only strict requirement imposed by Eq. (2.2) is that $\Delta U _ { 1 }$ must lag ${ \pmb p } _ { 1 }$ by $9 0 ^ { \circ }$ . Similarly, in Fig. 2.2c, the only strict requirement imposed by Eq. (2.5) is that $\Delta p _ { 1 }$ must lag $\pmb { U _ { 1 } }$ by $9 0 ^ { \circ }$ . Beyond these requirements, anything is possible, depending on the relative magnitudes and phases of ${ \pmb p } _ { 1 }$ and $\pmb { U _ { 1 } }$

Usually, both the inertance and the compliance of a channel simultaneously contribute to the behavior of the wave propagation in the channel, as illustrated in Fig. 2.3 for a channel of differential length dx. As before, note that $d p _ { 1 }$ lags $\scriptstyle { \bar { U } } _ { 1 }$ by $9 0 ^ { \circ }$ , and $d U _ { 1 }$ lags ${ \pmb p } _ { 1 }$ by $9 0 ^ { \circ }$

The complex ratio $Z = - p _ { 1 } / U _ { 1 }$ , which is called the impedance, is of great utility in discussing acoustic systems. Sometimes we refer to the impedance at a location in a wave, but sometimes we refer to the impedance of a component so that $Z = - \Delta p _ { 1 } / U _ { 1 }$ is related to the pressure difference across the component or $Z = - p _ { 1 } / \Delta U _ { 1 }$ describes the change in volumetric velocity caused by the component. In the latter modes, Eq. (2.5) shows that the impedance of an inertance is $Z = i \omega L ,$ and Eq. (2.2) shows that the impedance of a compliance is $Z = 1 / i \omega C .$

![[mu_ad18d396_2ad53b18c416d55fd164.jpg]]  
Figure 2.3: (a) A very short channel in which both the compressibility and the inertia of the gas are important. (b) Symbolic impedance diagram of the channel. (c) A possible phasor diagram for the channel.

The double Helmholtz resonator, illustrated in Fig. 2.4, is a simple acoustic resonator consisting of two bulbs, each of volume $V ,$ connected by a short neck with length $\Delta x$ and cross-sectional area A. All dimensions are shorter than the acoustic wavelength, so the lumped-impedance models of Figs. 2.1 and 2.2 are directly applicable: Each bulb is a compliance $^ { C , }$ and the neck connecting the two bulbs is an inertance $L .$ (In the simple, textbook Helmholtz resonator, the compliance of the neck and inertial effects in the compliances are assumed negligible.) Imagine the inertial mass of gas in the neck bouncing back and forth sinusoidally against forces exerted by the gas springs in the two bulbs. Combining Eqs. (2.2) and (2.5) appropriately (or remembering that series ac electric circuits are resonant when the sum of the impedances is zero), it is easy to show that ${ \pmb p } _ { \mathbf { 1 } }$ and $U _ { 1 }$ are nonzero only if

$$
i \omega L + 2 / i \omega C = 0 ,\tag{2.7}
$$

and hence that the resonance frequency of the Helmholtz resonator is given by

$$
( 2 \pi f ) ^ { 2 } = \omega ^ { 2 } = \frac { 2 } { L C } = 2 \frac { \gamma p _ { m } } { \rho _ { m } } \frac { A } { V \Delta x } .\tag{2.8}
$$

At this frequency, either Eq. (2.2) or (2.5) gives the relative magnitudes of ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ , and their relative phases. The relative phases are illustrated in the phasor diagram in Fig. 2.4c, where we have arbitrarily picked the phase of $U _ { 1 }$ in the inertance to be zero.

In lossless acoustic resonators more complicated than the Helmholtz resonator, the acoustic waves are described by the coupled differential equations (1.8) and (1.9). Hence, to understand lossless acoustic waves in a duct or resonator, we must simultaneously keep in mind the concepts of compliance and inertance. First consider the standing wave shown in Ani. Wave $/ \mathsf { s } .$ This animation illustrates a wave oscillating horizontally in a duct of uniform cross section. The uppermost graph shows the pressure of the gas in the wave as a function of position and time. The middle graph shows the velocity in the gas as a function of position and time (with positive velocity to the right). The lower part of the display shows the motion, or displacement, of the gas in the duct. The moving vertical lines move with the gas; imagine that these lines are massless sheets of cellophane or thin clouds of smoke moving with the gas.

![[mu_ad18d396_420d60ec06242da2654a.jpg]]  
Figure 2.4: The double Helmholtz resonator. (a) Schematic of the resonator, comprising two bulbs connected by a neck. (b) Impedance diagram of the resonator. (c) Phasor diagram.

First focus attention on the velocity node, where the gas never moves. This region of the duct is functionally similar to a bulb of the double Helmholtz resonator described above. With zero velocity, Eq. (2.5) indicates that there should be no spatial pressure gradient, and indeed the animation shows that the oscillating pressure has no gradient in the vicinity. Hence, the inertance per unit length in the duct is irrelevant in this vicinity. The nonzero oscillating ${ \pmb p } _ { 1 }$ in this vicinity, however, indicates that Eqs. (2.1) and (2.2) are important. This region of the duct has compliance per unit length, so that the oscillating pressure can only occur in the presence of a spatial gradient in velocity, which is needed to supply and remove the mass necessary to cause the local density to increase and decrease. The presence of i in Eq. (2.2) indicates a $9 0 ^ { \circ }$ temporal phase shift between the pressure oscillations and the oscillating velocity gradient; this temporal phase relationship is also evident in the animation.

Now focus attention on one of the pressure nodes in Ani. Wave $/ \mathbf { s } .$ This region of the duct is functionally similar to the neck of the double Helmholtz resonator described above. Here, ${ \displaystyle p _ { 1 } = 0 , }$ so Eq. (2.2) indicates that gradients in velocity must be zero and that the compliance per unit length in this portion of the duct is irrelevant. However, the nonzero oscillating velocity in this region and Eq. (2.5) show that here the oscillating pressure must have nonzero gradients, as seen in the animation; additionally, both Eq. (2.5) and the animation indicate a $9 0 ^ { \circ }$ temporal phase shift between pressure gradient and velocity.

Precisely at the pressure node in the standing wave, the compliance per unit length is irrelevant. Precisely at the velocity node, the inertance per unit length is irrelevant. Everywhere else in the standing wave, where neither ${ \pmb p } _ { 1 }$ nor $U _ { 1 }$ are zero, both inertance and compliance per unit length contribute to the behavior of the wave. (This is, in fact, what makes it a wave instead of a lumped-impedance oscillator such as the double Helmholtz resonator.) Near the pressure antinodes, the compliance per unit length is more important than the inertance per unit length; near the velocity antinodes, the inertance per unit length is more important than the compliance per unit length.

While separate regions of predominantly compliance and predominantly inertance are apparent in the standing wave, in the traveling wave illustrated in Ani. Wave /t each location is a time-shifted replica of any other location, with inertance and compliance temporally alternating in importance at each location. If you focus your attention on one location in the animation, you should be able to ${ \mathfrak { s e e } } ^ { \mathfrak { n } }$ this alternation. In wave propagation, the thermophysical properties responsible for compliance, $\gamma p _ { m }$ , and for inertance, $\rho _ { m } ,$ are combined to form the sound speed $a = \sqrt { \gamma p _ { m } / \rho _ { m } }$

Phasor diagrams for both wave animations are shown in Fig. 1.19.

Example: standing-wave engine. The resonator of the standing wave engine illustrated in Figs. 1.9 and 1.10 is particularly simple. It is essentially a half-wavelength-long resonator, closed at both ends so that the velocity nodes are at the ends and the pressure node is in the center. This overall wave shape is illustrated roughly in Ani. Standing /k. However, note in Fig. 1.10 that the diameter of the central portion of the resonator is slightly smaller than the diameter of the two ends. This diameter variation serves several functions, most of which we will discuss in Chapter 5. One of those functions is to lower the resonance frequency slightly below $f = a / 2 \Delta x$ , where $\Delta x$ is the overall length of the resonator. This frequency reduction is considered quantitatively in one of the exercises at the end of this chapter. However, using the concepts of inertance and compliance, it is easy to see qualitatively how this diameter variation leads to a lower resonance frequency: The half-wavelength resonator can be thought of crudely as consisting of two compliances on the two ends with an inertance the middle, so that the resonance crudely resembles that of the double Helmholtz resonator shown in Fig. 2.4. If the diameter of the inertance is reduced, L goes up according, to Eq. (2.6), and hence the resonance frequency of the CLC resonator goes down as suggested by Eq. (2.8). From an alternative point of view, if the diameter of the compliances is increased, the value of C goes up according to Eq. (2.3), and again the resonance frequency of the CLC circuit goes down according to Eq. (2.8). In the example drawn to scale in Fig. 1.10, but with the branch to the refrigerators sealed off, the resonance frequency was 10% lower than the frequency for which the half wavelength equals the length of the apparatus. (Nevertheless, we will continue to speak loosely of such a resonator as a half wavelength resonator, because this phrase captures the essential nature of the standing wave: pressure maxima at the two ends and a velocity maximum in the center.)

Example: standing-wave refrigerator. The standing-wave refrigerator resonator, shown in Figs. 1.11 and 1.12, also employs variations in diameter (visible in Fig. 1.11) to reduce the resonance frequency below that for which a full wavelength would equal the total path length around the resonator. The apparatus has left-to-right symmetry, so that driving the loudspeaker pairs 180° out of phase ensures that pressure nodes appear at the top center and bottom center of the resonator. Hence, these are the locations of high velocity, where inertance is important. The parts of the resonator near the loudspeakers have high pressure amplitude and hence are the regions where compliance is important. These compliance portions are enlarged in diameter relative to the inertance portions, so the resonance frequency is reduced. 1in

Example: lumped approximation to half-wavelength resonator. For the uniformdiameter half-wavelength resonator shown in Fig. 2.5a, the most accurate impedance diagram would have an infinite number of inertances $d L$ and compliances dC, as suggested by the large number of them in Fig. 2.5a, which would yield the sinusoidal x dependences of ${ \pmb p } _ { 1 }$ and $\pmb { U _ { 1 } }$ shown. Numerical integrations for accurate results might have 10 or 20 such segments, with each being integrated by a Runge-Kutta method so that each is effectively subdivided even further. However, the essence of the resonance is simply what is shown in the phasor diagram of Fig. 2.5b, with pressure oscillations at the two ends having equal magnitudes and opposite phases, and the velocity in the center phased $9 0 ^ { \circ }$ from the pressures. Hence, if numerically accurate results are not needed, the essence can be captured with the simpler impedance diagram shown in Fig. 2.5c, in which the central third of the resonator is modeled as an inertance and the two ends as compliances. The accuracy of this crude approximation is suggested by the close resemblance of the trapezoidal distributions for ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ , as compared to the sinusoids of Fig. 2.5a. (For further consideration of the accuracy of this crude approximation, see one of the exercises at the end of the chapter.)

![[mu_ad18d396_7f0b3c123e7b662b8d1e.jpg]]  
Figure 2.5: (a) The half-wavelength resonator, with sinusoidal $p _ { 1 } ( x )$ and $\bar { U } _ { 1 } ( x )$ , is properly regarded as an infinite series of infinitely small inertances and compliances. (b) The phasors at the ends and center are particularly simple. (c) Two compliances and one inertance capture these simple end.behaviors, with reduced accuracy in values of $\dot { p _ { 1 } }$ and $U _ { 1 }$ at intermediate x.

## 2.2. Viscous and thermal effects in large channels

To introduce the key concepts of dissipation and gain into the lossless acoustics picture developed so far, we'll start with a simple “complete" thermoacoustics problem: the ordinary viscous and thermal attenuation of sound propagating in a large channel due to the sound wave's interaction with the solid channel wall.

We consider sound.propagating in the x direction in an ideal gas within a channel with constant cross-sectional area A and perimeter II. The hydraulic radius

$$
R _ { h } = A / \Pi\tag{2.9}
$$

is conventionally defined as the ratio of cross-sectional area to perimeter. (The hydraulic radius can also be thought of as the ratio of gas volume to gas-solid contact area, or as the distance from a typical parcel of gas to the nearest solid surface. Note that the hydraulic radius of a circular channel is half the circle's actual radius!) In this section, we will consider only channels for which $R _ { h } \gg \delta _ { \nu }$ and $R _ { h } \gg \delta _ { \kappa }$ : the boundary-layer approximation. We use our usual complex notation for time-oscillatory quantities (pressure ${ \pmb p } ,$ temperature $T ,$ velocity component u in the x direction, density ${ \boldsymbol { \rho } } ,$ entropy per unit mass s) :

$$
\begin{array} { r } { p \ = \ p _ { m } + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] + \ldots , } \end{array}\tag{2.10}
$$

$$
\begin{array} { r } { u } { \ = \ \mathrm { R e } \left[ u _ { 1 } ( x , y ) e ^ { i \omega t } \right] + \ldots , } \end{array}\tag{2.11}
$$

$$
T ~ = ~ T _ { m } + \mathrm { R e } \left[ T _ { 1 } ( x , y ) e ^ { i \omega t } \right] + \ldots ,\tag{2.12}
$$

$$
\rho , s , \mathrm { e t c . } = \mathrm { s i m i l a r t o } T ,\tag{2.13}
$$

with $\mu , k ,$ etc. constant. In this section, the channel is assumed to be spatially isothermal, so $T _ { m }$ is independent of x in Eq. (2.12). The coordinate y measures the distance from the wall of the channel, with $y = 0$ at the wall, as shown in Fig. 2.6.

## 2.2.1. Viscous resistance

To develop quantitative understanding of viscous effects, we consider the situation illustrated in Fig. 2.6 to find the $_ y$ dependence of the gas velocity, using the x-component of the momentum equation, for which the acoustic approximation is

$$
i \omega \rho _ { m } u _ { 1 } ( x , y ) = - \frac { d p _ { 1 } ( x ) } { d x } + \mu \frac { \partial ^ { 2 } u _ { 1 } ( x , y ) } { \partial y ^ { 2 } } .\tag{2.14}
$$

The x derivatives of $\pmb { u } _ { 1 }$ have been neglected because they are of order $1 / \lambda .$ and hence are much smaller than the $\pmb { y }$ derivatives, of order $1 / \delta _ { \nu } .$ This equation is the appropriate approximation to Newton's law, $F = m a ,$ , for a differential volume of gas: The left hand side is mass times acceleration, and the right hand side is the sum of the forces—the pressure force and the viscous force.

Equation (2.14) is an ordinary differential equation for $u _ { 1 } ( x , y )$ as a function of $\pmb { y } .$ With two boundary conditions $u _ { 1 } ( y = 0 ) = 0$ at the solid surface and ${ \pmb u } _ { 1 }$ finite as $y \longrightarrow \infty ,$ its solution is

$$
u _ { 1 } = \frac { i } { \omega \rho _ { m } } \left[ 1 - e ^ { - ( 1 + i ) y / \delta _ { \nu } } \right] \frac { d p _ { 1 } } { d x } .\tag{2.15}
$$

![[mu_ad18d396_4a5cbae12a1bf74ffe92.jpg]]

Figure 2.6: The coordinate system used in this section. In the boundary-layer approximation, the opposite wall of the channel is at such large y that it doesn't appear in this figure.  
![[mu_ad18d396_557e0db3ad33f92b6faf.jpg]]  
Figure 2.7: The momentum equation describes inertial and resistive effects in a channel. (a) A short channel, of length $\pmb { \triangle x }$ and cross-sectional area A. (b) Impedance diagram showing inertance L and resistance $\scriptstyle { \mathcal { R } } _ { \nu } .$ (c) A typical phasor diagrams for this situation, showing that the pressure difference $\Delta p _ { 1 }$ is the sum of inertial and resistive components.

This function shows how viscosity reduces the magnitude of the oscillatory velocity and shifts its phase.

The complex notation is compact and easy to manipulate, but difficult to interpret intuitively. To gain a visual appreciation for the boundary-layer velocity expression, Eq. (2.15), study Ani. Viscous $/ \mathbf { m } ,$ which displays the particle displacement $x ( y , t ) = \mathrm { R e } \left[ u _ { 1 } ( y ) e ^ { i \omega t } / i \omega \right]$ ∝ Re $\left[ \left( 1 - e ^ { - ( 1 + i ) y / \delta _ { \nu } } \right) e ^ { i \dot { w } t } \right]$ with y vertical and the acoustic oscillation direction x horizontal. The moving line can be imagined to be a very thin cloud of smoke moving with the oscillating gas. The tic mark spacing on the vertical axis is the viscous penetration depth $\delta _ { \nu } .$ Gas that is much closer than $\delta _ { \nu }$ to the solid boundary is nearly at rest. Gas that is much farther than $\delta _ { \nu }$ from the solid boundary experiences essentially no viscous shear; it moves with a velocity and displacement that are independent. of y. This inviscid motion is purely inertial; the acceleration is in phase with the force, which is $- d p _ { 1 } / d x ,$ so the displacement is in phase with $+ d p _ { 1 } / d x$ . Gas that is roughly $\delta _ { \nu }$ from the nearest solid surface moves with a modified, y-dependent velocity and a significant, y-dependent phase shift.

In boundary-layer approximation, we often need the spatial average, over the crosssectional area A, of a boundary-layer function $\pmb { F } ( y )$ such as Eq. (2.15). Using Eq. (2.9) defining the hydraulic radius, we can write such an average as

$$
\left. F \right. = \frac { 1 } { A } \int { F d A } = \frac { 1 } { \Pi R _ { h } } \int _ { 0 } ^ { R _ { h } } { F ( y ) \Pi d y } \simeq \frac { 1 } { R _ { h } } \int _ { 0 } ^ { \infty } { F ( y ) d y } .\tag{2.16}
$$

Thus, the spatial average of Eq. (2.15) is

$$
\langle u _ { 1 } \rangle = \frac { i } { \omega \rho _ { m } } \left[ 1 - ( 1 - i ) \frac { \delta _ { \nu } } { 2 R _ { h } } \right] \frac { d p _ { 1 } } { d x } .\tag{2.17}
$$

In the previous section, the lossless momentum equation led to Eq. (2.5) and to the concept of inertance for a short channel with length $\Delta _ { i }$ x and area S. Now, including losses, Eq. (2.17) shows that the corresponding expression is

$$
\Delta p _ { 1 } ~ = ~ - \frac { i \omega \rho _ { m } \Delta x / A } { 1 - ( 1 - i ) \delta _ { \nu } / { 2 R _ { h } } } U _ { 1 }\tag{2.18}
$$

$$
\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - Z U _ { 1 } } \end{array}\tag{2.19}
$$

$$
\begin{array} { r l } { \mathrm { ~  ~ \omega ~ } = } & { { } - \left( i \omega L + R _ { \nu } \right) U _ { 1 } , } \end{array}\tag{2.20}
$$

so viscosity adds viscous resistance $\scriptstyle { \mathcal { R } } _ { \nu }$ in series with inertance $\scriptstyle { \cal L }$ to comprise total series impedance $Z = R _ { \nu } + i \omega L$ as shown in Fig. 2.7b. In this boundary-layer approximation, the inertance and resistance are

$$
L \ \simeq \ \frac { \rho _ { m } \Delta x } { A }\tag{2.21}
$$

$$
R _ { \nu } ~ \simeq ~ { \frac { \mu \Pi \Delta x } { A ^ { 2 } \delta _ { \nu } } } = { \frac { \mu \Delta S } { A ^ { 2 } \delta _ { \nu } } }\tag{2.22}
$$

to lowest order in $\delta _ { \nu } / R _ { h } ;$ I is the perimeter of the channel and $\Delta S = \Pi \Delta x$ is its surface area. Note that $\scriptstyle { R _ { \nu } }$ and L are real; hence, the $^ { \mathfrak { s e } _ { i ^ { \mathfrak { s } } } \mathfrak { s } }$ in Eq. (2.20) implies that the inertial contribution to the pressure difference leads the resistive contribution by $9 0 ^ { \circ }$ , as shown in Fig. 2.7c.

So think of any length of channel as having resistance caused by viscosity and inertance caused by mass. A fat channel, with $R _ { h } \gg \delta _ { \nu } ,$ has $\omega L \gg R _ { \nu }$ . In fact, in that limit the ratio $\omega L / R _ { \nu }$ is proportional to $A / \Pi \delta _ { \nu } ,$ so it is useful to think of the core of the channel, with volume $A \Delta x ,$ as being responsible for the inertance, while the lossy inner skin of the channel, with volume of order $\Pi \delta _ { \nu } \triangle x$ equal to the channel's surface area times the viscous penetration depth, as being responsible for the resistance.

Example: orifice pulse-tube refrigerator. Consider the lumped-element components at the top of the orifice pulse-tube refrigerator shown in Fig. 1.16: a compliance, an inertance, and two valves. The purpose of these components is to provide an adjustable acoustic impedance at the top of the pulse-tube refrigerator, with the adjustments made by the valve settings. To make a simple example, we will neglect resistances in the inertance and compliance, so that the network will be regarded as shown in Fig. 2.8a. We consider a 40-Hz, 3.1-MPa helium operating point, with the network at 300 K. The compliance has a volume of 9.8 liters, so according to Eq. (2.3) $C = 1 . 9 \times 1 0 ^ { - 9 } \ \mathrm { m } ^ { 3 } / \mathrm { P a }$ and its impedance $1 / \omega C = 2 . 1 ~ \mathrm { M P a } { - } \mathrm { s } / \mathrm { m } ^ { 3 }$ . The inertance has a length of 2.5 m and a diameter of 2.4 cm, so according to Eq. (2.6) $L = 2 6 8 0 0 ~ \mathrm { P a } { \cdot } \mathrm { s } ^ { 2 } / \mathrm { m } ^ { 3 }$ and its impedance $\omega L = 6 . 7 ~ \mathrm { M P a { - } \bar { s } / m ^ { 3 } }$ . To keep this example simple, regard the two valves as resistances $\scriptstyle { \mathcal { R } } _ { s }$ and $R _ { p } ,$ adjustable from zero to infinity. Then the net impedance provided by the network is

$$
Z = \frac { 1 } { 1 / \left( i \omega L + R _ { s } \right) + 1 / R _ { p } } + \frac { 1 } { i \omega C } .\tag{2.23}
$$

Plotting Eq. (2.23) for all values of $R _ { s }$ and $R _ { p }$ shows that adjustment of the two valves allows access to the entire region of complex Z that is shaded in Fig. 2.8b.

(a)  
![[mu_ad18d396_bd592eee97f7951976b9.jpg]]

(b)  
![[mu_ad18d396_30402dbf864e50fb9308.jpg]]

(c)  
![[mu_ad18d396_751c8e947c55d87536d8.jpg]]  
Figure 2.8: (a) Impedance diagram for the acoustic network at the top of the orifice pulsetube refrigerator. (b) The shaded zone of the plot shows values of $z$ accessible by adjusting the two valves. (c) Phasor diagram for one case in which the valve labeled $" R _ { p } "$ is closed.

Suppose the valves were set so that $R _ { p } = \infty \ ( { \mathrm { i . e . } }$ closed) and $R _ { s } = 3 . 3 5 ~ \mathrm { M P a } { - } \mathrm { s } / \mathrm { m } ^ { 3 }$ Then Eq. (2.23) shows that $Z = ( 3 . 3 5 + i 4 . 6 )$ $M P a - s / m ^ { 3 } ,$ so the phase of Z is $5 4 ^ { \circ }$ .The phasor diagram for this case is shown in Fig. 2.8b, where we have arbitrarily chosen the phase of $U _ { 1 }$ to be zero.

If we use DeltaE to model the inertance, we can account for its series resistance $\scriptstyle { \mathcal { R } } _ { \nu }$ . For one operating point, such a DeltaE model is

<table><tr><td colspan="3">BEGIN the setup</td></tr><tr><td>3.1114E+06 a Mean P</td><td></td><td>Pa</td></tr><tr><td>42.000</td><td>b Freq.</td><td>Hz</td></tr><tr><td>305.20</td><td>c T-beg</td><td>K</td></tr><tr><td>9.3205E+04 d lpl@0</td><td></td><td>Pa</td></tr><tr><td>0.0000</td><td>e Ph(p)0</td><td>deg</td></tr><tr><td>4.3536E-02 f |U|@0</td><td></td><td>m^3/s</td></tr><tr><td>-98.944</td><td>g Ph(U)0</td><td>deg</td></tr><tr><td>helium</td><td>Gas type</td><td></td></tr></table>

<table><tr><td>ideal</td><td colspan="2">Solid type</td><td colspan="2"></td></tr><tr><td></td><td>the inertance</td><td>7</td><td></td><td></td></tr><tr><td colspan="3">ISODUCT</td><td colspan="2"></td></tr><tr><td colspan="2">4.6400E-04 a Area</td><td> $\mathtt { m } ^ { \bullet \bullet }$ </td><td>2.0075E+05 A lpl</td><td>Pa</td></tr><tr><td colspan="2">7.6360E-02 b Perim</td><td>m</td><td>159.47 B Ph(p)</td><td>deg</td></tr><tr><td colspan="2">2.4900 c Length</td><td>m</td><td>4.0435E-02 C |U|</td><td> $\pi \sim 3 / 8$ </td></tr><tr><td colspan="2">5.0000E-04 d Srough</td><td></td><td>-96.129 D Ph(U)</td><td>deg</td></tr></table>

We compute $Z = { \triangle p _ { 1 } } / { U _ { 1 } }$ , where $\Delta p _ { 1 } = ( 2 8 1 - i 7 0 )$ kPa is the pressure difference across the inertance and $U _ { 1 } = ( 0 . 0 0 5 5 + i 0 . 0 4 1 6 )$ m³/s is the average of the volumetric velocities at the two ends of the inertance. The result is $Z = ( 0 . 7 8 + i 6 . 8 6 )$ $\mathrm { M P a } { \cdot } { \mathrm { s } } / \mathrm { m } ^ { 3 }$ , so that $L = 2 7 3 0 0$ $\mathrm { P a - s ^ { 2 } / m ^ { 3 } } , \omega L = 6 . 8 6 ~ \mathrm { M P a - s / m ^ { 3 } } ,$ and $R _ { \nu } = 0 . 7 8 ~ \mathrm { M P a } { \cdot } \mathrm { s } / \mathrm { m } ^ { 3 }$ . Our neglect of $\scriptstyle { R _ { \nu } }$ with respect to ωL in the previous paragraph was reasonable but not excellent; this calculated $\scriptstyle { \mathcal { R } } _ { \nu }$ is larger than we would guess from ω $L \delta _ { \nu } / R _ { h }$ because DeltaE includes the effect of turbulence, which we will discuss in Chapter 5. Our estimate of L in the previous paragraph differed only 2% from the result of this numerical integration.

Example: standing-wave refrigerator. Consider one of the central tees in the standing-wave refrigerator of Fig. 1.11. These locations are pressure nodes, so compliance (though it could be calculated) is irrelevant here; these are locations of high velocity, so inertance and series resistance are important. Because of the way the black cones fit into the tees, the horizontal passage through each tee actually comprises three ducts in series: a 12.7-cm-long, 11.2-cm-diam duct between two 5.7-cm-long, 10.2-cm-diam ducts. We compute L and $\scriptstyle { \mathcal { R } } _ { \nu }$ for each of these at a typical operating point: 300 K, 92 Hz, 8% argon and 92% helium at a mean pressure of 324 kPa. Since $\delta _ { \nu }$ is only 0.3 mm, the boundary-layer Eqs. (2.21) and (2.22) are appropriate. The results are $L = 2 4 . 1 ~ \mathrm { P a } – \mathrm { s } / \mathrm { m } ^ { 3 } , \omega L = 1 3 9 0 0$ $\tt P a - s / m ^ { 3 }$ , and $R _ { \nu } = 7 5 ~ \mathrm { P a } { \cdot } \mathrm { s } / \mathrm { m } ^ { 3 }$ Indeed, $\omega L \gg R _ { \nu } .$ , as expected for a large-diameter component. These two tees, with parts of the cones nearby, contribute the inertance necessary for the full-wave resonance. Although the resonator is not really lumped-element, we could represent it crudely as such, as shown in Fig. 2.9.

![[mu_ad18d396_22f32ca02ca21988e37c.jpg]]  
Figure 2.9: Crudest representation of the resonator of the standing-wave refrigerator.

## 2.2.2. Thermal-relaxation conductance

The viscous effects discusșed thus far are only one component of acoustic attenuation at a solid boundary; thermal relaxation effects can be equally important wherever oscillating

pressure exists, as it causes an oscillating temperature. The general equation of heat transfer [26]

$$
\begin{array} { r c l } { \rho { c _ { p } } \displaystyle \left( \frac { \partial T } { \partial t } + { \bf v } \cdot \nabla T \right) - \left( \frac { \partial p } { \partial t } + { \bf v } \cdot \nabla p \right) } & { = } & { \nabla \cdot ( k \nabla T ) } \\ & & { + ( \mathrm { t e r m s ~ q u a d r a t i c ~ i n ~ v e l o c i t y } ) } \end{array}\tag{2.24}
$$

expresses the fact that the temperature changes with time because of the sum of three effects: pressure changes, thermal conduction, and some velocity terms that don't concern us in the acoustic approximation. An example of the pressure-induced temperature changes is shown in Ani. Thermal $/ \ w .$ The animation shows temperature, pressure, and gas motion in a half-wavelength resonance; the temperature oscillations are both proportional to and in temporal phase with the pressure oscillations. Such adiabatic temperature oscillations are present in all sound waves in free space, although for typical “audio" amplitudes they are too small to be readily noticed.

Adopting the usual complex notation for the relevant variables, as expressed above in Eqs. (2.10)-(2.13), we find that Eq. (2.24) reduces to

$$
{ i \omega \rho _ { m } c _ { p } T _ { 1 } - i \omega p _ { 1 } = k \frac { \partial ^ { 2 } T _ { 1 } } { \partial y ^ { 2 } } }\tag{2.25}
$$

in the channel. Similar to the viscous derivation above, we have neglected the x derivatives of $\boldsymbol { \mathcal { T } _ { 1 } }$ because they are of order $\mathbb { 1 } / \lambda ,$ and hence are much smaller than the y derivatives, of order $1 / \delta _ { \kappa }$ . The solid usually has sufficient heat capacity and thermal conductivity to enforce $T _ { 1 } = 0$ on the gas at the solid surface $y = 0 ;$ the other necessary boundary condition is that $T _ { 1 } ( \infty )$ is finite. Equation (2.25) is an ordinary differential equation for $\mathcal { T } _ { 1 } ( y )$ , identical in form and boundary condition to Eq. (2.14) for $u _ { 1 } ( y )$ . Exploiting the similarity, the solution can be written

$$
T _ { 1 } = \frac { 1 } { \rho _ { m } c _ { p } } \left[ 1 - e ^ { - ( 1 + i ) y / \delta _ { \kappa } } \right] p _ { 1 } ,\tag{2.26}
$$

and its spatial average can be written

$$
\mathbf { \nabla } . \left. T _ { 1 } \right. = \frac { 1 } { \rho _ { m } c _ { p } } \left[ 1 - ( 1 - i ) \frac { \delta _ { \kappa } } { 2 R _ { h } } \right] p _ { 1 } .\tag{2.27}
$$

Equation (2.26) shows how thermal contact with the solid surface reduces the magnitude and shifts the phase of the oscillatory temperature, similar to the effect of viscosity on oscillatory velocity discussed above. Gas that is much farther than $\delta _ { \kappa }$ from the nearest solid surface is essentially adiabatic, experiencing adiabatic temperature oscillations $\mathcal { T } _ { 1 } =$ $( 1 / \rho _ { m } c _ { p } ) p _ { 1 }$ in phase with the pressure oscillations (as shown in Ani. Thermal $/ \pi )$ . The temperature of gas that is much closer than $\delta _ { \kappa }$ to the nearest solid surface oscillates little; it is locked to the time-independent wall temperature $\mathcal { T } _ { m }$ by the heat capacity of the solid wall. At approximately $\delta _ { \kappa }$ from' the nearest-solid surface, these oscillations are reduced in magnitude and shifted in phase. In this boundary-layer limit, the functional dependence of Eq. (2.26) is shown in Ani. Thermal $/ { \mathfrak { y } } ,$ in which the tics on the y axis are separated by $\delta _ { \kappa } .$

This animation shows the oscillating temperature as a function of time and distance y from the wall,

$$
T ( y , t ) = T _ { m } + \frac { 1 } { \rho _ { m } c _ { p } } \mathrm { R e } \left[ \left( 1 - e ^ { ( 1 + i ) y / \delta _ { \kappa } } \right) p _ { 1 } e ^ { i \omega t } \right] ,\tag{2.28}
$$

with the motion of the gas toward and away from the wall illustrated by the vertical straight lines moving left and right.

Using

$$
d \rho = - \frac { \rho } { T } d T + \frac { \rho } { p } d p\tag{2.29}
$$

we can express the spatially averaged density as

$$
\left. \rho _ { 1 } \right. = - \frac { \rho _ { m } } { T _ { m } } \left. T _ { 1 } \right. + \frac { \rho _ { m } } { p _ { m } } p _ { 1 } .\tag{2.30}
$$

Now we are finally ready to work with the continuity equation. Averaging Eq. (1.9) over the cross-sectional area of the channel gives

$$
i \omega \left. \rho _ { 1 } \right. + \rho _ { m } \frac { d \left. u _ { 1 } \right. } { d x } = 0 .\tag{2.31}
$$

Using Eqs. (2.30) and' (2.27), and eliminating $c _ { p }$ by using

$$
c _ { p } = \frac { \gamma } { \gamma - 1 } \frac { p _ { m } } { \rho _ { m } T _ { m } } ,\tag{2.32}
$$

yields

$$
\dot { w } \left[ 1 + \left( \gamma - 1 \right) \left( 1 - \dot { \mathfrak { i } } \right) \frac { \delta _ { \kappa } } { 2 R _ { h } } \right] \frac { p _ { 1 } } { \gamma p _ { m } } + \frac { d \left. u _ { 1 } \right. } { d x } = 0\tag{2.33}
$$

as an acoustic expression of the continuity equation in the presence of thermal relaxation effects.

In the previous section, the lossless continuity equation led to Eq. (2.2) and the concept of compliance. Here, the continuity equation leads to Eq. (2.33), which includes both compliance and thermal relaxation. Equation (2.33) can be rewritten for a short channel shown in Fig. 2.10a with volume $V = A \Delta x$ as

$$
p _ { 1 } = - Z \Delta U _ { 1 } ,\tag{2.34}
$$

where $z$ is the parallel combination .of a compliance and a resistance,

$$
\frac { 1 } { Z } = i \omega C + \frac { 1 } { R _ { \kappa } } ,\tag{2.35}
$$

as shown in Fig. 2.10b. The effective compliance is given by

$$
C \simeq \frac { V } { \gamma p _ { m } }\tag{2.36}
$$

![[mu_ad18d396_d48043a308eeffb19d18.jpg]]  
Figure 2.10: The continuity equation describes compliant and resistive effects in à channel. (a) A short channel, of length ∆x and cross-sectional area A. (b) Impedance diagram showing compliance $\pmb { C }$ and parallel resistance $\scriptstyle { \mathcal { R } } _ { \kappa }$ . (c) A typical phasor diagram for this situation, showing that the volumetric velocity change $\triangle U _ { 1 }$ is the sum of compliant and resistive components.

to lowest order in $\delta _ { \kappa } / R _ { h }$ . The effective resistance $\scriptstyle { \mathcal { R } } _ { \kappa }$ that is in parallel with the compliance is

$$
R _ { \kappa } \simeq \frac { 2 \gamma p _ { m } } { \omega \left( \gamma - 1 \right) \delta _ { \kappa } S } ,\tag{2.37}
$$

inversely proportional to the volume $S \delta _ { \kappa }$ which experiences thermal relaxation.

So think of any channel as having compliance and thermal-relaxation resistance, which cause $\Delta U _ { 1 }$ to change from one end of the channel to the other. A wide open volume, with $V \gg S \delta _ { \kappa } ,$ has $\omega C \gg 1 / R _ { \kappa } ,$ so the compliance dominates the net impedance. It is useful to think of the core of the volume $V ,$ with adiabatic compressibility, as being responsible for the compliance, while the vicinity of the inner surface, with effective volume $S \delta _ { \kappa }$ equal to the channel's surface area times the thermal penetration depth, has a compressibility intermediate between the adiabatic and isothermal compressibilities and is responsible for the thermal-relaxation resistance.

Example: standing-wave engine. Consider one of the outer "hot ducts" (outboard of the hot heat exchangers) in the standing-wave engine of Fig. 1.10. This location is near a velocity node, so inertance and series resistánce are unimportant. We will compute the compliance and its parallel thermal-relaxation resistance at a typical operating point: 3 MPa helium, 390 $\mathbb { H } \mathbf { z } ,$ 800 K. Each hot duct has a volume of $\mathsf { 1 2 0 ~ c m ^ { 3 } }$ and a surface area of $\scriptstyle 1 3 0 \ c m ^ { 2 }$ (accounting properly for the surface area and blocked volume due to electrical feedthroughs passing through this space). Since $\delta _ { \kappa }$ is only 0.2 mm, we can use boundarylayer Eqs. (2.36) and (2.37), finding $C = 2 . 4 \times 1 0 ^ { - 1 1 } \ \mathrm { m } ^ { 3 } / \mathrm { P a } , \ 1 / \omega C = 1 7 \ \mathrm { M P a } { - } \mathrm { s } / \mathrm { m } ^ { 3 }$ , and $R _ { \kappa } = 2 3 5 0 ~ \mathrm { M P a } – \mathrm { s } / \mathrm { m } ^ { 3 }$

![[mu_ad18d396_f7147be67fdbcd095eec.jpg]]  
Figure 2.11: The coordinate system used in this section. In the boundary-layer approximation, the opposite wall of the channel is at such large $y > > \delta _ { \kappa }$ that it doesn't apear in this figure.

Example: orifice pulse-tube refrigerator. The compliance at the top of the orifice pulse-tube refrigerator of Fig. 1.16 has a volume of 9.8 liters and a surface area of approximately $0 . 3 \ m ^ { 2 }$ . At 40 Hz with 3.1 MPa helium, we calculated a few pages ago that its compliance is $C = 1 . 9 \times 1 0 ^ { - 9 } \ \mathrm { m } ^ { 3 } / \mathrm { P a }$ and $1 / \omega C = 2 . 1 ~ \mathrm { M P a } { \cdot } \mathrm { s } / \mathrm { m } ^ { 3 }$ . Equation (2.37) shows that $R _ { \kappa } = 9 5 0 ~ \mathrm { M P a } { - } \mathrm { s } / \mathrm { m } ^ { 3 }$ . Hence, $1 / R _ { k }$ can be safely neglected in comparison to ωC.

## 2.3. Inviscid boundary-layer thermoacoustics

Now we'll finally proceed to thermoacoustics problems in which a mean temperature gradient along the direction of acoustic oscillation is significant. The simplest such problem that I know of is not perfectly realistic, because viscosity is neglected. (However, viscosity can't really be neglected, because viscous and thermal penetration depths in gases are typically about the same size.) Nevertheless, to gain intuition about thermoacoustics, we'll begin with a brief consideration of this unrealistic inviscid problem.

Consider a nonzero temperature gradient $d T _ { m } / d x$ along the direction x of acoustic oscillations, with a plane solid boundary at $y = 0 ,$ as shown in Fig. 2.11. Start from the general equation of heat transfer, Eq. (2.24), substitute the appropriate form of the acoustic approximation

$$
\begin{array} { r } { p } { \ = \ p _ { m } + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] + \ldots , } \end{array}\tag{2.38}
$$

$$
u \ = \ \mathrm { R e } \left[ u _ { 1 } ( x , y ) e ^ { i \omega t } \right] + \ldots ,\tag{2.39}
$$

$$
T \ = \ T _ { m } \left( x \right) + \mathrm { R e } \left[ T _ { 1 } ( x , y ) e ^ { i \omega t } \right] + \ldots ,\tag{2.40}
$$

$$
\rho , s , \mathrm { e t c . } = \mathrm { s i m i l a r } \ t o T ,\tag{2.41}
$$

and keep first-order terms to obtain the appropriate acoustic equation of heat transfer,

$$
\rho _ { m } c _ { p } \left( i \omega T _ { 1 } + u _ { 1 } \frac { d T _ { m } } { d x } \right) - i \omega p _ { 1 } = k \frac { \partial ^ { 2 } T _ { 1 } } { \partial y ^ { 2 } } .\tag{2.42}
$$

This differential equation for $T _ { 1 } ( y )$ is similar to Eq. (2.25) but with an additional nonzero $d T _ { m } / d x$ term. Remember we are assuming that the gas viscosity is zero, so ${ \pmb u } _ { 1 }$ is independent of y in this section. The necessary boundary conditions are $T _ { 1 } ( 0 ) = 0$ and $\displaystyle T _ { 1 } ( \infty )$ is finite.

The solution is

$$
T _ { 1 } = \left( \frac { p _ { 1 } } { \rho _ { m } c _ { p } } - \frac { u _ { 1 } } { i \omega } \frac { d T _ { m } } { d x } \right) \left[ 1 - e ^ { - ( 1 + i ) y / \delta _ { K } } \right]\tag{2.43}
$$

which resembles Eq. (2.26), but with more complexity arising from the $u _ { 1 } d T _ { m } / d x$ term. This solution is the product of two factors. The first factor gives the overall magnitude of the oscillating temperature at distances $y \gg \delta _ { \nu }$ from the solid boundary, and the second factor describes the y dependence of that oscillating temperature close to the solid boundary.

The y-dependent factor is the same complex boundary-layer function that we've seen before, in Eqs. (2.15) and (2.26), and in Anis. Viscous $/ \mathbf { m }$ and Thermal $/ { \mathfrak { y } } .$ View Ani. Thermal $/ { \bf y }$ again, and consider Fig. 2.12, which shows the real and imaginary parts of the second factor in Eq. (2.43). You should be able to visualize the time evolution shown in the animation being a smooth progression in time between the real and imaginary parts shown in Fig. 2.12, from real part to minus imaginary part to minus real part to imaginary part and back to real part.

The magnitude factor in Eq. (2.43) is itself the sum of two terms, each of which is easy to understand. The first term is simply the adiabatic temperature oscillation: When the pressure goes up the temperature goes up, and when the pressure goes down the temperature goes down. The second term is due to gas motion along ${ \pmb x } ,$ along the temperature gradient, and is due to the façt that the Eulerian, fixed-in-the-laboratory point of view used in the conventional formulation of the equations of fluid mechanics that we use. In all of our equations, such as Eqs. (2.38)-(2.43) in the present section, $( { \pmb x } , { \pmb y } )$ refers to a fixed location in space, past which gas moves. The $u _ { 1 } d T _ { m } / d x$ term in Eq. (2.43) simply reflects this reference frame: When a gas with a temperature gradient moves adiabatically past that point in space, the temperature at that point in space changes. (The alternative, Lagragian point of view focuses greater attention on a particular parcel of gas as it moves, not on a fixed location in space. The Lagrangian viewpoint is often better for developing intuition, so we rely on it in most of the animations. In the Lagrangian viewpoint, a parcel of gas at $y \gg \delta _ { \kappa }$ experiences $T _ { 1 } = p _ { 1 } / \rho _ { m } c _ { p }$ , quite independent of its velocity or whether a nonzero $d T _ { m } / d x$ exists.)

So the magnitude factor in $\mathtt { E q } .$ (2.43) is simply the linear superposition of adiabatic pressure-induced temperature oscillations and adiabatic motion-induced temperature oscillations. The magnitude factor is complex: It can have any sign and phase, depending on the relative phases of ${ \pmb p } _ { 1 }$ and $\pmb { u } _ { 1 }$ and the relative magnitude of the pressure term relative to the motion term.

For standing-wave phasing, the entire magnitude factor in $\mathtt { E q . }$ (2.43) can be zero, if

$$
\frac { \left| p _ { 1 } \right| } { \rho _ { m } c _ { p } } = \frac { \left| u _ { 1 } \right| } { \omega } \frac { d T _ { m } } { d x } .\tag{2.44}
$$

In this special circumstance, the gas properties, standing-wave impedance, and temperature gradient conspire so that the pressure-induced temperature oscillation and motion-induced temperature oscillation are equal in magnitude but opposite in sign. This circumstance is illustrated in Ani. Standing $/ \mathbf { c } ,$ where the upper part of the display shows a standing wave in a resonator with a stack near'the left end, with blue marker lines showing the moving gas. One particular piece of gas is highlighted with a moving white dot in the stack. The yellow oval marks the region that is shown magnified at the left center of the display, which shows that same parcel of moving gas and short fragments of the two stack plates adjacent to it. The volume of that parcel of gas changes in response to pressure and temperature. At the bottom left of the display is a plot of temperature vs position, in which the temperature of the parcel is the blue trace, and that of the nearby plate in the stack is the white line. Here, $R _ { h } \sim \delta _ { \kappa } ,$ so the thermal contact is poor; the parcel's temperature oscillation is due entirely to adiabatic pressure oscillation, and its temperature oscillation and motion just happen to match the local temperature gradient $d T _ { m } / d x$ exactly, so that the temperature at a fixed location is independent of time.

![[mu_ad18d396_2e4c4fb2228a9fa6ea05.jpg]]  
Figure 2.12: The real and imaginary part of the y-dependent factor in Eq.(2.43).

This circumstance is sufficiently important for standing-wave engines and refrigerators that we give it a specific name, the critical temperature gradient:

$$
\nabla T _ { \mathrm { c r i t } } = \frac { \omega A \left| p _ { 1 } \right| } { \rho _ { m } c _ { p } \left| U _ { 1 } \right| } .\tag{2.45}
$$

[The notation $( \nabla T _ { m } ) _ { \mathtt { c r i t } }$ , though more precise, is too awkward.] We will see later that inviscid standing-wave engines have $d T _ { m } / d x > \ " \nabla T _ { \mathrm { c r i t } }$ , and inviscid standing-wave refrigerators have $d T _ { m } / d x < \nabla T _ { \mathrm { c r i t } }$ . Although the reality of nonzero viscosity blurs this boundary considerably, $\nabla T _ { \mathbf { c r i t } }$ as defined in Eq. (2.45) still provides a useful benchmark.

Equation (2.43) is complex enough—in the literal sense of "complex" with real and imaginary parts, and in the common English meaning of "complex"—that the combination of the complex y dependent factor with the complex magnitude factor can yield essentially any sign, phase, and overall magnitude that you might want. Much of the rich variety encountered in thermoacoustics—standing wave behavior, traveling wave behavior, smallpore behavior and well-spaced behavior—fundamentally arises from the complexity of Eq. (2.43), expressing the simple thermal contact between an acoustic wave and an adjacent solid boundary parallel to the wave propagation direction.

## 2.4. General thermoacoustics

Having gained some intuition with the inviscid, boundary-layer thermoacoustics problem in the previous section and the boundary-layer dissipation problem earlier, we now proceed with a fully general derivation of the dynamic equations of thermoacoustics, including viscosity and arbitrary shape and size of channels.

## 2.4.1. The math

Naturally, the equations are based on the acoustic approximation, with the relevant variables now written as

$$
p ~ = ~ p _ { m } + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] ,\tag{2.46}
$$

$$
U ~ = ~ \mathrm { R e } \left[ U _ { 1 } ( x ) e ^ { i \omega t } \right] ,\tag{2.47}
$$

$$
\begin{array} { r } { u } { \ = \ \mathrm { \tiny ~ R e } \left[ u _ { 1 } ( x , y , z ) e ^ { i \omega t } \right] , } \end{array}\tag{2.48}
$$

$$
v , w \ = \ { \mathrm { s i m i l a r } } \ { \mathrm { t o } } \ u ,\tag{2.49}
$$

$$
\begin{array} { r } { \cal { T } } { \mathrm { ~  ~ \Gamma ~ } } = \cal { T } _ { m } ( x ) + \mathrm { R e } \left[ T _ { 1 } ( x , y , z ) e ^ { i \omega t } \right] ,  \end{array}\tag{2.50}
$$

$$
\rho , s ~ = ~ \mathrm { s i m i l a r } ~ \mathrm { t o } ~ T ~ ,\tag{2.51}
$$

$$
{ \bf \mathcal { \mu } } { \bf \Xi } = { \bf \Lambda } \mu ( { \bf \Lambda } x ) ,\tag{2.52}
$$

$$
a , \ k , \ \mathrm { e t c . } ~ \ = ~ \ \mathrm { s i m i l a r \ t o } \ \mu\tag{2.53}
$$

In this section, we are most interested in ${ \pmb { p } } _ { 1 }$ and $\dot { U _ { 1 } }$ , as described by the momentum and continuity equations.

For clarity, we continue to consider here only the case of large solid heat capacity, so that the temperature of the solid material in the stack is simply $\mathcal { T } _ { m } ( x )$ , independent of time, y, and $z ;$ and we continue to restrict our attention to ideal gases. (For finite solid heat capacity or non-ideal gas effects, see [25].)

The presence of nonzero $d T _ { m } / d x$ has no effect on the momentum equation in the acoustic approximation. Hence, we have for the x-component of the momentum equation

$$
\small { i \omega \rho _ { m } u _ { 1 } = - \frac { d p _ { 1 } } { d x } + \mu \left[ \frac { \partial ^ { 2 } u _ { 1 } } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } u _ { 1 } } { \partial z ^ { 2 } } \right] . }\tag{2.54}
$$

The x derivatives of ${ \pmb u } _ { 1 }$ have been neglected because they are of order $\mathbb { 1 } / \lambda ,$ and hence are much smaller than the y or z derivatives, of order $1 / \delta _ { \nu }$ Regarding Eq. (2.54) as a differential equation for $u _ { 1 } ( y , z )$ , with boundary condition $u _ { 1 } = 0$ at the solid surface, the solution is

$$
u _ { 1 } = \frac { i } { \omega \rho _ { m } } \left[ 1 - h _ { \nu } ( y , z ) \right] \frac { d p _ { 1 } } { d x } ,\tag{2.55}
$$

where $h _ { \nu } ( y , z )$ depends on the specific geometry under consideration.

Integrating both sides of Eq. (2.55) with respect to y and z over the cross-sectional area A of the channel, we obtain the volumetric velocity $\scriptstyle { \bar { U } } _ { 1 }$ on·the left side and we convert $h _ { \nu }$ on the right side into its spatial average $f _ { \nu }$ . Solving for $d p _ { 1 }$ yields

$$
d p _ { 1 } = - \frac { i \omega \rho _ { m } d x / A } { 1 - f _ { \nu _ { . } } } U _ { 1 } .\tag{2.56}
$$

In effect, we regard this approximation to the momentum equation as the origin of pressure gradient in thermoacoustics: The motion $U _ { 1 }$ of the gas causes the pressure gradient. If $f _ { \nu } = 0 _ { ; }$ , the pressure gradient is entirely “inertial", as indicated by the $s _ { i ^ { n } }$ in Eq. (2.56), but when $f _ { \nu } \neq 0$ the presence of viscosity and the stationary boundaries adds a resistive component to the pressure gradient and also effectively changes the magnitude of the inertial contribution.

The function $h _ { \nu }$ and its spatial average $f _ { \nu }$ are known for many geometries. The complex function fy is plotted for some of these geometries in Fig. 2.13. As we saw above, for $f _ { \nu }$ wide-open channels for which the boundary-layer approximation is appropriate,

$$
~ h ~ = ~ e ^ { - ( 1 + i ) y / \delta } ,\tag{2.57}
$$

$$
f ~ = ~ { \frac { ( 1 - i ) \delta } { 2 R _ { h } } } .\tag{2.58}
$$

If we take $y = 0$ to be the center between parallel plates of separation $2 y _ { 0 } = 2 R _ { h }$

$$
h ~ = ~ \frac { \cosh \left[ \left( 1 + i \right) y / \delta \right] } { \cosh \left[ \left( 1 + i \right) y _ { 0 } / \delta \right] } ,\tag{2.59}
$$

$$
f \ = \ \frac { \operatorname { t a n h } \left[ \left( 1 + i \right) y _ { 0 } / \delta \right] } { \left( 1 + i \right) y _ { 0 } / \delta } .\tag{2.60}
$$

For circular pores of radius $R = 2 R _ { h }$

$$
\begin{array} { r } { h \ = \ \frac { J _ { 0 } [ ( i - 1 ) r / \delta ] } { J _ { 0 } [ ( i - 1 ) R / \delta ] } , } \end{array}\tag{2.61}
$$

$$
f ~ = ~ \frac { 2 J _ { 1 } \left[ \left( i - 1 \right) R / \delta \right] } { J _ { 0 } \left[ \left( i - 1 \right) R / \delta \right] \left( i - 1 \right) R / \delta } ,\tag{2.62}
$$

where the coordinate $r = \sqrt { y ^ { 2 } + z ^ { 2 } }$ . These functions are also known for rectangular channels [36] of dimensions $2 y _ { 0 } \times 2 z _ { 0 }$

$$
\ h \ = \ 1 - \frac { 1 6 } { \pi ^ { 2 } } \sum _ { m , n o d d } \frac { \sin { ( m \pi y / 2 y _ { 0 } ) } \sin { ( n \pi z / 2 z _ { 0 } ) } } { m n Y _ { m n } } ,\tag{2.63}
$$

$$
f ~ = ~ 1 - { \frac { 6 4 } { \pi ^ { 4 } } } \sum _ { m , n o d d } { \frac { 1 } { m ^ { 2 } n ^ { 2 } Y _ { m n } } } ,\tag{2.64}
$$

where

$$
Y _ { m n } = 1 - i \frac { \pi ^ { 2 } \delta ^ { 2 } } { 8 y _ { 0 } ^ { 2 } z _ { 0 } ^ { 2 } } \left( m ^ { 2 } z _ { 0 } ^ { 2 } + n ^ { 2 } y _ { 0 } ^ { 2 } \right) ,\tag{2.65}
$$

and for the spaces between pins oriented along the direction of acoustic oscillations, each of radius $\pmb { r _ { i } }$ and arranged in a triangular array [37] with center-to-center spacing $\sqrt { 2 \pi } r _ { o } / \sqrt [ 4 ] { 3 } \simeq$ $1 . 9 0 5 r _ { o }$

$$
h ~ \simeq ~ \frac { Y _ { 1 } \left( \xi _ { o } \right) J _ { 0 } ( \xi ) - J _ { 1 } \left( \xi _ { o } \right) Y _ { 0 } \left( \xi \right) } { Y _ { 1 } \left( \xi _ { o } \right) J _ { 0 } \left( \xi _ { i } \right) - J _ { 1 } \left( \xi _ { o } \right) Y _ { 0 } \left( \xi _ { i } \right) } ,\tag{2.66}
$$

$$
f ~ \simeq ~ - \frac { 2 \xi _ { i } } { \xi _ { o } ^ { 2 } - \xi _ { i } ^ { 2 } } \frac { Y _ { 1 } \left( \xi _ { o } \right) J _ { 1 } \left( \xi _ { i } \right) - J _ { 1 } \left( \xi _ { o } \right) Y _ { 1 } \left( \xi _ { i } \right) } { Y _ { 1 } \left( \xi _ { o } \right) J _ { 0 } \left( \xi _ { i } \right) - J _ { 1 } \left( \xi _ { o } \right) Y _ { 0 } \left( \xi _ { i } \right) } ,\tag{2.67}
$$

where $\xi = ( i - 1 ) r / \delta$

In the continuity equation, an expression for the spatial average over y and z of the oscillatory temperature, $\langle \mathcal { T } _ { 1 } \rangle$ , is required. As above, it is derived from the general equation of heat transfer, for which the acoustic approximation is

$$
\rho _ { m } c _ { p } \left( i \omega T _ { 1 } + u _ { 1 } \frac { d T _ { m } } { d x } \right) - i \omega p _ { 1 } = \kappa \left[ \frac { \partial ^ { 2 } T _ { 1 } } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } T _ { 1 } } { \partial z ^ { 2 } } \right]
$$

![[mu_ad18d396_449422db99d795ee5cd2.jpg]]  
Figure 2.13: Spatial-average function f for several geometries. The rectangle here has 6:1 aspect ratio, and the pin array has $r _ { o } / r _ { i } = 6$ . The boundary-layer limit is approached at large $R _ { h }$ in all geometries.

when $d T _ { m } / d x \neq 0$ Regarding this as a differential equation for the y and z dependences of $T _ { 1 , }$ and following the same procedure as before but now including the y and z dependences of $\pmb { u } _ { 1 }$ and allowing for arbitrary channel cross section, we find that

$$
T _ { 1 } = \frac { 1 } { \rho _ { m } c _ { p } } \left( \dot { 1 } - h _ { \kappa } \right) p _ { 1 } - \frac { 1 } { i \omega \left( 1 - f _ { \nu } \right) } \frac { d T _ { m } } { d x } \left( 1 - \frac { h _ { \kappa } - \sigma h _ { \nu } } { 1 - \sigma } \right) \frac { U _ { 1 } } { A }\tag{2.68}
$$

and

$$
\left. T _ { 1 } \right. = \frac { 1 } { \rho _ { m } c _ { p } } \left( 1 - f _ { \kappa } \right) p _ { 1 } - \frac { 1 } { i \omega \left( 1 - f _ { \nu } \right) } \frac { d T _ { m } } { d x } \left( 1 - \frac { f _ { \kappa } - \sigma f _ { \nu } } { 1 - \sigma } \right) \frac { U _ { 1 } } { A } ,\tag{2.69}
$$

which are comparable to Eqs. (2.26), (2.27), and especially (2.43).

In the continuity equation, we must now include the x dependence of $\rho _ { m }$

$$
\dot { w } \left. \rho _ { 1 } \right. + \frac { d } { d x } \left( \rho _ { m } \left. u _ { 1 } \right. \right) = 0 .\tag{2.70}
$$

Substituting Eqs. (2.69) and (2.30) into this yields

$$
d \bar { U _ { 1 } } = - \frac { i \omega A d x } { \gamma p _ { m } } [ 1 + \left( \gamma - 1 \right) f _ { \kappa } ] p _ { 1 } + \frac { \left( f _ { \kappa } - f _ { \nu } \right) } { \left( 1 - f _ { \nu } \right) \left( 1 - \sigma \right) } \frac { d T _ { m } } { T _ { m } } U _ { 1 } .\tag{2.71}
$$

This expression finds easy physical interpretation as a complete thermoacoustic approximation to the continuity equation. The two terms in Eq. (2.71) show that a gradient in $U _ { 1 }$ can be caused either by pressure or by velocity along the temperature gradient. Consider the pressure term first. If $f _ { \kappa } = 0 ,$ there is no thermal contact between gas and solid, so the density oscillations are adiabatic; in this case, $1 / \gamma p _ { m }$ is the correct compressibility, and the compliance of the segment of channel of length dx must be $A d x / \gamma p _ { m } = d V / \gamma p _ { m }$ , as we found in Eq. (2.3). At the other extreme, if $f _ { \kappa } = 1$ , the thermal contact between gas and solid is perfect, so the gas is anchored at the local solid temperature. In this case, the isothermal compressibility $1 / p _ { m }$ is appropriate. For intermediate thermal contact, an effective compressibility $[ 1 + ( \gamma - 1 ) f _ { \kappa } ] / \gamma p _ { m } ,$ , intermediate in magnitude and with nontrivial phase, describes the spatial average of the density oscillations in response to pressure oscillations. Next consider the velocity term, in the easily interpreted inviscid limit (with $\textstyle f _ { \nu } = 0$ and $\sigma = 0 )$ so that it is simply $f _ { \kappa } U _ { 1 } d T _ { m } / T _ { m }$ . If $f _ { \kappa } = 0$ , there is no thermal contact between gas and solid, the velocity term is zero, and the gas density does not change as it moves along x. In the other extreme, if $f _ { \kappa } = 1$ , the gas is always at the local solid temperature, so that as it flows toward higher $\mathbf { \nabla } T _ { m }$ its density decreases and its velocity increases. In the more general, and more interesting, intermediate regime, oscillatory motion of the gas along the temperature gradient leads to complex density oscillations.

Equations (2.56) and (2.71) are applicable to a wide variety of thermoacoustic circumstances, and may be considered two of the principal tools of thermoacoustic analysis. Many earlier expressions in this chapter are simplified limits of these equations, and in the next subsection we will closely examine the effective compliance, inertance, and resistances indicated by these two equations.

[One more detail: The graphs and equations for f versus $R _ { h } / \delta$ that we've seen so far have listed several different geometries of interest mostly for standing-wave thermoacoustics. It is possible to follow through the same kind of analysis for the stacked-screen regenerators that are usually used in Stirling systems. Here's an outline of the derivation [38]. Assuming a sinusoidal volumetric velocity through a stacked-screen regenerator, and assuming that published steady-flow data [39] for stacked-screen viscous pressure drop and heat transfer are valid at each instant of time during this oscillation, a Fourier transform of the appropriate continuity and momentum equations can be taken, with those very complicated published curves of pressure drop and heat transfer built in. The results can be rearranged to yield $f _ { \kappa }$ and $f _ { \nu }$ as a function of $\mathcal { R } _ { h } / \delta _ { \kappa }$ and $\mathcal { R } _ { \hbar } / \delta _ { \nu }$ , the volumetric porosity of the screens, and the peak Reynolds number of the flow. The results are only valid for small $\mathcal { R } _ { h } / \delta _ { \kappa } .$ which is the regime of interest for traveling-wave devices. The results look qualitatively like the low- $\mathcal { R } _ { h } / \delta$ parts of the curves in Fig. 2.13, with slightly different results for different porosities in the screen bed and for different Reynolds numbers $( \mathfrak { i . e . }$ , different acoustic amplitudes). Another minor detail that you can find in the Ref. [38]: the $f _ { \kappa }$ that shows up in the ${ \pmb p } _ { 1 }$ term of continuity equation is actually a little different than the $f _ { \kappa }$ that shows up in the $U _ { 1 }$ term.]

Finally, at this point we could combine Eqs. (2.56) and (2.71), eliminating $U _ { 1 }$ , to obtain a second-order differential equation in ${ \mathfrak { p } } _ { 1 }$

$$
\left\{ 1 + \left( \gamma - 1 \right) f _ { \kappa } \right\} p _ { 1 } + \frac { \gamma p _ { m } } { \omega ^ { 2 } } \frac { d } { d x } \left( \frac { 1 - f _ { \nu } } { \rho _ { m } } \frac { d p _ { 1 } } { d x } \right) - \frac { a ^ { 2 } } { \omega ^ { 2 } } \frac { f _ { \kappa } - f _ { \nu } } { 1 - \sigma } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \frac { d p _ { 1 } } { d x } = 0 .\tag{2.72}
$$

This is Rott's wave equation, a milestone in the development of thermoacoustics. (Strictly, we should call it a Helmholtz equation, because the time derivatives have been replaced by $\dot { \imath } \omega ^ { \ast } \mathbf { s } . )$ For numerical computations, it is easiest to use Eqs. (2.56) and (2.71) separately; and

I think that greater intuition can be gained by considering Eqs. (2.56) and (2.71) separately, as we shall do in the next subsection.

## 2.4.2. The ideas

The principal results of the last subsection were the thermoacoustic versions of the momentum and continuity equations, Eqs. (2.56) and (2.71):

$$
\begin{array} { r c l } { { d p _ { 1 } } } & { { = } } & { { \displaystyle - \frac { i \omega \rho _ { m } d x / A } { 1 - f _ { \nu } } \dot { U _ { 1 } } , } } \\ { { } } & { { } } & { { } } \\ { { d \bar { U _ { 1 } } } } & { { = } } & { { \displaystyle - \frac { i \omega A d x } { \gamma p _ { m } } [ 1 + \left( \gamma - 1 \right) f _ { \kappa } ] p _ { 1 } + \frac { \left( f _ { \kappa } - f _ { \nu } \right) } { \left( 1 - f _ { \nu } \right) \left( 1 - \sigma \right) } \frac { d \bar { \cal T } _ { m } } { \cal T _ { m } } \bar { U _ { 1 } } . } } \end{array}
$$

In this subsection, we will try to gain a deep intuitive appreciation of these two equations, following the outline indicated in Fig. 2.14. In the figure, the channel of length $\pmb { \triangle x }$ is considered in two ways: in terms of the momentum equation to obtain its inertance and viscous resistance, and in terms of the continuity equation to obtain its compliance, thermalrelaxation resistance, and thermally induced volumetric velocity source. Combiningthese two points of view yiels a. complete impedance picture for thermoacoustics, just as the momentum and continuity equations provide a complete description of the dynamics linking ${ \pmb p } _ { 1 }$ and $U _ { 1 }$

We begin with the momentum equation. If we rewrite Eq. (2.56) in the form

$$
d p _ { 1 } = - \left( i \omega l d x + r _ { \nu } d x \right) U _ { 1 } ,\tag{2.73}
$$

as shown schematically in the left part of Fig. 2.14, then the inertance and viscous resistance per unit length of channel can be written

$$
l = \frac { \rho _ { m } } { A } \frac { 1 - \mathrm { R e } \left[ f _ { v } \right] } { \left| 1 - f _ { v } \right| ^ { 2 } }\tag{2.74}
$$

and

$$
r _ { \nu } = \frac { \omega \rho _ { m } } { A } \frac { \mathrm { I m } \left[ - f _ { \nu } \right] } { \left| 1 - f _ { \nu } \right| ^ { 2 } } .\tag{2.75}
$$

The boundary-layer expressions earlier in this chapter, Eqs.' (2.21) and (2.22), are simply limiting forms of Eqs. (2.74) and (2.75) for large $\mathcal { R } _ { h } / \delta _ { \nu }$

Study Eqs. (2.74) and (2.75) and Fig. 2.13 carefully, and think of any channel as having inertance and resistance, with the details depending on fy. Both l and r are always positive $f _ { \nu } .$ $\mathbf { \Delta } _ { \pmb { r } _ { \pmb { \nu } } }$ (and real). Hence, the momentum equation can never give behavior that looks like negative inertial mass, nor can it give a negative flow resistance. From the limiting behavior of $f _ { \nu }$ for large $\scriptstyle { { \mathcal { R } } _ { h } }$ shown in Fig. 2.13, it is clear that in that limit $l \longrightarrow \rho _ { m } / A$ and $r _ { \nu } \longrightarrow 0 .$ At lessthan-infinite but still large $\mathcal { R } _ { h } , r _ { \nu }$ rises above zero as the importance of viscous drag at the wall increase, and l rises above $\rho _ { m } / A$ as the viscous penetration depth at the wall effectively reduces the available flow area. This is the regime of interest in resonator components and in pulse tubes. Forming the ratio

$$
\frac { r _ { \nu } } { \omega l } = \frac { \mathrm { I m } \left[ - f _ { \nu } \right] } { 1 - \mathrm { R e } \left[ f _ { \nu } \right] } ,\tag{2.76}
$$

we can easily see that in the vicinity of $R _ { h } \simeq \delta _ { \nu }$ the resistive and inertial parts of the impedance are of comparable magnitude. This is the regime of interest in the stacks of standing-wave thermoacoustic devices. In the smallest passages, such as in the regenerators of traveling-wave devices, the inertial part of the impedance is negligible compared to the resistive part.

Now examine the continuity equation. We rewrite Eq. (2.71) in the form

$$
d U _ { 1 } = - \left( i \omega c d x + \frac { 1 } { r _ { \kappa } } d x \right) p _ { 1 } + e d x U _ { 1 } ,\tag{2.77}
$$

as shown schematically in the right part of Fig. 2.14. The two familar symbols in the figure represent the compliance per unit length

$$
c = \frac { A } { \gamma p _ { m } } \left( 1 + \left[ \gamma - 1 \right] \mathrm { R e } \left[ f _ { \kappa } \right] \right)\tag{2.78}
$$

and the thermal-relaxation conductance per unit length, which is the inverse of a resistance

$$
{ \frac { 1 } { r _ { \kappa } } } = { \frac { \gamma - 1 } { \gamma } } { \frac { \omega A \ \operatorname { I m } \left[ - f _ { \kappa } \right] } { p _ { m } } } .\tag{2.79}
$$

The boundary-layer expressions earlier in this chapter, such as Eqs. (2.36) and (2.37), are simply limiting forms of Eqs. (2.78) and (2.79) for $R _ { h } / \delta _ { \kappa } \longrightarrow \infty ,$

Study Eqs. (2.78) and (2.79) and Fig. 2.13 carefully. Both c and $\boldsymbol { r } _ { \kappa }$ are always positive (and real). From the limiting behavior of $f _ { \kappa }$ for large channel size shown in Fig. 2.13, it is clear that in that limit $c \longrightarrow A / \gamma p _ { m }$ and $r _ { \kappa } \longrightarrow \infty$ . At less-than-infinite but still large channel size, $1 / { r _ { \kappa } }$ rises above zero as the importance of thermal relaxation at the wall increase, and c rises above $A / \gamma p _ { m }$ as the thermal penetration depth at the wall contributes a greater compressibility per unit volume than the compressibility far from the wall. This is the regime of interest in resonator components and in pulse tubes. Forming the ratio

$$
\frac { 1 } { \omega r _ { \kappa } c } = \frac { \left( \gamma - 1 \right) \mathrm { I m } \left[ - f _ { \kappa } \right] } { 1 + \left( \gamma - 1 \right) \mathrm { R e } \left[ f _ { \kappa } \right] } ,\tag{2.80}
$$

we can easily see that in the vicinity of $R _ { h } \simeq \delta _ { \kappa }$ the thermal-relaxation resistance and the compliance parts of the impedance are of comparable magnitude. This is the regime of interest in the stacks of standing-wave thermoacoustic devices. In the smallest passages, such as in the regenerators of traveling-wave devices, the thermal-relaxation-resistance part of the impedance is negligible compared to the compliance part.

The third, new symbol in the impedance diagram represents a controlled source e dx $U _ { 1 }$ (or sink, depending on sign) of volumetric velocity, proportional to the local volumetric velocity $U _ { 1 }$ itself, with proportionality constant

$$
e = \frac { \left( f _ { \kappa } - f _ { \nu } \right) } { \left( 1 - f _ { \nu } \right) \left( 1 - \sigma \right) } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x }\tag{2.81}
$$

which represents a sort of complex gain/attenuation constant for volumetric velocity, and which arises only when the temperature gradient $d T _ { m } / d x$ along the channel is nonzero.

![[mu_ad18d396_a7571ac415d53ee41c93.jpg]]  
Figure 2.14: Summary of the most important concepts of this chapter.

The eU1 term in the continuity equation has no dependence on ${ \pmb p } _ { 1 }$ , so it must not represent any sort of compressibility. To understand this term, let ${ \mathfrak { p } } _ { 1 } = 0$ so that c and $\pmb { r _ { \kappa } }$ don't confuse the issues in this paragraph. The dependence of the $e U _ { 1 }$ term on $d T _ { m } / d x$ is key. In a pulse tube or other large-diameter thermal buffer column, $f _ { \kappa }$ and $f _ { \nu }$ are very small, so that $e \simeq 0$ even though $d T _ { m } / d x \neq 0 .$ In this case, the $e U _ { 1 }$ term in the continuity equation simply says that whatever volumetric velocity goes in one end comes out the other end. The behavior is essentially the same as the displacement of a solid piston with a temperature gradient and mass-density gradient. At the opposite extreme, if a nonzero temperature gradient $d T _ { m } / d x$ exists along a channel with very small pore size, such as in a regenerator, the volumetricvelocity source term $e U _ { 1 }$ is very important. The small-channel limit of $\mathtt { E q }$ (2.81) is most important and most easy to appreciate: For $R _ { h } \ll \delta _ { \kappa }$ and $R _ { h } \ll \delta _ { \nu }$

$$
e U _ { 1 } \simeq \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } U _ { 1 } .\tag{2.82}
$$

In this case, the $e U _ { 1 }$ term in the continuity equation says that $d U _ { 1 } / U _ { 1 } = d T _ { m } / T _ { m }$ : The volumetric velocity is amplified in proportion to the temperature rise (or attenuated in proportion to a temperature drop). This is easy to understand as constancy of first-order mass flux $\rho _ { m } U _ { 1 }$ , which for an ideal gas is equivalent to constancy of $U _ { 1 } / T _ { m }$ : Whatever mass flux goes in one end must come out the other. In this limit of good thermal contact, $T _ { 1 } = 0$ so there can be no oscillating mass density in the volume dV.

The even greater complications of the intermediate regime, $R _ { h } / \delta _ { \kappa } \sim 1$ , encountered in the stacks of standing-wave systems, is suggested by the boundary-layer limit of Eq. (2.81):

$$
e U _ { \mathrm { { I } } } \simeq \frac { 1 - i } { 2 } \frac { 1 } { 1 + \sqrt { \sigma } } \frac { \delta _ { \kappa } } { R _ { h } } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } U _ { \mathrm { { I } } } .\tag{2.83}
$$

In this case, the volumetric velocity source is proportional to the volumetric velocity itself, but with a phase shift of $\tt - 4 5 ^ { \circ }$

If now we combine the momentum and continuity pictures as shown at the bottom of Fig. 2.14, we arrive at a complete, general impedance picture of thermoacoustics in any channel. We can think of $p _ { 1 } , U _ { 1 } , T _ { m } , d T _ { m }$ , and the geometry as given, so that the impedance diagram serves as a reminder of how the continuity and momentum equations yield $d p _ { 1 }$ and $d U _ { 1 }$

In most circumstances in a given location in a thermoacoustic system, many or most of the components in this general impedance picture can be neglected. Recalling that $\delta _ { \kappa } \sim \delta _ { \nu }$ for ideal gases, we can form a table that summarizes relative sizes and importance:

<table><tr><td>resonator pulse tube stack regenerator</td><td> $\overline { R } _ { h } \gg \delta$   $R _ { h } \gg \delta$   $R _ { h } \sim \delta$   $R _ { h } \ll \delta$ </td><td> $\omega l \gg r _ { \nu }$  ωc  $\gg 1 / r _ { \kappa }$   $\omega l \gg r _ { \nu }$   $\omega c \gg 1 / r _ { \kappa }$   $\omega l \sim r _ { \nu }$   $\omega c \sim 1 / r _ { \kappa }$   $\omega l \ll r _ { \nu }$   $\omega c \gg 1 / r _ { \kappa } \quad e \simeq \nabla T _ { m } / T _ { m }$ </td><td> $e = 0$   $e \sim 0$  e complex</td></tr></table>

Further simplification in understanding thermoacoustic devices can be achieved by considering the relative sizes of $\mathcal { P } 1$ and $U _ { 1 }$ in a given component, to determine whether either L or C can be neglected.

Example: Standing-wave engine. Each stack in the engine of Figs. 1.9 and 1.10 was of parallel-plate constructio, with gaps between plates of 0.010 inch, so $R _ { h } = 0 . 1 3$ mm. At the stack center, where the temperature is about 550 K, the thermal and viscous penetration depths are $\delta _ { \kappa } = 0 . 1 2$ mm and $\delta _ { \nu } = 0 . 1 0$ mm at a typical operating point with 3 MPa helium at 390 Hz. Hence, with $R _ { h } / \delta _ { \kappa } = 1 . 1$ and $R _ { h } / \delta _ { \nu } = 1 . 3 ,$ we know that all of the impedance components—inertance, viscous resistance, compliance, thermal-relaxation resistance, and volumetric-velocity source-could be important. However, the stacks are close to the velocity nodes of the standing wave, so it is likely that the inertance and viscous resistance will be less important than the other three components. The impedance diagram shown in Fig. 2.15 probably has adequate detail to convey the most important features of the apparatus. The overall resonance is portrayed as Helmholtz-like, with an inertance between two compliances. Although this level of detail does not show the wave nature of the x dependences of ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ in the apparatus, it does successfully show that the pressures on the left and right halves of the apparatus are $1 8 0 ^ { \circ }$ out of phase, with the pressure on the left half of the apparatus leading the volumetric velocity through the inertance by $9 0 ^ { \circ }$ and the pressure on the right half of the apparatus lagging the volumetric velocity through the inertance by $9 0 ^ { \circ }$ . Judging by eye in Fig. 1.10 that the volumes of gas in each stack and hot duct are comparable, we know that the stack compliance must be as important as the hot-duct compliance; the stack compliance causes $\triangle U _ { 1 }$ across the stack tó be nearly as large as $U _ { 1 }$ itself at the hot end of the stack. It turns out that the thermal-relaxation resistance and volume velocity source in the stack cause a smaller change in $| U _ { 1 } |$ and only about $\approx 5 ^ { \circ }$ phase shift between $U _ { 1 }$ at the left and right ends of each stack; the effects of the branch to the refrigerators are'compárable.

![[mu_ad18d396_0622b28058cc80b1f777.jpg]]  
Figure 2.15: Schematic impedance diagram for the standing-wave engine example.

To obtain more detailed information about ${ \pmb p } _ { 1 }$ and $\scriptstyle { \bar { U } } _ { 1 }$ in this system, I gave DeltaE all the geometry of half of the apparatus, the helium pressure, temperatures, etc., picked one particular operating amplitude, and asked DeltaE to tabulate ${ \pmb p } _ { 1 }$ and $\pmb { U _ { 1 } }$ as a function of position in the apparatus. (See Appendix for details.) The result is shown in Fig. 2.16. (In anticipation of the next chapter, the figure is flipped left-to-right relative to previous figures of this apparatus.) I chose the phase of ${ \pmb p } _ { 1 }$ to be zero at ${ \pmb x } = { \pmb 0 } .$ . Then for a standing wave, we expect the pressure to remain real and to look largely like a cosine of ${ \pmb x } ,$ and the volumetric velocity to be imaginary and look largely like a sine of ${ \pmb x } ,$ as shown in the figure. The dependence of $A$ on ${ \pmb x } ,$ appararent in the scale drawing, causes $| p _ { 1 } |$ and $| \bar { U } _ { 1 } |$ to deviate from perfect trigonometric functions, but these deviations are not visible to the naked eye in the figure. For the most part, $d p _ { 1 } / d x$ is due to inertance and $U _ { 1 }$ , and $d U _ { 1 } / d x$ is due to compliance and ${ \pmb { p } } _ { \bf 1 }$

However, there are small out-of-phase components to ${ \pmb p } _ { \bf 1 }$ and $U _ { \mathbf { 1 } }$ , which have been multiplied by 20 and 10 respectively in Fig. 2.16 in order to display them clearly. As with most standing-wave systems, the phase difference between ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ remains so close to $9 0 ^ { \circ }$ that phasor diagrams are of limited usefulness. The step in $\mathtt { R e } [ U _ { 1 } ]$ occurs at the branch to the refrigerators, and accounts for the $U _ { 1 }$ flowing into the refrigerators. The upward slope of $\mathtt { R e } [ U _ { 1 } ]$ through the stack is due to the volumetric-velocity source term throughout the stack, and the upward slope of Im[pi] is due to $\pmb { r } _ { \pmb { \nu } }$ in the stack. The weaker slopes of $\mathtt { R e } [ U _ { 1 } ]$ and $\bf { I m } [ p _ { 1 } ]$ elsewhere are partly due to $\pmb { r _ { \kappa } }$ and $\mathbf { \Delta } _ { \pmb { r } _ { \pmb { \nu } } }$ elsewhere, but also from c and l interacting with Im $\{ p _ { 1 } \}$ and $\mathtt { R e } [ U _ { 1 } ]$ , respectively.

![[mu_ad18d396_751f79bbfc4bea624c45.jpg]]

![[mu_ad18d396_cde841129bd501bf01f3.jpg]]  
Figure 2.16: Results of numerical integration of the momentum and continuity equations for the standing-wave engine example. (a) Relevant portions of crude impedance diagram. (b) Scale drawing of apparatus. (c) p1. (d) $U _ { 1 }$

Example: Traveling-wave engine. The regenerator in the engine of Figs. 1.13 and 1.14 is a bed of stainless-steel screen with a hydraulic radius of $4 2 \mu \mathrm { m }$ At a typical operating point, 80 Hz and 3 MPa helium gas, and with the center of the regenerator at 650 K, the penetration depths are $\delta _ { \kappa } = 3 0 0 \mu \mathrm { m }$ and $\delta _ { \nu } = 2 5 0 . \mu \mathrm { m }$ . Hence, we have $R _ { h } \ll \delta ,$ so inertance and thermal-relaxation resistance are negligible, and the volumetric velocity source is well described by Eq. (2.82). The regenerator is adequately modeled with the three components labeled “regenerator" in Fig. 2.17. The thermal buffer column is 9 cm diam, so it has $R _ { h } \gg \delta ,$ so its most important dynamic characteristic is its compliance, also shown in Fig. 2.17. The feedback path is most roughly modeled as an inertance (the straight section) in series with a compliance (the 180-degree U bend at the left end); we neglect the resistances associated with these two components for now. The resonator to the right of the junction is approximately an inertance (the uniform-diam section) in series with a compliance (the big volume on the end), with both of these components having associated resistances. Neither of these resonator components is really lumped, but we will neglect those details for now. The adjustable load on the system, comprising an adjustable valve in series with a tank, can be modeled as a resistance in·series with a compliance. Hence, the impedance diagram of Fig. 2.17 shows the most important features of this system.

![[mu_ad18d396_f1859f6f373d72e69e53.jpg]]  
Figure 2.17: Impedance diagram for traveling-wave engine example.

Animation Tashe /t shows these same features for the traveling-wave engine, omitting the resonator and adjustable load. Study the animation and Fig. 2.17 together. In the animation, you should be able to "see" many features that we have discussed in this chapter. The expected behavior of each of the two large compliances should be apparent, with $U _ { 1 }$ $\mathfrak { s } _ { \mathtt { i n } } \mathfrak { n }$ differing from $U _ { 1 }$ "out"; close examination will show the $9 0 ^ { \circ }$ phase difference between $\triangle U _ { 1 }$ and ${ \pmb p } _ { 1 }$ . The joining conditions—conservation of ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ at the transitions between components—should be apparent, such as'at the ends of the inertance and at the three-way junction. It should be apparent that the velocity through the regenerator, which is resistive, is in phase with $\Delta p _ { 1 }$ , while the velocity through the inertance lags $\Delta p _ { 1 }$ by $9 0 ^ { \circ }$ . I know that the compliance and volumetric-velocity source associated with the regenerator are correctly programmed in this animation too, but I confess they are too subtle for me to see here.

Example: Standing-wave refrigerator. Figure 2.18 shows a lumped-impedance diagram for the standing-wave refrigerator of Figs. 1.11 and 1.12. The stacks have $R _ { h } / \delta \sim 1$ so all of the impedance components—inertance, viscous resistance, compliance, thermalrelaxation resistance, and volumetric-velocity source—could be important in them. In the standing-wave engine above, we argued that the stacks were close to the velocity nodes of the standing wave, so we neglected their inertance and viscous resistance. In this refrigerator, the stacks are not so close to the velocity nodes, so we cannot neglect these momentumequation contributions. The loudspeakers contribute significantly to the dynamics, so we should at least include the mass and spring constant of each; I've made up new symbols for these—a rectangular brick for mass, and something that reminds me of automotive leaf springs for the spring constant.

![[mu_ad18d396_6981f3bbe8b60f499528.jpg]]  
Figure 2.18: Schematic impedance diagram for the standing-wave refrigerator example.

Example: Traveling-wave refrigerator. The impedance diagram of Fig. 2.19a symbolically represents the most important dynamic features of the orifice pulse-tube refrigerator of Figs. 1.15 and 1.16. The rightmost compliance C is the so-called compliance itself. The adjacent inertance L and resistance $\scriptstyle { R _ { s } }$ represent the refrigerator's inertance tube and two valves, with valve settings the same as in the related example near Fig. 2.8 above: The parallel valve $R _ { p }$ in Fig. 2.8 is closed, and the series valve $R _ { \vartheta }$ in Fig. 2.8 is adjusted so that $\begin{array} { r } { \mathcal { R } _ { s } = \omega L / 2 } \end{array}$ The compliance of the pulse tube is significant, and is shown as $C _ { p t }$ . With $R _ { h } / \delta \sim 0 . 1$ in the regenerator, its compliance $C _ { \tt r e g }$ , viscous resistance $R _ { \tt r e g } ,$ and volumetric velocity source $\Delta U _ { 1 S } = - U _ { \mathrm { { l i n } } } \left( T _ { \mathrm { { i n } } } - T _ { c o l d } \right) / T _ { \mathrm { { i n } } }$ represent the regenerator well.

(a)  
![[mu_ad18d396_76cf196b3553471d9226.jpg]]

![[mu_ad18d396_5524492a452c998ced5b.jpg]]  
Figure 2.19: (a) Schematic impedance diagram of the orifice pulse-tube refrigerator. (b) Phasor diagram, with the phase of $U _ { \mathrm { 1 0 u t } }$ set to zero. (c) Same phasor diagram, but rotated so that the phase of ${ p } _ { 1 p t }$ is set to zero.

I used the impedance diagram of Fig. 2.19a and quantitative information about the hardware geometry to construct the phasor diagram of Fig. 2.19b, starting from the right end of the impedance network and working to the left. We already did part of the work in Fig. 2.8c above; $p _ { 1 C } , U _ { \mathrm { 1 o u t } } ,$ and $\scriptstyle p _ { 1 p t }$ are copied from that figure. The compliance of the pulse tube then determines $U _ { 1 \mathrm { c o l d } } ;$ next $C _ { \mathrm { r e g } }$ and $\Delta U _ { 1 s }$ determine $U _ { \mathrm { { 1 i n } } } ;$ finally $R _ { \tt r e g }$ determines $\pmb { p } _ { 1 \mathbf { i n } } .$

Example: iperfect inertance. Sometimes it is impossible to provide a desired phase shift in $Z = p _ { 1 } / U _ { 1 }$ using an inertance, because the unavoidable compliance and viscous resistance can cause phase shifts of the opposite sign, as illustrated in Fig. 2.20.

These variables are not completely independent, because the cross-sectional area, volume, and surface area of a tube are not independent. Suppose that the viscous resistance $\boldsymbol { r } _ { \nu }$ and the compliance c per unit length of this inertance are not negligible, as shown in the figure, and suppose it is desired that $Z _ { I _ { \pmb { n } } }$ should lead $Z _ { O u t } .$ Figure 2.20b shows that, even though l works in the correct direction, causing ${ p } _ { 1 I n }$ to lead $\scriptstyle { \mathcal { P } } 1 o _ { u t } ,$ the compliance c works to shift $U _ { 1 I n }$ ahead of $U _ { 1 O u t }$ , so that the impact on the phase of $z$ could have either sign, depending on the quantitative details of $l , r _ { \nu } ,$ and c.

(b)  
![[mu_ad18d396_d182e1a2681fe4c2edc1.jpg]]

![[mu_ad18d396_16521c0c6c72b5faf72c.jpg]]

![[mu_ad18d396_be72e0e6f937045947ed.jpg]]  
Figure 2.20: (a) A lossy inertance and a compliance, such as might be used at the end of a small pulse-tube refrigerator. A short length dx of the lossy inertance is highlighted (b) Impedance diagrams for the short length dx of the lossy inertance; on the left, the compliance per unit length is negligible, while on the right it is not negligible. (c) Phasor diagrams for the short length dx of the lossy inertance; on the left, the compliance per unit length is negligible, while on the right it is not negligible.

## 2.5. Exercises

2.1 Review complex notation: show that $\overline { { p ( t ) u ( t ) } } = \mathrm { R e } [ p _ { 1 } \widetilde { u _ { 1 } } ] / 2 = | p _ { 1 } | | u _ { 1 } | \left( \cos \phi \right) / 2$ , where $\phi$ is the phase angle between ${ \pmb p } _ { 1 }$ and $\boldsymbol { \mathscr { u } } _ { 1 }$

2.2 More review: show that the phase of the ratio of two complex numbers is the difference between the phases of the numbers. Consider $Z = p _ { 1 } / U _ { 1 }$ . What is the phase of the impedance of a traveling wave? If pressure oscillations lead velocity oscillations in a more general wave, is the phase of the impedance positive or negative?

2.3 The sealed resonator shown in Fig. 2.21, consisting of a central duct of length $\mathbf { 2 } \Delta \pmb { x _ { 1 } }$ and area A1 between two other ducts each of length ∆x2 and area A2, is intermediate between $A _ { 1 }$ $\Delta x _ { 2 }$ $\mathbf { A _ { 2 } } ,$ a double Helmholtz resonator and a plane wave resonator. Show that the fundamental frequency is given by

$$
\frac { A _ { 2 } } { A _ { 1 } } \tan \frac { \omega L _ { 1 } } { a } \tan \frac { \omega L _ { 2 } } { a } = 1 .\tag{2.84}
$$

Show that this reduces to something sensible when $A _ { 2 } = A _ { 1 }$ . Show that it reduces to the expression for a double Helmholtz resonator for $A _ { 1 } < A _ { 2 } , \Delta x _ { 1 } \ll \lambda$ and $\Delta x _ { 2 } \ll \lambda$

![[mu_ad18d396_087adb1b4b40cc06f722.jpg]]  
Figure 2.21: Geometry for exercise 2.3.

2.4 Does $p _ { 1 } ( x ) = C$ sin kx represent a standing wave or a traveling wave? Does $p _ { 1 } ( x ) =$ $\boldsymbol { C e } ^ { i k x }$ represent a standing wave or a traveling wavè? Use the lossless first-order momentum equation to write down $u _ { 1 } ( x )$ in both cases. Use the lossless first-order continuity equation to check your expressions for ${ \pmb u } _ { 1 } ( { \pmb x } )$ . How would you write $p _ { 1 } ( x )$ for a standing wave with a temporal phase shift of $9 0 ^ { \circ }$ relative to this standing wave? What about a quarter-wavelength spatial shift in the node locations?

2.5 Consider a lossless duct of uniform cross-sectional area, sealed at both ends, of length $\Delta { \pmb x } .$ The fundamental resonance frequency is $f = a / 2 \Delta x ,$ because that is the frequency for which a half-wavelength wave $" 6 t s "$ in the pipe, with velocity nodes at the sealed ends. If you knew nothing about waves, you might think this resonator was essentially like the double Helmholtz resonator, with an inertial mass of gas in the central third of the resonator bouncing against the compliances of gas in the outer thirds of the resonator. If you calculated the resonance frequency using this lumped-impedance picture, how different would your result be from the true resonance frequency $a / 2 \Delta x ?$ What if you used the central half and the outer quarters?

2.6 Verify that Eqs. (2.59) and (2.60) approach Eqs. (2.57) and (2.58) as $R _ { h } / \delta \longrightarrow \infty$

2.7 Combine Eqs. (2.56) and (2.71) to obtain Rott's wave equation.

2.8 Check the derivations of all equations in this chapter, except Eqs. (2.59)—(2.67).

2.9 Look closely at the computer animations Viscous and Oscwall. Use "pause" on your keyboard to study "viscous" very carefully. It looks like the gas motion about a penetration depth away from the wall leads the motion farther from the wall. Des this make sense, or did the author make a minus-sign mistake when he made the animation?

2.10 The specific acoustic impedance of a wave is defined as

$$
z = \frac { A p _ { 1 } } { U _ { 1 } } .\tag{2.85}
$$

Show that the specific acoustic impedance of a lossless plane traveling wave is $\pm \rho \alpha$ . Show that the specific acoustic impedance of a lossless plane standing wave is $\pm \rho  { \alpha }$ tan $\left\{ \omega \left( { \pmb x } - { \pmb x } _ { 0 } \right) / a \right\}$ As the wave crosses from a first duct of area $A _ { f }$ to a second duct of area $A _ { s }$ , which impedance is continuous—z or $Z ?$

2.12 Show that $T _ { 1 } / T _ { m } = ( \gamma - 1 ) p _ { 1 } / \gamma p _ { m }$ for an ideal gas experiencing adiabatic pressure oscillations. What is the value of $( \gamma - 1 ) / \gamma$ for your favorite gas? What is proportionality constant links $T _ { 1 } / T _ { m }$ and ${ \mathfrak { p } } _ { 1 } / { \mathfrak { p } } _ { m }$ for an ideal gas experiencing isothermal pressure oscillations? How big is $\mathcal { T } _ { 1 }$ at a few locations in your favorite hardware? How big is $\mathcal { T } _ { 1 }$ for “audio" acoustics in air?

2.13 Sketch $\left| p _ { 1 } \right\}$ and either $| U _ { 1 } |$ or $| \langle u _ { 1 } \rangle |$ for your favorite piece of hardware.

2.14 Estimate the inertance, compliance, and resistances of some components in your favorite piece of thermoacoustics hardware. Compare $R _ { \nu } , \ : \omega L , \ : 1 / \omega C ,$ and $1 / G _ { \kappa } .$ Do the relative magnitudes make sense?

2.15 A Helmholtz resonator consists of a 4 liter spherical volume V and a cylindrical neck having a diameter of $2 r = 2$ cm and a length $\Delta x = 5$ cm. It is filled with air at 300 Kelvin and 1 bar.

What is the inertance of the neck? How does it compare with the mass of gas in the neck? What is the compliance of the volume? What is the resonance frequency? At resonance, how does $\omega L$ compare with $1 / \omega C ?$ How does λ compare with the various dimensions in the problem? How do $\delta _ { \nu }$ and $\delta _ { \kappa }$ compare with the other dimensions?

2.16 Draw a reasonably detailed impedance diagram for your favorite piece of thermoacoustics hardware.

2.17 In this chapter, my choice of $U _ { 1 }$ and ${ \pmb p } _ { 1 }$ as the variables of greatest interest led to the forms of the momentum and continuity equations that we used, and from there to the forms of the impedance diagrams that we used. However, other choices can be made, with equal success if employed self consistently. Your task: reconstruct some of the important results and figures of this chapter from a different point of view, with the variables of greatest interest being the average gas velocity $\left. u _ { 1 } \right.$ and the fórce $F _ { 1 } = A p _ { 1 }$ exerted by the gas at x on the gas at $x + d x$ . To construct impedance diagrams, invent symbols for moving mass $^ { m , }$ spring $k ,$ dashpots $\textstyle { \mathcal { R } } _ { \nu }$ and $G _ { \kappa }$ , and thermally induced velocity source d $\langle u _ { 1 s } \rangle$ . Draw your version of the impedance diagram for the most general thermoacoustic element of length dx, thinking carefully which components should be drawn in parallel (sharing the same $\left. u _ { 1 } \right. )$ and in series (sharing the same $F _ { 1 } )$ . What are the joining conditions from one segment to the next, corresponding to our use of continuity of ${ \mathfrak { p } } _ { 1 }$ and $U _ { 1 }$ in the text? Do you think your version is more intuitively understandable than the version used in the text? Why or why not?

2.18 Assign names to the pressures and volumetric velocities at key locations in Fig. 2.17. (Remember to define a positive direction for each velocity.) Construct a phasor diagram, by examining the figure and Ani. Tashe /t. Don't worry about details; just try to get relative phase angles correct to within ±45°. Repeat this exercise for Fig. 2.18.

## 3. POWER

Products of first-order variables (such as ${ \pmb { p _ { 1 } } }$ and $\bar { U } _ { 1 } )$ represent power, which is of paramount importance in thermoacoustic engines and refrigerators. Introductory acoustics textbooks teach that

$$
\frac { \omega } { 2 \pi } \oint p ( t ) { \bf v } ( t ) d t = \frac { 1 } { 2 } \operatorname { R e } \left[ p _ { 1 } \widetilde { \bf v _ { 1 } } \right] ,\tag{3.1}
$$

which is called the acoustic intensity, is the time-averaged "power per unit area" in a sound wave. It's not so simple in thermoacoustics. We must be very careful to identify which type of power we are talking about, because there are so many important types of energy and power in thermodynamics—enthalpy, heat, Gibbs free energy, etc., etc.

The concept of acoustic intensity is so familiar to acousticians that we are reluctant to abandon it. Hence, in this book we will make as much use as possible of the integral of the acoustic intensity across the cross-sectional area of the channel:

$$
\dot { E } _ { 2 } ( x ) ~ = ~ \frac { \omega } { 2 \pi } \oint \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] \mathrm { R e } \left[ U _ { 1 } ( x ) e ^ { i \omega t } \right] d t\tag{3.2}
$$

$$
= \frac { 1 } { 2 } \operatorname { R e } \Big [ p _ { 1 } \widetilde { U _ { 1 } } \Big ] = \frac { 1 } { 2 } \operatorname { R e } \{ \widetilde { p _ { 1 } } U _ { 1 } \}\tag{3.3}
$$

$$
\mathbf { \Sigma } = \mathbf { \Sigma } \frac { 1 } { 2 } \left| p _ { 1 } \right| \left| U _ { 1 } \right| \cos \phi _ { p U } ,\tag{3.4}
$$

where $\phi _ { p U }$ is the phase angle between ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ . We call this the acoustic power flowing in the x direction, giving it the subscript 2 to remind us that it is second order—the product of two first-order quantities. Note also that it is a time average; we're not interested in instantaneous power delivered along ${ \pmb x } ,$ only the power averaged over an integer number of cycles of the sound wave.

Similarly; enthalpy is very familiar to mechanical and chemical engineers, because it is the key energy of fluid dynamics, of great use when considering the first law of thermodynamics. We will see below that

$$
\dot { H } _ { 2 } ( x ) = \frac { 1 } { 2 } \rho _ { m } \operatorname { R e } \left[ h _ { 1 } \widetilde { U _ { 1 } } \right] - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \frac { d T _ { m } } { d x } ,\tag{3.5}
$$

where $\boldsymbol { h }$ is the enthalpy per unit mass, is the acoustic approximation to the time-averaged total power flowing in the positive x direction.

·In this chapter and Chapter 4 our understanding of the use and meaning of $\dot { E } _ { 2 }$ and $\dot { H } _ { 2 }$ will grow.

![[mu_ad18d396_6bf3d3c19961054df990.jpg]]  
Figure 3.1: (a) Typical phasor diagrams for positive acoustic power flow in the positive x direction. The angle between ${ \mathfrak { p } } _ { 1 }$ and $\bar { U _ { 1 } }$ is acute. (b) Typical phasor diagrams for zero acoustic power flow. The angle between ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ is 90°. (c) Typical phasor diagrams for acoustic power flow in the negative x direction. The angle between ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ is obtuse.

## 3.1. Acoustic power

Acoustic power depęnds strongly on the phase angle between ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ . Whether using Eq. (3.2), (3.3), or (3.4) for acoustic power $\dot { E } _ { 2 }$ , it is immediately apparent that $\dot { E } _ { 2 } = 0$ when the phase between pressure and volumetric velocity is $9 0 ^ { \circ }$ , i.e. for standing-wave phasing. For a pure rightward traveling wave, $\dot { E } _ { 2 } > 0$ . For a pure leftward traveling wave, $\dot { E } _ { 2 } < 0$ Whenever $| \phi _ { p U } | < 9 0 ^ { \circ }$ , acoustic power flows in the positive x direction; when this angle is between 90° and 180°, acoustic power flows in the negative x direction, as illustrated in Fig. 3.1.

The utility of $\dot { E } _ { 2 } ( x )$ in acoustics is due largely to its intuitive appeal as describing a sort of flux of mechanical power past the location x. This interpretation is possible because the volumetric velocity $U _ { 1 } ( x )$ is equal (to first order only!) to the volumetric velocity of the particular slab of gas whose average position is at x. Letting V be the oscillating part of the volume of gas to the left of this slab of gas, so $U = d V / d t$

$$
\dot { E } _ { 2 } ( x ) = \frac { \omega } { 2 \pi } \oint p U d t = \frac { \omega } { 2 \pi } \oint p d V ,\tag{3.6}
$$

![[mu_ad18d396_e39bec915a1954e0a679.jpg]]  
Figure 3.2: Acoustic power flows down a channel of area A. The absorption of acoustic power within the length dx is of interest.

which we recognize as the standard thermodynamic expression for the time-averaged rate at which work is done by a piston. Hence, $\dot { E } _ { 2 } ( x )$ can be interpreted as giving the work done by a slab of gas, whose average position is ${ \pmb x } ,$ on the gas in front of it, as if the slab of gas whose average position is x were a solid piston.

These points are illustrated in Anis. Wave $/ { \mathbf { v } }$ and Wave $/ \mathbf { u } .$ Animation Wave $/ \mathbf { v }$ is the same rightward-traveling wave we examined in Chapter 1, but with additional purple ellipses representing $\dot { E } _ { 2 }$ at two typical locations. The horizontal coordinate of the small white dot tracing the ellipse is equal to the location of the slab of gas in question; the vertical coordinate is ${ \pmb p } .$ Hence, the purple area of the ellipse is proportional to $\oint _ { } \pmb { p } d V ,$ and so this area can be taken as a representation of $\dot { E } _ { 2 }$ . The clockwise rotation of the small white dot tracing the ellipse indicates that $\dot { E } _ { 2 } > 0$ . Recalling from Fig. 1.19 that ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ are exactly in phase for this animation, i.e. ${ \pmb p } _ { 1 }$ and $V _ { 1 }$ are $9 0 °$ out of phase, we see that this case gives the fattest ellipse possible for these amplitudes $\left| p _ { 1 } \right|$ and $| U _ { 1 } |$

Similarly, Ani. Wave $/ { \mathfrak { u } }$ is the same standing-wave animation we examined in Chapter ${ \mathfrak { l } } ,$ but with the addition of $\pmb { p V }$ traces at two typical locations. Recalling from Fig. 1.19 that ${ \pmb p } _ { 1 }$ and $\pmb { U _ { 1 } }$ are exactly $9 0 ^ { \circ }$ out of phase for this animation, i.e. $\dot { p _ { 1 } }$ and $V _ { 1 }$ are exactly in phase, we see why the $p V$ “ellipses" are nothing but reciprocating lines. Since these lines enclose no area, 'they show that $\dot { E } _ { 2 } = 0$ . Pure standing waves carry no acoustic power.

Typical waves of interest in thermoacoustic engines and refrigerators are neither pure standing wave nor pure traveling wave. In the typical so-called standing wave engine or refrigerator, the phase between pressure and volumetric velocity is typically in the range of $8 5 ^ { \circ }$ to $9 5 ^ { \circ }$ in the stack. Such a wave is illustrated in Ani. Wave $/ \mathbf { k } .$ At first glance this wave is barely distinguishable from a pure standing wave, but close examination shows nonzero area in the $\pmb { p V }$ ellipses, i.e. nonzero acoustic power transmitted to the right by the wave. Also note that there are no longer true nodes of pressure or velocity; the locations that at first appear to be nodes are actually regions of small amplitude having a slight nonzero oscillation eyerywhere.

Animation Wave, with any of its /options, assumes that $\dot { E } _ { 2 }$ is constant; $d \dot { E } _ { 2 } / d x = 0 .$ However, the interaction of a sound wave in a channel with the channel walls leads to $d \dot { E } _ { 2 } / d x \neq 0$ As in Chapter ${ \mathfrak { 2 } } ,$ we consider sound propagating in the $\pmb { x }$ direction in an ideal gas within a channel with constant cross sectional area $A ,$ as shown in Fig. 3.2. We adopt the usual complex notation for time-oscillatory quantities, namely Eqs. (2.10)-(2.13). To find the time-averaged acoustic power $d \dot { E }$ produced in a length dx of the channel, we write

$$
\frac { d \dot { E } } { d x } = \int \frac { d \left( \overline { { p { u } } } \right) } { d x } d y d z\tag{3.7}
$$

where the overbar denotes time averaging and the integral is over the cross-sectional area A of the channel. Rewriting Eq. (3.7) in complex notation and expanding the x derivative gives

$$
\frac { d \dot { E } _ { 2 } } { d x } = \frac { 1 } { 2 } \mathrm { R e } \left[ \widetilde { U _ { 1 } } \frac { d p _ { 1 } } { d x } + \widetilde { p _ { 1 } } \frac { d U _ { 1 } } { d x } \right] ,\tag{3.8}
$$

where the tilde denotes complex conjugation. We can obtain $d p _ { 1 } / d x$ and $d U _ { 1 } / d x$ from the momentum and continuity equations in Chapter $\mathbf { 2 ; }$ Equations. (2.73) and (2.77) provide a convenient form. Making these substitutions, we obtain

$$
\frac { d \dot { \bar { E } } _ { 2 } } { d x } = - \frac { r _ { \nu } } { 2 } | U _ { 1 } | ^ { 2 } - \frac { 1 } { 2 r _ { \kappa } } | p _ { 1 } | ^ { 2 } + \frac { 1 } { 2 } \mathrm { R e } \left[ e \widetilde { p _ { 1 } } U _ { 1 } \right] .\tag{3.9}
$$

When you look at an impedance diagram for a thermoacoustic component, such as the general impedance diagram of Fig. 2.14, realize that Eq. (3.9) shows that only three of the five impedance components affect acoustic power; inertance and compliance have no direct effect on acoustic power; they only cause $p _ { 1 } ( x )$ and $U _ { \mathbf { 1 } } ( { \pmb x } )$ to evolve in ways that keep $\scriptstyle { \frac { 1 } { 2 } } \mathrm { R e } [ \widetilde { p _ { 1 } } U _ { 1 } ]$ independent of x.

The first two terms in Eq. (3.9) are always negative; the first term gives the viscous dissipation of sound and the second term gives the less intuitively obvious thermal-relaxation dissipation. The third term, which can have either sign, is of the greatest interest in thermoacoustic engines and refrigerators. We will spend the rest of this section interpreting these three terms.

## 3.1.1. Acoustic power dissipation with $d T _ { m } / d x = 0$

With $d T _ { m } / d x = 0$ , Eq. (3.9) reduces to

$$
\frac { d \dot { E } _ { 2 } } { d x } = - \frac { r _ { \nu } } { 2 } \left| U _ { 1 } \right| ^ { 2 } - \frac { 1 } { 2 r _ { \kappa } } \left| p _ { 1 } \right| ^ { 2 } .\tag{3.10}
$$

This expression gives the ordinary dissipation of acoustic power per unit length in a channel. Fortunately, this expression is easy to interpret because it is so simple. Both terms are negative, so both always represent dissipation: If power flows in the positive x direction, then $| \dot { E } _ { 2 } ( x + d x ) | < | \dot { E } _ { 2 } ( x ) |$ , while if power flows in the negative x direction, then $| \dot { E } _ { 2 } ( x ) | <$ $| \dot { E } _ { 2 } ( x + d x ) |$ . Both terms in $d \dot { E } _ { 2 } / d x$ are independent of $\dot { E } _ { 2 } \sim p _ { 1 } \widetilde { U _ { 1 } }$ itself; i.e., the local dissipation of acoustic power is independent of the transmission of acoustic power. There is a clean separation between viscous and thermal-relaxation effects: The first term, describing viscous dissipation, is proportional to $| U _ { 1 } | ^ { 2 }$ and is independent of thermal conductivity, while the second term, describing thermal-relaxation dissipation, is proportional to $\lvert p _ { 1 } \rvert ^ { 2 }$ and is independent of viscosity.

In the boundary-layer approximation, in which all dimensions of the channel are much larger than the penetration depths, Eq. (3.10) can be written

$$
\frac { d \dot { E } _ { 2 } } { d S } = - \frac { 1 } { 4 } \rho _ { m } \left. \frac { U _ { 1 } } { A } \right. ^ { 2 } \delta _ { \nu } \omega - \frac { 1 } { 4 } \frac { \left. p _ { 1 } \right. ^ { 2 } } { \gamma p _ { m } } \left( \gamma - 1 \right) \delta _ { \kappa } \omega ,\tag{3.11}
$$

where S is the surface area of the channel. This expression gives the ordinary dissipation of $s$ acoustic power in a large channel, and is easily remembered in terms of the energy density. The mean kinetic energy per unit volume $\dot { \rho _ { m } } | \bar { U _ { 1 } } / A | ^ { 2 } / 4$ times $\delta _ { \nu }$ is roughly the kinetic energy in the gas within a viscous penetration depth of the solid surface, per unit area of the surface; the viscous dissipation term shows that this energy is dissipated by viscous shear at an average rate ω. Similarly, the thermal-relaxation term shows that the mean adiabatic $\omega .$ compressive energy density $| p _ { 1 } | ^ { 2 } / 4 \gamma p _ { m }$ stored in unit volume of the gas is dissipated at an average rate $( \gamma - 1 )$ ω within a region of thickness $\delta _ { \kappa }$ near the solid surface. The extra factor $( \gamma - 1 )$ appears because this thermal dissipation is proportional to the difference between the isothermal and adiabatic compressibilities, which is proportional to $( \gamma - 1 )$

The viscous term arose from the

$$
\mathbb { R e } \left[ \widetilde { U } _ { 1 } \frac { d p _ { 1 } } { d x } \right]
$$

term in Eq. (3.8), and can be better appreciated by considering Ani. Viscous $/ \mathbf { m } .$ Close examination of the animation shows that the gas motion far from the solid boundary is in phase with $d p _ { 1 } / d x ,$ so the velocity $u _ { 1 } ( \infty )$ far from the solid boundary is $9 0 ^ { \circ }$ out of phase from $d p _ { 1 } / d x$ . Hence, the gas far from the solid boundary, where the dynamics is purely inertial, has $\mathrm { R e } [ \widetilde { u _ { 1 } } d p _ { 1 } / d x ] = 0$ and contributes nothing to $d \dot { E } _ { 2 } / d x$ . The dissipation arises close to the solid boundary, where the phase of u1 is shifted by viscous interaction with the ${ \boldsymbol { u } } _ { 1 }$ wall. Naively, when I watch Ani. Viscous I see layers of gas sliding relative to one another, with viscous "friction" between the layers turning mechanical energy into heat.

Example: Standing-wave refrigerator. In Chapter ${ \mathfrak { 2 } } ,$ we calculated the viscous resistance of the lower central tee of the standing-wave refrigerator to be $R _ { \nu } = 7 5 ~ \mathrm { P a } { \cdot } \mathrm { s } / \mathrm { m } ^ { 3 }$ At a typical operating point, $| U _ { 1 } | = 0 . 1 6 ~ \mathrm { m } ^ { 3 } / \mathrm { s }$ Hence this component dissipates 1.0 Watt of acoustic power, due to viscosity. (There is negligible ${ \pmb p } _ { 1 }$ in this component, and hence negligible thermal-relaxation dissipation.) This is less than 2% of the total acoustic power $2 \%$ supplied to the resonator by the loudspeakers. The center of this component is a center of symmetry of the apparatus, so it must be that $\dot { E } _ { 2 } = 0$ at the center. Hence, 0.5 W must flow into the tee from each side. Taking the positive x direction toward the right, we would say that $\dot { E } _ { 2 } = + 0 . 5 $ W at the left end of the tee, and $\dot { E } _ { 2 } = - 0 . 5$ W at the right end of the tee.

Example: Traveling-wave refrigerator. Near Fig. 2.8, we introduced the impedance network at the end of the traveling-wave refrigerator, with an example in which $R _ { s } = 3 . 3 5$ $\mathrm { M P a } { \cdot } { \bf s } / \mathrm { m } ^ { 3 }$ . At a typical operating point, with $| U _ { 1 } | = 0 . 0 4 ~ \mathrm { m } ^ { 3 } / \mathrm { s } ,$ the flow resistance $\scriptstyle { R _ { s } }$

dissipates 2700 W of acoustic power. This impedance network consumes a significant fraction of the 9000 W of acoustic power supplied to the entire refrigerator.

Compared to viscous dissipation, the dissipation of acoustic power by thermal relaxation is more difficult to appreciate. Since thermal-relaxation dissipation is independent of $U _ { 1 }$ we can clarify the issues by considering a location in the wave where $\pmb { u } _ { 1 } = 0$ . Consider Ani. Thermal $/ \mathbf { e } ,$ showing a such a wave near a wall in boundary-layer approximation. (Note that we have made the wave-propagation direction x vertical in this animation, so everything fits on the display.) As we saw in Chapter 2, the temperature oscillates in phase with $\pmb { p _ { 1 } }$ far from the wall; close to the wall, the wall's heat capacity provides a thermal anchor that reduces the amplitude of the temperature oscillation and shifts its phase.

To consider dissipation of acoustic power in this region, imagine a piston moving with the gas, and compute the work done by that piston on the gas to the left of it. The work done by a piston is $\oint _ { } ^ { } p d V .$ In the animation, the small dot traces out the intersection of the pressure line and the voluine between the wall and the imaginary piston (whose average position is $4 \delta _ { \kappa }$ from the wall), so the area of the little ellipse drawn by the moving dot is proportional to $\oint _ { } ^ { } p d V .$ That slim elliptical area represents the work that the imaginary piston does on the gas between it and the wall. It's not zero, because of thermal relaxation of the gas to the wall. Gas immediately adjacent to the surface experiences isothermal density and pressure oscillations, which are perfectly springy; gas far from the surface experiences adiabatic density and pressure oscillations, which are also perfectly springy. In between, the gas approximately $\delta _ { \kappa }$ from the surface experiences a complex, hysteretic cycle of density changes in response to the pressure oscillations: first an increase in density due to quasiadiabatic compression by the sound wave, then a further increase in density as thermal relaxation to the surface removes heat from the gas, then a decrease in density due to quasi-adiabatic expansion by the sound wave, and finally a further decrease in density as thermal relaxation to the surface delivers heat to the gas. Since this gas experiences thermal expansion at low pressure and thermal contraction at high pressure, it absorbs work from the sound wave. This gas, approximately $\delta _ { \kappa }$ from the surface, is the most effective at absorbing work from the sound wave, whereas in the case of viscous dissipation the gas at the surface is most effective.

The lowest plot in Ani. Thermal /e shows the area of such a work ellipse as a function of the distance of the imaginary piston from the wall. This curve is steepest at $y / \delta _ { \kappa } \simeq 1$ which indicates that the gas approximately $\delta _ { \kappa }$ from the surface dissipates the most acoustic power.

Example: Standing-wave engine. In Chapter 2 we calculated that the thermalrelaxation resistance of one of the hot ducts in the standing-wave engine is $R _ { \kappa } = 2 3 5 0 ~ \mathrm { M P a } .$ $\mathsf { s } / \mathrm { m } ^ { 3 }$ . At a typical operating point of $| p _ { 1 } | = 3 0 0 \ \mathrm { k P a , }$ the thermal relaxation dissipation is $| \dot { p } _ { 1 } | ^ { 2 } / 2 R _ { \kappa } = 2 0$ W. Hence, if this loss could be eliminated in both hot ducts, the 1 kW of acoustic power delivered to the refrigerator could rise by 4%.

Example: Orifice pulse-tube refrigerator. The compliance at the top of the orifice pulse-tube refrigerator has only $| p _ { 1 } | = 9 0 \ \mathrm { k P a }$ . Hence, even though it has $0 . 3 ~ \mathrm { m } ^ { 2 }$ of surface area, the thermal-relaxation dissipation of acoustic power, obtained from the second term of Eq. (3.11), is only 5 W.

## 3.1.2. Acoustic power—general thermoacoustics, with $\mu = 0$

Equation (3.9), two sections above, was

$$
\frac { d \dot { \bar { E } } _ { 2 } } { d x } = - \frac { r _ { \nu } } { 2 } | \bar { U } _ { 1 } | ^ { 2 } - \frac { 1 } { 2 r _ { \kappa } } | p _ { 1 } | ^ { 2 } + \frac { 1 } { 2 } \operatorname { R e } \left[ e \widetilde { p _ { 1 } } \bar { U } _ { 1 } \right] .
$$

We have just examined the first two terms, which always consume acoustic power, exist independent of any temperature gradient along ${ \pmb x } ,$ and represent viscous and thermalrelaxation dissipation, respectively. Next we will examine the third term, which we will call the source/sink term because it can either produce or consume acoustic power and which exists only $\mathrm { i f } d T _ { m } / d x \neq 0$ . This term is difficult to fully understand, especially because $d \pmb { U _ { 1 s } }$ involves both $f _ { \kappa }$ and $f _ { \nu } .$ To build understanding, our qualitative discussion in this subsection will neglect viscosity in $d U _ { 1 s }$ setting $\pmb { f _ { \nu } } \doteq 0$ . In this limit, the third term of Eq. (3.9) can be written

$$
\begin{array} { l l l } { \displaystyle \frac { 1 } { 2 } \mathrm { R e } \left[ e \widetilde { p _ { 1 } } U _ { 1 } \right] } & { = } & { \displaystyle \frac { 1 } { 2 } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \mathrm { R e } \left[ \widetilde { p _ { 1 } } U _ { 1 } \right] \mathrm { R e } \left[ f _ { \mathrm { s } } \right] + \displaystyle \frac { 1 } { 2 } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \mathrm { I m } \left[ \widetilde { p _ { 1 } } U _ { 1 } \right] \mathrm { I m } \left[ - f _ { \mathrm { s } } \right] } \\ & { = } & { \displaystyle \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \dot { E } _ { 2 } \mathrm { R e } \left[ f _ { \mathrm { s } } \right] + \displaystyle \frac { 1 } { 2 } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \mathrm { I m } \left[ \widetilde { p _ { 1 } } U _ { 1 } \right] \mathrm { I m } \left[ - f _ { \mathrm { s } } \right] . } \end{array}\tag{3.12}
$$

(3.13)

Expressing it this way shows that $\mathbb { R e } \left[ f _ { \kappa } \right]$ is important for acoustic power in traveling-wave engines and refrigerators, in which Re $[ \widetilde { p _ { 1 } } U _ { 1 } ]$ is large, while Im $[ - f _ { \kappa } ]$ is important for acoustic power in standing-wave engines and refrigerators, in which Im $[ \widetilde { p _ { 1 } } U _ { 1 } ]$ is large.

## Traveling waves

Begin by considering the regenerator of a traveling-wave engine. To make the most of the first term on the right side of Eq. (3.12) or (3.13), we should make $\mathbb { R e } \left[ f _ { \kappa } \right]$ as large as possible; examination of Fig. 2.13 shows that this is accomplished at $R _ { h } \ll \delta _ { \kappa } ,$ where $\mathbb { R } { \mathsf { e } } \left[ f _ { \kappa } \right] \simeq 1$ Under these circumstances, thermal-relaxation resistance $\pmb { r _ { \kappa } }$ is negligible, as shown by Eq. (2.79). To generate (not dissipate) acoustic power requires that $d T _ { m } / d x$ and $\dot { E } _ { 2 }$ share the same sign; i.e. the temperature must increase through the regenerator in the direction of acoustic power flow. This situation is illustrated in Anis. Tashe /s and Tashe $/ { \tt r }$ Animation Tashe /s shows an overview of a traveling-wave engine, namely a traditional Stirling engine. The sign of the circulation of the pV ellipses indicates that acoustic power flows from left to right. The temperature rises in the direction of this acoustic power flow, so the first term in Eq. (3.12) or (3.13) shows that the acoustic power should increase fromi left to right; indeed, the right pV ellipse has greater area than the left $\pmb { p V }$ ellipse, showing this increase in acoustic power. If these two pistons were connected to a common crankshaft, that crankshaft would supply acoustic power to the gas at the left and remove it from the gas at the right. The extra acoustic power, represented by the difference between the right and left ellipse areas, is the net acoustic power generated by the engine, available to do external work such as generating electricity.

Animation Tashe $/ { \tt r }$ shows a close-up view inside the regenerator of Ani. Tashe $/ \mathbf { s } .$ One small piece of gas is highlighted, oscillating left and right while experiencing oscillating pressure. The phasing between pressure and motion is predominantly traveling wave: The gas moves to the right while the pressure is high, and moves to the left while the pressure is low, so the acoustic power flows from left to right. Temperatures are shown in the lower-left plot, where the temperature of the highlighted piece of gas, shown as the blue trace, is always locked to the local solid temperature, represented by the white line. This indicates that $R _ { h } \ll \delta _ { \kappa }$ ; equivalently, $f _ { \kappa } = 1$ . The volume of the highlighted piece of gas is shown on the horizontal axis of the lower-right plot, with the pressure plotted vertically. The gas expands while it moves to the right, because its temperature rises; it contracts while it moves to the left, because its temperature falls. This is the physical effect responsible for the volume source $e U _ { 1 }$ in a traveling-wave engine. The net effect—clockwise circulation on the ${ \mathfrak { p V } }$ diagram—is the production of acoustic power, because the expansion takes place while the gas is at high pressure and the contraction takes place while the gas is at low pressure. The difference between the right piston's work and the left piston's work in Ani. Tashe $/ \mathsf { s }$ is the total acoustic power produced by all the pieces of gas in the regenerator, each behaving as shown in Ani. Tashe $/ { \mathfrak { r } }$

Example: Traveling-wave engine. The traveling-wave engine of Figs. 1.13 and 1.14 follows the same thermodynamic cycle as discussed in the previous two paragraphs, but without pistons. The acoustic network that serves the function of the two pistons and their crankshaft is shown schematically in Ani. Tashe $/ \mathbf { u } .$ The acoustic power at several key locations is shown as purple ellipses. The size and signs of these $p V$ ellipses show how acoustic power is produced in the regenerator, with some of the produced power flowing out of the display to the right and the remainder fed back to the left end of the regenerator through the inertance. In this animation, we assume that. the regenerator is the only location where acoustic power is produced or dissipated. Hence, the areas of the lower two pV ellipses and the pV ellipse to the left of the regenerator are equal; the shape change at equal areas is due to $\boldsymbol { C }$ and $L .$ Similarly, the areas of the two pV ellipses at the ends of the thermal buffer column are equal, but with a shape change due to the intervening C. Continuity of ${ \pmb p } _ { 1 }$ and $\textstyle { \bar { U } } _ { 1 }$ at the three-way junction on the right ensures that the area of the ${ \mathfrak { p } } V$ ellipse representing power flowing out of the display to the right is the difference between the areas of the $p V$ ellipses at the right end of the thermal buffer column and the right end of the inertance.

For a typical operating point of the actual engine of Figs. 1.13 and 1.14, 1250 W of acoustic power flows into the ambient end of the regenerator and 3150 W of acoustic power flows out of the hot end of the regenerator. The $d T _ { m } / T _ { m }$ factor in Eq. (3.12) shows that, ideally, the ratio of these two powers, 2.5, could be the ratio of the engine's hot and ambient temperatures, $( 1 0 0 0 ~ \mathrm { K } ) / ( 3 0 0 ~ \mathrm { K } ) = 3 . 3$ . The other two terms in Eq. (3.9), especially the viscous term, account for this missing acoustic power in the regenerator. In addition, some 400 W of acoustic power is dissipated in viscous and thermal-relaxation effects in the inertance and compliance that form the acoustic network at the bottom of the display in Ani. Tashe; these losses are not shown in the ideal case shown in the animation.

The regenerator of a traveling-wave refrigerator is very similar to that of a traveling-wave engine; the primary difference is that $\scriptstyle { { \mathcal { T } } _ { m } }$ decreases in the direction of positive acoustic power in the refrigerator, so the third term in Eq: (3.9) is negative, so this term consumes ačoustic power. As with the engine, Re $[ f _ { \kappa } ]$ should be as large as possible, so we want $R _ { h } \ll \delta _ { \kappa } .$ This situation is illustrated in Anis. Ptr $/ { \mathsf s }$ and Ptr $/ { \tt r }$ Animation Ptr $/ { \mathsf s }$ shows an overview of a Stirling refrigerator. The sign of the circulation of the ${ \pmb { p V } }$ ellipses indicates that acoustic power flows from left to right. The temperature decreases in the direction of this power flow, so the first term in Eq. (3.12) shows that the acoustic power should decrease from left to right; indeed, the right $\pmb { p V }$ ellipse has smaller area than the left $\pmb { p V }$ ellipse, showing this decrease in acoustic power. If these two pistons were connected to a common crankshaft, that crankshaft would supply acoustic power to the gas at the left and remove it from the gas at the right. The difference between these two powers, represented by the difference between the left and right ellipse areas, is the net power required by the refrigerator; supplied by external means such as an electric motor.

Animation Ptr $/ { \tt r }$ shows a close-up view inside the regenerator of Ani. Ptr $/ \mathsf { s } .$ One-small piece of gas is highlighted, oscillating left and right while experiencing oscillating pressure. The phasing between pressure and motion is predominantly traveling wave: The gas moves to the right while the pressure is high, and moves to the left while the pressure is low, so the acoustic power flows from left to right. Temperatures are shown in the lower-left plot, where the temperature of the highlighted piece of gas, shown as the blue trace, is always locked to the local solid temperature, represented by the white line. This indicates that $R _ { h } \ll \delta _ { \kappa }$ ; equivalently, $f _ { \kappa } = 1$ . The volume of the highlighted piece of gas is shown on the horizontal axis of the lower-right plot, with the pressure plotted vertically. The gas expands while it moves to the left, because its temperature rises; it contracts while it moves to the right, because its temperature falls. The net effect—counterclockwise circulation on the ${ \pmb { p } } V$ diagram—is the consumption of acoustic power, because the expansion takes place while the gas is at low pressure and the contraction takes place while the gas is at high pressure. The difference between the right. piston's work and the left piston's work in Ani. Ptr $/ { \mathsf s }$ is the total acoustic power consumed by all the pieces of gas in the regenerator, each behaving as shown in Ani. Ptr $/ { \tt r }$

Example: Orifice pulse-tube refrigerator. The orifice pulse-tube refrigerator of Figs. 1.15 and 1.16 follows the same thermodynamic cycle as discussed in the previous two paragraphs, but without pistons. The acoustic network that allows the apparatus to follow this cycle is shown schematically in Ani. Ptr $/ { \mathfrak { p } } .$ The acoustic power at several key locations is indicated by purple ellipses. Thesize and signs of these ${ \pmb { p } } V$ ellipses show how acoustic power flows into the system from the left (supplied by external means, such as a motored piston or a thermoacoustic engine) and is absorbed in the regenerator and the LRC impedance network at the right end of the display. The areas of the two ${ \pmb { \mathscr { p V } } }$ ellipses at the ends of the thermal buffer column (a.k.a. pulse tube) are equal.

For a typical operating point of the actual refrigerator of Figs. 1.15 and 1.16, 8800 W of acoustic power flows into the ambient end of the regenerator and 3000 W of acoustic power flows out of the cold end of the regenerator. The $d T _ { m } / T _ { m }$ factor in Eq. (3.12) shows tha $^ { \mathbf { \scriptsize { t , } } }$ ideally, the ratio of these two powers, 2.9, could be the ratio of the engine's hot and ambient temperatures, (300 $\mathrm { K } ) / ( 1 2 0 \mathrm { K } ) = 2 . 5 .$ The other two terms in Eq. (3.9), especially the viscous term, account for the additional absorption of açoustic power in the regenerator.

## Standing waves

Next we will consider the stacks of standing-wave engines and refrigerators, continuing to imagine zero viscosity so that the source/sink term in $d \dot { E } _ { 2 } / d x$ is tractable. The first term in Eq. (3.12) or (3.13) is zero for standing-wave phasing. To make the most of the second term in Eq. (3.12) or (3.13), we should make Im $[ - f _ { \kappa } ]$ as large as possible; examination of Fig. 2.13 shows that this is accomplished at $R _ { h } \sim \delta _ { \kappa }$ , where Im $[ - f _ { \kappa } ] \simeq 0 . 4$ Equation (2.79) shows that $G _ { \kappa }$ cannot be neglected in this situation, so we should consider the source/sink term and the thermal-relaxation term in Eq. (3.9) together. Neglecting viscosity, we have from Eqs. (3.12), (3.9), and (2.79)

$$
\frac { d \dot { E } _ { 2 } } { d x } = \frac { 1 } { 2 } \left| p _ { 1 } \right| ^ { 2 } \frac { \left( \gamma - 1 \right) \omega A \mathrm { ~ I m } \left[ - f _ { \kappa } \right] } { \dot { \mathrm { ~  ~ \cdot ~ } } \mathrm { ~  ~ } \gamma p _ { m } } + \frac { 1 } { 2 } \mathrm { I m } \left[ p _ { 1 } \widetilde { U } _ { 1 } \right] \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \mathrm { I m } \left[ - f _ { \kappa } \right]\tag{3.14}
$$

Using Eqs. (2.45) and (2.32) to rearrange this expression, and assuming standing-wave phasing, leads to

$$
\frac { d \dot { E } _ { 2 } } { d x } = \frac { 1 } { 2 } | p _ { 1 } | ^ { 2 } \omega A \frac { \gamma - 1 } { \gamma p _ { m } } \operatorname { I m } \left[ - f _ { \kappa } \right] \left( \frac { d { T } _ { m } / d x } { \nabla { T } _ { \mathrm { c r i t } } ^ { \mathrm { } } } - 1 \right) ,\tag{3.15}
$$

where

$$
\nabla T _ { \mathrm { c r i t } } = \frac { \left| p _ { 1 } \right| / \rho _ { m } c _ { p } } { \left| U _ { 1 } \right| / A \omega }
$$

is the critical temperature gradient we first encountered in Chapter 2, Eq. (2.45).

The situation where $d T _ { m } / d x = \nabla T _ { \mathrm { c r i t } }$ , for which Eq. (3.15) shows that acoustic power is neither produced nor absorbed, is illustrated in Ani. Standing $/ \mathbf { c } .$ In the upper left of the display is a stack, with blue marker lines showing the moving gas. One particular piece of gas is highlighted in white in the stack. The yellow oval marks the region that is shown magnified at the left center of the display, which shows that same piece of moving gas and short fragments of the two stack plates adjacent. to it. The volume of that parcel of gas changes in response to pressure and temperature. At the bottom of the display are plots of pressure vs volume of the parcel of gas, and temperature vs position. In the temperature plot, the temperature of the parcel is the blue trace, and that of the nearby plate in the stack is the white line. In the previous, traveling-wave, animations, the blue trace and white line were superimposed because small $R _ { h }$ ensured good thermal contact between gas and solid. Here, $R _ { h } \sim \delta _ { \kappa } ,$ so the thermal contact is not so good; the alignment of the gas and solid temperatures is due only to the fact that we chose $d T _ { m } / d x = \nabla T _ { c r i t }$ for this animation. The parcel's temperature oscillation is due entirely to adiabatic pressure oscillation, and its temperature oscillation and motion just happen to match the local temperature gradient $d T _ { m } / d x$ exactly. Since the gas oscillations are merely adiabatic, the pV trace for this parcel is simply a reciprocating adiabat, so this parcel of gas neither produces nor absorbs acoustic power. This operating condition does not appear in useful thermoacoustic engines and refrigerators; $d T _ { m } / d x = \nabla T _ { c r i t }$ is only of academic interest, as it separates the regimes of standing-wave engine and standing-wave refrigerator.

Animation Standing /e shows an overview of a standing-wave engine. The display is basically the same as for Ani. Standing $/ \alpha$ discussed above, but now the temperature gradient is steeper, with $d T _ { m } / d x > \nabla T _ { c r i t } .$ , so that Eq. (3.15) indicates that acoustic power is produced. The steep temperature gradient means that the gas parcel's adiabatic temperature oscillation and motion do not match the local solid temperature gradient, so oscillatory heat transfer between the gas and the solid occurs, as indicated by the time-dependent red arrows in the magnified view of the stack. The phasing is such that thermal expansion occurs at high pressure and thermal contraction at low pressure, so the result is that the pV ellipse circulates clockwise, indicating that the parcel produces acoustic power. The acoustic power thus generated by all the parcels of gas in the stack is the power generated by the engine, available to do external work.

Similarly, Ani. Standing /r shows an overview of a standing-wave refrigerator. The display is basically the same as for Anis. Standing $/ \mathsf { c }$ and Standing $/ \tt e$ discussed above, but now the temperature gradient is less steep, with $d T _ { m } / d x < \nabla T _ { c r i t } ,$ so that Eq. (3.15) indicates that acoustic power is absorbed. The shallow temperature gradient means that the gas parcel's adiabatic temperature oscillation and motion do not match the local solid temperature gradient, so oscillatory heat transfer between the gas and the solid occurs, as indicated by the time-dependent red arrows in the'magnified view of the stack. The phasing is such that thermal expansion occurs at low pressure and thermal contraction at high pressure, so the result is that the pV ellipse circulates counterclockwise, indicating thàt the parcel produces acoustic power. The acoustic power thus absorbed by all the parcels of gas in the stack must be supplied by and external agent, such as a loudspeaker.

Example: Standing-wave engine. The standing-wave engine of Figs. 1.9 and 1.10 operates just as Ani. Standing /e discussed above, but at 350 Hz instead of the 0.1 Hz frequency of the animation. For a typical operating point, almost 700 W of acoustic power flow is produced in each stack. Under these conditions, the temperature gradient in the stack is x dependent, but it is approximately equal to $( T _ { H } - { \mathcal { T } } _ { 0 } ) / \Delta x = 6 0 ~ \mathrm { K / c m } .$ This is indeed larger than the critical temperature gradient, which we estimate to be 35 K/cm at the stack midpoint using Eq. (2.45).

## 3.2. Total power

Acoustic power is not the only power that is important in thermoacoustics; total power is perhaps of greater importance. Hence, we have to consider exactly what we mean by energy in thermoacoustics.

Engineers have long employed the concept of “control volume" for careful thought about energy balance issues in thermodynamic systems. A control volume is a space of-interest, surrounded by a well-defined imaginary boundary, to which we can apply the first law of

thermodynamics and similar principles.

(Apologies for the English language: We do not have shor $\mathbf { t } ,$ distinct terms for "rate at which work is done" or "rate at which heat is transferred." Most thermodynamics texts avoid this issue by sticking as much as possible with the variables having units of Joules, not Watts, but I prefer to focus attention on power. $\mathsf { S o , }$ in the interest of brevity and readability, some of my vocabulary will be a little awkward or ambiguous. When in doubt, look at the variables: Those with overdots, $\dot { W } , \dot { Q } , \dot { E } _ { 2 } , \dot { H } _ { 2 }$ , and Chapter 4's $\dot { X } _ { 2 }$ , are powers. However, for brevity I will refer to $\dot { \bar { W } }$ simply as work, and to $\dot { Q }$ simply as heat.)

![[mu_ad18d396_6aea6c63a94b427b0d15.jpg]]

![[mu_ad18d396_542e02edc05fb0a2d42d.jpg]]

![[mu_ad18d396_0bba46c217c0dec3edef.jpg]]  
Figure 3.3: A standing-wave refrigerator, insulated everywhere except at the heat exchangers. (a) A useful control volume for thermoacoustics, enclosing the left end. (b) Another useful control volume, enclosing part of the stack. (c) Graph of $\dot { E } _ { 2 }$ and $\dot { H } _ { 2 }$ in the refrigerator. The discontinuities in $\dot { H } _ { 2 }$ are the heats transferred at the heat exchangers.

Figure 3.3 introduces the topic of total power, showing two typical control volumes of interest in thermoacoustics. Consider the thermoacoustic refrigerator shown in Figs. 3.3a and 3.3b, driven by a piston or loudspeaker at the left and having thermal insulation around everything except the heat exchangers, so that heat can be exchanged with the outside world only at the two heat exchangers, and work can be exchanged with the outside world only at the piston. We can apply the principle of energy conservation to the control volume shown by the dotted line in Fig. 3.3a. In steady state, time-averaged over an integer number of acoustic cycles, the energy inside the control volume cannot change, so the rate at which energy flows into that control volume must equal the rate at which energy flows out. What flows in is clearly the time-averaged $p V$ piston work power (which is exactly equal to the acoustic power flowing from the face of the piston into the gas). That must equal the sum of the two outflowing powers, labeled heat power and total power. The heat is easy to think about—it's simply heat. It's always easiest to discuss such heat, flowing via conduction through a solid, so I like to imagine the control-volume boundary being within the metal case that separates the thermoacoustic gas from the outside world. The power flowing down the stack is much more subtle: It's not acoustic power, and it's not heat, and it's not work but we'd better understand $\mathbf { i t } ,$ because it's what counts in conservation of energy. Another typical important control volume is shown in Fig. 3.3b, intersecting a stack or regenerator in two places, with insulation around the side walls. Here the only powers flowing are the total powers in and out of the two end surfaces of the control volume. Applying the principle of energy conservation (again, steady state; time-averaged) to this control volume shows that total power in equals total power out. So total power can't depend on x within a stack or regenerator--it has to be constant, independent of ${ \pmb x } ,$ even while acoustic power depends strongly with ${ \pmb x } ,$ as we saw in the previous section.

![[mu_ad18d396_4bdd3e4b8beeccb1bdf5.jpg]]  
Figure 3.4: Merkli and Thomann's experiment, which detected cooling at the velocity antinode of a standing wave. Thermometers along the wall of the resonator detected temperature; these were used to infer local heat flux q to or from the wall. The negative values of q near the center of the resonance tube represent cooling.

![[mu_ad18d396_8e23d89b52be8c98e7f5.jpg]]  
Figure 3.5: An irregular parcel of gas passing through an imaginary rectangular opening fixed in space. As the parcel of gas passes through the imaginary opening, the energy that passes through that opening has several parts. The kinetic and internal energies are convected along with the gas. The pressure does work on the gas ahead as the parcel pushes other gas out of its way in order to pass through the opening. If a temperature gradient in the correct direction exists, heat is conducted through the opening. If the directions of the velocity and its gradients are suitable, viscous shear forces do work on the gas on the other side of the opening.

The 1975 experiment of Merkli and Thomann [40] also helps motivate this discussion of total power. As shown in Fig. 3.4, an acoustic resonator was driven at the half-wavelength resonance, using an oscillating piston and employing sensitive thermometers all along the resonator side wall. Merkli and Thomann were surprised to find that the central thermometers cooled, at the location of greatest dissipation of acoustic power per unit length, $\begin{array} { r } { \frac { 1 } { 2 } \left| U _ { 1 } \right| ^ { 2 } d R _ { \nu } / d x . } \end{array}$ That won't seem so surprising when we understand the important difference between total power and acoustic power.

So, what do we mean by total power? In moving gases (and liquids), the enthalpy is the correct energy to consider [26]. This is because the energy flux density in fluid mechanics is

$$
\mathbf { v } \left( \rho v ^ { 2 } / 2 + \rho h \right) - k \nabla T - \mathbf { v } \cdot \Sigma ,\tag{3.16}
$$

where h is the enthalpy per unit mass, $\rho \upsilon ^ { 2 } / 2$ is the kinetic-energy density, and Σ is the viscous shear tensor. The enthalpy itself is the sum of other energies:

$$
h = \epsilon + p / \rho ,\tag{3.17}
$$

where € is internal energy per unit mass, so the energy flux density can be thought of as the superposition of three flux densities: kinetic energy, internal energy, and ${ } ^ { \mathfrak { s } } p / \rho . { } ^ { \mathfrak { s } }$ Looking at Fig. 3.5, you can imagine the first two of these as being attached to the gas and hence being convected along with the gas at velocity v, and you can imagine the pressure term to represent the rate at which the pressure of the gas “does work" on the gas it is pushing ahead of it. You can imagine the thermal conduction term as giving the rate at which heat is conducted across the cross section, and you might vaguely imagine the final term as representing work that viscous shear does across the cross section. Any thermodynamic/fluid mechanics text should explain this more carefully.

To simplify this to a usable form, we take the x component of Eq. (3.16), substitute our usual acoustic approximations, Eqs. (2.46)-(2.53), for all variables, keep terms through second order, take the time average, and integrate over the cross-sectional area of the channel. The viscous-shear term is generally much smaller than the other surviving terms. We will call the result $\dot { H } _ { 2 } .$ , the acoustic approximation to the total power flowing in the positive x direction in the channel"total power" for short. This result is

$$
\dot { H } _ { 2 } ( x ) = \frac { 1 } { 2 } \rho _ { m } \int \operatorname { R e } \left[ h _ { 1 } \widetilde { u _ { 1 } } \right] d A - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \frac { d { \var} T _ { m } } { d x } .\tag{3.18}
$$

This acoustic approximation to the total power flowing in the x direction will suffice until we encounter streaming in Chapter 5.

The final term is simple conduction of heat, in which we've included conduction both in the gas and in whatever solid (e.g. stack or regenerator) is present. The first term is more interesting. Professor Thomann (of Merkli and Thomann) said that the energy equation is like a kaleidoscope: Every time you shake $\mathbf { i t } ,$ it looks completely different. There are many good ways to look at $\dot { H } _ { 2 }$ •

First, if we know $\dot { H } _ { 2 }$ and work, we can deduce the heat transferred at heat exchangers in thermoacoustic engines and refrigerators, as illustrated in Fig. 3.3a. Alternatively, if we know both work and heat, we can deduce $\dot { H } _ { 2 }$

Second, if we think of enthalpy as a function of temperature and pressure,

$$
\begin{array} { l l l } { { d h } } & { { = } } & { { \rho _ { m } c _ { p } d T + \left( 1 - T \beta \right) d p } } \\ { { } } & { { = } } & { { \rho _ { m } c _ { p } d T } } \end{array}\tag{3.19}
$$

(3.20)

and use the second version, which is true for an ideal gas, we find that Eq. (3.18) becomes

$$
\dot { H } _ { 2 } ( x ) = \frac { 1 } { 2 } \rho _ { m } c _ { p } \int \operatorname { R e } \left[ T _ { 1 } \widetilde { u _ { 1 } } \right] d A - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \frac { d T _ { m } } { d x } .\tag{3.21}
$$

This point of view is useful for calculations of $\dot { H } _ { 2 } ,$ and is especially useful for thinking about nearly ideal regenerators, in which $\mathcal { T } _ { 1 } \simeq 0$ . For example, consider the control volume shown by the dotted yellow box in the Stirling refrigerator shown in Ani. Ptr $/ \mathbf { c } .$ For an ideal regenerator, the heat capacity of the regenerator solid and the good thermal contact in the small pores there maintain temporally isothermal conditions at every location, so $\mathcal { T } _ { 1 } = 0$ If we can neglect the conduction of heat through the regenerator, $\mathtt { E q } .$ (3.21) shows that $\dot { H } _ { 2 } ^ { \enspace \enspace ^ { \enspace \enspace } } = 0$ . Hence, the time-averaged cooling power of the refrigerator must equal the timeaveraged mechanical power extracted by the cold piston. That is, in suitable units, the area of the $\pmb { p V }$ ellipse for the cold piston must equal the time-averagéd width of the red heat arrow at the cold heat exchanger.

Using Eqs. (2.68) and (2.55) for $\mathcal { T } _ { 1 }$ and ${ \pmb u } _ { 1 }$ , we can perform the integration in Eq. (3.21) to obtain

$$
\begin{array} { r c l } { \dot { H } _ { 2 } } & { = } & { \displaystyle \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \widetilde { U } _ { 1 } \left( 1 - \frac { \left( f _ { \kappa } - \widetilde { f } _ { \nu } \right) } { \left( 1 + \sigma \right) \left( 1 - \widetilde { f } _ { \nu } \right) } \right) \right] } \\ & & { \displaystyle + \frac { \rho _ { m } c _ { p } | U _ { 1 } | ^ { 2 } } { 2 A \omega \left( 1 - \sigma ^ { 2 } \right) \left| 1 - f _ { \nu } \right| ^ { 2 } } \mathrm { I m } \left( f _ { \kappa } + \sigma \widetilde { f } _ { \nu } \right) \displaystyle \frac { d T _ { m } } { d x } - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \displaystyle \frac { d T _ { m } } { d x } , } \end{array}\tag{3.22}
$$

first obtained by Rott [41].

![[mu_ad18d396_6dc8289e9ace990e0e53.jpg]]  
Figure 3.6: The fact that $\dot { H } _ { 2 }$ is independent of x within an insulated stack or regenerator determines the temperature distribution $T _ { m } ( x )$ within the stack or regenerator.

If $d T _ { m } / d x = 0 .$ , such as in a water-jacketed resonator component, Eq. (3.22) gives $\dot { H } _ { 2 } ( x )$ in that case, $d \dot { H } _ { 2 } / d x$ tells how much energy per unit length is deposited in (or removed from) the water jacket.

Third, if we think of enthalpy as a function of entropy and pressure,

$$
d h = T d s + d p / \rho ,\tag{3.23}
$$

we find that the total power can be written

$$
\begin{array} { r c l } { { \dot { \cal H } _ { 2 } } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \widetilde { U } _ { 1 } \right] + \frac { 1 } { 2 } \rho _ { m } T _ { m } \int \mathrm { R e } \left[ s _ { 1 } \widetilde { u } _ { 1 } \right] d A - \left( A k + A _ { \mathrm { 6 o l i d } } k _ { \mathrm { s o l i d } } \right) \displaystyle \frac { d { \cal T } _ { m } } { d x } } } \\ { { } } & { { } } & { { \displaystyle = \dot { \cal E } _ { 2 } + \frac { 1 } { 2 } \rho _ { m } { \cal T } _ { m } \int \mathrm { R e } \left[ s _ { 1 } \widetilde { u } _ { 1 } \right] d A - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \displaystyle \frac { d { \cal T } _ { m } } { d x } . } } \end{array}\tag{3.24}
$$

(3.25)

The first term is clearly nothing but acoustic power. The second term is $T _ { m }$ times the second-order hydrodynamic entropy flux, and the final term is simply conduction of heat. Many of us have found it helpful to our intuition to identify the sum of the last two terms

$$
\dot { H } _ { 2 } - \dot { E } _ { 2 } = \frac { 1 } { 2 } \rho _ { m } T _ { m } \int \operatorname { R e } \left[ s _ { 1 } \widetilde { u } _ { 1 } \right] d A - ( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } ) \frac { d { T } _ { m } } { d x } .\tag{3.26}
$$

as a sort of thermoacoustic heat-pumping power, with the ${ \pmb s } _ { 1 } { \pmb u } _ { 1 }$ term generally by far the largest contributor. Many of us who have worked in standing-wave thermoacoustics for a decade loosely refer to this as "thermoacoustic heat flux," and we have been criticized for this practice by careful people who know thermodynamics. Such careful people correctly point out that multiplying a hydrodynamic entropy fux by $\boldsymbol { \mathsf { T } }$ does not make a heat flux. The usual description of "bucket-brigade" standing-wave thermoacoustic "heat transport" as shown in Ani. Standing indeed shows heat flowing from plate to gas at one part of the cycle and heat flowing from gas to a different part of the plate 180° later in time, but careful people correctly point out that it is not accurate to say that the gas carries heat from the first location to the second, because there is more to gas thermodynamics than simply heat capacity. I no longer use such careless vocabulary when talking with experts, both to avoid controversy and to avoid a false sense of simple understanding. On the other hand, I continue to use this careless vocabulary often [25], mostly because it allows thermoacoustics novices to understand the phenomena without bogging them down in details.

In wide-open isothermal channels, like most resonator components, most of the gas should experience adiabatic oscillations and ${ \pmb s } _ { 1 }$ should be near zero over most of the area $A .$ Hence, Eq. (3.24) suggests that in this situation the total power and the acoustic power are nearly equal. This contributes to our ability to deduce a heat-exchanger's heat, from knowledge of the adjacent stack's total power and adjacent duct's acoustic power.

## 3.2.1. Traveling waves

Like a kaleidoscope: Shake the energy equation a little, and you see a new picture. If the total power through a good regenerator is approximately zero, then $\scriptstyle { \frac { 1 } { 2 } } \rho _ { m } T _ { m } \int$ Re $[ s _ { 1 } \widetilde { u _ { 1 } } ]$ dA must be approximately equal and opposite to the acoustic power $\scriptstyle { \frac { 1 } { 2 } } \mathrm { R e } [ p _ { 1 } \widetilde { U _ { 1 } } ]$ at each location x. This is another way of imagining the "cause" of the Stirling refrigerator's cooling power as due to the large acoustic power flowing through the regenerator plus the fact that the total power flowing through the regenerator is nearly zero. In Ani. Ptr $/ \mathbf { r } ,$ which shows a close-up view inside the regenerator of an orifice pulse-tube refrigerator, the red arrows show heat flow into and out of the parcel of gas; these heat flows cause the oscillating entropy ${ \pmb s } _ { \bf 1 }$ and its phasing relative to $\pmb { u } _ { 1 }$ , and hence cause Re $[ s _ { 1 } \widetilde { u _ { 1 } } ]$ to be nonzero.

In a pulse tube or thermal buffer column, ${ \pmb s } _ { \mathbf { 1 } }$ is due almost entirely to $\left( u _ { 1 } / i \omega \right) d s _ { m } / d x$ so Re $\{ s _ { 1 } \widetilde { u _ { 1 } } \} \simeq 0$ . Hence $\dot { H } _ { 2 } \simeq \dot { E } _ { 2 }$ in a pulse tube or thermal buffer column.

In the regenerators of traveling-wave systems, $T _ { 1 } \simeq 0 .$ , and hence $\dot { H } _ { 2 } \simeq 0$ . Hence, if a heat exchanger is sandwiched between a regenerator and a pulse tube or thermal buffer column, or between a regenerator and a resonator component, the heat-exchanger heat and the acoustic power flowing through it must be nearly equal. (In contrast, standing-wave systems have no such constraint on $\dot { H } _ { 2 }$ and so the heat-exchanger heat can be significantly larger than the acoustic power.)

## 3.2.2. Standing waves

For standing-wave phasing, the inviscid limit of Eq. (3.22),

$$
\dot { H } _ { 2 } \simeq \frac { 1 } { 2 } \left| \mathfrak { p } _ { 1 } \right| \left| \mathcal { U } _ { 1 } \right| \mathrm { I m } \left[ - f _ { \kappa } \right] \left( \frac { d T _ { m } / d x } { \nabla T _ { \mathrm { c r i t } } } - 1 \right) - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \frac { d T _ { m } } { d x } ,\tag{3.27}
$$

is simple and interesting, especially when considered in concert. with the standing-wave version of Eq. (3.24):

$$
\dot { H } _ { 2 } = \frac { 1 } { 2 } \rho _ { m } T _ { m } \int \operatorname { R e } \left[ s _ { 1 } \widetilde { u _ { 1 } } \right] d A - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) \frac { d { T } _ { m } } { d x }\tag{3.28}
$$

The first term of Eq. (3.27) resembles Eq. (3.15) for $d \dot { E } _ { 2 } / d x$ derived above: It has the same dependence on $f _ { \kappa }$ and on $d T _ { m } / d x$ . Hence, aside from the less interesting thermal-conduction term, the total power and the rate of change of acoustic power have the same dependences on channel geometry in standing waves; and both are zero when $d T _ { m } / d x = \nabla T _ { \mathrm { c r i t } } ,$ positive when $d T _ { m } / d x > \nabla T _ { \mathrm { c r i t } }$ , and negative when $d T _ { m } / d x < \nabla T _ { \mathrm { c r i t } }$

Furthermore, this term must be identified with the hydrodynamic entropy transport represented by the $\mathbb { R e } \left[ s _ { 1 } \widetilde { u _ { 1 } } \right]$ term in Eq. (3.28). Animation Standing $/ { \tt r }$ illustrates this $\mathbb { R e } \{ s _ { 1 } \widetilde { u _ { 1 } } \}$ contribution to the total power in a standing-wave refrigerator. The parcel of gas absorbs a little heat from the solid walls at the right extreme of its motion, as shown by the red arrows, carries entropy to the left, and gives heat to the solid walls at the left extreme of its motion, and returns to the right with less entropy. In this case, $\dot { H } _ { 2 }$ is negative. In moving left, the gas has moved up the temperature gradient, so it deposits its heat to the walls at a location of higher temperature than that at which it absorbed heat from the walls. Loosely speaking, the gas moves heat from right to left, up the temperature gradient. So this is a refrigerator, moving heat from right to left, up the temperature gradient. Overall every parcel of gas in the entire stack, each cycle of the wave, picks up a little heat from solid, moyes it a little to the left and deposits it again at a slightly higher temperature. The parcels in mid stack are like the middle members of a bucket brigade, passing heat along. At either end are parcels that oscillate between the stack and one of the heat exchangers. At the right end, such parcels absorb heat from the cold heat exchanger and deposit heat in the stack; at the left end, such parcels absorb heat from the stack and deposit heat in the ambient heat exchanger. So the net effect is to absorb heat from the cold heat exchanger, and reject waste heat at the ambient heat exchanger.

The process illustrated in Ani. Standing $/ { \mathfrak { r } }$ occurs in standing-wave refrigerators, for which $d T _ { m } / d x < \nabla T _ { c r i t }$ . If the temperature gradient in the stack is steeper, the signs of all the heat transfers change, as shown for the standing-wave engine of Ani. Standing $/ \mathbf { e } .$ In this case, even though the gas is heated adiabatically as it moves ${ \mathrm { l e f t } } ,$ it's not hot enough at the left extreme of its motion to match the local solid temperature when it gets there. So at the left extreme of its motion, at high pressure, it's still cooler than the solid, so heat flows into it, which increases its entropy. Similarly, at the right extreme of its motion, heat flows out of the gas into the solid, decreasing the entropy of the gas. The gas effectively shuttles heat from hot to cold, left to right, down the temperature gradient; $\dot { H } _ { 2 }$ is positive.

## 3.3. A point of view for computations

In Chapter 2, we developed the momentum equation to relate $U _ { 1 }$ and $d p _ { 1 } / d x ,$ as in $\mathtt { E q . }$ (2.56) or (2.73). The momentum equation can be interpreted in two ways, either as an expression of how flow causes a pressure gradient or as an expression of how a pressure gradient causes flow, and both points of view are useful. In steady-flow hydrodynamics, it is usually obvious which point of view is preferable in a given circumstancethe flow of water down a dam's spillway is caused by the gravitational pressure gradient, while the pressure gradients in the oil pumped through the passages of an automobile engine are caused by the volumetric velocity coming from the positive-displacement oil pump. In acoustics, the "correct" point of view is more subtle, as the momentum equation relates $U _ { 1 }$ and $d p _ { 1 } / d x$ while simultaneously the continuity equation relates ${ \mathfrak { p } } _ { 1 }$ and $\dot { d U _ { 1 } } / d x$

Similarly, two interpretations of the thermoacoustic total-power equation are possible and useful, whether Eq. (3.18), (3.21), (3.22), or (3.24). In one interpretation, the temperature gradient $d T _ { m } / d x$ (and all the other relevant variables, such as channel geometry, ${ \pmb p _ { 1 } } ,$ and $U _ { 1 } )$ cause total power $\dot { H } _ { 2 }$ to flow through a stack or regenerator. In another interpretation, $\dot { H } _ { 2 }$ (and all the other variables) cause the temperature gradient in the stack or regenerator. Both points of view are useful. For example, if you put a fixed heater power into the hot heat exchanger of the standing-wave engine of Fig. 1.10, that power has nowhere else to go but through the stack, so it determines the temperature gradient in the stack, in concert with many other variables such as those of the acoustic wave. On the other hand, if you power that heater using a thermostat set at a fixed $\scriptstyle { \mathcal { T } } _ { H }$ , the temperature difference across the stack determines the power flowing through the stack and hence determines the heater power that must be supplied.

The first interpretation of the total-power equation is particularly important because it shows that the total-power equation can be regarded as a first-order differential equation for $T _ { m } ( x )$ in a stack or regenerator, if ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ and the geometry are known. This is evident in the control-volume picture of Fig. 3.3b, which shows that the total power $\dot { H } _ { 2 }$ must be a constant, independent of ${ \pmb x } ,$ throughout the stack or regenerator whenever the side walls of the stack or regenerator are insulated. The other variables in Eq. (3.22) are presumably known from the considerations of Chapter 2. Although the temperatures at the ends of a stack or regenerator are often known, there is no better way than Eq. (3.22) to calculate the distribution of temperature at intermediate x.

Our numerical integrations in DeltaE rely on the first interpretation of the total-power, momentum, and continuity equations. DeltaE performs simultaneous integrations along x of the momentum, continuity, and total-power equations, in the form

$$
\begin{array} { l l l } { { d p _ { 1 } } } & { { = } } & { { { \cal F } _ { \mathrm { m o m } } ( T _ { m } , U _ { 1 } ; \omega , \mathrm { g a s ~ p r o p e r t i e s , ~ g e o m e t r y } ) d x } } \end{array}\tag{3.29}
$$

$$
\begin{array} { c c l } { { d U _ { 1 } } } & { { = } } & { { F _ { \mathrm { c o n t } } ( T _ { m } , p _ { 1 } , U _ { 1 } ; \omega , \mathrm { g a s ~ p r o p e r t i e s , g e o m e t r y } ) d x } } \end{array}\tag{3.30}
$$

$$
\begin{array} { r } { d T _ { m } ~ = ~ F _ { \mathrm { p o w } } ( T _ { m } , p _ { 1 } , U _ { 1 } ; \dot { H } _ { 2 } , \omega , \mathrm { g a s ~ p r o p e r t i e s , ~ g e o m e t r y } ) d x . } \end{array}\tag{3.31}
$$

to find $p _ { 1 } ( x ) , U _ { 1 } ( x )$ , and $\mathcal { T } _ { m } ( x )$ . These complicated functions $F _ { z a o m } , \ F _ { c o a t }$ , and $F _ { p o w }$ are appropriate functional forms of the momentum, continuity, and total-power equations. In Eq. (3.31), $\dot { H } _ { 2 }$ is taken to be independent of x within each stack or regenerator; its value may assigned based on nearby heat-exchanger heats, or may be found self-consistently. Once $p _ { 1 } ( x ) , U _ { 1 } ( x )$ , and $\mathcal { T } _ { m } ( x )$ are found, other results such as $\dot { E } _ { 2 } ( x )$ are straightforward.

## 3.4. Examples

Example: Standing-wave engine. While producing the curves of ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ shown in Fig. 2.16 for the standing-wave engine, DeltaE also computed $T _ { m } ( x )$ and the powers. The results are shown in Fig. 3.7. Within the stack, total power $\dot { H } _ { 2 }$ is constant at 2380 W, because of the sidewall insulation and the first law of thermodynamics. Its magnitude is the same as the heater power supplied at the hot heat exchanger. DeltaE used this value of $\dot { H } _ { 2 }$ and the total-power equation to determine $T _ { m } ( x )$ in the stack; it deviates noticeably from a straight line.

The calculated values of acoustic power $\dot { E } _ { 2 } ( x )$ follow directly from the values of $p _ { 1 } ( x )$ and $\pmb { U } _ { 1 } ( \pmb { x } )$ plotted in Fig. 2.16. Note that $\mathtt { R e } [ p _ { 1 } ]$ Im $[ U _ { 1 } ]$ contributes nothing to $\dot { E } _ { 2 } ;$ nonzero acoustic power arises from $\scriptstyle \mathrm { { R e } } [ p _ { 1 } ]$ times the small $\mathtt { R e } [ U _ { 1 } ]$ and from $\mathtt { R e } [ U _ { 1 } ]$ times the small

![[mu_ad18d396_ef902333afc5995472b0.jpg]]  
Figure 3.7: Acoustic power $\dot { E } _ { 2 } ,$ total power $\dot { H } _ { 2 } ,$ and mean temperature $T _ { m }$ as functions of position x for the standing-wave engine, under the same conditions as Fig. 2.16.

Im[pi]. A total of 670 W of acoustic power is generated throughout the stack, but especially near the hot end, and 500 W of acoustic power is assumed to flow from right to left at the right end of the figure, from the other 'acoustic engine shown in Fig. 1.10. This total of 1170 W of acoustic power is consumed elsewhere, most dramatically at the side branch to the refrigerators, where 1000 W is delivered. Acoustic power dissipation elsewhere is more subtle, as evidenced by the small negative slope of $\bar { E } _ { 2 } ^ { - } ( x )$ throughout the resonator; this negative slope is somewhat larger in the two heat exchangers. The small negative slope of $\dot { E } _ { 2 } ( x )$ in the hot duct, to the left of the stack and hot heat exchanger, which is almost invisible in the figure except as a slight change in line width between ${ \pmb x } = { \pmb 0 }$ and ${ \pmb x } = { \pmb 0 } . { \pmb 0 } { \ - }$ m. shows the dissipation of 20 W estimated at the end of Section 3.1.1 above.

Example: Orifice pulse-tube refrigerator. A similar plot of results of DeltaE's numerical integration is shown in Fig. 3.8 for the orifice pulse-tube refrigerator, under conditions similar to those shown in the phasor diagram of Fig. 2.19.

![[mu_ad18d396_2539dbbe971d4fbf8314.jpg]]  
Figure 3.8: Temperature $\mathbf { \delta } _ { T _ { m } , \mathrm { ~ ering } }$ total power $\dot { H } _ { 2 } .$ , and acoustic power $\dot { E } _ { 2 }$ throughout the orifice pulse-tube refrigerator of Fig. 1.16. Horizontal dimensions in the sketch above are aligned with corresponding locations in the graphs.

In the regenerator and the pulse tube, $\pmb { T _ { m } } ( x )$ is obtained by integration of the total-power equation, for a total power $\dot { H } _ { 2 } = 0 . 4 8$ kW in the regenerator and of 2.92 kW in the pulse tube. In the regenerator, this results in only slight deviation of $\pmb { T } _ { m } ( \pmb { x } )$ from a straight line.

The value of 0.48 kW is obtained self-consistently by the calculation, in order to allow the regenerator to reach from its ambient temperature of 292 K to its cold temperature of 128 K. Both terms in Eq. (3.21) contribute to $\bar { \dot { H } } _ { 2 }$ in the regenerator; the sum is small compared with other powers in the problem. The pulse tube radius is much greater than $\delta _ { \kappa , \gamma }$ so we expect $\dot { H } _ { 2 } \simeq \dot { E } _ { 2 }$ as shown in the figure. The small difference between these two is due primarily to $A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } d T _ { m } / d x$ in Eq. (3.24). The large changes in $\dot { H } _ { 2 }$ at each of the three heat exchangers represent the heats exchanged at these heat exchangers. The cooling power at 128 K is $2 . 9 2 - 0 . 4 8 = 2 . 4 4$ kW.

About $2 / 3$ of the 8.77 kW of acoustic power is consumed in the regenerator, and about $1 / 3$ is consumed in the flow resistance of the LRC network at the end of the refrigerator. These powers are calculated from the calculated values of $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ throughout, and are consistent with the phasors in Fig. 2.19 showing ${ \pmb p _ { 1 } }$ and $U _ { 1 }$ at a few locations. Small amounts of acoustic power are also consumed in the two largest heat exchangers, and a negligible amount of acoustic power is consumed in the pulse tube and in the large duct to the left of all the heat-exchange components.

## 3.5. Exercises

3.1 In the spirit of Fig. 1.19, draw phasor diagrams for several locations of the wave shown in Ani. Wave $/ \mathbf { k } .$ Discuss how your diagrams are consistent with positive acoustic power flow in the positive x direction, and with $d \dot { E } _ { 2 } / d x = 0$

3.2 In a double Helmholtz resonator, how much kinetic energy is in the gas in the neck when it is moving with velocity $| u _ { 1 } | ?$ Express your answer in terms of L and $U _ { 1 }$ . A quarter cycle later, all that kinetic energy is converted to potential energy stored in the compliances. Express that energy in terms of ${ \pmb p } _ { 1 }$ and C.

Using Eq. (3.11), write down expressions for the time-averaged viscous absorption of acoustic power in the neck, and the time-averaged thermal-relaxation absorption of acoustic power the bulbs. Which is typically bigger?

The quality factor of a resonance is given by Q = 2π(Stored energy)/(Energy dissipated per cycle). Write down an expression for the $Q$ of this double Helmholtz resonator.

Acoustics expertș only: In a simple acoustics textbook, look up the radiation impedance from a circular orifice whose diameter is much smaller than λ. There is an imaginary part, which adds to the inertance of the neck, and a real part, which adds to the dissipation. Estimate how much this “end effect" shifts the resonance frequency of the Helmholtz resonator How much does it change the Q?

3.3 If your favorite piece of thermoacoustics hardware has a stack or regenerator, estimate the heat deposited and removed from the solid during each half cycle of the oscillation. If you don't have a favorite, estimate the heat deposited and removed during each half cycle of an audio-amplitude sound wave in air per square meter of a solid boundary.

3.4 Estimate the critical temperature gradient in the stack or regenerator of your favorite piece of hardware. If you don't have a favorite, estimate the critical temperature gradient halfway between the pressure node and adjacent velocity node in a 240 Hz standing wave in air at atmospheric pressure. How much of the information given in the preceding sentence was unnecessary to find the answer?

3.5 If your favorite acoustic hardware has a power transducer such as a loudspeaker, estimate the acoustic power it transduces, using its $\left| x _ { 1 } \right|$ , area, frequency, etc.

3.6 Draw a few control volumes for your favorite thermoacoustics hardware. Discuss thermal insulation, and where energy can: cross the boundaries of the control volumes..

3.7 Estimate $\dot { H } _ { 2 }$ for the stack or regenerator in your favorite piece of thermoacoustics hardware. Black-body radiation is another contributor to total power, which was not included in our discussion. Estimate it for the same component.

3.8 Sketch $\dot { H } _ { 2 }$ and $\dot { E } _ { 2 }$ vs x for your favorite thermoacoustics hardware. Don't worry about the actual magnitudes of things; just try to get the overall qualitative picture right: the signs of the powers, the signs and locations of discontinuities, the signs of slopes. Also sketch $\left| p _ { 1 } \right|$ and $| \bar { U } _ { 1 } |$

3.9 Look closely at Ani. Thermal $/ \mathsf { e } .$ It looks like the power curve shows negative slope at about $y / \delta _ { \kappa } = 4$ . This suggests that thermal relaxation in gas at that distance from a solid wall does not dissipate acoustic power—it generates acoustic power!—because the imaginary piston at a distance $5 \delta _ { \kappa }$ from the wall has to supply less power to the gas between it and the wall than does the imaginary piston at a distance $4 \delta _ { \kappa }$ from the wall. Was the author was sloppy in programming the animation, or does the math confirm this surprising observation? Does something similar occur in boundary-layer viscous dissipation as illustrated in Ani. Viscous?

3.10 Can nonzero acoustic power pass a true pressure node in a standing wave? Can it pass a velocity node? Can nonzero total energy pass either a pressure node or a velocity node?

3.11 Consider a large-diameter channel with a nonzero temperature gradient, such as the thermal isolation tube or pulse tube of Figs. 1.14 or 1.16. Show that $\dot { H } _ { 2 } \simeq \dot { E } _ { 2 }$ if you can neglect boundary-layer effects at the walls and ordinary thermal conduction along $\pmb { x }$ (and if streaming, to be discussed in Chapter $\mathbf { 6 , }$ is negligible). Discuss this result from several points of view: Eq. (3.21), Eq. (3.24), and a Lagrangian picture of moving parcels of gas. With respect to Eq. (3.24), be sure to notice that ${ \mathfrak { s } } _ { 1 } \neq 0 .$

3.12 Consider a channel large enough that the boundary-layer approximation is valid. The channel has a spatially uniform $\scriptstyle { { \mathcal { T } } _ { m } }$ , maintained by water flowing in a jacket around the channel. Suppose $\pmb { p _ { 1 } }$ and $\pmb { U _ { 1 } }$ are known. Use Eq. (3.22) for $\dot { H } _ { 2 }$ and the principle of energy conservation to derive an expression for the heat dQ delivered to (or removed from?) the water in a length dx of the channel. In your answer, use results from Chapter 2 to express $d p _ { 1 } / d x$ in terms of $\scriptstyle { \bar { U } } _ { 1 }$ and to express $d U _ { 1 } / d x$ in terms of ${ \pmb p } _ { 1 }$ . Interpret the Merkli-Thomann experiment, Fig. 3.4, from this perspective—are their experimental results consistent with your answer?

3.13 Show that $\dot { H } _ { 2 } = \dot { E } _ { 2 }$ when $d T _ { m } / d x = 0 , \mu = 0$ , and $\pmb { k } = \pmb { 0 }$ , independent of the size of the channel.

3.14 Simplify Eq. (3.22) using boundary-layer expressions for $f _ { \kappa }$ and $f _ { \nu }$ and assuming standing-wave phasing.

3.15 Evaluate f Re $[ s _ { 1 } \widetilde { u _ { 1 } } ]$ dA in boundary-layer approximation. Make a graph, with the vertical axis $A \left| p _ { 1 } \right| / \rho _ { m } a \left| U _ { 1 } \right|$ running from 0 to 10, and the horizontal axis $( d T _ { m } / d x ) / \nabla T _ { c r i t }$ running from 0 to 4. On the graph, for ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ in phase, draw a line indicating where $\textstyle \int \operatorname { R e } \left[ s _ { 1 } \widetilde { u _ { 1 } } \right] d A = 0$ . Show which side of this line has $\textstyle \int \mathbb { R e } \left[ s _ { 1 } \widetilde { u _ { 1 } } \right] d A > 0$ and which side has $\int \mathbb { R } \mathrm { e } \left[ s _ { 1 } \widetilde { u _ { 1 } } \right] d A < 0$ . Repeat for phase differences between ${ \pmb p } _ { 1 }$ and $U _ { 1 }$ of $4 5 ^ { \circ } , 9 0 ^ { \circ } , 1 3 5 ^ { \circ }$ Interpret some of these graphs in terms of Ani. standing

## 4. EFFICIENCY

Both the raw efficiency and the "fraction of Carnot" serves as a useful measure of efficiency for the simplest'thermodynamic systems, such as the simple heat engine or the simple refrigerator [2] shown in Fig. 1.1 at the beginning of the book and reproduced here in Fig. 4.la. The raw efficiency is what you want divided by what you must spend, and in Chapter 1 we reviewed the well known bounds on raw efficiency given by Carnot's ratio of temperatures, which we quickly derived from the first and second laws of thermodynamics. So it is natural to also cite the fraction of Carnot, which is the ratio of the actual raw efficiency to the maximum raw efficiency allowed by the laws of thermodynamics. The physicists' ideal is 100%, but reality reduces this significantly. Typically, thermoacoustic engines and refrigerators that were designed for high efficiency have operated at or above 20% of Carnot; we expect to increase this to 40% of Carnot in the future.

Fraction of Carnot is fine for such simple systems. However, more complex systems need a more sophisticated measure of merit. For instance, consider the machine shown in Fig. 4.1b, which takes air at atmospheric temperature and pressure, and separates and cools it to produce liquid oxygen, liquid nitrogen, liquid argon, solid carbon dioxide, and liquid water. The machine is driven with some work power, and it dumps waste heat power to ambient temperature. How should we measure the efficiency of a complicated system like this? What we want to do and what we must spend in order to do it don't even have the same units. How can we understand what limit on the performance of such a system is imposed by the two laws of thermodynamics? This chapter introduces some advanced concepts in thermodynamics that can be used to answer these questions.

## 4.1. Lost work and entropy generation

In one common and powerful method of accounting for efficiency in complex thermodynamic systems [28, 42], all losses are measured in terms of equivalent lost work, and one température $\pmb { \mathcal { T } _ { 0 } }$ is identified as a special temperature, the environment temperature at which arbitrary amounts of heat of no value can be freely exchanged. (If two different environmental temperatures existed, with which heat of no value could be freely exchanged, then it would be possible to run a heat engine between them, producing unlimited work—of great value—from heat of no value. Hence, identification of a single "ambient" temperature $\scriptstyle { \mathcal { T } } _ { 0 }$ is not at all artificial.) We begin this section with several examples illustrating the use of this method of accounting.

First consider a simple a heat engine as shown in Fig. 4.2a. The engine's cold temperature is labeled with the subscript $0 ,$ to specify it as the environment temperature where waste heat of no value is rejected. We can write the engine's work as the hot heat times the

![[mu_ad18d396_0cedeec032fcfef06c16.jpg]]  
Figure 4.1: (a) The simplest engine and refrigerator, for which simple measures of efficiency suffice. (b) An air separator-liquefier, requiring a more sophisticated approach to efficiency.

Carnot efficiency minus something we'll call lost work:

$$
\dot { W } = \dot { Q } _ { H } \left( 1 - \frac { T _ { 0 } } { T _ { H } } \right) - \dot { W } _ { \mathrm { l o s t } } .\tag{4.1}
$$

The first term is the maximum work that an ideal engine could produce, according to the bounds imposed by the first and second laws of thermodynamics, as we reviewed at the beginning of Chapter 1. If the engine is not so ideal, the work it actually produces must be lower; we'll call the difference the lost work $\dot { W } _ { \mathrm { l o s t } }$ . Similarly, for the simple refrigerator shown in Fig. 4.2b, the work required is the sum of the minimum work that an ideal refrigerator would require plus extra work we call $\dot { W } _ { \mathrm { l o s t } }$

$$
\dot { W } = \dot { Q } c \frac { T _ { 0 } - T _ { C } } { T _ { C } } + \dot { W } _ { \mathrm { l o s t } } .\tag{4.2}
$$

A third example, a very simple example of lost work, is illustrated in Fig. 4.2c: Friction in machinery at ambient temperature dissipates work, all of which is clearly lost, so

$$
\dot { \bar { W } } _ { \mathrm { l o s t } } = \dot { \bar { W } } _ { \mathrm { f r i c } } .\tag{4.3}
$$

The fourth example, illustrated in Fig. 4.2d, is more subtle, and begins to show how challenging and how powerful this point of view can be. Figure 4.2d shows a refrigerator, within which some frictional dissipation occurs at a temperature less than the environment temperature $\pmb { \mathcal { T } _ { 0 } } .$ (Such dissipation could be due to drag on a piston in the cold part of the refrigerator.) How much lost work must be assigned to that frictional dissipation? Suppose that this friction is the only non-ideal feature in the system, so the system can be treated like an ideal refrigerator with Carnot's COP, powered by a drive mechanism with friction, with the drive mechanism thermally anchored to the cold temperature $\mathcal { T } _ { C } .$ , as shown in Fig. 4.2d. Some of the drive power $\dot { W }$ is dissipated into heat at $\mathit { \Pi } _ { \mathcal { T } _ { C } }$ by friction; the remaining power drives an ideal refrigerator, which must pump the heat generated by friction plus the external cooling load $\dot { Q } _ { C }$ from the low temperature to the environment temperature. Since the ideal refrigerator has Carnot's COP, we have

![[mu_ad18d396_f9721bdf9ad6b90afcf4.jpg]]

![[mu_ad18d396_33db8be30c2b11cb25e6.jpg]]

(b)  
![[mu_ad18d396_99eea17337923403ad72.jpg]]

(c)  
![[mu_ad18d396_2c8195c4f2f8d41c18b9.jpg]]  
Figure 4.2: Several examples to illustrate the concept of lost work. (a) A simple engine. (b) A simple refrigerator. (c) Friction at temperature $\pmb { T _ { 0 } } .$ (d) Friction at a temperature $T < T _ { 0 }$ (e) Heat transfer across a small thermal resistance.

$$
\dot { W } - \dot { W } _ { \mathrm { f r i c } } = \left( \dot { Q } c + \dot { W } _ { \mathrm { f r i c } } \right) \frac { T _ { 0 } - T _ { C } } { T _ { C } } ,\tag{4.4}
$$

which can be rewritten as

$$
\dot { W } = \dot { Q } c \frac { T _ { 0 } - T _ { C } } { T _ { C } } + \dot { W } _ { \mathrm { f r i c } } \frac { T _ { 0 } } { T _ { C } } .\tag{4.5}
$$

Hence, the lost work in this system is

$$
\dot { W } _ { \mathrm { l o s t } } = \dot { W } _ { \mathrm { f r i c } } { \frac { T _ { 0 } } { T _ { C } } } .\tag{4.6}
$$

Indeed, it seems reasonable that the lost work should be greater than the frictional dissipation, by a factor depending on the temperatures, because intuitively we expect that dissipating work at low temperature should be worse than dissipating it at room temperature: If work is "lost" at low temperature, pumping the resulting heat up to room temperature costs even more work.

A fifth example—imperfect heat transfer—is shown in Fig. 4.2e. Two thermal reservoirs, at nearly equal temperatures $\mathcal { T } + \delta \mathcal { T }$ and ${ \mathcal { T } } ,$ are connected by a thermal resistance through which heat $\dot { \boldsymbol { Q } }$ flows. The work lost in this process is the excess work that could have been produced by an ideal engine driving an ideal heat pump, with the engine operating between $T + \delta T$ and $\pmb { T _ { 0 } }$ and the heat pump operating between $\mathbfcal { T }$ and $\pmb { T _ { 0 } } .$ with the same heat $\dot { Q }$

exchanged with both reservoirs:

$$
\dot { W } _ { \mathrm { l o s t } } ~ = ~ \dot { W } _ { \mathrm { e n g i n e } } - \dot { W } _ { \mathrm { p u m p } }\tag{4.7}
$$

$$
= \dot { Q } \left( 1 - \frac { T _ { 0 } } { T + \delta T } \right) - \dot { Q } \left( 1 - \frac { T _ { 0 } } { T } \right)\tag{4.8}
$$

$$
\simeq ~ \dot { Q } \frac { T _ { 0 } \delta T } { T ^ { 2 } } ,\tag{4.9}
$$

which is small if the temperature difference $\delta T$ is small. (For illustration here, we assumed $T > T _ { 0 } .$ , but the same conclusion follows from assuming $T < T _ { 0 } . )$ Imperfect thermal contact in heat exchangers is responsible for this type of lost work.

These ideas are important because the lost work can be expressed as the product of the environment temperature $\scriptstyle { \mathcal { T } } _ { 0 }$ and the sum of all the entropy generated in the system,

$$
\dot { W } _ { \mathrm { l o s t } } = T _ { 0 } \sum \dot { S } _ { \mathrm { g e n } } ,\tag{4.10}
$$

a result known as the Guoy-Stodola theorem [29]. This theorem is presented clearly in the physics literature [42], but without reference to the decades-earlier work of Guoy and Stodola. We won't prove this theorem here, but we use some of the examples of Fig. 4.2 to illustrate it. First: The entropy generated by imperfect thermal contact in Fig. 4.2e must be the difference between the entropy $\dot { Q } / T$ gained by the lower reservoir and the entropy $\dot { Q } / ( T + \delta T )$ lost by the upper reservoir. The difference is $\dot { Q } \delta T / T ^ { 2 }$ to lowest order in $\delta T ;$ multiplying by $\scriptstyle { \mathcal { T } } _ { 0 }$ indeed yields the lost work given in $\mathtt { E q . }$ (4.9). Second: For friction at a temperature $\boldsymbol { \mathcal { T } }$ as illustrated in Fig. 4.2c, the entropy generation must be the heat generated, which is exactly $\dot { W } _ { \mathrm { f r i c } }$ , divided by T. Multiplying by $\scriptstyle { \mathcal { T } } _ { 0 }$ as prescribed by Eq. (4.10), yields

$$
\dot { W } _ { \mathrm { i o s t } } = \dot { W } _ { \mathrm { f r i c } } \frac { T _ { 0 } } { T } ,\tag{4.11}
$$

in agreement with both Eq. (4.3) and Eq. (4.6).

This method and theorem are important because entropy is an extensive quantity. The sum Σ in Eq. (4.10) can be performed any of a number of ways. The sum can be performed component by component throughout a piece of experimental hardware, tabulating how much entropy is generated in each heat exchanger, stack, resonator, etc. It can even be performed by location within a component, e.g. to determine whether the hot end of the stack, the middle of the stack, or the cold end of the stack is the lossiest. This sum can be performed process by process, tabulating how much entropy is generated by viscous processes, thermal processes, frictional processes, etc., either within each component or system-wide. There seems to be no limit to how finely this sum can be subdivided; one could even ask how much of the thermal entropy generation at a given location is due to heat diffusing in the x direction, and how much is due to heat diffusing perpendicular to x. The sum can be performed with respect to time instead of location or process, e.g. to learn whether the entropy generated by thermal relaxation in a regenerator occurs mostly during the compression and expansion phases of the cycle or during the gas-motion phases of the cycle.

Taken to extreme, this point of view would let us write

$$
\dot { S } _ { \mathrm { g e n } } = \frac { \omega } { 2 \pi } \int _ { 0 } ^ { 2 \pi / \omega } \int _ { V } \rho \dot { s } _ { \mathrm { g e n } } d V d t\tag{4.12}
$$

where the instantaneous rate of entropy generation per unit volume is

$$
\rho \dot { s } _ { \mathrm { g e n } } = \frac { \mu } { T } \ddot { \Phi } + \frac { k \left( \nabla T \right) ^ { 2 } } { T ^ { 2 } } + \frac { j ^ { 2 } / \sigma } { T } + \mathrm { f r i c t i o n } + \mathrm { c h e m i s t r y } + \ldots .\tag{4.13}
$$

This displays the time-averaged rate of entropy generation as an integral, over time and over the whole volume of an apparatus, of the instantaneous rate of entropy generation, which is itself the sum effects coming from different processes: viscous, thermal, electrical, frictional, chemical, etc. Having this in mind will let you think about where and how the inefficiencies arise in a system. Quoting from a clear review [42} of this method: $^ { \mathfrak { s o } } \mathbf { 1 } \mathbf { n }$ accordance with the circumstance that entropy is a quantity having extensive magnitude, it is evident that $[ T _ { 0 } \dot { S } _ { \mathrm { g e a } } ]$ can be calculated by adding together separate terms of the form $[ T _ { 0 } \dot { S } _ { \mathtt { g e a } } ]$ for each of the irreversible processes that accompany a total operation. This then allows us to take each of these separate terms ... as a measure of the loss in potential work that results from the corresponding particular irreversible processes in the total operation. This is an important principle, since it allows us to determine the reduction in efficiency resulting from any particular cause without making an analysis of the whole operation."

<table><tr><td>Source  $\dot { W } _ { \mathrm { l o s t } }$ </td><td>(macroscopic)  $\frac { \rho \dot { s } _ { \mathrm { g e n } } \ ( \mathrm { m i c r o s c o p i c } ) } { j ^ { 2 } / \sigma T }$ </td></tr><tr><td>Electrical</td><td> $\sqrt { I ^ { 2 } R T _ { 0 } / T }$ </td></tr><tr><td>Friction</td><td> $\dot { W } _ { t r i c } \mathcal { T } _ { 0 } / T$  vσ/T (per unit area)</td></tr><tr><td>Viscosity</td><td> $U \Delta p T _ { 0 } / T$   $\mu \ddot { \Phi } / T + \zeta \left( \nabla \cdot \mathbf { v } \right) ^ { 2 } / \dot { T }$  2  $\begin{array} { r } { \dot { \Phi } = \frac { 1 } { 2 } \left( \frac { \partial \psi _ { i } } { \partial x _ { k } } + \frac { \partial \upsilon _ { k } } { \partial x _ { i } } - \frac { 2 } { 3 } \delta _ { i k } \frac { \partial \upsilon _ { l } } { \partial x _ { l } } \right) } \end{array}$  where</td></tr><tr><td>Imperfect heat transfer  $( \delta T \ll T )$  Heat leak Thermal mixing</td><td> $\dot { Q } T _ { 0 } \delta T / T ^ { 2 }$   $k \left( \nabla T \right) ^ { 2 } / T ^ { 2 }$   $\dot { Q } T _ { 0 } \left( T _ { H } - T _ { C } \right) / T _ { H } T _ { C }$   $\pmb { k } \left( \nabla T \right) ^ { 2 } / T ^ { 2 }$   $\dot { m } c _ { p } T _ { 0 } \log \left[ \left( x + \tau ( 1 - x ) \right) / \tau ^ { 1 - x } \right]$  where  $m = m _ { 1 } + m _ { 2 } ,$   $x = m _ { 1 } / m _ { 2 } , \mathrm { a n d } \tau = T _ { 1 } / T _ { 2 }$ </td></tr></table>

The table above gives expressions for lost work and entropy generation for some dissipative processes encountered in thermoacoustics. (Watch out for factors of two if you use the macroscopic column for time-averaged acoustic situations.) For example, if dc electrical power is dissipated by resistance, the dissipated electrical power is $I ^ { 2 } R ,$ and the lost work is $ { T _ { 0 } } / T$ times the dissipated power. Microscopically, the entropy generatio is given by the heat generation rate $j ^ { \bar { 2 } } / \sigma$ per unit volume, divided by the temperature at which the heat is generated. Integrating that entropy generation over the whole volume of a resistor, and multiplying by $\scriptstyle { \mathcal { T } } _ { 0 }$ to convert from entropy generation to lost work, yields the macroscopic expression for lost work. As a second example, viscous flow down a pipe, if we are not concerned about microscopic details such as whether the flow is turbulent or laminar, we can compute the lost work with the macroscopic expression. If instead we are concerned with microscopic details, perhaps to understand the spatial distribution of dissipation within a channel of a stack, then we can use the microscopic expression. This list of entropy-generating processes could be extended greatly—it's amazing how many mechanisms contribute to the increase of the entropy of the universe!

Imperfect heat transfer is one of the most important loss mechanisms in engines and refrigerators, so consider the $k ( \nabla T ) ^ { 2 } / T ^ { 2 }$ term in more detail. If $k = 0$ —perfect insulation— there is no entropy generation. In the other extreme, $k = \infty ,$ there is also no loss, because in that case ∇T is zero. Only the in-between case is lossy. Unfortunately, all real gases and materials have nonzero, finite thermal conductivity, so all are lossy! In standing-wave systems, the situation is severe, because we depend on such imperfect thermal contact to get useful thermodynamic behavior, with heat being transferred irreversibly across a thermal penetration depth, throughout the stack, every cycle of the wave. For this reason, standingwave systems have sometimes been called “intrinsically irreversible" [43].

In our experience at Los Alamos, the important types of processes that are responsible for irreversibility in thermoacoustic engines and refrigerators are:

(1) Thermal relaxation occurs within the stack in any standing-wave system, because imperfect thermal contact characterized by $\mathrm { I m } [ f _ { \kappa } ] \neq 0$ in the stack is necessary for nonzero power in standing-wave systems. In traveling-wave systems, those losses are in principle and in practice smaller, giving traveling-wave systems an inherent efficiency advantage over standing-wave systems.

(2) Viscous drag in stacks and regenerators is important in both standing- and travelingwave systems. Some viscous loss is unavoidable, because for anything except liquid metals [44] the Prandtl number is of order one so the viscous penetration depth is of the same order as the thermal penetration depth.

(3) Ordinary conduction of heat in the x direction from hot to cold along stacks and regenerators is conceptually a very simple loss. However, it is unavoidable, especially in the wall of the pressure vessel.

(4) Thermal-relaxation loss and viscous loss occurs not only in stacks and regenerators but also on resonator walls and in heat exchangers.

(5) Serious thermal bottlenecks can occur elsewhere in heat exchangers, in the solid metal parts and in the fluids such as water flowing through them to carry heat to or from the system.

(6) When used, electroacoustic transducers contribute significantly to system loss, through electrical dissipation and sometimes through piston friction

(7) Finally, there are things that we don't yet understand; our systems never perform as well as we think they should. And effects beyond the acoustic approximation add to the severity of many of the items in this list; for example, turbulence in resonators adds to the viscous losses there.

## 4.2. Exergy

Consider the system shown in Fig. 4.3, processing a mass flow m of fluid from one temperature and pressure to another temperature and pressure. Liquefaction of nitrogen or methane is typical of such a process. The system consumes work $\dot { W } _ { ; }$ ,and waste heat $\dot { Q } _ { 0 }$ is rejected at temperature $\pmb { T _ { 0 } } .$ . The first law of thermodynamics indicates that the sum of the powers

![[mu_ad18d396_8d6994c1cb8a79ad731b.jpg]]

Figure 4.3: A thermodynamic device using work to process a flowing stream of material rn from an input condition to an output condition. The device rejects waste heat at $\pmb { \mathcal { T _ { 0 } } }$

going in must equal the sum of the powers going out:

$$
\dot { W } + \dot { m } h _ { \mathrm { i n } } = \dot { Q } _ { 0 } + \dot { m } h _ { \mathrm { o u t } } .\tag{4.14}
$$

Note the use of enthalpy here; it is the correct energy to use in the first law for open systems, as discussed briefly in Chapter 3 and extensively in most thermodynamics texts [29]. The second law of thermodynamics indicates that the entropy leaving the system must equal the sum of the entropy entering the system plus entropy generation within the system:

$$
{ \frac { \dot { Q } _ { 0 } } { T _ { 0 } } } + { \dot { m } } s _ { \mathrm { o u t } } = { \dot { m } } s _ { \mathrm { i n } } + T _ { 0 } \sum { \dot { S } } _ { \mathrm { g e n } } .\tag{4.15}
$$

The sources $\dot { S } _ { \mathrm { g e n } }$ inside the system are viscous, frictional, and other dissipative processes as discussed in the previous section.

Combining these two equations by eliminating the uninteresting quantity $\dot { Q } _ { 0 }$ yields

$$
\dot { \hat { W } } = \dot { m } \left[ \left( h - T _ { 0 } s \right) _ { \mathrm { o u t } } - \left( h - T _ { 0 } s \right) _ { \mathrm { i n } } \right] + T _ { 0 } \sum \dot { S } _ { \mathrm { g e n } } .\tag{4.16}
$$

This shows that $h { - } T _ { 0 } s$ is another important, special energy in thermodynamics problems. If the system is ideal—if there are no entropy-generating processes in the system, so $\Sigma S _ { \tt g e n } = 0$ —then the work needed to process unit mass of the fluid is given by the difference between the outgoing and incoming $h - T _ { 0 } s$ .Any real system must use at least that much work to perform this process. Physicists note: This is not the Gibbs energy $\hbar - T s$ . This energy per unit mass $\pmb { b } \equiv h - T _ { 0 } s$ is called the flow availability, well known to mechanical engineers and especially to chemical engineers. It is invaluable in evaluating the minimum work required to perform a complex process, such as that shown in Fig. 4.1b.

We can follow a similar philosophy [29] to derive an acoustic approximation to the Guoy-Stodola theorem, and to introduce the important concept of exergy $x ,$ an important energy that keeps track of the ability to do useful work when a thermal reservoir at temperature $\pmb { T _ { 0 } }$ is freely accessible. Consider the schematic of a generalized portion of thermoacoustic system shown in Fig. 4.4. If the portion shown is in steady-state operation, the first law of thermodynamics shows that the difference between energy fluxes going out and going in must be zero:

$$
0 = \dot { H } _ { 2 0 \mathrm { u t } } + \dot { W } - \dot { H } _ { \mathrm { 2 I n } } - \dot { Q } _ { 0 } - \sum _ { i } \dot { Q } _ { i } .\tag{4.17}
$$

![[mu_ad18d396_a2a9ab5ca0796d257fac.jpg]]  
Figure 4.4: A generalized portion of thermoacoustic apparatus. The x direction is horizontal, and the portion, with length $\Delta { x } ,$ has acoustic power $\dot { E } _ { 2 I n }$ and total power $\dot { H } _ { 2 I n }$ flowing into the left open end and acoustic power $\dot { E } _ { 2 O u t }$ and total power $\dot { H } _ { 2 O u t }$ flowing out of the right open end. In between, the portion produces (or receives) time-averaged work power $\bar { \boldsymbol { W } }$ absorbs (or rejects) heat power $\dot { Q } _ { 0 }$ to ambient at ${ \mathcal { T } } _ { 0 } ,$ and absorbs (or rejects) one or more other heat powers $\dot { Q } _ { i }$ to other temperature(s) $\mathcal { T } _ { i }$ . The sign conventions are indicated by the arrows.

The second law of thermodynamics says that the difference between the entropy fluxes going out and going in must equal the entropy generated within the portion:

$$
\dot { S } _ { \mathrm { g e n } } = \frac { \dot { H } _ { \mathrm { 2 O u t } } - \dot { E } _ { \mathrm { 2 O u t } } } { T _ { m \mathrm { O u t } } } - \frac { \dot { H } _ { \mathrm { 2 I n } } - \dot { E } _ { \mathrm { 2 I n } } } { T _ { m \mathrm { I n } } } - \frac { \dot { Q } _ { 0 } } { T _ { 0 } } - \sum _ { i } \frac { \dot { Q } _ { i } } { T _ { i } } .\tag{4.18}
$$

In Eq. (4.18), we use $( \dot { H } _ { 2 } - \dot { E } _ { 2 } ) / { T _ { m } }$ as the second-order entropy flux, as shown in Eq. (3.26) where the first term is $T _ { m }$ times the second-order hydrodynamic entropy flux and the second term is the conduction of heat along x through the gas and solid parts. Combining Eqs. (4.17) and (4.18) by eliminating the uninteresting heat $\dot { Q } _ { 0 }$ easily yields

$$
\begin{array} { r c l } { { T _ { 0 } \dot { S } _ { \mathrm { g e n } } } } & { { = } } & { { \displaystyle { \frac { T _ { 0 } } { T _ { m \mathrm { I n } } } \dot { E } _ { \mathrm { 2 I n } } + \left( 1 - \frac { T _ { 0 } } { T _ { m \mathrm { I n } } } \right) \dot { H } _ { \mathrm { 2 I n } } - \frac { T _ { 0 } } { \dot { T } _ { m \mathrm { O u t } } } \dot { E } _ { \mathrm { 2 O u t } } + \left( 1 - \frac { T _ { 0 } } { T _ { m \mathrm { O u t } } } \right) \dot { H } _ { \mathrm { 2 O u t } } } } } \\ { { } } & { { } } & { { \displaystyle { - \dot { W } + \sum _ { i } \dot { Q } _ { i } \left( 1 - \frac { T _ { 0 } } { T _ { i } } \right) . } } } \end{array}\tag{4.19}
$$

This is written in terms of exergy as

$$
T _ { 0 } \dot { S } _ { \mathrm { g e n } } = \dot { X } _ { \mathrm { 2 I n } } - \dot { X } _ { \mathrm { 2 O u t } } - \dot { X } _ { W } + \sum _ { i } \dot { X } _ { Q _ { i } } ,\tag{4.20}
$$

where the acoustic approximation to the time-averaged exergy flux $\dot { X } _ { 2 } ( x )$ in the x direction in a channel is

$$
\dot { X } _ { 2 } = \frac { T _ { 0 } } { T _ { m } } \dot { E } _ { 2 } + \left( 1 - \frac { T _ { 0 } } { T _ { m } } \right) \dot { H } _ { 2 } .\tag{4.21}
$$

Similarly, the exergy flux $\dot { X } _ { W }$ associated with work power is the work power $\dot { \bar { W } }$ itself,

$$
\dot { X } _ { W } = \dot { W } ,\tag{4.22}
$$

and the exergy flux $\dot { X } _ { Q }$ associated with a heat power $\dot { Q }$ flowing from temperature $\mathbfcal { T }$ is

$$
\dot { X } _ { Q } = \dot { Q } ( 1 - T _ { 0 } / T ) .\tag{4.23}
$$

Each of these three expressions for exergy flux gives the ability of the associated power to do work, in the presence of a thermal reservoir at $\pmb { \mathcal { T } _ { 0 } } .$ If $\dot { S } _ { \mathtt { g e n } } = 0$ , these expressions prescribe how work power, heat power, and oscillatory thermohydrodynamic power could be freely interchanged within the bounds of the first and second laws of thermodynamics.

Reminiscent of the total-power equation discussed in Chapter ${ \mathfrak { s } } ,$ the acoustic-approximation exergy-flux equation (4.21) is like a kaleidoscope, giving many different views depending on how it is shaken. We will look at a few:

In a stack, regenerator, or thermal buffer column, laterally insulated and bounded so that no exergy can flow out perpendicular to x, we have a thermoacoustic approximation to ${ \pmb x } ,$ the Guoy-Stodola theorem:

$$
T _ { 0 } \frac { d \sum { \dot { S } } _ { \mathrm { g e n } } } { d x } = - \frac { d { \dot { X } } _ { 2 } } { d x } .\tag{4.24}
$$

This equation expresses the combined first and second laws of thermodynamics in thermoacoustics, showing that

$$
\frac { d \dot { X } _ { 2 } } { d x } \leq 0\tag{4.25}
$$

always, just like $0 = d \dot { H } _ { 2 } / d x$ expresses the first law in a stack, regenerator, or thermal buffer column. Exergy is conserved if and only if no entropy is generated.

If $T _ { m } = T _ { 0 } ,$ then Eq. (4.21) shows that ${ \dot { X } } _ { 2 } = { \dot { E } } _ { 2 }$ . In words, acoustic power at $\pmb { T _ { 0 } }$ represents the ability to do work, in the thermodynamic sense. Thus far in this book, we may have tacitly assumed that this is true, but we have not proven it until this point! In this simplest situation, lost work and entropy generation are related in the most straightforward manner,

$$
- { \frac { d { \dot { X } } _ { 2 } } { d x } } = T _ { 0 } { \frac { d \sum { \dot { S } } _ { \mathrm { g e n } } } { d x } } = - { \frac { d { \dot { E } } _ { 2 } } { d x } } .\tag{4.26}
$$

Now suppose that $T _ { m } \neq T _ { 0 }$ , and consider an ideal regenerator with $\dot { H } _ { 2 } = 0$ . Then $\dot { X } _ { 2 } =$ $\dot { E } _ { 2 } T _ { 0 } / T _ { m }$ . Hence, acoustic power in a temporally isothermal space, such as a regenerator, at temperature $\mathcal { T } _ { m } < \mathcal { T } _ { 0 }$ has an ability to do work that is greater than $\dot { E } _ { 2 }$ itself. (This may make acousticians uneasy, but it is true, because a limitless source of heat at temperature $\scriptstyle { { \mathcal { T } } _ { 0 } }$ is presumed to be available. The first law shows that some such source of heat must be utilized if work is to be extracted from an ideal regenerator, in which $\dot { H } _ { 2 } = 0 . )$ Similarly, acoustic power in a temporally isothermal space at temperature $T _ { m } > T _ { 0 }$ represents a reduced ability to do work; the full $\dot { E } _ { 2 }$ cannot be converted to $\dot { \bar { W } }$ without adding exergy from another source, such as heat at temperature $\mathcal { T } _ { m } > \mathcal { T } _ { 0 }$

![[mu_ad18d396_edb323879e7caf8745a6.jpg]]  
Figure 4.5: Schematic of an ideal orifice pulse tube refrigerator, showing the total power, acoustic power, and exergy flux as functions of position. The apparatus is insulated except at the heat exchangers, so the piston work $\dot { W } .$ , aftercooler heat $\dot { Q } _ { 0 A }$ , refrigeration load $\dot { Q } _ { C }$ and final waste heat $\dot { Q } _ { 0 R }$ are the only energies entering or leaving the apparatus.

Continuing to suppose that $T _ { m } \neq T _ { 0 }$ , consider an ideal thermal buffer column or pulse tube, for which $\dot { E } _ { 2 } = \dot { H } _ { 2 }$ . Then $\dot { X } _ { 2 } = \dot { E } _ { 2 }$ , independent of $\mathcal { T } _ { m }$ . In this case, Eq. (4.26) holds, with $d \dot { E } _ { 2 } / d x = 0$ only if $\dot { S } _ { \mathtt { g e n } } = 0$ . Again, $\dot { E } _ { 2 }$ represents the ability to do work.

These points are illustrated in Fig. 4.5 for an ideal orifice pulse-tube refrigerator, assumed to be thermally insulated except at the three heat exchangers. The total power must be piecewise constant, with discontinuities at the heat exchangers equal to the heats transferred there. The acoustic power must be continuous, decreasing through the regenerator not because of viscosity but rather because $U _ { 1 }$ decreases as $\mathcal { T } _ { m }$ decreases, and decreasing again in the flow resistance $\scriptstyle { R }$ due to viscosity. The exergy flux is constant throughout the regenerator. It decreases at the cold heat exchanger by $\dot { Q } c ( 1 - T _ { 0 } / T _ { C } )$ , which is the amount of exergy carried out of the system by the heat load $\dot { Q } _ { C }$ . It is constant again along the pulse tube, finally dropping to zero smoothly in the flow resistance $R ,$ which is the only location with nonzero $\dot { S } _ { \mathtt { g e n } }$

Using Eq. (4.21) to write an explicit expression for $d \dot { X } _ { 2 } / d x$ in a stack, regenerator, or thermal buffer column, in which $d \dot { H } _ { 2 } / d x = 0$ , yields

$$
\frac { d \dot { X } _ { 2 } } { d x } = \frac { T _ { 0 } } { T _ { m } } \left[ \frac { d \dot { E } _ { 2 } } { d x } + \left( \dot { H } _ { 2 } - \dot { E } _ { 2 } \right) \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \right] .\tag{4.27}
$$

In the inviscid limit, $\mu = 0$ , and using appropriate expressions from Chapters 2 and 3, Eq.

(4.27) becomes

$$
\begin{array} { r c l } { \displaystyle \frac { d \dot { X } _ { 2 } } { d x } ~ = ~ - \frac { 1 } { 2 r _ { \kappa } } | p _ { 1 } | ^ { 2 } \left[ 1 + 2 \frac { d T _ { m } / d x } { \nabla T _ { \mathrm { c r i t } } } \sin \phi _ { p U } + \left( \frac { d T _ { m } / d x } { \nabla T _ { \mathrm { c r i t } } } \right) ^ { 2 } \right] } \\ { \displaystyle } & & { - ( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } ) \frac { \left( d T _ { m } / d x \right) ^ { 2 } } { T _ { m } } } \end{array}\tag{4.28}
$$

which is always $\leq 0 ,$ for any values of $d T _ { m } / d x$ and $\phi _ { p U } ,$ as expected. The angle $\phi _ { p U }$ is the phase difference by which ${ \pmb p } _ { 1 }$ leads $\boldsymbol { \mathcal { \tau } _ { 1 } }$ . The interpretation of the second term $( \ i . \ e . ,$ second line) of Eq. (4.28) is trivial based on our discussion of heat-transfer irreversibility in the previous section. The first term (i.e., first line) is more interesting. It can be reduced to zero by making $r _ { \kappa } = \infty ,$ as is approximately the case for traveling-wave systems. However, the intrinsic irreversibility of standing-wave systems is apparent here, as $1 / r _ { \kappa }$ ∝ Im $[ - f _ { \kappa } ]$ must be nonnegligible for standing-wave systems; otherwise they develop no power, as shown by the discussion near Eq. (3.27). In this case, the only way to make the first term in Eq. (4.28) zero is by setting sin $\phi _ { p U } = 1$ (i.e., pure standing waves) and $d T _ { m } / d x = \nabla T _ { \mathrm { c r i t } } ,$ exactly the situation for which standing-wave systems have zero power.

Thus far I have been unable to grind through the algebra to find a pretty version of $d \dot { X } _ { 2 } / d x$ for $\mu \neq 0 .$ I had hoped it would depend cleanly on $r _ { \kappa } , r _ { \nu } ,$ and $\left( { d T _ { m } } / { d x } \right) / { \nabla T _ { \mathrm { c r i t } } } ,$ because the only sources of irreversibility are viscous shear, imperfect thermal contact, and the trivial term arising from ordinary conduction of heat. along x.

## 4.3. Examples

Example: orifice pulse-tube refrigerator: The orifice pulse-tube refrigerator of Figs. 1.15 and 1.16 provides a realistic example similar to the ideal orifice pulse-tube refrigerator considered above. The flows of exergy, acoustic power, and total power are shown in Fig. $4 . 6 ,$ for the same operating point as that used to generate the power plots in Fig. 3.8 and the phasors in Fig. 2.19. The exergy curve was calculated using Eq. (4.21), using DeltaE's values for $\dot { H } _ { 2 } , \dot { E } _ { 2 } ,$ and $\scriptstyle { { \mathcal { T } } _ { m } }$ . Incoming from the left, the acoustic power, total power, and exergy flux are all nearly equal at 8.8 kW in the large-diameter entrance duct. The ambienttemperature aftercooler removes 8.3 kW of heat at $T _ { \mathbf { 0 } } ,$ which reduces the total power by that amount but has no effect on the exergy because heat·at $\pmb { T _ { 0 } }$ carries no ability to do work. There is a small reduction in acoustic power in the aftercooler, and the exergy decreases in step with this acoustic power, as required in a channel at temperature $\pmb { T _ { 0 } } .$ Next, in the regenerator the acoustic power drops considerably, but only part of this drop represents a loss in exergy (mostly due to viscosity); much of this decrease in acoustic power would occur even for $\mu = 0$ , as a result of the mean temperature gradient. The exergy flux drops through the cold heat exchanger, but this represents no lossonly the flow of exergy out of the thermoacoustic part of the system and into the refrigeration load. Through the pulse tube, exergy decreases only a little, due largely to the heat leak down the walls of the pulse tube. At the end of the apparatus, exergy is destroyed in viscous flow in the orifice, although thermal insulation around the orifice, inertance, and compliance ensure that the energy associated with that exergy destruction shows up at the adjacent heat exchanger. Overall, the exergy losses in the orifice and in the regenerator are comparable, and are larger than that in the aftercooler. The fact that almost half the exergy loss in this system occurs in the orifice motivated our research [45] into methods of feeding acoustic power from the hot end of the pulse tube back to the left of the heat exchange components instead of dissipating it in the orifice.

![[mu_ad18d396_c7f59c46c8798a564149.jpg]]  
Figure 4.6: Schematic of Cryenco pulse-tube refrigerator, with lengths along x to scale, and diagram showing acoustic power, total power, and exergy flux at a representative operating point.

Example: standing-wave engine: The engine of Figs. 1.9 and 1.10 serves as an additional illustration of the use of exergy. In Fig. 4.7, we have added an exergy curve calculated using Eqg. (4.21) to the energy plot of Fig. 3.7. At the hot heat exchanger, 2380 W of heat was added, causing 2380 W of total power to flow down the stack. This heat, at a temperature of 760 K, carried only 1440 W of exergy into the system. Some 720 W of this exergy is lost in the stack, due to viscosity, imperfect thermal contact, and conduction of heat along x, in the process of generating 670 W of acoustic power. A full 1000 W of exergy flows into the refrigerator at the side branch, in the form of 1000 W of acoustic power at $\scriptstyle { \mathcal { T } } _ { 0 }$

At another operating point for the standing-wave engine, one which received both experimental and calculational attention, a total of 3000 W of electric power was supplied to the heaters of the two engines, and 490 W of acoustic power was delivered to the pulse-tube refrigerator. The lost work is the difference between these: 2510 W. Although we didn't measure it, we would infer that 2510 W of heat was showing up in the room-temperature cooling-water streams at $\scriptstyle { \mathcal { T } } _ { 0 }$

![[mu_ad18d396_15ca657387995e9c17eb.jpg]]  
Figure 4.7: Powers for the standing-wave engine, at the same operating point as in Fig. 3.7, with an exergy curve added.

![[mu_ad18d396_9fdf7e66e992c39a5f5d.jpg]]  
Figure 4.8: At one experimental operating point, the standing wave engine accepted 3000 W of input electrical power and rejected 2510 W of waste heat at $\pmb { \mathcal { T } _ { 0 } } .$ Hence, 2510 W of work was lost.

To gain understanding of the sources of irreversibility in the system at this operating point, I made an arbitrary choice of how to break up this lost work: mostly by component, but with some subdividing according to process. Making intelligent estimates based partly on measurement and partly on a corresponding DeltaE model of this system generated this table.

<table><tr><td>Source  $\overline { { I ^ { 2 } R } }$ </td><td> $\widehat { W } _ { \mathrm { l o s t } }$  730 W</td></tr><tr><td>room heat leak hot heat exchgs acoustics hot heat exchgs δT stacks</td><td>300 W 20 W 10 W 950 W</td></tr><tr><td>stacks pressure vessel heat leak cold heat exchgs acoustics</td><td>150 W 10 W</td></tr><tr><td>cold heat exchgs  $\delta T$  resonator unknown</td><td>70 W 35 W 235 W</td></tr></table>

Such a table can serve as one guide when contemplating improvements to a thermoacoustic system, to help decide which components are responsible for losses, and maybe to help decide how to spend time and money most effectively to improve the overall system efficiency. In this case, consider the sources of lost work starting with the largest: The stacks contribute 950 W. I believe I optimized the gaps, lengths, and positions of these parallelplate stacks well during the design of this system, so I doubt that rebuilding the stacks with different gaps or lengths would improve performance much. However, most of that 950 W is thermal-relaxation loss, not viscous losses. The thermal-relaxation loss is large in this system because of the size constraint imposed by the project's sponsor; if we were free to make the system bigger, we could operate closer to the critical temperature gradient and thus have a more efficient thermoacoustic engine. Hence, this table strongly suggests that we should re-negotiate the size constraint with the sponsor. We might consider trying to build a pin-array stack, because computer calculations usually show that a pin-array stack should perform aboųt 20% better than a parallel-plate stack. However, building such an intricate pin array, with supports for the pins that don't block the sound wave badly, seems daunting (i.e. expensive). The. second-largest loss in the table is the $I ^ { 2 } R$ loss in the NiCr heaters in the two thermoacoustic engines. What does this mean, that 730 W is lost to $I ^ { 2 } R ,$ when 3000 W is converted from electricity to heat in the heaters? We're turning 3000 W of electrical power into 3000 W of heat at temperature $\mathcal { T } _ { H }$ . The formula in the previous table shows that the lost work in that process is $I ^ { 2 } R T _ { 0 } / T _ { H }$ "Work is lost” in this process because the first and second laws allow for a more efficient way to deliver 3000 W of heat to $T _ { H }$ , in principle: This 3000 W of heat could be delivered to the engine at $T _ { H } = 1 2 3 0$ Kelvin by spending only 2270 W of electric power, driving a heat pump with Carnot's COP operating between $\scriptstyle { \mathcal { T } } _ { 0 }$ and $\mathcal { T } _ { H }$ . The difference, 3000 W - 2270 W, is the lost work. Reducing lost work from this source also sounds expensive. The next largest sources seem more promising. Heat leak from $\mathcal { T } _ { H }$ to the room contributes 300 W, which might be reduced simply by more insulation, if the sponsor's size constraint is not compromised. Unknown sources contribute 235 W, which might serve as justification for asking the sponsor for more funds for fundamental research in thermoacoustics. The heat leaks along the two pressure vessels enclosing the two stacks contribute 150 W, which suggests that we might look for a reasonable-cost alloy with greater strength or lower thermal conductivity than the Incolloy 800H used here.

## 4.4. Exercises

4.1 A simple heat engine operates between temperatures $\pmb { T } _ { \pmb { H } }$ and $\pmb { T _ { 0 } } .$ Its work output is used to drive a simple refrigerator, which pumps heat from a load at temperature $\pmb { T _ { C } }$ ; it rejects waste heat at temperature $\pmb { \mathcal { T } _ { 0 } } .$ The efficiency of this composite system is the ratio of heat pumped from $\mathit { \Pi } _ { \mathcal { T } _ { C } }$ to heat consumed from $\mathcal { T } _ { H }$ . What is the limit on efficiency imposed by the first and second laws of thermodynamics?

4.2 An ideal gas, with temperature-independent specific heat $c _ { p } ,$ flowing with mass flow rate $\dot { m } ,$ must be cooled from $\pmb { \mathcal { T } _ { 0 } }$ to $\mathit { \Delta } \mathit { T _ { C } }$ . In case 1, the cooling is provided by a Carnot refrigerator removing heat from $\pmb { T _ { C } }$ and rejecting waste heat to $\pmb { \mathcal { T } _ { 0 } }$ . In case $\mathfrak { L } _ { \mathrm { j } }$ the cooling power is provided by two Carnot refrigerators rejecting waste heat to $\pmb { T _ { 0 } } ;$ the gas stream first encounters the first refrigerator, whose cold end is at $( T _ { 0 } + T _ { C } ) / 2 ,$ and then encounters the second refrigerator, whose cold end is at $\mathit { T _ { C } }$ . Case 3 is similar to case ${ \mathfrak { L } } ,$ except that the colder refrigerator rejects its waste heat at $( T _ { 0 } + T _ { C } ) / 2$ and the first refrigerator must absorb that heat in addition to the heat from the gas stream. Calculate the work required in all three cases, and compare it to the minimum work given by Eq. (4.16). How might you design cooling hardware that would approach the minimum work more closely?

4.3 Demonstrate the Guoy-Stodola theorem for the system of Fig. 4.2d, by showing that the difference between the entropy increase of the reservoir at $\pmb { T _ { 0 } }$ and the entropy decrease of the reservoir at $\mathit { \Delta } \mathit { T _ { C } }$ equals the lost work given by Eq. (4.6) divided by $\pmb { \mathcal { T } _ { 0 } }$

4.4 Investigate $\rho \dot { s } _ { \tt g e a }$ for the simplest thermal-penetration-depth problem, with $\pmb { u } _ { 1 } = 0$ and boundary-layer approximation. Make a plot of the time-average of the entropy generation per unit volume, as a function of distance from the wall. How does this plot compare with the plot of power dissipated per unit volume shown in Ani. Thermal? Does this make sense? Compare $\int \rho \dot { \boldsymbol { s } } _ { \mathrm { g e n } }$ dy with the results of exercise 4.8, to verify the Guoy-Stodola theorem in this context.

4.5 Pick one process, one component, or one process within one component of your favorite thermoacoustic system, and estimate (order of magnitude) the lost work. What fraction of the total lost work for the whole system does this represent?

4.6 In Chapter 3, we demonstrated the "intrinsic irreversibility" of standing-wave engines and refrigerators, even in the inviscid limit $\pmb { \mu } = 0$ , by showing that both the useful $e U _ { 1 }$ term and the harmful $\pmb { r _ { \kappa } }$ term in $d \dot { E } _ { 2 }$ are proportional to Im $[ f _ { \kappa } ]$ . With $\pmb { \mu } = 0$ and ignoring thermal conduction along $\pmb { x } ,$ re-examine the question of intrinsic irreversibility from the point of view of the exergy flux ${ \dot { X } } _ { 2 } ,$ ,showing that within a stack (where $\dot { H } _ { 2 }$ is independent of x) exergy is destroyed unless the temperature gradient equals $\nabla T _ { \mathsf { c r i t } }$

.4.7 On a trans-Pacific airplane flight, you are surprised to see your rich uncle, a banker, whom you haven't seen in 10 years. He tells you that he is about to invest heavily in a natural-gas recovery project that will make him unimaginably wealthy.

The project involves a huge, high-pressure natural-gas reservoir under the Arctic Ocean. The gas will arrive at the floating platform on the ocean surface in a pipe, at a pressure of

100 bar and a temperature of zero degrees Centigrade, which is the temperature of the ocean. He says that the brilliant scientist he will be investing in has invented two special machines. One machine will use the gas pressure to drive a special turbine, to generate power from the 100 bar gas. As it does work on the turbine, the gas will expand to atmospheric pressure, and cool. He doesn't remember how much it will cool. The second machine will use some of the power from the turbine to further cool the gas and liquefy it. There will be power left over, to run the lights, water pumps, radios, computers, heaters, etc. for 'the workers on the platform. The liquefied gas will be carried in cryogenic tankers to Tokyo.

He is certain that the planned platform will require no external source of power, nor will it need to burn any of the gas. It will be completely powered by the expansion of the gas from 100 bar. He remembers that one or both of the two machines will have a large heat exchanger connected to the ocean water.

You remember that methane liquefies at 112 Kelvin at atmospheric pressure, and that the latent heat is approximately equal to the total heat that must be removed to cool gaseous methane from zero degrees Centigrade to 112 Kelvin. You assume that the gaseous methane, $\dot { \mathrm { C H } } _ { 4 }$ , can be treated as an ideal gas. You remember that changes in enthalpy of an ideal gas are given by $d h = c _ { p } d T$ , and that changes in entropy of an ideal gas are given by $d s = \left( c _ { p } / T \right) d T - \left( 1 / \rho T \right) d p ,$

Evaluate the feasibility of this scheme using the first and second laws of thermodynamics. Convince your uncle that the first and second laws of thermodynamics are applicable to this scheme, and that you can decide that his investment plan is unwise without understanding any of the details of the two machines.

4.8 Derive the boundary-layer expression for $d \dot { X } _ { 2 } / d x$ in a stack. Express your answer using the same variables as in Eq. (4.28) plus $\boldsymbol { r } _ { \nu }$ and σ. Then assume standing-wave phasing to simplify your result, showing that it is $\leq 0$

4.9 Resolve this paradox: For an ideal gas, $\begin{array} { r } { \oint p u d t = \oint ( p / \rho ) \rho u d t = R f T \rho u d t . } \end{array}$ In a perfect regenerator, $\boldsymbol { \mathcal { T } }$ is independent of time, so it can be pulled outside the integral, leaving RT ∮ ρu dt. But $\oint \rho u d t = 0$ because there is no net time-averaged mass flux through a perfect regenerator. Hence, $\oint _ { } ^ { } p u d t = 0 $ So acoustic power cannot flow through a perfect regenerator. (If you get stuck, wait until Chapter 5.)

4.10 NASA probes to the outer planets require electric power generators that operate for a decade with extremely high reliability. Currently, this electricity is generated with the thermoelectric effect in a solid. The high-temperature heat is supplied to the thermoelectric component by radioactive decay of a plutonium isotope, and waste heat carried away from the thermoelectric component by a heat pipe and finally rejected by means of black-body radiation to space. The efficiency, i.e. the ratio of electric power to plutonium heat, is 7%.

Consider a thermoacoustic engine as an alternative to the thermoelectric component, perhaps with piezoelectric or electrodynamic transduction of acoustic to electric power. Your assignment: Decide whether this idea might be worth pursuing. Make some plausible assumptions, and make a few rough estimates using various approximate relations throughout the book, to see if a thermoacoustic system might have an efficiency greater than $7 \% ,$ while maintaining extremely high reliability. If you decide this idea might be worth pursuing, write a letter to your friend the program manager at NASA, explaining why you think it's worth pursuing—try to convince her that her office should provide you with financial support to attempt a meaningful design. If you decide the idea is not worth pursuing, write a letter to her explaining why she should reject any half-baked thermoacoustics proposals she receives.

4.11 A simple thermoacoustic refrigérator, with COP equal to 0.3 times Carnot's COP, lifts heat from 276 K and rejects waste heat at $T _ { \mathbf { 0 } } = 3 0 0$ K. The refrigerator is used to cool a stream of 10 grams/sec of water from 300 K to, 276 $\mathtt { K } ;$ this cooling load is the only load on the refrigerator.

In addition to the obvious irreversibility within the thermoacoustic refrigerator, the heat transfer in the cold heat exchanger must be irreversible, because this heat exchanger is at 276 K but the water enters it at 300 K. (Assume water's heat capacity is 4.2 Joule/gm-K, independent of temperature.)

How much heat must be removed from the water stream? How much work power is used to run this refrigerator? Calculate the lost work in the refrigerator and the lost work in the irreversible heat transfer. Compare the appropriate sum/difference of these three numbers with the minimum work required to cool this stream, using Eq. (4.16). How much exergy is added to the water stream? (Comment on the sign of this exergy term, regarding the ability of the cold water stream to do work.)

To reduce the irreversibility in the heat exchanger, it is proposed to use two refrigerators instead of one; the first will operate at 288 K and remove half the heat load from the water stream and the second will operate at 276 K and remove the other half of the heat load from the water stream. (Hence, each refrigerator will have half the cooling power of the original refrigerator.) Assume that both refrigerators reject heat to 300 $\mathbf { K } ,$ and both have $C O P / C O P _ { \mathrm { C a r n o t } } = 0 . 3$ What is the total work power required by this system? Tabulate the lost work in four locations: the two refrigerators, and the two cold heat exchangers.

Now suppose the colder of the two refrigerators rejects its waste heat at 288 K instead of 300 K, so that the warmer of the two refrigerators must pump this heat load in addition to the heat load due to the water stream. Again calculate the total work required, and tabulate the lost work in the four locations. Discuss some of this in terms of exergy; for example, where is exergy destroyed, where does it flow into and out of the apparatus, etc.

4.12 Show that heat exergy $Q ( 1 - T _ { 0 } / T )$ indeed represents the maximum ability to do work, by considering a Carnot engine operating between $\pmb { T }$ and $\scriptstyle { \mathcal { T } } _ { 0 }$ when $T > T _ { 0 }$

4.13 A machine absorbs heat at a rate $\dot { Q } c$ at temperature $\mathit { T _ { C } }$ . Show that a Carnot engine attached to this machine could produce work at a rate $\dot { W } = ( T _ { 0 } / T _ { C } - 1 ) \dot { Q } _ { C }$ . Interpret this result in terms of the heat exergy associated with $\dot { Q } _ { C }$

## 5. BEYOND ROTT'S THERMOACOUSTICS

We have now completed our review of the well-established foundations of thermoacoustics, as based mostly on the work of Nikolaus Rott. In Chapter $\mathfrak { Q } ,$ as summarized in Fig. 2.14, we came to regard any thermoacoustic apparatus as a series of short channels (possibly with internal structure, such as in a stack), each of which can be analyzed using the momentum and continuity equations. This allows us to view a short length of arbitrary thermoacoustic component as a combination of only five impedance elements: series inertance, series viscous resistance, parallel compliance, parallel thermal-relaxation resistance, and the parallel current-controlled current source that appears when a nonzero temperature gradient exists along the channel. In this representation, each dynamical variable, such as pressure ${ \pmb p } ,$ is assumed to have a sinusoidally oscillating part, with the amplitude and phase of the oscillation the only variables of interest. Once oscillating pressure and oscillating velocity are understood in this context, other oscillating variables such as temperature and density follow easily. The acoustic power $\dot { E } _ { 2 } ,$ the second-order total power $\dot { H } _ { 2 } ,$ the time-averaged heats $\dot { Q }$ transferred at heat exchangers, and the second-order exergy flux $\dot { X } _ { 2 }$ can be calculated without controversy from these oscillating variables, when the first and second laws of thermodynamics are brought into consideration.

If an engine or refrigerator is built according to these principles, and no mistakes are made (see Chapter 8), it will work as designed—but only in the limit of low amplitudes. Figure 5.1 illustrates this typical behavior, showing data obtained during early 'debugging of the standing-wave engine of Figs. 1.9 and 1.10, using only one engine and no load on the resonator. Heater power, displayed on the horizontal axis, was applied, resulting in measured pressure oscillations and hot temperatures as shown by the circles. The lines are calculations using DeltaE, based on the acoustic approximation and hence consistent with the discussion in Chapters 2 and 3. At low power, measurements and calculations agree, but at the highest powers the measured and calculated temperatures differ by almost 200°C and the measured and calculated pressure amplitudes differ by almost 25%. Thermoacoustic engines and refrigerators with practical levels of power per unit volume and per unit mass must operate at high amplitudes such as these, where actual behavior deviates significantly from the acoustic approximation. In the early days of thermoacoustic research, we were impressed that the acoustic approximation came so close to the truth at high amplitudes, but our standards are higher now: We hope to understand such deviations quantitatively.

In this chapter, we will examine some of the gas-dynamics phenomena leading to highamplitude deviations from the acoustic approximation. We know all the fundamental physics involved. Most of the relevant gas dynamics and thermodynamics are believed to be included in the general momentum, continuity, and energy equations

![[mu_ad18d396_15702a4eac3ce4580af8.jpg]]  
Figure 5.1: Pressure amplitude and hot temperature as functions of heater power, during early debugging of the standing-wave engine of Figs. 1.9 and 1.10, with the side branch to the refrigerators blocked, and using one spiral stack with its heat exchangers in one end of the resonator but no stack or hot heat exchanger in the other end of the resonator. Helium, 3 MPa, 370 Hz. The points are measurements; the lines are calculations using DeltaE, assuming laminar flow in the resonator.

$$
\frac { \partial \rho } { \partial t } + \pmb { \nabla } \cdot ( \rho \mathbf { v } ) \ = \ 0 ,\tag{5.1}
$$

$$
\rho \left[ \frac { \partial \mathbf { v } } { \partial t } + ( \mathbf { v } \cdot \overbar { \mathbf { V } } ) \mathbf { v } \right] = - \nabla p + \nabla _ { i } \mu \nabla _ { j } v _ { k } + \nabla \zeta \left( \nabla \cdot \mathbf { v } \right) ,\tag{5.2}
$$

$$
\frac { \partial } { \partial t } \left( \frac { 1 } { 2 } \rho { \boldsymbol v } ^ { 2 } + \rho { \boldsymbol \varepsilon } \right) = - \nabla \cdot \left[ \frac { 1 } { 2 } \rho { \boldsymbol v } ^ { 2 } { \bf v } + \rho h { \bf v } - \dot { \bf v } \cdot { \boldsymbol \Sigma } - k \nabla T \right] ,\tag{5.3}
$$

with appropriate boundary conditions, and in the properties of the gas

$$
\begin{array} { r } { p \ = \ \rho R T , } \end{array}\tag{5.4}
$$

$$
\mu ~ = ~ \mu ( p , T ) ,\tag{5.5}
$$

$$
k ~ = ~ k ( p , T ) ,\tag{5.6}
$$

$$
\gamma ~ = ~ \mathrm { c o n s t a n t } .\tag{5.7}
$$

The time-averaged total power [26] flowing in the x direction

$$
\dot { H } = \int \left[ \overline { { \rho u \left( v ^ { 2 } / 2 + h \right) } } - \overline { { k \frac { d T } { d x } } } - \overline { { \left( \mathbf { v } \cdot \Sigma \right) _ { x } } } \right] d A\tag{5.8}
$$

and the time-averaged exergy flux [29] in the x direction

$$
\dot { X } = \int \left[ \frac  \dot { \mathbf { \sigma } } \cdot \dot { \mathbf { \sigma } } ( h - h _ { 0 } ) ] - T _ { 0 } \overline { { \rho u \left( s - s _ { 0 } \right) } } - \overline { { k \left( 1 - \frac { T _ { 0 } } { T } \right) \frac { d T } { d x } } } - \overline { { ( \mathbf { v } \cdot \Sigma ) _ { x } } } \right] d A ,\tag{5.9}
$$

where $h _ { 0 }$ and ${ \pmb s } _ { \bf 0 }$ are the enthalpy and entropy per unit mass in the so-called dead state [29], are also unambiguous. However, knowing that all the fundamental physics involved is captured in these deceptively simple equations is of little use in the day-to-day practice of high-amplitude thermoacoustics, because personal computers and human brains are incapable of processing such complicated equations and truths quickly. The challenge is to find the relevant aspects of the truths expressed in Eqs. (5.1)-(5.9) and to distill them into comprehensible, compact forms and into usable design procedures and analysis procedures. Our “acoustic approximation" of Chapters $2 ^ { - 4 }$ is one such distillation, represented in the computer code DeltąE, but data like those displayed in Fig. 5.1 demonstrate that this approximation omits some important phenomena. Other computer codes include more physics and hence work better at high amplitudes, but sacrifice speed to do so.

While the first four chapters of the book are built. on a well-established foundation, the topics discussed in this chapter are at the frontiers of current understanding. If this chapter seems inelegant or confused, it may be due to the fact that these issues are indeed complicated, and are not well understood. I will not be surprised if some of this chapter turns out to be wrong.

Our approach here will be to build upon and extend our acoustic approximation, adding (you might say kludging) various phenomena onto it. One strength of this approach is that it builds on a firm foundation. One danger of this approach is that it will never find dramatically new phenomena, no matter how interesting or important they might be.

This chapter is still under construction. I have not yet. incorporated examples tied to the "example" hardware of Chapter 1. I have not done sections on porous media, harmonics, or similitude.

## 5.1. Tortuous porous media

In preparation. Screens [38], steel wool, sandstone?, power-law correlations.

## 5.2. Turbulence

Figure 5.2 is the well-known friction-factor diagram [27] for steady flow in a circular pipe. [Here "steady" means that U is independent of time, although $u ( x , y , z , t )$ may fluctuate rapidly.] The figure summarizes all practical knowledge about pressure drops in such flows. Although Eq. (5.2) includes all the physics displayed in Fig. 5.2, Eq. (5.2) is too far removed from the engineering reality of turbulent steady flow to be useful in daily engineering work.

![[mu_ad18d396_5a41d68b9cc4385568a0.jpg]]  
Figure 5.2: Friction factor vs Reynolds number in steady flow in a circular pipe. Reproduced from Fox and McDonald [27]. The different curves in the turbulent regime are for different surface roughnesses in the pipe. This figure (and everything else in Ref. [27]) uses Re to signify the Reynolds number on the horizontal axis, but we will use $N _ { R }$ to avoid confusion with the real part of a variable.

Note the use of dimensionless groups of variables in Fig. 5.2. Engineers have long realized that correlating data using such dimensionless groups provides the only practical compact approach for sharing data. The Reynolds number $N _ { R } = \rho \left. \boldsymbol { u } \right. D / \mu$ is a dimensionless measure of the average velocity, where D is the diameter of the pipe. The vertical axis is the dimensionless Moody friction factor $f _ { M } .$ which is the ratio of pressure drop $\Delta p$ to ${ \scriptstyle \frac { 1 } { 2 } } \rho \left. u \right. ^ { 2 } L / D$ , where L is the pipe length. The dimensionless relative roughness ε is the roughness height on the pipe's inner surface divided by the pipe diameter. We will often use such dimensionless groups in this chapter, and in the last section we will outline a formal approach to the selection of dimensionless groups for thermoacoustic phenomena.

Figure 5.2 shows that steady flow in a smooth circular pipe has two regimes. Below $N _ { R } \sim 2 0 0 0 .$ , the flow is laminar. In this regime, the second term on the left side of Eq. 5.2 can be neglected, and the equation is simple enough for analysis leading to a closed-form solution for the friction factor,

$$
f _ { M } = 6 4 / N _ { R } ,\tag{5.10}
$$

which is the straight line in the left part of Fig. 5.2. Above $N _ { R } \sim 2 0 0 0$ the flow is turbulent.   
Roughness $\varepsilon > 0$ gives higher friction factors in the turbulent regime.

For such steady flow in a circular pipe, two dimensionless parameters ${ \mathbf { \nabla } } \cdot N _ { R }$ and ε—are sufficient to span the space of all possible flows, so the friction factor of any steady flow can be obtained from Fig. 5.2 by specifying these two parameters. In oscillating flow, however, one additional parameter is needed, which must be related to the frequency of oscillations. The viscous penetration depth is a familiar frequency-dependent variable, so $R / \delta _ { \nu }$ (where R is pipe radius) provides a convenient dimensionless form for this third parameter. [The Womersley number $D / \sqrt { 2 } \delta _ { \nu }$ is also commonly used [46] for this third parameter.) One slice through the three-dimensional parameter space of oscillating flow is shown in Fig. 5.3 for a circular pipe; this slice is for $\varepsilon = 0$ , and shows the regimes of behavior as a function of peak Reynolds number $N _ { R , { \mathrm { p e a k } } } = \left| U _ { 1 } \right| D \rho / A \mu$ and $R / \delta _ { \nu }$

Figure 5.3 represents more complicated behavior than Fig. 5.2 represents. The laminar regime of Fig. 5.3 was the subject of chapter 2, and is well understood. We believe that the weakly turbulent regime shares the laminar regime's mathematically simple behavior in the boundary layers, with the turbulence essentially confined to the center of the tube, not in the boundary layers. A transitional zone exists between the weakly turbulet and conditionally turbulent regimes. In the conditionally turbulent regime, hot-wire anemometer measurements [48] show that the flow alternates between weakly turbulent and violently turbulent behavior, with the transition to turbulence occurring at the peak velocity and the return to weak turbulent flow occurring at the zero crossings of velocity. At higher Reynolds numbers, the flow is fully turbulent, essentially resembling the steady turbulent flow at high Reynolds number in Fig. 5.2. The mathematics we developed in Chapters 2 and 3 is probably inapplicable in the transitional, conditionally turbulent, and fully turbulent regimes, because in these regimes the turbulence disturbs the boundary layer deeply and violently.

At the high amplitudes necessary to achieve high power density, various components in thermoacoustic engines and refrigerators operate in all regimes shown in Fig. 5.3, and it is important to calculate peak Reynolds numbers at typical locations in each component to get a rough idea whether deviations from the acoustic approximation might be expected. Pulse tubes and thermal buffer tubes typically operate in the weakly turbulent regime. Resonator components are often fully turbulent, conditionally turbulent, or in the transition regime. Inertances in pulse-tube refrigerators are usually fully turbulent. For other components having non-circular cross sections but with parallel walls, we can only hope that Fig. 5.3 gives reasonable guidance, using $R \sim 2 r _ { h } ;$ with this criterion, we often find that standingwave stacks are in the high-Reynolds part of the laminar regime, sometimes with their cold ends extending into the conditionally turbulent regime, and heat exchangers may fall in any regime except fully turbulent. (As discussed in the previous section, the screen beds of regenerators typically have $r _ { h } / \delta _ { \nu } \ll 1$ and $N _ { R , \mathrm { p e a k } } \sim 5 0 0$ , but Fig. 5.3 offers no guidance for the microscopically tortured geometry of sċreen beds.)

![[mu_ad18d396_dde86b95b33d90316041.jpg]]  
Figure 5.3: Regimes of oscillating flow, in a smooth circular pipe, as a function of peak Reynolds number Re $( = N _ { R , \mathrm { p e a k } }$ in text) and the ratio of pipe radius R to viscous penetration depth $\delta _ { \nu } .$ Adapted from [47]

In Chapters 2 through $\mathbf { 4 } ,$ we learned how useful it is to have expressions for $d p _ { 1 } / d x$ $d U _ { 1 } / d x , d \dot { E } _ { 2 } / d x ,$ and $\dot { H } _ { 2 }$ everywhere. Reality today is not satisfactory in this regard. We're only certain of these expressions in the laminar regime in Fig. 5.3 (and even there entrance effects, to be discussed later this chapter, confuse the issue). We believe that the mathematical expressions developed in Chapter 2 are applicable in the distorted laminar regime, because we believe that the weak turbulence doesn't penetrate significantly into the boundary layer, and because we have some experimental evidence [49, 50 that laminar boundary-layer mathematics predicts phenomena accurately. Everywhere else in $\mathbf { F i g . }$ ${ \mathfrak { b } } . 3 ,$ our present understanding is too incomplete to give complete, quantitatively accurate predictions.

However, in the fully turbulent regime, Iguchi's hypothesis gives partial, quantitatively accurate guidance. In this regime, the displacement amplitude $\left| x _ { 1 } \right|$ of the gas is much larger than both $\delta _ { \nu }$ and $\scriptstyle { R , }$ so Iguchi [47]. suggested that the flow at any instant of time should have little memory of its past history:' The flow at each instant of time should be identical to that of fully developed steady flow with that same velocity, represented by Fig. 5.2. This hypothesis must be excellent in the low frequency limit, in which $R / \delta _ { \nu } \longrightarrow 0 _ { ; }$ , a limit that is approached in the inertances of many pulse-tube refrigerators. We do not know how good the assumption is for large $R / \delta _ { \nu }$ , which is of interest in many resonators.

To incorporate Iguchi's hypothesis into the impedance framework of Chapter ${ \mathfrak { L } } ,$ we can derive an expression for $d p _ { 1 } / d x ,$ modified to account for the turbulence. If the volumetric velocity and hence Reynolds number $N _ { R }$ vary sinusoidally in time, then the instantaneous friction factor $f _ { M } ( t )$ obtained from Fig. 5.2 has a complicated time dependence. We can simplify this time dependence by using a Taylor-series expansion around the peak Reynolds number:

$$
f _ { M } ( t ) \simeq f _ { M } + \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { p e a k } } \left( \frac { \left| \mathrm { R e } \left[ U _ { 1 } e ^ { i \omega t } \right] \right| } { \left| U _ { 1 } \right| } - 1 \right) ,\tag{5.11}
$$

where $f _ { M }$ and the derivative on the right-hand side are evaluated at the peak Reynolds number. It is then straightforward to integrate the instantaneous power dissipation over a full cycle, obtaining for the time-averaged dissipation of acoustic power per unit length

$$
\frac { d \dot { E } _ { 2 } } { d x } = \frac { \rho \left| U _ { 1 } \right| ^ { 3 } } { 3 \pi ^ { 3 } R ^ { 5 } } \left[ f _ { M } - \left( 1 - \frac { 9 \pi } { 3 2 } \right) N _ { R , \mathrm { p e a k } } \frac { d f _ { M } } { d N _ { R } } \right] ,\tag{5.12}
$$

where, again, $f _ { M }$ and $d f _ { M } / d N _ { R }$ are evaluated at the peak Reynolds number.

When this is compared to the equivalent result for laminar flow

$$
\frac { d \dot { E } _ { 2 } } { d x } = \frac { \rho \left| U _ { 1 } \right| ^ { 2 } \omega } { 2 \pi R ^ { 2 } } \mathrm { R e } \left[ \frac { i } { 1 - f _ { \nu } } \right] ,\tag{5.13}
$$

it is apparent that turbulence multiplies the power dissipation and the effective viscous resistance per unit length, $\mathbf { \Delta } _ { r _ { \nu } } ,$ by a factor m given by the ratio of the two expressions above:

$$
m = \frac { \delta _ { \nu } ^ { 2 } N _ { R } } { 6 \pi R ^ { 2 } } \frac { \left[ f _ { M } - \left( 1 - 9 \pi / 3 2 \right) N _ { R , \mathrm { p e a k } } d f _ { M } / d N _ { R } \right] } { \mathrm { R e } \left[ i / \left( 1 - f _ { \nu } \right) \right] } .\tag{5.14}
$$

We can evaluate $f _ { M }$ and $d f _ { M } / d N _ { R }$ as a function of $N _ { R }$ and $\varepsilon$ directly from Fig. 5.2, or by using the iterative expression

$$
\frac { 1 } { \sqrt { f _ { M } } } = 1 . 7 4 - 2 \log _ { 1 0 } \left( 2 \varepsilon + \frac { 1 8 . 7 } { N _ { R } \sqrt { f _ { M } } } \right) ,\tag{5.15}
$$

which is a remarkably good approximation to the friction factor [51].

At low enough velocities, $m \longrightarrow 1$ and the flow is laminar. According to Eq. (5.14), the $m = 1$ boundary between laminar and turbulent zones occurs roughly at

$$
N _ { R , \mathrm { p e a k } } ~ \simeq ~ 2 0 0 0 \mathrm { f o r } R / \delta _ { \nu } < 2 ,\tag{5.16}
$$

$$
\frac { N _ { R , \mathrm { p e a k } } } { R / \delta _ { \nu } } \simeq 1 0 0 0 \mathrm { f o r } R / \delta _ { \nu } > 2 ,\tag{5.17}
$$

which is in general agreement with the transitions from laminar or weakly laminar to transitional or conditionally turbulent in Fig. 5.3.

Turbulence must also affect the other parts of the impedance picture of Chapter 2: the inertance per unit length l, the compliance per unit length $\pmb { c } ,$ the thermal-relaxation resistance $\boldsymbol { r } _ { \kappa } ,$ and the source/sink factor e. As turbulence increases $\mathbf { \Delta } _ { T _ { v } , \mathrm { ~ ~ } }$ it probably changes the average velocity gradient at the wall, so the boundary-layer thickness probably changes, changing the effective area in the center of the duct that is available to carry the plug flow responsible for most of the inertance. Turbulence must also allow the influence of the isothermal boundary condition at the wall to reach farther into the gas, making more of the channel appear isothermal and hence increasing c. With more volume affected by thermal relaxation, $\mathbf { \Delta } ^ { \bullet } \mathbf { \kappa }$ probably decreases, and e may increase.

This analysis does not inspire confidence. Experimental confirmation exists only for $\mathbf { \nabla } _ { \pmb { r } _ { \nu } }$ [47], and only in a limited regime. Even in the fully turbulent regime, where Iguchi's hypothesis is most credible, we have no expression for $\dot { H } _ { 2 }$ and only qualitative ideas of the corrections to inertance, compliance, and thermal-relaxation resistance. Experiments and more careful analysis are clearly needed to improve the situation. Accurate estimates or experiments are needed for $u _ { 1 } ( y )$ and $\mathcal { T } _ { 1 } ( y )$ in and near the boundary layer.

## 5.2.1. Minor losses

In flow at high Reynolds number, additional pressure drops are associated with the transitions between channels, and with changes in direction of channels. These effects are known as "minor losses" because in long piping systems such transitions are indeed minor contributors to overall pressure drop. However, in thermoacoustic engines and refrigerators operating at high amplitudes, these so-called minor losses can be major, as in the traveling-wave engine of Figs. 1.13 and 1.14, where minor losses are severe in the tee and in the $1 8 0 ^ { \circ }$ and $9 0 ^ { \circ }$ bends.

![[mu_ad18d396_d19d982894d1f0ef9d72.jpg]]  
Figure 5.4: Typical chart giving minor loss coefficient K. Reproduced from Fox and Mc-Donald [27].

For steady flow, the pressure drop arising from minor losses is characterized by the dimensionless minor-loss coefficient $\kappa ,$

$$
\Delta p = K \frac { 1 } { 2 } \rho u ^ { 2 } = K \frac { \rho U ^ { 2 } } { 2 A ^ { 2 } } ,\tag{5.18}
$$

with K tabulated for a wide variety of geometries [51, 52], as illustrated in Fig. 5.4. These losses arise from turbulence and other types of "secondary" flow, as illustrated in Figs. 5.5 and 5.6.

For flow of such high amplitude that the displacement amplitude $\lvert x _ { 1 } \rvert$ is far larger than all other dimensions in the vicinity, Iguchi's hypothesis should be applicable: We can assume that Eq. (5.18) holds at each instance of time-dependent flow, so that

$$
\Delta p ( t ) = \frac { K } { 2 A ^ { 2 } } \rho ( t ) \left[ U ( t ) \right] ^ { 2 } .\tag{5.19}
$$

Using sinusoidal velocity

$$
U ( t ) = | U _ { 1 } | \sin \omega t\tag{5.20}
$$

and constant $\rho ,$ we can quickly calculate the fundamental Fourier component of $\Delta p ( t )$

$$
| \Delta p _ { 1 } | = \frac { 4 } { 3 \pi } \frac { K \rho _ { m } } { A ^ { 2 } } | U _ { 1 } | ^ { 2 }\tag{5.21}
$$

and the acoustic power dissipated by minor loss in the gas,

$$
\Delta \dot { E } _ { 2 } = \overline { { \Delta p ( t ) U ( t ) } } = \frac { 2 } { 3 \pi } \frac { K \rho _ { m } } { A ^ { 2 } } \left| U _ { 1 } \right| ^ { 3 } .\tag{5.22}
$$

Hence, in the impedance viewpoint of Chapter 2 we can assign a viscous flow resistance

$$
R _ { \nu } = \frac { 4 } { 3 \pi } \frac { K \rho _ { m } } { A ^ { 2 } } \left| U _ { 1 } \right|\tag{5.23}
$$

![[mu_ad18d396_c7e60e5dccdaa2487671.jpg]]

![[mu_ad18d396_0aabaff244c988310621.jpg]]  
Figure 5.5: Illustrations of turbulent eddies at abrupt expansions and contractions. Reproduced from Idelchik [52].

![[mu_ad18d396_c90ed312cfb1af5eaa68.jpg]]  
Figure 5.6: Illustrations of turbulent losses and dissipation at unions and in an elbow. Reproduced from Idelchik [52].

to each minor-loss location, if we can take K to be independent of velocity. In the DeltaE file for the traveling-wave engine included in the Appendix, many such minor-loss resistances are included, using Idelchik's extensive tabulations [52] of $\kappa .$

This type of nonlinear flow, with an amplitude-dependent resistance, is also present in the orifice (typically an adjustable valve) 'of an orifice pulse-tube refrigerator. Handbooks give typical values for the dimensionless head-loss coefficient K for valves and fittings, but American valve manufacturers usually specify a valve's flow impedance by $C _ { V }$ .Although catalogs give values for $C _ { V }$ without units, it. is not a dimensionless number: $C _ { V }$ is defined by the equation

$$
\Delta p = \rho U ^ { 2 } / C _ { V } ^ { 2 }\tag{5.24}
$$

for steady flow, using gallons per minute, pounds per square inch, and $\mathrm { \ g m } / \mathrm { c m } ^ { 3 }$ for $\displaystyle \boldsymbol { U } , \boldsymbol { \Delta p } ,$ and $\pmb { \rho }$ respectively, so $C _ { V }$ has units of

$$
\frac { \mathrm { g a l } } { \mathrm { m i n } } \sqrt { \frac { \mathrm { g m / c m ^ { 3 } } } { \mathrm { p s i } } } ,\tag{5.25}
$$

which is a unit of area equal to $2 4 \times 1 0 ^ { - 6 }$ m². The use of $C _ { V }$ instead of K in valve catalogs eliminates ambiguity about whether the area A appearing in Eq. (5.18) is the inside diameter of the pipes entering the valve, the smallest cross section inside the valve itself, or the "nominal" pipe size of the valve. To convert between $K , C _ { V _ { \bf 3 } }$ and $\scriptstyle { \mathcal { R } } _ { \nu }$ for steady flow, use any of

$$
K \ = \ \frac { 2 A ^ { 2 } } { [ ( 2 4 \times 1 0 ^ { - 6 } \mathrm { m } ^ { 2 } ) C _ { V } ] ^ { 2 } } ,\tag{5.26}
$$

$$
R _ { \nu } ~ = ~ { \frac { \rho U } { [ ( 2 4 \times 1 0 ^ { - 6 } \mathrm { m } ^ { 2 } ) C _ { V } ] ^ { 2 } } } = { \frac { \sqrt { \rho \Delta p } } { [ ( 2 4 \times 1 0 ^ { - 6 } \mathrm { m } ^ { 2 } ) C _ { V } ] } } ,\tag{5.27}
$$

$$
R _ { \nu } = \frac { K \rho U } { 2 A ^ { 2 } } = \sqrt { \frac { K \rho \Delta p } { 2 A ^ { 2 } } } ;\tag{5.28}
$$

for sinusoidal flow, use any of

$$
K \ = \ \frac { 2 A ^ { 2 } } { \left[ ( 2 4 \times 1 0 ^ { - 6 } \mathrm { m } ^ { 2 } ) C _ { V } \right] ^ { 2 } } ,\tag{5.29}
$$

$$
R _ { \nu } ~ = ~ \frac { 8 \rho _ { m } \left| U _ { 1 } \right| } { 3 \pi \left[ ( 2 4 \times 1 0 ^ { - 6 } \mathrm { m } ^ { 2 } ) C _ { V } \right] ^ { 2 } } = \frac { \sqrt { 8 \rho _ { m } \left| \Delta p _ { 1 } \right| / 3 \pi } } { \left[ ( 2 4 \times 1 0 ^ { - 6 } \mathrm { m } ^ { 2 } ) C _ { V } \right] } ,\tag{5.30}
$$

$$
R _ { \nu } ~ = ~ \frac { 4 K \rho _ { m } \left| U _ { 1 } \right| } { 3 \pi A ^ { 2 } } = \sqrt { \frac { 4 K \rho _ { m } \left| \Delta p _ { 1 } \right| } { 3 \pi A ^ { 2 } } } .\tag{5.31}
$$

. We hope that Eq. (5.23) and its variants incorporate the most important features of minor losses for thermoacoustics, but our understanding is very incomplete.. When minorloss locations are close together, such as the tee and elbow of Fig. 1.13, we do not know how their minor-loss phenomena interact, so we do not. know what effective $\scriptstyle { \mathcal { R } } _ { \nu }$ to assign. Sometimes we know that minor losses are large even when $\left| x _ { 1 } \right|$ is small enough that Iguchi's hypothesis may not be applicable and hence Eq. (5.23) is questionable. We do not know whether to assign to each minor-loss location some correction for inertance, compliance, or thermal-relaxation resistance in addition to the correction to viscous resistance given by Eq. (5.23). When both $U ( t )$ and $\Delta p ( t )$ contain harmonics, Eq. (5.23) is much too simple.

![[mu_ad18d396_eb1f47db6e19970afeb4.jpg]]  
Figure 5.7: Illustration of entrance effects for steady laminar flow, from [27]. The flow has its "fully developed" parabolic profile only at distances greater than $L _ { e n t r }$ downstream of the entrance to the channel; at shorter distances, the flow retains memory of its condition upstream of the entrance.

## 5.3. Entrance effects and joining conditions

One of the unspoken assumptions of our acoustic approximation is that the gas displacement amplitude $\left| x _ { 1 } \right|$ is much smaller than all other relevant dimensions in the x direction. This assumption is violated in thermoacoustic engines and refrigerators operating high amplitudes, where the displacement amplitude is typically comparable to the entire length of heat exchangers and may be one-tenth of the length of the stack

## 5.3.1. Entrance effects

Figure 5.7 illustrates one aspect of this situation for steady flow. Flow enters a channel from wide open space to the left with a flat velocity profile. It takes time for viscosity to diffuse the influence of the zero-velocity boundary condition at the wall into the flow, and time is equivalent to distance along the flow. For laminar flow, the entrance length [27] is given by

$$
L _ { e n t r } \simeq 0 . 0 6 N _ { R } D .\tag{5.32}
$$

To our knowledge, this phenomenon has not been carefully investigated for oscillating flow. However, a rough estimate is very illuminating. Let us assume that the entrance length for oscillating laminar flow is comparable to that for steady laminar flow. Then with

$$
D = 4 r _ { h } ,\tag{5.33}
$$

$$
N _ { R , \mathrm { p e a k } } = \frac { \rho \left| \boldsymbol { u } _ { 1 } \right| D } { \mu } = \frac { 8 r _ { h } \left| \boldsymbol { x } _ { 1 } \right| } { \delta _ { \nu } ^ { 2 } } ,\tag{5.34}
$$

$$
\left| x _ { 1 } \right| = \left| U _ { 1 } \right| / \omega A ,\tag{5.35}
$$

we have

$$
L _ { e n t r } \simeq 2 \left( \frac { r _ { h } } { \delta _ { \nu } } \right) ^ { 2 } \left| x _ { 1 } \right| .\tag{5.36}
$$

Hence, in a stack where typically $\dot { r _ { h } } \sim \delta _ { \nu } ,$ the entrance length is of the order of the displacement amplitude. At the 10% pressure amplitudes typical of the standing-wave engine of Figs. 1.9 and 1.10, roughly 10% of the length of the stack may be affected. In this region, the assumptions underlying all the derivations of Chapter 2 and 3 are violated.

## 5.3.2. Joining conditions

Some thermoacoustic computation algorithms have used continuity of complex pressure amplitude ${ \pmb p _ { 1 } } ,$ complex volumetric velocity amplitude $U _ { \mathbf { 1 } } .$ , and mean gas temperature ${ \mathcal { T } } _ { m }$ as "joining conditions," i.e., boundary conditions to match solutions across the interface between two adjacent thermoacoustic components. For example, DeltaE [20] has used these joining conditions to pass from the end of one segment to the beginning of the next. There are many situations for which we already know that these.traditional acoustic joining conditions may be inadequate. We saw above that continuity of ${ \pmb p } _ { 1 }$ is inappropriate if minor losses are important. Storch et al. [53] observed a distorted temperature profile near the ends of a pulse tube, as shown in Fig. 5.8, which we will attribute to an effective mismatch in $\mathbf { { \mathcal { T } } _ { m } }$ between the end of the pulse tube and the adjacent heat exchanger. Swift [54] observed a similar discontinuity in $T _ { m }$ between a hot heat exchanger and the adjacent duct in a standing-wave engine; the discontinuity in $T _ { m }$ was proportional to $\left| p _ { 1 } \right|$ . As a hypothetical example, consider two adjacent heat exchangers, with separation (along the direction of oscillatory gas motion) much less than the gas displacement amplitude, and each having plate spacing much smaller than the thermal penetration depth $\delta _ { \kappa } .$ If the two heat exchangers are at equal temperatures, then $U _ { 1 }$ is continuous across the interface between them. However, if the temperatures of the two heat exchangers differ by $\delta \mathcal { T } _ { \dot { m } } ,$ continuity of first-order mass flux $\rho _ { m } U _ { 1 }$ (with $\rho _ { m }$ the mean gas density) more accurately describes flow across the interface. Hence, $U _ { 1 }$ is discontinuous, with $\delta \left| U _ { 1 } \right| \sim \left| U _ { 1 } \right| \delta T _ { m } / T _ { m }$

As an alternative to continuity of $U _ { 1 }$ , Rott [55, 14] proposed continuity of

$$
\psi _ { 1 } = \frac { \omega } { i } \exp \left[ - \int \frac { \left( f _ { \kappa } - f _ { \nu } \right) d T _ { m } } { \left( 1 - \sigma \right) \left( 1 - f _ { \nu } \right) T _ { m } } \right] U _ { 1 } .\tag{5.37}
$$

The plausibility of $\psi _ { 1 }$ as a joining variable is easily examined for some simple cases. For example, Eq. (5.37) becomes

$$
\psi _ { 1 } = { \frac { \omega } { i } } \left[ 1 - \int { \frac { f _ { \kappa } d T _ { m } } { T _ { m } } } \right] U _ { 1 }\tag{5.38}
$$

for an inviscid ideal gas, if the integral is much smaller than unity. Then, in the adiabatic limit $( f _ { \kappa } \longrightarrow 0 )$ of traditional acoustics, continuity of $\psi _ { 1 }$ and of $U _ { 1 }$ are identical, so the $\psi _ { 1 }$

![[mu_ad18d396_481bc19fa6d616a8f31c.jpg]]  
Figure 5.8: Temperature profile in the pulse tube of a pulse tube refrigerator, reproduced from Storch et al. [53]. Naively one might expect a smooth profile, without the overshoots at the ends, whose magnitude is of the order of the adiabatic temperature oscillation amplitude.

joining condition reduces to the traditional acoustic $U _ { \mathbf { 1 } }$ joining condition. In contrast, in the isothermal limit $( f _ { \kappa } \longrightarrow 1 )$ , Eq. (5.38) becomes

$$
\psi _ { 1 } = \frac { \omega } { i } \left[ 1 + \frac { \delta \rho _ { m } } { \rho _ { m } } \right] U _ { 1 } ,\tag{5.39}
$$

so that in this case continuity of $\psi _ { 1 }$ and of first-order mass flux $\rho _ { m } U _ { 1 }$ are identical. As we argued in the preceding paragraph, this is the correct joining condition between two heat exchangers at different temperatures, with plate spacing $\ll \delta _ { \kappa }$

Although continuity of $\psi _ { 1 }$ appears plausible in these two limiting situations, we do not believe that it is generally correct. To demonstrate this, we will derive joining conditions for the interface between an isothermal space $( f _ { \kappa } = 1$ , such as a good heat exchanger) and an adiabatic space $( \mathcal { f } _ { \kappa } = 0$ , such as a pulse tube, thermal buffer tube, or resonator duct), as shown in Fig. 5.9. We seek expressions for the discontinuities to lowest order, hence we seek a first-order expression for $\delta T _ { m }$ and second-order expressions for $\delta { U _ { 1 } }$ and $\delta p _ { 1 }$ . We will assume that flow in the adiabatic space is stratified, as it would be for a pulse tube or buffer tube with adequate flow straightening (see “Jet-driven streaming" below).

## Mean temperature

Following Smith and Romm [56] (see also Kittel [57]), consider the interface, illustrated in Fig. 5.9, between an isothermal heat exchanger at temperature To and an open space $\mathcal { T } _ { 0 }$ in which the gas is stratified (such an ideal pulse tube). Neglect viscosity, and let the frequency be low so that the acoustic wavelength is much larger than any other distance of interest. Suppose that pistons or other external means cause the mass flux (positive to the right) across the interface at $\pmb { x } = 0$ to be exactly ω $M _ { a }$ sinωt and the pressure to be exactly $\mathcal { P } _ { m } + \left| \boldsymbol { p } _ { 1 } \right|$ sin (ωt - θ). Assume that the gas displacement amplitude is much greater than $\delta _ { \kappa } .$

(a)  
![[mu_ad18d396_6a8b8a385d5f4f5a6bac.jpg]]  
(b)

![[mu_ad18d396_e8d83f762254d1c9a8a1.jpg]]

(c)  
![[mu_ad18d396_1f8ee97b7bb1f8eac56a.jpg]]  
Figure 5.9: A guide to the discussion of joining conditions. (a) The geometry under consideration. The interface between an isothermal heat. exchanger (left) and an adiabatic duct (right) of area A is at $\boldsymbol { x } = 0$ , with x increasing to the right. In the duct, the peak-to-peak gas displacement is $2 \left| U _ { 1 } \right. \left/ \omega A \right.$ . Locations $" \mathbb { L } ^ { \mathfrak { s } }$ and $\mathfrak { s e } \mathfrak { s }$ are just to the left and right, respectively, of the interface. (b) For $\theta = 9 0 ^ { \circ }$ , the gas motion is essentially that of a standing wave, with pressure and displacement in phase. The "particular" slice of gas has both ${ \pmb x } ( t )$ and $T ( t ) - T _ { 0 }$ proportional to 1 - cos $\omega t .$ . The heavy line shows $\mathcal { T } ( t )$ vs ${ \pmb x } ( t )$ for this slice. Slices to the.right of the "particular" slice have similar $\boldsymbol { \mathcal { T } } ( t )$ vs ${ \pmb x } ( t )$ traces, shown as parallel lines. Slices to the left follow a portion of the "particular" slice's line while $x ( t ) > 0$ , and have $\mathcal { T } \equiv \mathcal { T } _ { 0 }$ while $x ( t ) < 0$ . (c) For $\theta = 0$ , the gas motion is essentially that of a traveling wave, with pressure and velocity in phase. The “particular" slice of gas has $x ( t )$ ∝ 1 - cosωt and $T ( t ) - T _ { 0 }$ ∝ sin $\omega t .$ The heavy ellipse shows $T ( t )$ vs ${ \pmb x } ( t )$ for this slice. Slices to the right of the "particular" slice follow similar $T ( t )$ vs $x ( t )$ ellipses; slices to the left follow truncated ellipses while $x ( t ) > 0$ and $\mathcal { T } \equiv \mathcal { T } _ { 0 }$ while $x ( t ) < 0$ . In' both (b) and $( \mathsf { c } )$ , the resulting Eulerian $\mathcal { T } _ { m } ( x )$ is shown as the solid curve; extrapolating it from large x to $\pmb { x = 0 }$ gives the effective discontinuity $\delta T _ { m }$ in mean temperature.

Because the gas in the open cylinder is stratified, we can (in principle) follow each differential slice of gas dM as it moves, considering its temperature, position, etc. as functions of time t. We begin by considering $T ( t )$ for the slice of gas that is at $x = 0 \mathrm { ~ a t ~ } t = 0$ . This particular slice touches the heat exchanger only at $t = 0 ;$ slices to the right of it never touch the heat exchanger; slices to the left of it spend a nonzero fraction of their time inside the heat exchanger. $\mathbf { A } \mathbf { t } \ t = 0 ,$ this particular slice has temperature $T _ { \mathbf { 0 } } ,$ because at that moment it is in thermal contact with the heat exchanger. Thereafter, its temperature evolves adiabatically in response to the changing pressure:

$$
T ( t ) = T _ { 0 } \left[ \frac { p _ { m } + \left| p _ { 1 } \right| \sin \left( \omega t - \theta \right) } { p _ { m } - \left| p _ { 1 } \right| \sin \theta } \right] ^ { ( \gamma - 1 ) / \gamma } .\tag{5.40}
$$

To first order in $p _ { 1 } , \mathtt { E q }$ (5.40) becomes

$$
T ( t ) = T _ { 0 } \left\{ 1 + \frac { \gamma - 1 } { \gamma } \frac { \left| p _ { 1 } \right| } { p _ { m } } \left[ \sin { \left( \omega t - \theta \right) } + \sin { \theta } \right] \right\} .\tag{5.41}
$$

Meanwhile, the position of that slice of gas is

$$
x ( t ) = \frac { M _ { a } } { \rho _ { m } A } \left( 1 - \cos \omega t \right) = \frac { \left| \boldsymbol { U } _ { 1 } \right| } { \omega A } \left( 1 - \cos \omega t \right)\tag{5.42}
$$

to first order, where A is the cross-sectional area of the open space. The path $\scriptstyle { \mathcal { T } } ( x )$ traced out by this particular slice of gas is shown as the heavy solid line with attached arrowheads in Figs. 5.9(b) and ${ \mathfrak { s } } . 9 ( { \mathfrak { c } } )$ for two choices of θ. Its average temperature is $T _ { 0 } + \left[ \left( \gamma - 1 \right) \left| p _ { 1 } \right| / \gamma p _ { m } \right] T _ { 0 }$ sin $\theta ,$ and its average location is $\left| U _ { 1 } \right| / \omega A .$

Slices of gas to the right of the particular slice essentially share its oscillating motion and oscillating temperature, but with. different average values. For $x > 2 \left| U _ { 1 } \right| / \omega A$ , the slope of their average temperatures $d T _ { m } / d x$ is determined by phenomena outside the scope of this paper (such as heat conduction in the gas). Slices of gas to the left of the particular slice we have considered have complicated temperature histories, with constant temperatures for times when $x ( t ) < 0$ , and temperatures evolving according to trigonometric functions of t (to first order) when $x ( t ) > 0$ The net effect of all such slices is to produce an average temperature profile $T _ { m } ( x )$ shown in Figs. 5.9(b) and $5 . 9 ( \mathrm { c } )$ , which is unremarkable for $x > 2 \left. \ 7 _ { 1 } \right. / \omega A$ but which is rather complicated for $0 < x < 2 | U _ { 1 } | / \omega A$ Experimental evidence of such complicated ${ \mathcal { T } } _ { m } ( x )$ in a pulse tube is shown in Fig. 5.8.

A suitable joining condition for $T _ { m }$ would allow convenient matching of the $\pmb { x } < 0$ and $x > 2 \left| U _ { 1 } \right| / \omega A$ solutions, each extrapolated to ${ \pmb x } = 0 .$ Examination of Figs. 1(b) and 1(c) shows that this occurs if Tm is given a discontinuity δTm $T _ { m }$ $\delta T _ { m }$ at $\pmb { x = 0 }$

$$
T _ { m , R } - T _ { m , L } = \delta T _ { m } = T _ { m } \frac { \gamma - 1 } { \gamma } \frac { | p _ { 1 } | } { p _ { m } } \sin \theta - \frac { | U _ { 1 } | } { \omega A } \frac { d T _ { m } } { d x } .\tag{5.43}
$$

The discontinuity is first order in the acoustic amplitudes, and it can have either sign. Equation (5.43) is in reasonable agreement with the measurements of Storch [53] (as far as I can tell) and Swift [54].

It turns out that Eq. (5.43) works whether the open cylinder is on the right [as in Fig. $1 ( a ) ]$ or on the left, as long as these conventions are followed: θ is the angle by which $U _ { 1 }$ leads $p _ { 1 } , U _ { 1 }$ is positive in the +x direction, and $d T _ { m } / d x$ is positive if $\scriptstyle { { \mathcal { T } } _ { m } }$ increases with x.

## Oscillating volumetric velocity

To deduce a suitable joining condition for volumetric velocity, we must consider in more detail the slices to the left of the “particular" slice of the previous section. We label each such slice by $\pmb { t } ^ { * } ,$ the time at which it crosses $\boldsymbol { x } = \dot { 0 }$ from right to left; thus $\pi \leq \omega t ^ { * } \leq 2 \pi$ includes all slices, and the “particular" slice of the previous section has $\omega t ^ { * } = 2 \pi$ Each slice crosses ${ \pmb x } = { \bf 0 }$ from left to right at time ${ { t } ^ { * * } }$ given by $\omega t ^ { * * } = 2 \pi - \omega t ^ { * }$ . While each slice enjoys adiabatic conditions at $\pmb { x } > 0 .$ , its pressure changes from $p _ { m } + | p _ { 1 } |$ sin $( 2 \pi - \omega t ^ { * } - \theta )$ to $p _ { m } \mathrm { + } \vert p _ { 1 } \vert \sin { ( \omega t ^ { \ast } - \theta ) }$ , a net pressure change of 2p1 cos θ sin ωt\*. Hence, just before that slice enters the heat exchanger, its temperature is $T _ { 0 } \left\{ 1 + 2 \left[ \left( \gamma - 1 \right) \left| p _ { 1 } \right| / \gamma p _ { m } \right] \right.$ cOs $\theta \sin \omega t ^ { * } \}$ . As it enters the heat exchanger, returning to temperature ${ \mathcal { T } } _ { 0 } ,$ its volume $d M / \rho _ { m }$ changes abruptly by $- 2 \left[ \left( \gamma - 1 \right) \left| p _ { 1 } \right| / \gamma p _ { m } \right]$ cos θ sin ωt\* $d M / \rho _ { m }$ The discontinuity in volumetric velocity is obtained by dividing by $\ b { d t ^ { * } }$

$$
\begin{array} { l } { { \delta U ( t ^ { * } ) ~ = ~ 2 { \frac { \gamma - 1 } { \gamma p _ { m } } } { \frac { \omega M _ { a } } { \rho _ { m } } } | p _ { 1 } | \cos \theta \sin ^ { 2 } \omega t ^ { * } , \qquad \pi \leq \omega t ^ { * } \leq 2 \pi } } \\ { { \delta U ( t ^ { * } ) ~ = ~ 0 , \qquad 0 \leq \omega t ^ { * } \leq \pi } } \end{array}\tag{5.44}
$$

The fundamental Fourier component of this function of ${ { t } ^ { * } }$ is

$$
\begin{array} { l l l } { { \delta U ( t ) } } & { { \cong } } & { { \displaystyle - \frac { 8 } { 3 \pi } \frac { ( \gamma - 1 ) } { \gamma p _ { m } } \frac { \omega M _ { a } } { \rho _ { m } } \left| p _ { 1 } \right| \cos \theta \sin \omega t } } \\ { { \mathrm { } } } & { { = } } & { { \displaystyle - \frac { 8 } { 3 \pi } \frac { ( \gamma - 1 ) } { \gamma p _ { m } } \left| p _ { 1 } \right| \left| U _ { 1 } \right| \cos \theta \sin \omega t . } } \end{array}\tag{5.45}
$$

Hence, the discontinuity of volumetric velocity contains a Fourier component at frequency $\omega ;$ we may correctly refer to it as $\delta { U _ { 1 } }$ . This discontinuity is in phase with the volumetric velocity itself, so there is no discontinuity in the phase of $U _ { 1 }$ . The discontinuity in $| \bar { U } _ { 1 } |$ is

$$
\begin{array} { r c l } { { \displaystyle \left| U _ { 1 } \right| _ { R } - \left| U _ { 1 } \right| _ { L } } } & { { = } } & { { \displaystyle \delta \left| U _ { 1 } \right| = - \frac { 8 } { 3 \pi } \frac { \gamma - 1 } { \gamma } \frac { \left| p _ { 1 } \right| \left| U _ { 1 } \right| } { p _ { m } } \cos \theta } } \\ { { } } & { { = } } & { { \displaystyle - \frac { 1 6 } { 3 \pi } \frac { \gamma - 1 } { \gamma } \frac { \dot { E } _ { 2 } } { p _ { m } } } } \end{array}\tag{5.46}
$$

(5.47).

where $\dot { E } _ { 2 } = \frac { 1 } { 2 } \left| p _ { 1 } \right| \left| U _ { 1 } \right|$ cos θ is the acoustic power. This expression may be used whether the open cylinder is on the right or on the left, as long as $\dot { E } _ { 2 }$ is taken to be positive when power flows in the +x direction. Note that $\delta \left| \bar { U } _ { 1 } \right|$ is second order in the acoustic amplitudes, and it is zero for standing-wave phasing. Hence, it larger for pulse-tube and Stirling refrigerators than for low-amplitude standing-wave thermoacoustic engines and refrigerators.

The overall form of Eq. (5.46) is not surprising. In the geometry under consideration, there is a volume of order $| U _ { 1 } | / \omega$ in the open cylinder,, adjacent to the heat exchanger, that might naively be considered adiabatic; in fact, the gas occupying this volume behaves as near to isothermally as to adiabatically. Hence, its response to changing pressure must be corrected in rough proportion to the difference between the adiabatic and isothermal compressibilities:

$$
\delta V \sim \frac { \vert U _ { 1 } \vert } { \omega } \vert p _ { 1 } \vert \left( \frac { 1 } { \gamma p _ { m } } - \frac { 1 } { p _ { m } } \right) .\tag{5.48}
$$

With multiplication by $\omega$ to convert from $\delta V$ to $\delta \left| U _ { 1 } \right|$ , and by cos $\pmb \theta$ to eliminate the effect for standing-wave phasing, we recover the form of Eq. (5.46).

Note that $\theta = 0$ and $d T _ { m } / d x = 0$ makes $\delta T _ { m } = 0$ in Eq. (5.43). In that case, examination of Eq. (5.37) or (5.38) shows that continuity of $\psi _ { 1 }$ implies continuity of $U _ { 1 }$ , yet Eq. (5.45) or (5.46) shows a maximum (with respect to $\theta )$ discontinuity in $| U _ { 1 } |$ . Hence, the joining condition derived here is fundamentally different from continuity of $\psi _ { 1 }$ . We suspect these two joining conditions are applicable in different circumstances.

## Oscillating pressure

Consistent with the previous section, we might expect a pressure discontinuity

$$
\delta p \sim U _ { 1 } \delta U _ { 1 }\tag{5.49}
$$

at the interface, due to the $( \mathbf { v } \cdot \nabla ) \mathbf { v }$ term in the momentum equation. Since this pressure discontinuity would apparently be third order in the acoustic amplitude, we will neglect it.

## Acoustic power dissipation and entropy generation

With spatially uniform oscillatory pressure, the discontinuity in volumetric velocity causes a third-order dissipation of acoustic power

$$
\begin{array} { r c l } { { \delta \dot { \vec { E } } _ { 2 } } } & { { = } } & { { \dot { \vec { E } } _ { 2 , L } - \dot { \vec { E } } _ { 2 , R } = \displaystyle \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } p ( t ) \delta \left| U _ { 1 } \right| \sin \omega t d ( \omega t ) } } \\ { { } } & { { = } } & { { \displaystyle \frac { 4 } { 3 \pi } \frac { \gamma - 1 } { \gamma p _ { m } } \left| p _ { 1 } \right| ^ { 2 } \left| U _ { 1 } \right| \cos ^ { 2 } \theta . } } \end{array}\tag{5.50}
$$

Naturally, this expression is never negative. It represents an inherent irreversibility at such an interface due to irreversible heat transfer in slices of gas approaching $\boldsymbol { x } = 0$ from the right with temperatures different from $\mathcal { T } _ { 0 }$ . This irreversibility was discussed by Smith and Romm [56] from the point of view of entropy generation. Combining our notation and their results, the interface dissipation per cycle 2π $\bar { \delta E _ { 3 } } / \omega = T _ { 0 } S _ { g e n }$ , where $S _ { g e n }$ is the entropy generation per cycle, obtained from the second law of thermodynamics

$$
S _ { g e n } = \int { S _ { R } } d M - \int { S _ { L } } d M - { \frac { 1 } { T _ { 0 } } } \int d Q\tag{5.51}
$$

where $S _ { R }$ and $S _ { L }$ are the entropies per unit mass just right and left of the interface, and $d Q = c _ { p } ( T _ { R } - T _ { L } )$ dM is the heat absorbed by mass dM crossing the interface. Smith and Romm numerically integrated Eq. (5.51) for a monatomic ideal gas $( \gamma = 5 / 3 )$ , without making the acoustic approximation, and they display a graph of their results as a function of $\pmb \theta$ and $\left. p _ { 1 } \right. / p _ { m }$ Our Eq. (5.50) is indistinguishable from their results at $\left| p _ { 1 } \right| / p _ { m } \sim 0 . 1$ and disagrees with their more accurate results by at most 10% at $\left. p _ { 1 } \right. / p _ { m } \sim 0 . 3$

[An expression similar to Eq. (5.50), but with $\theta = 0$ , was derived incorrectly by Swift [58]. The error in that derivation arises on page 4162, where the equation in the second line should be $\delta S = \delta Q \delta T / 2 T ^ { 2 }$ . This error propagated through that analysis, to Eqs. (27) and (28), which should have been divided by two.]

## Summary

This rather intricate derivation provides higher-order joining conditions between an isothermal channel and a stratified adiabatic channel. It lacks careful experimental confirmation, and it provides no guidance for higher-order joining conditions between other types of channels encountered throughout thermoacoustic engines and refrigerators.

## 5.4. Streaming

In acoustics, the term “streaming" refers to steady velocity that is superimposed on the larger oscillating acoustic velocity [59]. When streaming exists, it is useful to think of the motion of a parcel of gas during each cycle as something like 102 steps forward and 98 steps backward, equivalent to the superposition of a steady drift forward of 4 steps and an oscillating motion with a peak-to-peak amplitude of 100 steps. In thermoacoustic engines and refrigerators, streaming is important because it is a mechanism for convective heat transfer. Carrying heat, streaming can be either an undesirable loss mechanism or an essential heat-transfer method.

Pulse tubes and thermal buffer tubes are usually oriented vertically to avoid gravitydriven convection, which is one form of time-independent velocity superimposed on the oscillating velocity. In this section, we will consider four other undesirable steady flows, which can be called streaming because they are driven by the first-order acoustic phenomena. I will refer to the first two of these as Gedeon streaming and Olson streaming, because David Gedeon [60] and Jeff Olson [49] wrote clear papers on these subjects in the context of engines and refrigerators. Gedeon streaming is a time-averaged mass flux along x through a regenerator, pulse tube, etc. that accompanies $\dot { E } _ { 2 }$ . Olson streaming is a time-averaged toroidal circulation within a pulse tube or thermal buffer tube, driven by boundary-layer effects at the side walls. Jet-driven streaming is a third type, which is also a toroidal circulation within a pulse tube or buffer tube, but which is driven by inadequate flow straightening at an end of the tube. A fourth type, toroidal streaming within a regenerator or stack, presumably might also-occur under some circumstances. These generally undesirable types of streaming are illustrated in Fig. 5.10.

On the other hand, we can deliberately use superimposed steady flow to advantage in some circumstances, to deliberately transfer heat. This steady flow can be either parallel or perpendicular to ${ \pmb x } ,$ as illustrated in Fig. 5.11. The purpose of such flow is to carry heat, which is a second-order quantity in thermoacoustics, so we will think of these flows as second order, refer to them as streaming, and treat them in this section.

To discuss streaming, we extend the perturbation-series expansion of relevant variables one step beyond' the acoustic approximation:

$$
\begin{array} { r } { \xi ( t ) = \xi _ { m } + \mathrm { R e } \left[ \xi _ { 1 } e ^ { i \omega t } \right] + \xi _ { 2 , 0 } + \mathrm { R e } \left[ \xi _ { 2 , 2 } e ^ { 2 i \omega t } \right] . } \end{array}\tag{5.52}
$$

The subscript $^ { 6 6 } 2 , 0 ^ { \dprime }$ identifies the streaming term, which is independent of time. (The second-order oscillating term, which oscillates at 2ω, is of no interest in this section, but will be considered in "Harmonics" below.) The second-order time-averaged mass flux density $\dot { m } _ { 2 , 0 } ( x , y , z )$ is of primary interest, because it: convects a time-averaged heat flux density $\dot { m } _ { 2 , 0 } c _ { p } T$ . As illustrated in Figs. 5.10 and 5.11, the second-order time-averaged mass flow $\begin{array} { r } { \dot { M } _ { 2 } = \int \dot { m } _ { 2 , 0 } d A } \end{array}$ in the x direction may be either zero or nonzero, depending on the circumstances. Gradients in the second-order time-averaged pressure $\scriptstyle { \mathcal { P } } _ { 2 , 0 }$ are also important, and can be either large or small, depending on the impedance of the space through which $\dot { m } _ { 2 , 0 }$ flows.

![[mu_ad18d396_29d5832c941bfa304b28.jpg]]  
Figure 5.10: Illustration of some types of streaming, generally harmful to thermoacoustic engines and refrigerators. Arrows indicate the time-averaged velocity, which is superimposed on the much larger oscillating velocity discussed in Chapter 2. (a) Gedeon streaming. (b) Olson streaming. (c) Jet-driven streaming. (d) Streaming within a regenerator or stack.

![[mu_ad18d396_6eba88256cac4692c418.jpg]]  
Figure 5.11: Illustration of streaming that might be beneficial. Note the elimination of a heat exchanger in each case. (a) Flow parallel to ${ \pmb x } ,$ through a stack or regenerator. (b) Flow perpendicular to ${ \pmb x } ,$ across one end of a stack or regenerator.

## 5.4.1. Gedeon streaming

It is important that the time-averaged mass flow $\dot { M }$ in the x direction through a regenerator, pulse tube, stack, etc. should be near $\tt z e r o ,$ to prevent a large time-averaged convective heat flux $\dot { M } c _ { p } ( T _ { H } - T _ { 0 } )$ or $\dot { M } c _ { p } ( T _ { 0 } - T _ { C } )$ from flowing from hot to cold. In a refrigerator, such a steady energy flux would add an unwanted thermal load to the cold heat exchanger; in an engine, it would wastefully remove high-temperature heat from the hot heat exchanger without creating acoustic power. This type of streaming is illustrated in Fig. 5.10a.

In a traditional orifice pulse-tube refrigerator such as shown in Fig. 1.16 or in something like the standing-wave engine shown in Fig. 1.10, M is exactly zero in steady state operation: Otherwise, mass would steadily accumulate (or deplete, depending on sign) in the dead-end components. This means that every time-averaged term in the perturbation expansion of $\dot { M }$ must be zero; in particular, $\dot { M } _ { 2 } = 0$ in Eq. (5.52). In terms of density and volumetric velocity,

$$
\dot { M } _ { 2 } = \frac { 1 } { 2 } \mathrm { R e } \left[ \rho _ { 1 } \widetilde { U _ { 1 } } \right] + \rho _ { m } U _ { 2 , 0 } .\tag{5.53}
$$

Hence, in a traditional orifice pulse-tube refrigerator or standing-wave thermoacoustic engine or refrigerator, the two terms on the right hand side must turn out to be equal and opposite. The two first-order factors $\pmb { \rho _ { 1 } }$ and $U _ { 1 }$ are “known" from the considerations of Chapter ${ \mathfrak { 2 } } ,$ so setting $\dot { M } _ { 2 } = 0$ in Eq. (5.53) determines what $U _ { 2 , \mathbf { 0 } }$ must be. The second-order time average of the momentum equation,

$$
\omega \rho _ { 1 } \mathbf { v } _ { 1 } { \mathrm { t e r m } } + \rho _ { m } \mathbf { v } _ { 1 } \nabla \mathbf { v } _ { 1 } { \mathrm { t e r m } } = - { \frac { d p _ { 2 , 0 } } { d x } } + r _ { \nu } U _ { 2 , 0 }\tag{5.54}
$$

must also be true, so a nonzero $d p _ { 2 , 0 } / d x$ will generally also exist in a regenerator or stack whenever $\dot { M } _ { 2 } = 0$ through it. It is helpful to think of the $\Delta p _ { 2 , 0 }$ that exists across the regenerator as causing the viscous flow of $U _ { \mathbf { 2 } , \mathbf { 0 } }$ through the regenerator. In a traditional orifice pulse-tube refrigerator, this small time-averaged pressure difference appears automatically, because the topology imposes $\dot { M } _ { 2 } = 0$

However, as shown in Fig. 5.10, any system with the topology of a torus, such as the traveling-wave engine of Fig. 1.14, can have $\dot { M } _ { 2 } \neq 0$ if the two terms on the right side of Eq. (5.53) are not in balance. To estimate how severe the time-averaged convective heat flux carried by such streaming might be in a cryogenic refrigerator if this requirement is ignored, Gedeon [60] showed that

$$
\frac { 1 } { 2 } \mathbb { R } \mathrm { e } \left[ \rho _ { 1 } \widetilde { U _ { 1 } } \right] = \rho _ { m } \dot { \bar { E } } _ { 2 } / p _ { m }\tag{5.55}
$$

in a regenerator, where $\begin{array} { r } { \dot { E } _ { 2 } = \frac { 1 } { 2 } \operatorname { R e } [ p _ { 1 } \widetilde { U _ { 1 } } ] } \end{array}$ is the acoustic power passing through the regenerator. Hence, $\scriptstyle { \frac { 1 } { 2 } } \mathrm { R e } [ \rho _ { 1 } \widetilde { U _ { 1 } } ]$ must be nonzero in traveling-wave engines and refrigerators. Setting

Eq. (5.53) equal to zero shows that efficient regenerator operation requires

$$
U _ { 2 , 0 } = - \frac { 1 } { 2 } \operatorname { R e } \left[ \rho _ { 1 } \widetilde { U _ { 1 } } \right] / \rho _ { m } = - \dot { E } _ { 2 } / p _ { m } .\tag{5.56}
$$

The consequences of ignoring this requirement can be severe indeed. If $\dot { M } _ { 2 } > 0$ , an undesired, streaming-induced heat load

$$
\dot { Q } _ { \mathrm { l o s s } } \sim \dot { M } _ { 2 } c _ { p } \left( T _ { 0 } - T _ { C } \right)\tag{5.57}
$$

flows from ambient to cold through the regenerator. (If $\dot { M } _ { 2 } < 0$ , such heat flows from hot to cold through the pulse tube, with equally harmful effect.) For $U _ { 2 , { \bf 0 } } = { \bf 0 } ;$ the ratio of $\dot { Q } _ { \mathrm { l o s s } }$ to the ordinary regenerator loss $\dot { H } _ { 2 , \mathrm { r e g } }$ is of the order of

$$
\frac { \dot { Q } _ { \mathrm { l o s s } } } { \dot { H } _ { \mathrm { 2 , r e g } } } \sim \frac { \gamma } { \gamma - 1 } \frac { \left( T _ { 0 } - T _ { C } \right) } { T _ { 0 } } \frac { \dot { E } _ { 2 } } { \dot { H } _ { \mathrm { 2 , r e g } } } \sim \frac { \gamma } { \gamma - 1 } \frac { \left( T _ { 0 } - T _ { C } \right) } { T _ { C } } \frac { \dot { Q } _ { C , \mathrm { g r o s s } } } { \dot { H } _ { \mathrm { 2 , r e g } } } ,\tag{5.58}
$$

where $\dot { Q } _ { C , \mathrm { g r o s s } }$ is the gross cooling power, equal to $\dot { E } _ { 2 }$ in the cold heat exchanger [see Chapter 3]. In the final expression in Eq. (5.58), each of the three fractions is > 1 for cryocoolers; hence their product is $\gg 1$ , and the unmitigated streaming-induced heat load would be much greater than the ordinary regenerator loss.

A toroidal topology, such as shown in Fig. 5.10a, ensures that the path integral of $\boldsymbol { \nabla } p$ around the torus must be zero, in order that the pressure p at any location will be uniquely defined. At second order, this means that $\oint \left( d p _ { 2 , 0 } / d x \right) d x = 0$ around the torus. Equation (5.54) shows what $\Delta p _ { 2 , 0 }$ must exist across the regenerator to obtain the desired $U _ { \mathbf { 2 } , \mathbf { 0 } }$ in the regenerator. Hence, we must design the other components of the loop so that their aggregate $\Delta p _ { 2 , 0 }$ is equal and opposite to the $\Delta p _ { 2 , 0 }$ desired across the regenerator.

The desired $\Delta p _ { 2 , 0 }$ can be estimated using the low-Reynolds-number limit of Fig. 7-9 of Kays and London[39]

$$
\frac { d p } { d x } \simeq - \frac { 6 U \mu } { A r _ { h } ^ { 2 } }\tag{5.59}
$$

for the pressure gradient in a screen bed of cross-sectional area A and hydraulic radius $r _ { h } ,$ where $\boldsymbol { U }$ is the volumetric velocity and $\mu$ is the viscosity. (The numerical factor depends weakly on the volumetric porosity of the bed.) With Eq. (5.56) for $\begin{array} { r } { \boldsymbol { U } , } \end{array}$ this yields

$$
\Delta p _ { 2 , 0 } \simeq \frac { 6 } { A r _ { h } ^ { 2 } p _ { m } } \int _ { r e g } \mu _ { m } ( x ) \dot { E } _ { 2 } ( x ) ~ d x\tag{5.60}
$$

for the pressure difference across the regenerator when $\dot { M } _ { 2 } \equiv 0 .$ (The x dependence of the viscosity is due to the temperature gradient.) For the apparatus of Figs. 1.14 and 1.16 and for other traveling-wave systems having $p _ { m }$ of tens of bar and $\left| \boldsymbol { p } _ { 1 } \right| / p _ { m } \sim 0 . 1 , \Delta p _ { 2 , 0 }$ is typically of the order of a few hundred Pa.

In the limit of low viscosity or large tube diameters and in the absence of turbulence, p2,0 would be described by some acoustic version of the Bernoulli equation. This suggests that an acoustically ideal path through the torus from one end of the regenerator to the other would impose across the regenerator a pressure difference of the order of $\Delta \left[ \rho _ { m } u _ { 1 } \widetilde { u _ { 1 } } \right]$ . (Such an ideal loop might include a pulse tube or thermal buffer tube, inertance or transmission line, and compliance, without heat exchangers or other components with small passages.) This pressure difference is typically much smaller than the $\Delta p _ { 2 , 0 }$ given in Eq. (5.60) that is required for $\dot { M } _ { 2 } = 0$ . Hence, to produce the required $\Delta p _ { 2 , 0 }$ , we need an additional physical effect or structure in the torus, relying on turbulence, viscosity, or some other physical phenomenon not included in the Bernoulli equation.

![[mu_ad18d396_3afef7369fd852257e09.jpg]]  
Figure 5.12: Asymmetry of high-Reynolds-number flow at a transistion between' a small tube and wide-open space. (a) For outflow, a jet extends far into the open space, and downstream turbulence dissipates kinetic energy. (b) For inflow with a well-rounded entrance $\mathbf { l i p , }$ there is little dissipation.

Asymmetry in hydrodynamic end effects can produce this required $\triangle p _ { 2 , 0 } .$ . In a tapered transition between a small-diameter tube, where $\left| u _ { 1 } \right|$ is large, and a large-diameter tube, where $\left| u _ { 1 } \right|$ is small, turbulence would be avoided and Bernoulli's equation would hold if the taper were sufficiently gentle. At the opposite extreme, for an abrupt transition, we expect large $\left| u _ { 1 } \right|$ to generate significant turbulence, and further we expect the oscillatory pressure drop across-the transition to exhibit minor losses. Hence, the minor-loss coefficient K depends strongly on the direction of fow through the transition. In the example shown in Fig. 5.12, a small tube is connected to an essentially infinite open space. When the gas (at velocity u inside the tube) flows out of the tube, a jet occurs, and kinetic energy is lost to turbulence downstream of the jet; $K _ { o u t } = 1$ . In contrast, when gas flows into the tube, the streamlines in the open space are widely and smoothly dispersed; $K _ { i n }$ varies from 0.5 to 0.04, with smaller values for larger radius r of rounding of the edge of the entrance. For such asymmetric transitions, we must allow K to have time dependence in Eq. (5.19), which becomes

$$
\Delta p ( t ) = \frac { 1 } { 2 A ^ { 2 } } K ( t ) \rho ( t ) \left[ U ( t ) \right] ^ { 2 } .\tag{5.61}
$$

·If $U = | U _ { 1 } |$ sin ωt, we can calculate the time-averaged pressure drop by integrating Eq.

(5.61) in time:

$$
\begin{array} { r c l } { { \overline { { { \Delta p _ { m l } } } } } } & { { = } } & { { \displaystyle \frac { \omega } { 2 \pi A ^ { 2 } } \left( \int _ { 0 } ^ { \pi / \omega } K _ { o u t } \frac { 1 } { 2 } \rho \left| U _ { 1 } \right| ^ { 2 } \sin ^ { 2 } \omega t d t - \int _ { \pi / \omega } ^ { 2 \pi / \omega } K _ { i n } \frac { 1 } { 2 } \rho \left| U _ { 1 } \right| ^ { 2 } \sin ^ { 2 } \omega t d t \right) } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 8 A ^ { 2 } } \rho \left| U _ { 1 } \right| ^ { 2 } \left( K _ { o u t } - K _ { i n } \right) . } } \end{array}\tag{5.62}
$$

This is the source of $\triangle p _ { 2 , 0 }$ that we will use. Such simple control of $\dot { M } _ { 2 }$ is not without penalty, however; acoustic power is dissipated at a rate

$$
\begin{array} { l l l } { { \displaystyle \bigtriangleup \dot { \bar { E } } _ { 2 } ~ = ~ \frac { \omega } { 2 \pi } \int _ { 0 } ^ { 2 \pi / \omega } \Delta p _ { m l } U d t } } \\ { { ~ = ~ \frac { \omega } { 2 \pi A ^ { 2 } } \left( \int _ { 0 } ^ { \pi / \omega } K _ { o u t } \frac { 1 } { 2 } \rho | U _ { 1 } | ^ { 3 } \sin ^ { 3 } \omega t d t - \int _ { \pi / \omega } ^ { 2 \pi / \omega } K _ { i n } \frac { 1 } { 2 } \rho | U _ { 1 } | ^ { 3 } \sin ^ { 3 } \omega t d t \right) } } \\ { { ~ = ~ \frac { 1 } { 3 \pi A ^ { 2 } } \rho | U _ { 1 } | ^ { 2 } | U _ { 1 } | \left( K _ { o u t } + K _ { i n } \right) } } \\ { { ~ = ~ \frac { 8 } { 3 \pi } \frac { \Delta } { \Delta p _ { m l } } | U _ { 1 } | \frac { K _ { o u t } } { K _ { o u t } - K _ { i n } } , } } \end{array}\tag{5.63}
$$

(5.64)

where A is the area of the small tube. Equation (5.64) shows that the best way to produce a desired $\overline { { \Delta p _ { m } } }$ is to insert the device at a location where $| U _ { 1 } |$ is small, and to shape it so that $K _ { o u t } - K _ { i n }$ is as large as possible. Even though the acoustic power dissipation given in Eqs. (5.63) and (5.64) is formally of third order, it is large if $\boldsymbol { u } _ { 1 }$ is large enough to generate a substantial $\Delta p _ { m l }$

Our measurements at Los Alamos provide qualitative support of most of the features discussed here, but quantitative agreement between Eqs. (5.62) and (5.60) is poor. Once again, there is something important that we do not understand well.

## 5.4.2. Olson streaming

Ideally, the gas in a pulse tube or thermal buffer tube acts as a long (and slightly compressible) piston, transmitting pressure and velocity oscillations from one end to the other. The gas must also thermally insulate the ends of the tube from each other. Unfortunately, convective heat transfer within the tube can carry heat from one end to the other, adding a heat load to the cold heat exchanger in a refrigerator or consuming heat at the hot heat exchanger of an engine. If Gedeon streaming is eliminated, there can be no net mass flux $\dot { M } _ { 2 }$ through the tube, but the possibility remains that mass flux density $\dot { m } _ { 2 , 0 } ( r )$ can stream upward near the side walls of the tube and downward in the central portion of the tube. Such streaming can be caused by jetting due to inadequate flow straightening at either end of the tube, as described in the next subsection, but here we review Olson streaming, which is convection confined within the tube and driven by viscous and thermal boundary-layer phenomena at the side walls of the tube, as illustrated in Fig. 5.10c. The boundary-layer calculation [49] of streaming in such a geometry, based on the earlier work of Rott [61] and incorporating variable cross-sectional area $A ( x ) = \pi \{ R ( x ) \} ^ { 2 }$ , yields a prediction for the side-wall taper angle that suppresses streaming:

$$
\begin{array} { r c l } { \tan \displaystyle \frac { \phi } { 2 } } & { = } & { \frac { \pi R ^ { 3 } \omega | p _ { 1 } | } { 2 \gamma p _ { m } | U _ { 1 } | } [ ( 1 + \frac { 2 ( \gamma - 1 ) ( 1 - b \sigma ^ { 2 } ) } { 3 \sigma ( 1 + \sigma ) } ) \cos \theta  } \\ & & { + ( 1 + \frac { 2 ( \gamma - 1 ) ( 1 - b ) \sqrt { \sigma } } { 3 ( 1 + \sigma ) } ) \sin \theta ] + \frac { ( 1 - b ) ( 1 - \sqrt { \sigma } ) } { 6 ( 1 + \sigma ) ( 1 + \sqrt { \sigma } ) } \frac { R } { T _ { m } } \frac { d T _ { m } } { d x } } \\ & { \simeq } & { ( 7 . 4 \cos \theta + 6 . 3 \sin \theta ) \frac { R ^ { 3 } f | p _ { 1 } | } { p _ { m } | U _ { 1 } | } + 0 . 0 0 2 9 \frac { R } { T _ { m } } \frac { d T _ { m } } { d x } . } \end{array}\tag{5.65}
$$

(5.66)

In $\begin{array} { r l } { \mathbf { E q . } } & { { } ( 5 . 6 6 ) , \ f } \end{array}$ is frequency and numerical values for helium gas are used: $\gamma = 5 / 3 _ { \mathrm { ; } }$ $\sigma = 0 . 6 9 ,$ and $b = \left( T / \mu \right) d \mu / d T = 0 . 6 8$

When Eq. (5.65) or (5.66) is satisfied, a large number of side-wall boundary-layer effects are in delicate balance, with some trying to cause streaming up along the side walls and down through the center, while others try to cause streaming down along the side walls and up through the center. One such effect is easily imagined and is illustrated in Fig. 5.13c. Consider a small parcel of gas oscillating up and down along the wall, at a distance from the wall of the order of the relevant boundary layer: the viscous penetration depth $\delta _ { \nu }$ On average, the gas between the parcel and wall will have a different temperature during the parcel's upward motion than during its downward motion, due to imperfect thermal contact with the wall's temperature gradient and due to the adiabatic temperature oscillations with time phasing between' oscillatory motion and oscillatory pressure. The moving parcel will experience a different amount of viscous drag during its upward motion than during its downward motion because the viscosity depends on temperature, so it will undergo a different displacement during its upward motion than during its downward motion. After a full cycle, the parcel does not return to its starting point; it experiences a small net drift which contributes to $u _ { 2 , 0 }$ at its location. This process is represented by terms proportional to the product of $\boldsymbol { b } , T _ { 1 }$ , and $\pmb { u } _ { 1 }$ in the nonlinear equations of the derivation, and is responsible for the presence of b in Eq. (5.65).

The effect of a taper on streaming can also be imagined, with reference to Fig. 5.13d. In general, a gas parcel close to the wall will be farther from the wall during, say, its upward motion than during its downward motion, due $\mathbf { t o } ,$ for example, the compressibility of the gas in the boundary layer and the phasing between oscillatory motion and pressure. Hence, again the moving parcel will experience a different amount of viscous drag during its upward motion than during its downward motion, and so the parcel will again fail to return to its starting point after a full cycle. This effect is represented in the starting equations of the derivation by terms proportional to the product of ${ \pmb u } _ { 1 }$ and ${ \pmb v } _ { 1 }$ . However, the boundarylayer continuity equation couples ${ \pmb v } _ { \bf 1 }$ and $d u _ { 1 } / d x$ , while the y-averaged continuity equation iwA $\left. \rho _ { 1 } \right. + \rho _ { m } d \left. A u _ { 1 } \right. / d x = 0$ couples du₁/dx to $d A / d x$ . Hence, the process shown in Fig. 5.13d is controlled in part by the taper $d A / d x$ , and is responsible for the presence of $\phi$ in Eq. (5.65).

Including all such second-order streaming effects in the calculations allow determination of the conditions under which they all add to zero, represented by $\mathtt { E q }$ (5.65). .Note that all the variables in the right hand side of Eq. (5.65) or (5.66) should be known during the design of a pulse tube refrigerator and are experimentally. accessible.

The effort necessary to obtain expressions for p or u at second order, describing streaming, is far greater than the effort of Chapter 2 to obtain first-order expressions for these variables. For example, Olson's calculation begins with the x component of the general momentum equation [26]

(a)  
![[mu_ad18d396_9d44ccb375ea2ab03c11.jpg]]

(b)  
![[mu_ad18d396_7dcebd0fe330e2391368.jpg]]

(c)  
![[mu_ad18d396_22c881530e62640cc730.jpg]]

(d)  
![[mu_ad18d396_f1f4103ff24ab9f2f2d8.jpg]]  
Figure 5.13: (a) The net drift near the wall, illustrated in (c) and (d), affects the entire tube, causing an offset parabolic velocity profile which contributes to a second-order mass flux density $\dot { m } _ { 2 , 0 } ( r )$ . For the signs chosen here for illustration, the gas moving downward in the center of the tube is hotter than the gas moving upward around $\mathbf { i t } ,$ so that heat is carried downward. The coordinate r measures the distance from the center of the tube, of radius R. The calculations are for $R \gg \delta _ { \nu } .$ , but, for clarity, $\delta _ { \nu }$ is exaggerated in the figure. (b) Mass flux density for the case where the streaming is suppressed by tapering the tube. Although there is still some streaming near the wall and a correspondingly small offset mass flux in the rest of the tube, they carry negligible heat. (c) Illustration of net drift caused by one process within $\delta _ { \nu }$ of the tube wall. A parcel of gas is shown in three consecutive positions. Here we imagine that the temperature dependence of the viscosity is the only important effect, and assume that the temperature is lower during upward motion than during downward motion. (d) Illustration of net drift caused by a different. process, as discussed in the text.

$$
\rho \left[ \frac { \partial u } { \partial t } + \left( \mathbf { v } \cdot \nabla \right) u \right] = - \frac { \partial p } { \partial x } + \frac { \partial } { \partial x } \left[ \mu \left( \frac { 4 } { 3 } \frac { \partial u } { \partial x } + \frac { \partial v } { \partial y } \right) + \frac { \partial } { \partial y } \left( \frac { \partial u } { \partial y } + \frac { \partial \overset { . } { \partial v } } { \partial x } \right) \right] ,\tag{5.67}
$$

which becomes, to second order,

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \operatorname { R e } \left[ - i \omega \rho _ { 1 } \widetilde { u } _ { 1 } + \rho _ { m } \widetilde { u } _ { 1 } \frac { \partial u _ { 1 } } { \partial x } + \rho _ { m } \widetilde { v _ { 1 } } \frac { \partial u _ { 1 } } { \partial y } \right] } \\ { ~ } & { = ~ - \frac { d p _ { 2 , 0 } } { d x } + \rho _ { m } \frac { \partial ^ { 2 } u _ { 2 , 0 } } { \partial y ^ { 2 } } + \frac { 1 } { 2 } \operatorname { R e } \left[ \frac { \partial } { \partial y } \left( \mu _ { 1 } \frac { \partial \widetilde { u } _ { 1 } } { \partial y } \right) \right] . } \end{array}\tag{5.68}
$$

This is far more complicated than the first-order x component of the momentum equation, Eq. (2.54). In particular, to obtain correct answers at second order, viscosity must be kept inside the derivative on the right-hand side; this aspect of the present problem differs from most problems in acoustics and fluid dynamics.

The fact that Olson streaming in a pulse tube or thermal buffer tube can be suppressed so simply and conveniently is the result of a remarkable series of fortunate coincidences. First, there is no a priori guarantee that tapering the tube would have a large enough effect on streaming to cancel streaming's other causes. Second, it might have turned out that rather large taper angles (say, greater than $1 0 ^ { \circ }$ or $2 0 ^ { \circ } )$ were required; in this case, jet-like flow separation of the high-Reynolds-number first-order velocity from the tube wall would have invalidated the entire laminar, boundary-layer approach. Third, it is fortunate that most tubes operate in the "weakly turbulent" regime of oscillatory flow, and with tube surface roughness much smaller than the boundary-layer thickness, so that laminar analysis is adequate in'the boundary layer.

Fourth, the perturbation expansion upon which this calculation is based is only valid for zero or extremely weak streaming—the very situation we are most interested in. This point is subtle. Strong streaming (but nevertheless with streaming velocity small compared to the oscillatory velocity) distorts the axial temperature profile of the pulse tube significantly, contradicting the fundamental assumption that the time-averaged temperature, density, etc. in the boundary layer are well approximated by their zero-oscillation values $T _ { m } ( x )$ $\rho _ { m } ( x )$ , etc. This fundamental assumption requires that the streaming be so weak that the temperature profile in the pulse tube is unperturbed by the streaming- $- \infty \mathbf { r } ,$ equivalently, that the streaming is so weak that it carries negligible heat! Hence, the calculation selfconsistently predicts the conditions of zero streaming, but it cannot be relied on to accurately predict the magnitude of strong streaming.

Fifth, there are numerous other fourth-order energy flux terms in addition to $\dot { m } _ { 2 , 0 } c _ { p } T _ { 2 , 0 }$ which would in principle have to be considered to obtain a formally correct fourth-order result. Fortunately, the only other large term, $\rho _ { 2 , 0 } c _ { p } \operatorname { R e } [ T _ { 1 } \widetilde { U } _ { 1 } ] .$ , is zero at the same taper angle that makes $\dot { m } _ { 2 , 0 } c _ { p } T _ { 2 , 0 }$ zero, while the remaining terms, such as those involving products of first and third order quantities, are small for all angles. Hence, the suppression of $\dot { m } _ { 2 , 0 }$ is sufficient to suppress all fourth-order heat transport.

Finally, as a practical matter, it is extremely convenient that the streaming-suppression taper is independent of oscillation amplitude and is only weakly dependent on temperature gradient.

## 5.4.3. Jet-driven tube streaming

Ideally, the gas in a pulse tube or thermal buffer tube would do nothing more than oscillate in plug flow, transmitting $\dot { E } _ { 2 } \equiv \dot { H } _ { 2 }$ from one end to the other. In reality, several nonidealities can cause $\dot { E } _ { 2 } \neq \dot { H } _ { 2 } ,$ carrying heat down the temperature gradient: ordinary conduction along x (discussed in Chapter 3), ordinary thermoacoustic boundary-layer phenomena carrying entropy along x near the wall, bucket-brigade fashion (discussed in Chapter 3), Gedeon streaming (discussed in this chapter), Olson streaming (discussed in this chapter), gravitydriven convection, and jet-driven convection (discussed here). Simultaneous suppression of all these heat-transport mechanisms is not trivial.

A rough estimate indicates how easily Olson streaming or other convection internal to a pulse tube or thermal buffer tube can ruin $\dot { E } _ { 2 } \equiv \dot { H } _ { 2 }$ . In a tube with reasonably large diameter, such as $1 0 0 \delta _ { \kappa }$ , there is little radial thermal contact in the gas, so any time-averaged flow $\mathbf { \lambda } _ { u _ { 2 , 0 } }$ from end to end carries a full $\Delta T$ load of heat the length of the tube. If we desire a 98% effective pulse tube, this heat must be only 2% of $\dot { E } _ { 2 }$

$$
\rho c _ { p } u _ { 2 , 0 } \Delta T \sim \left( 0 . 0 2 \right) \frac { 1 } { 2 } \left| p _ { 1 } \right| \left| u _ { 1 } \right| .\tag{5.69}
$$

Using $\rho c _ { p } = \gamma p / ( \gamma - 1 ) T$ and solving for $\mathbf { \Delta } u _ { 2 , 0 }$ yields

$$
u _ { 2 , 0 } \sim 1 0 ^ { - 2 } \frac { \gamma - 1 } { \gamma } \frac { T } { \Delta T } \frac { \left| p _ { 1 } \right| } { p _ { m } } \left| u _ { 1 } \right| .\tag{5.70}
$$

Hence, in a typical case we might need $u _ { 2 , 0 } \lesssim 1 0 ^ { - 3 } ~ \mathrm { m } / \mathrm { s }$ in the presence of $| u _ { 1 } | = 1 0$ m/s. In terms of displacements, this means that we need gas displacements in the +x and $- \pmb { x }$ directions be matched to within $1 0 ^ { - 4 }$

We want this "imaginary piston" of gas in the tube to execute plug flow, but it is a very fragile object. Working to mix up this plug flow are the various streaming mechanisms listed in the first paragraph of this subsection. Working to maintain the plug flow are only a few subtle effects. First, gravity and the mean density gradient tend to keep this fragile imaginary piston stratified. With a typical mean-density difference of only a few $\bf k g / m ^ { 3 }$ only $\Delta p \sim \Delta \rho g \Delta x \sim 1$ Pa is available, in the presence of oscillations typically at least ${ \mathsf { 1 0 ^ { 4 } } }$ times larger. Viscous shear forces caused by gradients in $u _ { 2 , 0 }$ also tend to reduce $u _ { 2 , 0 } ,$ but the pressure differences available from this source are only of order $\mu \Delta x u _ { 2 , 0 } / R ^ { 2 }$ , which is typically much smaller than 1 Pa.

Good radial thermal contact in the tube could prevent $u _ { 2 , 0 }$ from carrying the full $\Delta T$ from end to end, essentially allowing the upflowing and downflowing streams of Olson streaming or jet-driven streaming to experience counterflow heat. exchange, so that the tube would enjoy $\dot { E } _ { 2 } \sim \dot { H } _ { 2 }$ even in the presence of a $_ { u _ { 2 , 0 } }$ greater than the value estimated above. If $u _ { 2 , 0 } \sim 0 . 1$ m/s and $\Delta x \sim 0 . 1$ m, then 1 second is available while the stream traverses the length of the tube. If the oscillation frequency is of order 100 Hz, then 100 acoustic periods are available; during this time, heat can diffuse roughly $1 0 \delta _ { \kappa }$ . Only the pulse tubes of the smallest cryocoolers are this small; most tubes are too large to enjoy substantial benefit from this mechanism. [However, note that the weak turbulence of most pulse tubes and buffer tubes may enhance such radial heat transport slightly.]

If either end of the tube has a small-diameter entrance, a jet may blow into the tube when gas enters, driving streaming within the tube, as illustrated in Fig. 5.10d. The spreading angle [51] of a high-Reynolds-number jet in free space is roughly $1 0 ^ { \circ }$ , so such a jet can extend a large distance, and even the array of small jets fcrmed by flow out of a heat exchanger or similar periodic structure requires some distance to heal into plug flow. Hence, flow straighteners are typically employed to break up such jets. A nonlinear impedance, such as that of a short stack of screens in which $N _ { R , \mathrm { p e a k } } \gtrsim 1 0 ^ { 3 } .$ , is most effective at straightening jets. We typically employ such a flow straightener whenever a jet, spreading at an angle of $1 0 ^ { \circ }$ would reach more than about $\mathbf { 2 } \left. x _ { 1 } \right.$ into the tube; we choose the flow straightener's resistance $R _ { \tt s t r a i g h t e n e r }$ by simply making the peak pressure drop across the straightener (assuming wellstraightened $\pmb { U } _ { 1 } )$ equal to about a fifth of the Bernoulli pressure of the strongest jet in the vicinity:

$$
\left| U _ { 1 } \right| R _ { \mathrm { s t r a i g h t e n e r } } \sim \frac { 1 } { 1 0 } \rho \left[ \frac { | U _ { 1 } | } { A _ { \mathrm { j e t } } } \right] ^ { 2 } .\tag{5.71}
$$

Because flow straighteners dissipate acoustic power, research leading to more quantitative design methods for flow straighteners will help improve the efficiency of thermoacoustic engines and refrigerators

## 5.4.4. Streaming within a regenerator or stack

We know little about streaming within a regenerator or stack, except that it should be avoided for the same reasons that Olson streaming should be avoided. We know it can occur, because we once suffered from harmful toroidal streaming within a regenerator when a narrow jet blew strongly on the heat exchanger at one end of the regenerator, due to an abrupt transition from a small duct to the diameter of the regenerator and heat exchanger. We fear that such toroidal time-averaged flows might also occur spontaneously, as has been observed when two or more regenerators are operated in parallel.

## 5.4.5. Deliberate streaming

Thermoacoustic systems suffer from a practical difficulty: They need heat exchangers to transfer heat between the thermodynamic working gas and the process fluid (usually air, combustion products, or water). Heat exchangers are expensive, and contribute to system inefficiency via temperature differences and viscous effects in the working fluid, in the process fluid, and often in an intermediate heat-exchange fluid. This difficulty is serious. For example, the decline of the Stirling engine and the rise of the Diesel and other internal combustion engines occurred in large part because the internal combustion engine needs no combustion-temperature heat exchanger (and also rejects most of its waste heat in its exhaust instead of through heat exchangers).

For some applications, we hope that some or all of the heat exchangers can be eliminated from thermoacoustic systems, by superposing the steady flow needed to deliver the process gas with the oscillatory flow needed for the thermodynamic cycle in the gas. We hope this idea will lead ultimately to thermoacoustic equipment for purposes such as drying of compressed air, combustion-powered air conditioning, combustion-powered dehumidification drying (such as for lumber), gas purification, or cryogen liquefaction.

To introduce some of the expected features that thermoacoustic systems with deliberate steady flow might have, we will focus attention on one specific case: a thermoacoustic air conditioning system. The ideas we illustrate using this example are equally applicable to other thermoacoustic engines and refrigerators and to Stirling engines and refrigerators.

![[mu_ad18d396_6ea7247e3e20c1aa7d5b.jpg]]  
Figure 5.14: A half-wavelength standing-wave thermoacoustic refrigerator, thermally coupled to two air ducts to form an air conditioner.

## Parallel flow

As a point of departure, Fig. 5.14 shows the main parts of an air conditioning system using conventional thermoacoustic refrigeration. Four heat exchangers are required: two in the thermoacoustic working gas and one in each of the two air streams. Heat transfer between working-gas heat exchangers and air heat exchangers, indicated by heavy black arrows, is accomplished via pumped water loops (or heat pipes, thermosyphons, etc.). The four heat exchangers and two water loops account for most of the capital cost of the system.

The air conditioning system in Fig. 5.15 illustrates a simplification that is possible by using the indoor air itself as the thermoacoustic gas. A midwall in the indoor-air duct separates two acoustic resonators, driven 180° out of phase from each other by an oscillating piston in the center of the midwall. The drive frequency is chosen to make the acoustic wavelength equal to twice the midwall length, so there will be pressure nodes at the ends of the midwall and, hence, negligible acoustic power radiated to distant parts of the duct. The position of the stack relative to the nodal pattern of the standing wave is chosen so that conventional standing-wave thermoacoustic processes pump heat from right to left. Superimposed on that thermoacoustic process, the gas drifts slowly through the stack from ambient to cold, so that it leaves the right end of the apparatus at the cold temperature.

This superposition can give the system of Fig. 5.15 a higher efficiency than that of the system of Fig. 5.14, for two reasons. First, two heat exchangers, and their internal small temperature differences, are eliminated. Second, a much more subtle improvement in efficiency arises because the system of Fig. 5.15 essentially puts the air stream sequentially in thermal contact with a large number of refrigerators in series—a sort of continuum limit of staged refrigeration. To understand this point, first imagine that thermoacoustic refrigerators are ideal, having Carnot's $C O P = T _ { C } / ( T _ { 0 } - T _ { C } )$ . Then, in the case of Fig. 5.14, removing heat $\dot { m } c _ { p } ( T _ { 0 } - T _ { C } )$ at temperature $\mathit { \Delta } \mathcal { T } _ { c }$ with the refrigerator requires work

![[mu_ad18d396_eec807bebc26e2c1cc56.jpg]]  
Figure 5.15: Two side-by-side half-wavelength thermoacoustic refrigerators in an air duct allow direct thermoacoustic cooling of the air. The standing-wave refrigerator of Figs. 1.11 and 1.12 has this topology, with the midwall in this figure equivalent to the large empty space in the center of the torus in Figs. 1.11 and 1.12.

$$
\dot { W } = \dot { m } c _ { p } ( T _ { 0 } - T _ { C } ) ^ { 2 } / T _ { C } .\tag{5.72}
$$

This is more than twice the minimum work required by the first and second laws of thermodynamics for this process, which we saw in Chápter 4 is given by the difference between the outgoing and-incoming flow availabilities:

$$
\begin{array} { r } { \dot { \hat { W } } ~ = ~ \hat { m } \left[ \left( h _ { C } - h _ { 0 } \right) - T _ { 0 } \left( s _ { C } - s _ { 0 } \right) \right] } \end{array}\tag{5.73}
$$

$$
\begin{array} { r l r } { } & { { } } & { = \ \dot { m } c _ { p } [ T _ { C } - T _ { 0 } + T _ { 0 } \ln ( T _ { 0 } / T _ { C } ) ] . } \end{array}\tag{5.74}
$$

(The second expression results from using ideal-gas expressions for h and ${ \pmb s } . )$ The trouble with the simple, one-stage refrigerator is that it removes all the heat load at $\pmb { T _ { C } }$ , where every watt of cooling power requires the same amount of work. It is much more efficient to remove as much of the heat load as possible at higher temperatures $T _ { C } ^ { \prime } .$ ,where each watt of çooling power requires less work because the Carnot $C O P = T _ { C } ^ { \prime } / ( \bar { T } _ { 0 } - T _ { C } ^ { \prime } )$ is higher. The perfect embodiment of this idea would employ an infinite number of ideal refrigerators, each providing an infinitesimal cooling power $\dot { m } c _ { p } d T _ { C } ^ { \prime }$ at $\pmb { T _ { C } } ^ { \prime }$ and rejecting an infinitesimal amount of waste heat at $\pmb { \mathcal { T } _ { 0 } }$ . The flow-through thermoacoustic refrigerator of Fig. 5.15 has some features of this perfect situation, if we imagine each length dx-of the stack to be a refrigerator unto itself, lifting heat from $\mathit { T _ { c } ^ { \prime } }$ to $T _ { c } ^ { \prime } + d T _ { c } ^ { \prime }$ . The flow-through system removes each watt of heat from the flowing stream at the highest possible temperature—but with an "infinite" number of less-than-ideal refrigerators, each of which must handle the waste heat of all its downstream neighbors in addition to the local heat load of the flowing stream.

With the addition of nonzero mean velocity along x, the gas moves through the system in a repetitive, "102 steps forward, 98 steps back" manner, in position, in temperature, and in density and entropy. This violates one assumption on which Chapters 2 and 3 are based, because there we assumed $u \dot { = } \mathbb { R e } \{ u _ { 1 } e ^ { i \omega t } \}$ , with no $^ { 6 6 } u _ { m } ^ { \mathrm { ~ ~ } \mathfrak { n } }$ . The apparatus shown in Figs. 1.11 and 1.12 was built to study this type of deliberate steady flow [16].

To derive corresponding equations in the presence of nonzero parallel steady flow, we again begin with the momentum, continuity, and energy equations. We write

$$
\begin{array} { r } { p \ = \ p _ { m } ( x ) + \mathrm { R e } \left[ p _ { 1 } ( x ) e ^ { i \omega t } \right] , } \end{array}\tag{5.75}
$$

$$
\begin{array} { r } { u } { \ = \ u _ { m } ( x , y , z ) + \mathrm { R e } \left[ u _ { 1 } ( x , y , z ) e ^ { i \omega t } \right] , } \end{array}\tag{5.76}
$$

$$
\begin{array} { r } { \boldsymbol { \upsilon } ~ = ~ \mathrm { R e } \left[ v _ { 1 } ( x , y , z ) e ^ { i \omega t } \right] , } \end{array}\tag{5.77}
$$

$$
w = \mathrm { \ s i m i l a r \ t o \ } \upsilon ,\tag{5.78}
$$

$$
\begin{array} { r } { \begin{array} { l l l } { T } & { = } & { T _ { m } ( x ) + T _ { m } ^ { \prime } ( x , y , z ) + \mathrm { R e } \left[ T _ { 1 } ( x , y , z ) e ^ { i \omega t } \right] , } \end{array} } \end{array}\tag{5.79}
$$

$$
\rho ~ = ~ \rho _ { m } ( x ) + \rho _ { m } ^ { \prime } ( x , y , z ) + \mathrm { R e } \left[ \rho _ { 1 } ( x , y , z ) e ^ { i \omega t } \right] ,\tag{5.80}
$$

$$
\mu , k , \mathrm { ~ e t c . ~ \ = ~ \ s i m i l a r ~ t o ~ } \rho \mathrm { ~ ( b u t ~ s e e ~ b e l o w ) . }\tag{5.81}
$$

We will consider $ { p _ { 1 } } /  { p _ { m } }$ and $\mathbf { v _ { 1 } } / a$ to be small, and will keep terms to first order in smallness in the momentum and continuity equations and to second order in smallness in the energy equation as usual. Note that we consider $d T _ { m } / d x$ to be of zeroth order. We will see below that the energy equation then requires us to consider $u _ { m } / a$ to be of second order; for the moment, we may imagine this to be an assumption.

Substituting Eqs. (5.75)-(5.81) into the momentum equation, and requiring that the time-independent terms and the terms proportional to $e ^ { i \omega t }$ must equate separately, yields the same first-order momentum equation as in Chapter 2, and a time-averaged equation:

$$
0 = - d p _ { m } / d x + \mu \nabla _ { y , z } ^ { 2 } u _ { m } .\tag{5.82}
$$

This time-averaged equation simply expresses the fact that viscosity and steady flow cause a steady pressure gradient. It shows that $d p _ { m } / d x$ is of second order (the same order as $u _ { m } )$ so we will neglect it, regarding $p _ { m }$ as a x-independent constant.

In the continuity and energy equations below, we will require expressions for the oscillatory temperature $\mathcal { T } _ { 1 }$ and its spatial average $\left. T _ { 1 } \right.$ over y and z. Starting from the general equation of heat transfer as we did in Chapter $^ { 2 , }$ we find the same first-order equation for $\boldsymbol { \mathcal { T } _ { 1 } }$ as in Chapter $^ { 2 , }$ and a time-averaged equation

$$
\rho _ { m } c _ { p } u _ { m } d T _ { m } / d x = k \nabla _ { y , z } ^ { 2 } T _ { m } ^ { \prime } .\tag{5.83}
$$

Our only use of Eq. (5.83) is to note that it implies $\mathcal { T } _ { m } ^ { \prime }$ is of second order. Hence $T _ { m } ^ { \prime } .$ and similarly $\rho _ { m } ^ { \prime } , \mu _ { m } ^ { \prime } , k _ { m } ^ { \prime } ,$ etc., can be neglected, because their contributions are of negligible order.

Next we consider the continuity equation

$$
\partial \rho / \partial t + \nabla \cdot ( \rho { \mathbf v } ) = 0 ,\tag{5.84}
$$

which can be integrated with respect to y and z to obtain to lowest order

$$
i w A \left. \rho _ { 1 } \right. + \frac { d ( \rho _ { m } U _ { 1 } ) } { d x } = 0 ,\tag{5.85}
$$

$$
\frac { d ( \rho _ { m } U _ { m } ) } { d x } ~ = ~ 0 .\tag{5.86}
$$

Again, the first-order expression is the same as in Chapter 2. Using $d \rho = - \left( \rho / T \right) d T +$ $( \gamma / a ^ { 2 } ) d p ,$ we can express the mean density as

$$
d \rho _ { m } / d x = - \left( \rho _ { m } / T _ { m } \right) d T _ { m } / d x .\tag{5.87}
$$

to lowest order. Substituting this into Eq. (5.86) yields

$$
\frac { d \bar { U } _ { m } } { d x } - \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } \bar { U } _ { m } = 0 ,\tag{5.88}
$$

which can be used to predict the x dependence of $U _ { m }$ during numerical integration along x. Finally, we consider the energy equation, as we did in Chapter 3. There, we saw that the important terms in the time-averaged energy equation are

$$
0 = \frac { d } { d x } \left[ A \left. \overline { { \rho u h } } \right. - A \left. \overline { { k \partial T / \partial x } } \right. - A _ { \mathrm { e o l i d } } \left. \overline { { k _ { \mathrm { s o l i d } } \partial T _ { \mathrm { s o l i d } } / \partial x } } \right. _ { \mathrm { s o l i d } } \right] .\tag{5.89}
$$

In principle, we must consider each ofthese terms to second order, but in practice, for situations of interest to us, zeroth order suffices for the last two terms, as it did in Chapter 3. Hence, we begin with the first term. Its expansion to second order is

$$
A \left. \rho _ { m } u _ { m } h _ { m } + \overline { { \rho _ { 1 } u _ { 1 } } } h _ { m } + \rho _ { m } \overline { { u _ { 2 } } } h _ { m } + \rho _ { m } \overline { { u _ { 1 } h _ { 1 } } } \right. ,\tag{5.90}
$$

where we have already set five terms equal to zero because the time average of first order quantities $( \mathbf { e . g . } , \overline { { \rho _ { 1 } } } \ \mathrm { o r } \ \overline { { u _ { 1 } } } )$ is zero. We regard the steady mass flow as fixed at $\rho _ { m } U _ { m } =$ $A \left. \rho _ { m } u _ { m } \right.$ , so that the second-order time-averaged mass flux $A \left. \overline { { \rho _ { 1 } u _ { 1 } } } + \rho _ { m } \overline { { u _ { 2 } } } \right. = 0$ . Hence (5.90) reduces to

$$
A \left. \rho _ { m } u _ { m } h _ { m } + \rho _ { m } \overline { { u _ { 1 } h _ { 1 } } } \right. .\tag{5.91}
$$

Using $d h = c _ { p } d T _ { \mathrm { : } }$ , and combining this with the other significant terms from Eq. (5.89), we conclude that

$$
\dot { H } _ { 2 } = \rho _ { m } c _ { p } ( T _ { m } - T _ { 0 } ) U _ { m } + A \rho _ { m } c _ { p } \left. \overline { { T _ { 1 } u _ { 1 } } } \right. - \left( A k + A _ { \mathrm { s o l i d } } k _ { \mathrm { s o l i d } } \right) d T _ { m } / d x .\tag{5.92}
$$

The new term, $\rho _ { m } c _ { p } ( T _ { m } - T _ { 0 } ) U _ { m } ,$ is of the same order (second) as the old $A \rho _ { m } c _ { p } \left. \overline { { T _ { 1 } u _ { 1 } } } \right.$ we obtained in Chapter 3. With $\dot { H } _ { 2 }$ independent of x in a stack, regenerator, or other thermally insulated channel, this equation allows us to predict the x dependence of $\mathbf { \nabla } \mathcal { T } _ { m }$ during numerical integration along x when steady flow $\tau _ { m }$ is superimposed on thermoacoustic oscillations. Generally, the steady flow causes $\pmb { T _ { m } } ( \pmb { x } )$ to bend significantly, as steady flow from hot to cold pushes the center of the stack or regenerator to warmer temperatures, or steady flow from cold to hot pushes the center of the stack or regenerator to colder temperatures [16].

![[mu_ad18d396_24eb4b45fa6c93c14811.jpg]]  
Figure 5.16: Two side-by-side three-quarter-wavelength thermoacoustic refrigerators, each with a baffle to direct the superimposed steady flow, in an air duct network. This arrangement allows direct thermoacoustic cooling of some of the steady air flow, rejecting waste heat to the remainder of the steady air flow, with no heat exchangers except the stack.

## Perpendicular flow

Thus far, we have discussed steady flow superimposed parallel to the oscillating flow. To introduce the idea of steady flow superimposed perpendicular to the oscillating flow, we return to our air-conditioner motif, showing in Fig. 5.16 the elimination of all heat exchangers from a thermoacoustic system. As in Fig. 5.15, a midwall separates the duct into two regions that resonate 180° out of phase from each other. The drive frequency is chosen so that 3/4 of the acoustic wavelength equals the midwall length, thereby putting a pressure antinode at the hard duct closure at the left end of the midwall and a pressure node at the right, open end of the midwall. Deflector walls further divide each of these two resonators in order to direct the steady flow of the air. This steady flow is introduced into the resonator at the pressure node 1/4 of a wavelength from the hard closure, so that negligible acoustic power is radiated into the air inlet duct. A significant fraction of the steady flow passes through the stack, is thereby cooled and dehumidified, and leaves the right end of the duct. Most of the steady flow passes vigorously past the hot end of the stack, moving perpendicular to the oscillating flow, in order to remove the waste heat from the thermoacoustic system and exhaust it. The quantitative understanding of oscillating thermodynamics in the presence of such a perpendicular steady flow is a significant and exciting challenge.

The air conditioner described above will, incidentally, dehumidify the air, returning cold dry air. But for many important drying applications, it is desired to dehumidify air and return it warm and dry. Hence, we could also consider configurations comprising coolers and heat pumps in the same resonator, to put the waste heat from the hot end of the cooling stack back into the air stream. This is but one of many possibilities for open thermoacoustic systems in which multiple stacks, serving multiple functions, share a resonator. As another example, industry has long dreamed of a combustion-powered heat pump hot water heater, which would have a (first-law) efficiency greater than 100%: It would use part of the heat of combustion to drive an engine, which would drive a heat pump to draw heat from ambient air and deliver it to the hot water. Such devices can (and have) been built with existing technology, but only at a cost that is prohibitive to today's consumer. We can imagine such a system using open flows through a thermoacoustic system, with a pulse combustor, thermoacoustic engine, and thermoacoustic heat pump in an air stream, all delivering heat to hot water passing through a heat exchanger.

## 5.5. Harmonics and shocks

In preparation.

## 5.6. Dimensionless groups

In preparation. Something like a summary of [62]

## 5.7. Exercises

5.1 Calculate the molecular mean free path for your favorite gas in your favorite thermoacoustic apparatus, by looking up the appropriate equations in something like an introductory statistical-mechanics textbook such as Reif's Statistical and Thermal Physics. Compare to dimensions in the apparatus and to $\delta _ { \nu }$ and $\delta _ { \kappa } .$ Is the mean free path so negligible compared to $\delta _ { \nu }$ that the representation in Ani. viscous should be accurate? Are the crevices between screen wires in your regenerator large compared to the mean free path?

5.2 Calculate the peak Reynolds number and $r _ { h } / \delta _ { \nu }$ at a few, locations in your favorite thermoacoustic apparatus. Where are they, on Fig. 5.3?

5.3 In the section on minor losses, we assumed that $\pmb { U } ( t )$ was sinusoidal. In some situations, it may be better to assume that $\Delta p ( t )$ is sinusoidal. Repeat the derivation of Eq. (5.23) assuming that $\Delta p ( t )$ is sinusoidal. Can you reconcile this answer with Eq. (5.23)?

5.4 To help assure yourself that the similitude-variable list is complete, express the Prandtl number at the reference temperature in terms of the variables listed: $\mu _ { r e f } , K _ { r e f } ,$ $a _ { r e f } , p _ { m } , T _ { r e f } ,$ , and $\gamma .$

5.5 Express the Mach number $u _ { 1 } / a$ and the Reynolds number in terms of ratios of lengths, using $| \langle x _ { 1 } \rangle | , r _ { h } , \lambda ,$ and $\delta _ { \nu }$

5.6 Your sponsor wants you to build a thermoacoustic engine to generate electricity on a satellite. The engine will operate from a plutonium heat source at 1800 K, and dump its waste heat to a tiny black-body radiator at 900 Kelvin. Helium will be the gas, at a pressure of 20 bar. You want to use similitude to do some preliminary tests in a model that operates between 600 Kelvin and 300 Kelvin-exactly $1 / 3$ the ultimate temperatures—so you can experiment using stainless steel instead of iridium and platinum. You want the model to have the same dimensions as the ultimate hardware. What mean pressure of helium must you use in the model? How much higher or lower will all powers be in the model? If you wanted to use a different monatomic gas instead of helium in the model, could you keep the mean pressure in the model lower/safer?

5.7 Figure 5.2 shows that the laminar friction factor is $f _ { M } = 6 4 / N _ { R }$ for steady flow in a circular pipe. Derive this from Eq. (5.2). Begin this process by justifying the neglect of most terms in Eq. (5.2), leaving only $\dot { 0 } = - d p / d x + \mu \nabla ^ { 2 } u$

For a serious mathematical challenge, show that combining Eqs. (2.56) and (2.62) gives the same result, in the limit $\omega \to 0$

5.8 Review Exercise 4.2. Repeat that exercise, assuming that all refrigerators operate at the same fraction $\eta _ { I I }$ of Carnot's COP. In which direction does the comparison between Case 2 and Case 3 shift? Now extend Case 3 of the original exercise from two refrigerators to an infinite number of refrigerators, showing by comparison to Eq. (5.74) that the work required is the minimum allowed by the laws of thermodynamics. Can you repeat this continuum calculation assuming that all the refrigerators operate at the same fraction $\eta _ { I I }$ of Carnot's COP?

## 6. HARDWARE

In preparation. remember thermal stress in pressure vessels

## 7. MEASUREMENTS

In preparation.

## 8. COMMON PITFALLS

in preparation

<table><tr><td colspan="4"></td></tr><tr><td>BEGIN the setup 2.9660E+06 a Mean P</td><td>Pa</td></tr><tr><td>b Freq. 390.27</td><td>Hz</td><td>390.27 G 758.28</td><td>AFreq. G( Ob) B T-beg G( 0c)</td></tr><tr><td>758.28 c T-beg 3.1963E+05 d lpl@0</td><td>K G</td></tr><tr><td>0.0000 e Ph(p)0</td><td>3.1963E+05 C Ipl@0 G( Od) G</td></tr><tr><td></td><td>P 2392.4 D HeatIn G( 3e) P</td></tr><tr><td>Pa deg</td><td></td></tr><tr><td>0.0000 f |U|@O m^3/s 0.0000 g Ph(U)0 deg</td><td></td></tr><tr><td>helium Gas type</td><td></td></tr><tr><td>ideal Solid type</td><td></td></tr><tr><td>ENDCAP hot end</td><td>1</td></tr><tr><td>2a a Area m^2 sameas</td><td>3.1963E+05 A Ipl Pa</td></tr><tr><td></td><td>0.0000 B Ph(p) deg</td></tr><tr><td></td><td>2.3740E-05 C |UI m^3/s</td></tr><tr><td></td><td>180.00</td></tr><tr><td></td><td>D Ph(U) deg</td></tr><tr><td>0 Gas type -3.7940 F Work</td><td>-3.7940 E Hdot W</td></tr><tr><td>sameas</td><td>W</td></tr><tr><td></td><td></td></tr></table>

## 9. APPENDIX

These are DeltaE files for parts of the example hardware shown in the Examples section in Chapter 1 and referred to throughout the book.

## 9.1. Standing-wave engine

This model of.part of the standing-wave engine starts at the right end of Fig. 1.10 and integrates to the left, past the branch up to the refrigerators, ending at the pressure node at the center of the resonator. The point of view adopted in this particular file is this: In order to have the as-built hardware run with p1| = 297 kPa at the branch to the refrigerators and supply 1000 W of acoustic power to the refrigerators, what hot temperature and heater power are required at the hot heat exchanger at the hot end of the stack, and at what frequency will the system resonate? (In this simplified model, we assume that the left engine can supply 500 W of acoustic power, but at Los Alamos we would typically fully include the left engine in the model.)

TITLE One engine, branch to OPTRs; stop calc at midplane. As-built dims. !->staneng.out

!Created@13:50:34 2-Jan-99 with DeltaE Vers. 4.5b7 for the IBM/PC-Compatible

<table><tr><td>ideal</td><td>Solid type</td><td></td><td>-3.7940</td><td>G HeatIn</td><td>W</td></tr><tr><td>ISODUCT</td><td>hot duct</td><td></td><td>2</td><td></td><td></td></tr><tr><td>2.8580E-03 a Area</td><td></td><td>m^2</td><td></td><td>3.1885E+05 A Ipl</td><td>Pa</td></tr><tr><td></td><td>0.1900 b Perim</td><td>m</td><td></td><td>1.3951E-03 B Ph(p)</td><td>deg</td></tr><tr><td>4.5900E-02 c Length</td><td></td><td>m</td><td></td><td>2.0855E-02 C|UI</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>-90.264</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>-15.375</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td>-15.375</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td>-11.581</td><td>G HeatIn</td><td>W</td></tr><tr><td>HXFRST</td><td></td><td>hot heat exchanger</td><td>3</td><td></td><td></td></tr><tr><td></td><td></td><td>m^2</td><td></td><td></td><td></td></tr><tr><td>sameas 6a</td><td>a Area</td><td></td><td></td><td>3.1843E+05 A lpl</td><td>Pa</td></tr><tr><td>0.8800</td><td>b GasA/A</td><td></td><td>1.7874E-02</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>9.5000E-03 c Length</td><td>m</td><td>2.5615E-02</td><td>C |UI</td><td>m^3/s</td></tr><tr><td>3.8000E-04 d y0</td><td></td><td>m</td><td>-91.519</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>2392.4</td><td>e HeatIn</td><td>W</td><td>G 2377.0</td><td>E Hdot</td><td>W</td></tr><tr><td>950.00</td><td>f Est-T</td><td>K</td><td>(t) -109.41</td><td>F Work</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td>2392.4</td><td>G Heat</td><td>W</td></tr><tr><td>copper</td><td>Solid type</td><td></td><td>781.38 4</td><td>H MetalT</td><td>K</td></tr><tr><td>STKSLAB</td><td>stack</td><td></td><td></td><td></td><td></td></tr><tr><td>sameas 6a</td><td>a Area</td><td>m^2</td><td>3.0688E+05 A lpl</td><td></td><td>Pa</td></tr><tr><td>0.8100</td><td>b GasA/A</td><td></td><td>0.9075</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>7.6200E-02 c Length</td><td></td><td>m</td><td>5.3140E-02</td><td>CIUI</td><td>m^3/s</td></tr><tr><td>1.3000E-04 d y0</td><td></td><td>m.</td><td>-84.938</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>2.5400E-05 e Lplate</td><td></td><td>m</td><td>2377.0</td><td>E Hdot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>590.70</td><td>F Work</td><td>W</td></tr><tr><td></td><td></td><td></td><td>758.28</td><td></td><td>K</td></tr><tr><td>sameas 0</td><td></td><td></td><td>318.27</td><td>G T-beg</td><td>K</td></tr><tr><td>stainless</td><td>Gas type</td><td></td><td>700.11</td><td>H T-end</td><td>W</td></tr><tr><td></td><td>Solid type</td><td></td><td>5</td><td>I StkWrk</td><td></td></tr><tr><td>HXLAST</td><td></td><td>cold heat exchanger</td><td></td><td></td><td></td></tr><tr><td>sameas 6a</td><td>a Area</td><td>m^2</td><td>3.0349E+05</td><td>A lpl</td><td>Pa</td></tr><tr><td>0.7500</td><td>b GasA/A</td><td></td><td>0.8885</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>1.2700E-02 c Length</td><td></td><td>m</td><td>5.7824E-02</td><td>C |U|</td><td>m^3/s</td></tr><tr><td>8.2600E-04 d y0</td><td></td><td>m</td><td>-85.412</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>0.0000</td><td></td><td>W</td><td>(t) 566.12</td><td>E Hdot</td><td>W</td></tr><tr><td></td><td>e HeatIn</td><td>K</td><td>= 5H? 566.12</td><td></td><td>W</td></tr><tr><td>295.00</td><td>f Est-T</td><td></td><td></td><td>F Work</td><td></td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td>-1810.9</td><td>G Heat</td><td>W</td></tr><tr><td>copper</td><td>Solid type</td><td></td><td>295.00</td><td>H MetalT</td><td>K</td></tr><tr><td></td><td></td><td></td><td>6</td><td></td><td></td></tr><tr><td>ISOCONE</td><td>adapter</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>3.1670E-03 a AreaI</td><td>m^2</td><td></td><td>2.9660E+05 A Ipl</td><td>Pa</td></tr><tr><td></td><td>0.1990 b PerimI</td><td>m</td><td></td><td>0.8144 B Ph(p)</td><td>deg</td></tr><tr><td>2.9000E-02 c Length sameas</td><td>d AreaF 8a 8b e PerimF</td><td>m m^2 m</td><td>-86.112 562.55 562.55</td><td>7.0745E-02 C IU| D Ph(U) E Hdot FWork -3.5678 G HeatIn</td><td>m^3/s deg W W W</td></tr><tr><td>ideal Solid type BRANCH sameas 0 ideal</td><td>3.9590E+07 a Re(Zb) Pa-s/m^3 -1.3200E+07 b Im(Zb) Pa-s/m^3 Gas type Solid type</td><td>branch to OPTRs, appearing partly resistive, partly complian</td><td>-91.502 -437.33 -437.33 999.88 8</td><td>2.9660E+05 A lpl 0.8144 B Ph(p) 7.2951E-02 C IUI D Ph(U) E Hdot F Work G Work_B</td><td>Pa deg m^3/s deg W W W</td></tr><tr><td>ISOCONE 2.8200E-03 a AreaI 0.1880 b PerimI 7.3000E-02 c Length 9a sameas 9b sameas sameas 0 ideal</td><td>a little more of the adapter m^2 m m d AreaF m^2 e PerimF m Gas type Solid type</td><td>9</td><td>2.6735E+05 A lpl 1.0419 9.7815E-02 -90.915 -446.54 -446.54 -9.2134</td><td>B Ph(p) C |UI D Ph(U) E Hdot F Work G HeatIn</td><td>Pa deg m^3/s deg W W W</td></tr><tr><td>ISODUCT 2.0270E-03 a Area 0.1600 0.3700 sameas 0 ideal</td><td rowspan="2">b Perim c Length</td><td rowspan="2">long thin duct at ambient temperature m^2 m m</td><td rowspan="2">6622.8 90.229 0.1510 -89.771 -500.00 -500.00 -53.456</td><td rowspan="2">AIpl B Ph(p) C |UI D Ph(U) E Hdot F Work G HeatIn</td><td rowspan="2">Pa deg m^3/s deg W W W</td></tr><tr><td>Gas type Solid type 10 pressure "node", with .500 W coming from a Re(Z) (t) b Im(Z) =10H?</td></tr></table>

MEANFlow mean flow   
0.0000 a U\_m m^3/s 6467.0 A lpl Pa   
90.000 B Ph(p) deg

TITLE segments 1-7 < Bob 9/97; segs 8-14 < Hiller ntbk, pg one, 10/97   
!->stanfrid.out   
!Created@13:58:15 2-Jan-99 with DeltaE Vers. 4.5b7 for the IBM/PC-Compatible

2.9660E+05 a Target =11A? 2.9660E+05 A FreeT   
7A b ResAdr

! The restart information below was generated by a previous run   
! You may wish to delete this information before starting a run   
! where you will (interactively) specify a different iteration   
! mode. Edit this table only if you really know your model!   
INVARS 4 0 2 0 3 0 4 3 5   
TARGS 4 5 6 10 2 11 1 12 1   
SPECIALS 0

## 9.2. Standing-wave refrigerator

This model of part of the standing-wave refrigerator starts near the drivers at one side of the refrigerator shown in Fig. 1.12 and integrates downward, through a stack and its neighboring heat exchangers, ending at the pressure node at the center of the bottom leg of the resonator. The point of view adopted in this particular file is this: In order to have the as-built hardware run with |pi| = 6467 Pa near the drivers and to reach an experimentally observed cold temperature of 285.6 K, what U1, f, and heat load on the cold heat exchanger should occur?

BEGIN Initialize in main duct where drivers are attached   
3.2388E+05 a Mean P Pa -5.2625E-02 A |U|@0 G( 0f) P   
91.650 b Freq. Hz 187.09 B Ph(U)O G( Og) P   
307.80 c T-beg K -32.862 C HeatIn G( 3e) P   
6467.0 d lpl@0 Pa   
90.000 e Ph(p)0 deg   
-5.2625E-02 f |U|@0 m^3/s G   
187.09 g Ph(U)0 deg G   
0.920hear Gas type   
ideal Solid type

<table><tr><td colspan="2"></td><td>5.2625E-02 C |UI 7.0926</td><td>D Ph(U)</td><td>m^3/s deg</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>21.011 21.011 0.0000</td><td>E Hdot F Work G U_m</td><td>W W m^3/s</td></tr><tr><td>ideal</td><td>Solid type</td><td>0.0000</td><td>H H_m </td><td>W</td></tr><tr><td></td><td></td><td>2</td><td></td><td></td></tr><tr><td>INSDUCT</td><td>Pre-stack Duct</td><td></td><td></td><td></td></tr><tr><td>1.8430E-02 a Area</td><td>m^2</td><td>6215.5</td><td>A lpl</td><td>Pa</td></tr><tr><td>0.4813</td><td>b Perim m</td><td>89.766</td><td></td><td></td></tr><tr><td>0.1494 c Length</td><td></td><td></td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>m</td><td>7.1223E-02</td><td>C IUI</td><td>m^3/s</td></tr><tr><td></td><td></td><td>5.1494</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td>21.011</td><td>E Hdot</td><td>W.</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>20.765</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td>0.0000</td><td>G HeatIn</td><td>W</td></tr><tr><td>HXFRST</td><td>Hot Heat exchanger</td><td>3</td><td></td><td></td></tr><tr><td>1.7211E-02 a Area</td><td>m^2</td><td>6154.2</td><td>A lpl</td><td>Pa</td></tr><tr><td>0.5227 b GasA/A</td><td></td><td>89.884</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>1.2700E-02 c Length</td><td>m</td><td>7.2140E-02</td><td>C IUI</td><td>m^3/s</td></tr><tr><td>6.3500E-04 d y0</td><td>m</td><td>4.9381</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>-32.862</td><td>e HeatIn W</td><td>-11.851</td><td>E Hdot</td><td>W</td></tr><tr><td>299.70</td><td>f Est-T K</td><td>19.554</td><td>F Work</td><td>W</td></tr><tr><td></td><td></td><td>-32.862</td><td>G Heat</td><td>W</td></tr><tr><td></td><td></td><td>307.22</td><td>H MetalT</td><td>K</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>0.0000</td><td>I U_m</td><td>m^3/s</td></tr><tr><td>copper</td><td>Solid type</td><td>0.0000</td><td>J H_m</td><td>W</td></tr><tr><td></td><td></td><td>4</td><td></td><td></td></tr><tr><td>STKREct</td><td>rectangular-pore stack</td><td></td><td></td><td>Pa</td></tr><tr><td>1.8824E-02 a Area</td><td>m^2</td><td>5558.2 93.242</td><td>AIpl</td><td>deg</td></tr><tr><td>0.7050 b GasA/A</td><td></td><td>8.6737E-02</td><td>B Ph(p) C|U|</td><td>m^3/s</td></tr><tr><td>0.1524 c Length</td><td>m</td><td>3.8486</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>4.0640E-04 d</td><td>m a</td><td></td><td></td><td>W</td></tr><tr><td>1.1811E-04 e Lplate</td><td>m</td><td>-11.851 2.5538</td><td>E Hdot F Work</td><td>W</td></tr><tr><td>6.3500E-03 f</td><td>b m</td><td></td><td></td><td>K</td></tr><tr><td></td><td></td><td>307.80</td><td>G T-beg</td><td>K</td></tr><tr><td></td><td></td><td>285.60</td><td>H T-end</td><td>W</td></tr><tr><td></td><td></td><td>-17.000</td><td>I StkWrk</td><td></td></tr><tr><td>sameas 0</td><td>Gas type</td><td>0.0000</td><td>J U_m</td><td>m^3/s</td></tr><tr><td>kapton</td><td>Solid type</td><td>0.0000</td><td>K H_m</td><td>W</td></tr><tr><td></td><td></td><td>5</td><td></td><td></td></tr><tr><td>FREETarget first stack thermocouple location</td><td></td><td></td><td></td><td></td></tr><tr><td>307.80</td><td>a Target</td><td>(t) 307.80</td><td>A FreeT</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4G b ResAdr</td><td></td><td>6</td><td></td><td></td></tr></table>

<table><tr><td colspan="6">FREETarget last stack thermocouple location a Target</td></tr><tr><td>285.60 4H b ResAdr HXLAST 1.7211E-02 a Area</td><td>Cold heat exchanger</td><td>= 6A?</td><td>285.60</td><td>A FreeT</td></tr><tr><td>0.9300 b GasA/A 6.3500E-03 c Length 1.0414E-03 d y0 0.0000 e HeatIn 0.0000 f Est-T</td><td>m^2 m m W K</td><td>(t) (t)</td><td>5537.1 93.272 8.7412E-02 3.7945 0.0000 E Hdot</td><td>A lpl Pa B Ph(p) deg C IUI m^3/s D Ph(U) deg W</td></tr><tr><td>sameas 0 copper INSDUCT</td><td>Gas type Solid type From cold hx to bolt flange, + a half</td><td>285.98 8</td><td>2.2065 F Work 11.851 G Heat H MetalT</td><td>W W K</td></tr><tr><td>2.0180E-02 a Area</td><td></td><td></td><td>inch</td><td></td></tr><tr><td></td><td>m^2</td><td></td><td>5229.9</td><td>Pa deg</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>AIpl</td></tr><tr><td>0.5036 b Perim</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>m</td><td></td><td>93.256</td><td>B Ph(p)</td></tr><tr><td>0.1210 c Length</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>m</td><td></td><td>0.1015</td><td>C IUI m^3/s</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>3.6951</td><td>D Ph(U) deg</td></tr><tr><td>sameas 0 Gas type</td><td></td><td></td><td>0.0000</td><td>E Hdot W</td></tr><tr><td></td><td></td><td></td><td>2.0337</td><td>F Work W</td></tr><tr><td>ideal Solid type</td><td></td><td></td><td>0.0000</td><td>G HeatIn W</td></tr><tr><td></td><td></td><td>9</td><td></td><td></td></tr><tr><td>INSDUCT</td><td>Duct, beginning 1/2 in below big bolt</td><td></td><td></td><td></td></tr><tr><td>1.8485E-02 a Area</td><td>m^2</td><td></td><td>flange</td><td></td></tr><tr><td>0.4820 b Perim</td><td></td><td></td><td>4698.8 AIpl</td><td>Pa</td></tr><tr><td>0.1650</td><td>m</td><td></td><td>93.235 B Ph(p)</td><td>deg</td></tr><tr><td></td><td>c Length m</td><td></td><td>0.1177 C IUI</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>3.6063 D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>0.0000 E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td>1.7925 F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td>0.0000 G HeatIn</td><td>W</td></tr><tr><td>INSDUCT</td><td>Elbow, 6 inch diam, 5 inch radius of</td><td>10</td><td></td><td>curvature on centerline</td></tr><tr><td>1.8240E-02 a Area</td><td>m^2</td><td></td><td>3947.2</td><td>Pa</td></tr><tr><td>0.4788</td><td>b Perim</td><td></td><td>Alpl 93.211</td><td>deg</td></tr><tr><td>0.2000</td><td>m</td><td></td><td>B Ph(p)</td><td>m^3/s</td></tr><tr><td></td><td>c Length m</td><td></td><td>0.1346 C |UI</td><td></td></tr><tr><td></td><td></td><td></td><td>3.5336 D Ph(U)</td><td>deg W</td></tr><tr><td></td><td></td><td></td><td>0.0000 E Hdot F Work</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td>1.4961 G HeatIn</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td>11</td><td>0.0000</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>INSDUCT</td><td>straight part of big black cone</td><td></td><td></td><td></td></tr><tr><td>1.8240E-02 a Area</td><td>m^2</td><td></td><td>3582.2 A Ipl</td><td>Pa</td></tr><tr><td></td><td></td><td></td><td>93.200</td><td></td></tr><tr><td>0.4788 b Perim</td><td>m</td><td></td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8.9000E-02 c Length</td><td>m</td><td></td><td>0.1412 C IUI</td><td>m^3/s</td></tr></table>

<table><tr><td>3.5093</td></tr><tr><td>0.0000 E Hdot Gas type 1.3635 F Work sameas 0 0.0000</td></tr><tr><td>W ideal Solid type G HeatIn W</td></tr><tr><td>12 INSCONE The long black plastic cone</td></tr><tr><td>sameas 11a a AreaI m^2 1139.0 A Ipl Pa</td></tr><tr><td>sameas 11b b PerimI 93.164 B Ph(p) deg m 0.3635 c Length 0.1547 C |UI m^3/s m</td></tr><tr><td>d AreaF 3.4614 D Ph(U) sameas 13a m^2</td></tr><tr><td>deg sameas 13b e PerimF 0.0000 E Hdot W m 0.4570 sameas F Work W 0</td></tr><tr><td>Gas type ideal Solid type 0.0000 G HeatIn W</td></tr><tr><td>13</td></tr><tr><td>INSDUCT little straight section of black cone 8.1070E-03 a Area m^2 545.42 A lpl</td></tr><tr><td>Pa 93.178 B Ph(p) deg 0.3192 b Perim m</td></tr><tr><td>5.7200E-02 c Length 0.1551 C |UI m^3/s</td></tr><tr><td>m D Ph(U) deg</td></tr><tr><td>3.4598</td></tr><tr><td>0.0000 E Hdot W</td></tr><tr><td>sameas 0 Gas type 0.2078 F Work W</td></tr><tr><td>ideal Solid type 0.0000 G HeatIn W</td></tr><tr><td>14</td></tr><tr><td>INSDUCT half the white &quot;tee&quot;, up to the symmetry midpoint</td></tr><tr><td>9.8100E-03 a Area m^2 6.4730E-12 A Ipl Pa 0.3511 b Perim 90.016 B Ph(p) deg &#x27;m</td></tr><tr><td>6.3500E-02 c Length m 0.1553 C |U| m^3/s</td></tr><tr><td>3.4592 D Ph(U) deg</td></tr><tr><td>1.0000E-03 d Srough</td></tr><tr><td>0.0000 E Hdot W</td></tr><tr><td>sameas Gas type 3.0183E-14 0 F Work W</td></tr><tr><td>ideal Solid type 0.0000 G HeatIn W</td></tr><tr><td>15 SOFTEND pressure. node</td></tr><tr><td>0.0000 a Re(Z) =15G? 6.4730E-12 A lpl Pa 0.0000 b Im(Z) =15H? 90.016 B Ph(p) deg 0.1553 C |UI m^3/s</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>3.4592</td></tr><tr><td>D Ph(U) deg 0.0000 W</td></tr><tr><td>E Hdot</td></tr><tr><td>3.0183E-14 F Work W</td></tr><tr><td>3.4519E-17 G Re(Z)</td></tr><tr><td></td></tr><tr><td>sameas 0. Gas type 5.7367E-16 H Im(Z)</td></tr><tr><td>ideal Solid type 285.60 I T K</td></tr><tr><td>16</td></tr><tr><td>1</td></tr><tr><td>THERMO properties 1.6667 A gamma</td></tr></table>

758.53 B a m/s   
0.9382 C rho kg/m^3   
3021.9 D c\_P J/kg/K   
0.1252 E KO W/m/K   
2.0110E-05 F mu kg/s/m   
3.5014E-03G beta 1/K   
3.9157E-04 H deltaK m   
2.7285E-04 I deltaN m   
1.0000E+08 J rho\_s kg/m^3   
sameas 0 Gas type 1.0000E+08 K c\_s J/kg/K   
ideal Solid type 1.0000E+08 L Ks W/m/K

! The restart information below was generated by a previous run   
! You may wish to delete this information before starting a run   
! where you will (interactively) specify a different iteration   
! mode. Edit this table only if you really know your model!   
INVARS 3 0 6 0 7 3 5   
TARGS 3 6 1 15 1 15 2   
SPECIALS 0

## 9.3. Traveling-wave engine

This model of the entire traveling-wave engine seems dauntingly complicated, but it is in fact typical of how our models at Los Alamos evolve after many months of interaction between experiments and computations. The model starts near the top of of Fig. 1.14, just above the ambient heat exchanger. It integrates up, left, and down, through the compliance and inertance to the junction. It then starts again just above the ambient heat exchanger, going down through the regenerator and thermal buffer column to reach the junction a second time, where complex ${ \pmb p } _ { 1 }$ must match up. The integration then proceeds through the resonator.

TITLE original, unpublished engine   
!->scotstrp.out   
!Created@14: 3:56 2-Jan-99 with DeltaE Vers. 4.5b7 for the IBM/PC-Compatible   
!-- 0   
BEGIN the setup   
3.1030E+06 a Mean P Pa 80.762 A Freq. G( 0b) P   
80.762 b Freq. Hz G -3.2035E+07 B Re(Zb) G( 1a) P   
302.00 c T-beg K 1.3860E+07 C Im(Zb) G( 1b) P   
.3.1000E+05 d Ip1@0 Pa -1620.9 D HeatIn G(24e) P   
0.0000 e Ph(p)0 deg 3599.7 E HeatIn G(30e) P   
0.0000 f |U1@0 m^3/s 2.4773E-08 F Target G(45a) P   
0.0000 g Ph(U)0 deg   
helium Gas type

<table><tr><td colspan="4">ideal Solid type 1</td></tr><tr><td colspan="4">TBRANCH Split G 3.1000E+05 A lpl G 0.0000 B Ph(p)</td></tr><tr><td colspan="4">-3.2035E+07 a Re(Zb) Pa-s/m^3</td></tr><tr><td colspan="4">1.3860E+07 b Im(Zb) Pa-s/m^3</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">-1263.4 helium Gas type -1263.4 ideal Solid type 1263.4</td></tr><tr><td colspan="4">2 ISODUCT Jetting space (pg 25 book 4) 6.8250E-03 a Area m^2 3.0996E+05 A lpl 1.0637E-02 B Ph(p)</td></tr><tr><td colspan="4">0.2930 b Perim m 1.9100E-02 c Length 1.1083E-02 C IU| m -137.41 -1264.8</td></tr><tr><td colspan="4">3.0000E-04 d Srough helium Gas type stainless Solid type</td></tr><tr><td colspan="4">-1264.8 F Work -1.3376 3 RPNTARGET Calculate jet pump minor loss resistor (pg 26 book 4) 1.5222E+06 A RPNval</td></tr><tr><td colspan="4">1.7000 a Target (t) 1.05 2C * 5a / 5a / 3a * 4 IMPEDANCE Jet pump minor loss Res. (pg 26 book 4 + minor loss notes)</td></tr><tr><td colspan="4">sameas 3A a Re(Zs) Pa-s/m^3 3.2259E+05 A lpl 0.0000 2.0384 B Ph(p) b Im(Zs) Pa-s/m^3 1.1083E-02 C |U| -137.41</td></tr><tr><td colspan="4">D Ph(U) -1358.2 E Hdot helium Gas type -1358.2 F Work ideal Solid type -93.483 G HeatIn 5</td></tr><tr><td colspan="4">ISOCONE Jet pump / estimated dimensions (pg 25 and 97 bk 4) 3.2154E+05 A lpl 1.1400E-04 a AreaI m^2 0.1850 b PerimI 2.4967 B Ph(p) m 1.1294E-02 C |UI|</td></tr><tr><td colspan="4">2.5400E-02 c Length m m^2 -136.37 D Ph(U) 5.8880E-04 d AreaF E Hdot</td></tr><tr><td colspan="4">0.4210 e PerimF -1367.7 m</td></tr><tr><td colspan="4">3.0000E-04 f Srough -1367.7 F Work</td></tr><tr><td colspan="4">helium Gas type -9.4273 G HeatIn stainless</td></tr><tr><td colspan="4">Solid type</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">6</td></tr><tr><td colspan="4">ISODUCT Paddle space above jet pump (pg 27 book 4) 8.1500E-03 a Area m^2</td></tr></table>

<table><tr><td>0.3200 b Perim 6.3500E-03 c Length 3.0000E-04 d Srough</td><td>m m</td><td></td><td>2.4997 B Ph(p) 1.2434E-02 C IUI -130.70 D Ph(U) -1368.2 E Hdot F Work -0.5225</td><td>deg m^3/s deg W</td></tr><tr><td>helium stainless ISODUCT</td><td>Gas type Solid type</td><td>-1368.2 7 180 bend plus brass connecting flange (pg 27 book 4)</td><td>G HeatIn</td><td>W W</td></tr><tr><td>8.1500E-03 a Area 0.3200</td><td>b Perim</td><td>m^2 m</td><td>3.1575E+05 A lpl 2.6691 B Ph(p)</td><td>Pa deg</td></tr><tr><td>0.3480</td><td>c Length</td><td>m</td><td>9.8509E-02 C |UI</td><td>m^3/s</td></tr><tr><td></td><td>6.0000E-04 d Srough</td><td></td><td>-92.484 D Ph(U)</td><td>deg W</td></tr><tr><td></td><td></td><td></td><td>-1396.9 E Hdot</td><td></td></tr><tr><td>helium</td><td>Gas type</td><td></td><td>-1396.9</td><td>F Work W.</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td>-28.728 8</td><td>G HeatIn W</td></tr><tr><td>RPNTARGET 0.5000</td><td></td><td>Calc minor loss resistor for 180 bend</td><td></td><td>(pg 28,52 book 4)</td></tr><tr><td>1.05 7C *</td><td>a Target 8a * 7a / 7a /</td><td>(t)</td><td>778.61</td><td>A RPNval</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IMPEDANCE</td><td></td><td></td><td>9</td><td></td></tr><tr><td>sameas 8A</td><td></td><td></td><td>Minor loss resistor for 180 bend (pg 28 book 4)</td><td></td></tr><tr><td>0.0000</td><td>a Re(Zs) Pa-s/m^3</td><td></td><td>3.1576E+05 A lpl</td><td>Pa</td></tr><tr><td></td><td>b Im(Zs) Pa-s/m^3</td><td></td><td>2.6829</td><td>B Ph(p) deg</td></tr><tr><td></td><td></td><td></td><td></td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>9.8509E-02 C |UI</td><td></td></tr><tr><td></td><td></td><td></td><td>-92.484 D Ph(U)</td><td>deg W</td></tr><tr><td>helium</td><td></td><td></td><td>-1400.7 E Hdot</td><td></td></tr><tr><td>ideal</td><td>Gas type</td><td></td><td>-1400.7 F Work</td><td>W G HeatIn W</td></tr><tr><td></td><td>Solid type</td><td></td><td>-3.7778</td><td></td></tr><tr><td>ISOCONE</td><td></td><td>10</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>4" to 3" Concentric reducer (pg 36 book 4)</td><td></td></tr><tr><td>0.3190</td><td>8.1070E-03 a AreaI b PerimI</td><td>m^2</td><td>3.1113E+05 A Ipl 2.7551 B Ph(p)</td><td>Pa</td></tr><tr><td>0.1020</td><td>c Length</td><td>m</td><td>C 1UI</td><td>deg</td></tr><tr><td>sameas 13a</td><td>d AreaF</td><td>m S=-3</td><td>0.1181</td><td>m^3/s</td></tr><tr><td>0.2390</td><td></td><td>m^2</td><td>-91.644 E Hdot</td><td>D Ph(U) deg</td></tr><tr><td></td><td>e PerimF</td><td>m</td><td>Fnc(10d) -1409.6</td><td>W</td></tr><tr><td>helium</td><td>6.0000E-04 f Srough</td><td></td><td>-1409.6 F Work</td><td>W</td></tr><tr><td></td><td>Gas type</td><td></td><td>-8.8766</td><td>G HeatIn W</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>11</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RPNTARGET</td><td></td><td></td><td>Calculate minor loss resistor for 4" to 3" exp (pg 37 book 4</td><td></td></tr><tr><td>0.2600</td><td></td><td>(t)</td><td></td><td></td></tr><tr><td></td><td>a Target</td><td></td><td>1550.9</td><td>A RPNval</td></tr><tr><td>1.05 10C *</td><td>10d / i0d / 11a *</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>12</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IMPEDANCE</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Minor loss resistor for 4" to 3" expansion (pg 37 book 4)</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>A a Re(Zs) Pa-s/m^3</td><td>3.1114E+05 A lpl</td><td>Pa</td></tr><tr><td>sameas 11A</td><td></td></tr><tr><td>helium ideal</td><td>0.0000 b Im(Zs) Pa-s/m^3 Gas type</td><td>-91.644 -1420.4 -1420.4 13</td><td>2.7887 B Ph(p) 0.1181 CIUI D Ph(U) E Hdot F Work. G HeatIn</td><td>deg m^3/s deg W W</td></tr><tr><td>ISODUCT 4.5600E-03 a Area 0.2390 0.2600</td><td>Solid type 3" FB Duct - Length given : m^2 b Perim m. c. Length m</td><td>S=-2 Fnc(13a)</td><td>-10.822 in concept.skf 2.9173E+05 A lpl 3.0672 B Ph(p) 0.1533 C |UI -90.650 -1449.9 -1449.9 -29.529</td><td>W Pa deg m^3/s</td></tr><tr><td>helium stainless</td><td>3.0000E-04 d Srough Gas type Solid type</td><td>14 Calc minor loss resistor for 1/2 of elbow (pg 37,52 book 4)</td><td>D Ph(U) E Hdot F Work G HeatIn</td><td>deg W W W</td></tr><tr><td>RPNTARGET 0.1700 1.05 13C * IMPEDANCE</td><td>a Target 16a / 16a / 14a *</td><td>(t) 15 Minor loss resistor for 1/2 of elbow (pg 37 book 4)</td><td>1316.1 A RPNval 2.9174E+05 A Ipl</td><td>Pa</td></tr><tr><td>sameas 14A 0.0000 helium ideal</td><td>a Re(Zs) Pa-s/m^3 b Im(Zs) Pa-s/m^3 Gas type Solid type</td><td>-1465.4 -1465.4 16</td><td>3.1067 B Ph(p) 0.1533 C|U| -90.650 D Ph(U) E Hdot F Work.. -15.469 G HeatIn</td><td>deg m^3/s deg W W W</td></tr><tr><td>ISOCONE</td><td></td><td></td><td></td><td>Pa deg m^3/s deg</td></tr><tr><td></td><td></td><td>(t)</td><td></td><td>W</td></tr><tr><td></td><td></td><td>17</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>Long radius reducing elbow (pg 36 book 4)</td></tr><tr><td></td><td>3.5" to 3"</td><td></td><td></td><td></td></tr><tr><td>sameas 13a</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a AreaI</td><td>m^2 S=-2</td><td></td><td></td></tr><tr><td>0.2390</td><td></td><td>Fnc(16a)</td><td>2.7526E+05 A lpl</td><td></td></tr><tr><td></td><td>b PerimI</td><td>m</td><td></td><td>B Ph(p)</td></tr><tr><td>0.2090</td><td></td><td></td><td>3.3339</td><td></td></tr><tr><td></td><td>c Length</td><td>m</td><td>0.1845</td><td>C IUI</td></tr><tr><td></td><td>6.2070E-03 d AreaF</td><td>m^2</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>-90.038</td><td>D Ph(U)</td></tr><tr><td></td><td>0.2790 e PerimF</td><td>m</td><td>-1493.7 -1493.7</td><td>E Hdot</td></tr><tr><td></td><td>6.0000E-04 f Srough</td><td></td><td></td><td>F Work</td></tr><tr><td>helium</td><td></td><td></td><td></td><td>W G HeatIn</td></tr><tr><td></td><td>Gas type Solid type</td><td></td><td>-28.310</td><td>W</td></tr><tr><td>stainless</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RPNTARGET</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Calc minor loss resistor for 2nd 1/2 of elbow (pg 37 book 4)</td><td></td></tr><tr><td>0.1700</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a Target</td><td></td><td></td><td>A RPNval</td></tr><tr><td></td><td></td><td></td><td>854.91</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.05 16C *</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>16d / 16d / 17a *</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>18</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>Minor loss resistor for 2nd 1/2 of elbow (pg 37 book 4)</td><td></td><td></td></tr><tr><td>IMPEDANCE</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>2.7527E+05 A lpl Pa</td></tr><tr><td>sameas 17A</td><td></td></tr><tr><td>0.0000</td><td>b Im(Zs) Pa-s/m^3</td><td>3.3667</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td>0.1845 -90.038</td><td>C IUI D Ph(U)</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td></td><td>deg</td></tr><tr><td></td><td></td><td>-1508.3</td><td>E Hdot</td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td>-1508.3</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td>-14.554</td><td>G HeatIn</td><td>W</td></tr><tr><td>ISODUCT</td><td>FB connector/part of tee (Pg 55 book 4 concept.skf)</td><td>19</td><td></td><td></td></tr><tr><td>6.2070E-03 a Area</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>m^2</td><td>2.6989E+05 A lpl</td><td></td><td>Pa</td></tr><tr><td>0.2790 b Perim</td><td>m</td><td>3.4386</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>7.0000E-02 c Length</td><td>m</td><td>0.1962</td><td>C IUI</td><td>m^3/s</td></tr><tr><td>6.0000E-04 d Srough</td><td></td><td>-89.848</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>helium</td><td></td><td>-1517.5</td><td>E Hdot</td><td>W</td></tr><tr><td>stainless</td><td>Gas type</td><td>-1517.5</td><td>F Work</td><td>W</td></tr><tr><td></td><td>Solid type</td><td>-9.2787 20</td><td>G HeatIn</td><td>W</td></tr><tr><td>RPNTARGET</td><td>Calc minor loss resistor for FB-Res</td><td>(pg</td><td>53-55 book 4)</td><td></td></tr><tr><td>0.3400</td><td></td><td>2053.6</td><td></td><td></td></tr><tr><td></td><td>a Target</td><td>(t)</td><td>A RPNval</td><td></td></tr><tr><td></td><td>1.05 39C SQRD *,19C / 48a / 48a / 20a *</td><td></td><td></td><td></td></tr><tr><td>IMPEDANCE</td><td></td><td>21</td><td></td><td></td></tr><tr><td>sameas 20A</td><td>Minor loss resistor for FB to resonator junction</td><td></td><td></td><td></td></tr><tr><td>0.0000</td><td>a Re(Zs) Pa-s/m^3</td><td></td><td>2.6992E+05 A lpl</td><td>Pa</td></tr><tr><td></td><td>b Im(Zs) Pa-s/m^3</td><td>3.5240</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td>0.1962</td><td>C|UI</td><td>m^3/s</td></tr><tr><td></td><td></td><td>-89.848</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>helium</td><td></td><td>-1557.1</td><td>E Hdot</td><td>W</td></tr><tr><td>ideal</td><td>Gas type</td><td>-1557.1</td><td>F Work</td><td>W</td></tr><tr><td></td><td>Solid type</td><td>-39.515 22</td><td>G HeatIn</td><td>W</td></tr><tr><td>SOFTEND</td><td>End of feedback branch</td><td></td><td></td><td></td></tr><tr><td>0.0000</td><td>a Re(Z) (t)</td><td>2.6992E+05 A lpl</td><td></td><td>Pa</td></tr><tr><td>0.0000</td><td>b Im(Z)</td><td>(t) 3.5240</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td>0.1962</td><td>C IUI</td><td>m^3/s</td></tr><tr><td></td><td></td><td>-89.848</td><td>D Ph(U)</td><td></td></tr><tr><td></td><td></td><td>-1557.1</td><td></td><td>deg</td></tr><tr><td></td><td></td><td></td><td>E Hdot</td><td>W</td></tr><tr><td></td><td></td><td>-1557.1</td><td>F Work</td><td>W</td></tr><tr><td>helium</td><td></td><td>-9.9306E-02</td><td>G Re(Z)</td><td></td></tr><tr><td></td><td>Gas type</td><td>1.6856</td><td>H Im(Z)</td><td></td></tr><tr><td>ideal</td><td>Solid type</td><td>302.00</td><td>I T</td><td>K</td></tr><tr><td>ISODUCT</td><td></td><td>23 Dummy duct used to get input properties</td><td></td><td></td></tr><tr><td>1.0000</td><td>a Area m^2</td><td></td><td>3.1000E+05 A Ipl</td><td>Pa</td></tr><tr><td>1.0000</td><td>b Perim m</td><td></td><td>0.0000 B Ph(p)</td><td>deg</td></tr><tr><td>0.0000</td><td>c Length</td><td></td><td>8.8813E-03 C |UI</td><td>m^3/s</td></tr><tr><td></td><td>m</td><td></td><td></td><td></td></tr><tr><td>0.0000</td><td>d Srough</td><td>23.395</td><td>D Ph(U)</td><td>deg</td></tr></table>

<table><tr><td>helium</td><td>Gas type</td><td></td><td>1263.4 1263.4</td><td>E Hdot F Work</td><td>W W</td><td></td></tr><tr><td>ideal TXFRST</td><td>Solid type 6.6580E-03 a Area</td><td></td><td>24 Main room temp water HX (pg 90 book 3)</td><td>0.0000</td><td>G. HeatIn</td><td>W</td></tr><tr><td></td><td></td><td>m^2</td><td></td><td>3.1008E+05 A Ipl</td><td></td><td>Pa</td></tr><tr><td></td><td>0.2275 b GasA/A</td><td></td><td></td><td>-5.7858E-02 B Ph(p)</td><td></td><td>deg</td></tr><tr><td>2.0400E-02 c Length</td><td></td><td>m</td><td></td><td>8.4615E-03 C IUI</td><td></td><td>m^3/s</td></tr><tr><td>1.2700E-03 d radius</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-1620.9</td><td></td><td>m</td><td></td><td>17.266</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>300.00</td><td>e HeatIn</td><td>W</td><td>G</td><td>-357.45</td><td>E Hdot</td><td>W</td></tr><tr><td>helium</td><td>f Est-T</td><td>K</td><td>(t)</td><td>1252.4</td><td>F Work</td><td>W</td></tr><tr><td>stainless</td><td>Gas type</td><td></td><td></td><td>-1620.9</td><td>G Heat</td><td>W</td></tr><tr><td>STKDUCT</td><td>Solid type</td><td></td><td></td><td>268.66</td><td>H MetalT</td><td>K</td></tr><tr><td></td><td></td><td></td><td>25</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>Regen cold end dead space due to ribs (pg 91 book 3)</td><td></td><td></td></tr><tr><td></td><td>4.9700E-03 a Area</td><td>m^2</td><td></td><td>3.1008E+05 A Ipl</td><td></td><td>Pa</td></tr><tr><td></td><td>0.7400 b Perim</td><td>m</td><td></td><td>-6.0230E-02 B Ph(p)</td><td></td><td>deg</td></tr><tr><td></td><td>3.1750E-03 c Length</td><td>m</td><td></td><td>8.3289E-03 C |U|</td><td></td><td>m^3/s</td></tr><tr><td></td><td>2.7000E-02 d WallA</td><td>m^2</td><td></td><td>14.079</td><td></td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>-357.45</td><td>D Ph(U)</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>E Hdot</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td>1252.2.</td><td>F Work</td><td></td></tr><tr><td>helium</td><td></td><td></td><td></td><td>302.00</td><td>G T-beg</td><td>K K</td></tr><tr><td>stainless</td><td>Gas type Solid type</td><td></td><td></td><td>314.90 -0.1465</td><td>H T-end I StkWrk</td><td>W</td></tr><tr><td>6.2070E-03 a Area</td><td>STKSCREEN Regenerator</td><td>(pg 92 book 3)</td><td>26</td><td>(Ks frac est:pg 20 book 4)</td><td></td><td></td></tr><tr><td></td><td>0.7190 b VolPor</td><td>m^2</td><td></td><td>2.7522E+05 A lpl 3.7737 B Ph(p)</td><td></td><td>Pa deg</td></tr><tr><td></td><td>7.3000E-02 c Length</td><td>m</td><td></td><td>3.2050E-02 C IUI</td><td></td><td>m^3/s</td></tr><tr><td></td><td>4.2200E-05 d r_H</td><td>m</td><td></td><td>-39.852</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td>0.3000 e KsFrac</td><td></td><td></td><td>-357.45</td><td>E Hdot</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td>3192.5</td><td>F Work</td><td>W</td></tr><tr><td>helium</td><td></td><td></td><td></td><td>314.90</td><td>G T-beg</td><td>K</td></tr><tr><td></td><td>Gas type</td><td></td><td></td><td>1000.0</td><td></td><td>K</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td></td><td>1940.3</td><td>H T-end I StkWrk</td><td>W</td></tr><tr><td></td><td></td><td></td><td>27</td><td></td><td></td><td></td></tr><tr><td>RPNTARGET 1000.0</td><td>Fix hot end</td><td>gas temperature</td><td></td><td></td><td></td><td></td></tr><tr><td>26H</td><td>a Target</td><td></td><td>=27A?</td><td>1000.0</td><td>A RPNval</td><td></td></tr><tr><td></td><td></td><td></td><td>28</td><td></td><td></td><td></td></tr><tr><td>RPNTARGET</td><td></td><td></td><td></td><td>Estimated heat leak through FiberFrax</td><td>(pg 22 book 4)</td><td></td></tr><tr><td>0.0000</td><td>a Target</td><td></td><td>(t)</td><td>282.63</td><td>A RPNval</td><td></td></tr><tr><td></td><td>26H 273 - 1.89 * 26H 273 - 1.11E-4 * 0.125 + *</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>29</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>INSDUCT</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>All regen hot end dead space (pg 92 book 3)(area is avg)</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></table>

<table><tr><td>4.6200E-03 a Area 2.0000 b Perim 8.7000E-03 c Length 6.0000E-04 d Srough helium Gas type</td></tr><tr><td>m^2 m 3.7669 B Ph(p) 3.2811E-02 C |UI m -41.385 D Ph(U) -357.45 E Hdot 3183.7 F Work Solid type 0.0000 G HeatIn 30 HHX (pg 93 book 4) heat xfer area used/not acoustic area</td></tr><tr><td>W stainless W HXMIDL 5.6970E-03 a Area m^2 2.7515E+05 A lpl Pa 3.7634 B Ph(p) deg 0.9867 b GasA/A 6.3500E-03 c Length m 3.3501E-02 C |UI m^3/s 7.9400E-04 d y0 -42.982 D Ph(U) deg m 3599.7 e HeatIn W G 3242.3 E Hdot W 900.00 f Est-T K (t) 3158.2 F Work W helium 3599.7 G Heat Gas type W stainless Solid type 1095.0 H MetalT K 31</td></tr><tr><td>STKDUCT hhx dead space (pg 94 book 3) stainless used for Qdot 5.4400E-03 a Area m^2 2.7514E+05 A lpl Pa 0.2620 b Perim m 3.7610 B Ph(p) deg 3.6830E-03 c Length m 3.3896E-02 C|U| m^3/s 4.0540E-03 d WallA m^2 -43.616 D Ph(U) deg 3242.3 E Hdot W</td></tr><tr><td>3157.7 F Work W 1000.0 G T-beg K helium Gas type 995.76 H T-end K stainless Solid type -0.5036 I StkWrk W 32 STKDUCT Straight section of pulse tube (pg 101 bk 4) 6.2070E-03 a Area m^2 S=-2 2.7477E+05 A lpl Pa 0.2790 b Perim m Fnc(32a) 3.7072 B Ph(p) deg 8.0000E-02 c Length m 4.4652E-02 C |UI m^3/s 1.1600E-03 d WallA m^2 -55.409 D Ph(U) deg E Hdot W</td></tr><tr><td>3242.3 3148.9 F Work W 995.76 G T-beg K helium Gas type 748.68 H T-end K stainless Solid type -8.8289 I StkWrk W 33 STKCONE Taperred section of pulse tube (pg 101 bk 4) sameas 32a a AreaI m^2 2.7272E+05 A Ipl Pa sameas 32b b PerimI m^2 3.5274 B Ph(p) deg 0.1600 c Length m 7.1159E-02 C |UI m^3/s</td></tr></table>

<table><tr><td>0.3048 e PerimF 1.1400E-02 f f_wall .Gas type</td><td>m</td><td rowspan="2">Fnc(33d) 34</td><td rowspan="2">3242.3 3145.1 748.68 296.41 -3.7294</td><td rowspan="2">E Hdot F Work G T-beg H T-end I StkWrk</td><td rowspan="2">W W K K W</td></tr><tr><td>helium stainless TXLASt</td><td>Solid type</td></tr><tr><td>6.6580E-03 a Area 0.2690 b GasA/A 1.0160E-02 c Length 2.2860E-03 d radius -250.00 290.00 sameas 0 ideal</td><td>Small water Xger m^2 m. m e HeatIn W f Est-T K Gas type Solid type</td><td>(t) =34H? 35</td><td>-67.707 3140.1 3140.1 -102.14 290.00</td><td>2.7167E+05 A Ipl 3.4652 BPh(p) 7.1632E-02 C |UI D Ph(U) E Hdot F Work G Heat H MetalT</td><td>Pa deg m^3/s deg W W W K</td></tr><tr><td>ISODUCT 6.2070E-03 a Area 5.1000E-02 c Length 6.0000E-04 d Srough</td><td>PT connector 0.2790 b Perim</td><td>(see pg 55 book 4 and concept.skf) m^2 m m</td><td>-69.683 3137.4</td><td>2.7015E+05 A Ipl 3.3628 B Ph(p) 7.9654E-02 C IUI D Ph(U) E Hdot</td><td>Pa deg m^3/s deg W</td></tr><tr><td>helium stainless RPNTARGET</td><td>Gas type Solid type Calc velocity in after union for minor loss</td><td></td><td>3137.4 36 (t)</td><td>F Work -2.7235 G HeatIn 0.2723 A RPNval</td><td>W W</td></tr><tr><td>0.0000 RPNTARGET 0.6700 a Target</td><td>a Target 35D 22D - COS 35C * 22C + SQRD 35D 22D - SIN 35C * SQRD + SQRT Calc minor loss resistor for PT to resonantor (pg 45 book 4)</td><td>37 (t)</td><td>9966.4</td><td>A RPNval</td><td></td></tr><tr><td>IMPEDANCE sameas 37A 0.0000</td><td>1.05 36A SQRD * 35C / 48a / 48a / 37a * Minor loss resistor for PT-Res (pg 53-55 book 4) a Re(Zs) Pa-s/m^3 b Im(Zs) Pa-s/m^3</td><td>38</td><td></td><td>2.6992E+05 A lpl 3.5240 B Ph(p)</td><td>Pa deg</td></tr><tr><td></td><td></td><td></td><td></td><td>7.9654E-02 C |UI</td><td>m^3/s</td></tr><tr><td>2.6992E+05 b IplEnd</td><td></td><td></td><td>3105.8</td><td>F Work</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>3105.8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>-69.683 D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>helium</td><td></td><td></td><td></td><td>E Hdot</td><td>W</td></tr><tr><td></td><td>Gas type</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>W</td></tr><tr><td>ideal</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Solid type</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>-31.617 G HeatIn</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>39</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UNION</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Rejoin</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>2.6992E+05 A lpl</td><td>Pa</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>3.5240 B Ph(p)</td><td>deg</td></tr><tr><td></td><td>a TendSg</td><td></td></table>

<table><tr><td>3.5240</td><td>c Ph(p)E</td><td>deg</td><td>=39B?</td><td>0.2723 -84.061</td><td>C |U| D Ph(U)</td><td>m^3/s deg</td></tr><tr><td></td><td></td><td></td><td></td><td>1548.7</td><td>E Hdot</td><td>W</td></tr><tr><td>helium ideal</td><td>Gas type</td><td></td><td></td><td>1548.7 0.0000</td><td>F Work G HeatIn</td><td>W W</td></tr><tr><td></td><td>Solid type</td><td></td><td>40</td><td></td><td></td><td></td></tr><tr><td>ISODUCT</td><td>Section of 3.5&quot; tee</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6.2070E-03 a Area</td><td></td><td>m^2</td><td></td><td>2.5893E+05 A lpl</td><td></td><td>Pa</td></tr><tr><td></td><td>0.2790 b Perim</td><td>m</td><td></td><td>3.4433</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>9.5300E-02 c Length</td><td>m</td><td></td><td>0.2878</td><td>C |UI</td><td>m^3/s</td></tr><tr><td></td><td>6.0000E-04 d Srough</td><td></td><td></td><td>-84.211</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>1524.8</td><td>E Hdot</td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>1524.8</td><td>F Work</td><td>W</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td>41</td><td>-23.965</td><td>G HeatIn</td><td>W</td></tr><tr><td>RPNTARGET 2.0000E-02 a Target</td><td> Calc minor loss resistor for 3.5&quot; to</td><td></td><td></td><td>4&quot;</td><td>adapt (pg 93 bk 4)</td><td></td></tr><tr><td></td><td>1.05 39C * 43a / 43a / 41a *</td><td></td><td>(t)</td><td>148.44</td><td>A RPNval</td><td></td></tr><tr><td>IMPEDANCE</td><td></td><td></td><td>42</td><td></td><td></td><td></td></tr><tr><td>sameas 41A</td><td></td><td></td><td></td><td>Minor loss resistor for 3.5&quot; to 4&quot; adapter (pg 93 bk 4)</td><td></td><td></td></tr><tr><td>0.0000</td><td></td><td>a Re(Zs) Pa-s/m^3</td><td></td><td>2.5893E+05 A Ipl</td><td></td><td>Pa</td></tr><tr><td></td><td></td><td>b Im(Zs) Pa-s/m^3</td><td></td><td>3.4527 B Ph(p)</td><td></td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>0.2878</td><td>C |U|</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td></td><td>-84.211</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>1518.6</td><td>E Hdot</td><td>W</td></tr><tr><td>helium</td><td></td><td></td><td></td><td>1518.6</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Gas type</td><td></td><td></td><td>-6.1459</td><td>G HeatIn</td><td>W</td></tr><tr><td></td><td>Solid type</td><td></td><td>43</td><td></td><td></td><td></td></tr><tr><td>ISOCONE</td><td>3.5&quot; to 4&quot;</td><td></td><td></td><td>cone to adapt to resonator (pg 93 book 4)</td><td></td><td></td></tr><tr><td></td><td>6.2070E-03 a AreaI</td><td>m^2</td><td></td><td>2.4783E+05 A Ipl</td><td></td><td>Pa</td></tr><tr><td>0.2790</td><td>)b PerimI</td><td>m</td><td></td><td>3.3664</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>0.1040</td><td>c Length</td><td>m</td><td></td><td>0.3062</td><td>C|U|</td><td>m^3/s</td></tr><tr><td></td><td>8.1070E-03 d AreaF</td><td>m^2</td><td></td><td>-84.371</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td>0.3200 e PerimF</td><td>m</td><td></td><td>1498.3</td><td>E Hdot</td><td>W W</td></tr><tr><td></td><td>3.0000E-04 f Srough</td><td></td><td></td><td>1498.3</td><td>F Work</td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>-20.290</td><td>G HeatIn</td><td></td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>44</td><td></td><td></td><td></td></tr><tr><td>ISODUCT</td><td>Initial section of resonator</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>8.1070E-03 a Area</td><td>m^2</td><td></td><td>2.4233E+05 A Ipl</td><td></td><td>Pa</td></tr><tr><td></td><td>0.3200 b Perim</td><td>m</td><td></td><td>3.3234</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>5.6000E-02 c Length</td><td>m</td><td></td><td>0.3172</td><td>C IUI</td><td>m^3/s</td></tr><tr><td></td><td>6.0000E-04 d Srough</td><td></td><td></td><td>-84.459</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>1487.4</td><td>E Hdot</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>1487.4</td><td>F Work</td><td>W</td></tr></table>

<table><tr><td>stainless</td><td>Solid type</td><td>-10.941</td><td>G HeatIn W</td></tr><tr><td>RPNTARGET Guess at 1/Re[Zbranch]</td><td>45</td><td colspan="2">2.4773E-08 A RPNval</td></tr><tr><td>2.4773E-08 a Target 45a</td><td>G 46</td><td></td><td></td></tr><tr><td>RPNTARGET 0.0000 a Target 1 45A /</td><td>Calculate Zbranch (t) 47</td><td>4.0367E+07 A RPNval</td><td></td></tr><tr><td>BRANCH sameas 46A 0.0000</td><td>a Re(Zb) Pa-s/m^3 b Im(Zb) Pa-s/m^3</td><td>RC dissipator - Imaginary part is not set yet 2.4233E+05 A Ipl 3.3234 B Ph(p) 0.3170 C IUI</td><td>Pa deg m^3/s</td></tr><tr><td>helium</td><td></td><td>-85.543 D Ph(U) 760.02 E Hdot</td><td>deg W</td></tr><tr><td>ideal</td><td>Gas type Solid type</td><td>760.02 F Work 727.38 48</td><td>W G Work_B W</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>ISODUCT</td><td>Continuation of resonator</td><td></td><td></td></tr><tr><td>sameas 44a</td><td>a Area m^2</td><td>1.4307E+04 A Ipl</td><td>Pa</td></tr><tr><td>0.3189</td><td>b Perim</td><td>-172.90 B Ph(p)</td><td>deg</td></tr><tr><td>1.8500</td><td>m</td><td>0.4990 C |U|</td><td>m^3/s</td></tr><tr><td>sameas 44d</td><td>c Length m</td><td>-86.201 D Ph(U)</td><td></td></tr><tr><td></td><td>d Srough</td><td>205.31 E Hdot</td><td>deg W</td></tr><tr><td>helium</td><td></td><td>205.31 F Work</td><td>W</td></tr><tr><td>stainless</td><td>Gas type Solid type</td><td>-554.71</td><td>G HeatIn W</td></tr><tr><td>RPNTARGET</td><td>49 Calc length of 7deg cone (pg</td><td>87 book 4)</td><td></td></tr><tr><td>0.0000 .2545 4 48a * 3.14159 / sqrt - .1223 /</td><td>a Target (t)</td><td>1.2502</td><td>A RPNval</td></tr><tr><td>RPNTARGET</td><td>50</td><td></td><td></td></tr><tr><td>0.1200</td><td>Calc minor loss coeff for 7 deg diffuser a Target (t)</td><td>956.71</td><td>A RPNval</td></tr><tr><td></td><td>1.05 48C * 48a / 48a / 50a *</td><td></td><td></td></tr><tr><td></td><td>-51</td><td></td><td></td></tr><tr><td></td><td>IMPEDANCE Minor loss resistor for 7 deg diffuser</td><td></td><td></td></tr><tr><td></td><td>sameas 50A a Re(Zs) Pa-s/m^3</td><td>1.4287E+04 A lpl</td><td>Pa</td></tr><tr><td></td><td>0.0000 b Im(Zs) Pa-s/m^3</td><td>-174.82 B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0.4990 C|UI</td><td>m^3/s</td></tr><tr><td></td><td></td><td>-86.201 D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td>86.188 E Hdot</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>helium</td><td>Gas type</td><td>86.188 F Work</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>52</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>-119.13</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>ideal</td><td></td><td></td><td>W</td></tr><tr><td></td><td></td><td></td><td>G HeatIn</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Solid type</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="6">7 degree cone - 10.02&quot; final diameter</td></tr><tr><td>ISOCONE sameas 48a</td><td>a AreaI</td><td>m^2</td><td>S=-2</td><td>8.6185E+04 A lpl</td><td></td><td>Pa</td></tr><tr><td>0.3194</td><td>b PerimI</td><td>m</td><td>Fnc(52a)</td><td>-176.16</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>sameas 49A</td><td>c Length</td><td>m</td><td></td><td>0.2661</td><td>C |U|</td><td>m^3/s</td></tr><tr><td>5.0870E-02 d AreaF</td><td></td><td>m^2</td><td></td><td>-86.205</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>0.8000</td><td>e PerimF</td><td>m</td><td></td><td>9.6170</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 48d</td><td>f Srough</td><td></td><td></td><td>9.6170</td><td>F Work</td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>-76.571</td><td>G HeatIn</td><td>W</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td>53</td><td></td><td></td><td></td></tr><tr><td>ISODUCT</td><td>10&quot; duct</td><td></td><td></td><td>P8</td><td></td><td></td></tr><tr><td>5.0870E-02 a Area</td><td></td><td>m^2</td><td></td><td>8.9816E+04 A lpl</td><td></td><td>Pa</td></tr><tr><td>0.8000</td><td>b Perim</td><td>m</td><td></td><td>-176.16</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>0.4088</td><td>c Length</td><td>m</td><td></td><td>8.5729E-02 C |UI</td><td></td><td>m^3/s</td></tr><tr><td>sameas 48d</td><td>d Srough</td><td></td><td></td><td>-86.206</td><td>DPh(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>3.0371</td><td>E Hdot</td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>3.0371</td><td>F Work</td><td>W</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td></td><td>-6.5799</td><td>G HeatIn</td><td>W</td></tr><tr><td>ISODUCT</td><td></td><td></td><td>54</td><td></td><td></td><td></td></tr><tr><td>5.0870E-02 a Area</td><td>10&quot; duct</td><td>m^2</td><td></td><td>9.0079E+04 A Ipl</td><td></td><td>Pa</td></tr><tr><td></td><td>0.8000 b Perim</td><td>m</td><td></td><td>-176.16</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>7.6200E-02 c Length</td><td>m</td><td></td><td>5.1487E-02 C |UI]</td><td></td><td>m^3/s</td></tr><tr><td>sameas 48d d Srough</td><td></td><td></td><td></td><td>-86.206</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>1.8215</td><td>E Hdot</td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>1.8215</td><td>F Work</td><td>W</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td></td><td>-1.2156</td><td>G HeatIn</td><td>W</td></tr><tr><td></td><td></td><td></td><td>55</td><td></td><td></td><td></td></tr><tr><td>ISODUCT</td><td>ellipsoidal head</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>5.0870E-02 a Area</td><td>m^2</td><td></td><td>9.0227E+04 A Ipl</td><td></td><td>Pa</td></tr><tr><td>0.8000</td><td>b Perim</td><td>m</td><td></td><td>-176.16</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>0.1143</td><td>c Length</td><td>m</td><td></td><td>5.1221E-07 C |UI</td><td></td><td>m^3/s</td></tr><tr><td>sameas 48d</td><td>d Srough</td><td></td><td></td><td>94.624</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>3.1683E-04 E Hdot</td><td></td><td>W</td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td>3.1683E-04 F Work</td><td></td><td>W</td></tr><tr><td>stainless</td><td>Solid type</td><td></td><td>56</td><td>-1.8212</td><td>G HeatIn</td><td>W</td></tr><tr><td>HARDEND</td><td>end of duct</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.0.0000</td><td>a R(1/Z)</td><td></td><td>=56G?</td><td>9.0227E+04 A lpl</td><td></td><td>Pa</td></tr><tr><td>0.0000</td><td>b I(1/Z)</td><td></td><td>=56H?</td><td>-176.16</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>5.1221E-07 C |UI</td><td></td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>94.624 D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>3.1683E-04 E Hdot</td><td></td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td>3.1683E-04 F Work</td><td></td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>7.8115E-09 G R(1/Z)</td><td></td></tr></table>

helium Gas type -5.6968E-07 H I(1/Z)   
stainless Solid type 296.41 I T K   
57   
RPNTARGET Stirling figure of merit based on metal temperatures   
0.0000 a Target (t) 0.5447 A RPNval   
39F 30G 28A + / 30H \* 30H 293 - /   
58   
RPNTARGET System figure of merit based on metal temperatures   
0.0000 a Target (t) 0.2558 A RPNval   
47G 30G 28A + / 30H \* 30H 293 - /   
! The restart information below was generated by a previous run   
! You may wish to delete this information before starting a run   
! where you will (interactively) specify a different iteration   
! mode. Edit this table only if you really know your model!   
INVARS 6 0 2 1 1 1 2 24 5 30 5 45 1   
TARGS 6 27 1 34 6 39 2 39 3 56 1 56 2   
SPECIALS 6 10 -3 13 -2 16 -2 32 -2 33 -3 52 -2

## 9.4. Traveling-wave refrigerator

Cryenco is presently unwilling to share construction details of the refrigerator of Fig. 1.15 publicly, so this model only covers the LRC network at the top of Fig. 1.16. The model starts in the compliance and ends just above the hot heat exchanger at the top of the pulse tube. The point of view adopted in this particular file is this: In order to achieve the values of p1 (both magnitude and phase) in the compliance and at the top of the pulse tube that were observed in a certain experiment, what must the flow resistances of the two valves be? One of those resistances has turned out to be negative, indicating an error in the model—perhaps DeltaE's estimate of turbulent effects in the inertance is inaccurate.

TITLE LRC network only   
!->ptrstrp.out   
!Created@14:10:27 2-Jan-99 with DeltaE Vers. 4.5b7 for the IBM/PC-Compatible   
0   
BEGIN at compliance!   
3.1114E+06 a Mean P Pa 6.4274E+06 A Re(Zb) G( 2a) P   
42.000 b Freq. Hz 2.8415E+06 B Im(Zb) G( 2b) P   
305.20 c T-beg K 2.2699E+07 C Re(Zs) G( 4a) P   
9.3205E+04 d lp1@0 Pa -1.4258E+05 D Re(Zs) G( 9a) P   
-153.30 e Ph(p)0 deg   
0.0000 f |U|@0 m^3/s   
0.0000 g Ph(U)0 deg   
helium Gas type   
ideal Solid type

<table><tr><td colspan="2">COMPLIANCE reserv. vol.</td><td colspan="3"></td></tr><tr><td colspan="2">0.3000 a SurfAr 9.8100E-03 b Volum</td><td>9.3205E+04 A Ipl -153.30</td><td>B Ph(p)</td><td>Pa</td></tr><tr><td colspan="2">m^3</td><td>4.6530E-02 C |UI</td><td></td><td>deg m^3/s</td></tr><tr><td colspan="2"></td><td>116.57</td><td>D Ph(U)</td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td>deg</td></tr><tr><td colspan="2"></td><td>-4.7356</td><td>E Hdot</td><td>W</td></tr><tr><td colspan="2">sameas Gas type 0</td><td>-4.7356</td><td>F Work</td><td>W</td></tr><tr><td colspan="2">ideal Solid type</td><td>-4.7356 2</td><td>G HeatIn</td><td>W</td></tr><tr><td colspan="2">TBRANCH to bypass path</td><td colspan="3"></td></tr><tr><td colspan="2">6.4274E+06 a Re(Zb) Pa-s/m^3</td><td colspan="3">G</td></tr><tr><td>2.8415E+06 b Im(Zb) Pa-s/m^3</td><td></td><td>9.3205E+04 A lpl</td><td></td><td>Pa</td></tr><tr><td></td><td>G</td><td>-153.30</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td>1.3263E-02 C |UI</td><td></td><td>m^3/s</td></tr><tr><td></td><td></td><td>-177.15</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td>565.31</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>565.31</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td>-570.05 3</td><td>G Work_T</td><td>W</td></tr><tr><td colspan="3">ISODUCT nuisance inertance</td><td></td><td></td></tr><tr><td>3.4000E-04 a Area</td><td>m^2</td><td>8.0592E+04 A |pl</td><td></td><td>Pa</td></tr><tr><td>6.5400E-02 b Perim</td><td>m</td><td>173.61</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>1.0000 c Length m</td><td></td><td>1.3511E-02 C IU|</td><td>m^3/s</td></tr><tr><td>3.0000E-04 d Srough</td><td></td><td>176.46</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td>543.77</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>543.77</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td>-21.545</td><td>G HeatIn</td><td>W</td></tr><tr><td></td><td></td><td>4</td><td></td><td></td></tr><tr><td colspan="3">IMPED bypass valve</td><td></td><td></td></tr><tr><td>2.2699E+07 a Re(Zs) Pa-s/m^3</td><td></td><td>G</td><td>2.2623E+05 A lpl</td><td>Pa</td></tr><tr><td></td><td>0.0000 b Im(Zs) Pa-s/m^3</td><td></td><td>-2.5287 B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>1.3511E-02 C |U|</td><td>m^3/s</td></tr><tr><td></td><td></td><td>176.46</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td>-1528.1</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>-1528.1</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td>-2071.9</td><td>G HeatIn</td><td>W</td></tr><tr><td>COMPL little header</td><td></td><td>5</td><td></td><td></td></tr><tr><td colspan="3">1.0000E-03 a SurfAr</td><td></td><td></td></tr><tr><td>3.0000E-05 b Volum</td><td>m^2 m^3</td><td></td><td>2.2623E+05 A lpl</td><td>Pa</td></tr><tr><td></td><td></td><td></td><td>-2.5287 B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>1.3510E-02 C |U|</td><td>m^3/s</td></tr><tr><td></td><td></td><td>177.92</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td>-1528.2</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td>-1528.2</td><td>F Work</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td>-9.3003E-02 G HeatIn</td><td>W</td></tr></table>

<table><tr><td rowspan="13">ISODUCT sameas</td><td colspan="2">short tube</td><td colspan="2">6</td><td colspan="2"></td></tr><tr><td>a Area 3a</td><td colspan="2">m^2</td><td colspan="2">2.2650E+05 A lpl</td></tr><tr><td>b Perim</td><td>m</td><td></td><td>-0.9736 B Ph(p)</td><td>Pa</td></tr><tr><td>sameas 3b</td><td>m</td><td></td><td></td><td>deg</td></tr><tr><td>0.1200</td><td>c Length</td><td></td><td>1.3536E-02 C |U|</td><td>m^3/s</td></tr><tr><td>sameas 3d</td><td>d Srough</td><td>180.00</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td>-1532.7 E Hdot -1532.7</td><td>W W</td></tr><tr><td colspan="2">ideal SOFTEND</td><td>Solid type</td><td>-4.5318</td><td>F Work G HeatIn W</td></tr><tr><td colspan="2">0.0000 0.0000</td><td>connect bypass to tr</td><td>7</td><td></td></tr><tr><td colspan="2">a Re(Z)</td><td>(t)</td><td>2.2650E+05 A lpl</td><td>Pa</td></tr><tr><td colspan="2">b Im(Z)</td><td>(t)</td><td>-0.9736 B Ph(p)</td><td>deg</td></tr><tr><td colspan="2"></td><td></td><td>1.3536E-02 C |UI</td><td>m^3/s</td></tr><tr><td colspan="2"></td><td></td><td>180.00 D Ph(U)</td><td>deg</td></tr><tr><td colspan="2"></td><td></td><td>-1532.7 E Hdot</td><td>W</td></tr><tr><td colspan="2"></td><td></td><td>-1532.7 F Work</td><td>W</td></tr><tr><td colspan="2"></td><td></td><td>-1.1276 G Re(Z)</td><td></td></tr><tr><td colspan="2">sameas 0 Gas type</td><td></td><td>1.9123E-02 H Im(Z)</td><td></td></tr><tr><td colspan="2">ideal Solid type</td><td></td><td>305.20 I T</td><td>K</td></tr><tr><td colspan="2">ISODUCT the inertance</td><td>8</td><td></td><td></td></tr><tr><td colspan="2">4.6400E-04 a Area m^2</td><td></td><td>2.1066E+05 A lpl</td><td>Pa</td></tr><tr><td colspan="2">7.6360E-02 b Perim m</td><td></td><td>-3.0564. B Ph(p)</td><td>deg</td></tr><tr><td colspan="2">2.4900 c Length m</td><td></td><td>3.9429E-02 C |U|</td><td>m^3/s</td></tr><tr><td colspan="2">sameas 3d d Srough</td><td></td><td>104.14 D Ph(U)</td><td>deg</td></tr><tr><td colspan="2"></td><td>-1227.9</td><td>E Hdot</td><td>W</td></tr><tr><td colspan="2">sameas Gas type 0</td><td>-1227.9</td><td>F Work</td><td>W</td></tr><tr><td colspan="2">ideal Solid type</td><td>-657.84</td><td>G HeatIn</td><td>W</td></tr><tr><td colspan="2"></td><td>9</td><td></td><td></td></tr><tr><td colspan="2">IMPEDANCE valve-inertance set -1.4258E+05 a Re(Zs) Pa-s/m^3 G</td><td></td><td>2.0907E+05 A Ipl</td><td>Pa</td></tr><tr><td colspan="2">0.0000 b Im(Zs) Pa-s/m^3</td><td>-1.5845</td><td>B Ph(p)</td><td>deg</td></tr><tr><td colspan="2"></td><td></td><td>3.9429E-02 C |U|</td><td>m^3/s</td></tr><tr><td colspan="2"></td><td>104.14</td><td>D Ph(U)</td><td>deg</td></tr><tr><td colspan="2"></td><td>-1117.1</td><td>E Hdot</td><td>W</td></tr><tr><td colspan="2">sameas.0 Gas type</td><td></td><td>F Work</td><td></td></tr><tr><td colspan="2">ideal Solid type</td><td>-1117.1</td><td></td><td>W</td></tr><tr><td colspan="2"></td><td>110.83</td><td>G HeatIn</td><td>W</td></tr><tr><td colspan="2"></td><td>10</td><td></td><td></td></tr><tr><td colspan="2">COMPL little header</td><td></td><td></td><td></td></tr><tr><td colspan="2">2.0000E-03 a SurfAr m^2</td><td></td><td>2.0907E+05 A lpl</td><td>Pa</td></tr><tr><td colspan="2">6.0000E-05 b Volum m^3</td><td></td><td>-1.5845 B Ph(p)</td><td>deg</td></tr><tr><td colspan="2"></td><td></td><td>3.8815E-02 C IUI</td><td>m^3/s</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td>104.40</td><td>D Ph(U)</td><td>deg</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td>-1117.2</td><td>E Hdot</td><td>W</td></tr></table>

<table><tr><td rowspan="2">sameas ideal</td><td rowspan="2">0</td><td rowspan="2">Gas type Solid type</td><td rowspan="2"></td><td>-1117.2</td><td>F Work</td><td>W</td></tr><tr><td>-0.1588</td><td>G HeatIn</td><td>W</td></tr><tr><td>ISODUCT</td><td>short tube</td><td></td><td>11</td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>6a</td><td>a Area m^2</td><td></td><td>2.2650E+05 A lpl</td><td></td><td>Pa</td></tr><tr><td>sameas</td><td>6b</td><td>b Perim m</td><td></td><td>-0.9736 B Ph(p)</td><td></td><td>deg</td></tr><tr><td>sameas</td><td>6c</td><td>c Length m</td><td></td><td>3.8344E-02 C |U|</td><td></td><td>m^3/s</td></tr><tr><td>sameas</td><td>6d</td><td>d Srough</td><td></td><td>104.67</td><td>D Ph(U)</td><td>deg</td></tr><tr><td rowspan="2">sameas</td><td rowspan="2"></td><td rowspan="2"></td><td>-1170.8</td><td>E Hdot</td><td>W</td></tr><tr><td>-1170.8</td><td>F. Work</td><td>W</td></tr><tr><td>ideal</td><td>Gas type Solid type</td><td></td><td>-53.541</td><td>G HeatIn</td><td>W</td></tr><tr><td>UNION</td><td></td><td></td><td>12</td><td></td><td></td><td></td></tr><tr><td>7.0000</td><td>connect bypass here</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a TendSg</td><td></td><td></td><td>2.2650E+05 A Ipl</td><td></td><td>Pa</td></tr><tr><td>-0.9736 c Ph(p)E</td><td>2.2650E+05 b IplEnd</td><td>Pa deg</td><td>=12A? =12B?</td><td></td><td>-0.9736 B Ph(p)</td><td>deg m^3/s</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">122.07</td><td>4.3776E-02 C |U|</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>-2703.5</td><td>E Hdot</td><td>W</td></tr><tr><td>sameas 0</td><td>Gas type</td><td></td><td></td><td>-2703.5</td><td>F Work</td><td>W</td></tr><tr><td rowspan="2">ideal</td><td rowspan="2">Solid type</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">0.0000</td><td rowspan="2">G HeatIn</td><td rowspan="2">W</td></tr><tr><td></td></tr><tr><td>ISODUCT</td><td>short tube</td><td></td><td>13</td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>8a a Area</td><td>m^2</td><td></td><td>2.3837E+05 A lpl</td><td></td><td>Pa</td></tr><tr><td>sameas</td><td>8b b Perim</td><td>m</td><td></td><td>0.5000</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>0.1100</td><td>c Length</td><td>m</td><td></td><td>4.3251E-02 C IUI</td><td></td><td>m^3/s</td></tr><tr><td></td><td>3.0000E-04 d Srough</td><td></td><td></td><td>122.58</td><td>D Ph(U)</td><td>deg</td></tr><tr><td rowspan="2">sameas 0</td><td rowspan="2">Gas type</td><td rowspan="2"></td><td rowspan="2"></td><td>-2738.1</td><td>E Hdot</td><td>W W</td></tr><tr><td>-2738.1</td><td>F Work</td><td></td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td>14</td><td>-34.620</td><td>G HeatIn</td><td>W</td></tr><tr><td rowspan="11">FREETARG</td><td></td><td>pulsetube magnitud</td><td></td><td></td><td></td><td></td></tr><tr><td>2.3837E+05 a Target</td><td></td><td>=14A?</td><td>2.3837E+05 A FreeT</td><td></td><td></td></tr><tr><td>13A b ResAdr</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>15</td><td></td><td></td><td></td></tr><tr><td>FREETARG 0.5000 a Target</td><td>pulsetube phase</td><td></td><td></td><td></td><td></td></tr><tr><td>13B b ResAdr</td><td></td><td>=15A?</td><td></td><td>0.5000 A FreeT</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COMPLIANCE volume under head</td><td></td><td></td><td>16</td><td></td><td></td></tr><tr><td>1.0000E-02 a SurfAr</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7.5000E-05 b Volum</td><td></td><td>m^2</td><td></td><td>2.3837E+05 A lpl</td><td>Pa</td></tr><tr><td></td><td></td><td>m^3</td><td></td><td>0.5000 B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>4.2488E-02 C |UI</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>123.25</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>-2739.1</td><td>E Hdot</td><td>W</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>sameas 0 Gas type</td><td></td><td></td><td>-2739.1</td><td>F Work</td><td>W</td></tr></table>

! The restart information below was generated by a previous run   
! You may wish to delete this information before starting a run   
! where you will (interactively) specify a different iteration   
! mode. Edit this table only if you really know your model!   
INVARS 4 2 1 2 2 4 1 9 1   
TARGS 4 12 2 12 3 14 1 15 1   
SPECIALS 0

## 10. LIST OF SYMBOLS

Roman   
A area, or amplitude, or a constant   
a sound speed   
B magnetic field, or flow availability   
b exponent for T dependence of µ or k, or flow availability per unit mass   
C compliance, or a constant   
c compliance per unit length   
$C O P$ coefficient of performance   
Cp isobaric heat capacity per unit mass   
D diameter   
e complex gain factor arising in continuity equation   
E energy   
È acoustic power   
F a function   
f frequency, or spatially averaged thermoviscous function   
G conductance (inverse of resistance)   
H total energy   
H rate at which total energy flows (total power)   
h thermoviscous function, or enthalpy per unit mass   
I electric current   
i $\sqrt { - 1 }$   
j electrical current density   
K minor-loss coefficient   
k thermal conductivity   
L inertance, or length   
l inertance per unit length   
m mass, or multiplier for turbulent viscous dissipation   
$N _ { R }$ Reynolds number   
p pressure   
Q heat, or quality factor of resonance   
Q rate at which heat is transferred (thermal power)   
R resistance, or gas constant, or radius   
r resistance per unit length, or radius, or radial coordinate   
S entropy, or surface area   
s entropy per unit mass   
T temperature   
t time

U volumetric velocity

u x component on velocity

V volume

v y component of velocity

W work

W rate at which work is done (mechanical power)

w z component of velocity

x coordinate along sound-propagation direction

X exergy

À rate at which exergy flows (power)

y coordinate perpendicular to sound-propagation direction

z coordinate perpendicular to sound-propagation direction,

or specific acoustic impedance

Z acoustic impedance

## Greek

α attenuation constant

Γ normalized temperature gradient

γ ratio of isobaric to isochoric specific heats

∆ big difference

δ penetration depth, or small difference

ε surface roughness

€ internal energy per unit mass

η efficiency

κ thermal diffusivity

λ wavelength

µ dynamic viscosity

ν kinematic viscosity

π 3.14159...

ψ Rott's joining function

ρ density

σ Prantl number, or electrical conductivity

φ phase angle

Φ viscous dissipation function

θ phase angle

ω angular frequency

ζ bulk viscosity

ξ arbitrary variable

## Subscripts

C cold, or Carnot

H hot

h hydraulic (i.e., Rh is hydraulic radius)

m mean (or mechanical)

R Reynolds (in NR)

κ thermal

ν viscous

0“environment”

1 first-order (usually a complex amplitude)

2 second-order

gen generated

ref reference location or temperature

reg regenerator

pt pulse tube

crit critical (i.e., ∇Tcrit)

## Special symbols

Im[ ] Imaginary part of

Re[] Real part of

{〉 average in y, z plane

|| magnitude of complex number

overdot time derivative

overbar time average, time rate

tilde complex conjugate

## BIBLIOGRAPHY

[1] G. J. Van Wylen and R. E. Sonntag. Fundamentals of Classical Thermodynamics. Wiley, 1965.

[2] H. B. Callen. Thermodynamics and an Introduction to Thermostatistics. Wiley, 1985.

[3] P. M. Morse. Thermal Physics. Benjamin, 1969.

[4] G. Walker. Stirling Engines. Clarendon, Oxford, 1960.

[5] G. Walker. Cryocoolers. Plenum, New York, 1983.

[6] J. R. Senft. Ringbom Stirling Engines. Oxford University Press, 1993.

[7] I. Urieli and D. M. Berchowitz. Stirling Cycle Engine Analysis. Adam Hilger, Bristol UK, 1984.

[8] C. D. West. Liquid Piston Stirling Engines. Van Nostrand Reinhold, 1983.

[9] P. H. Ceperley. A pistonless stirling engine-the traveling wave heat engine. J. Acoust. Soc. Am., 66:1508–1513, 1979.

[10] P. H. Ceperley. Gain and efficiency of a short traveling wave heat engine. J. Acoust. Soc. Am., 77:1239–1244, 1985.

[11] C. D. West. Liquid piston Stirling engines. Van Nostrand Reinhold, 1983.

[12] L. E. Kinsler, A. R. Frey, A. B. Coppens, and J. V. Sanders. Fundamentals of Acoustics. John Wiley and Sons, 1982.

[13] A. D. Pierce. Acoustics: An Introduction to Its Physical Principles and Applications. Acoustical Society of America, Woodbury, New York, 1989.

[14] N. Rott. Damped and thermally driven acoustic oscillations in wide and narrow tubes. Z. Angew. Math. Phys., 20:230–243, 1969.

[15] K. M. Godshalk, C. Jin, Y. K. Kwong, E. L. Hershberg, G. W. Swift, and R. Radebaugh. Characterization of 350 Hz thermoacoustic driven orifice pulse tube refrigerator with measurements of the phase of the mass flow and pressure. Advances in Cryogenic Engineering, 41:1411–1418, 1996.

[16] R. S. Reid, W. C. Ward, and G. W. Swift. Cyclic thermodynamics with open flow. Phys. Rev. Lett., 80:4617–4620, 1998.

[17] S. Backhaus and G. W. Swift. A thermoacoustic-stirling engine. 1999. Submitted to Nature.

[18] Cryenco manufactures large-scale cryogenic hardware, such as liquid-nitrogen tank trucks, storage tanks, and the cryogenic vessels for General Electric's MRI systems. 3811 Joliet, Denver CO 80239.

[19] G. W. Swift. Thermoacoustic natural gas liquefier. 1997. In proceedings of the DOE Natural Gas Conference, Houston TX, March 1997. Also available at http://libwww.lanl.gov/la-pubs/00412750.pdf.

[20] W. C. Ward and G. W. Swift. Design environment for low amplitude thermoacoustic engines (DeltaE). J. Acoust. Soc. Am., 95:3671-3672, 1994. Fully tested software and users guide available from Energy Science and Technology Software Center, US Department of Energy, Oak Ridge, Tennessee. To review DeltaE's capabilities, visit the Los Alamos thermoacoustics web site at http://rott.esa.lanl.gov/. For a beta-test version, contact ww@lanl.gov (Bill Ward) via Internet.

[21] D. Gedeon. A globally implicit Stirling cycle simulation. In Proceedings of the 21st Intersociety Energy Conversion Engineering Conference, page 550. American Chemical Society, 1986.

[22] A. Tominaga, Institute of Physics, University of Tsukuba, Tsukuba 305, Japan.

[23] J. Gary, A. O'Gallagher, and R. Radebaugh. A numerical model for regenerator performance. Technical report, NIST-Boulder, 1994. Also known as REGEN 3.1 Users Guide.

[24] R. Radebaugh. A review of pulse tube refrigeration. Adv. Cryogenic Eng., 35:1191-1205, 1990.

[25] G. W. Swift. Thermoacoustic engines. J. Acoust. Soc. Am., 84:1145–1180, 1988.

[26] L. D. Landau and E. M. Lifshitz. Fluid Mechanics. Pergamon, 1982.

[27] R. W. Fox and A. T. McDonald. Introduction to Fluid Mechanics. Wiley, 1985.

[28] A. Bejan. Entropy Generation Minimization: The Method of Thermodynamic Optimization of Finite-Size Systems and Finite-Time Processes. CRC press, 1995.

[29] Adrian Bejan. Advanced Engineering Thermodynamics. Wiley, second edition, 1997.

[30] A. Tominaga. Fundamental Thermoacoustics. ISBN4-7536-5079-0, 1998. In Japanese.

[31] G. W. Swift. Thermoacoustic engines and refrigerators. Physics Today, pages 22–28, . July 1995.

[32] G. W. Swift. Encyclopedia of Applied Physics, volume 21, chapter Thermoacoustic engines and refrigerators, pages 245-264. Wiley, for American Institute of Physics, 1997.

[33] N. Rott. Thermoacoustics. Adv. Appl. Mech., 20:135–175, 1980. and references therein.

[34] A. J. Organ. Thermodynamics and Gas Dynamics of the Stirling Cycle Machine. Cambridge University Press, 1992.

[35] G. Walker, L. Bauwens, and E. Bingham. Pulse-tube refrigerators: an introduction. ??, 1996. Available through Stirling Machine World, stirmach@juno.com

[36] W. P. Arnott, H. E. Bass, and R. Raspet. General formulation of thermoacoustics for stacks having arbitrarily shaped pore cross sections. J. Acoust. Soc. Am., 90:3228–3237, 1991.

[37] G. W. Swift and R. M. Keolian. Thermoacoustics in pin-array stacks. J. Acoust. Soc. Am., 94:941–943, 1993.

[38] G. W. Swift and W. C. Ward. Simple harmonic analysis of regenerators. Journal of Thermophysics and Heat Transfer, 10:652–662, 1996.

[39] W. M. Kays and A. L. London. Compact Heat Exchangers. McGraw-Hill, New York, 1964.

[40] P. Merkli and H. Thomann. Thermoacoustic effects in a resonance tube. J. Fluid Mech., 70:161-177, 1975.

[41] N. Rott. Thermally driven acoustic oscillations, part iii: Second-order heat flux. Z. Angew. Math. Phys., 26:43, 1975.

[42] R. C. Tolman and P. C. Fine. On the irreversible production of entropy. Rev. Mod. Phys., 20:51–77, 1948.

[43] J. C. Wheatley, T. Hofler, G. W. Swift, and A. Migliori. An intrinsically irreversible thermoacoustic heat engine. J. Acoust. Soc. Am., 74:153–170, 1983.

[44] A. Migliori and G. W. Swift. Liquid sodium thermoacoustic engine. Appl. Phys. Lett., 53:355-357, 1988.

[45] G. W. Swift, D. L. Gardner, and S. Backhaus. Acoustic recovery of lost power in pulse tube refrigerators. J. Acoust. Soc. Am., ??:??, 1999. To appear in February issue.

[46] J. R. Womersley. Method for the calculation of velocity, rate of flow, and viscous drag in arteries when the pressure gradient is known. Journal of Physiology, 127:553–563, 1955.

[47] M. Iguchi, M. Ohmi, and K. Maegawa. Analysis of free oscillating flow in a U-shaped tube. Bull. JSME, 25:1398, 1982.

[48] S. M. Hino, M. Sawamoto, and S. Takasu. Experiments on transition to turbulence in an oscillatory pipe flow: J. Fluid Mech., 75:193–207, 1976.

[49] J. R. Olson and G. W. Swift. Acoustic streaming in pulse tube refrigerators: Tapered pulse tubes. Cryogenics, 37:769–776, 1997.

[50] G. W. Swift, M. S. Allen, and J. J. Wollan. Perforn;ance of a tapered pulse tube. 1998. To be submitted to the proceedings of the 10th Irternational Cryocooler Conference, Monterey CA, May 1998.

[51] V. L. Streeter. Handbook of Fluid Dynamics. McGraw-Hill, 1961.

[52] I. E. Idelchik. Handbook of Hydraulic Resistance. CRC Press, 3rd edition, 1994.

[53] P. J. Storch, R. Radebaugh, and J. E. Zimmerman. Analytical model for the refrigeration power of the orifice pulse tube refrigerator. Technical note 1343, National Institute of Standards and Technology, 1990.

[54] G. W. Swift. Analysis and performance of a large thermoacoustic engine. J. Acoust. Soc. Am., 92:1551–1563, 1992.

[55] N. Rott and G. Zouzoulas. Thermally driven acoustic oscillations, part IV: Tubes with variable cross section. Z. Angew. Math. Phys., 27:197–224, 1976.

[56] J. L. Smith and M. Romm. Thermodynamic loss at component interfaces in Stirling cycles. In Proceedings of the 27th Intersociety Energy Conversion Engineering Conference, pages 5.529–5.532. Society of Automotive Engineers, 1992.

[57] P. Kittel. Temperature profile within pulse tubes. Adv. Cryogenic Eng., 43:1927-1932, 1998.

[58] G. W. Swift. A Stirling engine with a liquid working substance. J. Appl. Phys., 65:4157- 4172, 1989.

[59] W. L. M. Nyborg. Acoustic streaming. In W. P. Mason, editor, Physical Acoustics, Volume IIB, page 265. Academic Press, 1965.

[60] David Gedeon. DC gas flows in Stirling and pulse-tube cryocoolers. In R. G. Ross, editor, Cryocoolers 9, pages 385–392. Plenum, New York, 1997.

[61] N. Rott. The influence of heat conduction on acoustic streaming. Z. Angew. Math. Phys, 25:417, 1974.

[62] J. R. Olson and G. W. Swift. Similitude in thermoacoustics. J. Acoust. Soc. Am., 95:1405–1412, 1994.
