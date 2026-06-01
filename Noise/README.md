# Quantum Noise and Decoherence

A demonstration of how quantum noise affects Grover's Algorithm using depolarizing noise.

## What is Quantum Noise?

In real quantum computers, qubits interact with their environment and lose their quantum properties over time. This is called **decoherence**.

### Types of Noise
- **Bit flip error** — qubit randomly flips from $|0\rangle$ to $|1\rangle$
- **Phase flip error** — qubit's phase gets flipped ($|+\rangle$ becomes $|-\rangle$)
- **Depolarizing noise** — qubit randomly gets any error with some probability
- **Amplitude damping** — qubit decays from $|1\rangle$ to $|0\rangle$

### T1 and T2 Times
- **T1** — how long before qubit decays from $|1\rangle$ to $|0\rangle$
- **T2** — how long before qubit loses its phase information
- Real IBM qubits have T1/T2 of around **100 microseconds**

## Depolarizing Noise Model

The depolarizing channel applies a random error with probability $p$:

$$\mathcal{E}(\rho) = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)$$

### Noise Levels Used
- **Single qubit gates** (H, X, Z): 15% error rate
- **Two qubit gates** (CX, CZ): 40% error rate

## Results

### Perfect Simulator
```
Statevector: [0.0, 0.0, 0.0, -1.0]
```
$|11\rangle$ found with **100% probability** ✅

### Low Noise (1% / 5%)
```
Noisy results: {'11': 1.0}
```
Still gets correct answer ✅

### High Noise (15% / 40%)
```
Noisy results: {'01': 2364, '00': 2240, '11': 3046, '10': 2350}
```
Results are nearly **random** — algorithm is useless! ❌

## Why This Matters

This demonstrates why **quantum error correction** is essential for real quantum computers. Without it, noise makes results unreliable even for simple circuits.

Real IBM quantum hardware has noise levels that make results unreliable without error correction — this is the key challenge of the **NISQ (Noisy Intermediate-Scale Quantum)** era.

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python Noise.py
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy