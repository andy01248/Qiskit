# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:00:49 2020

@author: andy0
"""
import qiskit
qiskit.__qiskit_version__
from qiskit import IBMQ
IBMQ.save_account("f100752084475f7bb23336ec7454e81d42188439a2180a12d7974af695542f4477faf3401cca6747c3e2bbaf6c455e8314e6e8f532652959b25ac7b3f64afbe8")
IBMQ.load_account()