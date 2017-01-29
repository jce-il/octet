<TABLE cellpadding=0 cellspacing=0 class="t0">
<TR>
	<TD class="tr0 td0"><P class="p0 ft0">&nbsp;</P></TD>
	<TD class="tr0 td1"><P class="p0 ft1">The Octet Project: Summary & PLAN</P></TD>
</TR>
<TR>
	<TD class="tr1 td0"><P class="p0 ft2">Date:</P></TD>
	<TD class="tr1 td1"><P class="p1 ft2">26/Dec/2016</P></TD>
</TR>
<TR>
	<TD class="tr2 td0"><P class="p0 ft3">Update:</P></TD>
	<TD class="tr2 td1"><P class="p1 ft3">26/Dec/2016</P></TD>
</TR>
<TR>
	<TD class="tr3 td0"><P class="p0 ft2">Proposer:</P></TD>
	<TD class="tr3 td1"><P class="p1 ft2">Prof. Iaakov Exman</P></TD>
</TR>
</TABLE>
<P class="p2 ft4">1.  SUMMARY</P>
<P class="p3 ft6">The Octet Project is a proposal for a joint final project of 8 students doing the “Introduction to Research” course. The outcome of the Project is a <NOBR>multi-purpose</NOBR> flexible <NOBR><SPAN class="ft5">infra-structure</SPAN></NOBR><SPAN class="ft5"> software package for exploratory Computational Science</SPAN> called the Octet. This software package will enable agile prototyping of an exploratory Computational Science software package applicable to a chosen domain. The infrastructure will contain a set of degrees of freedom, which initially contains seven degrees of exploratory freedom and one additional <NOBR>infra-structure</NOBR> feature, enabling combination of <NOBR>sub-sets</NOBR> of degrees of freedom.</P>
<P class="p4 ft6">The Octet package will be extensible, allowing students in the next years to extend it to include additional sets of degrees of freedom, new input and output mechanisms, and pluggable computational modules.</P>
<P class="p3 ft6">The ultimate goal of this project is to have an Octet package running. The Octet package will be described in a scientific paper in which all the students will be <NOBR>co-authors.</NOBR> The paper will be submitted to an international forum (conference or journal).</P>
<P class="p5 ft4">2.  OCTET OF DEGREES OF FREEDOM</P>
<P class="p6 ft9"><SPAN class="ft7">2.1 </SPAN><SPAN class="ft8">DISTANCES</SPAN></P>
<P class="p7 ft6">Distances maybe distances between atoms in a molecule, distances between <NOBR>sub-systems</NOBR> such as wagons of a train, distances between <NOBR>micro-electronic</NOBR> components in VLSI or macro geographical distances. Distances are measured by real numbers and have units, such as kilometers or nanometers or <SPAN class="ft10">λ </SPAN>(lambda) values. Distances are varied by increments between a lower bound an upper bound.</P>
<P class="p8 ft9"><SPAN class="ft7">2.2 </SPAN><SPAN class="ft8">ANGLES</SPAN></P>
<P class="p7 ft6">Angles maybe formed between groups of atoms in a molecule, between <NOBR>sub-systems</NOBR> such as the body, a wing or an engine of an airplane, the axes of manipulators of movable robots. Angles are measure by real numbers having units of radians or degrees. Angles may be planar <NOBR>(2-D)</NOBR> or spatial <NOBR>(3-D).</NOBR> Angles are varied by increments between say zero to 2*<SPAN class="ft10">π </SPAN>radians.</P>
<P class="p8 ft9"><SPAN class="ft7">2.3 </SPAN><SPAN class="ft8">DISCRETE COMPOSITION</SPAN></P>
<P class="p9 ft6">Discrete composition is a finite and discrete set of symbols in a given domain. It maybe the elementary particles in a nuclear reaction, atoms or isotopes in a chemical or biochemical reaction, bases or <NOBR>amino-acids</NOBR> in genetics and/or biology, keywords in textual search, symbols of countries in a geographical context or Internet URL context. Discrete composition is varied by discrete randomizing symbol choices.</P>
</DIV>

<P class="p11 ft9"><SPAN class="ft7">2.4 </SPAN><SPAN class="ft8">TOPOLOGY</SPAN></P>
<P class="p9 ft6">Topology is usually represented as a graph with edges linking vertices. These may represent roads, rivers, communication links in the internet, and friendship links in a social network. Topology is varied by disconnecting/connecting vertices in the topology graph. An interesting display of topology is the usage of “hyperbolic tre es” or “hypertrees”; see the example in Fig. 1.</P>
<P class="p12 ft6">See also:</P>
<P class="p13 ft13"><SPAN class="ft6">The video demo at: </SPAN><SPAN class="ft12">https://www.youtube.com/watch?v=pwpze3RF55o</SPAN></P>
<P class="p14 ft6">A JSON animation is seen at: <SPAN class="ft12">https://philogb.github.io/jit/static/v20/Jit/Examples/Hypertree/example1.html</SPAN></P>
<P class="p15 ft6">Fig. 1 – An example of a hyperbolic tree.</P>
<P class="p16 ft9"><SPAN class="ft7">2.5 </SPAN><SPAN class="ft8">SPATIAL GRIDS</SPAN></P>
<P class="p7 ft6">Spatial grids divide a space of given dimensions (say <NOBR>3-D)</NOBR> and/or form (say a cube, cylinder or any other form) into discrete “finite elements”. On e should also provide relations among the elements, such as who are the neighbors of a given element. Boundary elements may have assigned neighbors in a periodical manner. Finite elements are varied by adding/deleting elements, distorting the whole form, etc.</P>
<P class="p17 ft9"><SPAN class="ft7">2.6 </SPAN><SPAN class="ft8">INTENSIVE CONTINUOUS QUANTITIES</SPAN></P>
<P class="p7 ft6">Intensive quantities have a value that is independent of the size of a body. For instance, the “temperature” of the human body is generally around 37<SPAN class="ft14">o </SPAN>Celsius, independent of the size of the body, whether a child or an adult. Another example of an intensive quantity is the density of a material. Intensive continuous quantities are represented by real numbers and are varied in increments between a lower and an upper bound.</P>
</DIV>
<DIV id="page_3">


<P class="p11 ft9"><SPAN class="ft7">2.7 </SPAN><SPAN class="ft8">EXTENSIVE CONTINUOUS QUANTITIES</SPAN></P>
<P class="p9 ft6">Extensive quantities have a value that is dependent of the size of a body. For instance, the “weight” of a person obviously depends on the size of the body. Extensive continuous quantities are also represented by real numbers and are varied in increments between a lower and an upper bound.</P>
<P class="p19 ft9"><SPAN class="ft7">2.8 </SPAN><SPAN class="ft8">COMBINED DEGREES OF FREEDOM</SPAN></P>
<P class="p7 ft6">Finally, we wish to be able to choose more than one degree of freedom to describe and explore a system of interest. Thus, we may have systems with both intensive and extensive quantities, or we may describe a system of molecules by jointly computing their composition and geometry (both distances and angles).</P>
<P class="p20 ft4">3. OCTET IMPLEMENTATION</P>
<P class="p21 ft6">Octet should be implemented by using any set of modules – for computation and visual display – written in various programming languages, as available in the internet. The overall “wrapper” of these modules should be programmed in Python, to fit the course contents.</P>
<P class="p5 ft4">4. TIME SCHEDULE & TASKS DIVISION</P>
<P class="p22 ft6">The Octet project should take one month to develop and test. Each of the 8 students should take one of the above degrees of freedom, design and implement, in a way that there is a common interface between the different degrees of freedom.</P>
</DIV>
</BODY>
</HTML>
