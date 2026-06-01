# Deutsch-Jozsa Algorithm

## Problem
Given a function $f(x)$ that is either **constant** or **balanced**, determine which one it is.

- **Constant:** $f(x)$ returns the same value (all 0s or all 1s) for every input
- **Balanced:** $f(x)$ returns 0 for exactly half the inputs and 1 for the other half

### Classical vs Quantum
- **Classically:** requires up to $2^{n-1} + 1$ queries in the worst case
- **Quantum:** requires only **1 query** regardless of $n$

## How it Works

### Circuit Steps
1. Initialize ancilla qubit to $|1\rangle$ using X gate
2. Apply H to all qubits → ancilla becomes $|-\rangle$
3. Apply oracle (CNOT from each input qubit to ancilla)
4. Apply H to input qubits again
5. Measure → all $|0\rangle$ = constant, any $|1\rangle$ = balanced

### The Oracle
The oracle computes:
$$|x\rangle|y\rangle \rightarrow |x\rangle|y \oplus f(x)\rangle$$

For a **balanced** oracle, CNOT is applied from every input qubit to the ancilla:
$$\text{CNOT}|+\rangle|-\rangle \rightarrow |-\rangle|-\rangle$$

This causes **phase kickback** — the phase is kicked back to the input qubit instead of flipping the ancilla!

### Why it Works
After the oracle, input qubits are in:
- $|-\rangle$ if $f$ depends on that bit → H gives $|1\rangle$
- $|+\rangle$ if $f$ doesn't depend on that bit → H gives $|0\rangle$

So measuring all $|0\rangle$ means **constant**, any $|1\rangle$ means **balanced**.

## Example
For $n = 3$ with a balanced oracle:

$$|\psi\rangle = \frac{1}{\sqrt{8}}\sum_{x=0}^{7}|x\rangle|-\rangle$$

After measurement, input qubits are **not** all zero → function is **balanced** ✅

## Output
```
Statevector: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, ...]
```
Non-zero amplitude at a non-zero index confirms **balanced function** ✅

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python "Deutsch Jozsa.py"
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy