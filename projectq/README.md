# Quantum computing with Projectq

Some Usuful quantum gates
* Random Numbers (3bits)
```
H | q[0]
H | q[1]
H | q[2]

Al(Measure) | q
```
#
* Not : ![equation](https://latex.codecogs.com/svg.latex?\Large&space;q[0]=\neg{q[0]})
```
X | q[0]
```
#
* AND : ![equation](https://latex.codecogs.com/svg.latex?\Large&space;q[2]=q[1]\wedge{q[0]})
```
ops.Toffoli  | (q[0], q[1], q[2])
```
#
* OR : ![equation](https://latex.codecogs.com/svg.latex?\Large&space;q[2]=q[1]\vee{q[0]})
```
X | q[0]
X | q[1]
ops.Toffoli  | (q[0], q[1], q[2])
```
#
* XOR : ![equation](https://latex.codecogs.com/svg.latex?\Large&space;q[2]=q[1]\oplus{q[0]})
```
X | q[0]
and1 = eng.allocate_qubit()
ops.Toffoli  | (q[0], q[1], and1)
  
X | q[0]
X | q[1]
and2 = eng.allocate_qubit()
ops.Toffoli  | (q[0], q[1], and2)
  
X | and1
X | and2
ops.Toffoli  | (and1, and2, q[2])
```
