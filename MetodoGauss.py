import copy

def MetodoDeEliminacao(A,b):
  n = len(b)
  # Calculo dos pivos.
  for k in list(range(1,n)):
    # Calculo dos multiplicadores.
    for i in list(range(k+1,n+1,1)):
        if A[k-1][k-1] != 0:
            m = A[i-1][k-1]/A[k-1][k-1]
        A[i-1][k-1] = 0
        b[i-1] = b[i-1] - m*b[k-1]
        # Atualizar demais valores da linha
        for j in list(range(k+1,n+1)):
            A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1] 
  return A,b

# Resolve o sistema triangular superior.
def triangular(U,b):
  n = len(b)
  x = [0]*n
  if U[n-1][n-1] != 0:
      x[n-1] = b[n-1]/U[n-1][n-1]
 

  for i in list(range(n-1,0,-1)):
    s = 0
    for j in list(range(i+1,n+1,1)):
      s = s + U[i-1][j-1]*x[j-1]

    if (U[i-1][i-1]) != 0:
        x[i-1] = (b[i-1]-s)/(U[i-1][i-1])
    
  return x




def CriaMatriz(linhas, colunas):
        
    # Teste com dados.
  
    
    matriz = []
    bi = []
    for i in range(linhas):
        linhaM = []
        for j in range(colunas):
            linhaM.append(float(input("Digite o elemento da °%i linha e °%i Coluna: "% (i+1, j+1) )))
        matriz.append(linhaM)

    for i in range(colunas):
        bi.append(float(input("Digite os valores de B: ")))

    return matriz, bi

def imprimeMatriz(U,b,x,linhas, colunas):
        
    print("U = " )
    for i in range(linhas):
        for j in range(colunas):
            if round(float(U[i][j]),2) < 0:
                print("      ",round(float(U[i][j]),2), end = ' ')
            else:
                print("       ",round(float(U[i][j]),2), end = ' ')

        print()

    print()
    cont = 1
    for i in b:
        print("Y%i = %.2f"%(cont, i))
        cont +=1
        
    print()
    cont = 1
    for i in x:
        print("X%i = %.2f"%(cont, i))
        cont +=1






print("Metodo De Gauss")
linhas = int(input("Digite a quantidade de Linhas da matriz: "))
colunas = int(input("Digite a quantidade de Colunas da matriz: "))
'''
matriz = [[5, -2, 6, 1],
      [0, 3, 7, -4],
      [0, 0, 4, 5],
      [0, 0, 0, 2]]

bi = [1, -2, 28, 8]


matriz = [[1, 4, 1],
      [1, 6, -1],
      [2, -1,2]]


#matriz = CriaMatriz(linhas, colunas)

bi = [7, 13, 5]

bi = [1,1,-3,4]

matriz = [[1, 1, 0,3],
      [2,1,-1,1],
      [3,-1,-1,2],
          [-1,2,3,-1]]

matriz = [[2,1,3],
          [4,2,2],
          [2,-5,3]]

bi = [8,4,-12]

matriz = [[1,4,5],
          [4,18,26],
          [3,16,30]]

#bi = [6,0,-6]
bi = [6,6,12]


matriz = [[1,2,4,17],
          [3,6,-12,3],
          [2,3,-3,2],
          [0,2,-2,6]]

bi = [17,3,3,4]
'''
matriz = [[2,2,2],
          [4,7,7],
          [6,18,22]]

bi = [6,24,70]
U,b = MetodoDeEliminacao(matriz,bi)
x = triangular(U,b)

imprimeMatriz(U,b,x, linhas, colunas)


