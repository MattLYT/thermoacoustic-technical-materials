---
title: A high performance thermoacoustic engine · MinerU全文
record_role: machine-transcription
parse_method: MinerU
source_sha256: fdd2e24fcc472e98d12a209ef266c2a0e9b2b0f34ce25c6bf42f8a89962b49c6
source_pages: 7
---

# A high performance thermoacoustic Stirling-engine

M.E.H. Tijani S. Spoelstra

Published in Journal of Applied Physics, Volume 110, 093519 1-6, 2011

ECN-W--11-051

NOVEMBER 2011

# A high performance thermoacoustic engine

M. E. H. Tijani<sup>a)</sup> and S. Spoelstra

Energy research Centre ofthe Netherlands (ECN), PO Box 1, 1755 ZG Petten, The Netherlands

(Received 7 April 2011; accepted 8 October 2011; published online 10 November 2011)

In thermoacoustic systems heat is converted into acoustic energy and vice versa. These systems use inert gases as working medium and have no moving parts which makes the thermoacoustic technology a serious alternative to produce mechanical or electrical power, cooling power, and heating in a sustainable and environmentally friendly way. A thermoacoustic Stirling heat engine is designed and built which achieves a record performance of 49% of the Carnot efficiency. The design and performance of the engine is presented. The engine has no moving parts and is made up of few simple components. VC 2011 American Institute ofPhysics. [doi:10.1063/1.3658872]

## I. INTRODUCTION

An engine extracts heat from a high-temperature source, converts part of it into work and rejects the other part to a low-temperature sink as illustrated in Fig. 1. First law of thermodynamics states that in steady state $Q _ { h } = Q _ { l } + W$ and the second law of thermodynamics states that the maximal fraction of $Q _ { h }$ that can be converted into work is $( I - T _ { l } / T _ { h } )$ which is always lower than 1. This fraction is called the Carnot efficiency.

Conventional engines like internal combustion engines, gas turbines, and Stirling cycle engines need complex mechanical parts like pistons, valves, and other mechanical elements to produce work. Thermoacoustic engines, however, have no moving mechanical parts. In an effort to eliminate the moving parts in Stirling systems<sup>1</sup> and related sealing problems, Ceperley<sup>2,3</sup> recognized in 1979 that the time phasing between the pressure and velocity of the gas in the regenerator of a Stirling system is the same as in a traveling acoustic wave. This inspired Ceperley to build a thermoacoustic traveling-wave (Stirling) engine consisting simply of a regenerator and two heat exchangers placed in a looped tube. However, this first thermoacoustic Stirling engine did not produce acoustic power due to the high viscous losses in the regenerator caused by high gas velocity. Additionally, the topology of the looped tube caused a streaming of gas which created an undesirable heat leak between hot side and cold side of the regenerator.<sup>4</sup> It is only in 1998 that the first working traveling-wave thermoacoustic engine was demonstrated but at very low efficiency.<sup>5</sup> The breakthrough in the development of thermoacoustic engines was realized by Backhaus et al.<sup>6,7</sup> in 1999 when they developed a traveling-wave thermoacoustic engine that converts heat into acoustic power with an efficiency of 30%, corresponding to 41% of the Carnot efficiency. They solved the problems encountered by Ceperley by placing the looped tube at the location of the pressure antinode of a quarter-wavelength standing-wave resonator. This location is characterized by a high acoustic pressure and a low gas velocity and thus a high acoustic impedance. This reduces the viscous losses in the regenerator. They also reduced the gas streaming to a minimum level by using a jet-pump.<sup>6,7</sup> However, up to date all the attempts done by different thermoacoustic research groups to improve or to reproduce this performance failed.

The aim of this paper is to present a study of a thermoacoustic Stirling-engine that achieves a record performance of 49% of the Carnot efficiency. The design, development, and performance measurements of the cooler will be presented. The remaining of this paper is organized as follows: Sec. II is devoted to description of the engine. Section III presents the performance indicators used to characterize the engine. Section IV shows the measurement results. In the last section some conclusions are drawn.

## II. DESCRIPTION OF THE ENGINE

A schematic illustration of the high-performance thermoacoustic Stirling-engine is shown in Fig. 2. The engine consists mainly of a torus-shaped section attached to a quarter-wavelength acoustic resonator. The resonator operates as a pressure vessel for the working gas and determines the operating resonance frequency of the system.

![[mu_fdd2e24f_be9d0cf681f9c70b387d.jpg]]  
FIG. 1. Illustration of a heat engine. An engine absorbs heat $Q _ { h }$ from a source at a high temperature $T _ { h } ,$ converts a part of that heat into work $\mathrm { w , }$ and rejects the remaining heat $Q _ { \mathrm { l } }$ to a sink at a low-temperature $T _ { \mathrm { l } } .$

![[mu_fdd2e24f_74473536b59fa23b2a77.jpg]]  
FIG. 2. Schematic illustration of the thermoacoustic Stirling-engine. An acoustic load is placed on the resonator to control the power output of the engine. The resonator and acoustic load are not to scale. The “P’s” are Pressure sensors.

Figure 3 shows the torus-shaped section which contains a first ambient heat exchanger (AHX1) to remove the rejected heat from the engine, a regenerator (REG), a hot heat exchanger (HHX) to supply heat to the engine, a thermal buffer tube (TBT), a second ambient heat exchanger (AHX2), and a feedback tube (L). The gas column in TBT provides thermal insulation between HHX and AHX2. AHX2 is not required for the operation of the engine but it is useful to intercept heat leaking down the TBT.

The thermoacoustic Stirling engine functions like an acoustic amplifier.<sup>2,3,7</sup> The application of heat to the HHX creates a temperature difference across the regenerator which generates spontaneously an acoustic wave.<sup>9</sup> The acoustic network formed by the elements in the torus section forces the acoustic wave to propagate anti-clock wise entering the regenerator via the AHX1, gets amplified by the imposed temperature gradient along the regenerator, and exits via the HHX. The acoustic wave is amplified by forcing the helium gas in the regenerator to execute a thermodynamic cycle similar to the Stirling cycle.<sup>3,7</sup> The acoustic wave takes care of the compression, displacement, expansion, and the timing necessary for the Stirling cycle. To keep the process ongoing, part of the acoustic power is fed back through the feedback tube (L) to the ambient side (AHX1) of the regenerator to be amplified. The remainder of the acoustic power is available as useful power at the junction to the resonator. During the thermoacoustic cycle part of the heat supplied to the HHX is converted into acoustic power and the remainder is rejected at the AHX1, similar to the engine in Fig. 1.

The thermoacoustic computer code DeltaE<sup>10</sup> is used to design the engine. The engine is designed to achieve high performance. In the following, a short description of the components of the engine is given with special attention to the design improvements that have been made compared to previous designs.<sup>7</sup> These improvements have led to the achievement of the high performance. It is worthwhile to note here that the engine achieves a higher performance than the Backhauss-Swift thermoacoustic-Stirling engine although its smaller dimensions.

![[mu_fdd2e24f_5398e1cea72a695765bc.jpg]]  
FIG. 3. (Color online) Thermoacoustic Stirling engine. (Left) Detailed schematic illustration of the torus section. (Right) CAD-illustration of the torus section. Beginning at the first ambient heat exchanger (AHX1) and anti-clockwise around the torus are the regenerator (REG), the hot heat exchanger (HHX), the thermal buffer tube (TBT), the second ambient heat exchanger (AHX2), the junction to the resonator, and the feedback tube (L).

## Operation conditions

The engine uses helium at 40 bar and an operation frequency of 130 Hz. Higher pressure and higher frequency means higher power density and less thermo-viscous losses in boundary layers.

## First ambient heat exchanger (AHX1)

The design of the ambient heat exchanger is of a kind that is more often used in thermoacoustic systems. It consists of a cylindrical brass block containing 240 parallel channels with an inside diameter of 1.5 mm and a length of 2 cm. The helium gas oscillates through these channels. The diameter of the channels is smaller than in previous designs.<sup>7</sup> This improves the heat transfer between the helium and the brass block and leads to an increase in performance. Water flows around the perimeter of this block to carry away the rejected heat.

## Regenerator (REG)

The regenerator consists of a 6 cm long stack of 200- mesh stainless steel screens with a diameter of 4.15 cm. The diameter of the screen wire is 36 lm. A volume porosity of 77% and a hydraulic radius of 33 lm are deduced from the weight of the regenerator. The hydraulic radius of the regenerator should be smaller than the thermal penetration depth of the helium gas at the prevailing conditions, to ensure good thermal contact between helium gas and the regenerator material. A smaller hydraulic radius leads to a better thermal contact but at the same time the viscous losses increase. The design of the regenerator is therefore a compromise between a good thermal contact between the gas and the solid matrix and low viscous losses. The thermal penetration depth is depending on the temperature and thus varies along the regenerator. The regenerator material has been selected to have a hydraulic radius that is on average 5 times smaller than the thermal penetration depth. This value is smaller than used in the past,<sup>7</sup> which leads to lower viscous losses.

## Hot heat exchanger (HHX)

The hot heat exchanger consists of a cylindrical stainless steel block which contains 108 parallel holes with a diameter of 3 mm and a length of 3 cm through which the helium gas oscillates. This ensures a good heat transfer from the HHX to the helium gas. Heat is supplied by cartridge heaters, inserted into the HHX block generating a maximal thermal power of 1.25 kW. The regenerator holder, HHX, and the TBT are machined from one stainless steel block.

## Thermal buffer tube (TBT)

The thermal buffer tube consists of a thin-walled cylindrical tube with a diameter of 4.2 cm which is much larger than the thermal penetration depth of helium (0.1 mm). The tube has a length of 20 cm which is about 10 times the peakpeak displacement of the helium gas at high acoustic amplitude. This makes the slug of oscillating gas long enough to provide good thermal insulation between HHX and AHX2.

## Feedback inertance (L)

The Backhauss-Swift thermoacoustic-Stirling engine uses separate feedback inertance and compliance<sup>7</sup> with different diameters. This leads to flow losses due to area changes. This problem is avoided by using a feedback tube with constant diameter (L). The feedback tube combines the function of the inertance and compliance and it is easy to construct. The internal surface of the tube is made smooth and bends are made gentle to further minimize acoustic losses.

## Acoustic network

The acoustic network formed by the torus components is designed in such a way that the velocity at the ambient side of the regenerator lags the pressure by 30<sup></sup>, whereas at the hot side the velocity leads the pressure by 30<sup></sup>. This forms the ideal condition for the Stirling cycle in the regenerator.<sup>11</sup> This condition is critical for the achievement of high performance.

## Resonator

The quarter-wavelength resonator consists of three parts. The first part is made of a straight cylindrical tube with a length of 1 m and an inside diameter of 5.5 cm (2” pipe), followed by a conical shaped part that increases the inside diameter to 16 cm over a length of 1.3 m. The last section is a stainless steel tube with a diameter of 16 cm and length of 39 cm, terminating in a cap. The large volume, formed by the last section, mimics an open end. The acoustic resonator is not optimized for minimal acoustic losses.

## Streaming

In addition to the precautions taken to minimize the acoustic losses due to minor-losses and turbulence, an elastic membrane is placed just above the AHX1 to suppress Gedeon streaming.<sup>4,7</sup> Gedeon streaming is a time-averaged mass flux which circulates around the torus removing heat from the hot heat exchanger and depositing it at AHX2 without taking part in the thermoacoustic conversion process in the regenerator. This causes a heat leak that seriously degrades the performance of the engine. The membrane is acoustically transparent but blocks completely Gedeon streaming. An elastic membrane causes less acoustic losses than a jet-pump.

Flow straighteners are placed in the thermal buffer tube at HHX and AHX2 to reduce jet-streaming in the TBZ.<sup>7</sup> The measurements of the heat leak down the TBZ and intercepted by AHX2 show that this is only due to heat conduction through the wall and gas of the TBZ. The absence or reduction to a minimal level of the heat leak from the hot heat exchanger due to Jet-streaming, Gedeon streaming, Rayleigh streaming, and radiation has contributed to the achievement of the high performance.

## Acoustic load

The variable acoustic load, shown in Fig. 2, consists of a 1-liter tank and an adjustable valve. The acoustic power dissipated in the load is a function of the valve setting.

## III. PERFORMANCE INDICATORS

The characterization of the performance of the engine requires knowledge of many quantities like temperatures, dynamic pressures at different locations of the system, heat powers at the hot and ambient heat exchangers, and acoustic power produced by the engine. Thermocouples are used to measure the temperature at various locations of the engine. One thermocouple is placed in the hot heat exchanger block. Three thermocouples are used to measure the temperature through the regenerator and are centered radially: one at the cold side, one at the center, and one at the hot side. The axial temperature profile within the regenerator is used to detect Gedeon streaming.<sup>7</sup> In the absence of Gedeon streaming the temperature profile is linear. Two thermocouples are used to measure the inlet and outlet temperatures of the water cooling the ambient heat exchangers. Several pressure sensors are placed throughout the system. They are indicated by “P” in Fig. 2. The acoustic power, produced by the engine, is measured by the 2-microphone method $^ { 7 , 1 2 ^ { \circ } }$ using the two pressure sensors $\mathrm { P } _ { 3 }$ and $\mathrm { P } _ { 4 } .$ The pressure sensors $\mathrm { P _ { 4 } }$ and $\mathrm { P } _ { 5 }$ are used to measure the acoustic power dissipated in the acoustic load.<sup>12</sup> The sensors are always calibrated at the beginning of each series measurement.

The thermal power input to the engine from the electrical heaters is given by

$$
\dot { Q } _ { h } = { V I } ,\tag{1}
$$

where V is the voltage across the heater and I is the current. The heat, extracted at the ambient heat exchangers by cooling water, is given by

$$
\begin{array} { r } { \dot { Q } _ { a } = \rho _ { w } c _ { p } U ( T _ { o u t } - T _ { i n } ) . } \end{array}\tag{2}
$$

Here is $\rho _ { w }$ the density of water, $c _ { p }$ is the specific heat, $U$ is the volume flow rate of water, and $T _ { i n }$ and $T _ { o u t }$ are the input and output temperatures of the water stream flowing through the ambient heat exchanger. The volume flow rate is measured with a turbine flow meter.

By reference to Fig. 2, the acoustic power flowing past the midpoint of the two pressure sensors $p _ { 3 }$ and $p _ { 4 }$ is given by<sup>12</sup>

$$
\dot { W } _ { 2 m i c } = \frac { A } { 2 \omega \rho _ { g } \Delta x } \left[ \left( 1 - \frac { \delta _ { \nu } } { r } \right) p _ { 3 } p _ { 4 } \sin \alpha + \frac { \delta _ { \nu } } { 2 r } \left( p _ { 3 } ^ { 2 } - p _ { 4 } ^ { 2 } \right) \right] .\tag{3}
$$

Here $p _ { 3 }$ and $p _ { 4 }$ are the amplitudes of the dynamic pressures measured by the two pressure sensors, Dx is the distance between the two transducers along the resonator, a is the phase angle by which $p _ { 3 }$ leads $p _ { 4 } .$ , x is the angular frequency, $\rho _ { g }$ is the average density of the gas, and $\delta _ { \nu }$ is the viscous penetration depth.<sup>12</sup>

The acoustic power dissipated in the load is given by<sup>12</sup>

$$
\dot { W } _ { l o a d } = \frac { \omega V _ { c } } { 2 \gamma p _ { m } } p _ { 4 } p _ { 5 } \sin \beta ,\tag{4}
$$

where $p _ { 4 }$ and $p _ { 5 }$ are the amplitudes of the dynamic pressures measured at the entrance of the load and in the compliance of the load respectively, $\beta$ is the phase difference between $p _ { 4 }$ and $p _ { 5 } ,$ x is the angular frequency, $V _ { c }$ is the volume of the compliance of the load, $p _ { m }$ is the average pressure of the gas, and $\gamma$ is the ratio of the isobaric to isochoric specific heats. The pressure transducer $P _ { 4 }$ is placed at the port of the load on the resonator. It is used for the two-microphone method and to measure the acoustic power dissipated in the load. The power measured by the two-microphone method $( \bar { W } _ { 2 m i c } )$ is the sum of the acoustic power dissipated in the resonator section to the left of the midpoint of the two-microphones $( \dot { W } _ { r e s } )$ and the acoustic power dissipated in the load $( \dot { W } _ { l o a d } ) , ^ { 7 }$

$$
\dot { W } _ { 2 m i c } = \dot { W } _ { r e s } + \dot { W } _ { l o a d } .\tag{5}
$$

The two-microphone method is difficult due to its sensitivity to the microphone position, the phase difference, and flow conditions.<sup>12</sup> The accuracy of the two-microphone measurements is checked by plotting expression (6) for different drive ratios. The drive ratio (dr) is the ratio of the dynamic pressure amplitude measured by $P _ { \perp }$ (antinode) and the mean pressure of the gas. The plot of $\bar { W } _ { 2 m i c }$ versus $\dot { W } _ { l o a d }$ at constant drive ratio should be a line of slope one and the intercept at $\dot { W } _ { l o a d } = 0$ gives $W _ { r e s }$ . This is because $\bar { W } _ { r e s }$ is constant if dr is constant. Loading the engine by opening the valve of the load causes a decrease of dr. The drive ratio is then kept constant by increasing the heat input $\dot { Q _ { h } }$

The performance of the engine is given by

$$
\eta = \frac { \dot { W } } { \dot { Q } _ { h } } ,\tag{6}
$$

where $\dot { \boldsymbol { W } }$ is the acoustic power produced by the engine (entering the resonator) which is deduced from $\bar { W } _ { 2 m i c }$ by extrapolation using the DeltaEC model of the system. The Carnot efficiency of the engine is given by

$$
\eta _ { C } = \frac { T _ { h } - T _ { a } } { T _ { h } } .\tag{7}
$$

Here $T _ { h }$ is the temperature of the hot side of the regenerator measured by the thermocouple placed between HHX and regenerator and $T _ { a }$ is the average temperature of the cooling water flowing through the ambient heat exchanger. The performance relative to Carnot is defined as the ratio

$$
\eta _ { r } = \frac { \eta } { \eta _ { C } } .\tag{8}
$$

The experimental results are presented for several drive ratios. The hot parts of the system are thermally insulated to minimize the heat leak to the surrounding.

## IV. RESULTS

Static measurements are first carried out to determine the static heat losses consisting of heat conduction, radiation, and convection from the system. The acoustic load is opened fully to prevent the engine to start-up. Different thermal heat powers are supplied to the hot heat exchanger and the temperatures are measured when a stationary situation is obtained. The static measurements show that typically about 70% of the heat input is lost by conduction through the regenerator and about 10% is lost by conduction through the TBZ. The remaining 20% of the heat input is lost by conduction through the insulation, conduction along feed-through like thermocouples, and radiation. The effective thermal conductivity of the regenerator is calculated to be about 2.6 W=Km. It includes conduction through the regenerator screens as well as conduction through the surrounding tube. This relatively large number is caused by conduction through the wall of the regenerator holder. The wall thickness at that location is 3 mm.

The first dynamic measurements with the engine and without membrane show that an appreciable amount of heat is leaking from the HHX to AHX2 which is much larger than what would be caused by heat conduction down the TBZ, through gas and wall. The analysis of the temperature profile along the regenerator shows that it deviates from linear. This is an evidence for the presence of Gedeon streaming.<sup>4,7</sup> Figure 4 shows an example of the temperature profile in the regenerator for a drive ratio of about 4% with and without membrane. In the rest of this paper all the measurements are done with a membrane placed at the AHX1.

To check the accuracy of the acoustic power measured by the two-microphone method $\dot { W } _ { 2 m i c }$ is plotted versus $\dot { W } _ { l o a d }$ for several drive ratio’s in Fig. 5. The solid lines are linear fits to experimental data. For all drive ratios, the slope is about 1 which gives confidence in the measurements. For the drive ratio of 8% the engine could not be loaded, so only one point is measured corresponding to the acoustic power dissipated in the resonator.

The measured thermal performance of the engine is shown in Fig. 6. The performance increases slightly as a function of the hot end temperature of the regenerator for all drive ratios. The graph also includes a measurement point at a drive ratio of 8.14%. An important increase is recorded as function of the drive ratio. At $t _ { h } = 5 1 0 ^ { \circ } \mathrm { C }$ for example the performance is 20% for a drive ratio of 3% while at 7% the performance is 30%. According to the linear approximation of thermoacoustics, the efficiency would not depend on drive ratio. However, loss mechanisms like heat conduction and heat convection do not scale with the square of the drive ratio, as the acoustics does. Therefore, the loss mechanisms become less important at higher drive ratios, leading to a higher efficiency. Increasing the drive ratio even further would eventually lead to non-linear effects that degrade performance. It is not clear at the moment at which drive ratio this will occur. At its most efficient operating point (drive ratio ¼ 8.14% and $t _ { h } = 5 8 0 ^ { \circ } \mathrm { C } )$ the engine produces 280 W of acoustic power at a thermal efficiency of 32%, corresponding to 49% of Carnot efficiency. At this point, no load measurements could be performed but a comparable performance is also measured for a drive ratio of 7% where the engine can be loaded. This performance is the highest performance that has been measured up to date.

![[mu_fdd2e24f_29d283ad4649a68e1e79.jpg]]  
FIG. 4. (Color online) Temperature profile in the regenerator with and without membrane for a drive ratio of 4%. The lines are only guides to the eye. Without membrane the temperature profile in the regenerator is not linear indicating the existence of Gedeon streaming. The temperature of the axial midpoint is lower than it would be in absence of streaming. This is due to the flux of cold gas entering the cold end of the regenerator. The use of the membrane leads to the suppression of the Gedeon streaming as indicated by the linear temperature profile.

![[mu_fdd2e24f_a732a677b7028de2f450.jpg]]  
FIG. 5. (Color online) Acoustic power measured with the two microphone method as a function of the power dissipated in the acoustic load. The measurements are performed for several drive ratios. The solid lines are linear fits to data. For all drive ratio’s the slope is about 1.

![[mu_fdd2e24f_db5527d900243e2d6211.jpg]]  
FIG. 6. Measured thermal efficiency of the engine as function of the hot temperature for different drive ratios. The lines connecting the points are only to guide the eye.

## V. CONCLUSIONS

A high performance thermoacoustic Stirling-engine without moving parts is designed, built, and tested. The engine achieved a record efficiency of 49% of the Carnot efficiency. The high performance in addition to the environmentally friendly character, the lack of moving parts, the elegance, and low cost will make the thermoacoustic technology more attractive for industrial applications.

## ACKNOWLEDGMENTS

This work has been partly funded by SenterNovem (Dutch agency for sustainable development and innovation) within the EOS-LT program.

<sup>1</sup>G. Walker, Stirling Engines (Clarendon, Oxford, 1980).

<sup>2</sup>P. H. Ceperley, J. Acoust. Soc Am. 66, 1508 (1979).

<sup>3</sup>P. H. Ceperley, J. Acoust. Soc Am. 77, 1239 (1985).

<sup>4</sup>D. Gedeon, in Cryocoolers, edited by R. G. Ross (Plenum, New York, 1997), Vol. 9, p. 385.

<sup>5</sup>T. Yazaki, A. Iwata, and T. Maekawa, Phys. Rev. Lett. 81, 3128 (1998).

<sup>6</sup>S. Backhaus and G. W. Swift, Nature 399, 335 (1999).

<sup>7</sup>S. Backhaus and G. W. Swift, J. Acoust. Soc. Am. 107, 3148 (2000).

<sup>8</sup>P. H. Ceperley, U.S. patent 4,355,517 (1982).

<sup>9</sup>A. T. A. M. De Waele, J. Sound Vib. 325, 974 (2009).

<sup>10</sup>W. C. Ward and W. G. W Swift, J. Acoust. Soc. Am. 95, 3671 (1994).

<sup>11</sup>R. Radebaugh and G. O’ Gallagher, Adv. Cryog. Eng. 51, 1919 (2006).

<sup>12</sup>A. M. Fusco, W. C. Ward, and G. W. Swift, J. Acoust. Soc. Am. 91, 2229 (1992).
