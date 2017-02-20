        
import Atoms
import Astronomy
import Subsystems
import datetime

#%%   P = 4i + 0j + 7k and Q = -2i + j + 3k
print(Subsystems.BetweenSubSystems([4,0,7],[-2,1,3]))

print(Atoms.BetweenAtoms(2,2,4))


print (Astronomy.GetSolarPosition(31.78734, 35.18145,datetime.datetime.now()))
