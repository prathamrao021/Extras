# Gossip Protocol
## DOSP Project 2

### Team Members
- Pratham Rao
- Pankaj Nitin Warke
- Indu Potla
- Suchithra Macha

### Steps to run the program
1. Move to the project directory
2. Run the following command: ```donet run <numNodes> <topology> <algorithm>```

### Gossip Algorithm
Our goal with the gossip protocol is to spread a message or messages to every node in a network. The counter and the topology make up the two primary parts of our gossip system. Every node that has converged is tracked by the counter. Every time all the nodes converge, it also ends the system as a whole. The configuration of every node in the system is described by the topology. In our approach, a scheduler is started to regularly invoke the actor whenever a node gets a message for the first time (Initialization). The actor chooses a random neighbor for each round and propagates the message within until either a specific node terminates, or the system as a whole converges. The convergence and termination conditions are configured as follows: 
- Convergence condition: Upon receiving the message at least once, the node is considered to have converged. When every node receives the message at least once, the system as a whole converges.
- Termination condition: A node transmits a message after convergence until it receives it nine times or more. Maintaining an actor's sanity following convergence contributes to the system's overall convergence. Concurrently, the termination condition facilitates effective network overhead management resulting from actor space. It is essential that the overhead on the network increases with the number of nodes. 

### Push Sum Algorithm
The goal of push sum is to determine the average or total of all the nodes' values inside a network. The way we build our push sum technique to compute the average is as follows. It initiates a scheduler and transmits the pair (si, wi) to itself in the first round. In this case, wi is initialized to 1 for each node, and si is the node value xi. The total of all the messages si received in time step t-1 is updated at each succeeding time step t. The procedure for calculating wi values is the same. A neighbor is now chosen at random. The si and wi values are then divided in half. Then, half is sent to the neighbor and the other half is delivered to the sender. Each actor at a particular round likewise verifies its s/w value. When there is less than 10^-10 difference between the previous 10 (count) consecutive S/W values, the actor converges and ceases to participate in the next rounds. We experimented with various count numbers, varying from 3 to 15. Nodes at 3 converged fast, but precision was poor. At 15, though, both the accuracy and the time it took for a node to converge were high. Hence, we selected 10 out count value. 

### What is working?
All the topologies have successfully converged various number of nodes.

### What is the largest network you managed to deal with for each type of topology and algorithm?

For Gossip Algorithm

| Topology | Largest Ntwork Size |
| -------- | ------------------- |
| Line | 15000 |
