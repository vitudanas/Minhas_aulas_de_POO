from pasta_programa import sistema_tv
televisao = Televisao(15,50,100)

decisao_canal = int(input("Deseja mudar canal?"))
if decisao_canal == 'sim':
    televisao.novo_canal_tv = int(input("Digite o canal que deseja"))
    televisao.mudar_canal()

decisao_brilho = int(input("Deseja mudar brilho?"))
if decisao_brilho == 'sim':
    televisao.novo_brilho_tv = int(input("Digite o brilho que deseja"))
    televisao.mudar_brilho()

decisao_volume = int(input("Deseja mudar volume?"))
if decisao_volume == 'sim':
    televisao.novo_volume_tv = int(input("Digite o novo volume:"))
    televisao.mudar_volume()