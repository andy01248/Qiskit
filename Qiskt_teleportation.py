# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:31:28 2020

@author: andy0
"""


from qiskit import *
from qiskit.tools.visualization import plot_histogram #get plot_histogram

circuit = QuantumCircuit(3,3)  #teleportate Q0 to Q2
circuit.draw(output="mpl")

circuit.x(0)
circuit.barrier()
circuit.draw(output="mpl")

#algorithm starts and teleport the Q0 state before barrier
#Make Q1 and Q2 entangled
circuit.h(1)
circuit.cx(1,2)
circuit.draw(output="mpl")

circuit.cx(0,1)
circuit.h(0)
circuit.draw(output="mpl")

circuit.barrier()
circuit.measure([0,1],[0,1]) #measureQ0 and Q1, save to C0 and C1
circuit.draw(output="mpl")

circuit.barrier()
circuit.cx(1,2) 
circuit.cz(0,2)
circuit.measure(2,2)
circuit.draw(output="mpl")


simulator = Aer.get_backend("qasm_simulator")
result = execute(circuit, simulator).result()
plot_histogram(result.get_counts()) #only get the answer that Q2 = Q0
