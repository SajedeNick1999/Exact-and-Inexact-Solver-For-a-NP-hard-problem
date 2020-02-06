# Exact and Inexact Solver For a NP-hard problem
there is a NP-hard problem in 'AI_3891_PROJECT' and there is two type of solve for it:
1)exact solution : for small instances
2)inexact solution : for big instances
two instance files are added for test
## **Getting started**
you can test each example files and othere files by changing the name of file in codes
### **Prerequisites**
you have to install 'python3' and 'minizinc API for python3'
## **Running**
for small instance type this in terminal :
```shell
$ python3 exact.py
```
and for big instance type this :
```shell
$ python3 walksat.py
```
you can also change the 'FileName' string to run this programs for evary instances you want.

## **About Algorithem**
### **Exact solution** 
for exact program I use 'minizinc API for python3' and 'gecode' solver.
I just read from file then create a CSP instance and run this instance in minizinc.
### **Inexact solution** 
for this program I use somthing like 'walkSAT' approach.
and aslo I have a fittness function that is minimal is optimal solution.

## **Support**
Reach out to me at one of the following places!
- Telegram at <a href="https://t.me/sajede_nick" target="_blank">@sajede_nick</a>
- Gmail at <a href="mailto:sajede.nicknadaf78@gmail.com" target="_blank">sajede.nicknadaf78@gmail.com</a>

## **LICENSE**

[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
