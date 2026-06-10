# Grover's Algorithm

## Problem
Given an unsorted database of $N$ items, find the marked item.

- **Classically:** requires $O(N)$ queries on average
- **Quantum:** requires only $O(\sqrt{N})$ queries — **quadratic speedup**

## How it Works

Grover's algorithm works by repeatedly applying two operations:

### 1. Oracle
Flips the phase of the target state:
$$|x\rangle \rightarrow -|x\rangle \text{ if } x = \text{target}$$

For searching $|11\rangle$, the oracle is simply:
$$\text{CZ}|11\rangle \rightarrow -|11\rangle$$

### 2. Diffusion Operator
Reflects all amplitudes around the average:
$$\text{new amplitude} = 2\langle\psi\rangle - \text{old amplitude}$$

Mathematically this is:
$$2|\psi\rangle\langle\psi| - I$$

The gate sequence is:
$$H \rightarrow X \rightarrow H \rightarrow CX \rightarrow H \rightarrow X \rightarrow H$$

### Circuit Steps
1. Apply H to all qubits → equal superposition
2. Apply oracle → flip phase of $|11\rangle$
3. Apply diffusion operator → amplify $|11\rangle$
4. Measure → get $|11\rangle$ with high probability

## Why it Works

After oracle, amplitudes are:
$$|00\rangle = 0.5, \quad |01\rangle = 0.5, \quad |10\rangle = 0.5, \quad |11\rangle = -0.5$$

Average $= 0.25$

After diffusion:
$$\text{new}_{|11\rangle} = 2(0.25) - (-0.5) = \boldsymbol{1.0}$$
$$\text{new}_{|00\rangle} = 2(0.25) - (0.5) = \boldsymbol{0.0}$$

$|11\rangle$ gets **100% probability** in just 1 iteration! ✅

## Example
Searching for $|11\rangle$ in a 2-qubit system:

For $n = 2$, only **1 iteration** is needed.

## Output
```
Statevector: [0.0, 0.0, 0.0, -1.0]
```
Amplitude of $-1.0$ at index 3 = $|11\rangle$ ✅

The negative sign is a global phase and doesn't affect measurement.

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python "Grover's Algorithm.py"
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy
