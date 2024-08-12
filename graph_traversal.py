import networkx as nx
import matplotlib.pyplot as plt


# Create a graph
G = nx.Graph()

# Add nodes with weights
G.add_node('A', weight=0)
G.add_node('B', weight=0)
G.add_edge('A', 'B', weight=10)
G.add_node('C', weight = 0)
G.add_edge('B','C',weight = 5)
G.add_node('D', weight = 0)
G.add_edge('A','C',weight = 1)
G.add_edge('B','D',weight = 7)
G.add_node('E', weight = 0)
G.add_edge('E','C',weight = 2)
G.add_node('F', weight = 0)
G.add_edge('F','C',weight = 8)
G.add_edge('D','E',weight = 0)
# Get edge weights for visualization
weight = nx.get_edge_attributes(G, 'weight')




# if edge_weights[('B','D')] > edge_weights[('D','E')]:

# Draw the graph
pos = nx.spring_layout(G)

nx.draw(G, pos,with_labels = True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
plt.show()

G.nodes['D']['color'] = 'black'

def algo(G, S):
    distance = {v: float('inf') for v in G}
    previous = {}
    distance[S] = 0

    unvisited = set(G)
    unvisited.remove('F')

    while unvisited:
        U = min(unvisited, key=lambda v: distance[v])

        unvisited.remove(U)


        # U is the current node
        #v is the target node you are trying to reach.

        #weight is the weight connecting U to v.
        
        for v in G[U]:
            weight = G[U][v]['weight']
            print(f"Processing weight {U}:{weight}:{v}")  # Debugging line
            # The line of code is checking if the path through node U to node v is shorter than the previously known shortest path to v. If it is, it updates the shortest path estimate for v to this new shorter distance.


            if distance[U] + weight < distance[v]:
                
                distance[v] = distance[U] + weight
                previous[v] = U

                
                                                                                                  
                
                

            
            if v == 'D':
                
                return 'found'
                
                
                





algo(G, 'F')
