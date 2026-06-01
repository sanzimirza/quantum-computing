# Quantum Teleportation

## What is Quantum Teleportation?

Quantum teleportation transfers the **exact quantum state** of one qubit to another 
qubit at a different location — without physically moving the qubit itself.

> "Teleportation doesn't move matter, it moves information."

### Key Points
- The original qubit is **destroyed** in the process
- Requires a **classical communication channel** (2 classical bits)
- Cannot transfer information faster than light (no FTL communication)
- Demonstrates the power of **quantum entanglement**

## How it Works

### Qubits
- **q_0** — Alice's qubit to teleport (initialized to $|1\rangle$)
- **q_1** — Alice's entangled qubit
- **q_2** — Bob's entangled qubit

### Circuit Steps

**Step 1: Create Bell State between q_1 and q_2**

$$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

q_1 and q_2 are now **entangled** — Alice holds q_1, Bob holds q_2.

**Step 2: Prepare qubit to teleport**

$$q_0 = |1\rangle$$

**Step 3: Alice's operations**

Alice applies CNOT then H to her qubits:
$$\text{CNOT}(q_0, q_1) \rightarrow H(q_0)$$

**Step 4: Bob's corrections (deferred measurement)**

Using the **deferred measurement principle**, classical measurements are 
replaced by quantum controlled gates:

$$\text{CX}(q_1, q_2) \rightarrow \text{CZ}(q_0, q_2)$$

- If $q_1 = 1$ → apply X to $q_2$
- If $q_0 = 1$ → apply Z to $q_2$

After corrections, $q_2$ is in the **exact same state** as the original $q_0$!

## Phase Kickback in Teleportation

The Bell state creates **correlations** between Alice and Bob's qubits. 
Alice's measurement results determine which correction Bob applies:

| $q_0$ | $q_1$ | Bob's correction |
|--------|--------|-----------------|
| 0 | 0 | None |
| 0 | 1 | X |
| 1 | 0 | Z |
| 1 | 1 | XZ |

## Output
```
Statevector: [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5]
```
Non-zero amplitudes only where $q_2 = 1$ ✅  
State of $q_0$ ($|1\rangle$) successfully teleported to $q_2$! ✅

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python teleportation.py
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy