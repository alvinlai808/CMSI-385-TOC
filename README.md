# CMSI-385-TOC

I've chosen to implement a NFA Simulator in Python which would take in the description of an NFA and a string, then return whether or not the string is in the language of the NFA.

Input should be formatted as such:
// Start State
A

// Accept States
A B

// Transitions (as 3-tuples)
A 0 B
A 1 A
B 1 A
*enter blank line to indicate end of input*

// String to test
1001
