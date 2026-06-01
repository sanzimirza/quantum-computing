# Shor's Algorithm

## What is Shor's Algorithm?

Shor's Algorithm is a quantum algorithm for **integer factorization**. 
It can factor a number $N$ exponentially faster than the best known classical algorithm.

### Classical vs Quantum
- **Classical:** best algorithms run in $O(e^{n^{1/3}})$ — exponential time
- **Shor's:** runs in $O(n^3)$ — **polynomial time**

This makes Shor's Algorithm a **threat to RSA encryption**, which relies on 
factoring being hard classically!

## How it Works

### Goal: Factor $N = 15$

**Step 1: Pick a random number**

Choose $a = 7$ (any number sharing no factors with $N$)

**Step 2: Find the period of $f(x) = a^x \mod N$**

| $x$ | $7^x \mod 15$ |
|-----|---------------|
| 0 | 1 |
| 1 | 7 |
| 2 | 4 |
| 3 | 13 |
| 4 | 1 |
| 5 | 7 |

Period $r = 4$ ✅

**Step 3: Use QFT to find the period**

1. Create superposition of all $x$ values simultaneously
2. Apply modular exponentiation oracle: $|x\rangle|0\rangle \rightarrow |x\rangle|7^x \mod 15\rangle$
3. Apply **inverse QFT** to the counting register
4. Measure → peaks appear at multiples of $\frac{N}{r} = \frac{256}{4} = 64$

**Step 4: Extract factors using the period**

$$\gcd(a^{r/2} - 1, N) = \gcd(7^2 - 1, 15) = \gcd(48, 15) = \mathbf{3}$$
$$\gcd(a^{r/2} + 1, N) = \gcd(7^2 + 1, 15) = \gcd(50, 15) = \mathbf{5}$$

$$3 \times 5 = 15 \checkmark$$

## Circuit Structure

- **Counting register:** 8 qubits (represents $x$ from 0 to 255)
- **Work register:** 4 qubits (stores $7^x \mod 15$)
- **Total:** 12 qubits

### Key Components
1. **H gates** on counting register → equal superposition
2. **Modular exponentiation oracle** → controlled-$U$ gates for $7^x \mod 15$
3. **Inverse QFT** on counting register → extracts period information

## Output
```
Top 10 results: {'00000000': 244, '10000000': 214, '11111111': 198, 
                 '01111111': 98, '01000000': 99, ...}
```

Dominant peaks at:
- `00000000` = 0 ✅
- `01000000` = 64 ✅  
- `10000000` = 128 ✅
- `11000000` = 192 ✅

These are multiples of 64 = $\frac{256}{4}$, confirming period $r = 4$!

```
Factor 1: 3
Factor 2: 5
```
$15 = 3 \times 5$ ✅

## How to Run
```bash
pip install qiskit qiskit-aer numpy
python "Shor's Algorithm.py"
```

## Requirements
- Python 3.8+
- Qiskit
- Qiskit-Aer
- NumPy