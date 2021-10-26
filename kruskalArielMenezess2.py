
nV , nA  = input().split()
nV = int(nV)
nA = int(nA)
# nV is the number of vertices in the undirected graph
# nA is the number of edges in the undirected graph
orded_edge_vector = []
#orded_edge_vector is the list of lists with contain the edges ordered by their cost


def ord_per_cost(heap,vector):
    """
    heap is the vector of vectors with contain the cost and vertice one and two
    vector is the vector with coitan the cost and vertice one and two
    """ 
    heap.append(vector)        
    heap.sort()
            

for i in range(nA):
    """[this for read the inputs v1,v2,c ... v1 is the vertice one of the pair of vertices taht makes the
        edge, v2 is the vertice two of that pair and c is the cost of the edge traveling from vertice one
        to vertice two and vice versa.]

    Args:
        aux ([list]): [aux is the auxiliar thats guard the v1,v2,c, and the second input of the 
                        ord_per_cost function]
        v1 ([int]): [is the vertice one]
        v2 ([int]): [is the vertice two]
        c  ([int]): [is the cost of the edge v1,v2]
    """
    aux = []
    v1,v2,cust = input().split()
    cust = int(cust)
    v1 = int(v1)
    v2 = int(v2)
    aux.append(cust)
    aux.append(v1)
    aux.append(v2)
    ord_per_cost(orded_edge_vector,aux)
    

vertice = [[] * nV for i in range(nV)]
#vertice is the list with contain the vertices of the undirected graph
# in this moment is full of empty lists

 
for i in range(nV):
    vertice[i].append(i)
#in this for the vertice become to be populated with the vertice from 0 to nv-1
   

components = []
#components is the list that indicated what tree the vertice belongs
for i in range(nV):
    components.append(i)
#in this for like the other the components become to be populated with the vertice what they belong
    
    
cont = 0
#cont is the amount of interactions of the list of vectors until they became one single tree
cost = 0
#cost is the sum of all the cost of the vertices with the algorithm pass to create the final tree
vPé = 0
while cont < nV-1:
    c,v1,v2  = arestas_ord_valor.pop(vPé)
    if componenetes[v1] != componenetes[v2]:
        cost = cost + c
        comp1 = componenetes[v1]
        comp2 = componenetes[v2]
        if comp2 <= comp1:
            comp1, comp2 = comp2, comp1
        for i in vertice[comp2]:
            componenetes[i] = comp1
        vertice[comp1].extend(vertice[comp2])
        vertice[comp2] = []
        cont += 1
        print(vertice)
        print(componenetes)
        
print(f"custo={cost}")        
    
    
    
    
    
    
    
    
    
