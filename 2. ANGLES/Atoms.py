#2.2 ANGLES
#Angles maybe formed between groups of atoms in a molecule, between sub-systems such as the
#body, a wing or an engine of an airplane, the axes of manipulators of movable robots. Angles are
#measure by real numbers having units of radians or degrees. Angles may be planar (2-D) or
#spatial (3-D). Angles are varied by increments between say zero to 2*π radians. 



#%%

BondAngle = {}
for r in range(2,10):
    BondAngle[r] = {}
    for p in range (4):
        BondAngle[r][p]={}

BondAngle[2][0][2] = ["Linear",[180]]
BondAngle[2][1][3] = ["bent",[120]]
BondAngle[3][0][3] = ["trigonal planar",[120]]
BondAngle[2][2][4] = ["bent",[109.5]]
BondAngle[3][1][4] = ["trigonal pyramidal",[109.5]]
BondAngle[4][0][4] = ["tetrahedral",[109.5]]
BondAngle[2][3][5] = ["Linear",[180]]
BondAngle[3][2][5] = ["T-shaped",[90,180]]
BondAngle[4][1][5] = ["seesaw",[90]]
BondAngle[5][0][5] = ["trigonal bipyramidal",[90, 120, 180]]
BondAngle[4][2][6] = ["square planar",[90, 180]]
BondAngle[5][1][6] = ["square pyramidal",[90]]
BondAngle[6][0][6] = ["octahedral",[90, 180]]
BondAngle[5][2][7] = ["planar pentagonal",[72, 144]]
BondAngle[6][1][7] = ["pentagonal pyramidal",[72, 90, 144]]
BondAngle[7][0][7] = ["pentagonal bipyramidal",[90, 72, 180]]
BondAngle[8][0][8] = ["square antiprismatic",[]]
BondAngle[9][0][9] = ["tricapped trigonal prismatic",[]]
#%%

