from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')
n_count = 8
n_work = 4

def qft(qc, n):
    for j in range(n):
        qc.h(j)
        for i in range(j+1, n):
            angle = 2 * np.pi / (2 ** (i - j + 1))
            qc.cp(angle, i, j)
    for i in range(n//2):
        qc.swap(i, n-1-i)

def inverse_qft(qc, n):
    qft_circ = QuantumCircuit(n)
    qft(qft_circ, n)
    inverse = qft_circ.inverse()
    qc.append(inverse, range(n))
    return qc.decompose()

def c_amod15(a, power, control, targets):
    U = QuantumCircuit(4)
    for _ in range(power):
        if a == 7:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
            U.x(0)
            U.x(1)
            U.x(2)
            U.x(3)
    gate = U.to_gate()
    gate.name = f"{a}^{power} mod 15"
    controlled_gate = gate.control(1)
    qc.append(controlled_gate, [control] + targets)

qc = QuantumCircuit(n_count + n_work, n_count)

for i in range(n_count):
    qc.h(i)

qc.x(n_count)

for i in range(n_count):
    c_amod15(7, 2**i, i, list(range(n_count, n_count + n_work)))

qc = qc.decompose()
qc = inverse_qft(qc, n_count)
qc.measure(range(n_count), range(n_count))

backend = AerSimulator()
result = backend.run(qc, shots=1000).result()
counts = result.get_counts()
# top 10 most frequent
top10 = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10])
print("Top 10 results:", top10)
print()
print("Counts:", counts)
import math
a = 7
r = 4
print(math.gcd(a**(r//2) - 1, 15))  # should give 3
print(math.gcd(a**(r//2) + 1, 15))  # should give 5