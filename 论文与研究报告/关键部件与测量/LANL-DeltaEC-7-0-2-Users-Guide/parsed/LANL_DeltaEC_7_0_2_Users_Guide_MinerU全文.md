---
title: 'Design Environment for Low-amplitude Thermoacoustic Energy Conversion: DeltaEC Version 7.0.2 Users Guide
  · MinerU全文'
record_role: machine-transcription
parse_method: MinerU
source_sha256: 66afcceef942c658a41894b75dc38d8dea5cdee78b30991697d9ee606e571cf4
source_pages: 310
---

<!-- Original PDF pages 1-200 -->

# Design Environment for Low-amplitude Thermoacoustic Energy Conversion DELTAEC Version 7.0.2 Users Guide LA-CC-01-13, LA-CC-16-053

Bill Ward, John Clark, and Greg Swift Los Alamos National Laboratory

For the latest version, visit www.losalamosthermoacoustics.org

![[mu_66afccee_4f490c718c4ed8a07549.jpg]]

## Contents

1 Introduction 1   
1.1 What DELTAEC does 1   
1.2 The Users Guide 6   
1.3 Obtaining DELTAEC 7   
1.4 Installing DELTAEC 7   
1.5 Acknowledgments 8   
1.6 Copyright 8   
PART I: TUTORIAL 9   
2 Acoustics & user interface 10   
2.1 Acoustics in DELTAEC 10   
2.2 I/o file structure 12   
2.3 Running DELTAEC 14   
2.3.1 Font augmentation 17   
2.3.2 Running DELTAEC from terminal . 17   
2.4 State plots 17   
2.5 Guesses and targets 19   
2.6 Other acoustics features 25   
2.6.1 Simple segment types 25   
2.6.2 The zero of time 27   
2.6.3 Gases and solids 27   
2.6.4 Turbulence 28   
2.7 Other useful features 29   
2.7.1 Keeping parameters equal 29   
2.7.2 Master-slave links 30   
2.7.3 Schematic view 33   
2.7.4 Highlights display 34   
2.7.5 Structured branches, loops, and networks 34   
2.7.6 Manipulating entire segments 39   
2.7.7 Thermophysical properties 39   
3 More about plotting 41   
3.1 State plots . 41   
3.1.1 Cloning 42   
3.1.2 Legs 43   
3.1.3 Phasor plotting options 43   
3.2 Incremental plotting 45   
3.2.1 One-dimensional incremental plots 46   
3.2.2 Two-dimensional incremental plots 48   
3.2.3 Rewinding incremental plots 49   
3.2.4 Incremental plots when more than one model is run 50   
4 RPN math 51   
4.1 Summary 51   
4.2 Non-standard results 52   
4.3 List Linkages 54   
4.4 Non-standard inputs 54   
4.5 Non-standard targets 55   
4.6 Changing an integration variable 57   
4.7 Two examples 58   
4.8 Non-standard guesses 59   
4.9 Linking multiple models 60   
4.10 Other math segments 61   
5 Engines & refrigerators 62   
5.1 Principles of calculation 62   
5.2 Hofler's refrigerator 64   
5.3 Choosing guesses and targets 74   
5.4 Meeting targets in an elaborate model 78   
5.4.1 Basic rules . 78   
5.4.2 Developing a substantially new model 79   
5.4.3 Modifying an existing model 81   
5.5 Standing-wave engine 82   
5.6 More thermoacoustic segments 87   
5.7 More user-interface features 88   
5.8 Stirling and pulse-tube refrigerators 89   
5.8.1 Alpha Stirling crvocooler 89   
5.8.2 Beta or gamma cryocooler 93   
5.8.3 Pulse-tube refrigerator 96   
5.9 Exergy flow 101   
6 Steady flow, too 103   
6.1 Principles of calculation 103   
6.2 Reid's refrigerator 105   
6.3 TASHE 109   
6.4 Self-circulating heat exchanger 115   
7 Mixture separation 127   
7.1 Principles of calculation 127   
7.2 Boundary conditions 129   
7.3 Continuous He-Ar separator 131   
PART II: REFERENCE 135   
8 General principles 136   
8.1 Integration from BEGIN to \*\*END 136   
8.1.1 Additional details for N and p2,0,DEC 138   
8.2 Shooting method 139   
8.3 Numerical options . 141   
8.3.1 Integration options 141   
8.3.2 Shooting options 141   
8.4 Error messages 142   
8.5 Inherent limitations 144   
9 Good design habits 147   
9.1 Attention to details 147   
9.1.1 Imperfect external heat exchange 147   
9.1.2 Internal 2-D effects from imperfect external heat exchange 148   
9.1.3 Heat leaks 148   
9.1.4 Geometry 149   
9.1.5 Actual operating conditions 149   
9.1.6 Thermophysical properties 149   
9.2 Component conservatism 149   
9.2.1 Turbulence 150   
9.2.2 Adiabatic-isothermal mixing 150   
9.2.3 Stacked screen regenerators 150   
9.2.4 Pulse tubes and thermal buffer tubes 150   
9.2.5 Standing-wave engine stacks 151   
10 Physical segments 153   
10.1 Ducts and cones 153   
10.1.1 DUCT 153   
10.1.2 CONE 159   
10.2 Lumped elements 162   
10.2.1 COMPLIANCE 162   
10.2.2 SURFACE 164   
10.2.3 IMPEDANCE 165   
10.2.4 MINOR 166   
10.3 Series transducers 170   
10.3.1 VESPEAKER, IESPEAKER, VEDUCER, and IEDUCER 170   
10.4 Side-branch transducers and side-branch impedances 174   
10.4.1 BRANCH, OPNBRANCH, and PISTBRANCH 174   
10.4.2 VSPEAKER. ISPEAKER. VDUCER, and IDUCER 176   
10.5 Stacks and regenerators 180   
10.5.1 STKSLAB. STKCIRC. STKRECT, and STKPIN 180   
10.5.2 STKSCREEN and STKPOWERLW 186   
10.6 Pulse tubes and thermal buffer tubes 192   
10.6.1 STKDUCT and STKCONE 192   
10.7 Heat exchangers . 194   
10.7.1 HX and TX 195   
10.7.2 SX and PX 198   
10.7.3 VXQ1, VXQ2, VXT1, and VXT2 204   
10.8 Adiabatic-isothermal interface loss 217   
10.8.1 JOIN 217   
10.9 Mixture separation 219   
10.9.1 MIXBL, MIXSLAB, and MIXCIRC 219   
10.9.2 MIXTBL. MIXTSLAB. and MIXTCIRC 222   
11 Logistical segments 228   
11.1 Starting and ending 228   
11.1.1 TITLE 228   
11.1.2 BEGIN 228   
11.1.3 HARDEND and SOFTEND 232   
11.2 Structured branches and unions 234   
11.2.1 TBRANCH 234   
11.2.2 UNION 236   
11.3 Insulation 239   
11.3.1 ANCHOR and INSULATE 239   
11.4 Math segments 240   
11.4.1 RPN. 240   
11.4.2 VOLUME 248   
11.4.3 CONSTANTS 249   
11.5 Interfaces to external programs and files 249   
11.5.1 BLKDATA 249   
11.5.2 SYSEXEC 251   
11.5.3 Running DELTAEC from a terminal or another program 253   
12 Gases (and liquids) 255   
12.1 Helium (helium) 255   
12.2 Real helium (CryoHe) 256   
12.3 Helium-argon mixtures (HeAr) 256   
12.4 Real argon (argon) 258   
12.5 Helium-xenon mixtures (HeXe) 258   
12.6 Neon (neon) 258   
12.7 Air (air) 258   
12.8 Humid air and fog (HumidAir) 258   
12.9 Nitrogen (nitrogen) 259   
12.10 Real hydrogen (H2normal and H2para) 259   
12.11 Ideal-gas hydrogen (hydrogen) 260   
12.12 Deuterium (deuterium) 260   
12.13 Carbon dioxide (C02) 260   
12.14 Neon-xenon mixtures (NeXe) 261   
12.15 Natural-gas combustion products (NGCbProd) 262   
12.16 Liquid sodium (sodium) 262   
12.17 Liquid sodium-potassium eutectic (NaK-78) 263   
12.18 User-defined gases 264   
12.18.1 User-defined pure gases 264   
12.18.2 User-defined gas mixtures 265   
13 Solids 267   
13.1 Ideal solid (ideal) 267   
13.2 Heavium (heavium) 267   
13.3 Copper (copper) 268   
13.4 Nickel (nickel) 268   
13.5 Stainless steel (stainless) 268   
13.6 Molybdenum (molybdenum) 268   
13.7 Tungsten (tungsten) 268   
13.8 Kapton (kapton) 268   
13.9 Mylar (mylar) . 268   
13.10 Celcor (celcor) 269   
13.11 Phosphor bronze (P-bronze) 269   
13.12 Gadolynium oxysulfide (a.k.a GOS; Gd202S) 269   
13.13 Antimonial lead (Pb95Sb05) 269   
13.14 HoCu₂ (HoCu2) 269   
13.15 50-50 erbium praseodymium alloy (Er50Pr50) 270   
13.16 50-50 erbium nickel alloy (ErNi) 270   
13.17 User-defined solids 271   
BACK MATTER 272   
14 Derivations 273   
14.1 Force $F _ { 1 }$ on pressure vessel 273   
14.2 Second-order time-averaged pressure 274   
14.3 Tortuous geometry 〈T1〉 and dTm/dx 276   
14.4 Third-order $p _ { 1 }$ dependence in dp2,0.pEc/dx 278   
14.5 Pole-tip flux, linear motor or alternator, \*\*SPEAKER 282   
14.6 Pulsed combustion 283   
15 Symbols 287   
Bibliography 292   
Alphabetical indexes 299

## 1. Introduction

DELTAEC—Design Environment for Low-Amplitude ThermoAcoustic Energy Conversion— is a computer program that can calculate details of how thermoacoustic equipment performs, or can help the user to design equipment to achieve desired performance. Input data can be modified or entered via DELTAEC's user interface (or, very awkwardly, by using any text editor). Results can be examined via the user interface, built-in graphics displays, the operating system's text utilities, or any spreadsheet or graphics software.

For good portability, the computational core of DELTAEC is compiled from GNU Fortran and the user interface is built on Python. All calculations are performed in double precision.

## 1.1 What DeltaEC does

DELTAEC numerically integrates in one spatial dimension using a low-amplitude, “acoustic" approximation and sinusoidal time dependence. It integrates the wave equation and sometimes other equations such as the energy equation, in a gas (or a very compressible, thermodynamically active liquid), in a geometry given by the user as a sequence of segments (no more than 200) such as ducts, compliances, transducers, and thermoacoustic stacks and regenerators. A glance through the figures below will orient the new user to a broad range of situations that DELTAEC can handle.

DELTAEC always assumes a time dependence of $e ^ { i \omega t }$ , so its “wave" equation is essentially the second-order Helmholtz differential equation for the complex pressure amplitude $p _ { 1 } ( x )$ which can be regarded as two coupled first-order differential equations for $p _ { 1 } ( x )$ and the complex volume flow rate amplitude $U _ { 1 } ( x )$ . An integration of these differential equations is performed for each segment, with pressures, volume flow rates, and some other variables matched at the junctions between segments. In stacks and regenerators, the acoustic solution for the complex pressure and volume flow rate amplitudes is found simultaneously with the solution of the energy-flow equation to obtain the mean-temperature profile as well. The energy flow through stacks and regenerators is controlled by temperatures and/or heat flows at adjacent heat exchangers. With binary gas mixtures in mixture-separation channels, the solution of the wave equation is found simultaneously with that of the equation describing the mole fluxes of the components of the mixture, inverted to find the light mole fraction as a function of position. Modeling of acoustics superimposed on steady flows is also supported.

With its multi-parameter shooting method to satisfy a variety of mixed boundary conditions, DELTAEC gives the user considerable freedom in choosing which variables are computed as "solutions." For example, in a simple acoustic resonator (the first example below),

![[mu_66afccee_902a73957f18f6d6fe0d.jpg]]  
Figure 1.1: Driven, lossy plane-wave resonator.

![[mu_66afccee_6bc7a2ef48110bc05e6b.jpg]]  
Figure 1.2: Driven, radiating Helmholtz resonator.

![[mu_66afccee_c8442e280a0098993a4d.jpg]]  
Figure 1.3: Driven duct network.

![[mu_66afccee_76bf7692f33d2900a12e.jpg]]  
Figure 1.4: Standing-wave thermoacoustic refrigerator (Hofler style [1, 2]).

![[mu_66afccee_9ed31bc99c852d8f53f0.jpg]]  
Figure 1.5: Standing-wave thermoacoustic refrigerator (TALSR style [3])

![[mu_66afccee_daa60a25d0e98d38e971.jpg]]  
Figure 1.6: John Wheatley's heat-driven refrigerator, affectionately called “the beer cooler" in the early 1980s [4].

![[mu_66afccee_7ee3f2fe5a24ef60a78b.jpg]]  
Figure 1.7: Thermoacoustic-Stirling hybrid engine [5].

![[mu_66afccee_30c6a5a566826c27e759.jpg]]  
Figure 1.8: Double-inlet pulse-tube refrigerator [6, 7].

![[mu_66afccee_fd8e1b82c6fe8f52c67a.jpg]]  
Figure 1.9: Resonant self-circulating heat exchanger with one gas diode. [8, 9]

![[mu_66afccee_b9b96590f5f61dab26d3.jpg]]  
Figure 1.10: Half-wavelength helium-argon mixture separator [10].

DELTAEC can compute the input impedance as a function of frequency, or the resonance frequency for a given geometry and gas, or the length required to give a desired resonance frequency, or even the concentration in a binary gas mixture required to give a desired resonance frequency in a given geometry.

DELTAEC includes few of the nonlinear effects that arise at high amplitudes, so be cautious using it when Mach numbers or Reynolds numbers are high. The principal exceptions to this rule are the turbulence algorithm in ducts and cones (introduced briefly in Chapter 2 and described in detail in Section 10.1.1) and the minor-loss segment, which models lumped-element dissipation where pressure difference is proportional to the square of the velocity (introduced briefly in Chapter 6 and described in detail in Section 10.2.4).

## 1.2 The Users Guide

This Users Guide is a <.pdf> document, compatible with Adobe Acrobat 6.0 and later versions. Its internal hyperlinking is convenient for online navigating.

In Part I, “Tutorial," we teach the use of DELTAEC by increasingly complicated examples in Chapters 2-7. Chapter 2 is just acoustics, without thermoacoustics. It serves to introduce DELTAEC's input/output formats and editing, running, and plotting features. Chapter 5 gives the most complete discussion of the overall principles behind the thermoacoustics computations, and the simplest thermoacoustic engine and refrigerator examples. The agreement of such examples with published experimental data serves as validation of the code. Chapter 6 introduces the effects of superimposed steady flows, and Chapter 7 introduces separation mole fluxes and concentration gradients in binary-gas mixtures.

Part II, “Reference," includes segment-by-segment reference sections for the experienced user, documenting the assumptions built into the computations for each segment and the data format for each segment. “Reference" also includes chapters with calculation formulas for thermophysical properties. It is our hope that experienced users can quickly find the information they need in Part II, especially using the index and the internal hyperlinks, while new users will find the wordier explanations of the Tutorial chapters helpful.

The examples we've included are simpler than DELTAEC files we use in our own research. We've maintained this simplicity in the Users Guide to avoid clutter. Experienced users will find that the number of segments in their DELTAEC files grows and grows, as small effects are included and non-standard features are implemented with RPN segments.

Some of the examples here were run many years ago in MS-DOS, others on a Mac, others with Windows. Many of the examples were created using earlier versions of DELTAE and DELTAEC, so there may be some formatting irregularities. In Chapter 2, screen shots of the user interface are often shown, but in later chapters most examples are displayed as they appear in a text editor after DELTAEC has saved them to the disk. This keeps the Users Guide <.pdf> file size smaller.

We assume that the reader of the Users Guide is very comfortable with basic linear acoustics [11, 12], and reasonably familiar with thermoacoustics for Chapters 5-7. The choices of which variables to regard as independent and integrable reflects the philosophy of Ref. [13], extended here to accommodate mixture separation and superimposed steady flow. We use variables as defined, for example, in the lists of symbols in Refs. [13] and [4],

## 1.3 Obtaining DeltaEC

The latest version of DELTAEC is freely available at www.losalamosthermoacoustics. org/. DELTAEC is under intermittent development, so regular users should check for updates occasionally.

There is no formal registration for DELTAEC, no fee, and no formal support or warranty of any kind (please read the copyright notice and disclaimer in Section 1.6). We are interested in hearing from users so we can fix any bugs that are found. Please report any bugs related to platform compatibility and the user interface to Bill Ward (ww@lanl.gov), with a cc to Greg Swift (swift@lanl.gov); please report any bugs related to thermoacoustic computations or the Users Guide to Greg with a cc to Bill.

News of your successes using this code will encourage us to consider this effort worthwhile and will enable us to continue DELTAEC's development and freely-shared status. We are especially grateful when you acknowledge DELTAEC in publications and reports and when you mention it to individuals at agencies that support acoustics research. This improves our chances to create and distribute improvements to DELTAEC in the future.

## 1.4 Installing DeltaEC

From www.losalamosthermoacoustics.org/, download and run the installation file (for Windows) or download and unzip the tar file (for Mac). DELTAEC should automatically install itself in <c: Program Files\DeltaEC> or some other sensible default folder. This Users Guide (<UsersGuide.pdf>) appears in the same folder

In Windows, this all appears as a program group accessible in the usual way through the Start button, and a desktop icon for launching the program should appear. The file extension <.out> should be automatically associated with DELTAEC, so double clicking any <.out> file should also launch the program. (If not, try the standard rebooting of the computer that Windows usually requires for establishing such file association after program installation.) During installation, choose a location without write protection, such as <MyDocuments>, for installing the Examples discussed in the rest of the Users Guide; or put an archival copy of the Examples into the write-protected installation folder, and later make an additional “working" copy elsewhere.

DELTAEC can be uninstalled via the Windows Control Panel, Add or Remove Programs; or by running <d:\Program Files\DeltaEC\D-uninst.exe>. To install a new version of DELTAEC, it should not be necessary to un-install a previous version. If a re-installation of DELTAEC does not work as it should, even after uninstalling the previous version, look for ghost processes named <DeltaEC.exe> in the Windows task manager, and kill them; or reboot your computer to kill such ghosts. (If you can reproducibly create such ghosts, please let us know how, so we can prevent them in future versions. We haven't seen a ghost since version 6.2, so we hope we've exorcised them forever.)

## 1.5 Acknowledgments

The development of DELTAE and DELTAEC was supported in part by many agencies and entities: Tektronix Corporation, SPAWAR, the Naval Postgraduate School, ONR, Praxair, and, most importantly, by several offices of the Department of Energy: Advanced Industrial Concepts, Materials Science (a part of Basic Energy Sciences in the Office of Science), the Technology Transfer Initiative Office, and the Office of Fossil Energy. Local support at Los Alamos has also been provided, via our Industrial Partnership Office (later called the Technology Transfer Division; now the Feynman Center for Innovation), our Locally Directed R&D program, and our local management in the Materials Physics and Applications Division and the Advanced Engineering Technology Division here at LANL.

In the 1990s, a long discussion with Pat Arnott helped us define the initial scope of this work, and comparisons with the results of parallel-plate-stack codes (written by Al Migliori and Dick Martin) were useful in the early stages. Suggestions by Kim Godshalk, Charles Jin, Tom Hofler, Jeff Olson, Scott Backhaus, Vince Kotsubo, and Jalal Zia led to significant improvements in capability and usability through the years. The TRITON project-kickoff meeting at Penn State motivated the development of the RPN segment. Charles Jin, Ray Radebaugh, and the code REGEN3.1 were indispensable in development of the stackedscreen algorithm. Scott Backhaus, David Gardner, Matt Poese, Steve Garrett, and Robert Keolian have helped shape the DELTAEC user interface. For version 7, Ryan Snodgrass made important suggestions for the STKSCREEN and STKPOWERLW calculations. Countless additional users have provided constructive criticism throughout DELTAEC's history.

## 1.6 Copyright

This Software was produced under a U.S. Government contract (DE-AC52-06NA25396) by Los Alamos National Laboratory, which is operated by Triad National Security LLC (Triad) for the U.S. Department of Energy's National Nuclear Security Administration. The U.S. Government is licensed to use, reproduce, and distribute this Software. Permission is granted to the public to copy and use this Software without charge, provided that this Notice and any statement of authorship are reproduced on all copies. Neither the Government nor Triad makes any warranty, express or implied, or assumes any liability or responsibility for the use of this Software.

Part I: Tutorial

## 2. Acoustics & user interface

In this Chapter we use the simplest acoustic segments, especially ducts and cones, to introduce DELTAEC's most basic acoustics and user-interface features.

## 2.1 Acoustics in DeltaEC

DELTAEC deals with one-dimensional sequences of acoustic and thermoacoustic elements, called segments, so DELTAEC's “wave" equation is one-dimensional. We always assume a time dependence of Re[“any complex variable" eiωt], so the “wave" equation can be taken as the second-order Helmholtz differential equation for the complex pressure amplitude $p _ { 1 } ( x )$ In its most familiar form, for an x-independent cross-sectional area A, without viscous or thermal-hysteresis losses, it is

$$
p _ { 1 } + \frac { a ^ { 2 } } { \omega ^ { 2 } } \frac { d ^ { 2 } p _ { 1 } } { d x ^ { 2 } } = 0 .\tag{2.1}
$$

It is often easier to think of this second-order equation as two coupled first-order equations in pressure $p _ { 1 }$ and volume flow rate $U _ { 1 }$

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { A } U _ { 1 } ,\tag{2.2}
$$

$$
\frac { d U _ { 1 } } { d x } = - \frac { i \omega A } { \rho _ { m } a ^ { 2 } } p _ { 1 } .\tag{2.3}
$$

This point of view is taken in Ref. [13]. The $d p _ { 1 } / d x$ equation is derived from the momentum equation of fluid mechanics and the $d U _ { 1 } / d x$ equation is derived from the continuity equation of fluid mechanics. In this form, the equations are ready for simultaneous numerical integration along the axial position coordinate x to generate solutions $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$

![[mu_66afccee_73328032b532ab645f1d.jpg]]

DELTAEC uses more complicated momentum and continuity equations that include additional effects such as dissipation of acoustic power along the sides of ducts. It uses different equations in different segments to suit local circumstances. For example, in boundary-layer approximation in large-diameter ducts and shallow cones, the governing equations are

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { A } \left[ 1 - \frac { 1 - i } { 2 } \frac { \Pi } { A } \delta _ { \nu } \right] ^ { - 1 } U _ { 1 } ,\tag{2.4}
$$

$$
\frac { d U _ { 1 } } { d x } = - \frac { i \omega A } { \rho _ { m } a ^ { 2 } } \left[ 1 + \frac { 1 - i } { 2 } \frac { \Pi } { A } \frac { \gamma - 1 } { 1 + \epsilon _ { s } } \delta _ { \kappa } \right] p _ { 1 } .\tag{2.5}
$$

where A is the cross-sectional area, I is the perimeter, $\delta _ { \nu }$ and $\delta _ { \kappa }$ are the viscous and thermal penetration depths, respectively, $\gamma$ is the ratio of isobaric and isochoric specific heats, and $\epsilon _ { s }$ is a correction for thermal properties of the solid wall that is usually negligible. The equations for each DELTAEC segment are given in Chapters 10 and 11.

DELTAEC uses continuity of $p _ { 1 }$ and $U _ { 1 }$ to pass from the end of one segment to the beginning of the next. Within each segment, wave propagation depends on local parameters such as area and perimeter as well as on global parameters such as frequency. Although DELTAEC uses analytic solutions to the governing equations for some of the simplest segment types, it usually must integrate the equations numerically, so it is generally correct to imagine DELTAEC beginning at the beginning of a series of segments and numerically integrating “a momentum equation" Fmomentum, such as Eq. (2.2) or (2.4), and “a continuity equation" $\mathcal { F } _ { \mathrm { c o n t i n u i t y } } .$ , such as Eq. (2.3) or (2.5), through each segment, sequentially, to the end of the series of segments, always using the local values of variables such as area, perimeter, and $p _ { 1 }$ and $U _ { 1 }$ themselves:

$$
\frac { d p _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { m o m e n t u m } } ( p _ { 1 } , U _ { 1 } , T _ { m } , p _ { m } , \omega , \mathrm { g e o m e t r y , \ g a s \ p r o p e r t i e s , \ s o l i d \ p r o p e r t i e s , \ e t c . } ) ,\tag{2.6}
$$

$$
\frac { d U _ { 1 } } { d x } ~ = ~ \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , p _ { m } , \omega , \mathrm { g e o m e t r y , \ g a s \ p r o p e r t i e s , \ s o l i d \ p r o p e r t i e s , \ e t c . } ) ,\tag{2.7}
$$

where most variables on the right-hand sides of these equations are functions of x.

The solution $p _ { 1 } ( x ) , U _ { 1 } ( x )$ is only determined uniquely if four real boundary conditions are imposed, because the governing equations can be expressed as two coupled first-order equations in two complex variables or as four coupled first-order equations in four real variables. This is true whether considering a single segment or a one-dimensional series of segments with each joined to its neighbor(s) by continuity of $p _ { 1 }$ and $U _ { 1 }$ . If all four boundary conditions are given at the initial end of the apparatus (i.e., if we know the magnitude and phase of $p _ { 1 }$ and the magnitude and phase of $U _ { 1 }$ at the initial end) then the integration is straightforward, proceeding from the initial end to the final end. But usually one or more boundary conditions are instead given at the final end. In such circumstances DELTAEC uses a shooting method,1 by guessing any unknowns among the four numbers defining $p _ { 1 }$ and $U _ { 1 }$ at the initial end of the integration, integrating to the other end, comparing the results with the target boundary conditions imposed at that other end or elsewhere, and adjusting its guesses until the integration results meet the targets.

![[mu_66afccee_8461f61bac97e203e031.jpg]]  
Figure 2.1: A simple open-topped bottle for the first example, <bottle0 .out>. (a) Conventional representation. (b) DELTAEC representation.

One of DELTAEC's most powerful features is that the guesses are not limited to the conventional choices consisting of the integration variables themselves, $p _ { 1 }$ and $U _ { 1 }$ , at the initial end of the numerical integration along x. Any variables that have an effect on the downstream target variables can be used. This enables DELTAEC to calculate a resonance frequency, a geometrical dimension, a temperature, or even the concentration in a binary gas mixture to satisfy given boundary conditions.

## 2.2 I/o file structure

We begin this tutorial with an open-topped bottle. This example introduces the basic input/output file structure of DELTAEC and how to “"run" the numerical integration.

DELTAEC recognizes all of its own output files as valid input files. In practice, users rarely make a new file from scratch; it is much more common to start with an existing file and modify it as needed. Thus, we begin with a file called <bottle0.out> (included in the <Examples\Acoustics> directory or folder that DELTAEC installs, usually in <d:\ProgramFiles\DeltaE\Examples\Acoustics>), which we created earlier from DELTAEC's user interface. Figure 2.1 shows the acoustician's usual cartoon of this bottle and a pictorial representation of how we modeled it for DELTAEC. For now, examine this file in a text editor. A DELTAEC model file must always be a plain text file, in the native text format of the machine on which it is running. The file name and path should avoid accented characters.

TITLE Model of 1982 Penn State Championship Bottle   
! - 0   
BEGIN The mouth   
1.0000E+05 a Mean P Pa   
300.00 b Freq Hz   
300.00 c TBeg K   
1.0000 d |pl Pa   
0.0000 e Ph(p) deg   
1.0000E-04 f |U| m^3/s   
0.0000 g Ph(U) deg   
air Gas type   
!--   
DUCT the neck   
2.1410E-04 a Area m^2 0.0000 A Ipl Pa   
5.1870E-02 b Perim m 0.0000 B Ph(p) deg   
1.7780E-02 c Length m 0.0000 C |U| m^3/s

<table><tr><td></td><td></td><td>0.0000 D Ph(U) 0.0000 E Htot 0.0000 F Edot</td><td rowspan="2">deg W W</td></tr><tr><td>ideal !-</td><td>Solid type 2</td></tr><tr><td>CONE Transition from neck to volume</td><td></td><td></td></tr><tr><td>2.1410E-04 a AreaI m^2</td><td>0.0000 A Ipl</td><td>Pa</td></tr><tr><td>5.1870E-02 b PerimI m</td><td>0.0000 B Ph(p)</td><td>deg</td></tr><tr><td>0.1003 c Length m</td><td></td><td>m^3/s</td></tr><tr><td>1.8680E-03 d AreaF m^2</td><td>0.0000 C IUI</td><td></td></tr><tr><td>0.1532 e PerimF m</td><td>0.0000 D Ph(U)</td><td>deg W</td></tr><tr><td>ideal Solid type</td><td>0.0000 E Htot</td><td>W</td></tr><tr><td>!- 3</td><td>0.0000 F Edot</td><td></td></tr><tr><td>DUCT Bottle volume</td><td></td><td></td></tr><tr><td>1.8680E-03 a Area m^2</td><td>0.0000 A Ipl</td><td>Pa</td></tr><tr><td>0.1532 b Perim m</td><td>0.0000 B Ph(p)</td><td>deg</td></tr><tr><td>0.1270 ) c Length m</td><td>0.0000 C |UI</td><td>m^3/s</td></tr><tr><td></td><td>0.0000 D Ph(U)</td><td>deg</td></tr><tr><td></td><td>0.0000 E Htot</td><td>W</td></tr><tr><td>ideal Solid type</td><td>0.0000 F Edot</td><td>W</td></tr><tr><td>SURFACE Bottom End</td><td>4</td><td></td></tr><tr><td>1.8680E-03 a Area m^2</td><td>0.0000 A Ipl</td><td>Pa</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>0.0000 B Ph(p)</td><td>deg</td></tr><tr><td></td><td>0.0000 C |UI</td><td>m^3/s</td></tr><tr><td></td><td>0.0000 D Ph(U)</td><td>deg</td></tr><tr><td></td><td>0.0000 E Htot</td><td>W</td></tr><tr><td>ideal Solid type</td><td>0.0000 F Edot</td><td>W</td></tr></table>

Several features of DELTAEC model files are illustrated here. Model files should be named <something. out>. These files consist of a set of “segments" whose order and format are important. After a TITLE (with an optional heading where the user can type notes), the initial (or "zeroth") segment is always a BEGIN segment. This is one of the "logistical" segments of DELTAEC, usually having no actual geometrical correspondence to parts of the hardware being modeled. Subsequent segments describe the geometry and other properties of the "physical" hardware parts of the acoustic system—here, DUCTs, a CONE, and a SURFACE. All units are MKS. The number and order of data in each segment is crucial. Within each line, the first number (e.g., “1.e5" or “100.") or word (e.g., "helium" or "BEGIN") is the most important to DELTAEC as input.2 Subsequent fields on each line give the units or name of the variable whose value appears. Lines that begin with "!" are comments with no impact on the integrations. Numbers can be in fixed or exponential format.3 Segment names are stored uppercase, and only the first five characters are interpreted.

The column of zeroes on the right side shows where DELTAEC's calculated results will appear. At the moment, they are all zero because DELTAEC has not yet calculated anything.

BEGIN sets the stage, in this case, with 1-bar room-temperature air being driven at 300 Hz with a pressure amplitude of 1 Pa and a volume flow rate amplitude of 0.0001 m3/s, in phase with the pressure oscillation. Some of these variables, such as frequency, extend unchanged through all subsequent segments. Other variables, such as pressure amplitude, are initial conditions for DELTAEC's numerical integration through subsequent segments.

A lossy duct segment, DUCT, comes next. Here, we have made the perimeter equal to √4π × area, to make this a circular duct. A CONE and another DUCT come next, completing the shape of the bottle. The file ends with a SURFACE to account for oscillatory-pressure thermal-hysteresis dissipation at the bottom.

## 2.3 Running DeltaEC

As children, most of us learn that blowing across the mouth of a bottle produces a pleasant audible tone. With this example, the new user of DELTAEC will obtain the frequency of that tone, while exploring the user interface and learning to "run" the numerical integration.

Open the file <bottle0.out>, using whichever of these three methods you prefer:

1. Open the folder <... \Examples\Acoustics> wherever your installation has created it, and double click on the file <bottle0.out>. If this folder is write-protected from changes, SaveAs to an unprotected folder immediately.

2. In Windows, find DELTAEC through the Start button at the bottom-left corner of your desktop, via Programs and the DELTAEC group. Double click on the program to launch it. Then open the file <bottle0.out> via the DELTAEC Files pulldown menu or by clicking the icon that looks like a manila folder. In either case, find your way to the <Examples Acoustics> folder in the usual way.

3. Double click on the Desktop DELTAEC icon to launch DELTAEC, and open the file <bottle0.out> as described in method 2.

After opening <bottle0.out>, DELTAEC displays the list of segments, like this:

![[mu_66afccee_64bcff0019efb1819011.jpg]]

Clicking on the “+" next to any segment's name exposes that segment's details. For example, to see the dimensions of the neck, click on the “+" next to 1 DUCT:

![[mu_66afccee_95dcf6d5c5d1b12e13c3.jpg]]

Blue text (numbers or words) means you can double click or right click to make a change or see more options. Italic red numbers indicate what will be a result, as soon as the calculation is run, but right now the red color indicates that these numbers are probably inconsistent with the blue input numbers. Green numbers that you will see shortly indicate good results: calculated by DELTAEC and consistent with all the other numbers in the model.

Now show all the segments in the model, by clicking on the “+" for each segment or on the big $^ { 6 6 } + / - ^ { 3 3 }$ on the toolbar. What you see should look like this:4

TITLE Model of 1982 Penn State Championship Bottle   
0   
BEGIN The mouth   
1.0000E+05 a Mean P Pa   
300.00 b Freq Hz   
300.00 c TBeg K   
1.0000 d lpi Pa   
0.0000 e Ph(p) deg   
1.0000E-04 f |UI m^3/s   
0.0000 g Ph(U) deg   
air Gas type   
!– 1   
DUCT the neck   
2.1410E-04 a Area m^2 0.0000 AIpl Pa   
5.1870E-02 b Perim m 0.0000 B Ph(p) deg   
1.7780E-02 c Length m 0.0000 C IUI m^3/s   
0.0000 D Ph(U) deg   
0.0000 E Hdot W   
ideal Solid type 0.0000 F Edot W   
2   
CONE Transition from neck to volume   
2.1410E-04 a AreaI m^2 0.0000 AIpl Pa   
5.1870E-02 b PerimI m 0.0000 B Ph(p) deg   
0.1003 c Length m 0.0000 C IUI m^3/s   
1.8680E-03 d AreaF m^2 0.0000 D Ph(U) deg   
0.1532 e PerimF m 0.0000 E Hdot W   
ideal Solid type 0.0000 F Edot W   
3   
DUCT Bottle volume   
1.8680E-03 a Area m^2 0.0000 AIpl Pa   
0.1532 b Perim m 0.0000 B Ph(p) deg   
0.1270 c Length m 0.0000 C |UI m^3/s   
0.0000 D Ph(U) deg   
0.0000 E Hdot W   
ideal Solid type 0.0000 F Edot W   
(etc.)

The BEGIN segment establishes that the bottle is full of air at atmospheric pressure and room temperature, and it launches a 300-Hz wave into the bottle with a pressure amplitude of 1 Pa and a volume-flow-rate amplitude of $1 0 ^ { - 4 } ~ \mathrm { m ^ { 3 } / s }$ (We will examine its “optional" parameters in later chapters, when we encounter them.)

Now, run the file, by typing 'r', by clicking the blue "Run" button, or by accessing "Run" in the Tools pulldown menu. (To encourage users to get in the habit of using the keyboard shortcuts, the Users Guide summarizes all such options in the briefest possible way, with the shortcut letter underlined, e.g., run. Infrequently used operations whose shortcuts the user has not memorized can be found by browsing the pulldown menus.)

Upon running, the Run Monitor appears at the bottom of the display, indicating with its cheerful green color and the word "Success" that the run has succeeded, in this case taking only a fraction of a second. (Typing "b" toggles the Run Monitor display off and on, and resets it to default size.) Now the results in the right column of the model display are nonzero, and they have changed from red italic to green, indicating that they are consistent with one another and with the blue input numbers:

![[mu_66afccee_3c84ef32c8c7cbf3df00.jpg]]  
DELTAEC has integrated through the model and calculated some results, in particular $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ . The results in the right column of the <. out> file show values for $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ and other results at the end of each segment. If a few numbers are all you want to see, you are done!

One of the other results is the acoustic power Edot,

$$
\dot { E } = \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \widetilde { U } _ { 1 } \right] ,\tag{2.8}
$$

which is always listed at line F.

The total power Htot, listed at line E, is introduced in Chapter 5; it can safely be ignored in this chapter, and for all purely acoustic problems in which heat exchangers and time-averaged temperature gradients in the x direction are of no concern.

## 2.3.1 Font augmentation

You can change the size of the font in DELTAEC's main display and many secondary windows by spinning your mouse wheel while holding down the Ctrl key, or by using Ctrl n, Ctrl b, and Ctrl /. (Be sure the computer's focus is on the DELTAEC window—click it if necessary.) Resizing the DELTAEC window by dragging its perimeter with the mouse, or making DELTAEC fill the entire screen by clicking the usual Windows "Maximize" button in the top-right corner, makes more room for a bigger font.

Alternatively, enlarge everything, including the menu texts, via your computer's operating system: In Windows 10, Start, Settings, Ease of Access; in Windows 7, Start, Control Panel, Ease of Access Center.

The shades of blue, green, and red used to indicate different types of variables seem to show up well for color-blind users, and italic is used with red to emphasize its difference.

## 2.3.2 Running DeltaEC from terminal

See Section 11.5.3 for launching DELTAEC from a Windows Command Prompt, so it can be controlled by human keystrokes or by another program.

## 2.4 State plots

State plots allow the user to view graphs showing the distribution of temperature, pressure, volume flow rate, energy, and many other variables as functions of x along the entire length of a model or any subset of that length. After each successful run, DELTAEC creates a state-plot file, <.sp>, with this information in tabular format. You can open this file from your hard disk folder with any text editor or spreadsheet program, or display it with DELTAEC's plotter, using "Plot SP file" in the Display pulldown menu. The example below, <bottle2.sp> (<bottle2> is identical to <bottle0>, except that it includes the <.ssv.\*> files, described below), does not show all of the available columns of data; a text editor or spreadsheet would let you scroll across to view more columns to the right.

-> bottle2.sp   
!Created@16:15:21 26-Jun-2020 with DeltaEC Fortran Vers. 6.4b2.8 for the IBM/PC-Compatible   
== Model of 1982 Penn State Championship Bottle   
Leg:Seg x(m) GasA(m^2) Tm(K) Re[p](Pa) m[p](Pa) Re[U](m3/s) Im[U] (m3/ Edot (W) Htot(W) Xdot(W) H2k(W)   
0: 1 0.0000 2.1410E-04 300.00 1.0000 0.00000 1.0000E-04 0.00000 5.0000E-05 5.0000E-05 5.0000E-05 5.0000E-05   
0: 1 0.17780E-02 2.1410E-04 300.00 0.97044-1.8466 9.9995E-05 -5.0520E-09 4.8524E-05 5.0000E-05 4.8524E-05 5.0000E-05   
0: 1 0.35560E-02 2.1410E-04 300.00 0.94079-3.6931 9.9981E-05 -9.8803E-09 4.7049E-05 5.0000E-05 4.7049E-05 5.0000E-05   
0: 1 0.53340E-02 2.1410E-04 300.00 0.91106 -5.5391 9.9957E-05 -1.4484E-08 4.5574E-05 5.0000E-05 4.5574E-05 5.0000E-05   
0: 1 0.71120E-02 2.1410E-04 300.00 0.88126-7.3847 9.9924E-05 -1.8864E-08 4.4099E-05 5.0000E-05 4.4099E-05 5.0000E-05   
0: 1 0.88900E-02 2.1410E-04 300.00 0.85138-9.2296 9.9881E-05 -2.3019E-08 4.2625E-05 5.0000E-05 4.2625E-05 5.0000E-05   
0: 1 0.10668E-01 2.1410E-04 300.00 0.82145 -11.074 9.9828E-05 -2.6948E-08 4.1151E-05 5.0000E-05 4.1151E-05 5.0000E-05   
0: 1 0.12446E-01 2.1410E-04 300.00 0.79147-12.916 9.9766E-05 -3.0652E-08 3.9679E-05 5.0000E-05 3.9679E-05 5.0000E-05   
0: 1 0.14224E-01 2.1410E-04 300.00 0.76143 -14.758 9.9695E-05 -3.4131E-08 3.8207E-05 5.0000E-05 3.8207E-05 5.0000E-05   
0: 1 0.16002E-01 2.1410E-04 300.00 0.73136-16.598 9.9614E-05-3.7384E-08 3.6737E-05 5.0000E-05 3.6737E-05 5.0000E-05   
0: 1 0.17780E-01 2.1410E-04 300.00 0.70125-18.437 9.9523E-05 -4.0410E-08 3.5268E-05 5.0000E-05 3.5268E-05 5.0000E-05   
0: 2 0.17780E-01 2.1410E-04 300.00 0.70125-18.437 9.9523E-05-4.0410E-08 3.5268E-05 5.0000E-05 3.5268E-05 5.0000E-05   
0: 2 0.27810E-01 3.0593E-04 300.00 0.57049-27.070 9.8705E-05-5.6936E-08 2.8926E-05 5.0000E-05 2.8926E-05 5.0000E-05   
0: 2 0.37840E-01 4.1411E-04 300.00 0.49056 -33.194 9.7221E-05 -7.4038E-08 2.5075E-05 5.0000E-05 2.5075E-05 5.0000E-05   
0: 2 0.47870E-01 5.3864E-04 300.00 0.43818 -37.714 9.4922E-05-9.2322E-08 2.2537E-05 5.0000E-05 2.2537E-05 5.0000E-05   
0: 2 0.57900E-01 6.7951E-04 300.00 0.40204 -41.137 9.1660E-05 -1.1240E-07 2.0738E-05 5.0000E-05 2.0738E-05 5.0000E-05   
0: 2 0.67930E-01 8.3673E-04 300.00 0.37614 -43.769 8.7294E-05 -1.3491E-07 1.9370E-05 5.0000E-05 1.9370E-05 5.0000E-05   
0: 2 0.77960E-01 1.0103E-03 300.00 0.35699 -45.807 8.1687E-05 -1.6050E-07 1.8257E-05 5.0000E-05 1.8257E-05 5.0000E-05   
0: 2 0.87990E-01 1.2002E-03 300.00 0.34247-47.382 7.4709E-05-1.8981E-07 1.7290E-05 5.0000E-05 1.7290E-05 5.0000E-05   
0: 2 0.98020E-01 1.4065E-03 300.00 0.33123-48.585 6.6239E-05-2.2353E-07 1.6400E-05 5.0000E-05 1.6400E-05 5.0000E-05   
(etr etr

bottle2.sp  
![[mu_66afccee_bbaf85b05a19a7c90837.jpg]]  
Figure 2.2: State plots of $p _ { 1 }$ and $U _ { 1 }$ for <bottle2>.

State-plot files have the following features:

• Numbers are lined up in columns. The initial columns are leg number (relevant when TBRANCH and/or multiple BEGIN segments are used; described in Section 11.2.1), segment number, and x.

• DELTAEC writes Nint +1 lines of data for each segment that it integrates $( \mathrm { e . g . }$ , ducts, cones, and stacks). Nint is the number of Runge-Kutta integration steps—see Section 8.1 for details.

• DELTAEC writes two lines of data for lumped elements (e.g., SURFACE) and other short segments that do direct end-to-end calculations (e.g., most heat exchangers): one line before and one line after the segment is computed.

• Logistical segments (e.g., BEGIN) that do not correspond to any hardware parts generate nothing in the <.sp> file.

The files <bottle2.ssv.dir> and <bottle2.ssv.dat> instructed DELTAEC's plotter that we wish to see graphs of $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ after each run. These graphs, shown in Fig. 2.2, will automatically refresh after each new run, as the user makes changes to the model.

The real parts of $p _ { 1 }$ and $U _ { 1 }$ show the values of oscillating pressure and oscillating volume flow at times $\omega t \ = \ 0$ , 2π, 4π, ... and the imaginary parts show their values at times $\omega t = - \pi / 2 , 2 \pi - \pi / 2 , 4 \pi - \pi / 2$

DELTAEC's plotter lets the user select other plots easily. The time-averaged product of $\mathrm { R e } [ p _ { 1 } e ^ { i \omega t } ]$ and $\operatorname { R e } [ U _ { 1 } e ^ { i \omega t } ]$ is acoustic power $\dot { E }$ , which is also interesting. To change the display for this model to $\dot { E }$ VS $x ,$ check the y box under Edot, and uncheck the Re[p], Im[p], Re[U], and Im[U] boxes, to obtain Fig. 2.3. Chapter 3 explains much more about DELTAEC's plot capabilities.

Now use Save Copy As to save this file with a new name, <bottle3.out>. Examine the resulting file with a text editor. Note that the output results giving $p _ { 1 }$ and $U _ { 1 }$ at the ends of the DUCT, CONE, DUCT, and SURFACE are now part of the file. The fact that we want to plot $\dot { E }$ vs x from now on has also been included in the associated <bottle3.ssv> file.

![[mu_66afccee_db1ae0016038864332c7.jpg]]  
Figure 2.3: $\dot { E }$ vs x for <bottle2>.

## 2.5 Guesses and targets

The astute reader may have noticed that $U _ { 1 }$ was not zero at the SURFACE above. (In fact, we left a hole in the bottom of Fig. 2.1(b) to indicate the possibility of this leakage.) This shows that our choice of initial values for $p _ { 1 }$ and $U _ { 1 }$ at the BEGIN was incompatible with a bottle that is supposed to be sealed at the bottom. In this section we introduce DELTAEC's shooting method to resolve this issue, allowing boundary conditions at the end of a model (or anywhere else in a model) to be “targeted" to desired values.

Start DELTAEC again, opening file <bottle2.out>. As a matter of good habit, run it, and check some plots for sanity (your own sanity, as well as DELTAEC's). Now open the “Guesses and Targets" summary display box. You can open this box through the pull-down menus by clicking on Display, then Guesses Targets. Alternatively, just type $\mathrm { ^ { 6 } g ^ { 3 } }$ (the $\mathrm { ^ { 6 } g ^ { 3 } }$ stands for “guesses"). The guess-target summary should look like this:

![[mu_66afccee_c58407d0dab912806d9a.jpg]]

![[mu_66afccee_7b086dbba63236cd79fc.jpg]]  
Figure 2.4: The bottle. (a) HARDEND untargeted, so $U _ { 1 }$ can be nonzero at the bottom. (b) HARDEND targeted to (0.00, 0.00), to seal the bottom.

The table is blank: At this point DELTAEC has no guesses and no targets. Each time we have run DELTAEC thus far in the tutorial, it has integrated along x only once, starting from the values of $p _ { 1 }$ and $U _ { 1 }$ that we gave it in the BEGIN segment.

To set up this model with appropriate targets, we need to insert an additional segment at the end of the model. To insert a segment, pull down the Edit menu and click on Insert Seg, or type ${ } ^ { \mathfrak { s } } { } _ { 1 } ^ { \mathfrak { s } }$ , or right click below the last segment and select Append. Whichever way you choose to do it, insert a HARDEND, at the end of the model, after the SURFACE.

Now establish 5a and 5b in the HARDEND as targets by clicking on Possible targets in the HARDEND itself or through Add Targ in the guess-target summary. Inspect your work thus far by examining the guess-target summary:

![[mu_66afccee_abb3c33281356508b83c.jpg]]  
Also notice how the targets are flagged with yellow markers in the main display.

(We could have programmed HARDEND segments with the real and imaginary parts of $U _ { 1 }$ as our targets, but experience has shown that the DELTAEC shooting-method algorithm usually works without extra attention from us if we normalize the targeted $U _ { 1 }$ by dividing by area and $p _ { 1 }$ . The rare occasions when more attention is needed are described in Section 8.3.2.)

We have two targets, which will soon enforce complex $U _ { 1 } = 0$ at the bottom end of the model, appropriate for the sealed end of the bottle. We must choose two guesses that DELTAEC can adjust to meet those targets.5 Basically, DELTAEC integrates from BEGIN to HARDEND. DELTAEC will refine whatever two guess variables we allow it to vary, to find a solution to this acoustics problem that arrives at the HARDEND with zero complex volume flow rate. What to choose as these guesses depends on exactly what situation you are trying to model. Do you have in mind a resonator driven by a fixed volume flow rate amplitude, or one that is driven by a fixed pressure amplitude? Neither answer is wrong; it depends on the circumstances.

In the present example, we arbitrarily choose to keep $| U _ { 1 } |$ fixed at 0.0001 $\mathrm { m ^ { 3 } / s } ,$ and let DELTAEC adjust $p _ { 1 }$ . Begin to accomplish this by adding 0d and 0e as guesses, by double clicking or right clicking on their values and selecting “guess," or through Add Guess in the guess-target summary. Inspect the resulting situation by looking at the summary.

![[mu_66afccee_049058c8990035f1c1fe.jpg]]  
The target values are red italic, indicating that DELTAEC does not know whether results

5Users sometimes ask why we need two targets and two guesses when we are really only trying to impose one constraint at the HARDEND, namely $| U _ { 1 } | = 0$ . The answer to this question can be appreciated by imagining a blindfolded archer trying to hit a bull's-eye. If an observer tells the archer “Your last attempt missed by 2.5 meters," which way is the archer supposed to revise her aim for her next attempt to hit the target? More useful information is conveyed if the observer tells the archer “Your last attempt struck 1.5 meters above the bull's-eye and 2.0 meters to the left of the bull's-eye." Like the blindfolded archer's target, DELTAEC's HARDEND is a point target in a two-dimensional space, namely the complex plane of $U _ { 1 }$ DELTAEC needs to adjust its aim (its guesses) in two dimensions to hit the target, and DELTAEC can hit the target in a small number of attempts if it gets two-dimensional information about how far off-target it is.

are consistent with input variables; it knows that it has not yet run with the most recent changes of input variables. The guesses (1 Pa, 0 degrees) are still just the values that are left over from before. DELTAEC has not yet adjusted the guesses to try to hit the targets, but it is ready to do so, because there are equal numbers of guesses and targets: two each in this case.

With an equal number of guesses and targets, let's run. After running, DELTAEC's Run Monitor at the bottom of the display reports that it integrated along x 28 times while adjusting guesses and coming ever closer to the targets, and it spent 0.08 seconds doing so. (The numbers that are reported by the Run Monitor may vary from computer to computer and version to version. How close to the targets is judged to be “close enough" is described in Section 8.3.2.)

Inspect the results:

![[mu_66afccee_47c13e42cbeaea53790e.jpg]]

The value of the phase shown in 0e, 7288.6°, might seem strange until we realize that DELTAEC does not understand that integer multiples of 360° can be subtracted from any phase angle without consequence. With the initial guessed value of 0d so far from reality, DELTAEC's shooting method wandered far, looking for a solution; under normal circumstances, we might have given it a more plausible starting point (such as the result of a previous run). Subtracting 7200° from the value of 0e for the sake of our human sanity and running again yields

![[mu_66afccee_b7ada4c2fc7c0512ff40.jpg]]  
The targets are accurately met, because DELTAEC has adjusted the two guesses to be

![[mu_66afccee_1f017b39b293a6d69e71.jpg]]  
Figure 2.5: State plots for the bottle, with HARDEND targets met so $U _ { 1 } = 0$ at the bottom.

31.870 Pa, 88.622 degrees. The state plots in Fig. 2.5 also show that the targets have been met, because they show that $| U _ { 1 } | = 0$ at the end.

Saveas the <.out> file with a new filename of your choosing, and examine it with a text editor to see how DELTAEC has indicated which variables are guesses and targets, next to the guesses and targets themselves and in the restart table at the bottom of the file.

Most of the thought required to successfully use DELTAEC occurs while trying to figure out which of the variables are appropriate targets and guesses, i.e., what constraints must be imposed on results of a single DELTAEC integration pass, and what variables are needed as inputs by a single DELTAEC integration pass but are in fact unknown to us when we ask DELTAEC to run. While many choices are possible (as long as the number of guesses equals the number of targets), some choices are physically nonsensical and cannot succeed. For example, asking DELTAEC to try to achieve resonance in a given bottle by guessing the mean pressure of the air would be futile, because the speed of sound in an ideal gas is independent of pressure. In the examples in subsequent Chapters, and in advanced use of DELTAEC, the choice of good target and guess variables is seldom as easy as it is in this simple example.

Notice the use of columnar location and color in the display: Columns organize variables according to DELTAEC's most short-sighted internal needs, while colors organize variables according to users' needs. The numbers in the left column (ordinary blue numbers, and the guesses, and the bull's-eye target values) are variables needed by DELTAEC in each pass of its integration, as it integrates repeatedly, adjusting the guesses to try to hit the bull's-eyes. Variables in the right column are computed as results in each pass, and are displayed green when targets are met. We users, however, often wish to forget that DELTAEC must adjust guesses and hit targets. From our perspective, blue numbers are what we give DELTAEC as known quantities, and green numbers are the results that we want DELTAEC to give us. If the green numbers are indeed green, DELTAEC feels confident of its results, but when those numbers are red DELTAEC is not displaying a consistent set of results, for any of a number of reasons—usually because we have not yet run it or because it has missed the targets.

Now let's find the resonance frequency f, which is the frequency at which the bottle

![[mu_66afccee_c86398286f76e51f3ca7.jpg]]  
Figure 2.6: State plot with HARDEND targeted and resonance achieved, so $U _ { 1 } = 0$ at the bottom and $p _ { 1 }$ and $U _ { 1 }$ are in phase at the mouth.

sings when we blow across its top. Look at the guess-target summary to get oriented.

Guess-Target Summary:   
GUESS 0d Oe   
name BEGIN: lpl BEGIN:Ph(p)   
units Pa deg   
value 31.870 88.587   
TARGET 5a 5b   
name HARDE:R(1/z HARDE:I(1/z   
value 0.0000 0.0000   
result -5.6504E-13 4.1801E-14

First, think about the physics long enough to realize that having $p _ { 1 }$ and $U _ { 1 }$ in phase at the mouth is a suitable, approximate condition for resonance.6 Now make the corresponding changes in the DELTAEC model: modify 0e to be $0 ^ { \circ }$ instead of 88 $. 6 ^ { \circ }$ and remove 0e from the guess list so DELTAEC cannot change it any more. Next, add 0b, the frequency, in the guess list. Inspect the guess-target summary again. Now, “run" the calculation. Inspect the results in the main display or the guess-target summary, finding that the resonance frequency is 194.95 Hz. Inspect the state plots in Fig. 2.6, to see that the desired boundary conditions at both ends are met. Save (save) this version as bottle5, for use later in this Chapter.

As acousticians, we know that this resonator has more than one resonance mode. To find another one, modify 0b to be 600 Hz, and run again. With this starting guess, DELTAEC converges on the 2nd mode, resembling $3 / 4$ of a wavelength from end to end, at 1029.6 Hz.

DELTAEC can use any physically appropriate input variable as a guess. We could have learned what temperature makes the system resonate at 180.00 Hz, by using 0c instead of

0b as a guess. (The answer is 255 Kelvin.) Or, by using 1c as a guess, we could have found out what length the neck should be to put the resonance at 180 Hz at 300 K.

DELTAEC's gas library contains three binary mixtures of gases: He-Xe, He-Ar, and Ne-Xe. These introduce another real variable in BEGIN: the mole fraction of helium in the mixture (for example, He-Ar with $n _ { L } = 0 . 8 8 9$ indicates 88.9% helium and 11.1% argon). The helium fraction in one of these mixtures can be used as a guess variable for resonance. Simply add 0j as a guess. Thus, we could learn the helium concentration that would have to be added to argon in the bottle to make the resonance equal 180.00 Hz

For advanced guidance about using guesses and targets, see Sections 5.2 and 5.3.

## 2.6 Other acoustics features

Here we briefly describe some additional DELTAEC features that are relevant to a simple acoustic apparatus for which $\mathcal { F } _ { \mathrm { m o m e n t u m } }$ and $\mathcal { F } _ { \mathrm { c o n t i n u i t y } }$ in Eqs. (2.6) and (2.7) are the only equations that we want DELTAEC to integrate.

## 2.6.1 Simple segment types

A list of the most commonly used purely acoustic segment types (including those introduced above) is given below. More detailed descriptions and the calculations performed by each are given in Chapter 10 and Chapter 11.

TITLE Required at the top.

BEGIN Required immediately after TITLE. The "zeroth" segment must be BEGIN. It contains global variables such as mean pressure, gas type, and frequency, and initial conditions for variables that can vary with x, including p1, U1, and mean temperature (whose x dependence is introduced in Chapter 5). See details in Section 11.1.2.

SURFACE A surface area with pressure-hysteresis loss in its thermal penetration depth. Usually used at ends of ducts. See details in Section 10.2.2.

DUCT A duct, with viscous and thermal losses at the wall if the perimeter is realistically nonzero. Separate entry of area and perimeter accommodates ducts of any crosssectional shape. Laminar or turbulent. See details in Section 10.1.1

CoNE A cone, often used to adapt between ducts of different sizes. Uses lossy Webster horn / \ equation. Laminar or turbulent. See details in Section 10.1.2.

COMPLIANCE An acoustic compliance, i.e., a volume full of gas. Pressure-hysteresis losses on surface. See details in Section 10.2.1.

IMPEDANCE A lumped-parameter, series impedance. Resistance and inertial reactancegare specified. See details in Section 10.2.3. 1WW

IDUCER and vDUCER Current-driven and voltage-driven transducers, with parameters independent of frequency, connected “on the side" of the DUCTs or other segments. See Fig. 2.7. See details in Section 10.4.2

ISPEAKER and vSPEAKER Current-driven and voltage-driven electrodynamic transducers, parameterized by mass, B-l product, etc., so impedance coefficients depend on frequency. Connected “on the side" of a sequence of DUCTs or other segments. See Fig. 2.7. See details in Section 10.4.2.

IEDUCER and VEDUCER, IESPEAKER and VESPEAKER The four transducers that were described above, which do not have “E" as the second letter in their names, are connected in side-branched configurations, where the “back side" of the transducer hangs outside of DELTAEC's computation space. The four Enclosed versions are their series counterparts, with one side of the transducer facing the previous segment and the other side facing the subsequent segment, so the volume flow rate remains constant across the segment (except for thermal-hysteresis effects on the surfaces) and $p _ { 1 }$ usually changes significantly. See Fig. 2.8. See details in Section 10.3.1.

$$
v = \frac { \beta } { \alpha }
$$

Figure 2.7: IDUCER, VDUCER, ISPEAKER, and VSPEAKER are attached as side branches to the series of DELTAEC segments.

$$
\begin{array}{c} v = \boxed { \boxed { \begin} {array} { r l } \end{array} }
$$

Figure 2.8: IEDUCER, VEDUCER, IESPEAKER, and VESPEAKER are acoustically in series with the adjacent DELTAEC segments.

BRANCH A frequency-independent side-branch impedance. See details in Section 10.4.1.

$$
1 1 0 0 - m - 1 1
$$

OPNBRANCH and PISTBRANCH Frequency-dependent side-branch impedances with the frequency characteristics of the radiation impedance of an opening into 4π or 2π solid angle, respectively. See details in Section 10.4.1.

HARDEND A logistical final segment, used to enforce $U _ { 1 } = 0$ through use of the inverse of the acoustic impedance in the target list. See details in Section 11.1.3.

SOFTEND A logistical final segment. Can be used to set $p _ { 1 } = 0$ through use of the acoustic impedance in the target list. Useful for defining a mirror-image plane in symmetric apparatus with a pressure node at a center of symmetry. Also used for loops and networks of segments, to mark a location that will be reconnected elsewhere in the model. See details in Section 11.1.3.

## 2.6.2 The zero of time

The phases of the complex functions $p _ { 1 }$ and $U _ { 1 }$ encode the time phases of the sinusoidally oscillating parts of $p ( t )$ and $U ( t )$ . Within a DELTAEC model, phase differences are vital, but the overall “zero" of phase is arbitrary, for the same reason that the "zero" of time is arbitrary in classical physics. For example, in the <bottle> considered above, any arbitrary phase θ can be added to 0e and 0g, and the only consequence is that θ is added to all Ph(p) and Ph(U) results, shifting the zero of time by $- ( \theta / 3 6 0 ^ { \circ } ) ( 1 / f )$

The skilled user of DELTAEC should be conscious of where the overall, arbitrary time phase is set in a model. Usually this occurs in BEGIN, where Ph(p) or Ph(U) is fixed at zero or some other value. However, in some models, the phase of a transducer's electric current or voltage is fixed, and the phase of whichever phasor in BEGIN has nonzero amplitude must be guessed. (If one of the phasors has zero amplitude, its time phase is meaningless.)

Human convenience or convention often suggests a wise choice for the zero of phase in a model. In the <bottle>'s <.sp> plots, the real and imaginary parts of $p _ { 1 }$ and $U _ { 1 }$ are easiest to interpret if the phases of $p _ { 1 }$ and $U _ { 1 }$ are mostly near $0 ^ { \circ } , 9 0 ^ { \circ } , 1 8 0 ^ { \circ }$ , and/or $2 7 0 ^ { \circ }$ rather than near 45°, 135°, etc. In pulse-tube-refrigerator models, some of us find it most convenient to set Ph $( \mathsf { p } ) = 0$ in the pulse tube itself, or at a nearby pressure sensor, which requires guessing one or both of the BEGIN phases and using an RPN target (see Chapter 4) to enforce the desired condition. When a phase must be targeted, avoid doing so near 180°, because target results must be smooth functions of guesses, as explained at the end of Section 8.5.

## 2.6.3 Gases and solids

DELTAEC recognizes many gases7 and solids, and routinely calculates their properties such as density, specific heat, and viscosity. Gases are specified in BEGIN segments, and solids are specified in each physically realistic segment. As described in detail in Chapter 12, DELTAEC includes the following “gases": dry air, humid air and fog, helium (in idealgas approximation), cryogenic helium (accurate near 4 Kelvin), neon, argon, He-Xe mixtures, He-Ar mixtures, Ne-Xe mixtures, hydrogen, deuterium, nitrogen, carbon dioxide, natural-gas combustion products (i.e., flue gas), liquid sodium, and eutectic liquid sodiumpotassium. The ideal-gas equation of state is used for most of the gases, while carbon dioxide, cryogenic helium, argon, sodium, and eutectic sodium-potassium have more-accurate equations of state.

Solids, described in detail in Chapter 13, include Kapton, Mylar, stainless steel, molybdenum, tungsten, copper, nickel, Celcor, ideal, and a few exotic solids used in cryogenic regenerators. An ideal solid has extremely high heat capacity, density, and thermal conductivity.

DELTAEC also allows users to specify “external," user-defined gases or solids that are not part of its own internal library. Properties are calculated, according to local $T _ { m }$ and $p _ { m }$ from coefficients read from a user-written text file. Up to five user-defined gases and five user-defined solids can be used at one time. Details of user-defined pure gases and binary mixtures are described in Sections 12.18.1 and 12.18.2, respectively. Details of user-defined solids are described in Section 13.17.

To illustrate the use of a single-component user-defined gas, consider the example below. To replace DELTAEC's internal “ideal" helium gas (see Section 12.1) with a more accurate representation that calculates density and sound speed including the first coefficient of the virial expansion for helium, we can create the following file in a text editor, call it <helium.tpf>, and put it in the same folder as our model:

! user-defined gas; He with first virial coeff (B=12cc/mole)   
! Equation is in UsersGuide Section 12.15:   
! CO + C1\*pm/(T+C2\*pm) + C3\*T + C4\*T^2 + C5\*T^C6 + pm^2 \*C7\*T^C8 + pm\*C9   
! Density, rho (m^3):   
0. 4.814e-4 1.44e-6   
! isobaric heat capacity, cp (J/kg-K):   
5192.   
! Thermal conductivity, k (W/m-K):   
0. 0. 0. 0. 0. 0.0025672 0.716   
! Square of sound speed, a^2 (m^2/s^2):   
0. 0. 0. 3461.92 0. 0. 0. 0. 0. .0100   
! Viscosity, mu (kg/m-s):   
0. 0. 0. 0. 0. 0.412e-6 0.68014

The coefficients for density in this file are used by DELTAEC in Eq. (12.1) and were determined by a user who knew that

$$
\rho _ { m } = \frac { p _ { m } m } { R _ { \mathrm { u n i v } } ( T _ { m } + B p _ { m } / R _ { \mathrm { u n i v } } ) } ,\tag{2.9}
$$

where $R _ { \mathrm { u n i v } } = 8 . 3 1 4 ~ \mathrm { J / m o l e - K }$ , the molar mass $m = 0 . 0 0 4 0 0 2 6 ~ \mathrm { k g / m o l e } .$ and the first virial coefficient $B = 1 . 2 \times 1 0 ^ { - 5 } ~ \mathrm { m ^ { 3 } / m o l e }$ . Thus, the user set $C _ { 1 } = m / R _ { \mathrm { u n i v } }$ and $C _ { 2 } = B / R _ { \mathrm { u n i v } }$ in the density line in the <.tpf> file. For squared sound speed, the user knew that

$$
a ^ { 2 } = \frac { \gamma R _ { \mathrm { u n i v } } T } { m } \left( 1 + 2 \frac { B p _ { m } } { R _ { \mathrm { u n i v } } T _ { m } } \right) ,\tag{2.10}
$$

yielding $C _ { 3 } = \gamma R _ { \mathrm { u n i v } } / m$ , and $C _ { 9 } = 2 B \gamma / m$ in the square-of-sound-speed line in the <.tpf> file, where $\gamma = 5 / 3$

User-defined gas mixtures (described in Section 12.18.2) and user-defined solids (described in Section 13.17) follow similar formats.

It is a good idea to check your implementation of a new user-defined gas or solid very carefully by using one of the two ways of displaying or plotting thermophysical properties described in Section 2.7.7.

## 2.6.4 Turbulence

A turbulence algorithm can be enabled in DUCT and CONE, by double clicking on “Optional parameters." Checking the Turbulence box brings up parameter d in DuCT and parameter f in CoNE, which specify the relative roughness (roughness height divided by pipe diameter). Set the roughness equal to a small value greater than zero for rough walls. (We usually use

$5 \times 1 0 ^ { - 4 }$ , even if this is larger than the actual relative roughness of the channel.) To ensure a laminar calculation, check the laminar box for the segment (which causes the roughness parameter to be hidden from view in the <.out> file).

The turbulence algorithm, which is described in detail in Section 10.1.1, follows the quasisteady approximation, (the spirit of the assumptions of Iguchi et al., Ref. [15]), assuming that oscillatory-flow losses can be calculated by using the steady-flow Moody friction factor at each instant of time during the oscillatory flow, with the surface roughness used as an experimentally determined fitting parameter. The quasi-steady assumption has only a little experimental validation for DUCTs and CoNEs in the range of Reynolds number and $R / \delta _ { \nu }$ of interest in thermoacoustics (where R is radius), but we believe it provides a useful estimate, much better than no estimate at all.

## 2.7 Other useful features

## 2.7.1 Keeping parameters equal

The sameas nl feature ties an input parameter in one segment to a value elsewhere. This helps prevent typographical errors in the <.out> file, and is especially useful in linking dimensions of adjacent segments that you might want to vary all together while modifying or plotting, such as areas of adjacent segments when increasing the size of the apparatus. Specify the segment number and line letter (e.g., “sameas 3a").

The following example is for the bottle we modeled above:

1   
DUCT The neck   
2.141e-4 a Area m   
5.187E-2 b Perim m   
1.778E-2 c Length m   
ideal Solid type   
!-- 2   
CONE transition from neck to volume   
sameas 1a a AreaI m^2   
sameas 1b b PerimI m   
.100 c Length m   
sameas 3a d AreaF m^2   
sameas 3b e PerimF m   
ideal Solid type   
!-- 3   
DUCT Bottle volume   
1.868e-3 a Area m^2   
0.1532 b Perim m   
0.1270 c Length m   
ideal Solid type   
!-- 4   
SURFACE Second End   
sameas 3a a Area m^2   
ideal Solid type

![[mu_66afccee_cd35599a389e0c36a36d.jpg]]

When you add a parameter specified by sameas to the guess list, you must first sever the sameas relationship. This is required because the value at this point will be controlled by DELTAEC's shooting method. But if a variable that is the root of one or several sameas references is caused to change by DELTAEC itself in any way, e.g., as a guess, all sameas references to this root within the model will change with it.

## 2.7.2 Master-slave links

When geometric variables are changed, whether by the user, by DELTAEC's shooting method, or by DELTAEC's incremental plot routine, there are often geometric relationships with other parameters that should be maintained. For example, if the area of a duct increases, we should usually increase the associated perimeter as well. Another common wish is to lengthen one segment while simultaneously shortening another segment to keep overall length constant. Master-slave links are available in some segments for just these purposes; a Master-Slave Links option appears in a segment whenever a built-in parameter-linking capability is possible for variables in that segment.

For example, consider a DUCT whose cross section is a half circle attached to a square, as shown in Fig. 2.9. The cross-sectional area is

$$
A = { \frac { 1 } { 2 } } { \frac { \pi } { 4 } } d ^ { 2 } + d ^ { 2 } ,\tag{2.11}
$$

and the perimeter is

$$
\Pi = \frac { \pi } { 2 } d + 3 d .\tag{2.12}
$$

Notice that

$$
c = \frac { \Pi ^ { 2 } } { A } = \frac { { ( \pi + 6 ) } ^ { 2 } } { \pi / 2 + 4 } \simeq 1 5 . 0 0 1\tag{2.13}
$$

is a constant, independent of the size d of the DUCT, but depending on the half-circle-plussquare character of its shape. Additional examples are $c = 4 \pi$ for a circular duct, $c = 1 6$ for a square duct. When perimeter-area linking is established in a DUCT, DELTAEC remembers the value of this constant $c ,$ and uses it thereafter in

$$
\Pi = { \sqrt { c A } }\tag{2.14}
$$

to update the perimeter based on the area, thereby maintaining the cross-sectional shape. Thus, as area is changed, this link keeps a circular duct circular and maintains the aspect ratio of a rectangular duct.

Below is a list of all parameter-link options and the segment types for which they are available, including some for segments that have not yet been introduced in this tutorial. The numbers in parentheses at the end indicate how the link is recorded in the restart table at the bottom of the <.out> file. Figure 2.10 illustrates these links.

![[mu_66afccee_92fcf2538bba7f7ce3a7.jpg]]  
Figure 2.9: When the area of a DUCT is changed and perimeter-area linking is in use, the perimeter is automatically recalculated to maintain the DUCT's shape.

(a)  
![[mu_66afccee_a59f68064e078c1b1a6a.jpg]]

![[mu_66afccee_a700721d18fd5c94af9c.jpg]]

![[mu_66afccee_3e089c9234bf38766a4b.jpg]]

![[mu_66afccee_7a811840d624e69375b2.jpg]]

![[mu_66afccee_9f6d0c00428a13a562cd.jpg]]

(f)  
![[mu_66afccee_a815cf62f32ea63fb1ee.jpg]]

![[mu_66afccee_65184a8281fe4c98e89b.jpg]]

![[mu_66afccee_d1d3b6d77d0e3f86e291.jpg]]

![[mu_66afccee_90602ffd67199d50bd3a.jpg]]

![[mu_66afccee_a02b8e979e0e71a97b3c.jpg]]  
Figure 2.10: Illustration of some master-slave linking. (a) Two lengths can be linked so the total length remains constant when one length is changed. (b), (c), (d) Perimeters can be linked to areas so shapes remain constant when areas are changed. (e) In STKSLAB, porosity can be linked to pore size and solid thickness, to keep the fraction of the stack that's devoted to support structure constant. The plane of this illustration is perpendicular to x. (f) In STKCIRC and TX, porosity can be linked to hole radius, to keep the number of holes constant. The plane of this illustration is perpendicular to x. (g), (h) In segments with impedances, the imaginary part can be linked to the real part so either phase or magnitude remains constant when the real part is changed. (i) In STKDUCT, maintain shape and volume when length is changed. (j) In CoNE, adjust length to maintain taper angle when areas are changed.

Adjust length in segment n when the length here changes, to keep their sum constant: All segments with length. (In the restart table, this is indicated as $n > 0 . )$ 1

Adjust porosity (i.e., GasA/A) when gas gap or solid thickness changes in STKSLAB, keeping constant area and constant fraction of the area devoted to support ribs. Adjust porosity (i.e., GasA/A) when hole radius or area changes in STKCIRC or TX, keeping constant number of holes. Set porosity (i.e., GasA/A) equal to $a b / ( a + l ) ( b + l )$ in STKRECT. For details, see Section 10.5.1. (In the restart table, this is indicated as -1.)

Adjust perimeter when area changes, to maintain shape: DUCT and STKDUCT. Adjust initial perimeter when initial area changes, to maintain initial end's shape: CONE and STKCONE. (In the restart table, this is indicated as -2.)

Adjust final perimeter when final area changes, to maintain shape of final end: CoNE and STKCONE. (In the restart table, this is indicated as -3.)

Adjust length and both perimeters, to maintain end shapes and taper angle: CoNE and STKCONE. (In the restart table, this is indicated as -4.)

Adjust surface area when volume changes, to maintain shape: COMPLIANCE. (In the restart table, this is indicated as -5.)

Adjust area and perimeter when length changes, to maintain constant volume and crosssectional shape: STKDUCT. (In the restart table, this is indicated as -6.)

Adjust imaginary part when real part changes, to maintain constant magnitude (when possible): IMPEDANCE, BRANCH, and TBRANCH. (In the restart table, this is indicated as -7.)

Adjust imaginary part when real part changes, to maintain constant phase angle: IMPEDANCE, BRANCH, and TBRANCH. (In the restart table, this is indicated as —8.)

Adjust initial and final perimeters in CONE and STKCONE as initial and final areas change, maintaining the shapes on both ends. (In the restart table, this is indicated as -9.)

Master-slave links can be tracked by status fields in the center of the <. out> file, between the input and output columns. The master parameter—the one through which the mode is controlled—is labeled Mstr. The slave parameter, i.e., the one that cannot be modified independently when it is controlled by a link, has a status indicator of the form nnp to indicate its master's address (e.g., 2a).

Newly inserted DUCT and CONE segments automatically initialize with their perimeters linked to their areas on the basis of a circular shape, with a radius of 1 meter.

With each of the <bottle> model's perimeters slaved to its local area, and adjacent areas that must be identical connected by sameas, the <bottle> model looks like this:

```csv
2±O BEGIN Initial
12日 1 DUCT the neck
13 2.1410E-04 a Area m^2 Mstr 12.044 A |pl Pa
14 5.1870E-02 b Perim m 1a -87.986 B Ph(p) deg
15 1.7780E-02 c Length m 9.9797E-05 C |U| m^3/s
16 Master-Slave Links -9.4266E-03 D Ph(U) deg
17 Optional Parameters 3.3197E-05 E Htot W
18 ideal Solid type 2.1219E-05 F Edot W
19 E 2 CONE Transition from neck to volume
20 21 22 23 24 25 Same 1a 2.1410E-04 a AreaI m^2 33.945 A |pl Pa
Same 1b 5.1870E-02 b PerimI m -89.794 B Ph(p) deg
0.1003 c Length m 7.5895E-05 C |U| m^3/s
Same 3a 1.8680E-03 d ÀreaF m^2 -3.4905E-02 D Ph(U) deg
Same 3b 0.1532 e PerimF m 3.3197E-05 E Htot W
Master-Slave Links 5.4209E-06 F Edot W BEGIN
26 27 Optional Parameters
ideal Solid type DUCT
29 29 30 31 E 3 DUCT Bottle volume
1.8680E-03 a Area m^2 Mstr 37.703 A |pl Pa CONE
0.1532 b Perim m 3a -89.859 B Ph(p) deg
0.1270 c Length m 2.3620E-08 C |U| m^3/s
32 Master-Slave Links -89.859 D Ph(U) deg
3 34 Optional Parameters 3.3197E-05 E Htot W DUCT
ideal Solid type 4.4527E-07 F Edot W
35 4 SURFACE Bottom End SURFACE
36 Same 3a 1.8680E-03 a Àrea m^2 37.703 A |pl Pa HARDEND
37 -89.859 B Ph(p) dea
```

so it is apparent that the bottle has only five independent geometrical dimensions—neck area, bulb area, and the lengths of the neck, cone, and bulb—whose independence is indicated by their blue color. All other dimensions depend on those five. The user who is interested in studying the resonance frequency as a function of geometry can now change those five dimensions at will, confident that self-consistent geometry will be maintained by the master-slave and sameas links.

![[mu_66afccee_30d3ec8aeaef88bdc6e8.jpg]]  
Figure 2.11: (a) The schematic display of the <bottle> model. Dimensions are to scale, assuming that areas are circular. Right-clicking on any segment brings up a menu of options, similar to right-clicking on a segment in the main model display. (b) Some phasor diagrams added to the schematic.

## 2.7.3 Schematic view

A schematic view of the geometry of a DELTAEC model can be turned on by clicking on "view schematic" in the Display pulldown menu. As an example, the schematic of the <bottle> model is shown in Fig. 2.11. The schematic is to scale: Dimensions in the x direction are proportional to the lengths of segments with length, and dimensions perpendicular to x are proportional to $\sqrt { 4 A / \pi }$ in segments having area and length. A glance at this display can help you catch order-of-magnitude typographical errors in a model and keep track of the topology of large models. Left click and drag up to zoom in for a closer view, and right click to bring up a menu of segment operations similar to the right-click segment menu in the main model.

When both a schematic view and a state plot are active, phasor information from the state plot can be displayed on the schematic, based on the position of the mouse cursor within the schematic. Click Alt when the cursor is over the desired position in a highlighted physical segment in the schematic, to create a small phasor plot showing both $p _ { 1 }$ and $U _ { 1 }$ at that position. The magnitude of each phasor is scaled by the maximum magnitude found in the model. The colors are the same as the default colors in the state plot: black for $p _ { 1 }$ blue for $U _ { 1 }$ . Drag the phasor circle or its anchor point with the mouse to reposition them. In integrable segments like DUCTs, Nint unique x locations are available; nonintegrable segments like COMPLIANCE have only one location.

To delete a phasor circle, move the mouse over the anchor point and press the Alt or Delete key. To delete all phasor circles, close and reopen the schematic window.

## 2.7.4 Highlights display

DELTAEC models often have many dozens of segments. The user is usually not interested in examining every numerical result after every run—typically, we examine the guesses (and perhaps targets) to ensure that DELTAEC has not gotten completely lost, and we examine a small number of other results of particular interest. The highlights display shows a compact, user-customized list of such variables of particular interest, which is updated after every run.

Any input variable can be added to the highlight list, by double clicking or right clicking. Output variables can be added by double clicking

Returning to the bottle as an example, we might be particularly interested in the pressure amplitude at the mouth of the bottle and at the bottom of the bottle, and the resonance frequency, as we explore different dimensions of the neck by modifying its area and/or length and running. A convenient setup for such an investigation looks something like the figure below, just after lengthening the neck and running. In ordinary use, we would type ‘m' to modify one or more parameters, then 'r' to run, examine the results, and repeat.

![[mu_66afccee_42e06a792cb1ea7fe0dc.jpg]]

## 2.7.5 Structured branches, loops, and networks

Although BRANCH and OPNBRANCH can be useful, they are often inadequate for describing the variations in branch impedance with operating conditions. For example, the branch might be a Helmholtz resonator whose impedance changes significantly with frequency. Further, BRANCH and OPNBRANCH are wholly inadequate when networks include reconnecting topology, as in Fig. 1.3. The TBRANCH and UNION segments overcome these inadequacies.

![[mu_66afccee_b92d365dfc6c52a98b79.jpg]]  
Figure 2.12: TBRANCH allows DELTAEC to integrate in branched geometries like this.

When it encounters a TBRANCH, DELTAEC treats subsequent segments as the sequential members of the branch, integrating until it reaches a HARDEND or SOFTEND. It then "returns to the trunk," treating further segments as trunk members. The logic of this is shown in Fig. 2.12. At the TBRANCH, the branch impedance determines how the (complex) volume flow rate splits up. Usually we use the branch impedance as a pair of guesses that DELTAEC adjusts in its usual way to hit two targets elsewhere. TBRANCHed models tend to have many guesses and targets, since every \*\*END contributes two targets (and a few more targets are almost always needed for temperatures and other variables). Of course, branches can have sub-branches of their own.

Networks with loops, like Fig. 1.3, can also be handled by DELTAEC, through use of TBRANCH and UNION. The UNION segment is used to tell DELTAEC to "connect" a TBRANCH's SOFTEND back to the trunk at the location of the UNION segment. The branch's SOFTEND potential targets are not used. However, at least two input variables (b and c) of the UNION segment should always be used as targets. As DELTAEC processes the UNION segment, it assigns the current values of the complex pressure at the SOFTEND referenced by the number in parameter a of the UNION segment to inputs b and c of the UNION. These values are compared to the local complex pressure result, at this UNION, in the trunk, and DELTAEC's shooting-method iteration should run until their difference is zero. This assures that the end of the branch and the trunk share the same complex $p _ { 1 }$ where they meet at the UNION. As before, a guessed branch impedance usually determines how the (complex) volume flow rate splits up at the TBRANCH. Volume flow rates are summed at the UNION. (Note that the UNION targets are somewhat different from HARDEND targets discussed above, because "target" numerical values in UNION are not specified by the user—they vary from run to run, depending on what is happening at the associated sOFTEND.)

Figure 2.13 and the DELTAEC models below show three ways to use TBRANCH and UNION to model a parallel LRC network. The reader is encouraged to invent one or more additional ways to model this network, and try them. Here is the DELTAEC model corresponding to Fig. 2.13(b):

![[mu_66afccee_0e32d8735da81b326fff.jpg]]  
Figure 2.13: A driven, parallel LRC network. (a) Schematic. (b) One way to model the LRC network in DELTAEC, with the L and C in the TBRANCH and the R in the trunk, rejoined at the UNION, whose downstream end must be sealed by a targeted HARDEND. (c) Another way to model the LRC, with the L in the TBRANCH and the R in the trunk, rejoined at the UNION, whose downstream end feeds the C, whose exit must be sealed by a targeted HARDEND. (d) A third way, with the L, R, and C all in the TBRANCH. Returning to the trunk, DELTAEC encounters no segment before the UNION, so the UNION effectively connects the initial and final ends of the branch to each other. The UNION's exit must be sealed by a targeted HARDEND.

```csv
TITLE Example LRC1
! lrc1.out
!Created@19:30:01 9-Jul-06 with DeltaE Vers. 5.5b6 for the IBM/PC-Compatible
0
BEGIN Initialize things
1.0000E+05 a Mean P Pa 6.1460E-03 A IUI G( Of) P
60.000 b Freq Hz 80.940 B Ph(U) G( 0g) P
300.00 c TBeg K 3.7260E+05 C Re(Zb) G( 1a) P
2000.0 d lpi Pa -2.7012E+05 D Im(Zb) G( 1b) P
0.0000 e Ph(p) deg
6.1460E-03 f |U| m^3/s G
80.940 g Ph(U) deg G
air Gas type
1
TBRANCH the split
3.7260E+05 a Re(Zb) Pa-s/m^3 G 2000.0 AIpl Pa
-2.7012E+05 b Im(Zb) Pa-s/m^3 G 0.0000 B Ph(p) deg
4.3459E-03 C |U| m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
-2.5508 G EdotTr W
2
IMPEDANCE pure inertance
0.0000a Re(Zs) Pa-s/m^3 2282.4 AIpl Pa
1.0000E+05 b Im(Zs) Pa-s/m^3 -8.8682 B Ph(p) deg
4.3459E-03 C |U| m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
3
COMPLIANCE a compliance tank
4.8360E-02 a SurfAr m^2 Fn( 3b) 2282.4 AIpl Pa
1.0000E-03 b Volume m^3 S= -5 -8.8682 B Ph(p) deg
4.3459E-03 C |UI m^3/s
-54.060 D Ph(U) deg
3.4951 E Hdot W
ideal Solid type 3.4951 F Edot W
4
SOFTEND this will reconnect at the UNION
0.0000 a Re(z) (t) 2282.4 AIpl Pa
0.0000 b Im(z) (t) -8.8682 B Ph(p) deg
```

```csv
4.3459E-03 C |UI m^3/s
-54.060 D Ph(U) deg
3.4951 E Hdot W
3.4951 F Edot W
44.392 G Re(z)
44.690 H Im(z)
5
IMPEDANCE pure resistance
1.0000E+05 a Re(Zs) Pa-s/m^3 2282.4 Alpl Pa
0.0000 b Im(Zs) Pa-s/m^3 -8.8682 B Ph(p) deg
4.3459E-03 C |U| m^3/s
125.94 D Ph(U) deg
-3.4951 E Hdot W
-3.4951 F Edot W
6
UNION close the loop here
4.0000 a SegNum 2282.4 AIpl Pa
2282.4 b IpIEnd Pa = 6A? -8.8682 B Ph(p) deg
-8.8682 c Ph(p)E deg = 6B? 7.0901E-17 C |U| m^3/s
-82.266 D Ph(U) deg
2.3118E-14 E Hdot W
7
HARDEND seal the final end of the resonator
0.0000 a R(1/z) = 7G? 2282.4 AIpl Pa
0.0000 b I(1/z) = 7H? -8.8682 B Ph(p) deg
7.0901E-17 C |UI m^3/s
-82.266 D Ph(U) deg
2.3118E-14 E Hdot W
2.3118E-14 F Edot W
7.4001E-17 G R(1/z)
```

## And here is the DELTAEC model corresponding to Fig. 2.13(c):

```csv
TITLE Example LRC2
lrc2.out
!Created@19:31:13 9-Jul-06 with DeltaE Vers. 5.5b6 for the IBM/PC-Compatible
0
BEGIN Initialize things
1.0000E+05 a Mean P Pa 6.1460E-03 A IUI G( Of) P
60.000 b Freq Hz 80.940 B Ph(U) G( 0g) P
300.00 c TBeg K 3.7260E+05 C Re(Zb) G( 1a) P
2000.0 d lpl Pa -2.7012E+05 D Im(Zb) G( 1b) P
0.0000 e Ph(p) deg
6.1460E-03 f |UI m^3/s G
80.940 g Ph(U) deg G
air Gas type
1
TBRANCH the split
3.7260E+05 a Re(Zb) Pa-s/m^3 G 2000.0 AIpl Pa
-2.7012E+05 b Im(Zb) Pa-s/m^3 G 0.0000 B Ph(p) deg
4.3459E-03 C |U| m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
-2.5508 G EdotTr W
2
IMPEDANCE pure inertance
0.0000 a Re(Zs) Pa-s/m^3 2282.4 AIpl Pa
1.0000E+05 b Im(Zs) Pa-s/m^3 -8.8682 BPh(p) deg
4.3459E-03 C |UI m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
3
SOFTEND this will reconnect at the UNION
0.0000 a Re(z) (t) 2282.4 AIpl Pa
0.0000 b Im(z) (t) -8.8682 B Ph(p) deg
4.3459E-03 C |U| m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
44.690 G Re(z)
4
IMPEDANCE pure resistance
1.0000E+05 a Re(Zs) Pa-s/m^3 2282.4 AIpl Pa
0.0000 b Im(Zs) Pa-s/m^3 -8.8682 B Ph(p) deg
4.3459E-03 C |U| m^3/s
125.94 D Ph(U) deg
-3.4951 E Hdot W
```

```csv
-3.4951 F Edot W
5
UNION close the loop here
3.0000 a SegNum 2282.4 AIpl Pa
2282.4 b IpIEnd Pa = 5A? -8.8682 B Ph(p) deg
-8.8682 c Ph(p)E deg = 5B? 6.1460E-03 C |U| m^3/s
80.940 D Ph(U) deg
2.3429E-02 E Hdot W
2.3429E-02 F Edot W
300.00 G End-T K
6
COMPLIANCE a compliance tank
4.8360E-02 a SurfAr m^2 Fn( 6b) 2282.4 AIpl Pa
1.0000E-03 b Volume m^3 S= -5 -8.8682 BPh(p) deg
2.8686E-14 C |U| m^3/s
119.89 D Ph(U) deg
-2.0495E-11 E Hdot W
ideal Solid type -2.0495E-11 F Edot W
7
HARDEND seal the final end of the resonator
0.0000 a R(1/z) = 7G? 2282.4 AIpl Pa
0.0000 b I(1/z) = 7H? -8.8682 B Ph(p) deg
2.8686E-14 C |U| m^3/s
119.89 D Ph(U) deg
-2.0495E-11 E Hdot W
-2.0495E-11 F Edot W
-6.5606E-14 G R(1/z)
```

And finally, here is the DELTAEC model corresponding to Fig. 2.13(d):

TITLE Example 1: Plane-wave resonator   
lrc3.out   
!Created@19:32:21 9-Jul-06 with DeltaE Vers. 5.5b6 for the IBM/PC-Compatible !Created@19:32:21 9-Jul-06 with DeltaE Vers. 5.5b6 for the IBM/PC-Compatible

```csv
0
BEGIN Initialize things
1.0000E+05 a Mean P Pa 6.1460E-03 A |UI G( Of) P
60.000 b Freq Hz 80.940 B Ph(U) G( 0g) P
300.00 c TBeg K 3.7260E+05 C Re(Zb) G( 1a) P
2000.0 d lpi Pa -2.7012E+05 D Im(Zb) G( 1b) P
0.0000 e Ph(p) deg
6.1460E-03 f |U| m^3/s G
80.940 g Ph(U) deg G
air Gas type
1
TBRANCH the split
3.7260E+05 a Re(Zb) Pa-s/m^3 G 2000.0 AIpl Pa
-2.7012E+05 b Im(Zb) Pa-s/m^3 G 0.0000 B Ph(p) deg
4.3459E-03 C |U| m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
-2.5508 G EdotTr W
2
IMPEDANCE pure inertance
0.0000 a Re(Zs) Pa-s/m^3 2282.4 AIpl Pa
1.0000E+05 b Im(Zs) Pa-s/m^3 -8.8682 B Ph(p) deg
4.3459E-03 C |U| m^3/s
35.940 D Ph(U) deg
3.5185 E Hdot W
3.5185 F Edot W
3
COMPL a compliance tank
4.8360E-02 a SurfAr m^2 Fn( 3b) 2282.4 AIpl Pa
1.0000E-03 b Volume m^3 S= -5 -8.8682 B Ph(p) deg
4.3459E-03 C |U| m^3/s
-54.060 D Ph(U) deg
3.4951 E Hdot W
ideal Solid type 3.4951 F Edot W
!- 4
IMPEDANCE pure resistance
1.0000E+05 a Re(Zs) Pa-s/m^3 2000.0 AIpl Pa
0.0000 b Im(Zs) Pa-s/m^3 -3.4849E-13 B Ph(p) deg
4.3459E-03 C |U| m^3/s
-54.060 D Ph(U) deg
2.5508 E Hdot W
2.5508 F Edot W
5
SOFTEND this will reconnect at the UNION
0.0000 a Re(z) (t) 2000.0 AIpl Pa
```

0.0000 b Im(z) (t) -3.4849E-13 B Ph(p) deg   
4.3459E-03 C |U| m^3/s   
-54.060 D Ph(U) deg   
2.5508 E Hdot W   
2.5508 F Edot W   
32.398 G Re(z)   
6   
UNION close the loop here   
5.0000 a SegNum 2000.0 Alpl Pa   
2000.0 b IpIEnd Pa = 6A? 0.0000 B Ph(p) deg   
-3.4849E-13 c Ph(p)E deg = 6B? 1.3999E-16 C |U| m^3/s   
-73.811 D Ph(U) deg   
3.9031E-14 E Hdot W   
7   
HARDEND seal the final end of the resonator   
0.0000 a R(1/z) = 7G? 2000.0 Alpl Pa   
0.0000 b I(1/z) = 7H? 0.0000 B Ph(p) deg   
1.3999E-16 C |U| m^3/s   
-73.811 D Ph(U) deg   
3.9031E-14 E Hdot W   
3.9031E-14 F Edot W

A topologically similar model of a complicated thermoacoustic system using TBRANCH and UNION is given in the traveling-wave-engine example in Section 6.3. Examples of heirarchically nested structured branches and loops are shown in Figs. 6.9 and 11.1.

## 2.7.6 Manipulating entire segments

An entire segment, or a block of segments, can be copied, cut, pasted, and deleted, much like copying and pasting a paragraph or a contiguous block of paragraphs in a text editor.

Dragging the cursor over a segment indicates its selection via a background color change. After a first segment has been selected, the selection can be extended to a block of segments by further dragging or by holding down the Shift key while either clicking the desired final segment or using the up and down arrow keys. The spacebar unrolls and re-rolls the selected segment(s), just like the “+" and “-" box at the left margin of a segment.

When a segment or segments are selected, right clicking brings up a menu that includes cut/copy/paste the segment(s). DELTAEC retains sameas addresses, RPN addresses, and master-slave links inside the copied block of segments, while replacing any such addresses that point outside the block with appropriate numerical values. Segments and blocks of segments can be moved from one model to another using this feature, if both models are open in the same DELTAEC window.

Whether or not segments are selected, Shift+left-margin click will unroll or re-roll the entire model, and Shift+Ctrl+left-margin click (or, in Macs, Shift+Cmd+left margin click) unrolls or re-rolls all the segments in a leg (i.e., between a TBRANCH and SOFTEND—legs are introduced in Chapter 3).

## 2.7.7 Thermophysical properties

The Tools / thermophysical properties pulldown-menu selection gives the user keyboard access to DELTAEC's library of gas and solid properties for a given mean pressure and temperature. This feature is so convenient that we often start DELTAEC simply to look up the transport properties of air, helium, and other common gases.

RPN segments, introduced in Chapter 4 and described fully in Section 11.4.1, can also be used to access thermophysical properties. These segments can be inserted anywhere in a model where the user wants to know the gas or solid properties at the local temperature and pressure. By using the incremental plot feature described in Section 3.2, tables and graphs of properties can be generated over ranges of temperature and pressure, with $T _ { m }$ and $p _ { m }$ as independent plot variables in a BEGIN segment upstream of such RPN segments.

## 3. More about plotting

DELTAEC's built-in plotter, which is accessible in DELTAEC's Display pulldown menu, provides convenient graphical displays of DELTAEC results.

In state plots, the state of the wave and other thermoacoustic variables such as temperature and energy flux are displayed vs location x in the model whenever a run has converged properly. Data are tabulated in a file with the extension <.sp>.

In incremental plots, the relationships among a number of DELTAEC variables are displayed for a set of many converged runs, as one or two independent variables are automatically incremented between runs. Data are tabulated in a file with the extension <.ip>. Incremental plotting is also used to let DELTAEC automatically accomplish a large change in some variable via a series of many smaller changes, to avoid target-convergence problems, as described in Section 5.4.3

DELTAEC's plotter has many built-in, rudimentary formatting features. Curves can be identified by color, line width, or line type. Default axis labels can be overwritten, and the units on axes can be changed by factors of 10. The view can be changed by zooming, and logarithmic scales can be used. Curves can be examined closely by moving the mouse cursor onto them and reading the horizontal and vertical coordinates. Segment numbers can be displayed on graphs, showing where each segment ends. The graphical results can be exported as <. jpg>, <.bmp>, or other graphics files.

DELTAEC saves the user's most recent plotting and formatting preferences for each <.out> file in auxiliary files with extensions <.ssv.dir>, <.ssv.dat>, <.isv.dir> and <.isv.dat>, for the <.sp> and <.ip> files, respectively. (If the plotter is not working, close DELTAEC, delete the <.ssv.\*> and <.isv.\*> files associated with your model, and try again. This is also recommended when updating from one version of DELTAEC to another.)

## 3.1 State plots

State plots show the current state of the DELTAEC model. DELTAEC's plotter makes state plots from the <.sp> file that is created by DELTAEC after every successful run. If the user modifies a parameter in the model, and re-runs it, DELTAEC quickly updates its plot displays to reflect the new reality, just like it updates its numerical displays. This feature was introduced in Section 2.4, where the <bottle> model awoke with a state plot showing $p _ { 1 }$ and $U _ { 1 }$ vs x, and we changed it to display $\dot { E }$ vS x.

DELTAEC subdivides integrable segments like DUCTs and STK\*\*s into Nint pieces, writing Nint +1 lines of numbers to the <. sp> file for each segment. On the <.sp> plot display, each segment is then represented by Nint short, straight lines connecting those Nint +1 points. The accuracy of the underlying calculation is generally better than what is indicated by the kinkiness of the plot, because the fourth-order Runge-Kutta integration technique [16] essentially simulates the physics on a finer length scale than the <.sp> file actually tabulates.

## 3.1.1 Cloning

The experienced user will soon want to display more than one plot simultaneously. “Cloning" DELTAEC plots lets this occur. Return to <bottle6> of Chapter 2, which awakens displaying $p _ { 1 }$ vs x. Format this curve for visual appeal, and then "clone" it twice from the plotter's File pulldown menu, editing each clone to arrive at something that looks like this layout:

![[mu_66afccee_3780b0fd6b42afbc9047.jpg]]  
All five curves displayed here (on three graphs) are updated every time the model runs successfully, and all our effort of formatting and cloning is saved in the two <.ssv.\*> files if we save when closing the model, so these formatted graphs will reappear if we return to the <bottle6.out> model weeks later.

Sometimes it is useful to include $A _ { \mathrm { g a s } }$ vs x in one or more of the state plots, to have a sort of “drawing" of the apparatus lined up with the data graphs. The SegEndMarks option in the plotter's Options menu puts segment numbers on the graphs, at the end of each segment, as another indication of apparatus locations on the data graphs. The schematic view, available on DELTAEC's Display pulldown menu, also gives a picture of the geometry (see Fig. 2.11 and the Users Guide's title page for examples).

## 3.1.2 Legs

Models with one or more TBRANCHes and/or two or more BEGINs are topologically complicated, so DELTAEC's <. sp> file breaks them down into "legs," with each leg starting over at $x = 0$ for purposes of displaying graphs of data. For example, Fig. 3.2 shows a branched resonator, which we modeled with <legs . out> (available in the <Examples\Plotting> folder). Figure 3.3 shows the standing-wave part of the pressure in that resonator. The side-branch parts of the data form one curve, and the trunk parts of the data form another curve.

Using clone plots and the Legs pulldown menu, the user can show one variable per graph, with all legs plotted in each graph; or can show one leg per graph with all variables of interest plotted in each graph.

## 3.1.3 Phasor plotting options

The complex variables $p _ { 1 }$ and $U _ { 1 }$ are usually of the greatest interest in thermoacoustic systems, so DELTAEC offers several ways of displaying them graphically.

State plots awaken by default with $\mathrm { R e } [ p _ { 1 } ]$ and $\mathrm { I m } [ p _ { 1 } ]$ displayed, and $\mathrm { R e } [ U _ { 1 } ]$ and $\mathrm { I m } [ U _ { 1 } ]$ easily accessible by checking the appropriate boxes at the top of the state-plot display. The real and imaginary parts of the ratio $Z = p _ { 1 } / U _ { 1 }$ and of the lateral spatial average of the oscillating temperature, $\left. T _ { 1 } \right.$ , are also easily accessible. All four of these complex functions can also be displayed in terms of magnitude and phase, through the small pulldown menus assocated with each real or imaginary variable, as illustrated in Fig. 3.4.

In standing-wave systems, the state plots that display variables such as $p _ { 1 }$ and $U _ { 1 }$ as functions of x are usually the most useful. However, for traveling-wave systems, phasor diagrams often offer vital insight, so they are included among DELTAEC's standard stateplot options. To enable a phasor plot, check $\mathrm { R e } [ p _ { 1 } ]$ or $\mathrm { R e } [ U _ { 1 } ]$ instead of $x$ as the “x axis" of the plot, and then use Im $[ p _ { 1 } ]$ or $\mathrm { I m } [ U _ { 1 } ]$ as the “y axis." Alternatively, check "Phasor Mode" in the plotter's Options pulldown menu, to allow both $p _ { 1 }$ and $U _ { 1 }$ phasors on the same graph.

Phasor diagrams are only used for complex variables, here $p _ { 1 }$ and $U _ { 1 }$ . (Other examples include transducer current and voltage, but these are not available in DELTAEC's <.sp> files.) In a phasor diagram, these complex variables are plotted on the complex plane, with the real part plotted along the horizontal axis and the imaginary part plotted along the vertical axis. Conventionally, arrows from the origin point to each such complex value, but these arrows are absent in DELTAEC. One can imagine all of the phasors on a phasor diagram rotating counterclockwise around the origin at radian frequency ω. Then the actual variables represented by the phasors are the time-dependent projections of the phasors on the horizontal axis. Thus a phasor diagram shows the relative magnitudes and time-phase relationships of a number of phasors. The difference between phasors at adjacent places in an apparatus also offers insight into the impedance of what lies between. The difference between pressure phasors is related to the volume flow rate phasor via the momentum equation, which can include resistance and inertance; the difference between volume-flow-rate phasors is related to the pressure phasor via the continuity equation and the compressibility of the intervening gas [13|.

![[mu_66afccee_a56fb1c23ba16809d43b.jpg]]  
Figure 3.1: The bottle, used as an example in both Chapter 2 and the present chapter.

![[mu_66afccee_789ece3fe20e5e679728.jpg]]  
Figure 3.2: A branched resonator. In the model of this resonator, $p _ { 1 }$ and $U _ { 1 }$ have the same phase at BEGIN, and the frequency is a guess. The magnitude of $p _ { 1 }$ in BEGIN is fixed and the magnitude of $U _ { 1 }$ in BEGIN is a guess. Both TBRANCH impedances are guesses, and the four targets in the two HARDENDs are used.

![[mu_66afccee_90286990afb2a18c6132.jpg]]  
Figure 3.3: The standing-wave part of the pressure oscillation in the branched resonator of Fig. 3.2. There are two curves because the resonator has two legs and both legs have been selected in the Legs pulldown menu. The kink in the upper curve occurs at the same pressure as the start of the lower curve, because these are the same location: the TBRANCH.

![[mu_66afccee_ca439c206ef2f7f32b96.jpg]]  
Figure 3.4: A traveling wave with $| p _ { 1 } |$ nearly constant at 100 Pa and the phase of $p _ { 1 }$ starting at zero and going down by $3 6 0 ^ { \circ }$ , resetting from $- 1 8 0 ^ { \circ }$ to $+ 1 8 0 ^ { \circ }$ near $x = 5 \mathrm { ~ m ~ }$ . The little menus to convert the real and imaginary parts of $p _ { 1 }$ to the magnitude and phase are indicated here by the red boxes. Similar features are available for $U _ { 1 }$ and Z.

Figure 3.5 shows the $U _ { 1 }$ phasors for the bottle.

Another way to look at phasors, based on mouse cursor position in the schematic view, is described in Section 2.7.3.

## 3.2 Incremental plotting

DELTAEC allows for incremental "plotting" by automatically incrementing (or decrementing) an independent variable (or two independent variables) and running repeatedly. This can be used either to keep DELTAEC's shooting method happily well-targeted while changing a single independent variable by many small, “safe" steps when a single leap to a desired new value would fail to meet targets (see Section 5.4.3),1 or to tabulate the changing independent variable(s) together with one or more changing output variables in a file named <.ip>. Users can then manipulate and/or plot the <.ip> file with DELTAEC's built-in plotter (or with their favorite graphics or spreadsheet software). We illustrate these features by continuing two previous examples.

![[mu_66afccee_ade44463fb1d12eee669.jpg]]  
Figure 3.5: The phasor plot displays complex $p _ { 1 }$ and/or $U _ { 1 }$ on the real-imaginary plane. With SegEndMarks selected in the Options pulldown menu, segment numbers are displayed at the end of each segment.

## 3.2.1 One-dimensional incremental plots

A driven, parallel LRC network was used as an example of structured branches and unions in Section 2.7.5. Here, we use the same example to illustrate a simple incremental plot in DELTAEC. The system is illustrated in the figure below, and the file we start with is <lrc1.out> from the <Examples\Acoustics> folder. Open that file, and save it as <lrc1b.out> so subsequent changes don't affect the original. Review the model, to understand that this LRC network is driven at 60 Hz and 2 kPa. Under these circumstances, the pressure amplitude in the COMPLIANCE is 2.28 kPa—higher than at the driver.

![[mu_66afccee_bfb188caeb3f37fa0454.jpg]]

Let's see how the pressure amplitude in the COMPLIANCE depends on frequency, using an incremental plot. Unroll the BEGIN segment, double click on the frequency, and check the Plot box. Let the frequency incrementing start from 40 Hz, end at 800 Hz, and do so in 77 steps so the increments are 10 Hz. Now unroll the COMPLIANCE segment, double click on output A—the pressure amplitude—and select it as a dependent plot variable. Note that 0b and 3A are flagged in the main display as plot variables now. Open the Incremental Plot Summary from the Tools pulldown menu, and see what information is presented. (Note that. in addition to our selection of 3A, all four guesses are listed as dependent plot variables—to let the user return to any incrementally plotted point easily, as described in Section 3.2.3.)

Plot summary:lrc1b.out -0   
Independent: Dependent:   
Outer: Inner:   
addr desc unit addr desc unit addr desc val unit   
0b Freq Hz of |U| 0.006145961 m^3/s   
Start: 40.0 0g Ph(U) 80.94040607 deg   
End: 800.0 1a Re (Zb) 372598.0874 Pa-s/m^3   
Step: 10.0 1b Im (Zb) -270116.690 Pa-s/m^3   
Points: 76 3A Ipl 0.0 Pa   
Close Refresh

Now start the repetitive run. DELTAEC begins at the initial value of the frequency, 40 Hz, and performs an ordinary run, adjusting the guesses until the targets are met. It writes a line to the incremental-plot file <lrc1b. ip>, recording on one line the independent variable (f), the guesses, and the chosen dependent variables (|p1| in the COMPLIANCE in the present case). Then DELTAEC increments the independent variable by its step (10 Hz in this case), performs another ordinary run, and records the results on the next line in the <.ip> file..repeating until the final value of the independent variable is reached. In a text editor, the <.ip> file shows this:

BEGIN:Freq BEGIN:|U| BEGIN:Ph(U) TBRAN:Re(Zb TBRAN:Im(Zb COMPL:lpl   
Hz m^3/s deg Pa-s/m^3 Pa-s/m^3 Pa   
Ob OA OB OC OD 3A   
40.00 3.9237E-03 84.11 5.5931E+05-4.5475E+05 2186.   
50.00 5.0127E-03 82.56 4.4726E+05-3.4400E+05 2234.   
60.00 6.1460E-03 80.94 3.7260E+05-2.7012E+05 2282.

and opening <lrc1b.ip>, and choosing to plot 3A vs 0b, displays this:

![[mu_66afccee_a3b612dc87a65a13a3bf.jpg]]

The pressure amplitude starts at 2 kPa at low frequency, and rises with frequency at first, peaking near 200 Hz. Could it be a resonance? The user could now change a parameter such as the resistance in segment 5, repeat the repetitive run, and examine the effects of such a change on the resonance frequency and quality factor. (Don't forget that a frequencyindependent Im $[ Z _ { s } ]$ in segment 2 is not the same as a frequency-independent inertance!)

## 3.2.2 Two-dimensional incremental plots

We use the bottle example from Chapter 2 again, starting from <bottle6.out> in the <Examples\Acoustics> folder. Make the guess-target summary look like this:

Guess-Target Summary:   
GUESS Of 0g   
name BEGIN:|U| BEGIN:Ph(U)   
value 1.00E-04 90.   
units m^3/s deg   
TARGET 5a 5b   
name HARDEND :R(1/z HARDEND :I(1/z   
value .00 .00

Now display the Incremental Plot Summary:

Dependent Variables (outputs):   
PLOTS Of 0g   
name BEGIN:|U| BEGIN:Ph(U)   
units m^3/s deg

Keep these parameters as two of the dependent variables to be plotted (they are copies of the guesses).

We will watch these variables as functions of two independent variables: frequency f and mean temperature $T _ { m }$ . To set up these two independent variables to be incremented, modify each of them, checking the Plot box in the Parameter Edit dialog and then entering initial and final values, and the number of steps. Use only three values of mean temperature in the “outer" loop—300, 400, and 500 K—by letting $T _ { m }$ go from 300 to 500 K in three steps of 100 K, and let f go from 100 Hz to 1200 Hz in 551 steps to get exactly 2-Hz increments in the “inner" loop. Also add the pressure in the bottom of the bottle, 5A, as another dependent plot variable, by double clicking on it and selecting it for plotting. After these actions, check the Incremental Plot Summary again:

```yaml
Outer: Inner: Dependent:
addr desc unit addr desc unit addr desc unit
0c TBeg K Ob Freq Hz Of |U| m^3/s
Start: 300.0 Start: 100.0 0g Ph(U) deg
End: 500.0 End:1200.0 5A lpl Pa
Step: 100.0 Step: 2.0
Points: 3 Points: 551
```

Now start a repetitive run. DELTAEC steps through the frequency and mean temperature, taking several seconds. For each value of frequency and mean temperature, it adjusts guesses until targets are met, and then writes one line to the <. ip> file, recording the values of the independent and dependent plot variables, including all guesses. When it has finished, use the pc's operating system to find the new file, <bottle6.ip>:

BEGIN:TBeg BEGIN:Freq BEGIN:|U| BEGIN:Ph(U) HARDEN:|p|   
K Hz m^3/s deg Pa   
0c Ob Of 0g 5A   
300.000 100.000 2.0250E-06-8.8471E+04 1.38690   
300.000 102.000 2.0953E-06 -8.8471E+04 1.40830

![[mu_66afccee_ee4dcf88d5172cff421a.jpg]]  
Figure 3.6: Pressure amplitude at the bottom of the bottle as a function of drive frequency, with the pressure amplitude at the mouth held constant at 1 Pa, for three different temperatures.

```csv
300.000 104.000 2.1682E-06 -8.8471E+04 1.43090
500.000 1198.00 1.6259E-07-8.8481E+04 0.61493
500.000 1200.00 1.7641E-07-8.8480E+04 0.62388
```

The results are displayed by DELTAEC's plotter as shown in Fig. 3.6. The plotter's pulldown menu must be used to get all three curves to show on the plot.

## 3.2.3 Rewinding incremental plots

The rewind feature takes DELTAEC quickly back to a user-selected, previously calculated state that has been saved in the <.ip> file. This is useful for:

Selecting a new operating point after using incremental plotting to explore a broad range of behaviors. For example, the user could select a point at the top of one of the peaks in Fig. 3.6.

Selecting a recent well-converged operating point from an incremental plot that contains both converged and unconverged operating points and/or from a long incremental plot that seemed to go awry and was canceled by the user.

The rewind feature is available whenever an <.ip> file exists. It is accessible in the Tools pulldown menu or through a button on the toolbar near the top of the main display. When a point is selected, DELTAEC restores the independent plot variable(s) and the values of guesses at that point. It also restores any output parameters that it has in the <.ip> file, which it might have selected in addition to the users choices because it caught the user inadvertently or boldly using a sameas or RPN pointer to an output parameter in a segment downstream of that sameas or RPN, despite DELTAEC's "Forward Reference Condition" warning about the unstable shooting-method behavior that can result from using such downstream results. (See Section 5.4 for an example.)

## 3.2.4 Incremental plots when more than one model is run

Two or more models can be open in DELTAEC at the same time. If these models are run separately, any incremental plots in any of those models will run separately, just as if they were open in separate DELTAEC windows.

Linking two or more models together in a single DELTAEC window and running them together with Run All is described in Section 4.9. The interaction between incremental plots and multi-model running is described near the end of that section.

Rewinding from an incremental plot of inter-linked models behaves similarly to a singlemodel plot rewinding as described above in Section 3.2.3.

## 4. RPN math

## 4.1 Summary

The RPN segment lets the user create nonstandard guesses, targets, and simple algebraic calculations anywhere in a DELTAEC model. The format of the segment is shown in this example:

10   
! The result(s) of the second line's calculations show up as output(s) in the right column.   
RPN Dimensionless magnitude of specific acoustic impedance   
0.000 a 7.8540E-05 A Znorm   
p1 U1 / mag 9a \* rho / a /

Input $^ { 6 6 } \mathrm { a } ^ { \prime \prime }$ is a real number, which can be a guess, a target, and/or a number used subsequently in calculations via sameas links that point to it. The second line (line “b") is a formula expressing a user-defined algebraic procedure in Reverse Polish Notation (RPN), a parenthesis-free algebra encoding technique. Variables such as density rho are re-evaluated at this RPN segment's location in the model (using, for example, $T _ { m }$ at this location) during each numerical integration through the model.

A complete lesson in Reverse Polish Notation (also called postfix) can be found in instruction manuals for most HP (Hewlett-Packard) pocket calculators and on many websites, including Refs. [17] and [18]. DELTAEC users who are unfamiliar with RPN notation are encouraged to consult such a resource. Briefly, as numbers (including pointers to numbers elsewhere in the model, and including variables introduced below) are encountered in the instruction line, these numbers are pushed down onto a stack. Any numbers already present on the stack are pushed deeper into the stack. When a unary operator such as cos, log, or sqrt is encountered in the formula, it takes a single number off the stack ("pops" it), acts on it, and pushes the result back onto the stack. When a binary operator such as + or \* is encountered, it pops two numbers off the stack, combines them appropriately, and pushes the result back onto the stack. Other numbers that may be on the stack but are not involved in the current operation simply move up and down during the operation so no gaps appear in the stack and no uninvolved numbers get lost. (Some of us find it helpful to visualize a spring-loaded stack of dishes at a cafeteria, which adjusts itself so the top dish is always at the most convenient height no matter how many dishes are hidden underneath it.)

After a simple formula has been processed, there may be only one number remaining on the stack; if so, this number is the “result" of the RPN segment and is displayed as a single output, “A." However, it is often desirable to leave additional results on the stack to be accessed elsewhere or viewed by the user. Whatever is left on the stack after the instruction line has been processed is displayed as outputs A, B, C,... For example, if the instruction line is $^ { \cdot \cdot } 1 \ 2 \ 3 \ 4 + 4 5 \ \cos ^ { 3 }$ , the segment's output values will be $\mathtt { A } = 0 . 7 0 7 1 , \mathtt { B } = 7 , \mathtt { C } = 2 , \mathtt { D } = 1$ To assist in human readability, DELTAEC recognizes the semicolon as a punctuation mark that the user can insert anywhere without affecting the calculation. Thus, the instruction line given above could also be written “1 ; 2 ; 3 4 + ; 45 cos". (Note that blanks must both precede and follow the semicolon.) Three shades of colored highlighting in the main display of RPN segments also help human readability.

As a further aid to human readability, clicking on an output parameter in an RPN segment and then clicking on "List Linkages" brings up a display showing how that parameter is calculated, among other things. There, an RPN calculation can be displayed with parentheses if desired. For example, outputs A and B in the last paragraph can be displayed as cos(45) and 3+4, respectively.

DELTAEC's RPN segment recognizes the common trigonometric, logarithmic, exponential, and algebraic functions present on most pocket calculators, as well as hyperbolic and Bessel functions that are not available on most calculators. Most of these functions accept complex arguments. Other functions convert between complex numbers and real numbers in the usual ways (e.g., real, imaginary, magnitude, phase). For complete lists and short descriptions of DELTAEC's RPN operations, see the tables in Section 11.4.1.

Whenever the command string of an RPN is being modified, clicking the ShowOps button displays a reminder of available operations and variables similar to the following:

Valid RPN commands listed below.   
(It is OK to type lower case, except Bessel functions.)   
Basic: + \* 1 inv   
log 1og10 exp tenx sqrt sqrd abs   
Trig: cos acos sin asin tan atan atanr pi   
cosr acosr sinr asinr tanr atan2 atan2r   
sinh cosh tanh   
Bessel: JO J1 YO Y1   
RPN stack: # 1stx a<>b sto rcl min max avg inp   
Complex: mag real imag arg argr conj i cmplx cmplxr   
Gas: gamma a rho cp k mu beta enth dk dn m   
Mixture: nL kT D12 mL mH NLdot nLzero   
Solid: rhos CS ks ds   
State: Tm W f pm p1 U1 <T1>   
Thermodyn: Edot Htot H2k Xdot Tzero   
Mean flow: Ndot p20DEC p20tot   
Cumulative: F1 vol x   
Change: =Tm =p1 =U1 =H2k =Ndot =NLdot   
=pm =f =nL =F1 =vol =p20DE   
=Tzero =nLzro

Clicking on one of these reminders will save the user a little typing.

Where capital letters appear in the preferred spelling of an RPN operation, DELTAEC will usually accept lower-case typing.

The rest of this chapter introduces many ways that RPN segments can be used.

## 4.2 Non-standard results

The RPN segment is often used to display interesting results for the user.

For example, to calculate and display the gas displacement amplitude

$$
| \xi _ { 1 } | = \frac { | U _ { 1 } | } { \omega A }\tag{4.1}
$$

at the end of, for example, a DUCT at segment 5, an RPN after segment 5 could be written

RPN magU1 over omega A (units: meters)   
0.00   
5C 2 / pi / 0b / 5a /

The "List Linkages, Show with parentheses" display shows this as $\{ [ ( \mathrm { 5 C / 2 } ) / \mathrm { p i } ] / 0 \mathrm { b } \} / \mathrm { 5 a } /$ The $\ " 0 . 0 0 \ "$ in line a is not used in this example. 5C points to $| U _ { 1 } |$ in segment 5, 0b points to the frequency in segment 0, and 5a points to the duct area in segment 5. Alternative ways to arrive at the same result in DELTAEC RPN formulas include

5C 2 pi \* 0b \* 5a \* /   
or   
5C 2 pi 0b 5a \* \* \* /   
or   
U1 mag w / 5a /

These examples show how DELTAEC recognizes numbers $\left( \mathrm { e . g . , ~ } ^ { \ast } 2 ^ { \mathfrak { 3 } } \right)$ , pointers to input and output numbers $( \mathrm { e . g . , \ ^ { \ast } 0 b ^ { \prime } } )$ and $ { \mathrm { \Sigma } } ^ { \prime \prime }  { \mathrm { 5 C } } ^ { \prime \prime } )$ , special constants (here “pi"), and local complex and real variables (here $U _ { 1 }$ and ω).

As a second example, the user could display the local values of several thermophysical properties of the gas, namely $\rho _ { m } , c _ { p } , a _ { ; }$ and $\mu ,$ by inserting this RPN segment into a model: RPN A=rho, B=cp, C=sound speed, D=viscosity (MKS units) 0.00

DELTAEC can perform complex arithmetic in RPNs. For example, it can calculate

$$
f _ { k } = \frac { \operatorname { t a n h } \left[ \left( 1 + i \right) y _ { 0 } / \delta _ { \kappa } \right] } { \left( 1 + i \right) y _ { 0 } / \delta _ { \kappa } }\tag{4.2}
$$

for a parallel-plate geometry [e.g., see the first of Eqs. (10.111)]. We let the input parameter, line “a", be equal to the plate half-spacing yo so we can change it easily later:

RPN Thermal function for parallel plate geom. "a"=y0 (meters)   
2.0000E-04 a (t) ( 0.9244,-0.2392) A   
(1,1) inp \* dk / tanh lstx /

Here (1,1) illustrates the entry of a complex constant, (1 + i). This complex constant could just as well have been made by entering 1 i + . The input variable of the segment, line a, is referenced via inp in the RPN command string, and the thermal penetration depth $\delta _ { \kappa }$ is accessed via dk. The "List Linkages, Show with parentheses" display shows this result as tanh $( [ ( 1 , 1 ) ^ { * } 2 \mathrm { a } ] / \mathrm { d } \mathrm { k } ) / \{ [ ( 1 , 1 ) ^ { * } 2 \mathrm { a } ] / \mathrm { d } \mathrm { k } \}$

For complicated algebra that won't fit in one RPN, the user can cascade two or more RPNs, each relying on the output(s) of the previous one(s).

It can be dangerous to link the master of a master-slave set to the result of an RPN segment through a sameas link. Such an arrangement works fine until the model is saved to the disk and later re-opened by DELTAEC. While opening such a model, DELTAEC calculates the constant associated with the master-slave link during file parsing, before the model is run and thus before the numerical value of the master is calculated with Fortran double-precision accuracy. Thus, the constant might be set inaccurately. If the <.out> file has been modified in a text editor, values of the output parameters read from the disk, which are usually irrelevant to subsequent model behavior, can affect such master-slave linkages severely.

## 4.3 List Linkages

When cascaded RPNs also involve parameters that are slaved to, or sameas, other parameters, and input parameters in other, non-RPN segments are sameas to the RPN results, the dependencies can become very complicated. The List Linkages display, available in the modify-parameter dialog for both input and output variables (with RPN parameter b being the only exception—click on the associated output variable(s) instead) can be very useful for avoiding mistakes, diagnosing infinite loops of pointers, diagnosing Forward Reference Conditions, etc. At Los Alamos, we often find ourselves with complicated situations, illustrated with this example for the Linkages List from variable 8A, segment 8 being an RPN:

8A k(m-1) is an RPN result, calculated by 8b, via   
the formula (sqrt[{1+[(gamma-1)\*7B]}/(1-7A)]\*w/a,   
which needs 7B and 7A.   
7A fnu is an RPN result, calculated by 7b, via   
the formula ({[(1-i)\*8a]\*dn}/2)/7a,   
which needs 8a and 7a.   
7B fkappa is an RPN result, calculated by 7b, via   
the formula ({[(1-i)\*8a]\*dk}/2)/7a,   
which needs 8a and 7a.   
8a G\_or\_T does not need other parameters.   
7a G\_or\_T does not need other parameters.   
9A needs 8A via RPN calc.   
9B needs 8A via RPN calc.   
9C needs 8A via RPN calc.   
10a needs 9A via sameas.   
10b needs 9B via sameas.

If you were planning to delete this segment, the final lines in the List Linkages display would inform you to look first at segments 9 and 10 for unintended consequences, and it would suggest that you could investigate whether any other segments need segment 7, which might then become another candidate for deletion.

## 4.4 Non-standard inputs

Line a of an RPN segment can be used as an input variable that is unavailable in any other segment. This is convenient for a variable that the user wants to manipulate in non-MKS units, a variable that is frequently changed by the user, or a variable that is changed by DELTAEC as a guess or an independent incremental-plot variable .

For example, suppose that a user is concerned with the volume of a cylindrical resonator, and wants to find out what shape of cylinder requires the lowest drive power for a given pressure amplitude. The user also prefers to work with the resonator's diameter instead of its area.

TITLE Example 1: Plane-wave resonator   
!Created@13:21:32 8-Jul-06 with DeltaE Vers. 5.5b6 for the IBM/PC-Compatible   
!– 0   
BEGIN Initialize things   
1.0000E+05 a Mean P Pa 7903.3 A Freq G( 0b) P   
7903.3 b Freq Hz G 3.9873E-05 B |UI G( Of) P   
300.00 c TBeg K   
1000.0 d lpl Pa   
0.0000 e Ph(p) deg   
3.9873E-05 f |U| m^3/s G   
0.0000 gPh(U) deg   
helium Gas type   
!- 1   
RPN a=diam (cm), A=cross-sectional area (square meters)   
1.0000 a G or T (t) 7.8540E-05 A Area   
3.1372E-02 B Perim   
inp 100 / sto pi \* rcl sqrd pi \* 4 /   
!-- 2 -   
RPN a=volume (cubic cm). A=length (meters)   
10.000 a G or T (t) 0.1273 A length   
inp 1E6 / 1A /   
1- 3   
SURFACE top end cap of resonator (imagine it's a moving driver)   
sameas 1A a Area m^2 1000.0 Alpl Pa   
0.0000 B Ph(p) deg   
3.9203E-05 C |UI m^3/s   
0.0000 D Ph(U) deg   
1.9602E-02 E Hdot W   
ideal Solid type 1.9602E-02 F Edot W   
!- 4   
DUCT the most important piece of this resonator   
sameas 1A a Area m^2 996.65 AIpl Pa   
sameas 1B b Perim m 5.8368E-04 B Ph(p) deg   
sameas 2A c Length m 6.6737E-07 C |U| m^3/s   
5.8368E-04 D Ph(U) deg   
3.3257E-04 E Hdot W   
ideal Solid type 3.3257E-04 F Edot W   
5   
SURFACE End of the pipe   
sameas 1A a Area m^2 996.65 Alpl Pa   
5.8368E-04 B Ph(p) deg   
2.2261E-19 C |U| m^3/s   
-104.32 D Ph(U) deg   
-2.7438E-17 E Hdot W   
ideal Solid type -2.7438E-17 F Edot W   
!- 6   
HARDEND seal the final end of the resonator   
0.0000 a R(1/z) = 6G? 996.65 AIpl Pa   
0.0000 b I(1/z) = 6H? 5.8368E-04 B Ph(p) deg   
2.2261E-19 C |U| m^3/s   
-104.32 D Ph(U) deg   
-2.7438E-17 E Hdot W   
-2.7438E-17 F Edot W   
-1.1503E-16 G R(1/z)   
-4.5062E-16 H I(1/z)

![[mu_66afccee_225faa3b8b007a976897.jpg]]

With this file, the user can modify the diameter (in cm) and the volume (in cm3³) conveniently in 1a and 2a, and could use those as independent plot variables or as guesses. RPN instruction 1b calculates the area $( \mathrm { i n ~ m ^ { 2 } } )$ and puts it in output 1A for use in segments 3, 4, and 5. RPN instruction 2b calculates the length from the given diameter and volume, putting it in output 2A for use in segment 4.

Note that segments 3, 4, and 5 show how sameas can point to DELTAEC outputs (capital letters) as well as inputs (small letters).

## 4.5 Non-standard targets

DELTAEC has a few specially assigned input parameters that hold target values in segment types that have outputs very commonly used in targets. Some of these were introduced in Chapter 2: the complex normalized impedances $z _ { n }$ in HARDEND and SOFTEND, and the complex pressure $p _ { 1 }$ in UNION. Other routine, built-in targets are the solid temperatures in heat exchangers, which will be introduced in Chapter 5. DELTAEC knows which output variables in these segments should be associated with their "default" target values when the shooting-method algorithm is using them.

The experienced user will soon hunger for more possibilities. An application may call for specifying piston stroke, acoustic power, or pressure or velocity (magnitude or phase) somewhere other than BEGIN. The RPN segment is used to establish such variables as targets The first of the RPN outputs, $^ { \langle \ell } \mathsf { A } , ^ { \prime \rangle }$ is recognized by DELTAEC as paired with the RPN input $\ " { \sf a } ^ { \prime \prime }$ to comprise a potential target/result.

For example, the stroke of a linear motor is often limited by the flexure characteristics of its suspension. Here is an example using the RPN segment to find out how much current must be delivered to a motor to keep the motor's stroke targeted at 2 mm while driving a resonator. The usual HARDEND targets are also used, with complex $U _ { 1 }$ in BEGIN being the corresponding guesses. The RPN segment's input, 2a, which is set by the user at 2.000, is the user's desired target, and the RPN formula yields the motor stroke, which is written in 2A. DELTAEC has adjusted guess 1h, the motor current, until the motor stroke met its target.

TITLE Example 1: Plane-wave resonator   
!Created@14:22:59 8-Jul-06 with DeltaE Vers. 5.5b6 for the IBM/PC-Compatible   
!--   
BEGIN Initialize things   
1.0000E+05 a Mean P Pa   
150.00 b Freq Hz   
300.00 c TBeg K   
0.0000 d lpi Pa   
0.0000 e Ph(p) deg   
9.4483E-03 f IUI m^3/s G   
147.39 g Ph(U) deg G   
helium Gas type   
1   
IESPEAKER a linear motor and piston   
sameas 3a a Area m^2 2443.2 AIpl Pa   
1.0000 b R ohms -177.67 B Ph(p) deg   
3.0000E-03 c L H 9.4248E-03 C |UI m^3/s   
5.0000 d BLProd T-m 147.29 D Ph(U) deg   
1.0000E-02 e M kg 9.4267 E Hdot W   
1.0000E+04 f K N/m 9.4267 F Edot W   
0.1000 g Rm N-s/m 20.919 G WorkIn W   
4.7776 h III A G 14.031 H Volts V   
0.0000 i Ph(I) deg 4.7776 I Amps A   
51.381 J Ph(V/I) deg   
2443.2 K |Px| Pa   
ideal Solid type -177.67 L Ph(Px) deg   
!- 2   
RPN peak to peak stroke of the motor (mm)   
2.0000 a G or T = 2A? 2.0000 A stroke   
U1 mag 1a / w / 2 \* 1000 \*   
3   
DUCT the most important piece of this resonator   
1.0000E-02 a Area m^2 S= -2 2441.6 AIpl Pa   
0.3540 b Perim m Fn( 3a) -177.56 B Ph(p) deg   
6.7000 c Length m 2.8677E-05 C |U| m^3/s   
-177.56 D Ph(U) deg   
3.5009E-02 E Hdot W   
ideal Solid type 3.5009E-02 F Edot W   
4   
SURFACE End of the pipe   
sameas 3a a Area m^2 2441.6 AIpl Pa   
-177.56 B Ph(p) deg   
8.8927E-15 C |U| m^3/s   
-36.711 D Ph(U) deg   
-8.4187E-12 E Hdot W   
ideal Solid type -8.4187E-12 F Edot W   
5

![[mu_66afccee_1c0bc0a6ca31f4c693d6.jpg]]

RPN   
0.00   
320 =Tm   
or   
RPN   
320.0   
inp =Tm   
To increment the temperature by 20 Kelvin, use either   
RPN   
0.00   
Tm 20 + =Tm   
or   
RPN   
20.0   
Tm inp + =Tm

HARDEND seal the final end of the resonator   
0.0000 a R(1/z) = 5G? 2441.6 AIpl Pa   
0.0000 b I(1/z) = 5H? -177.56 B Ph(p) deg   
8.8927E-15 C |U| m^3/s   
-36.711 D Ph(U) deg   
-8.4187E-12 E Hdot W   
-8.4187E-12 F Edot W   
-4.6190E-14 G R(1/z)   
3.7606E-14 H I(1/z)   
! The restart information below was generated by a previous run   
! You may wish to delete this information before starting a run   
! where you will (interactively) specify a different iteration   
! mode. Edit this table only if you really know your model!   
guessz 0f 0g 1h   
xprecn -1.1737E-08 4.2373E-03 -2.9847E-05   
targs 2a 5a 5b   
Mstr-slave 1 3 -2

The target parameter of an RPN, like any other target, can be used as the independent variable in a plotting loop.

An RPN segment should usually be placed downstream of all the results and guesses that it depends on, so the RPN will have current values during each DELTAEC integration sequentially through the segments—especially if the RPN is used as a target or if its results are used elsewhere in the model.

## 4.6 Changing an integration variable

It is occasionally necessary to abruptly change the value of one or more of DELTAEC's integration variables in the middle of its integration. The RPN segment lets the user change these in response to a simple algebraic calculation, by using an RPN operator of the form =variable, where variable is one of the integration variables. For example, one might have a resonator whose top half is wrapped in a water bath at one temperature and whose bottom half is bathed at another temperature. Splitting the resonator duct into two sequential DuCTs and inserting an RPN with an appropriate command string between the two DUCTs will change the gas temperature $T _ { m }$ halfway along the resonator. To change the temperature from 300 Kelvin (set in the BEGIN) to 320 Kelvin, the segment between the DUCTs could be

Used in this way, RPNs can essentially act like a user-created lumped-element segment, changing the integration variables in ways not available in DELTAEC's built-in segments. For a complicated example of a “custom segment" implemented with RPNs that change three integration variables, see "pulsed combustion" in Section 14.6.

## 4.7 Two examples

The <Examples\RPN> folder of DELTAEC's installation has more-elaborate examples of using RPN segments in the ways described above.

<LinearAlternator.out> is a 24-segment model in which most of the segments are RPNs. The model simulates a linear alternator, including leakage through an imperfect piston seal. One RPN input specifies the leakage gap around the piston, and another RPN calculates the flow impedance of that gap, for use in a subsequent IMPEDANCE segment, verifying that the Reynolds number is low enough that the laminar calculation of the flow impedance should be accurate. Another RPN calculates the piston stroke. A few more RPNs allow the IESPEAKER's complex current to be guessed, to target a specified electrical impedance: A 100-Ohm resistor in series with a $3 9 \mathrm { - } \mu \mathrm { F }$ capacitor, chosen to cancel the effect of the IESPEAKER's internal inductance. Final RPNs and other segments confirm that all incoming acoustic power is accounted for as the sum of electrical power delivered, electrical power dissipated in the IESPEAKER's internal resistance, mechanical power dissipated in the IESPEAKER's $R _ { m }$ , and thermal-hysteresis losses on all the surface areas in the model.

![[mu_66afccee_05cb948d16973b1d2dec.jpg]]

![[mu_66afccee_748bd74838be2799f268.jpg]]  
Figure 4.1: Two examples using many RPN segments. (a) A linear alternator with specified load impedance and piston leakage. (b) A loop of tubing filled with air and driven at fullwave resonance by two speakers separated by a quarter wavelength

<closedLoop. out> shows a loop of tubing 2 meters long, with two side-branch drivers a half meter apart being electrically driven $9 0 °$ out of phase at a frequency intended to create a full-wavelength traveling wave in the air in the loop. This example illustrates the use of four RPNs as targets, to ensure that DELTAEC “connects" the end of the model back to the beginning, by making $p _ { 1 }$ and $U _ { 1 }$ identical at the end and at the beginning.

```csv
O BEGIN Start in the middle of nowhere, and integrate around a loop
1.0000E+5 a Mean P Pa
178.50 b Freq Hz
300.00 c TBeg K
686.78 dlpl Pa G
-0.96981 e Ph(p) deg G
1.7140E-3 f |UI m^3/s G
2.3500 g Ph(U) deg G
air Gas type
1 RPN Edot passing this point
2 DUCT FIRST QUARTER WAVELENGTH
3 TBRANCH
-2.5435E+5 a Re(Zb) Pa-s/m^3 G
1.7389E+6 b Im(Zb) Pa-s/m^3 G
4 VESPEAKER FIRST DRIVER
5 RPN driver resonance frequency
6 SOFTEND backside of driver open to the room
0.0000 a Re(z) =6G
0.0000 b Im(z) =6H
7 DUCT SECOND QUARTER WAVELENGTH
8 RPN miscellaneous calculations, some needed later
9 TBRANCH
-4.5652E+5 a Re(Zb) Pa-s/m^3 G 698.69 AIpl Pa
1.7396E+6 b Im(Zb) Pa-s/m^3 G -174.46 B Ph(p) deg
10 VESPEAKER SECOND DRIVER
11 SOFTEND backside of driver open to the room
0.0000 a Re(z) =11G
0.0000 b Im(z) =11H
12 DUCT THIRD AND FOURTH QUARTER WAVELENGTH
13 RPN close the loop: lp1l
sameas 0d a =A? 686.78 A Pa
p1 mag
14 RPN close the loop: phase(p1)
sameas Oe a =A? -0.96981 A deg
p1 arg
15 RPN close the loop: |U1I
sameas Of a =A? 1.7140E-3 A m3/s
U1 mag
16 RPN close the loop: phase(U1)
sameas 0g a =A? 2.3500 A deg
U1 arg
```

## 4.8 Non-standard guesses

Like most other DELTAEC inputs, parameter a in an RPN segment can be used as a guess. For example, to let DELTAEC guess the temperature increment needed at the present location to hit a target downstream, guess input a in an RPN segment like this:

RPN   
20.0 G   
Tm inp + =Tm

As a contrived example, suppose that the magnetic field B in a speaker depends on temperature $T _ { m }$ according to a strange equation such as

$$
B ^ { 3 } - 5 B ^ { 2 } + 3 = T _ { m } ,\tag{4.3}
$$

and we want DELTAEC to correctly incorporate a temperature-dependent Bl product in a SPEAKER segment. We don't know how to solve Eq. (4.3) for B analytically, but we can make DELTAEC find the root of the cubic equation numerically by guessing B and targeting Eq. (4.3):

RPN (a)=magnetic field (tesla), guessed. 1.6 meters of wire. (A)= BL product.   
12.863 a G or T A 20.581 B x L   
inp 1.6 \*

```csv
RPN Target the strange equation in the Users Guide:
0.00 a G or T A 0.000 A zero
14a 3 ^ 14a 2 ^ 5 * - 3 + Tm -
!--- ---16---
IESPEAKER a linear motor and piston
sameas 3a a Area m^2 2443.2 AIpl Pa
1.0000 b R ohms -177.67 B Ph(p) deg
3.0000E-03 c L H 9.4248E-03 C |UI m^3/s
sameas 14A d BLProd T-m 147.29 D Ph(U) deg
1.0000E-02 e M kg 9.4267 E Hdot W
1.0000E+04 f K N/m 9.4267 F Edot W
0.1000 g Rm N-s/m 20.919 G WorkIn W
4.7776 h III A G 14.031 H Volts V
0.0000 i Ph(I) deg 4.7776 I Amps A
51.381 JPh(V/I) deg
2443.2 K |Px| Pa
ideal Solid type -177.67 L Ph(Px) deg
```

## 4.9 Linking multiple models

Two or more models can be open simultaneously in a single DELTAEC window, and it is sometimes useful to bring a number from one model into another model. For example, we have sometimes been interested in a few unequal engines and many unequal refrigerators sharing a common resonator, requiring so many segments and so many guesses and targets that several models are needed to hold them all. How can such multiple models communicate with one another automatically? This is accomplished with an extended RPN pointer of the form filename:addr in an RPN formula.

For example, suppose that three models, named <engine1.out>, <engine2.out>, and <engine3. out>, which represent a cascade engine [19], are simultaneously open in DELTAEC. Suppose that hot-heat-exchanger heats are given at address 12e in all three models. An RPN segment near the end of <engine3.out> could calculate the total heat required by the set of three engines with the following formula which brings results from <engine1.out> and <engine2.out> into <engine3.out>:

engine1:12e engine2:12e + 12e +

Extending this example, if the beginning of the <engine2.out> model is supposed to be fed by the end of the <engine1.out> model, where segment 87 is a STK\*\* and 88 is a HX\*\*, the key variables can be shared if the beginning of <engine2.out> looks like

! engine2.out   
BEGIN This segment is required, even though these variables are re-initialized below!   
999. Pa a Mean P   
999. Hz b Freq   
999. K c TBeg   
999. Pa d lpl   
999. deg e Ph(p)   
999. m3/s f |UI   
999. deg g Ph(U)   
helium Gas type   
RPN bring pm and f from the other model   
engine1:0a =pm %:0b =f   
1== 2   
RPN bring Tm from the other model   
engine1:87H =Tm   
3   
RPN bring p1 and U1 from the other model   
engine1:88B %:88A cmplx =p1 %:88D %:88C cmplx =U1

(The notation “% " in an interlinked RPN formula signifies "the previously named model.")

To run all of the models open in DELTAEC together, use Run All, with capital-R as its keyboard shortcut. The order of running will be left to right in the sequence in which the model tabs are laid out. Use the mouse to drag tabs from side to side to change that order. (Drag a tab off the side, top, or bottom of the panel to split the panel into two or more displays so two or more models can be seen simultaneously.) Choose the order of running carefully, so each model has up-to-date values of any numbers that it gets from other models. For convenience, choose file names so the default alphabetical opening of multiple models puts them in the desired tab order.

If two or more models are run separately, any incremental plots in any of those models will run separately, just as if they were open in separate DELTAEC windows. However, Run All can optionally change this behavior dramatically, disabling any incremental plots in the separate models and following the choices established by the user in the Multi-Model Incremental Plot Control dialog, which is available in the Display pulldown menu. The Multi-Model Plot Control lets the user choose one or two of the independent plot variables that exist in one of the individual models1 as the overall independent plot variable (1- dimensional plot) or variables (2-dimensional plot), and choose from among the established dependent plot variables (including guesses) in all of the individual models too. A Run All will then run all the models, increment an independent plot variable, run all the models again, etc., creating a table of results in a file called <MultiMod.ip>. For example, a set of linked models often share the same frequency, linked together via RPN formulas similar to firstmodelname:Ob =f . If parameter 0b in model firstmodelname is chosen as the independent Multi-Model Plot variable, then a Run All will sequentially increment the frequency in all of the linked models.

To view graphs of <MultiMod. ip> after such a Run All, click the appropriate button in the Multi-Model Plot Control. DELTAEC tries to include variables in the <MultiMod.ip> file that assist Rewinding when the user has ignored Forward-Reference-Condition warnings, so don't be surprised to find a few variables there that you don't remember including yourself

Please don't create more than one set of inter-linked models with Multi-Model Plotting in a single folder, because DELTAEC can have only one <MultiMod.ip> file per folder.

## 4.10 Other math segments

The CoNSTANTS segment allows the user to insert up to a dozen real constants in one segment. These can then be referred to by other segments (via sameas) and can be modified, used as guesses, or used as independent incremental-plot variables. See details in Section 11.4.3.

The vOLUME segment automatically adds up the volume in a series of segments. See details in Section 11.4.2. vOLUME adds up the volume of gas plus the volume of the solids in porous structures such as heat exchangers, so it gives one estimate of the size of an apparatus. (The RPN variable vol, described in Section 11.4.1, is similar to the segment voLuME, but it accesses the cumulative gas volume in the model, without involving the solid volume in the porous segments.)

## 5. Engines & refrigerators

The examples given in the previous Chapters were relatively simple cases of linear acoustics. In this Chapter, we introduce the full thermoacoustic computing power of DELTAEC with some simple engines and refrigerators. After discussing the principles and assumptions that are built into the computation, we present example calculations.

## 5.1 Principles of calculation

DELTAEC processes one-dimensional strings of acoustic and thermoacoustic elements (or networks of such strings—see Section 2.7.5 and Chapter 11 for TBRANCHs and UNIONs), so the one-dimensional “wave" equation is of the greatest importance. We assume a time dependence of $\mathrm { R e } [ \mathrm { \cdots } \mathrm { v a r i a b l e } ^ { \prime \prime } e ^ { i \omega t } ]$ , so the “wave” equation is the second-order Helmholtz differential equation for the complex pressure

![[mu_66afccee_02afbe7a82055051da00.jpg]]

amplitude $p _ { 1 } ( x )$ . As was described at the beginning of Chapter 2, we find it easiest to think of this as two coupled first-order equations in pressure $p _ { 1 }$ and volume flow rate $U _ { 1 }$ . This point of view is taken in Refs. [13] and [20]. In coupled, first-order form, the equations are ready for numerical integration along x.

In Chapter 2, we introduced such equations for DUCTs and CONEs, in which $T _ { m }$ did not vary with x. Nicholas Rott [21] derived the corresponding equation when $d T _ { m } / d x \ne 0$

$$
\left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \rho _ { m } a ^ { 2 } } { \omega ^ { 2 } } \frac { d } { d x } \left( \frac { 1 - f _ { \nu } } { \rho _ { m } } \frac { d p _ { 1 } } { d x } \right) - \beta \frac { a ^ { 2 } } { \omega ^ { 2 } } \frac { \left( f _ { \kappa } - f _ { \nu } \right) } { ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } \frac { d p _ { 1 } } { d x } = 0 ,\tag{5.1}
$$

which can be rewritten as two coupled first-order equations:

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega \rho _ { m } } { A \left( 1 - f _ { \nu } \right) } U _ { 1 } , } \\ { \displaystyle \frac { d U _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega A } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { \left( \gamma - 1 \right) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \left( f _ { \kappa } - f _ { \nu } \right) } { \left( 1 - \sigma \right) \left( 1 + \epsilon _ { s } \right) } \beta \frac { d T _ { m } } { d x } U _ { 1 } . } \end{array}\tag{5.2}
$$

These equations are used in most of the STK\*\* segments introduced below, which accommodate $d T _ { m } / d x \ne 0$ in engines and refrigerators. The complex variables $f _ { \nu }$ and $f _ { \kappa }$ depend on the size and shape of the pores and on the gas properties. Of course the right sides of these equations depend implicitly on the local value of $T _ { m }$ , because gas properties such as $\rho _ { m }$ and a depend on $T _ { m }$

To complete this picture for many thermoacoustic engines and refrigerators, only two more equations are required, i.e., those for the temperature $T _ { m } ( x )$ and the total power $\dot { H } _ { \mathrm { t o t } } ( x )$ . As for $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ , the equations for $T _ { m } ( x )$ and $\dot { H } _ { \mathrm { t o t } } ( \dot { x } )$ depend on the type of segment, and $T _ { m }$ and $\dot { H } _ { \mathrm { t o t } }$ are continuous across the junctions between segments.

In DELTAEC, the total power is treated as the sum of two terms,

$$
\dot { H } _ { \mathrm { t o t } } = \dot { H } _ { 2 , k } + \dot { H } _ { \dot { N } } .\tag{5.3}
$$

The first term, $\dot { H } _ { 2 , k }$ , represents power carried in the x direction by second-order thermoacoustic effects, generally proportional to the lateral spatial average of $\mathrm { R e } [ T _ { 1 } \widetilde { u } _ { 1 } ]$ , and by zeroth-order thermal conduction. The second term, $\dot { H } _ { \dot { N } }$ , represents power carried by nonzero time-averaged flow of gas in the x direction. In the present chapter, we consider only zero time-averaged flow, so $\dot { H } _ { \mathrm { t o t } } = \dot { H } _ { 2 , k }$ . (Nonzero $\dot { H } _ { \dot { N } }$ is introduced in Chapter 6.)

Most segments, such as DUCTs and CONEs described in Chapter 2, obey simply $d T _ { m } / d x = 0$ and $d \dot { H } _ { \mathrm { t o t } } / d x = 0$

STK\*\* segments have a more complicated differential equation for $T _ { m } ( x )$ , which is derived from Rott's energy equation [22], here generalized to include fluids that are not ideal gases,

$$
\begin{array} { r c l } { \dot { H } _ { 2 , k } } & { = } & { \displaystyle \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U } _ { 1 } \left( 1 - \frac { T _ { m } \beta ( f _ { \kappa } - \tilde { f } _ { \nu } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) ( 1 - \tilde { f } _ { \nu } ) } \right) \right] } \\ & { + } & { \displaystyle \frac { \rho _ { m } c _ { p } | U _ { 1 } | ^ { 2 } } { 2 A _ { \mathrm { g a s } } \omega ( 1 - \sigma ) | 1 - f _ { \nu } | ^ { 2 } } \frac { d T _ { m } } { d x } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \tilde { f } _ { \nu } ) ( 1 + \epsilon _ { s } f _ { \nu } / f _ { \kappa } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) } \right] } \\ & { - } & { ( A _ { \mathrm { g a s } } k + A _ { \mathrm { s o l i d } } k _ { s } ) \frac { d T _ { m } } { d x } , } \end{array}\tag{5.4}
$$

by solving it algebraically for $d T _ { m } / d x$

The total power flow $\dot { H } _ { \mathrm { t o t } }$ through a STK\*\* segment is assumed to be independent of $x ,$ because the side walls are assumed to be rigid and thermally insulated. The total power $\dot { H } _ { \mathrm { t o t } }$ changes with x in heat exchanger segments, according to

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } = \dot { q } ,\tag{5.5}
$$

where $\dot { q }$ is the heat added per unit length in the heat exchanger.

(There is also a "thermally anchored" mode in which $d \dot { H } _ { 2 , k } / d x = d \dot { E } / d x$ in DUCTs, CONEs, etc. to reflect the assumption that such segments are immersed in heat sinks; this exception to the normal circumstances will be described in Section 11.3.1.)

So, for thermoacoustic calculations, DELTAEC integrates from the BEGINning through the sequence of subsequent segments, with respect to two complex and two real variables: $p _ { 1 } ( x ) , U _ { 1 } ( x ) , T _ { m } ( x )$ , and $\dot { H } _ { \mathrm { t o t } } ( x )$ . DELTAEC uses continuity of $p _ { 1 } , U _ { 1 } , T _ { m }$ , and $\dot { H } _ { \mathrm { t o t } }$ to pass from the end of one segment to the beginning of the next. Within each segment, it uses equations appropriate to that segment type, governed by local parameters, such as area and perimeter, by global parameters, such as frequency and mean pressure, and by evolving parameters such as $p _ { 1 } , U _ { 1 } , T _ { m }$ and $\dot { H } _ { \mathrm { t o t } }$ themselves and the properties of the gas and solid. Mathematically, the DELTAEC integration can be regarded as

(5.6)

$$
\begin{array} { r l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = \mathcal { F } _ { \mathrm { n o n e n t u m } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; p _ { m } , \omega ; \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) , } \\ { \displaystyle \frac { d U _ { 1 } } { d x } } & { = \mathcal { F } _ { \mathrm { c o n t i m i t y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; p _ { m } , \omega , \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) , } \\ { \displaystyle \frac { d T _ { m } } { d x } } & { = \mathcal { F } _ { z \mathrm { e n o n g y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; p _ { m } , \omega , \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) , } \\ { \displaystyle \frac { d \dot { H } _ { \mathrm { t o t } } } { d x } } & { = \mathcal { F } _ { \mathrm { l a t e a l ~ e n e r g y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; p _ { m } , \omega , \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) } \end{array}\tag{5.7}
$$

(5.8)

(5.9)

In reality, as documented here and in Chapter 10, most of the equations for specific segments are simpler than what's suggested by the fully general forms of Eqs. (5.6)-(5.9). For example, the right-hand side of the momentum equation never depends explicitly on $\dot { H } _ { \mathrm { t o t } }$ ; many segment types have simply $d U _ { 1 } / d x = 0$ or $d T _ { m } / d x = 0$ or can calculate $\Delta p _ { 1 }$ algebraically instead of with a numerical integration; and $d H _ { \mathrm { t o t } } / d x$ is usually zero or as simple as Eq. (5.5). Nevertheless, it is useful to keep in mind the fully general picture of Eqs. (5.6)−(5.9), to help remember what DELTAEC needs to know at each location x as it proceeds with its numerical integration.

## 5.2 Hofler's refrigerator

Tom Hofler's thermoacoustic refrigerator was described in detail in his Ph.D. thesis [1] and was briefly summarized in Ref. [2]. We use this case to further illustrate capabilities of DELTAEC, generating curves similar to Figs. 16 and 17 in Ref. [1] (Figs. 5 and 6 in Ref. [2]).

The apparatus is shown here in Fig. 5.1. We begin with a file (<hofler1.out>, in the <Examples\EnginesAndRefr> folder) whose geometry is that of Hofler's "long" apparatus. (We originally typed this file in a Notepad text editor while studying Ref. [1].) The list of segments serves as an outline of the model:

```makefile
O BEGIN:
1 SURFACE: driver end
2 DUCT : ambient temperature duct
3 HX : ambient temperature heat exchanger
4 STKSLAB: Stack
5 HX : Cold heat exchanger
6 DUCT : Cold Duct
7 CONE :
8 COMPLIANCE: end bulb
```

and clicking the toolbar “+" shows details:

![[mu_66afccee_4e7e98e82151d1c50705.jpg]]  
Figure 5.1: Hofler's thermoacoustic refrigerator.

<table><tr><td colspan="6">TITLE</td></tr><tr><td colspan="6">!Created@16:29:08 1.</td></tr><tr><td colspan="6">BEGIN</td></tr><tr><td colspan="6">1.0000E+06 a Mean P</td></tr><tr><td>500.00</td><td>b Freq</td><td>Pa Hz</td><td></td><td></td><td></td></tr><tr><td>300.00</td><td>c TBeg</td><td>K</td><td></td><td></td><td></td></tr><tr><td>3.0000E+04 d</td><td>|pl</td><td>Pa</td><td></td><td></td><td></td></tr><tr><td>0.0000</td><td>e Ph(p)</td><td>deg</td><td></td><td></td><td></td></tr><tr><td>5.0000E-04</td><td>f |U|</td><td>m^3/s</td><td></td><td></td><td></td></tr><tr><td>0.0000</td><td>g Ph(U)</td><td>deg</td><td></td><td></td><td></td></tr><tr><td>helium</td><td>Gas type</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SURFACE</td><td>driver end</td><td>m^2</td><td></td><td></td><td></td></tr><tr><td>1.1340E-03 a Area</td><td></td><td></td><td>0.0000</td><td>AIpl</td><td>Pa</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>C |UI</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td></td><td>0.0000 E Htot F Edot</td><td>W W</td></tr><tr><td></td><td></td><td></td><td>0.0000 2</td><td></td><td></td></tr><tr><td>DUCT</td><td></td><td>ambient temperature duct</td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>1a a Area</td><td>m^2</td><td>0.0000</td><td>AIpl</td><td>Pa</td></tr><tr><td></td><td>0.1190 b Perim</td><td>m</td><td>0.0000</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>4.2600E-02 c Length</td><td></td><td>m</td><td>0.0000</td><td>C IUI</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>E Htot</td><td>W</td></tr><tr><td>ideal 1</td><td>Solid type</td><td></td><td>0.0000</td><td>F Edot</td><td>W</td></tr><tr><td colspan="6"></td></tr><tr><td>HX</td><td>ambient temperature heat exchanger</td><td></td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>1a a Area</td><td>m^2</td><td>0.0000</td><td>AIpl</td><td>Pa</td></tr><tr><td>0.6000</td><td>b GasA/A</td><td></td><td>0.0000</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>6.3500E-03</td><td>c Length</td><td>m</td><td>0.0000</td><td>C |UI</td><td>m^3/s</td></tr><tr><td>1.9000E-04</td><td>dy0</td><td>m</td><td>0.0000</td><td>D Ph(U)</td><td>deg</td></tr><tr><td>-9.6400</td><td>e HeatIn</td><td>W</td><td>0.0000</td><td>E Htot</td><td>W</td></tr><tr><td>300.00</td><td>f Est-T</td><td>K</td><td>0.0000</td><td>F Edot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>G GasT</td><td>K</td></tr><tr><td>copper</td><td>Solid type</td><td></td><td>0.0000</td><td>H SolidT</td><td>K</td></tr><tr><td colspan="6">!</td></tr><tr><td>STKSLAB</td><td>Stack</td><td></td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>1a a Area</td><td>m^2</td><td>0.0000</td><td>AIpl</td><td>Pa</td></tr><tr><td></td><td>0.7240 b GasA/A</td><td></td><td>0.0000</td><td>B Ph(p)</td><td>deg</td></tr><tr><td></td><td>7.8500E-02 c Length</td><td>m</td><td>0.0000</td><td>C |UI</td><td>m^3/s</td></tr><tr><td>1.8000E-04 d y0</td><td></td><td>m</td><td>0.0000</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td>4.0000E-05 e Lplate</td><td>m</td><td>0.0000</td><td>E Htot</td><td>W W</td></tr><tr><td></td><td></td><td></td><td>0.0000</td><td>F Edot G TBeg</td><td>K</td></tr><tr><td>kapton</td><td></td><td></td><td>0.0000 0.0000</td><td>H TEnd</td><td>K</td></tr><tr><td></td><td>Solid type</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="6">HX</td></tr><tr><td>sameas</td><td>1a a Area</td><td>Cold heat exchanger m^2</td><td></td><td>Alpl</td><td>Pa</td></tr><tr><td>0.6700 b GasA/A</td><td></td><td></td><td>0.0000 0.0000</td><td>B Ph(p)</td><td>deg</td></tr><tr><td>2.5400E-03 c Length</td><td></td><td>m</td><td>0.0000</td><td>C |UI</td><td>m^3/s</td></tr><tr><td>2.5500E-04 d y0</td><td></td><td>m</td><td>0.0000</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>3.0000 e HeatIn</td><td>W</td><td>0.0000</td><td>E Htot</td><td>W</td></tr></table>

![[mu_66afccee_41df4da117e11efc1bbb.jpg]]

<table><tr><td>200.00</td><td>f Est-T</td><td>K</td><td>(t) 0.0000 0.0000</td><td>F Edot G GasT</td><td>W K</td></tr><tr><td>copper</td><td>Solid type</td><td></td><td>0.0000 6</td><td>H SolidT</td><td>K</td></tr><tr><td>DUCT</td><td>Cold Duct</td><td></td><td></td><td></td><td></td></tr><tr><td>3.8400E-04 a Area</td><td></td><td>m^2</td><td></td><td>0.0000 Alpl</td><td>Pa</td></tr><tr><td>6.9400E-02 b Perim</td><td></td><td>m</td><td></td><td>0.0000 B Ph(p)</td><td>deg</td></tr><tr><td></td><td>0.1670 c Length</td><td>m</td><td></td><td>0.0000 C |U|</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td></td><td>0.0000 D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>0.0000 E Htot</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td></td><td>0.0000 F Edot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>7</td><td></td><td></td></tr><tr><td>CONE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>6a a AreaI</td><td> $\mathtt { m } \hat { \ } 2$ </td><td></td><td>0.0000 AIpl</td><td>Pa</td></tr><tr><td>sameas</td><td>6b b PerimI</td><td>m</td><td></td><td>0.0000 BPh(p)</td><td>deg</td></tr><tr><td>1.1600E-03 d AreaF</td><td>6.6800E-02 c Length</td><td>m</td><td></td><td>0.0000 C |U|</td><td>m^3/s</td></tr><tr><td>0.1210</td><td></td><td> $\mathtt { m } \hat { \ } 2$ </td><td></td><td>0.0000 D Ph(U)</td><td>deg</td></tr><tr><td></td><td> e PerimF</td><td>m</td><td>0.0000</td><td>E Htot</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td>0.0000 8</td><td>F Edot</td><td>W</td></tr><tr><td>! – COMPLIANCE end bulb</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.9000E-02 a SurfAr</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.0600E-03 b Volume</td><td></td><td>m^2</td><td>0.0000</td><td>AIpl B Ph(p)</td><td>Pa</td></tr><tr><td></td><td></td><td>m^3</td><td>0.0000 0.0000</td><td>C |UI</td><td>deg m^3/s</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>0.0000 D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td></td><td>0.0000 E Htot</td><td>W</td></tr><tr><td>ideal</td><td>Solid type</td><td></td><td></td><td>0.0000 F Edot</td><td>W</td></tr></table>

The segments that were not introduced in Chapter 2 are HX and STKSLAB.

HX's have parallel-plate geometry, with plate spacing $2 y _ { o }$ . Wave propagation through heat exchangers is computed using the momentum and continuity equations, including both viscous and thermal dissipation, much like the calculations in DuCTs. There is one additional input: the heat added to the thermoacoustic wave from an external thermal reservoir (or, if negative, the heat rejected to the external reservoir). The heat flow determines the change in total energy flow $\dot { H } _ { \mathrm { t o t } }$ in the heat exchanger. As an input variable, heat flow can either be specified by the user (and, optionally, an independent plot variable) or it can be a guess. There is also a potential target: the temperature of the solid in the heat exchanger, which is assumed to be spatially uniform and which differs from the temperature in the gas in proportion to the heat, as described in Chapter 10. The temperature difference between gas and solid can presently be computed only with an accuracy of about a factor of 2, even in the acoustic approximation; nevertheless, it is included in DELTAEC, to prevent naive users from being led to designs with heat exchangers of negligible surface area that have negligible losses and that would appear to have no disadvantages if this temperature difference were not included. We hope that future revisions of DELTAEC will have a more accurate calculation algorithm for this effect. Meanwhile, however, if you prefer not to use this feature, watch or target the gas mean temperature instead of the solid temperature by using RPN (see Chapter 4) or observing the gas temperature in the adjacent stack segment (parameter G or H).

STKSLAB also has parallel-plate geometry. This is the first segment we have encountered in the Tutorial in which $T _ { m }$ can depend on x. DELTAEC obtains the x dependence by integrating the thermoacoustic energy equation, schematically given by Eq. (5.8) and in detail in Eqs. (5.4) and the equations given in Section 10.5.1, with $\dot { H } _ { \mathrm { t o t } }$ independent of x.

Using the lessons we learned in Chapter 2, we recognize that we do not know all the initial conditions at BEGIN, so we must introduce some necessary guesses and targets. We know that zero $U _ { 1 }$ must flow through the bottom of the refrigerator, so we insert a HARDEND there and use its two impedance targets. Corresponding to those targets, we'll guess two variables in BEGIN. These might be complex $U _ { 1 }$ , but Hofler always ran his refrigerator on resonance, so we'll guess $| U _ { 1 } |$ and frequency f as guesses to get started, leaving the phases of $p _ { 1 }$ and $U _ { 1 }$ equal (both zero) as the condition for resonance at the driver. After adding these variables, the guess-target list looks like

GUESS Ob Of   
name BEGIN:Freq BEGIN:|U|   
units Hz m^3/s   
value 5.00E+02 5.00E-04   
TARGET 9a 9b   
name HARDE:R(1/z HARDE:I(1/z   
value .00 .00

Running this case yields f = 497.4 Hz and $| U _ { 1 } | = 5 . 0 5 6 \times 1 0 ^ { - 4 } ~ \mathrm { m ^ { 3 } / s }$ We are gratified that none of the results thus far appear crazy. If you are running this file for yourself, note also that the solid is cooler than the gas in the ambient heat exchanger, where the (negative) heat flows from gas to solid, and that the solid is warmer than the gas in the cold heat exchanger, where the (positive) heat flow is from solid to gas.

Now consider what guesses and targets might be required by the heat and temperature aspects of this model. We know that the bottom of the apparatus was thermally insulated, so no energy can flow in or out there. We also note from Ref. [1] that Hofler maintained the solid temperature in the ambient heat exchanger at 300 K by vigorous flow of temperatureregulated water through it. These two constraints, not at the BEGINning, call for the use of two targets: 9c and 3f. Hofler applied a known electrical heater power to the cold heat exchanger, so we need not guess that; we leave its value at 3.00 W for now. However, he did not control the heat removed at the ambient heat exchanger, nor the temperature of the gas at the ambient end; so DELTAEC must guess those two variables: 0c and 3e. After making the necessary changes, the guess-target summary looks like

GUESS Ob 0c Of 3e   
name BEGIN:Freq BEGIN:TBeg BEGIN:|U| HX:HeatI   
units Hz K m^3/s W   
value 497.40 300.0 5.056E-04 -9.640   
TARGET 3f 9a 9b 9c   
name HX:Est-T HARDE:R(1/z HARDE:I(1/z HARDE: Hdot   
units K W   
value 300.0 0.00 0.00 0.00   
before running, and   
GUESS Ob 0c Of 3e   
name BEGIN:Freq BEGIN:TBeg BEGIN: |U| HX:HeatI   
units Hz K m^3/s W   
value 503.47 300.79 5.4187E-04 -11.128   
TARGET 3f 9a 9b 9c   
name HX:Est-T HARDE:R(1/z HARDE:I(1/z HARDE:Htot   
units K W   
value 300.00 0.0000 0.0000 0.0000   
result 300.00 -6.0493E-12-1.0355E-101.7764E-15

after running. By examining segment 5 in the <.out> file, we see that DELTAEC predicts a cold temperature of 223.27 K with this 3.00 W heat load on the cold heat exchanger.

All of these results are reasonable, so now we examine Ref. [1] very closely to consider what else we should do to compare DELTAEC results directly to the published results of Hofler's experiments. Hofler added the calculated dissipation in the DUCT, CONE, and CoMPLIANCE to his electrically applied heat load, to plot the gross cooling power instead of the net cooling power. So we do the same, with an RPN segment at the end of the model. We add another RPN to display another of his plotted variables, the temperature ratio. On the basis of the gross cooling power and the measured acoustic power delivered to the resonator by the driver, Hofler also plotted the coefficient of performance, $C O P = \dot { Q } _ { C , \mathrm { g r o s s } } / \dot { E } .$ relative to Carnot's COP, $C O P _ { \mathrm { C a r n o t } } { = } T _ { C } / \left( T _ { 0 } - T _ { C } \right)$ , so we calculate $C O P / C O P _ { \mathrm { C a r n o t } }$ with a third RPN at the end. These additions look like

+ O BEGIN   
+ 1 SURFACE driver end   
+ 2 DUCT ambient temperature duct   
+ 3 HX ambient temperature heat exchanger   
+ 4 STKSLAB Stack   
+ 5 HX Cold heat exchanger   
+ 6 DUCT Cold Duct   
+ 7 CONE   
+ 8 COMPLIANCE end bulb   
+ 9 HARDEND target this to seal the end   
!-- - 10-   
RPN gross cooling power is net power plus tail dissipation   
0.0000 a G or T (t) 3.8502 A Qg (W)   
5e 5F +   
!- - 11   
RPN temperature ratio, Tc/TO   
0.0000 a G or T (t) 0.74424 A ratio   
5H 3H  /   
1 - - 12   
RPN COP / Carnot's COP   
0.0000 a G or T (t) 0.1635 A COP rel   
10A 1F / 5H 3H 5H - / /

We let the net cooling power, i.e., heat 5e at the cold heat exchanger, be the independent plot variable in DELTAEC, ranging from 1 to 7 W in 0.5 W steps. To obtain the variables we want to display, we add 10A, 11A, and 12A to the list of dependent plot variables. After running this case, we changed $| p _ { 1 } |$ to 0.015 of $p _ { m }$ , and changed 5e to 0.5 W, making those changes by hand in a couple of steps to make sure DELTAEC did not get lost. Then we again used 5e as the independent plot variable, over the range of $\dot { Q } _ { C }$ to 0.5–3.5 W in steps of 0.25 W, and ran it again, appending the results to the previous plot run. We imported the resulting <.ip> file into a spreadsheet so we could display it together with Hofler's experimental data. The results are shown in Figs. 5.2. The DELTAEC calculations come reasonably close to the measurements presented in Figs. 16 and 17 of Hofler's thesis [1].

Let's modify this example a little more, using it to illustrate some points about sidebranch and series transducers and about DELTAEC's consistency with the first law of thermodynamics. First, let's add a more realistic driver to the system, using VSPEAKER. We insert VSPEAKER at the beginning, using Ref. [1] for approximate numerical values for the mass, resistance, and force constant for the speaker, and we delete the SURFACE segment that was previously near the beginning because vSPEAKER accounts for the oscillatory pressurization losses on its surface area. We use the drive voltage as a guess, so we are asking DELTAEC what voltage we must supply to maintain $| p _ { 1 } | = 3 0 ~ \mathrm { k P a }$ in front of the speaker; we estimate it will take about 20 V to drive it, so we use that as our starting value for the guess. We'll also add an RPN target after the VSPEAKER, to enforce resonance by ensuring that the phases of $p _ { 1 }$ and $U _ { 1 }$ are equal at the driver. We do this by forcing their difference, computed by subtracting the values appearing as results 1B and 1L, to be zero, which is the value given in line 2a.

With this change, BEGIN is no longer at a position of nonzero $| U _ { 1 } |$ ; BEGIN is now at a place where $U _ { 1 } = 0$ and $p _ { 1 }$ is nonzero, and the subsequent side-branch vSPEAKER adds all the volume flow rate that flows into the subsequent segments. We change guesses and initial values accordingly. With these changes, but before running, the guess-target list becomes

![[mu_66afccee_8d62b9841368687b8a59.jpg]]  
Figure 5.2: Hofler refrigerator results. Lines are DELTAEC results; points are from experimental data presented in Hofler's thesis. Squares, $p _ { 1 } = 0 . 0 1 5 p _ { m }$ . Circles, $p _ { 1 } = 0 . 0 3 p _ { m }$

<table><tr><td rowspan="4">GUESS name units value TARGET</td><td>Ob</td><td>0c</td><td>Oe</td><td>1h BEGIN:Ph(p) VSPEA:AplVo</td><td>4e</td></tr><tr><td>BEGIN:Freq Hz</td><td>BEGIN:TBeg K</td><td>deg</td><td>V</td><td>HX:HeatI W</td></tr><tr><td>503.47</td><td>300.79</td><td>100.00</td><td>20.000</td><td>-11.128</td></tr><tr><td>2a</td><td>4f</td><td>10a</td><td>10b</td><td>10c</td></tr><tr><td>name units</td><td>RPN:Targe</td><td></td><td></td><td>HX:Est-T HARDE:R(1/z HARDE:I(1/z HARDE:Htot</td><td></td></tr><tr><td>value</td><td>0.0000</td><td>K 300.00</td><td>0.0000</td><td>0.0000</td><td>W 0.0000</td></tr><tr><td></td><td></td><td></td><td></td><td>5.8006E-14 -1.7764E-15</td><td></td></tr><tr><td>result</td><td>0.0000</td><td>300.00</td><td>-7.8635E-15</td><td></td><td></td></tr></table>

## and when we run it the guess-target list becomes

<table><tr><td>GUESS name</td><td>Ob</td><td>0c</td><td>Oe</td><td>1h BEGIN:Ph(p) VSPEA:AplVo</td><td>4e HX:HeatI</td></tr><tr><td>units</td><td>BEGIN:Freq Hz</td><td>BEGIN:TBeg K</td><td>deg</td><td>V</td><td>W</td></tr><tr><td>value</td><td>504.85</td><td>302.56</td><td>152.55</td><td>23.379</td><td>-36.018</td></tr><tr><td>TARGET</td><td>2a</td><td>4f</td><td>10a</td><td>10b</td><td>10c</td></tr><tr><td>name</td><td>RPN:Targe</td><td></td><td></td><td>HX:Est-T HARDE:R(1/z HARDE:I(1/z HARDE:Htot</td><td></td></tr><tr><td>units value</td><td>0.0000</td><td>K 300.00</td><td>0.0000</td><td>0.0000</td><td>W 0.0000</td></tr><tr><td></td><td></td><td></td><td></td><td>2.5373E-12-2.5260E-11-4.2633E-12</td><td></td></tr><tr><td>result</td><td>1.7536E-11</td><td>300.00</td><td></td><td></td><td></td></tr></table>

## and the <.out> file becomes

```csv
TITLE Hofler's 1986 thermoacoustic refrigerator
!Created@21:47:02 26-Jun-20 with DeltaE Vers. 6.4b2.8 for the IBM/PC-Compatible
0
BEGIN
1.0000E+06 a Mean P Pa
504.85 b Freq Hz G
302.56 c TBeg K G
3.0000E+04 d lpl Pa
152.55 e Ph(p) deg G
0.0000 f |U| m^3/s
0.0000 g Ph(U) deg
helium Gas type
1
VSPEAKER electrodynamic driver
6.0000E-04 a Area m^2 3.0000E+04 A lpl Pa
6.0000 b R ohms 152.55 B Ph(p) deg
0.0000 CL H 5.4231E-04 C |U| m^3/s
8.0000 d BLProd T-m 152.42 D Ph(U) deg
5.0000E-03 e M kg 33.018 E Htot W
0.0000 f K N/m 8.1346 F Edot W
0.0000 g Rm N-s/m 33.018 G WorkIn W
23.379 h AplVol V G 23.379 H Volts V
2.8789 I Amps A
-11.151 J Ph(V/I) deg
5.4356E-04 K |Ux| m^3/s
ideal Solid type 152.55 L Ph(-Ux deg
2
RPN enforce resonance
0.0000 a G or T = 2A? 1.7536E-11 A null
1B 1L -
+ 3 DUCT ambient temperature duct
+ 4 HX ambient temperature heat exchanger
+ 5 STKSLAB Stack
+ 6 HX Cold heat exchanger
+ 7 DUCT Cold Duct
+ 8 CONE
+ 9 COMPLIANCE end bulb
+ 10 HARDEND target this to seal the end
+ 11 RPN gross cooling power is net power plus tail dissipation
+ 12 RPN temperature ratio, Tc/TO
+ 13 RPN COP / Carnot's COP
```

![[mu_66afccee_e501417cc0af0775f4a5.jpg]]

Comparing the values of the guesses here with those before we inserted the VSPEAKER shows two big differences: the phase of the pressure and the heat rejected at the ambient heat exchanger.

The change in the phase of the pressure is essentially trivial: The vSPEAKER segment sets the overall time phase of everything in the model, because the phase of its voltage is fixed at zero. Previously, the phase of $U _ { 1 }$ at the top of the model was arbitrarily set to zero by the

BEGIN segment. Now, the VSPEAKER controls the overall time phase of the model, and the nonzero imaginary part of the speaker's mechanical impedance causes a large phase shift between $V _ { 1 }$ and $U _ { 1 }$ . This simply shifts all $p _ { 1 }$ and $U _ { 1 }$ phasors by about 30°. A further $1 8 0 ^ { \circ }$ phase shift enters because of the sign convention for positive voltage built into the segment.

The increase in the heat rejected at the ambient heat exchanger from 11.1 W to 36.0 W is meaningful. The extra heat comes from the VSPEAKER, and illustrates how DELTAEC handles energy for \*\*SPEAKERs and \*\*DUCERs: They are treated as thermally insulated, so all of the electrical energy going into them shows up either as acoustic power or as heat. This transducer is not remarkably efficient at converting electrical power into acoustic power; most of its electrical power becomes heat, which is rejected at the ambient heat exchanger in this model. The extra load on the ambient heat exchanger increases the temperature difference in that heat exchanger a little, which leads to the small increase in gas temperature seen in 0c, which in turn leads to the small increase in resonance frequency seen in 0b.

The speaker can also be included in the model “in series," using a VESPEAKER segment, with yet another reconfiguration of the BEGIN and associated guesses and targets to reflect new circumstances. As shown below, we include the cavity above the speaker, which appears from Ref. [1] to have a volume of approximately a liter. Above that volume, the BEGIN starts with $U _ { 1 } = 0$ and with a guessed $p _ { 1 }$ . We arbitrarily set the time phase of the entire model by setting the phase of $p _ { 1 }$ in that volume to zero in the BEGIN. We note that Hofler had cooling-water tubes attached to the driver housing, to try to remove as much of the driver's electrical and other dissipation as possible. To crudely model the effect of these tubes, we insert an RPN below the driver, which we craft so it removes 75% of the driver's heat, to illustrate the use of RPN for such purposes. With these changes, and after running, the guess-target list becomes

GUESS Ob 0c Od 2h 2i 7e   
name BEGIN:Freq BEGIN:TBeg BEGIN: lpl VESPE: |V| VESPE:Ph(V) HX:HeatI   
units Hz K Pa V deg W   
value 503.85 301.22 283.95 23.252 116.79 -17.225   
TARGET 3a 4a 7f 13a 13b 13c   
name RPN:Targe RPN:Targe HX:Est-T HARDE:R(1/z HARDE:I(1/z HARDE:Htot   
units K W   
value 0.0000 3.0000E+04 300.00 0.0000 0.0000 0.0000   
result -5.5422E-13 3.0000E+04 300.00 1.7565E-14 1.8398E-13 2.4869E-14

and the <.out> file becomes

```csv
TITLE Hofler's 1986 thermoacoustic refrigerator
!Created@18:52:37 3-0ct-06 with DeltaE Vers. 6.0g2 for the IBM/PC-Compatible
BEGIN
1.0000E+06 a Mean P Pa
503.85 b Freq Hz G
301.22 c TBeg K G
283.95 d lpi Pa G
0.0000 e Ph(p) deg
0.0000 f |U| m^3/s
0.0000 g Ph(U) deg
helium Gas type
1
COMPLIANCE the space above the speaker
0.1000 a SurfAr m^2 283.95 AIpl Pa
1.0000E-03 b Volume m^3 0.0000 B Ph(p) deg
5.4133E-04 C |U| m^3/s
-90.208 D Ph(U) deg
0.0000 E Htot W
ideal Solid type -2.7938E-04 F Edot W
2
```  
VESPEAKER electrodynamic driver

![[mu_66afccee_bb5507d27555fde15c06.jpg]]

```csv
6.0000E-04 a Area m^2 3.0000E+04 A Ipl Pa
6.0000 b R ohms -90.333 B Ph(p) deg
0.0000 CL H 5.4017E-04 C |U| m^3/s
8.0000 d BLProd T-m -90.333 D Ph(U) deg
5.0000E-03 e M kg 32.591 E Htot W
0.0000 f K N/m 8.1025 F Edot W
0.0000 g Rm N-s/m 32.591 G WorkIn W
23.252 h IVI V G 23.252 H Volts V
116.79 i Ph(V) deg G 2.8560 I Amps A
-11.022 J Ph(V/I) deg
3.0003E+04 K |Px| Pa
-90.875 L Ph(Px) deg
3
RPN enforce resonance
0.0000 a G or T = 3A? -5.5422E-13 A null
2B 2D
! - 4
RPN enforce desired pressure amplitude
3.0000E+04 a G or T = 4A? 3.0000E+04 A Ip1I
p1 mag
!- 5
RPN (a)= % of driver heat removed by water tubes on driver box
0.7500 a G or T (t) 14.225 A Watt
18.366 B Watt
Htot Edot - inp * sto Htot rcl - =H2k
! –- 6
DUCT ambient temperature duct
1.1340E-03 a Area m^2 2.9736E+04 A Ipl Pa
0.1190 b Perim m -90.527 B Ph(p) deg
4.2600E-02 c Length m 2.8048E-03 C |U| m^3/s
-169.55 D Ph(U) deg
14.225 E Htot W
ideal Solid type 7.9441 F Edot W
+ 7 HX ambient temperature heat exchanger
+ 8 STKSLAB Stack
+ 9 HX Cold heat exchanger
+ 10 DUCT Cold Duct
+ 11 CONE
+ 12 COMPLIANCE end bulb
+ 13 HARDEND target this to seal the end
+ 14 RPN gross cooling power is net power plus tail dissipation
+ 15 RPN temperature ratio, Tc/TO
+ 16 RPN COP / Carnot's COP
```

Notice how the DELTAEC RPN operator =H2k has been used to override DELTAEC's normal continuity of $\dot { H }$ between segments, to simulate the removal of 18.366 W of heat by the water-cooled tubing on Hofler's driver housing.

The standing-wave components of the pressure and volume-flow-rate waves in this refrigerator model are shown in Fig. 5.3—it is essentially a quarter-wave device. In DELTAEC models of thermoacoustic engines and refrigerators, it is often also worthwhile to examine graphs of $\dot { H }$ and $\dot { E }$ and to think about their consistency with the laws of thermodynamics, e.g., to reveal possible fuzzy thinking about how BEGIN and \*\*END are set up in the model. In the present case, shown in Fig. 5.4, the acoustic power delivered by the driver drops most rapidly in the stack and more slowly in the bottom part of the resonator, and the constancy of $\dot { H } _ { \mathrm { t o t } }$ in each insulated segment (i.e., everywhere but in heat exchangers) is evident. The positive signs of these power flows indicate flows in the positive-x direction, i.e., from the BEGIN toward the HARDEND in the model.

Another instructive graph displays gas temperature $T _ { m }$ and solid temperature $T _ { \mathrm { s o l i d } }$ as functions of $x ,$ as illustrated for the present example in Fig. 5.5. In heat exchangers, the difference $T _ { \mathrm { s o l i d } } - T _ { m }$ is due to the time-averaged heat flowing from solid to gas. In other segments, where there is no time-averaged heat flowing from solid to gas, these two temperatures are equal.

hofler7.spl  
![[mu_66afccee_5d122d06da49c98c635a.jpg]]  
Figure 5.3: Standing-wave parts of the $p _ { 1 }$ and $U _ { 1 }$ wave in Hofler's refrigerator.

![[mu_66afccee_a68388e94c920dc07d24.jpg]]  
Figure 5.4: Acoustic power $\dot { E }$ (dashed blue) and total power $\dot { H }$ (solid red) as a function of x in the refrigerator model. The BEGIN, COMPLIANCE, and VSPEAKER are all crowded into $x = 0$ . The drop in $\dot { H }$ marks the ambient heat exchanger and the smaller rise in $\dot { H }$ marks the cold heat exchanger.

hofler7.spl  
![[mu_66afccee_ea4bc9f7b259da3ceaf6.jpg]]  
Figure 5.5: DELTAEC results for gas temperature $T _ { m }$ and solid temperature $T _ { \mathrm { s o l i d } }$ as functions of x in the uppermost part of Hofler's refrigerator. These temperatures differ only in the heat exchanger.

## 5.3 Choosing guesses and targets

The final example in the previous section used six targets and six guesses—the most complicated guess-target summary table we have yet encountered in the Users Guide. In this section, we discuss how we chose its members, and explain some general guidelines for guess-target choices.

Recall the purpose of guesses and targets. DELTAEC is numerically integrating equations for $p _ { 1 } , U _ { 1 }$ , and $T _ { m }$ , which can generally be regarded as

$$
\frac { d p _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { m o m e n t u m } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{5.10}
$$

$$
\frac { d U _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{5.11}
$$

$$
\frac { d T _ { m } } { d x } = \mathcal { F } _ { x \mathrm { { r \mathrm { - } e n e r g y } } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{5.12}
$$

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } = \dot { q } \mathrm { i n h e a t e x c h a n g e r s ; = 0 e l s e w h e r e . }\tag{5.13}
$$

from the BEGIN segment to the end of the model. Some of the results of that integration are actually known a priori by the user, and some of the variables needed by DELTAEC to perform that integration are not known a priori by the user. These exceptional variables are specified by the user as targets and guesses, respectively, and DELTAEC uses a shooting-method algorithm, attempting to meet the targets by finding suitable values for the guesses. Initial values for guesses are usually left over from a previous run of DELTAEC, but sometimes they are provided by the user.

For the refrigerator example of the previous section, we chose targets and guesses by considering what integration results were known by us a priori and what input variables were not known by us a priori. We looked first near the end of the model for possible targets. We definitely needed the three HARDEND variables $\operatorname { R e } [ 1 / z _ { n } ]$ , Im $\left[ 1 / z _ { n } \right]$ , and $\dot { H } _ { \mathrm { t o t } }$ in the target list, all targeted to zero, because there is no hole in the end of the apparatus that would allow nonzero $U _ { 1 }$ or $\dot { H } _ { \mathrm { t o t } }$ to escape—these are integration results that are known to us a priori. Experimentally, Hofler maintained the hot heat exchanger at 300 Kelvin; but DELTAEC computes that as a result of each integration pass, so it also had to be a target. We looked first at the BEGIN segment for candidate guesses. The beginning gas temperature was not known a priori by us: DELTAEC had to adjust the beginning $T _ { m }$ to arrive at the first HX $T _ { \mathrm { s o l i d } }$ correctly, so 0c had to be a guess. Next, we did not know the frequency needed to maintain resonance a priori, so it too had to be a guess. But how was resonance determined experimentally? By comparing the phases of $p _ { 1 }$ and $U _ { 1 }$ at the driver. These phases are computed by DELTAEC as results. Hence, we added their difference = 0 as a fifth target. While we were thinking about the driver, we realized that we wanted to imagine that $| p _ { 1 } |$ just below the driver was fixed, because Hofler adjusted his driver voltage to achieve a desired amplitude. Thus $\left| p _ { 1 } \right|$ at that location—a calculated result in DELTAEC—had to be a target, and the driver voltage had to be a guess. The heat rejected in the first heat exchanger had to be guessed because we didn't know it or control it experimentally, yet it is required by DELTAEC for each numerical integration. By now we had six targets and four guesses, so we needed two more guesses. One guess must be $| p _ { 1 } |$ at the beginning, which is in the cavity above the loudspeaker, where we had no a priori knowledge of pressure. One more guess was needed. The overall time phase of a DELTAEC model is meaningless; somewhere there is always one time-phase variable that can be chosen arbitrarily. However, here we still had two phases set arbitrarily: the phase of $p _ { 1 }$ at the BEGIN and the phase of $V _ { 1 }$ in the driver. One of these had to be used as a guess. We chose to use the phase of $V _ { 1 }$ as that guess.

We chose a point of view where we wanted to learn the cold solid temperature 9H for a given cooling power 9e. Had we wanted to have DELTAEC tell us the cooling power at a known cold temperature, we would have used an additional guess-target pair, targeting $T _ { C }$ and guessing $\dot { Q } _ { C }$

Although some situations that we model in DELTAEC are not this confusing, choosing the guesses and targets is never easy for a complicated thermoacoustic system. To choose them wisely, two things are essential: careful thought about the particular thermoacoustic system itself, and an appreciation of what variables are results of a single DELTAEC integration from BEGIN to \*\*END and what variables are needed by DELTAEC for each such integration. We introduce a few general guidelines for this thought process here.

To understand which variables are candidate targets, you must know which variables are computed as results by DELTAEC during each pass. To understand which variables are candidate guesses, you must know which variables are needed by DELTAEC for each pass of its integration. To aid this understanding, look at Eqs. (5.10)-(5.13), where computed results are the variables on the left-hand sides, and variables needed are on the right-hand sides. Print these equations (or the more complete versions at the beginning of Chapter 10) and post them near your workstation, so you can look at them for inspiration when you are trying to figure out guesses and targets for a new or modified model. Also look at the columnar structure of the $\mathbf { < . { o u t } b } \mathbf { \hat { \Pi } } \cdot \mathbf { \hat { \Pi } } \mathrm { { h l e } }$ , where variables needed by DELTAEC for each pass of its integration are in the left column (as are potential targets) and variables that DELTAEC computes as results during each pass are in the right column. For a perfect understanding there is no good substitute for studying the summaries of the computation algorithms for each segment, as discussed briefly in the tutorial chapters of the Users Guide, and more fully in Chapter 10.

Table 5.1: Choosing guesses and targets.
<table><tr><td></td><td>Variables we think of as known</td><td>Variables we think of as results</td></tr><tr><td>Variables that DELTAEC needs as inputs for each pass of integration. Includes  $T _ { m } { \mathrm { - b e g i n } } ,$   $p _ { 1 } \mathrm { - b e g i n } , U _ { 1 } \mathrm { - b e g i n } , p _ { m } , f .$  all dimensions, &#x27;ducer coefficients, heat at heat exchangers, gas-mixture mole fraction.</td><td>simply fixed</td><td>guess</td></tr><tr><td>Variables that DELTAEC calculates as results of each pass of integration. Includes all  $T _ { m }$   $p _ { 1 } , U _ { 1 } , \dot { H } _ { \mathrm { t o t } }$  except in BEGIN; combinations of above such as  $\dot { E }$  ,RPN results, and  $z _ { n }$  at ends.</td><td>target</td><td>simply results in &lt;.out&gt; and &lt;.sp&gt; files</td></tr></table>

To understand what variables should be regarded as known a priori by the user, it is sometimes helpful to think about what variables are (or could be, in principle) experimentally controlled, in contrast to what variables are experimentally observed. These must be compared with the variables that DELTAEC computes as results during each integration pass and those that DELTAEC needs as inputs during each integration pass through the system. Note that our definition of an experimental result is more general than usual. In the Hofler refrigerator case, we considered the drive voltage an experimental result because it is determined experimentally by the condition that the pressure amplitude have the desired value. The viewpoint expressed in Table 5.2 is appropriate for comparison of DELTAEC and experimental data. In this case, geometrical parameters are simply fixed. Targets are experimentally fixed or controlled variables that are results of a single pass of numerical integration, chosen from among $T _ { m } , p _ { 1 }$ , and $U _ { 1 }$ (everywhere but in BEGIN); current magnitudes and phases in VDUCERs and voltage magnitudes and phases in IDUCERs; etc. Guesses may be unknown parameters chosen from among $f _ { ; }$ the magnitude and phase of $U _ { \mathrm { 1 } } { \mathrm { - } } \mathrm { B E G I N }$ and $\displaystyle p _ { 1 } – \mathsf { B E G I N }$ $T _ { m } { \mathrm { - } } \mathtt { B E G I N }$ , heats at heat exchangers, the magnitude and phase of voltage at VEDUCERs, etc.

When designing hardware instead of analyzing it, a different viewpoint may be adopted. In this case, many geometrical parameters are not yet fixed, but desired operating temperatures, powers, frequency, etc. have been chosen. Often, several geometrical parameters are included as guesses, and more temperatures and other numerical results are included as targets. Hence, another useful way to think about guesses and targets is represented by Table 5.3.

Table 5.2: Interpreting input and result variables: experimental viewpoint.
<table><tr><td></td><td>Experimentally controlled variable</td><td>Experimental result</td></tr><tr><td>Variable needed as input for each pass of DELTAEC&#x27;s integration</td><td>simply fixed</td><td>guess</td></tr><tr><td>Variable computed as a result of each pass of DELTAEC&#x27;s integration</td><td>target</td><td>simply a result in &lt;.out&gt; and &lt; .sp&gt; files</td></tr></table>

Table 5.3: Interpreting input and result variables: design viewpoint.
<table><tr><td></td><td>Variable we want to think Variable we want to think of as fixed</td><td>of as a result</td></tr><tr><td>Variable needed as input for each pass of DELTAEC&#x27;s integration</td><td>simply fixed</td><td>guess</td></tr><tr><td>Variable computed as a result of each pass of DELTAEC&#x27;s integration</td><td>target</td><td>simply a result in &lt;.out&gt; and &lt;.sp&gt; files</td></tr></table>

As we did in our description of the choices of guesses and targets for the refrigerator example above, it is useful to look for targets at the end or middle of the model, then look for guesses in the beginning or middle of the model. Sometimes it is easy to mentally associate each target with a corresponding guess, as we did for some of them in the discussion above. A few targets, such as the HARDEND targets in the example above, may be utterly obvious and necessary, depending only on the model but not on the user's point of view. However, many targets depend on the user's point of view. Does the user want to consider an electrically driven refrigerator to be driven at fixed frequency, or to be kept on resonance by active control? Is the user interested in cooling power at a given cold temperature, or in the cold temperature that is reached for a given cooling load? Thus, it is essential to think carefully about what we want to think of as "known" and what we want to think of as “unknown" for every model and for every use of that model.

It is also important to remember that the overall time phase of a DELTAEC model is arbitrary, to find the one and only one location in the model where that time phase is set (usually in the BEGIN, but sometimes in a transducer or an RPN target), and to make sure there are no other conflicting time-phase input variables (multiple side-branch transducers often being problematic).

## 5.4 Meeting targets in an elaborate model

## 5.4.1 Basic rules

Guesses must precede targets: At least one guess must precede the first target; at least two guesses must precede the first two targets; etc. DELTAEC warns if this rule is violated.

Avoid a sameas or RPN that needs a downstream result, if the sameas result or RPN result affects any integration result that is compared with a target. This would confuse DELTAEC by making the targeted result depend on a result left over from the previous integration instead of only on the upstream results of the present integration. (When several sameas's and RPNs point to one another, it can be hard to see whether they are all independent of downstream results. DELTAEC should warn if this rule is violated. List Linkages, described in Section 4.3, is also useful for diagnosis.) For example, this will not work, but changing the RPN formula from 3A to 1A will fix it:

BEGIN the setup   
5.5400E+06 a Mean P Pa   
94.000 b Freq Hz   
300.00 c TBeg K   
2.9938E+05 d Ipl Pa   
-514.8 e Ph(p) deg   
1.5400E-03 f |U| m^3/s G   
125.00 g Ph(U) deg   
1.0000 j nL   
HeAr Gas type   
!-- 1   
DUCT bypass tube   
1.6417E-05 a Area m^2 6.1161E+05 A lpl Pa

![[mu_66afccee_6e91eedfc5ee4a3bb557.jpg]]

## 5.4.2 Developing a substantially new model

Occasionally the user can create a completely new model, establish several targets and guesses, hit the blue run button, and enjoy instant success. However, it is much more common to find that this approach yields no more than a message from DELTAEC explaining that it has failed to meet targets. Several strategies can be used to overcome this situation:

Understand approximately what to expect from your model before you even begin working with DELTAEC, so you can provide reasonable initial estimates for guesses. For example, use your knowledge of acoustics to make reasonable initial estimates of values for TBRANCH impedances to give DELTAEC a plausible starting point.

Proofread your model carefully. One of the most common problems in DELTAEC models is an order-of-magnitude typographical error in an input variable. Use the schematic view for a quick check of dimensions.

clear all guesses and targets, then run the model and examine the results for approximate sanity. Or use Run with Fixed Guesses (Alt-R) (Better yet, do this sanity check before you establish any guesses and targets in the first place.) If you see a result that is wildly unrealistic, such as a temperature of 10,000 Kelvin, modify something upstream to fix it, so DELTAEC's shooting-method algorithm begins in the correct ballpark.

Even though you may have chosen guesses and targets by thinking about the end of the model first, introduce the guesses and targets starting near the beginning, one target and one guess at a time. To be sure that your first guess will be a suitable partner for your first target, think about the physics of cause and effect. Modify the candidate guess's value by hand before you establish it as a guess, running to confirm that changing the candidate guess has a significant effect on the intended target. Then add that guess and target, run, and confirm that the target is met. If successful, repeat this process to add the next candidate guess and target.

Save your model frequently, so you can backtrack if things go awry. You can save a file with any filename extension, and we frequently find ourselves naming saved files to indicate the order they are created, e.g., <bottle01.out>, <bottle02.out>, <bottle03.out>, or to indicate what they represent to us, e.g., <bottle1targ.out>, <bottle2targs.out>, etc. We keep notes to show what each saved file represents.

As the number of guesses and targets increases, DELTAEC's shooting method has more and more work to do. Be kind. Before adding the Nth target and guess, modify the candidate guess by hand to make the intended target variable very close to the desired value before asking DELTAEC to take over responsibility for that target and guess.

If an overly bold change has gotten DELTAEC lost, use Restore all guessez, described in Section 5.7, to recover the previous set of guesses.

If DELTAEC seems to be missing targets by only a little, reduce the convergence tolerance or adjust one of the other shooting-method tuneup parameters, which are accessible through the Edit pulldown menu as Options, described in Section 8.3.2.

Consider whether the number of guesses and targets could be reduced by beginning at the \*\*END and ending at the BEGINning. If so, "flip" the model as described in Section 5.7.

Consider other ways to reduce the number of guesses and targets. For example use vSPEAKER instead of VESPEAKER if possible. Or avoid a transducer by using a nonzero $U _ { 1 }$ in BEGIN.

Change the guess-list membership, if you can think of an appropriate alternative to one or more existing guesses.

In a model with a STK\*\* segment, it is common for a heat upstream of that segment to be a guess, corresponding to a temperature target downstream of that segment. With regenerators, pulse tubes, and thermal buffer tubes, small changes in the guessed heat tend to cause large changes in the downstream temperature while the shooting method is exploring the landscape. If long DuCTs or other temperature-sensitive segments are downstream of the temperature-target segment, any targets downstream of the long segments can be wildly affected by the shooting method's exploratory changes in the heat guess. Shooting-method stability can be improved in such cases by putting an RPN segment that fixes the temperature $\left( \mathrm { e . g . , ~ } ^ { \cdot \cdot } 3 0 0 ~ = \mathrm { T m } ^ { ; \cdot } \right)$ immediately upstream of the long segment(s)

If convergence seems strangely problematical, consider changing the relative importance of different targets. If some targets (such as heat-exchanger temperatures) are aimed at a nonzero number while others (such as \*\*END impedance) are aimed at zero, DELTAEC sometimes has trouble deciding how close is close enough. The relative weight can be changed via the Normalization Mode parameter described in Section 8.3.2, but it is sometimes more productive to change the weight of an individual target by incorporating it into an RPN segment that is aimed at zero and multiplying (or dividing) the calculated target result by a large number to emphasize (or deemphasize) it; or adding 1 to what would otherwise be a zero target, to de-emphasize it.

If convergence seems strangely problematical, also consider whether some guesses might essentially have large fixed offsets. The shooting method begins by calculating the sensitivities of the results to changes in the guesses by changing each guess by a fixed percentage (described in Section 8.3.2). If a part-per-million change in one guess causes part-per-million changes in targeted results, but a part-per-million change in a second guess causes an order of magnitude change in one or more targeted results, the shooting method will fail. In such cases, it helps to use an RPN input parameter as a small guess, add a large offset to it in the RPN's line b to make a number that's the size of the original guess, and sameas the original guess to the RPN result. This will ensure that ppm changes in all guesses cause ppm changes in all targeted results.

A feature introduced in DELTAEC version 6.4b8 might assist users with the strategies of this subsection and the next. Clearing all Guesses and Targets enables a “Reactivate" button in the guess-target summary, which launches another dialog, which in turn has an “Analyze" button. The “Analyze" button produces a logarithmic table of sensitivities of each recently cleared target to ±10 ppm changes of each recently cleared guess. Look for sensitivities near 1, which indicate direct control: a 10 ppm change in one of the potential guesses causes $\mathrm { a \simeq 1 0 }$ ppm change is the corresponding target. A much smaller number indicates negligible leverage of a potential guess on a potential target; a much large number can occur when the leverage is too strong, such as the way a heat guess upstream of a STK\*\* segment affects temperature and hence sound speed of every downstream segment in a model. “Nil" indicates zero leverage, often because that guess is downstream of that target. “ZerCr" indicates a zero crossing: The potential target's sign is different for +10 ppm and -10 ppm changes of the potential guess, which is a good situation for a target that will be set to zero. (Note that "0" indicates a sensitivity $e \simeq 2 . 7$ times weaker than “1", not zero sensitivity.) As advised above, look for upstream candidates for reactivation first, and look for upstream heat guesses that can target a downstream temperature. After reactivating one guess and one target, run the model again, and repeat the analysis for the remaining recently cleared guesses and targets.

## 5.4.3 Modifying an existing model

Purely acoustic models with only a few guesses and targets, like the bottle in Chapter 2, are usually robust: From a state with all targets met, the user can often change any variable by a factor of two or so, and DELTAEC's shooting method will once again hit the targets. However, DELTAEC's shooting method gets lost more easily for thermoacoustic models with more than about five targets and five guesses, especially with STKDuCT and STKCoNE segments. Some strategies for successful routine modifications of complex models, starting from a state in which targets are met, include:

If an overly bold change has gotten DELTAEC lost, use Restore all guessez, described in Section 5.7, to recover the previous set of guesses. Then use Run with Fixed Guesses (Alt-R), trying to understand what went wrong either by inspecting the target block in the guess-target summary or scrolling through the model and to see where results first become unreasonable.

If an overly bold change has gotten DELTAEC lost, use Restore all guessez to recover the previous set of guesses. Then use the incremental plot feature to change a variable by small steps. (In this use of incremental plotting, there is no need for any dependent plot variables.) In practice, this usually means: Observe that a big change led to failure to converge; Restore guessez and un-do the big change manually to return to the secure starting condition; Try a smaller change (such as 1/10 of the original change); If the smaller change still leads to failure to converge, then restore and undo again, and try an even smaller change; When a small-enough change has been found, use that change as the step in the incremental plot feature to let DELTAEC accomplish the desired big change in 10, 100, or more small steps. (If DELTAEC gets part way through these small steps and then loses its ability to hit targets, use the plot rewind feature, described in Section 3.2.3, to recover a meaningful operating point that is at least part way toward the desired change.)

Insert a new segment gradually, by first inserting it with near-zero volume and near-zero impedance, then gradually increasing these with the incremental plot feature. Often this entails inserting a new segment with near-zero length and gradually increasing the length. Similarly, the heat of a new heat exchanger can be increased gradually from zero; the impedance of a new side-branch impedance can be reduced gradually from a very large value; the impedance of a series impedance can be increased gradually from zero.

Kill an undesired segment gradually by reducing its length with the incremental plot feature before Killing it.

Save your model frequently, so you can recover from the unexpected.

The shooting method within DELTAEC can sometimes get stuck around an inappropriate local minimum. Try manually changing one of the guesses slightly and see if DELTAEC will loose its fondness for this particular sticky point.

Always check results carefully for reasonableness, particularly when modeling complicated systems or using any of DELTAEC's more elaborate features. While DELTAEC is a useful tool, it is far from foolproof—for example, the shooting method can easily end up generating devices that are several wavelengths long or wander into the completely unrealistic realm of negative values for guessed frequency or length.

## 5.5 Standing-wave engine

This standing-wave-engine example is described in detail in Ref. [23]. The device described there is used here to illustrate the thermoacoustic capabilities of DELTAEC in the context of an engine. We will reproduce some of the figures in that paper here.

The apparatus is shown in Fig. 5.6. After running the file <5inch.out>, the result is:

![[mu_66afccee_6d84254d9395e6160b27.jpg]]  
Figure 5.6: Five-inch-diameter standing-wave engine.

```csv
TITLE Five-Inch Thermoacoustic Engine
!Created@16:20:53 27-Jun-2020 with DeltaEC version 6.4b2.8!under win32.
!- 0
BEGIN Initial
1.3800E+6 a Mean P Pa
121.15 b Freq Hz G
556.89 c TBeg K G
7.3502E+4 d Ipl Pa G
0.0000 e Ph(p) deg
0.0000 f |UI m^3/s
0.0000 g Ph(U) deg
helium Gas type
!- 1
SURFACE Hot End
1.2920E-2 a Area m^2 7.3502E+4 AIpl Pa
0.0000 B Ph(p) deg
4.7330E-5 C |UI m^3/s
-135.0 D Ph(U) deg
0.0000 E Htot W
ideal Solid type -1.230 F Edot W
2
DUCT Hot Duct
sameas 1a a Area m^2 7.2637E+4 Alpl Pa
0.4030 b Perim m 5.5412E-3 B Ph(p) deg
0.2790 c Length m 8.7666E-2 C |UI m^3/s
-90.21 D Ph(U) deg
0.0000 E Htot W
ideal Solid type -11.953 Edot W
!- 3
HX Hot HX
sameas 1a a Area m^2 7.1468E+4 Ipl Pa
0.3930 b GasA/A 0.39052 B Ph(p) deg
6.0000E-2 c Length m 9.6743E-2 C |UI m^3/s
4.8300E-4 dy0 m -91.205 D Ph(U) deg
2210.0 e HeatIn W 2210.0 E Htot W
999.00 f SolidT K -96.25 F Edot W
556.89 G GasT K
ideal Solid type 562.74 H SolidT K
!- 4
STKCIRC Honey Stack
sameas 1a a Area m^2 6.5648E+4 AIpl Pa
0.8100 b GasA/A 2.7637 BPh(p) deg
0.2790 c Length m 0.15967 C IUI m^3/s
5.0000E-4 d radius m -85.361 D Ph(U) deg
5.0000E-5 e Lplate m 2210.0 E Htot W
171.54 F Edot W
556.89 G TBeg K
stainless Solid type 306.34 H TEnd K
!-- 5
HX Ambient HX
1.2670E-2 a Area m^2 6.3033E+4 AIpl Pa
0.4860 b GasA/A 3.2621 B Ph(p) deg
5.0800E-2 c Length m 0.16734 C |U| m^3/s
4.0600E-4 dy0 m -85.811 D Ph(U) deg
-2124.7 e HeatIn W G 85.290 E Htot W
```

![[mu_66afccee_b79ba040337601821586.jpg]]

```csv
303.00 f SolidT K =5H 85.290 F Edot W
306.34 G GasT K
ideal Solid type 303.00 H SolidT K
!- 6
ANCHOR subsequent duct is water jacketed
! – 7
DUCT Ambient Duct
sameas 5a a Area m^2 6.9592E+4 AIpl Pa
0.3990 b Perim m -176.57 B Ph(p) deg
3.6500 c Length m 2.6516E-5 C |U| m^3/s
-131.57 D Ph(U) deg
0.6524 E Htot W
ideal Solid type 0.6524 F Edot W
8
SURFACE Ambient End
sameas 5a a Area m^2 6.9592E+4 AIpl Pa
-176.57 B Ph(p) deg
1.0573E-16 C |U| m^3/s
104.61 D Ph(U) deg
7.1327E-13 E Htot W
ideal Solid type 7.1327E-13 F Edot W
!- 9
HARDEND target this to seal the end
0.0000 a R(1/z) =9G 6.9592E+4 AIpl Pa
0.0000 b I(1/z) =9H -176.57 B Ph(p) deg
1.0573E-16 C |U| m^3/s
104.61 D Ph(U) deg
7.1327E-13 E Htot W
7.1327E-13 F Edot W
5.1922E-17 G R(1/z)
-2.6273E-16 H I(1/z)
10
RPN ensure all ambient-duct dissipation goes to water jacket
0.0000 a =A? 5.6843E-14 A ChngeMe
5E 5F -
```

Examining the guess-target summary, we find
<table><tr><td>GUESS</td><td>Ob</td><td>0c</td><td>0d</td><td>5e</td></tr><tr><td>name</td><td>BEGIN:Freq</td><td>BEGIN:TBeg</td><td>BEGIN: lpl</td><td>HX:HeatI</td></tr><tr><td>units</td><td>Hz</td><td>K</td><td>Pa</td><td>W</td></tr><tr><td>value</td><td>121.15</td><td>556.89</td><td>7.3502E+04-2124.7</td><td></td></tr><tr><td>TARGET</td><td>5f</td><td>9a</td><td>9b</td><td>10a</td></tr><tr><td>name</td><td></td><td>HX:Est-T HARDE:R(1/z HARDE:I(1/z</td><td></td><td>RPN:Targe</td></tr><tr><td>units</td><td>K</td><td></td><td></td><td></td></tr><tr><td>value</td><td>303.00</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>result</td><td>303.00</td><td></td><td></td><td>1.3878E-17-4.3970E-16-5.6843E-14</td></tr></table>

and some <.sp> graphs show the wave, power, and temperature profiles in Fig. 5.7.

Targets 9a and 9b, the real and imaginary parts of $1 / z _ { n }$ , are of course necessary to impose $U _ { 1 } = 0$ at the closed ambient end of the resonator. Our choices of other targets and guesses were made to reflect the perspective of Ref. [23], in which the as-built hardware was driven by a fixed heat input (ordinary input 3e) and the ambient heat exchanger was held at fixed temperature (target 5f). Frequency 0b is a guess, because we want DELTAEC to tell us the frequency at which it thinks the system should spontaneously oscillate. Initial temperature 0c and initial pressure amplitude 0d are also guesses, because we want DELTAEC to tell us the hot temperature and the pressure amplitude at which it thinks the system should oscillate for the given hot heat input. The final target and guess, 10a and 5e, allow DELTAEC to tell us the heat rejected at the ambient temperature, under the constraint that $\dot { E } = \dot { H } _ { \mathrm { t o t } }$ at the interface between the ambient heat exchanger and the long ambient resonator duct. We judge this to be a reasonable energy-closure condition for the model because the resonator duct was water-cooled in this apparatus, so the heat arising from $\dot { E }$ dissipated in it might be expected to be carried away locally by water. (This is of course not strictly true; boundary-layer thermoacoustic processes redistribute energy along x, as was dramatically demonstrated in Ref. [24] long ago.) Consistent with this energy-closure condition, the ANCHOR segment just before the final DUCT overrides the default behavior of the subsequent segments (thermally insulated, except in heat exchangers), ensuring that $\dot { H } _ { \mathrm { 2 , k } } = \dot { E }$ thereafter.

![[mu_66afccee_70afbe0cf97c3f946e4e.jpg]]  
Figure 5.7: Graphs of the wave (left), total power and acoustic power (top right), and temperature (bottom right) as functions of x in <5inch.out>. Changing temperature and constant $\dot { H } _ { \mathrm { t o t } }$ show the location of the stack. The heat exchanger locations are indicated by the steep changes in $\dot { H } _ { \mathrm { t o t } }$

Other choices could be made for the guesses and targets. For instance, the cold-duct length could be substituted for the frequency as one of the guesses, if we were designing an apparatus to operate at a desired frequency. The hot-heat-exchanger temperature 3f could be added to the target list and, simultaneously, the hot-heat-exchanger heat 3e could be added to the guess list, if we were designing an apparatus to operate at a desired hot temperature. For now, however, the guesses and targets will be left as they are, since they reflect the point of view adopted in Ref. [23].

To plot some results for this 5-inch engine case, we started DELTAEC with this file again and prepared parameters so the plot summary became

Dependent Variables (outputs):   
PLOTS OA OB OC OD 3H 8A   
name BEGIN:Freq BEGIN:TBeg BEGIN:IpI BEGIN:HeatI HX:Solid HARDE:lpl   
units Hz K Pa W K Pa   
Independent Variables (inputs):   
Outer loop: 3e HX:HeatI Beg= 9.50E+02 End= 50. Step= -33.

by adding 3H and 8A to the dependent-plot-variable list and establishing 3e as an independent plot variable, setting its initial, final, and step values. (Some other variables such as TBeg are of minor interest now, but cannot be deleted from the list of plot variables because guesses appear here by default.)

Next, we modified mean pressure to be 19.2 bar, and ran the code. When completed, we modified mean pressure to 13.8 bar, and ran it again, appending the new results to the <.ip> file. Three more runs with mean pressures of 9.6, 6.9, and 5.2 bar completed the data set. We exited from DELTAEC, and read the <.ip> file into a spreadsheet/graphics program for a little massaging: converting pressure amplitude at the cold end from Pascals to bar, and then squaring that number; subtracting 303 Kelvin from $T _ { H }$ , and adding the measured heat leak to the room to $\dot { Q } _ { H }$ . Plotting these results then yields the curves shown in Fig. 5.8, resembling Figs. 5, 6, and 7 in Ref. [23]. These curves differ slightly from those in the reference, because of DELTAEC's inclusion of the small gas-to-solid temperature differences in the heat exchangers.

![[mu_66afccee_85e3bc5706b02bfddbd1.jpg]]  
Figure 5.8: Standing-wave engine results. Lines are DELTAEC results; points are from experimental data in Ref. [23].

More detailed comparison between DELTAEC computations and measurements with this apparatus can be found in Ref. [25]. The agreement is excellent at low amplitude, but disagreement grows large at high amplitude—typical of our experience with standing-wave engines up to $\left| p _ { 1 } \right| / p _ { m } \simeq 0 . 1$ . See Section 9.2.5 for details about such disagreement.

![[mu_66afccee_17899f73149e6c4fea88.jpg]]  
Figure 5.9: More thermoacoustic segments: stacks, regenerators, and heat exchangers.

## 5.6 More thermoacoustic segments

In this section we list thermal segments that are commonly used for engines and refrigerators: the several types of heat exchangers, stacks, and regenerators. More details on each can be found in Chapter 10 and Chapter 11.

STKCIRC A stack or regenerator with circular pores. We also use this to model hexagonal honeycomb stacks.

STKSLAB A stack or regenerator with parallel-plate geometry.

STKRECT A stack or regenerator with rectangular (or square) pore geometry.

STKPIN A stack or regenerator comprised of an array of pins aligned parallel to x.

STKDUCT A “stack" with lateral dimensions much larger than $\delta _ { \kappa }$ , computed in boundarylayer approximation. (Used for pulse tubes and thermal buffer tubes.)

STKCoNE A tapered “stack" with lateral dimensions much larger than $\delta _ { \kappa } .$ computed in boundary-layer approximation. (Used for pulse tubes and thermal buffer tubes.)

STKSCREEN A screen regenerator for Stirling systems.

STKPOwERLW A porous medium with friction factor and heat-transfer coefficient specified as power-law functions of Reynolds number.

HX A parallel-plate heat exchanger.

TX Tube-array heat exchanger, with the thermoacoustic working gas inside the tubes.

SX Stacked-screen heat exchangers, valid only for $\delta _ { \kappa }$ greater than hydraulic radius.

PX Power-law heat exchangers, with friction factor and heat-transfer coefficient characterized by power laws in Reynolds number.

VXT1 and VXT2 Heat exchangers with fixed solid temperature, in which gas temperature can vary with x.

VXQ1 and VXQ2 Heat exchangers with fixed heat per unit length, in which gas temperature can vary with x.

ANCHOR This segment overrides what would otherwise be default thermal-insulation mode in subsequent DUCTs, CONEs, COMPLIANCEs, IMPEDANCEs, SURFACEs, etc., so DELTAEC treats those segments as if they are immersed in a thermal bath at $T = T _ { m }$

INSULATE This segment is used to re-establish the default thermal-insulation condition if it was previously overridden by ANCHOR.

## 5.7 More user-interface features

These options offer substantial power and convenience for experienced users.

Restore all guessez. Before beginning iterations during a run, DELTAEC saves copies of the guess values. It also saves copies of a few output parameters if it caught the user inadvertently or boldly using a sameas or RPN pointer to an output parameter in a segment downstream of that sameas or RPN, despite DELTAEC's “Forward Reference Condition" warning about the unstable shooting-method behavior that can result from using such downstream results. (See Section 5.4 for an explanation of this danger.) Whenever an unsuccessful run overwrites the guesses (leaving you and DELTAEC lost), you can use this option to restore all of these variables to their earlier values. Simply Restore guessez, then modify one or more variables yourself (e.g., returning anything you recently changed to earlier, more successful values), and try again.

Comment lines. If the heading on the first line of a segment does not provide enough space for the user's notes, additional comment lines can be added below it. Examples are shown at the beginning of the next section, Section 5.8.1.

Split segment. This option, available by right clicking on the top line of a segment or in the Edit pulldown menu, automates the process of splitting any segment with length (e.g., a DUCT, CONE, or STK\*\*) into two segments, each having half of the original length, correcting the sameas and RPN references everywhere in the model, and correcting the guess, target, and plot lists. (To partition the lengths unequally while keeping the correct total length, you can use master-slave linking (Section 2.7.2) after splitting a segment in equal halves: slave the first length to the second, then modify the first length, then clear the length link to allow the two pieces to be modified independently.)

AutoLayout. Sometimes auxiliary windows such as plots and the highlight display become lost off the edge of the computer's screen. (For example, undocking a laptop from a larger screen can cause this.) The AutoLayout option, available in the Display pulldown menu, brings all of DELTAEC's auxiliary displays close to DELTAEC itself. (If this fails for a plot, close it, delete the associated <.ssv. \*> or <.isv.\*> files from your model's folder, and try again.)

Flip a block of segments. The number of guesses and targets can sometimes be reduced by beginning the integration of a model from what you had previously considered the “end." Orifice pulse-tube refrigerators (described in Section 5.8) are a particularly good example because we naturally think of them as beginning at the driver, but they “end" with an accurately known impedance in the COMPLIANCE tank, while the driver impedance is usually less well known; BEGINning in the tank can often reduce the number of guesses and targets. Similarly, shooting-method stability can sometimes be improved by putting regenerators upstream of thermal buffer tubes, instead of the other way around. The “Flip Selected Segs" operation automates switching back and forth between these two directions of integration, simplifying an otherwise very tedious and error-prone process. Highlight a block of segments, such as an entire model or the segments between a TBRANCH and its SOFTEND, and right-click to access the "Flip Selected Segs" feature. Flipping reverses the order of the physical segments in the block, and interchanges parameters such as AreaI and AreaF within unsymmetrical segments such as CONEs. DELTAEC tries to relocate any RPN segments intelligently in the block, but sometimes gives up and puts them at the end of the block. “Flip Selected Segs" takes care of sameas pointers, RPN-segment pointers, and plot references, and preserves the guess and target lists. Always proofread very carefully after flipping; in complicated models there is always something that DELTAE handles incorrectly, and intelligent human intervention will be needed to fix things like TBRANCH impedances feeding into flipped segment blocks and targets getting moved upstream of the corresponding guesses.

## 5.8 Stirling and pulse-tube refrigerators

Rott's equations implemented in DELTAEC are valid for any phase difference between $p _ { 1 }$ and $U _ { 1 }$ , and any degree of thermal contact in the “stack." Hence, DELTAEC can be used to model Stirling thermodynamic systems, in which $p _ { 1 }$ and $U _ { 1 }$ are substantially in phase, as well as standing-wave thermoacoustic devices, in which the phases $p _ { 1 }$ and $U _ { 1 }$ differ by nearly $9 0 ^ { \circ }$ as described in Sections 5.2 and 5.5. The principal additional DELTAEC segment that is often needed for Stirling systems is one for stacked screen beds, STKSCREEN, because stackedscreen regenerators are more common than parallel-plate, circular-pore, or rectangular-pore regenerators in Stirling systems. In our opinion, the principal shortcomings of DELTAEC for Stirling applications are DELTAEC's acoustic approximation (which leads to reduced accuracy at high pressure amplitudes) and its inability to predict two-dimensional effects and streaming-driven convective heat transport in pulse tubes (shortcomings shared by many other design programs). DELTAEC's main virtues are speed and easy inclusion of some auxiliary components such as ducts, dead volumes, and linear motors in the model.

Harmonic analysis of Stirling systems is introduced by I. Urieli and D. M. Berchowitz in Ref. [26] and by A. J. Organ in Ref. [27].

## 5.8.1 Alpha Stirling cryocooler

The example file <Stirling.out> represents a simple 55-Hz, 2-MPa helium Stirling cryocooler with stacked-screen regenerator and heat exchangers. This apparatus is illustrated in Fig. 5.10. (It does not resemble any real cryocooler known to us; we created it only to illustrate DELTAEC's capabilities.) First, we examine <Stirling.out>:

![[mu_66afccee_f7726b186b85d04dcbc3.jpg]]  
Figure 5.10: A Stirling cryocooler.

![[mu_66afccee_d409489088ffdc3fb260.jpg]]

The physical segments consist of a first heat exchanger, at 300 K, the regenerator, and a second heat exchanger at 80 K. All three are stacked screens. The other segments—BEGIN and the RPNs—define the end conditions.

The hydraulic radius $r _ { h }$ and volumetric porosity $\phi$ for the screens can be calculated from

![[mu_66afccee_92daa8468fcceae17533.jpg]]  
Figure 5.11: Total power (solid black) and acoustic power (dashed blue) vs position in the Stirling cryocooler example. The total power $\dot { H } _ { \mathrm { t o t } }$ is constant and small in the regenerator, and changes in the heat exchangers

the screen manufacturer's specs, using expressions from Ref. [27]:

$$
\phi ~ \simeq ~ 1 - \frac { \pi m d } { 4 } ,\tag{5.14}
$$

$$
r _ { h } = \frac { d } { 4 } \frac { \phi } { 1 - \phi } ,\tag{5.15}
$$

where d is wire diameter and m is mesh number (i.e., number of wires per unit length). The second equation results from the conventional definition of hydraulic radius: Gas volume divided by gas-solid interface area. This regenerator is a little over 1 cm in diameter and is 5 cm long. The heat exchangers are the same diameter but only 1 mm long.

DELTAEC estimates the temperature difference between the helium gas and the copper screen wires in the heat exchangers, but it has no provision for estimating the temperature difference between the screen wires and the “housing" in which they are mounted (a temperature difference caused by the finite thermal conductance of the screen wires themselves). This is not a serious concern for small machines, but should be checked by hand on a case-by-case basis.

Line e in the regenerator segment, "ksFrac," is the fudge factor by which longitudinal conduction through the regenerator is adjusted due to the spatially intermittent thermal contact between adjacent screens and due to the conduction of the pressure-vessel wall. Following Ref. [28], we often set ksFrac somewhere between 0.1 and 0.3, the lower end of the range being appropriate if the conduction of the pressure-vessel wall is negligible and the screens are metal.

Our point of view with respect to boundary conditions in this example is most easily displayed by running DELTAEC on this file and examining the guess-target summary,

<table><tr><td>units value</td><td>K 300.14</td><td>Pa 2.8505E+05</td><td>deg -43.141</td><td>W -35.912</td><td>W 5.0262</td></tr><tr><td>TARGET name</td><td>1f SX:Est-T</td><td>3f SX:Est-T</td><td>4a RPN:Targe</td><td>5a RPN:Targe</td><td>6a RPN:Targe</td></tr><tr><td>units</td><td>K</td><td>K</td><td></td><td></td><td></td></tr><tr><td>value</td><td>300.00</td><td>80.000</td><td>0.0000</td><td>6.2000E-05</td><td>-52.000</td></tr><tr><td>result</td><td>300.00</td><td>80.000</td><td>-2.2675E-12</td><td>6.2000E-05</td><td>-52.000</td></tr></table>

and the BEGIN segment. We are considering the complex volume flow rates at the two ends to be given, as if we have in mind an “alpha" Stirling machine, with the motions of the two pistons determining the volumes of the compression and expansion spaces. The volume flow rate at the hot end is set by lines 0f and 0g in the BEGIN segment. The $0 ^ { \circ }$ phase of line 0g essentially determines the zero of phase for the entire system. The volume flow rate $3 . 6 5 \times 1 0 ^ { - 4 } ~ \mathrm { m ^ { 3 } / s }$ of line 0f (together with the frequency set in line 0b) implies a volumetric stroke of 2.1 $\mathrm { c m ^ { 3 } }$ peak-to-peak at the hot end. The RPNs at the cold end ensure that DELTAEC's shooting method arrives there with the desired cold piston stroke and phase. To arrive at these two targets, DELTAEC adjusts two guesses: the pressure amplitude and phase in the BEGIN segment (and hence throughout the cooler). We also insist that the solid temperatures in the two heat exchangers be 300 K and 80 K; DELTAEC achieves these two targets by adjusting two more guesses: the heat extracted at the hot heat exchanger, and the temperature in the BEGIN segment. We also insist that the acoustic power and total power leaving the cold heat exchanger are equal, implying that the cold piston is thermally insulated. (Acoustic power and total power are also equal at the ambient piston, because the BEGIN segment assigns $\dot { H } _ { 2 , k } = \dot { E }$ by default.)

DELTAEC predicts that, under these circumstances, the cooler will reject 36 W at the hot heat exchanger and will have a cooling power of 5 W. This cooling power accounts for heat conduction and enthalpy flow through the regenerator, but does not account for any heat load imposed by frictional irreversibilities in the cold piston, nor any heat load imposed by the regenerator case conduction except to the extent that it is included in ksFrac.

We now make or suggest a few simple modifications to this file to illustrate additional features of DELTAEC.

To discover what temperature the cooler would maintain with a heat load of 10 W instead of 5 W, we remove 3f—the cold heat exchanger temperature—from the target list, and we remove 3e—the cooling power—from the guess list, and modify it to 10 W. Running DELTAEC shows that the shooting method is lost with such a dramatic change, so we Restore guessez, modify 3e back to 5 W, and use an incremental plot of 3e from 5 W to 10 W, step 0.2 W, to reach the desired heat load. Under these circumstances the cold temperature will be 232 K.

Using 3e as an independent plot variable running from 10 W to 2 W with steps of, say, 0.2 W, and using 3H (cold solid temperature) as a dependent plot variable will generate a table and plot of cold temperature (and other defaults) vs heat load.

Insertion of two \*ESPEAKER segments, before the aftercooler and after the cold heat exchanger, would model use of linear motors and pistons there.

In the next subsection, we will use TBRANCH and UNION to change this model from an "alpha" Stirling machine to a "beta" or “gamma" machine, with one power piston on the hot end and a displacer piston in parallel with the heat exchange elements.

![[mu_66afccee_8d174a6f8975595da4fd.jpg]]  
Figure 5.12: “Gamma"-style Stirling machine.

## 5.8.2 Beta or gamma cryocooler

The use of TBRANCH and UNION for hardware with branches and loops was introduced in Section 2.7.5. Recall the method of computation: At a TBRANCH, the branch impedance determines how the (complex) volume flow rate splits up; volume flow rates are added at the UNION. In purely acoustic models, the complex branch impedance is most often used as a pair of guesses that DELTAEC adjusts in its usual way to get the complex pressure at the SOFTEND of the TBRANCH to come out to be the same as it is at the UNION. In models with thermoacoustic components, a third guess-target pair is also employed: The fraction of the energy flow $\dot { H } _ { \mathrm { t o t } }$ going down the TBRANCH is guessed, and the temperature at the SOFTEND of the TBRANCH is targeted to equal the temperature at the UNION. Models with TBRANCHs and UNIONs tend to have many guesses and targets, since every SOFTEND and UNION contributes two or three targets (and a few more targets are almost always needed for temperatures, heats, etc.). Keep in mind that UNION targets differ from the usual RPN, \*\*END and heat-exchanger-temperature targets because their actual values are not specified by the user—they vary from one integration to the next, depending on what is happening at the associated sOFTEND segment, as the shooting method varies the guesses.

As an example of use of TBRANCH and UNION in a thermoacoustic setting, we return to the Stirling cryocooler example above, and convert it to a "displacer"-style [26] Stirling machine, with a compressor piston at the hot end and a driven displacer piston connecting the hot and cold ends. In the previous example, PU power (i.e., E in DELTAEC vocabulary) flowed in at the BEGIN and out at the end; no explicit segments indicated the pistons there. Here, with a displacer piston, the cold-end PU power is returned automatically to the hot end, reducing the hot-end PU power requirement.

The apparatus layout is illustrated in Fig. 5.12. The corresponding display of segment headings in <gamma.out> is

O BEGIN:G P Initialize things   
1 COMPLIANCE: space around power-piston motor   
2 IESPEAKER: the power piston   
3 COMPLIANCE: a little space in front of the power piston   
4 TBRANCH:G branch to displacer   
5 IESPEAKER: a spring-mounted, driven moving mass   
6 RPN:G reassign Tm (Displacer is "axially insulating.")   
7 COMPLIANCE: a little volume for the connection   
8 SOFTEND: reconnect at UNION

9 SX :GT aftercooler   
10 STKSCREEN: regenerator   
11 SX :GT cold heat exch   
12 UNION: T displacer cold end   
13 HARDE: T close the end   
14 RPN : T simulate insulation in the displacer piston

and the guess-target summary is the largest we have yet encountered in the Users Guide:
<table><tr><td rowspan="2">GUESS</td><td rowspan="2">0c</td><td rowspan="2">0d</td><td rowspan="2">0e</td><td rowspan="2">4a</td><td rowspan="2">4b</td><td rowspan="2">4c</td><td rowspan="2">6a</td><td rowspan="2">9e</td><td rowspan="2">11e SX:HeatI</td></tr><tr><td>BEGIN:Ph(p) TBRAN:Re(Zb TBRAN:Im(Zb TBRAN:HtotB RPN:Guess</td></tr><tr><td>name BEGIN:TBeg BEGIN: lpl</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SX:HeatI</td><td></td></tr><tr><td>units</td><td>K</td><td>Pa 6316.9</td><td>deg</td><td>Pa-s/m^3</td><td>Pa-s/m^3</td><td>W</td><td></td><td>W</td><td>W</td></tr><tr><td>value TARGET</td><td>300.21</td><td></td><td>114.69</td><td>-2.9921E+09-3.2892E+09</td><td></td><td>-6.7503</td><td>79.964</td><td>-45.213</td><td>4.5878</td></tr><tr><td>name</td><td>9f SX:Est-T</td><td>11f</td><td>12b</td><td>12c</td><td>12d</td><td>13a</td><td>13b</td><td>13c</td><td>14a</td></tr><tr><td>units</td><td>K</td><td>K</td><td>SX:Est-T UNION:IpISO UNION:Ph(p) UNION:Tm</td><td></td><td>K</td><td>HARDE:R(1/z HARDE:I(1/z HARDE:Htot</td><td></td><td></td><td>RPN:Targe</td></tr><tr><td>value</td><td>300.00</td><td>80.000</td><td>Pa</td><td>deg -44.127</td><td>79.962</td><td></td><td></td><td>W</td><td></td></tr><tr><td>result 300.00</td><td></td><td></td><td>2.5375E+05 2.5375E+05</td><td>-44.127</td><td>79.962</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td></td><td></td><td>80.000</td><td></td><td></td><td></td><td>8.9507E-14</td><td></td><td></td><td>2.8896E-13-2.499E-11-4.838E-11</td></tr></table>

One can think of these guesses and targets as paired up in the following way. The TBeg guess lets DELTAEC hit the T-ambient target. (These two are so nearly equal, and so trivially related, that they could easily be omitted.) The two branch-impedance guesses let DELTAEC reach the two $p _ { 1 }$ targets at the UNION. The branch-Htot guess lets DELTAEC hit the RPN target at segment 13, which enforces thermal insulation on the cold end of the displacer piston. The temperature-reassignment guess, which lets us imagine the displacer piston to be axially insulating, trivially targets the UNION temperature. The heat removed at the hot heat exchanger lets DELTAEC reach the target temperature at the cold heat exchanger. Finally, the two $p _ { 1 }$ guesses in the BEGIN segment and the heat in the cold heat exchanger allow DELTAEC to achieve $U _ { 1 } = 0$ and $\dot { H } _ { \mathrm { t o t } } = 0$ at the HARDEND at the end of the apparatus.

The corresponding <. out> file is

![[mu_66afccee_fcb463d11e92b1601a09.jpg]]

<table><tr><td>ideal !--</td><td>Solid type</td><td>-39.82 3</td><td>L Ph(Px)</td><td>deg</td></tr><tr><td rowspan="10">1.0000E-3 a SurfAr m^2 2.0000E-6 b Volume m^3</td><td rowspan="10"></td><td>2.9241E+5 -39.288</td><td>AIpl B Ph(p)</td><td>Pa deg</td></tr><tr><td></td><td></td><td></td></tr><tr><td>2.7596E-4</td><td>C |UI</td><td>m^3/s</td></tr><tr><td>18.368</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td>E Htot</td><td>W</td></tr><tr><td></td><td>F Edot</td><td>W</td></tr><tr><td>21.586</td><td></td><td></td></tr><tr><td>4</td><td></td><td></td></tr><tr><td>branch to displacer</td><td>2.9241E+5</td><td>Pa</td></tr><tr><td>Pa-s/m^3 G Pa-s/m^3 G</td><td></td><td>Alpl B Ph(p)</td></tr><tr><td>-6.7503</td><td>c HtotBr W G</td><td>-39.288 6.5763E-5 93.004 -6.7503</td><td>C |UI D Ph(U)</td></tr><tr><td></td><td></td><td></td><td>E HtotBr W EdotBr W</td></tr><tr><td></td><td></td><td>-6.4699</td><td>F G EdotTr W</td></tr><tr><td>IESPEAKER</td><td></td><td>28.056</td><td></td></tr><tr><td>5.0000E-5</td><td>a spring-mounted, driven moving mass</td><td></td><td></td></tr><tr><td></td><td>m^2</td><td></td><td></td></tr><tr><td></td><td>a Area</td><td></td><td></td></tr><tr><td>0.5000</td><td>b R ohms</td><td>2.5369E+5</td><td>AIpl</td></tr><tr><td>0.0000</td><td></td><td>-44.129</td><td>B Ph(p)</td></tr><tr><td></td><td>CL H</td><td></td><td></td></tr><tr><td>1.0000</td><td>d BLProd T-m</td><td>6.5761E-5</td><td>C |UI</td></tr><tr><td>7.0000E-3</td><td>e M kg</td><td>93.275</td><td>D Ph(U)</td></tr><tr><td>1190.0</td><td>fK</td><td>-6.1407</td><td>E Htot</td></tr><tr><td>0.0000</td><td>N/m</td><td>-6.1406</td><td>F Edot</td></tr><tr><td>1.0000</td><td>g Rm N-s/m</td><td>0.60956</td><td>G WorkIn W</td></tr><tr><td>-30.00</td><td>h III A</td><td>1.6427</td><td>H Volts</td></tr><tr><td></td><td>i Ph(I) deg</td><td>1.0000</td><td>I Amps</td></tr><tr><td></td><td></td><td>-42.087</td><td>J Ph(V/I) deg</td></tr><tr><td>ideal</td><td></td><td>4.5040E+4</td><td>K |Px|</td></tr><tr><td>!-</td><td>Solid type</td><td>169.10</td><td>L Ph(Px) deg</td></tr><tr><td>RPN 79.964</td><td>Reassign Tm. (Displacer is &quot;axially insulating.&quot;)</td><td></td><td></td></tr><tr><td>inp =Tm</td><td>a G or T</td><td></td><td></td></tr><tr><td>!-</td><td></td><td>79.964</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>1.0000E-6</td><td>COMPLIANCE a little volume for the connection</td><td></td><td></td></tr><tr><td></td><td>a SurfAr m^2</td><td></td><td></td></tr><tr><td>5.0000E-7 b Volume m^3</td><td></td><td>2.5369E+5</td><td>Alpl</td></tr><tr><td></td><td></td><td></td><td>B Ph(p)</td></tr><tr><td></td><td></td><td>-44.129</td><td>C</td></tr><tr><td></td><td></td><td>5.7679E-5</td><td>IUI</td></tr><tr><td></td><td></td><td>102.94</td><td>D Ph(U)</td></tr><tr><td>ideal</td><td></td><td>-6.1407</td><td>E Htot</td></tr><tr><td></td><td>Solid type</td><td>-6.1407</td><td>F Edot</td></tr><tr><td>SOFTEND</td><td></td><td></td><td></td></tr><tr><td>0.0000 a Re(z)</td><td>reconnect at UNION</td><td></td><td></td></tr><tr><td>0.0000 b Im(z)</td><td></td><td>2.5369E+5</td><td>AIpl</td></tr><tr><td>0.0000 c Htot</td><td></td><td>-44.129</td><td>B Ph(p)</td></tr><tr><td></td><td>W</td><td></td><td>C IUI</td></tr><tr><td></td><td></td><td>5.7679E-5</td><td>D Ph(U)</td></tr><tr><td></td><td></td><td>102.94</td><td>E Htot</td></tr><tr><td></td><td></td><td>-6.1407</td><td></td></tr><tr><td></td><td></td><td>-6.1407</td><td>F Edot</td></tr><tr><td></td><td></td><td>-29.136</td><td>G Re(z)</td></tr><tr><td></td><td></td><td>-18.872</td><td>H Im(z)</td></tr><tr><td></td><td></td><td>79.964</td><td>I T</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>SX</td><td>aftercooler</td><td></td><td></td></tr><tr><td>sameas 10a a Area</td><td>m^2</td><td></td><td>AIpl</td></tr><tr><td>0.6000 b VolPor</td><td></td><td>2.8990E+5</td><td></td></tr><tr><td>1.0000E-3 c Length m</td><td></td><td>-39.765</td><td>B Ph(p)</td></tr><tr><td>sameas 10d d rh</td><td></td><td>2.6375E-4</td><td>C |UI</td></tr><tr><td>-45.213</td><td>m</td><td>4.0412</td><td>D Ph(U)</td></tr><tr><td>300.00</td><td>e HeatIn W G</td><td>1.5529</td><td>E Htot</td></tr><tr><td></td><td>f SolidT K =9H</td><td>27.590</td><td>Edot</td></tr><tr><td></td><td></td><td>300.21</td><td>G GasT</td></tr><tr><td>copper</td><td>Solid type</td><td></td><td>H SolidT K</td></tr><tr><td>! -</td><td></td><td>300.00</td><td></td></tr><tr><td>STKSCREEN regenerator</td><td></td><td></td><td></td></tr><tr><td>1.1670E-4 a Area</td><td></td><td></td><td>|pl</td></tr><tr><td>0.6860 b VolPor</td><td>m^2</td><td>2.5401E+5</td><td></td></tr><tr><td>5.0000E-2 c Length m</td><td></td><td>-44.172</td><td>B Ph(p)</td></tr><tr><td></td><td></td><td>5.6191E-5</td><td>deg |UI m^3/s</td></tr><tr><td>1.3900E-5 d rh</td><td></td><td></td><td>D Ph(U)</td></tr><tr><td>0.3000</td><td></td><td>-74.427</td><td>deg</td></tr><tr><td>e ksFrac</td><td></td><td>1.5529</td><td>E Htot W</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>6.1645 F</td><td>Edot W</td></tr><tr><td></td><td></td><td></td><td>G TBeg K</td></tr><tr><td>stainless</td><td></td><td>300.21</td><td></td></tr><tr><td></td><td>Solid type</td><td>79.964</td><td>H TEnd K</td></tr><tr><td>!--</td><td></td><td></td><td></td></tr><tr><td>SX cold heat exch</td><td>11</td><td></td><td></td></tr><tr></table>

sameas 10d d rh m -77.062 D Ph(U) deg   
4.5878 e HeatIn W G 6.1407 E Htot W   
80.000 f SolidT K =11H 6.1407 F Edot W   
79.964 G GasT K   
copper Solid type 80.000 H SolidT K   
!- 12   
UNION displacer cold end   
8 a SegNum 2.5369E+5 AIpl Pa   
sameas 8A b lpISft Pa =12A -44.129 B Ph(p) deg   
sameas 8B c Ph(p)S deg =12B 2.8823E-18 C |U| m^3/s   
sameas 8I d TSoft K =12G -48.383 D Ph(U) deg   
-2.4869E-14 E Htot W   
3.6461E-13 F Edot W   
79.964 G T K   
13   
HARDEND close the end   
0.0000 a R(1/z) =13G 2.5369E+5 AIpl Pa   
0.0000 b I(1/z) =13H -44.129 B Ph(p) deg   
0.0000 c Htot W =13E 2.8823E-18 C |U| m^3/s   
-48.383 D Ph(U) deg   
-2.4869E-14 E Htot W   
3.6461E-13 F Edot W   
6.1508E-16 G R(1/z)   
-4.5751E-17 H I(1/z)   
!- 14   
RPN simulate insulation in the displacer piston   
0.0000 a =A? -2.6645E-15 A ChngeMe   
7E 7F   
guessz 0c Od Oe 4a 4b 4c 6a 9e 11e   
xprecn -3.8026E-3 7.5295E-3 -4.8956E-5 -2.2194E+4 1.4047E+4 -3.6186E-5-1.5964E-4 4.3401E-4-3.0683E-5   
targs 9f 11f 12b 12c 12d 13a 13b 13c 14a

We are using IESPEAKER segments for both the displacer and the driver, because linear motors and loudspeakers share the same physical transduction mechanism.

The user will soon discover that this is a surprisingly robust model, considering the large number of guesses and targets: The model tolerates steps in many independent variables of several percent without getting lost. The user might next generate cooling-power curves by using the cold-temperature target as an independent plot variable and the cooling power as dependent plot variable; or the user might explore the frequency dependence of the cooler. by using frequency as an independent plot variable.

## 5.8.3 Pulse-tube refrigerator

Changing a Stirling cryocooler into an orifice pulse-tube refrigerator (OPTR) is a simple matter of replacing the cold piston with a pulse tube, heat exchanger, orifice, inertance (optional), and compliance volume in series. Figure 5.13 represents such a cooler. The example file <optr.out> represents a 300 Hz, 3 MPa helium orifice pulse-tube refrigerator. (It is not representative of any real hardware known to us. In fact, it is deliberately inefficient, to serve as a lesson in the next section.) The <.out> file is:

![[mu_66afccee_bccb50fb8ddf827b4612.jpg]]

<table><tr><td>TITLE 1 BEGIN 3.0000E+6 300.00 300.09 2.4000E+5</td><td>a crude cooler design, not optimal 0 Start with 8% p osc a Mean P Pa</td><td colspan="4"></td></tr><tr><td>d lpl 0.0000 6.9614E-3 52.843 helium !- SX 1.0290E-3 0.6900 1.2500E-2 6.4500E-5 -455.03 300.00 copper</td><td>e Ph(p) deg f IUI m^3/s g Ph(U) deg Gas type Aftercooler a Area m^2 b VolPor c Length m d rh m</td><td>G G</td><td>2.3020E+5 A |pl -3.4902 5.8349E-3 C|UI 46.790 49.535 429.17 300.09</td><td>B Ph(p) D Ph(U) E Htot</td><td>Pa deg m^3/s deg W W K</td></tr><tr><td>!- STKSCREEN sameas 0.7300 5.5000E-2 2.4000E-5 0.3000 stainless !--</td><td>e HeatIn W f SolidT K Solid type Regenerator 1a a Area b VolPor c Length m d rh e ksFrac</td><td>G =1H m^2 m</td><td>300.00 2 1.7210E+5 -19.576 1.2324E-3 -29.775 49.535 104.37 300.09 149.91</td><td>F Edot G GasT H SolidT K AIpl BPh(p) C IUI D Ph(U) E Htot W F Edot W G TBeg K H TEnd K</td><td>Pa deg m^3/s deg</td></tr><tr><td>SX sameas 0.6900 2.0000E-3 6.4500E-5 14.354 150.00 copper !-- JOIN</td><td>5a a Area m^2 b VolPor c Length m d rh m e HeatIn W f SolidT K Solid type pulse-tube end effects</td><td>Cold heat exchanger G =3H</td><td>3 1.1385E+5 -14.83 1.2326E-3 -30.085 63.889 67.692 149.91 150.00 4 1.1385E+5 -14.83</td><td>AIpl B Ph(p) C |U| D Ph(U) E Htot F Edot G GasT H SolidT K A |pl B Ph(p)</td><td>Pa deg m^3/s deg W W K Pa deg</td></tr><tr><td>STKDUCT 5.6870E-5 2.6740E-2 0.2000 1.0000E-5</td><td>Pulse tube a Area m^2 b Perim m</td><td>Mstr</td><td>1.2173E-3 -30.085 63.889 66.850 149.91 149.89 5 1.0284E+5 -43.915 1.3030E-3 -51.102 63.889</td><td>C |UI D Ph(U) E Htot W F Edot W G TBeg K H TEnd K AIpl B Ph(p) C IUI D Ph(U) E Htot W</td><td>m^3/s deg Pa deg m^3/s</td></tr><tr><td>stainless !-- JOIN !- SX Hot heat exchanger sameas 5a a Area 0.6900 5.0000E-3</td><td></td><td>d WallA m^2 Solid type pulse-tube end effects</td><td>66.473 149.89 300.22 6 1.0284E+5 -43.915 1.2880E-3 -51.102 63.889 65.706 300.22 300.19</td><td>F Edot G TBeg H TEnd Alpl B Ph(p) C |U| D Ph(U) E Htot F Edot G TBeg</td><td>deg W K K Pa deg m^3/s deg W W K H TEnd K</td></tr></table>

<table><tr><td>GUESS 0c Of 0g 1e 3e</td></tr></table>

![[mu_66afccee_ef23fa4837bd558987dd.jpg]]  
Figure 5.13: An orifice pulse-tube refrigerator (OPTR). The orifice can be purely resistive, as shown here, but adding inertance in series with the resistive orifice improves performance.

```csv
8
IMPEDANCE The orifice
1.0000E+7 a Re(Zs) Pa-s/m^3 1.2986E+4 AIpl Pa
0.0000 b Im(Zs) Pa-s/m^3 11.749 B Ph(p) deg
1.2887E-3 C IUI m^3/s
-51.43 D Ph(U) deg
-4.5475E-13 E Htot W
3.7754 F Edot W
9
DUCT inertance
1.0000E-5 a Area m^2 Mstr 2.2724E+4 AIpl Pa
1.1210E-2 b Perim m 9a -141.31 B Ph(p) deg
3.0000E-2 c Length m 1.2880E-3 CIUI m^3/s
5.0000E-4 d Srough -51.444 D Ph(U) deg
-4.5475E-13 E Htot W
ideal Solid type 3.3642E-2 F Edot W
! - 10
COMPLIANCE Reservoir volume
1.2680E-2 a SurfAr m^2 10b 2.2724E+4 A Ipl Pa
1.5000E-4 b Volume m^3 Mstr -141.31 B Ph(p) deg
9.0138E-12 C |U| m^3/s
-178.43 D Ph(U) deg
-4.5475E-13 E Htot W
ideal Solid type 8.1665E-8 F Edot W
11
HARDEND The end
0.0000 a R(1/z) =11G 2.2724E+4 AIpl Pa
0.0000 b I(1/z) =11H -141.31 B Ph(p) deg
0.0000 c Htot W =11E 9.0138E-12 C |U| m^3/s
-178.43 D Ph(U) deg
-4.5475E-13 E Htot W
8.1665E-8 F Edot W
1.5514E-7 G R(1/z)
-1.1740E-7 H I(1/z)
```

The Stirling part of the system is modeled as a stacked-screen regenerator STKSCREEN and two stacked-screen heat exchangers SX. We model the pulse tube itself as a STKDUCT, using Rott's wave equation and enthalpy flux equation in boundary-layer approximation, because the pulse-tube diameter is $\gg \delta _ { \kappa }$ . The JOIN segments are used at the ends of the pulse tube to model the temperature overshoots and adiabatic-isothermal interface losses there, as explained in Section 10.8. The heat exchanger at the hot end of the pulse tube is the HX. The orifice, inertance, and compliance are easily modeled as DELTAEC IMPEDANCE, DUCT, and COMPLIANCE, respectively. Our use of zero for the imaginary part of the IMPEDANCE reflects our intention that this orifice should truly be resistive, with its pressure drop in phase with mass flux.

For purposes of illustration here, we will regard the geometry of the apparatus as given, and will explore its performance for a given, fixed input $\left| p _ { 1 } \right|$ . The guess-target summary indicates our point of view:

![[mu_66afccee_13cc6bff0bc6c9b66b0e.jpg]]  
Figure 5.14: Plotting <optr. sp> using $\mathrm { R e } [ p _ { 1 } ]$ as the horizontal axis and $\mathrm { I m } [ p _ { 1 } ]$ as the vertical axis yields a pressure-phasor plot. The SegEndMarks option tags the curve with numbers indicating the ends of the segments. Cloning the plot and switching $p _ { 1 }$ to $U _ { 1 }$ yields a volumeflow-rate phasor plot. These can also be created with Phasor Mode in the plotter's Options pulldown menu.

<table><tr><td>name units</td><td>BEGIN:TBeg K</td><td>BEGIN:|U| m^3/s</td><td>BEGIN:Ph(U) deg</td><td>SX:HeatI W</td><td>SX:HeatI W</td><td>SX:HeatI W</td></tr><tr><td>value TARGET</td><td>300.09 1f</td><td>6.9614E-03 3f</td><td>52.843 7f</td><td>-455.03 11a</td><td>14.354 11b</td><td>-63.889 11c</td></tr><tr><td>name</td><td>SX:Est-T</td><td>SX:Est-T</td><td></td><td>SX:Est-T HARDE:R(1/z HARDE:I(1/z HARDE:Htot</td><td></td><td></td></tr><tr><td>units</td><td>K</td><td>K</td><td>K</td><td></td><td></td><td>W</td></tr><tr><td>value</td><td>300.00</td><td>150.00</td><td>300.00</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>result</td><td>300.00</td><td>150.00</td><td>300.00</td><td></td><td>3.6105E-09-2.7741E-09-2.8422E-14</td><td></td></tr></table>

Three of the six targets fix the hot and cold temperatures at 300 K and 150 K. We leave the amplitude of the oscillatory pressure at the BEGINning at 8% of mean pressure, and leave the frequency fixed at 300 Hz. Hence, we are asking: What is the cooling power at 150 K, and how much input power, volume flow rate, etc. are required, for fixed frequency and pressure amplitude, and for this geometry? The result, given in the file listings above: 14 W of cooling power, requiring 500 W of input power from the compressor.

As with most OPTR models we have worked with in DELTAEC, this one is not particularly "robust." An abrupt change of a typical variable by 20% or 30% will likely cause DELTAEC to get hopelessly lost, unable to adjust its guesses to hit the targets. Much of the shooting-method "fragility" of OPTR models (and other models with a STKDUCT or STKCONE) in DELTAEC is due to the fact that small changes in variables near the BEGINning, such as $p _ { 1 } , U _ { 1 }$ , and the heat removed at a heat exchanger, have a large effect on temperatures at the end of the pulse tube. Some of the fragility is due to the fact that OPTR models typically have a large number of guesses and targets. When you encounter a fragile DELTAEC model, try to reduce the number of guesses and targets as much as possible (particularly in initial design explorations when you are changing things dramatically) and, once you have a convergent model, make only small changes in variables. Try negative values of the Normalization Mode,1 accessible in the Edit, Options pulldown menu; we often find that Mode = -4 works much better than DELTAEC's default Mode = 1. Try reducing DELTAEC's convergence tolerance (Section 8.3.2) if you have to use more than 5 guesses and 5 targets. Remember to subdivide a large change in a variable into a series of small changes, using an incremental plot. A fast computer and frequent hard-disk saving of satisfactory converged models will minimize frustration. See Section 5.4 for additional tips.

Examination of the pulse tube segment STKDUCT above shows a possible problem: The pulse tube figure of merit $\dot { H } _ { \mathrm { t o t } } / \dot { E }$ , which can theoretically be as high as 1.000 but is usually more like 0.8, may be unrealistically high: $\dot { H } _ { \mathrm { t o t } } / \dot { E } \simeq 6 3 . 9 ~ \mathrm { W } / 6 6 . 5 ~ \mathrm { W } \simeq 0 . 9 6 .$ DELTAEC knows nothing about jet- or streaming-driven convection, and pulse-tube experimentalists are only beginning to learn how to reliably avoid such convection. (For a discussion of streaming-driven convection, see Refs. [29] or [30], and [31] and [13].) To force DELTAEC to accommodate a reduced pulse-tube figure of merit, the user can introduce an RPN and an additional guess-target pair. The RPN instruction line can compute the ratio of $\dot { H } _ { \mathrm { t o t } }$ to $\dot { E }$ in the pulse tube, and the target value in line a can be set to something like 0.8. The user can simulate the thermal loading of streaming-driven convection, etc. by letting DELTAEC guess an unphysically large value for the cross section of the pulse tube solid wall (line 4d), which then conducts significant heat from hot to cold, allowing DELTAEC to meet its target of 0.8. We will not do so here.

Our choices for nearly all input variables in this model were random, not guided by good design sense or any real cryocooler. In particular, our choice of $\mathrm { R e } [ Z _ { s } ] = 1 \times 1 0 ^ { 7 }$ for the orifice impedance above was random. To find a better orifice setting, use $\mathrm { R e } [ Z _ { s } ]$ as an independent plot variable, letting it range from $1 \times 1 0 ^ { 7 }$ to $1 \times 1 0 ^ { 8 }$ . The cooling power peaks at 14.7 W for $\mathrm { R e } [ Z _ { s } ] = 2 . 4 \times 1 0 ^ { 7 }$ . This is not much improvement. For guidance on what to try changing next to improve the performance, we consider exergy in the next section.

## 5.9 Exergy flow

Among the many important thermodynamic variables having units of power (e.g., Watts) is exergy flow. In thermodynamics, exergy represents the ability to do useful work, in principle, assuming unlimited access to an infinitely large thermal reservoir at an “ambient" temperature $T _ { 0 }$ at which heat has no value [32].

Novice thermoacousticians sometimes suppose that the acoustic power $\dot { E }$ represents the ability to do useful work, because the treatment of intensity and power in adiabatic waves in introductory acoustics courses implies that the face of a moving piston is a perfect interface between mechanical power $( F u )$ and acoustic power $( p U )$ . However, thermoacoustic waves are generally not adiabatic. The "heat" carried near solid surfaces by the $s _ { 1 } \widetilde u _ { 1 }$ term in the second-order enthalpy flow represents an ability to do useful work that is separate from $\dot { E }$ , because this term in the enthalpy flow can be usefully coupled to the assumed thermal reservoir at $T _ { 0 }$ through a heat engine if time-averaged su is flowing at a temperature different from $T _ { 0 }$ . Taking this into account [13], the exergy flow associated with a thermoacoustic wave is

$$
\dot { X } = \frac { T _ { 0 } } { T _ { m } } \dot { E } + \left( 1 - \frac { T _ { 0 } } { T _ { m } } \right) \dot { H } _ { 2 , k } .\tag{5.16}
$$

(For an adiabatic sound wave, $\dot { H } _ { 2 , k } = \dot { E }$ , so this reduces to ${ \dot { X } } = { \dot { E } }$ , independent of $T _ { m }$ as expected.) DELTAEC's ambient temperature $T _ { 0 }$ is set to 300 K by default in the BEGIN segment; this default can be overridden by using =Tzero in a subsequent RPN segment.

The usefulness of the concept of exergy arises from its relationship to irreversible entropy generation, expressed by the Guoy-Stodola theorem [32],

$$
\Delta \dot { X } = T _ { 0 } \dot { S } _ { \mathrm { g e n } } .\tag{5.17}
$$

In this simplified expression of the theorem, $\Delta \dot { X }$ represents the difference in exergy flow between two locations in an apparatus between which exergy cannot flow in or out laterally, and the theorem says that this difference is the product of $T _ { 0 }$ and the rate of irreversible entropy generation between those two locations. In a perfectly efficient apparatus, there is no irreversible entropy generation, so $\Delta \dot { X } = 0$ (except where $\dot { X }$ flows in or out, e.g., at a heat exchanger or a \*\*DUCER or \*\*SPEAKER). Thus, a graph of $\dot { X }$ vs x can help show the user what parts of an apparatus are most responsible for its inefficiency

For example, consider the OPTR described in Section 5.8.3. The <.sp> plot of $\dot { E } , \dot { H } _ { \mathrm { t o t } }$ and $\dot { X }$ is shown in Fig. 5.15. Most of the exergy is lost in the regenerator, and the rate of exergy loss is steepest near the ambient end of the regenerator. This suggests that viscous losses in the regenerator may be severe. Indeed, the <.out> file shows a large pressure drop in the regenerator. The user might try changing the dimensions of the regenerator to improve the performance. Figure 5.15 also shows significant drops in $\dot { X }$ in the ambient and cold heat exchangers. There, the analysis of the situation is a little more complicated because the heats flowing into a heat exchanger contribute exergy according to [13]

![[mu_66afccee_3edf71282db5de9de311.jpg]]  
Figure 5.15: Graph of total power (black solid line), acoustic power (blue dashed line), and exergy flow (green dot-dashed line) in the OPTR example. The locations where $\dot { H } _ { \mathrm { t o t } }$ changes are the three heat exchangers.

$$
\Delta \dot { X } = \dot { Q } \left( 1 - T _ { 0 } / T _ { m } \right) ,\tag{5.18}
$$

where $T _ { 0 }$ is ambient temperature and $T _ { m }$ is the local temperature. At the ambient heat exchanger, $T _ { m } = T _ { 0 }$ , so the drop in exergy there is entirely lossy. At the cold heat exchanger, $T _ { m } \neq T _ { 0 }$ , but the loss in thermoacoustic exergy due to $\dot { Q }$ is only 15 W, so most of the drop in X in Fig. 5.15 at the cold heat exchanger is lossy. Thus, the heat exchangers are also contributing significantly to the poor performance in this OPTR. At this point, the user might suspect that the poor performance of this OPTR arises from trying to force too much flow through pores that are too tight or an area that is too small.

Subsequent chapters describe additional steady-flow and mixture-separation features in DELTAEC. These phenomena also contribute to $\dot { X }$ , and the terms that they add to Eq. (5.16) are given in Eq. (8.9).

## 6. Steady flow, too

The superposition of steady flow and oscillating flow creates many interesting and important effects that can be modeled with DELTAEC. A nonzero steady flow profoundly affects $T _ { m } ( x )$ in stacks and regenerators, creates Doppler shifts [33] and increases the turbulent dissipation of acoustic power in DuCTs, and causes a small x dependence in the time-averaged pressure. In systems such as Reid's refrigerator (shown below in Fig. 6.1), externally forced steady flow provides the ability to deliver cold gas from a thermoacoustic refrigerator without a cold heat exchanger. In more conceptually subtle situations, the acoustic oscillations themselves cause the steady flow, which is then called “streaming" by acousticians [34]. In some circumstances, such as the thermoacoustic-Stirling hybrid engine shown in Fig. 1.7 or 6.4, we try to understand the streaming well enough to eliminate it. In other circumstances, such as the self-circulating heat exchanger shown in Fig. 1.9, we try to make streaming as large as possible without undue dissipation of acoustic power

## 6.1 Principles of calculation

DELTAEC accounts for steady flow as $\dot { N }$ , the moles per second¹ flowing through the segments in the positive-x direction. It can be specified or guessed in BEGIN, and it splits up at TBRANCHs, adds up at UNIONs, and can be abruptly changed in RPNs. Otherwise, $\dot { N }$ flows unchanged through segments. (But note that it seldom makes sense to imagine that nonzero $\dot { N }$ could flow through one of the enclosed \*EDUCER or \*ESPEAKER segments.)

Steady flow carries power

$$
\dot { H } _ { \dot { N } } = \dot { N } m w _ { m } ,\tag{6.1}
$$

where $m$ is the molar mass and $w _ { m }$ is the mean enthalpy per unit mass. The total power

$$
\dot { H } _ { \mathrm { t o t } } = \dot { H } _ { 2 , k } + \dot { H } _ { \dot { N } }\tag{6.2}
$$

is, to second order, the power that obeys the first law of thermodynamics for open control volumes. It is the sum of the second-order time-averaged thermoacoustic enthalpy flux, the ordinary thermal conduction in the x direction, and $\bar { \dot { H } } _ { \dot { N } } = \dot { N } m w _ { m }$

In DELTAEC, mean enthalpy is referenced to zero at temperature $T _ { 0 }$ which is set to 300 Kelvin by default in the first BEGIN segment of a model. (This default can be overridden by using the =Tzero operation in an RPN segment.) For an ideal gas, Eq. (6.1) can then be regarded as

$$
\dot { H } _ { \dot { N } } = \dot { N } m c _ { p } \left( T _ { m } - T _ { 0 } \right) .\tag{6.3}
$$

Nonzero $\dot { N }$ also contributes a term

$$
\dot { N } \left( m w _ { m } - T _ { 0 } m s _ { m } \right)\tag{6.4}
$$

to exergy flow $\dot { X }$ . Like the enthalpy per unit mass $w _ { m }$ , the entropy per unit mass $s _ { m }$ is referenced² to zero at $T _ { 0 }$

DELTAEC also introduces a new integration variable, the second-order time-averaged head-loss pressure p2,0,DEc, to keep track of the small but important effects of steady flow on the time-averaged pressure. The second-order head-loss pressure p2,o,DEc is initialized at zero in BEGIN and evolves with x in most other segments. When $\dot { N }$ and p2,0,DEC are involved in a DELTAEC calculation, the numerical-integration picture that is summarized in Eqs. (5.6)–(5.9) for thermoacoustics with $\dot { N } = 0$ , namely

$$
\frac { d p _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { m o m e n t u m } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega ; \ \mathrm { g e o m e t r y } , \ \mathrm { g a s ~ p r o p e r t i e s } , \ \mathrm { e t c } . ) ,
$$

$$
\frac { d U _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega , \mathrm { g e o m e t r y , g a s \ p r o p e r t i e s , e t c . } ) ,
$$

$$
\frac { d T _ { m } } { d x } = \mathcal { F } _ { x - \mathrm { e n e r g y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega , \mathrm { g e o m e t r y } , \mathrm { g a s \ p r o p e r t i e s } , \mathrm { e t c . } ) ,
$$

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } ~ = ~ \mathcal { F } _ { \mathrm { l a t e r a l ~ e n e r g y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; ~ p _ { m } , \omega , \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) .
$$

must be replaced by this slightly more complicated picture:

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle \mathcal { F } _ { \mathrm { m o m e n t u m } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega , \dot { N } ; \ \mathrm { g e o m e t r y , \ g a s \ p r o p e r t i e s , \ e t c . } ) , } \end{array}\tag{6.5}
$$

$$
\frac { d U _ { 1 } } { d x } ~ = ~ \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; ~ p _ { m } , \omega , \dot { N } , \mathrm { g e o m e t r y , \ g a s ~ p r o p e r t i e s , ~ e t c . } ) ,\tag{6.6}
$$

$$
\frac { d T _ { m } } { d x } = \mathcal { F } _ { x \mathrm { { - e n e r g y } } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega , \dot { N } , \mathrm { g e o m e t r y } , \mathrm { g a s ~ p r o p e r t i e s } , \mathrm { e t c . } ) ,\tag{6.7}
$$

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } = \mathcal { F } _ { \mathrm { l a t e r a l e n e r g y } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega , \dot { N } , \mathrm { g e o m e t r y , \mathrm { g a s ~ p r o p e r t i e s } , \mathrm { e t c . } } ) ,\tag{6.8}
$$

$$
\begin{array} { r l r } { \frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } } & { = } & { \mathcal { F } _ { \mathrm { h e a d } } \log ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { H } _ { \mathrm { t o t } } ; \ p _ { m } , \omega , \dot { N } , \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) . } \\ & { } & \end{array}\tag{6.9}
$$

Please note that $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ is usually nonzero even when $\dot { N } = 0$ , because $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ arises in part from viscous drag on $U _ { 2 , 0 }$ , given by

$$
\rho _ { m } U _ { 2 , 0 } \simeq { \dot { N } } m - \frac { 1 } { 2 } \mathrm { R e } \int [ \rho _ { 1 } \widetilde { u } _ { 1 } ] ~ d A _ { \mathrm { g a s } } ,\tag{6.10}
$$

where $m$ is the molar mass, as explained in more detail near $\operatorname { E q } .$ (8.15).

Our confidence in the accuracy of the DELTAEC implementation of these equations is lower than in the equations described in Chapters 2 and 5. We are very confident of the effect of nonzero $\dot { N }$ on $\mathcal { F } _ { x - \mathrm { e n e r g y } }$ and $\mathcal { F } _ { \mathrm { l a t e r a l ~ e n e r g y } }$ under all circumstances we have encountered, and confident of the effect of nonzero $\dot { N }$ on all the equations when the steady and oscillating flows are both laminar, but for turbulent flow our understanding of $\mathcal { F } _ { \mathrm { h e a d ~ l o s s } }$ and of the effects of nonzero $\dot { N }$ on $\mathcal { F } _ { \mathrm { m o m e n t u m } }$ and $\mathcal { F } _ { \mathrm { c o n t i n u i t y } }$ are still evolving, and are mostly based on the quasisteady approximation, namely that the behavior at any instant of time $t$ is the same as it would be for steady flow with volume flow rate $U = \dot { N } m / \rho _ { m } { + } \mathrm { R e } [ U _ { 1 } e ^ { i \omega t } ]$ , an approximation with obvious shortcomings in acoustics where inertial effects of gas acceleration are usually as important as anything else. The complicated details of the current steady-flow DELTAEC implementation are given in Chapter 10.

One other variable is sometimes useful in the context of nonzero $\dot { N }$ . The (total) secondorder, time-averaged pressure $p _ { \mathrm { 2 , 0 , t o t } }$ corresponds to pressure changes as measured by sidewall pressure transducers [35], because $p _ { \mathrm { 2 , 0 , t o t } }$ is given by

$$
p _ { 2 , 0 , \mathrm { t o t } } = p _ { 2 , 0 , \mathrm { t r a d } } + p _ { 2 , 0 , \mathrm { D E C } }\tag{6.11}
$$

where the reversible part of the second-order time-averaged pressure [36] is given by

$$
p _ { 2 , \mathrm { 0 , t r a d } } ( x ) = \frac { \left| p _ { 1 } \right| ^ { 2 } } { 4 \rho _ { m } a ^ { 2 } } - \frac { \rho _ { m } \left| U _ { 1 } \right| ^ { 2 } } { 4 A _ { \mathrm { g a s } } ^ { 2 } } .\tag{6.12}
$$

The variable p20tot is available in RPN segments. Note that it depends on area, which may not have a sensible value after segments without area, such as BEGIN, TBRANCH, UNION, or IMPEDANCE.

User-defined gases specified by $< . \tt t p f >$ files cannot be used with $\dot { N }$ enabled, because $\operatorname { E q }$ (6.1) requires $m .$ , which is not available in $< . \tt t p f >$ format. To circumvent this shortcoming when a user-defined gas must be used with nonzero $\dot { N }$ use $\mathrm { a } < . { \tt t p m } >$ file and set the mole fraction of one component to zero.

In the rest of this chapter, we illustrate DELTAEC's steady-flow features with three examples. In the first example, nonzero $\dot { N }$ is externally driven and $p _ { \mathrm { 2 , 0 , D E C } }$ is of little interest. In the second example, $\dot { N } = 0$ is desired, but must be accomplished through careful balancing of small $p _ { \mathrm { 2 , 0 , D E C } }$ effects. In the third example, nonzero $\dot { N }$ is driven by large p2,0,DEC effects

## 6.2 Reid's refrigerator

Bob Reid's standing-wave refrigerator, shown in Fig. 6.1 and described in Refs. [37, 38, 39], was built for the study of large nonzero $\dot { N }$ through the stacks. The standing wave in the resonator had pressure nodes at the top-center and bottom-center locations, and out-ofphase pressure antinodes near the left and right speaker pairs. Steady flow of ambienttemperature working gas was injected into the resonator at the upper pressure node. This flow was cooled as it passed through the stacks, so cold gas flowed out of the resonator at the lower pressure node. There was no concern that acoustic power might flow out into the steady-flow piping because the steady-flow connections were made at pressure nodes.

![[mu_66afccee_44a1b0d67f601adf7370.jpg]]  
Figure 6.1: Standing-wave refrigerator with nonzero steady flow through the stacks, studied by Reid [37, 38, 39]. Steady flow was injected at the upper pressure node at ambient temperature and flowed out at the lower pressure node at a cold temperature.

To model this apparatus in DELTAEC, we will consider only one half of the apparatus, because the other half is identical (though shifted in time phase by 180°). Focusing only on the thermal aspects, we begin the model just below the speakers in the right half, and end it where the right half joins the left half, at the exit port at the bottom. The BEGIN and the guess-target summary reflect the following perspective: The refrigerator is driven at a known frequency and with a known pressure amplitude near the drivers; a known steady flow of gas at a known temperature goes down through the apparatus; the ambient heat exchanger solid is held at a known temperature by cooling water. We want to learn the temperature of the exiting steady flow of cold gas, among other things.

GUESS Of 0g 3a 5e   
name BEGIN:|U| BEGIN:Ph(U) RPN:G or T HX:HeatI   
units m^3/s deg W   
value 5.4963E-02 8.7929 6.7539E-02 -135.76   
TARGET 5f 15a 15b 15c   
name HX:Est-T SOFTE:Re(z) SOFTE:Im(z) SOFTE:Htot   
units K W   
value 300.00 0.0000 0.0000 -66.713   
result 300.00 -5.3646E-17 3.9259E-16 -66.713   
TITLE segments 1-7 < Bob 9/97; segs 8-14 < Hiller ntbk, pg one, 10/97   
!->reid4.out   
0   
BEGIN Initialize in main duct where drivers are attached   
3.2388E+05 a Mean P Pa   
92.000 b Freq Hz

RPN U mean here (liter/sec)

![[mu_66afccee_a18cc9c0f2fea5df6062.jpg]]

reid4.spl  
![[mu_66afccee_9c81f1fa4a9938cec397.jpg]]  
Figure 6.2: Temperatures vs x in Reid's refrigerator. Red line, gas temperature $T _ { m } ( x )$ Black line, solid temperature $T _ { \mathrm { s o l i d } } ( x )$

Output 6H tells us that the refrigerator cools the gas to 295 Kelvin. The <.sp> plots shown in Figs. 6.2 and 6.3 show details of the temperature profile in the stack and the heat exchanger upstream of it, and how the energy flow is independent of x in the stack even as energy shifts from $\dot { N } m c _ { p } T _ { m }$ to $\dot { H } _ { 2 , k }$ . The temperature profile is so severely curved— essentially horizontal near the ambient end—that an increase in flow above the present value of 0.67 mol/s (segment 0), which is about 5 liters per second (segment 13), would probably be undesirable. Note that the solid temperature equals the gas temperature everywhere except in the heat exchanger, where the solid is cooler than the gas so it can remove ambient heat from the gas.

When $\dot { N } \neq 0$ , the energy boundary conditions at the BEGINning and END of a model often require careful thought. The most commonly desired boundary condition is

$$
\dot { H } _ { \mathrm { t o t } } = \dot { E } + \dot { N } m w _ { m } .\tag{6.13}
$$

On its face, this condition sets total power equal to the sum of acoustic power and steady-flow enthalpy. Comparison of this expression with Eqs. (6.1) and (6.2) here and with Eq. (5.29) in Ref. [13] shows what this condition deliberately omits: axial thermal conduction in the gas and solid, and boundary-layer, bucket-brigade thermoacoustic entropy transport in the gas. Thus, this boundary condition is appropriate whenever a long, large-diameter, unremarkable DUCT or other segment starts or ends a model with $\dot { N } \neq 0$ . This condition is encountered so frequently that it is taken to be the default in BEGIN, which can be overridden by accessing the Default Htot / Other Htot choice in the Optional Parameters in BEGIN. The Default Htot choice sets the initial value of $\dot { H } _ { \mathrm { t o t } }$ according to Eq. (6.13). This condition must also sometimes be enforced in subsequent S0FTENDs, where an RPN that expresses Eq. (6.13) can be used, as illustrated above in segments 14 and 15.

![[mu_66afccee_0c6ac18380b6b32a442a.jpg]]  
Figure 6.3: Power flows in Reid's refrigerator. Blue dashed line is $\dot { E } .$ Solid black line is $\dot { H } _ { \mathrm { t o t } }$ Dot-dashed red line is $\dot { H } _ { 2 , k }$

Another new issue is addressed in segment 3 now that $\dot { N } \neq 0$ . This variable, $F _ { \dot { Q } \dot { N } }$ , tells DELTAEC what fraction of the heat exchanger's heat $\dot { Q }$ should be allocated to changing energy in the steady flow through the heat exchanger; the remainder is allocated to $H _ { 2 , k }$ When $\dot { N } \neq 0$ , we often use $F _ { \dot { Q } \dot { N } }$ as a guess, to let DELTAEC meet temperature and energyflow targets.

Output J in segment 15 gives $p _ { 2 , 0 , \mathrm { D E C } } = - 2 4 ~ \mathrm { P a }$ . Since $p _ { \mathrm { 2 , 0 , D E C } }$ is initialized to zero in BEGIN, this shows that only 24 Pa of steady pressure is needed to push the 5 liters per second through the stack and heat exchanger. To learn how much of that falls across the heat exchanger and how much falls across the stack, we could insert an RPN segment between the heat exchanger and the stack, with p20DEC in line b, or display p2,0,DEc in a <.sp> plot.

## 6.3 TASHE

The thermoacoustic-Stirling hybrid engine (TASHE), shown in Fig. 6.4 and described in detail in Refs. [5, 40], will be used to illustrate the use of DELTAEC to design a toroidal thermoacoustic apparatus without Gedeon streaming [41]. Without intelligent design, Gedeon streaming around the loop of the TASHE can convect an enormous amount of heat away from the hot heat exchanger.

We created this DELTAEC model starting from Backhaus's 1998 DELTAE model $( \mathrm { A p - }$ pendix B4 of Ref. [13]. We removed some inessential segments to reduce the total number, in an effort to save room in the Users Guide. We modified some segment types to bring the model up to date in DELTAEC version 6. For selecting guesses and targets, we have adopted the following perspective: At what frequency, amplitude, and hot temperature will this engine run, for a given $\dot { Q } _ { H }$ applied at the hot heat exchanger? Ambient temperature and gas mean pressure are given, and hardware dimensions are fixed. In anticipation of adding more targets and guesses later, we make a special effort to minimize their numbers here. Thus, we do not use gas temperature 0c as a guess and ambient heat-exchanger solid temperature 12f as a target; we simply set 0c manually to a value that brings 12H near 25°C. With those simplifications, we still have 32 segments, 6 targets, and 6 guesses. This file is in the <Examples\SteadyFlow> folder, as <tashe1.out>.

![[mu_66afccee_952ed620493356f37dcc.jpg]]  
Figure 6.4: Illustrations of the TASHE. (a) Scale drawing of the toroidal part of the TASHE, containing the heat exchangers. (b) Overall scale drawing, with the toroidal part at the left end. (c) DELTAEC's Schematic view of the TASHE, with some phasor diagrams inserted to illustrate the wave.

```csv
!Created@21:31:07 13-Dec-2022 with DeltaEC version 6.4b2.9!under win32,
0
BEGIN the setup
3.1030E+6 a Mean P Pa
85.815 b Freq Hz G
325.00 c TBeg K
3.1730E+5 d lpl Pa G
0.0000 Ph(p) deg
0.0000 f |UI m^3/s
0.0000 g Ph(U) deg
helium Gas type
! 1
TBRANCH Split up the flow
-1.8314E+7 a Re(Zb) Pa-s/m^3 G 3.1730E+5 AIpl Pa
1.4254E+7 b Im(Zb) Pa-s/m^3 G 0.0000 B Ph(p) deg
-1263.0 c HtotBr W 1.3672E-2 C IUI m^3/s
-142.11 D Ph(U) deg
-1263.0 E HtotBr W
-1711.8 F EdotBr W
1711.8 G EdotTr W
+ 2 DUCT 180 bend plus brass connecting flange (pg 27 book 4)
+ 3 CONE 4" to 3" Concentric reducer (pg 36 book 4)
+ 4 DUCT 3" FB Duct - Length given in concept.skf
+ 5 CONE 3.5" to 3" Long radius reducing elbow (pg 36 book 4)
+ 6 MINOR minor loss, small end of elbow
+ 7 DUCT FB connector/part of tee (Pg 55 book 4 concept.skf)
! 8
SOFTEND End of feedback branch
0.0000 a Re(z) 2.6366E+5 AIpl Pa
0.0000 b Im(z) 1.0936 BPh(p) deg
0.0000 c Htot W 0.20575 C |UI m^3/s
-92.826 D Ph(U) deg
-1263.0 E Htot W
-1854.2 F Edot W
-0.11153 G Re(z)
1.6277 H Im(z)
325.00 I T K
x 9 CONE gas diode plate
! 10
MINOR minor loss here
sameas 9d a Area m^2 3.0895E+5 Alpl Pa
0.8000 b K+ -1.9187 B Ph(p) deg
7.0000E-2 c K- 1.3456E-2 C |U| m^3/s
36.935 D Ph(U) deg
1263.0 E Htot W
1618.7 F Edot W
+ 11 DUCT jetting space
! 12
TX Main room temp water HX (pg 90 book 3)
6.6580E-3 a Area m^2 3.0909E+5 AIpl Pa
0.2275 b GasA/A -2.006 B Ph(p) deg
2.0400E-2 c Length m 1.0864E-2 C |U| m^3/s
1.2700E-3 d radius m 15.077 D Ph(U) deg
-1603.9 e HeatIn W G -340.86 E Htot W
300.00 f SolidT K 1605.0 F Edot W
325.00 G GasT K
stainless Solid type 293.14 H SolidT K
+ 13 DUCT Regen cold end dead space due to ribs (pg 91 book 3)
! - 14
STKSCREEN Regenerator (pg 92 book 3) (Ks frac est:pg 20 book 4)
6.2070E-3 a Area m^2 2.6898E+5 A |pl Pa
0.7190 b VolPor 1.5574 B Ph(p) deg
7.3000E-2 c Length m 3.2813E-2 C |U| m^3/s
4.2200E-5 d rh m -37.968 D Ph(U) deg
0.3000 e ksFrac -340.86 E Htot W
3404.0 F Edot W
325.00 G TBeg K
stainless Solid type 862.30 H TEnd K
+ 15 DUCT All regen hot end dead space (pg 92 book 3)(area is avg)
```

![[mu_66afccee_f5b2949389d58ce4d26e.jpg]]

```csv
!– 16
HX HHX (pg 93 book 4) heat xfer area used/not acoustic area
5.6970E-3 a Area m^2 2.6890E+5 AIpl Pa
0.9867 b GasA/A 1.5427 BPh(p) deg
6.3500E-3 c Length m 3.4190E-2 C |UI m^3/s
7.9400E-4 dy0 m -41.222 D Ph(U) deg
3700.0 e HeatIn W 3359.1 E Htot W
0.0000 f SolidT K 3374.8 F Edot W
862.30 G GasT K
stainless Solid type 954.80 H SolidT K
+ 17 JOIN thermal buffer tube end effects
+ 18 DUCT hhx dead space (pg 94 book 3) stainless used for Qdot
+ 19 STKDUCT Straight section of pulse tube (pg 101 bk 4)
+ 20 JOIN thermal buffer tube end effects
!-- 21
TX Small water Xger
6.6580E-3 a Area m^2 2.6518E+5 AIpl Pa
0.2690 b GasA/A 1.2013 B Ph(p) deg
1.0160E-2 c Length m 7.4062E-2 C |UI m^3/s
2.2860E-3 d radius m -69.477 D Ph(U) deg
-704.13 e HeatIn W G 2655.0 E Htot W
290.00 f SolidT K 3249.2 F Edot W
325.00 G GasT K
ideal Solid type 282.25 H SolidT K
+ 22 DUCT PT connector (see pg 55 book 4 and concept.skf)
+ 23 UNION Rejoin
+ 24 ANCHOR assume resonator and load can dump heat as needed
+ 25 DUCT Section of 3.5" tee
+ 26 CONE 3.5" to 4" cone to adapt to resonator (pg 93 book 4)
+ 27 DUCT Initial section of resonator
+ 28 BRANCH RC dissipator
+ 29 DUCT Continuation of resonator
+ 30 CONE 7 degree cone - 10.02" final diameter
+ 31 DUCT 10" duct P8
+ 32 SURFACE end cap of resonator
33
HARDEND end of duct
0.0000 a R(1/z) =33G 9.5025E+4 AIpl Pa
0.0000 b I(1/z) =33H -178.64 BPh(p) deg
0.0000 c Htot W 1.1193E-13 C |U| m^3/s
91.975 D Ph(U) deg
-9.0949E-13 E Htot W
5.6613E-11 F Edot W
1.2018E-15 G R(1/z)
-1.1289E-13 H I(1/z)
34
RPN energy closure
0.0000 a =A? 0.0000 AW
Htot Edot -
GUESS Ob 0d 1a 1b 12e 21e
name BEGIN:Freq BEGIN: lpl TBRAN:Re(Zb TBRAN:Im(Zb TX:HeatI TX:HeatI
units Hz Pa Pa-s/m^3 Pa-s/m^3 W W
value 85.815 3.1730E+05-1.8314E+07 1.4254E+07-1603.9 -704.13
TARGET 23b 23c 23d 33a 33b 34a
name UNION:IpISO UNION:Ph(p) UNION:T_SOF HARDE:R(1/z HARDE:I(1/z RPN
units Pa deg K
value 2.6366E+05 1.0936 325.00 0.0000 0.0000 0.0000
result 2.6366E+05 1.0936 325.00 -1.1441E-16 1.0380E-15 0.0000
```

With 3700 W applied to the hot heat exchanger, the apparatus resonates at 85.8 Hz with an amplitude of 317 kPa at BEGIN. The hot gas temperature is 862 K and the hot solid temperature is 955 K.

One strange-looking number appears above: Segment 1, TBRANCH, input c, -1263 W, HtotBr. DELTAEC arrives at the TBRANCH with some value for $\dot { H } _ { \mathrm { t o t } }$ . (It is zero in the present example, but not always.) $\dot { H } _ { \mathrm { t o t , b r } }$ tells DELTAEC how much $\dot { H } _ { \mathrm { t o t } }$ to send into the branch; the balance goes into the trunk. At this early stage of model development, neither we nor DELTAEC may know the right value for this number in the present model, because the contribution of Rayleigh- and jet-driven streaming to heat convection in the part of the torus that connects the main ambient heat exchanger (segment 12) and the secondary ambient heat exchanger (segment 21) is unknown. Such streaming helps determine how much of the heat that comes from dissipation of $\dot { E }$ in the load and resonator (assumed insulated here) shows up in each of those heat exchangers. Fortunately, the performance of the apparatus is insensitive to $\dot { H } _ { \mathrm { t o t , b r } }$ : If we change its value from -1263 W to -1763, the resonance frequency, pressure amplitude, and hot temperature change by less than 0.1%, even though the heat rejected at the main ambient heat exchanger increases by 500 W and that in the secondary ambient heat exchanger decreases by the same amount. In the absence of any evidence to the contrary, it is sometimes reasonable to set

$$
\dot { H } _ { \mathrm { t o t , b r } } = \dot { E } _ { \mathrm { b r } } + \dot { N } _ { \mathrm { b r } } m w _ { m } ,\tag{6.14}
$$

and this is available as a check-box option in the TBRANCH segment. Another reasonable option here would be to add $\dot { H } _ { \mathrm { t o t , b r } }$ to the guess list, using it to allow DELTAEC to maintain equal solid temperatures in the two ambient-temperature heat exchangers. Since we are trying to minimize the number of guesses and targets right now, we choose the first option.

Now we let DELTAEC begin to consider Gedeon streaming, by checking the “Enable Ndot" box in BEGIN. This enables nonzero $\dot { N } _ { \mathrm { b r } }$ and the calculation and display of p2,0,DEC $p _ { 2 , 0 }$ throughout the model. For now, we leave $\dot { N } _ { \mathrm { b r } } = 0$ and examine the UNION at segment 24:

23   
UNION Rejoin   
8.0000 a SegNum 2.6374E+05 A Ipl Pa   
2.6374E+05 b lplSft Pa = 22A? 1.0921 B Ph(p) deg   
1.0936 c Ph(p)S deg = 22B? 0.2841 C|U| m^3/s   
325.00 d TSoft K = 22G? -86.777 D Ph(U) deg   
-0.7019 e p20DES Pa (t) 1392.0 E Htot W   
1393.2 F Edot W   
325.00 GT K   
-4060.6 H p20DEC Pa

“Allowing steady flow" has turned on the calculation of $p _ { \mathrm { 2 , 0 , D E C } }$ . Parameter e here shows that $p _ { 2 , 0 , \mathrm { D E C } } = - 0 . 7$ Pa at SOFTEND segment 8, which is the end of the TBRANCH and is supposedly reconnected to the trunk here at segment 24. However, parameter H shows that $p _ { 2 , 0 , \mathrm { D E C } } = - 4 0 6 0$ Pa here in the trunk.

There is a mismatch of 4 kPa in second-order time-averaged pressure in this UNION segment. We have already targeted $p _ { 1 }$ and $T _ { m }$ in the UNION, to satisfy acoustic and thermodynamic boundary conditions; now we must add $p _ { 2 , \ast }$ o,DEC in the UNION to the target list. Our corresponding guess will be $\dot { N } _ { \mathrm { b r } }$ in segment 1: We ask DELTAEC how much Gedeon streaming will flow around the torus, and what effects that will have on operation of the apparatus.

We make a small increase in $\dot { N } _ { \mathrm { b r } }$ and watch segment 24, to make sure p2,0,DEC changes in the right direction, to make sure we understand what we're doing. We note that DELTAEC gets lost if we change $\dot { N } _ { \mathrm { b r } }$ by 0.01 mol/s, so we make smaller changes of 0.0001 mol/s until p2,0,DEc in segments 8 and 24 are nearly matched. Then we add 1d and 24e to the guess and target lists, respectively.

Making those changes and running, we notice that the state plot of $T _ { m } ( x )$ is not smooth in the thermal buffer tube. We increase the number of steps in the numerical integration of STKDUCT (and the other integrated segments), by increasing Nint. The irregularities in $T _ { m } ( x )$ go away above Nint = 30. Running with Nint = 40, the guess-target summary becomes

GUESS Ob Od 1a 1b 1d 12e 21e   
name BEGIN:Freq BEGIN: Ipl TBRAN:Re(Zb TBRAN:Im(Zb TBRAN:Ndotb TX:HeatI TX:HeatI   
units Hz Pa Pa-s/m^3 Pa-s/m^3 mol/s W W

![[mu_66afccee_cd2df9db316d2ec0c601.jpg]]  
Figure 6.5: State plot of the TASHE example, with steady-flow calculations enabled but Gedeon streaming not properly eliminated. Solid black curve is $T _ { \mathrm { s o l i d } }$ , dashed red curve is $T _ { m }$ , and dot-dashed green curve is p2,0,DEC. The locations of the three heat exchangers are evident as short plateaus in $T _ { \mathrm { s o l i d } }$

value 86.160 2.0250E+05-2.0030E+07 1.4319E+07 0.28088 -3925.0 -704.13   
TARGET 23b 23c 23d 24e 33a 33b 34a   
name UNION:IpISO UNION:Ph(p) UNION:T\_SOF UNION:p2ODE HARDE:R(1/z HARDE:I(1/z RPN   
units Pa deg K Pa   
value 1.6818E+05 1.0268 325.00 -0.4848 0.0000 0.0000 0.000   
result 1.6818E+05 1.0268 325.00 -0.4848 -1.2258E-13-1.4742E-130.000

and the interesting characteristics of the engine become f = 86 Hz, $| p _ { 1 } | = 2 0 0$ kPa, $T _ { m , H } =$ 753 K, and $T _ { \mathrm { s o l i d } , H } = 8 4 4 ~ \mathrm { K }$ . This estimate of performance is probably much more realistic than the values of $3 1 7 \mathrm { k P a }$ , 862 K, and 955 K we found earlier, because now we have included the Gedeon streaming, which is carrying away a lot of heat from the hot heat exchanger without contributing to any thermoacoustic power generation.

To decide what to do about the Gedeon streaming, we can either look at the sign of $\dot { N } _ { \mathrm { b r } }$ or examine temperatures and $p _ { \mathrm { 2 , 0 , D E C } }$ in the state plot shown in Fig. 6.5. The regenerator is running far on the hot side of a linear temperature profile, and $\dot { N }$ is streaming through it from hot to cold. Apparently the gas diode is too tight, overcompensating for the tendency of the regenerator to stream in the direction of $\dot { E } .$ No other segments contribute significantly to p2,0,DEc. Examination of the gas-diode segments,

```csv
9
CONE gas diode plate
5.8880E-4 a AreaI m^2 2.0319E+5 AIpl Pa
0.4210 b PerimI m -0.5312 B Ph(p) deg
2.5399E-2 c Length m 8.1011E-3 C |UI m^3/s
1.1400E-4 d AreaF m^2 34.526 D Ph(U) deg
0.1850 e PerimF m 1263.0 E Htot W
5.0000E-4 f Srough 673.73 F Edot W
ideal Solid type
!- 10
MINOR minor loss here
sameas 9d a Area m^2 1.9990E+5 AIpl Pa
0.8000 b K+ -1.1955 B Ph(p) deg
7.0000E-2 c K- 8.1011E-3 C |UI m^3/s
34.526 D Ph(U) deg
```

![[mu_66afccee_ad26f9ead0f8ecfbc1fe.jpg]]

![[mu_66afccee_d1dae1f79562bceb65c3.jpg]]  
Figure 6.6: (a) The TASHE of the previous section, with a traditional hot heat exchanger between the regenerator and the thermal buffer tube. (b) The same TASHE, with the hot heat exchanger replaced by a mixing chamber, self-circulating loop, and flow straightener.

$$
\begin{array} { r l r l } { { 1 } 2 6 3 . 0 } & { { } \quad \mathsf { E } \enspace \mathrm { H t o t } } & { } & { { } \mathsf { W } } \\ { 6 5 7 . 3 9 } & { { } \quad \mathsf { F } \enspace \mathrm { E d o t } } & { } & { { } \mathsf { W } } \end{array}
$$

shows that they are qualitatively in order, with the minor-loss coefficient larger in the +x direction than in the —x direction, as necessary to fight Gedeon streaming. We surmise that the area at the small end of the gas diode, $\mathrm { 1 . 1 4 ~ c m ^ { 2 } }$ , may be too small. We tentatively increase that area about 1% (leaving its perimeter constant, since this was an adjustable slit in the experimental hardware), and we are pleased to see that DELTAEC converges on a solution with reduced streaming and higher amplitude. We use the incremental plot to continue increasing that area, watching $\dot { N } _ { \mathrm { b r } }$ and stopping the sequence when it gets close to zero. We then clear $\dot { N } _ { \mathrm { b r } }$ from the guess list and set it equal to zero, and add the gas-diode's small-end area to the guess list. A run then yields <tashe5.out> in the <Examples|SteadyFlow> folder, which shows that an area of $2 . 4 9 ~ \mathrm { c m ^ { 2 } }$ stops Gedeon streaming, and with this area the apparatus runs with $f = 8 6 \ \mathrm { H z } , | p _ { 1 } | = 3 0 0 \ \mathrm { k P a } , T _ { m , H } = 7 3 4 \ \mathrm { K }$ , and $T _ { \mathrm { s o l i d } , H } = 8 2 4 \ \mathrm { K - }$ better than before. A quick glance at the state plot shows near-linear temperature profiles in the stack and thermal buffer tube, even with Nint back down at its default value of 10.

## 6.4 Self-circulating heat exchanger

References [8] and [42] describe the use of a gas diode in a resonant loop to induce a large $\dot { N }$ for deliberate heat transfer. This gives us the freedom to design heat exchangers that are not constrained by geometrical proximity to a regenerator or stack. In the present section, we will continue to explore the use of nonzero $\ddot { N }$ in DELTAEC by replacing the hot HX in the TASHE example of the previous section with a self-circulating hot heat-transfer loop. This replacement is illustrated in Fig. 6.6, which builds on Fig. 6.4. The heat-transfer loop here bears a qualitative resemblance to the system described in Ref. [8], but the quantitative details here are entirely made up and no details have been optimized or even thoughtfully chosen. The purpose of this section is only to illustrate the development of a topologically complicated DELTAEC model.

(Note that Fig. 3 in Ref. [43] shows another, potentially better way to make a selfcirculating thermoacoustic heat exchanger.)

We began with the realization that this is going to be a complicated model, so initial simplification is important. To begin that simplification, we stripped <tashe5.out>, described at the end of the previous section, down to only a few segments in the vicinity of the hot heat exchanger:

```diff
BEGIN the setup
3.1030E+06 a Mean P Pa
85.894 b Freq Hz
325.00 c TBeg K
2.9889E+05 d Ipl Pa
-0.9265 e Ph(p) deg
1.3258E-02 f |U| m^3/s
14.065 g Ph(U) deg
-313.42 h Htot W
0.0000 i Ndot mol/s
helium Gas type
+ 1 STKSCREEN Regenerator (pg 92 book 3) (Ks frac est:pg 20 book 4)
+ 2 DUCT All regen hot end dead space (pg 92 book 3)(area is avg)
+ 3 HX HHX (pg 93 book 4) heat xfer area used/not acoustic area
+ 4 DUCT hhx dead space (pg 94 book 3) stainless used for Qdot
+ 5 JOIN thermal buffer tube end effects
+ 6 STKDUCT Straight section of pulse tube (pg 101 bk 4)
```

We set the initial conditions in BEGIN to match the conditions of the segment just upstream of the STKSCREEN in <tashe5.out>, so the integration proceeds through the rest of the model as it did in <tashe5.out>, with no need for guesses and targets.

Next, we install a hot self-circulating loop instead of the hot heat exchanger. In place of the HX, we insert, as a side-branch loop, in sequence: a quarter wavelength of duct, a gas diode, an adapter cone, a vXQ1 heat exchanger, another adapter, and a quarter-wavelength return duct. We also insert a flow straightener above the thermal buffer tube. We keep guesses and targets at a minimum: those that are necessary at the UNION and TBRANCH, and one additional guess-target pair, guessing the input heat and targeting the thermal buffer tube's final temperature.

```csv
! Examples\SteadyFlow\hotloop3.out
!Created@11:21:54 28-Jun-2020 with DeltaEC version 6.4b2.8!under win32,
using Win 6.2.9200 () under Python 2.7.9.
!-- 0
BEGIN the setup
3.1030E+6 a Mean P Pa
85.894 b Freq Hz
325.00 c TBeg K
2.9889E+5 d lpl Pa
-0.9265 e Ph(p) deg
1.3258E-2 f IUI m^3/s
14.065 g Ph(U) deg
-313.42 h Htot W
0.0000 i Ndot mol/s
helium Gas type
1
STKSCREEN Regenerator (pg 92 book 3) (Ks frac est:pg 20 book 4)
6.2070E-3 a Area m^2 2.5403E+5 AIpl Pa
0.7190 b VolPor 1.9140 BPh(p) deg
7.3000E-2 c Length m 3.2262E-2 C |U| m^3/s
4.2200E-5 d rh m -30.722 D Ph(U) deg
0.3000 e ksFrac -313.42 E Htot W
3450.8 F Edot W
325.00 G TBeg K
734.14 H TEnd K
stainless Solid type -313.42 I H2k W
!– 2
DUCT top half of mixing chamber
6.2000E-3 a Area m^2 Mstr 2.5400E+5 Alpl Pa
0.2791 b Perim m 2a 1.9031 BPh(p) deg
```

![[mu_66afccee_f209f44d5479a4fe15fb.jpg]]

<table><tr><td>1.0000E-2 c Length m ideal</td><td rowspan="3"></td><td rowspan="3">3.3175E-2 C |U| -33.132 D Ph(U) E Htot F Edot</td><td rowspan="3">m^3/s deg W W Pa</td></tr><tr><td>Solid type TBRANCH branch into hot loop 5.5883E+7 a Re(Zb) Pa-s/m^3 G 4.0267E+7</td><td>-313.42 3449.8 3</td></tr><tr><td>b Im(Zb) Pa-s/m^3 G 0.74791 d NdotBr mol/s G</td><td>2.5400E+5 AIpl 1.9031 B Ph(p) 3.6876E-3 C |UI -33.872</td></tr><tr><td rowspan="4">DUCT 7.0000E-4 9.3748E-2 4.6000 5.0000E-4 ideal !-</td><td>4 quarter-wave duct from engine to diode</td><td>7129.2 379.95 3069.8</td><td>m^3/s D Ph(U) deg E HtotBr W F EdotBr W G EdotTr W AIpl B Ph(p)</td></tr><tr><td>a Area m^2 Mstr b Perim m 4a c Length m d Srough</td><td>1.0534E+4 -163.78 5.5253E-2 -87.712 7129.2</td><td>Pa deg C |UI m^3/s D Ph(U) E Htot W F Edot W</td></tr><tr><td>Solid type 5 calculate Borda-Carnot minor loss here</td><td>70.056 0.18367</td><td>deg</td></tr><tr><td>0.0000 a G or T 1 6a 4a / - sqrd</td><td></td><td></td></tr><tr><td>4.0000E-4 5.0000E-2 b K+ sameas 5ACK-</td><td>asymmetric flow at gas diode a Area m^2</td><td>6 1.0247E+4 -173.92 5.5253E-2</td><td>AIpl B Ph(p) C|UI</td><td>A Chnge Pa deg m^3/s</td></tr><tr><td>I CONE</td><td></td><td>-87.712 7129.2 18.723</td><td>D Ph(U) E Htot F Edot</td><td>deg W W</td></tr><tr><td>sameas 6a a AreaI 7.0899E-2 0.4000 c Length m</td><td>expansion to plenum m^2 Mstr b PerimI m 7a</td><td>2.0081E+4</td><td>AIpl B Ph(p) C |UI</td><td>Pa deg m^3/s deg</td></tr><tr><td>sameas 0.4342 e PerimF m 5.0000E-4</td><td>9a d AreaF m^2 Mstr 7d</td><td>-176.63 5.0461E-2 -87.793</td><td>D Ph(U) E Htot</td><td>W W</td></tr><tr><td>ideal !-</td><td>f Srough Solid type</td><td>7129.2 10.238</td><td>F Edot</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>A Chnge</td></tr><tr><td>RPN 5.0000</td><td>watch that angle</td><td>8</td><td></td><td></td></tr><tr><td>7e 7b - pi !--</td><td>a G or T / 7c / atan plenty of room for heat transfer</td><td>16.125</td><td></td><td></td></tr><tr><td>VXQ1 1.5000E-2</td><td></td><td>9</td><td></td><td></td></tr><tr><td>0.4000</td><td>a Area m^2</td><td>1.7545E+4</td><td></td><td></td></tr><tr><td>0.1000</td><td>b GasA/A</td><td>-176.03</td><td>AIpl B Ph(p)</td><td>Pa</td></tr><tr><td>1.0000E-2</td><td>c SolA/A</td><td>5.7679E-2</td><td>E Htot</td><td>deg</td></tr><tr><td>1.0000E-2</td><td>d rh m</td><td></td><td>C IUI</td><td></td></tr><tr><td>6.0000</td><td></td><td></td><td>92.124</td><td>m^3/s</td></tr><tr><td>1.0000E-2</td><td>e LenTS1 m</td><td>1.0034E+4</td><td></td><td>D Ph(U) deg</td></tr><tr><td></td><td>f Len P1 m</td><td></td><td></td><td>W</td></tr><tr><td>2904.3</td><td>G</td><td>-16.283 736.99 923.98</td><td></td><td></td></tr><tr><td></td><td>g LenTS2 m</td><td>379.95</td><td>I H2k</td><td>F Edot</td></tr><tr><td>1.0000</td><td></td><td></td><td></td><td>W</td></tr><tr><td></td><td>h HeatP1 W</td><td></td><td></td><td>G TSolBeg P1 K</td></tr><tr><td>stainless</td><td>i FracQN</td><td></td><td></td><td>H TSolEnd P1 K</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>!-</td><td>Solid type</td><td></td><td></td><td>W</td></tr><tr><td>CONE</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>adapt between heat exchanger and quarter-wave tube</td><td>10</td><td></td><td></td></tr><tr><td>sameas</td><td></td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>7d a AreaI m^2</td><td></td><td>1.0851E+4</td><td></td></tr><tr><td>sameas</td><td>7e b PerimI m</td><td></td><td>-174.31</td><td>AIpl Pa</td></tr><tr><td>sameas</td><td>7c c Length m</td><td></td><td>6.2114E-2 C</td><td>B Ph(p) deg D Ph(U)</td></tr><tr><td>sameas f</td><td>11a d AreaF m^2</td><td></td><td>92.244 1.0034E+4</td><td>|UI m^3/s E Htot</td></tr><tr><td>5.0000E-4</td><td>11b e PerimF m</td><td></td><td>-20.27</td><td>deg F Edot</td></tr><tr><td>ideal</td><td>Srough</td><td></td><td></td><td>W</td></tr><tr><td>! -</td><td>Solid type</td><td></td><td></td><td>W</td></tr><tr><td>DUCT</td><td>quarter wave connection tube</td><td>11</td><td></td><td></td></tr><tr><td>sameas</td><td></td><td></td><td></td><td></td></tr><tr><td>sameas</td><td>4a a Area m^2</td><td></td><td>2.5400E+5 AIpl</td><td>Pa</td></tr><tr><td>5.0000</td><td>4b b Perim m</td><td></td><td>1.9031</td><td>B Ph(p) deg m^3/s</td></tr><tr><td>sameas</td><td>c Length m</td><td></td><td>6.2065E-3 C</td><td></td></tr><tr><td></td><td>4d d Srough</td><td></td><td></td><td>|UI</td></tr><tr><td></td><td></td><td></td><td>124.46</td><td>D Ph(U) deg</td></tr><tr><td>ideal</td><td></td><td></td><td>1.0034E+4</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>E Htot W</td></tr><tr><td></td><td>Solid type</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>-424.16</td><td>F Edot W</td></tr><tr><td>!-</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>12</td><td></td><td></td></tr><tr><td>SOFTEND</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.0000 a Re(z)</td><td>end of the branch; this will reconnect to trunk at UNION</td><td></td><td>2.5400E+5</td><td>AIpl Pa</td></tr></table>

<table><tr><td></td><td></td><td></td><td>1.0034E+4 -424.16 -5.3226 -8.3368 920.96 1635.8</td><td>E Htot F Edot G Re(z) H Im(z) I T J p20DEC Pa</td><td>D Ph(U) deg W W K</td></tr><tr><td colspan="6">UNION reconnect the &quot;final&quot; end of</td></tr><tr><td>12</td><td>a SegNum</td><td></td><td>the loop 2.5400E+5</td><td>here A |pl B Ph(p)</td><td>Pa deg</td></tr><tr><td>sameas</td><td>12A b lpISft Pa</td><td>=13A</td><td>1.9031 2.3872E-2</td><td>IUI</td><td>m^3/s</td></tr><tr><td>sameas</td><td>12B c Ph(p)S deg</td><td></td><td>=13B</td><td>C Ph(U)</td><td>deg</td></tr><tr><td>sameas</td><td>12I d TSoft</td><td>K</td><td>=13H</td><td>-27.33 D E Htot</td><td>W</td></tr><tr><td>sameas</td><td>12J e p20DES Pa</td><td></td><td>2590.9 2645.6</td><td>F Edot 734.14</td><td>W K</td></tr><tr><td>1</td><td></td><td></td><td>1635.8 14</td><td>GT H p20DEC Pa</td><td></td></tr><tr><td>DUCT</td><td>bottom half of mixing chamber</td><td></td><td></td><td></td><td>Pa</td></tr><tr><td>sameas sameas</td><td>2a a Area</td><td>m^2</td><td>2.5397E+5</td><td>AIpl</td><td>deg</td></tr><tr><td>sameas</td><td>2b b Perim</td><td>m</td><td>1.8948</td><td>B Ph(p)</td><td>m^3/s</td></tr><tr><td></td><td>2c c Length m</td><td></td><td>2.4714E-2 -30.681</td><td>C IUI D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>2590.9</td><td>E Htot</td><td>W</td></tr><tr><td>ideal !-</td><td></td><td>Solid type</td><td>2644.6</td><td>F Edot</td><td>W</td></tr><tr><td>SX</td><td>flow straightener (no heat input)</td><td></td><td>15</td><td></td><td></td></tr><tr><td>sameas</td><td>14a a Area</td><td>m^2</td><td>2.5380E+5</td><td>AIpl</td><td>Pa deg</td></tr><tr><td>0.6500</td><td>b VolPor</td><td></td><td>1.9101</td><td>BPh(p)</td><td>m^3/s</td></tr><tr><td>5.0000E-3</td><td>c Length m</td><td></td><td>2.4866E-2</td><td>C |UI D Ph(U)</td><td>deg</td></tr><tr><td>5.0000E-4 0.0000</td><td>d rh</td><td>m</td><td>-32.06 2590.9</td><td>E Htot</td><td>W</td></tr><tr><td>0.0000</td><td>f SolidT K</td><td>e HeatIn W</td><td>2616.9</td><td>F Edot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>734.14</td><td>G GasT</td><td>K K</td></tr><tr><td>ideal</td><td></td><td></td><td>734.14 2590.9</td><td>H SolidT I H2k</td><td>W</td></tr><tr><td>!- JOIN</td><td></td><td>Solid type</td><td>16</td><td></td><td></td></tr><tr><td></td><td></td><td>thermal buffer tube end effects</td><td>2.5380E+5</td><td>Alpl</td><td>Pa deg</td></tr><tr><td></td><td></td><td></td><td></td><td>1.9101 B Ph(p) C</td><td>m^3/s</td></tr><tr><td></td><td></td><td></td><td>2.4293E-2</td><td>|UI</td><td></td></tr><tr><td></td><td></td><td></td><td>-32.06</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>2590.9</td><td>E Htot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>2556.6</td><td>F Edot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>734.14</td><td>G TBeg</td><td>K</td></tr><tr><td>!</td><td></td><td></td><td>733.64</td><td></td><td>K</td></tr><tr><td>STKDUCT</td><td></td><td></td><td>17</td><td>H TEnd</td><td></td></tr><tr><td>7.0000E-3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.2963</td><td>a Area</td><td>Straight section of pulse tube (pg 101 bk 4) m^2</td><td>2.5152E+5</td><td></td><td>Pa</td></tr><tr><td>0.2400</td><td>b Perim</td><td></td><td></td><td>Alpl</td><td>deg</td></tr><tr><td>1.1600E-3</td><td>c Length m</td><td>m</td><td></td><td>1.6470 BPh(p)</td><td>m^3/s</td></tr><tr><td></td><td></td><td>d WallA m^2</td><td>6.1290E-2</td><td>C IUI</td><td></td></tr><tr><td></td><td></td><td></td><td>-69.092</td><td>D Ph(U)</td><td>deg</td></tr><tr><td></td><td></td><td></td><td>2590.9 2542.6</td><td>E Htot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>733.64</td><td>F Edot</td><td>W</td></tr><tr><td></td><td></td><td></td><td>300.00</td><td>G TBeg</td><td>K</td></tr><tr><td>stainless</td><td></td><td></td><td></td><td>H TEnd</td><td>K</td></tr><tr><td>!-</td><td></td><td>Solid type</td><td>2590.9</td><td>I H2k</td><td>W</td></tr><tr><td>RPN</td><td></td><td></td><td>18</td><td></td><td></td></tr><tr><td></td><td></td><td>temperature target</td><td></td><td></td><td></td></tr><tr><td>300.00</td><td>a =A?</td><td></td><td>300.00</td><td></td><td></td></tr><tr><td>Tm</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GUESS</td><td>3a</td><td>3b</td><td>3d</td><td>9h</td><td></td></tr><tr><td>name</td><td></td><td>TBRAN:Re(Zb TBRAN:Im(Zb TBRAN:Ndotb</td><td></td><td>VXQ1:HeatP</td><td></td></tr><tr><td>units</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Pa-s/m^3</td><td>Pa-s/m^3</td><td>mol/s</td><td></td><td></td></tr><tr><td>value</td><td>5.5883E+07</td><td>4.0267E+07</td><td>0.7479</td><td>2904.3</td><td></td></tr><tr><td>TARGET</td><td>13b</td><td>13c</td><td>13e 18a</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>name</td><td></td><td>UNION:IpISO UNION:Ph(p)</td><td>UNION:p20DEC RPN:Targe</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>units</td><td>Pa</td><td>deg</td><td>Pa</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1635.8 300.00</td><td></td><td></td></tr><tr><td>value</td><td>2.5400E+05</td><td>1.9031</td></table>

Several features that have not been previously encountered or discussed in the Users Guide are displayed in this file. Details about each of these features are given in Chapter 10.

Segment MINOR is employed here with unequal minor-loss coefficients, as appropriate for an asymmetrical geometry and as necessary to create a pumping effect to move $\dot { N } \simeq 0 . 8$ mole/sec around the loop [42]. Figure 6.7 shows the state plot of $p _ { \mathrm { 2 , 0 , D E C } }$ around the loop. The rise near $x = 4$ m is the abrupt effect of the gas diode's MINOR segment. The gradual decreases elsewhere are the pressure gradients in the DUCTs (and, much smaller, in the VXQ1), which the gas-diode pump is overcoming. The gradient $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ varies along each DUCT, despite the constancy of the area and flow rate, because of the nonlinear interaction between $U _ { 1 }$ and $\dot { N }$ , which increases $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ where $| U _ { 1 } |$ is largest. The nature of that nonlinear interaction is controlled in part by the value of the roughness parameter in DuCT segments 4 and 11. As described in detail in Section 10.1.1, the interaction between turbulent steady flow and turbulent oscillating flow is also governed by which of the Optimistic, Average, or Pessimistic boxes are checked in a DUCT. The p2oDEC target in the UNION ensures that $p _ { 2 , 0 , \mathrm { D E C } } ( x = 1 6 . 5 \mathrm { m } ) = p _ { 2 , 0 , \mathrm { D E C } } ( x = 0 )$ . Recall that the zero of $p _ { \mathrm { 2 , 0 , D E C } }$ is set arbitrarily in the BEGIN segment, so the vertical offset of this graph is meaningless for the present discussion; it only indicates $\Delta p _ { \mathrm { 2 , 0 , D E C } }$ across the regenerator when $\dot { N } = 0$ in the regenerator.

![[mu_66afccee_f74dceeded25fba1b5d9.jpg]]  
Figure 6.7: Second-order head-loss pressure vs x in the heat-exchange loop. The abrupt rise marks the location of the gas diode.

Segment 9, VXQ1, is one of the family of “variable" heat exchanger, VX, segments. The other types of heat exchanger segments—HX, TX, SX, and PX—are assumed to be short, and to have x-independent solid and gas temperatures. The VX\*\* segments are numerically integrated with Nint steps, so they can be long. VXT1 and VXT2 are intended to model long heat exchangers with shell-side heat transfer such that the solid surfaces are held essentially isothermal. The gas temperature $T _ { m } ( x )$ and heat transfer per unit length ${ \dot { q } } ( x )$ are obtained numerically in the VXT\*\* segments. VXQ1 and vXQ2 are intended to model long heat exchangers with shell-side heat transfer such that the heat input per unit length is independent of x. The gas temperature $T _ { m } ( x )$ and and solid temperature $T _ { \mathrm { s o l i d } } ( x )$ are obtained numerically in the $\boldsymbol { \mathrm { V X Q } } * *$ segments. vxQ2 and vXT2 allow for two-part heat exchangers, such as heat exchangers with two passes on the shell side. Additional lengths for tubesheets, where no heat transfer occurs, are built into both ends of the VX\*\* segments. For more details, see Section 10.7.3. In the present example, Fig. 6.8 shows temperatures around the loop. Outside of the heat exchanger, gas and solid temperatures are equal, as usual. Inside the heat exchanger, $T _ { m }$ increases linearly with x because this is an ideal gas flowing though a VXQ1 segment, with $c _ { p }$ and $\dot { q }$ independent of x. The difference $T _ { \mathrm { s o l i d } } - T _ { m }$ peaks in the center of the VX, where $| U _ { 1 } |$ is the smallest and hence turbulent heat transfer is the least effective at

![[mu_66afccee_b1e334333c1f5ae79aab.jpg]]  
Figure 6.8: Temperatures around the hot loop. Solid black line, solid temperature. Dashed red line, gas temperature. The velocity-dependent gas-solid heat-transfer coefficient in vXQ1 is evident in the difference between the two curves. (Nint = 20 for this plot.)

transferring heat from the solid to the gas.

The logistical segments in <hotloop3.out> also have a few peculiar features. In the BEGIN, $\dot { H } _ { \mathrm { t o t } }$ is set to the value that it had just upstream of the regenerator in <tashe5. out>, and $\dot { N }$ is enabled and set to zero, to turn on $p _ { \mathrm { 2 , 0 , D E C } }$ and steady-flow calculations in the rest of the model. $\dot { N }$ is, of course, zero or negligible in the regenerator, since <tashe5. out> properly suppressed Gedeon streaming with its gas diode. However, $\dot { N } _ { \mathrm { b r } }$ in the TBRANCH is large. DELTAEC adjusts this guess to hit the $p _ { \mathrm { 2 , 0 , D E C } }$ target at the UNION. We don't know exactly what $\dot { H } _ { \mathrm { t o t , b r } }$ should be, because we $\mathrm { d o n ^ { \prime } t }$ know exactly how much heat might be convected into the loop by $\dot { N }$ here, but the measurements reported in Ref. [8] indicate that any such convected heat is much smaller than what is convected out of such a loop at the other end, so we simply set $\dot { H } _ { \mathrm { t o t , b r } } = \dot { E } _ { \mathrm { b r } }$ in the TBRANCH. At the UNION, we do not use the temperature target, because this would force the gas temperatures at both ends of the loop to be equal, which would contradict the entire purpose of the circulating loop. Instead, we essentially let the 919-K gas coming out of the SOFTEND of the loop pour into the UNION where $T _ { m } = 7 3 2 \mathrm { ~ K ~ }$ . We rely on the energy-conserving feature of DELTAEC's UNION to add the heat picked up in the loop into the $\dot { H } _ { \mathrm { t o t } }$ leaving the UNION.

Next, as shown in Fig. 6.9, we combine <hotloop3.out> and <tashe5.out>, to make a complete DELTAEC model of the TASHE, the hot self-circulating heat-exchange loop, and the resonator. We run <tashe5.out>, Kill its traditional hot heat exchanger, and then copy and paste the appropriate segments from <hotloop3.out>. We fix a few things that DELTAEC did not do correctly. A run fails to converge, so we Restore guessez and then clear all guesses and targets, intending to introduce them one pair at a time. With no guesses and targets, a run shows mostly sensible results, except at the HARDEND at the end of the model, where acoustic power is flowing in, in the -x direction. We introduce guesses and targets beginning with the four each that were involved in the hot loop, since they are closest to being on-target already. Then we add three of the four UNION targets that were used in <tashe5.out> (skipping the temperature target for the moment), and three corresponding guesses, two $Z _ { \mathrm { b r } }$ in the segment-1 TBRANCH and the third being the slot width in the gas diode in segment 9. At this point, we have 8 targets and 8 guesses, and each change we make is requiring small, gentle steps. We remove the temporary RPN target we had been using in <hotloop3.out> to keep the temperature near ambient at the end of <hotloop3.out>, adding instead the segment-35 UNION temperature target. We add frequency as a guess, and Im $\left( 1 / z _ { n } \right)$ at the HARDEND as a target. Pause to think. In <tashe5.out>, our perspective was to give the engine a known hot heat input, and observe performance. Here, we are currently guessing the hot heat input, because that is what we did in <hotloop3.out>. Clear that guess, and try guessing the main ambient heat instead. With that change, DELTAEC still tolerates changes to variables reasonably well, given the fact that we have 9 targets and 9 guesses. In <tashe5.out>, we injected 3700 W of hot heat; let's increase the heat in our hot loop to the same value here, for a fair comparison to the earlier model. We begin incremental plotting to higher hot heat, in 5-W steps which are small enough that DELTAEC stays converged at each step. Along the way, we notice that the $\dot { E }$ flowing in at the as-yet-incompletely-targeted HARDEND is steadily decreasing, approaching zero at about 3500 W. We stop there, and add the HARDEND's $\operatorname { R e } [ 1 / z _ { n } ]$ to the target list and the BEGIN's $\left| p _ { 1 } \right|$ to the guess list, and resume our increase of $\dot { Q } _ { H }$ up to 3700.

![[mu_66afccee_6f998224e69bc999af2a.jpg]]  
Figure 6.9: Sketch of the <combo.out> model. The TASHE feedback loop hangs to the left of the trunk, and the hot self-circulating heat exchanger loop hangs to the right.

The resulting file, <combo2.out>, appears below. Whereas <tashe5.out> ran at an amplitude (in segment 0) of 300 kPa, <combo2.out> runs at 314 kPa. However, <tashe5.out> required only $T _ { \mathrm { s o l i d } , H } = 8 2 4$ K; <combo2.out> requires solid temperatures from 1336 K to 1420 K.

This example may not yet be practical, but it does demonstrate the creation of a DELTAEC model for a topologically complicated apparatus with 10 targets and 10 guesses.

GUESS Ob 1a 2a 2b 10d 13e   
name BEGIN:Freq RPN: G TBRAN:Re(Zb TBRAN:Im(Zb CONE:AreaF TX:HeatI   
units Hz Pa-s/m^3 Pa-s/m^3 m^2 W   
value 90.040 -3.3293 -1.4489E+07 1.5859E+07 1.8906E-04-2086.3   
GUESS 17a 17b 17d 33e   
name TBRAN:Re(Zb TBRAN:Im(Zb TBRAN:Ndotb TX:HeatIn   
units Pa-s/m^3 Pa-s/m^3 mol/s W   
value 1.4855E+06 7.5698E+06 2.1335 -400.82   
TARGET 27b 27c 27e 35b 35c 35d   
name UNION:IpISO UNION:Ph(p) UNION:p2ODEC UNION:IpISO UNION:Ph(p) UNION:T\_SOF   
units Pa deg Pa Pa deg K   
value 2.5537E+05 1.5555 11.006 2.5512E+05 1.1012 325.00   
result 2.5537E+05 1.5555 11.006 2.5512E+05 1.1012 325.00   
TARGET 35e 45a 45b 46a   
name UNION:p2ODEC HARDE:R(1/z HARDE:I(1/z   
units Pa   
value -0.46756 0.0000 0.0000 0.0000   
result -0.46756 -1.3244E-14 3.5147E-12 0.0000

```csv
! Examples\SteadyFlow\combo2.out
!Created@11:28:04 14-Dec-2022 with DeltaEC version 6.4b2.9!under win32,
using Win 6.2.9200 () under Python 2.7.9.
!-- 0
BEGIN the setup
3.1030E+6 a Mean P Pa
90.040 b Freq Hz G
325.00 c TBeg K
3.1436E+5 d Ipl Pa
0.0000 e Ph(p) deg
0.0000 f |UI m^3/s
0.0000 g Ph(U) deg
0.0000 i Ndot mol/s
helium Gas type
!-- 1
RPN use this to de-sensitize the model to RK4 adjusting p1
-3.3293 a G or T G 3.1436E+5 A Pa
```

<table><tr><td rowspan=1 colspan=1>p1 inp + =p12TBRANCH   Split up the flow-1.4489E+7a Re(Zb)Pa-s/m^3 G         3.1436E+5 A|pl   Pa1.5859E+7b Im(Zb) Pa-s/m^3 G             0.0000B Ph(p) deg0.0000 d NdotBr mol/s              1.4634E-2C IUI   m^3/s-132.41   D Ph(U) deg-1551.4   E HtotBr W-1551.4   F EdotBr W1551.4    G EdotTr W+ 3 DUCT      180 bend plus brass connecting flange (pg 27 book 4)+4 CONE      4&quot; to 3&quot; Concentric reducer (pg 36 book 4)+5 DUCT      3&quot; FB Duct - Length given in concept.skf+ 6 CONE      3.5&quot; to 3&quot; Long radius reducing elbow (pg 36 book 4)+7 MINOR     minor loss, small end of elbow+8 DUCT      FB connector/part of tee (Pg 55 book 4 concept.skf)9</td></tr><tr><td rowspan=1 colspan=1>SOFTEND   End of feedback branch0.0000 a Re(z)                      2.5512E+5 AIpl   Pa0.0000 b Im(z)                         1.1015B Ph(p) deg0.0000 c Htot  W                     0.21452C IUI   m^3/s-92.463  D Ph(U) deg-1551.4   E Htot  W-1701.3    F Edot  W-9.4135E-2G Re(z)1.5111 H Im(z)325.00   I T     K-0.46756   J p20DEC Pa10</td></tr><tr><td rowspan=1 colspan=1>CONE      gas diode plate5.8880E-4a AreaIm^2                3.1604E+5AIpl   Pa0.4210b PerimI m                 -0.41775   B Ph(p) deg2.5399E-2c Length m                  1.4346E-2 C |U|   m^3/s1.8906E-4d AreaF m^2     G            46.713  D Ph(U) deg0.1850e PerimF m                  1551.4    E Htot  W5.0000E-4f Srough                    1542.3   F Edot Wideal          Solid type11</td></tr><tr><td rowspan=1 colspan=1>MINOR     minor loss heresameas10d a Area m^2                3.1274E+5AIpl   Pa0.8000 b K+                           -1.0738B Ph(p) deg7.0000E-2 c K-                         1.4346E-2C |UI   m^3/s46.713  D Ph(U) deg1551.4   E Htot W1507.2   F Edot  W12</td></tr><tr><td rowspan=1 colspan=1>DUCT      jetting space6.8250E-3a Area m^2                3.1280E+5AIpl   Pa0.2930b Perimm                    -1.0867 B Ph(p) deg1.9000E-2c Length m                  1.1441E-2C IUI   m^3/s5.0000E-4d Srough                      31.615  D Ph(U) deg1551.4   E Htot  Wideal          Solid type              1505.7    F Edot  W!-                                 13</td></tr><tr><td rowspan=1 colspan=1>TX        Main room temp water HX(pg90 book 3)6.6580E-3a Area m^2                3.1297E+5AIpl   Pa0.2275b GasA/A                      -1.1585B Ph(p) deg2.0400E-2c Length m                  1.0793E-2C IUI   m^3/s1.2700E-3d radius m                    26.732  D Ph(U) deg-2086.3   e HeatIn W       G         -534.91   E Htot  W300.00   f SolidT K                  1492.8   F Edot  W325.00   G GasT K284.54   H SolidT Kstainless          Solid type           -534.91   I H2k   W1                                  14</td></tr><tr><td rowspan=1 colspan=1>DUCT      Regen cold end dead space due to ribs(pg 91 book 3)4.9700E-3a Area m^2                3.1298E+5 A|pl   Pa0.7400b Perimm                    -1.1614B Ph(p) deg3.1750E-3c Length m                  1.0545E-2C IUI   m^3/s24.128  D Ph(U) deg-534.91   E Htot  Wstainless          Solid type          1492.1   F Edot W15</td></tr><tr><td rowspan=1 colspan=1>STKSCREENRegenerator (pg 92 book 3)(Ks frac est:pg20 book 4)6.2070E-3a Area m^2                2.5539E+5 A|pl   Pa0.7190b VolPor                        1.5642 B Ph(p) deg7.3000E-2c Length m                  4.1269E-2C IUI   m^3/s4.2200E-5d rh    m                   -24.558  D Ph(U)deg0.3000e ksFrac                     -534.91   E Htot  W4731.5   F Edot W</td></tr></table>

<table><tr><td colspan="2"></td><td rowspan="2">325.00 1330.7 -534.91</td><td rowspan="2">G TBeg H TEnd I H2k</td><td rowspan="2">K K W</td></tr><tr><td>stainless</td><td>Solid type 16</td></tr><tr><td colspan="2">DUCT 6.2000E-3 a Area</td><td>top half of mixing chamber</td><td></td><td></td></tr><tr><td colspan="2"></td><td>Mstr 2.5537E+5</td><td>AIpl B Ph(p)</td><td>Pa</td></tr><tr><td colspan="2">0.2791 b Perim 1.0000E-2</td><td>16a</td><td>1.5557</td><td>deg</td></tr><tr><td colspan="2">c Length m 6.0000E-4</td><td></td><td>4.2054E-2 C IUI</td><td>m^3/s</td></tr><tr><td colspan="2">d Srough</td><td></td><td>-26.702 D Ph(U)</td><td>deg</td></tr><tr><td colspan="2">stainless Solid type</td><td>-534.91 4729.8</td><td>E Htot F Edot</td><td>W</td></tr><tr><td colspan="2">TBRANCH branch into hot loop</td><td>17</td><td></td><td>W</td></tr><tr><td colspan="2">1.4855E+6</td><td></td><td></td><td>Pa</td></tr><tr><td colspan="2">a Re(Zb) Pa-s/m^3 G 7.5698E+6 b Im(Zb)</td><td></td><td>2.5537E+5 AIpl 1.5557 B Ph(p)</td><td>deg m^3/s</td></tr><tr><td colspan="2">Pa-s/m^3 G 606.94 c HtotBr W 2.1335 d NdotBr mol/s G</td><td>3.3104E-2</td><td>C IUI</td><td>deg</td></tr><tr><td colspan="2"></td><td>-77.341 606.94</td><td>D Ph(U) E HtotBr W</td><td></td></tr><tr><td colspan="2">+ 18 DUCT</td><td>813.99 3915.8</td><td></td><td>F EdotBr W G EdotTr W</td></tr><tr><td colspan="2">+ 19 RPN</td><td>quarter-wave duct from engine to diode calculate Borda-Carnot minor loss here</td><td></td><td></td></tr><tr><td colspan="2">+ 20 MINOR + 21 CONE</td><td>asymmetric flow at gas diode expansion to plenum</td><td></td><td></td></tr><tr><td colspan="2">+ 22 RPN</td><td>watch that angle 23</td><td></td><td></td></tr><tr><td colspan="2">!- VXQ1</td><td>plenty of room for heat transfer</td><td></td><td></td></tr><tr><td colspan="2">1.5000E-2 a Area m^2</td><td>2.9185E+4</td><td>AIpl</td><td>Pa</td></tr><tr><td colspan="2">0.4000 b GasA/A</td><td>-174.35</td><td>B Ph(p)</td><td>deg</td></tr><tr><td colspan="2">0.1000 C SolA/A</td><td>7.4359E-2</td><td>C |U|</td><td>m^3/s</td></tr><tr><td colspan="2">1.0000E-2 d rh m</td><td>92.715 4306.9</td><td>D Ph(U) E Htot</td><td>deg W</td></tr><tr><td colspan="2">1.0000E-2 e LenTS1 m 6.0000 f Len P1 m</td><td>-55.587</td><td>F Edot</td><td>W</td></tr><tr><td colspan="2">1.0000E-2 g LenTS2 m</td><td>1336.0</td><td></td><td>G TSolBeg P1 K</td></tr><tr><td colspan="2">3700.0 h HeatP1 W</td><td>1420.2</td><td></td><td>H TSolEnd P1 K</td></tr><tr><td colspan="2">1.0000 i FracQN</td><td>-4.5102E+4</td><td>I H2k</td><td>W</td></tr><tr><td colspan="2">stainless Solid type + 24 CONE adapt between heat exchanger and quarter-wave tube</td><td></td><td></td><td></td></tr><tr><td colspan="2">+ 25 DUCT quarter wave connection tube 26</td><td></td><td></td><td></td></tr><tr><td colspan="2">SOFTEND 0.0000 a Re(z) 0.0000 b Im(z) 0.0000 c Htot</td><td>end of the branch; this will reconnect</td><td>to 2.5537E+5 A |pl 1.5557 B Ph(p)</td><td>trunk at UNION Pa deg</td></tr><tr><td colspan="2"></td><td>2.9250E-2 103.93</td><td>C IUI D Ph(U) 4306.9 E Htot F Edot</td><td>m^3/s deg W</td></tr><tr><td colspan="2"></td><td>-800.6 -0.56049</td><td>G Re(z) -2.5539 H Im(z)</td><td>W</td></tr><tr><td colspan="2"></td><td>1414.1 11.023</td><td>I T Jp20DEC Pa</td><td>K</td></tr><tr><td colspan="2">UNION reconnect the "final" end of the loop here</td><td>27</td><td></td><td></td></tr><tr><td colspan="2">26 a SegNum</td><td>2.5537E+5</td><td>A |pl</td><td>Pa</td></tr><tr><td colspan="2">sameas 26A b IpISft Pa</td><td>=27A 1.5557</td><td>B Ph(p)</td><td>deg</td></tr><tr><td colspan="2">sameas 26B c Ph(p)S deg sameas 26I d TSoft K</td><td>=27B 4.7834E-2</td><td>C |U|</td><td>m^3/s</td></tr><tr><td colspan="2">26J e p20DES Pa</td><td>60.889</td><td>D Ph(U)</td><td>deg</td></tr><tr><td colspan="2">sameas =27H</td><td>3165.1</td><td>E Htot</td><td>W</td></tr><tr><td colspan="2"></td><td>3115.2</td><td>F Edot</td><td>W</td></tr><tr><td colspan="2"></td><td>1330.7</td><td>GT</td><td>K</td></tr><tr><td colspan="2"></td><td>11.023</td><td>H p20DEC Pa</td><td></td></tr><tr><td colspan="2"></td><td>28</td><td></td><td></td></tr><tr><td colspan="2">DUCT bottom half of mixing chamber</td><td></td><td></td><td>Pa</td></tr><tr><td colspan="2">sameas 16a a Area m^2</td><td>2.5541E+5</td><td>AIpl</td><td>deg</td></tr><tr><td colspan="2">sameas 16b b Perim m</td><td>1.5499</td><td>B Ph(p) C IUI</td><td>m^3/s</td></tr><tr><td colspan="2">sameas 16c c Length m</td><td>4.6334E-2</td><td></td><td>deg</td></tr><tr><td colspan="2"></td><td>59.802</td><td>D Ph(U)</td><td>W</td></tr><tr><td colspan="2"></td><td></td><td>E Htot</td><td>W</td></tr><tr><td colspan="2">ideal Solid type</td><td>3165.1</td><td>F Edot</td><td></td></tr><tr><td colspan="2"></td><td>3113.5</td><td></td><td></td></tr><tr><td colspan="2">!-</td><td>29</td><td></td><td>Pa</td></tr><tr><td colspan="2">SX flow straightener (no heat input)</td><td></td><td></td><td></td></tr><tr><td colspan="2">sameas 28a a Area m^2</td><td></td><td>AIpl</td><td>deg</td></tr><tr><td colspan="2"></td><td>2.5525E+5</td><td></td><td>m^3/s</td></tr><tr><td colspan="2">0.6500 b VolPor</td><td>1.4738</td><td>B Ph(p) 4.5510E-2 C IUI 59.398 D Ph(U)</td><td>deg E Htot W</td></tr><tr><td< table=""></td<></tr><tr><td colspan="4">!- 30 JOIN thermal buffer tube end effects 2.5525E+5 1.4738 4.4835E-2</td></tr><tr><td colspan="4">59.398 D Ph(U) deg 3165.1 E Htot W 3038.7 F Edot W</td></tr><tr><td>STKDUCT Straight section of pulse tube (pg 101 bk 4) 7.0000E-3 a Area 0.2963</td><td>31 m^2 Mstr b Perim m 31a c Length m</td><td>1330.7 1335.2 2.5557E+5 1.2883 2.5064E-2 -19.922</td><td>G TBeg K H TEnd K A |pl Pa BPh(p) deg C IUI m^3/s D Ph(U) deg E Htot</td></tr><tr><td colspan="4">1.1600E-3 d WallA m^2</td></tr><tr><td>stainless !</td><td>Solid type 32</td><td>3165.1 2985.9 F 1335.2 G TBeg 321.72 H TEnd 3165.1 I H2k</td><td>W Edot W K K W Pa</td></tr><tr><td>JOIN</td><td>thermal buffer tube end effects</td><td>2.5557E+5 1.2883 2.4411E-2 -19.922 3165.1 2908.0</td><td>AIpl B Ph(p) deg C IUI m^3/s D Ph(U) deg E Htot W F Edot W G TBeg K</td></tr><tr><td colspan="4">H TEnd K 33 TX</td></tr><tr><td rowspan="4">6.6580E-3 a Area m^2 0.2690 b GasA/A</td><td>Small water Xger</td><td>325.00</td><td rowspan="4">AIpl Pa deg m^3/s deg</td></tr><tr><td>c Length m</td><td>2.5541E+5</td></tr><tr><td></td><td>1.2107 B Ph(p) 2.4587E-2 C |UI</td></tr><tr><td>-21.096</td><td>D Ph(U) E Htot</td></tr><tr><td rowspan="5">290.00 ideal</td><td>e HeatIn W G f SolidT K</td><td>2764.3 2904.9 325.00</td><td>W F Edot W G GasT K</td></tr><tr><td></td><td>301.24</td><td>H SolidT K I H2k W AIpl</td></tr><tr><td>Solid type</td><td>2764.3</td><td>Pa deg m^3/s</td></tr><tr><td>PT connector (see pg 55 book 4 and concept.skf) 6.2070E-3 a Area m^2 0.2790 b Perim m 5.1000E-2</td><td>34 2.5512E+5</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td colspan="4">35</td></tr><tr><td rowspan="4">6.0000E-4 stainless 1-</td><td>c Length m</td><td>1.1015 2.9105E-2 -37.478</td><td>B Ph(p) C |UI D Ph(U) E Htot F Edot</td></tr><tr><td>d Srough</td><td></td><td></td></tr><tr><td>Solid type</td><td>2764.3 2902.3</td><td>deg W W</td></tr><tr><td>Rejoin</td><td></td><td></td></tr><tr><td colspan="4">sameas</td></tr><tr><td rowspan="5">9 sameas 9A b lpISft Pa sameas</td><td>a SegNum</td><td>2.5512E+5</td><td>AIpl B Ph(p)</td><td></td></tr><tr><td></td><td></td><td>1.1015 C IUI</td><td>Pa deg m^3/s deg W</td></tr><tr><td>9B c Ph(p)S deg</td><td>=35A =35B</td><td>0.23245 D Ph(U) E Htot</td><td>W</td></tr><tr><td>9I d TSoft K 9J e p20DES Pa</td><td>=35G =35H</td><td>-86.577 F Edot</td><td>K</td></tr><tr><td></td><td></td><td>1212.9 1200.9 325.00 GT -0.46756</td><td>H p20DEC Pa</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">+ 36 ANCHOR assume resonator and load can dump heat as needed + 37 DUCT Section of 3.5" tee</td></tr><tr><td colspan="4">+ 38 CONE 3.5" to 4" cone to adapt to resonator (pg 93 book 4) + 39 DUCT Initial section of resonator</td></tr><tr><td colspan="4">+ 40 BRANCH RC dissipator Continuation of resonator</td></tr><tr><td colspan="4">+ 41 DUCT + 42 CONE 7 degree cone - 10.02" final diameter</td></tr><tr><td colspan="4">+ 43 DUCT 10" duct P8 + 44 SURFACE end cap of resonator</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">8.4959E+4</td></tr><tr><td colspan="4">-178.72</td></tr><tr><td colspan="4">4.5867E-12</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">0.0000 d Ndot mol/s</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">0.0000 b I(1/z) =45H</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">45</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">HARDEND end of duct 0.0000 a R(1/z) =45G</td></tr></table>

!- 46   
RPN energy closure   
0.0000 a =A? 0.0000 AW   
Htot Edot -

## 7. Mixture separation

A sound wave in a binary gas mixture in a channel causes time-averaged molar fluxes of the two components of the mixture in opposite directions, and can create a significant molefraction gradient along the channel. This occurs because oscillating lateral thermal diffusion causes the light and heavy components of the mixture to take turns enriching the central region of the channel, where the oscillating motion is the greatest; the time phasing is best when the oscillating enrichment and oscillating velocity are in phase, causing the velocity oscillations to carry light-enriched gas in one direction and heavy-enriched gas in the other direction [44, 45, 46]. The light component usually flows in the direction of $\dot { E }$

The thermoacoustic mixture-separation mole flux and mole-fraction gradient are in some ways analogous to the time-averaged enthalpy flux and temperature gradient that a sound wave creates in a stack in a standing-wave thermoacoustic refrigerator.

DELTAEC can model this effect accurately [10].

## 7.1 Principles of calculation

Consider a binary gas mixture flowing steadily in the x direction through a channel, with a molar flow rate $\dot { N }$ . Let the mole fraction of the lighter component be $n _ { L }$ and let its molar flow rate be $\dot { N } _ { L } ;$ similarly $n _ { H }$ and $\dot { N } _ { H }$ for the heavy component. It is always true that

$$
n _ { L } + n _ { H } = 1\tag{7.1}
$$

and

$$
\dot { N } _ { L } + \dot { N } _ { H } = \dot { N } .\tag{7.2}
$$

In a simple "bulk" flow of the gas mixture (i.e., flow that does not involve mass diffusion, mole-fraction gradients, or thermoacoustic mixture separation), it is also true that

$$
\dot { N } _ { L } = n _ { L } \dot { N } .\tag{7.3}
$$

Combining Eqs. (7.1)−(7.3) algebraically shows that

$$
\dot { N } _ { H } = n _ { H } \dot { N }\tag{7.4}
$$

is also true in a bulk flow, as expected from the symmetry of the equations. Thus, bulk flow in a binary mixture can be uniquely described by assigning values to just two variables, which can be chosen as $\dot { N }$ and $n _ { L }$

Nontrivial flows arise in binary mixtures whenever mass diffusion or thermoacoustic mixture separation occurs. For example, for $\dot { N } = 0$ and no thermoacoustics, a nonzero $\dot { N } _ { L }$ and an equal and opposite $\dot { N } _ { H }$ arise from ordinary diffusion in the $x$ direction whenever a mole-fraction gradient $d n _ { L } / d x \equiv - d n _ { H } / d x$ exists; Eq. (7.3) is obviously not satisfied. Thus, DELTAEC must routinely handle nontrivial mixture flows, which must be specified by three independent variables. DELTAEC takes those three variables to be $\dot { N } , \dot { N } _ { L } .$ and $n _ { L }$

For $d T _ { m } / d x = 0$ , DELTAEC allows the mole fraction to evolve with x in segment types MIXBL (boundary-layer approximation), MIXSLAB (between parallel plates), and MIXCIRC (circular channel), according to the theory described in Ref. [10] and references therein. Nonzero $d n _ { L } / d x$ is supported for three of DELTAEC's gas mixtures: He-Ar, He-Xe, and Ne-Xe. The user can create an external file to specify the properties of other gas mixtures, as described in Section 12.18.2. The equations being integrated in these MIX\*\* segments are

$$
\begin{array} { l l l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle \mathcal { F } _ { \mathrm { m o m e n t u m } } ( p _ { 1 } , U _ { 1 } , T _ { m } ; ~ p _ { m } , \omega ; ~ \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) , } \end{array}\tag{7.5}
$$

$$
\begin{array} { l l l } { \displaystyle \frac { d U _ { 1 } } { d x } } & { = } & { \displaystyle \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( p _ { 1 } , U _ { 1 } , T _ { m } ; ~ p _ { m } , \omega ; \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) , } \end{array}\tag{7.6}
$$

$$
\frac { d T _ { m } } { d x } = 0 ,\tag{7.7}
$$

$$
\begin{array} { r c l } { \displaystyle \frac { d n _ { L } } { d x } } & { = } & { \displaystyle \mathcal { F } _ { \mathrm { m i x \ s e p } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { N } , \dot { N } _ { L } ; \ p _ { m } , \omega ; \mathrm { g e o m e t r y , \mathrm { g a s \ p r o p e r t i e s , \ e t c . } } ) . } \end{array}\tag{7.8}
$$

The similar segment types MIXTBL, MIXTSLAB, and MIXTCIRC allow $d T _ { m } / d x \ne 0$ , so the equations being integrated in these segments are

$$
\begin{array} { l l l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle \mathcal { F } _ { \mathrm { m o m e n t u m } } ( p _ { 1 } , U _ { 1 } , T _ { m } ; ~ p _ { m } , \omega ; ~ \mathrm { g e o m e t r y , ~ g a s ~ p r o p e r t i e s , ~ e t c . } ) , } \end{array}\tag{7.9}
$$

$$
\frac { d U _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( p _ { 1 } , U _ { 1 } , T _ { m } ; ~ p _ { m } , \omega ; \mathrm { g e o m e t r y , \mathrm { g a s ~ p r o p e r t i e s } , \mathrm { e t c . } } ) ,\tag{7.10}
$$

$$
\frac { d T _ { m } } { d x } = \mathcal { F } _ { \mathrm { e n e r g y } } ( p _ { 1 } , U _ { 1 } , T _ { m } ; ~ p _ { m } , \omega ; \mathrm { g e o m e t r y , \mathrm { g a s ~ p r o p e r t i e s } , \mathrm { e t c . } } ) ,\tag{7.11}
$$

$$
\begin{array} { r c l } { \displaystyle \frac { d n _ { L } } { d x } } & { = } & { \displaystyle \mathcal { F } _ { \mathrm { m i x \ : s e p } } ( p _ { 1 } , U _ { 1 } , T _ { m } , \dot { N } , \dot { N } _ { L } ; \ : p _ { m } , \omega ; \mathrm { g e o m e t r y , \mathrm { g a s \ : p r o p e r t i e s , \ : e t c . } } ) . } \end{array}\tag{7.12}
$$

In DELTAEC's BEGIN segment, we specify $\dot { N }$ and $n _ { L }$ . If the "bulk NLdot" box is checked, DELTAEC calculates $\dot { N } _ { L }$ using Eq. (7.3); if the bulk NLdot box is not checked, the user must specify $\dot { N } _ { L }$ (perhaps as a guess).

Continuity of $n _ { L }$ between segments is enforced. $\dot { N }$ and $\dot { N } _ { L }$ split up at TBRANCHs, add at UNIONs, and are independent of x in all physical segments.

## 7.2 Boundary conditions

Deciding how to handle $\dot { N } , \dot { N } _ { L }$ and $n _ { L }$ at BEGINs, SOFTENDs, etc. is subtle and depends on exactly what the user wants to model. A feedstock with a given $n _ { L }$ might be injected into the middle or end of a mixture separator whose vigorous thermoacoustic processes maintain a locally different $n _ { L } ;$ in this case, $n _ { L }$ can be regarded as discontinuous [10], and Eq. (7.3) would not apply if the local thermoacoustic channel's $n _ { L }$ were used, even while the feedstock flow itself is bulk [i.e., the feedstock mole fraction and feedstock flows satisfy Eq. (7.3)]. In other circumstances, one location of the mixture separator might be firmly connected to an essentially infinite bath of feedstock, so $n _ { L }$ would be maintained by net molar or partial-molar flows to or from the bath that might not satisfy Eq. (7.3). If a \*\*END represents a location where the acoustics stops and an enriched product flows out of the system, Eq. (7.3) must apply to the outflow.

Here are several possible situations, with discussions of how to initialize variables in BEGIN and how to choose guesses and targets for each of them in DELTAEC. We only discuss the mixture-specific guesses and targets here; realistic mixture-separation models typically also include guesses and targets related to $p _ { 1 }$ and $U _ { 1 }$

## Sealed system

The steady-state conditions of Refs. [44, 45] represent sealed systems with $\dot { N } = 0$ everywhere. Those experiments had no steady inflow or outflow, but were constrained by the mole fractions present in the original charge of gas mixture, so getting the right answer from DELTAEC depends on constraining DELTAEC's solution with an integral of $n _ { L }$ over the volume of the apparatus to match the total number of moles of light component that was present in the original charge. Getting the correct answer to that integral would be the target corresponding to the guessed value of $n _ { L }$ in the BEGIN. In practice, we might approximate such an integral in DELTAEC with a simple, volumetrically weighted average of values at a small number of locations. Each such value could be captured with an RPN segment. The BEGIN should have $\dot { N } = 0$ (and, by default $\dot { N } _ { L } = 0 )$ , because nothing flows in or out there.

## Firm connection to feedstock bath, no steady flow

If one end of a mixture-separation channel is firmly connected to a feedstock bath, then the system could be modeled starting at that end with a BEGIN having a known mole fraction and a guessed $\dot { N } _ { L }$ , and integrating along the channel. If the BEGIN is not at a location where the system is firmly connected to a feedstock bath, then $n _ { L }$ could be guessed at the BEGIN and the mole fraction could be targeted wherever the system is firmly connected to a feedstock bath. Allow for the likelihood that $\dot { N } _ { L }$ is discontinuous at the location of such a mid-model "bath" connection,

## Inject feedstock at one end, withdraw product at the other end

Now consider a slow injection of feedstock at one end of the acoustic separation channel, and a removal of product at the other end, through capillaries [9]. When the system reaches steady state, the flow variables at the exit— $\dot { N } _ { L }$ and $\dot { N }$ —must equal their incoming values. Yet, if the flow is weak enough, we feel confident that a mole-fraction gradient must exist from end to end. Thus, the flow cannot satisfy $\dot { N } _ { L } = n _ { L } \dot { N }$ at both ends. What happens? The exit flow is bulk, the mole fraction in the exit flow must be the same as the mole fraction in the feedstock, and the feedstock mixes abruptly into a locally different mole fraction at the feedstock-end of the apparatus.

To model that situation with DELTAEC, the easiest approach is to put the BEGIN at the exit end, because the exit flow is bulk so we have fewer unknowns to guess there. Suppose we know the incoming $\dot { N }$ and $n _ { L }$ . We use these values in the BEGIN (with a minus sign for the molar flux), check the "bulk flow" box to set $\dot { N } _ { L }$ appropriately, and integrate straightforwardly to the other end of the channel, where we learn what the mole fraction in the channel is where the feedstock mixes into it. This approach is the easiest because it involves only two segments—BEGIN and MIXBL—and it involves no targets or guesses.

A seemingly more logical and readable approach to this situation is to begin at the feedstock end, but then we need more DELTAEC baggage, to work around the fact that we know less information a priori at that end:

0. BEGIN with the known $p _ { 1 } , U _ { 1 }$ , feedstock $\dot { N }$ , and feedstock $n _ { L }$ . Since the feedstock capillary flow is bulk, check the "bulk" box in the BEGIN segment to establish the correct $\dot { N } _ { L }$

1. RPN with 1a a guessed mole fraction at the feedstock end of the separation channel and 1b having inp =nL .

2. MIXCIRC.

3. RPN expressing the bulk condition, Eq. (7.3), for the exit flow, and target it. This target is associated with the guess in segment 1. For example, put 0. in 3a and $^ { \circ } \mathrm { n L }$ Ndot $* { \mathrm { N L d o t } } - \mathrm { ? }$ in 3b.

## Feedstock in the middle of a long tube, products extracted at both ends

Let's assume that we know the molar flow rate and mole fraction of the feedstock injected into the middle of a long separation tube, and that external control of the capillary flow impedances forces a known fraction of that molar flow out the top and the remainder out the bottom. We'll begin at one of the places where the steady flow goes out, because we can count on bulk flow there. This situation is modeled in Ref. [10] and shown in the example in Section 7.3 below.

0. BEGIN with the acoustic conditions at one end of the channel, with guessed $n _ { L }$ . Set $\dot { N }$ equal to the known rate of product extraction here. Check the "bulk" box in the BEGIN segment so $\dot { N } _ { L }$ is automatically assigned the appropriate, bulk value at this product-outflow location.

1. MIXBL for the first part of the channel.

2. RPN with the helium mole fraction of the injected feedstock in 2a. (not targeted!)

3. RPN with the injected molar flow rate in 3a and with the following instructions in 3b to add the correct increment to both $\dot { N }$ and $\dot { N } _ { L }$ : 3a Ndot + =Ndot 3a 2a \* NLdot + =NLdot

4. MIXBL for the second part of the channel.

At this point, we have the correct $\dot { N }$ and $\dot { N } _ { L }$ , but we are not necessarily guaranteed the bulk condition needed for outflow into a capillary. Hence, we need the next segment:

5. RPN expressing the bulk condition, Eq. (7.3), and target it. For example, put 0. in 5a and “ nL Ndot \* NLdot - Ndot $\mathbf { \Phi } / \mathbf { \Phi } ^ { \dag }$ in 5b. (We often multiply the bulk-flow-enforcement expression $0 = n _ { L } \dot { N } - \dot { N } _ { L }$ by a large number, or divide it by $\dot { N }$ , to give DELTAEC a weighty enough target.) This target corresponds to the guessed value of $n _ { L }$ in segment 0.

Firm connection to feedstock bath in the middle of a long tube, products extracted at both ends

This time, let's assume that we know the two exiting molar flow rates and the mole fraction of the feedstock bath in the middle. The feedstock bath must supply $\dot { N }$ and $\dot { N } _ { L }$ in the center, but not necessarily in bulk proportions.

In hardware, how might we make a firm connection to a fixed mole fraction in the middle of a tube? We could have two capillaries there, and pump a huge mole flux into one of them and a nearly equal mole flux at a slightly different mole fraction out of the other one. The net flow—the sum of these two—is not a bulk flow.

0. BEGIN at one end of the channel with a guessed $n _ { L }$ and the known $\dot { N }$ . Check the “bulk flow" box to get the known $\dot { N } _ { L }$ , because this is a location of product outflow.

1. MIXBL for the first part of the channel.

2. RPN Target the feedstock bath's mole fraction here, with the target value in 2a and nL in 2b.

3. RPN Guess the incremental $\dot { N }$ in 3a. Add the incremental $\dot { N }$ and $\dot { N } _ { L }$ to the separation tube in 3b using inp Ndot + =Ndot inp 2a \* NLdot + =NLdot .

4. MIXBL for the second part of the channel.

5. RPN expressing the bulk condition, Eq. (7.3), and target it. For example, put 0. in 5a and nL Ndot \* NLdot - Ndot / in 5b.

We have 2 targets (segments 2, 5) and 2 guesses (segments 0, 3).

## 7.3 Continuous He-Ar separator

Guidance for choosing the guesses and targets related specifically to mixture separation was given above. Here is an extended example from Ref. [10] including the targets and guesses relating to the acoustic wave. The apparatus is shown in Fig. 7.1.

First, we use DELTAEC to predict the shape of $n _ { H } ( x )$ for steady flow injected at the tube midpoint and extracted at the ends, for one particular operating point, namely

Nfeedstock = 1.59 µmol/s of 50–50 He−Ar at x = 0.5 m,

$$
\dot { N } _ { \mathrm { p r o d u c t } } = 2 0 \% \times 1 . 5 9 \ \mu \mathrm { m o l / s } \ \mathrm { a t } \ x = 0 . 0 \ \mathrm { m } ,
$$

$$
\dot { N } _ { \mathrm { p r o d u c t } } = 8 0 \% \times 1 . 5 9 \ \mu \mathrm { m o l / s } \ \mathrm { a t } \ x = 1 . 0 \ \mathrm { m } ,
$$

$$
| p _ { 1 } | = 3 . 0 0 \ \mathrm { k P a } \ \mathrm { a t } \ x = 0 . 5 0 \ \mathrm { m } ,
$$

$z = A p _ { 1 } / U _ { 1 } = \rho _ { m } a$ , purely real, at x = 0.5 m.

The DELTAEC model for the hardware dimensions given in Ref. [10] and the conditions listed above uses the mixture-specific guess and target described above under the heading "Feedstock in the middle of a long tube, products extracted at both ends," plus three

![[mu_66afccee_a79e28f216f66b71cd01.jpg]]  
Figure 7.1: Apparatus for helium-argon separation used in Ref. [10] and in this example.

additional guesses and targets to enforce the acoustic conditions specified in that paper. The <.out> file is

```csv
TITLE planned first expt in fy 06
!Examples\MixSep\05081220.out
!Created@13:36:58 28-Jun-2020 with DeltaEC version 6.4b2.8!under win32,
0
BEGIN in front of top driver
7.9907E+4 a Mean P Pa
200.00 b Freq Hz
298.15 c TBeg K
3883.3 d Ipl Pa G
0.0000 e Ph(p) deg
9.7136E-5 f |U| m^3/s G
-1.0139 g Ph(U) deg G
-2.6300E-8 h Htot W
-3.1800E-7 i Ndot mol/s
0.34099 j nL G
HeAr Gas type
! 1
MIXCIRC tube #1 (bottom)
8.5630E-6 a Area m^2 3000.0 AIpl Pa
1.0000 b GasA/A -101.31 BPh(p) deg
0.5000 c Length m 8.1417E-5 C |U| m^3/s
1.6510E-3 d radius m -101.31 D Ph(U) deg
-2.6300E-8 E Htot W
0.12213 F Edot W
0.34099 G nL Beg
0.46622 H nL End
1- 2
RPN pressure amplitude in center
3000.0 a =A? 3000.0 A ChngeMe
p1 mag
!-- 3
RPN set Re[z]= rho a
0.0000 a =A? 1.8016E-16 A ChngeMe
rho a * p1 U1 / 1a * real - rho a * /
!- 4
RPN set Im[z] = 0
0.0000 a =A? -1.1148E-16 A ChngeMe
p1 U1 / 1a * imag rho a * /
! – 5
RPN feedstock concentration
0.5000 a G or T 0.0000 A ChngeMe
0
!- 6
RPN [a]=injection (micromol/sec)
1.5900 a G or T 6.8657E-7 A ChngeMe
1.2720E-6 B ChngeMe
6a 1e-6 * Ndot + =Ndot 6a 1e-6 * 5a * NLdot + =NLdot
! 7
MIXCIRC tube #2 (bottom)
sameas 1a a Area m^2 2345.1 AIpl Pa
sameas 1b b GasA/A 163.58 BPh(p) deg
sameas 1c c Length m 6.7276E-5 C |U| m^3/s
sameas 1d d radius m 163.66 D Ph(U) deg
-6.1169E-5 E Htot W
7.8886E-2 F Edot W
0.46622 G nL Beg
0.53975 H nL End
! 8
RPN exit bulk condition
0.0000 a =A? 5.8267E-16 A ChngeMe
nL Ndot * NLdot - Ndot /
```

The <.sp> file from that run was imported into a spreadsheet to convert $n _ { L }$ to $n _ { H } = 1 - n _ { L }$ for plotting in Ref. [10]. Figure 7.2 shows the result, compared with measurements of the heavy mole fraction $n _ { H }$ that were made at 7 locations along the separation tube.

Next, an incremental plot was made, with feedstock $\dot { N }$ as the independent variable and with an RPN segment maintaining the molar flow rate in the BEGIN segment equal to -20% of the feedstock flow. The result is shown in Fig. 7.3.

![[mu_66afccee_986e27ea2ec3b010a46d.jpg]]  
Figure 7.2: Heavy mole fraction $n _ { H }$ vs position in tube for one particular operating condition that is described in the text. The points are measurements from Ref. [10] and the curve is the result of DELTAEC's calculation as described in the text.

![[mu_66afccee_73f911c7508ea54f5d06.jpg]]  
Figure 7.3: Heavy mole fractions $n _ { H }$ at $x = 0$ and $x = 1$ m, at various feedstock molar flows, with one product flow equal to 20% of the feedstock flow and the other product flow equal to 80% of the feedstock flow. The points are measurements from Ref. [10] and the curves are DELTAEC calculations as described in the text.

Part II: Reference

## 8. General principles

## 8.1 Integration from BEGIN to \*\*END

Except for trivial cases $( \mathrm { e . g . }$ , IMPEDANCE) that are handled algebraically, each of DELTAEC's physical segments numerically integrates two or more of the following differential equations from its initial end to its final end:

$$
\frac { d p _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { m o m e n t u m } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{8.1}
$$

$$
\frac { d U _ { 1 } } { d x } = \mathcal { F } _ { \mathrm { c o n t i n u i t y } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{8.2}
$$

$$
\frac { d T _ { m } } { d x } = \mathcal { F } _ { x \mathrm { { r \mathrm { - } e n e r g y } } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{8.3}
$$

$$
\frac { d T _ { \mathrm { s o l i d } } } { d x } = \mathcal { F } _ { \mathrm { s o l i d } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{8.4}
$$

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } = \mathcal { F } _ { \mathrm { l a t e r a l \ e n e r g y } } ( \mathrm { l o c a l \ a n d \ g l o b a l \ p a r a m e t e r s \ a n d \ v a r i a b l e s } ) ,\tag{8.5}
$$

$$
\frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } = \mathcal { F } _ { \mathrm { h e a d ~ l o s s } } ( \mathrm { l o c a l ~ a n d ~ g l o b a l ~ p a r a m e t e r s ~ a n d ~ v a r i a b l e s } ) ,\tag{8.6}
$$

$$
\frac { d n _ { L } } { d x } = \mathcal { F } _ { \mathrm { m i x \ s e p } } ( \mathrm { l o c a l \ a n d \ g l o b a l \ p a r a m e t e r s \ a n d \ v a r i a b l e s } ) .\tag{8.7}
$$

The first of these equations, involving $p _ { 1 }$ and $U _ { 1 }$ , are sufficient for users who are interested only in acoustics, without thermoacoustics. For these users, the other equations can be ignored. Users who are interested in ordinary thermoacoustic and Stirling engines and refrigerators must also concern themselves with $T _ { m } , T _ { \mathrm { s o l i d } }$ , and $\dot { H } _ { \mathrm { t o t } }$ . Very few users have to consider all seven of these equations simultaneously

In most segments that employ numerical integration of these equations, Nint steps of fourth-order Runge-Kutta integration [16] are employed. However, HX, TX, SX, and PX, which are most often used for heat exchangers whose lengths are only of the order of $| \xi _ { 1 } |$ , employ only one step of fourth-order Runge-Kutta integration

For each integration through the segments in the model, the initial values of the integration variables, $p _ { 1 } , U _ { 1 } , T _ { m } , { \dot { H } } _ { \mathrm { t o t } } , p _ { 2 , 0 , \mathrm { D E C } }$ and $n _ { L }$ , are set in the BEGIN segment. Except for $T _ { \mathrm { s o l i d } }$ , all of these variables are taken to be continuous between segments; but $T _ { \mathrm { s o l i d } }$ is usually discontinuous at the ends of heat exchangers

A few additional variables, such as $\dot { N }$ ,are also initialized in the BEGIN segment but are independent of x unless they are changed abruptly at a logistical segment such as a TBRANCí or via a variable-reassignment operator such as =Ndot in an RPN segment.

The total power flow $\dot { H } _ { \mathrm { t o t } }$ is often independent of $x ,$ but there are important exceptions. In heat exchangers, $\dot { H } _ { \mathrm { t o t } }$ changes by the amount of heat added (or removed), and in transducers it changes by the amount of power added (or removed). If the ANCHOR logistical segment (described in Section 11.3.1) is used upstream, $\dot { H } _ { \mathrm { t o t } }$ also changes in every component except STK\*\*s, because ANCHOR means that acoustic power dissipation is removed locally as heat in each such component.

Usually the initial values of at least some of these integration variables are unknown at the BEGIN, so DELTAEC uses a shooting method to find initial values that are consistent with targeted results that are identified by the user elsewhere in the model. The shooting method is described in the next section.

After the shooting method has met its targets, DELTAEC knows the complete solution $p _ { 1 } ( x ) , U _ { 1 } ( x ) , T _ { m } ( x ) , T _ { \mathrm { s o l i d } } ( x ) , \dot { H } _ { \mathrm { t o t } } ( x )$ , p2,0,DEC(x), and $n _ { L } ( x )$ . Three additional useful functions of x are calculated straightforwardly from that solution: the acoustic power $\dot { E }$ the exergy flow $\dot { X }$ , and the total second-order time-averaged pressure $p _ { \mathrm { 2 , 0 , t o t } }$

$$
\dot { E } ( x ) \ = \ \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \widetilde { U } _ { 1 } \right] ,\tag{8.8}
$$

$$
\dot { X } ( x ) ~ = ~ \frac { T _ { 0 } } { T _ { m } } \dot { E } + \left( 1 - \frac { T _ { 0 } } { T _ { m } } \right) \dot { H } _ { 2 , k } + \dot { N } \left( m w _ { m } - T _ { 0 } m s _ { m } \right)
$$

$$
+ \dot { N } _ { L } R _ { \mathrm { u n i v } } T _ { 0 } \ln \left( \frac { n _ { L } } { n _ { L , 0 } } \right) + \left( \dot { N } - \dot { N } _ { L } \right) R _ { \mathrm { u n i v } } T _ { 0 } \ln \left( \frac { 1 - n _ { L } } { 1 - n _ { L , 0 } } \right) ,\tag{8.9}
$$

$$
\begin{array} { r c l } { { p _ { 2 , 0 , \mathrm { t o t } } ( x ) } } & { { = } } & { { p _ { 2 , 0 , \mathrm { t r a d } } + p _ { 2 , 0 , \mathrm { D E C } } } } \\ { { } } & { { = } } & { { \displaystyle \frac { | p _ { 1 } | ^ { 2 } } { 4 \rho _ { m } a ^ { 2 } } - \frac { \rho _ { m } | U _ { 1 } | ^ { 2 } } { 4 A _ { \mathrm { g a s } } ^ { 2 } } + p _ { 2 , 0 , \mathrm { D E C } } . } } \end{array}\tag{8.10}
$$

(8.11)

The expression for acoustic power is discussed in Ref. [13] and should be familiar to most acousticians.

The expression for $\dot { X }$ is an amalgam of the basic thermoacoustic exergy flow derived in Ref. [13], a steady-flow component derived in Ref. [32], and the $\dot { N } \neq 0$ extension of the thermoacoustic mixture-separation expression derived in Ref. [45]. The reference temperature $T _ { 0 }$ , which is the ambient temperature at which heat has no value, is set to 300 K by default in BEGIN segments and can be changed to a different value by using the operation =Tzero in an RPN segment soon after the BEGIN. Steady pressure makes no contribution to the steady-flow component because we assume that the reference pressure for exergy is $p _ { m }$ The second line of Eq. (8.9) is relevant only for mixtures. The zero-exergy mixture mole fraction, $n _ { L , 0 }$ , is the mole fraction for which the mixture has no value, typically the feedstock's mole fraction. It is set to 0.500 by default in BEGIN segments, and can be changed to another value by using =nLzro in an RPN segment soon after the BEGIN.

The traditional part of the second-order time-averaged pressure, $p _ { \mathrm { 2 , 0 , t r a d } }$ , is derived in Ref. [36], and measurements of $p _ { \mathrm { 2 , 0 , t o t } }$ are described in Ref. [35]

These ten functions of $x _ { i }$ as well as many others $( \mathrm { e . g . }$ , the mean density $\rho _ { m }$ , the vibration force $F _ { 1 }$ described in Section 11.4.1, the complex amplitude $\left. T _ { 1 } \right.$ of the oscillating temperature in the gas averaged over the spatial dimensions perpendicular to x) are available to the user in tabular and graphical forms via the <.sp> file, at the end of each segment in the <.out> file, and/or at any location via RPN segments.

The lateral spatial average of the complex temperature amplitude, $\left. T _ { 1 } \right.$ , differs from the integration variables and the variables such as $\dot { E }$ that are calculated only from integration variables, because $\left. T _ { 1 } \right.$ often changes from the end of one segment to the beginning of the next, since it depends on segment-dependent variables such as $f _ { \nu } , \ f _ { \kappa } ,$ or $d T _ { m } / d x$ as well as on the integration variables. A broadly applicable expression for $\left. T _ { 1 } \right.$ can be obtained by converting Eq. (A10) in Ref. [4] to modern notation, and then taking the lateral spatial average to convert $h _ { \kappa }$ and $h _ { \nu }$ to $f _ { \kappa }$ and $f _ { \nu }$ . See details for $\left. T _ { 1 } \right.$ for each segment in Chapter 10. At a transition between segments in the $< . { \mathrm { s p } } > { \mathrm { f i l e } }$ , one line shows $\left. T _ { 1 } \right.$ at the end of one physical segment, and the next line shows it at the beginning of the subsequent physical segment. In an RPN segment, $\left. T _ { 1 } \right.$ yields the value at the end of the previous physical segment.

## 8.1.1 Additional details for $\dot { N }$ and p2,0,DEC

DELTAEC's input parameter Ndot, denoted in the Users Guide by $\dot { N }$ , represents the true time-averaged molar flow, which is the steady-flow quantity under the most direct experimental control and the quantity that carries steady enthalpy flux

$$
\dot { H } _ { \dot { N } } = \dot { N } m w _ { m } ,\tag{8.12}
$$

where m is the molar mass and $w _ { m }$ is the mean enthalpy per unit mass. The total power

$$
\dot { H } _ { \mathrm { t o t } } = \dot { H } _ { 2 , k } + \dot { H } _ { \dot { N } }\tag{8.13}
$$

is the power that obeys the first law of thermodynamics for open control volumes. The total power $\dot { H } _ { \mathrm { t o t } }$ is the sum of the second-order time-averaged thermoacoustic enthalpy flux, the ordinary thermal conduction in the x direction, and $\dot { H } _ { \dot { N } } = \dot { N } m w _ { m }$

In DELTAEC, mean enthalpy is referenced to zero at temperature $T _ { 0 }$ , which is set to 300 Kelvin by default in the first BEGIN segment of a model. (This default can be overridden by using the =Tzero operator in an RPN segment.) For an ideal gas, Eq. (8.12) can then be regarded as

$$
\dot { H } _ { \dot { N } } = \dot { N } m c _ { p } \left( T _ { m } - T _ { 0 } \right) .\tag{8.14}
$$

To second order,

$$
\dot { N } m \simeq \frac { 1 } { 2 } \mathrm { R e } \int [ \rho _ { 1 } \widetilde { u } _ { 1 } ] ~ d A _ { \mathrm { g a s } } + \rho _ { m } U _ { 2 , 0 } ,\tag{8.15}
$$

where m is the molar mass. However, the second-order time-averaged momentum equation shows that second-order time-averaged head-loss gradients due to viscosity and turbulence are generated by $U _ { 2 , 0 }$ , with no contribution from $\rho _ { 1 } \widetilde { u } _ { 1 }$ . Defining $\dot { N } _ { 2 , 0 } \equiv \rho _ { m } U _ { 2 , 0 } / m$ , substituting $\rho _ { 1 } = \left( \gamma / a ^ { 2 } \right) p _ { 1 } - \rho _ { m } \beta T _ { 1 }$ in Eq. (8.15), and solving for $\begin{array} { r } { \frac { 1 } { 2 } \mathrm { R e } \int [ T _ { 1 } \widetilde { u } _ { 1 } ] \ d A _ { \mathrm { g a s } } } \end{array}$ in the standard thermoacoustic expression for $\dot { H } _ { 2 , k }$ , it is easy to show that Eq. (8.15) is equivalent to

$$
\dot { N } _ { \mathrm { 2 , 0 } } = \dot { N } + \frac { \beta } { m c _ { p } } \left[ \dot { H } _ { \mathrm { 2 , } k } + \left( A _ { \mathrm { g a s } } k + A _ { \mathrm { s o l i d } } k _ { s } \right) \frac { d T _ { m } } { d x } \right] - \left( \frac { 1 } { m a ^ { 2 } } + \frac { \beta } { m c _ { p } } \right) \dot { E } ,\tag{8.16}
$$

which is the molar flow that is used in most of DELTAEC's p2,0,DEC calculations.1 Note that $\dot { N } _ { 2 , 0 }$ is often nonzero when $\dot { N } = 0$ , which means that interesting second-order, time-averaged head losses arise in many circumstances having $\dot { N } = 0$ , such as in the regenerators of TASHEs and pulse-tube refrigerators. Click the Enable Ndot button in the BEGIN segment's Optional parameters to “turn on" the display of p2oDEC even when $\dot { N } = 0$

In addition to viscous contributions to p2,o,DEC caused by $U _ { 2 , 0 }$ , there are second-order forces per unit volume caused by gradients in $\rho _ { m }$ and $\rho _ { m } a ^ { 2 }$ , as summarized in Section 14.2.

## 8.2 Shooting method

If initial values of all of the integration variables of interest [chosen from among $p _ { 1 } ( x )$ $U _ { 1 } ( x ) , T _ { m } ( x ) , T _ { \mathrm { s o l i d } } ( x ) , \dot { H } _ { \mathrm { t o t } } ( x ) , p _ { 2 , 0 , \mathrm { D E C } } ( x )$ , and $n _ { L } ( x ) ]$ are known at the BEGINning end of the thermoacoustic apparatus, then DELTAEC's numerical integration is straightforward, proceeding from the initial end to the final end. But usually one or more boundary conditions are instead specified at the final end or somewhere in the middle. In such circumstances DELTAEC uses a shooting method [16], by guessing any unknowns at the BEGIN, integrating to the \*\*END, comparing the results with the target boundary conditions imposed at that end and/or elsewhere, and adjusting its guesses until the targets are met. Up to eighteen guesses and eighteen targets are allowed. One of DELTAEC's most powerful features is that the guesses and targets are not limited to the conventional choices, which would be the initial values of integration variables at the BEGIN as guesses and calculated values of integration variables at the \*\*END as targets. Any results can be used for targets, and any upstream variables that have effects on downstream target variables can be used as guesses. This enables DELTAEC to calculate a resonance frequency, a geometrical dimension, a temperature, or even the concentration in a binary gas mixture to satisfy desired boundary conditions.

DELTAEC treats its collection of n guesses and n targets as a system of n nonlinear equations,

$$
F _ { 1 } ~ = ~ r _ { 1 } ( g _ { 1 } , g _ { 2 } , g _ { 3 } . . . g _ { n } ) - t _ { 1 } ,\tag{8.17}
$$

$$
F _ { 2 } ~ = ~ r _ { 2 } ( g _ { 1 } , g _ { 2 } , g _ { 3 } . . . g _ { n } ) - t _ { 2 } ,\tag{8.18}
$$

$$
F _ { 3 } ~ = ~ r _ { 3 } ( g _ { 1 } , g _ { 2 } , g _ { 3 } . . . g _ { n } ) - t _ { 3 } ,\tag{8.19}
$$

(8.20)

$$
F _ { n } = r _ { n } ( g _ { 1 } , g _ { 2 } , g _ { 3 } . . . g _ { n } ) - t _ { n } ,\tag{8.21}
$$

where $g _ { i }$ is the ith guess, $t _ { i }$ is the ith target value, and $r _ { i }$ is the ith calculated result, which we hope can be made equal to the ith target $t _ { i }$ by suitable choices of the n guesses $g _ { i }$ . Thus, DELTAEC must seek values of the n guesses $g _ { i }$ that make $F _ { i } = 0$ for all $i .$ Several methods for finding the simultaneous zeroes of complicated, simultaneous functions exist. The routine incorporated in DELTAEC is called DNSQ, and it is part of the SLATEC Common

Mathematical Library, which is freely available through the internet software repository at http://www.netlib.org. The algorithm used is a modification of the Powell hybrid method [47, 48] (a.k.a. the Powell dogleg method). The ordinary DELTAEC user can just as well imagine that DNSQ is the Newton-Raphson method, which is easy to understand and is described in Ref. [16] and many tutorial websites. The description below is based on this oversimplification.2

A Newton-Raphson algorithm begins with initial “guessed" values of the guesses, and calculates the n values of $\bar { F } _ { i \cdot } \ \mathrm { I f } \ \sum \left( F _ { i } \right) ^ { 2 }$ is not close enough to zero, the algorithm estimates the $n ^ { 2 }$ local slopes

$$
{ \frac { \partial F _ { i } } { \partial g _ { j } } } \simeq { \frac { F _ { i } ( g _ { 1 } , g _ { 2 } , \ \ldots \ g _ { j } + \delta g _ { j } , \ \ldots \ g _ { n } ) - F _ { i } ( g _ { 1 } , g _ { 2 } , \ \ldots \ g _ { j } , \ \ldots \ g _ { n } ) } { \delta g _ { j } } } .\tag{8.22}
$$

The algorithm forms a “better" set of guesses based on the assumption that these functions $F _ { i }$ are linear, and repeats the process, until it judges the results to be close enough to the targets, according to

$$
{ \sqrt { \sum \left( w _ { i } F _ { i } \right) ^ { 2 } } } \leq { \mathrm { T o l e r a n c e ~ } } \times { \sqrt { \sum \left( w _ { i } t _ { i } \right) ^ { 2 } } } ,\tag{8.23}
$$

where the weighting factors $w _ { i }$ passed from DELTAEC to DNSQ are given by

$$
w _ { i } = \frac { 1 } { 3 6 0 } \mathrm { ~ i f ~ t h e ~ t a r g e t ~ i s ~ a ~ p h a s e ~ a n g l e } ,\tag{8.24}
$$

$$
= \ { \frac { 1 } { \left| t _ { i } \right| } } { \mathrm { ~ i f ~ } } \left| t _ { i } \right| \geq 1 0 ^ { - 4 } { \mathrm { ~ a n d ~ t h e ~ t a r g e t ~ i s ~ n o t ~ a ~ p h a s e ~ a n g l e } } ,\tag{8.25}
$$

$$
= 1 0 ^ { 4 } { \mathrm { ~ i f ~ } } | t _ { i } | \leq 1 0 ^ { - 4 } { \mathrm { ~ a n d ~ t h e ~ t a r g e t ~ i s ~ n o t ~ a ~ p h a s e ~ a n g l e } }\tag{8.26}
$$

in the default "Normalization Mode = 1." When Tolerance $= 1 0 ^ { - N }$ , this should ensure N digits of accuracy for most targets like temperatures and pressure amplitudes, and values $< 1 0 ^ { - ( N + 4 ) }$ for “zero" targets such as normalized \*\*END impedances. Small negative values for the Normalization Mode $\left( \mathrm { e . g . , ~ \mathrm { - 4 } } \right)$ seem to work best for pulse-tube refrigerators and many other models.

This only works if the functions $F _ { i }$ are reasonably smooth. To ensure that each target result is a smooth function of all guesses, we have deliberately made DELTAEC's built-in features be continuous functions. However, some have discontinuous changes in slope [e.g., Eqs. (10.121) and (10.122)]. For an example of a pathological discontinuity that could easily overwhelm the shooting method, see the end of Section 8.5.

In complicated models, choosing appropriate guesses and targets and getting DELTAEC to hit the targets are the most challenging aspects of using DELTAEC. Guidance for choosing guesses and targets and for meeting targets appear in Secs. 5.3 and 5.4, respectively.

## 8.3 Numerical options

DELTAEC has many internal parameters that can be altered by the experienced user to control the behavior of DELTAEC's numerical integration and shooting method. These parameters are accessible via Options in the Edit pulldown menu.

If any of the parameters described below are modified from their default values, it is usually desirable to keep the new values for all subsequent runs, even after exiting from DELTAEC and restarting. Therefore, whenever the default settings are changed, all of the tunable parameters are written to a special file when the model is saved. This file has the same base filename as the model, ending with <.ini>. Whenever a new model is loaded, DELTAEC checks in the same folder for a <.ini> file with a matching base filename and loads these settings if it is found. This file is written in NAMELIST format which makes it easy to examine and modify using any text editor.

Frequently, a collection of similar models will reside in a single folder, and these files will share identical custom settings. For these situations, any <.ini> file can be copied (or renamed) to <default.ini> and DELTAEC will use the settings within <default.ini> for any model run from that folder. If a model has its own individual <.ini>, the individual settings take precedence over <default.ini>.

## 8.3.1 Integration options

Runge-Kutta steps. Default: 10. Recommended range: 1 - 100. This is an integer Nint that determines the number of integration steps used to span each STK\*\*, DUCT, CONE, MIX\*\*, and VX\*\* segment. It does not affect other segment types. It also determines the resolution in state plots: Nint +1 points per integrable segment. Larger values will cause a slower, more accurate computation. Larger values are beneficial for long VX\*\* segments, when large nonzero N flows through STK\*\* segments, and when fluid or solid properties vary dramatically with temperature (e.g., for near-critical helium and/or with the magnetic solids often used in regenerators below 20 K). Small values will increase speed at the price of integration accuracy and possible convergence problems.

Minimum Temperature. Default: 10 K. This is a temperature floor to prevent DELTAEC's shooting method from exploring unphysical temperatures such as negative temperatures. Brave users with special needs at lower temperatures can set this floor to a lower value. (Some of DELTAEC's internal gases use a higher temperature floor. See Chapter 12.)

## 8.3.2 Shooting options

Most of these parameters are described more fully in the online documentation for DNSQ at the SLATEC software repository. More tips on successful shooting in complicated DELTAEC models are in Section 5.4.

Convergence Tolerance. Default: $1 0 ^ { - 8 }$ . Recommended range: $1 0 ^ { - 8 }$ or smaller. This parameter governs the accuracy at which DELTAEC considers its shooting-method iterations finished. See Eq. (8.23). At $1 0 ^ { - N }$ , this should ensure N digits of accuracy for most targets, and values $< 1 0 ^ { - ( N + 4 ) }$ for "zero" targets if the Normalization Mode is 1.

Normalization Mode. Default: 1. In a numerical problem in which the output variables used in the target list differ greatly in magnitudes, a difficulty arises in choosing how much to weigh the errors between each target and corresponding result. This particularly affects \*\*END segments. A 0.001 K error in a heat-exchanger temperature is fairly benign to us, but an error of 0.001 in the normalized complex end impedance $z _ { n }$ could leave us with tens of watts of power flow where there must be zero. In the standard Normalization Mode (1), DELTAEC uses the target weighting described in Eqs. (8.24)–(8.26) to normalize targets, which often does a reasonable job. For unusual cases, set Normalization Mode to an integer $\neq 1$ . Then Eqs. (8.24)–(8.26) become

$$
\begin{array} { l l l } { { w _ { i } } } & { { = } } & { { \mathrm { m i n } \left( { \displaystyle { \frac { 1 } { 3 6 0 } } } , 1 0 ^ { 3 + \mathrm { M o d e } } \right) \mathrm { i f ~ t h e ~ t a r g e t ~ i s ~ a ~ p h a s e ~ a n g l e } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \mathrm { m i n } \left( { \displaystyle { \frac { 1 } { \vert t _ { i } \vert } } } , 1 0 ^ { 3 + \mathrm { M o d e } } \right) \mathrm { i f ~ t h e ~ t a r g e t ~ i s ~ n o t ~ a ~ p h a s e ~ a n g l e } , } } \end{array}
$$

so a higher Mode assigns greater weight to targets $| t _ { i } | \le 1 0 ^ { - 4 }$ . We often find that Mode = -3, -4, or -5 works well for pulse-tube refrigerators and other travelingwave systems with large numbers of guesses and targets. See also the strategy for changing the weights of individual targets described near the end of Section 5.4.2.

EpsFcn. Default: $1 0 ^ { - 1 0 }$ . Recommended range: $> 5 \times 1 0 ^ { - 1 5 }$ . To estimate $\partial F _ { i } / \partial g _ { j }$ using Eq. (8.22), DELTAEC sets $\delta g _ { j } = g _ { j } \sqrt { \mathtt { E p s F c n } }$ (But if $g _ { j } = 0$ , then $\delta g _ { j } = \sqrt { \tt E p s F c n } . )$ A large value of EpsFcn can sometimes speed iterations when initial values of guesses are very inaccurate. Too small a value can cause the solver to lose its way completely, as roundoff error in the computer ruins the accuracy with which $\partial F _ { i } / \partial g _ { j }$ is calculated. The optimal value is computer-dependent and model-dependent. To guard against too-small values, EpsFcn has a built-in floor of $2 \times 1 0 ^ { - 1 6 }$ , twice the double-precision roundoff bound (see Wikipedia, "Machine epsilon").

Step Bound Factor. Default: 100. Recommended range: 0.01-100. This parameter controls the boldness with which DELTAEC first tries to adjust the $g _ { i }$ after the $\partial F _ { i } / \partial g _ { j }$ have been calculated for the first time. Some difficult cases can benefit from a smaller Step Bound Factor.

## 8.4 Error messages

To report a reproducible problem in DELTAEC, email ww@lanl.gov and swift@lanl.gov, with an explanation of what you were doing, including if possible a model that triggers the problem. DELTAEC saves some error-diagnostic messages in <DeltaEC.exe.1og>, whose contents can be seen in the Help pulldown menu. This file might be stored in a folder such as <C: \Users|MyName or <\MyDocuments>. Be sure you can reproduce the problem you plan to report, and include the contents of the log file in your email if your problem causes any messages there.

Occasionally DELTAEC will produce a “wxWidgets Debug Alert." If you see this alert, please copy the cryptic message in the top of the box and send it to ww@lanl.gov and swift@lanl.gov, with a brief explanation of what you were doing. Please also check for a <DeltaEC.exe.1og> file as described in the previous paragraph.

Most of DELTAEC's other diagnostics are meant to be self-explanatory, but some may require additional explanation:

Warnings were generated while parsing... This may indicate a problem with the <. out> file. This can occur when a version-5 model is opened in version 6 or 7 for the first time, or when the savvy user has made a minor mistake when editing a <.out> file with a text editor instead of using DELTAEC's built-in parameter- and segment-modification methods. Examine the <. err> file for specific information. When translating a model from version 5 to version 6 or 7, DELTAEC gives warnings whenever it is unsure of itself, even though it usually makes the right assumptions about the translation.

Success, Partial convergence, or FAILED. The Run Monitor at the bottom of the main display gives one of these three messages after every run, on a panel of green, yellow, or red. "Success" indicates that targets were met with the accuracy implied by Convergence Tolerance (or no targets and guesses exist at all). “FAILED" and Iteration is complete, but some results may not be near their targets indicate that targets have definitely not been met to DELTAEC's satisfaction. If the error occurs on a model that has displayed good convergence under other conditions, this may simply be one pathological point. The user may be able to jump-start it by manually (somewhat intelligently) changing the value of one or two members of the guess list to put the solver on the right track. Otherwise, consider the tactics described in Section 5.4. “Partial convergence" indicates that targets are almost met to DELTAEC's satisfaction, and in most cases the user can also be satisfied. Usually “Partial convergence" can quickly be changed to “Success" simply by running again. If the frequent appearance of “Partial success" becomes a nuisance, try changing the Tolerance and/or Normalization Mode, described in Section 8.3.2. Two other problems are also indicated in the Run Monitor: Choked flow, i.e., velocity amplitude greater than sound speed; and $T _ { m }$ out of bounds, i.e., outside the range from Tmin to 9999 Kelvin.

Plot non-convergence indicators. When a convergence error occurs during an incremental plotting operation, a ‘\*’ is prepended to the plot line for that point, followed by a single digit representing the "info" variable at that point. A typical line in the <.ip> file might then look like this:   
\*4 2.990 98.61 528.2 45.36 559.3 3219.

The plotter indicates such suspicious and failed convergence by plotting the point in red. Below is a key to interpreting the “info" codes:

(a)  
(b)  
![[mu_66afccee_c1839b26135d3420c1d2.jpg]]

![[mu_66afccee_d40995878f9dafc29f4e.jpg]]  
Figure 8.1: (a) Naive and (b) more-realistic sketches of streamlines where two large-diameter DUCTs join. DELTAEC performs inherently one-dimensional calculations, so it naively imagines that the streamlines are as shown in (a). In reality, some high-velocity flow extends into the large-diameter duct, adding inertance that DELTAEC does not automatically account for, and resistive minor losses also occur at high Reynolds numbers. These effects can and usually should be modeled with RPN calculations, MINOR and/or IMPEDANCE segments, and human intelligence.

info= |Significance

$\overline { { * _ { 0 } } }$ Suspicious result. Either choked flow or $T _ { m }$ out of bounds.

$^ * 1$ Partial convergence: The solver considers the iteration successful, but the residual error is suspiciously large.

$^ { * 2 }$ The solver was making progress, but the maximum number of iterations has been reached. Another run might make further progress.

$^ * 3$ Note: Tolerance is set too small for machine double precision.

$^ * 4$ |FAILED: The solver was unable to converge.

Sometimes the user may want to delete the prepended asterisk and number. For example, if the code is $\mathrm { \ddot { \iota } n f o { = } 2 , \mathrm { \ ' } }$ and the remaining error that the solver was working on was already quite small, it might be quite valid to use this plot point instead of discarding it.

## 8.5Inherent limitations

Users should be aware of fundamental, inherent limitations in DELTAEC's ability to model real hardware:

DELTAEC assumes that $p _ { 1 }$ depends only on $x ,$ that $u _ { 1 }$ depends only on x except within the viscous boundary layer, and that $T _ { m }$ depends only on x. Thus, DELTAEC cannot accurately model flow in short-radius elbows, flow and pressure at abrupt transitions between DUCTs of different areas (as shown in Fig. 8.1), or inertial or thermal effects in thermal buffer tubes and pulse tubes with significant Rayleigh streaming. (For example, in STKDUCT, $T _ { m } ( x )$ and $T _ { \mathrm { s o l i d } } ( x )$ are equal for all x, which is a very bad approximation if significant Gedeon streaming, Rayleigh streaming, or jet-driven streaming is present.) We use MINOR segments, RPN segments, IMPEDANCE segments, and off-line hand calculations to try to account for 2- and 3-dimensional effects like these.

The derivations of most thermoacoustic equations rely on the assumption that the gas displacement amplitude $| U _ { 1 } | / \omega A$ is much smaller than all other relevant dimensions in the x direction. This assumption is often violated in thermoacoustic components, especially heat exchangers, whose length in the x direction is seldom larger than $2 \left| U _ { 1 } \right| / \omega A$

The turbulence algorithm in DUCT, CONE, and $\boldsymbol { \mathrm { V X * * } }$ is based on the quasi-steady approximation, namely that the pressure gradient at any instant of time in time-dependent flow is the same as that which would be present for steady flow at the same rate. This is known to be naive [49, 50, 51, 52].

Similarly, the turbulence algorithm in STKSCREEN and STKPOWERLW is based on the quasisteady approximation, which is a poor approximation when gas displacement amplitude is smaller than, or comparable to, the screen pore size. Thus, this aspect of DELTAEC works poorly at low amplitudes.

Harmonics are often present in $p ( t )$ and $U ( t )$ , but DELTAEC works exclusively with the fundamentals $p _ { 1 }$ and $U _ { 1 }$ . This limitation usually has little impact on the accuracy of power calculations [13], but experiments being compared to DELTAEC calculations must use instruments that measure the fundamental components of the wave, not rms or peak values.

DELTAEC's shooting method is efficient at converging to solutions for complicated systems; however, it knows nothing about acoustics, or any other aspect of physical reality. DELTAEC doesn't know that negative frequencies, negative lengths, or pressure amplitudes greater than the mean pressure are improper; it simply does the math. Thus, the reasonableness of the answers produced by DELTAEC's shooting method often depends on the quality of the initial guesses, which in turn depends on the thermoacoustics knowledge of the user.

Be alert for situations where DELTAEC cannot be expected to understand the user's intentions. DELTAEC does not warn the user of all such possible inconsistencies and ambiguities. For example, DELTAEC can't guess why a user would allow nonzero $\dot { N }$ to flow through an enclosed \*\*SPEAKER or \*\*DUCER, so no change in $p _ { \mathrm { 2 , 0 , D E C } }$ is calculated. The velocity term in Eq. (6.12) for $p _ { \mathrm { 2 , 0 , t o t } }$ depends on area, so $\mathrm { d o n ^ { \prime } t }$ be surprised if you disagree with its calculation at an IMPEDANCE segment, since IMPEDANCEs have no area. Allowing significant nonzero $\dot { H } _ { 2 , k }$ (when $\dot { H } _ { 2 , k } \neq \dot { E } )$ to flow through an IMPEDANCE or a tight-gapped HX or TX is physically implausible, and leads to errors in the calculation of $\dot { N } _ { 2 , 0 }$ via Eq. (8.16) and thus to erroneous calculation of $p _ { \mathrm { 2 , 0 , D E C } }$

vXQ1 and vXQ2 rely on assumptions that may be invalid in some circumstances. See Section 10.7.3 for details.

The shooting method requires that target results change smoothly as guesses are varied, so the near-linearity assumed in Eqs. (8.22) can be a good-enough approximation for small variations in the guesses. So, be wary of building step-function or absolutevalue calculations into RPN segments if downstream target results depend on them. For example, if a model is operating near $| \xi _ { 1 } | = D$ at the location of an orifice plate in a DuCT, abruptly switching on a minor loss as shown here may be very problematic if the model is operating close enough to the transition that DELTAEC's guess variations carry it back and forth between $\left. \xi _ { 1 } \right. > D$ and $| \xi _ { 1 } | < D$

5   
RPN inp = orifice diameter (m); result = area (m2)   
1.0000E-2 a G or T 7.8540E-5 A m2   
inp 2 / sqrd pi \*   
!- 6   
RPN Turn on minor loss only if |xi\_1| > D. Result is 0 or 1.   
0.0000 a G or T 1.0000 A K+, K-  
U1 mag 5A / w / 5a - sto abs rcl / 1 + 2 /   
MINOR small orifice plate in big duct   
sameas 5A a Area m^2   
sameas 6A b K+   
sameas 7b c K-

A more subtle abrupt change in results can arise from DELTAEC's treatment of phase angles. When displaying its internal complex numbers as magnitude and phase, DELTAEC selects the phase to be $- 1 8 0 ^ { \circ } < \theta \leq 1 8 0 ^ { \circ }$ . Targeting phase angles near $0 ^ { \circ }$ $9 0 ^ { \circ } , \ \mathrm { o r \ } - 9 0 ^ { \circ }$ is unproblematic. However, when trying to target a phase to be $1 8 0 ^ { \circ }$ DELTAEC's shooting method explores guess values that yield results both slightly above and slightly below $1 8 0 ^ { \circ }$ . The results that are slightly above 180° will be seen by the shooting method as slightly above $- 1 8 0 ^ { \circ } ~ ( \mathrm { e . g . , 1 8 1 ^ { \circ } }$ becomes $- 1 7 9 ^ { \circ } )$ , and the shooting method will have no chance to hit this target. The simplest way to avoid this problem is to shift the time phase of the entire model by a large, convenient amount, such as $1 8 0 ^ { \circ } ~ \mathrm { o r } ~ \pm 9 0 ^ { \circ }$ . (See Section 2.6.2.) Another simple work-around is to target sin θ = 0 instead of $\theta = 1 8 0 ^ { \circ }$ , although this technique can sometimes let the shooting method “jump"from $\theta = 1 8 0 ^ { \circ } { \mathrm { ~ t o ~ } } \theta = 0 ^ { \circ }$ . More awkwardly, to convert a standard DELTAEC phase angle to a function that changes smoothly as it passes through 180°, use the following trick, which yields ph(U) if $\mathtt { p h } ( \mathtt { U } ) > 0 .$ and adds $3 6 0 ^ { \circ }$ to ph(U) if $\mathtt { p h } ( \mathtt { U } ) < 0$ , thus shifting the troublesome discontinuity from 180° to $0 ^ { \circ }$

7   
RPN target phase(U1) here to be 180   
180.00   
U1 arg U1 arg abs - U1 arg / 180 \* U1 arg +

## 9. Good design habits

When we study fundamental thermoacoustics issues, we try to design experiments to minimize unrelated effects so the issues being studied stand out clearly. In contrast, when we apply what we know about thermoacoustics to design a practical device for a goal-oriented sponsor, we often find ourselves forced by the sponsor's goals into operating conditions with great complexity and significant uncertainty, and yet we must account for everything as well as possible. This chapter outlines some habits that we use at Los Alamos, as of 2008, to make complex DELTAEC design models as realistic as possible, so we and our goal-oriented sponsors are not disappointed when hardware is built and tested.

Our philosophy: (1) Attention to details, because there are many details and their effects add up. (2) Component-by-component conservatism, based on experimental evidence when it differs from “raw" DELTAEC results. Ignoring these considerations can lead to factor-oftwo overprediction of performance.

We try to be honest with ourselves about these issues: If there are enough such issues present in a given design, then uncertainties should tend to average out if each issue is treated honestly, so we'll end up with hardware that works approximately like we predict, with equal probability of working a little better or a little worse. In contrast, neglecting these issues early in a design process can produce misleading “optimization" that does not represent reality, and neglecting them in the final stages of a design usually leads to disappointment when hardware is tested.

Note that some of these details can be neglected at low amplitudes.

(Thanks to Scott Backhaus for contributions to this chapter.)

## 9.1 Attention to details

## 9.1.1 Imperfect external heat exchange

We pay attention to the interfaces between DELTAEC-modeled heat exchangers and their environment. Even though DELTAEC is not set up to model anything outside the “skin" of the solid that is in contact with the thermoacoustic gas in heat exchangers, many effects beyond that boundary are important, and should be modeled, either using RPN segments within DELTAEC or using calculations elsewhere (e.g., spreadsheets). For example, in a water-cooled heat exchanger, non-negligible temperature differences usually exist across the water boundary layer (due to the finite thermal conductivity of the water) and between the inlet and outlet streams (due to the finite specific heat and flow rate of the water). Our sponsors usually care about the water inlet temperature, not DELTAEC's heat-exchanger internal temperature. Similar considerations apply in a drilled metal-block heat exchanger that relies on conductivity of metal to transfer heat between the thermoacoustic gas in the drilled channels and an external heat source or sink at the perimeter of the block.

## 9.1.2 Internal 2-D effects from imperfect external heat exchange

DELTAEC assumes that $p _ { 1 } , U _ { 1 }$ , and $T _ { m }$ are independent of coordinates perpendicular to x. Sometimes the low heat capacity and/or low flow rate of an external heat-transfer fluid (especially combustion products from a burner flowing through an engine's hot heat exchanger) ruin this $\mathrm { l a t e r a l l y - u n i f o r m } { - } T _ { m }$ assumption in a cross-flow heat exchanger, thereby ruining the same assumption in an adjacent stack or regenerator, which in turn can cause lateral nonuniformity in $U _ { 1 }$ and/or internal streaming in the stack or regenerator. DELTAEC is fundamentally ill suited to modeling such issues, yet we must consider them. To get a rough idea of the impact of such nonuniformity, we have sometimes used TBRANCH and UNION to split a hx-regen-hx (or hx-stack-hx) package into two (or even three) parallel subsets, each with half (or a third) of the total area, allowing different $T _ { m } ( x )$ in each. RPN calculations can be used to keep the heat-exchanger temperatures consistent with the heat-transfer fluid's flow rate and heat capacity. (Such split models usually require so many guesses and targets that other guesses and targets in the model must be disabled while this issue is being explored.)

## 9.1.3 Heat leaks

We include axial thermal conduction of the pressure vessel surrounding any STK\*\* components that have nonzero axial temperature gradients. This is built in to STKDUCT and STKCONE segments, but it is not built in to the other STK\*\* segments used for stacks and regenerators. In STKSCREEN regenerators, we often tie ksFrac to an RPN calculation that knows the vessel wall geometry, so the vessel wall conduction shows up directly in HX or other \*X segments' results. If the screens and the pressure vessel are made of the same material, the expression is

$$
k _ { s , \mathrm { F r a c , e f f e c t i v e } } = k _ { s , \mathrm { F r a c , L e w i s } } + \frac { A _ { \mathrm { w a l l } } } { \left( 1 - \phi \right) A _ { \mathrm { s c r e e n } } } ,\tag{9.1}
$$

where $k _ { s , \mathrm { F r a c , L e w i s } } = 0 . 1$ is recommended by Lewis et al. [28] for stacked metal screens. In other cases, we add and subtract appropriate conduction estimates to HX and other \*X heats using RPN segments, yielding “net" heats as RPN results. In the early stages of a design, such RPNs can keep wall thickness proportional to STK\*\* diameter, making this heat leak track the reality of ASME pressure-vessel design.

We model black-body radiation heat leaks along pulse tubes and thermal buffer tubes using RPNs, adding them to DELTAEC's built-in \*X calculations to obtain "net" heats. We assume that the walls of such tubes are fairly good infrared reflectors and the flow straighteners at the ends are fairly good black-body surfaces, so we use $\sigma _ { \mathrm { S t e f a n - B o l t z m a n n } } A \left( T _ { H } ^ { 4 } - T _ { C } ^ { 4 } \right) / 2$ where A is the inside area of the STKDUCT and the factor of 2 accounts very roughly for the "fairly good" surfaces. We neglect black-body radiation within STKSCREENs, which are optically opaque. We still debate whether and how to account for black-body radiation in standing-wave stacks, where the long aspect ratio of the channels gives radiation ample opportunity for absorption and re-emission at intermediate temperatures.

We also account for unavoidable heat flow through insulation layers wrapped around components, with RPNs or separate spreadsheets.

In systems with toroidal topology (e.g., TASHE [40, 5]), we suppress Gedeon streaming, or account for it with nonzero $\dot { N }$

## 9.1.4 Geometry

As a design evolves towards its final state, we add more and more geometrical detail to the DELTAEC model. Even including the short gaps between regenerators and heat exchangers, or accounting for weld shrinkage that shortens such gaps, is not too much attention to detail.1 When shop drawings are being prepared, we modify the DELTAEC model to reflect machine-shop realities (e.g., inch-based dimensions; available drill sizes). While assembling parts, we often check measured dimensions against the DELTAEC model one more time.

## 9.1.5 Actual operating conditions

Actual operating conditions are seldom identical to the final "design" condition, especially for ambient temperature. When comparing experimental results with DELTAEC calculations to decide whether hardware is working acceptably well, we always use actual, experimental conditions for parameters like ambient temperature. (See also Section 5.3 in this Users Guide, and Section 9.4 in Ref. [13], to consider what variables to regard as "given.")

In high-power systems, different parts of an “ambient"-temperature resonator can have significantly different temperatures. We often use RPN expressions like “inp =Tm" or “Tm inp + =Tm" to make our DELTAEC models follow this reality.

## 9.1.6 Thermophysical properties

DELTAEC's built-in thermophysical properties may not be accurate in the temperature (or pressure) range of interest for a new design. If we are going to work far from room temperature and/or with a new gas or solid, we check DELTAEC's gas and solid properties against some reliable reference, and create our own <.tpf> file if necessary.

## 9.2 Component conservatism

We rely on best-estimate "headroom" associated with every segment in the DELTAEC models wherever our previous experience shows that experimental performance falls a little short of the built-in first-principles calculations.

## 9.2.1 Turbulence

We habitually use a value of $5 \times 1 0 ^ { - 4 }$ for the relative surface roughness in DUCTs and CONEs, even when it is greater than the actual roughness, because this gives results that fit a lot of $\dot { N } = 0$ data over the past 15 years. When steady flow is superimposed, we use the “average" turbulence setting, which is consistent with halfway between the two lines in Fig. 9 in Ref. [42].

We use MINOR segments generously wherever appropriate, e.g., corner turning, TBRANCHs and uNIONs, and area changes (except very gently tapered cones), with Idelchik's book [53] for estimates of the K coefficients. We even check the need for MINOR segments at transitions between heat exchangers and open ducts, where abrupt changes in GasA/A occur. In toroidal TASHEs [40, 5], we might include almost a dozen MINOR segments.

## 9.2.2 Adiabatic-isothermal mixing

We use J0IN segments wherever appropriate, e.g., on both ends of pulse tubes, thermal buffer tubes, and hx-regen-hx packages. J0IN segments are usually negligible around hx-stack-hx packages in standing-wave systems, but we always check anyway.

We know that some of the same dissipative physics is present if the gap between a heat exchanger and an adjacent regenerator or stack is an appreciable fraction of the volumeflow-rate amplitude and is spatially stratified, so we strive to keep such gaps small and/or well-mixed by jets.

## 9.2.3 Stacked screen regenerators

We determine the “nominal" hydraulic radius $r _ { h }$ of a stacked-screen regenerator using the manufacturer's specified wire diameter, the volumetric porosity determined by weighing the complete regenerator, and Eq. (10.124). We have never seen a pressure drop across a stacked-screen regenerator that is smaller than DELTAEC predicts using this nominal $r _ { h }$ Our measured pressure drops have ranged from 0% to 15% above DELTAEC predictions using the nominal value. Conservatively taking the upper half of that range, and noting that the pressure drop goes like $r _ { h } ^ { - 2 }$ , we usually set the DELTAEC $r _ { h }$ equal to 0.93–0.96 times the nominal value.

We set ksFrac equal to 0.1 to account for screen-to-screen conduction, as recommended for metal screens by Ref. [28], unless we are using this parameter to account for pressurevessel-wall conduction [see Eq. (9.1)] as well as the screen-to-screen conduction.

Remember that the friction-factor and heat-transfer coefficients are valid only over a narrow range of porosity, perhaps as narrow as $0 . 6 < \phi < 0 . 7 7$ , as shown in Ref. [54] or [55]. Results can depend strongly on $\phi ,$ so make changes gradually within this narrow range.

## 9.2.4 Pulse tubes and thermal buffer tubes

We know that jet-driven streaming in pulse tubes and thermal buffer tubes can carry a lot of heat, so we always use screen flow straighteners on both ends, using SX segments to model their acoustic characteristics in DELTAEC and using the guidance near Eq. (7.86) in Ref [13] to choose the screen size and number of layers. Since this design process does not fill us with confidence, we sometimes double the number of layers, because it is often easier to remove unnecessary layers later than to add layers later.

Rayleigh streaming can also carry a lot of heat in these tubes. In the experiment described in Ref. [31], very careful tuning of the phase of $Z$ in a pulse tube could bring that streaming heat leak to zero, but we generally don't expect to keep pulse tubes so accurately tuned at all times. Thus, we try to work as close as possible to the zero-Rayleigh-streaming condition described in Ref. [29] while avoiding cone angles that might create flow separation, and even then we usually deduct 10% of $\dot { E }$ at the cold heat exchanger from DELTAEC's raw prediction of cooling power in pulse-tube refrigerators, and add 10% of $\dot { E }$ at the hot heat exchanger to the heater power in engines having thermal buffer tubes. (This correction also affects the ambient heat exchangers at the other ends of the tubes.) It is not unreasonable to encode the math described in Ref. [29] in RPN segments (it takes more than one!) to keep an eye on this issue in a model with a pulse tube or thermal buffer tube. Note that our experience is mostly with high-power, large-aspect-ratio engines and refrigerators; these issues are probably less important in slender pulse tubes and thermal buffer tubes.

Large-aspect-ratio refrigerator regenerators can suffer from regenerator internal streaming, as described in Ref. [56], which must be accounted for, even if only approximately.

(See also “Adiabatic-isothermal mixing" and "Heat leaks—black-body radiation" above.)

## 9.2.5 Standing-wave engine stacks

At low amplitudes, standing-wave engines have worked in agreement with DELTAEC predictions, so we trust that the calculations are correct to lowest order (i.e., energy expressions are correct to second order in acoustic amplitude). However, at higher amplitude, measurements on standing-wave engines are always worse than calculations: higher hot temperature $T _ { H }$ and higher heater power $\dot { Q } _ { H }$ for a given $p _ { 1 }$ and $Z .$ Thus, until research brings understanding to this situation, we build some “headroom" into our DELTAEC designs of standing-wave engines.

Figures 2 and 3 in Ref. [25] show that the extra, unaccounted-for heater power is proportional to ${ \left| p _ { 1 } \right| } ^ { 3 }$ and the extra, unaccounted-for hot temperature is proportional to $\left| p _ { 1 } \right| ^ { 2 }$ In the absence of any evidence to the contrary, we assume that these dependences on $\left| p _ { 1 } \right|$ are applicable to all standing-wave engines.

Figure 9.1 summarizes our experience with a few standing-wave engines, with all data extrapolated to $\left. p _ { 1 } \right. / p _ { m } = 0 . 1 0$ at the hot end of the stack using the pressure dependences described in the previous paragraph. The honeycomb data (small symbols) are more reliable than the parallel-plate data (large triangles), so we trust the honeycomb fit (dashed curves) more than the parallel-plate fit (solid curves). We believe that putting some headroom in standing-wave designs as suggested by Fig. 9.1 and the pressure dependences described above is much better than putting in no headroom at all.

![[mu_66afccee_22daeb5112770719749a.jpg]]  
Figure 9.1: The vertical axis shows the experimentally observed extra $T _ { H }$ (blue) or $\dot { Q } _ { H }$ (pink), in excess of DELTAEC's calculations, divided by DELTAEC's values, for standingwave engines that we have used. The horizontal axis is $\delta _ { \kappa }$ at the ambient end of the stack, divided by $r _ { h }$ . All data are scaled to $\left| p _ { 1 } \right| / p _ { m } = 0 . 1 0$ at the hot end of the stack, using $\left| p _ { 1 } \right| ^ { 3 }$ scaling for extra $\dot { Q } _ { H }$ and $| p _ { 1 } | ^ { 2 }$ scaling for extra $T _ { H }$ . Data from three honeycomb (STKCIRC) stacks are shown: “simil honeycomb" is Ref. [25], "cascade honey" is Ref. [19], and “Tex honeycomb" is Ref. [57]. Unpublished data from two spiral (STKSLAB) stacks are shown: “Cryenco 100 gpd" is from the engine shown in Fig. 4 of Ref. [58], corroborated by measurements on a half-scale model at Los Alamos, and with the range of data for heater power indicating low acoustic load (more excess heat) vs. heavy acoustic load (less excess heat), and “Tek spiral" is from the engine described in Ref. [57] but with the honeycomb stacks replaced by spiral stacks as shown in Fig. 1.11 in Ref. [13].

## 10. Physical segments

All of DELTAEC's physically meaningful segment types are listed in this chapter, organized by function. Logistical and management segments appear in the next chapter. An alphabetical index of all segment types is in the Segment Index at the end of the Users Guide.

## 10.1 Ducts and cones

## 10.1.1 DUCT

## General description:

Use DUCT for circular ducts of any diameter, and for large ducts (i.e., with $r _ { h } \gg \delta _ { \nu } , \delta _ { \kappa } )$ of any cross-sectional shape by giving suitable area and perimeter. Mean temperature is independent of x, while $p _ { 1 }$ and $U _ { 1 }$ evolve with x.

DELTAEC's turbulence algorithm is controlled through optional parameter d, the relative roughness ε, whose definition for steady flow can be found in fluid-mechanics textbooks [59]: roughness height divided by pipe diameter. We have found that $\varepsilon = 0 . 0 0 0 5$ works well in highamplitude acoustics, even if the geometrical roughness is smaller than

![[mu_66afccee_40b8243f63313767394c.jpg]]

this value. Omitting this parameter forces the calculation to be laminar at all Reynolds numbers, no matter how large.

(See also STKDUCT in Section 10.6.1, which allows a temperature gradient along a duct in boundary-layer approximation.)

## Input variables:

Area $( \mathrm { m } ^ { 2 } )$ Cross-sectional area A available to the gas, based on inside dimensions of the DUCT.

Perim (m) Perimeter I of the inside cross section described above.

Length (m) The length $\Delta x$ of the DUCT.

Laminar/turbulent Whenever the laminar box is checked, the calculations of $d p _ { 1 } / d x$ and $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ in the DUCT are based on noninteracting flow, using laminar flow for $d p _ { 1 } / d x$ and either laminar or turbulent flow for $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ , depending on the steady-flow Reynolds number. The laminar condition is identified in the <.out> file as a blank line where input d would otherwise be.

Srough This input variable appears if the turbulent box is checked in the Optional Parameters dialog. Srough is ε, the surface roughness inside the DUCT, relative to the diameter. This is called “relative roughness" in many fluid-mechanics books, for steady flow. However, for oscillating flow, we usually regard Srough as a fitting parameter, with a typical value of $\varepsilon = 5 \times 1 0 ^ { - 4 }$ . Larger values yield higher turbulent dissipation of $\dot { E }$

Optimistic/Normal/Pessimistic These choices appear if the turbulence box is checked in the Optional Parameters dialog and if the "Enable Ndot" box is checked in the BEGIN segment. These choices control the nonlinear interaction between oscillating flow and steady flow in the DUCT. “Optimistic" and "Pessimistic" refer to the two calculation schemes described in Ref. [42], and “Normal" is the average of the two. For the optimistic case, the turbulent steady and turbulent oscillating flows are assumed to be independent, simply superimposed. For the pessimistic case, the turbulent steady flow and turbulent oscillating flow are assumed to interact with each other and to increase each other's resistive effects according to the quasi-steady approximation. In the <.out> file, Optimistic/Normal/Pessimistic is recorded with SrOptm, Srough, or SrPess to indicate the name of ε.

Solid The solid material on the inside surface of the DUCT. (This is used only in the calculation of $\epsilon _ { s } .$ , which is seldom significant in DUCTs.)

## Potential targets:

None.

## Master—slave links:

The perimeter of a DuCT can be slaved to its area to keep the cross-sectional shape the same when area is varied.

The length of a DUCT can be slaved to the length of another segment to keep the total length constant.

(For an introduction to master-slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

Many examples of DUCT occur throughout Chapters 2, 5, and 6.

Calculation of $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ with $\dot { N } = 0$

In DUCTs with no superimposed steady flow, $p _ { 1 }$ and $U _ { 1 }$ evolve according to

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A } U _ { 1 } ,\tag{10.1}
$$

$$
\frac { d U _ { 1 } } { d x } = - \frac { i A \omega } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { \gamma - 1 } { 1 + \epsilon _ { s } } f _ { \kappa } \right) p _ { 1 } ,\tag{10.2}
$$

which are equivalent to

$$
\left( 1 + \frac { \gamma - 1 } { 1 + \epsilon _ { s } } f _ { \kappa } \right) p _ { 1 } + \frac { a ^ { 2 } } { \omega ^ { 2 } } \left( 1 - f _ { \nu } \right) \frac { d ^ { 2 } p _ { 1 } } { d x ^ { 2 } } = 0 .\tag{10.3}
$$

In laminar DUCTs of length $\Delta x$ , these are equivalent to

$$
\begin{array} { r c l } { { p _ { 1 , \mathrm { o u t } } } } & { { = } } & { { p _ { 1 , \mathrm { i n } } \cos k \Delta x - \cfrac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) k A } U _ { 1 , \mathrm { i n } } \sin k \Delta x , } } \\ { { } } & { { } } & { { } } \\ { { U _ { 1 , \mathrm { o u t } } } } & { { = } } & { { U _ { 1 , \mathrm { i n } } \cos k \Delta x - \cfrac { i ( 1 - f _ { \nu } ) k A } { \omega \rho _ { m } } p _ { 1 , \mathrm { i n } } \sin k \Delta x , } } \end{array}\tag{10.4}
$$

with complex wave number k given by

$$
k = \frac { \omega } { a } \sqrt { \frac { 1 + ( \gamma - 1 ) f _ { \kappa } / ( 1 + \epsilon _ { s } ) } { 1 - f _ { \nu } } } .\tag{10.5}
$$

In DUCTs, we define the effective radius to be $r _ { 0 } = 2 A / \Pi$ . (For circular cross sections, this is indeed the radius of the circle. For other cross sections, it is twice the hydraulic radius.) In narrow DUCTs, for $r _ { 0 } / \delta _ { j } < 2 5 $ 2 $f _ { \kappa }$ and $f _ { \nu }$ are calculated using complex Bessel functions

$$
f _ { j } = \frac { 2 J _ { 1 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } { ( i - 1 ) ( r _ { 0 } / \delta _ { j } ) J _ { 0 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } \mathrm { f o r } j = \kappa \mathrm { o r } \nu .\tag{10.6}
$$

Where $r _ { 0 } / \delta _ { j } > 3 0$ , the boundary-layer approximation is used:

$$
f _ { j } = ( 1 - i ) \Pi \delta _ { j } / 2 A \mathrm { ~ f o r ~ } j = \kappa \mathrm { ~ o r ~ } \nu .\tag{10.7}
$$

For intermediate values, linear interpolation is used to make a smooth match between the two regimes. While the narrow-duct solution assumes a circular cross section, the shape of the duct is irrelevant in the boundary-layer approximation. A square duct with dimensions much larger than the penetration depth can be modeled simply by choosing $\Pi = 4 { \sqrt { A } }$ , for example.

When turbulent, $p _ { 1 }$ and $U _ { 1 }$ are numerically integrated according to Eqs. (10.1) and (10.2) above, with $f _ { \nu }$ and $f _ { \kappa }$ modified as described below to account for the turbulence. DELTAEC's turbulence algorithm is described in detail in Chapter 7.2 of Ref. [13] and is based on the quasi-steady approximation: that turbulent oscillatory flow is described by the Moody friction factor at each instant of time during the oscillatory flow. (See any engineering fluid mechanics textbook, such as Ref. [59], to review the Moody friction factor as a function of Reynolds number and relative roughness of the pipe wall.) This assumption must be excellent in the low-frequency limit, in which $r _ { 0 } / \delta _ { \nu }  0$ . This limit is approached in the inertances of the lowest-power pulse-tube refrigerators. We have learned by experience with a few large systems that the assumption is reasonable for large $r _ { 0 } / \delta _ { \nu }$ , which is of interest in the resonators of standing-wave thermoacoustic systems. For experimental validation of the assumption for intermediate $r _ { 0 } / \delta _ { \nu }$ , see Ref. [15].

To account for turbulence, DELTAEC increases the resistive component of the pressure gradient, and hence the viscous power dissipation, by

$$
m _ { \nu } = \frac { \delta _ { \nu } ^ { 2 } N _ { R } } { 2 4 \pi r _ { h } ^ { 2 } } \frac { \left[ f _ { M } - \left( 1 - 9 \pi / 3 2 \right) N _ { R } d f _ { M } / d N _ { R } \right] } { \mathrm { R e } \left[ i / \left( 1 - f _ { \nu } \right) \right] } .\tag{10.8}
$$

DELTAEC evaluates the Moody friction factor $f _ { M }$ and its derivative with respect to Reynolds number, $d f _ { M } / d N _ { R }$ , as functions of Reynolds number and $\varepsilon$ using the iterative expression

$$
\frac { 1 } { \sqrt { f _ { M } } } = 1 . 7 3 8 5 - 2 \log _ { 1 0 } \left( 2 \varepsilon + \frac { 1 8 . 5 7 4 } { N _ { R } \sqrt { f _ { M } } } \right) ,\tag{10.9}
$$

which is a remarkably good approximation [59, 60]. (In our own work at Los Alamos, we have set roughness equal to $5 \times 1 0 ^ { - 4 }$ for many years, as representative of most turbulent acoustic losses in ducts, even when the actual surface roughness over pipe diameter is smaller than this value.) DELTAEC decreases the inertial pressure gradient by

$$
m _ { \nu } ^ { \prime } = \left( \frac { 1 - \delta _ { \nu } / r _ { 0 } } { 1 - \delta _ { \nu } / m _ { \nu } r _ { 0 } } \right) ^ { 2 }\tag{10.10}
$$

to correct approximately for the steeper velocity gradient at the wall, which increases the effective area open to gas that contributes to inertial effects. The factors $m _ { \nu }$ and $m _ { \nu } ^ { \prime }$ are applied using

$$
\mathrm { I m } \left[ \frac { 1 } { 1 - f _ { \nu } } \right] = m _ { \nu } \mathrm { I m } \left[ \frac { 1 } { 1 - f _ { \nu , \mathrm { l a m i n a r } } } \right] ,\tag{10.11}
$$

$$
\mathrm { R e } \left[ \frac { 1 } { 1 - f _ { \nu } } \right] = m _ { \nu } ^ { \prime } \mathrm { R e } \left[ \frac { 1 } { 1 - f _ { \nu , \mathrm { l a m i n a r } } } \right] ,\tag{10.12}
$$

$$
f _ { \nu } = 1 - \left( \mathrm { R e } \left[ \frac { 1 } { 1 - f _ { \nu } } \right] + i \mathrm { I m } \left[ \frac { 1 } { 1 - f _ { \nu } } \right] \right) ^ { - 1 }\tag{10.13}
$$

DELTAEC also multiplies $\delta _ { \kappa }$ by $m _ { \nu }$ before using $\delta _ { \kappa }$ in Eq. (10.6) or (10.7), in an attempt to account very approximately for changes in thermal relaxation losses due to increased heat transfer.

At low enough velocities, $m _ { \nu }  1$ and DELTAEC reverts to a laminar calculation. The $m _ { \nu } = 1$ boundary between the laminar and turbulent zones in DELTAEC occurs roughly at

$$
N _ { R } ~ \simeq ~ 2 0 0 0 \mathrm { f o r } r _ { 0 } / \delta _ { \nu } < 2 ,\tag{10.14}
$$

$$
{ \frac { N _ { R } } { 2 r _ { h } / \delta _ { \nu } } } ~ \simeq ~ 1 0 0 0 ~ \mathrm { f o r } ~ r _ { 0 } / \delta _ { \nu } > 2 .\tag{10.15}
$$

Whether laminar or turbulent, and in both small and large DUCTs, the boundary-layer approximation is used for the effect of the solid on thermal-hysteresis loss:

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } .\tag{10.16}
$$

Calculation of $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ with $\dot { N } \neq 0$

Nonzero $\dot { N }$ in a DUCT creates a Doppler-shift effect on $p _ { 1 }$ and $U _ { 1 }$ , an increased resistive effect on $p _ { 1 }$ if the flows are turbulent, and a time-averaged resistive head loss. Whether the flows are treated as laminar or as one of three varieties of turbulent is controlled by the user. The pressure and volume flow rate change with x according to

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { A ( 1 - f _ { \nu } ) } U _ { 1 } + \frac { i \omega m \dot { N } } { \rho _ { m } a ^ { 2 } A } \frac { 1 + ( \gamma - 1 ) f _ { \kappa } / ( 1 + \epsilon _ { s } ) } { ( 1 - f _ { \nu } ) } p _ { 1 } ,\tag{10.17}
$$

$$
\frac { d U _ { 1 } } { d x } ~ = ~ - \frac { i \omega A } { \rho _ { m } a ^ { 2 } } \frac { 1 + ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } p _ { 1 } + \frac { i \omega m \dot { N } } { \rho _ { m } a ^ { 2 } A ( 1 - f _ { \nu } ) } U _ { 1 } ,\tag{10.18}
$$

which can be derived using standard results of thermoacoustics combined with Eqs. (11.1.3) in Morse and Ingard's Theoretical Acoustics, Ref. [33]. (In CoNEs, A is a function of x.)

Reference [42] describes two approaches to the calculation of the resistive effects on $f _ { \nu } , f _ { \kappa } ,$ and $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ if the flow is turbulent. These two approaches, which we call “optimistic" and "pessimistic," bracket the experimental results in that paper. In DELTAEC the user can select either of these two approaches, or their average. Until more physics is learned, we recommend selecting the average by checking the "Normal" box, because the experimental results in Ref. [42] were roughly the average of the optimistic and pessimistic calculations.

For the optimistic case, the turbulent steady and turbulent oscillating flows are assumed to be independent, simply superimposed. Turbulent $f _ { \nu }$ and $f _ { \kappa }$ are calculated with Eqs. (10.8)−(10.10).

For the pessimistic case, the turbulent steady flow and turbulent oscillating flow are assumed to interact with each other and to increase each other's resistive effects, as described in the appendix of Ref. [42]. In this case, $f _ { \nu }$ and $f _ { \kappa }$ are calculated according to the procedure described near Eqs. (10.8)-(10.10), but with the turbulent multiplier $m _ { \nu }$ enhanced by the steady flow according to

$$
m _ { \nu } = \frac { \delta _ { \nu } N _ { R , \mathrm { m a x } } } { 1 6 r _ { h } } \left[ \left| \varepsilon _ { 2 , 0 } \right| f _ { M , \mathrm { m a x } } + \frac { \left( 3 - 2 \left| \varepsilon _ { 2 , 0 } \right| \right) \left( 1 - 2 \left| \varepsilon _ { 2 , 0 } \right| \right) } { 8 ( 1 + \left| \varepsilon _ { 2 , 0 } \right| ) } \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } \right] , \left| \varepsilon _ { 2 , 0 } \right| \geq 1 ,\tag{10.19}
$$

$$
\begin{array} { c } { { \displaystyle = \frac { \delta _ { \nu } N _ { R , \mathrm { m a x } } } { 1 2 \pi r _ { h } } \{ [ ( 1 + \frac { \varepsilon _ { 2 , 0 } ^ { 2 } } { 2 } ) \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { 3 } { 2 } \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } ] f _ { M , \mathrm { m a x } }  } } \\ { { \displaystyle - [ ( 1 + \frac { \varepsilon _ { 2 , 0 } ^ { 2 } } { 2 } ) \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { 3 } { 2 } \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } - \frac { 9 \pi } { 3 2 } \frac { 1 + 4 \varepsilon _ { 2 , 0 } ^ { 2 } } { 1 +  \varepsilon _ { 2 , 0 }  } ] \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } \} , ~  \varepsilon _ { 2 , 0 }  \le 1 , } } \end{array}\tag{10.20}
$$

where the friction factor and its slope are based on the peak Reynolds number

$$
N _ { R , \operatorname* { m a x } } = \frac { \left( m | \dot { N } _ { 2 , 0 } | / \rho _ { m } + | U _ { 1 } | \right) 4 r _ { h } \rho _ { m } } { A \mu }\tag{10.21}
$$

and $\varepsilon _ { 2 , 0 } = m \dot { N } _ { 2 , 0 } / \rho _ { m } \left| U _ { 1 } \right|$ . The derivations of these expressions can be found in the appendix of Ref. [42].

## Calculation of $p _ { 2 , 0 , \mathbf { D E C } } ( x )$ with $\dot { N } \neq 0 :$

How the flow is treated depends on the roughness parameter in the DUCT. There are three cases: optimistic, pessimistic, and "normal," which is the average of the other two.

For the optimistic case, the turbulent steady and turbulent oscillating flows are assumed to be independent, simply superimposed. The steady-flow pressure drop is calculated using

$$
\frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } = - \mathrm { s i g n } ( \dot { N } _ { 2 , 0 } ) \frac { 1 } { 2 } \rho _ { m } \left( \frac { m \dot { N } _ { 2 , 0 } } { \rho _ { m } A } \right) ^ { 2 } \frac { f _ { \mathrm { M o o d y , s t e a d y } } } { 4 r _ { h } } .\tag{10.22}
$$

The steady-flow Moody friction factor fMoody,steady is calculated with a Reynolds number based on the steady velocity:

$$
N _ { R , 2 , 0 } = \frac { m | \dot { N } _ { 2 , 0 } | 4 r _ { h } } { A \mu } .\tag{10.23}
$$

For the pessimistic case, the turbulent steady flow and turbulent oscillating flow are assumed to interact with each other and to increase each other's resistive effects, as described in the appendix of Ref. [42] ignoring any dependence on $p _ { 1 }$ and in Section 14.4 including the lowest-order dependence on $p _ { 1 }$ . From Section 14.4, the steady-flow pressure drop is calculated using

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 2 , 0 , 0 , \mathrm { I 6 e C } } } { d x } } & { = } & { - \displaystyle \mathrm { s i g n } ( \dot { N } _ { 2 , 0 } ) \frac { m ^ { 2 } \dot { N } _ { 2 , 0 } ^ { 2 } } { 8 \beta _ { 0 } m _ { \mathrm { r } } \lambda ^ { 2 } } [ ( 1 + \frac { 1 } { 2 \dot { \varepsilon } _ { 2 , 0 } ^ { 2 } } + \frac { | p _ { 1 } | } { \gamma \eta _ { m } } \frac { \cos \phi } { \varepsilon _ { 2 , 0 } } ) f _ { \mathrm { \mathcal { H } , m a x } }  } \\ & & { } & {  - \frac { 2 \dot { \varepsilon } _ { 2 , 0 } ^ { 2 } - 2 } { 2 \varepsilon _ { 2 , 0 } ^ { 2 } ( 1 + | \varepsilon _ { 2 , 0 } | ) } \frac { d f _ { \mathrm { \mathcal { H } } } } { d N _ { R } } N _ { R , \mathrm { H z a x } } ] , } \\ & & { = } & { - \displaystyle \frac { \rho _ { \mathrm { r } } | U _ { 1 } | ^ { 2 } } { 8 \pi r _ { 1 } A ^ { 2 } } \{ [ ( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } ) \sin ^ { - 1 } \varepsilon _ { 2 , 0 } + 3 \varepsilon _ { 2 , 0 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } }   } \\ & & { } & {   + \frac { 2 | p _ { 1 } | } { \gamma \eta _ { m } } \cos \phi ( \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } + \frac { 2 + \varepsilon _ { 2 , 0 } ^ { 2 } } { 3 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } ) ] f _ { \mathrm { \mathcal { H } , m a x } }  } \\ & & { } &   + [ \pi \tilde { \tau } _ { 2 , 0 } \frac { 3 / 2 + \varepsilon _ { 2 , 0 } ^ { 2 } } { 1 + | \varepsilon _ { 2 , 0 } | } - 3 \varepsilon _  \end{array}\tag{10.24}
$$

where $\varepsilon _ { 2 , 0 } = m \dot { N } _ { 2 , 0 } / \rho _ { m } \left| U _ { 1 } \right|$

Calculation of $T _ { m } ( x )$ $\dot { H } ,$ and $\left. T _ { 1 } \right.$

$T _ { m }$ is not affected by DUCTs.

The exiting energy flow is left as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } ~ = ~ \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ in insulated mode, described in Section 11.1.2. This essentially assumes that the side walls are thermally insulated, so the heat generated by acoustic power dissipation finds its way to a heat exchanger somewhere else. If several DUCTs (and/or CONEs) are strung together in insulated mode, the power dissipated in all of them must show up at one or two nearby heat exchangers.

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ in “anchored" mode, described in Section 11.1.2. This essentially assumes that the duct wall is thermally anchored, e.g., by a water bath, so heat generated by acoustic-power dissipation is carried away locally. Thermoacoustic heat transport in the boundary layer along the perimeter, which in fact contributes a small difference between $\dot { H } _ { 2 , k }$ and $\check { E }$ in ducts, is neglected in “anchored" mode.

The spatial average of the complex oscillating temperature amplitude is calculated using

$$
\langle T _ { 1 } \rangle = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { f _ { \kappa } } { 1 + \epsilon _ { s } } \right] .\tag{10.26}
$$

## 10.1.2 CONE

## General description:

Use CONE to find the evolution of $p _ { 1 }$ and $U _ { 1 }$ with x in tapered channels of any cross-sectional shape (e.g., square, circular) by giving suitable areas and perimeters. The perimeter is linearly interpolated between its initial and final values, and the area is quadratically interpolated between its initial and final values. Use this segment only when $T _ { m }$ is independent of x. (See STKCONE in Section 10.6.1, to allow nonzero $d T _ { m } / d x . )$ The calculation is identical to that for a DUCT if the initial and final areas are equal and the initial and final perimeters are equal. As discussed below, the laminar calculation is accurate for circular cones of any diameter, and for large cones (i.e., with $r _ { 0 } \gg \delta _ { \nu } , \delta _ { \kappa } )$ of any cross-sectional shape.

In a CoNE, DELTAEC's turbulence algorithm is controlled through optional parameter f, the relative roughness ε, whose definition for steady flow can be found in fluid-mechanics textbooks [59]: roughness height divided by pipe diameter. We have found that $\varepsilon = 0 . 0 0 0 5$ works well in high-amplitude acoustics, even if the geometrical roughness is smaller than this value. Omitting this parameter forces the oscillatory calculation to be laminar at all Reynolds numbers.

At high enough amplitudes, we believe that a steeply tapered coNE experiences separation during the half of the cycle when the flow goes from small toward large radius, just like the separation at high Reynolds number in a too-steeply-tapered diffuser. DELTAEC does not warn of this condition. To account for such separation, the user could include minor loss, described in Section 10.2.4

## Input variables:

AreaI $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { I }$ available to the gas at the initial end of the CoNE, based on inside dimensions.

PerimI (m) Perimeter $\Pi _ { I }$ of the initial inside cross section described above.

Length (m) The length $\Delta x$ of the CONE.

AreaF $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { F }$ available to the gas at the final end of the CoNE, based on inside dimensions.

PerimF (m) Perimeter $\Pi _ { F }$ of the final inside cross section described above.

Laminar/Turbulent Whenever the laminar box is checked, the calculations of $d p _ { 1 } / d x$ and $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ in the CoNE are based on noninteracting, laminar flow. The laminar condition is identified in the <.out> file as a blank line where parameter f would otherwise be.

Srough This input parameter appears if the turbulent box is checked in the Optional Parameters dialog. Srough is ε, the surface roughness inside the CoNE, relative to the diameter. This is called “relative roughness" in many fluid-mechanics books, for steady flow. However, for oscillating flow, we often regard Srough as a fitting parameter, with a typical value of $5 \times 1 0 ^ { - 4 }$ . Larger values yield higher turbulent dissipation of $\dot { E }$

Optimistic/Normal/Pessimistic These choices appear if the turbulence box is checked in the Optional Parameters dialog and if the "Enable Ndot" box is checked in the BEGIN segment. These choices control the nonlinear interaction between oscillating flow and steady flow in the CONE. “Optimistic" and "Pessimistic" refer to the two calculation schemes described in Ref. [42], and “Normal" is the average of the two. For the optimistic case, the turbulent steady and turbulent oscillating flows are assumed to be independent, simply superimposed. For the pessimistic case, the turbulent steady flow and turbulent oscillating flow are assumed to interact with each other and to increase each other's resistive effects according to the quasi-steady approximation. In the <.out> file, Optimistic/Normal/Pessimistic is recorded with SrOptm, Srough, or SrPess to indicate the name of ε.

Solid The solid material on the inside surface of the CoNE. (This is used only in the calculation of $\epsilon _ { s }$ , which is seldom significant in CONEs.)

## Potential targets:

None.

## Master-slave links:

The initial perimeter of a CoNE can be slaved to the initial area, to keep the cross-sectional shape the same when area is changed.

The final perimeter of a CoNE can be slaved to the final area to keep the cross-sectional shape the same when area is changed.

Both perimeters of a CoNE can be slaved to their respective areas to keep the cross-sectional shapes the same when either or both areas are changed.

The length and both perimeters of a CoNE can be slaved to its two areas, to keep the cross-sectional shapes of the ends and the wall taper angle constant when either or both areas are changed.

![[mu_66afccee_2a03fc775ebe982d190a.jpg]]

The length of a CoNE can be slaved to the length of another segment to keep the total length constant.

(For an introduction to master-slave links, and a complete listing of possible links for all segments, see Section 2.7.2.)

## Format and examples:

Examples of the use of CoNE appear throughout Chapters 2, 5, and 6.

Calculation of $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$ with $\dot { N } = 0$

In CONEs, $p _ { 1 }$ and $U _ { 1 }$ evolve according to

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A } U _ { 1 } , } \\ { \displaystyle \frac { d U _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i A \omega } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { \gamma - 1 } { 1 + \epsilon _ { s } } f _ { \kappa } \right) p _ { 1 } , } \end{array}\tag{10.27}
$$

which are equivalent to the Webster horn equation [61] with losses included:

$$
\left( 1 + \frac { \gamma - 1 } { 1 + \epsilon _ { s } } f _ { \kappa } \right) p _ { 1 } + \frac { a ^ { 2 } } { \omega ^ { 2 } } \frac { 1 } { A } \frac { d } { d x } \left[ \left( 1 - f _ { \nu } \right) A \frac { d p _ { 1 } } { d x } \right] = 0 .\tag{10.28}
$$

The perimeter varies linearly from its initial value to its final value, and area varies quadratically:

$$
\Pi ( x ) ~ = ~ \Pi _ { I } + \left( \Pi _ { F } - \Pi _ { I } \right) \frac { x - x _ { o } } { \Delta x } ,\tag{10.29}
$$

$$
A ( x ) = \left[ \sqrt { A _ { I } } + \left( \sqrt { A _ { F } } - \sqrt { A _ { I } } \right) \frac { x - x _ { o } } { \Delta x } \right] ^ { 2 } ,\tag{10.30}
$$

where $x _ { o }$ is the x coordinate of the initial end of the CONE. Hence, CONEs that are circular at both ends have circular cross sections everywhere in between, with diameter varying linearly with axial position

In CONEs, we define the effective radius to be $r _ { 0 } ( x ) = 2 A / \Pi$ (For circular cross sections, this is indeed the radius of the circle. For other cross sections, it is twice the hydraulic radius.) For $r _ { 0 } / \delta _ { j } < 2 5 , f _ { \kappa }$ and $f _ { \nu }$ are calculated using complex Bessel functions:

$$
f _ { j } = \frac { 2 J _ { 1 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } { ( i - 1 ) ( r _ { 0 } / \delta _ { j } ) J _ { 0 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } \mathrm { ~ f o r ~ } j = \kappa \mathrm { ~ o r ~ } \nu .\tag{10.31}
$$

Where $r _ { 0 } / \delta _ { j } > 3 0$ , the boundary-layer approximation is used:

$$
f _ { j } = { \big ( } 1 - i { \big ) } \delta _ { j } / r _ { 0 } .\tag{10.32}
$$

For intermediate values, linear interpolation is used to make a smooth match between the two regimes. While the narrow solution assumes a circular cross section, the cross-sectional shape of the cone is irrelevant in the boundary-layer approximation.

In CoNE, the effects of turbulence are calculated exactly the same as given above for DUCT.

In all cases, boundary-layer approximation is used for the effect of the solid:

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } .\tag{10.33}
$$

Calculation of $p _ { 1 } ( x ) , U _ { 1 } ( x )$ , and $p _ { 2 , 0 , \mathbf { D E C } } ( x )$ with $\dot { N } \neq 0$

In CoNE, these calculations are exactly the same as given above for DUCT, except that A and $r _ { 0 }$ are functions of x in the equations for CONE.

## Calculation of $T _ { m } , { \dot { H } } .$ and $\left. T _ { 1 } \right.$

$T _ { m }$ is not affected by CONE. (But see also STKCONE in Section 10.6.1, which allows nonzero $d T _ { m } / d x . )$

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ in insulated mode, described in Section 11.1.2. This essentially assumes that the side walls are thermally insulated, so the heat generated by acoustic power dissipation is deposited in an adjacent heat exchanger. If several CoNEs (and/or DUCTs) are strung together in insulated mode, the power dissipated in all of them should show up in a nearby heat exchanger.

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ in anchored mode, described in Section 11.1.2. This mode essentially assumes that the cone wall is thermally anchored, e.g., by a water bath, so heat generated by acoustic-power dissipation is carried away externally. Thermoacoustic heat transport along the perimeter, which in fact contributes a small difference between $\dot { H } _ { 2 , k }$ and $\dot { E }$ in CONEs, is neglected.

The spatial average of the complex oscillating temperature amplitude is calculated using

$$
\langle T _ { 1 } \rangle = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { f _ { \kappa } } { 1 + \epsilon _ { s } } \right] .\tag{10.34}
$$

## 10.2 Lumped elements

## 10.2.1 COMPLIANCE

## General description:

A CoMPLIANCE is a lumped acoustic volume element, with adiabatic volumetric compressibility and surface thermal-hysteresis dissipation.

## Input variables:

Area $( \mathrm { m } ^ { 2 } )$ The surface area S inside the COMPLIANCE.

Volume (m³) The volume V inside the COMPLIANCE.

Solid The solid material on the inside surface of the COMPLIANCE. (This is used only in the calculation of $\epsilon _ { s }$ , which seldom differs significantly from its value for a solid with infinite conductivity and specific heat in COMPLIANCEs.)

## Potential targets:

None.

## Master-slave links:

The surface area of a compliance can be slaved to its volume, so the shape remains the same when the volume is changed.

(For an introduction to master-slave links, and a complete listing of link options for all segments, see Section 2.7.2.)

Format and examples:

COMPLIANCE this one is a sphere, R = 0.01 m   
0.1257 m2 Area   
4.189e-3 m3 Volume   
nickel solid

![[mu_66afccee_df79794a18dcfa111c5c.jpg]]

Other examples of COMPLIANCE can be found in Sections 5.2 and 5.8.2.

## Calculations:

Pressure amplitude and mean temperature are unchanged by COMPLIANCE. Volume flow changes according to

$$
U _ { \mathrm { 1 , o u t } } = U _ { \mathrm { 1 , i n } } + - i \frac { \omega p _ { 1 } } { \rho _ { m } a ^ { 2 } } \left[ V + ( 1 - i ) \frac { \gamma - 1 } { 1 + \epsilon _ { s } } S \frac { \delta _ { \kappa } } { 2 } \right] ,\tag{10.35}
$$

with the thermal-hysteresis contribution of the solid calculated in boundary-layer approximation:

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } .\tag{10.36}
$$

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ in insulated mode. This essentially assumes that the component is thermally insulated, so the heat generated by acoustic power dissipation must somehow be deposited elsewhere, either upstream or downstream, such as in an adjacent heat exchanger (or flowing out through a BEGIN or \*\*END segment).

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E }$ in anchored mode. This is intended to model a component that is thermally anchored, e.g., by a water bath, so heat generated by acoustic power dissipation is carried away locally.

The spatial average of the complex oscillating temperature amplitude is calculated using

$$
\langle T _ { 1 } \rangle = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { 1 - i } { 2 \left( 1 + \epsilon _ { s } \right) } \frac { S \delta _ { \kappa } } { V } \right] .\tag{10.37}
$$

COMPLIANCE behaves the same whether $\dot { N } = 0$ or not. Since $T _ { m }$ is unchanged in COMPLIANCE. $\dot { H } _ { \dot { N } , \mathrm { o u t } } = \dot { H } _ { \dot { N } , \mathrm { i n } }$

## 10.2.2 SURFACE

## General description:

A SuRFACE is a surface area with thermal-hysteresis dissipation. It always absorbs acoustic power. It has no volume of its own. It is often used at the end of a DUCT, before a HARDEND. (See Fig. 10.1 for two other typical uses for SURFACE.)

## Input variables:

Area $( \mathrm { m } ^ { 2 } )$ The surface area $S$ exposed to oscillating pressure in the SURFACE segment, not accounted for in other segments nearby.

Solid The solid material on the exposed surface. (This is used only in the calculation of $\epsilon _ { s }$ which seldom differs significantly from its value for a solid with infinite conductivity and specific heat on SURFACEs.)

## Potential targets; Master-slave links:

None.

Format and examples:

SURFACEa surface with thermal hysteresis dissipation   
1.134e-3 m2 Area   
ideal solid

Examples of SURFACE also occur throughout Chapter 2 and Sections 5.2 and 5.5.

## Calculations:

A SURFACE does not affect mean temperature or pressure amplitude. Volume flow changes according to

$$
U _ { \mathrm { 1 , o u t } } = U _ { \mathrm { 1 , i n } } - ( 1 + i ) \frac { \omega p _ { 1 } } { \rho _ { m } a ^ { 2 } } \frac { \gamma - 1 } { 1 + \epsilon _ { s } } S \frac { \delta _ { \kappa } } { 2 } .\tag{10.38}
$$

(This is the same calculation as would occur in a COMPLIANCE with zero volume.) The influence of the solid on thermal hysteresis is calculated in boundary-layer approximation:

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } .\tag{10.39}
$$

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ in insulated mode. This essentially assumes that the component is thermally insulated, so the heat generated by acoustic power dissipation must somehow be deposited elsewhere, either upstream or downstream, such as in an adjacent heat exchanger (or flow out through a BEGIN or \*\*END segment).

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ in anchored mode. Thus, in a series of such anchored segments, heat generated by acoustic power dissipation is carried away locally.

The spatial average of the complex oscillating temperature amplitude is calculated using $\langle T _ { 1 } \rangle = T _ { m } \beta p _ { 1 } / \rho _ { m } c _ { p }$

SURFACE behaves the same whether $\dot { N } = 0$ or not. Since $T _ { m }$ is unchanged in SURFACE, $\dot { H } _ { \dot { N } , \mathrm { o u t } } = \dot { H } _ { \dot { N } , \mathrm { i n } }$

## 10.2.3 IMPEDANCE

## General description:

An IMPEDANCE is a lumped series complex impedance.

## Input variables:

Re(Z) (Pa·s/m3) The real part of the series acoustic impedance Z. If the impedance has resistance, this number is positive

Im(Z) (Pa·s/m3) The imaginary part of the series acoustic impedance Z. If the impedance has inertance L, this number is equal to ωL.

## Potential targets:

None.

## Master-slave links:

In an IMPEDANCE, Im[Z] can be slaved to Re[Z] so [Z| remains constant when Re[Z] is changed. Note, however, that this becomes impossible if Re[Z] is changed to a value that is too large.

Alternatively, Im[Z] can be slaved to Re[Z] so phase(Z) remains constant when Re[Z] is changed.

(For an introduction to master-slave links and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

IMPEDANCE just a lumped series impedance, i.e., resistance plus inertance   
1.0 Pa-s/m3 Re(Z)   
0.2 Pa-s/m3 Im(Z)

Linked to one or more RPN calculations, IMPEDANCE gives the user the freedom to create nonlinear impedances. The following example shows an impedance with its resistance proportional to the square of the flow and its inertance proportional to the flow:

--2   
RPN real part of impedance   
12.0   
U1 mag sqrd inp \*   
!--- --3   
RPN imaginary part of impedance   
3.0E-4   
U1 mag inp \*   
!-- -4   
IMPEDANCE   
sameas 2A   
sameas 3A

Another example of IMPEDANCE, in the context of the orifice of a pulse-tube refrigerator, is in Section 5.8.3.

## Calculations:

At an IMPEDANCE, volume flow rate and mean temperature are unchanged. Pressure changes according to

$$
p _ { 1 , \mathrm { o u t } } = p _ { 1 , \mathrm { i n } } - Z U _ { 1 } .\tag{10.40}
$$

The spatial average of the complex oscillating temperature amplitude is calculated using $\langle T _ { 1 } \rangle = T _ { m } \beta p _ { 1 , j } / \rho _ { m } c _ { p }$ , where $j$ is either “out" or “in."

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ in insulated mode, described in Section 11.1.2. This assumes that the component is thermally insulated, so the heat generated by acoustic power dissipation must somehow be deposited elsewhere, either upstream or downstream, such as in a nearby heat exchanger (or flow out through a BEGIN or \*\*END segment).

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ for anchored mode, described in Section 11.1.2. This essentially assumes that the component is thermally anchored, such as by a water bath, so heat generated by acoustic power dissipation is carried away locally.

If $\dot { N } \neq 0$ in IMPEDANCE, the steady flow and the oscillating flow are assumed to be independent, simply superimposed, as if the flows are laminar. Thus, the difference in $p _ { 1 }$ across an IMPEDANCE is unaffected by the presence of the steady flow, and the change in $p _ { \mathrm { 2 , 0 , D E C } }$ is given by

$$
\begin{array} { r } { p _ { 2 , 0 , \mathrm { D E C } , \mathrm { o u t } } - p _ { 2 , 0 , \mathrm { D E C } , \mathrm { i n } } = \mathrm { R e } [ Z ] \dot { N } _ { 2 , 0 } m / \rho _ { m } . } \end{array}\tag{10.41}
$$

Since an IMPEDANCE has no defined area, $p _ { \mathrm { 2 , 0 , t r a d } }$ is calculated based on the area of the most recent upstream segment having area.

## 10.2.4 MINOR

## General description:

Segment type MInOR accounts conveniently for minor-loss effects. The basic equation for a minor loss for steady flow [59, 53] is simply

$$
\Delta p = - \frac { 1 } { 2 } K \rho \boldsymbol { u } ^ { 2 } ,\tag{10.42}
$$

where K is the minor-loss coefficient and u is the velocity. DELTAEC's treatment of minor loss in MINOR is based on this equation.

Equations (10.43)-(10.50) were derived using the quasi-steady approximation, in which it is assumed that Eq. (10.42) is obeyed at each instant of time as u varies in time, with K independent of time except for its dependence on the direction of flow. This approximation is very good when $| \xi _ { 1 } | \gg r _ { h }$ . For $| \xi _ { 1 } | \sim r _ { h }$ or $| \xi _ { 1 } | \ll r _ { h }$ , actual pressure drops may differ significantly from values calculated in MINOR.

Since DELTAEC uses $U _ { 1 }$ to characterize flow, MINOR has an area for converting $U _ { 1 }$ to velocity. Because DELTAEC treats oscillating flow, MINOR has two inputs for Ks: $K _ { + }$ for the minor-loss coefficient in the +x direction, and K\_ for the minor-loss coefficient in the -x direction. The coefficient in the $\dot { N } = 0$ equations below differs from the $1 / 2$ in Eq. (10.42) because of the sinusoidal time dependence of the velocity.

As shown in the second example below, the gas diodes in Ref. [42] can be modeled as a MINOR and a CONE in series.

We often obtain $K _ { + }$ and $K _ { - }$ from Ref. [53], even though that reference is for steady flow. This approximation should be fairly accurate when the Reynolds number is large and $\left| \xi _ { 1 } \right|$ is much greater than any dimensions of the component.

## Input variables:

Area $( \mathrm { m } ^ { 2 } )$ The area A used in the equations below. This is the area on which the minorloss coefficients are based. Conventionally, this is usually the smallest area for areachanging geometries such as diffusers, but it is sometimes the nominal pipe area for valves and fittings.

K+ Minor-loss coefficient $K _ { + }$ for flow in the positive-x direction

K- Minor-loss coefficient K\_ for flow in the negative-x direction.

## Potential targets:

None.

Master-slave links:

None. (Use sameas if you want to keep $K _ { + }$ and K\_ equal to each other.)

## Format and examples:

This is an example of a small orifice plate mounted in a pipe, as illustrated in Fig. 10.1(a):

9   
DUCT Pre-orifice pipe   
1.8000E-02 a Area m^2 S= -2 2.2139E+04 A Ipl Pa   
0.4756 b Perim m Fn( 9a) -141.30 B Ph(p) deg   
0.1500 c Length m 2.3148E-02 C |U| m^3/s   
128.66 D Ph(U) deg   
4.1756E-09 E Htot W   
ideal Solid type -0.1923 F Edot W   
!– 10   
RPN calculate area difference (m2)   
0.0000 a G or T (t) 1.6000E-02 A ChngeMe   
9a 12a -   
11   
SURFACE surface area on top of orifice plate   
sameas 10A a Area m^2 2.2139E+04 A Ipl Pa

![[mu_66afccee_23c66016b72ea0f8a287.jpg]]  
Figure 10.1: Examples of the use of MINOR. (a) Orifice plate in a channel. (b) Conical gas diode.

-141.30 B Ph(p) deg   
2.3148E-02 C |U| m^3/s   
128.65 D Ph(U) deg   
4.1756E-09 E Htot W   
ideal Solid type -0.2320 F Edot W   
12   
MINOR minor loss in orifice plate   
2.0000E-03 a Area m^2 2.2140E+04 A Ipl Pa   
1.0000 b K+ -140.59 B Ph(p) deg   
1.0000 C K- 2.3148E-02 C |U| m^3/s   
128.65 D Ph(U) deg   
4.1756E-09 E Htot W   
-3.3973 F Edot W   
13   
SURFACE surface area on bottom of orifice plate   
sameas 11a a Area m^2 2.2140E+04 A Ipl Pa   
-140.59 B Ph(p) deg   
2.3148E-02 C |U| m^3/s   
128.64 D Ph(U) deg   
4.1756E-09 E Htot W   
ideal Solid type -3.4370 F Edot W   
14   
DUCT Post-orifice pipe   
sameas 9a a Area m^2 1.9565E+04 A Ipl Pa   
sameas 9b b Perim m -140.52 B Ph(p) deg   
sameas 9c c Length m 4.4525E-02 C |U| m^3/s   
129.01 D Ph(U) deg   
4.1756E-09 E Htot W   
ideal Solid type -3.6358 F Edot W

This is an example of a conical gas diode, such as is described in Ref. [42] and illustrated in Fig. 10.1(b).

```csv
4
DUCT quarter-wave duct from engine to diode
7.0000E-04 a Area m^2 S= -2 7705.2 AIpl Pa
9.3748E-02 b Perim m Fn( 4a) -161.41 B Ph(p) deg
4.6000 c Length m 5.4080E-02 C |U| m^3/s
9.0500E-02 d Srough -87.804 D Ph(U) deg
354.15 E Htot W
ideal Solid type 58.812 F Edot W
5
RPN surface area of adapter plate
0.0000 a G or T (t) 3.0000E-04 A ChngeMe
4a 8a -
6
SURFACE surface area of adapter plate
sameas 5A a Area m^2 7705.2 AIpl Pa
-161.41 B Ph(p) deg
5.4080E-02 C |U| m^3/s
-87.804 D Ph(U) deg
354.15 E Htot W
ideal Solid type 58.812 F Edot W
1 - 7
RPN calculate Borda-Carnot minor loss here
0.0000 a G or T (t) 0.1837 A ChngeMe
1 8a 4a / - sqrd
8
MINOR asymmetric flow at gas diode
4.0000E-04 a Area m^2 7402.7 AIpl Pa
5.0000E-02 b K+ -174.70 B Ph(p) deg
```

sameas 7AC K- 5.4080E-02 C |U| m^3/s   
-87.804 D Ph(U) deg   
354.15 E Htot W   
10.829 F Edot W   
9   
CONE expansion to plenum   
sameas 8a a AreaI m^2 S= -9 1.7471E+04 A Ipl Pa   
7.0899E-02 b PerimI m Fn( 9b) -177.49 B Ph(p) deg   
0.4000 c Length m 4.9949E-02 C |U| m^3/s   
1.5000E-02 d AreaF m^2 S= -9 -87.809 D Ph(U) deg   
0.4342 e PerimF m Fn( 9d) 354.15 E Htot W   
5.0000E-04 f Srough 2.4219 F Edot W   
ideal Solid type

Other examples of MINOR are found in Sections 6.3 and 6.4.

Pressure calculations for $\dot { N } = 0$

In the $\dot { N }  0$ limit, changes in $p _ { 1 }$ across segment type MINOR are given by

$$
p _ { \mathrm { 1 , o u t } } - p _ { \mathrm { 1 , i n } } = - \left( K _ { - } + K _ { + } \right) \frac { 2 \rho _ { m } \left| U _ { 1 } \right| } { 3 \pi A ^ { 2 } } U _ { 1 } ,\tag{10.43}
$$

and changes in p20DEC are given by

$$
p _ { 2 , \mathrm { { 0 , D E C , o u t } } } - p _ { 2 , \mathrm { { 0 , D E C , i n } } } = \left( K _ { - } - K _ { + } \right) { \frac { \rho _ { m } \left| U _ { 1 } \right| ^ { 2 } } { 8 A ^ { 2 } } } .\tag{10.44}
$$

Pressure calculations for $\dot { N } \neq 0$

For $\dot { N } \neq 0$ , changes in $p _ { 1 }$ across segment type MINOR are given by

$$
\begin{array} { r c l } { p _ { 1 , \mathrm { o u t } } - p _ { 1 , \mathrm { i n } } } & { = } & { \varepsilon K _ { - } \displaystyle \frac { \rho _ { m } | U _ { 1 } | } { A ^ { 2 } } U _ { 1 } \mathrm { ~ f o r ~ } \varepsilon \leq - 1 , } \\ & { = } & { \displaystyle - \left[ \left( 1 + \frac { \varepsilon ^ { 2 } } { 2 } \right) \sqrt { 1 - \varepsilon ^ { 2 } } + \frac { 3 } { 2 } \varepsilon \sin ^ { - 1 } \varepsilon - \frac { K _ { - } - K _ { + } } { K _ { - } + K _ { + } } \frac { 3 \pi \varepsilon } { 4 } \right] ( K _ { - } + K _ { + } ) } \\ & & { \displaystyle \times \frac { 2 \rho _ { m } | U _ { 1 } | } { 3 \pi A ^ { 2 } } U _ { 1 } \mathrm { ~ f o r ~ } | \varepsilon | \leq 1 , } \\ & { = } & { \displaystyle - \varepsilon K _ { + } \frac { \rho _ { m } | U _ { 1 } | } { A ^ { 2 } } U _ { 1 } \mathrm { ~ f o r ~ } \varepsilon \geq 1 , } \end{array}\tag{0.45}
$$

0.46)

0.47)

where $\varepsilon = m \dot { N } / \rho _ { m } | U _ { 1 } |$ . Changes in p20DEC are given by

$$
\begin{array} { r l } { p _ { 2 , \mathrm { O D E C , c o u r - } } - p _ { 2 , \mathrm { O D E C ; i n } } } & { = K - \frac { m ^ { 2 } \hat { \mathcal { X } } _ { 2 , \mathrm { O } } ^ { 2 } } { 2 p _ { \mathrm { o D } } A ^ { 2 } } \left( 1 + \frac { 1 } { 2 \varepsilon _ { \mathrm { g } , \mathrm { O } } ^ { 2 } } + \frac { | p _ { 1 } | } { \gamma p _ { \mathrm { o p } } } \frac { \cos \phi } { \varepsilon _ { \mathrm { g } , \mathrm { O } } } \right) \mathrm { ~ f o r ~ } \varepsilon _ { 2 , \mathrm { O } } \leq - 1 , \quad \mathrm { ( I t ) } } \\ & { = \ \frac { \rho _ { m } | \mathcal { X } _ { 1 } | ^ { 2 } } { 8 A ^ { 2 } } \bigg \{ ( K - K _ { + } ) \left( 1 + 2 \varepsilon _ { 2 , \mathrm { O } } ^ { 2 } + 2 \varepsilon _ { 2 , \mathrm { O } } \frac { | p _ { 1 } | } { \gamma p _ { \mathrm { m e } } } \cos \phi \right) } \\ & { \quad - \left( K _ { + } + K _ { - } \right) \frac { 2 } { \pi } \left[ \left( 1 + 2 \varepsilon _ { 2 , \mathrm { O } } ^ { 2 } + 2 \varepsilon _ { 2 , \mathrm { o p } } \frac { | p _ { 1 } | } { \gamma p _ { \mathrm { m e } } } \cos \phi \right) \sin ^ { - 1 } \varepsilon _ { 2 , \mathrm { O } } \right. } \\ & { \quad \left. + \left( 3 \varepsilon _ { 2 , \mathrm { O } } + \frac { 4 } { 3 } \left[ 1 + \varepsilon _ { 2 , \mathrm { O } } ^ { 2 } / 2 \right] \frac { | p _ { 1 } | } { \gamma p _ { \mathrm { m e } } } \cos \phi \right) \sqrt { 1 - \varepsilon _ { 2 , \mathrm { O } } ^ { 2 } } \right] \bigg \} } \\ &  = \ - K \frac { m ^ { 2 } \hat { \mathcal { X } } _ { 2 , \mathrm { O } } ^ { 2 } } { 2 \rho _ { \mathrm { o m } } A ^ { 2 } } \bigg ( 1 + \frac { 1 }  2 \varepsilon _  \end{array}\tag{.48}
$$

.49)

.50)

![[mu_66afccee_9ef0b40a53b14c9d3152.jpg]]  
Figure 10.2: Enclosed \*EDUCER or \*ESPEAKER.

where $\varepsilon _ { 2 , 0 } = m \dot { N } _ { 2 , 0 } / \rho _ { m } | U _ { 1 } |$ and $\phi$ is the phase angle between $p _ { 1 }$ and $U _ { 1 }$ . Derivations of these equations neglecting the terms in $p _ { 1 }$ are given in Ref. [42]; and derivations including the $p _ { 1 }$ terms appear in Section 14.4.

## Other calculations

Segment MINOR leaves $T _ { m }$ and $U _ { 1 }$ unchanged.

The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ in insulated mode, described in Section 11.1.2. This assumes that the component is thermally insulated, so the heat generated by acoustic power dissipation must somehow be deposited elsewhere, either upstream or downstream, such as in a nearby heat exchanger (or can flow out through a BEGIN or \*\*END segment). The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ for anchored mode, described in Section 11.1.2. This essentially assumes that the component is thermally anchored, such as by a water bath, so heat generated by acoustic power dissipation is carried away locally.

The spatial average of the complex oscillating temperature amplitude is calculated using $\langle T _ { 1 } \rangle = T _ { m } \beta p _ { 1 , j } / \rho _ { m } c _ { p }$ , where $j$ is either “out" or “in."

## 10.3 Series transducers

## 10.3.1 VESPEAKER, IESPEAKER, VEDUCER, and IEDUCER

## General description:

The \*EDUCERs and \*ESPEAKERs are electroacoustic transducers with both ends “Enclosed" in the DELTAEC model, so they are in series between the previous segment and the subsequent segment.

\*ESPEAKERs let the user specify mass, spring constant, force constant, resistance, and inductance, so frequency-dependent (even resonant) electrodynamic transducers (e.g., linear motors and linear alternators, as well as loudspeakers) can be modeled easily. These \*ESPEAKER segments can be used to model moving-magnet transducers as well as moving-coil transducers; in the former case, set the Bl product equal to the moving-magnet transducer's force constant, expressed in newtons per amp.

\*EDUCERs have specified transduction coefficients, which can be linked to the results of RPN calculations upstream to create the frequency or amplitude dependences of piezoelectric or any other type of transducer.

With IEDUCER and IESPEAKER, the user specifies the complex current, and each pass of DELTAEC calculates the complex voltage; with VEDUCER and VESPEAKER, the user specifies complex voltage, and DELTAEC computes complex current. VEDUCER and VESPEAKER cannot be used with zero electrical impedance because this would lead to a division by zero (see below). Hence, use IEDUCER or IESPEAKER for "electrically ideal" transducers.

\*ESPEAKERs incorporate thermal-hysteresis losses on their upstream and downstream areas, as if they included two SURFACEs of equal areas but generally different pressure amplitudes. The \*EDuCER segments, which have no area parameter, have no built-in thermalhysteresis losses, so use SURFACEs upstream and downstream if needed.

See also Section 14.5 for a discussion of the saturation of magnetic flux in \*ESPEAKERs.

See also the side-branch transducers described in Section 10.4.2 below, which have their backsides hanging outside the DELTAEC model.

## Input variables, VESPEAKER and IESPEAKER:

Area $( \mathrm { m } ^ { 2 } )$ The surface area A of the moving part of the \*ESPEAKER. An area A is exposed to oscillating pressures on both the back side and the front side. The velocity of the moving element is $U _ { 1 } / A$

R (ohm) The electrical resistance $R _ { e }$ of the coil.

L (henry) The electrical inductance L of the coil when it is prevented from moving.

BLProd (tesla·m, which is equivalent to N/amp) For a traditional moving-coil loudspeaker the product of the magnetic field B and the wire length l that is immersed in B. More generally, the force in newtons exerted when one amp of current is applied and nothing is allowed to move.

M (kg) The moving mass M of the transducer.

K (N/m) The spring constant K of the transducer. This should include zero-current magnetic forces (present in moving-magnet, stationary-iron transducers) and forces from mechanical springs, but not the gas-pressure forces on the front and back of area A.

Rm (N·s/m) The mechanical resistance $R _ { m }$ of the transducer.

|V| or [I| (volts or amps) In VESPEAKER, the amplitude of the oscillating voltage, $| V _ { 1 } |$ . In IESPEAKER, the amplitude of the oscillating current, $\left| I _ { 1 } \right|$

ph(V) or ph(I) (degrees) In VESPEAKER, the phase of the oscillating voltage $V _ { 1 }$ . Similarly, in IESPEAKER, the phase of the oscillating current $I _ { 1 }$

Solid The solid material on the leading and trailing surfaces A. (This is used only in the calculation of $\epsilon _ { s } ,$ which seldom differs significantly from its value for a solid with infinite conductivity and infinite specific heat in \*SPEAKERs.)

Input variables, VEDUCER and IEDUCER:

Re(Ze) (ohm) The real part of the transducer's electrical impedance $Z _ { e }$ when it is prevented from moving.

Im(Ze) (ohm) The imaginary part of the transducer's electrical impedance $Z _ { e }$ when it is prevented from moving.

Re(T1) $\mathrm { ( V { \cdot } s / m ^ { 3 } ) }$ The real part of the complex transduction coefficient $\tau$ in the equations below.

Im(T1) $\mathrm { ( V { \cdot } s / m ^ { 3 } ) }$ The imaginary part of the complex transduction coefficient $\tau$ in the equations below.

Re(T2) $\mathrm { ( P a / A ) }$ The real part of the complex transduction coefficient $\tau ^ { \prime }$ in the equations below.

Im(T2) $\mathrm { ( P a / A ) }$ The imaginary part of the complex transduction coefficient $\tau ^ { \prime }$ in the equations below.

Re(Z) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The real part of the acoustic impedance Z of the transducer.

Im(Z) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The imaginary part of the acoustic impedance $Z$ of the transducer.

|V| or $| \mathbf { I } |$ (volts or amps) In VEDUCER, the amplitude of the oscillating voltage $V _ { 1 }$ . In IEDUCER, the amplitude of the oscillating current $I _ { 1 }$

ph(V) or ph(I) (degrees) In VEDUCER, the phase of the oscillating voltage $V _ { 1 }$ . In IEDUCER, the phase of the oscillating current $I _ { 1 }$

## Potential targets:

None.

## Master-slave links:

None. The use of sameas is sometimes convenient in \*EDUCERs, to keep $\tau ^ { \prime } = \tau$

## Format and examples:

```csv
VEDUCER Enclosed driver
1.000E-09 a Re(Ze) ohms
.000 b Im(Ze) ohms
1.000E+04 c Re(T1) V-s/m^3
.000 d Im(T1) V-s/m^3
-1.000E+04 e Re(T2) Pa/A
.000 f Im(T2) Pa/A
1.000E-09 g Re(Z) Pa-s/m^3
1.000E-09 h Im(Z) Pa-s/m^3
10.0 i Vin V
45.0 j Ph(Vin) deg
```

![[mu_66afccee_cf9118a20009b75f52fd.jpg]]

IEDUCER: same as VEDUCER, except that current appears in lines i and j instead of voltage.

```csv
VESPEAKER
6.000E-04 a Area m^2
6.00 b R ohms
.000 CL H
8.00 d BLProd T-m
5.000E-03 e M kg
1.000E+04 f K N/m
.000 g Rm N-s/m
62.0 h Vin V
-37.2 i Ph(Vin) deg
kapton Solid type
```

IESPEAKER: same as VESPEAKER, except that current appears in line h and i instead of voltage.

Other examples of series \*ESPEAKERs are in Sections 5.2 and 5.8.2.

## Calculations:

An Enclosed transducer IEDUCER, VEDUCER, IESPEAKER, VESPEAKER is an object attached in series with other segments, as shown in Fig. 10.2. Volume flow rate $U _ { 1 }$ is nearly unchanged (except for surface thermal-hysteresis losses—see below), but pressure is changed by the force exerted by the transducer, obeying the complex canonical equations

$$
\begin{array} { r } { V _ { 1 } } & { = ~ Z _ { e } I _ { 1 } - \tau U _ { 1 } , } \end{array}\tag{10.51}
$$

$$
\begin{array} { r l r } { p _ { 1 , \mathrm { o u t } } - p _ { 1 , \mathrm { i n } } } & { { } = } & { \tau ^ { \prime } I _ { 1 } - Z U _ { 1 } . } \end{array}\tag{10.52}
$$

• If current $I _ { 1 }$ is specified, then use IESPEAKER or IEDUCER, and find $p _ { 1 , \mathrm { o u t } } = p _ { 1 , \mathrm { i n } } +$ $\tau ^ { \prime } I _ { 1 } - Z U _ { 1 }$ and $V _ { 1 } = Z _ { e } I _ { 1 } - \tau U _ { 1 }$

• If voltage $V _ { 1 }$ is specified, then use VESPEAKER or VEDUCER, and find $I _ { 1 } = ( V _ { 1 } + \tau U _ { 1 } ) / Z _ { e }$ and $p _ { 1 , \mathrm { o u t } } = p _ { 1 , \mathrm { i n } } + \tau ^ { \prime } I _ { 1 } - Z U _ { 1 }$

• If a fixed electrical load impedance $Z _ { \mathrm { e x t } }$ is attached to the transducer, it can be modeled using an IMPEDANCE segment instead of a \*ESPEAKER or \*EDUCER segment, with $Z _ { \mathrm { i m p } } =$ $Z - \tau \tau ^ { \prime } / ( Z _ { e } + Z _ { \mathrm { e x t } } )$ ; or use one of these Enclosed transducer segments with one or more RPN targets to maintain the impedance, as shown in the example in Section 4.7.

For \*EDUCERs, the complex electrical impedance $Z _ { e } = \mathrm { R e } [ Z _ { e } ] + i \mathrm { I m } [ Z _ { e } ]$ and the complex acoustic impedance $Z = \mathrm { R e } [ Z ] + i \mathrm { I m } [ Z ]$ are given explicitly by the user.

In the case of \*ESPEAKERs, $Z _ { e } = R _ { e } + i \omega L \ ; \ \tau = - \tau ^ { \prime } = B l / A \ ; \ Z = R _ { m } / A ^ { 2 } + i ( \omega M -$ $K / \omega ) / A ^ { 2 }$ Thermal surface losses are computed for area A using the same approach as for a SURFACE, but Enclosed speakers have area A exposed to $p _ { 1 , \mathrm { i n } }$ and area A exposed to $p _ { \mathrm { 1 , o u t } }$ , because typically both sides of the speaker experience oscillatory pressure. This thermal hysteresis on those two surfaces manifests itself as a small change in volume flow rate, according to

$$
U _ { \mathrm { 1 , o u t } } = U _ { \mathrm { 1 , i n } } - ( 1 + i ) \frac { \omega } { \rho _ { m } a ^ { 2 } } \frac { \gamma - 1 } { 1 + \epsilon _ { s } } \frac { \delta _ { \kappa } } { 2 } A \left( p _ { \mathrm { 1 , i n } } + p _ { \mathrm { 1 , o u t } } \right) ,\tag{10.53}
$$

and $U _ { 1 }$ in Eqs. (10.51) and (10.52) is actually the value after the first thermal-hysteresis loss:

$$
U _ { 1 } = U _ { \mathrm { 1 , i n } } - ( 1 + i ) \frac { \omega } { \rho _ { m } a ^ { 2 } } \frac { \gamma - 1 } { 1 + \epsilon _ { s } } \frac { \delta _ { \kappa } } { 2 } A p _ { 1 , \mathrm { i n } } .\tag{10.54}
$$

The Px outputs for these segments give the complex pressure difference across the transducer.

None of these segments affects $T _ { m }$

The exiting energy flow is computed as $\dot { H } _ { 2 , k , \mathrm { o u t } } = \dot { H } _ { 2 , k , \mathrm { i n } } + \dot { W } _ { \mathrm { e l e c } }$ in insulated mode, described in Section 11.1.2. This assumes that the component is thermally insulated, so the electrical energy added at the transducer must flow out of the segment, either upstream or downstream. The exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ for thermally anchored mode, described in Section 11.1.2.

The spatial average of the complex oscillating temperature amplitude is calculated using $\langle T _ { 1 } \rangle = T _ { m } \beta p _ { 1 , j } / \rho _ { m } c _ { p } .$ where $j$ is either “out" or $^ { 6 \mathfrak { c } } _ { \mathrm { l n } }$

The WorkIn output variable displays the electrical power $\mathrm { R e } [ V _ { 1 } \tilde { I _ { 1 } } ] / 2$ that must be supplied to the transducer. If negative, this is electrical power produced by the transducer.

The Ph(V/I) variable is especially useful for constructing a target related to the electrical load impedance attached to a \*SPEAKER that is used as an alternator; for example, Ph $( \mathrm { V } / \mathrm { I } ) = 1 8 0 ^ { \circ }$ means that the load impedance is purely resistive. See Fig. 4.1a for a more complicated example with both resistance and capacitance.

It is hard for us to anticipate what a user might intend if nonzero $\dot { N }$ were to flow through a series transducer, so these segments behave the same whether $\dot { N } = 0$ or not.

## 10.4 Side-branch transducers and side-branch impedance

## 10.4.1 BRANCH, OPNBRANCH, and PISTBRANCH

## General description:

BRANCH, OPNBRANCH, and PISTBRANCH are side branches with specified impedances. With BRANCH, the user specifies the real and imaginary parts of the impedance, assumed independent of frequency (unless linked by sameas to results of frequency-dependent RPN calculations). OPNBRANCH and PISTBRANCH incorporate the frequency dependence of radiation impedances. PISTBRANCH approximates the radiation impedance of a flanged piston of the given radius, while radiation impedance at an opening radiating into $4 \pi$ solid angle can be modeled as an OPNBRANCH. Long ago, OPNBRANCH was added to DELTAE before RPN segments were available. Today, we find OPNBRANCH very awkward; it seems much easier to model the end of an open tube radiating into 4π solid angle with RPN calculations and a SOFTEND segment. An example is shown in Section 11.1.3.

(If a side branch has nonzero $\dot { N }$ flowing past it, the user might consider what fraction of the energy added by the transducer goes into raising the temperature of the steady flow passing by and what fraction is added to the thermoacoustic wave. In a VX\* heat-exchanger segment, $F _ { \dot { Q } \dot { N } }$ , (FracQN) determines these fractions. With a side-branch transducer, an RPN segment can be used, with user-specified assignment of these fractions using =Tm and =H2k.)

Input variables, BRANCH:

Re(Z) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The real part of the branch impedance $Z _ { \mathrm { b r } }$

![[mu_66afccee_c1116480241c880cd237.jpg]]  
Figure 10.3: BRANCH, OPNBRANCH, or PISTBRANCH.

Im(Z) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The imaginary part of the branch impedance $Z _ { \mathrm { b r } }$

HtotBr (W) How much power $\dot { H }$ flows out of the trunk into the branch.

## Input variables, OPNBRANCH:

Re(Z)/k^2 (Pa·s/m) The real part of the branch impedance $Z _ { \mathrm { b r } }$ , divided by the square of the wave number $k = \omega / a$

Im(Z)/k (Pa·s/m2) The imaginary part of the branch impedance $Z _ { \mathrm { b r } }$ , divided by the wave number $k = \omega / a .$

HtotBr (W) How much power $\dot { H } _ { \mathrm { t o t } }$ flows out of the trunk into the branch

## Input variables, PISTBRANCH:

Radius (m) The radius r of the circular, flanged radiating surface.

## Potential targets:

None.

## Master-slave links:

The imaginary part of a BRANCH impedance can be slaved to the real part, to hold the magnitude constant or to hold the phase constant when the real part is changed.

No master-slave options are available for OPNBRANCH and PISTBRANCH.

(For an introduction to master-slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

![[mu_66afccee_553f454d376e94a6498f.jpg]]

![[mu_66afccee_44f8ba6e0988ba406bfa.jpg]]  
Figure 10.4: The side-branched transducers: IDUCER, ISPEAKER, VDUCER, or VSPEAKER.

## Calculations:

A BRANCH is a side branch with complex impedance $Z _ { \mathrm { b r } }$ . Pressure is unchanged in the trunk, but volume flow rate in the trunk changes according to $U _ { \mathrm { 1 , o u t } } = U _ { \mathrm { 1 , i n } } - p _ { 1 } / Z _ { \mathrm { b r } }$

For an OPNBRANCH, the numbers in lines a and b are multiplied by $( \omega / a ) ^ { 2 }$ and $\omega / a$ respectively, to obtain the impedance $Z _ { \mathrm { b r } }$ . These dependences on frequency [12] are correct in the low-frequency limit, $\omega r / a \ll 1$ . As for BRANCH, pressure is unchanged in the trunk, but volume flow rate in the trunk changes according to $U _ { \mathrm { 1 , o u t } } = U _ { \mathrm { 1 , i n } } - p _ { 1 } / Z _ { \mathrm { b r } }$

Similarly, for a flanged piston of radius r where the wave number is $k = \omega / a$ locally, the PISTBRANCH radiation impedance is given by [62]

$$
Z _ { \mathrm { b r } } = { \frac { \rho _ { m } a } { A } } \left( 1 - { \frac { 2 J _ { 1 } ( 2 k r ) } { 2 k r } } + i \left\{ \begin{array} { l l } { \left( { \frac { 4 / \pi } { 2 k r } } + { \frac { \sqrt { 8 / \pi } \sin ( 2 k r - 3 \pi / 4 ) } { ( 2 k r ) ^ { 3 / 2 } } } \right) } & { { \mathrm { i f ~ } } 2 k r > 2 . 6 8 , } \\ { { \frac { ( 4 / \pi ) 2 k r } { 3 } } \left( 1 - { \frac { ( 2 k r ) ^ { 2 } } { 1 5 } } \right) } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. \right)\tag{10.55}
$$

Note the implicit assumption that the outside and inside gases have the same density and sound speed.

Thus, the usual method for modeling a flanged piston or open tube radiating into 2π solid angle is DUCT, PISTBRANCH, HARDEND, with the HARDEND's impedance targets targeted to zero to enforce $U _ { \mathrm { 1 , o u t } } = 0$ , ensuring that $U _ { \mathrm { 1 , i n } } = U _ { \mathrm { 1 , b r } } = p _ { 1 } / Z _ { \mathrm { b r } }$ at the PISTBRANCH.

Output EdotBr gives the acoustic power $\dot { E } _ { \mathrm { b r } }$ flowing out of the branch.

None of these segments affects $T _ { m }$ . In BRANCH and OPNBRANCH, the trunk exiting energy flow is computed as $\dot { H } _ { 2 , k , \mathrm { o u t } } = \dot { H } _ { 2 , k , \mathrm { i n } } - \dot { H } _ { \mathrm { b r } }$ in insulated mode, described in Section 11.1.2. The trunk exiting energy flow is computed as $\dot { H } _ { 2 , k , \mathrm { o u t } } = \dot { H } _ { 2 , k , \mathrm { i n } } - \dot { E } _ { \mathrm { b r } }$ in PISTBRANCH in insulated mode. In thermally anchored mode, described in Section 11.1.2, $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ in all three of these segments. The spatial average of the complex oscillating temperature amplitude is calculated using $\langle T _ { 1 } \rangle = T _ { m } \beta p _ { 1 } / \rho _ { m } c _ { p }$

The behavior of these segments is independent of $\dot { N }$

## 10.4.2 VSPEAKER, ISPEAKER, VDUCER, and IDUCER

## General description:

The \*DUCERs and \*SPEAKERs without $\mathcal { \epsilon } _ { \mathbb { E } } ^ { \prime \prime }$ as their second character are electroacoustic transducers mounted as side branches to the apparatus. \*DUCERs have frequency-independent parameters; \*SPEAKERs let the user specify mass, spring constant, force constant, resistance, and inductance, so frequency-dependent (even resonant) transducers can be modeled. With

IDUCER and ISPEAKER, the user specifies the (real) current, and each pass of DELTAEC calculates the complex voltage; with VDUCER and vSPEAKER, the user specifies the (real) voltage, and DELTAEC computes complex current. IDUCER and ISPEAKER cannot be used with zero mechanical impedance because this would lead to a division by zero (see below). Hence, use VDuCER or VSPEAKER for lossless resonant or massless-and-springless transducers.

\*SPEAKER segments incorporate thermal-hysteresis losses on their area as if they included a SURFACE, but \*DUCER segments, which have no area parameter, do not.

Side-branched transducer elements, which accept only the magnitude of voltage or current applied as an input, but not the phase, effectively fix the overall time phase of the entire DELTAEC model by enforcing zero time phase for that voltage or current. The phase of pressure or volume flow rate (or both, if both $| p _ { 1 } |$ and $| U _ { 1 } |$ are nonzero) in the BEGIN statement must usually be allowed to vary (i.e., guessed) to accommodate this condition. This effectively limits a model to only one V or ISPEAKER (or \*DUCER), unless they are wired exactly in phase (or 180° out of phase, which can be accommodated with a minus sign).

(If a side-branch transducer has nonzero N flowing past it, the user might consider what fraction of the energy added by the transducer goes into raising the temperature of the steady flow passing by and what fraction is added to the thermoacoustic wave. In a VX\* heat-exchanger segment, $F _ { \dot { Q } \dot { N } }$ , (FracQN) determines these fractions. With a side-branch transducer, an RPN segment can be used, with user-specified assignment of these fractions using =Tm and =H2k.)

See also Section 14.5 for a discussion of the saturation of magnetic flux in \*SPEAKERs.

See also the series transducers described in Section 10.3.1 above.

## Input variables, VSPEAKER and ISPEAKER:

Area $( \mathrm { m } ^ { 2 } )$ The surface area S of the moving part of the \*SPEAKER. An area S is exposed to oscillating pressure on the front side. The velocity of the moving element is $U _ { 1 } / S$

R (ohm) The electrical resistance $R _ { e }$ of the coil.

L (henry) The electrical inductance L of the coil when it is prevented from moving.

BLProd (tesla·meter, which is equivalent to newton/amp) For a traditional moving-coil loudspeaker, the product of the magnetic field B and the wire length l immersed in B. More generally, the force in newtons exerted when one amp of current is applied and nothing is allowed to move.

M (kg) The moving mass M of the transducer.

K (N/m) The spring constant K of the transducer. This should include mechanical-spring forces and zero-current magnetic forces, but not gas-pressure forces exerted on area S.

Rm (N·s/m) The mechanical resistance $R _ { m }$ of the transducer.

|V| or [I| (volts or amps) In vSPEAKER, the amplitude of the oscillating voltage $V _ { 1 }$ , which is taken to be real. In ISPEAKER, the amplitude of the oscillating current $I _ { 1 }$ , which is taken to be real.

Solid The solid material on the surface S. (This is used only in the calculation of $\epsilon _ { s } ,$ which seldom differs significantly from its value for a solid with infinite conductivity and infinite specific heat in \*SPEAKERs.)

## Input variables, VDUCER and IDUCER:

Re(Ze) (ohm) The real part of the transducer's electrical impedance $Z _ { e }$ when it is prevented from moving.

Im(Ze) (ohm) The imaginary part of the transducer's electrical impedance $Z _ { e }$ when it is prevented from moving.

Re(T1) $\mathrm { ( V { \cdot } s / m ^ { 3 } ) }$ The real part of the complex transduction coefficient τ in the equations below.

Im(T1) $\mathrm { ( V { \cdot } s / m ^ { 3 } ) }$ The imaginary part of the complex transduction coefficient $\tau$ in the equations below.

Re(T2) $\mathrm { ( P a / A ) }$ The real part of the complex transduction coefficient $\tau ^ { \prime }$ in the equations below.

Im(T2) $\mathrm { ( P a / A ) }$ The imaginary part of the complex transduction coefficient $\tau ^ { \prime }$ in the equations below.

Re(Z) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The real part of the acoustic impedance $Z$ of the transducer.

Im(Z) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The imaginary part of the acoustic impedance Z of the transducer.

|V| or [I| (volts or amps) In VDUCER, the amplitude of the oscillating voltage $V _ { 1 }$ , which is taken to be real. In IDUCER, the amplitude of the oscillating current $I _ { 1 }$ , which is taken to be real.

## Potential targets:

None.

## Master-slave links:

None. The use of sameas is sometimes convenient in \*DUCERs, to keep $\tau ^ { \prime } = \tau .$

## Format and examples:

```csv
VDUCER
1.000E-09 a Re(Ze) ohms
.000 b Im(Ze) ohms
1.000E+04 c Re(T1) V-s/m^3
.000 d Im(T1) V-s/m^3
-1.000E+04 e Re(T2) Pa/A
.000 f Im(T2) Pa/A
1.000E-09 g Re(Z) Pa-s/m^3
1.000E-09 h Im(Z) Pa-s/m^3
10.0 i AplVol V
```

![[mu_66afccee_56cf074911781c55b388.jpg]]

```csv
VSPEAKER
6.000E-04 a Area m^2
6.00 b R ohms
.000 CL H
8.00 d BLProd T-m
5.000E-03 e M kg
.000 f K N/m
.000 g Rm N-s/m
-22.5 h AplVol V
ideal Solid type
```  
Another example of VSPEAKER is in Section 5.2.

## Calculations:

A side-branch transducer IDUCER, VDUCER, ISPEAKER, VSPEAKER is an object attached as shown Fig. 10.4 like a branch impedance, but obeying the complex equations $V _ { 1 } = Z _ { e } I _ { 1 } +$ $\tau U _ { x } , p _ { 1 } = \tau ^ { \prime } I _ { 1 } + Z U _ { x }$ . Pressure is unchanged, but volume flow rate changes according to $U _ { \mathrm { 1 , o u t } } = U _ { \mathrm { 1 , i n } } - U _ { x }$ . The volume flow rate of the transducer, $U _ { x } .$ is displayed in the output column.

• If current $I _ { 1 }$ is specified (note! its phase must be real), then use ISPEAKER or IDUCER, and find $U _ { x } = ( p _ { 1 } - \tau ^ { \prime } I _ { 1 } ) / Z$ and $V _ { 1 } = Z _ { e } I _ { 1 } + \tau U _ { x }$

• If voltage $V _ { 1 }$ is specified (note! its phase must be real), then use VSPEAKER or VDUCER, and find $I _ { 1 } = ( Z V _ { 1 } - \tau p _ { 1 } ) / ( Z _ { e } Z - \tau \tau ^ { \prime } )$ and $U _ { x } = ( V _ { 1 } - Z _ { e } I _ { 1 } ) / \tau$

• If a fixed electrical load impedance $Z _ { \mathrm { e x t } }$ is attached to the transducer, it can be modeled using a BRANCH segment instead of a \*SPEAKER or \*DUCER segment, with $Z _ { \mathrm { b r } } = p _ { 1 } / U _ { x } =$ $Z - \tau \tau ^ { \prime } / ( Z _ { e } + Z _ { \mathrm { e x t } } )$

In the case of speakers, $Z _ { e } = R _ { e } + i \omega L ~ ; ~ \tau = - \tau ^ { \prime } = B l / S ~ ; ~ Z = R _ { m } / S ^ { 2 } + i ( \omega M -$ $K / \omega ) / S ^ { 2 }$ . Side-branch speakers are assumed to have area $S$ exposed to the oscillating pressure. Thermal-hysteresis surface losses are computed for that area $S$ using the same formula as for a SURFACE, Eqs. (10.38) and (10.39). As described in Section 10.2.2, thermalhysteresis losses manifest themselves as a small change in volume flow rate

Note that IDUCER and ISPEAKER will crash if $Z$ is zero, so it is best to use VDUCER or vSPEAKER for mechanically ideal or lossless resonant transducers.

None of these segments affects $T _ { m }$ . The spatial average of the complex oscillating temperature amplitude is calculated using $\langle T _ { 1 } \rangle = T _ { m } \beta p _ { 1 } / \rho _ { m } c _ { p }$

The trunk's exiting energy flow is computed as $\dot { H } _ { 2 , k , \mathrm { o u t } } = \dot { H } _ { 2 , k , \mathrm { i n } } + \dot { W } _ { \mathrm { e l e c } }$ in insulated mode, described in Section 11.1.2. This assumes that the component is thermally insulated, so the electrical energy added at the transducer must flow out of the segment along the trunk, either upstream or downstream. The trunk's exiting energy flow is computed as $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ for thermally anchored mode, described in Section 11.1.2.

The WorkIn output variable displays the electrical power $\mathrm { R e } [ V _ { 1 } \tilde { I _ { 1 } } ] / 2$ that must be supplied to the transducer. If negative, this is electrical power produced by the transducer.

The Ph(V/I) variable is especially useful for constructing a target related to the electrical load impedance attached to a \*SPEAKER that is used as an alternator; for example, Ph(V/I) $= 1 8 0 ^ { \circ }$ means that the load impedance is purely resistive. See Fig. 4.1 for a more complicated example with both resistance and capacitance.

These segments behave the same whether $\dot { N } = 0$ or not.

![[mu_66afccee_78c380320ae304aa5f27.jpg]]  
Figure 10.5: Common smooth-stack geometries, with the x axis perpendicular to the page. (a) STKSLAB. (b) STKRECT. (c) STKCIRC.

## 10.5 Stacks and regenerators

The first three letters STK indicate a segment¹ that can develop a nonzero $d T _ { m } / d x$ . These segments are used to model the stacks of standing-wave thermoacoustic engines and refrigerators, the regenerators of Stirling engines and refrigerators (including pulse-tube refrigerators), the thermal buffer tubes of thermoacoustic-Stirling hybrid engines and refrigerators, and the pulse tubes of pulse-tube refrigerators. They are collected into three groups here: the smooth porous media STKSLAB, STKRECT, STKCIRC, and STKPIN, which can be used for either stacks or regenerators and are described in Section 10.5.1, the tortuous porous media STKSCREEN and STKPOWERLW for modeling regenerators, described in Section 10.5.2, and the boundary-layer STKDUCT and STKCONE segments, mostly used for pulse tubes and thermal buffer tubes and described in Section 10.6.1. If pore size or plate separation is much greater than thermal and viscous penetration depths, use STKDUCT or STKCONE.

## 10.5.1 STKSLAB, STKCIRC, STKRECT, and STKPIN

## General description of smooth stacks and regenerators:

Use STKSLAB for parallel-plate or spiral stacks or regenerators. Use STKRECT for square pores or rectangular pores whose aspect ratio is not large enough to justify the use of STKSLAB (see Ref. [63]). Use STKCIRC for circular or hexagonal pores. Use STKPIN for stacks comprised of pin arrays (see Ref. [64] for geometrical details of pin arrays).

In STKSLABs, STKRECTs, STKCIRCs, and STKPINs, the “Area" (the first line of the segment) is the total cross sectional area of the stack assembly, including both gas cross section and solid cross section.

In STKSLABs, STKRECTs, and STKCIRCs, $A _ { \mathrm { g a s } } = ( \tt A r e a ) \times ( \tt G a s A / A )$ and $A _ { \mathrm { s o l i d } } = ( \mathsf { A r e a } ) \times$ $\left( 1 - \mathtt { G a s A } / \mathtt { A } \right)$ . Plate half thickness (the 4th line of the segment) is used only for computing $\epsilon _ { s } ,$ not for computing heat conduction along x or what fraction of the Area is available to the gas. This allows separate accounting for area blocked by “ideal" fins and by support struts, pressure-vessel walls, or other heat-conducting structure as shown in Fig. 2.10(e). In most cases, $\epsilon _ { s }$ is near 0, so plate thickness need not be specified with much accuracy; GasA/A is far more important.

Because of the need to compute specialized functions, STKCIRCs compute more slowly than STKSLABs or STKDUCTs; STKPINs are slower still, and STKRECTs are very slow, especially for large aspect ratios. Hence, in the latter case, it may be convenient to use STKSLABs, at

least until a design is almost finalized.

## Input variables, STKSLAB:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A = y _ { 0 } / \left( y _ { 0 } + l \right)$ , where $A _ { \mathrm { g a s } }$ is the thermoacoustic area. The solid fraction $1 - \phi$ is used for the calculation of axial thermal conduction by the solid.

Length (m) The length $\Delta x$ of the stack or regenerator.

y0 (m) Half the plate spacing is $y _ { 0 }$ . In other words, $2 y _ { 0 }$ is the gap available to the gas—not the center-to-center spacing of the plates. See Fig. 10.5(a).

Lplate (m) Half the thickness of the solid plate is l. Thus, 2l is the plate thickness. See Fig. 10.5(a). This variable is used in the calculation of $\epsilon _ { s }$ to account for any imperfection in the imposition of the isothermal boundary condition imposed on the gas by the solid.

Solid The solid of which the plates are made.

## Input variables, STKRECT:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$ . The solid fraction $1 - \phi$ is used for the calculation of axial thermal conduction by the solid. Often, the user intends $\phi \ =$ $a b / \left( a b + a l + b l + l ^ { 2 } \right)$ ; this can be enforced with a master-slave link (see below).

Length (m) The length $\Delta x$ of the stack or regenerator.

a (m) Half of pore width. Thus, 2a is the small dimension of the rectangular pore available to the gas. See Fig. 10.5(b)

Lplate (m) Half the thickness of the solid plate. Thus, 2l is the plate thickness. This variable is used for the calculation of $\epsilon _ { s }$ to account for any imperfection in the imposition of the isothermal boundary condition imposed on the gas by the solid. See Fig. 10.5(b).

b (m) Half of pore breadth 2b. Thus, $2 a \times 2 b$ is the cross-sectional area available to the gas in a single pore. See Fig. 10.5(b)

Solid The solid of which the stack is made.

Input variables, STKCIRC:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$ . The solid fraction $1 - \phi$ is used for the calculation of axial thermal conduction by the solid.

Length (m) The length $\Delta x$ of the stack or regenerator.

radius (m) The radius $r _ { 0 }$ of the circular pore. Thus, $\pi r _ { 0 } ^ { 2 }$ is the cross-sectional area available to the gas in a single pore. (When we use STKCIRC to model hexagonal “honeycomb" pores, we choose $r _ { 0 }$ so the pore has the correct cross-sectional area: $r _ { 0 } = \left( \sqrt [ 4 ] { 3 } / \sqrt { 2 \pi } \right) b \simeq 0 . 5 2 5 0 3 8 b$ , where b is the flat-to-flat distance across the hexagonal pore.)

Lplate (m) Half the thickness of the solid sheet between pores. Thus, 2l is the plate thickness. This variable is used in the calculation of $\epsilon _ { s }$ to account for any imperfection in the imposition of the isothermal boundary condition imposed on the gas by the solid.

Solid The solid of which the sheets are made.

## Input variables, STKPIN:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$ , but usually not intended to include the cross-sectional area of the pressure-vessel wall.

2y0 (m) $2 y _ { 0 }$ is the center-to-center, nearest-neighbor pin-to-pin distance in the hexagonal lattice of pins. See Ref. [64]

Length (m) The length $\Delta x$ of the stack or regenerator.

R pin (m) The radius $r _ { i }$ of each pin.

Solid The solid of which the pins are made.

Potential targets:

None.

## Master—slave links:

The porosity $\phi \ ( = \mathtt { G a s A } / \mathtt { A } )$ of some of these segments can be slaved to other parameters: In STKSLAB, the porosity $\phi$ can be slaved to other parameters through the equation

$$
\phi = c { \frac { y _ { 0 } } { y _ { 0 } + l } } \ ,\tag{10.56}
$$

where $c$ is calculated when the link is first enabled, using

$$
c = \phi \frac { y _ { 0 } + l } { y _ { 0 } } \ .\tag{10.57}
$$

If $c = 1$ , this simply means that all of the cross section is full of gas and plate, with no struts, support members, or pressure-vessel wall. Otherwise, $c \neq 1$ indicates that a fraction of the area is occupied by such structure; the link keeps that fraction a constant.

In STKRECT, the porosity $\phi$ can be slaved to other parameters through the equation

$$
\phi = { \frac { a b } { ( a + l ) ( b + l ) } } \ ,\tag{10.58}
$$

so the geometry looks exactly as shown in ${ \mathrm { F i g } } .$ 10.5. No constant $c$ is used.

In STKCIRC, the porosity $\phi$ can be slaved to other parameters through the equation $\phi = \mathrm { \ m i n } ( c r _ { 0 } ^ { 2 } / A , 1 )$ , with $c$ calculated when the link is first enabled using $c = \phi A / r _ { 0 } ^ { 2 } .$ This link maintains a constant number of holes, but with the porosity clipped at a maximum value of 1.

The length of any of these segments can be slaved to the length of another segment to keep the total length constant.

(For an introduction to master-slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

STKSLAB parallel-plate stack   
sameas 1 Area   
0.724 GasA/A   
7.85e-2 m Length   
1.8e-4 m y0 (half the plate spacing)   
4.0e-5 m Lplate (half the plate thickness)   
kapton Solid   
STKRECT rectangular-pore stack   
sameas 1 Area   
0.694 GasA/A   
7.85e-2 m Length   
2.0e-4 m a (half of pore width)   
4.0e-5 m Lplate (half the plate thickness)   
4.0e-4 m b (pore area is 2a times 2b)   
stainless Solid   
STKCIRC approximates hexagonal honeycomb stack   
sameas 1 (m^2) total area   
0.81 gas area/total area   
0.279 (m) length   
0.50e-3 (m) radius of circular pore   
0.05e-3 (m) L:half of sheet thickness   
stainless stack material   
STKPIN Muller/Keolian pinstack invention   
sameas 2a a area m^2   
3.2e-4 b 2y0 m2y0 = nearest-neighbor center-to-center distance   
! in the hexagonal lattice   
0.1 c Length m   
4.e-5 d R pin m pin radius   
stainless

Another example of STKSLAB is in Section 5.2. STKCIRC is used in Section 5.5, and STKRECT is used in Section 6.2.

Calculations in smooth stacks and regenerators for $\dot { N } = 0$

Pressure propagates according to Rott's wave equation, written in the form

(10.59)

$$
\frac { d U _ { 1 } } { d x } ~ = ~ - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \beta ( f _ { \kappa } - f _ { \nu } ) } { ( 1 - f _ { \nu } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 } ,\tag{10.60}
$$

subject to the condition that the total energy flow $\dot { H } _ { 2 , k }$ is independent of $x ,$ which imposes the following condition on $T _ { m } ( x )$

$$
\frac { d T _ { m } } { d x } = \frac { \dot { H } _ { 2 , k } - \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U _ { 1 } } \left( 1 - \frac { T _ { m } \beta ( f _ { \kappa } - \tilde { f } _ { \nu } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) ( 1 - \tilde { f } _ { \nu } ) } \right) \right] } { \frac { \rho _ { m } c _ { p } | U _ { 1 } | ^ { 2 } } { 2 \omega A _ { \mathrm { g a s } } ( 1 - \sigma ) | 1 - f _ { \nu } | ^ { 2 } } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \tilde { f } _ { \nu } ) ( 1 + \epsilon _ { s } f _ { \nu } / f _ { \kappa } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) } \right] - A _ { \mathrm { g a s } } k - A _ { \mathrm { s o l i d } } k _ { s } } .\tag{10.61}
$$

For STKSLAB,

$$
f _ { j } ~ = ~ \frac { \operatorname { t a n h } [ ( 1 + i ) y _ { 0 } / \delta _ { j } ] } { ( 1 + i ) y _ { 0 } / \delta _ { j } } , ~ \mathrm { f o r } ~ j = \kappa ~ \mathrm { o r } ~ \nu ,\tag{10.62}
$$

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } \frac { \operatorname { t a n h } [ ( 1 + i ) y _ { 0 } / \delta _ { \kappa } ] } { \operatorname { t a n h } [ ( 1 + i ) \ell / \delta _ { s } ] } .\tag{10.63}
$$

For STKRECT,

$$
f _ { j } ~ = ~ 1 - { \frac { 6 4 } { \pi ^ { 4 } } } \sum _ { m , n \mathrm { o d d } } { \frac { 1 } { m ^ { 2 } n ^ { 2 } Y _ { m n } ( \delta _ { j } ) } } , \mathrm { f o r } ~ j = \kappa \mathrm { o r } \nu ,\tag{10.64}
$$

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } \frac { f _ { \kappa } ( 1 + i ) a b / \delta _ { \kappa } ( a + b ) } { \operatorname { t a n h } [ ( 1 + i ) \ell / \delta _ { s } ] } ,\tag{10.65}
$$

$$
\begin{array} { l } { \mathrm { w h e r e } \ Y _ { m n } ( \delta ) } \ = \ 1 - i \frac { \pi ^ { 2 } \delta ^ { 2 } } { 8 a ^ { 2 } b ^ { 2 } } ( b ^ { 2 } m ^ { 2 } + a ^ { 2 } n ^ { 2 } ) .  \end{array}\tag{10.66}
$$

For STKCIRC,

$$
f _ { j } ~ = ~ \frac { 2 J _ { 1 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } { ( i - 1 ) ( r _ { 0 } / \delta _ { j } ) J _ { 0 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } , ~ \mathrm { f o r } ~ j = \kappa ~ \mathrm { o r } ~ \nu ,\tag{10.67}
$$

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } \frac { f _ { \kappa } ( 1 + i ) r _ { 0 } / 2 \delta _ { \kappa } } { \operatorname { t a n h } [ ( 1 + i ) \ell / \delta _ { s } ] } .\tag{10.68}
$$

For STKPIN,

$$
f _ { j } = - \frac { \delta _ { j } } { ( i - 1 ) } \frac { 2 r _ { i } } { r _ { o } ^ { 2 } - r _ { i } ^ { 2 } } \frac { Y _ { 1 } [ ( i - 1 ) r _ { o } / \delta _ { j } ] J _ { 1 } [ ( i - 1 ) r _ { i } / \delta _ { j } ] - J _ { 1 } [ ( i - 1 ) r _ { o } / \delta _ { j } ] Y _ { 1 } [ ( i - 1 ) r _ { i } / \delta _ { j } ] } { Y _ { 1 } [ ( i - 1 ) r _ { o } / \delta _ { j } ] J _ { 0 } [ ( i - 1 ) r _ { i } / \delta _ { j } ] - J _ { 1 } [ ( i - 1 ) r _ { o } / \delta _ { j } ] Y _ { 0 } [ ( i - 1 ) r _ { i } / \delta _ { j } ] }
$$

$$
\mathrm { f o r } ~ j = \kappa ~ \mathrm { o r } ~ \nu ,\tag{10.69}
$$

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } \frac { J _ { 0 } ( \sqrt { - i \omega / \kappa _ { s } } r _ { i } ) } { J _ { 1 } ( \sqrt { - i \omega / \kappa _ { s } } r _ { i } ) } f _ { \kappa } \sqrt { - i \omega / \kappa } \frac { r _ { o } ^ { 2 } - r _ { i } ^ { 2 } } { 2 r _ { i } } ,\tag{10.70}
$$

where $\kappa = k / \rho _ { m } c _ { p } , \kappa _ { s } = k _ { s } / \rho _ { s } c _ { s } , r _ { i }$ is pin radius, and $r _ { o } ^ { 2 } = \left( \sqrt { 3 } / 2 \pi \right) \left( 2 y _ { o } \right) ^ { 2 }$ with $2 y _ { o }$ being the center-to-center distance between nearest-neighbor pins in the hexagonal array of pins.

The spatial average of the complex oscillating temperature amplitude is calculated using

$$
\left. T _ { 1 } \right. = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { f _ { \kappa } } { 1 + \epsilon _ { s } } \right] - \frac { U _ { 1 } } { i \omega A _ { \mathrm { g a s } } \left( 1 - \sigma \right) \left( 1 - f _ { \nu } \right) } \frac { d T _ { m } } { d x } \left[ 1 - \frac { f _ { \kappa } + \epsilon _ { s } f _ { \nu } } { 1 + \epsilon _ { s } } - \sigma \left( 1 - f _ { \nu } \right) \right] .\tag{10.71}
$$

Calculations in smooth stacks and regenerators for $\dot { N } \neq 0$

To turn on steady-flow calculations, check the appropriate box in the Optional Parameters dialog in the BEGIN segment. In the affected STK\*\* segments, the dependence of $T _ { m }$ on x can be changed significantly by the nonzero $\dot { N }$

The display of information is slightly changed. H2k is the “acoustic"-plus-longitudinalconduction part of the total energy flux—not including the steady-flow part of the total energy flux, $\dot { N } m w _ { m }$ , where $w _ { m }$ is the enthalpy per unit mass. Htot is the sum of H2k and $\dot { N } m w _ { m }$

Nonzero $\dot { N }$ changes the temperature profile in smooth stacks according to Refs. [38, 39, 13]: The temperature gradient in stacks is computed using constancy of total energy flux $\dot { H } _ { \mathrm { t o t } }$ . In other words, we solve this equation for $d T _ { m } / d x$

$$
\begin{array} { r c l } { \dot { H } _ { \mathrm { t o t } } } & { = } & { \displaystyle \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \widetilde { U } _ { 1 } \left( 1 - \frac { T _ { m } \beta \left( f _ { \kappa } - \widetilde { f } _ { \nu } \right) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) \left( 1 - \widetilde { f } _ { \nu } \right) } \right) \right] } \\ & & { \displaystyle + \frac { \rho _ { m } c _ { p } } { 2 A _ { \mathrm { g a s } } \omega ( 1 - \sigma ) \left| 1 - f _ { \nu } \right| ^ { 2 } } \frac { d T _ { m } } { d x } \left| U _ { 1 } \right| ^ { 2 } \mathrm { I m } \left[ \widetilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \widetilde { f } _ { \nu } ) ( 1 + \epsilon _ { s } f _ { \nu } / f _ { \kappa } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) } \right] } \\ & & { \displaystyle - ( A _ { \mathrm { g a s } } k + A _ { \mathrm { s o l i d } } k _ { s } ) \frac { d T _ { m } } { d x } + \dot { N } m w _ { m } } \end{array}\tag{10.72}
$$

and DELTAEC uses $\dot { H } _ { \mathrm { t o t } } = \mathrm { c o n s t a n t }$ to integrate with respect to x through a stack. The only $\dot { N } \neq 0$ feature in this equation is the final term, $\dot { N } m w _ { m }$ , where $w _ { m }$ is the mean enthalpy per unit mass. The mean enthalpy is referenced to zero at the environment temperature $T _ { 0 }$ which is 300 K by default and can be set to another value via =Tzero in an RPN segment. As usual, the value of $\dot { H } _ { \mathrm { t o t } }$ is determined by conditions in segments other than the stack, such as the value of $\dot { N }$ set in the BEGIN segment and the heat flows in adjacent heat exchangers.

The stack energy equation, Eq. (10.72), is reasonable only if $\dot { N }$ is essentially of second order, and hence only if $\dot { N }$ is formally negligible in the first-order momentum and energy equations [38, 39, 13]. Hence, we have not implemented any Doppler effect on $d p _ { 1 }$ and $d U _ { 1 }$ in stacks.

In the smooth stacks, $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ is calculated with laminar expressions:

(10.73)

$$
\begin{array} { r c l } { \frac { d p _ { 2 , 0 , 0 , \mathrm { B e G } } } { d x } } & { = } & { - \frac { | p _ { 1 } | ^ { 2 } } { 4 } \frac { d } { d x } ( \frac { 1 } { \rho _ { m a } ^ { 2 } } ) - \frac { | U _ { 1 } | ^ { 2 } } { 4 A _ { g g s } } \frac { d \rho _ { m } } { d x } - \frac { 8 \mu m \hat { N } _ { 2 , 0 } } { \rho _ { m } A _ { g s } v ^ { 2 } } \mathrm { f o r ~ S T K C I R C } , } \\ & { = } & { - \frac { | p _ { 1 } | ^ { 2 } } { 4 } \frac { d } { d x } ( \frac { 1 } { \rho _ { m a } ^ { 2 } } ) - \frac { | U _ { 1 } | ^ { 2 } } { 4 A _ { g g s } } \frac { d \rho _ { m } } { d x } - \frac { 3 \mu m \hat { N } _ { 2 , 0 } } { \rho _ { m } A _ { g a g } v _ { 0 } ^ { 2 } } \mathrm { f o r ~ S T K S I R } , } \\ & { = } & { - \frac { | p _ { 1 } | ^ { 2 } } { 4 } \frac { d } { d x } ( \frac { 1 } { \rho _ { m a } ^ { 2 } } ) - \frac { | U _ { 1 } | ^ { 2 } } { 4 A _ { g g s } } \frac { d \rho _ { m } } { d x } - \frac { 3 \mu m \hat { N } _ { 2 , 0 } } { \rho _ { m } A _ { g a s } a ^ { 2 } F _ { \mathrm { F i a n g } } } \mathrm { f o r ~ S T K R } } \\ & { - } & { - \frac { | p _ { 1 } | ^ { 2 } } { 4 } \frac { d } { d x } ( \frac { 1 } { \rho _ { m a } ^ { 2 } } ) - \frac { | U _ { 1 } | ^ { 2 } } { 4 A _ { g g s } } \frac { d \rho _ { m } } { d x }  } \\ & { } &   - \frac { 8 \mu m \hat { N } _ { 2 , 0 } }  \rho _ { m } A _ { \mathrm { t e n g } } r _ { 0 } ^  \end{array}\tag{10.74}
$$

,(10.75)

(10.76)

where the STKRECT's shape factor in Eq. (10.75) is given by

$$
\begin{array} { r c l } { { \displaystyle F _ { \mathrm { s h a p e } } } } & { { = } } & { { 1 - \displaystyle \frac { 1 9 2 a } { \pi ^ { 5 } } \displaystyle \sum _ { i = 1 , 3 , 5 , \ldots } \displaystyle \frac { \operatorname { t a n h } ( n \pi b / 2 a ) } { n ^ { 5 } } } } & { { ( 1 0 . 7 7 ) } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \simeq } } & { { 1 - \displaystyle \frac { 1 9 2 } { \pi ^ { 5 } } \displaystyle \frac { a } { b } \left[ \operatorname { t a n h } \displaystyle \frac { \pi b } { 2 a } + \displaystyle \frac { \operatorname { t a n h } ( 3 \pi b / 2 a ) } { 3 ^ { 5 } } + \displaystyle \frac { \operatorname { t a n h } ( 5 \pi b / 2 a ) } { 5 ^ { 5 } } + 0 . 0 0 0 0 8 8 5 3 6 \right] ~ \mathrm { f o r } ~ a \le b . } } \end{array}\tag{10.78}
$$

## 10.5.2 STKSCREEN and STKPOWERLW

(For a general description of all of the STK\*\* segments, see the first paragraph of Section 10.5.)

## General description of tortuous regenerators:

Use STKSCREEN for stacked-screen regenerators (see Ref. [55]). Use STKPOWERLW for any other regenerator for which friction factor and heat-transfer coefficients follow power laws in Reynolds number. The algorithms for these segments assume reasonably good internal thermal contact, so do not trust these segments for $r _ { h } \sim \delta _ { k }$ and certainly not for $r _ { h } > \delta _ { k }$ DELTAEC has no capability to model the physics of oscillating flow through tortuous porous media except in the small-pore, nearly isothermal limit.

## Input variables, STKSCREEN:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$ , including the screens but not including the cross-sectional area of the pressure-vessel wall.

VolPor The volumetric porosity $\phi .$ This is the ratio of the volume of gas in the regenerator to the total volume of the regenerator. For plain square-weave screen with m wires per unit length and wire diameter $d _ { \mathrm { w i r e } }$ , we use

$$
\phi \simeq 1 - \frac { \pi m d _ { \mathrm { w i r e } } } { 4 } ,\tag{10.79}
$$

as recommended by Organ [27], or we weigh the regenerator and use its $A , \Delta x .$ and the known density of its wire material to calculate $\phi .$ [See also Eq. (5.14).] Note that Eqs. (10.84) and (10.85) are fits [55] to data [54] over only a limited range of porosity, $0 . 6 0 < \phi < 0 . 7 7$ . Outside of this narrow range, a look at the original literature is advised, and STKPOWERLW might be a better choice than STKSCREEN.

Length (m) The length $\Delta x$ of the regenerator.

rh (m) The hydraulic radius $r _ { h }$ of the regenerator. This is the ratio of the gas volume to the gas-solid contact area. For plain square-weave screen with wire diameter $d _ { \mathrm { w i r e } }$ , we use

$$
r _ { h } \simeq d _ { \mathrm { w i r e } } \frac { \phi } { 4 ( 1 - \phi ) } ,\tag{10.80}
$$

as recommended by Organ [27].

ksFrac If the solid material in the regenerator were arranged in smooth columns parallel with the x axis, as in the smooth stacks described above in Section 10.5.1, then the contribution of ordinary thermal conduction in the solid to $\dot { H } _ { 2 , k }$ would be $\left( 1 - \phi \right) A k _ { s } \ d T _ { m } / d x$ . However, in STKSCREEN the solid conduction is reduced by the random point contacts between wires. ksFrac is the reduction factor. Reference [28] recommends a value of 0.1 for metal screens. We often use a larger value, to include the thermal conductance of the pressure-vessel wall around the regenerator. [See Eq. (9.1).] A user of plastic screens points out that low values of ksFrac are physically unrealistic when $k _ { s } / k \sim 1$

Solid The solid of which the wires are made.

## Input variables, STKPOWERLW:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$ , not including the cross-sectional area of the pressure-vessel wall.

VolPor The volumetric porosity $\phi .$ This is the ratio of the volume of gas in the regenerator to the total volume of the regenerator.

Length (m) The length $\Delta x$ of the regenerator.

rh (m) The hydraulic radius $r _ { h }$ of the regenerator. This is the ratio of the gas volume to the gas-solid contact area.

ksFrac If the solid material in the regenerator were arranged in smooth columns parallel with the x axis, as in the smooth stacks described above in Section 10.5.1, then the contribution of ordinary thermal conduction in the solid to $\dot { H } _ { 2 , k }$ would be $\left( 1 - \phi \right) A k _ { s } \ d T _ { m } / d x$ . However, in porous media such as balls the solid conduction is reduced by the random point contacts in the x direction between pieces of the solid. ksFrac is the reduction factor. Reference [28] recommends a value of 0.1 for woven screens. Use a larger value to include the thermal conductance of the pressure-vessel wall around the regenerator. [See Eq. (9.1).]

f con The friction-factor parameter $f _ { \mathrm { c o n } }$ in the equations below.

f exp The friction-factor parameter $f _ { \mathrm { e x p } }$ in the equations below.

h con The heat-transfer parameter $h _ { \mathrm { c o n } }$ in the equations below.

h exp The heat-transfer parameter $h _ { \mathrm { e x p } }$ in the equations below.

Solid The solid with which the regenerator is made.

## Potential targets:

None.

## Master-slave links:

The length of either of these segments can be slaved to the length of another segment to keep the sum of the two lengths constant.

(For an introduction to master-slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples of tortuous regenerators:

```csv
STKSCREEN a screen regenerator
sameas 1a a Area m^2 cross section of regenerator
.673 b VolPor volumetric porosity
5.500E-02 c Length m
1.830E-05 d rh m hydraulic radius
.300 e ksFrac fudge factor F for solid conduction
stainless Solid type
STKPOWERLW an etched foil regenerator
sameas 1a a Area m^2 cross section of regenerator
.700 b VolPor volumetric porosity
0.04 c Length m
40.e-6 d rh m hydraulic radius
.300 e ksFrac fudge factor for solid conduction
36. f f_con
1.0 g f_exp
24. h h_con
0.8 i h_exp
stainless Solid type
! ***** STKPOWERLW Sphere-bed example *****
!-
RPN Reynolds number cold (next time, use end-end avg)
0.0000 a G or T 415.18 A Reynolds
U1 mag 5a / 5b / 4 * 5d * rho * mu /
2
RPN Use f = 35/NR^0.9 + 0.5 for spheres, K&L Fig 7-10
0.0000 a G or T 35.000 A
0.5000 B
0.9000 C
0.9 0.5 35
!- 3
RPN f_con, f_exp, spheres, K&L Fig 7-10
!fcon and fexp by matching value and slope to equation in previous segment
0.0000 a G or T 0.21198 A f_exp
0.65405 Bf
2A 1A 2C ^ / 2B + sto 2C 2A * rc1 / 1A 2C ^ /
!-- 4
RPN fcon and fexp, continued
0.0000 a G or T 2.3476 A f_con
3B 1A 3A^ *
5
```  
STKPOWERLW Regenerator

```csv
6.9577E-4 a Area m^2
0.3900 b VolPor
4.0000E-2 c Length m
2.3000E-5 d rh m
0.1000 e ksFrac
sameas 4A f f_con
sameas 3A g f_exp
0.2300 h h_con
0.3000 i h_exp
```

Other examples of the use of STKSCREEN are in Sections 5.8 and 6.3.

Calculations in tortuous regenerators for $\dot { N } = 0$

In STKSCREEN regenerators, the pressure, volume flow rate, and mean temperature evolve according to

$$
\frac { d p _ { 1 } } { d x } = - i \omega \rho _ { m } \left[ 1 + \frac { ( 1 - \phi ) ^ { 2 } } { 2 ( 2 \phi - 1 ) } \right] \langle u _ { 1 } \rangle - \frac { \mu } { r _ { h } ^ { 2 } } \left( \frac { c _ { 1 } ( \phi ) } { 8 } + \frac { c _ { 2 } ( \phi ) N _ { R , 1 } } { 3 \pi } \right) \langle u _ { 1 } \rangle ,\tag{10.81}
$$

$$
\begin{array} { r c l } { \displaystyle \frac { d \left. u _ { 1 } \right. } { d x } } & { = } & { \displaystyle - \frac { i \omega \gamma } { \rho _ { m } a ^ { 2 } } p _ { 1 } + \beta \frac { d T _ { m } } { d x } \left. u _ { 1 } \right. + } \\ & & { } & { i \omega \beta \left[ \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } \frac { \epsilon _ { s } + \left( g _ { c } + e ^ { 2 i \theta _ { p } } g _ { v } \right) \epsilon _ { h } } { 1 + \epsilon _ { s } + \left( g _ { c } + e ^ { 2 i \theta _ { T } } g _ { v } \right) \epsilon _ { h } } p _ { 1 } - \frac { 1 } { i \omega } \frac { d T _ { m } } { d x } \frac { \epsilon _ { s } + \left( g _ { c } - g _ { v } \right) \epsilon _ { h } } { 1 + \epsilon _ { s } + \left( g _ { c } + e ^ { 2 i \theta _ { T } } g _ { v } \right) \epsilon _ { h } } \left. u _ { 1 } \right. \right] , } \end{array}\tag{10.82}
$$

$$
\begin{array} { r c l } { \displaystyle \frac { d T _ { m } } { d x } } & { = } & { \left\{ \mathrm { R e } \left[ \left( T _ { m } \beta \frac { \epsilon _ { s } + \epsilon _ { h } ( g _ { c } + e ^ { 2 i \theta _ { r } } g _ { v } ) } { 1 + \epsilon _ { s } + \epsilon _ { h } ( g _ { c } + e ^ { 2 i \theta _ { r } } g _ { v } ) } + 1 - T _ { m } \beta \right) p _ { 1 } \widetilde { \langle u _ { 1 } \rangle } \right] - \frac { 2 \dot { H } _ { 2 , k } } { \phi A } \right\} } \\ & & { \quad \quad / \left\{ \frac { \rho _ { m } c _ { p } } { \omega } \mathrm { I m } \left[ \frac { \epsilon _ { s } + \epsilon _ { h } ( g _ { c } - g _ { v } ) } { 1 + \epsilon _ { s } + \epsilon _ { h } ( g _ { c } + e ^ { 2 i \theta _ { r } } g _ { v } ) } \right] \langle u _ { 1 } \rangle \widetilde { \langle u _ { 1 } \rangle } + 2 \left[ k _ { s , \mathrm { e f f } } \frac { 1 - \phi } { \phi } + k \right] \right\} , } \end{array}\tag{10.83}
$$

using

$$
c _ { 1 } ( \phi ) = 1 2 6 8 - 3 5 4 5 \phi + 2 5 4 4 \phi ^ { 2 } , \quad c _ { 2 } ( \phi ) = - 2 . 8 2 + 1 0 . 7 \phi - 8 . 6 \phi ^ { 2 } ,\tag{10.84}
$$

$$
b ( \phi ) = 3 . 8 1 - 1 1 . 2 9 \phi + 9 . 4 7 \phi ^ { 2 } ,\tag{10.85}
$$

$$
\begin{array} { r } { N _ { R , 1 } = 4 \left| \langle u _ { 1 } \rangle \right| r _ { h } \rho _ { m } / \mu , } \end{array}\tag{10.86}
$$

$$
\epsilon _ { s } = \phi \rho _ { m } c _ { p } / ( 1 - \phi ) \rho _ { s } c _ { s } , \quad \epsilon _ { h } = 8 i r _ { h } ^ { 2 } / b ( \phi ) \sigma ^ { 1 / 3 } \delta _ { \kappa } ^ { 2 } ,\tag{10.87}
$$

$$
\delta _ { \kappa } ^ { 2 } = 2 k / \omega \rho _ { m } c _ { p } ,\tag{10.88}
$$

$$
\theta _ { p } = \mathrm { p h a s e } ( \langle u _ { 1 } \rangle ) - \mathrm { p h a s e } \left( p _ { 1 } \right) , \quad \theta _ { T } = \mathrm { p h a s e } ( \langle u _ { 1 } \rangle ) - \mathrm { p h a s e } \left( \langle T \rangle _ { u , 1 } \right) ,\tag{10.89}
$$

$$
g _ { c } = \displaystyle \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \displaystyle \frac { d z } { 1 + N _ { R , 1 } ^ { 3 / 5 } \cos ^ { 3 / 5 } ( z ) } , \quad g _ { v } = - \displaystyle \frac { 2 } { \pi } \displaystyle \int _ { 0 } ^ { \pi / 2 } \displaystyle \frac { \cos ( 2 z ) d z } { 1 + N _ { R , 1 } ^ { 3 / 5 } \cos ^ { 3 / 5 } ( z ) } .\tag{10.90}
$$

These expressions were derived [55] with the assumption that viscous and thermal penetration depths are much larger than $r _ { h }$ . The spatial average oscillatory velocity $\langle u _ { 1 } \rangle =$ $U _ { 1 } / \phi A$ , where $\phi$ is volumetric porosity and A is regenerator cross-sectional area; and $k _ { s , \mathrm { e f f } } = ( \tt k s F r a c ) \ / k _ { s }$ where ksFrac is a factor to reduce thermal conduction along x due to the poor thermal contact between adjacent screen layers (Reference [28] recommends ksFrac $\approx 0 . 1$ for metal screens). ksFrac can also be used to account for conduction in the case surrounding the regenerator. The trigonometric integrals in Eqs. (10.90) are not evaluated by DELTAEC; these integrals were performed once, off-line, to obtain simple functional fits that DELTAEC uses during computation.

The spatial average of the complex oscillating temperature amplitude, $\left. T _ { 1 } \right.$ , is calculated using Eq. (29) in Ref. [55]. See Section 14.3 for the details of DELTAEC's implementation of the mathematics in Ref. [55], whose equations for $d T _ { m } / d x$ and $\left. T _ { 1 } \right.$ must be solved iteratively.

STKPOWERLW segments are calculated in the same manner as STKSCREEN, with a few exceptions. The steady-flow friction factor and heat transfer coefficients are parameterized by

$$
f ~ = ~ f _ { \mathrm { c o n } } { N } _ { R } ^ { - f _ { \mathrm { e x p } } } ,\tag{10.91}
$$

$$
N _ { S t } \sigma ^ { 2 / 3 } = h _ { \mathrm { c o n } } N _ { R } ^ { - h _ { \mathrm { e x p } } } ,\tag{10.92}
$$

where $N _ { S t }$ is the Stanton number and the Reynolds number $N _ { R }$ is defined in the usual way as

$$
N _ { R } = \frac { 4 U r _ { h } \rho } { \phi A \mu } .\tag{10.93}
$$

[Note: Equation (10.91) is Fanning friction factor, the friction factor used by Kays and London [54], so instantaneously $d p / d x = - \left( f / r _ { h } \right) \textstyle { \frac { 1 } { 2 } } \rho u ^ { 2 } . ]$ The pressure equation is replaced by

$$
\frac { d p _ { 1 } } { d x } = - i \omega \rho _ { m } \left. u _ { 1 } \right. - I _ { f } \frac { \mu } { 8 r _ { h } ^ { 2 } } f _ { \mathrm { c o n } } N _ { R , 1 } ^ { 1 - f _ { \mathrm { e x p } } } \left. u _ { 1 } \right. ,\tag{10.94}
$$

where

$$
I _ { f } = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } \sin ^ { 3 - f _ { \mathrm { e x p } } } ( z ) d z .\tag{10.95}
$$

In the volume-flow-rate and mean-temperature equations, these parameters are redefined for the power-law stack:

$$
g _ { c } ~ = ~ N _ { R , 1 } ^ { h _ { \mathrm { e x p } } - 1 } \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \cos ^ { h _ { \mathrm { e x p } } - 1 } ( z ) d z ,\tag{10.96}
$$

$$
g _ { v } ~ = ~ - N _ { R , 1 } ^ { h _ { \mathrm { e x p } } - 1 } \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \cos 2 z \cos ^ { h _ { \mathrm { e x p } } - 1 } ( z ) d z ,\tag{10.97}
$$

$$
\begin{array} { c c l } { { b ( \phi ) } } & { { = } } & { { h _ { \mathrm { c o n } } . } } \end{array}\tag{10.98}
$$

The trigonometric integrals in Eqs. (10.96) and (10.97) are not evaluated by DELTAEC; these integrals were performed once, off-line, to obtain simple functional fits that DELTAEC

uses during computation. 2

Calculations in tortuous regenerators for $\dot { N } \neq 0$

The temperature gradient in STKSCREEN and STKPOWERLW is computed using constancy of total energy flux $\dot { H } _ { \mathrm { t o t } } = \dot { H } _ { 2 , k } + \dot { N } m w _ { m }$ . In other words, we solve this equation for $d T _ { m } / d x$

$$
\begin{array} { r c l } { \dot { H } _ { \mathrm { t o t } } } & { = } & { \displaystyle \frac { \phi A } { 2 } \mathrm { R e } \left[ \left( 1 - T _ { m } \beta + T _ { m } \beta \frac { \epsilon _ { s } + \epsilon _ { h } \left( g _ { c } + e ^ { 2 i \theta _ { p } } g _ { v } \right) } { 1 + \epsilon _ { s } + \epsilon _ { h } \left( g _ { c } + e ^ { 2 i \theta _ { T } } g _ { v } \right) } \right) p _ { 1 } \widetilde { \left. u _ { 1 } \right. } \right] } \\ & & { \displaystyle - \frac { \phi A \rho _ { m } c _ { p } } { 2 \omega } \frac { d T _ { m } } { d x } \mathrm { I m } \left[ \frac { \epsilon _ { s } + \epsilon _ { h } \left( g _ { c } - g _ { v } \right) } { 1 + \epsilon _ { s } + \epsilon _ { h } \left( g _ { c } + e ^ { 2 i \theta _ { T } } g _ { v } \right) } \right] \left. u _ { 1 } \right. \widetilde { \left. u _ { 1 } \right. } } \\ & & { \displaystyle - [ \phi A k + ( 1 - \phi ) A k _ { s , \mathrm { e f f } } ] \frac { d T _ { m } } { d x } + \dot { N } m w _ { m } , } \end{array}\tag{10.99}
$$

and DELTAEC uses $\dot { H } _ { \mathrm { t o t } } = \mathrm { c o n s t a n t }$ to find $T _ { m } ( x )$ through the regenerator. The only term with nonzero $\dot { N }$ in this equation is the final one, $\dot { N } m w _ { m }$ . As usual, the value of $\dot { H } _ { \mathrm { t o t } }$ is determined by conditions in segments other than the regenerator, such as the heat flows in adjacent heat exchangers.

The first-order pressure gradient $d p _ { 1 } / d x$ is unchanged by nonzero $\dot { N }$ , and $d \left. u _ { 1 } \right. / d x$ is changed only indirectly through its dependence on $d T _ { m } / d x$

In STKSCREEN, the expression for head-loss gradient is a straightforward result of using the quasi-steady approximation, as outlined in Section 14.4:

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 2 , 0 / \mathrm { D E C } } } { d x } } & { = } & { \displaystyle - \frac { \mu m \dot { N } _ { 2 , 0 } } { 8 r _ { h } ^ { 2 } \rho _ { m } \phi A } \left[ c _ { 1 } ( \phi ) + c _ { 2 } ( \phi ) N _ { { \cal R } , 2 , 0 } \left( 1 + \frac { 1 } { 2 \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { | p _ { 1 } | } { p _ { m } } \frac { \cos \phi } { \varepsilon _ { 2 , 0 } } \right) \right] , ~ | \varepsilon _ { 2 , 0 } | \ge 1 , } \\ & & { } & { \displaystyle \left( 1 0 . 1 0 0 \right) } \\ & { = } & { \displaystyle - \frac { \mu m \dot { N } _ { 2 , 0 } } { 8 r _ { h } ^ { 2 } \rho _ { m } \phi A } \left\{ c _ { 1 } ( \phi ) + \frac { c _ { 2 } ( \phi ) N _ { { \cal R } , 2 , 0 } } { \pi \varepsilon _ { 2 , 0 } ^ { 2 } } \left[ \left( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { | p _ { 1 } | } { p _ { m } } \cos \phi \right) \sin ^ { - 1 } | \varepsilon _ { 2 , 0 } | \right. \right. } \\ & { } & { \displaystyle \left. \left. + \mathrm { s i g n } ( \varepsilon _ { 2 , 0 } ) \left( 3 \varepsilon _ { 2 , 0 } + \frac { 2 } { 3 } \left( 2 + \varepsilon _ { 2 , 0 } ^ { 2 } \right) \frac { | p _ { 1 } | } { p _ { m } } \cos \phi \right) \right] \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } \right\} , ~ | \varepsilon _ { 2 , 0 } | \le 1 , } \end{array}\tag{10.101}
$$

where the steady-flow Reynolds number is

$$
N _ { R , 2 , 0 } = \frac { m \left| \dot { N } _ { 2 , 0 } \right| 4 r _ { h } } { \phi A \mu }\tag{10.102}
$$

and $\varepsilon _ { 2 , 0 } = m \dot { N } _ { 2 , 0 } / \rho _ { m } \left| U _ { 1 } \right|$ . See Section 8.1.1 for explanation of the use of $\dot { N } _ { 2 , 0 }$ instead of $\dot { N }$ here.

In STKPOWERLW, the expression for head-loss gradient is the same as the pessimistic case in turbulent DUCTs, but with $f _ { M }$ and $d f _ { M } / d N _ { R }$ given by the STKPOWERLW expression, Eq. (10.91), and with $| p _ { 1 } | / \gamma p _ { m }$ replaced by $| p _ { 1 } | / p _ { m }$ to model isothermal oscillations.

## 10.6 Pulse tubes and thermal buffer tubes

(For a general description of all of the STK\*\* segments, see the first paragraph of Section 10.5.)

## 10.6.1 STKDUCT and STKCONE

## General description:

If $d T _ { m } / d x \ne 0$ and pore size or plate separation is much greater than thermal and viscous penetration depths, use STKDUCT or STKCONE. These segments are used mostly for pulse tubes and thermal buffer tubes.

In a STKCONE, the variable fwal1 (parameter f) specifies the wall thickness. If f $\mathtt { w a l l } { < } 1$ the wall thickness is constant, but if fwal1> 1, the wall thickness is proportional to the local cone radius (so the wall stress can be constant, which is the minimum-weight, minimumthermal-conductance design).

The one-dimensional nature of DELTAEC calculations can be particularly unrealistic in STKDUCT and STKCONE, because DELTAEC assumes that $T _ { m } ( x )$ and $T _ { \mathrm { s o l i d } } ( x )$ are equal at all x, despite the fact that these are likely to be very different if any type of streaming occurs

Input variables, STKDUCT:

Area $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { \mathrm { g a s } }$ available to the gas, based on inside dimensions of the STKDUCT.

Perim (m) Perimeter I of the inside cross section described above.

Length (m) The length $\Delta x$ of the STKDUCT.

WallA $( \mathrm { m } ^ { 2 } )$ The cross-sectional area $A _ { \mathrm { s o l i d } }$ of the wall material.

Solid The solid material comprising the walls.

Input variables, STKCONE:

AreaI $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { \mathrm { g a s } , I }$ available to the gas at the initial end of the STKCONE, based on inside dimensions.

PerimI (m) Perimeter $\Pi _ { I }$ of the initial inside cross section described above.

Length (m) The length $\Delta x$ of the STKCONE.

AreaF $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { \mathrm { g a s } , F }$ available to the gas at the final end of the STKCONE, based on inside dimensions.

PerimF (m) Perimeter $\Pi _ { F }$ of the final inside cross section described above.

f\_wall For fwall < 1, wall thickness = fwall × initial perimeter, and is independent of x. For fwall > 1, wall thickness = local perimeter/fwall, so local wall cross-sectional area = (local perimeter)²/fwal1.

Solid The solid material comprising the walls.

## Potential targets:

None.

## Master—slave links:

In STKDUCT, the perimeter can be slaved to the area to maintain the cross-sectional shape when the area is changed.

In STKDUCT, the perimeter and the area can also be slaved to the length, to maintain both constant volume and constant cross-sectional shape when the length is changed.

In STKCoNE, the initial perimeter can be slaved to the initial area, the final perimeter can be slaved to the final area, or both perimeters can be slaved to both areas, so shapes are maintained when areas are changed.

The length and both perimeters of a STKCoNE can be slaved to its two areas, to keep the cross-sectional shapes of the ends and the wall taper angle constant when either or both areas are changed.

The length of either of these segments can be slaved to the length of another segment to keep the sum of the two lengths constant.

(For an introduction to master-slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

STKDUCT boundary-layer approx   
0.01 m2 area of gas   
0.4 m perimeter (this duct is square)   
1. m length   
0.001 m2 wall material's cross-sectional area   
stainless   
STKCONE boundary-layer w/ taper   
0.01 m2 area of gas   
0.35 m perimeter   
1. m length   
sameas 8a   
sameas 8b   
0.001fwall   
stainless

Other examples of STKDUCT are in Sections 5.8.3 and 6.3.

Calculations for $\dot { \underline { { N } } } = 0 \dot { : }$

In STKDUCT and STKCONE, pressure propagates according to Rott's wave equation, written in the form

(10.103)

$$
\frac { d U _ { 1 } } { d x } ~ = ~ - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \beta ( f _ { \kappa } - f _ { \nu } ) } { ( 1 - f _ { \nu } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 } ,\tag{10.104}
$$

subject to the condition that energy flow $\dot { H } _ { 2 , k }$ is independent of $x ,$ which imposes the following condition on $T _ { m } ( x )$

$$
\frac { d T _ { m } } { d x } = \frac { \dot { H } _ { 2 , k } - \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U _ { 1 } } \left( 1 - \frac { T _ { m } \beta ( f _ { \kappa } - \tilde { f } _ { \nu } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) ( 1 - \tilde { f } _ { \nu } ) } \right) \right] } { \frac { \rho _ { m } c _ { p } | U _ { 1 } | ^ { 2 } } { 2 \omega A _ { \mathrm { g a s } } ( 1 - \sigma ) | 1 - f _ { \nu } | ^ { 2 } } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \tilde { f } _ { \nu } ) ( 1 + \epsilon _ { s } f _ { \nu } / f _ { \kappa } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) } \right] - A _ { \mathrm { g a s } } k - A _ { \mathrm { s o l i d } } k _ { s } } .\tag{10.105}
$$

For STKDUCT and STKCONE,

$$
f _ { j } ~ = ~ ( 1 - i ) \Pi \delta _ { j } / 2 A , ~ \mathrm { f o r } ~ j = \kappa ~ \mathrm { o r } ~ \nu ,\tag{10.106}
$$

$$
\epsilon _ { s } ~ = ~ \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } \frac { 1 } { \operatorname { t a n h } [ ( 1 + i ) \ell / \delta _ { s } ] } ~ , \mathrm { { w h e r e } } ~ \ell = \frac { \mathrm { w a l l ~ c r o s s \mathrm { - } s e c t ~ a r e a } } { \mathrm { p e r i m e t e r } } ,\tag{10.107}
$$

so long as $2 A / \Pi \delta _ { i } > 3 0$ . For $2 A / \Pi \delta _ { j } < 2 5$ , the functions are the same as for STKCIRC, with $r _ { 0 } ( x ) = 2 A ( x ) / \Pi ( x )$ . In between, a linear combination is used.

The spatial average of the complex oscillating temperature amplitude is calculated using

$$
\left. T _ { 1 } \right. = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { f _ { \kappa } } { 1 + \epsilon _ { s } } \right] - \frac { U _ { 1 } } { i \omega A _ { \mathrm { g a s } } \left( 1 - \sigma \right) \left( 1 - f _ { \nu } \right) } \frac { d T _ { m } } { d x } \left[ 1 - \frac { f _ { \kappa } + \epsilon _ { s } f _ { \nu } } { 1 + \epsilon _ { s } } - \sigma \left( 1 - f _ { \nu } \right) \right] .\tag{10.108}
$$

## Calculation with $\dot { N } \neq 0 ;$

STKDUCT treats nonzero $\dot { N }$ in the same way as STKCIRC. STKCONE is similar, but with variation of A and Ⅱ with x. Remember to increase Nint if $T _ { m } ( x )$ curves significantly.

## 10.7 Heat exchangers

DELTAEC heat exchangers are used to inject or remove heat. The first law of thermodynamics insists that this heat must equal the difference between upstream and downstream $\dot { H } _ { \mathrm { t o t } }$ DELTAEC heat exchangers necessarily have surface area, so they experience both viscous and thermal dissipation of acoustic power.

Heat exchangers are collected into three groups here. The smooth, short HX and TX have parallel-plate and tubular geometry, respectively, and are described in Section 10.7.1. The short, tortuous porous heat exchangers SX and PX, for screens and power-law structures, respectively, are described in Section 10.7.2. The long, smooth, variable-temperature and variable-heat-density exchangers VXT1, VXT2, VXQ1, and VXQ2 are described in Section 10.7.3

<!-- Original PDF pages 201-310 -->

## 10.7.1 HX and TX

## General description:

For a general description of all DeltaEC heat exchangers, see the initial paragraphs of the heat-exchanger documentation, Section 10.7.

In HX the thermoacoustic working gas is between parallel plates; in TX it is inside cylindrical tubes. Heat $\dot { Q }$ is positive when it flows from the solid into the thermoacoustic gas, adding to $\dot { H } _ { \mathrm { t o t } }$ . The temperature diference between the solid temperature $T _ { \mathrm { s o l i d } }$ and the gas temperature $T _ { m }$ is proportional to ${ \dot { Q } } .$ . The proportionality constant is not well validated, either theoretically or experimentally; we find that it usually seems to be accurate within a factor of 2.

HX and TX are assumed to be so short that the numerical integration from one end to the other is performed with a single fourth-order Runge-Kutta step. (Most other integrated segments, i.e., DUCT, CONE, MIX\*\*, STK\*\*, and VX\*\*, are integrated with Nint fourth-order Runge-Kutta steps.) See VX\*\* in Section 10.7.3 below for longer tubular heat exchangers.

Input variables, HX:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$

Length (m) The length $\Delta x$ of the heat exchanger.

y0 (m) The plate spacing is $2 y _ { 0 }$ . In other words, $2 y _ { 0 }$ is the gap available to the gas—not the center-to-center spacing of the plates.

HeatIn The heat $\dot { Q }$ added to the thermoacoustic gas in the heat exchanger. Positive $\dot { Q }$ indicates heat flow from solid to gas.

Solid The solid material on the inside surface of the HX. This is used only in the calculation of $\epsilon _ { s }$ , which seldom difers significantly from its value for a solid with infinite conductivity and specific heat.

Input variables, TX:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$

Length (m) The length $\Delta x$ of the heat exchanger.

radius (m) The radius of each tube, $r _ { 0 }$

HeatIn The heat $\dot { Q }$ added to the thermoacoustic gas in the heat exchanger. Positive $\dot { Q }$ indicates heat flow from solid to gas.

Solid The solid material on the inside surface of the TX. This is used only in the calculation of $\epsilon _ { s }$ , which seldom difers significantly from its value for a solid with infinite conductivity and specific heat.

## Potential targets:

TSolid If used as a target, DeltaEC’s shooting method compares $T _ { \mathrm { s o l i d } }$ to this value.

## Master–slave links:

In TX, the porosity $\phi$ can be slaved to other parameters via the equation $\phi = \operatorname* { m i n } ( c r _ { 0 } ^ { 2 } / A , 1 )$ with c calculated when the link is first enabled via $c = \phi A / r _ { 0 } ^ { 2 }$ . This link maintains a constant number of holes, up to a maximum porosity of 1.

The length of HX or TX can be slaved to the length of another segment to keep the sum of the two lengths constant.

(For an introduction to master–slave links, and a complete list of linking options for all segments, see Section 2.7.2.)

## Format and examples:

HX parallel-plate heat exchanger   
sameas 1 Area   
0.600 GasA/A   
6.35e-3 m Length   
1.9e-4 m y0 = half of plate spacing   
-20.0 W HeatIn   
300. K Est-T Target   
copper solid   
TX tube-in-shell heat exchanger   
0.2 a Area m^2   
.188 b GasA/A   
.400 c Length m   
6.350E-03 d radius m (radius of each tube)   
1.818E+05 e HeatIn W   
possible target   
nickel Solid type  
Other examples of HX appear in Chapter $5$

![[mu_66afccee_a4763918969f84f1dfbc.jpg]]

## Calculations:

In HX and TX, wave propagation is calculated using

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A _ { \mathrm { g a s } } } U _ { 1 } ,\tag{10.109}
$$

$$
\frac { d U _ { 1 } } { d x } = - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } .\tag{10.110}
$$

HX uses parallel plate geometry in computing $f _ { \kappa } , f _ { \nu }$ , and $\epsilon _ { s }$

$$
f _ { j } = \frac { \operatorname { t a n h } [ ( 1 + i ) y _ { 0 } / \delta _ { j } ] } { ( 1 + i ) y _ { 0 } / \delta _ { j } } , \mathrm { f o r } \ j = \kappa \ \mathrm { o r } \ \nu ,\tag{10.111}
$$

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } .\tag{10.112}
$$

Similarly, TX uses cylindrical geometry in computing $f _ { \kappa }$ and $f _ { \nu } \colon$ For $r _ { 0 } / \delta _ { j } < 2 5 , f _ { \kappa }$ and $f _ { \nu }$ are calculated using complex Bessel functions

$$
f _ { j } = \frac { 2 J _ { 1 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } { ( i - 1 ) ( r _ { 0 } / \delta _ { j } ) J _ { 0 } [ ( i - 1 ) r _ { 0 } / \delta _ { j } ] } \mathrm { f o r } j = \kappa \mathrm { o r } \nu .\tag{10.113}
$$

For $r _ { 0 } / \delta _ { j } > 3 0$ , the boundary-layer approximation is used:

$$
f _ { j } = ( 1 - i ) \delta _ { j } / r _ { 0 } ~ \mathrm { f o r } ~ j = \kappa ~ \mathrm { o r } ~ \nu .\tag{10.114}
$$

For intermediate values, linear interpolation is used to make a smooth match between the two regimes. In both cases, $\epsilon _ { s }$ is calculated using

$$
\epsilon _ { s } = \left( \frac { k \rho _ { m } c _ { p } } { k _ { s } \rho _ { s } c _ { s } } \right) ^ { 1 / 2 } .\tag{10.115}
$$

In TX, the radius $r _ { 0 }$ is that of one circular pore, so for a heat exchanger comprised of N circular pores, the total cross-sectional area available to the working gas is $N \pi r _ { 0 } ^ { 2 } =$ $( \tt A r e a ) ( \tt G a s A / A )$

The spatial average of the complex oscillating temperature amplitude is calculated using

$$
\langle T _ { 1 } \rangle = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { f _ { \kappa } } { 1 + \epsilon _ { s } } \right] .\tag{10.116}
$$

HX and TX have no turbulence algorithms.

For $\dot { N } = 0$ , temperature and power change according to

$$
\frac { d T _ { m } } { d x } = 0 ,\tag{10.117}
$$

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } = \frac { d \dot { H } _ { 2 , k } } { d x } = \frac { \dot { Q } } { \Delta x } ,\tag{10.118}
$$

$$
T _ { \mathrm { s o l i d } } = T _ { m } + \frac { \dot { Q } } { h ~ A _ { \mathrm { g a s } } x _ { \mathrm { e f f } } / r _ { h } } ,\tag{10.119}
$$

where $\Delta x$ is the heat exchanger length and $\dot { Q }$ is the heat added to the heat exchanger. Positive heat $\dot { Q }$ (parameter $^ { \mathsf { e } ) }$ flows into the apparatus. The heat flow $\dot { Q }$ is an input for each pass of DeltaEC, and it is often used as a guess for the shooting method described in Section 2.5. The heat-transfer coeficient h is estimated with

$$
h = { \frac { k } { y _ { \mathrm { e f f } } } } ,\tag{10.120}
$$

and

$$
x _ { \mathrm { e f f } } = \mathrm { m i n } [ 2 \left| \xi _ { 1 } \right| , \Delta x ]\tag{10.121}
$$

$$
\begin{array} { r c l } { y _ { \mathrm { e f f } } } & { = } & { \operatorname* { m i n } [ \delta _ { \kappa } , r _ { h } ] , } \end{array}\tag{10.122}
$$

with hydraulic radius $r _ { h }$ equal to $y _ { 0 }$ for HX and equal to $r _ { 0 } / 2$ for TX. These expressions may be quite inaccurate, but we believe they are more useful than nothing. A little experimental evidence for $T _ { \mathrm { s o l i d } } - T _ { m }$ is presented in Ref. [23]. A user who mistrusts these expressions can use the gas temperature (available through RPN, and as an output in the adjacent stack segment) instead of the solid temperature for plotting or targeting, and/or use RPNs to construct custom expressions instead of Eqs. (10.119)–(10.122).

For $\dot { N } \neq 0$ , the wave and energy calculations are unchanged, so all of the heat goes into $\dot { H } _ { 2 , k }$ and none into the steady flow. This seems fine for weak steady flows, such as weak Gedeon streaming when a TASHE is operated slightly away from the conditions at which its gas diode enforces $\dot { N } = 0$ . For strong steady flow, the user can override the built-in calculations with an RPN such as

13 RPN Fix Tm. Inp = frac of heat that should go to mean flow   
0.25   
H2k inp 12e \* - =H2k ; inp 12e \* Ndot / m / cp / Tm + =Tm

following the heat exchanger, where 12e is the heat in the upstream heat exchanger and 13a is the steady-flow heat fraction. That fraction is often guessed, to give DeltaEC enough flexibility to meet nearby temperature and energy boundary conditions. Alternatively, the fraction can also be set equal to a simple expression like $\left( 1 + \rho _ { m } \left. U _ { 1 } \right. / \left. \dot { N } \right. m \right) ^ { - 1 }$ in an RPN, supplying an experimentally unsupported but plausible estimate of how power divides itself between the steady flow and the acoustic flow.

For $\dot { N } \neq 0$ , the gradients in $p _ { 2 , 0 }$ <sub>,DEC</sub> are calculated using Eq. (10.74) for HX and Eq. (10.73) for TX.

## 10.7.2 SX and PX

## General description:

For a general description of all DeltaEC heat exchangers, see the initial paragraphs of the heat-exchanger documentation, Section 10.7.

In SX, the thermoacoustic working gas flows through a pile of woven screens. The PX segment allows the user to specify heat-exchanger parameters for which the steady-flow friction factor and heat transfer coeficient are known power laws in Reynolds number. The SX calculations assume fairly good thermal contact between gas and solid, so these calculations are valid only for hydraulic radius smaller than thermal and viscous penetration depths. There is no warning if this condition is not met.

Heat $\dot { Q }$ is positive when it flows from the solid into the thermoacoustic gas, adding to $\dot { H } _ { \mathrm { t o t } }$ . In SX, typically the screen material has high thermal conductivity and the area is small, because typically the heat must flow radially through the screen wires, from the pressure vessel around the screens to the thermoacoustic gas.

The temperature diference between the solid temperature $T _ { \mathrm { s o l i d } }$ and the gas temperature $T _ { m }$ is proportional to $\dot { Q }$ . The proportionality constant is not well supported, either theoretically or experimentally; we find that it seems to be accurate within a factor of 2.

SX and PX are assumed to be so short that the numerical integration from one end to the other is performed with a single fourth-order Runge-Kutta step. (Most other integrated segments, i.e., DUCT, CONE, MIX\*\*, STK\*\*, and VX\*\*, are integrated with Nint fourth-order Runge-Kutta steps.)

## Input variables, SX:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

VolPor The volumetric porosity $\phi .$ This is the ratio of the volume of gas in the SX to the total volume of the heat exchanger. For plain square-weave screen with m wires per unit length and wire diameter $d _ { \mathrm { w i r e } }$ , we sometimes use

$$
\phi \simeq 1 - \frac { \pi m d _ { \mathrm { w i r e } } } { 4 } ,\tag{10.123}
$$

as recommended by Organ [27], or we weigh the pile of screens, measure its overall dimensions $A$ and $\Delta x$ , and use the known density of its wire material to calculate $\phi .$

Length (m) The length $\Delta x$ of the heat exchanger.

rh (m) The hydraulic radius $r _ { h }$ of the SX. This is the ratio of the gas volume to the gas–solid contact area. For plain square-weave screen with wire diameter $d _ { \mathrm { w i r e } }$ , we sometimes use

$$
r _ { h } \simeq d _ { \mathrm { w i r e } } \frac { \phi } { 4 ( 1 - \phi ) } ,\tag{10.124}
$$

as recommended by Organ [27].

HeatIn The heat $\dot { Q }$ added to the thermoacoustic gas in the heat exchanger. Positive $\dot { Q }$ indicates heat flow from solid to gas.

Solid The solid material of the wires. This is used only in the calculation of $\epsilon _ { s } .$ which seldom difers significantly from its value for a solid with infinite conductivity and specific heat in SXs.

## Input variables, PX:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } }$

VolPor The volumetric porosity $\phi .$ . This is the ratio of the volume of gas in the heat exchanger to the total volume of the heat exchanger.

Length (m) The length $\Delta x$ of the heat exchanger.

rh (m) The hydraulic radius $r _ { h }$ of the heat exchanger. This is the ratio of the gas volume to the gas–solid contact area.

HeatIn The heat $\dot { Q }$ added to the thermoacoustic gas in the heat exchanger. Positive $\dot { Q }$ indicates heat flow from solid to gas.

f con The friction-factor parameter $f _ { \mathrm { c o n } }$ in the equations below.

f exp The friction-factor parameter $f _ { \mathrm { e x p } }$ in the equations below.

h con The heat-transfer parameter $h _ { \mathrm { c o n } }$ in the equations below.

h exp The heat-transfer parameter $h _ { \mathrm { e x p } }$ in the equations below.

Solid The solid with which the PX is made. This is used only in the calculation of $\epsilon _ { s } .$ , which seldom difers significantly from its value for a solid with infinite conductivity and specific heat in heat exchangers.

## Potential targets:

TSolid If used as a target, DeltaEC’s shooting method compares $T _ { \mathrm { s o l i d } }$ to this value.

## Master–slave links:

The length of either of these segments can be slaved to the length of another segment to keep the sum of the two lengths constant.

(For an introduction to master–slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

SX Hot heat exchanger   
1.029E-03 a Area m^2 total cross sectional area   
0.690 b VolPor volumetric porosity   
2.000E-02 c Length m   
6.450E-05 d rh m hydraulic radius   
-284. e HeatIn W   
300. f Est-T K (t)   
copper Solid type   
PX   
1.0E-4 a Area m^2 total cross-sectional area   
0.70 b GasA/A volumetric porosity   
0.04 c Length m   
4.000E-05 d rh m hydraulic radius = gas volume / gas-solid contact area   
900. e HeatIn W   
0.07 f f\_con   
0.22 g f\_exp   
0.035 h h\_con   
0.22 i h\_exp   
copper Solid type

![[mu_66afccee_da3ce61312d880e316a8.jpg]]  
Examples of SX occur throughout Sections 5.8 and 6.3.

## Calculations:

In SX, dp /dx and $d \left. u _ { 1 } \right.$ /dx are calculated in the same way as in STKSCREEN, as described in [55]. Note that Eqs. (10.127) and (10.128 are fits [55] to data only over the limited range $0 . 6 0 < \phi < 0 . 7 7$ . Outside of this narrow range, a look at the original literature is advised, and PX might be a better choice.

$$
\frac { d p _ { 1 } } { d x } = - i \omega \rho _ { m } \left[ 1 + \frac { ( 1 - \phi ) ^ { 2 } } { 2 ( 2 \phi - 1 ) } \right] \langle u _ { 1 } \rangle - \frac { \mu } { r _ { h } ^ { 2 } } \left( \frac { c _ { 1 } ( \phi ) } { 8 } + \frac { c _ { 2 } ( \phi ) N _ { R , 1 } } { 3 \pi } \right) \langle u _ { 1 } \rangle ,\tag{10.125}
$$

$$
\frac { d \left. u _ { 1 } \right. } { d x } = - \frac { i \omega \gamma } { \rho _ { m } a ^ { 2 } } p _ { 1 } + \frac { i \omega T _ { m } \beta ^ { 2 } } { \rho _ { m } c _ { p } } \frac { \epsilon _ { s } + ( g _ { c } + e ^ { 2 i \theta _ { p } } g _ { v } ) \epsilon _ { h } } { 1 + \epsilon _ { s } + ( g _ { c } + e ^ { 2 i \theta _ { T } } g _ { v } ) \epsilon _ { h } } p _ { 1 } ,\tag{10.126}
$$

using

$$
c _ { 1 } ( \phi ) = 1 2 6 8 - 3 5 4 5 \phi + 2 5 4 4 \phi ^ { 2 } , \quad c _ { 2 } ( \phi ) = - 2 . 8 2 + 1 0 . 7 \phi - 8 . 6 \phi ^ { 2 } ,\tag{10.127}
$$

$$
b ( \phi ) = 3 . 8 1 - 1 1 . 2 9 \phi + 9 . 4 7 \phi ^ { 2 } ,\tag{10.128}
$$

$$
\begin{array} { r } { N _ { R , 1 } = 4 \left| \langle u _ { 1 } \rangle \right| r _ { h } \rho _ { m } / \mu , } \end{array}\tag{10.129}
$$

$$
\epsilon _ { s } = \phi \rho _ { m } c _ { p } / ( 1 - \phi ) \rho _ { s } c _ { s } , \quad \epsilon _ { h } = 8 i r _ { h } ^ { 2 } / b ( \phi ) \sigma ^ { 1 / 3 } \delta _ { \kappa } ^ { 2 } ,\tag{10.130}
$$

$$
\delta _ { \kappa } ^ { 2 } = 2 k / \omega \rho _ { m } c _ { p } ,\tag{10.131}
$$

$$
\theta _ { p } = \mathrm { p h a s e } ( \langle u _ { 1 } \rangle ) - \mathrm { p h a s e } \left( p _ { 1 } \right) , \quad \theta _ { T } = \mathrm { p h a s e } ( \langle u _ { 1 } \rangle ) - \mathrm { p h a s e } \left( \langle T \rangle _ { u , 1 } \right) ,\tag{10.132}
$$

$$
g _ { c } = \displaystyle \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \displaystyle \frac { d z } { 1 + N _ { R , 1 } ^ { 3 / 5 } \cos ^ { 3 / 5 } ( z ) } , \quad g _ { v } = - \displaystyle \frac { 2 } { \pi } \displaystyle \int _ { 0 } ^ { \pi / 2 } \displaystyle \frac { \cos ( 2 z ) d z } { 1 + N _ { R , 1 } ^ { 3 / 5 } \cos ^ { 3 / 5 } ( z ) } .\tag{10.133}
$$

The spatial average oscillatory velocity $\left. u _ { 1 } \right. = \left. U _ { 1 } \right. / \phi A$ , where $\phi$ is volumetric porosity and A is heat-exchanger cross-sectional area. These expressions were derived with the assumption that the thermal and viscous penetration depths are much larger than $r _ { h }$

For both SX and PX, see Section 14.3 for the details of DeltaEC’s implementation of the mathematics in Ref. [55], whose equation for $\left. T _ { 1 } \right.$ (which appears in Eq. (10.126) through $e ^ { 2 i \theta _ { T } } )$ must be solved iteratively.

The PX segment can be used when the steady-flow friction factor and heat-transfer coeficient are known power laws in Reynolds number $N _ { R }$ . The derivation assumes fairly good thermal contact between gas and solid. Area $A$ is the total cross-sectional area of the heat exchanger, VolPor $\phi$ is its volumetric porosity, and $\Delta x$ is its length, so $\phi A \ : \Delta x$ is the total volume of gas in the heat exchanger. The steady-state friction factor and heat-transfer coeficients must be known by the user in power-law forms:

$$
f = f _ { \mathrm { c o n } } \left( N _ { R } \right) ^ { - f _ { \mathrm { e x p } } } ,\tag{10.134}
$$

$$
N _ { S t } \sigma ^ { 2 / 3 } = h _ { \mathrm { c o n } } ( N _ { R } ) ^ { - h _ { \mathrm { e x p } } } ,\tag{10.135}
$$

where $N _ { S t } = N _ { N u } / \sigma N _ { R }$ is the Stanton number, and the Reynolds number $N _ { R }$ is defined in the usual way as

$$
N _ { R } = \frac { 4 U r _ { h } \rho _ { m } } { \phi A \mu } = \frac { 4 \left. u \right. r _ { h } \rho _ { m } } { \mu } .\tag{10.136}
$$

Note: this is Fanning friction factor, the friction factor used by Kays and London, so instantaneously

$$
\frac { d p } { d x } = \frac { f } { r _ { h } } \frac { 1 } { 2 } \rho \left. u \right. ^ { 2 } = \frac { \mu } { 8 r _ { h } ^ { 2 } } f N _ { R } \left. u \right. .\tag{10.137}
$$

The complex pressure gradient is computed using

$$
\frac { d p _ { 1 } } { d x } = - i \omega \rho _ { m } ~ \langle u _ { 1 } \rangle - I _ { f } \frac { \mu } { 8 r _ { h } ^ { 2 } } f _ { \mathrm { c o n } } ~ | N _ { R , 1 } | ^ { 1 - f _ { \mathrm { e x p } } } \langle u _ { 1 } \rangle\tag{10.138}
$$

where

$$
I _ { f } = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } \sin ^ { 3 - f _ { \mathrm { e x p } } } \omega t d ( \omega t ) .\tag{10.139}
$$

Thermal-relaxation efects due to oscillating pressure are computed using the same equations for d $\left. u _ { 1 } \right. / d x$ as for screen heat exchangers but with

$$
g _ { c } ~ = ~ | N _ { R , 1 } | ^ { h _ { \mathrm { e x p } } - 1 } \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \cos ^ { h _ { \mathrm { e x p } } - 1 } \omega t d ( \omega t ) ,\tag{10.140}
$$

$$
g _ { v } ~ = ~ - \vert N _ { R , 1 } \vert ^ { h _ { \mathrm { e x p } } - 1 } \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \cos { 2 \omega t } \cos ^ { h _ { \mathrm { e x p } } - 1 } \omega t d ( \omega t ) ,\tag{10.141}
$$

$$
\begin{array} { c c l } { { b ( \phi ) } } & { { = } } & { { h _ { \mathrm { c o n } } . } } \end{array}\tag{10.142}
$$

The solid temperature is computed relative to the gas mean temperature using

$$
\Delta T = I _ { h } \frac { \dot { Q } } { k h _ { \mathrm { c o n } } \left| N _ { R , 1 } \right| ^ { 1 - h _ { \mathrm { e x p } } } } \frac { r _ { h } ^ { 2 } } { \phi A x _ { \mathrm { e f f } } } ,\tag{10.143}
$$

where $x _ { \mathrm { e f f } } = \mathrm { m i n } \{ 2 \left| \left. u _ { 1 } \right. \right| / \omega , \ \Delta x \} , \ N _ { R , 1 }$ is the Reynolds number amplitude (based on the amplitude of the velocity), and

$$
{ \cal I } _ { h } = \frac { 4 } { \pi } \int _ { 0 } ^ { \pi / 2 } \cos ^ { h _ { \mathrm { e x p } } + 1 } \omega t d ( \omega t ) = \frac { h _ { \mathrm { e x p } } } { h _ { \mathrm { e x p } } + 1 } \frac { 4 } { \pi } \int _ { 0 } ^ { \pi / 2 } \cos ^ { h _ { \mathrm { e x p } } - 1 } \omega t d ( \omega t ) .\tag{10.144}
$$

(The second form of $I _ { h }$ , obtained from the first via integration by parts, expresses $I _ { h }$ in terms of $g _ { c } \ \mathrm { a b o v e . } )$ To maintain DeltaEC’s high speed, the trigonometric integrals are not evaluated by DeltaEC; we use simple functional fits to these integrals in DeltaEC.

The head-loss pressure gradient $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ in SX is calculated in the same way as for STKSCREENs. The nonlinear nature of the screen friction factor $f = c _ { 1 } ( \phi ) / N _ { R } + c _ { 2 } ( \phi )$ also causes the mean flow to afect $d p _ { 1 } / d x$ in SX, according to

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { \mu U _ { 1 } } { 8 r _ { h } ^ { 2 } \phi A } \left[ c _ { 1 } ( \phi ) + 2 c _ { 2 } ( \phi ) N _ { R , 2 , 0 } \right] , | \varepsilon _ { 2 , 0 } | \ge 1 , } \\ & & { = } & { \displaystyle - \frac { \mu U _ { 1 } } { r _ { h } ^ { 2 } \phi A } \left\{ \frac { c _ { 1 } ( \phi ) } { 8 } + \frac { c _ { 2 } ( \phi ) N _ { R , 1 } } { 3 \pi } \left[ \left( 1 + \frac { \varepsilon _ { 2 , 0 } ^ { 2 } } { 2 } \right) \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { 3 } { 2 } \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } \right] \right\} , } \end{array}\tag{.145}
$$

(10.146)

where the acoustic Reynolds-number amplitude is

$$
N _ { R , 1 } = \frac { | U _ { 1 } | 4 r _ { h } \rho _ { m } } { \phi A \mu } .\tag{10.147}
$$

[Note $N _ { R , 2 , 0 }$ in Eq. (10.145) but $N _ { R , 1 }$ in Eq. (10.146) — not a typographical error.] We did not incorporate a mean flow efect on $d p _ { 1 } / d x$ in STKSCREEN because the energy equation restricts the magnitude of $\dot { N }$ in stacks. No such restriction exists in heat exchangers.

In PX, $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ is calculated just as in STKPOWERLW. The mean flow afects $d p _ { 1 } / d x$ in

PX according to

$$
\begin{array} { r l } & { \frac { d p _ { 1 } } { d x } = - i \omega \rho _ { m }  u _ { 1 }  } \\ & { \quad - \frac { \rho _ { m }   u _ { 1 }    u _ { 1 }  } { 4 r _ { h } } [  \varepsilon _ { 2 , 0 }  f _ { M , \mathrm { m a x } } + \frac { ( 3 - 2  \varepsilon _ { 2 , 0 }  ) ( 1 - 2  \varepsilon _ { 2 , 0 }  ) } { 8 ( 1 +  \varepsilon _ { 2 , 0 }  ) } \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } ] ,  \varepsilon _ { 2 , 0 }  \geq 1 , } \\ & { \qquad ( 1 0 . 1  } \\ & { \quad  = - i \omega \rho _ { m }  u _ { 1 }  - \frac { \rho _ { m }   u _ { 1 }    u _ { 1 }  } { 3 \pi r _ { h } } \{ [ ( 1 + \frac { \varepsilon _ { 2 , 0 } ^ { 2 } } { 2 } ) \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { 3 } { 2 } \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } ] f _ { M , \mathrm { m a x } }   } \\ & { \quad   - [ ( 1 + \frac { \varepsilon _ { 2 , 0 } ^ { 2 } } { 2 } ) \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { 3 } { 2 } \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } - \frac { 9 \pi } { 3 2 } \frac { 1 + 4 \varepsilon _ { 2 , 0 } ^ { 2 } } { 1 +  \varepsilon _ { 2 , 0 }  } ] \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } \} ,  \varepsilon _ { 2 , 0 }  \leq 1 . } \end{array}\tag{48}
$$

(10.149)

which is a hybrid of Eq. (10.138) here and Eqs. (A13) and (A14) in Ref. [42].

For $\dot { N } = 0$ , temperature and power change according to

$$
\frac { d T _ { m } } { d x } = 0 ,\tag{10.150}
$$

$$
\frac { d \dot { H } _ { \mathrm { t o t } } } { d x } ~ = ~ \frac { \dot { Q } } { \Delta x } ,\tag{10.151}
$$

where $\Delta x$ is the heat exchanger length and $\dot { Q }$ is the heat added to the heat exchanger. Positive heat $\dot { Q }$ (parameter $^ { \circ } \Theta ^ { \prime \prime } )$ flows into the apparatus. The heat flow $\dot { Q }$ is an input for each pass of DeltaEC, and it is often used as a guess for the shooting method described in Section 2.5.

For $\dot { N } \neq 0$ , the wave and energy calculations are unchanged, so all of the heat goes into $\dot { H } _ { 2 , k }$ and none into the steady flow. This seems fine for weak steady flows, such as weak Gedeon streaming when a TASHE is operated slightly away from the conditions at which its gas diode enforces $\dot { N } = 0$ . For strong steady flow, the user can override the built-in calculations with an RPN such as

13 RPN Fix Tm. Inp = frac of heat that should go to mean flow   
0.25   
H2k inp 12e \* - =H2k ; inp 12e \* Ndot / m / cp / Tm + =Tm

following the heat exchanger, where 12e is the heat in the upstream heat exchanger and 13a is the steady-flow heat fraction. That fraction is often guessed, to give DeltaEC enough flexibility to meet nearby temperature and energy boundary conditions. Alternatively, the fraction can also be set equal to a simple expression like $\left( 1 + \rho _ { m } | U _ { 1 } | / | \dot { N } | m \right)$ −1 in an RPN, supplying an experimentally unsupported but plausible estimate of how power divides itself between the steady flow and the acoustic flow.

In SXs and PXs, the spatial average of the complex oscillating temperature amplitude is calculated in the same way as in STKSCREEN and STXPOWERLW, respectively, with $d T _ { m } / d x = 0$

In SXs, the solid temperature is computed relative to gas mean temperature using

$$
\Delta T = \frac { \dot { Q } } { k } \frac { r _ { h } ^ { 2 } ( g _ { c } - g _ { v } ) } { b ( \phi ) \phi A x _ { \mathrm { e f f } } }\tag{10.152}
$$

where $x _ { \mathrm { { e f f } } } = \mathrm { { m i n } \{ 2 | \langle \xi _ { 1 } \rangle | , \Delta x \} }$ . In PXs, the solid temperature is computed relative to the gas mean temperature using

$$
\Delta T = I _ { h } \frac { \dot { Q } } { k h _ { \mathrm { c o n } } N _ { R , 1 } ^ { 1 - h _ { \mathrm { e x p } } } } \frac { r _ { h } ^ { 2 } } { \phi A x _ { \mathrm { e f f } } } ,\tag{10.153}
$$

where $x _ { \mathrm { e f f } } = \operatorname* { m i n } \{ 2 \left| \langle \xi _ { 1 } \rangle \right| , \Delta x \} , N _ { R , 1 }$ is the Reynolds number based on the amplitude of the velocity, and $I _ { h }$ is defined above. Then

$$
\begin{array} { r } { T _ { \mathrm { s o l i d ~ \delta } } = \displaystyle \operatorname* { m a x } \left[ T _ { m } ( 0 ) , T _ { m } ( \Delta x ) \right] + \Delta T \qquad \mathrm { i f } \ \dot { Q } > 0 , } \end{array}\tag{10.154}
$$

$$
\begin{array} { r l r } { \mathrm { ~  ~ \omega ~ } } & { { } = } & { \operatorname* { m i n } \left[ T _ { m } ( 0 ) , T _ { m } ( \Delta x ) \right] + \Delta T \qquad \mathrm { i f } \ \dot { Q } < 0 , } \end{array}\tag{10.155}
$$

These expressions may be very inaccurate, but we believe they are more useful than nothing. The user who mistrusts them can use the gas temperature (available as an output in the adjacent stack segment, and through RPN) instead of the solid temperature for plotting or targeting, and/or use RPNs to construct customized expressions for Eqs. (10.152)–(10.155).

## 10.7.3 VXQ1, VXQ2, VXT1, and VXT2

## General description:

For a general description of all DeltaEC heat exchangers, see the initial paragraphs of the heat-exchanger documentation, Section 10.7.

The “variable” heat exchanger segments VXT1, VXT2, VXQ1, and VXQ2 allow gas temperature $T _ { m }$ and/or heat flux per unit length $\dot { q }$ to vary with x. The two VXQ\* segments further allow $T _ { \mathrm { s o l i d } }$ to depend on x. Hence, these segments combine some features of previous heatexchanger segments with some features of previous stack segments.

The third character in the segment name, T or Q, determines which of two extreme, limiting heat-transfer conditions is assumed for the non-thermoacoustic side of the heat exchanger. In VXT\*, $T _ { \mathrm { s o l i d } }$ is independent of x. Thinking of a shell-and-tube heat exchanger in which the thermoacoustic processes take place inside the tubes while a heat-transfer liquid passes through the shell, the idea is that VXT\* should be used when the shell-side flow has such a high heat-transfer coeficient (e.g., vigorous flow of water) that the solid surfaces of the heat exchanger tubes are fixed in temperature, independent of x. In VXQ\*, the heat flux delivered to/from the heat exchanger per unit length is independent of x. In the shell-and-tube situation, the idea is that VXQ\* should be used when the shell-side gas is weakly coupled to the solid (e.g., combustion products at low Reynolds number) so the temperature diference between the shell-side gas and the solid surface can be much larger than any changes in temperature along the solid surface. To decide which case is most appropriate for individual circumstances, use a standard heat-transfer book to estimate the heat-transfer coeficients on the shell side and on the thermoacoustic side. If the heat transfer is much better on the shell side, use VXT\*. If the heat transfer is much better on the thermoacoustic side, use VXQ\*.

The fourth character in the segment name, 1 or 2, allows the segment to be formed of 1 or 2 separate heat-transfer pieces along x (in addition to the two “tubesheets” at either

louse @ (0.0262, 929.8969)

![[mu_66afccee_525ce440e3a6deda2b5f.jpg]]

![[mu_66afccee_df06388ee52d1ea68f67.jpg]]  
Figure 10.6: Example results from VXT1, STKSCREEN, VXQ1 segments in series in a Stirling engine. The VXT1 extends from $x = 0$ to $x = 0 . 0 5$ m, with tubesheets 0.005 m long at each end. The STKSCREEN extends from $x = 0 . 0 5$ m to $x = 0 . 1 0$ m. The VXQ2 extends from $x = 0 . 1 0$ m to $x = 0 . 2 4$ m, with tubesheets 0.02 m long on each end. Temperatures in upper panel. The gas temperature (solid line) varies with x in all three segments. The solid temperature (dashed line) does not vary with x in the VXT1 segment. Lower panel shows $\dot { H } _ { \mathrm { t o t } }$ (solid line) and $\dot { E }$ (dashed line).

![[mu_66afccee_3939bc2bea890f926786.jpg]]  
Figure 10.7: Two perpendicular cross sections through a VXT2, sandwiched between a duct above and a regenerator below. Thermoacoustic oscillations in the vertical direction pass through the insides of 33 tubes, of which 7 are exposed in the cross section in the lower part of this figure. Cooling water passes through the “shell” in two passes: rightward across the lower half, and then leftward across the upper half.

![[mu_66afccee_cd296d3fbdd9c6d88cb4.jpg]]  
Figure 10.8: Schematic of a short section of a VX\*\* segment. The solid lines show the edges of the solid and the gas. The dashed box is the short control volume, dx long, used to write the conservation laws for this situation. The space above the solid represents the external heat-transfer gas such as water or combustion gases, which transfer heat at rate $d \dot { Q }$ to the control volume.

end). Thus, $" 2 '$ is intended for heat exchangers with two “passes” on the shell side. Figure 10.7 shows some of the geometry parameters for a VXT2 (or VXQ2).

To understand the philosophy behind the VX\*\* calculations, consider Fig. 10.8, which shows a length dx of this segment. In contrast with the STK\*\* segments, where the mean temperature of the solid is assumed to be the same as the mean temperature of the gas, here those time-mean temperatures can be diferent, so large time-averaged heat flows can be driven from one to the other. Let $T _ { m } ( x )$ be the mean temperature of the gas and $T _ { \mathrm { s o l i d } } ( x )$ be the mean temperature of the solid. Both may be functions of x. Artificially, assume that $T _ { m }$ in the gas is independent of the coordinate perpendicular to x. This is equivalent to assuming that the heat-transfer bottleneck for the time-averaged heat transfer occurs in a thin layer adjacent to the surface.

## Input variables, VXQ1 and VXQ2:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } } + A _ { \mathrm { s h e l l - s i d e } } .$

GasA/A The fraction of the total area that is available to gas, $A _ { \tt g a s } / A$

SolA/A The fraction of the total area occupied by solid that contributes to solid thermal conduction in the x direction, $A _ { \mathrm { s o l i d } } / A$

rh (m) The hydraulic radius $r _ { h }$ of the gas channels. Hydraulic radius is defined as the ratio of the gas volume to the gas–solid contact area. For the present case of an xindependent channel cross section, $r _ { h } = A _ { \mathrm { g a s } } / \Pi$ where Π is the inside perimeter of the channel.

LenTS1 (m) The length of the first tubesheet in the heat exchanger. This region experiences viscous and thermal-hysteresis loss, but not time-averaged heat transfer.

Len P1 (m) The length of the heat-transfer region in VXQ1; the length of the first of two heat-transfer regions in VXQ2.

Len P2 (m) The length of the second heat-transfer region in VXQ2. (Not present in VXQ1.)

LenTS2 (m) The length of the second tubesheet in the heat exchanger. This region experiences viscous and thermal-hysteresis loss, but not time-averaged heat transfer.

HeatP1 The heat added to the thermoacoustic gas in VXQ1. The heat added to the thermoacoustic gas in the first heat-transfer region in VXQ2. Positive heat indicates heat flow from solid to gas.

HeatP2 The heat added to the thermoacoustic gas in the second heat-transfer region in VXQ2. (Not present in VXQ1.) Positive heat indicates heat flow from solid to gas.

FracQN If “Enable Ndot” is checked in an upstream BEGIN, this variable, $F _ { \dot { Q } \dot { N } }$ , determines what fraction of heat is added to $\dot { H } _ { \dot { N } } = \dot { N } m w _ { m }$ . (The remainder is added to $\dot { H } _ { 2 , k } . )$ In VXQ2, the same value of $F _ { \dot { Q } \dot { N } }$ is applied to both passes.

Solid The solid material in the heat exchanger.

## Input variables, VXT1 and VXT2:

Area $( \mathrm { m } ^ { 2 } )$ The total cross-sectional area $A = A _ { \mathrm { g a s } } + A _ { \mathrm { s o l i d } } + A _ { \mathrm { s h e l l - s i d e } } .$

GasA/A The fraction of the total area that is available to gas, $A _ { \mathrm { g a s } } / A$

SolA/A The fraction of the total area occupied by solid that contributes to solid thermal conduction in the x direction, $A _ { \mathrm { s o l i d } } / A$

rh (m) The hydraulic radius $r _ { h }$ of the gas channels. Hydraulic radius is defined as the ratio of the gas volume to the gas–solid contact area. For the present case of an xindependent channel cross section, $r _ { h } = A _ { \mathrm { g a s } } / \Pi$ where Π is the inside perimeter of the channel.

LenTS1 (m) The length of the first tubesheet in the heat exchanger. This region experiences viscous and thermal-hysteresis loss, but not time-averaged heat transfer.

Len P1 (m) The length of the heat-transfer region in VXT1; the length of the first of two heat-transfer regions in VXT2.

Len P2 (m) The length of the second heat-transfer region in VXT2. (Not present in VXT1.)

LenTS2 (m) The length of the second tubesheet in the heat exchanger. This region experiences viscous and thermal-hysteresis loss, but not time-averaged heat transfer.

TSolP1 The solid temperature in the heat-transfer region in VXT1. The solid temperature in the first heat-transfer region in VXT2.

TSolP2 The solid temperature in the second heat-transfer region in VXT2. (Not present in VXT1.)

FracQN If “Enable Ndot” is chekced in an upstream BEGIN, this variable, $F _ { \dot { Q } \dot { N } }$ , determines what fraction of heat is added to $\dot { H } _ { \dot { N } } = \dot { N } m w _ { m }$ . (The remainder is added to $\dot { H } _ { 2 , k } . )$ In VXT2, the same value of $F _ { \dot { Q } \dot { N } }$ is applied to both passes.

Solid The solid material in the heat exchanger.

## Potential targets:

HeatP1 or HeatP2 If used as a target in VXT1 or VXT2, DeltaEC’s shooting method compares its calculated total heat for the corresponding heat-transfer region to this value.

There are no built-in potential targets in VXQ1 and VXQ2. Use RPN targets as needed.

## Master–slave links:

None.

## Format and examples:

VXT2 compare to segment 13   
sameas 13a a Area m^2 1.9116 A |p| Pa   
sameas 13b b GasA/A -0.1565 B Ph(p) deg   
sameas 13c c SolA/A 9.9874E-07 C |U| m^3/s   
sameas 13d d rh m 90.003 D Ph(U) deg   
sameas 13e e LenTS1 m 7.0105 E Htot W   
sameas 13f f Len P1 m -2.6557E-09 F Edot W   
sameas 13g g Len P2 m 1.0009 G HeatP1 W   
sameas 13h h LenTS2 m 5.0097 H HeatP2 W   
0.00 i HeatP1 W (t) 1605.5 I qmaxP1 W/m^2   
0.00 j HeatP2 W (t) 8034.8 J qmaxP2 W/m^2   
321.70 k TSolP1 K 0.0000 K H2k W   
408.00 l TSolP2 K   
1.0000 m FracQN   
stainless Solid type  
Section 6.4 gives an example of the use of VXQ1.

## Calculations for $\dot { N } = 0 \colon$

The first-order continuity and momentum equations are taken to be unchanged by the timeaveraged heat transfer. Hence, $p _ { 1 }$ and $U _ { 1 }$ evolve according to

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A _ { \mathrm { g a s } } } U _ { 1 } , } \\ { \displaystyle \frac { d U _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \beta ( f _ { \kappa } - f _ { \nu } ) } { ( 1 - f _ { \nu } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 } , } \end{array}\tag{10.156}
$$

(10.157)

in all four VX\*\* segments, just the same as in laminar stacks. Also the same as in laminar stacks is the calculation of the lateral spatial average of complex temperature amplitude,

$$
\left. T _ { 1 } \right. = \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } p _ { 1 } \left[ 1 - \frac { f _ { \kappa } } { 1 + \epsilon _ { s } } \right] - \frac { U _ { 1 } } { i \omega A _ { \mathrm { g a s } } \left( 1 - \sigma \right) \left( 1 - f _ { \nu } \right) } \frac { d T _ { m } } { d x } \left[ 1 - \frac { f _ { \kappa } + \epsilon _ { s } f _ { \nu } } { 1 + \epsilon _ { s } } - \sigma \left( 1 - f _ { \nu } \right) \right] .\tag{10.158}
$$

However, the energy equation used in stacks does not sufice here: $\dot { H } _ { \mathrm { 2 } , k , \mathrm { g a s } }$ and $\dot { H } _ { \mathrm { s o l i d } }$ should be considered separately instead of only considering their sum $\dot { H } _ { 2 , k }$ , and the gas mean temperature $T _ { m }$ and solid temperature $T _ { \mathrm { s o l i d } }$ might sometimes evolve separately with x. So, here there are four equations related to energy flux and energy conservation:

$$
\begin{array} { r l } { \tilde { H } _ { \mathcal { I } , k } } & { = \frac { 1 } { 2 } \mathrm { R e } [ \mathcal { P } _ { i } \tilde { V } _ { i } ] ^ { * } ( 1 - \frac { T _ { m } \beta ( f _ { \varepsilon } - \tilde { f } _ { \varepsilon } ) } { ( 1 + \varepsilon _ { \varepsilon } ) ( 1 - \sigma ) } ) ] } \\ & { \quad + \frac { \beta T _ { m } c _ { 0 } | | \bar { H } | ^ { 2 } } { 2 \mathrm { d } A _ { \mathcal { I } , \alpha } ( 1 - \sigma ) | 1 - f _ { \varepsilon } | | ^ { 2 } } \frac { d T _ { m } } { d x } \mathrm { I m } [ \tilde { f } _ { \varepsilon } \cdot \frac { ( \tilde { f } _ { \varepsilon } - \tilde { f } _ { \varepsilon } ) ( 1 + \varepsilon _ { \varepsilon } \tilde { f } _ { \varepsilon } / f _ { \varepsilon } ) } { ( 1 + \varepsilon _ { \varepsilon } ) ( 1 + \sigma ) } ] } \\ & { \quad - A _ { \mathcal { I } , \alpha } k \frac { \bar { H } T _ { m } } { d x } + \tilde { H } _ { \mathcal { I } , \alpha } + } \\ { \tilde { H } _ { \mathcal { I } , \alpha | \mathrm { d } } } & { = - A _ { \mathcal { I } , \beta | \mathcal { I } } k \frac { \bar { H } \mathrm { e n d } } { d x } , } \\ { \tilde { q } ( x ) } & { = \frac { d \tilde { H } _ { \mathcal { I } , k } } { d x } , } \\ { \tilde { q } ( x ) } & { = \frac { d \tilde { H } _ { \mathcal { I } , k 0 } } { d x } + \frac { A _ { \mathcal { I } , \beta | \mathcal { I } , k 0 } } { 4 f _ { \varepsilon } ^ { 2 } } N _ { \mathcal { I } } ( T _ { \mathrm { s a b d } } - T _ { m } ) , } \end{array}\tag{10.159}
$$

(10.160)

(10.161)

(10.162)

where $\dot { q }$ is the heat per unit length externally delivered to the heat exchanger (if negative, it’s the heat removed).

The first of these four equations describes the total energy transport in the x direction, and the second describes the energy transport (via heat conduction) in the x direction in the solid.

The third equation expresses conservation of energy for the dashed-line control volume in Fig. 10.8, showing that the heat input $d { \dot { Q } } = { \dot { q } } ( x )$ dx equals the diference $( d \dot { H } _ { 2 , k } / d x )$ dx between energy transport in and out along x.

The fourth equation similarly expresses conservation of energy for the solid separately within the control volume.

Equations (10.159)–(10.162) are used to obtain the evolution of the temperatures $T _ { m } ( x )$ and $T _ { \mathrm { s o l i d } } ( x )$ , and the energy flows $\dot { H } _ { 2 } ( x ) , \dot { H } _ { \mathrm { s o l i d } } ( x )$ , and ${ \dot { q } } ( x )$ , as functions of $x _ { i }$ , simultaneously with the use of Eqs. (10.156) and (10.157) to obtain $p _ { 1 } ( x )$ and $U _ { 1 } ( x )$

Some details are diferent in VXT\* segments and VXQ\* segments:

In the VXT\* segments, $T _ { \mathrm { s o l i d } }$ is independent of x and is a user’s input. Then $\dot { H } _ { \mathrm { s o l i d } } = 0$ Eq. (10.159) is solved for $d T _ { m } / d x$ to yield the evolution of $T _ { m } ( x )$ , Eqs. (10.161) and (10.162) together yield $d \dot { H } _ { 2 , k } / d x$ , and Eq. (10.161) yields $\dot { q } ( x ) = d \dot { H } _ { 2 , k } / d x$ . The heat transfer per unit length ${ \dot { q } } ( x )$ is integrated with respect to x to obtain the total heat transfer rate $\dot { Q }$ . (In VXT2, the two “passes” can have diferent values of $T _ { \mathrm { s o l i d } } . )$ Thus, Eqs. (10.156)–(10.162) are regarded as first-order diferential equations for $d p _ { 1 } / d x , d U _ { 1 } / d x , d T _ { m } / d x$ , and $d \dot { H } _ { 2 , k } / d x$ (and

${ \dot { q } } ( x )$ is obtained trivially from $d \dot { H } _ { 2 , k } / d x )$

(10.163)

$$
\begin{array} { r l } { \frac { d T _ { m } } { d x } = } & { \frac { \tilde { H } _ { 2 , k } - \frac { 1 } { 2 } \mathrm { R e } [ p _ { 1 } \tilde { U } _ { 1 } ( 1 - \frac { \eta _ { m } g ( \tilde { t } _ { e } - \tilde { t } _ { o } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \epsilon _ { s } ) } ) ] } { \frac { \beta _ { \mathrm { o u t } } ( 1 - \epsilon _ { 1 } ) ! ^ { 2 } } { 2 \tilde { u } _ { s o } ( 1 - \epsilon _ { 1 } ) ( 1 - f _ { 1 } ) ^ { 2 } } \mathrm { I m } [ \tilde { f } _ { s } + \frac { ( f _ { m } - \tilde { t } _ { o } ) ( 1 + \epsilon _ { s } / f _ { 1 } f _ { m } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \epsilon _ { s } ) } ] - A _ { \mathrm { g u t } } k } , } \\ { \frac { d \tilde { p } _ { 1 } } { d x } = } & { - \frac { i \omega \rho _ { m } } { ( 1 - f _ { 1 } ) A _ { \mathrm { g a } } } U _ { 1 , } , } \\ { \frac { d \tilde { U } _ { 1 } } { d x } = } & { - \frac { i \omega A _ { \mathrm { g a } } } { \rho _ { m } a ^ { 2 } } ( 1 + \frac { ( \gamma - 1 ) f _ { n } } { 1 + \epsilon _ { s } } ) p _ { 1 } + \frac { \beta ( f _ { n } - f _ { n } ) } { ( 1 - f _ { e } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 , } } \\ & { \mathrm { w i t h } \frac { d \tilde { U } _ { m } } { d x } \mathrm { g i v e n ~ b y ~ E q . ~ ( 1 0 . 1 6 3 ) , } } \\ { \frac { d \tilde { H } _ { 2 , k } } { d x } = } &  \frac { A _ { \mathrm { g a } } k } { 4 \eta _ { k } ^ { 2 } } \mathfrak { 3 } . 7 m _ { k } ( \mathcal { T } _  \mathrm  s a \end{array}\tag{10.164}
$$

(10.165)

(10.166)

The factor $" 3 . 7 "$ in Eq. (10.166) is the laminar, isothermal-wall Nusselt number for a circular channel (Ref. [54], Table 6-1), so except for the presence of $m _ { k }$ this is just the simplest laminar, circular heat-transfer equation. The multiplier $m _ { k }$ accounts for the enhancement of the Nusselt number due to turbulence, as is described below.

Starting conditions are straightforward for VXT\* segments: The starting $p _ { 1 } , U _ { 1 , } T _ { m }$ , and $\dot { H } _ { 2 , k }$ are obtained directly from the end of the previous segment, and $T _ { \mathrm { s o l i d } }$ is given by the user (or as a guess, of course).

In the VXQ\* segments, the heat exchange per unit length $\dot { q }$ is independent of x and is set by the user, as the segment’s heat parameter divided by the appropriate length parameter. In VXQ2, the two “passes” can, of course, have diferent values of heat and length, and hence diferent values of ${ \dot { q } } .$ To make progress, it is necessary to make a couple of assumptions to simplify the starting equations. Solving Eqs. (10.159)–(10.162) for $d T _ { m } / d x , d T _ { \mathrm { s o l i d } } / d x .$ $d \dot { H } _ { 2 , k } / d x$ , and $d \dot { H } _ { \mathrm { s o l i d } } / d x$ and integrating them would require initial values for $T _ { \mathrm { s o l i d } }$ and $\dot { H } _ { \mathrm { s o l i d } }$ , in addition to the initial values of $T _ { m }$ and $\dot { H } _ { 2 , k }$ that are passed into the VXQ\* segment from the end of the previous segment. To avoid having to specify or guess the initial values of $T _ { \mathrm { s o l i d } }$ and $\dot { H } _ { \mathrm { s o l i d } }$ , we assume that most of $\dot { q }$ goes into the thermoacoustic gas in cases of interest to us, so the first term on the right side of Eq. (10.162) can be neglected there. This assumption probably leads only to a slight overestimation of the temperature diference $\left. T _ { \mathrm { s o l i d } } - T _ { m } \right.$ in cases of interest to us. Second, we assume that $d T _ { \mathrm { s o l i d } } / d x =$ $d T _ { m } / d x$ . Examination of Eq. (10.162) (with the aforementioned first assumption, and with $\dot { q }$ independent of $x$ here for a VXQ\* segment) shows that this assumption is equivalent to $d ( k N _ { N u } ) / d x = 0$ , which seems reasonable enough (until someone figures out a better way to do all this simply enough for DeltaEC). Then the starting equations can be rearranged

$$
\frac { d T _ { m } } { d x } ~ = ~ \frac { \dot { H } _ { 2 , k } - \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U } _ { 1 } \left( 1 - \frac { T _ { m } \beta ( f _ { \kappa } - \tilde { f } _ { \nu } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) ( 1 - \tilde { f } _ { \nu } ) } \right) \right] } { \frac { \rho _ { m } c _ { p } | U _ { 1 } | ^ { 2 } } { 2 \omega A _ { \mathrm { g a s } } ( 1 - \sigma ) | 1 - f _ { \nu } | ^ { 2 } } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \tilde { f } _ { \nu } ) ( 1 + \epsilon _ { s } f _ { \nu } / f _ { \kappa } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) } \right] - A _ { \mathrm { g a s } } k - A _ { \mathrm { s o l i d } } k _ { s } } ,\tag{10.167}
$$

$$
\frac { d U _ { 1 } } { d x } ~ = ~ - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \beta ( f _ { \kappa } - f _ { \nu } ) } { ( 1 - f _ { \nu } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 } ,\tag{10.168}
$$

$$
\mathrm { w i t h ~ } \frac { d T _ { m } } { d x } \mathrm { ~ g i v e n ~ b y ~ E q . ~ } ( 1 0 . 1 6 7 ) ,\tag{10.169}
$$

$$
{ \frac { d \dot { H } _ { 2 , k } } { d x } } ~ = ~ \dot { q } ,\tag{10.170}
$$

$$
T _ { \mathrm { s o l i d } } = T _ { m } + { \frac { 4 r _ { h } ^ { 2 } } { 4 . 4 m _ { k } A _ { \mathrm { g a s } } k } } \dot { q } ,\tag{10.171}
$$

The factor $^ { 6 } 4 . 4 ^ { 9 }$ in Eq. (10.171) is the laminar, constant-heat-flux-density Nusselt number for a circular channel (Ref. [54], Table 6-1), so except for the presence of $m _ { k }$ this is just the simplest laminar, circular heat-transfer equation. The multiplier $m _ { k }$ accounts for the enhancement of the Nusselt number due to turbulence, as is described below.

Because of the assumptions in the previous paragraph, the starting conditions for the numerical integration are unambiguous: the four integrated variables $T _ { m } , p _ { 1 } , U _ { 1 }$ , and $\dot { H } _ { 2 , k }$ all start with the values left over from the previous segment of the DeltaEC model.

Tubesheets are treated exactly like stacks, with $\dot { H } _ { 2 , k }$ constant and

$$
\begin{array} { r l } { \frac { d T _ { m } } { d x } } & { = \ \frac { \tilde { H } _ { 2 , k } - \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U } _ { 1 } \left( 1 - \frac { \tilde { \Gamma } _ { m } \tilde { \beta } ( f _ { k } - \tilde { f } _ { \nu } ) } { ( 1 + \epsilon _ { 0 } ) ( 1 + \sigma ) } \right) \right] } { \frac { \rho _ { m } \epsilon _ { 0 } | U _ { 1 } | ^ { 2 } } { 2 \omega A _ { \mathrm { E e } } ( 1 - \sigma ) | 1 - f _ { \nu } | ^ { 2 } } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( \tilde { f } _ { \nu } - \tilde { f } _ { \nu } ) ( 1 + \epsilon _ { \nu } / f _ { k } ) } { ( 1 + \epsilon _ { 0 } ) ( 1 + \sigma ) } \right] - A _ { \mathrm { g a b } } k - A _ { \mathrm { s a l i d } } k _ { s } } , } \\ { \frac { d p _ { 1 } } { d x } } & { = \ - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A _ { \mathrm { g a b } } } U _ { 1 , } } \\ { \frac { d U _ { 1 } } { d x } } & { = \ - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \beta ( f _ { \kappa } - f _ { \nu } ) } { ( 1 - f _ { \nu } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 } , } \\ & { \mathrm { w i t h } \ \frac { d T _ { m } } { d x } \mathrm { g i v e n ~ b y ~ E q . ~ } ( 1 0 . 1 7 2 ) , } \end{array}\tag{10.172}
$$

(10.173)

(10.174)

but with $A _ { \mathrm { s o l i d } } = A _ { \mathrm { t o t a l } } - A _ { \mathrm { g a s } }$

The important viscous and thermal functions $f _ { \nu }$ and $f _ { \kappa }$ needed in Eqs. (10.156)–(10.159) and their variants are calculated as described here. For large displacement amplitudes, the efective length of the tube is its geometrical length (the total geometrical length, i.e., the sum of tubesheet and heat-transfer-region lengths). For small displacement amplitudes, the efective length is infinite. In between, this interpolation is used:

$$
\Delta x _ { \mathrm { e f f } } = \frac { 4 \Delta x _ { \mathrm { g e o m } } } { 1 0 \left| \xi _ { 1 } \right| / \Delta x _ { \mathrm { g e o m } } - 1 } \mathrm { w h e n } \frac { \Delta x _ { \mathrm { g e o m } } } { 1 0 } < \left| \xi _ { 1 } \right| < \frac { \Delta x _ { \mathrm { g e o m } } } { 2 } .\tag{10.175}
$$

![[mu_66afccee_f41d10fa007dceb8183f.jpg]]  
Figure 10.9: Efective length as a function of displacement amplitude $| \xi _ { 1 } |$ . For $\dot { N }$ disabled, only the horizontal axis is relevant. For $\dot { N }$ enabled, this plot displays Eqs. (10.192)–(10.194).

(The choices of this functional form, and of $1 / 1 0$ and $1 / 2$ as transitions, are arbitrary and without justification, but these details have little efect on the final results.) With this efective length, shown along the x axis in Fig. 10.9, the top half of Fig. 7-1 in Kays and London is used to estimate the efect of turbulence on $f _ { \nu }$ and $f _ { \kappa }$ in the tube. (That figure shows friction factor as a function of Reynolds number, for a few values of $\Delta x / D . )$ DeltaEC’s internal approximations to the Kays and London data are shown here in Fig. 10.10. Power laws

$$
F = g 1 0 ^ { - B N _ { R } }\tag{10.176}
$$

are fit to Kays and London’s high- $N _ { R }$ straight lines, and similar power laws with ofsets are fit to their low- $. N _ { R }$ straight lines, with interpolations for $2 4 5 0 < N _ { R } < 1 0 , 0 0 0$ using a cubic polynomial matched to the inner ends of the two straight lines in both slope and value. (Here F is the Moody friction factor, four times the Fanning friction factor that Kays and London call $f . )$ Then, using the peak Reynolds number, a multiplier

$$
m _ { \nu } = \operatorname * { m a x } \left[ 1 , \ \frac { \delta _ { \nu } ^ { 2 } N _ { R } } { 2 4 \pi r _ { h } ^ { 2 } } \frac { F } { \operatorname { R e } \left[ i / \left( 1 - f _ { \nu } \right) \right] } \right]\tag{10.177}
$$

gives the estimate of how turbulence (including entrance efects) afects what would otherwise be a laminar boundary layer. This expression is easily derived from the discussion about turbulence in Section 10.1.1.

Bessel-function (or, for large R, boundary-layer) expressions are used for “starting values” of $f _ { \nu }$ and $f _ { \kappa }$ . Then $m _ { \nu }$ as described above is used to generate modified $f _ { \nu }$ and $f _ { \kappa }$ for the momentum and continuity equations above, exactly as described in Section 10.1.1: DeltaEC increases the resistive component of the pressure gradient, and hence the viscous power dissipation, by $m _ { \nu }$ . It decreases the inertial pressure gradient by

$$
m _ { \nu } ^ { \prime } = \left( \frac { 1 - \delta _ { \nu } / R } { 1 - \delta _ { \nu } / m _ { \nu } R } \right) ^ { 2 }\tag{10.178}
$$

to correct approximately for the steeper velocity gradient at the wall, which increases the efective area open to gas contributing to inertial efects. It applies the same turbulence

![[mu_66afccee_6d9bd20525a2e6d3cd8f.jpg]]  
Figure 10.10: DeltaEC’s fits for Kays and London’s Fig. 7-1. The upper set of curves is the Fanning friction factor [Fanning = Moody $/ 4 = F / 4$ in Eqs. (10.176) and (10.177)], and the lower set is for the heat-transfer coeficient. Within each set, the diferent curves are for diferent $L / D$ : infinity, 100, 50, 25, 15, and 1 from bottom to top.

correction to $f _ { \kappa }$ as to $f _ { \nu }$ , with no justification other than the idea that turbulent eddies carry heat and momentum similarly. For both f ’s,

$$
\mathrm { I m } \left[ \frac { 1 } { 1 - f _ { j } } \right] = m _ { \nu } \mathrm { I m } \left[ \frac { 1 } { 1 - f _ { j , \mathrm { l a m i n a r } } } \right] ,\tag{10.179}
$$

$$
\mathrm { R e } \left[ \frac { 1 } { 1 - f _ { j } } \right] = m _ { \nu } ^ { \prime } \mathrm { R e } \left[ \frac { 1 } { 1 - f _ { j , \mathrm { l a m i n a r } } } \right] ,\tag{10.180}
$$

$$
f _ { j } = 1 - \left( \mathrm { R e } \left[ \frac { 1 } { 1 - f _ { j } } \right] + i \mathrm { I m } \left[ \frac { 1 } { 1 - f _ { j } } \right] \right) ^ { - 1 }\tag{10.181}
$$

[Note that, perhaps somewhat inconsistently, $m _ { \nu }$ enhances heat transfer in $f _ { \kappa }$ in Eqs. (10.157) and (10.159) while $m _ { k }$ is used in the time-averaged heat-transfer Eqs. (10.166) and (10.171).]

The value of $m _ { k }$ needed in Eq. (10.162) is obtained as follows. Power laws

$$
\Sigma = A 1 0 ^ { - B N _ { R } }\tag{10.182}
$$

are fit to the $\mathrm { l o w } { - } N _ { R }$ and $\mathrm { h i g h } { - N _ { R } }$ straight lines in the lower half of Kays and London Fig. 7-1, with interpolations for $2 4 5 0 < N _ { R } < 1 0 , 0 0 0$ using a cubic polynomial matched to the inner ends of the two straight lines in both slope and value. (That figure shows heat-transfer factor as a function of Reynolds number, for a few values of $\Delta x / D$ . Here $\Sigma$ is the heat-transfer factor that Ref. [54] calls $N _ { S t } \sigma ^ { 2 / 3 } . )$ Figure 10.10 shows these fits. Since time-averaged heat transfer is desired, these equations are evaluated using the time-averaged Reynolds number $\left( 2 / \pi \right) | N _ { R , 1 } |$ . Finally, a multiplier

$$
m _ { k } = \frac { \Sigma } { \Sigma _ { \mathrm { l a m i n a r } } ( \Delta x _ { \mathrm { e f f } } = \infty ) }\tag{10.183}
$$

gives the turbulence correction factor in the otherwise laminar Eqs. (10.166) and (10.171).

## Modifications to calculations for $\dot { N } \neq 0$

In the presence of nonzero steady flow $\dot { N }$ , the starting equations are modified and augmented as follows:

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A _ { \mathrm { g a s } } } U _ { 1 } + \frac { i \omega m \dot { N } } { \rho _ { m } a ^ { 2 } A _ { \mathrm { g a s } } } \frac { 1 + ( \gamma - 1 ) f _ { \kappa } / ( 1 + \epsilon _ { s } ) } { 1 - f _ { \nu } } p _ { 1 } , } \\ { \displaystyle \frac { d U _ { 1 } } { d x } } & { = } & { \displaystyle - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left( 1 + \frac { ( \gamma - 1 ) f _ { \kappa } } { 1 + \epsilon _ { s } } \right) p _ { 1 } + \frac { \beta ( f _ { \kappa } - f _ { \nu } ) } { ( 1 - f _ { \nu } ) ( 1 - \sigma ) ( 1 + \epsilon _ { s } ) } \frac { d T _ { m } } { d x } U _ { 1 } } \\ & & { \displaystyle + \frac { i \omega m \dot { N } } { \rho _ { m } a ^ { 2 } A _ { \mathrm { g a s } } ( 1 - f _ { \nu } ) } U _ { 1 } , } \end{array}\tag{10.184}
$$

(10.185)

$$
\begin{array} { r c l } { \dot { H } _ { \mathrm { t o t } } } & { = } & { \displaystyle \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U } _ { 1 } \left( 1 - \frac { T _ { m } \beta ( f _ { \kappa } - \tilde { f } _ { \nu } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) ( 1 - \tilde { f } _ { \nu } ) } \right) \right] } \\ & & { + \frac { \rho _ { m } c _ { p } \left| U _ { 1 } \right| ^ { 2 } } { 2 \omega A _ { \mathrm { g a s } } ( 1 - \sigma ) \left| 1 - f _ { \nu } \right| ^ { 2 } } \frac { d T _ { m } } { d x } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \tilde { f } _ { \nu } ) ( 1 + \epsilon _ { s } f _ { \nu } / f _ { \kappa } ) } { ( 1 + \epsilon _ { s } ) ( 1 + \sigma ) } \right] } \\ & & { - A _ { \mathrm { g a s } } k \frac { d T _ { m } } { d x } + \dot { H } _ { \mathrm { s o l i d } } + \dot { N } m w _ { m } , } \end{array}\tag{10.186}
$$

$$
\dot { H } _ { \mathrm { s o l i d } } ~ = ~ - A _ { \mathrm { s o l i d } } k _ { s } \frac { d T _ { \mathrm { s o l i d } } } { d x } ,\tag{10.187}
$$

$$
\dot { q } ( x ) ~ = ~ \frac { d \dot { H } _ { \mathrm { t o t } } } { d x } \cong \frac { \dot { N } m c _ { p } } { F _ { \dot { Q } \dot { N } } } \frac { d T _ { m } } { d x } \mathrm { ~ i n ~ a ~ p a s s , ~ b u t = 0 ~ i n ~ a ~ t u b e s h e e t , }\tag{10.188}
$$

$$
\dot { q } ( x ) = \frac { A _ { \mathrm { g a s } } k } { 4 r _ { h } ^ { 2 } } N _ { N u } \left( T _ { \mathrm { s o l i d } } - T _ { m } \right) ,\tag{10.189}
$$

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } } & { = } & { \displaystyle - \frac { | p _ { 1 } | ^ { 2 } } { 4 } \frac { d } { d x } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) - \frac { | U _ { 1 } | ^ { 2 } } { 4 A _ { \mathrm { g a s } } } \frac { d \rho _ { m } } { d x } } \\ & & { \displaystyle - \mathrm { s i g n } ( \dot { N } _ { 2 , 0 } ) \frac { 1 } { 2 } \rho _ { \mathrm { m } } \left( \frac { m \dot { N } _ { 2 , 0 } } { \rho _ { \mathrm { m } } A _ { \mathrm { g a s } } } \right) ^ { 2 } \frac { F } { 4 r _ { h } } \sqrt { \frac { 1 } { 2 } + \left( \frac { \rho _ { \mathrm { m } } | U _ { 1 } | } { m \dot { N } _ { 2 , 0 } } \right) ^ { 2 } } } \end{array}\tag{10.190}
$$

where $\dot { N } _ { 2 , 0 }$ and $\dot { N }$ are related by

$$
\dot { N } _ { 2 , 0 } = \dot { N } + \frac { \beta } { m c _ { p } } \left[ \dot { H } _ { \mathrm { t o t } } - \dot { N } m w _ { m } \right] - \left( \frac { 1 } { m a ^ { 2 } } + \frac { \beta } { m c _ { p } } \right) \dot { E } _ { 2 } .\tag{10.191}
$$

Important: Equation (10.191) omits the $\left( A _ { \mathrm { g a s } } k + A _ { \mathrm { s o l i d } } k _ { s } \right) d T _ { m } / d x$ term that is present in Eq. (8.16) because we expect it to be negligible most of the time and because DeltaEC needs $\dot { N } _ { 2 , 0 }$ before it knows $d T _ { m } / d x$ in each pass of its numerical integration. In Eqs. (10.184)– (10.190), DeltaEC evaluates $m _ { \nu }$ and $F$ on the basis of $\sqrt { { \left| N _ { R , 1 } \right| } ^ { 2 } + N _ { R , 2 , 0 } ^ { 2 } } .$ , and it evaluates $m _ { \kappa }$ on the basis of $\sqrt { 4 \left| N _ { R , 1 } \right| ^ { 2 } / \pi ^ { 2 } + N _ { R , 2 , 0 } ^ { 2 } }$ . The square-root factor at the end of the equation for $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ is a rough empirical match to steady-flow DUCT results; this factor helps counteract the fact that high $| U _ { 1 } |$ biases the friction factor $F$ toward values that are unrealistically low for use in this equation. The friction and heat-transfer factors are based on an efective tube length $\Delta x _ { \mathrm { e f f } }$ plotted in Fig. 10.9 and given by

$$
\begin{array} { r l r } { \Delta x _ { \mathrm { e f f } } } & { = } & { \infty \mathrm { w h e n } \left( \displaystyle { \frac { | \xi _ { 1 } | } { \Delta x _ { \mathrm { g e o m } } } } \right) ^ { 2 } + \left( \displaystyle { \frac { N _ { R , 2 , 0 } } { 1 0 0 0 } } \right) ^ { 2 } \le \displaystyle { \frac { 1 } { 1 0 0 } } , ( 1 0 . 1 9 2 \mathrm { w h e n ~ \frac { | \xi _ { 1 } | } { \Delta x _ { \mathrm { g e o m } } } } ) } \\ & { = } & { \displaystyle { \frac { 4 \Delta x _ { \mathrm { g e o m } } } { 1 0 \sqrt { \left( \frac { | \xi _ { 1 } | } { \Delta x _ { \mathrm { g e o m } } } \right) ^ { 2 } + \left( \frac { N _ { R , 2 , 0 } } { 1 0 0 0 } \right) ^ { 2 } } - 1 } } \mathrm { w h e n ~ } \displaystyle { \frac { 1 } { 1 0 0 } } \le \left( \displaystyle { \frac { | \xi _ { 1 } | } { \Delta x _ { \mathrm { g e o m } } } } \right) ^ { 2 } + \left( \displaystyle { \frac { N _ { R , 2 , 0 } } { 1 0 0 0 } } \right) ^ { 2 } \le \displaystyle { \frac { 1 } { 4 } } , } \\ & { } & { \medskip } \\ & { = } & { \displaystyle { \Delta x _ { \mathrm { g e o m } } } \mathrm { w h e n ~ } \left( \displaystyle { \frac { | \xi _ { 1 } | } { \Delta x _ { \mathrm { g e o m } } } } \right) ^ { 2 } + \left( \displaystyle { \frac { N _ { R , 2 , 0 } } { 1 0 0 0 } } \right) ^ { 2 } \ge \displaystyle { \frac { 1 } { 4 } } . ( 1 0 . 1 9 4 \mathrm { w h e n ~ } \displaystyle { \frac { | \xi _ { 1 } | } { \Delta x _ { \mathrm { g e o m } } } } ) } \end{array}
$$

## 10.8 Adiabatic–isothermal interface loss

## 10.8.1 JOIN

## General description:

The JOIN segment accounts for “small” discontinuities in thermoacoustic variables at the interface between a heat exchanger or other isothermal segment and an unmixed, thermally stratified, adiabatic region such as a pulse tube. The discontinuity $\delta T _ { m }$ in mean temperatures is first order in the acoustic amplitude, the discontinuity $\delta U _ { 1 }$ in volume flow rate is second order, and there is no discontinuity in pressure. See Refs. [65, 66] for $\delta T _ { m }$ , Ref. [67] for $\delta U _ { 1 }$ , and Ref. [13] and references therein for both $\delta T _ { m }$ and $\delta U _ { 1 }$

When it encounters a JOIN segment, DeltaEC looks upstream and downstream (ignoring logistical segments such as RPN) to figure out whether the “heat exchanger” is upstream and the “pulse tube” is downstream, or vice versa. Both A and $d T _ { m } / d x$ are obtained from the “pulse tube” or other open duct, with $d T _ { m } / d x = 0$ for DUCTs and CONEs, and $d T _ { m } / d x$ nonzero for STKDUCTs or STKCONEs. (If the relevant duct is a STKDUCT or STKCONE downstream of the JOIN segment, DeltaEC integrates ahead momentarily to evaluate $d T _ { m } / d x . )$

The JOIN feature does not yet do anything diferent for nonzero $\dot { N }$

## Input variables; Potential targets; Master–slave links:

None.

## Format and examples:

8   
SX p.t. hot h.x.   
1.1675E-04 a Area m^2 1.3507E+05 A |p| Pa   
0.6470 b VolPor -17.664 B Ph(p) deg   
3.0000E-03 c Length m 2.9183E-04 C |U| m^3/s   
1.2000E-05 d rh m 138.51 D Ph(U) deg   
2.8164 e HeatIn W G -13.711 E Hdot W   
Possible targets -18.030 F Edot W   
copper Solid type 300.00 H SolidT K   
9   
JOIN first join example   
1.3507E+05 A |p| Pa   
-17.664 B Ph(p) deg   
2.9863E-04 C |U| m^3/s   
138.51 D Ph(U) deg   
-13.711 E Hdot W   
-18.450 F Edot W   
300.00 G TBeg K   
324.67 H TEnd K   
10   
STKDUCT the pulse tube   
1.1675E-04 a Area m^2 S=-2 1.3511E+05 A |p| Pa   
3.8307E-02 b Perim m Fnc(10a) -17.530 B Ph(p) deg   
7.0000E-02 c Length m 2.7164E-04 C |U| m^3/s   
5.8678E-05 d WallA m^2 166.83 D Ph(U) deg   
-13.711 E Hdot W   
-18.298 F Edot W   
324.67 G TBeg K   
57.932 H TEnd K   
stainless Solid type 0.1518 I StkEdt W   
1- 11   
RPN ratio of cold end displacement to p.t. length   
0.1000 a G or T (t) 9.2000E-02 A ChngeMe   
10C 2 / pi / 0b / 10a / 10c /   
12

JOIN second example; note that RPNs can go between   
1.3511E+05 A |p| Pa   
-17.530 B Ph(p) deg   
2.7854E-04 C |U| m^3/s   
166.83 D Ph(U) deg   
-13.711 E Hdot W   
-18.763 F Edot W   
57.932 G TBeg K   
89.997 H TEnd K   
13   
RPN ratio of warm end displacement to p.t. length   
6.0000 a G or T (t) 9.8838E-02 A ChngeMe   
8C 2 / pi / 0b / 10a / 10c /   
! - 14   
SX cold heat exchanger adj rh   
1.1675E-04 a Area m^2 1.5473E+05 A |p| Pa   
0.6470 b VolPor -16.785 B Ph(p) deg   
5.7150E-03 c Length m 2.7985E-04 C |U| m^3/s   
1.2000E-05 d rh m 169.37 D Ph(U) deg   
...etc...

## Calculations:

The discontinuity in temperature at JOIN is:

$$
T _ { m , \mathrm { o u t } } - T _ { m , \mathrm { i n } } = \left( - \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } \left| p _ { 1 } \right| \sin \theta - \frac { \left| U _ { 1 } \right| _ { \mathrm { i n } } } { \omega A _ { \mathrm { g a s } } } \frac { d T _ { m } } { d x } \right) F ,\tag{10.195}
$$

where $\theta$ is the angle by which $p _ { 1 }$ leads $U _ { 1 } , d T _ { m } / d x$ is evaluated on the thermally stratified, adiabatic side of the JOIN, and the factor F is given by

$$
F = \sqrt { \frac { 2 \left( A _ { \mathrm { g a s } } k \ d T _ { m } / d x \right) ^ { 2 } } { \left( A _ { \mathrm { g a s } } k \ d T _ { m } / d x \right) ^ { 2 } + \left( \dot { H } _ { 2 , k } - \dot { E } \right) ^ { 2 } } } .\tag{10.196}
$$

The factor $F$ is a very crude attempt to account for the two-dimensional nature of the JOIN problem within DeltaEC’s inherently one-dimensional character. The derivation of the $T _ { m }$ joining condition in the references neglects the thermal conductivity of the wall of the tube and the boundary-layer shuttle entropy flux. If these are zero while $d T _ { m } / d x \ne 0$ , then $F = 1$ and Eq. (10.195) represents the joining condition derived in the references. On the other hand, if the wall of the duct or the boundary layer is efectively a thermal short circuit compared to bulk gas conductivity, then $F = 0$ and no temperature discontinuity appears at the JOIN segment. We arbitrarily chose a simple smooth function that passes through these two limiting cases. (This function was changed between DeltaEC version 6.3 and version 6.4, to cure a rare situation that had nonsensically yielded $F \gg 1 . )$

The discontinuity in $| U _ { 1 } |$ at JOIN is

$$
\begin{array} { r c l } { { \displaystyle \left| U _ { 1 } \right| _ { \mathrm { o u t } } } } & { { = } } & { { \displaystyle \left| U _ { 1 } \right| _ { \mathrm { i n } } - \frac { 8 } { 3 \pi } \frac { ( \gamma - 1 ) } { \rho _ { m } a ^ { 2 } } \left| p _ { 1 } \right| \left| U _ { 1 } \right| _ { \mathrm { i n } } \cos \theta } } \\ { { \displaystyle } } & { { = } } & { { \displaystyle \left| U _ { 1 } \right| _ { \mathrm { i n } } - \frac { 1 6 } { 3 \pi } \frac { \gamma - 1 } { \rho _ { m } a ^ { 2 } } \dot { E } . } } \end{array}\tag{10.197}
$$

There is no discontinuity in $p _ { 1 }$ , in the phase of $U _ { 1 }$ , or in $\dot { H } _ { 2 , k }$

Note that Eqs. (10.195)–(10.197) are a lowest-order approximation to what is usually a small efect. Worrying about whether to evaluate variables such as $\rho _ { m }$ on the upstream or downstream side of the JOIN is unjustified. DeltaEC evaluates them on the “easy” (upstream) side.

## 10.9 Mixture separation

## 10.9.1 MIXBL, MIXSLAB, and MIXCIRC

## General description:

The MIXBL, MIXSLAB, and MIXCIRC segments calculate $d p _ { 1 } / d x , ~ d U _ { 1 } / d x$ , and $d n _ { L } / d x$ for sound propagation in gas mixtures, with or without steady flow, according to the theory described in Ref. [10], which builds on the theory described in Refs. [45, 68]. MIXBL performs the calculations in boundary-layer approximation, MIXSLAB in parallel-plate geometry of arbitrary gap $2 y _ { 0 }$ , and MIXCIRC in circular pores of arbitrary radius R. The solid is assumed to be ideal, so it imposes a perfect isothermal boundary condition on the gas.

## Input variables, MIXBL:

Area $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { \mathrm { g a s } }$ available to the gas, based on inside dimensions.

Perim (m) Perimeter Π of the inside cross section described above.

Length (m) The length $\Delta x$ of the segment.

## Input variables, MIXSLAB:

Area $( \mathrm { m } ^ { 2 } )$ Total cross-sectional area A including gas and solid.

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$ . (We often fix this at 1.000 and set Area equal to the gas area.)

Length (m) The length $\Delta x$ of the segment.

y0 (m) Half the plate spacing is $y _ { 0 }$ . Thus, $2 y _ { 0 }$ is the gap available to the gas.

## Input variables, MIXCIRC:

Area $( \mathrm { m } ^ { 2 } )$ Total cross-sectional area A including gas and solid.

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A .$ . (We often fix this at 1.000 and set Area equal to the gas area.)

Length (m) The length $\Delta x$ of the segment.

radius (m) The radius R of the pores.

## Potential targets:

None.

## Master–slave links:

The length of any of these segments can be slaved to the length of another segment to keep the sum of the two lengths constant.

(For an introduction to master–slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

![[mu_66afccee_768bd4086ab941b4ed07.jpg]]  
Section 7.3 has an example DeltaEC file using MIXCIRC.

## Calculations:

The evolution of $p _ { 1 }$ with x in MIXBL, MIXSLAB, and MIXCIRC is given by the same integration as in DeltaEC’s other ducts,

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A _ { \mathrm { g a s } } } U _ { 1 } ,\tag{10.198}
$$

because Ref. [69] showed that the first-order thermoacoustic momentum equation is unchanged by mixture-separation efects. The evolution of $U _ { 1 }$ with x is given by Eq. (8) in Ref. [69], but they didn’t write the result explicitly [10]. The explicit result, in DeltaEC’s notation, is

$$
\frac { d U _ { 1 } } { d x } = - \frac { i \omega A _ { \mathrm { g a s } } } { \rho _ { m } a ^ { 2 } } \left\{ 1 + \left( \gamma - 1 \right) \left[ B f _ { \nu } + C f _ { \kappa D } + \left( 1 - B - C \right) f _ { D \kappa } \right] \right\} p _ { 1 } ,\tag{10.199}
$$

where B and C are given in Ref. [45], and the other variables carry their usual DeltaEC meanings or are defined below.

The evolution of the light fraction $n _ { L }$ with x is given by solving Eq. (7) in Ref. [10] for $d n _ { H } / d x$ , and integrating numerically for fixed $\dot { N } _ { L }$ , which is equivalent to fixed $\dot { N } _ { H }$ and fixed $\dot { N } = \dot { N } _ { H } + \dot { N } _ { L }$ . Solving Eq. (7) for $d n _ { H } / d x$ yields

$$
\frac { d n _ { H } } { d x } = \frac { \dot { N } _ { H } - n _ { H } \dot { N } - \frac { \delta _ { \kappa } } { 4 r _ { h } } \frac { \gamma - 1 } { \gamma } \frac { k \gamma } { R _ { \mathrm { u n i v } } T _ { m } } \left| p _ { 1 } \right| \left| U _ { 1 } \right| \left( F _ { \mathrm { t r a v } } \cos \theta + F _ { \mathrm { s t a n d } } \sin \theta \right) } { \frac { \delta _ { \kappa } } { 4 r _ { h } } \frac { \rho _ { m } \left| U _ { 1 } \right| ^ { 2 } } { m _ { \mathrm { a v g } } \omega A _ { \mathrm { g a s } } } F _ { \mathrm { g r a d } } - \frac { \rho _ { m } } { m _ { \mathrm { a v g } } } A _ { \mathrm { g a s } } D _ { 1 2 } } ,\tag{10.200}
$$

and then DeltaEC uses dn $_ L / d x = - \ d n _ { H } / d x$ to obtain the desired result.

In addition to the usual definitions of the viscous and thermal penetration depths $\delta _ { \nu } =$ $\sqrt { 2 \mu / \omega \rho _ { m } }$ and $\delta _ { \kappa } = \sqrt { 2 k / \omega \rho _ { m } c _ { p } }$ , two new penetration depths are defined for mixtures:

$$
\delta _ { \kappa D } ^ { 2 } \ = \ \frac 1 2 \delta _ { \kappa } ^ { 2 } \left[ 1 + \left( 1 + \varepsilon \right) / L + \sqrt { \left[ 1 + \left( 1 + \varepsilon \right) / L \right] ^ { 2 } - 4 / L } \right] ,\tag{10.201}
$$

$$
\delta _ { D \kappa } ^ { 2 } = \frac { 1 } { 2 } \delta _ { \kappa } ^ { 2 } \left[ 1 + \left( 1 + \varepsilon \right) / L - \sqrt { \left[ 1 + \left( 1 + \varepsilon \right) / L \right] ^ { 2 } - 4 / L } \right] ,\tag{10.202}
$$

where

$$
\varepsilon = \frac { \gamma - 1 } { \gamma } \frac { k _ { T } ^ { 2 } } { n _ { L } \left( 1 - n _ { L } \right) } ,\tag{10.203}
$$

$k _ { T }$ is the thermal difusion ratio, $L = k / \rho _ { m } c _ { p } D _ { 1 2 }$ , and $D _ { 1 2 }$ is the binary mass-difusion coeficient.

In MIXBL, DeltaEC uses the boundary-layer results of Ref. [45]. For $f _ { \nu } , f _ { \kappa D }$ , and $f _ { D \kappa }$ the boundary layer result is

$$
f _ { j } = ( 1 - i ) \frac { \delta _ { j } } { 2 r _ { h } } ,\tag{10.204}
$$

where $j$ is $\nu , \kappa D$ , or $D \kappa$ . For the three $F \mathrm { \ ' } _ { \mathrm { s } }$ , the boundary-layer results are

$$
{ \cal F } _ { \mathrm { t r a v } } ~ = ~ { \frac { \sigma \sqrt { \sigma L } - \sqrt { \sigma } - \sigma \sqrt { L } \left( \delta _ { \kappa D } / \delta _ { \kappa } + \delta _ { D \kappa } / \delta _ { \kappa } \right) } { \left( 1 + \sqrt { L } \right) \left[ ( 1 + \sigma ) ( 1 + \sigma L ) + \varepsilon \sigma \right] } } ,\tag{10.205}
$$

$$
F _ { \mathrm { s t a n d } } ~ = ~ { \frac { - \sigma { \sqrt { \sigma L } } + { \sqrt { \sigma } } - \sigma { \sqrt { L } } \left( \delta _ { \kappa D } / \delta _ { \kappa } + \delta _ { D \kappa } / \delta _ { \kappa } \right) } { \left( 1 + { \sqrt { L } } \right) \left[ \left( 1 + \sigma \right) \left( 1 + \sigma L \right) + \varepsilon \sigma \right] } } ,\tag{10.206}
$$

$$
\begin{array} { r l } { F _ { \mathrm { g r a d } } } & { = \ \frac { \sqrt { \sigma } L \left( 1 - \sigma ^ { 2 } \right) \left( 1 + \sqrt { L } \right) + \varepsilon \sqrt { \sigma } \left( \sqrt { L } - 1 \right) + \left[ \left( \sigma ^ { 2 } - 1 \right) L + \varepsilon \sigma \sqrt { L } \right] \left( \frac { \delta _ { x D } } { \delta _ { \kappa } } + \frac { \delta _ { D \kappa } } { \delta _ { \kappa } } \right) } { \left( 1 + \sqrt { L } \right) \left[ \left( 1 + \sigma \right) \left( 1 + \sigma L \right) + \varepsilon \sigma \right] \left[ \left( 1 - \sigma \right) \left( 1 - \sigma L \right) - \varepsilon \sigma \right] / \sigma } } \end{array}\tag{10.207}
$$

In MIXSLAB and MIXCIRC, DeltaEC uses the following expressions:

$$
F _ { \mathrm { t r a v } } ~ = ~ - \frac { 2 r _ { h } } { \delta _ { \kappa } } \mathrm { R e } \left[ \frac { G } { \left( 1 - \tilde { f } _ { \nu } \right) } \right] ,\tag{10.208}
$$

$$
F _ { \mathrm { s t a n d } } = { \frac { 2 r _ { h } } { \delta _ { \kappa } } } \mathrm { I m } \left[ { \frac { G } { \left( 1 - \tilde { f } _ { \nu } \right) } } \right] ,\tag{10.209}
$$

$$
\begin{array} { r c l } { { F _ { \mathrm { g r a d } } } } & { { = } } & { { \displaystyle - \frac { 2 r _ { h } } { \delta _ { \kappa } } \frac { 1 } { \left| 1 - f _ { \nu } \right| ^ { 2 } } \frac { \sigma } { \left( 1 - \sigma \right) \left( 1 - \sigma L \right) - \varepsilon \sigma } } } \\ { { } } & { { } } & { { \cdot \ \mathrm { I m } \left[ \frac { \left( 1 - \sigma \right) } { \sigma S } f _ { \nu } \left( \frac { \delta _ { \kappa } ^ { 2 } - \delta _ { \kappa D } ^ { 2 } } { \delta _ { \nu } ^ { 2 } + \delta _ { \kappa D } ^ { 2 } } f _ { \kappa D } - \frac { \delta _ { \kappa } ^ { 2 } - \delta _ { D \kappa } ^ { 2 } } { \delta _ { \nu } ^ { 2 } + \delta _ { D \kappa } ^ { 2 } } f _ { D \kappa } + \frac { \left( 1 + \sigma \right) L Q } { M } \tilde { f } _ { \nu } + S \right) + \varepsilon G \right] , } } \end{array}\tag{10.210}
$$

where $r _ { h }$ is the hydraulic radius and

$$
\begin{array} { r c l } { S } & { = } & { \left( \displaystyle \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { D \kappa } ^ { 2 } } - 1 \right) f _ { D \kappa } - \left( \displaystyle \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { \kappa D } ^ { 2 } } - 1 \right) f _ { \kappa D } , } \end{array}\tag{10.211}
$$

$$
Q ~ = ~ { \frac { \delta _ { \kappa D } ^ { 2 } - \delta _ { D \kappa } ^ { 2 } } { \delta _ { \kappa } ^ { 2 } } } ,\tag{10.212}
$$

$$
\begin{array} { l l l } { { M } } & { { = } } & { { ( 1 + \sigma ) ( 1 + \sigma L ) + \varepsilon \sigma , } } \end{array}\tag{10.213}
$$

$$
G ~ = ~ \frac { \sigma L Q } { M S } f _ { \kappa D } f _ { D \kappa } + \frac { \tilde { f } _ { \nu } } { S } \left( \frac { f _ { \kappa D } } { 1 + \delta _ { \nu } ^ { 2 } / \delta _ { D \kappa } ^ { 2 } } - \frac { f _ { D \kappa } } { 1 + \delta _ { \nu } ^ { 2 } / \delta _ { \kappa D } ^ { 2 } } \right) .\tag{10.214}
$$

These expressions appear in Ref. [10] in the context of a circular tube.<sup>3</sup> In MIXCIRC the three $f ^ { \ast } \mathrm { { s } }$ are given by

$$
f _ { j } = \frac { 2 J _ { 1 } [ ( i - 1 ) R / \delta _ { j } ] } { ( i - 1 ) ( R / \delta _ { j } ) J _ { 0 } [ ( i - 1 ) R / \delta _ { j } ] } ,\tag{10.215}
$$

where $R$ is the circle radius, $r _ { h } = R / 2$ , and $j$ is $\nu , \kappa D ,$ , or $D \kappa$ . In MIXSLAB, the three f’s are given by

$$
f _ { j } = \frac { \mathrm { t a n h } [ ( 1 + i ) y _ { 0 } / \delta _ { j } ] } { ( 1 + i ) y _ { 0 } / \delta _ { j } } ,\tag{10.216}
$$

where the plate separation is $2 y _ { 0 } = 2 r _ { h }$ and j is $\nu , \kappa D$ , or $D \kappa$

The calculation of $\left. T _ { 1 } \right.$ is given by Eq. (10.221) with $d T _ { m } / d x = 0$

The head-loss pressure gradient $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ is calculated on the basis of laminar flow. See Eqs. (10.73) and (10.74).

## 10.9.2 MIXTBL, MIXTSLAB, and MIXTCIRC

## General description:

The MIXTBL, MIXTSLAB, and MIXTCIRC segments calculate $d p _ { 1 } / d x , \ d U _ { 1 } / d x , \ d n _ { L } / d x$ , and $d T _ { m } / d x$ for sound propagation in gas mixtures, with or without steady flow, according to the theory described in Ref. [70], which builds on the theory described in Refs. [45, 68, 10]. MIXTBL performs the calculations in boundary-layer approximation, MIXTSLAB in parallelplate geometry of arbitrary gap $2 y _ { 0 }$ , and MIXTCIRC in circular pores of arbitrary radius R.

The solid is assumed to be laterally ideal, so it imposes a perfect isothermal boundary condition on the oscillating temperature of the gas. This assumption would correspond to $\epsilon _ { s } = 0$ in a STK\*\* segment. However, the solid’s finite thermal conductivity in the x direction is included in the calculation of $d T _ { m } / d x$ in MIXT\*\* segments, in the same way as in STK\*\* segments.

Input variables, MIXTBL:

Area $( \mathrm { m } ^ { 2 } )$ Cross-sectional area $A _ { \mathrm { g a s } }$ available to the gas, based on inside dimensions.

Perim (m) Perimeter Π of the inside cross section described above.

Length (m) The length $\Delta x$ of the segment.

WallA $( \mathrm { m } ^ { 2 } )$ The cross-sectional area $A _ { \mathrm { s o l i d } }$ of the wall material.

Solid The material comprising the walls.

Input variables, MIXTSLAB:

Area $( \mathrm { m } ^ { 2 } )$ Total cross-sectional area A including gas and solid.

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$

Length (m) The length $\Delta x$ of the segment.

y0 (m) Half the plate spacing is $y _ { 0 }$ . Thus, $2 y _ { 0 }$ is the gap available to the gas between the plates.

Solid The material comprising the walls.

Input variables, MIXTCIRC:

Area $( \mathrm { m } ^ { 2 } )$ Total cross-sectional area A including gas and solid.

GasA/A The areal porosity $\phi = A _ { \mathrm { g a s } } / A$

Length (m) The length $\Delta x$ of the segment.

radius (m) The radius R of the pores.

Solid The material comprising the walls.

Potential targets:

None.

## Master–slave links:

The length of any of these segments can be slaved to the length of another segment to keep the sum of the two lengths constant.

(For an introduction to master–slave links, and a complete listing of linking options for all segments, see Section 2.7.2.)

## Format and examples:

1   
MIXTCIRC an array of circular pores   
2.2000E-05 a Area m^2 5637.2 A |p| Pa   
0.9100 b GasA/A 162.98 B Ph(p) deg   
0.1000 c Length m 1.4540E-03 C |U| m^3/s   
1.0000E-03 d radius m -86.581 D Ph(U) deg   
-2.6300E-08 E Htot W   
-1.4313 F Edot W   
0.3463 G nL Beg   
0.3452 H nL End   
310.00 I TBeg   
stainless Solid type 451.23 J TEnd

## Calculations:

In MIXTBL, MIXTSLAB, and MIXTCIRC, the integration variables evolve according to

$$
\frac { d T _ { m } } { d x } = \frac { \dot { H } _ { \mathrm { t o t } } - \dot { N } m w _ { m } - \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \tilde { U _ { 1 } } \left( 1 - \frac { f _ { \kappa } - \tilde { f } _ { \nu } } { ( 1 + \sigma ) ( 1 - \tilde { f } _ { \nu } ) } \right) \right] } { \frac { \rho _ { m } c _ { p } \left| U _ { 1 } \right| ^ { 2 } } { 2 \omega A _ { \mathrm { g a s } } ( 1 - \sigma ) \left| 1 - f _ { \nu } \right| ^ { 2 } } \mathrm { I m } \left[ \tilde { f } _ { \nu } + \frac { ( f _ { \kappa } - \tilde { f } _ { \nu } ) } { ( 1 + \sigma ) } \right] - A _ { \mathrm { g a s } } k - A _ { \mathrm { s o l i d } } k _ { s } } ,\tag{10.217}
$$

$$
\frac { d p _ { 1 } } { d x } = - \frac { i \omega \rho _ { m } } { ( 1 - f _ { \nu } ) A _ { \mathrm { g a s } } } U _ { 1 } ,\tag{10.218}
$$

$$
\begin{array} { r l } & { \frac { d n _ { H } } { d x } = } \\ &  \frac { \dot { N } _ { H } - n _ { H } \dot { N } - \frac { \delta _ { \mathrm { g } } } { 4 r _ { h } } \frac { ( \gamma - 1 ) k _ { T } } { \gamma R _ { \mathrm { u n i v } } T _ { m } } \left| p _ { 1 } \right| \left| U _ { 1 } \right| \left( F _ { \mathrm { t r a x } } \cos \theta + F _ { \mathrm { s t a n d } } \sin \theta \right) + \frac { \rho _ { m } } { m } \frac { k _ { T } } { T _ { m } } \frac { d T _ { m } } { d z } \left( A _ { \mathrm { g a s } } D _ { 1 2 } - \frac { \delta _ { \mathrm { g } } } { 4 r _ { h } } \frac { \left| U _ { 1 } \right| ^ { 2 } F _ { \mathrm { V } \mathrm { T } } } { \omega A _ { \mathrm { g a s } } } \right) } \\ & { \quad \quad \quad \quad \quad \frac { \rho _ { m } } { m } \left( \frac { \delta _ { \mathrm { s } } } { 4 r _ { h } } \left| U _ { 1 } \right| ^ { 2 } \frac { F _ { \mathrm { g r a d } } } { \omega A _ { \mathrm { g a s } } } - A _ { \mathrm { g a s } } D _ { 1 2 } \right) } \end{array}\tag{10.219}
$$

$$
\frac { d U _ { 1 } } { d x } ~ = ~ - i \omega A _ { \mathrm { g a s } } \left( \frac { p _ { 1 } } { p _ { m } } - \frac { \langle T _ { 1 } \rangle } { T _ { m } } + \frac { m _ { H } - m _ { L } } { m _ { \mathrm { a v g } } } \langle n _ { H , 1 } \rangle \right) + \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } U _ { 1 } - \frac { m _ { H } - m _ { L } } { m _ { \mathrm { a v g } } } \frac { d n _ { H } } { d x } U _ { 1 } ,\tag{10.220}
$$

where

$$
\frac { \left. T _ { 1 } \right. } { T _ { m } } = \frac { \gamma - 1 } { \gamma } \left[ 1 - B f _ { \nu } - C f _ { \kappa D } - \left( 1 - B - C \right) f _ { D \kappa } \right] \frac { p _ { 1 } } { p _ { m } } - \frac { \left( 1 - f _ { D \kappa } \right) } { i \omega A _ { \mathrm { g a s } } \left( 1 - f _ { \nu } \right) } \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } U _ { 1 } ,\tag{10.221}
$$

$$
\begin{array} { r l r } {  { \langle n _ { H , 1 } \rangle = } } \\ & { } & { - \frac { \gamma - 1 } { \gamma } \frac { m _ { L } } { m _ { \mathrm { a w g } } } \frac { k _ { T } } { \varepsilon } [ B ( 1 - \frac { 1 } { \sigma } ) f _ { \nu } + C ( 1 - \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { \kappa D } ^ { 2 } } ) f _ { \kappa D } + ( 1 - B - C ) ( 1 - \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { D \kappa } ^ { 2 } } ) f _ { D \kappa } ] \frac { p _ { 1 } } { p _ { m } } } \\ & { } & { - \frac { 1 } { i \omega A _ { \mathrm { g a s } } } \frac { d n _ { H } } { d x } U _ { 1 } + \frac { m _ { L } } { m _ { \mathrm { a w g } } } \frac { k _ { T } } { \varepsilon } \frac { 1 } { i \omega A _ { \mathrm { g a s } } ( 1 - f _ { \nu } ) } [ ( 1 - \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { D \kappa } ^ { 2 } } ) f _ { D \kappa } - f _ { \nu } ] \frac { 1 } { T _ { m } } \frac { d T _ { m } } { d x } U _ { 1 } , ( 1 0 . 2 2 2 ) } \end{array}
$$

and

$$
B ~ = ~ \frac { i e ^ { - i \theta } } { 1 - f _ { \nu } } \frac { \sigma } { \left( 1 - \sigma \right) \left( 1 - \sigma L \right) - \varepsilon \sigma } \left[ \left( \sigma L - 1 \right) \frac { d T _ { m } / d x } { \nabla T _ { \mathrm { c r i t } } } + \varepsilon \frac { d n _ { H } / d x } { \nabla n _ { \mathrm { c r i t } } } \right] ,\tag{10.223}
$$

$$
{ \cal C } ~ = ~ { \frac { \sqrt { L } \delta _ { \kappa D } - \delta _ { D \kappa } } { \left( 1 + \sqrt { L } \right) \left( \delta _ { \kappa D } - \delta _ { D \kappa } \right) } } \left[ 1 - B \left( 1 - { \frac { 1 - \sigma } { \sqrt { \sigma } } } { \frac { \delta _ { \kappa } } { \sqrt { L } \delta _ { \kappa D } - \delta _ { D \kappa } } } \right) + \right.
$$

$$
+ \frac { i e ^ { - i \theta } } { 1 - f _ { \nu } } ( 1 + \sqrt { \sigma } \frac { \delta _ { \kappa } } { \sqrt { L } \delta _ { \kappa D } - \delta _ { D \kappa } } ) \frac { d T _ { m } / d x } { \nabla T _ { \mathrm { c r i t } } } ] ,\tag{10.224}
$$

$$
\nabla T _ { \mathrm { c r i t } } = \frac { \gamma - 1 } { \gamma } \frac { | p _ { 1 } | } { p _ { m } } \frac { \omega A _ { \mathrm { g a s } } } { | U _ { 1 } | } T _ { m } ,\tag{10.225}
$$

$$
\nabla n _ { \mathrm { c r i t } } = \frac { \gamma - 1 } { \gamma } \frac { | p _ { 1 } | } { p _ { m } } \frac { \omega A _ { \mathrm { g a s } } } { | U _ { 1 } | } k _ { T } .\tag{10.226}
$$

In addition to the usual definitions of the viscous and thermal penetration depths $\delta _ { \nu } =$ $\sqrt { 2 \mu / \omega \rho _ { m } }$ and $\delta _ { \kappa } = \sqrt { 2 k / \omega \rho _ { m } c _ { p } }$ , two new penetration depths are defined for mixtures:

$$
\delta _ { \kappa D } ^ { 2 } \ = \ \frac 1 2 \delta _ { \kappa } ^ { 2 } \left[ 1 + \left( 1 + \varepsilon \right) / L + \sqrt { \left[ 1 + \left( 1 + \varepsilon \right) / L \right] ^ { 2 } - 4 / L } \right] ,\tag{10.227}
$$

$$
\delta _ { D \kappa } ^ { 2 } = \frac { 1 } { 2 } \delta _ { \kappa } ^ { 2 } \left[ 1 + \left( 1 + \varepsilon \right) / L - \sqrt { \left[ 1 + \left( 1 + \varepsilon \right) / L \right] ^ { 2 } - 4 / L } \right] ,\tag{10.228}
$$

where

$$
\varepsilon = \frac { \gamma - 1 } { \gamma } \frac { k _ { T } ^ { 2 } } { n _ { L } \left( 1 - n _ { L } \right) } ,\tag{10.229}
$$

$k _ { T }$ is the thermal difusion ratio, $L = k / \rho _ { m } c _ { p } D _ { 1 2 }$ , and $D _ { 1 2 }$ is the binary mass-difusion coeficient.

For MIXTBL,

$$
f _ { j } = ( 1 - i ) \frac { \delta _ { j } } { 2 r _ { h } } ,\tag{10.230}
$$

where $j$ is $\nu , \kappa , \kappa D$ , or $D \kappa$ and $r _ { h }$ is the hydraulic radius, and the four $F ^ { \prime } \mathrm { s }$ are given by

$$
F _ { \mathrm { t r a v } } = \frac { \sigma \sqrt { \sigma L } - \sqrt { \sigma } - \sigma \sqrt { L } \left( \delta _ { \kappa D } / \delta _ { \kappa } + \delta _ { D \kappa } / \delta _ { \kappa } \right) } { \left( 1 + \sqrt { L } \right) \left[ ( 1 + \sigma ) ( 1 + \sigma L ) + \varepsilon \sigma \right] } ,\tag{10.231}
$$

$$
F _ { \mathrm { s t a n d } } = \frac { - \sigma \sqrt { \sigma L } + \sqrt { \sigma } - \sigma \sqrt { L } \left( \delta _ { \kappa D } / \delta _ { \kappa } + \delta _ { D \kappa } / \delta _ { \kappa } \right) } { \left( 1 + \sqrt { L } \right) \left[ \left( 1 + \sigma \right) \left( 1 + \sigma L \right) + \varepsilon \sigma \right] } ,\tag{10.232}
$$

$$
\begin{array} { r l } & { F _ { \mathrm { g r a d } } = } \\ & { \qquad \frac { \sqrt { \sigma } L \left( 1 - \sigma ^ { 2 } \right) \left( 1 + \sqrt { L } \right) + \varepsilon \sqrt { \sigma } \left( \sqrt { L } - 1 \right) + \left[ \left( \sigma ^ { 2 } - 1 \right) L + \varepsilon \sigma \sqrt { L } \right] \left( \delta _ { \kappa D } / \delta _ { \kappa } + \delta _ { D \kappa } / \delta _ { \kappa } \right) } { \left( 1 + \sqrt { L } \right) \left[ \left( 1 + \sigma \right) \left( 1 + \sigma L \right) + \varepsilon \sigma \right] \left[ \left( 1 - \sigma \right) \left( 1 - \sigma L \right) - \varepsilon \sigma \right] / \sigma } , } \end{array}\tag{10.233}
$$

$$
\begin{array} { r l } & { - F _ { \nabla T } = } \\ & { \frac { { \sqrt { \sigma T } \left( 1 + \sqrt { L } \right) \left( 1 + \sigma ^ { 2 } \sqrt { L } \right) + \sigma ^ { \frac { 3 } { 2 } } L + \varepsilon \sqrt { \sigma } - \frac { 1 } { \sqrt { \sigma } } + \left[ \sqrt { L } \left( 1 - \sigma L - \varepsilon \sigma \right) - \sigma L \left( 1 + \sigma \right) \right] \left( \frac { \delta _ { \kappa , D } } { \delta _ { \kappa } } + \frac { \delta _ { D \kappa } } { \delta _ { \kappa } } \right) } } { { \left( 1 + \sqrt { L } \right) \left[ \left( 1 + \sigma \right) \left( 1 + \sigma L \right) + \varepsilon \sigma \right] \left[ \left( 1 - \sigma \right) \left( 1 - \sigma L \right) - \varepsilon \sigma \right] / \sigma } } . } \end{array}\tag{10.234}
$$

In MIXTSLAB and MIXTCIRC, DeltaEC uses the following expressions:

$$
F _ { \mathrm { t r a v } } ~ = ~ - \frac { 2 r _ { h } } { \delta _ { \kappa } } \mathrm { R e } \left[ \frac { G } { \left( 1 - \tilde { f } _ { \nu } \right) } \right] ,\tag{10.235}
$$

(10.236)

$$
\begin{array} { r c l } { { F _ { \mathrm { g r a d } } } } & { { = } } & { { \displaystyle - \frac { 2 r _ { h } } { \delta _ { \star } } \frac { 1 } { \left| 1 - f _ { \nu } \right| ^ { 2 } } \frac { \sigma } { \left( 1 - \sigma \right) \left( 1 - \sigma L \right) - \varepsilon \sigma } } } \\ { { } } & { { } } & { { \displaystyle \cdot \mathrm { I m } \left[ \frac { \left( 1 - \sigma \right) } { \sigma S } f _ { \nu } \left( \frac { \delta _ { \kappa } ^ { 2 } - \delta _ { \kappa D } ^ { 2 } } { \delta _ { \nu } ^ { 2 } + \delta _ { \kappa D } ^ { 2 } } f _ { \kappa D } - \frac { \delta _ { \kappa } ^ { 2 } - \delta _ { D \kappa } ^ { 2 } } { \delta _ { \nu } ^ { 2 } + \delta _ { D \kappa } ^ { 2 } } f _ { D \kappa } + \frac { \left( 1 + \sigma \right) L Q } { M } \tilde { f } _ { \nu } + S \right) + \varepsilon G \right] , } } \end{array}\tag{10.237}
$$

$$
\begin{array} { r c l } { { F _ { \nabla T } } } & { { = } } & { { \displaystyle \frac { 2 r _ { h } } { \delta _ { \kappa } } \frac { 1 } { | 1 - f _ { \nu } | ^ { 2 } } \frac { \sigma } { ( 1 - \sigma ) \left( 1 - \sigma L \right) - \varepsilon \sigma } } } \\ { { } } & { { } } & { { \cdot \mathrm { I m } \left[ \frac { f _ { \nu } } { S } \left( \frac { \delta _ { \kappa } ^ { 2 } - \delta _ { \kappa D } ^ { 2 } } { \delta _ { \nu } ^ { 2 } + \delta _ { \kappa D } ^ { 2 } } f _ { \kappa D } - \frac { \delta _ { \kappa } ^ { 2 } - \delta _ { D \kappa } ^ { 2 } } { \delta _ { \nu } ^ { 2 } + \delta _ { D \kappa } ^ { 2 } } f _ { D \kappa } + \frac { \left( 1 + \sigma \right) L Q } { M } \tilde { f } _ { \nu } + S \right) + \frac { 1 - \sigma L - \varepsilon \sigma } { \sigma } G \right] , } } \end{array}\tag{10.238}
$$

where $r _ { h }$ is the hydraulic radius and

$$
\begin{array} { r c l } { S } & { = } & { \left( \displaystyle \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { D \kappa } ^ { 2 } } - 1 \right) f _ { D \kappa } - \left( \displaystyle \frac { \delta _ { \kappa } ^ { 2 } } { \delta _ { \kappa D } ^ { 2 } } - 1 \right) f _ { \kappa D } , } \end{array}\tag{10.239}
$$

$$
Q ~ = ~ { \frac { \delta _ { \kappa D } ^ { 2 } - \delta _ { D \kappa } ^ { 2 } } { \delta _ { \kappa } ^ { 2 } } } ,\tag{10.240}
$$

$$
\begin{array} { l l l } { { M } } & { { = } } & { { ( 1 + \sigma ) ( 1 + \sigma L ) + \varepsilon \sigma , } } \end{array}\tag{10.241}
$$

$$
G ~ = ~ \frac { \sigma L Q } { M S } f _ { \kappa D } f _ { D \kappa } + \frac { \tilde { f } _ { \nu } } { S } \left( \frac { f _ { \kappa D } } { 1 + \delta _ { \nu } ^ { 2 } / \delta _ { D \kappa } ^ { 2 } } - \frac { f _ { D \kappa } } { 1 + \delta _ { \nu } ^ { 2 } / \delta _ { \kappa D } ^ { 2 } } \right) .\tag{10.242}
$$

These expressions appear in Refs. [10, 70] in the context of a circular tube.

In MIXTCIRC the three $f \mathrm { ^ { \prime } s }$ are given by

$$
f _ { j } = \frac { 2 J _ { 1 } [ ( i - 1 ) R / \delta _ { j } ] } { ( i - 1 ) ( R / \delta _ { j } ) J _ { 0 } [ ( i - 1 ) R / \delta _ { j } ] } ,\tag{10.243}
$$

where $R$ is the circle radius, $r _ { h } = R / 2$ , and $j$ is $\nu , \kappa D$ , or $D \kappa$

In MIXTSLAB, the three $f \mathrm { ^ { \prime } s }$ are given by

$$
f _ { j } = \frac { \mathrm { t a n h } [ ( 1 + i ) y _ { 0 } / \delta _ { j } ] } { ( 1 + i ) y _ { 0 } / \delta _ { j } } ,\tag{10.244}
$$

where the plate separation is $2 y _ { 0 } = 2 r _ { h }$ and $j$ is $\nu , \kappa D$ , or $D \kappa$

The head-loss pressure gradient dp<sub>2,0,DEC</sub>/dx is calculated on the basis of laminar flow in MIXT\*\* segments. See Eqs. (10.73) and (10.74).

## 11. Logistical segments

Details about DeltaEC’s physically realistic thermoacoustics segments were described in Chapter 10. Here, we detail the logistical segments, which perform only trivial computations or no computations but are used to coordinate other segments, impose boundary conditions, and display non-standard results.

The behavior of some of these segments depends on whether the DeltaEC model using the segments is pure acoustics or thermoacoustics or includes nonzero $\dot { N }$ or includes separation efects in gas mixtures. The discussion of $\dot { N } _ { L }$ and $n _ { L }$ only applies when MIX\*\* segments and gas mixtures are in use. The discussion of $\dot { N }$ and $p _ { \mathrm { 2 , 0 , D E C } }$ only applies when nonzero time-averaged flow is involved. Users who are interested only in acoustics can focus entirely on $p _ { 1 }$ and $U _ { 1 }$ here, and can safely ignore all discussion of H,<sup>˙</sup> $T _ { m } , \dot { N } , p _ { 2 , 0 , \mathrm { D E C } } , \dot { N } _ { L }$ , and $n _ { L }$

An alphabetical listing of segments is in the Segment Index at the end of the Users Guide.

## 11.1 Starting and ending

## 11.1.1 TITLE

## General description:

TITLE has no numerical inputs. It automatically appears at the very beginning of a DeltaEC file, and its heading and (optional) notes should be descriptive, to remind the user what the file is about.

## Format and examples:

engine2006-d July 2006 engine with Karen’s modifications.

## 11.1.2 BEGIN

## General description:

After the TITLE segment, BEGIN is counted as the zeroth segment of the file. It is used to initialize “global” variables that are shared among subsequent segments (e.g., frequency and mean pressure) and the integration variables required by each pass of DeltaEC to get started (e.g., real and imaginary parts of $p _ { 1 }$ and $U _ { 1 } )$

BEGIN segments can be used anywhere in a DeltaEC file, to set any or all of DeltaEC’s integration variables or global variables to new values. This can be useful for packing two or more related DeltaEC models into a single file or for changing from one gas to another in the middle of a model. (Do not use such a BEGIN within a teebranch; instead, use RPN “change” assignments to set or reset variables in a teebranch.) When more than one BEGIN is used in a model, each BEGIN starts a new leg. (Legs are described in Section 11.2.1.)

BEGIN causes subsequent DUCTs, CONEs, SURFACEs, and IMPEDANCEs to set $\dot { H } _ { \mathrm { t o t , o u t } } ~ =$ $\dot { H } _ { \mathrm { t o t , i n } } ,$ so the user should imagine such segments to be thermally insulated. ANCHOR, described in Section 11.3.1, can be used to override this default, and the user should imagine segments downstream of ANCHOR to be attached to a heat sink at the local temperature $T _ { m }$ (ANCHOR is useful for very low power systems and simple systems where total energy flow is irrelevant, and of course for systems with DUCTs and other components that actually are well-attached to a heat sink.)

## Input variables:

Mean P (Pa) The mean pressure of the gas, $p _ { m }$ .

Freq (Hz) The frequency f of the sinusoidal oscillations in subsequent segments. Most equations in the Users Guide use $\omega = 2 \pi f$

TBeg (K) The initial temperature $T _ { m }$ of the gas.

|p| (Pa) The initial value of $| p _ { 1 } |$

Ph(p) (deg) The initial phase of $p _ { 1 }$ .

|U| $\mathrm { ( m ^ { 3 } / s ) }$ The initial value of $| U _ { 1 } |$

Ph(U) (deg) The initial phase of $U _ { 1 }$

Gas The gas type, e.g., helium or air.

Default Htot / Other Htot (W) With this choice in the Optional Parameters dialog, the user can let DeltaEC assign the default value to the total energy flow $\dot { H } _ { \mathrm { t o t } }$ or can assign a numerical value or let it be a guess.

Enable Ndot / Disable Ndot This check box in the Optional Parameters dialog controls some calculations and results in many subsequent segments.

Ndot (mol/s) If “Enable Ndot” is checked, the user can specify or guess the steady molar flow rate $\dot { N }$

nL If the gas type is a gas mixture, this parameter initializes the light-component mole fraction $n _ { L }$

Bulk NLdot / Other NLdot (mol/s) If the gas type is a gas mixture, this check box in the Optional Parameters dialog controls whether DeltaEC assigns the default, bulk value to the light component’s steady molar flow rate $\dot { N } _ { L }$ or lets the user assign a diferent value.

or mples:   
BEGIN This example is the minimal format, as saved in an out file.   
1.0e6 Pa a Mean P   
500. Hz b Freq   
300. K c TBeg   
3.0e4 Pa d |p|   
0.00 deg e Ph(p)   
0.00 m3/s f |U|   
0.00 deg g Ph(U)   
helium Gas type   
BEGIN This example is the most complicated possible format, as saved in an out file.   
1.0e6 Pa a Mean P   
500. Hz b Freq   
300. K c TBeg   
3.0e4 Pa d |p|   
0.00 deg e Ph(p)   
0.00 m3/s f |U|   
0.00 deg g Ph(U)   
2000. h Htot   
1.00E-8 i Ndot   
0.800 j nL   
1.00E-9 k NLdot   
HeAr Gas type   
TITLE Argon cover on top of sodium-potassium column, illustrating two BEGINs in on   
!->2beg.out   
!Created@10:20:31 29-Mar-07 with DeltaE Vers. 6.0g7 for the IBM/PC-Compatible   
1.   
BEGIN Initialize in the argon   
1.0000E+05 a Mean P Pa 3.9676E-05 A |U| G( 0f) P   
100.00 b Freq Hz 87.799 B Ph(U) G( 0g) P   
400.00 c TBeg K   
1000.0 d |p| Pa   
0.0000 e Ph(p) deg   
3.9676E-05 f |U| m^3/s G   
87.799 g Ph(U) deg G   
0.0000 h Htot W   
0.0000 j nL   
HeAr Gas type   
1   
DUCT the argon on top   
1.0000E-04 a Area m^2 S= -2 1015.7 A |p| Pa   
3.5449E-02 b Perim m Fn( 1a) -7.9065E-02 B Ph(p) deg   
0.1000 c Length m 1.9924E-08 C |U| m^3/s   
89.527 D Ph(U) deg   
0.0000 E Htot W   
ideal Solid type 6.9504E-08 F Edot W   
1--: 2   
BEGIN transition from argon to Na-K   
sameas 0a a Mean P Pa   
sameas 0b b Freq Hz   
sameas 0c c TBeg K   
sameas 1A d |p| Pa   
sameas 1B e Ph(p) deg   
sameas 1C f |U| m^3/s   
sameas 1D g Ph(U) deg   
sameas 1E h Htot W   
NaK-78 Gas type   
!-- 3   
DUCT The sodium-potassium column   
sameas 1a a Area m^2 1069.7 A |p| Pa   
sameas 1b b Perim m -0.1210 B Ph(p) deg   
1.0000 c Length m 3.7365E-13 C |U| m^3/s   
-0.1156 D Ph(U) deg   
0.0000 E Htot W   
ideal Solid type 1.9984E-10 F Edot W   
4   
SURFACE Bottom end

None.

## Format and examples:

sameas 1a a Area m^2 1069.7 A |p| Pa   
-0.1210 B Ph(p) deg   
3.5753E-17 C |U| m^3/s   
83.367 D Ph(U) deg   
0.0000 E Htot W   
ideal Solid type 2.1686E-15 F Edot W   
1- 5   
HARDEND terminate in the liquid metal   
0.0000 a R(1/z) = 5G? 1069.7 A |p| Pa   
0.0000 b I(1/z) = 5H? -0.1210 B Ph(p) deg   
3.5753E-17 C |U| m^3/s   
83.367 D Ph(U) deg   
0.0000 E Htot W   
2.1686E-15 F Edot W   
6.3787E-11 G R(1/z)   
5.5883E-10 H I(1/z)

## Calculations:

BEGIN establishes initial values of $p _ { m } , \ f , T _ { m } , p _ { 1 } , U _ { 1 } , \ \dot { H } _ { 2 , k } , \ \dot { N }$ , and (if applicable) $n _ { L }$ and $\dot { N } _ { L }$ . It establishes the gas type. Unless subsequently overridden by an ANCHOR segment, it establishes “insulate” mode, efectively putting thermal insulation around all subsequent segments except heat exchangers.

If Htot is omitted from the <.out> file, or if the “Default Htot” box is checked in the Optional Parameters dialog in the user interface, BEGIN sets an initial value of

$$
\dot { H } _ { \mathrm { t o t } } = \dot { E } + \dot { N } m w _ { m } ,\tag{11.1}
$$

which implies that $\dot { H } _ { 2 , k } = \dot { E }$ . Otherwise, Htot is an ordinary input parameter, which can be set by the user or guessed.

If the “Disable Ndot” box is checked in the Optional Parameters dialog or the Ndot input parameter is missing from the <.out> file, DeltaEC assigns $\dot { N } = 0$ , skips all subsequent $p _ { \mathrm { 2 , 0 , D E C } }$ calculations, and ignores any possible efect of nonzero $\dot { N } _ { 2 , 0 }$ on $d p _ { 1 } / d x$ If the “Enable Ndot” box is checked, $p _ { \mathrm { 2 , 0 , D E C } }$ is initialized to zero and its dependence on x is calculated in all subsequent segments. This also allows input parameter $\dot { N }$ to appear in BEGIN, and allows other input and output parameters that are relevant to steady flow to appear in subsequent segments. When this box is checked, nonnegligible $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ and nonlinear efects on $d p _ { 1 } / d x$ can occur in subsequent segments even if $\dot { N } \simeq 0$ , because of the diference between $\dot { N }$ and $\dot { N } _ { 2 , 0 }$ described in Eq. (8.16).

If the gas type is a binary mixture, the initial mole fraction of the light component, $n _ { L }$ appears as an input parameter, which can only change in MIX\*\* segments or be reassigned using =nL in an RPN segment downstream.

Other, less commonly used variables are invisibly initialized in BEGIN:

$\angle \mathrm { T } 1 > = T _ { m } \beta p _ { 1 } / \rho _ { m } c _ { p }$ , described in Section 11.4.1.

vol = 0, described in Section 11.4.1.

$F _ { 1 } = 0$ , described in Section 11.4.1.

Tzero = 300 Kelvin, described above Eq. (6.3) in the context of $\dot { H }$ and below Eq. (8.9) in the context of $\dot { X }$

nLzero = 0.5, described below Eq. (8.9) in the context of $\dot { X }$

$\dot { N } _ { L } = n _ { L } \dot { N }$ , if the gas is a binary gas mixture and the “Bulk NLdot” box is checked. $T _ { \mathrm { s o l i d } } = T _ { m }$

## 11.1.3 HARDEND and SOFTEND

## General description:

Often, the final segment (except possibly RPN segments) will be either HARDEND or SOFTEND.   
These contain three or four potential targets.

HARDEND targets are appropriate when the user wants the complex volume flow rate somewhere to be zero. This is the usual case at the end of a closed thermoacoustic system. HARDEND is also often used at the end of a closed, sealed TBRANCH.

SOFTEND targets are appropriate when the user wants the complex pressure amplitude somewhere to be zero. This is often useful for symmetrical systems, where SOFTEND indicates that the remainder of the apparatus is a mirror image of what is in the <.out> file and forces a complex-pressure node. Also use the SOFTEND segment, but without using its targets, to signal the end of a TBRANCHed sequence of segments that will be reattached elsewhere at a UNION, or anywhere that a leg must end with circumstances that can best be defined using custom-made RPN targets.

Either \*\*END segment can also be targeted to enforce a non-trivial impedance at the end of a branch or a model. An example of SOFTEND to model the radiation impedance from an open-ended tube is shown on the next page.

The third default target in these segments, $\dot { H } _ { \mathrm { t o t } }$ , can be targeted to zero to represent thermal insulation at a HARDEND or the energy aspect of a mirror-image symmetry location in SOFTEND.

In both \*\*ENDs, the complex specific impedances are made dimensionless by dividing by $\rho _ { m } a$ evaluated at the local temperature.

Disabling the targets in \*\*ENDs is often useful in debugging a new model that doesn’t readily converge. Set these targets nonzero to model a known, nonzero end impedance—or use BRANCH (followed by a zero-targeted HARDEND) to work with Z instead of $z / \rho a$

## Input variables:

None.

## Potential targets, HARDEND:

R(1/z) If targeted, this number is compared with DeltaEC’s calculation of the real part of the inverse of the normalized specific impedance, $\operatorname { R e } [ 1 / z _ { n } ]$ , at the HARDEND.

I(1/z) If targeted, this number is compared with DeltaEC’s calculation of the imaginary part of the inverse of the normalized specific impedance, Im $[ 1 / z _ { n } ]$ , at the HARDEND.

Htot (W) Total energy flow $\dot { H } _ { \mathrm { t o t } }$ . This potential target appears in insulated mode. If targeted, this number is compared with DeltaEC’s calculation of $\dot { H } _ { \mathrm { t o t } }$ at the HARDEND.

Ndot (mol/s) Steady molar flow rate $\dot { N }$ . This potential target appears when “Enable Ndot” is checked in an upstream BEGIN. If targeted, this number is compared with DeltaEC’s calculation of $\dot { N }$ at the HARDEND. Useful only in rare circumstances.

## Potential targets, SOFTEND:

R(z) If targeted, this number is compared with DeltaEC’s calculation of the real part of the normalized specific impedance, $\mathrm { R e } [ z _ { n } ]$ , at the SOFTEND.

I(z) If targeted, this number is compared with DeltaEC’s calculation of the imaginary part of the normalized specific impedance, Im[z<sub>n</sub>], at the SOFTEND.

Htot (W) Total energy flow $\dot { H } _ { \mathrm { t o t } }$ . This potential target appears in insulated mode. If targeted, this number is compared with DeltaEC’s calculation of $\dot { H } _ { \mathrm { t o t } }$ at the SOFTEND.

Master–slave links:

None.

Format and examples:

```csv
97
HARDEND looks like this if steady-flow calculations are turned off 1
0.000 R(1/z)
0.000 I(1/z)
0.000 Htot
!- 40
DUCT final resonator tube, open to the room
8.0000E-4 a Area m^2 Mstr 1023.8 A |p| Pa
0.10027 b Perim m 40a -0.95235 B Ph(p) deg
3.1783E-2 c Length m G 2.2366E-2 C |U| m^3/s
5.0000E-4 d Srough -87.544 D Ph(U) deg
0.68065 E Htot W
ideal Solid type 0.68065 F Edot W
!- 41
RPN calc radius from area
0.0000 a G or T 0.1461 A kr
1.5958E-2 B m rad
40a pi / sqrt ; # w * a /
!-- 42
RPN radiation impedance from open tube / (rho a / A)
! Levine and Schwinger, Phys Rev 73, 383-406 (1948)
! but see also Dalmont, Nederveen, and Joly, J. Sound Vib.
244, 505-534 (2001).
! Z = rho a / A times z ;
! z = (kr)^2 / 4 + j 0.6133 kr
0.0000 a G or T 5.3360E-3 A Re(z)
8.9601E-2 B Im(z)
0.6133 41A * ; 41A sqrd 4 /
1- 43
SOFTEND radiate sound into 4 pi solid angle in the room
! Note: z calc here uses closest upstream area (40a) internally AND via RPN 41A
sameas 42A a Re(z) =43G 1023.8 A |p| Pa
sameas 42B b Im(z) =43H -0.95235 B Ph(p) deg
0.0000 c Htot W 2.2366E-2 C |U| m^3/s
-87.544 D Ph(U) deg
0.68065 E Htot W
0.68065 F Edot W
5.3360E-3 G Re(z)
8.9601E-2 H Im(z)
293.00 I T K
```

## Calculations:

The normalized impedance in HARDEND and SOFTEND is calculated according to

$$
z _ { n } = \frac { A p _ { 1 } } { \rho _ { m } a U _ { 1 } } ,\tag{11.2}
$$

with A from the most recent segment having an area (or $A = 1 0 ^ { - 6 } ~ \mathrm { m ^ { 2 } }$ if no such segment exists), and with $\rho _ { m }$ and a evaluated at the local $T _ { m }$

## 11.2 Structured branches and unions

Figure 11.1 shows how TBRANCH and UNION can be used to model complicated branched and multiply-connected thermoacoustic equipment.

![[mu_66afccee_c8f61c3895a249b9cf57.jpg]]  
Figure 11.1: (a) Example of an 18-segment DeltaEC model of a linear array of thermoacoustic components. (b) Example of a model of a multiply-branched apparatus. (c) Example of a model of a multiply-connected apparatus. Line a of UNION 17 must point to SOFTEND 13, line a of UNION 31 must point to SOFTEND 20, and line a of UNION 32 must point to SOFTEND 26.

## 11.2.1 TBRANCH

## General description:

Use TBRANCH for branched systems that are too complicated for BRANCH or OPNBRANCH.

When it encounters a TBRANCH, DeltaEC treats subsequent segments as the sequential members of a side branch (which we call a “teebranch” in the Users Guide), until it reaches a HARDEND or SOFTEND. Then it “returns to the trunk,” treating the rest of the segments as trunk members. The HARDEND termination of a teebranch is appropriate for a closed-end leg. The SOFTEND termination of a teebranch is appropriate for later reconnection to the trunk at a UNION in the trunk.

To manage the plotter display of results from models with one or more TBRANCHes, the <.sp> file’s initial column, “leg number,” is incremented each time a TBRANCH or BEGIN is encountered, and decremented when a SOFTEND or HARDEND is encountered. The user can display plots of one or more selected legs, suppressing results from uninteresting legs.

The complex impedance in the TBRANCH segment tells DeltaEC how to split up the volume flow rate between the teebranch and the trunk. Usually this complex impedance is used as two guesses to hit two downstream targets, often either complex $1 / z _ { n }$ in a HARDEND at the end of a dead-ended teebranch or complex $p _ { 1 }$ at a subsequent UNION for a multiplyconnected teebranch. Unless ANCHOR appears upstream, HtotBr tells DeltaEC how to split up the total power $\dot { H } _ { \mathrm { t o t } }$ between the branch and the trunk. This is often used as a guess to hit a downstream temperature target, such as at a UNION. The parameter NdotBr tells DeltaEC how to split any nonzero time-averaged molar flow N<sup>˙</sup> between the branch and the trunk. Similarly, NLdotB specifies the portion of the time-averaged mole flux of the lighter component of a mixture, $\dot { N } _ { L }$ , that goes into the branch.

For duct networks in which temperature is constant and $p _ { 1 }$ and $U _ { 1 }$ are the only integration variables of interest, use ANCHOR after the BEGIN segment, so TBRANCH will not worry about how to split $\dot { H } _ { \mathrm { t o t } }$ and UNION will not think of temperature as a potential default target.

Nested teebranches are allowed, as shown in Figs. 11.1(b) and (c). However, never use a BEGIN segment within a teebranch to re-initialize variables.

The incoming values of the RPN variables F1 and vol are retained for the trunk, and these variables are initialized to zero for the teebranch.

## Input variables:

Re(Zb) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The real part of the branch impedance $Z _ { \mathrm { b r } }$

Im(Zb) $\left( \mathrm { P a { \cdot } s / m ^ { 3 } } \right)$ The imaginary part of the branch impedance $Z _ { \mathrm { b r } }$

HtotBr (W) This optional input variable, $\dot { H } _ { \mathrm { b r } }$ , can be used in insulated mode. It specifies how much total power flows into the teebranch. The default value is equal to $\dot { E } _ { \mathrm { b r } } +$ $\dot { N } _ { \mathrm { b r } } m w _ { m }$ , which is simply $\dot { E } _ { \mathrm { b r } }$ when there is no steady flow.

NdotBr (mol/s) This input variable, $\dot { N } _ { \mathrm { b r } }$ , appears when “Enable Ndot” is checked in an upstream BEGIN. It specifies how much steady flow goes into the teebranch.

NLdotB (mol/s) This input variable, $\dot { N } _ { L , \mathrm { b r } }$ , appears when “Enable Ndot” is checked in an upstream BEGIN and when a gas mixture and MIX\*\* segments are in use. It specifies how much steady flow of the light component of the mixture goes into the teebranch. The default value represents bulk flow into the branch, $\dot { N } _ { L , \mathrm { b r } } = n _ { L } \dot { N } _ { \mathrm { b r } }$

## Potential targets:

None.

## Master–slave links:

The imaginary part of the branching impedance can be linked to the real part in two possible ways: to preserve either the magnitude or the phase while the real part is changed.

(For an introduction to master–slave links, and a complete listing of these link options for all segments, see Section 2.7.2.)

## Format and examples:

TBRANCH the fork in the road, in the default "insulated" mode   
4.412E+07 a Re(Zb) Pa-s/m^3 G   
-3.528E+06 b Im(Zb) Pa-s/m^3 G   
0.49 c HtotBr G   
TBRANCH the fork in the road, if "ANCHOR" segment appears somewhere upstream   
4.412E+07 a Re(Zb) Pa-s/m^3 G   
-3.528E+06 b Im(Zb) Pa-s/m^3 G

## Calculations:

The TBRANCH segment leaves $T _ { m } , p _ { 1 }$ , and p<sub>20DEC</sub> unchanged. Other variables change according to

$$
\begin{array} { r l r } { U _ { 1 , \mathrm { b r } } } & { = } & { p _ { 1 } / Z _ { \mathrm { b r } } , } \end{array}\tag{11.3}
$$

$$
\begin{array} { r c l } { U _ { \mathrm { 1 , t r u n k } } } & { = } & { U _ { \mathrm { 1 , i n } } - U _ { \mathrm { 1 , b r } } , } \end{array}\tag{11.4}
$$

$$
\begin{array} { r c l } { \dot { H } _ { \mathrm { b r } } } & { = } & { \dot { H } _ { \mathrm { b r } } , } \end{array}\tag{11.5}
$$

$$
\dot { H } _ { \mathrm { t r u n k } } = \dot { H } _ { \mathrm { i n } } - \dot { H } _ { \mathrm { b r } } ,\tag{11.6}
$$

$$
\begin{array} { r c l } { \dot { N } _ { \mathrm { b r } } } & { = } & { \dot { N } _ { \mathrm { b r } } , } \end{array}\tag{11.7}
$$

$$
\dot { N } _ { \mathrm { t r u n k } } = \dot { N } _ { \mathrm { i n } } - \dot { N } _ { \mathrm { b r } } ,\tag{11.8}
$$

$$
\begin{array} { r c l } { \dot { N } _ { L , \mathrm { b r } } } & { = } & { \dot { N } _ { L , \mathrm { b r } } , } \end{array}\tag{11.9}
$$

$$
\dot { N } _ { L , \mathrm { t r u n k } } = \dot { N } _ { L , \mathrm { i n } } - \dot { N } _ { L , \mathrm { b r } } ,\tag{11.10}
$$

$$
F _ { 1 , \mathrm { b r } } \quad = \quad 0 ,\tag{11.11}
$$

$$
\begin{array} { r c l } { { F _ { 1 , \mathrm { t r u n k } } } } & { { = } } & { { F _ { 1 , \mathrm { i n } } , } } \end{array}\tag{11.12}
$$

$$
\mathrm {  ~ \ v o l _ { \mathrm { b r } } ~ } = ~ 0 ,\tag{11.13}
$$

$$
\mathrm { v o l } _ { \mathrm { t r u n k } } \ = \ \mathrm { v o l } _ { \mathrm { i n } } .\tag{11.14}
$$

TBRANCH has an extra output, EdotTr, to display the acoustic power flowing past the branch in the trunk.

## 11.2.2 UNION

## General description:

A UNION is used in concert with a TBRANCH and a SOFTEND somewhere upstream, to create loops of segments as illustrated in Fig. 11.1(c). In this arrangement, when it encounters a TBRANCH, DeltaEC treats subsequent segments as the sequential members of a branch until it reaches a SOFTEND; then it “returns to the trunk,” treating the rest of the segments as trunk members. Subsequently, a UNION segment in the trunk tells DeltaEC where to connect the teebranch’s SOFTEND back to the trunk.

When reconnected with a UNION, the teebranch’s SOFTEND potential impedance targets should not be used; instead, enable the UNION’s targets to ensure that $p _ { 1 }$ (complex) at the UNION is equal to $p _ { 1 }$ (complex) at the SOFTEND of the teebranch. Often, guessing the teebranch impedance determines how the (complex) volume flow rate splits up at the TBRANCH and allows the complex $p _ { 1 }$ target at the UNION to be met.

In all but the simplest acoustic duct network, additional potential targets can be used at a UNION to properly tie the teebranch’s SOFTEND to the trunk at the UNION with continuity of relevant variables. These include $T _ { m } , p _ { 2 , \mathrm { 0 , D E C } }$ , and $n _ { L }$

UNION targets are unusual, because their target values are dynamically rewritten by DeltaEC during each iteration, so they always reflect the current result at the referenced SOFTEND. (When the user enables a UNION’s target, the target input parameters, e.g., magnitude and phase of pressure, can be initialized to any values, because DeltaEC will overwrite them during each integration pass with the current magnitude and phase of pressure at the referenced SOFTEND via automatic sameas links from the UNION to the SOFTEND.)

Oscillating volume flow rates are added at the UNION, as are time-averaged energy flows and mole fluxes. The RPN variables F1 and vol are also added.

When TBRANCH and UNION are used for duct networks, where temperature is constant and hence $p _ { 1 }$ and $U _ { 1 }$ are the only variables of interest, an ANCHOR segment upstream of the TBRANCH will eliminate confusion that might arise from the display of uninteresting, irrelevant variables.

## Input variables:

SegNum The segment number of a SOFTEND, upstream of the UNION, which terminates a teebranch and which should be connected to the trunk here. See Fig. 11.1(c).

## Potential targets:

|p|Sft (Pa) If used as a target, DeltaEC’s shooting method compares its calculation of $| p _ { 1 } |$ here in the trunk with its calculation of $| p _ { 1 } |$ at the SOFTEND identified by SegNum. DeltaEC updates the value of this variable continuously.

Ph(p)S (deg) If used as a target, DeltaEC’s shooting method compares its calculation of the phase of $p _ { 1 }$ here in the trunk with its calculation of the phase of $p _ { 1 }$ at the SOFTEND identified by SegNum. DeltaEC updates the value of this variable continuously.

TSoft (K) This potential target appears in insulated mode. If used as a target, DeltaEC’s shooting method compares its calculation of $T _ { m }$ here in the trunk with its calculation of $T _ { m }$ at the SOFTEND identified by SegNum. DeltaEC updates the value of this variable continuously.

p20DES (Pa) This potential target appears when “Enable Ndot” is checked in an upstream BEGIN. If used as a target, DeltaEC’s shooting method compares its calculation of p<sub>2,0,DEC</sub> here in the trunk with its calculation of $p _ { \mathrm { 2 , 0 , D E C } }$ at the SOFTEND identified by SegNum. DeltaEC updates the value of this variable continuously.

nLSoft This potential target appears when a gas mixture is in use and any MIX\*\* segment appears in the model. If used as a target, DeltaEC’s shooting method compares its calculation of $n _ { L }$ here in the trunk with its calculation of $n _ { L }$ at the SOFTEND identified by SegNum. DeltaEC updates the value of this variable continuously.

## Master–slave links:

None.

## Format and examples:

13   
UNION reconnect the "final" end of the loop, segment 8, here   
8.000 a SegNum 2.5420E+05 A |p| Pa   
2.5420E+05 b |p|Sft Pa = 13A? 1.9444 B Ph(p) deg   
1.9444 c Ph(p)S deg = 13B? 3.0515E-02 C |U| m^3/s   
781.66 d TSoft K (t) -44.624 D Ph(U) deg   
1603.6 e p20DES Pa = 13H? 2674.7 E Htot W   
2666.4 F Edot W   
702.66 G T K   
1603.6 H p20DEC Pa

![[mu_66afccee_80a6f56f3201ab5ba748.jpg]]

## Calculations:

Calculations at UNION are simple arithmetic:

$$
\begin{array} { c c l } { T _ { m , \mathrm { o u t } } } & { = } & { T _ { m , \mathrm { i n } } , } \end{array}\tag{11.15}
$$

$$
\begin{array} { r l r } { p _ { 1 , \mathrm { o u t } } } & { { } = } & { p _ { 1 , \mathrm { i n } } , } \end{array}\tag{11.16}
$$

$$
\begin{array} { r c l } { U _ { 1 , \mathrm { o u t } } } & { = } & { U _ { 1 , \mathrm { i n } } + U _ { 1 , \mathrm { e n d } } , } \end{array}\tag{11.17}
$$

$$
\dot { H } _ { \mathrm { t o t , o u t } } ~ = ~ \dot { H } _ { \mathrm { t o t , i n } } + \dot { H } _ { \mathrm { t o t , e n d } } ,\tag{11.18}
$$

$$
\dot { N } _ { \mathrm { o u t } } = \dot { N } _ { \mathrm { i n } } + \dot { N } _ { \mathrm { e n d } } ,\tag{11.19}
$$

$$
\dot { N } _ { L , \mathrm { o u t } } ~ = ~ \dot { N } _ { L , \mathrm { i n } } + \dot { N } _ { L , \mathrm { e n d } } ,\tag{11.20}
$$

$$
\begin{array} { r c l } { F _ { 1 , \mathrm { o u t } } } & { = } & { F _ { 1 , \mathrm { i n } } + F _ { 1 , \mathrm { e n d } } , } \end{array}\tag{11.21}
$$

$$
\mathrm { \Delta \ v o l _ { o u t } } ~ = ~ \mathrm { \Delta \ v o l _ { i n } + v o l _ { e n d } } ,\tag{11.22}
$$

where the subscript “in” refers to the closest trunk segment upstream of the UNION (i.e., almost always simply the segment immediately preceding the UNION) and the subscript “end” refers to the SOFTEND that is identified by SegNum in the first input parameter of the UNION, i.e., the SOFTEND that terminates the teebranch that is being joined to the trunk at the UNION. Note that Eq. (11.18) implies $\dot { H } _ { \mathrm { 2 , } k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 , } k , \mathrm { i n } } + \dot { H } _ { \mathrm { 2 , } k , \mathrm { e n d } }$ only if $T _ { m }$ is successfully targeted.

In thermally anchored mode, Eq. (11.18) is replaced by $\dot { H } _ { \mathrm { t o t , o u t } } = \dot { E }$

## 11.3 Insulation

## 11.3.1 ANCHOR and INSULATE

## General description:

By default, DeltaEC assumes that the only places total power can flow into or out of a model are

• heat exchangers, where heat can be added to the total power (or, if heat is negative, subtracted from the total power),

• electroacoustic transducers, where electrical power can be added to or subtracted from the total power,

• BRANCH, OPNBRANCH, and PISTBRANCH,

• BEGIN, unless $\dot { H } _ { \mathrm { t o t } }$ is explicitly set equal to zero (or is set equal to $\dot { E } + m w _ { m } \dot { N }$ which in turn happens to equal zero),

• SOFTEND and HARDEND, unless $\dot { H } _ { \mathrm { t o t } }$ is targeted to zero.

Other segments—stacks and regenerators, ducts and cones, and compliances, surfaces, and impedances—are assumed to have perfect insulation wrapped around their side-wall boundaries by default, so whatever total power $\dot { H } _ { \mathrm { t o t } }$ flows into them from the previous segment must flow out of them to the subsequent segment.

However, sometimes it is useful to change the behavior of ducts, cones, compliances, surfaces, and impedances so the total power flowing out of them is equal to the acoustic power out of them. In a series of such segments, acoustic power dissipation in each segment “disappears” from the model, as it might if the segment were thermally anchored to a heat sink at the same temperature as the local gas temperature $T _ { m }$ , and as if enthalpy flow difering from $\dot { E }$ [24] can be ignored. This behavior can be started by an ANCHOR segment before the first of a series of segments that are supposed to be thermally anchored. Thereafter, such segments obey $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { E } _ { \mathrm { o u t } }$ . The complementary INSULATE segment, or a BEGIN segment, can be used to return the computation to the default, thermally insulated mode in which $\dot { H } _ { \mathrm { 2 } , k , \mathrm { o u t } } = \dot { H } _ { \mathrm { 2 } , k , \mathrm { i n } }$ . ANCHOR is most useful for very low power systems and simple systems where total energy flow is irrelevant, and of course for components that actually are immersed in a heat sink.

Stacks and regenerators remain insulated when ANCHOR is in efect.

Some users who are interested only in acoustics, not thermoacoustics, habitually put ANCHOR immediately after BEGIN, to reduce irrelevant clutter.

Use the default, insulated mode for ducts, compliances, or impedances that come between stacks and heat exchangers, and for modeling insulated acoustic networks attached to thermoacoustic devices.

Table 11.1: List of RPN number-entry methods. Each number is piled on top of the stack.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment or example</td></tr><tr><td rowspan=1 colspan=1>&lt;Constant&gt;</td><td rowspan=1 colspan=1>Real or complex number</td><td rowspan=1 colspan=1>8.3; 6.02e23; (-0.1, 1)</td></tr><tr><td rowspan=1 colspan=1>pi</td><td rowspan=1 colspan=1>3.1415926536...</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>i</td><td rowspan=1 colspan=1>√-1</td><td rowspan=1 colspan=1>complex</td></tr><tr><td rowspan=1 colspan=1>&lt;Input address&gt;</td><td rowspan=1 colspan=1>Segment number and l.c. letter</td><td rowspan=1 colspan=1>3c</td></tr><tr><td rowspan=1 colspan=1>&lt;Output address&gt;</td><td rowspan=1 colspan=1>Segment number and cap letter</td><td rowspan=1 colspan=1>3F</td></tr><tr><td rowspan=1 colspan=1>&lt;filename:addr&gt;</td><td rowspan=1 colspan=1>Filename:segment number and letter(linking two or more models together)</td><td rowspan=1 colspan=1>bottle:3F</td></tr><tr><td rowspan=1 colspan=1>&lt;%:addr&gt;</td><td rowspan=1 colspan=1>% = shortcut for previous filename</td><td rowspan=1 colspan=1>bottle:3A %:3a * %:3C /</td></tr><tr><td rowspan=1 colspan=1>inp</td><td rowspan=1 colspan=1>Parameter “a&quot; of this RPN segment</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>rcl</td><td rowspan=1 colspan=1>Recall from Storage Register</td><td rowspan=1 colspan=1>see also sto</td></tr><tr><td rowspan=1 colspan=1>#</td><td rowspan=1 colspan=1>Put a copy of the stack&#x27;s top numberon top of the stack.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1stx</td><td rowspan=1 colspan=1>Recall what was on top of the stackbefore the most recent math operation,and put it on top of the stack.</td><td rowspan=1 colspan=1></td></tr></table>

Format and examples:

ANCHOR this segment has no inputs or outputs

INSULATE this segment also has no inputs or outputs

## 11.4 Math segments

Use this class of segments to access or display variables that DeltaEC would not otherwise display, to perform simple arithmetic operations, and to create targets other than DeltaEC default targets. See Chapter 4 for many examples.

## 11.4.1 RPN

## General description:

Results of the RPN segment are computed by interpreting the formula (line “b”) in Reverse Polish Notation, as described in [17, 18] and especially in all of Chapter 4. The formula is a sequence of numbers, addresses, internal DeltaEC variables, and algebraic operators. Variables such as Htot can be typed as lower case; DeltaEC will automatically convert to its preferred case. The formula in an RPN should not be longer than 80 characters. As with RPN calculators, when operators do not consume all numbers on the “stack,” more than one output is generated—a feature that can be exploited to display multiple results. The stack, whose members may be complex numbers, grows downward, from A–J. Valid operators and inputs are summarized in Tables 11.1–11.6. To display an RPN formula with parentheses, click on the output parameter, and then click on List Linkages.

Table 11.2: RPN variable-entry methods. Each number is piled on top of the stack.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment or units</td></tr><tr><td rowspan=1 colspan=3>Thermophysical properties</td></tr><tr><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1> $a ;$ sound speed</td><td rowspan=1 colspan=1> $\mathrm { m } / \mathrm { s }$ </td></tr><tr><td rowspan=1 colspan=1>beta</td><td rowspan=1 colspan=1> $\overline { { \beta ; } }$ expansion coefficent</td><td rowspan=1 colspan=1> $\overline { { 1 / \mathrm { K } } }$ </td></tr><tr><td rowspan=1 colspan=1>cp</td><td rowspan=1 colspan=1> $c _ { p } ;$ heat capacity</td><td rowspan=1 colspan=1> $\overline { { \mathrm { J } / \mathrm { k g } \cdot \mathrm { K } } }$ </td></tr><tr><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1> $c _ { s } ;$ solid heat capacity</td><td rowspan=1 colspan=1> $\overline { { \mathrm { J } / \mathrm { k g } \cdot \mathrm { K } } }$ </td></tr><tr><td rowspan=1 colspan=1>dk</td><td rowspan=1 colspan=1> $\delta _ { \kappa } ;$ thermal penetration depth</td><td rowspan=1 colspan=1>m</td></tr><tr><td rowspan=1 colspan=1>dn</td><td rowspan=1 colspan=1> $\delta _ { \nu } ;$ viscous penetration depth</td><td rowspan=1 colspan=1>m</td></tr><tr><td rowspan=1 colspan=1>ds</td><td rowspan=1 colspan=1> $\delta _ { s } ;$ solid thermal penetration depth</td><td rowspan=1 colspan=1>m</td></tr><tr><td rowspan=1 colspan=1>D12</td><td rowspan=1 colspan=1> $D _ { 1 2 } \colon$ binary mass diffusion coefficient</td><td rowspan=1 colspan=1> $\overline { { \mathrm { ~ m } ^ { 2 } / \mathrm { { s } } } } ,$ for gas mixtures</td></tr><tr><td rowspan=1 colspan=1>enth</td><td rowspan=1 colspan=1> $w _ { m } ;$ enthalpy per unit mass</td><td rowspan=1 colspan=1> $\mathrm { J / k g }$ </td></tr><tr><td rowspan=1 colspan=1>gamma</td><td rowspan=1 colspan=1> $\gamma = c _ { p } / c _ { v }$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>ks</td><td rowspan=1 colspan=1> $k _ { s } ;$ solid thermal conductivity</td><td rowspan=1 colspan=1>W/m·K</td></tr><tr><td rowspan=1 colspan=1>kT</td><td rowspan=1 colspan=1> $k _ { T } ;$ thermal diffusion ratio</td><td rowspan=1 colspan=1>for gas mixtures</td></tr><tr><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1> $k ;$ thermal conductivity</td><td rowspan=1 colspan=1> $\overline { { \mathrm { W / m } { \cdot } \mathrm { K } } }$ </td></tr><tr><td rowspan=1 colspan=1>m</td><td rowspan=1 colspan=1> $m ;$ molar mass (avg. mass of mixture)</td><td rowspan=1 colspan=1> $\overline { { { \mathrm { k g / m o l } } } }$ </td></tr><tr><td rowspan=1 colspan=1>mu</td><td rowspan=1 colspan=1> $\mu ;$ viscosity</td><td rowspan=1 colspan=1> $\mathrm { \overline { { k g / m \cdot s } } }$ </td></tr><tr><td rowspan=1 colspan=1>mL</td><td rowspan=1 colspan=1> $m _ { L } ;$ molar mass of light component of mixture</td><td rowspan=1 colspan=1> $\mathrm { k g / m o l }$ </td></tr><tr><td rowspan=1 colspan=1>mH</td><td rowspan=1 colspan=1> $m _ { H } ;$ molar mass of heavy component of mixture</td><td rowspan=1 colspan=1> $\mathrm { k g / m o l }$ </td></tr><tr><td rowspan=1 colspan=1>nLzero</td><td rowspan=1 colspan=1> $n _ { L , 0 } ;$ reference mole fraction for X</td><td rowspan=1 colspan=1>Eq. (8.9)</td></tr><tr><td rowspan=1 colspan=1>rho</td><td rowspan=1 colspan=1> $\rho _ { m } ;$ density</td><td rowspan=1 colspan=1> $\mathrm { \ k g / m ^ { 3 } }$ </td></tr><tr><td rowspan=1 colspan=1>rhos</td><td rowspan=1 colspan=1> $\rho _ { s } ;$ solid density</td><td rowspan=1 colspan=1> $\mathrm { \overline { { k g / m ^ { 3 } } } }$ </td></tr><tr><td rowspan=1 colspan=1>Tzero</td><td rowspan=1 colspan=1> $T _ { 0 } ;$ reference temperature for $w _ { m }$ and $\overrightharpoon { X }$ </td><td rowspan=1 colspan=1>K</td></tr><tr><td rowspan=1 colspan=3>State variables</td></tr><tr><td rowspan=1 colspan=1>Edot</td><td rowspan=1 colspan=1> $\dot { E } ;$ acoustic power flow</td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>f</td><td rowspan=1 colspan=1> $f ;$ frequency</td><td rowspan=1 colspan=1> $\mathrm { H z }$ </td></tr><tr><td rowspan=1 colspan=1>F1</td><td rowspan=1 colspan=1> $F _ { 1 } ;$ cumulative force phasor</td><td rowspan=1 colspan=1>N; complex; see text</td></tr><tr><td rowspan=1 colspan=1>H2k</td><td rowspan=1 colspan=1> $\dot { H } _ { \mathrm { 2 } , k } ;$ thermoacoustic plus conduction power flow</td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>Htot</td><td rowspan=1 colspan=1> $\dot { H } _ { \mathrm { t o t } } ;$ total power flow, incl. steady flow</td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>Ndot</td><td rowspan=1 colspan=1> $\overbrace { N } ;$  time-averaged molar flow</td><td rowspan=1 colspan=1>mol/s</td></tr><tr><td rowspan=1 colspan=1>nL</td><td rowspan=1 colspan=1>molar fraction of light gas in mixture</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NLdot</td><td rowspan=1 colspan=1> $\dot { N } _ { L } ;$ time-avg. molar flow, light component of mixt.</td><td rowspan=1 colspan=1>mol $/ \mathrm { s }$ </td></tr><tr><td rowspan=1 colspan=1>pm</td><td rowspan=1 colspan=1> $p _ { m } ;$ mean pressure</td><td rowspan=1 colspan=1> $\mathrm { P a }$ </td></tr><tr><td rowspan=1 colspan=1>p1</td><td rowspan=1 colspan=1> $p _ { 1 } ;$ oscillatory pressure</td><td rowspan=1 colspan=1> $\mathrm { P a } ;$ complex</td></tr><tr><td rowspan=1 colspan=1>p20DEC</td><td rowspan=1 colspan=1>p2,0,DEc; time-averaged head-loss &amp; F-density pressure</td><td rowspan=1 colspan=1> $\mathrm { P a }$ </td></tr><tr><td rowspan=1 colspan=1>p20tot</td><td rowspan=1 colspan=1> $p _ { \mathrm { 2 , 0 , t o t } }$ ; time-averaged pressure [Eq. (8.11)]</td><td rowspan=1 colspan=1> $\mathrm { P a }$ </td></tr><tr><td rowspan=1 colspan=1>Tm</td><td rowspan=1 colspan=1> $T _ { m } i$ mean temperature</td><td rowspan=1 colspan=1>K</td></tr><tr><td rowspan=1 colspan=1>&lt;T1&gt;</td><td rowspan=1 colspan=1> $\overline { { \langle T _ { 1 } \rangle } }$ ; spatially averaged oscillating gas temperature</td><td rowspan=1 colspan=1> $\mathrm { { K } ; }$ complex</td></tr><tr><td rowspan=1 colspan=1>U1</td><td rowspan=1 colspan=1> $U _ { 1 } ;$ oscillatory volume flow rate</td><td rowspan=1 colspan=1> $\overline { { { \mathrm { m } } ^ { 3 } / { \mathrm { s } } } } ;$ complex</td></tr><tr><td rowspan=1 colspan=1>vol</td><td rowspan=1 colspan=1>cumulative gas volume</td><td rowspan=1 colspan=1> ${ \overline { { \mathrm { m } ^ { 3 } } } } ;$ see text</td></tr><tr><td rowspan=1 colspan=1>w</td><td rowspan=1 colspan=1> $\omega ;$ radian frequency</td><td rowspan=1 colspan=1> $\mathrm { r a d } / \mathrm { s }$ </td></tr><tr><td rowspan=1 colspan=1>x</td><td rowspan=1 colspan=1>integration coordinate</td><td rowspan=1 colspan=1>m</td></tr><tr><td rowspan=1 colspan=1>Xdot</td><td rowspan=1 colspan=1> ${ \dot { X } } ;$ exergy flow                        241</td><td rowspan=1 colspan=1>W</td></tr></table>

Table 11.3: List of RPN unary functions. Each function removes a number from the top of the stack, acts on it, and puts the result on top of the stack. These functions accept and return complex numbers, unless otherwise noted. Whether phase angles are treated as radians or degrees is noted.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment or explanation</td></tr><tr><td rowspan=1 colspan=3>Algebra</td></tr><tr><td rowspan=1 colspan=1>sqrt</td><td rowspan=1 colspan=1> $x = { \sqrt { x } }$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>sqrd</td><td rowspan=1 colspan=1> $x = x * x$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>~</td><td rowspan=1 colspan=1> $x = - x$ </td><td rowspan=1 colspan=1>change sign</td></tr><tr><td rowspan=1 colspan=1>abs</td><td rowspan=1 colspan=1> $x = | x |$ </td><td rowspan=1 colspan=1>absolute value</td></tr><tr><td rowspan=1 colspan=1>inv</td><td rowspan=1 colspan=1> $x = 1 / x$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>real</td><td rowspan=1 colspan=1> $x = \operatorname { r e a l } ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>imag</td><td rowspan=1 colspan=1> $x = \operatorname { i m a g } ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>mag</td><td rowspan=1 colspan=1> $x = | x |$ </td><td rowspan=1 colspan=1>magnitude of complex x</td></tr><tr><td rowspan=1 colspan=1>conj</td><td rowspan=1 colspan=1> $x = \tilde { x }$ </td><td rowspan=1 colspan=1>complex conjugate of x</td></tr><tr><td rowspan=1 colspan=1>arg</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>phase of complex x (degrees)</td></tr><tr><td rowspan=1 colspan=1>argr</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>phase of complex x (radians)</td></tr><tr><td rowspan=1 colspan=3>Trigonometry in degrees</td></tr><tr><td rowspan=1 colspan=1>sin; asin</td><td rowspan=1 colspan=1> ${ \overline { { x = \sin ( x ) ; x = \sin ^ { - 1 } ( x ) } } }$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=1>cos; acos</td><td rowspan=1 colspan=1> $x = \cos ( x ) ; x = \cos ^ { - 1 } ( x )$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=1>tan; atan</td><td rowspan=1 colspan=1> $x = \tan ( x ) ; x = \tan ^ { - 1 } ( x )$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=2>Trigonometry in radians</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>sinr</td><td rowspan=1 colspan=1> $x = \sin ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>asinr</td><td rowspan=1 colspan=1> $\overline { { x = \sin ^ { - 1 } ( x ) } }$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=1>cosr</td><td rowspan=1 colspan=1> $x = \cos ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>acosr</td><td rowspan=1 colspan=1> $\overline { { x = \cos ^ { - 1 } ( x ) } }$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=1>tanr</td><td rowspan=1 colspan=1> $x = \tan ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>atanr</td><td rowspan=1 colspan=1> $\overline { { x = \tan ^ { - 1 } ( x ) } }$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=3>Hyperbolic functions</td></tr><tr><td rowspan=1 colspan=1>sinh</td><td rowspan=1 colspan=1> $\overline { { x = \sinh ( x ) } }$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>cosh</td><td rowspan=1 colspan=1> $x = \cosh ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tanh</td><td rowspan=1 colspan=1> $x = \operatorname { t a n h } ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=3>Bessel functions</td></tr><tr><td rowspan=1 colspan=1>JO</td><td rowspan=1 colspan=1> $\overline { { x = J _ { 0 } ( x ) } }$ </td><td rowspan=1 colspan=1>Bessel function of zero order</td></tr><tr><td rowspan=1 colspan=1>J1</td><td rowspan=1 colspan=1> $x = J _ { 1 } ( x )$ </td><td rowspan=1 colspan=1>Bessel function of first order</td></tr><tr><td rowspan=1 colspan=1>YO</td><td rowspan=1 colspan=1> $x = Y _ { 0 } ( x )$ </td><td rowspan=1 colspan=1>Neumann function of zero order</td></tr><tr><td rowspan=1 colspan=1>Y1</td><td rowspan=1 colspan=1> $x = Y _ { 1 } ( x )$ </td><td rowspan=1 colspan=1>Neumann function of first order</td></tr><tr><td rowspan=1 colspan=3>Logarithms and exponentials</td></tr><tr><td rowspan=1 colspan=1>1og</td><td rowspan=1 colspan=1> $x = \log _ { e } ( x )$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>exp</td><td rowspan=1 colspan=1> $x = e ^ { x }$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1og10</td><td rowspan=1 colspan=1> $x = \log _ { 1 0 } ( x )$ </td><td rowspan=1 colspan=1>real argument only</td></tr><tr><td rowspan=1 colspan=1>tenx</td><td rowspan=1 colspan=1> $x = 1 0 ^ { x }$ </td><td rowspan=1 colspan=1></td></tr></table>

Table 11.4: Ordinary RPN binary operations and functions. Each operation or function removes two numbers from the top of the stack, combines them, and puts the result on top of the stack. In this table, $^ { 6 6 } x ^ { \prime \prime }$ refers to the number on top of the stack, and $^ { 6 6 } y ^ { \dag }$ refers to the number second from the top of the stack.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment or example</td></tr><tr><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1> $x = y + x$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1> $x = y - x$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>*</td><td rowspan=1 colspan=1> $x = y * x$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1> $x = y / x$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>^</td><td rowspan=1 colspan=1> $x = y ^ { x }$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>min; max</td><td rowspan=1 colspan=1> $\overline { { x = \operatorname* { m i n } [ x , y ] ; x = \operatorname* { m a x } [ x , y ] } }$ </td><td rowspan=1 colspan=1>real arguments only</td></tr><tr><td rowspan=1 colspan=1>avg</td><td rowspan=1 colspan=1> $x = ( x + y ) / 2$ </td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>cmplx</td><td rowspan=1 colspan=1> $x = x ( \cos y + i \sin y )$ </td><td rowspan=1 colspan=1>y in degrees</td></tr><tr><td rowspan=1 colspan=1>cmplxr</td><td rowspan=1 colspan=1> $x = x ( \cos y + i \sin y )$ </td><td rowspan=1 colspan=1>y in radians</td></tr><tr><td rowspan=1 colspan=1>atan2</td><td rowspan=1 colspan=1> $\overline { { x = \tan ^ { - 1 } ( x / y ) ; } }$ 2-argument, 4-quadrant arctangent</td><td rowspan=1 colspan=1>degrees</td></tr><tr><td rowspan=1 colspan=1>atan2r</td><td rowspan=1 colspan=1> $\overline { { x = \tan ^ { - 1 } ( x / y ) } } ;$ 2-argument, 4-quadrant arctangent</td><td rowspan=1 colspan=1>radians</td></tr></table>

Table 11.5: RPN actions that have no efect on the RPN stack, but have an efect elsewhere.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment</td></tr><tr><td rowspan=1 colspan=1>sto</td><td rowspan=1 colspan=1> $S = x$ </td><td rowspan=1 colspan=1>Store the number that&#x27;s on top of the stackin the Storage Register. (See also rc1)</td></tr><tr><td rowspan=1 colspan=1> ${ = } \mathbf { f }$ </td><td rowspan=1 colspan=1> $f = x$ </td><td rowspan=1 colspan=1>Set $\overline { { f } }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $\tt { = F 1 }$ </td><td rowspan=1 colspan=1> $F _ { 1 } = x$ </td><td rowspan=1 colspan=1>Set the accumulated-force phasor equal tothe number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1>=H2k</td><td rowspan=1 colspan=1> $\overbrace { H _ { 2 , k } = x }$ </td><td rowspan=1 colspan=1>Set $\dot { \overline { { H _ { 2 , k } } } }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> ${ \tt = } \tt { N d o t }$ </td><td rowspan=1 colspan=1> $\stackrel { \textstyle \bigwedge } { N } = x$ </td><td rowspan=1 colspan=1>Set $\overrightharpoon { N }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $= \mathtt { n L }$ </td><td rowspan=1 colspan=1> $n _ { L } = x$ </td><td rowspan=1 colspan=1>Set $n _ { L }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $= \tt N L d o t$ </td><td rowspan=1 colspan=1> $\dot { N } _ { L } = x$ </td><td rowspan=1 colspan=1>Set $\dot { N } _ { L }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> ${ \tt = } _ { \tt N L z r o }$ </td><td rowspan=1 colspan=1> $n _ { L , 0 } = x$ </td><td rowspan=1 colspan=1>Set $n _ { L , 0 }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1>=pm</td><td rowspan=1 colspan=1> $p _ { m } = x$ </td><td rowspan=1 colspan=1>Set $p _ { m }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1>=p1</td><td rowspan=1 colspan=1> $p _ { 1 } = x$ </td><td rowspan=1 colspan=1>Set $p _ { 1 }$ phasor equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $\tt { \tt = } \tt { p } 2 0 \tt { D E }$ </td><td rowspan=1 colspan=1> $p _ { 2 , 0 , \mathrm { D E C } } = x$ </td><td rowspan=1 colspan=1>Set $p _ { 2 } .$ o,DEc equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1>=Tm</td><td rowspan=1 colspan=1> $T _ { m } = x$ </td><td rowspan=1 colspan=1>Set $T _ { m }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $= \mathtt { T z e r o }$ </td><td rowspan=1 colspan=1> $T _ { 0 } = x$ </td><td rowspan=1 colspan=1>Set $T _ { 0 }$ equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $\mathtt { = U 1 }$ </td><td rowspan=1 colspan=1> $U _ { 1 } = x$ </td><td rowspan=1 colspan=1>Set $U _ { 1 }$ phasor equal to the number that&#x27;s on top of the stack.</td></tr><tr><td rowspan=1 colspan=1> $\mathtt { \Gamma } = \mathtt { v } \mathtt { o } 1$ </td><td rowspan=1 colspan=1> $\mathsf { v o l } = x$ </td><td rowspan=1 colspan=1>Set the accumulated volume equal tothe number that&#x27;s on top of stack.</td></tr></table>

Table 11.6: RPN actions that afect the top two numbers on the RPN stack.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment or example</td></tr><tr><td rowspan=1 colspan=1>a&lt;&gt;b</td><td rowspan=1 colspan=1>x = y; y = x</td><td rowspan=1 colspan=1>Interchange top two numbers on the stack.</td></tr></table>

Table 11.7: RPN tokens that have no efect.
<table><tr><td rowspan=1 colspan=1>Item</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Comment or example</td></tr><tr><td rowspan=1 colspan=1>•n</td><td rowspan=1 colspan=1>No effect</td><td rowspan=1 colspan=1>Punctuation mark for human readability.</td></tr></table>

Format and examples of RPN:

RPN magU1 over 2 pi freq Area (meters)   
! gas displacement amplitude after duct in segment five   
0.00 0.0153 A ChngeMe   
5C 2 / pi / 0b / 5a /   
--23   
RPN efficiency divided by Carnot’s efficiency   
! electrical power out of alternator is 19G   
! heat into engine is 6e   
! hot temperature is 6f   
! ambient temperature is 8f   
1.00 0.2438 A eta\_rel   
19G 6e / 1 8f 6f / - /   
21 --   
RPN B=diam. A= Reynolds number amplitude here   
! 20a is the area in segment 20   
0.0000 2838.5 A NR1   
0.123 B D(m)   
20a 4 \* pi / sqrt # U1 mag \* rho \* 20a / mu /   
! ------ 128 --   
RPN some gas properties here   
0.0000 a G or T 1.6667 A gamma   
519.22 B rho c   
0.6625C Prandt1   
mu cp \* k / ; rho a \* ; gamma

## Potential targets in RPN:

Input line a is the potential target to which output line A can be compared. If line a is used as a target, A should be real.

## A detail of <T1> calculation in RPN:

The lateral spatial average of the complex temperature amplitude, $\left. T _ { 1 } \right.$ , depends on segmentdependent variables such as $f _ { \nu } , \ f _ { \kappa } ,$ , and $d T _ { m } / d x$ . In an RPN segment, <T1> yields the value at the end of the previous physical segment. See details for $\left. T _ { 1 } \right.$ for each segment in Chapter 10.

## Details of F1 calculation in RPN:

Using the F1 variable in RPN segments, DeltaEC can calculate the net oscillating force exerted by the oscillating gas (and oscillating parts of speakers) on the surrounding pres-

sure vessel, which is assumed to be rigid. As far as we know, the approach is not published anywhere, so the theory behind it is derived in Section 14.1. Here, we describe the implementation in DeltaEC, and we give two examples of its use.

DeltaEC always keeps track of the integral on the right-hand side of

$$
F _ { 1 } = - i \omega \int { ( \rho _ { m } u _ { 1 } ) } d V = - i \omega \int { \rho _ { m } ( x ) } U _ { 1 } ( x ) d x\tag{11.23}
$$

during the course of its other integrations. The derivation in Section 14.1 shows that this integral gives the total force amplitude exerted by the gas on the pressure vessel. The result is accessible to the user at any location by putting $\ @ 1 ^ { \mathfrak { s } }$ in line b of an RPN segment, yielding the complex number $F _ { 1 }$ and making it available for further RPN calculations. (As usual, lower-case typing is accepted.)

DeltaEC initializes F1 to zero at BEGIN and at the beginning of the teebranch of every TBRANCH. The trunk’s F1 and the referenced-SOFTEND’s F1 are added in UNION. Any other segment adds its own F1 contribution [according to Eq. (11.23)] to whatever total F1 has accumulated before it.

These defaults can be overridden via RPN segments that include the change command $\displaystyle { \bf \ddot { \omega } } ^ { \prime \prime } = \mathtt { F } 1 ^ { \prime \prime }$ . The defaults must often be overridden for thermoacoustic systems with elbows or side branches sticking out at diferent angles, to resolve the components of the force-amplitude vector in diferent directions and to take care of minus signs in toroidal acoustic paths.

For a $9 0 ^ { \circ }$ miter elbow, split the elbow into two segments. Displaying and then rezeroing the force variable between those segments (with $\ " \mathtt { F } 1 \ "$ and $\displaystyle { \mathrm {  ~ \omega ~ } ^ { \scriptscriptstyle ( \zeta ) } = } \mathtt { F } 1 ^ { \prime } { } ^ { \xi }$ , respectively) is a useful approach. For a smoothly radiused $9 0 °$ elbow, strictly speaking we ought to do an integral of a vector velocity around the corner to obtain a vector force. This is beyond DeltaEC’s current capability. However to the extent that $U _ { 1 }$ does not vary from one end of such an elbow to the other, that integral yields simply $2 / \pi$ times DeltaEC’s full-elbow DUCT integral for the vertical direction and $2 / \pi$ times DeltaEC’s full-elbow DUCT integral for the horizontal direction. The user who requires $F _ { 1 }$ in such an elbow can use RPN calculations to implement the factor of $2 / \pi$ , as shown in the second example below.

For IESPEAKER and VESPEAKER segments, DeltaEC evaluates $\textstyle \int { \rho _ { m } U _ { 1 } }$ dx in Eq. (11.23) as simply the speaker’s moving mass times its velocity phasor.

## Example 1

To find the oscillating velocity of a freely suspended, 14-kg pressure vessel enclosing a half-wavelength resonance driven by a noncompliant transducer at the far end, use this series of segments.

```csv
BEGIN no transducer at this end
2.000E+06 a Mean P Pa
173.53 b Freq Hz
300.00 c TBeg K
1.0000E+05 d |p| Pa
0.0000 e Ph(p) deg
0.0000 f |U| m/s
0.0000 g Ph(U) deg
SURFACE first end
sameas 2a a Area m^2
DUCT
1.0000E-02 a Area m^2
```

![[mu_66afccee_eb72dd3f674d7632bca6.jpg]]  
Figure 11.2: Example 2. Left, a sketch of a half-wavelength, two-speaker, standing-wave refrigerator. Right, force diagram, in which the directions of the arrows indicate the “positive” direction of calculated forces. In both parts of the figure, “c.g.” indicates the center of gravity.

0.3545 b Perim m   
1.0000 c Length m   
SURFACE noncompliant transducer at this end   
sameas 2a a Area m^2   
HARDEND   
0.0000 a R(1/z) (t)   
0.0000 b I(1/z) = 4H?   
!- 5   
RPN (a)=mass of pressure vessel (kg). [A]= velocity phasor of pressure vessel (m/s).   
14.000 a G or T (t) (-8.8680E-05, 0.1309 ) m/s   
F1 5a / i / w /   
1-   
RPN viscous drag force phasor (newtons)   
0.0000 a G or T (t) ( 1.3536 , -1.3536 ) N   
F1 p1 3a \* 0d 1a \* - -   
guessz 0b   
targs 4b

We arbitrarily defined zero phase to be that of the pressure at segments 0 and 1. Segment 5 shows that the phase of the velocity is almost 90<sup>◦</sup>, which is consistent with the phases of the pressure on the two ends of the half-wavelength resonator at segments 1 and 3. Segment 6 subtracts the normal end-cap forces from the total force to display what’s left over, which must be the integrated viscous shear force on the side walls.

## Example 2

To find oscillating forces and torques on the half-wavelength refrigerator shown in Fig. 11.2, we use a DeltaEC model like this:

TITLE symmetric speaker-driven refrigerator, example2.out   
00 BEGIN in the motor enclosure. Guess temperature and complex p1.   
01 INSULATE   
02 SURFACE top lid   
03 DUCT backside of piston = motor enclosure   
04 SURFACE extra surface area for motor parts   
05 IESPEAKER motor-driven piston. Guess phase of current.   
06 RPN annular surface area around piston   
07 SURFACE annular surface area around piston   
08 DUCT short duct   
09 HX ambient heat exchanger. Guess heat rejected and target temperature.   
10 STKSLAB the stack   
11 HX cold heat exchanger   
12 CONE adapter to small-diam resonator   
13 RPN capture F1 here, and reset it to zero   
0.0000 a G or T (t) 0.0000 A Newton

( 9.2386 , -113.62 ) B Newton   
F1 0 =F1   
14 DUCT 90 degree elbow   
15 RPN vertical and horizontal forces on elbow; then set F1=0   
0.0000 a G or T (t) 0.0000 A Newton   
( 3.0179E-03, -3.6644 ) B Newton   
( 3.0179E-03, -3.6644 ) C Newton   
F1 2 \* pi / # 0 =F1   
16 DUCT horizontal run of pipe, to mirror-image location   
17 SOFTEND mirror-image plane. Target zero complex impedance and zero Hdot.   
18 RPN for aesthetics, enforce phase(U1)=0 here. Target this.   
0.0000 a G or T = 18A? -2.5791E-14 A deg   
U1 arg   
19 RPN force due to horizontal segment   
0.0000 a G or T (t) ( 6.9004E-04, -6.0857 ) A Newton   
F1   
20 RPN [A]=net vertical force; [B]=net horizontal force (newtons)   
0.0000 a G or T (t) ( 9.2416 , -117.29 ) A Newton   
( 3.7079E-03, -9.7501 ) B Newton   
1 C 19A 13 1

Most of the input and output have been eliminated from the listing for clarity, leaving only the relevant RPN segments fully displayed. Segment 13 captures $F _ { 1 }$ for the vertical components, segment 15 captures $F _ { 1 }$ for the elbow using the approximation that $U _ { 1 }$ is uniform in the elbow, and segment 19 captures $F _ { 1 }$ for the horizontal part of the resonator. Then segment 20 adds up the previous results to yield the net horizontal and vertical $F _ { \mathrm { 1 } } \mathrm { s }$ for this half of the full refrigerator.

Considering the symmetry of the full refrigerator as shown in the figure (only half of which is modeled above with DeltaEC ) to get the minus signs and factors of two correct, we see that the total horizontal force exerted on the pressure vessel is 2× [20B], the total vertical force is zero, and the total counter-clockwise torque around the center of gravity “c.g.” is $2 \times ( [ 2 0 \mathrm { A } ] L _ { H } + [ 2 0 \mathrm { B } ] L _ { V } )$ where $L _ { H }$ and $L _ { V }$ are distances between the center of gravity and the axes of the parts of the refrigerator as shown in the figure. Both the total horizontal force and the torque have time phases of about $- 9 0 ^ { \circ }$ , relative to the time phase of the velocity at the mirror-image plane, which is set to $0 ^ { \circ }$ with segment 18.

## Details of vol calculation in RPN:

Beginning with version 6, DeltaEC keeps track of the cumulative gas volume in a series of segments while performing its other integrations. The result is accessible to the user at any location by putting “vol” in line b of an RPN segment. (A similar result is accessible through the VOLUME segment, described in Section 11.4.2, which calculates the volume in a range of segments, including both gas volume and the volume of fins, plates, and struts in STK\*\*s and heat exchangers.)

By default, DeltaEC initializes “vol” to zero at BEGIN and at the beginning of a TBRANCH’s teebranch, and adds the branch “vol” and trunk “vol” at UNIONs. Any other segment adds its own contribution to whatever total “vol” has accumulated before it. These defaults can be overridden via RPN segments that include the change command “=vol”.

The volume of a cone uses its average area $( \mathbf { A r e a I } + { \sqrt { \mathbf { A r e a I } \cdot \mathbf { A r e a F } } } + \mathbf { A r e a F } ) / 3$ and its length.

Example

TITLE symmetric speaker-driven refrigerator, example2v.out   
00 BEGIN in the motor enclosure. Guess temperature and complex p1.   
01 INSULATE   
02 SURFACE top lid

03 DUCT backside of piston = motor enclosure   
04 SURFACE extra surface area for motor parts   
05 IESPEAKER motor-driven piston. Guess phase of current.   
06 SURFACE annular surface area around piston   
07 DUCT short duct   
08 HX ambient heat exchanger. Guess heat rejected and target temperature.   
09 STKSLAB the stack   
10 HX cold heat exchanger   
11 CONE adapter to small-diam resonator   
12 DUCT 90 degree elbow   
13 DUCT horizontal run of pipe, to mirror-image location   
14 SOFTEND mirror-image plane. Target zero complex impedance and zero Hdot.   
15 RPN for aesthetics, enforce phase(U1)=0 here. Target this.   
16 RPN volume of gas (cubic meters) in segments 01 through 14   
0.0000 a G or T (t) 6.857E-02 A m3   
vol

The vol operator in segment 16 causes the cumulative volume to be displayed: The total volume of gas in the DUCTs, HXs, STKSLAB, and CONE. (The other segments in this example have no gas volume.)

## 11.4.2 VOLUME

## General description:

Result A of a VOLUME segment is the sum of the volumes in all duct, cone, stack, compliance, and heat exchanger segments beginning with BegAddr and ending with EndAddr (parameter letters are inconsequential). Porosity is ignored in calculating this volume, so the result is the volume of the gas plus the volume of internal fins, plates, etc. in heat exchangers and stacks. (In contrast, the vol variable, accessible in RPN segments, gives the cumulative gas volume, not including internal fins and plates.) This segment is intended to give an indication of the overall size of an apparatus for doing trade-of analysis during design.

The volume of a cone uses its average area (AreaI + AreaI · AreaF + AreaF)/3 and its length.

## Input variables:

BegSeg The first of the segments whose volumes are to be summed.

EndSeg The last of the segments whose volumes are to be summed.

## Potential targets:

Line “a” is the target at which VOLUME output line “A” can be aimed.

## Master–slave links:

None.

## Format and examples:

VOLUME   
0.50 a targeted volume (cubic meters)   
1 b BegSeg   
10 c EndSeg

## 11.4.3 CONSTANTS

## General description:

The CONSTANTS segment allows the user to input a dozen real numbers in one segment. This is useful when a subsequent RPN segment depends on a large number of nonstandard parameters that the user must control or that DeltaEC must guess. (Without CONSTANTS, a dozen RPN segments would be required.) This segment performs no calculations and has no potential targets.

## Format and examples:

CONSTANTS parameters used elsewhere   
1.55 a   
2.00 b user-  
3.22 c editable   
4.00 d descriptors   
5.00 e are here   
6.00 f   
7.00 g height(ft)   
6.02E23 h   
-0.048 i   
0.00 j   
0.00 k   
0.00 l

## 11.5 Interfaces to external programs and files

## 11.5.1 BLKDATA

## General description:

BLKDATA is a specialized segment designed for users who have a quantity of tabular data that they want DeltaEC to follow. The data may represent experimental results, the results from other computational methods, or simply an irregular parameter space to be explored that is not well served by DeltaEC’s incremental-plot capability (e.g., irregular step size or parametric plotting). The data file is in text format, delimited with spaces or tabs, and it may contain up to 14 columns and any number of lines, all with the same number of entries. The first one or two lines can optionally contain descriptive strings that are read into the parameters’ description and unit fields, respectively. Only one BLKDATA segment per model is allowed. The data file must have the sufix <.blk> and its root name is supplied in the heading of the BLKDATA segment. When the file is opened, the number of lines and columns are counted, and initial column headings are read in, if present. The number of input parameters for the segment is equal to the number of columns in the <.blk> file. During a run, each numeric line of the <.blk> file is read sequentially, and DeltaEC runs the model once for each line. Each line of the file is inserted into the input parameters of the BLKDATA segment, one line per data point. The use of sameas provides a direct means to tie the values of DeltaEC input parameters to the tabulated data.

Enforcing values that normally appear as DeltaEC outputs is a little more subtle. This requires an RPN target to be sameas’ed to an input parameter in the BLKDATA segment, so the RPN’s calculated output value can be forced to hit the targeted value. This target must be used, of course, and an appropriately related input parameter must be added to the guess list. Segment 5 in the example below illustrates such a target.

## Input variables:

The heading field, which is to the right of “BLKDATA,” must contain the root name of the <.blk> file. For example, if the user’s data is in <mydata.blk>, the BLKDATA segment looks like the example below.

## Potential targets; Master–slave links:

None.

## Format and examples:

If the BLKDATA segment looks like this:

BLKDATA mydata

and the file <mydata.blk> looks like this:

Freq |p|@0 SkrAmp   
Hz Pa A   
511.4 6653. 0.031   
511.0 14401. 0.076   
511.9 9872. 0.055

then DeltaEC will immediately transform the BLKDATA segment to this:

BLKDATA mydata   
511.40 a Freq Hz   
6653.0 b |p|@0 Pa   
3.1000E-02 c SkrAmp A

and will read subsequent lines of <mydata.blk> into place in subsequent iterations of the run. If the file <mydata.blk> is a log of experimental data, we can ask DeltaEC to emulate the experimental conditions by inserting appropriate sameas statements, as in the following fragment that matches the experimental applied frequencies, pressure amplitudes, and speaker currents:

BEGIN the setup   
7.8000E+04 a Mean P Pa   
sameas 1a b Freq Hz   
300.00 c TBeg K   
sameas 1b d |p|@0 Pa   
0.0000 e Ph(p)0 deg   
0.0000 f |U|@0 m^3/s   
0.0000 g Ph(U)0 deg   
air Gas type   
ideal Solid type   
BLKDATA mydata   
511.40 a Freq Hz   
6653.0 b |p|@0 Pa   
3.1000E-02 c SkrAmp A   
+ 2 SURFACE cavity back surface   
+ 3 DUCT back duct   
!-- 4   
VESPEAKER ...using an IESPEAKER would be simpler,   
! but would not illustrate BLKDATA plus target.   
1.5000E-04 a Area m^2 68.286 A |p| Hz

```csv
4.6000 b R ohms -91.445 B Ph(p) deg
5.5000E-05 c L H 5.2965E-06 C |U| m^3/s
3.3000 d BLProd T-m -90.455 D Ph(U) deg
4.0000E-04 e M kg 1.8081E-04 E Hdot W
8560.0 f K N/m 1.8081E-04 F Edot W
0.8000 g Rm N-s/m 1.8597E-03 G EdotIn W P
0.1945 h |V| V 0.1945 H Volts V
243.00 i Ph(V) deg 2.2615E-02 I Amps V
32.263 J Ph(V/I) deg
sameas 0 Gas type 121.99 K |Px| Pa
ideal Solid type -145.97 L Ph(Px) deg
!-- 5
RPN use to match speaker current output to measured value
sameas 1c a = 5A? 2.2615E-02 A
4I
```

## 11.5.2 SYSEXEC

## General description:

The SYSEXEC segment allows DeltaEC to send data to an external program via the computer’s file-handling system, execute that external program, and bring any results of that external program back into DeltaEC. The use of sameas allows any input or output numbers in DeltaEC to be brought into the SYSEXEC segment’s input parameters so they can be sent to the external program, and subsequently allows any DeltaEC input parameters or RPN tokens to be set equal to results of the external program.

The first action taken by SYSEXEC is to write all of its 14 real input parameters to a text file called <ToSys.dat> in single-column format. SYSEXEC then pauses DeltaEC execution and runs an external program using the entire text string specified in the heading of the SYSEXEC segment. The external program might or might not make use of the numbers in <ToSys.dat>. If the external program’s results should be brought back in to DeltaEC, the external program must put those results in a file named <FromSys.dat> in the same ASCII, single-column format. (If more than 14 values are required, the leftovers might be read in through a BLKDATA segment or a second SYSEXEC segment.) When the external program has finished running, control returns to DeltaEC, which then reads up to 14 parameters from the file <FromSys.dat> if it exists, putting those numbers in the output list of the SYSEXEC segment, and resumes its numerical integrations.

## Format and examples:

The following is a trivial example showing how a set of integers assigned to SYSEXEC input parameters can be sorted by the Windows CMD sort command. The SYSEXEC segment was initially prepared like this:

RPN a silly example   
87.0 a 13.000 A   
5 8 +   
2   
SYSEXEC sort tosys.dat > fromsys.dat   
3.0000 a In 1   
4.0000 b In 2   
6.0000 c In 3   
7.0000 d In 4   
2.0000 e In 5   
sameas 1a f In 6   
2.0000 g In 7   
1.0000 h In 8   
10.000 i In 9

sameas 1A j In 10   
5.0000 k In 11   
4.0000 l In 12   
11.000 m In 13   
9.0000 n In 14

When the SYSEXEC segment is encountered by DeltaEC during a run, DeltaEC creates the file <ToSys.dat> containing the parameters a through n:

3.0000   
4.0000   
6.0000   
7.0000   
2.0000   
87.000   
2.0000   
1.0000   
10.000   
13.000   
5.0000   
4.0000   
11.000   
9.0000

and passes the segment’s heading field, sort tosys.dat > fromsys.dat, to the operating system as a command string. Next, the operating system sends the newly created file <tosys.dat> to the sort function. The sort command sorts the numbers into ascending order. The results of the sort are piped into the <fromsys.dat> file using the ‘greater than’ character, i.e., the ‘>’ character, in the command string. Finally, the SYSEXEC segment reads the <fromsys.dat> file and puts the results in the output column of the segment, so the segment ends up looking like this:

```csv
! Sort input parameters into output parameters (Windows version)
1
RPN a silly example
87.0 a 13.000 A
5 8 +
2
SYSEXEC sort tosys.dat > fromsys.dat
3.0000 a In 1 1.0000 A Out 1
4.0000 b In 2 2.0000 B Out 2
6.0000 c In 3 2.0000 C Out 3
7.0000 d In 4 3.0000 D Out 4
2.0000 e In 5 4.0000 E Out 5
sameas 1a f In 6 4.0000 F Out 6
2.0000 g In 7 5.0000 G Out 7
1.0000 h In 8 6.0000 H Out 8
10.000 i In 9 7.0000 I Out 9
sameas 1A j In 10 9.0000 J Out 10
5.0000 k In 11 10.000 K Out 11
4.0000 l In 12 11.000 L Out 12
11.000 m In 13 13.000 M Out 13
9.0000 n In 14 87.000 N Out 14
```

Then an RPN or sameas in a subsequent segment that points to output 2N will access the largest number in the original list, which was 87.000 in this example.

As an entertaining exercise, put a SYSEXEC segment at the end of a model, sameas some of the SYSEXEC inputs to all of the guesses in the model, sameas other SYSEXEC inputs to all of the targeted results in the model, and write a little batch file or python script (if python exists on your computer) to append the numbers in <ToSys.dat> as a single line in another file. Put the name of that batch file or python script in the SYSEXEC’s header. Ignore <FromSys.dat>. Running the model will then produce a nice table of the values of all the guesses and targeted results during each pass of the shooting method, showing the details of what DeltaEC’s shooting method is actually doing.

The SYSEXEC segment can also be used to “insert” a user-created segment in a model. Use <ToSys.dat> to send $p _ { m }$ and f (both from segment 0) and integration variables such as $p _ { 1 } , \ U _ { 1 }$ , and $T _ { m }$ (from the preceding segment) to the operating system, run your own program to change the values of integration variables such as $p _ { 1 } , U _ { 1 }$ , and $T _ { m }$ , return your new values of $p _ { 1 } , U _ { 1 }$ , and $T _ { m }$ to DeltaEC in <FromSys.dat>, and finally use a subsequent RPN segment with tokens such as =Tm to pass your custom-calculated values to the next segment in DeltaEC.

## 11.5.3 Running DeltaEC from a terminal or another program

Advanced users might want to run DeltaEC under control of another computer program.   
Here are two ways to do so.

Python’s pywinauto can send simulated keystrokes and mouse actions to Windows programs and watch the results, so a python program can find an open instance of the DeltaEC GUI and do almost anything that a human can do in its main window and any of its subsidiary windows. As the simplest example, this script will find the DeltaEC GUI and run a model that’s already open in it:

```python
from pywinauto import application
class GuiRunner:
def __init__(self):
self.app = application.Application()
self.app.connect(best_match=’DeltaEC’)
def runModel(self):
self.app.DeltaEC.menu_select("Tools->Run")
test = True
while test:
test = self.app.window(title=’Model run progress’).exists(retry_interval=0.4)
return
if __name__ == "__main__":
GR = GuiRunner()
GR.runModel()
```

As an alternative to its GUI, DeltaEC can be launched and operated from a terminal, e.g., a Windows command prompt. In the syntax of Windows CMD/terminal calls, a human, a batch file, or a makefile can control DeltaEC in this environment. For example, from a terminal in the folder in which DeltaEC.exe resides, typing deltaec.exe -h will display a help message with launching options, and

will launch the program and open filename.out, displaying a menu of operations accessible with single keystrokes:

MAIN:   
r (r)un model x (x)plore (open loop run)   
a (a)nalyze sensitivities A (A)nalysis display   
n (n)ew model input file E (E)xtras . . .   
w (w)rite current model state W (W)rite model As:   
u (u)se in Guess/Target list d (d)isplay   
p (p)lot another parameter P (P)lot status summary   
R (R)estore listsReset params c (c)lear a guess, targ, plot, etc   
g (g)uess/target list summary C (C)lear all guess&targs or highlts   
m (m)odify parameter value i (i)nterpreter (Python)   
s (s)pecial modes editing t (t)hermophysical properties   
I (I)nsert segment K (K)ill segment   
h (h)ighlight parameter e (e)xit DeltaE   
? (?)show this menu

path\to\the\file\filename.Main: (rxaAnEwWudpPRcgCmistIKhe?)

Typing ‘r’ will run the model, ‘w’ will write the result to the disk (requiring $\mathrm { { } ^ { \circ } y ^ { \prime } }$ to confirm), and ‘e’ will exit.

DeltaEC runs can be automated from scripts (BATCH files, makefiles, etc.) by redirecting standard input/output to supply the expected keyboard responses. To automate the example above, do this:

prompt> deltaec.exe -c ..\path\to\the\file\filename.out < ..\path\to\the\file\keystrokes.txt,

with ‘r w $\mathrm { ~ y ~ e ~ } ^ { \prime }$ on four lines in keystrokes.txt and where ‘<’ redirects stdin to be drawn from the keystrokes file. Equivalently, try

prompt> (echo r & echo w & echo y & echo e) | deltaec.exe -c ..\path\to\the\file\filename.out where stdin is filled from a pipeline.

## 12. Gases (and liquids)

We provide an artificial temperature floor Tmin = 10 Kelvin and an artificial ceiling Tmax = 9999 Kelvin to prevent DeltaEC from trying to use extreme or even negative temperatures when it is really lost. Consequently, no temperatures beyond these extremes should be used. (Most of the equations for the fluids or solids are very inaccurate when these limits are reached anyway.) DeltaEC’s numerical integration can naively carry $T _ { m }$ beyond these bounds, but the underlying evaluation of the thermophysical properties is clipped at Tmin or Tmax. The 10-K floor can be modified within Options in the Edit pulldown menu, and it is automatically reduced when CryoHe is used.

In what follows, ta is temperature in Kelvin, t1 is temperature in Celsius.

DeltaEC looks for a 10-character field in the BEGIN segment to determine gas type. If you are modifying a model with a text editor, be sure to use plenty of trailing spaces after short gas names like “air” to get “gas-type” out of the 10-character field.

A “fluid” is a gas or a liquid. Gases are the most commonly used fluids in thermoacoustics and DeltaEC. However, liquid sodium and eutectic liquid sodium-potassium are included in DeltaEC because they are thermodynamically powerful, with non-negligible thermal expansion coeficients and non-negligible $( \partial s / \partial p ) _ { T }$ , when close enough to their critical points. For further details on the use of these liquids in thermoacoustics, see Ref. [14] and references therein. Perhaps we should refer to the “gases” used in DeltaEC as “fluids,” but for simplicity we always call them gases despite the fact that some liquids are included.

Equations used here accurately cover ranges of T and p that have been of interest to the Los Alamos thermoacoustics team. DeltaEC issues no warning if it goes outside the accurate range. The user must study the equations here, or examine the results of these equations via the properties tokens in an RPN segment or the thermophysical-properties dialog, to decide if these equations are accurate enough or if a user-defined gas is called for.

To change gases in the middle of a model (e.g., after a flexible membrane), insert a BEGIN segment with the new gas, linking most or all other variables in the BEGIN to the previous BEGIN (to get $p _ { m }$ and f) and to the results of the previous segment (e.g., to get $p _ { 1 }$ and $U _ { 1 } )$ using sameas. See example in Section 11.1.2.

## 12.1 Helium (helium)

Ideal gas approximation for equation of state (including sound speed and expansion coeficient) and specific heat. Transport properties are simple fits to data in Ref. [71], valid above 200 K and below 10 MPa.

This is a change from DeltaEC version 6.4b2.7. Users who prefer to keep the earlier calculation for helium transport properties can create a <helium.tpf> file, with ideal-gas expressions for $\rho , c _ { p } .$ , and $^ { a , }$ and with $\mu = 0 . 4 1 2 \times 1 0 ^ { - 6 } \ : T ^ { 0 . 6 8 0 1 4 } , k = 0 . 0 0 2 5 6 7 2 \ : T ^ { 0 . 7 1 6 } . )$

## 12.2 Real helium (CryoHe)

Bicubic spline interpolation based on Ref. [71], whose data are valid over a wide range of temperature and pressure including near the critical point. DeltaEC’s approximate implementation, which computes rapidly, has an accuracy of better than about 2% from 2.2 K to 1500 K and from 0.3 MPa to 4 MPa, except $c _ { p } , \beta _ { ; }$ , and $\gamma$ have errors as high as $5 \%$ at the lowest pressures and at temperatures near the critical temperature. Inconsistencies between properties such as $\rho$ and $\beta _ { ; }$ , or among $\gamma , c _ { p } .$ , and $^ { a , }$ are of the same magnitude, because these are all calculated from separate splines rather than via formulas such as $\beta = - ( 1 / \rho ) \partial \rho / \partial T$

When a user changes the fluid in a model to CryoHe, DeltaEC will change Tmin to 1 Kelvin, giving DeltaEC’s shooting method something to work with during its artificial numerical explorations below 2.2 K. This change will be saved to the .ini file if the model is saved. The user must remember to increase Nint for regenerators that include quickly varying fluid properties.

For each fluid property, such as $\rho ,$ we used the Excel spreadsheet version of Ref. [71] to create a table of the property, normalized by its ideal-gas value, as a function of $1 / T$ and $p _ { m }$ over the ranges noted above, the data being densest near the critical point. Next we used separate software to fit a slightly smoothed bicubic spline to the table, and recorded the coeficients of the spline (in b-spline representation) in the format of a fortran include statement. DeltaEC makes its CryoHe calculations from those coeficients. An example is shown in Figs. 12.1 and 12.2.

## 12.3 Helium–argon mixtures (HeAr)

Number in 0j is helium fraction. Ideal gas approximation for equation of state and specific heat. Transport properties for the pure gases are simple fits to data in Ref. [71], valid above 225 K and below 3 MPa for argon. The expressions that obtain the mixture transport properties from those of the pure gases are less certain, and based on data in Refs. [72, 73].

k0he=0.00273d0\*ta\*\*0.707d0+1.d-9\*(2000.d0-ta)\*\*2\*(1.d0+2.d-14\*pm\*\*2)   
amuhe=0.35d-6\*ta\*\*0.707d0+2.5d-19\*(1300.d0-ta)\*\*4\*(1.d0+2.d-14\*pm\*\*2)   
k0ar=6.55d-4\*ta\*\*0.61d0-0.27d-8\*(ta-1400.d0)\*\*2\*(1.d0-3.5d-14\*pm\*\*2)   
7 73 7 0 621 0 3 3 12 ( 1400 0) 2 (1 0 6 8 )   
k0=x1\*k0ar+x2\*k0he-(k0ar+k0he)\*x1\*x2\*\*1.5   
mu=x1\*amuar+x2\*amuhe+0.2\*(amuar+amuhe)\*x1\*x2   
diff12= 7.49d0\*(1.d0 - 0.05d0\*x2)\*(ta/295.d0)\*\*1.66d0/pm   
ktherm= 0.38d0 \* x2\*\*1.2d0 \* x1\*\*0.8d0

![[mu_66afccee_826bdd14ed9f193e096a.jpg]]  
Figure 12.1: Density of real helium, normalized by its ideal-gas value. Horizontal axis 1/T runs from 1/(1500 K) at the left to 1/(2 K) at the right, although beyond 2.2 K the curves are physically meaningless. Curves are for pressures ranging from 0.3 MPa to 4.0 MPa.

![[mu_66afccee_bc25bbeb57b3d6a10571.jpg]]  
Figure 12.2: Percent diferences between DeltaEC’s CryoHe density and Ref. [71] values, for a few dozen pressures, as a function of $1 / T .$ . The zero crossings are near the “knots” of the b-spline.

## 12.4 Real argon (argon)

Bicubic spline interpolation based on Ref. [71], whose data are valid over a wide range of temperature and pressure including near the critical point. DeltaEC’s approximate implementation, which computes rapidly, has an accuracy of better than about 0.1% from 150 K to 1500 K and from 0.1 MPa to 4 MPa, except $k , c _ { p } , \beta$ , and $\gamma$ have errors as high as 0.5% near 150 K and 4 MPa. Inconsistencies between properties such as $\rho$ and $\beta ,$ or among $\gamma , \ c _ { p } ,$ and $^ { a , }$ are of the same magnitude, because these are all calculated from separate splines rather than via formulas such as $\beta = - ( 1 / \rho ) \partial \rho / \partial T$

Details of the calculation are similar to those described above for CryoHe.

## 12.5 Helium–xenon mixtures (HeXe)

Number in 0j is helium fraction. Ideal gas approximation for equation of state and specific heat. Transport from Refs. [72, 73]. Our fits to the published transport data are only accurate for frxe <0.5 or for frxe =1.000.

k0he=0.00273d0\*ta\*\*0.707d0+1.d-9\*(2000.d0-ta)\*\*2\*(1.d0+2.d-14\*pm\*\*2)  
amuhe=0.35d-6\*ta\*\*0.707d0+2.5d-19\*(1300.d0-ta)\*\*4\*(1.d0+2.d-14\*pm\*\*2)  
k0xe=4.75e-5\*ta\*\*0.84\*(1.+1.e-7\*pm)  
amuxe=0.187e-6\*ta\*\*0.85\*(1.+25.e-9\*pm)  
frxe=1.-fhe  
k0=k0he\*fhe+k0xe\*frxe-2.\*(k0he+k0xe)\*frxe\*fhe\*fhe  
mu=amuhe\*fhe+amuxe\*frxe+(amuhe+amuxe)\*frxe\*fhe\*fhe\*(0.8+3.7\*fhe\*fhe\*(0.25-frxe))  
diff12=5.9d0\*(1.d0-0.074d0\*litefrac)\*(ta/300.d0)\*\*1.72d0/0.96d0/pm  
ktherm= 0.4d0 \* litefrac\*\*1.3d0 \* frxe\*\*0.7d0

## 12.6 Neon (neon)

Ideal gas approximation for equation of state and specific heat. Transport from Ref. [74].

k0=0.001149\*ta\*\*0.65907   
mu=0.735e-6\*ta\*\*0.66065

## 12.7 Air (air)

Ideal gas approximation for equation of state and specific heat. Transport from Ref. [61].

```javascript
parameter (tps=110.4,tpa=245.4,tpb=27.6,tp0=300.,tpexp=223.8306)
k0=2.624e-2*(ta/tp0)**1.5*(tp0+tpexp)/(ta+tpa*exp (-tpb/ta))
mu=1.846e-5*(ta/tp0)**1.5*(tp0+tps)/(ta+tps)
```

## 12.8 Humid air and fog (HumidAir)

The number in 0j is the water mole fraction in a mixture of air and water. As with other gas mixtures, the water mole fraction can be modified or used as an independent plot variable. However, unlike other gas mixtures, the MIX\*\* segments do not act on humid air. We worry that future improvements to understanding will bring dramatic change to this part of DeltaEC. Nevertheless, for the present:

In DeltaEC, we think of humid and wet air as a sort of single gas, having two or three interpenetrating components: dry air, water vapor, and sometimes liquid water.

The molar volume v and molar enthalpy w are DeltaEC’s primary dependent variables, as functions of three independent variables: mean pressure $p _ { m }$ , mean temperature $T _ { m }$ , and mole fraction of water $n _ { \mathrm { w a t } }$ . To determine whether a given mixture is wet or merely humid, DeltaEC compares $n _ { \mathrm { w a t } }$ with $p _ { \mathrm { s a t } } / p _ { m }$ , where $p _ { \mathrm { s a t } } ( T _ { m } )$ is the saturated vapor pressure at temperature $T _ { m }$

For humid air, DeltaEC uses the ideal-gas equation of state for v and a slightly nonlinear temperature dependence for $w$ (due to the $T$ dependence of $c _ { p }$ for water vapor in the ASHRAE tables). Also in accordance with ASHRAE recommendations, we set $\mu$ and k equal to their dry-air values.

In wet air, in accordance with Hiller’s measurements [75], the oscillating thermodynamics in DeltaEC is that of humid air at saturation, while the mean flow thermodynamics includes the enthalpy of the liquid when $\dot { N } \neq 0$ . In other words, if there is no mean flow, the calculation proceeds exactly as for an ideal-gas mixture and ignores the condensate, but if mean flow is nonzero DeltaEC performs stack integrations with idealgas-mixture properties in the momentum and continuity equations but with the heat of condensation/evaporation (plus the small enthalpy of the condensate itself) included in the energy equation as it is integrated to find $d T _ { m } / d x$ . In all cases, we ignore the dynamic efects of oscillating difusion of the water vapor through the air, which have been described by Raspet [76] and Slaton [77].

Although the enthalpy of wet air calculated in DeltaEC’s gas-properties algorithm includes the latent heat of freezing and melting as the condensate passes through $0 ^ { \circ } \mathrm { C }$ , we have not yet incorporated this latent heat, of the liquid-to-solid phase transition, into the numerical integrations in STK\*\* segments, so integrating through $T _ { m } = 0 ^ { \circ } \mathrm { C }$ in wet air is of dubious value. (Anyway, we have not thought of any good reason to use wet air in DeltaEC below $0 ^ { \circ } \mathrm { C }$ , because we believe the stack would simply plug up with ice.)

The saturated vapor pressure is accurate from $- 1 0 0 ^ { \circ } \mathrm { C }$ to $3 7 0 ^ { \circ } \mathrm { C } ;$ other properties are reasonably accurate from $- 5 0 ^ { \circ } \mathrm { C }$ to $1 5 0 \mathrm { { } ^ { \circ } C }$

## 12.9 Nitrogen (nitrogen)

Ideal gas approximation for equation of state and specific heat. Transport from Ref. [74].

k0=0.0003609\*ta\*\*0.7512   
mu=0.3577e-6\*ta\*\*0.6885

## 12.10 Real hydrogen (H2normal and H2para)

Bicubic spline interpolation based on Ref. [71], whose data are valid over a wide range of temperature and pressure including near the critical point. Regarding the spin isomers of hydrogen, Ref. [71] says

“Two equations of state are available for hydrogen to account for the diferent quantum states of the molecule. Normal hydrogen should be used in applications where it was created and stored at 250 K or above, or when it was cooled to below 250 K and stored without a catalyst for less than a day. The parahydrogen equation should be used where hydrogen was catalyzed or stored for several days at the normal boiling point and used at any temperature within 1 day of storage at the NBP. Since the rate of conversion between quantum states is dependent on temperature, pressure, and the storage container, these values are only estimates.”

DeltaEC’s approximate implementation, which computes rapidly, has an accuracy of better than 0.3% from 0.1 to 1 MPa and from the boiling temperature to 1000 K, except at the coldest temperatures near 1 MPa, where errors rise to 1.5% for $\mu$ and 0.7% for the other properties. Inconsistencies between properties such as $\rho$ and $\beta _ { ; }$ or among $\gamma , c _ { p } .$ , and $^ { a , }$ are of the same magnitude, because these are all calculated from separate splines rather than via formulas such as $\beta = - ( 1 / \rho ) \partial \rho / \partial T$

Details of the calculation are similar to those described above for CryoHe.

## 12.11 Ideal-gas hydrogen (hydrogen)

Ideal gas approximation for equation of state and specific heat. Transport from Ref. [74].

k0=0.002627\*ta\*\*0.744   
mu=0.19361e-6\*ta\*\*0.6723

## 12.12 Deuterium (deuterium)

Ideal gas approximation for equation of state and specific heat. Transport from Ref. [74].

k0=0.002795\*ta\*\*0.686  
mu=0.2726e-6\*ta\*\*0.6721

## 12.13 Carbon dioxide (CO2)

Before DeltaEC version 6.4b2.9, these equations provided a 1% match to the data available at webbook.nist.gov/chemistry/fluid/ from 300 K to 1100 K at 1 bar, 5 bar, and 10 bar.

DATA cpco2/ 560.0d0, 1.13d0, -0.00045d0, 4.0d-9, 1.5d0, 100.0d0 /   
DATA aco2/ -0.015d0, 7.0d0, 1.0d-5, 400000.0d0 /   
DATA rhoco2/ 4.3d-9, 1.7, 70.0 /   
DATA kco2/ 2.8d-5, 1.1395d0, 4.0d-4, 4.0d-10, -2.2d-8, 625.0d0 /   
DATA muco2/ 1.4187d-7, 0.8216d0, 1.5416d-7, 0.8094d0, -8.0d-12, 650.0d0, 8.0d-7 /   
oldgam=1.2857d0   
massavg=0.04401d0   
r=runiv/massavg   
cp=cpco2(1)+cpco2(2)\*ta+cpco2(3)\*ta\*\*2+cpco2(4)\*pm\*\*cpco2(5)\*ta\*dexp(-ta/cpco2(6))   
enth=cpco2(1)\*(ta-tzero)+cpco2(2)/2.\*(ta\*\*2-tzero\*\*2)+cpco2(3)/3.\*(ta\*\*3-tzero\*\*3)   
& -cpco2(4)\*pm\*\*cpco2(5)\*cpco2(6)   
& \*(dexp(-ta/cpco2(6))\*(1+ta/cpco2(6))-dexp(-tzero/cpco2(6))\*(1+tzero/cpco2(6)))   
entro=cpco2(1)\*dlog(ta/tzero)+cpco2(2)\*(ta-tzero)   
& +cpco2(3)/2.\*(ta\*\*2-tzero\*\*2)-cpco2(4)\*pm\*\*cpco2(5)\*cpco2(6)   
& \*(dexp(-ta/cpco2(6))-dexp(-tzero/cpco2(6)))   
a=dsqrt(oldgam\*r\*ta)+aco2(1)\*(1+dexp(-pm/aco2(4)))\*ta+aco2(2)-aco2(3)\*pm   
rho=pm/r/ta+rhoco2(1)\*pm\*\*rhoco2(2)\*dexp(-ta/rhoco2(3))   
beta=(pm/r/ta\*\*2+rhoco2(1)/rhoco2(3)\*pm\*\*rhoco2(2)\*dexp(-ta/rhoco2(3)))/rho   
gamma=ta\*beta\*\*2 \* a\*\*2/cp + 1.0d0   
k0=kco2(1)\*ta\*\*kco2(2)+kco2(3)+kco2(4)\*pm+ kco2(5)\*(ta-kco2(6))\*\*2   
mu=muco2(1)\*ta\*\*muco2(2)+(pm/1.0d6-1.0d0)\*(muco2(3)\*ta\*\*muco2(4)   
& -muco2(1)\*ta\*\*muco2(2))+muco2(5)\*(ta-muco2(6))\*\*2+muco2(7)

![[mu_66afccee_984b6d4993c4fffe072a.jpg]]

Figure 12.3: Black lines show the boundary of the region of pressure–temperature in which the bicubic spline fit gives accurate values for carbon-dioxide properties. Red line is the vapor-pressure curve, ending in the critical point.  
![[mu_66afccee_680a63002396000ee8c1.jpg]]  
Figure 12.4: DeltaEC’s values for carbon dioxide $T _ { m } \beta$ near the critical temperature, for eleven values of mean pressure: 15 bar, 25 bar, 35 bar, ... 115 bar.

Beginning with DeltaEC version 6.4b2.9c, those equations are used below 10 bar, and a bicubic spline interpolation based on the properties of carbon dioxide in Ref. [71] is used above 10 bar. DeltaEC’s interpolation computes rapidly, and has an accuracy better than 1% for all properties, within the zone shown in Fig. 12.3. Inconsistencies between properties such as $\rho$ and $\beta _ { ; }$ , or among $\gamma , c _ { p } .$ , and $^ { a , }$ exist because these are all calculated from separate splines rather than via formulas such as $\beta = - ( 1 / \rho ) \partial \rho / \partial T$ . Two examples of properties of carbon dioxide are shown in Figs. 12.4 and 12.5.

## 12.14 Neon–xenon mixtures (NeXe)

The number in $0 \mathrm { j }$ is neon fraction. Ideal gas approximation for equation of state and specific heat. Transport from Refs. [72, 73]. (Thermal conductivity not very accurate for high xenon concentrations.)

![[mu_66afccee_165f4d2248334f462eed.jpg]]  
Figure 12.5: DeltaEC’s values for carbon dioxide $c _ { p }$ near the critical temperature, normalized by $6 R _ { \mathrm { u n i v } } / m$ , for eleven values of mean pressure: 15 bar, 25 bar, 35 bar, ... 115 bar.

amuhe=0.735e-6\*ta\*\*0.66065   
k0xe=4.75e-5\*ta\*\*0.84\*(1.+1.e-7\*pm)   
amuxe=0.187e-6\*ta\*\*0.85\*(1.+25.e-9\*pm)   
frxe=1.-fhe(ns)   
k0=k0he\*fhe(ns)+k0xe\*frxe-1.3\*(k0he+k0xe)\*frxe\*fhe(ns)\*\*2.5   
mu=amuhe\*fhe(ns)+amuxe\*frxe+0.12\*(amuhe+amuxe)\*frxe\*fhe(ns)\*\*4   
diff12=2.21d0\*(1.d0+0.0326d0\*frxe/(1.d0+0.531d0\*frxe))\*(ta/300.d0)\*\*1.71d0/pm   
ktherm= 0.258d0 \* litefrac\*\*1.31d0 \* frxe\*\*0.69d0

## 12.15 Natural-gas combustion products (NGCbProd)

Natural Gas combustion products with 5% excess air. Use around 1 atm only. Our 1993 notes say “Data supplied by British Gas (private communication from R. J. Tucker to Bill Ward) for typical North-Sea gas. Molar weight is a fit to data in Ref. [78] between 288 K and 4000 K.”

```matlab
gamma=1.4
cp=gasprop(ta,1392.02d0,39.3769d0,-3.89819d0,-0.0317961d0,
0.0327554d0,-1.44149d-3)
if (ta.gt.2000.) then
mass=27.9495-7.81175*dexp(-((ta-4151.85)/1047.42)**2)
else
mass=27.84
endif
r=8314.
a=dsqrt(gamma*r*ta/mass)
rho=pm*mass/(r*ta)
beta=1./ta
k0=gasprop(ta,0.0997279d0,0.0125516d0,6.73728d-5,4.22761d-4,
1.43198d-4,1.35508d-5)
mu=gasprop(ta,50.2973d0,4.68523d0,-0.12061d0,0.0140082d0,
-0.001488951d0,4.97968d-5)*1.d-6
return
real*8 function gasprop(ta,a,b,c,d,e,f)
real*8 z,ta,a,b,c,d,e,f
z=(ta-1400)/200
gasprop=a+z*(b+ z*(c + z*(d +z*(e+f*z))))
return
end
```

## 12.16 Liquid sodium (sodium)

Data for sodium from Ref. [79].

a0=2578.   
at1=-.52   
ap=6.1e-7   
r0=950.1   
rt1=-2.2976e-1   
rt2=-1.46e-5   
rt3=5.638e-9   
c0=1.4361e3   
ct1=-5.8024e-1   
ct2=4.6208e-4   
k0=.918e2-4.9e-2\*t1   
if(t1.le.500.) then   
e1=.697   
e2=1.235e-5   
else   
e1=1.04   
e2=8.51e-6   
endif   
a=a0+at1\*t1   
rho=r0+rt1\*t1+rt2\*t1\*\*2+rt3\*t1\*\*3   
beta=(-rt1-2.\*rt2\*t1-3.\*rt3\*t1\*\*2)/rho   
bt=beta\*\*2-(2.\*rt2+6.\*rt3\*t1)/rho   
cp=c0+ct1\*t1+ct2\*t1\*\*2   
rp=1./a/a+ta\*beta\*\*2/cp   
bp=-beta/(rho\*a\*\*2)+2.\*at1/(rho\*a\*\*3)-beta\*\*2/rho/cp   
bp=bp-2.\*ta\*beta\*bt/rho/cp-ta\*beta\*\*3/rho/cp   
bp=bp+ta\*beta\*\*2\*(ct1+2.\*ct2\*t1)/rho/cp/cp   
cpp=-ta\*(beta\*\*2+bt)/rho   
c So far, everything is evaluated at p=0.   
a=a+ap\*pm   
rho=rho+rp\*pm   
beta=beta+bp\*pm   
cp=cp+cpp\*pm   
gamma=1.+ta\*beta\*\*2\*a\*\*2/cp   
mu=e2\*rho\*\*(1./3.)\*exp (e1\*rho/ta)

## 12.17 Liquid sodium–potassium eutectic (NaK-78)

This is for eutectic sodium–potassium; data from Ref. [79].

a0=2051.   
at1=-.53   
ap=0.   
r0=876.4   
rt1=-2.183e-1   
rt2=-2.982e-5   
rt3=0.   
c0=970.69   
ct1=-.36903   
ct2=3.4309e-4   
k0=21.4+2.07e-2\*t1-2.2e-5\*t1\*\*2   
if(t1.le.400.) then   
e1=.688   
e2=1.16e-5   
else   
e1=.979   
e2=8.2e-6   
endif   
a=a0+at1\*t1   
rho=r0+rt1\*t1+rt2\*t1\*\*2+rt3\*t1\*\*3   
beta=(-rt1-2.\*rt2\*t1-3.\*rt3\*t1\*\*2)/rho   
bt=beta\*\*2-(2.\*rt2+6.\*rt3\*t1)/rho   
cp=c0+ct1\*t1+ct2\*t1\*\*2   
rp=1./a/a+ta\*beta\*\*2/cp   
bp=-beta/(rho\*a\*\*2)+2.\*at1/(rho\*a\*\*3)-beta\*\*2/rho/cp   
bp=bp-2.\*ta\*beta\*bt/rho/cp-ta\*beta\*\*3/rho/cp   
bp=bp+ta\*beta\*\*2\*(ct1+2.\*ct2\*t1)/rho/cp/cp   
cpp=-ta\*(beta\*\*2+bt)/rho   
c So far, everything is evaluated at p=0.   
a=a+ap\*pm   
rho=rho+rp\*pm   
beta=beta+bp\*pm   
cp=cp+cpp\*pm   
gamma=1.+ta\*beta\*\*2\*a\*\*2/cp   
mu=e2\*rho\*\*(1./3.)\*exp (e1\*rho/ta)

line 1: $\rho _ { m }$   
line 2: $c _ { p }$   
line 3: $k$   
line 4: $a ^ { 2 }$   
line 5: $\mu$

## 12.18 User-defined gases

## 12.18.1 User-defined pure gases

Files that define non-standard gases can have any name valid under the operating system under which DeltaEC is running, and should end with the extension <.tpf>. If the root filename is the same as any pre-defined gases, DeltaEC replaces its internal calculations for that gas with those given in the user’s file. The <.tpf> file should be in the same directory or folder as the model file. The name of the gas is set to the root filename of the user-defined gas file. Up to five distinct user-defined gases can be active at one time. Please limit the root of the file name to eight characters.

Each of five gas properties is specified by a line containing 1–10 real coeficients to be read in as $C _ { 0 } C _ { 1 } \ldots C _ { 9 }$ . Trailing unspecified parameters are taken to be zero. The order of the property lines is $\rho _ { m } , c _ { p } , k , a ^ { 2 }$ , and $\mu .$ Comment lines can be inserted anywhere in the <.tpf> file with an initial ‘!’, and blank lines are not allowed.

It is critical that the properties be arranged in this order: 0

Each of the five properties is derived from its 10 coeficients using the following equation:

$$
\mathrm { g a s \ p r o p e r t y } = C _ { 0 } + C _ { 1 } \frac { p _ { m } } { T _ { m } + C _ { 2 } p _ { m } } + C _ { 3 } T _ { m } + C _ { 4 } T _ { m } ^ { 2 } + C _ { 5 } T _ { m } ^ { C _ { 6 } } + C _ { 7 } p _ { m } ^ { 2 } T _ { m } ^ { C _ { 8 } } + C _ { 9 } p _ { m } ,\tag{12.1}
$$

where $T _ { m }$ and $p _ { m }$ are the absolute temperature (K) and mean pressure (Pa). An example <.tpf> file is shown in Section 2.6.3.

Equation (12.1) is a compromise between simplicity and flexibility; it is intended for use with a variety of simple expressions for gases and liquids and has a uniform syntax for specifying all five properties. There is only a limited mean-pressure dependence, suitable for nearly ideal gases; for more complicated mean-pressure dependence, multiple <.tpf> files should be written for each range of mean pressure used.

DeltaEC also needs the ratio of specific heats, $\gamma ,$ and the expansion coeficient $\beta _ { ; }$ but these are calculated internally from

$$
\beta = - \frac { 1 } { \rho } \frac { { \partial \rho } } { { \partial T } } \ \mathrm { a n d } \ \gamma = 1 + \frac { { T \beta ^ { 2 } } { a ^ { 2 } } } { c _ { p } } .\tag{12.2}
$$

To employ a user-defined gas, select its filename as the gas type in a BEGIN segment.

User-defined gases specified by $< . \tt t p f >$ files cannot be used with nonzero $\dot { N }$ , because Eq. (6.1) requires $m$ , which is not available in $< . \tt t p f >$ format. To circumvent this shortcoming when a user-defined gas must be used with nonzero $\dot { N }$ , use a <.tpm> file as described in the next Section, and set the mole fraction of the unused component to zero in the BEGIN segment of the model.

## 12.18.2 User-defined gas mixtures

The user can define the properties of his/her own binary ideal-gas mixture that is not a member of DeltaEC’s internal library of mixtures, by using a file <filename.tpm> in the folder in which the DeltaEC model is running. If filename is one of DeltaEC’s known gases, DeltaEC will replace its own properties with the user’s properties. Please limit filename to eight characters.

The file format, shown below, is similar to that of $< . \tt t p f >$ files for pure gases. Blank lines are not allowed, and extra lines beginning with $\mathbf { \check { \Psi } } ^ { ( 4 ) } \mathbf { \Psi } _ { : } ^ { ( 5 ) }$ are regarded as comments, which are very useful for keeping track of which line is which.

Properties are functions of mean pressure $p _ { m } \ \mathrm { ( P a ) }$ , absolute temperature $T _ { m } ~ \mathrm { { ( K ) } }$ , and mole fraction $n _ { L }$ . Each function is specified by a line containing a sequence of real coeficients (separated by blanks) which are read sequentially. Unused trailing parameters are set to zero. The properties must be arranged in this order:

line 1: m<sub>L</sub> m<sub>H</sub> γ<sub>L</sub> γ<sub>H</sub>

line 2: $k _ { \mathrm { p u r e } ~ L }$

line 3: $k _ { \mathrm { p u r e } \ H }$

line 4: $\mu _ { \mathrm { p u r e } ~ L }$

line 5: µ<sub>pure</sub> <sub>H</sub>

line 6: $k _ { \mathrm { m i x } }$

line 7: $\mu _ { \mathrm { m i x } }$

line 8: $D _ { 1 2 }$

line 9: $k _ { T }$

The four numbers in line 1, which are $m _ { L } , m _ { H } , \gamma _ { L }$ , and $\gamma _ { H }$ , are used to calculate state properties based on ideal-gas behavior as follows:

$$
m _ { \mathrm { a v g } } = m _ { L } n _ { L } + m _ { H } \left( 1 - n _ { L } \right) ,\tag{12.3}
$$

$$
\rho _ { m } ~ = ~ { \frac { p _ { m } m _ { \mathrm { a v g } } } { R _ { \mathrm { u n i v } } T _ { m } } } ,\tag{12.4}
$$

$$
\frac { 1 } { \gamma - 1 } = \frac { n _ { L } } { \gamma _ { L } - 1 } + \frac { 1 - n _ { L } } { \gamma _ { H } - 1 } ,\tag{12.5}
$$

$$
a ^ { 2 } = \frac { \gamma R _ { \mathrm { u n i v } } T _ { m } } { m _ { \mathrm { a v g } } } ,\tag{12.6}
$$

$$
c _ { p } = \frac { \gamma } { \gamma - 1 } \frac { R _ { \mathrm { u n i v } } } { m _ { \mathrm { a v g } } } .\tag{12.7}
$$

The pure-gas transport properties, $k _ { \mathrm { p u r e } \ L } , \ k _ { \mathrm { p u r e } \ H } , \ \mu _ { \mathrm { p u r e } \ L }$ , and $\mu _ { \mathrm { p u r e } \ H }$ , are calculated from numbers $C _ { 0 } C _ { 1 } \ldots C _ { 9 }$ in each of lines 2 through 5 using the following equation:

$$
\mathrm { p r o p e r t y } = C _ { 0 } + C _ { 1 } \frac { p _ { m } } { T + C _ { 2 } p _ { m } } + C _ { 3 } T + C _ { 4 } T ^ { 2 } + C _ { 5 } T ^ { C _ { 6 } } + C _ { 7 } p _ { m } ^ { 2 } T ^ { C _ { 8 } } + p _ { m } C _ { 9 } .\tag{12.8}
$$

Equation (12.8) is a compromise between simplicity and flexibility. It is intended for use with most coeficients set to zero in a variety of simple expressions. Finally, the numbers in

lines 6 through 9 are used in these equations:

line 6:

$$
k _ { \mathrm { m i x } } = n _ { L } k _ { \mathrm { p u r e } \ L } + \left( 1 - n _ { L } \right) k _ { \mathrm { p u r e } \ H } + \left( C _ { 0 } + C _ { 1 } T _ { m } ^ { C _ { 2 } } \right) n _ { L } ^ { C _ { 3 } } \left( 1 - n _ { L } \right) ^ { C _ { 4 } } ,\tag{12.9}
$$

line 7:

$$
\mu _ { \mathrm { m i x } } = n _ { L } \mu _ { \mathrm { p u r e } L } + \left( 1 - n _ { L } \right) \mu _ { \mathrm { p u r e } H } + \left( C _ { 0 } + C _ { 1 } T _ { m } ^ { C _ { 2 } } \right) n _ { L } ^ { C _ { 3 } } \left( 1 - n _ { L } \right) ^ { C _ { 4 } }\tag{,(12.10}
$$

line 8:

$$
D _ { 1 2 } = \frac { C _ { 0 } } { \left( p _ { m } / [ 1 0 ^ { 5 } \mathrm { ~ P a } ] \right) } \left( 1 - C _ { 1 } n _ { L } \right) \left( \frac { T _ { m } } { [ 3 0 0 \mathrm { ~ K } ] } \right) ^ { C _ { 2 } } + C _ { 3 } ,\tag{12.11}
$$

line 9:

$$
k _ { T } = C _ { 0 } n _ { L } ^ { C _ { 1 } } \left( 1 - n _ { L } \right) ^ { C _ { 2 } } \left( \frac { T _ { m } } { \left[ 3 0 0 \mathrm { ~ K } \right] } \right) ^ { C _ { 3 } } + C _ { 4 } .\tag{12.12}
$$

As an example of the use of these coeficients, consider the example below for neon, a mixture of two isotopes.

```fortran
! user-defined mixture: neon, a mixture of two isotopes, 20 and 22.
! Natural abundance is nL = 0.91
! mL(kg/mole) mH(kg/mole) gammaL gammaH:
0.01999 0.02199 1.6667 1.6667
! k pure L (W/m-K):
0. 0. 0. 0. 0. 0.00122 0.65
! k pure H (W/m-K):
0. 0. 0. 0. 0. 0.00116 0.65
! mu pure L (kg/m-s):
0. 0. 0. 0. 0. 7.41E-7 0.66
! mu pure H (kg/m-s):
0. 0. 0. 0. 0. 7.70E-7 0.66
! k mixture (W/m-K):
0.
! mu mixture (kg/m-s):
0.
! D12 (m2/s):
0.53E-4 0. 1.72
! kT:
0.0267 1.0 1.0
```

To employ a user-defined mixture, select its filename as the gas type in a BEGIN segment.

## 13. Solids

We provide an artificial temperature floor Tmin = 10 Kelvin and an artificial ceiling Tmax = 9999 Kelvin to prevent DeltaEC from trying to use extreme or even negative temperatures when it is really lost. Consequently, no temperatures beyond these extremes should be used. (Most of the equations for the fluids or solids are very inaccurate when these limits are reached anyway.) DeltaEC’s numerical integration can naively carry $T _ { m }$ beyond these bounds, but the underlying evaluation of the thermophysical properties is clipped at Tmin or Tmax. The 10-K floor can be modified within Options in the Edit pulldown menu, and it is automatically reduced when CryoHe is used.

In what follows, ta is temperature in Kelvin, t1 is temperature in Celsius.

DeltaEC looks for a 10-character field to determine solid type. When editing a <.out> file with a text editor, be sure to use plenty of trailing spaces after short solid names like “mylar” to get “solid-type” out of the 10-character field.

Equations used here accurately cover ranges of T and p that have been of interest to the Los Alamos thermoacoustics team. No warning is issued by DeltaEC if it goes outside the accurate range. It is up to the user to study the equations here, or examine the results of these equations via the properties tokens in an RPN segment or the thermophysicalproperties dialog, and decide if these equations are accurate enough or if a user-defined solid is necessary.

## 13.1 Ideal solid (ideal)

ks, rhos, and cs are efectively infinite, so $\epsilon _ { s } = 0$

ks=1.d8   
rhos=1.d8   
cs=1.d8

## 13.2 Heavium (heavium)

Intended for exploring the idealized physics of cryogenic regenerators, “heavium” has plenty of heat capacity, to enforce $\epsilon _ { s } = 0$ , but a reasonable thermal conductivity (the same as that of antimonial lead).

ks=4.57d0\*ta\*\*0.33d0 ! same as Pb95Sn05   
rhos=1.d10   
cs=1.d2 ! approx 50 K Pb95Sb05

## 13.3 Copper (copper)

ks=398.-.0567\*(ta-300.)   
rhos=9000.   
cs=420.

## 13.4 Nickel (nickel)

if (ta.lt.631) then   
ks=63.8+.08066\*(631.-ta)   
else   
ks=63.8+.02156\*(ta-631.)   
endif   
rhos=8700.   
cs=530.

## 13.5 Stainless steel (stainless)

Type 304 stainless steel from 6 K to 1300 K. Conductivity data from Ref. [80] and upmet.com.   
Density from Refs. [80, 81], bssa.org.uk, and upmet.com. Specific heat from Refs. [80, 82].

rhos=7993-(0.3\*ta+0.00008\*ta\*\*2)\*ta\*\*2/(20000+ta\*\*2)   
ks=(266800\*ta\*\*(-5.2)+0.21416\*ta\*\*(-1.6))\*\*(-0.25)   
cs=(1.7054e-6\*ta\*\*(-0.88962)+23324/ta\*\*6)\*\*(-1/3) + 15/ta - 35/ta\*\*2 + 25/ta\*\*3

Prior to version 3.5b2, DeltaEC’s stainless steel properties were very inaccurate at cryogenic temperatures.

## 13.6 Molybdenum (molybdenum)

rhos= 10868.6 -2637.52 \* exp (-((T1-11383.7)/9701.36)\*\*2)   
cs= 253.791 +0.0583812 \*T1-2.73919e-06\*T1\*\*2   
ks= (33.9616 -0.00947953 \*T1-4.12809e-08\*T1\*\*2)\*4.186

## 13.7 Tungsten (tungsten)

```javascript
cs=.13576e3*(1.-4805./ta**2)+.0091159*ta+2.31341e-9*ta**3
ks=135.5+1.05e4/ta-.023*ta
rhos=19254*(1.-3.*(-8.69e-5+3.83e-6*t1+7.92e-10*t1**2))
```

## 13.8 Kapton (kapton)

ks=0.2\*(1.-exp(-ta/100.))   
rhos=1445.-0.085\*ta   
cs=3.64\*ta

## 13.9 Mylar (mylar)

ks=0.11+1.7e-4\*ta   
rhos=1400.-0.175\*ta   
cs=3.7\*ta

## 13.10 Celcor (celcor)

Properties from Steve Garrett, Penn State University (private communication).

ks=2.5   
rhos=2510.   
cs=262.5 + 1.864\*ta - 0.001011\*ta\*\*2

## 13.11 Phosphor bronze (P-bronze)

Phosphor bronze with 5% by weight tin. Density from alloys.copper.org. Thermal expansion coeficient and specific heat from Ref. [83]. Thermal conductivity from lakeshore.com. Formulas are accurate below 300 K.

logt=DLOG10(ta)   
ks=1.4731\*logt\*\*3+4.6076\*logt\*\*2-1.2418\*logt+0.2213   
vexco=3.d0\*(-5.25d-11\*ta\*\*2+3.305e-8\*ta+1.1755d-5)   
rhos=8600.\*(1.d0-vexco\*(ta-300.))   
logcs=0.39199\*logt\*\*5-2.5868\*logt\*\*4+5.49693\*logt\*\*3-4.14538\*logt\*\*2+3.02208\*logt-2.22073   
cs=10\*\*logcs

## 13.12 Gadolynium oxysulfide (a.k.a GOS; Gd2O2S)

Thermal conductivity from Ref. [84]; formula is only accurate below 15 or 20 K. Density from wikipedia; thermal expansion coeficient is neglected. Specific heat interpolated from a table of $\rho _ { s } c _ { s }$ from 1 K to 300 K from Ref. [85]. DeltaEC’s results of this interpolation are shown in Fig. 13.1.

ks=-0.0162\*ta\*\*2+1.0635\*ta-2.4576   
rhos=7320.   
cs=splevcaller(ta)

## 13.13 Antimonial lead (Pb95Sb05)

Lead with 5% antimony. Density at room temperature the average of values given in Ref. [86] for 4% and 6% antimony. Thermal expansion ignored. Thermal conductivity at room temperature from Ref. [86]. Thermal conductivity from [84]; formula is only accurate below 15 or 20 K. Specific heat interpolated from a table of $\rho _ { s } c _ { s }$ from 1 K to 300 K from Ref. [85]. DeltaEC’s results of this interpolation are shown in Fig. 13.1.

ks=4.57d0\*ta\*\*0.33d0   
rhos=10950.d0   
cs=splevcaller(ta)

## 13.14 HoCu<sub>2</sub> (HoCu2)

Following Ref. [87] and without finding any data, we use the thermal conductivity of stainless steel here. Density from materialsproject.org; thermal expansion coeficient is neglected. Specific heat interpolated from a table of $\rho _ { s } c _ { s }$ from 1 K to 300 K from Ref. [85]. DeltaEC’s results of this interpolation are shown in Fig. 13.1.

![[mu_66afccee_1748167a55a3066ceadb.jpg]]  
Figure 13.1: Specific heats of the five solids calculated via interpolation of tables.

ks=(266800.d0\*ta\*\*(-5.2d0)+0.21416d0\*ta\*\*(-1.6d0))\*\*(-0.25d0) ! same as stainless for now   
rhos=9162.d0   
cs=splevcaller(ta)

## 13.15 50-50 erbium praseodymium alloy (Er50Pr50)

Following Ref. [87] and without finding any conductivity data, we use the thermal conductivity of stainless steel here. Density a suitable average of the densities of the pure metals. Thermal expansion coeficient is neglected. Specific heat interpolated from a table of $\rho _ { s } c _ { s }$ from 1 K to 300 K from Ref. [85]. DeltaEC’s results of this interpolation are shown in Fig. 13.1.

ks=(266800.d0\*ta\*\*(-5.2d0)+0.21416d0\*ta\*\*(-1.6d0))\*\*(-0.25d0) ! same as stainless for now   
rhos=7750.d0   
cs=splevcaller(ta)

## 13.16 50-50 erbium nickel alloy (ErNi)

Thermal conductivity from [84]. Density a suitable average of the densities of the pure metals. Thermal expansion coeficient is neglected. Specific heat interpolated from a table of $\rho _ { s } c _ { s }$ from 1 K to 300 K from Ref. [85]. DeltaEC’s results of this interpolation are shown in Fig. 13.1.

## 13.17 User-defined solids

User-defined solids, like user-defined gases, are derived from coeficients in user-written text files that must be named <filename.tpf>. Please limit filename to eight characters. Up to five user-defined solids can be active at once. Each of three properties is specified by a line containing 1–10 real coeficients to be read in as $C _ { 0 } \ C _ { 1 } \ C _ { 2 } \ \dots \ C _ { 9 }$ , where unspecified parameters are taken to be zero. The order of the property lines is

line 1: $\rho _ { s }$

line 2: $c _ { s }$

line 3: $k _ { s }$

Comment lines can be added with an initial ‘!’, and blank lines are not allowed.

Each of the three properties is derived from its 10 coeficients using the following equation:

$$
\mathrm { p r o p e r t y } = C _ { 0 } + C _ { 1 } \exp ( - C _ { 2 } T _ { m } ) + C _ { 3 } T _ { m } + C _ { 4 } T _ { m } ^ { 2 } + C _ { 5 } T _ { m } ^ { C _ { 6 } } + C _ { 7 } p _ { m } ^ { 2 } T _ { m } ^ { C _ { 8 } } + C _ { 9 } p _ { m } .\tag{13.1}
$$

To request a user-defined solid, simply use the root file name as the solid type. The <.tpf> file should be in the same directory or folder as the model file. If the name matches any pre-defined solid name, the (constant) user-defined properties will replace DeltaEC’s internal calculations.

User-defined gases and user-defined solids share the <.tpf> file extension. DeltaEC can tell the diference between a solid and a fluid via the number of non-comment lines in the file.

Back Matter

## 14. Derivations

In this appendix, we present our derivations of a few aspects of DeltaEC that are not derived or fully explained in the archival thermoacoustics literature. Sections below include: ◦ The oscillating force on the pressure vessel due to the fluid motion inside,

◦ How DeltaEC splits second-order time-averaged pressure into the part that can contribute to streaming around a loop and the part that cannot contribute,

◦ The calculation of $\left. T _ { 1 } \right.$ in STKSCREEN, STKPOWERLW, SX, and PX, involving $d T _ { m } / d x$ in the first two of those segments,

◦ A third-order contribution to second-order time-averaged pressure, which DeltaEC includes in some segments,

◦ Magnetic saturation in the pole tips of linear motors and alternators,

◦ Pulsating combustion in DeltaEC models.

## 14.1 Force $F _ { 1 }$ on pressure vessel

Consider a rigid, uniaxial pressure vessel containing a thermoacoustic gas oscillation at angular frequency $\omega .$ . Newton’s laws of motion show that the force exerted by the gas (and by moving parts of transducers, if present) on the rigid pressure vessel equals the force exerted on the gas (and optional transducers) $b y$ the rigid vessel, and this force equals the rate of change of momentum $\rho \mathbf { v }$ of the gas (and optional transducers). Consider only forces and motion at $\omega .$ . Then the total first-order oscillating force exerted on the rigid pressure vessel by the oscillations inside it, in the x direction, is

$$
F _ { 1 } = - i \omega \int { ( \rho _ { m } u _ { 1 } ) } d V = - i \omega \int { \rho _ { m } ( x ) } U _ { 1 } ( x ) d x .\tag{14.1}
$$

The right-hand side of this equation is what DeltaEC’s RPN force operator, F1, calculates; this operator is described in Section 11.4.1. If $F _ { 1 } = 0$ , the vessel does not vibrate. Otherwise, if the vessel is freely suspended and we want to learn its acceleration amplitude, we simply divide by its mass M; if we want its velocity amplitude, we divide by iωM; its displacement amplitude, we divide by $- \omega ^ { 2 } M$

Equation (14.1) includes both the normal force exerted by gas pressure on the vessel and the shear force exerted by viscosity and gas velocity on the vessel. Newton’s laws say that this must be true, but it can also be verified directly, as follows. Calculus shows that

$$
\frac { \partial } { \partial t } \left( \rho \mathbf { v } \right) = \rho \frac { \partial \mathbf { v } } { \partial t } + \mathbf { v } \frac { \partial \rho } { \partial t } .\tag{14.2}
$$

Switching to “sum over repeated indices” notation (as in Ref. [36]), the continuity equation is

$$
\frac { \partial \rho } { \partial t } = - \frac { \partial } { \partial x _ { k } } \left( \rho v _ { k } \right)\tag{14.3}
$$

and the momentum equation is

$$
\rho \frac { \partial v _ { i } } { \partial t } = - \rho \left( v _ { k } \frac { \partial v _ { i } } { \partial x _ { k } } \right) - \frac { \partial p } { \partial x _ { i } } + \frac { \partial } { \partial x _ { k } } \sigma _ { i k } ^ { \prime } ,\tag{14.4}
$$

where $\sigma _ { i k } ^ { \prime }$ is the viscous stress tensor. Substituting Eqs. (14.3) and (14.4) into (14.2) and doing a little algebra to combine terms yields

$$
\frac { \partial } { \partial t } \left( \rho v _ { i } \right) = - \frac { \partial } { \partial x _ { k } } \left( \rho v _ { i } v _ { k } + p \delta _ { i k } - \sigma _ { i k } ^ { \prime } \right) .\tag{14.5}
$$

Now integrate over the whole volume of gas, and use Green’s formula to convert the volume integral of the divergence on the right side into a surface integral:

$$
\frac { \partial } { \partial t } \int \left( \rho v _ { i } \right) \ d V = - \int \left( \rho v _ { i } v _ { k } + p \delta _ { i k } - \sigma _ { i k } ^ { \prime } \right) \ d S _ { k } ,\tag{14.6}
$$

where dV is a diferential element of the volume and $d S _ { k }$ is a vector normal to an element of surface with area dS. The velocity is zero on the unmoving surface, so

$$
\frac { \partial } { \partial t } \int \left( \rho v _ { i } \right) \ d V = - \int \left( p \delta _ { i k } - \sigma _ { i k } ^ { \prime } \right) \ d S _ { k } .\tag{14.7}
$$

The right side is the total force exerted on the gas by the solid vessel bounding the gas. It is the sum of the pressure forces and the viscous forces. The x component of the left side is Eq. (14.1), which is what DeltaEC’s F1 operator calculates.

## 14.2 Second-order time-averaged pressure

Koulakis et al. [88, 89] derived an Euler-like equation for the second-order, time-averaged velocity in a fluid as a function of the second-order, time-averaged pressure and the acoustic pressure and velocity. We adapt their Eq. (15) to our needs by using DeltaEC notation, assuming steady state, taking a simple areal integral perpendicular to x across the thermoacoustic channel, and adding an empirical term for viscous and turbulent drag at the channel walls. We neglect the diference between $\left| U _ { 1 } \right| ^ { 2 } / A$ and $\int u _ { 1 } ^ { 2 } d A$ . These steps are not strictly justifiable when $u _ { 1 }$ depends on lateral position in a channel, as it must when viscous and turbulent drag are involved, but we hope the result is reasonably close to reality. This yields

$$
0 = - \frac { d p _ { 2 , 0 , \mathrm { t o t } } } { d x } + \frac { 1 } { 4 \rho _ { m } a ^ { 2 } } \frac { d \left. p _ { 1 } \right. ^ { 2 } } { d x } - \frac { \rho _ { m } } { 4 } \frac { d \left. U _ { 1 } / A \right. ^ { 2 } } { d x } - \frac { d \rho _ { m } } { d x } \frac { \left. U _ { 1 } / A \right. ^ { 2 } } { 2 } - r U _ { 2 , 0 } ,\tag{14.8}
$$

where r is the flow resistance of the duct per unit length. All of the variables in Eq. (14.8) might be functions of x. The Eulerian second-order, time-averaged pressure $p _ { \mathrm { 2 , 0 , t o t } }$ is what

is measured by a side-wall pressure transducer [35, 42], so it is available to the user in DeltaEC’s RPN segments.

Within DeltaEC, we choose to express $p _ { \mathrm { 2 , 0 , t o t } }$ as the sum of two terms,

$$
p _ { 2 , 0 , \mathrm { t o t } } = p _ { 2 , 0 , \mathrm { t r a d } } + p _ { 2 , 0 , \mathrm { D E C } } \ ,\tag{14.9}
$$

where

$$
p _ { 2 , \mathrm { 0 , t r a d } } = { \frac { \left| p _ { 1 } \right| ^ { 2 } } { 4 \rho _ { m } a ^ { 2 } } } - { \frac { \rho _ { m } \left| U _ { 1 } / A \right| ^ { 2 } } { 4 } }\tag{14.10}
$$

is the traditional expression for acoustic “radiation pressure” given in publications [36, 90, 35] with no concern for gradients in mean temperature, mean density, or sound speed and no concern about turbulence or viscosity, and $p _ { \mathrm { 2 , 0 , D E C } }$ comprises some other terms that we believe are important in some thermoacoustic systems. Substituting Eqs. (14.9) and (14.10) into Eq. (14.8) and separating the traditional and “other” parts quickly yields

$$
\frac { d p _ { 2 , \mathrm { 0 , t r a d } } } { d x } = \frac { d } { d x } \left( \frac { | p _ { 1 } | ^ { 2 } } { 4 \rho _ { m } a ^ { 2 } } - \frac { \rho _ { m } | U _ { 1 } / A | ^ { 2 } } { 4 } \right) ,\tag{14.11}
$$

$$
\frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } = - \frac { \left| p _ { 1 } \right| ^ { 2 } } { 4 } \frac { d } { d x } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) - \frac { \left| U _ { 1 } / A \right| ^ { 2 } } { 4 } \frac { d \rho _ { m } } { d x } - r U _ { 2 , 0 } .\tag{14.12}
$$

DeltaEC’s steady-flow calculations are usually focused on streaming around toroidal paths. Since the right-hand side of Eq. (14.11) is a perfect diferential, its integral around any toroidal path through a series of segments is zero, so $p _ { \mathrm { 2 , 0 , t r a d } }$ cannot contribute anything to DeltaEC’s streaming calculation. Therefore, DeltaEC’s built-in results use and display only $p _ { \mathrm { 2 , 0 , D E C } }$ . (Conveniently, $p _ { \mathrm { 2 , 0 , t r a d } }$ depends only on variables that are already known everywhere in a DeltaEC model, so no new numerical integration variable is needed to obtain it wherever the user wants to see $p _ { \mathrm { 2 , 0 , t o t } }$ in an RPN segment.)

Note that our statement about $p _ { \mathrm { 2 , 0 , t r a d } }$ being unable to contribute to streaming is not true when a minor loss is involved, whether the minor loss occurs in a series of components (e.g., Refs. [42, 8])or at a tee (e.g., Ref. [43]).

The three terms appearing in $p _ { \mathrm { 2 , 0 , D E C } }$ are interesting. The first two terms on the righthand side of Eq. (14.12) are the acoustic force density given by Eq. (13) in Karlsen et al. [91], which arises from gradients in the mean properties of the fluid. The $d \rho _ { m } / d x$ term was called the pycnoclinic acoustic force by Koulakis et al., who were not aware of the earlier work of Karlsen et al. Analogously, we call the $d ( \rho _ { m } a ^ { 2 } )$ /dx term the elastoclinic acoustic force, which vanishes for pure and well-mixed ideal gases, for which $\rho _ { m } a ^ { 2 } = \gamma p _ { m }$ is independent of temperature. (Note, however, that the elastoclinic force is nonzero in an ideal-gas mixture if $d n _ { L } / d x \ne 0$ and $\gamma _ { L } \neq \gamma _ { H } . )$ In DeltaEC, these two terms can contribute in STK\*\*, VX\*\*, and MIX\*\* segments. The third term arises from viscosity and turbulence in most DeltaEC segments, and the complicated expressions for r for each segment type can be found in the detailed description of that segment type elsewhere in the Users Guide. [The third term was called $d p _ { 2 , 0 , H L } / d x$ (HL for “Head $\mathrm { L o s s } ^ { \prime \prime } )$ in DeltaEC’s version 6.4b2.7 and earlier. DeltaEC includes the pycnoclinic and elastoclinic forces beginning with version 6.4b2.8.] Numerical integration is needed to obtain $p _ { \mathrm { 2 , 0 , D E C } }$ throughout a model, as illustrated with Eqs. (6.5) or (8.6).

In our (admittedly limited) experience thus far, the pycnoclinic and elastoclinic terms are important only in STKDUCT and STKCONE segments used to model pulse tubes and thermal bufer tubes in looped models, and in large-channel VX\*\* segments with rather small $\dot { N }$ in looped models, because these are the situations where these terms are large compared with ${ r U } _ { 2 , 0 }$ . We have also included these two terms in STKCIRC, STKSLAB, STKRECT, STKPINS, and MIX\*\*, because these segments are sometimes used in boundary-layer approximation. However, when pores are small in such segments, please realize that Refs. [88] and [91] do not consider viscous boundary layers at all, so the validity of Eq. (14.12) is dubious. We do not include these two terms in STKSCREEN and STKPOWERLW because we believe these segments are only suitable for tortured flow where viscous efects are even more dominant.

The pycnoclinic coeficient is calculated in DeltaEC via

$$
\frac { d \rho _ { m } } { d x } = \frac { \partial \rho _ { m } } { \partial T _ { m } } \frac { d T _ { m } } { d x } + \frac { \partial \rho _ { m } } { \partial n _ { L } } \frac { d n _ { L } } { d x }\tag{14.13}
$$

$$
\mathrm { ~  ~ \Gamma ~ } = \mathrm { ~  ~ \Gamma ~ } - \rho _ { m } \beta \frac { d T _ { m } } { d x } + \frac { \partial \rho _ { m } } { \partial n _ { L } } \frac { d n _ { L } } { d x } .\tag{14.14}
$$

The only mixtures allowing $d n _ { L } / d x \ne 0$ in DeltaEC are ideal gases, for which

$$
\frac { \partial \rho _ { m } } { \partial n _ { L } } = - \rho _ { m } \frac { m _ { H } - m _ { L } } { m } .\tag{14.15}
$$

Similarly, the elastoclinic coeficient is calculated in DeltaEC via

$$
\frac { d } { d x } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) = \frac { \partial } { \partial T _ { m } } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) \frac { d T _ { m } } { d x } + \frac { \partial } { \partial n _ { L } } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) \frac { d n _ { L } } { d x } .\tag{14.16}
$$

For ideal gases, the first term is zero and the second term is only nonzero in a mixture whose components have diferent $\gamma \mathrm { { s } }$ , because then

$$
\frac { \partial } { \partial n _ { L } } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) \equiv \frac { \partial } { \partial n _ { L } } \left( \frac { 1 } { \gamma p _ { m } } \right) = - \frac { \left( \gamma - 1 \right) ^ { 2 } } { \gamma ^ { 2 } p _ { m } } \left( \frac { 1 } { \gamma _ { H } - 1 } - \frac { 1 } { \gamma _ { L } - 1 } \right) ,\tag{14.17}
$$

with the final step relying on the diferentiation of Eq. (12.5). For fluids other than ideal gases, the first term of Eq. (14.16) is obtained via

$$
\frac { \partial } { \partial T _ { m } } \left( \frac { 1 } { \rho _ { m } a ^ { 2 } } \right) = - \frac { 1 } { \rho _ { m } a ^ { 2 } } \left( \frac { 2 } { a } \frac { \partial a } { \partial T _ { m } } - \beta \right) ;\tag{14.18}
$$

mixtures of fluids other than ideal gases only exist for fixed $n _ { L } \ \mathrm { ( e . g . , a i r ) }$ in DeltaEC, so the second term is irrelevant.

## 14.3 Tortuous geometry $\left. T _ { 1 } \right.$ and dT<sub>m</sub>/dx

The state variables in STKSCREEN and STKPOWERLW are complex $p _ { 1 }$ , complex $\left. u _ { 1 } \right.$ , and real $T _ { m }$ . The Runge-Kutta integrator requires explicit expressions for $d / d x$ of those. (SX and PX are similar, but simpler because $d T _ { m } / d x = 0 . )$ DeltaEC’s calculations in these segments are based on Ref. [55], and are challenging because they require an iterative calculation of $\left. T _ { 1 } \right.$

 Reference [55]’s Eq. (D1) gives $d p _ { 1 } / d x$ in terms of $\left. u _ { 1 } \right.$ . That’s simple.

 Reference [55]’s Eq. (D3) gives $d T _ { m } / d x$ in terms of $p _ { 1 } , \ \langle u _ { 1 } \rangle$ , and $\left. T _ { 1 } \right.$ . The variable $\left. T _ { 1 } \right.$ appears in the factor $e ^ { 2 i \theta _ { T } }$ , which appears twice.

 Reference [55]’s Eq. (29) gives $\left. T _ { 1 } \right.$ in terms of $p _ { 1 } , \langle u _ { 1 } \rangle , d T _ { m } / d x$ , and $\left. T _ { 1 } \right.$ itself through the factor $e ^ { 2 i \bar { \theta } _ { T } }$ again.

 Reference [55]’s Eq. (D2) can be rewritten

$$
\frac { d \langle u _ { 1 } \rangle } { d x } = - \frac { i \omega \gamma } { \rho _ { m } a ^ { 2 } } p _ { 1 } + \beta \frac { d T _ { m } } { d x } \langle u _ { 1 } \rangle + i \omega \beta \langle T _ { 1 } \rangle ,\tag{14.19}
$$

which is straightforward to calculate after $d T _ { m } / d x$ and $\left. T _ { 1 } \right.$ have already been found self-consistently.

Thus, the self-consistent calculation of $\left. T _ { 1 } \right.$ and $d T _ { m } / d x$ at each x is the unusual challenge of STKSCREEN and STKPOWERLW. Even for SX and PX, for which $d T _ { m } / d x = 0$ , the calculation of $\left. T _ { 1 } \right.$ isn’t straightforward.

When first implemented, DeltaEC simply used successive substitution with a finite number of steps: ten. That seemed good enough at the time, but it started giving one user trouble for an exotic solid in STKPOWERLW at cryogenic temperatures. We improved the algorithm with a better initial guess to get the successive substitution started, plus more steps, with a gradually adjusted blend of the previous iteration if needed to avoid oscillating behavior. However, a few odd cases remained problematic. So, here’s a derivation of the self-consistent calculation that DeltaEC is using in version $7 { : }$

Reference [55]’s Eqs. (29) and (D3) can be written:

$$
\langle T _ { 1 } \rangle ~ = ~ { \frac { J } { D } } - { \frac { B } { D } } { \frac { d T _ { m } } { d x } } ,\tag{14.20}
$$

$$
\frac { d T _ { m } } { d x } = \frac { \mathrm { R e } [ J \langle \widetilde { u _ { 1 } } \rangle / D + E ] } { \mathrm { R e } [ B \langle \widetilde { u _ { 1 } } \rangle / D ] + F } ,\tag{14.21}
$$

where

$$
J ~ = ~ \frac { T _ { m } \beta } { \rho _ { m } c _ { p } } \left[ \epsilon _ { s } + ( g _ { c } + e ^ { 2 i \theta _ { p } } g _ { v } ) \epsilon _ { h } \right] p _ { 1 } ,\tag{14.22}
$$

$$
B = \frac { 1 } { i \omega } \left[ \epsilon _ { s } + ( g _ { c } - g _ { v } ) \epsilon _ { h } \right] \langle u _ { 1 } \rangle ,\tag{14.23}
$$

$$
\begin{array} { c c l } { { { \cal D } } } & { { = } } & { { 1 + \epsilon _ { s } + \left( g _ { c } + e ^ { 2 i \theta _ { T } } g _ { v } \right) \epsilon _ { h } , } } \end{array}\tag{14.24}
$$

$$
\begin{array} { r c l } { E } & { = } & { \left[ ( 1 - T _ { m } \beta ) p _ { 1 } \langle \widetilde { u _ { 1 } } \rangle - 2 \dot { H } _ { 2 } / \phi A \right] / \rho _ { m } c _ { p } , } \end{array}\tag{14.25}
$$

$$
F = \frac { 2 } { \rho _ { m } c _ { p } } \left( k + k _ { s , \mathrm { e f f } } \frac { 1 - \phi } { \phi } \right) .\tag{14.26}
$$

For SX and PX, Eq. (14.21) would instead be simply $d T _ { m } / d x = 0$

In the equations above, we follow the notation of Ref. [55]. Note that

$$
\begin{array} { r c l } { { \theta _ { p } } } & { { = } } & { { \theta _ { u 1 } - \theta _ { p 1 } , } } \end{array}\tag{14.27}
$$

$$
\begin{array} { r c l } { { \theta _ { T } } } & { { = } } & { { \theta _ { u 1 } - \theta _ { T 1 } , } } \end{array}\tag{14.28}
$$

where for example $\theta _ { T 1 }$ is given by

$$
\langle T _ { 1 } \rangle = | \langle T _ { 1 } \rangle | e ^ { i \theta _ { T 1 } } ,\tag{14.29}
$$

and $\theta _ { p 1 }$ and $\theta _ { u 1 }$ follow the same pattern.

Combine Eqs. (14.20) and (14.21) to eliminate $d T _ { m } / d x$ , obtaining

$$
\begin{array} { r c l } { \langle T _ { 1 } \rangle } & { = } & { \displaystyle \frac { J } { D } - \frac { B } { D } \frac { \mathrm { R e } \left[ J \langle \widetilde { u _ { 1 } } \rangle / D + E \right] } { \mathrm { R e } \left[ B \langle \widetilde { u _ { 1 } } \rangle / D \right] + F } \mathrm { f o r ~ \mathrm { S T K S C R ~ a n d ~ \mathrm { S T K P O } , } } } \\ & { = } & { \displaystyle \frac { J } { D } \mathrm { f o r ~ \mathrm { S X ~ a n d ~ \mathrm { P X } . } } } \end{array}\tag{14.30}
$$

(14.31)

The right-hand sides of Eqs. (14.30) and (14.31) depend on $\theta _ { T 1 }$ through $D ,$ and the left-hand side depends on it directly as shown in Eq. (14.29). In principle, we can solve Eq. (14.30) or (14.31) for $\theta _ { T 1 }$

We have not found an analytical solution, even for SX and PX. The simplest numerical approach we’ve found begins with defining

$$
\begin{array} { r c l } { g ( \theta _ { T 1 } ) } & { = } & { \left( \frac { J } { D } - \frac { B } { D } \frac { \mathrm { R e } \left[ J \langle \widetilde { u _ { 1 } } \rangle / D + E \right] } { \mathrm { R e } \left[ B \langle \widetilde { u _ { 1 } } \rangle / D \right] + F } \right) e ^ { - i \theta _ { T 1 } } \mathrm { ~ f o r ~ } \mathrm { S T K S C R ~ a n d ~ } \mathrm { S T K P O } , } \\ & { = } & { \displaystyle \frac { J } { D } e ^ { - i \theta _ { T 1 } } \mathrm { ~ f o r ~ } \mathrm { S X ~ a n d ~ } \mathrm { P X } . } \end{array}\tag{14.32}
$$

(14.33)

We seek $\theta _ { T 1 }$ such that Im $. [ g ( \theta _ { T 1 } ) ] = 0$ while $\mathrm { R e } [ g ( \theta _ { T 1 } ) ] > 0$ . With that $\theta _ { T 1 }$ , Eqs. (14.20) and (14.21) then yield $d T _ { m } / d x$ and $\left. T _ { 1 } \right.$

DeltaEC finds the solution by evaluating g at up to 64 values of $\theta _ { T 1 }$ , equally spaced around $2 \pi$ radians, beginning at our best a priori estimated value, looking for any interval with a zero crossing in Im[g] while $\mathrm { R e } [ g ] > 0$ . After the zero-crossing interval is identified, DeltaEC homes in on the value of $\theta _ { T 1 }$ to double-precision accuracy using the bisection method.

That method occasionally fails, e.g., if no zero crossing is found with such a coarse search, or if $\operatorname { I m } [ g ( \theta _ { T 1 } ) ]$ changes sign at a singularity. If it fails, DeltaEC evaluates $g$ at 2048 equally spaced values of $\theta _ { T 1 }$ from 0 to $2 \pi$ , again ignoring $\mathrm { R e } [ g ( \theta _ { T 1 } ) ] < 0$ and choosing the zero-crossing interval with the smallest $\Delta \mathrm { I m } [ g ]$ , again using bisection to home in on the final result.

## 14.4 Third-order $p _ { 1 }$ dependence in $d p _ { 2 , 0 , \mathbf { D E C } } / d x$

Derivations of $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ in publications of the Los Alamos thermoacoustics team through 2006, such as Refs. [42, 13], neglected the pycnoclinic and elastoclinic terms and kept terms only through second order in $u _ { 1 }$ in the $r U _ { 2 , 0 }$ term. In 2006, Scott Backhaus found one example (a stacked-screen regenerator with a small $u _ { 2 , 0 } )$ in which a third-order term, proportional to $\left| \rho _ { 1 } \right| \left| u _ { 1 } \right| ^ { 2 }$ , contributed significantly to $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ . This led us to include that term in DeltaEC’s STKSCREEN calculations, and for consistency we have included similar third-order contributions in other segments, including MINOR, DUCT, and CONE. This section outlines the derivations of these expressions for $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ , which include these small terms proportional to $p _ { 1 }$ . Scott Backhaus’s contributions to these derivations are gratefully acknowledged.

## MINOR

The time-averaged pressure drop across a minor-loss component is, by definition, given by

$$
\overline { { \Delta p } } = - \frac { 1 } { 2 } \overline { { K \rho } } u | u | ,\tag{14.34}
$$

where $u$ is the spatially averaged velocity, $\rho$ is the density, K is the minor-loss coeficient, and all three of these variables can be time dependent. In previous derivations, such as in Ref. [13], we have taken $\rho$ to be independent of time, because we were satisfied with results to second order. Here we retain the fundamental component of $\rho \mathrm { ^ { \circ } s }$ time dependence.

Write Eq. (14.34) as

$$
\begin{array} { r c l } { \overline { { \Delta p _ { \mathrm { m i n o r } } } } } & { = } & { \displaystyle - \frac { 1 } { 2 } \overline { { K ( t ) \left[ \rho _ { m } + \left| \rho _ { 1 } \right| \cos \left( \omega t + \phi \right) \right] \left( \left| u _ { 1 } \right| \cos \omega t + u _ { 2 , 0 } \right) \left| \left| u _ { 1 } \right| \cos \omega t + u _ { 2 , 0 } \right| } } ( 1 4 . 3 5 ) } \\ & { = } & { \displaystyle - \frac { 1 } { 4 \pi } \int _ { 0 } K ( t ) \left[ \rho _ { m } + \left| \rho _ { 1 } \right| \cos \left( \omega t + \phi \right) \right] \left( \left| u _ { 1 } \right| \cos \omega t + u _ { 2 , 0 } \right) \left| \left| u _ { 1 } \right| \cos \omega t + u _ { 2 , 0 } \right| d ( \omega t ) . } \end{array}\tag{14.36}
$$

In the interval $0 ~ < ~ \omega t ~ < ~ 2 \pi$ , the argument of the absolute value changes sign at $\omega t = \mathrm { \ A r c c o s } ( - u _ { 2 , 0 } / \left| u _ { 1 } \right| ) \equiv \tau _ { 0 }$ and $\omega t = 2 \pi - \mathrm { ~ A ~ }$ rccos $( - u _ { 2 , 0 } / \left| u _ { 1 } \right| ) = 2 \pi - \tau _ { 0 } \mathrm { i f } \left| u _ { 2 , 0 } / u _ { 1 } \right| < 1$ at these zero crossings, the value of K changes from $K _ { + }$ to $K _ { - }$ and back again. Thus

$$
\overline { { \Delta p _ { \mathrm { m i n o r } } } } = - \frac { 1 } { 4 \pi } \left( { K _ { + } \int _ { - \pi _ { 0 } } ^ { \pi _ { 0 } } { - K _ { - } \int _ { \tau _ { 0 } } ^ { 2 \pi _ { - } } } } \right) \left[ \rho _ { m } + | \rho _ { 1 } | \cos \left( \omega t + \phi \right) \right] \left( | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } \right) ^ { 2 } d ( \omega t )\tag{14.37}
$$

if $u _ { 2 , 0 } / \left| u _ { 1 } \right| < 1$ . Evaluating this (e.g., with the symbolic-mathematics software Mathematica) yields

$$
\begin{array} { r c l } { { \overline { { { \Delta p _ { \mathrm { m i n o r } } } } } } } & { { = } } & { { \displaystyle \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { 4 \pi } \left\{ \left( K _ { - } - K _ { + } \right) \frac { \pi } { 2 } \left( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos \phi \right) \right. } } \\ { { } } & { { } } & { { - \left. \left( K _ { + } + K _ { - } \right) \left[ \left( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos \phi \right) \sin ^ { - 1 } \varepsilon _ { 2 , 0 } \right. } } \\ { { } } & { { } } & { { \left. + \left( 3 \varepsilon _ { 2 , 0 } + \displaystyle \frac { 4 } { 3 } \left[ 1 + \varepsilon _ { 2 , 0 } ^ { 2 } / 2 \right] \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos \phi \right) \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } \right] \right\} } } \end{array}\tag{14.38}
$$

if $| \varepsilon _ { 2 , 0 } | \leq 1$ , where $\varepsilon _ { 2 , 0 } = u _ { 2 , 0 } / \left| u _ { 1 } \right|$

If $\left| \varepsilon _ { 2 , 0 } \right| \geq 1$ , the integral is less complicated because the argument of the absolute value never crosses zero; the results are

$$
\begin{array} { r l r } { \overline { { \Delta p _ { \mathrm { m i n o r } } } } } & { = } & { - \displaystyle \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { 4 } K _ { + } \left( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos \phi \right) \mathrm { ~ f o r ~ } \varepsilon _ { 2 , 0 } \ge 1 , } \\ & { = } & { \displaystyle \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { 4 } K _ { - } \left( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos \phi \right) \mathrm { ~ f o r ~ } \varepsilon _ { 2 , 0 } \le - 1 . } \end{array}\tag{14.39}
$$

(14.40)

We take the density oscillations to be adiabatic, so $\rho _ { 1 } / \rho _ { m } = p _ { 1 } / \gamma p _ { m }$ . These results appear in Section 10.2.4.

## STKSCREEN and SX

The momentum equation in a screen bed is [55, 13]

$$
\frac { d p } { d x } = - \frac { c _ { 1 } } { 8 r _ { h } ^ { 2 } } \mu u - \frac { c _ { 2 } } { 2 r _ { h } } \rho u \left| u \right| ,\tag{14.41}
$$

where $u$ is the spatially averaged velocity, $\rho$ is the density, $\mu$ is the viscosity, and $r _ { h }$ is the hydraulic radius. We take

$$
\begin{array} { r c l } { u } & { = } & { \left| u _ { 1 } \right| \cos \omega t + u _ { 2 , 0 } , } \end{array}\tag{14.42}
$$

$$
\rho ~ = ~ \rho _ { m } + | \rho _ { 1 } | \cos ( \omega t + \phi ) .\tag{14.43}
$$

We might also write $\mu = \mu _ { m } + \left| \mu _ { 1 } \right| \cos ( \omega t + \theta )$ , but the oscillations in a regenerator are nearly isothermal and viscosity is independent of pressure, so we neglect $\mu _ { 1 }$ in the first term in Eq. (14.41).

The time average of the left-hand side, to second order, is $d p _ { 2 , \mathrm { 0 , D E C } } / d x$

The time average of the first term on the right-hand side, to second order, is

$$
- \frac { c _ { 1 } } { 8 r _ { h } ^ { 2 } } \mu _ { m } u _ { 2 , 0 } .\tag{14.44}
$$

Taking the time average of the second term involves the integral

$$
\begin{array} { r c l } { { I _ { \mathrm { s c r e e n } } } } & { { = } } & { { \displaystyle [ \rho _ { m } + | \rho _ { 1 } | \cos ( \omega t + \phi ) ] ( | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } ) | | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } | } } \\ { { } } & { { } } & { { \displaystyle ( 1 4 \cos \omega t + | \rho _ { 1 } | \cos ( \omega t + \phi ) ] ( | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } ) | | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } | \ d ( \omega t ) . } } \\ { { } } & { { } } & { { \displaystyle  \frac { 1 } { 2 \pi } \int _ { 0 } ^ { } [ \rho _ { m } + | \rho _ { 1 } | \cos ( \omega t + \phi ) ] ( | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } ) | | u _ { 1 } | \cos \omega t + u _ { 2 , 0 } | \ d ( \omega t ) . } } \end{array}\tag{.45}
$$

(14.46)

In the interval $0 < \omega t < 2 \pi$ , the argument of the absolute value near the end of the equation changes sign at $\omega t = \mathrm { \ A r c c o s } ( - u _ { 2 , 0 } / \left| u _ { 1 } \right| ) \equiv \tau _ { 0 }$ and $\omega t = 2 \pi - \operatorname { A r c c o s } ( - u _ { 2 , 0 } / \left| u _ { 1 } \right| ) = 2 \pi - \tau _ { 0 }$ if $| u _ { 2 , 0 } / u _ { 1 } | < 1$ , so we can write

$$
I _ { \mathrm { s c r e e n } } = { \frac { 1 } { 2 \pi } } \left( \int _ { - \pi _ { 0 } } ^ { \tau _ { 0 } } - \int _ { \tau _ { 0 } } ^ { 2 \pi - \tau _ { 0 } } \right) \left[ \rho _ { m } + \left| \rho _ { 1 } \right| \cos \left( \omega t + \phi \right) \right] \left( \left| u _ { 1 } \right| \cos \omega t + u _ { 2 , 0 } \right) ^ { 2 } d ( \omega t ) .\tag{14.47}
$$

Evaluating this with the symbolic-mathematics software Mathematica yields

$$
\begin{array} { r l r } { { \cal I } _ { \mathrm { s c r e e n } } } & { = } & { \displaystyle \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { \pi } \left\{ \left[ \left( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } \right) \sin ^ { - 1 } \varepsilon _ { 2 , 0 } + 3 \varepsilon _ { 2 , 0 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } \right] \right. } \\ & { } & { \left. + 2 \displaystyle \frac { | \rho _ { 1 } | } { \rho _ { m } } \cos \phi \left[ \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } + \frac { 2 + \varepsilon _ { 2 , 0 } ^ { 2 } } { 3 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } \right] \right\} . } \end{array}\tag{14.48}
$$

where $\varepsilon _ { 2 , 0 } = u _ { 2 , 0 } / \left| u _ { 1 } \right|$

Combining all of these intermediate results and taking $\rho _ { 1 } / \rho _ { m } = p _ { 1 } / p _ { m }$ for approximately isothermal oscillations yields

$$
\begin{array} { r l r } { \frac { d p _ { 2 , \mathrm { 0 , D E C } } } { d x } } & { = } & { - \frac { c _ { 1 } } { 8 r _ { h } ^ { 2 } } \mu _ { m } u _ { 2 , 0 } - \frac { c _ { 2 } } { 2 \pi r _ { h } } \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } \bigg \{ \bigg ( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { \left| p _ { 1 } \right| } { p _ { m } } \cos \phi \bigg ) \sin ^ { - 1 } \varepsilon _ { 2 , 0 } } \\ & { } & { + \left[ 3 \varepsilon _ { 2 , 0 } + \frac { 2 } { 3 } \left( 2 + \varepsilon _ { 2 , 0 } ^ { 2 } \right) \frac { \left| p _ { 1 } \right| } { p _ { m } } \cos \phi \right] \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } \bigg \} \eqno \left( 1 . 7 \right) } \end{array}\tag{4.49}
$$

for $| \varepsilon _ { 2 , 0 } | \leq 1$

In SX, $\left| \varepsilon _ { 2 , 0 } \right| \geq 1$ may sometimes be of interest. In that case,

$$
\frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } = - \frac { c _ { 1 } } { 8 r _ { h } ^ { 2 } } \mu _ { m } u _ { 2 , 0 } - \frac { c _ { 2 } } { 4 r _ { h } } \rho _ { m } | u _ { 1 } | ^ { 2 }  \mathrm { s i g n } ( \varepsilon _ { 2 , 0 } ) ( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } + 2 \varepsilon _ { 2 , 0 } \frac { | p _ { 1 } | } { p _ { m } } \cos \phi ) .\tag{14.50}
$$

These results appear in Sections 10.5.2 and 10.7.2.

DUCT and CONE

We follow the outline in the appendix of Ref. [42], but we change the time dependence from sine to cosine, to be consistent with other results in this section, and we keep some dependence on $\rho _ { 1 }$ by writing Eq. (A6) in Ref. [42] as

$$
\frac { d p } { d x } = - f _ { M } ( t ) \frac { \rho _ { m } + | \rho _ { 1 } | \cos ( \omega t + \phi ) } { 2 D } u ( t ) | u ( t ) | ,\tag{14.51}
$$

where $u = U / S$ in Ref. [42]. Using Eq. (A4) in Ref. [42] for $f _ { M }$ yields

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } } & { = } & { \displaystyle - \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { 2 D } \frac { 1 } { 2 \pi } \left( \int _ { - \eta _ { 0 } } ^ { \eta _ { 0 } } - \int _ { \eta _ { 0 } } ^ { 2 \pi - \tau _ { 0 } } \right) \left[ f _ { M , \mathrm { m a x } } + \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } \left( \frac { \left| \cos \omega t + \varepsilon _ { 2 , 0 } \right| } { 1 + \left| \varepsilon _ { 2 , 0 } \right| } - 1 \right) \right] } \\ & & { \displaystyle \times \left[ 1 + \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos { \left( \omega t + \phi \right) } \right] \left( \cos \omega t + \varepsilon _ { 2 , 0 } \right) ^ { 2 } d ( \omega t ) , } & { \left( 1 4 . 5 \pi \alpha ^ { \prime } \right) ^ { 2 } , } \end{array}
$$

where $\varepsilon _ { 2 , 0 } = u _ { 2 , 0 } / \left| u _ { 1 } \right|$ and $\tau _ { 0 } = \operatorname { A r c c o s } ( - u _ { 2 , 0 } / \left| u _ { 1 } \right| )$ as for the STKSCREEN derivation above. We neglect $\left| u _ { 1 } \right| ^ { 2 } N _ { R , \operatorname* { m a x } } \left| \rho _ { 1 } \right|$ because it is fourth order. Then

$$
\begin{array} { r l r } { \displaystyle \frac { d p _ { 2 , \mathrm { 0 , D E C } } } { d x } } & { = } & { - \displaystyle \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { 2 D } \frac { f _ { M , \mathrm { m a x } } } { 2 \pi } \left( \int _ { - \tau _ { 0 } } ^ { \tau _ { 0 } } - \int _ { \tau _ { 0 } } ^ { \tau _ { n } - \tau _ { 0 } } \right) \left[ 1 + \frac { \left| \rho _ { 1 } \right| } { \rho _ { m } } \cos \left( \omega t + \phi \right) \right] \left( \cos \omega t + \varepsilon _ { 2 , 0 } \right) ^ { 2 } d ( \omega t ) } \\ & { } & { - \displaystyle \frac { \rho _ { m } \left| u _ { 1 } \right| ^ { 2 } } { 2 D } \frac { d f _ { M } } { d N _ { R } } \frac { N _ { R , \mathrm { m a x } } } { 2 \pi } \left( \int _ { - \tau _ { 0 } } ^ { \tau _ { 0 } } - \int _ { \tau _ { 0 } } ^ { 2 \pi - \tau _ { 0 } } \right) \left( \frac { \left| \cos \omega t + \varepsilon _ { 2 , 0 } \right| } { 1 + \left| \varepsilon _ { 2 , 0 } \right| } - 1 \right) \left( \cos \omega t + \varepsilon _ { 2 , 0 } \right) ^ { 2 } d ( \omega t ) } \end{array}\tag{14.53}
$$

The integral in the first line was evaluated above, in Eqs. (14.47)–(14.48). The integral in the second line was evaluated to obtain the bottom line in Eq. (A10) in Ref. [42]. Pulling all the pieces together, and using $\rho _ { 1 } / \rho _ { m } = p _ { 1 } / \gamma p _ { m }$ for adiabatic oscillations, yields

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } } & { = } & { \displaystyle - \frac { \rho _ { m } | u _ { 1 } | ^ { 2 } } { 2 \pi D } \{ [ ( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } ) \sin ^ { - 1 } \varepsilon _ { 2 , 0 } + 3 \varepsilon _ { 2 , 0 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } \ f _ { M , \mathrm { m a x } }   } \\ & & { \displaystyle  + \frac { 2 | p _ { 1 } | } { \gamma p _ { m } } \cos \phi ( \varepsilon _ { 2 , 0 } \sin ^ { - 1 } \varepsilon _ { 2 , 0 } + \frac { 2 + \varepsilon _ { 2 , 0 } ^ { 2 } } { 3 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } ) ]  } \\ & & { \displaystyle + [ \pi \varepsilon _ { 2 , 0 } \frac { 3 / 2 + \varepsilon _ { 2 , 0 } ^ { 2 } } { 1 + | \varepsilon _ { 2 , 0 } | } - 3 \varepsilon _ { 2 , 0 } \sqrt { 1 - \varepsilon _ { 2 , 0 } ^ { 2 } } - ( 1 + 2 \varepsilon _ { 2 , 0 } ^ { 2 } ) \sin ^ { - 1 } \varepsilon _ { 2 , 0 } ] \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } \} , } \end{array}
$$

$$
\begin{array} { r c l } { \displaystyle \frac { d p _ { 2 , 0 , \mathrm { D E C } } } { d x } } & { = } & { \displaystyle - \ \mathrm { s i g n } ( u _ { 2 , 0 } ) \frac { \rho _ { m } u _ { 2 , 0 } ^ { 2 } } { 2 D } \left[ \left( 1 + \frac { 1 } { 2 \varepsilon _ { 2 , 0 } ^ { 2 } } + \frac { | p _ { 1 } | } { \gamma p _ { m } } \frac { \cos \phi } { \varepsilon _ { 2 , 0 } } \right) f _ { M , \mathrm { m a x } } \right. } \\ & & { \displaystyle \left. - \frac { 2 \varepsilon _ { 2 , 0 } ^ { 2 } - 2 | \varepsilon _ { 2 , 0 } | + 1 } { 2 \varepsilon _ { 2 , 0 } ^ { 2 } ( 1 + | \varepsilon _ { 2 , 0 } | ) } \frac { d f _ { M } } { d N _ { R } } N _ { R , \mathrm { m a x } } \right] , } & { | \varepsilon _ { 2 , 0 } | \geq 1 . ( 1 4 . 5 5 ) } \end{array}
$$

These results appear in Section 10.1.1 for DUCT and 10.1.2 for CONE.

## STKPOWERLW and PX

The result for $d p _ { 2 , \mathrm { 0 , D E C } } / d x$ in STKPOWERLW and PX is the same as for DUCT and CONE above, except that we replace $\gamma p _ { m }$ with $p _ { m }$ to model isothermal oscillations and we include the pycnolinic and elastoclinic terms describe above.

## 14.5 Pole-tip flux, linear motor or alternator, \*\*SPEAKER

The pole-tip magnetic-flux phasor is the sum of the flux phasor due to current and the flux phasor due to motion:

$$
\Phi _ { p t , 1 } = \Phi _ { I , 1 } + \Phi _ { b E M F , 1 }\tag{14.56}
$$

where the subscript $^ { 6 6 } 1 ^ { \mathfrak { n } }$ indicates a complex phasor as usual. Obviously

$$
\Phi _ { I , 1 } = - L I _ { 1 } .\tag{14.57}
$$

We use $^ { 6 6 } - ^ { 9 9 }$ instead of $^ { 6 6 } + \ '$ here because we always write $\vert V \vert = \vert L d I / d t \vert$ and basic-physics books write $V = - d \Phi / d t$ and $\oint E \cdot d l = - L d I / d t$ with minus signs expressing Lenz’s law (induced EMF opposes changes in current). Similarly, we know that the unmeasurable internal voltage $V _ { b E M F , 1 } ~ = ~ - d \Phi _ { b E M F , 1 } / d t = - i \omega ~ \Phi _ { b E M F , 1 }$ , and in the linear operating regime we express this as $V _ { b E M F , 1 } = - ( B l ) v _ { 1 } = - ( B l ) U _ { 1 } / A$ in DeltaEC’s language of $^ { 6 6 } B l ^ { 9 }$ product and velocity. (Note DeltaEC’s electromechanical sign convention, described in Sections 10.3.1 and 10.4.2, difers from some others’ conventions, e.g., Ref. [12], via

$V _ { 1 }  - V _ { 1 } , I _ { 1 }  - I _ { 1 }$ , and $B l  - B l$ . Basically, this amounts to a rotation of all electrical and magnetic phasors by $1 8 0 ^ { \circ }$ relative to all mechanical and acoustic phasors.) Hence

$$
\Phi _ { b E M F , 1 } = - i ( B l ) U _ { 1 } / \omega A .\tag{14.58}
$$

Combining these three equations gives us

$$
\Phi _ { p t , 1 } = - L I _ { 1 } - i ( B l ) U _ { 1 } / \omega A .\tag{14.59}
$$

Using the law of cosines for triangles, we obtain the magnitude of the pole-tip flux

$$
\left| \Phi _ { p t , 1 } \right| = \sqrt { \left[ L \left| I _ { 1 } \right| \right] ^ { 2 } + \left[ \left( B l \right) \left| U _ { 1 } \right| / \omega A \right] ^ { 2 } - 2 \left[ L \left| I _ { 1 } \right| \right] \left[ \left( B l \right) \left| U _ { 1 } \right| / \omega A \right] \sin \alpha }\tag{14.60}
$$

where α is the phase angle by which $U _ { 1 }$ leads $I _ { 1 }$ . (Note: cos(α − 90<sup>◦</sup>) = sin α.)

(Thanks to John Corey for help with this section.)

Example

Here’s a DeltaEC fragment giving $| \Phi _ { p t , 1 } |$ as the result of RPN segment 17, while segment 16 displays $\left| \Phi _ { I , 1 } \right| = L \left| I _ { 1 } \right| \mathrm { a n d } \left| \Phi _ { b E M F , 1 } \right| = \left( B l \right) \left| U _ { 1 } \right| / \omega A .$

15   
IESPEAKER the driver 7.5 diam   
2.8500E-02 a Area m^2 9.7598E+04 A |p| Pa   
0.5200 b R ohms 154.96 B Ph(p) deg   
3.2200E-02 c L H 7.3587E-02 C |U| m^3/s   
84.700 d BLProd T-m -115.16 D Ph(U) deg   
15.000 e M kg 7.4617 E Hdot W   
7.3300E+04 f K N/m 7.4617 F Edot W   
105.00 g Rm N-s/m 6602.7 G WorkIn W   
59.466 h |I| A G 654.43 H Volts V   
93.911 i Ph(I) deg G 59.466 I Amps A   
70.164 J Ph(V/I)deg   
4.3376E+05 K |Px| Pa   
174.36 L Ph(Px) deg   
ideal Solid type -1273.9 M HeatIn W   
! - -- 16 --   
RPN A = IL flux [weber]; B = bEMF flux [weber]; C = alpha [degree]   
0.0000 a Target (t) 1.9148 A weber   
0.5801 B weber   
150.93 C deg   
15D 15i - 15d 15C \* 2 / pi / 0b / 15a / 15c 15h \*   
!--- -- 17 --   
RPN peak pole-tip flux. [weber = tesla.m^2]   
0.0000 a Target (t) 1.7099 A weber   
16A sqrd 16B sqrd + 2 16A \* 16B \* 16C sin \* - sqrt  
Dividing by pole-tip efective area would turn 17A into the magnetic field, in tesla.

## 14.6 Pulsed combustion

Suppose fuel is injected into an air stream in a duct, and combustion occurs. If the injection and combustion are steady, then conservation of matter applied to a small region around the combustion zone implies that

$$
\dot { N } _ { \mathrm { o u t } } = \dot { N } _ { \mathrm { i n } } + \Delta \dot { N } ,\tag{14.61}
$$

where $\dot { N } _ { \mathrm { i n } }$ and $\dot { N } _ { \mathrm { o u t } }$ are the molar flow rates of the incoming fresh air and the outgoing combustion products, respectively, and $\Delta \dot { N }$ is the additional molar flow rate due to the injection of the fuel and the change in mole numbers accompanying the combustion. Similarly,

$$
T _ { \mathrm { o u t } } = T _ { \mathrm { i n } } + \frac { \dot { Q } } { m c _ { p } \dot { N } _ { \mathrm { o u t } } } ,\tag{14.62}
$$

where $T _ { \mathrm { i n } }$ and $T _ { \mathrm { o u t } }$ are the temperatures of the incoming and outgoing streams, respectively, $\dot { Q }$ is the rate at which the combustion releases heat, and $m$ and $c _ { p }$ are the average molar mass and the heat capacity per unit mass of the outgoing stream.

In a thermoacoustic system, the combustion might be time dependent, because of the pressure dependence of the chemical reaction rate and/or a time dependence in the fuel injection. Suppose that the region of interest in the duct is small enough that the pressure is spatially uniform at every instant of time. Let the instantaneous heating rate be ${ \dot { q } } ( t )$ , so the average heating rate must be

$$
\dot { Q } = \frac { \omega } { 2 \pi } \intop _ { 0 } ^ { 2 \pi / \omega } \dot { q } ( t ) \ d t .\tag{14.63}
$$

Similarly, let the instantaneous rate of increase of moles in the region of interest, due to fuel injection and combustion, be ${ \dot { n } } ( t )$ , whose average must be

$$
\Delta \dot { N } = \frac { \omega } { 2 \pi } \intop _ { 0 } ^ { 2 \pi / \omega } \dot { n } ( t ) \ d t .\tag{14.64}
$$

Assuming ideal gases, the local rate of change of temperature due to ${ \dot { q } } ( t )$ is

$$
\dot { T } ( t ) = \frac { \dot { q } ( t ) } { V \rho _ { m } c _ { p } } = \frac { \gamma - 1 } { \gamma } \frac { \dot { q } ( t ) } { V p _ { m } / T _ { m } } ,\tag{14.65}
$$

where $V$ is the volume in which the combustion occurs, and the rate of change of that volume due to this heating is

$$
\begin{array} { r l r } { \dot { V } _ { q } ( t ) } & { = } & { V \dot { T } ( t ) / T _ { m } } \\ & { = } & { \frac { \gamma - 1 } { \gamma } \frac { \dot { q } ( t ) } { p _ { m } } . } \end{array}\tag{14.66}
$$

(14.67)

Similarly, $\dot { n } ( t )$ contributes a time-dependent volume change

$$
\dot { V } _ { n } ( t ) = m ~ \dot { n } ( t ) / \rho .\tag{14.68}
$$

The fundamental Fourier component of ${ \dot { V } } _ { q } + { \dot { V } } _ { n }$ contributes to the acoustic power $\dot { E }$ if the time phasing relative to $p _ { 1 }$ is favorable. In the DeltaEC paradigm, it causes a local increment in $U _ { 1 }$ which in turn causes a local increment in ${ \dot { E } } { \longrightarrow } \mathrm { o r }$ a decrement, depending on the time phasing. The real function $\dot { V } _ { q } ( t ) + \dot { V } _ { n } ( t )$ can be written as a Fourier series of sin’s and cos’s at ω, 2ω, 3ω, etc. and in the DeltaEC paradigm we are only interested in the $\omega$ components, which we can express in dimensionless form as $\Lambda _ { 1 }$

$$
\lambda ( t ) ~ = ~ { \frac { \dot { V } _ { q } ( t ) + \dot { V } _ { n } ( t ) } { ( \gamma - 1 ) \dot { Q } / \gamma p _ { m } } } ,\tag{14.69}
$$

$$
\Lambda _ { 1 } ~ = ~ \frac { 1 } { \pi } \int \lambda ( \omega t ) e ^ { i \omega t } ~ d ( \omega t ) .\tag{14.70}
$$

Depending on the circumstances, the phase of the complex variable Λ might be related to the local phase of either $p _ { 1 }$ or $U _ { 1 }$

Thus, the change in DeltaEC’s complex volumetric-flow-rate amplitude across the region of interest is

$$
\Delta U _ { 1 } = \frac { \gamma - 1 } { \gamma } \frac { \dot { Q } } { p _ { m } } \Lambda _ { 1 } ,\tag{14.71}
$$

and the local increment in acoustic power at the fundamental frequency is

$$
\Delta \dot { E } = \frac { \gamma - 1 } { \gamma } \frac { \dot { Q } } { p _ { m } } \frac { 1 } { 2 } \mathrm { R e } \left[ p _ { 1 } \widetilde { \Lambda _ { 1 } } \right] .\tag{14.72}
$$

For air, $( \gamma - 1 ) / \gamma = 2 / 7 .$ , and we might hope for $\left| p _ { 1 } \right| / p _ { m } \sim 0 . 2$ . If $| \Lambda _ { 1 } | \sim 1$ , then the eficiency of conversion of $\dot { Q }$ to acoustic power could be roughly 3%. This is small, but not negligible, compared with normal thermoacoustic-engine eficiencies.

(This derivation, new in the 6.3 Users Guide, might benefit from critical analysis by users! Feedback will be appreciated.)

To implement this in DeltaEC via RPN segments, the user will have to know $\dot { Q }$ and $\Delta \dot { N }$ , make an estimate of the time dependence for ${ \dot { q } } ( t )$ and $\dot { n } ( t )$ (including the time phase relative to $p _ { 1 }$ or $U _ { 1 } )$ , and do the math (or eyeball it graphically) to obtain a numerical value for $\Lambda _ { 1 }$ . Then put all those values into RPN segments, and use Eqs. (14.61), (14.62), and (14.71) above to impose local changes in DeltaEC’s integration variables $\dot { N } , T _ { m }$ , and $U _ { 1 }$ Here is one way to implement it:

```csv
BEGIN at a pressure node, where fresh air is easily injected.
1.0000E+05 a Mean P Pa
60.000 b Freq Hz
900.00 c TBeg K
0.0000 d |p| Pa
0.0000 e Ph(p) deg
2.0000 f |U| m^3/s
0.0000 g Ph(U) deg
2.0000E-02 i Ndot mol/s
air Gas type
!-- 1
DUCT pipe from pressure node to somewhere more interesting
3.0000E-02 a Area m^2 Mstr 1.5548E+04 A |p| Pa
0.6140 b Perim m 1a -90.098 B Ph(p) deg
2.5000 c Length m 2.0572E-02 C |U| m^3/s
5.0000E-04 d Srough 119.96 D Ph(U) deg
349.21 E Htot W
ideal Solid type -138.43 F Edot W
!- 2
RPN (a) is time-average combustion power (Watt)
! Verify (A) > 1, to ensure enough fresh air. The fuel is methane,
! which has 50 MJ/kg LHV and 0.016 kg/mole. We need 2 moles of O2,
! and so 10 moles of air, per mole of CH4.
1000.0 a G or T 1.6000 A Verif
Ndot inp 50e6 / 0.016 / / 10 /
BEGIN Change from air to natural-gas combustion products.
sameas 0a a Mean P Pa
sameas 0b b Freq Hz
sameas 0c c TBeg K
sameas 1A d |p| Pa
sameas 1B e Ph(p) deg
sameas 1C f |U| m^3/s
sameas 1D g Ph(U) deg
sameas 0i i Ndot mol/s
NGcbProd Gas type
RPN (a) is methane’s ratio of DeltaNdot to Qdot (mole/Joule)
! This is the value for methane, assuming H2O stays vapor:
```

! 3 moles combustion products / moleCH4.

! This segment increments Ndot appropriately. ! This segment increments Ndot appropriately.

3.7500E-06 a G or T 2.3750E-02 A mol/s   
3.7500E-03 B mol/s

RPN guess Tm increment 1105.8 a G or T G 2005.8 A K

Tm inp + =Tm 6

g sameas 2a a G or T =6A 1000.0 A W Htot 1E -

RPN (a) is |Lambda1|, assuming sinusoidal combustion and

! (A) is the new U1. (B) is the increment in U1 due to pulsed combustion. 1.1000 a G or T (-1.0278E-02, 1.4681E-02) A m3/s (-5.3554E-06, -3.1429E-03) B m3/s

RPN (A) is the acoustic power created by pulsed combustion 0.0000 a G or T 24.433 A W Edot 1F -

## 15. Symbols

Variables not found here are intermediate factors, constants, or functions defined in the text close to where they are used.

English letters   
A area, $\mathrm { m ^ { 2 } }$   
a sound speed, $\mathrm { m } / \mathrm { s }$   
a half of rectangular pore’s width, m   
B magnetic field, tesla   
B first virial coeficient, m<sup>3</sup>/mol   
b a constant or function   
b half of rectangular pore’s breadth, m   
C compliance, $\mathrm { m ^ { 3 } / P a }$   
C a constant or function   
c a constant or function   
c heat capacity per unit mass, $\mathrm { J / k g \cdot K }$   
$c _ { p }$ isobaric heat capacity per unit mass, $\mathrm { J / k g \cdot K }$   
$C O P$ coeficient of performance, $\dot { Q } / \dot { W }$ or $\dot { Q } / \dot { E }$   
$D _ { 1 2 }$ binary mass difusion coeficient, $\mathrm { m ^ { 2 } / s }$   
D diameter, m   
d diameter, m   
$d$ diferential   
$\dot { E }$ acoustic power, W   
e 2.71828...   
$F$ force, N   
F a factor, fraction, friction factor, constant, or function   
$\mathcal { F }$ a function   
f frequency, Hz   
f spatially averaged difusion function   
f friction factor   
$f _ { M }$ Moody friction factor   
H<sup>˙</sup> rate at which energy flows, W   
h heat transfer coeficient per unit area, $\mathrm { W / m ^ { 2 } { \cdot } K }$

I electric current, amp   
i $\sqrt { - 1 }$   
J Bessel function   
K spring constant, N   
K minor-loss coeficient   
ksFrac fudge factor by which $( 1 - \phi ) k _ { s }$ is adjusted in STKSCREEN   
k thermal conductivity, W/m·K   
$k _ { T }$ thermal difusion ratio   
k real or complex wave number, $\mathrm { m } ^ { - 1 }$   
$\begin{array} { r l } { L } & { { } = k / \rho _ { m } c _ { p } D _ { 1 2 } } \end{array}$   
L electric inductance, henry   
$L$ length, m   
l length, m   
l half of plate thickness, m   
M mass, kg   
m molar mass, kg/mol (e.g., 0.004002 kg/mol for helium)   
m screen mesh number, wires/m   
$m _ { \nu }$ multiplier for turbulent efects   
$m _ { \nu } ^ { \prime }$ turbulence multiplier for inertial pressure gradient   
$N _ { N u }$ Nusselt number   
$N _ { R }$ Reynolds number   
$N _ { S t }$ Stanton number, $= N _ { N u } / \sigma N _ { R }$   
$\dot { N }$ molar flow rate, mo $\mathrm { \Omega } | / \mathrm { s }$ (One mole $= 6 . 0 2 2 \times 1 0 ^ { 2 3 }$ molecules)   
n mole fraction   
pressure, Pa   
Q heat, J   
Q˙ rate at which heat is transferred (thermal power), W   
q˙ rate at which heat is transferred per unit length, W/m   
R acoustic resistance, $\mathrm { P a { \cdot } s / m ^ { 3 } }$   
R electric resistance, ohm   
R mechanical resistance, $\mathrm { k g / s }$   
R radius, m   
$R _ { \mathrm { u n i v } }$ universal gas constant, J/mol·K   
r radius, m   
r radial coordinate, m   
S entropy, $\mathrm { J / K }$   
S surface area, $\mathrm { m ^ { 2 } }$   
S˙ rate of entropy generation, $\mathrm { { J / K { \cdot } s } }$   
s entropy per unit mass, J/kg·K   
T temperature, K   
t time, s   
U volume flow rate, $\mathrm { m ^ { 3 } / s }$   
u x component of velocity, m $/ \mathrm { s }$   
V volume, $\mathrm { m ^ { 3 } }$   
V voltage, volt

```latex
v molar volume, $\mathrm { m ^ { 3 } / m o l }$
v vector velocity, m $/ \mathrm { s }$
$W$ work, J
$\dot { W }$ rate at which work is done (mechanical or electrical power), W
w enthalpy per unit mass, $\mathrm { J / k g }$
X exergy, J
X<sup>˙</sup> rate at which exergy flows, W
x coordinate along sound-propagation direction, m
Y Neumann function
y coordinate perpendicular to x direction, m
Z acoustic impedance, $\mathrm { P a { \cdot } s / m ^ { 3 } }$
Z electric impedance, ohm
z coordinate perpendicular to $x$ and $y ,$ m
specific acoustic impedance, $\mathrm { k g / m ^ { 2 } { \cdot } s = P a { \cdot } s / m }$
$\begin{array} { r l } { z _ { n } } & { { } = z / \rho a } \end{array}$
Greek letters
$\begin{array} { c l } { \beta } & { = - ( 1 / \rho ) ( \partial \rho / \partial T ) _ { p } , } \end{array}$ thermal expansion coeficient, $\mathrm { K } ^ { - 1 }$
$\gamma$ ratio of isobaric to isochoric specific heats
$\Delta$ big diference
$\delta$ penetration depth, m
$\delta$ small diference
$\delta _ { i k }$ the unit tensor, equal to unity for $i = k$ and zero for $i \neq k$
$\varepsilon$ surface roughness
$\varepsilon$ in mixtures, function defined by Eq. (10.203)
$\begin{array} { r l } { \varepsilon _ { 2 0 } } & { { } = m \dot { N } _ { 2 0 } / \rho _ { m } \left| U _ { 1 } \right| } \end{array}$
ε $= m \dot { N } / \rho _ { m } \left| U _ { 1 } \right|$
$\epsilon _ { s }$ correction factor for finite solid heat capacity
η eficiency, $\dot { W } / \dot { Q } _ { H }$ or $\dot { E } / \dot { Q } _ { H }$
$\theta$ phase angle
κ thermal difusivity, $\mathrm { m ^ { 2 } / s }$
$\mu$ dynamic viscosity, $\mathrm { k g / m \cdot s }$
ν kinematic viscosity, $\mathrm { m ^ { 2 } / s }$
$\xi$ displacement of gas in x direction, m
Π perimeter, m
$\pi$ 3.14159...
$\rho$ density, $\mathrm { k g / m ^ { 3 } }$
$\sigma$ Prandtl number
$\sigma _ { i k }$ nine-component viscous stress tensor, $\mathrm { P a }$
$\tau$ transduction coeficient, $\mathrm { N / a m p = v o l t / ( m / s ) }$
$\tau$ $\omega t$
$\phi$ volumetric porosity
$\begin{array} { r l } { \omega } & { { } = 2 \pi f . } \end{array}$ , radian frequency, $\mathrm { s } ^ { - 1 }$
```

## Subscripts

bEMF back EMF br branch C cold e electric ef efective ext external fric friction gen generated geom geometrical grad gradient H hot H heavy component of mixture h hydraulic (i.e., r<sub>h</sub> is hydraulic radius) i inner imp impedance ini initial k thermal L light component of mixture M Moody mix sep mixture separation m mean (or mechanical) max maximum N<sup>˙</sup> steady flow Nu Nusselt(i.e., N<sub>Nu</sub> is Nusselt number)) o outer DEC, DE DeltaEC p pressure Q˙ heat R Reynolds (i.e., N<sub>R</sub> is Reynolds number) rad radiation S SOFTEND (at UNION) s series s solid sat saturation stand standing T temperature tot total trad traditional trav traveling wat water Dκ coupled mass and thermal difusion κD coupled mass and thermal difusion

κ thermal

ν viscous

0 “environment” or “ambient” or independent of time

1 first order, usually a complex amplitude

2 second order

2, k sum of second-order enthalpy and ordinary conduction

\+ positive-x direction

− negative-x direction

univ universal (i.e., $R _ { \mathrm { u n i v } } \simeq 8 . 3 1 4$ J/mol·K is the molar gas constant)

## Special symbols

Im[ ] Imaginary part of

Re[ ] Real part of,

⟨ ⟩ spatial average perpendicular to x

| | magnitude of complex number

overbar time average

overdot time derivative, time rate

tilde complex conjugate

## Bibliography

[1] T. J. Hofler. Thermoacoustic refrigerator design and performance. PhD thesis, Physics department, University of California, San Diego, 1986.

[2] T. J. Hofler. Concepts for thermoacoustic refrigeration and a practical device. In Chairman Paul Lindquist, editor, Proceedings of the 5th International Cryocoolers Conference, pages 93–101, Wright-Patterson AFB, OH, August 1988. Wright-Patterson Air Force Base.

[3] S. L. Garrett, D. K. Perkins, and A. Gopinath. Thermoacoustic refrigerator heat exchangers: Design, analysis, and fabrication. In G. F. Hewitt, editor, Heat Transfer 1994: Proceedings of the 10th International Heat Transfer Conference. Vol. 4, pages 375–380, Rugby, England, 1994. Institution of Chemical Engineers.

[4] G. W. Swift. Thermoacoustic engines. J. Acoust. Soc. Am., 84:1145–1180, 1988.

[5] S. Backhaus and G. W. Swift. A thermoacoustic-Stirling heat engine: Detailed study. J. Acoust. Soc. Am., 107:3148–3166, 2000.

[6] R. Radebaugh. A review of pulse tube refrigeration. Adv. Cryogenic Eng., 35:1191– 1205, 1990.

[7] R. Radebaugh. Development of the pulse tube refrigerator as an eficient and reliable cryocooler. Proc. Institute of Refrigeration (London), pages 11–29, 2000. https://trc.nist.gov/cryogenics/Papers/Review/1999- Development of the Pulse Tube Refrigerator.pdf.

[8] S. Backhaus, G. W. Swift, and R. S. Reid. High-temperature self-circulating thermoacoustic heat exchanger. Appl. Phys. Lett., 87:014102, 2005.

[9] G. W. Swift and S. Backhaus. Gas diodes for thermoacoustic self-circulating heat exchangers. In CP838, Innovations in Nonlinear Acoustics: 17th International Symposium on Nonlinear Acoustics, edited by A. A. Atchley, V. W. Sparrow, and R. M. Keolian, pages 399–406, Melville, New York, 2001. American Institute of Physics.

[10] G. W. Swift and D. A. Geller. Continuous thermoacoustic mixture separation. J. Acoust. Soc. Am., 120:2648–2657, 2006. Erratum J. Acoust. Soc. Am. 124:2421, 2008.

[11] S. L. Garrett. Understanding Acoustics: An Experimentalist’s View of Acoustics and Vibration. ASA Press (Springer), 2nd edition, 2020.

[12] L. E. Kinsler, A. R. Frey, A. B. Coppens, and J. V. Sanders. Fundamentals of Acoustics. John Wiley and Sons, 4th edition, 1999.

[13] G. W. Swift. Thermoacoustics: A Unifying Perspective for Some Engines and Refrigerators. First Edition: Acoustical Society of America Publications, Sewickley PA, 2002. (Second Edition: ASA Press and Springer, 2017).

[14] A. Migliori and G. W. Swift. Liquid sodium thermoacoustic engine. Appl. Phys. Lett., 53:355–357, 1988.

[15] M. Iguchi, M. Ohmi, and K. Maegawa. Analysis of free oscillating flow in a U-shaped tube. Bull. JSME, 25:1398–1405, 1982.

[16] W. H. Press, B. P. Flannery, S. A. Teukolsky, and W. T. Vetterling. Numerical Recipes in FORTRAN 77: The Art of Scientific Computing, Second Edition. Cambridge University Press, 1992.

[17] Reverse Polish notation. In Wikipedia. Retrieved on March 17, 2024, from https://en.wikipedia.org/wiki/Reverse Polish notation.

[18] B. Brown, 2001. Postfix Notation Mini-Lecture. Retrieved on 3/17/2024 from http://bbrown.spsu.edu/web lectures/postfix/.

[19] D. L. Gardner and G. W. Swift. A cascade thermoacoustic engine. J. Acoust. Soc. Am., 114:1905–1919, 2003.

[20] G. W. Swift. Encyclopedia of Applied Physics, volume 21, chapter Thermoacoustic engines and refrigerators, pages 245–264. Wiley, for American Institute of Physics, 1997.

[21] N. Rott. Damped and thermally driven acoustic oscillations in wide and narrow tubes. Z. Angew. Math. Phys., 20:230–243, 1969.

[22] N. Rott. Thermally driven acoustic oscillations, part III: Second-order heat flux. Z. Angew. Math. Phys., 26:43–49, 1975.

[23] G. W. Swift. Analysis and performance of a large thermoacoustic engine. J. Acoust. Soc. Am., 92:1551–1563, 1992.

[24] P. Merkli and H. Thomann. Thermoacoustic efects in a resonance tube. J. Fluid Mech., 70:161–177, 1975.

[25] J. R. Olson and G. W. Swift. Similitude in thermoacoustics. J. Acoust. Soc. Am., 95:1405–1412, 1994.

[26] I. Urieli and D. M. Berchowitz. Stirling Cycle Engine Analysis. Adam Hilger, Bristol UK, 1984.

[27] A. J. Organ. Thermodynamics and Gas Dynamics of the Stirling Cycle Machine. Cambridge University Press, 1992.

[28] M. A. Lewis, T. Kuriyama, F. Kuriyama, and R. Radebaugh. Measurement of heat conduction through stacked screens. Adv. Cryogenic Eng., 43:1611–1618, 1998.

[29] J. R. Olson and G. W. Swift. Acoustic streaming in pulse tube refrigerators: Tapered pulse tubes. Cryogenics, 37:769–776, 1997.

[30] J. R. Olson and G. W. Swift. Suppression of acoustic streaming in tapered pulse tubes. In R. G. Ross, Jr., editor, Cryocoolers 10, pages 307–313. Plenum, New York, 1999.

[31] G. W. Swift, M. S. Allen, and J. J. Wollan. Performance of a tapered pulse tube. In R. G. Ross, Jr., editor, Cryocoolers 10, pages 315–320. Plenum, New York, 1999.

[32] A. Bejan. Advanced Engineering Thermodynamics. Wiley, New York, 2nd edition, 1997.

[33] P. M. Morse and K. U. Ingard. Theoretical Acoustics. McGraw-Hill, 1968.

[34] W. L. M. Nyborg. Acoustic streaming. In W. P. Mason, editor, Physical Acoustics, Volume IIB, pages 265–331. Academic Press, 1965.

[35] B. L. Smith and G. W. Swift. Measuring second-order time-average pressure. J. Acoust. Soc. Am., 110:717–723, 2001.

[36] L. D. Landau and E. M. Lifshitz. Fluid Mechanics. Pergamon, 1982.

[37] R. S. Reid, W. C. Ward, and G. W. Swift. Cyclic thermodynamics with open flow. Phys. Rev. Lett., 80:4617–4620, 1998.

[38] R. S. Reid and G. W. Swift. Experiments with a flow-through thermoacoustic refrigerator. J. Acoust. Soc. Am., 108:2835–2842, 2000.

[39] R. S. Reid. Open cycle thermoacoustics. PhD thesis, Georgia Institute of Technology, School of Mechanical Engineering, 1999.

[40] S. Backhaus and G. W. Swift. A thermoacoustic-Stirling heat engine. Nature, 399:335– 338, 1999.

[41] David Gedeon. DC gas flows in Stirling and pulse-tube cryocoolers. In R. G. Ross, Jr., editor, Cryocoolers 9, pages 385–392. Plenum, New York, 1997.

[42] G. W. Swift and S. Backhaus. A resonant, self-pumped, circulating thermoacoustic heat exchanger. J. Acoust. Soc. Am., 116:2923–2938, 2004.

[43] Maarten Elferink and Thomas Steiner. Thermoacoustic waste heat recovery engine: Comparison of simulation and experiment. In Proceedings of Meetings on Acoustics, page 065002. Acoustical Society of America, 2019. Vol. 35.

[44] P. S. Spoor and G. W. Swift. Thermoacoustic separation of a He–Ar mixture. Phys. Rev. Lett., 85:1646–1649, 2000.

[45] D. A. Geller and G. W. Swift. Saturation of thermoacoustic mixture separation. J. Acoust. Soc. Am., 111:1675–1684, 2002.

[46] D. A. Geller and G. W. Swift. Thermoacoustic enrichment of the isotopes of neon. J. Acoust. Soc. Am., 115:2059–2070, 2004.

[47] M. J. D. Powell. A hybrid method for nonlinear equations. In P. Rabinowitz, editor, Numerical Methods for Nonlinear Algebraic Equations, pages 87–114. Gordon and Breach, London, 1970.

[48] M. J. D. Powell. A FORTRAN subroutine for solving systems of nonlinear algebraic equations. In P. Rabinowitz, editor, Numerical Methods for Nonlinear Algebraic Equations, pages 115–161. Gordon and Breach, London, 1970.

[49] S. M. Hino, M. Sawamoto, and S. Takasu. Experiments on transition to turbulence in an oscillatory pipe flow. J. Fluid Mech., 75:193–207, 1976.

[50] M. Ohmi, M. Iguchi, K. Kakehashi, and M. Tetsuya. Transition to turbulence and velocity distribution in an oscillating pipe flow. Bull. JSME, 25:365–371, 1982.

[51] M. Ohmi and M. Iguchi. Critical Reynolds number in an oscillating pipe flow. Bull. JSME, 25:165–172, 1982.

[52] M. Ohmi, M. Iguchi, and I. Urahata. Flow patterns and frictional losses in an oscillating pipe flow. Bull. JSME, 25:536–543, 1982.

[53] I. E. Idelchik. Handbook of Hydraulic Resistance. Begell House, New York, 3rd edition, 1994.

[54] W. M. Kays and A. L. London. Compact Heat Exchangers. McGraw-Hill, New York, 1964.

[55] G. W. Swift and W. C. Ward. Simple harmonic analysis of regenerators. J. Thermophysics and Heat Transfer, 10:652–662, 1996.

[56] J. H. So, G. W. Swift, and S. Backhaus. An internal streaming instability in regenerators. J. Acoust. Soc. Am., 120:1898–1909, 2006.

[57] J. R. Olson and G. W. Swift. A loaded thermoacoustic engine. J. Acoust. Soc. Am., 98:2690–2693, 1995.

[58] G. W. Swift and J. J. Wollan. Thermoacoustics for liquefaction of natural gas. NETL GasTIPS, 8(4):21–26, 2002.

[59] R. W. Fox and A. T. McDonald. Introduction to Fluid Mechanics. Wiley, 1985.

[60] R. M. Olson. Essentials of Engineering Fluid Mechanics. Intext Educational Publishers, New York, 1973.

[61] A. D. Pierce. Acoustics: An Introduction to Its Physical Principles and Applications. Acoustical Society of America, Woodbury, New York, 1989.

[62] A. D. Pierce. Acoustics: An Introduction to Its Physical Principles and Applications. Acoustical Society of America, Woodbury, New York, 1989. Eqs. (5-4.8), (5-4.9), (5- 4.11b), (5-4.13b).

[63] W. P. Arnott, H. E. Bass, and R. Raspet. General formulation of thermoacoustics for stacks having arbitrarily shaped pore cross sections. J. Acoust. Soc. Am., 90:3228–3237, 1991.

[64] G. W. Swift and R. M. Keolian. Thermoacoustics in pin-array stacks. J. Acoust. Soc. Am., 94:941–943, 1993.

[65] P. J. Storch, R. Radebaugh, and J. E. Zimmerman. Analytical model for the refrigeration power of the orifice pulse tube refrigerator. Technical note 1343, National Institute of Standards and Technology, 1990.

[66] N. T. Weiland and B. T. Zinn. Open cycle traveling wave thermoacoustics: Mean temperature diference at the regenerator interface. J. Acoust. Soc. Am., 114:2791– 2798, 2003.

[67] J. L. Smith and M. Romm. Thermodynamic loss at component interfaces in Stirling cycles. In Proceedings of the 27th Intersociety Energy Conversion Engineering Conference, pages 5.529–5.532. Society of Automotive Engineers, 1992.

[68] G. W. Swift and P. S. Spoor. Thermal difusion and mixture separation in the acoustic boundary layer. J. Acoust. Soc. Am., 106:1794–1800, 1999. Errata J. Acoust. Soc. Am. 107:2299, 2000; 109:1261, 2001.

[69] D. A. Geller and G. W. Swift. Thermodynamic eficiency of thermoacoustic mixture separation. J. Acoust. Soc. Am., 112:504–510, 2002.

[70] D. A. Geller and G. W. Swift. Thermoacoustic mixture separation with an axial temperature gradient. J. Acoust. Soc. Am., 125:2937–2945, 2009.

[71] E. W. Lemmon, Ian H. Bell, M. L. Huber, and M. O. McLinden. NIST Standard Reference Database 23: Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 10.0, National Institute of Standards and Technology, 2018.

[72] Y. S. Touloukian, S. C. Saxena, and P. Hestermans. Viscosity: Thermophysical Properties of Matter, Volume 11. Plenum, 1975.

[73] Y. S. Touloukian, P. E. Liley, and S. C. Saxena. Thermal Conductivity: Nonmetallic Liquids and Gases: Thermophysical Properties of Matter, Volume 3. Plenum, 1970.

[74] Y. S. Touloukian and C. Y. Ho. Properties of Nonmetallic Fluid Elements. McGraw-Hill, 1981.

[75] R. A. Hiller and G. W. Swift. Condensation in a steady-flow thermoacoustic refrigerator. J. Acoust. Soc. Am., 108:1521–1527, 2000.

[76] Richard Raspet, William V. Slaton, Craig J. Hickey, and Robert A. Hiller. Theory of inert gas-condensing vapor thermoacoustics: Propagation equation. J. Acoust. Soc. Am., 112:1414–1422, 2002.

[77] William V. Slaton, Richard Raspet, Craig J. Hickey, and Robert A. Hiller. Theory of inert gas-condensing vapor thermoacoustics: Transport equations. J. Acoust. Soc. Am., 112:1423–1430, 2002.

[78] R. Pritchard, J. J. Guy, and N. E. Connor. Industrial Gas Utilization—Engineering Principles and Practice. Bowker Publishing Company, Epping, Essex, 1977.

[79] O. J. Foust, editor. Sodium-NaK Engineering Handbook. Gordon and Breach, New York, 1972.

[80] E. D. Marquardt, J. P. Le, and Ray Radebaugh. Cryogenic material properties database. In R. G. Ross, Jr., editor, Cryocoolers 11, pages 681–688. Springer, 2000.

[81] Choong S. Kim. Thermophysical properties of stainless steels. Technical Report ANL-75-55, Argonne National Laboratory, 1975.

[82] D. Bentz and Kuldeep Prasad. Thermal performance of fire resistive materials I. characterization with respect to thermal performance models. Technical Report NISTIR 7401, National Institute of Standards and Technology, 2007.

[83] N. J. Simon, E. S. Drexler, and R. P. Reed. Properties of copper and copper alloys at cryogenic temperature. Technical Report NIST Monograph 177, National Institute of Standards and Technology, 1992.

[84] K. Matsumoto, T. Numazawa, Y. Ura, T. Ujiyama, and S. Abe. Thermal and magnetic properties of regenerator material $\mathrm { G d _ { 2 } O _ { 2 } S }$ . J. Phys.: Conf. Ser., 897:012010, 2017.

[85] Ray Radebaugh, personal communication.

[86] ASM Handbook Committee. ASM Handbook. ASM International, 1990.

[87] J. Gary, A. O’Gallagher, and R. Radebaugh. A numerical model for regenerator performance. Technical report, NIST-Boulder, 1994. Also known as REGEN 3.1 Users Guide.

[88] John P. Koulakis, Seth Pree, Alexander L. F. Thornton, Alexander S. Nguyen, and Seth Putterman. Pycnoclinic acoustic force. In Proceedings of the 21st International Symposium on Nonlinear Acoustics, acousticalsociety.org, 2018. Acoustical Society of America. paper S1-4.

[89] John P. Koulakis and S. Putterman. Convective instability in a stratified ideal gas containing an acoustic field. J. Fluid Mech., 915, 2021. doi:10.1017/jfm.2021.83.

[90] T. G. Wang and C. P. Lee. Radiation pressure and acoustic levitation. In M. F. Hamilton and D. T. Blackstock, editors, Nonlinear Acoustics, pages 177–205. Academic Press, 1998.

[91] Jonas T. Karlsen, Per Augustsson, and Henrik Bruus. Acoustic force density acting on inhomogeneous fluids in acoustic fields. Phys. Rev. Lett., 117:114504–1–114504–6, 2016.

## Segment index

ANCHOR examples, 82 reference summary, 239 tutorial discussion, 84 with TBRANCH, 235   
BEGIN examples, 66, 68, 71, 105, 120 reference summary, 228 twice in one model, 230   
BLKDATA reference summary, 249   
BRANCH examples, 175 reference summary, 174   
COMPLIANCE examples, 64 reference summary, 162   
CONE examples, 12, 64, 161 reference summary, 159 tutorial discussion ignoring steady flow, 25   
CONSTANTS reference summary, 249   
DUCT examples, 12, 64, 82, 154 reference summary, 153 tutorial discussion ignoring steady flow, 12, 25   
HARDEND examples, 64, 82, 109 reference summary, 232

tutorial discussion ignoring steady flow, 20, 21 with steady flow, 109 HX examples, 64, 82, 105 reference summary, 195 IDUCER examples, 178 reference summary, 176 tutorial discussion, 25 IEDUCER examples, 172 reference summary, 170 tutorial discussion, 26 IESPEAKER as alternator, 58 examples, 93, 172 magnetic flux saturation, 282 reference summary, 170 with piston blowby , 58 IMPEDANCE reference summary, 165 INSULATE reference summary, 239 ISPEAKER examples, 178 magnetic flux saturation, 282 reference summary, 176 tutorial discussion, 26 JOIN examples, 96, 109 reference summary, 217 MINOR

examples, 109, 116 reference summary, 166 tutorial discussion with steady flow, 115   
MIXBL reference summary, 219 tutorial discussion, 127   
MIXCIRC examples, 131 reference summary, 219 tutorial discussion, 127   
MIXSLAB reference summary, 219 tutorial discussion, 127   
MIXTBL reference summary, 222   
MIXTCIRC reference summary, 222   
MIXTSLAB reference summary, 222   
OPNBRANCH examples, 175 reference summary, 174   
PISTBRANCH examples, 175 radiation impedance from flanged tube, 176 reference summary, 174   
PX calculation subtleties, 276 reference summary, 198   
RPN examples, 58, 89 reference summary, 240 tutorial discussion, 51   
SOFTEND as open-tube radiation impedance, 233 examples, 105, 109, 233 reference summary, 232 tutorial discussion ignoring steady flow, 34 with steady flow, 105, 109   
STKCIRC examples, 82, 183 reference summary, 180   
STKCONE reference summary, 192   
STKDUCT examples, 96 reference summary, 192   
STKPIN examples, 183 reference summary, 180   
STKPOWERLW calculation subtleties, 276 reference summary, 186 sphere-bed example, 188   
STKRECT examples, 105, 183 reference summary, 180 tutorial discussion with steady flow, 105   
STKSCREEN calculation subtleties, 276 examples, 89, 109 reference summary, 186 tutorial discussion ignoring steady flow, 89 with steady flow, 109   
STKSLAB examples, 64, 183 reference summary, 180   
SURFACE examples, 64, 82 reference summary, 164   
SX calculation subtleties, 276 examples, 89 reference summary, 198   
SYSEXEC examples, 251 reference summary, 251   
TBRANCH examples, 58, 93, 109, 120 reference summary, 234

tutorial discussion ignoring steady flow, 34 with steady flow, 109 TITLE reference summary, 228 TX reference summary, 195 UNION examples, 58, 93, 109, 120 reference summary, 236 tutorial discussion ignoring steady flow, 34 with steady flow, 109 VDUCER examples, 178 reference summary, 176 tutorial discussion, 25 VEDUCER examples, 172 reference summary, 170 tutorial discussion, 26 VESPEAKER

as alternator, see IESPEAKER examples, 71, 172 magnetic flux saturation, 282 never use with R = ωL = 0, 170 reference summary, 170   
VOLUME reference summary, 248   
VSPEAKER examples, 68, 178 magnetic flux saturation, 282 never use with R = ωL = 0, 170 reference summary, 176 tutorial discussion, 26   
VXQ1 examples, 115 reference summary, 204 tutorial discussion with steady flow, 115   
VXQ2 reference summary, 204   
VXT1 reference summary, 204   
VXT2 reference summary, 204

## Subject index

Accessibility options, see Visually impaired users Autolayout, 88

Black-body radiation, 148   
Branches, structured, 34, 234   
Bugs, reporting, 7, 142   
Choked flow, 142   
Colors, meanings of, 23   
Combustion, pulsed, 283   
Comment lines, 88   
example, 89   
Continuity equation, 10, 62, 136   
Convergence problems   
useful strategies, 79, 81   
Convergence tolerance, 141   
Copyright, 8   
Debug alerts, 142   
<default.ini>, 141   
<DeltaEC.exe.log>, 142

Elastoclinic acoustic force, 275   
Energy equation axial, 63, 136 lateral, 104, 136   
Energy notation, 138   
Error messages, 142 reporting, 142   
Examples alternator load impedance, 58 electrical alternator, 58 force phasor, 245 gas diode, 109, 116 gas, changing mid-model, 230

incremental plots, 45, 64, 82 looped model, 35, 58, 93, 109, 116 mixture separation, 131 piston blowby, 58 pulse-tube refrigerator, 96 pulsed combustion, 283 radiation impedance, 176, 233 self-circulating heat exchanger, 115 standing-wave engine, 82 standing-wave refrigerator, 64, 105 state plots, 17, 64, 82, 89, 96, 105, 109, 115, 131 Stirling engine, 109 Stirling refrigerator, 89 structured branches, 34, 109, 115, 234 traveling-wave engine, 109 traveling-wave refrigerator, 89 with nonzero N<sup>˙</sup> , 105, 109, 115, 131 Exergy, 101, 104 File types <.blk>, 249 <.err>, 143 <.ini>, 141 <.ip>, 45 <.isv.dat>, 41 <.isv.dir>, 41 <.log>, 142 <.out>, 12 <.sp>, 41 <.ssv.dat>, 41 <.ssv.dir>, 41 <.tpf>, 27, 264, 271 <.tpm>, 265 Flipping segments, 88

Font, changing size, 17   
Force-phasor calculation, 244, 273   
Forward reference condition avoiding, 78   
FRC, see Forward reference condition   
Gas diode, examples, 109, 116, 168   
Gases, 27, 255 including liquids, 27 mid-model change of, 230, 255 temperature floor, 141 user-defined, 27, 264, 265   
Graphs, see State plots, Incremental plots, Phasor plots, Schematic view   
Guesses and targets convergence dificulty, 79, 81 examples, 19, 74, 91, 93, 120 general guidance, 19, 74, 78, 139 in RPN, 55, 59 maximum number, 139 meeting targets, 79, 81 mixture separation, 129 non-standard guesses, 59 non-standard targets, 55, 244 phase target near ±180<sup>◦</sup>, 146 restoring, 88 rewinding incremental plots, 49 Run with Fixed Guesses, 81 shooting-method parameters, 141 troubleshooting, 79, 81 with nonzero N<sup>˙</sup> , 108, 112   
Harmonic content, 144   
Head-loss equation, 104, 136   
Heat exchange, external ∆T, 147   
Highlights display, 34   
Hydraulic radius of screens, 90, 150, 187   
Incremental plots, 45 cloning, 42 examples, 68, 85 multiple models, 60 poor-convergence indicators, 143 rewinding, 49   
Inherent limitations, 144   
Installation, 7   
Integration variables, 136 acoustics only, 11 thermoacoustics, 64 with mixture separation, 128 with steady flow, 104   
ksFrac including vessel-wall conduction, 148 recommended value, 148   
Legs, 43, 234   
License, 8   
Limitations, 144, 148, 150   
Linking multiple models, 60, 240   
List linkages, 54   
Looped models, examples, 35, 58, 93, 109, 116   
Magnetic flux saturation, 282   
Master–slave links, 30, 53   
Messages, error and warning, 142   
Mixture separation, typical end conditions, 129   
Mixture-separation equation, 128, 136   
Mode, see Normalization mode   
Momentum equation, 10, 62, 136   
Multi-model plots, 60   
Multiple models, see Linking multiple models   
Nint, 141   
Nonlinear efects, 6   
Normalization mode, 141   
Notation, 6, 287 energy, 138   
Notes, user-specified, 88   
Numerical integration method, 139   
Numerical options integration steps, 141 shooting method, 141 temperature floor, 141   
Open tube, radiation impedance, 174, 233   
Options, numerical, 141   
Overview of DeltaEC, 1, 10, 62, 136   
Phases near ±180<sup>◦</sup>, 146   
Phasor plots, 33, 43, 98   
Plots, see State plots, Incremental plots, Phasor plots, Schematic view   
Polar plots, see Phasor plots   
Power notation, 138   
Pressure, second-order, 104 examples, see Looped models inherent limitations, 145 subtleties in calculation, 138   
Pulsed combustion, 283   
Pycnoclinic acoustic force, 275   
Radiation impedance open end of flanged tube, 176 open end of unflanged tube, 233   
Rayleigh streaming, 151   
Reporting bugs, 7, 142   
Restoring guesses, 88   
Rewinding incremental plots, 49   
Run monitor, 15   
Running DeltaEC from another program, 253 from GUI, 7, 14 from terminal, 253   
sameas, 29   
Schematic view, 33   
Screens, hydraulic-radius and porosity calculation, 90, 150, 187   
Shooting method, see Guesses and targets   
Size of font, 17   
Solids, 27, 267 temperature floor, 141 user-defined, 271   
Sphere bed, example, 188   
Splitting a segment, 88   
Standing-wave engine headroom, 151   
State plots, 17, 41 cloning, 42 examples, 72, 84, 108 phasor, 43, 98 with legs, 43   
Steady flow, 103, 138 and user-defined gases, 264   
Structured branches, 34, 234   
Symbols, 287   
⟨T<sub>1</sub>⟩, 138, 244   
Targets, see Guesses and targets   
Temperature floor, 141, 142, 255, 267   
Thermophysical properties formulas for each gas, 255 formulas for each solid, 267 from the keyboard, 39 in RPN, 53, 240   
Time phase, 27, 70, 75 examples, 68, 71 in side-branch transducers, 177   
Tmin, see Temperature floor   
Tolerance, convergence, 141   
Toroidal models, see Looped models   
Total Power, typical end condition, 108, 112   
Turbulence, 29, 144 in CONE, 29, 145, 150, 159 in DUCT, 29, 145, 150, 153, 155 in MINOR, 150, 166 in PX, 201 in STKPOWERLW, 145, 191 in STKSCREEN, 145, 191 in SX, 200 in VX\*\*, 145, 209   
User interface, GUI, 14 terminal, 253   
Users Guide, 6   
Variables, 287   
Visually impaired users, features for, 17   
Warning messages, see Error messages
