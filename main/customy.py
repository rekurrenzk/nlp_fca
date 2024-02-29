import spacy

e_text =\
"""
Non-equilibrium state variables
The suitable relationship that defines non-equilibrium thermodynamic state variables is as follows. When the system is in local equilibrium, non-equilibrium state variables are such that they can be measured locally with sufficient accuracy by the same techniques as are used to measure thermodynamic state variables, or by corresponding time and space derivatives, including fluxes of matter and energy. In general, non-equilibrium thermodynamic systems are spatially and temporally non-uniform, but their non-uniformity still has a sufficient degree of smoothness to support the existence of suitable time and space derivatives of non-equilibrium state variables.

Because of the spatial non-uniformity, non-equilibrium state variables that correspond to extensive thermodynamic state variables have to be defined as spatial densities of the corresponding extensive equilibrium state variables. When the system is in local equilibrium, intensive non-equilibrium state variables, for example temperature and pressure, correspond closely with equilibrium state variables. It is necessary that measuring probes be small enough, and rapidly enough responding, to capture relevant non-uniformity. Further, the non-equilibrium state variables are required to be mathematically functionally related to one another in ways that suitably resemble corresponding relations between equilibrium thermodynamic state variables.[10] In reality, these requirements, although strict, have been shown to be fulfilled even under extreme conditions, such as during phase transitions, at reacting interfaces, and in plasma droplets surrounded by ambient air.[11][12][13] There are, however, situations where there are appreciable non-linear effects even at the local scale.[14][15]
"""

nlp = spacy.