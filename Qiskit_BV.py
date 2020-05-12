# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:49:28 2020

@author: andy0
"""

from qiskit import *
from qiskit.tools.visualization import plot_histogram

serectnumber = '1000'
circuit = QuantumCircuit (len(serectnumber)+1,len(serectnumber))
#circuit.h([0,1,2,3,4,5])
circuit.h(range(len(serectnumber)))
circuit.x(len(serectnumber))
circuit.h(len(serectnumber))
circuit.barrier()

#The secret number representation
for index, value in enumerate(reversed(serectnumber)):
    if value == '1':
        circuit.cx(index, len(serectnumber))

# circuit.cx(5,6)
# circuit.cx(3,6)
# circuit.cx(0,6)

circuit.barrier()
circuit.h(range(len(serectnumber)))

circuit.barrier()
circuit.measure(range(len(serectnumber)),range(len(serectnumber)))

circuit.draw(output="mpl")

simulator = Aer.get_backend("qasm_simulator")
result =  execute(circuit, simulator, shots = 1000).result()  #1 attempt
plot_histogram(result.get_counts())

IBMQ.load_account()
provider = IBMQ.get_provider("ibm-q")                   #Choose the actual quatnum computer provider
qcomp = provider.get_backend("ibmq_london")        #get the actual quantum compter as backend
job = execute(circuit,backend=qcomp)                    #assign the job sending to the quantum computer to run
from qiskit.tools.monitor import job_monitor
job_monitor(job)                                        #to monitor the current job status since it maybe queed. 
answer_q = job.result()
plot_histogram(answer_q.get_counts(circuit))