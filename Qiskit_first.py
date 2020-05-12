# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:20:43 2020

@author: andy0
"""
import qiskit
from qiskit import *       #* means everything
from qiskit.tools.visualization import plot_histogram #get plot_histogram

qr = QuantumRegister(2)    #2 qubits quantum register
cr = ClassicalRegister(2)  #2 bits classical register
circuit = QuantumCircuit(qr,cr) #create quantum circuit with register
circuit.draw(initial_state=True)

#%%

circuit.h(qr[0])               #hadamard gate on qubit q0_0
circuit.draw(output="mpl")
circuit.cx(qr[0],qr[1])        #CNOT gate control qubit q0_0 target qubitq0_1
circuit.draw(output="mpl")
circuit.measure(qr,cr)         #Add measure action on circuit to save qubit results in classcial register
circuit.draw(output="mpl")

simulator=Aer.get_backend("qasm_simulator")  #choose to use the quantum simuilator and run on local computer. simulator name -> qasm_simulator
answer = execute(circuit,backend = simulator).result()      #execute the circuit with backend is simulator
plot_histogram(answer.get_counts(circuit))                # plot the histogram of results of this circuit

IBMQ.load_account()
provider = IBMQ.get_provider("ibm-q")                   #Choose the actual quatnum computer provider
qcomp = provider.get_backend("ibmq_london")        #get the actual quantum compter as backend
job = execute(circuit,backend=qcomp)                    #assign the job sending to the quantum computer to run
from qiskit.tools.monitor import job_monitor
job_monitor(job)                                        #to monitor the current job status since it maybe queed. 
answer_q = job.result()
plot_histogram(answer_q.get_counts(circuit))

