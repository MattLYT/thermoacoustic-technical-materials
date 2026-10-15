---
title: Performance analysis and verification of a novel high temperature difference heat pump · MinerU全文
record_role: machine-transcription
parse_method: MinerU
source_sha256: 194b6167223f55117069079d4ce7f54bbf5228b3c1cb2a3d6d4c2cb47fbad1ad
source_pages: 10
---

# PERFORMANCE ANALYSIS AND VERIFICATION OF A NOVEL HIGHTEMPERATURE DIFFERENCE HEAT PUMP

Tor-Martin Tveit, R&D Manager, Single-Phase Power AS, Nye Vakås vei 80,

NO-1395 Hvalstad, Norway;

Arne Høeg, CTO, Single-Phase Power AS, Nye Vakås vei 80, NO-1395 Hvalstad, Norway;

Abstract: This paper present the performance of a novel high temperature difference heat pump. The SPP HighLift engine series SPP 4-106 is designed for heat pumping applications with sink temperatures up to $20 0 ^ { \circ } \mathsf C$ . As the working medium of the process is a gas and do not undergo any phase changes during the process - it is a single-phase process - the HighLift heat pumps have very few restrictions on source- and sink temperatures. In addition, the process will quickly find a new equilibrium state with changing temperatures, meaning that the process is very robust with respect to e.g. large and sudden changes in inlet temperatures. The results shows for example that the heat pump can deliver over 400 kW of heat at $1 0 5 ^ { \circ } \mathsf { C } \ ( \neg 2 2 0 \ ^ { \circ } \mathsf { F } )$ with a temperature lift of almost 80 K with a ${ \mathsf { C O P } } _ { \mathsf { h } }$ at 2.0. In many applications both the heating and cooling can be useful. Combining the delivered heat and cooling gives an overall COP of between 3.1 at the same conditions.

Key Words: very high temperature heat pump, high temperature lift, combined heating and cooling

## 1 INTRODUCTION

This paper present the performance of a novel high temperature difference heat pump. The performance is measured at a commercial installation of the heat pump, operating with a heat source at around $\boldsymbol { 2 5 ^ { \circ } \mathrm { C } }$ and a heat sink at $10 5 ^ { \circ } \mathrm { C }$ . The process is based on keeping the working medium in a single phase. This means that the heat pump does not have many of the limits on temperatures the more common heat pump processes have.

We will show that the heat pump at full load has an overall COP (both cooling and heating) of more than 3 for a temperature lift of 78 K, delivering heat at 105 °C (\~220 °F). Another version of the heat pump is operating at a temperature difference of 120 K, but is not discussed in this paper.

The first sections give an description of the heat pump, the thermodynamic process, the process layout and the instrumentation. The next sections presents the results from testing the heat pump at different loads and the comparison between the measured parameters and simulated values. The discussion and conclusions are given in the last section.

## 2 DESCRIPTION OF THE HEAT PUMP, SPP HIGHLIFT 4-106-series

The technology behind the heat pump is based on the Stirling cycle. The engine uses less than 2 kg of helium (refrigerant gas R-704) as its working medium. Helium makes the heat pumps suitable for any application, as it is an environmentally friendly working medium that is nontoxic, non-flammable and with a global warming potential (GWP) of 0. The heat pumps have a rated output of 400-500 kW heat, and are basically double-acting piston compressors with integrated heat exchangers, mounted on a skid, and connected by flanges to the external energy systems.

The SPP HighLift engine series SPP 4-106 is designed for heat pumping applications with sink temperatures up to $20 0 ^ { \circ } \mathsf { C }$ Many aspects of the design resemble large ship diesel engine designs. A detailed description of the process components is given by the others in the paper [Høeg A., et. al 2009]. The heat pump is a four-cylinder double-acting engine with four gas circuits, with a normal crankcase with crankshaft, oil lubricated bearings and crossheads, connected by two-piece connecting rods. The process components, i.e. cylinders and heat exchanger components, differ from the ones found in diesel engines. Separate process cylinders with double-acting pistons, are bolted onto the crosshead liners, and the pistons are connected to the crossheads with piston rod, retained by hydraulically tightened nuts. The cylinder volumes are connected by heat exchanger packages, bolted on to the sides of the process cylinders. Linear gas seals around the piston rods prevent gas and oil leakage between the gas circuits and the engine block. The engine/heat pump’s gas circuits are pressurized with helium. The figure below shows photos of two commercial installations of the heat pump.

![[mu_194b6167_b20b5418f21a5d27012e.jpg]]  
(a) Installation at the dairy plant TINE Byrkjelo

![[mu_194b6167_1e65bb89e25210a60230.jpg]]  
(b) Installation at the dairy plant TINE Frya  
Figure 1: Photos of two commercial installations of the HighLift heat pump

The heat pumps have separate subsystems for oil lubrication and cooling, working medium handling and control, diagnostics and logging.

## 2.1 The thermodynamic process and implementation

The heat pump is divided into a hot- and a cold side. There is a heat storage placed between these two sides. When the gas is in the hot side of the engine it is being compressed, resulting in a higher gas temperature. Heat is then transferred to the hot water (sink) at a high temperature. Then the gas is moved to the cold side of the engine heat is transferred to the heat storage. When the gas is in the cold side it is expanded, resulting in an even lower temperature. Heat is then transferred to the gas from the cold water (source) at a low temperature. When the gas is moved back to the hot side, it is heated by the heat storage. The figure below shows an infrared image of one of the heat exchanger packages on the engine during operation.

![[mu_194b6167_944b90c8263877f08f3a.jpg]]  
(a) Heat exchanger package: cold side on the left and the hot side on the right. Water inlets and outlets are respectively on the bottom and top side for both hot and cold side.

![[mu_194b6167_3823f214354ba7858d70.jpg]]  
(b) Infrared image of the heat exchanger package during operation. Temperatures are in degrees Celsius.  
Figure 2: Infrared image of the heat exchange package during operation, showing how the heat pump is divided into a hot- and cold side.

The cycle sketched above thus consists of heating and cooling of the working medium (a gas with no phase changes), as well as compression and expansion. The real Stirling cycle will have an elliptical shape in a pressure-volume diagram, of which an example is given in the figure below.

![[mu_194b6167_821b36bb3ccd21e06e7b.jpg]]  
Figure 3: The thermodynamic process. Heat is entering the heat pump at a low temperature when the pressure in the heat pump is low (1) and heat is rejected at a high temperature when the pressure is high (3). The heat storage stores the heat when the working medium is cooled (4) and gives it back to the process when the working medium is heated (2).

Heat transfer from the cold source and the hot sink is taking place when the gas is respectively expanded and compressed at an almost constant temperature (isothermal process). Heat transfer to and from the internal heat storage takes place when the volume is approximately constant (isochoric process). The internal heat storage - or regenerator - is the key to making the process feasible. The regenerator makes the temperature variations of the gas in the heat exchangers small, and thus considerably increasing the efficiency of the process.

As the working medium of the process is a gas and do not undergo any phase changes during the process - it is a single-phase process - the HighLift heat pumps have very few restrictions on source- and sink temperatures. In addition, the process will quickly find a new equilibrium state with changing temperatures, meaning that the process is very robust with respect to e.g. large and sudden changes in inlet temperatures.

## 2.2 Instrumentation and measurements

With respect to the performance of the heat pump, the most important process parameters are the inlet/outlet-temperatures of the external circuits, the mass flows of the external circuits and the electric power consumption of the main motor. The values for the process parameters are collected by various sensors and from the drive of the main motor (ABB ACS800) by an embedded control and acquisition system (NI cRIO-9073).

The temperatures are measured using thermocouples (type-J) connected to a thermocouple input module with built-in cold-junction compensation (NI-9213). The power consumption by the main motor is an analog signal (4-20 mA) sent by the drive and collected by a current input module (NI-9208). The mass flows are collected by electromagnetic flow meters (Euromag MUT2200EL) and they are also analog current signals collected by the same current input module.

The figure below shows the P&ID for the hot side of the heat pump.

![[mu_194b6167_3b8df0b3269d6f50fd37.jpg]]  
Figure 4: PI&D for the hot side of the heat pump with the most important sensors marked. The mass flow is divided internally in the heat pump into two parts which are heated in parallel by the two cylinder banks.

The symbol $\mathsf { m } _ { \mathsf { h c } }$ is the mass flow of the hot water circuit. The temperatures are ${ \sf T } _ { \sf i n } , { \sf T } _ { \sf o u t , b 1 3 }$ and T<sub>out,b24</sub>, which are respectively the input temperature, the outlet temperature after cylinder bank 13 and the outlet temperature after cylinder bank 24. The figure below shows the P&ID for the cold side of the heat pump.

![[mu_194b6167_95a3afd7595151f33fff.jpg]]  
Figure 5: PI&D for the cold side of the heat pump with the most important sensors marked. The mass flow is cooled in series by the two cylinder banks.

The main difference from the hot side is that the cold water is connected in series across the banks, whereas the hot water is connected in parallel.

## 3 MAIN ENERGY FLOWS

The main energy flows in the heat pump are the electric power driving the motor, W, and the heats transferred from the external circuits, $\ Q _ { \mathfrak { h } }$ and $\mathsf { Q } _ { \mathsf { c } } .$ The figure below shows a Sankey diagram of the process, which is to scale with the calculated and measured energies of the heat pump at full load.

![[mu_194b6167_9ee49fb442f710b36d90.jpg]]  
Figure 6: Sankey diagram of the main energy flows in the heat pump, the most important $\mathsf { \Omega } \mathsf { c } ,$ $w _ { \tt _ { E L } }$ and $\mathbf { Q _ { \Sigma \Sigma \Sigma \Sigma } } _ { \Sigma }$ refers respectively to the cooling, electricity consumption of the main motor and the heating.

The minor losses included in the Sankey diagram are the electric efficiency of the motor, heat from the oil pumps, internal thermal short circuits and thermal losses to the surroundings (convection and radiation).

## 4 DESCRIPTION OF THREE TEST RUN CASES

In order to validate the performance of the heat pump, the performance has been measured at three different loads. The measurements were made on SPP 4-106B at TINE meieriet Frya on Wednesday the 2nd of October, 2013. A time series of the load in percentage is shown in the figure below, where the analysed load cases are marked in different colours.

![[mu_194b6167_8ab3f8963dd05da94331.jpg]]  
Figure 7: Induced load time-series for SPP 4-106B on Wednesday the 2nd of October, 2013. The load is varied by changing the shaft speed and charge pressure of the working medium.

The periods are 10 minutes long. The load can be varied by changing the shaft speed or by changing the charge pressure of the working medium. Case #1 and #2 differs by the charge pressure and Case #2 and #3 differs by their shaft speed. The details are given in Table 1 in the next section. The load is also changed by the temperatures of the heat source and sink. The heat sink is hot water normally entering the heat pump at temperatures between 100 and $1 1 0 ^ { \circ } \mathsf { C }$ The heat source is water used to cool ammonia, which normally enters the heat pump at temperatures between 20 to $30 ^ { \circ } C$ The temperatures changes according to the heating and cooling load at the plant and are not controllable by the heat pump. The cases have been chosen so that the average external temperatures are approximately equal for all the cases. The time series for the external circuit for the three cases are shown in the figures below.

![[mu_194b6167_3abe5d4cb6242a4b243e.jpg]]  
(a) External hot side temperatures

![[mu_194b6167_85631bb92eecc7af8714.jpg]]  
(b) External cold side temperatures  
Figure 8: Time-series of the temperatures of the external circuits (heat sink and source) for SPP 4-106B on Wednesday the 2nd of October, 2013. The small temperature difference is due to the relatively large mass flow of water (55 kg/s and 15 kg/s respectively).

As there is an considerable thermal inertia in the heat pump due to heating and cooling of the process components, care has been taken to try to ensure that the periods include both increases and decreases of the temperatures, preferably in equal measures.

## 5 RESULTS FROM THE TEST RUNS WITH VARIOUS LOADS

The average process parameters for the three cases are show in the table below.

Table 1: Summary of parameters for the three cases. The values are average values based on data for 10 minutes of operation of each case.
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Loadpercentage</td><td rowspan=1 colspan=1> ${ \bar { \mathbf { I } } } _ { \mathsf { h } } \left( { \mathsf { C } } \right)$ </td><td rowspan=1 colspan=1> ${ \boldsymbol { \mathsf { T } } } _ { \mathsf { c } } \left( \mathsf { c } \right)$ </td><td rowspan=1 colspan=1>Ω (r/min)</td><td rowspan=1 colspan=1> ${ \textsf { P } } ( { \mathsf { b a r } } )$ </td><td rowspan=1 colspan=1> $\mathtt { c o p } _ { \mathfrak { h } }$ </td><td rowspan=1 colspan=1> $\mathbf { Q } _ { \mathsf { h } } \left( \mathsf { k } \mathbf { W } \right)$ </td><td rowspan=1 colspan=1> $\mathsf { Q } _ { \mathsf { c } } \left( \mathsf { k } \mathsf { W } \right)$ </td><td rowspan=1 colspan=1>W (kW)</td></tr><tr><td rowspan=1 colspan=1>Case #1</td><td rowspan=1 colspan=1>54%</td><td rowspan=1 colspan=1>106</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>630</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>217</td><td rowspan=1 colspan=1>119</td><td rowspan=1 colspan=1>108</td></tr><tr><td rowspan=1 colspan=1>Case #2</td><td rowspan=1 colspan=1>84%</td><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>628</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>351</td><td rowspan=1 colspan=1>204</td><td rowspan=1 colspan=1>157</td></tr><tr><td rowspan=1 colspan=1>Case #3</td><td rowspan=1 colspan=1>100%</td><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>751</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>408</td><td rowspan=1 colspan=1>215</td><td rowspan=1 colspan=1>203</td></tr></table>

where $\mathsf { C O P } _ { \mathsf { h } }$ is defined as $\sf Q _ { h } / \sf W$ and Ω is the shaft speed. In many applications both the heating and cooling can be useful, combining the delivered heat and cooling gives an overall COP of between 3.1 and 3.5.

The sample rate for the measurements is 5 s, which corresponds to 120 samples for each case. The figure below shows a more detailed picture of the performance.

![[mu_194b6167_07a6a652cd07f50a0963.jpg]]

![[mu_194b6167_4406a8a622c2f56302f8.jpg]]

![[mu_194b6167_59d8c3449b64b50b2e47.jpg]]

![[mu_194b6167_355b62f9e53a59bf577c.jpg]]

![[mu_194b6167_21f83cb81ab03fc67e9e.jpg]]

![[mu_194b6167_c31c6cd18c36aa470b1b.jpg]]

![[mu_194b6167_3a84c658bba80e5746c6.jpg]]  
Figure 9: Measurements for the three cases. The graphs on the left show the time series of the delivered heating, cooling and electric power, $\mathbf { Q } _ { \mathrm { h } } , \mathbf { Q } _ { \mathrm { c } }$ and W respectively. The graphs on the right shows the distribution of the calculated $\mathtt { c o P } _ { \mathtt { h } }$ for the cases based on the measurements.

The variations in the heat load and electric power is due to the changes in the temperatures of the external circuits, which correspondingly also explains the variations in $\mathsf { C O P } _ { \mathsf { h } }$

## 6 COMPARISON OF THE RESULTS WITH SIMULATIONS

During the development of the process a simulation model of the engine was developed and refined as the design evolved. The simulation model was made in Sage, which is a software package specially designed to simulate Stirling engines. Sage is developed by David Gedeon [Gedeon, 2009]. The development and use of the simulation model is described in detail in a previous paper by the authors, [Tveit, et.al., 2009].

The simulation model takes into account certain losses, e.g. gas friction losses in the tube heat exchangers, but not the mechanical losses and heat losses by convection and radiation of the exposed surfaces

The three cases are simulated and some of the results are shown in the figure below.

![[mu_194b6167_991b52ac3b7db2e4eeae.jpg]]  
(a)

![[mu_194b6167_a104ddfc288b42363766.jpg]]  
(b)  
Figure 10: Comparison of the measured and simulated values for the heat delivery and $\mathtt { c o p } _ { \mathfrak { n } }$ of the three cases. The measured values are in blue and the simulated in orange.

The calculated estimates of the losses in the heat pump varies between 10-20 kW, depending on the shaft speed and charge pressure. The difference in electric power input between the measured and simulated values for the three cases varies from 9 to 19 kW.

In addition to the losses not included in the model, the main source of the difference between the measured and simulated values are the simplification that only the lower circuits of the engine has been simulated. There is a slight difference between the processes above and below the pistons due to the movement of the pistons, area of the piston rod and volume differences due to the mechanical design.

## DISCUSSION AND CONCLUSIONS

The analysis of the measurements shows that the heat pump can deliver heat at a temperature lift well beyond the more traditional heat pump processes. The coefficient of performance is high enough to make the heat pump interesting for many applications, especially where it is possible to utilise both the heating and cooling.

The difference between the simulated and measured values are close to the estimated losses. This supports the measurements and loss calculations and gives confidence in the results. There are many sources of uncertainties in the measurements. For example in the calculations of the heat to and from the heat sink and source. The mass flow of water in the external hot circuit is very high compared to the temperature difference over the heat pump. This means that the measurements are very sensitive to the accuracy of the temperature measurements. An error of 0.1 degree Kelvin will for instance result in a calculated error of over 20 $\mathsf { k W } _ { \mathsf { t h } }$ . A lot of resources has been put into the calibration of the measurements of the temperature difference, as well as the measurements of the mass flows. The measurements of both the mass flow and temperature differences have been calibrated and extensively tested with other measurement equipment, consequently reducing the uncertainties.

## REFERENCES

Gedeon D., 2009, "Sage User’s Guide, Stirling, Pulse-Tube and Low-T Cooler Model Classes", Gedeon Associates

Tveit T.-M., Høeg A., and Asphjell T.-A., 2009, "A simulation based interactive multi-criterion strategy for optimising stirling-engine designs", The 14th International Stirling Engine Conference, Groningen, The Netherlands.

Høeg A., Tveit T.-M., and Asphjell T.-A., 2009, "The development of a double-acting stirling lab engine for low temperature heat utilisation", The 14th International Stirling Engine Conference, Groningen, The Netherlands.

Senft J., 1996, "An Introduction to Low Temperature Differential Stirling Engines", Moriya Press
