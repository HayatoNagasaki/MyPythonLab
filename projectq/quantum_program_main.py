from projectq import MainEngine, ops
from projectq.ops import All, CNOT, H, Measure, X, Y, Z, Tensor, QFT
from projectq.ops import All, Measure, QubitOperator, TimeEvolution
import projectq_funcs as F

def main(n_bits):
  eng = MainEngine()
  q = eng.allocate_qureg(n_bits)  
  a= eng.allocate_qubit()
  
  # Program here ****************
  # EXample of AND gate
  H | q[0]
  H | q[1]
  
  ops.Toffoli  | (q[0], q[1], q[2])
  
  # ***********************************
  All(Measure) | q
  result=F.int_qubits(q)
  
  eng.flush()
  return result[::-1]

n_bits=3
results=[]
for i in range(500):
  results.append(main(n_bits))
  
possible, p = F.percentage(results, n_bits)

print("[q[2], q[1], q[0]]")
for i in range(len(possible)):
  print(possible[i], p[i])
