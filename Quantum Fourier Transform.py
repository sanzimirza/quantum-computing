
print("script started")
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

sim = AerSimulator(method = 'statevector') #method = statevector tracks the full statevector

def run_and_print(qc, label):
    
    qc.save_statevector() # after running this circuit save a snapshot of this so that I can review this later
    result = sim.run(qc).result() #submission and fetching of the result
    sv = np.asarray(result.get_statevector())
    #sv = result.get_statevector() # sv is a list of complex numbers (the amplitudes of the collapse states)
    print(f"\n---{label} ---") #prints the heading lol
    print(qc.draw('text')) #draws a nice diagram for your circuit
    print("Statevector:", [complex(round(x.real, 3), round(x.imag, 3)) for x in sv])
     #this line has been changed prints the real part of all the amplitudes

import numpy as np

#Quantum Fourier Transform
n = 4

qc = QuantumCircuit(n)

qc.x(0)
qc.x(2)

qc.h(0)
qc.cp(np.pi/2, 1, 0) #qc.cp(angle, control, target)  
qc.cp(np.pi/4, 2, 0)   
qc.cp(np.pi/8, 3, 0) 

qc.h(1)
qc.cp(np.pi/2, 2, 1)   
qc.cp(np.pi/4, 3, 1)  

qc.h(2)
qc.cp(np.pi/2, 3, 2)  

qc.h(3)

qc.swap(3,0)
qc.swap(2,1)

run_and_print(qc,"QFT")

