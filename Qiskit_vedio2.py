# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:15:32 2020

@author: andy0
"""

from qiskit import *
import math
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.visualization import plot_histogram 

statevector_simulator = Aer.get_backend("statevector_simulator")
qasm_simulator = Aer.get_backend("qasm_simulator")

#the job doing function
def do_job(circuit):
    state_result = execute(circuit, backend=statevector_simulator).result()
    statevec = state_result.get_statevector()
    n_qubits = circuit.num_qubits
    try:
        circuit.measure(range(n_qubits),range(n_qubits))
    except:
        circuit.measure(range(circuit.num_clbits), range(circuit.num_clbits))
    qasm_result = execute(circuit , backend = qasm_simulator, shots =1024).result()
    counts = qasm_result.get_counts()
    return statevec, counts

#Build the circuit    
circuit = QuantumCircuit(3,3) 
circuit.h(0)
circuit.h(1)
circuit.ccx(0,1,2)

#Do job and get result
statevec, counts = do_job(circuit)
print(statevec) #Tensor product of all qubits
plot_bloch_multivector(statevec)

#gate is actually phase rotation
circuit = QuantumCircuit(3,1) 
circuit.h(0)
circuit.h(1)
circuit.rx(math.pi,2)  #phase rotation around x axis
#Do job and get result
statevec, counts = do_job(circuit)
print(statevec) #Tensor product of all qubits
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts