# Relatório sobre a apresentação do algoritmo boruvka
## Nome: Ariel araujo Oliveira Menezes
## RA: 101911203

----------------------------------------------------------------
### Fiz a apresentação do algoritmo boruvka que é um algoritmo derivado do algoritmo kruskal. 


### Ele pode ser implementado de forma recursiva, não utiliza de uma lista de arestas ordenada pelo custo como o kruskal faz, no caso do boruvka ele olha cada vertice a ligação de menor custo, ou seja, ele olha o menor caminho e se liga ao veritce no final desse caminho.

### Boruvka olha os vertices em ordem crescente e em caso do vertice ter mais de uma ligação com o mesmo custo ele pode ter duas abordagens para escolher entre o empate, pode-se escolher em ordem crescemte ou de forma arbritária. De forma crescente por exemplo se estou no vertice 5 e as arestas 5,6 e 5,4 tem mesmo custo 4, então escolhendo em ordem crescente o algoritmo escolhe o vertice 4, ou seja, aresta 5,4.

------------------------------------------------
## representação gráfica:

* ### Aqui está um grafo valorado antes da execução do boruvka:
    <img src="grafimgs/grafo1.png">
-----------------------------------------------
* ## A primeira iteração do algoritmo de boruvka fica:
    * ### Aqui está a primeira irteração e o mapeamento de cada vertice procurando a aresta de custo minimo ligada a ele:
        * #### Aqui temos o vertice A que se ligou como o vertice D por ter o menor custo, aresta A,D == 5:
            <img src="grafimgs/grafo2.png">
        * ### Vertice B empata o custo nas arestas B,A e B,E ambas de custo 7 , usando a escolha em ordem alfabética a aresta escolhida foi B,A==7:
            <img src="grafimgs/grafo3.png">
        
        * ### Vertice C escolhe a aresta C,E de custo 5:
            <img src="grafimgs/grafo4.png">
        * ### O vertice D escolhe a aresta D,A por ter menor custo:
            <img src="grafimgs/grafo3.png">
        * ### o vertice E se liga com o C:
            <img src="grafimgs/grafo4.png">
        * ### O vertice F escolhe a aresta F,D:
            <img src="grafimgs/grafo5.png">
        * ### E por fim o vertice G escolhe a aresta G,E:
            <img src="grafimgs/grafo6.png">
------------------------------------------
* ## Ao final da primeira iteração o grafo fica uma floresta de duas arvores, ou seja temos dois grupos, dois subgrafos:
    #### Temos aas arvores A=vermelho e B=azul
    <img src="grafimgs/floresta.png">
----------------------------------

* ## Já na segunda iteração ele procura o menor caminho entre a arvore A e B e o menor caminho é 7:
    <img src="grafimgs/ArvoreFinal1.png">

* ## Então após sair do looping seja ele recursivo ou iterativo:
    <img src="grafimgs/ArvoreFinal2.png"> <br>
    ### Seu custo é de 5+6+7+7+9+5=39

