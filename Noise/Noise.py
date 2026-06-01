
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

#Grover's Algorithm

n = 2

qc = QuantumCircuit(n) #no ancilla

for i in range (n):
    qc.h(i)

# ORACLE
qc.cz(0,1)

#Diffusion Operator
qc.h(range(n))
qc.x(range(n))
qc.h(n-1)
qc.cx(0, n-1)
qc.h(n-1)
qc.x(range(n))
qc.h(range(n))

run_and_print(qc,"Grover's Algorithm")



from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer import AerSimulator

# create noise model
noise_model = NoiseModel()

# add depolarizing error to single qubit gates
error_1q = depolarizing_error(0.15, 1)  # 15% error rate
noise_model.add_all_qubit_quantum_error(error_1q, ['h', 'x', 'z'])

# add depolarizing error to two qubit gates
error_2q = depolarizing_error(0.4, 2)  # 40% error rate
noise_model.add_all_qubit_quantum_error(error_2q, ['cx', 'cz'])

# create noisy simulator
noisy_sim = AerSimulator(noise_model=noise_model)

# run on perfect simulator
perfect_result = sim.run(qc).result()

# run on noisy simulator
noisy_result = noisy_sim.run(qc, shots=1000).result()
counts = noisy_result.get_counts()
print("Noisy results:", counts)

# make a copy of the circuit with measurements for noisy simulation
qc_measure = qc.copy()
qc_measure.measure_all()

# run on noisy simulator
noisy_result = noisy_sim.run(qc_measure, shots=10000).result()
counts = noisy_result.get_counts()
print("Noisy results:", counts)                                                                                                                                                                                                                                                                                                    
