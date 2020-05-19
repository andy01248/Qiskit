# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:58:37 2020

@author: andy0
"""
#use ignis to generate calibration fitter and use fitter to generate filter

from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor


nqubits =3
circuit = QuantumCircuit(nqubits,nqubits)
circuit.h(0)
circuit.cx(0,1)
circuit.cx(1,2)
circuit.measure(range(nqubits),range(nqubits))

circuit.draw(output='mpl')

simulator = Aer.get_backend("qasm_simulator")
result =  execute(circuit, simulator, shots = 1024).result()  #1 attempt
plot_histogram(result.get_counts())

IBMQ.load_account()
provider = IBMQ.get_provider("ibm-q")
qcom = provider.get_backend("ibmq_burlington")
job = execute(circuit, qcom, shots=1024)
job_monitor(job) 
result_q=job.result()
plot_histogram(result_q.get_counts())

## main part!
from qiskit.ignis.mitigation.measurement import (complete_meas_cal, CompleteMeasFitter)
cal_circuits, state_labels = complete_meas_cal(qr = circuit.qregs[0], circlabel = "measerrormitigationcal") #circuit.qregs[0] is the quantum register to show all qubits we have 
#cal_circuits is the calibrated circuit of all qubits possible outcomes, state labels are 000 - 111
cal_job = execute(cal_circuits, qcom, shots=1024, optimization_level = 0)
print(cal_job.job_id())
job_monitor(cal_job) 
result_cal=cal_job.result()
plot_histogram(result_cal.get_counts())

#Build the measurement fitter which extracts the parameters from calibration results
meas_fitter = CompleteMeasFitter(result_cal, state_labels) #fit the calibrated results with actucal labels
meas_fitter.plot_calibration()

#Make the calibration filter to mitigate the results
#This filter can be used for other 3 qubuits circuit
meas_filter = meas_fitter.filter
result_mitigated = meas_filter.apply(result_q) #Generate mitigated result by applying filter to the quantum computer result

#get result
counts_q = result_q.get_counts()
counts_mitigated = result_mitigated.get_counts()
plot_histogram([counts_q, counts_mitigated], legend = ["noisy result",'mitigated result'])





