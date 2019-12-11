# CMSI-385-TOC

I've chosen to implement a NFA Simulator in Python which would take in the description of an NFA and a string, then return whether or not the string is in the language of the NFA.

Input should be formatted as such:

START=q0;ACCEPT=q2,q1

q0:a->q1

q0:a->q2

q0->q2

q0:a->q0
