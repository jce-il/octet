import numpy

class AnglesCalculator:
    def Radian2Degree(angleInRad):
        return angleInRad * 180 / numpy.pi
    def Degree2Radian(angleInDeg):
        return angleInDeg * numpy.pi / 180
    def NormalizeDegree(angle):
        return angle % 360
    def NormalizeRadian(angle):
        return AnglesCalculator.Degree2Radian(AnglesCalculator.NormalizeDegree(AnglesCalculator.Radian2Degree(angle)))
    def BetweenAtoms(BoneElectronPair, LonePair,ElectronDomain):
        if BoneElectronPair in  BondAngle.keys():
            if LonePair in BondAngle[BoneElectronPair].keys():
                if ElectronDomain in BondAngle[BoneElectronPair][LonePair]:
                    return BondAngle[BoneElectronPair][LonePair][ElectronDomain]
        return []
    def BetweenSubSystems(SubSys1,SubSys2):
        if (len(SubSys1) != len(SubSys2)):
            return -1.0
        P = []
        Q = []
        PQ = []
        for d in range(len(SubSys1)):
            P.append(SubSys1[d]**2)
            Q.append(SubSys2[d]**2)
            PQ.append(SubSys1[d]*SubSys2[d])
        npP = numpy.sqrt(sum(P))
        npQ = numpy.sqrt(sum(Q))
        npPQ = sum(PQ)
        return AnglesCalculator.Radian2Degree(numpy.arccos(npPQ / (npP * npQ)))
    
