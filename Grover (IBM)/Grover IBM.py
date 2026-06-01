from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit import QuantumCircuit, transpile
import numpy as np

# save your account (only need to do this once)
QiskitRuntimeService.save_account(
    channel="ibm_cloud",
    token="kIEqcQgnnKOfUVpnBzb6prLFYfQru6hQXC4JdtvP-Rvp",  # pasting my API key here
    overwrite=True
)

service = QiskitRuntimeService(channel="ibm_cloud")
backend = service.least_busy(operational=True, simulator=False)
print("Using:", backend.name)

# Grover's circuit
n = 2
qc = QuantumCircuit(n)
for i in range(n):
    qc.h(i)
qc.cz(0, 1)
qc.h(range(n))
qc.x(range(n))
qc.h(n-1)
qc.cx(0, n-1)
qc.h(n-1)
qc.x(range(n))
qc.h(range(n))
qc.measure_all()

# transpile and run
qc = transpile(qc, backend)
sampler = SamplerV2(backend)
job = sampler.run([qc], shots=1000)
result = job.result()
print(result)
print()
# extract counts from result
pub_result = result[0]
counts = pub_result.data.meas.get_counts()
print("Counts:", counts)

# sort by most frequent
sorted_counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
print("Sorted:", sorted_counts)