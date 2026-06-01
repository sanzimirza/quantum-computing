# Quantum Gates

A demonstration of fundamental quantum gates using Qiskit.

## Gates Implemented

### 1. X Gate (NOT Gate)
The quantum equivalent of a classical NOT gate. Flips $|0\rangle$ to $|1\rangle$ and vice versa.

$$X|0\rangle = |1\rangle \qquad X|1\rangle = |0\rangle$$

**Output:**
```
Statevector: [0.0, 1.0]
```
Qubit flipped from $|0\rangle$ to $|1\rangle$ ✅

---

### 2. H Gate (Hadamard Gate)
Creates **superposition** — puts a qubit in an equal combination of $|0\rangle$ and $|1\rangle$.

$$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}} = |+\rangle$$

**Output:**
```
Statevector: [0.707, 0.707]
```
50% chance of measuring $|0\rangle$, 50% chance of measuring $|1\rangle$ ✅

---

### 3. CNOT Gate
A two-qubit gate. Flips the **target** qubit if the **control** qubit is $|1\rangle$.

$$\text{CNOT}|10\rangle = |11\rangle \qquad \text{CNOT}|00\rangle = |00\rangle$$

Combined with H gate, creates a **Bell State** (maximally entangled state):

$$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

**Output:**
```
Statevector: [0.707, 0.0, 0.0, 0.707]
```
Qubits are entangled — measuring one instantly determines the other ✅

---

### 4. Toffoli Gate (CCX)
A three-qubit gate. Flips the **target** qubit only if **both** control qubits are $|1\rangle$.

$$\text{CCX}|110\rangle = |111\rangle$$

This is the quantum equivalent of an **AND gate**:
$$\text{target} = \text{target} \oplus (\text{control}_1 \wedge \text{control}_2)$$

**Output:**
```
Statevector: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
```
Amplitude of $1.0$ at index 7 = $|111\rangle$ ✅

---

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python gates.py
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy