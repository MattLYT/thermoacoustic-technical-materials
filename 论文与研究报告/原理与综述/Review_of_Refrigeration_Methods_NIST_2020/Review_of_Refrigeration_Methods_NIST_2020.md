---
record_category: "论文与研究报告/原理与综述"
source_id: "nist:2020:radebaugh-review-refrigeration-methods"
title: "Review of Refrigeration Methods"
authors:
  - "Ray Radebaugh"
year: 2020
institution:
  - "National Institute of Standards and Technology"
engineering_type: "低温制冷方法综述"
function_boundary: "制冷方法、COP、比功率与温区适用性比较"
drive_chain: "覆盖 Stirling、GM、脉管、JT 与大型液化循环"
phase_control: "综述各类低温制冷机的调相与回热器"
topology: "综述低温制冷机与液化系统"
evidence_grade: "NIST 书章投稿版 PDF；MinerU 全文转换"
source_status: "MinerU-full-pdf"
source_path: "相关资料/论文与研究报告/原理与综述/Review_of_Refrigeration_Methods_NIST_2020/source/Review_of_Refrigeration_Methods_NIST_2020.pdf"
mineru_method: "extract --model pipeline --language en"
---

Submitted to:   
Handbook of Superconducting   
Materials, D. A. Cardwell and D.   
Larbelestier, eds., Taylor and Francis Books, 2020

# F1. Review of Refrigeration Methods<sup></sup>

Ray Radebaugh

Applied Chemicals and Materials Division National Institute of Standards and Technology Boulder, Colorado 80305 USA

## F1.1 INTRODUCTION

Superconductors require cooling to cryogenic temperatures $( T < 1 2 0 \mathrm { ~ K ~ } )$ for all practical applications. Cryogenic fluids (cryogens) are commonly used for cooling superconductors in laboratory environments, but most practical applications require the use of closed-cycle refrigerators, of which smaller units are commonly referred to as cryocoolers. Cryogens may be used along with cryocoolers in some large-scale applications of superconductors to provide for the heat transfer between the superconductor and the cold tip of the cryocooler. Such hybrid systems also provide redundancy for higher reliability. Cryocoolers are required for a wide variety of applications, and the number of applications keeps expanding as improvements to cryocoolers are made. One of the earliest applications, and one that appeared about 60 years ago, was for cooling infrared sensors to about 80 K for night vision capability of the military. By 1998 over 125,000 Stirling cryocoolers for this tactical military application had been produced (Dunmire, 1998). Today the total number probably exceeds 200,000. Refrigeration powers vary from about 0.15 W to 1.75 W at 80 K. Recently, advances in infrared sensors designed for operation at higher temperatures have led to a surge of research and development efforts on miniature 150 K cryocoolers. Such temperatures are too high for current superconductors, but some of the miniature technology can be adapted for lower temperature applications.

In the past two decades or so, the desire for night vision surveillance and missile detection from satellites has prompted much research on improved cryocoolers to meet the very stringent requirements for space use. Each application has a unique set of requirements that have led to many recent improvements in cryocoolers. Many applications of superconductors have not reached the marketplace yet because of some disadvantages associated with cryocoolers. The major disadvantages of cryocoolers are listed in Table F1.1, but only a few of those may be of any concern for any specific application. For satellite applications, all the disadvantages listed in Table F1.1 are of major concern, but the cost can be much higher than that for commercial applications before it becomes a concern. Some space-qualified cryocoolers can cost \$1.0M or more, but they are an enabling component in many missions costing tens to hundreds of million dollars. Lifetimes of 10 years are now standard requirements for most space applications, and several cryocoolers have operated continuously in space for more than 10 years (Ross, 2016). Lifetime goals of 2 to 5 years have become common for most terrestrial commercial applications. Cryocooler input power, which is usually related to size and weight, can be a hindrance for some space, remote, or portable applications. The ratio of net refrigeration power $\dot { Q } _ { c }$ to input power $\dot { W } _ { 0 }$ is called the coefficient of performance (COP) and the reciprocal is called the specific power $P _ { s } .$ Both are often related to the ideal, reversible refrigeration process in which the COP is given by the Carnot value of

$$
\mathrm { C O P } _ { C a r n o t } = \frac { \dot { Q } _ { c } } { \dot { W } _ { 0 , i d e a l } } = \frac { T _ { c } } { T _ { h } - T _ { c } } ,\tag{1}
$$

where $\dot { W } _ { 0 , i d e a l }$ is the power input for an ideal, reversible system and $T _ { c }$ and $T _ { h }$ are the cold and hot temperatures. The actual COP of a real refrigerator can be expressed as a percentage of the Carnot COP and is called the second law efficiency. Figure F1.1 shows how the specific power varies with temperature for various second-law efficiencies of cryocoolers. Until recently efficiencies of 3 to 10% of Carnot were typical of these small cryocoolers operating near 80 K, whereas efficiencies of 15 to 25% of Carnot are now possible. At 4 K efficiencies range from less than 1 % of Carnot for small (<2 W) cryocoolers to about 35 % of Carnot for very large refrigeration and liquefaction plants.

Figure F1.1

Since 1925, with passage of the Helium Conservation Act, the U. S. government has played a significant role in the production, refining and storage of helium. But in 1996, Congress directed the helium business to be privatized and the federal reserves to be sold at market prices to pay off the \$1.4 billion debt of the program. After a 2013 congressional action modified the 1996 act, the life of the helium reserve has been extended under government control. However, the price of helium, including liquid helium, has risen sharply since 1996 and it is in short supply. Consequently, many small applications that had been using liquid helium are now turning to the use of commercial 4 K Gifford-McMahon (GM) or pulse tube cryocoolers, which became available since about 1995. Though these cryocoolers use helium as the working fluid, they are closed cycle devices that do not require replenishment of the fluid. They can be used to cool a superconducting device attached directly to the cold tip, or they can be used to condense the boiloff vapor from a liquid helium vessel, such as with magnetic resonance imaging (MRI) systems for maintaining the submerged superconducting magnet at 4.2 K. Refrigeration powers for small commercial 4 K cryocoolers range from about 0.1 W to

1.5 W with input powers ranging from 1 to 12 kW. More than 40,000 4 K GM cryocoolers have been sold as of 2015 (Xu, 2015).

Larger 4 K refrigerators or liquefiers are used for cooling the superconducting magnets or superconducting rf cavities of particle accelerators. These refrigerators or liquefiers use the Claude cycle in which the helium working fluid is precooled by expansion in either piston or turbine expanders, with final cooling and liquefaction occurring by expansion through a Joule-Thomson valve. Such systems may also be used for liquefying helium gas collected from boiloff in laboratories using liquid helium in many experiments.

After a brief discussion on the use of cryogens for cooling superconductors, this section reviews the principles of the various types of cryocoolers or refrigeration systems and discusses some of the latest advances that have made them more suitable for many applications. Other reviews of cryocoolers have been given by (Radebaugh, 2009), (Radebaugh, 2000), (Ravex, 1998), and (Walker and Bingham, 1994). Section F2 reviews in more detail the modeling and advances in pulse tube cryocoolers. Temperatures down to about 50 mK are required for some very sensitive transition edge superconducting (TES) detectors of single photons or for quantum effect experiments with superconductors. Such temperatures are achieved by use of adiabatic demagnetization refrigerators (ADRs) or <sup>3</sup>He/<sup>4</sup>He dilution refrigerators. The refrigerators discussed in this chapter are used for precooling these millikelvin refrigerators to about 4 K. This chapter does not discuss ADRs or dilution refrigerators, but detailed descriptions are found in the book by Pobell (Pobell, 2007).

## F1.2 COOLING WITH CRYOGENIC FLUIDS

## F1.2.1 Properties of Cryogenic Fluids

Table F1.2

In most cases, liquid nitrogen is used for cooling high temperature superconductors and liquid helium is used for cooling low temperature superconductors. The properties of several cryogenic fluids (cryogens) are listed in Table F1.2. Except where indicated, these properties are taken from NIST Standard Reference Database 23 (Lemmon et al., 2010). Liquid neon may occasionally be used for achieving temperatures around 25 to 30 K, although it is much more expensive even than liquid helium. In the simplest of experiments, a sample to be cooled is immersed in the cryogen at atmospheric pressure. Cooling comes from the heat of vaporization of the liquid. This heat of vaporization increases with the normal boiling point. When temperatures above the normal boiling point are required, the cold vapor is often used for cooling the sample. Table F1.2 also lists the sensible heat, or the enthalpy change, of the vapor in warming from the normal boiling point to 300 K. The heat absorbed by the vapor when warming to any temperature is proportional to the temperature rise for an ideal gas, since for an ideal gas the specific heat is independent of temperature. A boiling cryogen provides excellent temperature stability even in the presence of large fluctuating heat loads. With power applications of superconductors, a boiling cryogen may be necessary for peak shaving as well as providing some lead time in the case of a cryocooler failure.

## F1.2.2 Cryostat Construction

The cooling of small samples to the temperature of the normal boiling point of a cryogen is most conveniently done by using the storage dewar as the cryostat. The sample is simply immersed in the cryogen as shown by the first example in Figure F1.2. For the case of samples too large to fit down the neck of a storage dewar, it becomes necessary to construct a special cryostat. The advantage of the immersion cryostat is its simplicity. Its disadvantage is that it does not allow for any temperature variation of the sample.

Figure F1.2

The center and right illustrations in Figure F1.2 show two methods used to cool samples while allowing them to be heated with an electrical heater to some temperature higher than the normal boiling point of the cryogen. Both cases provide a semi-weak thermal link between the sample and the cryogenic liquid. The use of a low-pressure exchange gas (usually helium) allows the thermal conductance of the link to be varied by changing the pressure of the exchange gas. For sufficiently low pressures the thermal conductivity of a gas becomes proportional to the pressure.

For cooling very sensitive superconducting electronics, such as Superconducting Quantum Interference Devices (SQUIDs), metal dewars may need to be replaced with non-metallic dewars made with fiberglass-epoxy to reduce magnetic field noise associated with metal dewars. In some large-scale applications of superconductors, the cryogen may be pumped around the superconducting system as part of the cryogenic refrigerator or with a separate cryogenic pump. Balshaw (1998), Claudet (1998), and Van Sciver (2012) provide further information on the design and use of cryostats for use with cryogens.

## F1.3 TYPES OF CRYOCOOLERS

Figure F1.3

Figure F1.4

Figures F1.3 and F1.4 show the six types of cryocoolers in common use today. The Joule-Thomson (JT), Brayton, and Claude cryocoolers or refrigerators shown in Figure F1.3 are of the recuperative type in which the working fluid flows steadily in one direction, with steady low- and high-pressure lines, analogous to DC electrical systems. A reciprocating compressor uses inlet and outlet check valves to maintain the steady flow, whereas centrifugal compressors or screw compressors would not have such valves. Such compressors are oil lubricated for long life, so oil-removal equipment is placed in the compressor outlet to prevent oil from reaching the cold end and freezing. The recuperative heat exchangers transfer heat from one flow stream to the other across a solid wall separating the two flow streams. Recuperative heat exchangers with the high effectiveness needed for cryocoolers can be expensive to fabricate. The Claude cycle is a combination of the Brayton cycle with the addition of a final Joule-Thomson expansion stage for the liquefaction of the working fluid. It is commonly used in large helium liquefaction systems for cooling superconducting magnets and rf cavities in accelerators.

The three regenerative cycles shown in Figure F1.4 operate with an oscillating flow and an oscillating pressure, analogous to AC electrical systems. Average pressures range from about 1.5 MPa to 3 MPa, and the dynamic pressure amplitude is typically about 10 to 20 % of the average pressure. Frequencies vary from about 1 Hz for the Gifford-McMahon (GM) and some pulse tube cryocoolers to about 60 Hz for Stirling and some pulse tube cryocoolers. As shown in Figure F1.4, the oscillating pressure required for pulse tube cryocoolers can be generated either with a valveless reciprocating compressor like that of the Stirling cycle or with a standard refrigeration compressor combined with another set of valves to switch between the low and high pressure streams like that of the

GM cycle. The terms Stirling-type or GM-type are often used to describe the two types of pulse tube cryocoolers.

## F1.3.1 Recuperative Cycles

The steady pressure in these cryocoolers allows them to use large gas volumes anywhere in the system with little adverse thermodynamic effects except for larger radiation heat leaks if the additional volume is at the cold end. Thus, it is possible to “transport cold” to any number of distant locations after the gas has expanded and cooled. In addition, the cold head can be separated from the compressor by a large distance, which greatly reduces the electromagnetic interference (EMI) and vibration associated with the compressor. Oil removal equipment with its large gas volume can also be incorporated in these cryocoolers right after the compressor’s high-pressure outlet to remove any traces of oil from the high-pressure working gas before it is cooled in the heat exchanger. Unlike conventional refrigerators operating near ambient temperature, any oil in the working fluid will freeze at cryogenic temperatures and plug the system.

## F1.3.1.1 Joule-Thomson cryocoolers

Joule-Thomson (JT) cryocoolers produce cooling when the high-pressure gas expands through a flow impedance (orifice, valve, capillary, porous plug), often referred to as a JT valve. The expansion occurs with no heat input or production of work, which means the process occurs at a constant enthalpy. The heat input occurs after the expansion and is used to warm up the cold gas or to evaporate any liquid formed in the expansion process. In an ideal gas the enthalpy is independent of pressure for a constant temperature, but real gases experience an enthalpy change with pressure. Thus, cooling in a JT expansion occurs only with real gases and at temperatures below the inversion curve. Typically, nitrogen or argon are used in small 80 K JT coolers, but pressures of 20 MPa (200 bar) or more on the high-pressure side are needed to achieve reasonable cooling. Such high pressures are difficult to achieve and require special compressors with short lifetimes.

The main advantage of JT cryocoolers is the fact that there are no moving parts at the cold end. The cold end can be miniaturized and provide a very rapid cool-down. This rapid cool-down (a few seconds to reach 77 K) has made them the cooler of choice for cooling infrared sensors used in missile guidance systems. These coolers utilize a small cylinder pressurized to about 45 MPa with nitrogen or argon as the source of highpressure gas. In this open-cycle mode, cooling lasts for only a few minutes until the gas is depleted. Figure F1.5 shows a typical JT cryocooler used for missile guidance. Miniature finned tubing is used for the heat exchanger. An explosive valve is used to start the flow of gas from the high-pressure bottle, and after flowing through the cooler, the gas is vented to the atmosphere.

Figure F1.5

A disadvantage of the JT cryocooler is the susceptibility to plugging by moisture of the very small orifice. Another disadvantage is the low efficiency when used in a closed cycle mode. Compressor efficiencies are very low when compressing to such high pressures. Temperatures below about 70 K require the use of a second compressor and a neon or hydrogen working fluid for precooling the second stage.

Recent advances in JT cryocoolers have been associated with the use of mixed refrigerants as the working fluid rather than pure gases. The use of mixed refrigerants was first proposed in 1936 for the liquefaction of natural gas [see discussion by

Radebaugh (1997)], but it was not used extensively for this purpose until the last 30 or 40 years. It is commonly referred to as the mixed refrigerant cascade (MRC) cycle. The use of small JT coolers with mixed refrigerants for cooling infrared sensors was first developed under classified programs in the Soviet Union during the 1970s and 1980s. Such work was first discussed in the open literature by Little (1988). Missimer (1994), Little (1988), and Radebaugh (1995) review the use of mixed refrigerants in JT cryocoolers. Typically, higher boiling-point components, such as methane, ethane, and propane can be added to nitrogen to make the mixture behave more like a real gas over the entire temperature range. The larger enthalpy changes result in increased cooling powers and efficiencies with pressures (about 2.5 MPa) that can be achieved in conventional compressors used for domestic or commercial refrigeration. Some research is currently underway pertaining to the solubility of oil in various mixtures and the freezing point of mixtures. Marquardt et al. (1998) discuss the optimization of gas mixtures for a given temperature range and show how a mixed refrigerant JT cryocooler can be used for a cryogenic catheter only 3 mm in diameter. Such miniature systems could also be used for cooling superconducting electronic devices. The gas mixture in these systems undergoes boiling and condensing heat transfer in the heat exchanger that contributes to its high efficiency. Commercial mixed-refrigerant JT cryocoolers are being used for the cooling of high-purity germanium nuclide detectors to about 80 K and have shown lifetimes greater than 10 years in continuous operation. Figure F1.6 shows an example of one of these nuclide detector systems that use the mixed refrigerant JT process, sometimes referred to as the Kleemenko cycle (Little, 1988).

Small helium JT cryocoolers precooled to 10-18 K by a regenerative cryocooler have recently received much attention for cooling detectors to temperatures of 2-7 K. Such systems have provided 4 K in space for detector cooling in astronomical missions. The James Webb Space Telescope will be using a helium JT stage precooled to 18 K by a three-stage pulse tube cryocooler to cool the Mid-Infrared Instrument MIRI to 7 K (Ross, 2016). Similar systems can be used for temperatures down to about 2 K by use of subatmospheric pressure on the intake side of the JT system. Such low temperatures are useful for cooling superconducting single photon detectors (Kotsubo et al., 2017).

## F1.3.1.2 Brayton cryocoolers

Cooling occurs in Bryton cryocoolers as the expanding gas does work against a piston or turbine. Figure F1.3 shows a reciprocating expansion engine for this purpose, but an expansion turbine supported on gas bearings is more commonly used to give high reliability. According to the first law of thermodynamics, the heat absorbed with an ideal gas in the Brayton cycle is equal to the work produced. This process is then more efficient than the JT cycle, and it does not require as high a pressure ratio. A challenge for small Brayton cryocoolers is the fabrication of miniature turboexpanders that maintain high expansion efficiency. Turbine diameters of about 6 mm on shafts of 3 mm diameter spinning at 2000 to 5000 rev/s are typical in systems reviewed by McCormick et al. (1997) for use in space applications of cooled infrared sensors. Centrifugal compressors providing a pressure ratio of about 1.6 with a low-side pressure of 0.1 MPa are used with these systems. A similar system used on the Hubble Space Telescope provides 8 W of cooling at 70 K with an efficiency of 8 % of Carnot (Swift et al., 2008).

It has operated continuously since 2002. The working fluid used in the turbo-Brayton cryocoolers is usually neon when operating above 35 K, but helium is required for lower temperatures.

An advantage of the Brayton cryocooler is the very low vibration associated with rotating parts in a system with turboexpanders and centrifugal compressors. This low vibration is often required with sensitive telescopes in satellite applications, such as with the Hubble telescope. The expansion engine gives the Brayton cycle high efficiency over a wide temperature range, although the efficiency is not as high as some Stirling and pulse tube cryocoolers at temperatures above about 50 K. The low-pressure operation of the miniature Brayton systems requires relatively large and expensive heat exchangers. The expansion turbines are also expensive to fabricate, especially in very small sizes.

## F1.3.1.3 Claude-Cycle Liquefiers and Refrigeration Systems

The presence of a liquid phase in an expansion engine can damage the engine, so the Brayton cycle is seldom used for liquefaction of gases. Gas liquefaction is usually carried out in the Claude cycle, as shown in figure F1.3, in which liquefaction takes place in a final JT expansion after the gas is precooled with one or more expansion engines. The efficiency of the JT expansion into the two-phase region is rather high, so little efficiency is lost when substituting the JT valve for a final-stage expansion engine. Most large-scale air, hydrogen, and helium gas liquefaction is carried out using the Claude cycle, but with many more stages of expansion engines than are shown in figure F1.3. The Collins helium liquefier, which was developed in 1947 and became the first commercially available helium liquefier, uses two reciprocating expansion engines for precooling the helium before it enters the JT expansion valve to be liquefied. The liquefaction rate can vary from about 190 L/day to 400 L/day without liquid nitrogen precooling, depending on the size of the compressor. The use of liquid nitrogen precooling will about double the liquefaction rate. This liquefier and larger ones that use gas-bearing turboexpanders are designed to provide a source of liquid helium that can be used for cooling at some other site. It is useful to note that the evaporation of 1.38 L/hr of liquid helium at atmospheric pressure can provide 1 W of cooling at 4.2 K. To conserve helium, these helium liquefiers are usually combined with helium recovery and purification systems to capture the boiloff helium gas from experiments and return it to the liquefier. The second-law efficiencies of these Claude helium liquefiers without liquid nitrogen precooling are in the range of 5-8 % of Carnot for the Collins type to about 12 % of Carnot for somewhat larger systems with turbine expanders. Figure F1.7 illustrates how the input power and operating cost (electrical power only) of various types of helium liquefiers varies with liquefaction rate.

Figure F1.7

For very large systems, the Claude cycle is usually integrated with the experimental apparatus, so the returning helium boiloff gas is returned through the heat exchangers to increase efficiency. Examples are the large helium refrigeration plants for accelerators with superconducting magnets, of which the plant for the Large Hadron Collider (LHC) is the world’s largest. It consists of eight refrigerators with a combined capacity of 144 kW of refrigeration at 4.5 K and 19.2 kW at 1.8 K (Delikaris and Tavian, 2014). The total input power is about 40 MW, which gives a second-law efficiency of 31 % of Carnot for a 295 K ambient temperature. These very large helium refrigerators employ 8 to 10 stages of expansion turbines to yield these high efficiencies.

## F1.3.2 Regenerative Cryocoolers

Regenerative cryocoolers operate with oscillating pressures and mass flows in the cold head. The working fluid is almost always helium gas. The oscillating pressure can be generated with a valveless compressor (pressure oscillator), as shown in figure F1.4 for the Stirling, or with valves that switch the cold head between a low- and high-pressure source, as shown for the Gifford-McMahon (GM) cryocooler. In the latter case, a conventional compressor with inlet and outlet valves (or a scroll compressor) is used to generate the high- and low-pressure sources. These compressors are commercial oillubricated air conditioning or refrigeration compressors modified for use with helium gas, and they are used primarily for commercial applications of cryocoolers where low cost is very important. Oil removal equipment can be placed in the high-pressure line where there is no pressure oscillation. The use of valves greatly reduces the efficiency of the system. Pulse tube cryocoolers can use either source of pressure oscillations, as indicated in figure F1.4.

The main heat exchanger in regenerative cycles is called a regenerator. In a regenerator, incoming hot gas transfers heat to the matrix of the regenerator, where the heat is stored for a half cycle in the heat capacity of the matrix. In the second half of the cycle the returning cold gas, flowing in the opposite direction through the same channel, absorbs heat from the matrix and returns the matrix to its original temperature before the cycle is repeated. Very high surface areas for enhanced heat transfer are easily achieved in regenerators by using stacked fine-mesh screen or packed spheres.

## F1.3.2.1 Stirling cryocoolers

The Stirling cycle was invented in 1815 by Robert Stirling for use as a prime mover. Though used occasionally in the latter part of that century as a refrigerator, it was not until the middle of the $2 0 ^ { \mathrm { t h } }$ century that it was first used to liquefy air and soon thereafter for cooling infrared sensors for tactical military applications. They cannot provide the very fast cooldown times of JT cryocoolers, so they are not used on missile guidance systems. The long history of the Stirling cryocooler in cooling infrared equipment has resulted in the development of models tailored specifically to that application that are manufactured by several manufacturers. The refrigeration powers of these models range from 0.15 to 1.75 W, which is also appropriate for many superconducting electronic applications, though issues of reliability and EMI are important issues that must be considered.

A pressure oscillation by itself in a system would simply cause the temperature to oscillate and produce no refrigeration. In the Stirling cryocooler the second moving component, the displacer, is required to separate the heating and cooling effects by causing motion of the gas in the proper phase relationship with the pressure oscillation. When the displacer in figure F1.4(a) is moved downward, the helium gas is displaced to the warm end of the system through the regenerator. The piston in the compressor then compresses the gas, and the heat of compression is removed by heat exchange with the ambient. Next the displacer is moved up to displace the gas through the regenerator to the cold end of the system. The piston then expands the gas, now located at the cold end, and the cooled gas absorbs heat from the sample before the displacer forces the gas back to the warm end through the regenerator. In practice the gas volume in the regenerator is large enough that any gas element only traverses part way through the regenerator before it reverses direction. Each gas element absorbs heat near the cold end and rejects it closer to the hot end. Stirling cryocoolers usually have the regenerator inside the displacer instead of external as shown in figure F1.4(a). The resulting single cylinder provides a convenient cold finger.

In practice, motion of the piston and the displacer are nearly sinusoidal, and they must be oil free to prevent oil freezing in the cold end. The correct phasing occurs when the volume variation in the cold expansion space leads the volume variation in the warm compression space by about 90. With this condition, the mass flow or volume flow through the regenerator is approximately in phase with the pressure. In analogy with AC electrical systems, real power flows only when current and voltage are in phase with each other. The moving displacer reversibly extracts net work from the gas at the cold end and transmits it to the warm end where it contributes some to the compression work. In an ideal system, with isothermal compression and expansion and a perfect regenerator, the process is reversible. Thus, the coefficient of performance COP for the ideal Stirling refrigerator is the same as the Carnot COP given previously by Eq. (1).

Figure F1.8 shows the four sizes of Stirling cryocoolers that are currently used for military tactical applications of infrared sensors. All except the smallest cooler in this figure are split systems in which the cold finger can be located a short distance from the compressor. The refrigeration powers listed for each cooler are for a temperature of about 77 to 80 K, except the 1.75 W system, which is for a temperature of 67 K. They have efficiencies of about 10 % of Carnot. All the coolers shown in figure F1.8 use linear drive motors and dual-opposed pistons to reduce vibration. The linear drive reduces side forces between the piston and the cylinder and the Mean-Time-To-Failure (MTTF) is at least 4000 hours, with some recent systems achieving times of over 10,000 hrs. The displacer is driven pneumatically with the oscillating pressure in the system, and because there is only one displacer it gives rise to some vibration. The cost of a single unit ranges from about \$5000 to \$10,000. Efforts are currently underway to increase the MTTF of these Stirling cryocoolers since they are usually the least reliable component in an infrared system.

The development of cryocoolers for space applications has led to greatly improved reliabilities, and a MTTF of 10 years is now usually specified for these applications. The Stirling cooler was first used in these space applications after flexure bearings were developed for supporting the piston and displacers in their respective cylinders with little or no contact in a clearance gap of about 15 m (Davey, 1990). Figure F1.9 shows an example of a flexure bearing geometry and how they are used in a compressor. These flexure-supported Stirling cryocoolers were initially very expensive, but advances in manufacturing have reduced the price to where these flexures are now available for use in compressors in tactical and commercial applications. Such compressors are also used for pulse tube cryocoolers.

## F1.3.2.2 Gifford-McMahon cryocoolers

Gifford-McMahon (GM) cryocoolers use oil-lubricated compressors made by the millions for the refrigeration or air conditioning industry. The oil removal equipment is placed in the high-pressure line ahead of the switching valve that generates the oscillating pressure. The compressor can be located as much as several meters from the switching

Figure F1.10

valves because pressures in these connecting lines do not oscillate. Figure F1.10 shows a simple drawing of the layout and typical lifetimes of components. The GM cycle was first developed in the late 1950s (Gifford and McMahon, 1959) and (McMahon and Gifford, 1960) and is described in more detail elsewhere (Ravex, 1998) and (Walker and Bingham, 1994). These cryocoolers are most commonly used in two-stage 15 K versions for cryopumps in the semiconductor fabrication industry. Thousands per year are made worldwide with costs for one unit ranging from about \$10,000 to \$20,000. The GM cryocooler also was used for cooling shields to 10 to 15 K in MRI systems to reduce the boil-off rate of liquid helium, but since 1995 4 K GM cryocoolers became available and are now used to provide zero boiloff of the liquid helium in MRI systems. Single-stage units for temperatures above about 30 K are somewhat cheaper. Refrigeration powers at 80 K generally range from about 10 W to 600 W with input powers ranging from about 800 W to 14 kW. The oil-lubricated compressors have lifetimes of at least 5 years, but the adsorber cartridge for oil removal must be replaced once every year or two. Replacement of seals on the displacer must be performed about once every year.

Most of the recent developments in GM cryocoolers have involved the use of high heat capacity regenerator materials to reach temperatures of 4 K in two stages without the aid of a Joule-Thomson stage. Rare-earth materials that undergo magnetic transitions in the range of 4 to 20 K are generally used for these new regenerators. With lead spheres replaced by Er<sub>3</sub>Ni spheres in the second stage, a minimum temperature of 4.5 K was achieved with a two-stage GM cryocooler (Kuriyama et al., 1990). The development in Japan of the technique (Sahashi et al., 1990) to produce high quality spheres of many different rare-earth materials greatly aided the advancement of 4 K GM refrigerators.

The cost of these materials significantly increases the cost of the 4 K GM cryocoolers. Commercial 4 K GM cryocoolers are now available in sizes ranging from 0.1 W to 2 W of refrigeration at 4.2 K.

## F1.3.2.3 Pulse tube cryocoolers

The moving displacer in the Stirling and Gifford-McMahon cryocoolers has several disadvantages. It is a source of vibration, has a limited lifetime, and contributes to axial heat conduction as well as to a shuttle heat loss. In the pulse tube cryocooler, shown in figure F1.4(b), the displacer is eliminated. The proper gas motion in phase with the pressure is achieved through use of an orifice, along with a reservoir volume to store the gas during a half cycle. The reservoir volume is large enough that negligible pressure oscillation occurs in it during the oscillating flow. The pressure drop across the orifice is simply the dynamic pressure in the pulse tube, and the flow through the orifice is in phase with the dynamic pressure. This flow through the orifice causes the gas motion at the cold end to be similar to that which occurs in a Stirling or GM cryocooler due to the displacer motion. However, the flow is in phase with the pressure at the orifice rather than in the regenerator, which is the ideal case achieved with a displacer. The oscillating flow through the orifice separates the heating and cooling effects just as the displacer does for the Stirling and Gifford-McMahon refrigerators. The orifice pulse tube refrigerator (OPTR) operates ideally with adiabatic compression and expansion in the pulse tube. Thus, for a given frequency there is a lower limit on the diameter of the pulse tube to maintain adiabatic processes. The four steps in the cycle are as follows. (1) The piston moves down to compress the gas (helium) in the pulse tube. (2) Because this heated, compressed gas is at a higher pressure than the average in the reservoir, it flows through the orifice into the reservoir and exchanges heat with the ambient surrounding through the heat exchanger at the warm end of the pulse tube. The flow stops when the pressure in the pulse tube is reduced to the average pressure. (3) The piston moves up and expands the gas adiabatically in the pulse tube. (4) This cold, low-pressure gas in the pulse tube is forced past the cold end by the gas flow from the reservoir into the pulse tube through the orifice. The flow stops when the pressure in the pulse tube increases to the average pressure. The cycle then repeats. More detailed analyses of pulse tube cryocooler thermodynamics are given in section F2 and by (Radebaugh, 2003).

One function of the pulse tube is to insulate the processes at its two ends. That is, it must be large enough that gas flowing from either the warm end or the cold end traverses only part way through the pulse tube before flow is reversed. Gas in the middle portion of the pulse tube never leaves the pulse tube and forms a temperature gradient that insulates the two ends. Roughly speaking, the gas in the pulse tube is divided into three segments, with the middle segment acting like a displacer but consisting of gas rather than a solid material. For this gas plug to effectively insulate the two ends of the pulse tube, turbulence in the pulse tube must be minimized. Thus, flow straightening at the two ends is crucial to the successful operation of the pulse tube refrigerator.

Pulse tube refrigerators were invented by (Gifford and Longsworth, 1964) in the mid-1960s, but that type was different than what is shown in figure F1.4(b) and only reached a low temperature of 124 K. In 1984 (Mikulin et al., 1984) introduced the concept of an orifice to the original pulse tube cryocooler and reached 105 K. In 1985 (Radebaugh et al., 1986) changed the location of the orifice to that shown in figure F1.4(b) and reached

60 K. Further improvements since then have led to a low-temperature limit of about 20 K with one stage and 2 K with two stages (Radebaugh, 2000).

Figure F1.11

There are three different geometries that have been used with pulse tube cryocoolers as shown in figure F1.11. The inline arrangement is the most efficient because it requires no void space at the cold end to reverse the flow direction nor does it introduce turbulence into the pulse tube from the flow reversal. The disadvantage is the possible awkwardness associated with having the cold region located between the two warm ends. The most compact arrangement and the one most like the geometry of the Stirling cryocooler is the coaxial arrangement. That geometry has the potential problem of a mismatch of temperature profiles in the regenerator and in the pulse tube that would lead to steady heat flow between the two components and a reduced efficiency. However, that problem has been minimized, and a coaxial geometry was developed at NIST as an oxygen liquefier for NASA with an efficiency of 17 % of Carnot (Marquardt and Radebaugh, 2000).

The absence of a moving displacer in pulse tube cryocoolers gives them many potential advantages over Stirling or GM cryocolers. These advantages include higher reliability, lower cost, lower vibration, less EMI, and insensitivity to large side forces on the cold region. Disadvantages are difficulty in scaling to very small sizes (less than about 10 W input power) and the possibility of convective instabilities in the pulse tube when operated with the cold end up or horizontal in a gravity environment. Early pulse tube cryocoolers were not nearly as efficient as Stirling cryocoolers, but advances in the last twenty years and described in the next section have made Stirling-type pulse tube cryocoolers as efficient as Stirling cryocoolers. Efficiencies of about 24 % of Carnot at 80 K have been achieved (Wang, et al., 2015).

However, the pulse tube cryocooler has one intrinsic loss that prevents even the ideal case from having the Carnot COP. The PV work recovered by the displacer at the cold end of a Stirling or GM cryocooler is introduced back into the warm end of the regenerator by the opposite end of the displacer. That additional PV work input reduces the work required from the compressor. The gas motion in the pulse tube cold end gives a PV diagram like that in the Stirling or GM cryocooler, but that motion produces only a potential to do real work, which is called a Gibbs free energy flow or often referred to as acoustic power flow. Without the displacer, no real work is recovered and introduced back into the warm end. Instead the acoustic power is dissipated in the orifice. The expansion work at the displacer cold end gives rise to the $T _ { c }$ term in the numerator of equation (1), but the compression work reintroduced to the system at the warm end of the displacer gives rise to the $T _ { c }$ term in the denominator of equation (1). Since no work is recovered in the case of the pulse tube cryocooler, the ideal pulse tube COP is $T _ { c } / T _ { h }$ (Kittel, 1992). At 80 K the efficiency of the ideal pulse tube cryocooler is then reduced to 73 % of Carnot.

## F1.4 RECENT ADVANCES IN PULSE TUBE CRYOCOOLERS

## F1.4.1 Phase Shift Mechanisms

In regenerative cryocoolers, the optimum phase relationship between the pressure and the mass (or volume) flow is to have them in phase with each other near the center of the regenerator. With such a phase relationship flow and thermal losses in the regenerator are minimized, and the compressor swept volume is minimized. However, the resistive nature of the orifice causes the flow at that location to be in phase with the pressure. Flow in the regenerator then leads the pressure by as much as 30 to 50 degrees and causes greater regenerator losses because of the larger amplitude of flow for the same PV power flow. The double inlet system and the inertance tube are two methods to adjust the phase between the flow and pressure in a beneficial direction.

## F1.4.1.1 Double inlet (secondary orifice)

In 1990 (Zhu et al., 1990) introduced the concept of a secondary orifice to the OPTR in which the secondary orifice allows a small fraction (about 10 %) of the gas to travel directly between the compressor and the warm end of the pulse tube, thereby bypassing the regenerator, as shown in figure F1.12. They called this the double-inlet pulse tube refrigerator. This bypass flow is used to compress and expand the portion of the gas in the warm end of the pulse tube that always remains at the warm temperature. The bypass flow reduces the flow through the regenerator, thereby reducing the regenerator loss. An alternative explanation shows that the secondary orifice causes the flow at the warm end of the pulse tube to lag the pressure, which is the desired phase shift.

Though the introduction of the secondary orifice usually led to increased efficiencies compared to the OPTR, it also introduced a problem. Performance of the double-inlet pulse tube refrigerator was not always reproducible, and sometimes the cold end temperature would slowly oscillate by several degrees with periods of several minutes or more. This erratic behavior has been attributed (Gedeon, 1997) to DC flow that can sometimes occur around the loop formed by the regenerator, pulse tube, and secondary orifice.

## F1.4.1.2 Inertance tube

The inertia of the oscillating mass flow in regenerative systems causes a component of the pressure drop to lead the flow by 90. This inertance effect is analogous to that of an inductance in electrical systems where the voltage leads the current by 90. Because of the resistive component of pressure drop and the compliance (analogous to capacitance) due to void volume, the actual phase shift will always be less than 90. In fact, in the pulse tube and regenerator the compliance effect dominates at normal operating frequencies of 1 to 60 Hz. A component with an optimized geometry to maximize the inertance effect is required to bring about the desired phase shift of any significance. This component is known as the inertance tube (Radebaugh, 1997 and Radebaugh, 2000) and is shown in figure F1.12. It is a long thin tube of about 1 to 2 m in length. In practice, the required resistive component can be incorporated into the inertance tube, so the primary orifice can be eliminated unless some control is desired. With an inertance tube the flow at the warm end of the pulse tube lags the pressure instead of being in phase as with only the primary orifice. If the phase shift is large enough to cause the flow and pressure to be in phase in the regenerator, then no secondary orifice is required and DC flow is eliminated. The maximum phase shift in the inertance tube increases with the flow in the system. Small pulse tubes of only a few watts of refrigeration at 80 K usually need the addition of the secondary orifice to obtain enough of a phase shift for improved performance.

## F1.4.1.3 Warm Expander or Displacer

An expander can be used at the warm end of the pulse tube to provide an optimum phase shift, even for small pulse tubes (Matsubara and Miyake, 1988). Such an expander can be actively driven to vary the phase shifting or it can be designed for passive operation at a fixed frequency and phase shift by incorporating dissipation (Sobol and Grossman, 2016). With a warm expander, the back side of the piston is at the average pressure (reservoir volume) and the expansion work must be dissipated unless there is a complex mechanical or electrical connection to the compressor to return the work. Without that connection, the ideal efficiency is still $T _ { c } / T _ { h }$ . However, if the piston back side is connected to the regenerator warm end, it becomes a warm displacer that can return the expansion work to the system. The warm-displacer pulse tube cryocooler can then achieve the Carnot COP given by equation (1). The introduction of the warm expander or displacer introduces a second moving part just like that of the Stirling or GM cryocoolers, except in this case all moving parts are at ambient temperature and can even be placed in one housing using dual opposed pistons and flexure bearings for both the compressor and warm displacer. (Wang et al., 2015).

## F1.4.2 Small helium liquefiers

Soon after the introduction of commercial rare-earth regenerator materials with high heat capacities around 10 K were introduced around 1990, their use in two-stage GMtype pulse tube cryocoolers allowed temperatures below 4 K to be achieved (Wang, Thummes, and Heiden, 1997). Commercial versions are now available with refrigeration powers ranging from 0.2 W to 2 W at 4 K with significant refrigeration also available at temperatures around 50 K. These cryocoolers along with 4 K GM cryocoolers are frequently used for cooling superconducting electronics and small magnets to 4 K without the use of liquid helium. In cases where liquid helium is still desired for its improved heat transfer, and for experiments that require extremely low vibration, small helium liquefiers are now commercially available that make use of the 4 K GM-type pulse tube cryocooler. These liquefiers make use of precooling the incoming helium gas along the length of the regenerator to enhance the liquefaction rate beyond what is possible when using only the cold tip to do all the cooling (Wang, 2008 and Wang, 2009). Liquefaction rates of about 20 L/day are typical, as shown in figure F1.7. If the incoming helium gas is pressurized to about its critical pressure (220 kPa), the liquefaction rate can be increased further to about 35 L/day (Rillo et al., 2015).

## F1.4.3 Examples of pulse tube cryocoolers

Figure F1.13 shows the first commercial pulse tube cryocooler (a GM-type), which was introduced in Japan in 1993, and made available worldwide later in similar versions. It utilizes the U-tube geometry and is driven with a Gifford-McMahon compressor requiring about 800 W of input power. A rotary valve provides the pressure oscillation and is located some distance from the cold head to reduce EMI from the valve motor. The oscillating frequency is about 1 Hz. This pulse tube provides 2 W of refrigeration at 77 K. Figure F1.14 shows a commercial two-stage 4 K pulse tube cryocooler (GM-type) that provides 0.5 W at 4.2 K with about 5 kW of input power. Figure F1.15 shows an example of a space-qualified pulse tube cryocooler (Stirling-type) designed for cooling

Figure F1.14

Figure F1.15

infrared sensors. It can provide 7 W of cooling at 80 K with 125 W of compressor input power at 300 K (15 % of Carnot) (Raab and Tward, 2010). Several have flown in space with some logging more than 10 years of continuous operation with no degradation (Raab and Tward, 2010 and Ross, 2016). It uses the latest technology in flexure-bearing compressors to reduce the size and mass of the compressor. The cold head is an inline arrangement, and the reservoir volume is an annular volume outside the left linear compressor. The total mass is about 4.3 kg. Commercial Stirling-type pulse tube cryocoolers are available with refrigeration powers up to 1 kW at 80 K.

## F1.5 CRYOCOOLER COMPARISONS

The typical operating region for various cryocoolers is shown in figure F1.16. Some of these boundaries have not been fully explored, especially the larger sizes for pulse tube refrigerators. The same chart shows the operating regions for various applications, including most of the superconducting applications. Figure F1.17 compares efficiencies of various types of cryocoolers operating at 77-80 K as a function of the input power to the compressor. The data are mostly from the period of 1990 to 2016 and include highefficiency R&D coolers of each type. The highest efficiency commercial Stirling cryocooler (29.5 % of Carnot with 1.2 kW of refrigeration power at 80 K) uses a rotary motor and crankshaft, known as a kinematic version. The highest efficiency cryocooler (30 % of Carnot) represented in the graph in figure F1.17 is an R&D integral Stirling cryocooler that uses linear motors (Penswick et al., 2014). Though not shown in figure F1.17, the highest efficiency achieved with any cryocooler is 41 % of Carnot with 20 kW of refrigeration power at 77 K in a very large Stirling cryocooler (Dros, 1965). The

Figure F1.16

highest efficiency pulse tube cryocooler (24 % of Carnot) is from 2015 and incorporates a warm displacer (Wang et al., 2015). The next highest efficiency pulse tube cryocooler (22 % of Carnot) uses an inertance tube and is from 2010 (Hu et al., 2010). The 2015 survey of tactical cryocoolers (Yi and Yuan, 2015) reviewed 35 different models. Two facts emerge from this figure. The first is that efficiencies improve with larger sizes and the second is that pulse tube refrigerators with Stirling-like (valveless) compressors are as efficient as Stirling cryocoolers. One noticeable exception to the trend of higher efficiencies with higher powers is that of pulse tube cryocoolers, as indicated in figure F1.17. The decrease in efficiency of pulse tube cryocoolers for refrigeration powers higher than about 100 W is attributed to flow inhomogeneities in both the regenerator and pulse tube (Dietrich, Yang, and Thummes, 2007). The efficiencies of mixed-gas JT cryocoolers increases rapidly as the temperature is increased from 80 to 90 K, whereas the efficiency of the other cryocoolers changes very little with temperature over this temperature range. The efficiencies of these small cryocoolers has increased considerably since 1974 when the survey by (Strobridge, 1974) showed an average efficiency of about 2 % of Carnot at a refrigeration power of 1 W.

## F1.6 INTEGRATION OF SUPERCONDUCTORS WITH CRYOCOOLERS

One of the more challenging problems in cooling superconductors with cryocoolers is that of reducing the associated vibration and EMI caused by the motor and other moving parts. The problem is most serious with SQUID devices because of their extreme sensitivity to magnetic fields and to vibration in the earth’s magnetic field. Thus, we concentrate this section on these applications. In the case of power applications of superconductors, the major concerns are efficiency, cost, reliability, and how to distribute the cold from a cold head to a large superconducting device. In that case, the cryocooler is often used to liquefy the boiloff from a cryogenic bath in which the superconductor is immersed.

To reduce noise in a superconducting device caused by the cryocooler, the following points should be considered: (1) selection of cryocooler type, (2) selection of materials, (3) distance between cryocooler and superconductor, (4) mounting platforms, (5) shielding, (6) thermal damping, and (7) signal processing. Of the various cryocooler types, the Joule-Thomson and pulse tube cryocoolers are good choices because they have no cold moving parts. Because the pulse tube cryocooler uses oscillating pressures, the temperature of the cold tip will also oscillate slightly at the operating frequency.

A combination of techniques such as shielding of the Stirling compressor, use of dual, opposed pistons and displacers, and separation of SQUIDs from the cold finger by flexible copper braids was used for a high T<sub>c</sub> SQUID heart scanner cooled with a pair of Stirling cryocoolers (Blom et al., 1999). A hybrid JT/GM cryocooler has been used for cooling a 61-channel magnetoencephalography (MEG) system (Sata et al., 1997). In this case the final JT stage separates the SQUIDs from the moving displacer in the GM refrigerator. The noise of the system was about 4 pT peak-to-peak, which was reduced further by digital filtering. More recently, (Takeda et al., 2009) modified a commercial MEG system by using a 4 K GM cryocooler to reliquefy the boiloff helium and have it return to the dewar by gravity through a transfer line that isolates the cryocooler vibration from the MEG system. They achieved a noise level below $1 0 \mathrm { f T / H z } ^ { 1 / 2 }$ for 2-40 Hz, which is comparable to the noise level with the GM cryocooler turned off. With a careful selection of materials and a separate support for a high $T _ { c }$ SQUID magnetometer in a metal shield, (Lienerth et al., 2001) used a pulse tube cooler for the system and achieved a white noise level above 1 kHz of 35 fT/Hz<sup>1/2</sup> compared with 45 fT/Hz<sup>1/2</sup> for liquid nitrogen cooling. In fact, the white noise level for cooling with the pulse tube was less than with liquid nitrogen cooling for all frequencies above about 2 Hz. However, the pulse tube produced sharp peaks in the noise spectra at the operating frequency of 4.6 Hz and its harmonics. Earlier measurements in the same laboratory compared vibration and field noise spectra at the cold tips of a mixed-gas JT cooler and a pulse tube cooler (Hohmann et al., 1999). These comparisons of vibration and field noise are shown in figures F1.18 and F1.19. Except for the sharp peaks in the noise spectra at the operating frequency and its harmonics, the pulse tube cooler produced less noise than the JT cooler and less noise than with liquid nitrogen cooling at frequencies above about 40 Hz. The broad vibration and noise peaks in the frequency range from 100 to 500 Hz with the JT cooler may be caused by turbulent fluid flow.

Figure F1.18

Figure F1.19

The vibration forces on the cold head mounting flange of commercial 4 K GM and pulse tube cryocoolers were compared by (Wang and Gifford, 2001). The pulse tube peak force was 3.6 N whereas that of the GM cryocooler was 178 N, due to the displacer motion. The amplitude of vibration at the 4 K cold tip of the pulse tube was about 52 µm in the Z-direction. Later measurements showed vibration amplitudes at the 4 K cold tip of about 10 µm for both pulse tube and GM commercial cryocoolers (Mauritsen et al., 2009). These vibration amplitudes can be reduced to about 200 nm in the Z-direction and 20 nm in the x- and y-directions by the method shown in figure F1.20 (Ikushima et al., 2008).

Temperature oscillations at the cold tip of a 4 K GM or GM pulse tube cryocooler operating at about 1 Hz can be about 0.5 K because of the low heat capacity of the metals at such low temperatures (Li et al., 1997), but various means have been employed to reduce such temperature oscillations an order of magnitude or more (Li et al., 1997 and Mauritsen et al., 2009). There is still much more work to be done regarding some of the other cryocooler disadvantages, especially cost, reliability, and in some cases efficiency, to help superconductors to make it to the marketplace more easily.

## REFERENCES

Balshaw N H (1998) Cryostats. In: Handbook of Applied Superconductivity, Vol 1 (Seeber B, ed), pp 763-793. Bristol and Philadelphia: Institute of Physics Publishing.

Blom C J H A, ter Brake H J M, Holland H J, Rijpma A P, and Rogalla H (1999) Construction and tests of a high-T<sub>c</sub> SQUID-based heart scanner cooled by small Stirling cryocoolers. Cryocoolers 10 pp 837-846. New York: Plenum Press.

Claudet G (1998) Bath cryostats for superfluid helium cooling. In: Handbook of Applied Superconductivity, Vol 1 (Seeber B, ed), pp 795-800. Bristol and Philadelphia: Institute of Physics Publishing.

Davey G (1990) Review of the Oxford cryocooler. Adv. in Cryogenic Engineering, Vol. 35 pp 1423-1430. New York: Plenum Press.

Delikaris D and Tavian L (2014) The LHC cryogenic system and operational experience from the first three years. J. Cryo. Super. Soc. Jpn. 49:590-600.

Dietrich M, Yang L W, and Thummes G (2007) High-power Stirling-type pulse tube cryocooler: Observation and reduction of regenerator temperature inhomogeneities. Cryogenics 47: 306-314.

Dros A A (1965) Large capacity industrial Stirling machine. Adv. in Cryogenic Engineering, vol. 10 pp 7-12. New York: Plenum Press.

Dunmire H (1998) U. S. Army cryocooler status update. Military and commercial applications for low cost cryocoolers, San Diego Jan. ’98, Arlington, VA: Electronic Industries Association (EIA).

Gedeon D (1997) DC gas flows in Stirling and pulse tube refrigerators. Cryocoolers 9 pp 385-392. New York: Plenum Press.

Gifford W E and Longsworth R C (1964) Pulse tube refrigeration. Trans. of the ASME, Journal of Engineering for Industry, paper No. 63-WA-290, August

Gifford W E and McMahon H O (1959) A new refrigeration process. Proc. Tenth International Congress of Refrigeration, Vol. 1, Copenhagen, Denmark.

Hohmann R, Lienerth C, Zhang Y, Bousack H, Thummes G, and Heiden C (1999) Comparison of low noise cooling performance of a Joule-Thomson cooler and a pulse tube cooler using a HT SQUID. IEEE Trans. Appl. Supercond., Vol. 9, pp 3688-3691.

Hu J Y, Dai W, Luo E C, Wang X T, and Huang Y (2010) Development of high efficiency Stirling-type pulse tube cryocoolers. Cryogenics 50:603-607.

Ikushima Y, Li R, Tomaru T, Sato N, Suzuki T, Haruyama T, Shintomi T, and Yamamoto A (2008) Ultra-low-vibration pulse-tube cryocooler system—cooling capacity and vibration. Cryogenics 48:406-412.

Kittel P (1992) Ideal orifice pulse tube refrigerator performance. Cryogenics 32:843-844.

Kotsubo V, Radebaugh R, Henderschott P, Bonczyski M, Wilson W, Nam S W, and Ullom J M (2017) Compact 2.2 K cooling system for superconducting nanowire single photon detectors. IEEE Trans. on Appl. Supercond., Vol. 27 (4), 9500405.

Kuriyama T, Hakamada R, Nakagome H, Tokai Y, Sahashi M, Li R, Yoshida O, Matsumoto K, and Hashimoto T (1990) High efficiency two-stage GM refrigerator with magnetic material in the liquid helium temperature region. Adv. in Cryogenic Engineering, Vol. 35 pp 1261-1269. New York: Plenum Press.

Lemmon E W, Huber M L, and McLinden M O (2010) NIST standard reference database 23, NIST Reference Fluid Thermodynamic and Transport Properties (REFPROP) version 10.0. Gaithersburg, MD: NIST.

Li R, Onishi A, Satoh T, and Kanazawa Y (1997) Temperature stabilization on cold stage of 4 K G-M cryocooler. Cryocoolers 9 pp 765-771. New York: Plenum Press.

Lienerth C, Thummes G, and Heiden C (2001) Progress in low noise cooling performance of a pulse-tube cooler for HT-SQUID operation. IEEE Trans. Appl. Supercond., Vol. 11, pp 812-816.

Little W A (1988) Recent developments in Joule-Thomson cooling: gases, coolers, and compressors. Proc. 5<sup>th</sup> International Conference on Cryocoolers, pp 3-11. Monterey, CA. Marquardt E D and Radebaugh R (2000) Pulse tube oxygen liquefier. Adv. in Cryogenic Engineering, Vol. 45 pp 457-464. New York: Plenum Press.

Marquardt E D, Radebaugh R, and Dobak J (1998) A cryogenic catheter for treating heart arrhythmia. Adv. in Cryogenic Engineering, Vol. 43, pp 903-910. New York: Plenum Press.

Matsubara Y, and Miyake A (1988) Alternative methods of orifice pulse tube refrigerator. Cryocoolers 5 pp 127-135. Monterey.

Mauritsen L, Snow D, Woidtke A, Chase M, and Henslee I (2009) Low vibration, low thermal fluctuation system for pulse tube and Gifford-McMahon cryocoolers. Cryocoolers 15 pp 581-585. Boulder: ICC Press.

McCormick J A, Swift W L, and Sixsmith H (1997) Progress on the development of miniature turbomachines for low-capacity reverse-Brayton cryocoolers. Cryocoolers 9 pp 475-483. New York: Plenum Press.

McMahon H O and Gifford W E (1960) A new low-temperature gas expansion cycle. Adv. in Cryogenic Engineering, Vol. 5 pp 354-372. New York: Plenum Press.

Mikulin E I, Tarasov A A, and Shkrebyonock M P (1984) Low temperature expansion pulse tubes. Adv. in Cryogenic Engineering, Vol. 29 pp 629-637. New York: Plenum Press.

Missimer D J (1994) Auto-Refrigerating Cascade (ARC) systems – an overview. Tenth Intersociety Cryogenic Symposium, (AIChE Spring National Meeting, March).

Pobell F (2007) Matter and methods at low temperatures. Berlin Heidelberg: Springer-Verlag.

Penswick L, Olan R W, Williford I, Drancey S, and Buchholz G (2014) High-capacity and efficiency Stirling cycle cryocooler. Cryocoolers 18 pp 155-162. Boulder: ICC Press.

Raab J and Tward E (2010) Northrop Grumman Aerospace Systems cryocooler overview. Cryogenics 50:572-581.

Radebaugh R (1995) Recent developments in cryocoolers. Proc. 19<sup>th</sup> International Congress of Refrigeration, pp 973-989. The Hague, Netherlands.

Radebaugh R (1997) Advances in cryocoolers. Proc. ICEC16/ICMC, pp 33-44. Oxford: Elsevier Science.

Radebaugh R (2000) Development of the pulse tube refrigerator as an efficient and reliable cryocooler. Proc. Institute of Refrigeration (London) Vol 96: pp 11-31.

Radebaugh R (2003) Thermodynamics of regenerative refrigerators. In: Generation of low temperature and it’s application (Ohtsuka T and Ishizaki Y, eds), pp 1-20. Kamakura: Shonan Tech Center.

Radebaugh R (2009) Cryocoolers: the state of the art and recent developments. J. Phys.: Condens. Matter 21:164219.

Radebaugh R, Zimmerman J, Smith D R, and Louie B (1986) A comparison of three types of pulse tube refrigerators: New methods for reaching 60 K. Adv. in Cryogenic Engineering, Vol. 31 pp 779-789. New York: Plenum Press.

Ravex A (1998) Small cryocoolers. In: Handbook of Applied Superconductivity, Vol 1 (Seeber B, ed), pp 721-746. Bristol and Philadelphia: Institute of Physics Publishing.

Rillo C, Gabal M, Lozano M P, et al. (2015) Enhancement of the liquefaction rate in small-scale helium liquefiers working near and above the critical point. Phys Rev. Applied 3: 051001.

Ross, R.G. Jr. (2016) Refrigeration systems for achieving cryogenic temperatures. In: Low temperature materials and mechanisms (Bar-Cohen Y, ed), pp 109-181. Boca Raton, FL: CRC Press.

Sahashi M, Tokai Y, Kuriyama T, Nakagome H, Li R, Ogawa M, and Hashimoto T (1990) New magnetic material R<sub>3</sub>T system with extremely large heat capacities used as

heat regenerators. Adv. in Cryogenic Engineering, Vol. 35 pp 1175-1182. New York: Plenum Press.

Sata K, Fujimoto S, Fukui N, Haraguchi E, Kido T, Nishiguchi K, and Kang Y-M (1997) Development of SQUID based systems cooled by GM/JT cryocoolers Proc. ICEC16/ICMC pp 1173-1176. Oxford: Elsevier Science.

Sobol S and Grossman G (2016) Diaphragm-type mechanism for passive phase shifting in miniature PT cryocooler. Cryocoolers 19 pp 219-228. Boulder: ICC Press.

Strobridge T R (1974) Cryogenic refrigerators – An updated survey. NBS Technical Note 655 (Washington: National Bureau of Standards)

Swift W L, Dolan, F X, and Zagarola M V (2008) The NICMOS cooling system—5 years of successful on-orbit operation. Adv. In Cryogenic Engineering, Vol. 53 pp 799- 806. Melville, NY: American Institute of Physics.

Takeda T, Okamoto M, Atsuda K, Katagiri K (2009) Performance of a helium circulation system for a MEG. Cryogenics 49:144-150.

Van Sciver S (2012) Helium Cryogenics. Berlin Heidelberg: Springer-Verlag.

Walker G and Bingham E R (1994) Low-Capacity Cryogenic Refrigeration. Oxford: Oxford University Press.

Wang C, Thummes G, and Heiden C (1997) A two stage pulse tube cryocooler operating below 4 K. Cryogenics 37: 159-164.

Wang C and Gifford P E (2001) Performance characteristics of a 4 K pulse tube in current applications. Cryocoolers 11 pp 205-212. New York: Kluwer Academic/Plenum Publishers.

Wang C (2008) Intermediate cooling from pulse tube and regenerator in a 4 K pulse tube cryocooler. Cryogenics 48: 154-159.

Wang C (2009) Small scale helium liquefaction system. J. of Phys. Conf. Series 150 012053.

Wang X, Zhang Y, Li H, Dai W, Chen S, Lei G, and Luo E (2015) A high efficiency hybrid Stirling-pulse tube cryocooler. AIP Advances 5:037127.

Xu M (2015) Private communication.

Yi S and Yuan W K (2015) Tactical cryocooler vendor survey: 2015. Aerospace report no. TOR-2015-02442.

Zhu S, Wu P, and Chen Z (1990) Double inlet pulse tube refrigerators: an important improvement. Cryogenics 30:514-520.

Table F1.1. Cryocooler disadvantages.

• Reliability

• Efficiency

Size and weight

• Vibration

• Electromagnetic Interference (EMI)

• Heat rejection

Cost

Table F1.2. Properties of several cryogenic fluids
<table><tr><td>Property</td><td>3He</td><td> $^ { 4 } \mathrm { H e }$ </td><td>Para  $\underline { { \mathrm { H } _ { 2 } } }$ </td><td>Normal  $\mathrm { H } _ { 2 }$ </td><td> $\mathrm { N e }$ </td><td> ${ \bf N } _ { 2 }$ </td><td>Ar</td></tr><tr><td>Molecular Weight (g/mol)</td><td>3.017</td><td>4.003</td><td>2.016</td><td>2.016</td><td>20.18</td><td>28.01</td><td>39.95</td></tr><tr><td>Normal Boiling Point, NBP, (K)</td><td>3.191</td><td>4.222</td><td>20.28</td><td>20.39</td><td>27.10</td><td>77.36</td><td>87.30</td></tr><tr><td>Triple Point Temperature (K)</td><td></td><td> $\mathrm { T } _ { \lambda } = 2 . 1 7 7$ </td><td>13.80</td><td>13.96</td><td>24.56</td><td>63.15</td><td>83.81</td></tr><tr><td>Triple Point Pressure (kPa)</td><td></td><td> $\mathrm { P } _ { \lambda } = 5 . 0 4 2$ </td><td>7.042</td><td>7.20</td><td>43.38</td><td>12.46</td><td>68.91</td></tr><tr><td>Critical Temperature (K)</td><td>3.324</td><td>5.195</td><td>32.94</td><td>33.19</td><td>44.49</td><td>126.19</td><td>150.69</td></tr><tr><td>Critical Pressure (MPa)</td><td>0.117</td><td>0.2275</td><td>1.284</td><td>1.315</td><td>2.679</td><td>3.396</td><td>4.863</td></tr><tr><td>Liquid Density at NBP (g/cm³)</td><td>0.05844</td><td>0.1249</td><td>0.07080</td><td>0.0708</td><td>1.207</td><td>0.8061</td><td>1.395</td></tr><tr><td>Gas Density at 0 °C &amp; 1 atm (kg/m³)</td><td>0.134</td><td>0.1785</td><td>0.08988</td><td>0.08988</td><td>0.8998</td><td>1.250</td><td>1.784</td></tr><tr><td>Heat of Vaporization at NBP (J/g)</td><td>7.714</td><td>20.72</td><td>445.5</td><td>445.6</td><td>85.75</td><td>199.18</td><td>161.14</td></tr><tr><td>Sensible Heat from NBP to 300 K</td><td></td><td>1543.3</td><td>4010.5</td><td>3510.8</td><td>255.3</td><td>234.03</td><td>112.28</td></tr><tr><td colspan="8">(J/g)</td></tr><tr><td>Heat of Fusion (J/g)</td><td></td><td></td><td>58.23</td><td>58.23</td><td>16.6</td><td>25.5</td><td>27.8</td></tr><tr><td>Heat of Vaporization per Volume of Liquid at NBP (J/cm³)</td><td>0.4508</td><td>2.588</td><td>31.54</td><td>31.55</td><td>103.5</td><td>160.6</td><td>224.8</td></tr><tr><td>Sensible Heat per Volume of Liquid at NBP (J/cm³)</td><td></td><td>192.8</td><td>283.9</td><td>248.6</td><td>308.1</td><td>188.7</td><td>156.6</td></tr></table>

![](images/fee042ba013d121d0f729c23147c6e306a3230a2cc9fbbdc2d5fc85c1882c41a.jpg)

(c) Claude $\dag \dot { Q } _ { c } , T _ { c }$  
Figure F1.1. Specific power (input power/net refrigeration power) for refrigerators as a function of cold temperature and second law efficiency.  
![](images/73241051330f0bd730468583a41be7bcfab12e0072013b28c4683b8740ecfb69.jpg)

![](images/354c08ec1b22bad1a30c587c6a3eb05d5b5c0ebaffa6c8122f0b29c4354458f8.jpg)

![](images/795caa324be932651746f2a8c3a78c127043c321565109d90d86bf8d2bcb69b9.jpg)  
Semi-Weak Thermal Link

Figure F1.2. Use of cryogens for sample cooling.  
![](images/edbb89e5c50d2f1818efe4cde080dfff2f6843702efd6edde8e1cfdb8271ebcc.jpg)  
(a) Joule-Thomson

![](images/1ad8b6288d7e396f6fd252e754a0180a9bac46dc37fdbdcb3ec7767820524614.jpg)  
(b) Brayton

![](images/c2599010195dc1f7261ba9e937367ccfa8e3933f9bce71fb8ad1ba3b584b3912.jpg)  
Figure F1.3. Schematics of the most common recuperative cryocoolers.

![](images/64e2c8995bab001bf29d130bed3003ebc66d6cd3399ab57add225dc422df1b52.jpg)  
(a) Stirling  
(b) Pulse Tube

![](images/a2886d75e8780419ff653ad52ad569f71a4e140f6afd48f805185ef2c9aa0e74.jpg)  
(c) Gifford-McMahon  
Figure F1.4. Schematics of the most common regenerative cryocoolers.

![](images/0754af7fe1a828ef2d2c7bf0dc608447df811ba17339c0cd070d0df856056267.jpg)  
Figure F1.5. Open-cycle Joule-Thomson cryocooler for missile guidance.

![](images/e39146327b474e64cfdf184b25cbbd889a397e33a8065ebcf98632121a2161f8.jpg)  
Figure F1.6. Commercial 5 W at 80 K mixed-refrigerant JT (Kleemenko) cryocooler used for cooling high-purity germanium nuclide detectors.

![](images/53f896dc092d6299d20a252489276f8948c212017bdf4f47ebabf3450d92a304.jpg)

Figure F1.7. Input power and electrical operating cost for helium liquefiers of various liquefaction rates.  
![](images/56ae8a5d6fafccfad411f2658d39b1696b1d11e5625d44f7fd20c7e7963999c6.jpg)  
Figure F1.8. Four sizes of Stirling cryocoolers with dual-opposed linear compressors.

![](images/ede88e0c4d56635ab738e10fdf0ccce1eecd3ab951b849e54d0671c9984e1c34.jpg)  
Figure F1.9. Schematic of (a) linear compressor with (b) spiral flexure bearings.

![](images/609359d66625049ef855a527cc85be235ade98d5dfbcf1fe8fa91cec428ba924.jpg)  
Figure F1.10. Schematic of a Gifford-McMahon (GM) cryocooler showing parts of the cold head and compressor along with typical lifetime of components when operating continuously.

![](images/55863d33e9b2d835b969f53f719c873ea1c99370e9fac5e20f94725710d44b69.jpg)  
Figure F1.11. Three different geometries for pulse tube cryocoolerss.

![](images/a595011126896ec82e1f45f8c0741bf7b99ea0141ffe735592406b0000196bce.jpg)  
Figure F1.12. Schematic of pulse tube cryocooler with secondary orifice (double inlet) and inertance tube.

![](images/72f3ffda6384ce72a5e5ac9cfb5c22feb90dcd1ca55cd9a3c136b6a2b701fb14.jpg)  
Figure F1.13. First commercial pulse tube cryocooler, showing Gifford-McMahon compressor and rotary valve.

![](images/2228ae66ec7d515c06c48ef1e027339f33cece4ef5942746e71e330c31b48609.jpg)  
Figure F1.14. Commercial two-stage GM-type pulse tube cryocooler that provides 0.5 W at 4.2 K.

![](images/129a8f27d5ec042060e0e1fd91f956bf3a2face033d3e6806f5bf78ce34e0838.jpg)  
Figure F1.15. High-efficiency Stirling-type pulse tube cryocooler for space applications.

![](images/ce633051a528e2fea900ff1899a877e70ee9096234768c61fd81b2e26e21d1d5.jpg)  
Figure F1.16. Applications and operating regions for various cryocoolers.

![](images/55180e2a21c8634a2bf5df7e8667690c3b8809649a3236a1cb8e065a414ef719.jpg)  
Figure F1.17. Efficiencies of various types of cryocoolers at 80 K.

![](images/a8773e9d7780cf7aa678563354cac1f4f7428302d434c7bc48419362d03954dd.jpg)

Figure F1.18. Vibration at the cold tip of a pulse tube cryocooler and a mixed-gas Joule-Thomson cryocooler. Reproduced from Hohmann et al, 1999 by permission of IEEE.  
![](images/7e52172b50e22ccaa9eef9c3d27adfbf27257f721df928c98f9227bcfbe12473.jpg)  
Figure F1.19. Field noise in a SQUID caused by various cooling methods. Reproduced from Hohmann et al, 1999 by permission of IEEE.

![](images/2f03c5d239bda957ce69fb2fd8f672ec842f8837e322b4479b43e4951c1c2aa4.jpg)  
Figure F1.20. Sample vibration damping arrangement to achieve 200 nm vibration amplitude in the z-direction and 20 nm in the x- and y-directions. After Ikushima et al, 2008.
