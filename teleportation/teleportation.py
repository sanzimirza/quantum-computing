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
    print("Statevector:", [round(float(x.real),3) for x in sv]) #prints the real part of all the amplitudes

qc = QuantumCircuit(3)

#bellstate AB
qc.h(1)
qc.cx(1,2)

#hadamard on q0 or x gate. This is the qubit that will be teleported
qc.x(0)

#Alice's Qubit Q
qc.cx(0,1)
qc.h(0)

#Bob's corrections
qc.cx(1,2)  #if q1 is 1 apply x to q2
qc.cz(0,2)  #if q0 is 1 apply z to q2

run_and_print(qc,"bell")