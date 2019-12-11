# CMSI-385-TOC

I've chosen to implement a NFA Simulator in Python which would take in the description of an NFA and a string, then return whether or not the string is in the language of the NFA.

Input should be formatted as such:<br/>
// Start State<br/>
A

// Accept States<br/>
A B

// Transitions (as 3-tuples)<br/>
A 0 B<br/>
A 1 A<br/>
B 1 A<br/>
*enter blank line to indicate end of input*

// String to test<br/>
1001
