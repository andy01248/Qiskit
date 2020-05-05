# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:20:43 2020

@author: andy0
"""
import qiskit
from qiskit import *       #* means everything

#%%

qr = QuantumRegister(2)    #2 qubits quantum register
cr = ClassicalRegister(2)  #2 bits classical register
circuit = QuantumCircuit(qr,cr) #create quantum circuit with register
circuit.draw()






#%%
