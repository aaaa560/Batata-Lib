from potato.geral import mostra, CORES

for tipo in CORES:
    mostra(tipo, end=': ')
    for cor in CORES[tipo]:
        mostra(cor, end=', ')
    mostra()
