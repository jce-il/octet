# octet
1
The Octet Project: Summary & PLAN
Date: 26/Dec/2016
Update: 26/Dec/2016
Proposer: Prof. Iaakov Exman
1. SUMMARY
The Octet Project is a proposal for a joint final project of 8 students doing the “Introduction
to Research” course. The outcome of the Project is a multi-purpose flexible infra-structure
software package for exploratory Computational Science called the Octet. This software package
will enable agile prototyping of an exploratory Computational Science software package
applicable to a chosen domain. The infrastructure will contain a set of degrees of freedom, which
initially contains seven degrees of exploratory freedom and one additional infra-structure feature,
enabling combination of sub-sets of degrees of freedom.
The Octet package will be extensible, allowing students in the next years to extend it to
include additional sets of degrees of freedom, new input and output mechanisms, and pluggable
computational modules.
The ultimate goal of this project is to have an Octet package running. The Octet package will
be described in a scientific paper in which all the students will be co-authors. The paper will be
submitted to an international forum (conference or journal).
2. OCTET OF DEGREES OF FREEDOM
2.1 DISTANCES
Distances maybe distances between atoms in a molecule, distances between sub-systems such as
wagons of a train, distances between micro-electronic components in VLSI or macro
geographical distances. Distances are measured by real numbers and have units, such as
kilometers or nanometers or λ (lambda) values. Distances are varied by increments between a
lower bound an upper bound.
2.2 ANGLES
Angles maybe formed between groups of atoms in a molecule, between sub-systems such as the
body, a wing or an engine of an airplane, the axes of manipulators of movable robots. Angles are
measure by real numbers having units of radians or degrees. Angles may be planar (2-D) or
spatial (3-D). Angles are varied by increments between say zero to 2*π radians.
2.3 DISCRETE COMPOSITION
Discrete composition is a finite and discrete set of symbols in a given domain. It maybe the
elementary particles in a nuclear reaction, atoms or isotopes in a chemical or biochemical
reaction, bases or amino-acids in genetics and/or biology, keywords in textual search, symbols of
countries in a geographical context or Internet URL context. Discrete composition is varied by
discrete randomizing symbol choices. 
2
2.4 TOPOLOGY
Topology is usually represented as a graph with edges linking vertices. These may represent
roads, rivers, communication links in the internet, and friendship links in a social network.
Topology is varied by disconnecting/connecting vertices in the topology graph. An interesting
display of topology is the usage of “hyperbolic trees” or “hypertrees”; see the example in Fig. 1.
See also:
The video demo at: https://www.youtube.com/watch?v=pwpze3RF55o
A JSON animation is seen at:
https://philogb.github.io/jit/static/v20/Jit/Examples/Hypertree/example1.html
Fig. 1 – An example of a hyperbolic tree.
2.5 SPATIAL GRIDS
Spatial grids divide a space of given dimensions (say 3-D) and/or form (say a cube, cylinder or
any other form) into discrete “finite elements”. One should also provide relations among the
elements, such as who are the neighbors of a given element. Boundary elements may have
assigned neighbors in a periodical manner. Finite elements are varied by adding/deleting
elements, distorting the whole form, etc.
2.6 INTENSIVE CONTINUOUS QUANTITIES
Intensive quantities have a value that is independent of the size of a body. For instance, the
“temperature” of the human body is generally around 37o
 Celsius, independent of the size of the
body, whether a child or an adult. Another example of an intensive quantity is the density of a
material. Intensive continuous quantities are represented by real numbers and are varied in
increments between a lower and an upper bound. 
3
2.7 EXTENSIVE CONTINUOUS QUANTITIES
Extensive quantities have a value that is dependent of the size of a body. For instance, the
“weight” of a person obviously depends on the size of the body. Extensive continuous quantities
are also represented by real numbers and are varied in increments between a lower and an upper
bound.
2.8 COMBINED DEGREES OF FREEDOM
Finally, we wish to be able to choose more than one degree of freedom to describe and explore a
system of interest. Thus, we may have systems with both intensive and extensive quantities, or we
may describe a system of molecules by jointly computing their composition and geometry (both
distances and angles).
3. OCTET IMPLEMENTATION
Octet should be implemented by using any set of modules – for computation and visual display –
written in various programming languages, as available in the internet. The overall “wrapper” of
these modules should be programmed in Python, to fit the course contents.
4. TIME SCHEDULE & TASKS DIVISION
The Octet project should take one month to develop and test. Each of the 8 students should take
one of the above degrees of freedom, design and implement, in a way that there is a common
interface between the different degrees of freedom.
 
