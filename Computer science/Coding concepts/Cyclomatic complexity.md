Cyclomatic complexity is **a measurement developed by Thomas McCabe to determine the stability and level of confidence in a program**. It measures the number of linearly-independent paths through a program module.

Formula: 
```
M = E – N + P

E = the number of edges in the control flow graph   
N = the number of nodes in the control flow graph   
P = the number of connected components
```

Example calculation:
![[cyclomatic_complexity.png.png]]
The graph shows seven shapes(nodes), and seven lines(edges), hence cyclomatic complexity is 7-7+2 = 2.