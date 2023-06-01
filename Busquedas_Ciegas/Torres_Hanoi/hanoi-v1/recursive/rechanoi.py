def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        #print("Mover disco 1 de", origen, "a", destino)
        discos[destino].append(discos[origen].pop())
        print(discos)
        return
    hanoi(n-1, origen, auxiliar, destino)
    #print("Mover disco", n, "de", origen, "a", destino)
    discos[destino].append(discos[origen].pop())
    print(discos)
    hanoi(n-1, auxiliar, destino, origen)

n = 5

discos = {'A':[i for i in range(n,0,-1)], 'B': [], 'C': []}
print(discos)
hanoi(n, 'A', 'C', 'B')
