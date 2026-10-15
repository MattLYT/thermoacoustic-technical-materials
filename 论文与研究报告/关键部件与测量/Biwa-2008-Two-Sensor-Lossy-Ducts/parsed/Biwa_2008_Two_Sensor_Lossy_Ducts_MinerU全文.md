---
title: Experimental verification of a two-sensor acoustic intensity measurement in lossy ducts · MinerU全文
record_role: machine-transcription
parse_method: MinerU
source_sha256: 00b178faa92ee4f1d2370fce9747105cbdcdeab944280b3fb9278dd48787cff7
source_pages: 7
---

# Experimental verification of a two-sensor acoustic intensity measurement in lossy ducts

Tetsushi Biwa

Department of Mechanical Systems and Design, Tohoku University, Sendai 980-0013, Japan

Yusuke Tashiro and Hiroshi Nomura

Department of Crystalline Materials Science, Nagoya University, Nagoya 464-8603, Japan

Yuki Ueda

Tokyo University ofAgriculture and Technology, Koganei, Tokyo 184-8588, Japan

Taichi Yazaki

Department of Physics, Aichi University of Education, Kariya 448-8542, Japan

!Received 16 January 2008; revised 2 June 2008; accepted 5 June 2008"

Two-sensor method proposed by Fusco et al. #“Two-sensor power measurements in lossy ducts,” J. Acoust. Soc. Am. 91, 2229–2235 !1992"\$ is a novel technique that determines acoustic intensity of a gas column in a wide duct from measurements of pressure based on the boundary layer approximation. For further development of this method, its validity is experimentally tested through comparison with the direct method measuring the pressure and the velocity simultaneously, and its formulation is modified to include the narrow duct range where the duct radius is smaller than the viscous boundary layer thickness of the gas. It is shown that the modified two-sensor method enables quick and accurate evaluation of the acoustic intensity seamlessly from narrow to wide duct ranges. © 2008 Acoustical Society of America. #DOI: 10.1121/1.2953311\$

PACS number!s": 43.58.Fm, 43.20.Ye #RR\$

Pages: 1584–1590

## I. INTRODUCTION

Acoustic intensity I represents a time-averaged energy flux accompanied by oscillations of pressure and velocity of a gas. For a sound wave in a duct, the acoustic intensity I is expressed by

$$
\begin{array} { r } { I = \langle { P V } \rangle { } = \frac { 1 } { 2 } \operatorname { R e } [ \widetilde { p } v ] , } \end{array}\tag{!1"}
$$

where $P = p ( x ) e ^ { i \omega t }$ and $V = v ( x ) e ^ { i \omega t }$ are the acoustic pressure and the radial average of axial acoustic particle velocity at position x; the angular brackets % & represent the time average; Re# \$ and the tilde denote the real part and the complex conjugation, respectively; ! is the angular frequency of the acoustic wave. Whereas the viscous interaction between the acoustic wave and the duct wall decreases I, the thermal interaction can increase I when the duct has a steep temperature gradient.<sup>1,2</sup> Measurement of I plays a key role in deepening the experimental understanding of such acoustic power dissipation and production in ducts.<sup>3–13</sup>

Two experimental methods have been used in the measurements of I. One is the direct method simultaneously measuring P and V using a small pressure sensor and a laser Doppler velocimeter !LDV". This method was first reported in 1998 !Ref. 3" and has been employed for the measurements of the acoustic power of thermoacoustic heat engines<sup>4–8</sup> and the quality factor of an acoustic resonator.<sup>9</sup>

The other method is called a two-sensor method.<sup>10,14–16</sup> In this method, pressures $p _ { A } { = } p ( - \Delta x / 2 )$ and $p _ { B } { = } p ( \Delta x / 2 )$ are measured by two pressure sensors separated by a distance $\Delta x ,$ as shown in Fig. 1. The pressure $p ( 0 )$ and the velocity v!0" at the middle !x=0" are theoretically deduced from the sum and the difference of $p _ { A }$ and $p _ { B } .$ . The intensity at the middle is then determined from $p ( 0 )$ and v!0" through Eq. !1". In order to accurately estimate $p ( 0 )$ and v!0", Fusco et $a l . ^ { 1 0 }$ proposed to take viscous and thermal interactions of the gas with duct walls into account using the boundary layer approximation. Their method has been successfully used in the measurements of acoustic power in thermoacoustic heat engines, particularly those using pressurized gases as the working gas.<sup>11–13</sup>

The two-sensor method has a clear advantage to the direct method, since pressure measurements are much easier and simpler than the LDV that needs installation of seeding particles and use of transparent ducts. However, the intensity estimated from pressures has not been experimentally verified yet by the direct measurements. Besides, the application of the two-sensor method has been limited to wide ducts where the duct size, such as the radius $r _ { 0 }$ for a circular tube, is much larger than the viscous boundary layer thickness # formed at the duct wall. Here, #is given by $\sqrt { 2 \nu / \omega }$ , where \$ is the kinematic viscosity of a gas.

The propagation of the acoustic wave in ducts can be classified by the magnitude of the ratio of duct radius $r _ { 0 }$ to the viscous boundary layer thickness #. For example, for 1 bar air # is 0.22 mm at 100 Hz, and so the ratio of duct radius $r _ { 0 }$ to #easily becomes the order of 100 for tubes with $r _ { 0 } > 2 2$ mm. The two-sensor method has been found to be useful for such a wide duct. However, the ratio $r _ { 0 } / \delta$ decreases even below unity in the porous media such as the stack of thermoacoustic heat engines, and sound absorbers in architectural acoustics and anechoic chambers. It should be tested whether the present two-sensor method is applicable to these narrow ducts.

![[mu_00b178fa_85eb1f7b57a48068a11b.jpg]]  
FIG. 1. A cylindrical duct of radius $r _ { 0 }$ with two pressure sensors separated by "x. The origin x=0 is taken at the middle of the sensors. $p _ { + }$ and $p _ { - }$ denote the complex amplitudes of pressure wave traveling in the positive and negative directions.

In this paper, in order to extract the full ability of the two-sensor method, its validity is experimentally studied by the direct method measuring the pressure and the velocity simultaneously, for ducts with $1 . 3 0 { \leqslant } r _ { 0 } / \delta { \leqslant } 8 2 . 8$ . We show that the two-sensor method becomes inapplicable with $r _ { 0 } / \delta$ =1.3, and introduce a more general formulation of the method applicable regardless of the ratio $r _ { 0 }$ to $\delta . ^ { 1 7 }$ It is shown that the two-sensor method that we developed enables quick and accurate evaluation of the intensity I in narrow and wide ducts.

## II. FORMULATION OF TWO-SENSOR METHOD

We briefly describe here the principle of the two-sensor method referring to the derivation given by Fusco et $a l . ^ { 1 0 }$ Figure 1 schematically explains a cylindrical hollow duct through which the acoustic waves propagate. The locations of two pressure sensors A and B are also shown in Fig. 1. We consider the duct whose radius is much smaller than the wavelength, so the acoustic wave has a plane wave front. Thus, the acoustic pressure is expressed as $P = p ( x ) e ^ { i \omega t }$ independent of the radial coordinate, where the x axis is directed from A to B and its origin is taken at the middle of the sensors. We decompose the pressure $p ( x )$ as

$$
p ( x ) = ( p _ { + } e ^ { - i k x } + p _ { - } e ^ { i k x } ) ,\tag{!2"}
$$

where k is the complex wavenumber. Complex constants $p _ { + }$ and $p _ { - }$ include the amplitude and the phase of acoustic wave traveling in the positive and negative directions of x. The radial average of the axial velocity $v ( x )$ is given from the momentum equation as

$$
v ( x ) = \frac { i F } { \omega \rho } \frac { d p ( x ) } { d x } ,\tag{!3"}
$$

where $\rho$ is the mean density of the gas, and F is a complex function of $r _ { 0 } / \delta$ that we will show later in this section. Using Eqs. !2" and !3", the pressure $p ( 0 )$ and the pressure gradient $d p ( 0 ) / d x$ at the middle !x=0" are, respectively, written as

$$
p ( 0 ) = p _ { + } + p _ { - }\tag{!4"}
$$

and

$$
v ( 0 ) = { \frac { i F } { \omega \rho } } \left. { \frac { d p } { d x } } \right| _ { x = 0 } = { \frac { k F } { \omega \rho } } ( p _ { + } - p _ { - } ) .\tag{!5"}
$$

In order to relate $p ( 0 )$ and $v ( 0 )$ to the pressures $p _ { A }$ $= p ( - \Delta x / 2 )$ and $p _ { B } { = } p ( \Delta x / 2 )$ measured by two pressure sensors $A$ and B, we insert $x = \pm \Delta x / 2$ into Eq. !2" and, obtain the sum ${ p / } _ { + } + { p / } .$ and the difference ${ p / } _ { + } - { p / } _ { + }$ <sub>−</sub> as

$$
p _ { + } + p _ { - } = \frac { p _ { A } + p _ { B } } { 2 \cos ( k \Delta x / 2 ) }\tag{!6"}
$$

and

$$
p _ { + } - p _ { - } = \frac { ( p _ { A } - p _ { B } ) } { 2 i \sin ( k \Delta x / 2 ) } ,\tag{!7"}
$$

respectively.

After combining Eq. !4" with Eq. !6", and also Eq. !5" with Eq. !7", the pressure $p ( 0 )$ and the velocity v!0" are expressed using measured pressures $p _ { A }$ and $p _ { B } .$ Finally, the acoustic intensity I!0" is given through Eq. !1" by

$$
{ \cal I } = \frac { 1 } { 8 \omega \rho } \{ \mathrm { I m } [ H ] ( | p _ { A } | ^ { 2 } - | p _ { B } | ^ { 2 } ) + 2 \mathrm { R e } [ H ] | p _ { A } | | p _ { B } | \mathrm { s i n } \theta \} ,\tag{!8"}
$$

using

$$
H = \frac { k F } { \cos ( \widetilde { k } \Delta x / 2 ) \sin ( k \Delta x / 2 ) } ,\tag{!9"}
$$

where Im# \$ represents the imaginary part, and ) $= \mathrm { a r g } [ p _ { A } / p _ { B } ]$ represents the phase lead of $p _ { A }$ relative to $p _ { B } .$ In this way, the acoustic intensity I is determined through measurements of pressure amplitudes $\left| p _ { A } \right|$ and $\left| p _ { B } \right|$ , and their phase difference ), without involving velocity measurements.

Different from the two-sensor method on the basis of the and F !Ref. 18" for small-amplitude waves in a cylindrical duct given by

$$
k = - i k _ { 0 } \sqrt { \frac { J _ { 0 } ( i ^ { 3 / 2 } \sqrt { 2 } r _ { 0 } / \delta ) } { J _ { 2 } ( i ^ { 3 / 2 } \sqrt { 2 } r _ { 0 } / \delta ) } } \sqrt { \gamma + ( \gamma - 1 ) \frac { J _ { 2 } ( i ^ { 3 / 2 } \sqrt { 2 \sigma } r _ { 0 } / \delta ) } { J _ { 0 } ( i ^ { 3 / 2 } \sqrt { 2 \sigma } r _ { 0 } / \delta ) } }\tag{!10"}
$$

and

$$
F = 1 - \frac { 2 J _ { 1 } ( i ^ { 3 / 2 } \sqrt { 2 } r _ { 0 } / \delta ) } { i ^ { 3 / 2 } ( \sqrt { 2 } r _ { 0 } / \delta ) J _ { 0 } ( i ^ { 3 / 2 } \sqrt { 2 } r _ { 0 } / \delta ) } ,\tag{!11"}
$$

where <sub>\*</sub> and + are the specific heat ratio and Prandtl number, $J _ { n }$ is the nth order complex Bessel function, and $k _ { 0 }$ is the wavenumber in free space given by ! divided by the adiabatic speed of sound. Equations !10" and !11" are valid for small-amplitude sound waves in gases contained in a long rigid tube with constant circular cross section. The original two-sensor method that Fusco et al. developed uses approximate solutions $k ^ { \prime }$ and $F ^ { \prime }$ given by

$$
k ^ { \prime } = k _ { 0 } \left\{ 1 + \frac { 1 - i } { 2 } \frac { \delta } { r _ { 0 } } \Bigg ( 1 + \frac { \gamma - 1 } { \sqrt { \sigma } } \Bigg ) \right\}\tag{!12"}
$$

and

![[mu_00b178fa_ab2a9c2fc074e62058ec.jpg]]  
FIG. 2. Schematic illustration of the present experimental setup. The axial coordinate x is directed from the acoustic driver to the closed end.

$$
F ^ { \prime } = 1 - \frac { 1 - i } { r _ { 0 } / \delta } ,\tag{!13"}
$$

respectively. Both k and $F$ asymptotically approach $k ^ { \prime }$ and $F ^ { \prime }$ in the limit of $r _ { 0 } / \delta \mathfrak { P } 1$ , respectively.

Exact solutions k and $F$ have much more complicated expression than $k ^ { \prime }$ and $F ^ { \prime }$ , but there is no practical difficulties in the evaluation of them. We can easily handle the Bessel functions with complex arguments with commercially available software such as MATHEMATICA and MATLAB.

We experimentally test the applicability of the original two-sensor method developed by Fusco et al. for wide ducts $( r _ { 0 } / \delta \mathrm { = } 3 . 7 6 - 8 2 )$ . Also, we show, using the narrow duct having $r _ { 0 } / \delta \mathrm { = } 1 . 3$ , that the modified two-sensor method that uses k and F extends the applicability of the two-sensor method to narrow duct range.

## III. EXPERIMENTAL PROCEDURE

## A. Experimental setup

Figure 2 shows a schematic of the present experimental setup. A Pyrex glass cylindrical resonator, closed by a rigid plate at one end and driven at the other end, was filled with atmospheric air at room temperature !284 K". Short copper ducts with a length of 10 mm and an inner radius of 1 mm were attached to the resonator wall, through which the pressure was measured. The number of ducts and the spacing between them were varied by the resonator used. The origin of an axial coordinate x was placed at the driver end of the resonator. Monofrequency sinusoidal voltages were fed from a synthesizer to the acoustic driver !Electro-Voice, ID60DT" through a power amplifier !Yamaha, P1000S". The resonator radius $r _ { 0 }$ and the driving frequency $f \left( = \omega / 2 \pi \right)$ were chosen as listed in Table I. Thus, five different values of $r _ { 0 } / \delta$ were achieved covering from wide to narrow duct ranges.

TABLE I. Experimental conditions, where L denotes the resonator duct length.
<table><tr><td> $r _ { 0 } / \delta$ </td><td>(mm)  $r _ { 0 }$ </td><td> $f \left( \mathrm { H z } \right)$ </td><td> $L ~ ( \mathrm { m } )$ </td><td></td></tr><tr><td>58.6</td><td>10.5</td><td>148.5</td><td>1.0</td><td>Fundamental</td></tr><tr><td>82.8</td><td>10.5</td><td>298.5</td><td>1.0</td><td>Second mode</td></tr><tr><td>11.9</td><td>2.0</td><td>168.0</td><td>4.3</td><td></td></tr><tr><td>3.76</td><td>2.0</td><td>16.8</td><td>4.3</td><td></td></tr><tr><td>1.3</td><td>2.0</td><td>2.0</td><td>4.3</td><td></td></tr></table>

## B. Intensity measurements

## 1. Two-sensor method

Acoustic pressure $p ( x )$ was measured by a series of small pressure transducers !JTEKT, DD102-1F" flush mounted on the resonator wall. The natural frequency $f _ { 0 }$ of the present transducer is about 3 kHz, and our experimental frequency was always below $f _ { 0 } / 1 0 .$ Linear sensitivity was used for the pressure transducers. A multichannel spectrum analyzer !ONOSOKKI, DS-2000" was used to determine the amplitude and the phase of pressures at multiple locations. Prior to the experiments, all the transducers were simultaneously mounted on the rigid end of a dummy resonator, and the sensitivity was calibrated with each other at the frequencies in Table I.

In the two-sensor method, a pair of pressures is needed to determine I at the middle of them. Therefore, using the multiple numbers of pressure transducers makes it possible to determine I at different positions, and so, the axial distribution of I can be quite easily obtained in a single measurement of pressures.

## 2. Direct method

Axial acoustic particle velocity U!x" on the central axis of the resonator was measured using a LDV. Two laser beams emitted from the identical laser source were crossed inside the glass duct filled with air at ambient pressure and the appropriate amount of cigarette smoke as seeding particles. The intensity of the scattered light was detected by a photomultiplier and was sent to a tracker-type processor. The processor converts the frequency of the intensity variation to the voltage that is proportional to the instantaneous velocity. The voltage signal from the processor was monitored using the spectrum analyzer together with the pressure measured at the same x. The time delay of $2 . 7 \times 1 0 ^ { - 5 }$ s caused by the processor as well as that associated with the pressure measurements were taken into account when the phase of the velocity was evaluated.<sup>19</sup>

The measured velocity $U ( x )$ was confirmed to be in a laminar-flow regime, so the amplitude and the phase of the radial average velocity $V ( x )$ were determined from $U ( x ) .$ 9 using the theoretical result of the laminar flow theory instead of measuring the radial profile. The acoustic intensity is determined from Eq. !1" as

$$
I = { \textstyle \frac { 1 } { 2 } } | p | | v | \cos \phi ,\tag{!14"}
$$

where $\phi$ denotes the phase lead of v to $p .$ The acoustic intensity I determined by the direct method is used as a reference for the intensity I determined by the two-sensor method.

## IV. RESULTS AND DISCUSSION

## A. Wide duct range

Quality factor Q of a resonator filled with air is approximately given by $Q \simeq r _ { 0 } / \left( 1 . 5 \delta \right) . ^ { 9 , 2 0 }$ An infinitely high Q value results in a pure standing wave field in the resonator, but as the $Q$ decreases, a fraction of the traveling wave component increases in the acoustic field. Figures 3!a" and 3!b" show the axial profile of the pressure amplitude $| p |$ and the phase $\Theta ( x ) = \mathrm { a r g } [ p ( x ) / p _ { e } ]$ in a resonator $\left( r _ { 0 } { = } 1 0 . 5 ~ \mathrm { m m } \right)$ driven at the fundamental resonance frequency $\left( f { = } 1 4 8 . 5 ~ \mathrm { H z } \right)$ , where $p _ { e }$ represents the acoustic pressure at the closed end. The parameter $r _ { 0 } / \delta \mathrm { = } 5 8 . 6$ results in $Q = 3 9$ of this resonator, which is sufficiently high to produce a standing-wave-like acoustic field. Hence, the axial distribution of $| p |$ is close to a rectified cosine wave, and the slope of $\Theta ( x )$ is very small except the vicinity of the pressure node $( x \mathrm { { \simeq } } 0 . 4 5 ~ \mathrm { { m } ) }$ . A small but finite fraction of the traveling wave component is seen in a nonzero slope of 0!x" in the inset of Fig. 3!b".

![[mu_00b178fa_e6dd830ceb89dcd887cb.jpg]]  
FIG. 3. Acoustic field in the resonator with $r _ { 0 } / \delta \mathrm { = } 5 8 . 6 .$ . Axial profile of !a" \*p\* and !b" 0, and !c" the acoustic intensity I. The open circles !!" in !c" represent I determined by the direct method, whereas the solid squares !"" represent I by the two-sensor method.

Figure 3!c" shows the acoustic intensity I obtained by the two-sensor method when the pairs of pressures separated by the distance $\Delta x { = } 0 . 2 \mathrm { ~ m ~ }$ are used. We used $k ^ { \prime }$ and $F ^ { \prime }$ in Eqs. !12" and !13" for the derivation of I in this resonator, according to the ordinary prescription of the two-sensor method. It can be quickly tested whether the experimental I is plausible, by confirming that I monotonically decreases to zero at the closed end, as shown in Fig. 3!c". This is because the velocity and I should become zero at the rigid end, and also because the slope of I should be negative due to the viscous and thermal attenuations. The acoustic intensity I obtained by the direct method was also plotted in Fig. 3!c" as a reference. An excellent agreement was obtained between them. The acoustic intensity I obtained with $\Delta x { = } 0 . 1 , ~ 0 . 3$ and 0.4 m was also found to agree with I determined by the direct method. Thus, it is clear that the two-sensor method is applicable to the wide-tube resonator with $r _ { 0 } / \delta \mathrm { = } 5 8 . 6$

In order to achieve lower $r _ { 0 } / \delta$ values, the duct with $r _ { 0 }$ $= 2 . 0$ mm was tested. The gas column was driven at $f$ =168 Hz, resulting in $r _ { 0 } / \delta \mathrm { = } 1 1 . 9 . \mathrm { A }$ lower Q value $\left( = 7 . 9 \right)$ of this duct increases the ratio of the traveling wave to the standing wave components. As a result, \*p\* shown in Fig. $4 ( \mathrm { a } )$ is significantly different from that in a pure standing wave field. The pairs of pressures with $\Delta x { = } 0 . 3 5$ and 1.5 m, together with $k ^ { \prime }$ and $F ^ { \prime }$ , were used for the estimation of v and I. We found a good agreement between v measured with the LDV and that determined by the pressures. As a result, the intensities by the two methods agreed well with each other, as shown in Fig. 4!b". This fact assures that the twosensor method proposed by Fusco et al. is applicable also when $r _ { 0 } / \delta \mathrm { = } 1 1 . 9$

![[mu_00b178fa_ad4f7049dadc09f11a09.jpg]]  
FIG. 4. !Color online" Axial profile of !a" \*p\* and !b" I when $r _ { 0 } /$ #= 11.9. The open and solid circles represent I by the direct method and that by the two-sensor method, respectively. The solid line in !a" is a guide to the eye. Error of I is within the size of their symbols.

We further decreased $r _ { 0 } / \delta$ down to 3.76 by decreasing f by a factor of 10. The results obtained by the direct method and the two-sensor method $( \Delta x { = } 0 . 7 ~ \mathrm { m } )$ are plotted in Fig. 5. The acoustic intensities obtained by these two methods agree with each other, with the relative error of 5% at $x { = } 0 . 4 5$ . This fact means that Fusco’s method based on the boundary layer approximation is practically applicable even when $r _ { 0 } / \delta$ =3.76. So, this method can cover a quite wide range of $r _ { 0 } / \delta .$ Before showing the test results with a further lower $r _ { 0 } / \delta$ in the next section, it would be beneficial to note pitfalls that we encountered when choosing the distance of the two pressure sensors.

The second term of I in Eq. !8" has a factor of sin ), so the relative error of this term is very sensitive to the error of when is close $\mathrm { t o } \ { \pm n \pi } ,$ where n is an integer. Hence, it is important to locate the sensors so that a sufficient phase difference is achieved between them. In high Q resonators, the axial distribution of $\Theta ( x )$ becomes like a step function, as shown in Fig. 3!b". This means that the distance $\Delta x$ between the sensors can become a considerable fraction of the resonator. In our experiments, we only used the pair of pressures that satisfies $\left| \theta - n \pi \right| > 1 . 0 ^ { \circ }$ , so as to decrease the error of I within the size of the symbols in the figures.

![[mu_00b178fa_c69e44daeab66c20d768.jpg]]  
FIG. 5. !Color online" Axial profile of the acoustic intensity I when $r _ { 0 } / \delta$ =3.76. The solid !!" and open !!" circles represent I obtained by the direct method and by the two-sensor method, respectively.

![[mu_00b178fa_7dbbcd21d119c70b66ff.jpg]]  
FIG. 6. Axial profile of the acoustic intensity I in the resonator with $r _ { 0 } / \delta$ $= 8 2 . 8 .$ . The open squares !#" represent I determined by the direct method, whereas the solid circles !!" and squares !"" represent I determined by the two-sensor method with the use of pressures separated by $\Delta x { = } 0 . 2$ and 0.6 m, respectively.

We should also pay attention to the function H in $\operatorname { E q }$ !8", when choosing a pair of sensors having appropriate distance $\Delta x . ^ { 1 6 , 2 1 }$ Figure 6 shows the acoustic intensity I in the resonator $\left( r _ { 0 } { = } 1 0 . 5 ~ \mathrm { m m } \right)$ driven at the second harmonic frequency $\left( f = 2 9 8 . 5 \ \mathrm { H z } \right)$ . The data plotted by the solid circles !!" were obtained using the pairs of sensors with $\Delta x$ =0.2 m, which agree well with I determined by the direct method !#". However, when $\Delta x$ was increased to 0.6 m, it was found that the deviation of I by the two-sensor method from the true values became significantly large. As explained below, the "x-dependence of the function H is responsible for the error with $\Delta x { = } 0 . 6 \ \mathrm { m }$

Figure 7 shows the real part $\mathrm { R e } [ H ]$ and the imaginary part Im#H\$ of the function H as a function of the distance $\Delta x .$ It is shown that $\mathrm { R e } [ H ]$ and Im#H\$ greatly change with $\Delta x$ particularly when $\Delta x$ approaches $n \lambda / 2$ , where n is a positive integer, and 1 is the wavelength. This means that I is very sensitive to slight differences of $\Delta x ;$ large errors are easily induced by small errors of $\Delta x .$ . Similar error of I is unavoidable when errors are present in the constants included in $k ,$ such as the adiabatic speed of sound, regardless of whether the boundary layer approximation is valid. $\mathrm { S o } ,$ it is better to avoid $\Delta x { = } n \lambda / 2 \ ( n { = } 1 , 2 , 3 , { \ldots } )$ , but to choose $\Delta x$ near $\lambda / 4$ $+ ( n - 1 ) \lambda / 2$ , which is best suited to the two-sensor method.

![[mu_00b178fa_72c2521b80aad71df581.jpg]]  
FIG. 7. !Color online" Real part Re#H\$ !solid line" and imaginary part Im#H\$ !broken line" as a function of "x. Here $k ^ { \prime }$ and $F ^ { \prime }$ are used.

![[mu_00b178fa_3e46f5bf46ba7f4b0478.jpg]]  
FIG. 8. !Color online" Axial profile of $| p | ,$ \*v\*, /, and I when $r _ { 0 } / \delta \mathrm { = } 1 . 3$ . The open triangles $( \triangle )$ represent the data obtained by the original two-sensor method developed by Fusco et $a l .$ , and the open squares !#" represent those by the modified two-sensor method using $k$ and $F .$ The solid circles !!" represent the data obtained by the direct method.

## B. Narrow duct range

To test the two-sensor method when $r _ { 0 } / \delta \mathrm { = } r _ { 0 } \sqrt { \omega / 2 \nu }$ is close to 1, the same glass duct with $r _ { 0 } { = } 2 . 0$ mm was used as in the preceding section, but the frequency was further reduced to $f { = } 2 . 0$ Hz. As a result, the ratio $r _ { 0 } / \delta \mathrm { = } 1 . 3$ was achieved. With the duct closed by a rigid plate, the phase $\Theta ( 4 . 2 )$ at the driver end was found to be $2 . 6 ^ { \circ }$ , meaning that a very large $\Delta x$ between the sensors was needed to satisfy $| \theta | > 1 . 0 ^ { \circ }$ . So, in this particular experiment, we replaced the rigid plate with a rubber balloon, to increase the traveling wave component.<sup>17</sup>

We determined $p$ and v using the pressures separated by the distance $\Delta x { = } 0 . 7$ m. We adopted the original two-sensor method, namely, using $k ^ { \prime }$ and $F ^ { \prime }$ obtained under the boundary layer approximation. The estimated $| p |$ , \*v\*, and their phase difference $\phi$ are plotted by open triangles $( \triangle )$ in Figs. $8 ( \mathrm { a } ) { - } 8 ( \mathrm { c } )$ , respectively. For comparison, those determined by the direct measurements are also plotted by solid circles !!". It is shown that the pressure amplitude $| p |$ is in good agreement with the true value, but v estimated by the two-sensor method is apparently different from that directly measured by the LDV; \*v\* is 2.2 times larger than the true value, and the phase $\phi$ leads the true v by $1 2 ^ { \circ }$ . Since I depends on both $| v |$ and $\phi$ through the factor \*v\*cos $\phi$ in Eq. !14", the twosensor method gives significantly different I from that by the direct method, which is shown in Fig. 8!d". Thus, we conclude that the two-sensor method using $k ^ { \prime }$ and $F ^ { \prime }$ becomes inappropriate when $r _ { 0 } / \delta$ decreases to 1.3.

![[mu_00b178fa_bd2080a30a8a85246438.jpg]]

![[mu_00b178fa_1e4209ff98c8d0def4b3.jpg]]  
FIG. 9. The complex factor ${ \mathit { F } } { = } | F | e ^ { i \Psi }$ as a function of the ratio $r _ { 0 } / \delta .$ The dotted curves represent $F ^ { \prime }$ obtained under the boundary layer approximation.

In order to obtain the correct I by the two-sensor method, we modified the original method by replacing $k ^ { \prime }$ and $F ^ { \prime }$ with k and F that are given in Eqs. !10" and !11". The results determined by the modified two-sensor method are shown by open squares !#" in Figs. 8!a"–8!d". We see that \*v\*, /, and I obtained by the modified two-sensor method agree with those by the direct method. This result shows that the present formulation using k and $F$ makes it possible to successfully measure I in narrow ducts.

The complex wavenumber k is theoretically derived by row duct range from $r _ { 0 } / \delta \mathrm { = } 1 0 ^ { - 2 }$ to 10 recently.<sup>22</sup> As is shown in these literatures, $k ^ { \prime }$ obtained under the boundary layer approximation deviates from k below $r _ { 0 } / \delta \sim 4$ . However, in the present experiment, the use of $k ^ { \prime }$ does not cause serious difference. As shown in $\mathrm { F i g . \ 8 ( a ) }$ , the amplitude $| p |$ estimated by the two-sensor methods $( \triangle$ and #" falls onto the directly measured data, irrespective of whether $k ^ { \prime }$ is substituted for $k .$ Such agreement is attributable to the fact that "x is much smaller than the wavelength in this experiment; if "x is comparable to the wavelength, the use of k instead of $k ^ { \prime }$ would become necessary.

Large discrepancy of I in the original two-sensor method comes from the complex factor $F ^ { \prime }$ . We plotted F and $F ^ { \prime }$ in Figs. 9!a" and 9!b" as a function of $r _ { 0 } / \delta .$ The difference between the absolute values of $F$ and $F ^ { \prime }$ rapidly grows below $r _ { 0 } / \delta \sim 4$ , and the difference between their arguments becomes a few degrees with $r _ { 0 } / \delta < 1 0$ . When $r _ { 0 } / \delta \mathrm { = } 1 . 3$ , the ratio of their absolute values reaches 2.2 and the phase difference becomes $1 2 ^ { \circ } .$ , respectively. These differences result in the large deviation of v having the factor $F$ in Eq. !5". It should be noted that the original two-sensor method fortuitously worked well when $r _ { 0 } / \delta \mathrm { = } 3 . 7 6$ . The difference of the argument reaches $2 . 5 ^ { \circ }$ between F and $F ^ { \prime }$ in this case, whereas $\left| { \cal F } ^ { \prime } \right| { = } 1 . 0 2 | { \cal F } |$ . The deviation of the phase $\phi$ can be critical in the measurement of I!3cos $\phi )$ , when $\phi$ is close to the standing wave phase $\left( \pm \pi / 2 \right) . ^ { 9 }$ Indeed, in Fig. 5, the relative error of I exceeds 60% at $x { = } 3 . 8 5$ m where $\phi$ reaches $8 5 ^ { \circ }$ , while it remains within 5% at $x { = } 0 . 4 5$ m where / $= 2 8 ^ { \circ }$ . Thus, it is strongly recommended to use k and F to obtain the best result in the measurement of I in ducts.

## V. SUMMARY

In this paper, the acoustic intensity I in cylindrical ducts was determined by the two-sensor method and also by the direct method measuring pressure and velocity. From the comparison with the acoustic intensity obtained by the direct method, the applicability of the two-sensor method was tested with $r _ { 0 } / \delta$ values from 1.3 to 82.8. The two-sensor method is useful for wide ducts, but it was found to become inappropriate for a narrow duct with $r _ { 0 } / \delta \mathrm { = } 1 . 3$ . We developed the two-sensor method to include a narrow duct range by modifying the formulation of the method. It is shown that the two-sensor method that we developed enables quick and accurate evaluation of the acoustic intensity I in lossy ducts from narrow to wide duct ranges.

<sup>1</sup>G. W. Swift, Thermoacoustics: A Unifying Perspective for Some Engines and Refrigerators !Acoustical Society of America, Sewickley, PA, 2002".

${ } ^ { 2 } \mathrm { A } .$ . Tominaga, “Thermodynamic aspects of thermoacoustic theory,” Cryogenics 35, 427–440 !1995"; Fundamental Thermoacoustics !Uchida Roukakuho, Tokyo, Japan 1998".

<sup>3</sup>T. Yazaki and A. Tominaga, “Measurement of sound generation in thermoacoustic oscillations,” Proc. R. Soc. London, Ser. A 454, 2113–2122 !1998".

<sup>4</sup>T. Yazaki, A. Iwata, T. Maekawa, and A. Tominaga, “Traveling wave thermoacoustic engine in a looped tube,” Phys. Rev. Lett. 81, 3128–3131 !1998".

<sup>5</sup>T. Yazaki, T. Biwa, and A. Tominaga, “A pistonless Stirling cooler,” Appl. Phys. Lett. 80, 157–159 !2002".

<sup>6</sup>Y. Ueda, T. Biwa, U. Mizutani, and T. Yazaki, “Acoustic field in a thermoacoustic Stirling engine having a looped tube and resonator,” Appl. Phys. Lett. 81, 5252–5254 !2002"; “Experimental studies of a thermoacoustic Stiriling prime mover and its application to a cooler,” J. Acoust. Soc. Am. 115, 1134–1141 !2004".

<sup>7</sup>T. Biwa, Y. Tashiro, U. Mizutani, M. Kozuka, and T. Yazaki, “Experimental demonstration of thermoacoustic energy conversion in a resonator,” Phys. Rev. E 69, 066304 !2004".

<sup>8</sup>H. Bailliet, P. Lotton, M. Bruneau, V. Gusev, J. C. Valiere, and B. Gazengel, “Acoustic power flow measurement in a thermoacoustic resonator by means of laser Doppler anemometry !L. D. A." and microphonic measurement,” Appl. Acoust. 60, 1–11 !2000".

<sup>9</sup>T. Biwa, Y. Ueda, H. Nomura, U. Mizutani, and T. Yazaki, “Measurement of the Q value of an acoustic resonator,” Phys. Rev. E 72, 026601 !2005".

<sup>10</sup>A. M. Fusco, W. C. Ward, and G. W. Swift, “Two-sensor power measurements in lossy ducts,” J. Acoust. Soc. Am. 91, 2229–2235 !1992".

<sup>11</sup>G. W. Swift, D. L. Gardner, and S. Backhaus, “Acoustic recovery of lost power in pulse tube refrigerators,” J. Acoust. Soc. Am. 105, 711–724 !1999".

<sup>12</sup>G. Petculescu and L. A. Wilen, “Traveling-wave amplification in a variable standing wave ratio device,” ARLO 3, 71–76 !2002".

<sup>13</sup>D. L. Gardner and G. W. Swift, “A cascade thermoacoustic engine,” J. Acoust. Soc. Am. 114, 1905–1919 !2003".

<sup>14</sup>J. Y. Chung and D. A. Blaster, “Transfer function method of measuring in-duct acoustic properties. I. theory,” J. Acoust. Soc. Am. 68, 907–913 !1980"; “Transfer function method of measuring in-duct-acsoutic properties. II. experiment,” J. Acoust. Soc. Am. 68, 913–921 !1980".

<sup>15</sup>W. T. Chu, “Extension of the two-microphone transfer function method for

impedance tube measurements,” J. Acoust. Soc. Am. 80, 347–348 !1986".

<sup>16</sup>A. F. Seybert and D. F. Ross, “Experimental determination of acoustic properties using a two-microphone random-excitation technique,” J. Acoust. Soc. Am. 61, 1362–1370 !1977".

<sup>17</sup>T. Biwa, Y. Tashiro, H. Nomura, Y. Ueda, and T. Yazaki, “Acoustic intensity measurement in a narrow duct by a two-sensor method,” Rev. Sci. Instrum. 78, 086110 !2007".

<sup>18</sup>H. Tijdeman, “On the propagation of sound waves in cylindrical tubes,” J. Sound Vib. 39, 1–33 !1975".

<sup>19</sup>T. Biwa, Y. Ueda, T. Yazaki, and U. Mizutani, “Work flow measurements in a thermoacoustic engine,” Cryogenics 41, 305–310 !2001".

<sup>20</sup>G. W. Swift, “Thermoacoustic engines,” J. Acoust. Soc. Am. 84, 1145– 1180 !1988".

<sup>21</sup>H. Bodén and M. Åbom, “Influence of errors on the two-michrophone method for measuring acoustic properties in ducts,” J. Acoust. Soc. Am. 79, 541–549 !1986".

<sup>22</sup>T. Yazaki, Y. Tashiro, and T. Biwa, “Measurement of sound propagation in narrow tubes,” Proc. R. Soc. London, Ser. A 463, 2855–2862 !2007".
