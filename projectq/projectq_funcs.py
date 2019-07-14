from projectq import MainEngine, ops
from projectq.ops import All, CNOT, H, Measure, X, Y, Z, Tensor, QFT
from projectq.ops import All, Measure, QubitOperator, TimeEvolution

import math
eng = MainEngine()  # create a default compiler (the back-end is a simulator)

def create_bell_pair(eng):
  b1 = eng.allocate_qubit()
  b2 = eng.allocate_qubit()
  H | b1
  CNOT | (b1, b2)
  return b1, b2

def int_qubits(qubits):
  num=len(qubits)
  
  L=[]
  for i in range(num):
    L.append(int(qubits[i]))
    
  return L

def percentage(results, n_bit):
  import math
  n_re=len(results)
  
  possible=[]
  
  num=int(math.pow(2, n_bit))
  for i in range(num):
    b=bin(i)[2:]
    temp=[]
    for i in range(len(b)):
      temp.append(int(b[i]))
    if(len(b)<n_bit):
      while(len(temp)!=n_bit):
        temp=[0]+temp
    possible.append(temp)
  
  p=[]
  for i in range(num):
    p.append(i)
    p[i]=0
    
  for re in results:
    try:
      n=possible.index(re)
      p[n]=p[n]+1
    except:
      pass
  
  for i in range(num):
    p[i]=p[i]/len(results)*100
  
  return possible, p
