nV , nA  = input().split()
nV = int(nV)
nA = int(nA)
#
arestas_ord_valor = []

def ordenar_per_cost(heap,vector): 
    heap.append(vector)        
    heap.sort()
            

for i in range(nA):
    aux = []
    v1,v2,cust = input().split()
    cust = int(cust)
    v1 = int(v1)
    v2 = int(v2)
    aux.append(cust)
    aux.append(v1)
    aux.append(v2)
    ordenar_per_cost(arestas_ord_valor,aux)
    

vertice = [[] * nV for i in range(nV)]

 
for i in range(nV):
    vertice[i].append(i)
    

componenetes = []

for i in range(nV):
    componenetes.append(i)
    
    
cont = 0
cost = 0
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
    
    
    
    
    
    
    
    
    
