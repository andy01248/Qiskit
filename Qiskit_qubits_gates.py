# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:18:28 2020

@author: andy0
"""
from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.visualization import plot_histogram #get plot_histogram

#Circuit manipulation
circuit = QuantumCircuit(3,3)  #Create circuit with 1 qubit and 1 bit
circuit.x(0)                   #Give the qubit X gate    (0) means 1st qubit (1) means 2nd qubit

#Show the result in state vector. 
simulator = Aer.get_backend("statevector_simulator")          
job = execute( circuit, simulator)
result = job.result()
statevector = result.get_statevector()
print(statevector)                                         #State vector representation
plot_bloch_multivector(statevector)                        #show vector in bloch
circuit.draw(output="mpl")

#Show the matrix representation of gate 
simulator = Aer.get_backend("unitary_simulator")          
result1 = execute(circuit,simulator).result()
unitary = result1.get_unitary()
print(unitary)                                         #gate matrix representation representation


#Show the measurement result in bits representation and probabilities. 
circuit.measure([0,1,2],[0,1,2])                           #in this representation, measurement is required. 
backend = Aer.get_backend("qasm_simulator")
answer = execute(circuit, backend, shots=2000).result()   #Note that 001 for this case because the last bit is the result of qubit 0.
counts = answer.get_counts(circuit)
plot_histogram(counts)


