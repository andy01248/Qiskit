# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:47:20 2020

@author: andy0
"""

from qiskit import *
from qiskit.visualization import plot_histogram #Can use plot_histogram directly
from qiskit.tools.monitor import job_monitor

#%%
circuit = QuantumCircuit(2,2)
circuit.x(0)
circuit.cx(0,1)
circuit.measure([0,1],[0,1])
circuit.draw(output='mpl')
IBMQ.load_account()
provider = IBMQ.get_provider("ibm-q")

#show the current q_com status
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = "simulated"
        
    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")       
    #print(backend.name() + " has" , backend.status().pending_jobs, "queued and ", qubit_count, "qubits")

#Find the backend with smallest number of queue
q_com = provider.get_backend("ibmqx2")
job = execute(circuit, backend = q_com, shots = 1024)
job_monitor(job)
plot_histogram(job.result().get_counts(), legend = ["q_com result"])

#%%
simulator =  Aer.get_backend("qasm_simulator")
job = execute(circuit, backend = simulator ,shots = 1024)
result = job.result()
counts = result.get_counts()
plot_histogram(counts)