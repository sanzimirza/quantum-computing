# Quantum Fourier Transform (QFT)

## What is QFT?

The Quantum Fourier Transform is the quantum equivalent of the classical 
Discrete Fourier Transform (DFT). It transforms a quantum state from the 
**computational basis** to the **Fourier basis**.

For an input state $|x\rangle$, QFT produces:

$$\text{QFT}|x\rangle = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i xk/N} |k\rangle$$

Where $N = 2^n$ for $n$ qubits.

## Why is it Important?

QFT is a building block for some of the most powerful quantum algorithms:
- **Shor's Algorithm** — factors large numbers exponentially faster than classical
- **Quantum Phase Estimation** — used in VQE for chemistry simulation
- **Hidden Subgroup Problems** — general framework for many quantum speedups

### Classical vs Quantum
- **Classical DFT:** $O(N \log N)$ operations
- **QFT:** $O(\log^2 N)$ operations — **exponential speedup**!

## How it Works

### Circuit Steps
For each qubit $j$ from $0$ to $n-1$:
1. Apply **H gate** to qubit $j$
2. Apply **controlled phase rotations** from all qubits $i > j$:

$$\text{CP}\left(\frac{2\pi}{2^{i-j+1}}\right)$$

3. Apply **SWAP gates** at the end to fix bit ordering

### Phase Rotations
The angles for controlled phase gates are:
- $k=2$: $\frac{\pi}{2}$
- $k=3$: $\frac{\pi}{4}$  
- $k=4$: $\frac{\pi}{8}$

### Key Insight
The input number determines how fast the phase rotates across output states. 
For input $|x\rangle$, the phase at output $|k\rangle$ is $e^{2\pi i xk/N}$ — 
the input number $x$ is the **frequency** of the phase oscillation!

## Example

Input state: $|0101\rangle$ (number 5 in decimal)

After QFT, all 16 amplitudes have **equal magnitude** $\frac{1}{\sqrt{16}} = 0.25$ 
but **different phases** encoding the number 5.

## Output
```
Statevector: [(0.25-0j), (0.25-0j), (-0.25+0j), (-0.25+0j), 
              0.25j, 0.25j, (-0-0.25j), (-0-0.25j), 
              (-0.177-0.177j), (-0.177-0.177j), (0.177+0.177j), 
              (0.177+0.177j), (0.177-0.177j), (0.177-0.177j), 
              (-0.177+0.177j), (-0.177+0.177j)]
```
All amplitudes have equal magnitude of $0.25$ ✅  
Different phases encode the input number $5$ ✅

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python "Quantum Fourier Transform.py"
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy