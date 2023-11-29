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
