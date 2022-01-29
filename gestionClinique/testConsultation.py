from medecin import Medecin
from patient import Patient
from consultation import Consultation

p1 = Patient('Fall','Abdou','77658900','M')
m1 = Medecin('Diagne','Soukeye','097JKL','F')

c1 = Consultation(p1,m1)

print(c1)
