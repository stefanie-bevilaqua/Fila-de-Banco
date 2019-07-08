#_______________________Fila__de__Banco___________________________

fila_prioritaria = []
fila_gestante = []
fila_normal = []
escolha = int(input("Digite 1 para executar ou 2 para adicionar alguém em uma fila: "))

while escolha != 1:
    print("Em qual fila você quer entrar?")
    print("="*50)
    print ("1-Fila prioritária, 2-Fila gestante, 3-Fila normal")
    print("="*50)
    decisao = int(input("Digite aqui sua decisão: "))
    if decisao == 3:
        fila_normal.append("§")
        print("Fila prioritária: ",fila_prioritaria)
        print("Fila gestante: ",fila_gestante)
        print("Fila normal: ",fila_normal)
    elif decisao == 2:
        fila_gestante.append("§")
        print("Fila prioritária: ",fila_prioritaria)
        print("Fila gestante: ",fila_gestante)
        print("Fila normal: ",fila_normal)
    elif decisao == 1:
        fila_prioritaria.append("§")
        print("Fila prioritária: ",fila_prioritaria)
        print("Fila gestante: ",fila_gestante)
        print("Fila normal: ",fila_normal)

    print("="*50)
    escolha = int(input("Digite 1 para executar ou 2 para adicionar alguém em alguma fila: "))
else:
    del fila_prioritaria
    fila_prioritaria = []
    print("Fila prioritária: ",fila_prioritaria)
    print("Fila gestante: ",fila_gestante)
    print("Fila normal: ",fila_normal)
    print("="*50)
    del fila_gestante
    fila_gestante = []
    print("Fila prioritária: ",fila_prioritaria)
    print("Fila gestante: ",fila_gestante)
    print("Fila normal: ",fila_normal)
    print("="*50)
    del fila_normal
    fila_normal = []
    print("Fila prioritária: ",fila_prioritaria)
    print("Fila gestante: ",fila_gestante)
    print("Fila normal: ",fila_normal)
