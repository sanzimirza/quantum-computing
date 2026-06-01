
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

#Bernstein Vazirani Algorithm

n = 4
s = "1011" #take s as a string
srev = s[::-1] #qiskit reverses the s value so we need to counter that
qc = QuantumCircuit(n+1)
qc.x(n)

for i in range (n+1):
    qc.h(i)

# ORACLE
for i in range(n):#CNOT with |−⟩ ancilla = phase kickback to control qubit
    if srev[i] == "1":
        qc.cx(i, n)  # CNOT only where secret bit is 1

for i in range (n):
    qc.h(i)
    
run_and_print(qc,"Bernstein Vazirani Algorithm")

