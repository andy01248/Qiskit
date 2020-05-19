# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:00:54 2020

@author: andy0
"""
#Deutsch Jozsa Algorithm  -- balanced circuit always 11 constant circuit always 00

from qiskit import *
import math
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.visualization import plot_histogram 

statevector_simulator = Aer.get_backend("statevector_simulator")
qasm_simulator = Aer.get_backend("qasm_simulator")

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

def balanced_black_box(circuit):
    circuit.cx(0,2)
    circuit.cx(1,2)
    return circuit

def constant_black_box(circuit):
    return circuit
#%%Build the circuit  -- just uncertain qubits    
circuit = QuantumCircuit(2,2) 
circuit.ry(math.pi/4 ,0)
circuit.ry(math.pi/4 ,1)

statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts

#%%Build the circuit  -- hadamard in front of uncertain qubits    
circuit = QuantumCircuit(2,2) 
circuit.h(0)
circuit.h(1)
circuit.ry(math.pi/4 ,0)
circuit.ry(math.pi/4 ,1)

statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts

#%%Build the circuit  -- hadamard sandwich on uncertain qubits    
circuit = QuantumCircuit(2,2) 
circuit.h(0)
circuit.h(1)
circuit.ry(math.pi/4,0)
circuit.ry(math.pi/4 ,1)
circuit.h(0)
circuit.h(1)

statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts

#%%Build the circuit  -- just certain qubits    
circuit = QuantumCircuit(2,2) 
circuit.x(0)
circuit.x(1)

statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts

#%%Build the circuit  -- hadamard sandwich on certain qubits    
circuit = QuantumCircuit(2,2) 
circuit.h(0)
circuit.h(1)
circuit.x(0)
circuit.x(1)
circuit.h(0)
circuit.h(1)
statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts

#%%  on balanced circuit
circuit = QuantumCircuit(3,3)
circuit.x(2)
circuit.h([0,1,2])
circuit.barrier()
circuit = balanced_black_box(circuit)
circuit.barrier()
circuit.h([0,1,2])
statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts

#%%
circuit = QuantumCircuit(3,3)
circuit.x(2)
circuit.h([0,1,2])
circuit.barrier()
circuit = constant_black_box(circuit)
circuit.barrier()
circuit.h([0,1,2])
statevec, counts = do_job(circuit)
circuit.draw(output='mpl')
plot_bloch_multivector(statevec)
plot_histogram(counts) #Meausre is related to counts