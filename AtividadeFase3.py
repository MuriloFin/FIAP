# Nome: Murilo Favoretto Finardi
# RM: 99950


colheita_total = 0
colheita_maquinas_total = 0
desperdicio_manual_total = 0
desperdicio_maquinas_total = 0

for mes in range(1, 13):
    colheita = float(input(f'\nInforme a colheita (em toneladas) para o mês {mes}: '))

    desperdicio_manual = colheita * 0.05
    desperdicio_maquinas = colheita * 0.15

    colheita_manual = colheita - desperdicio_manual
    colheita_maquinas = colheita - desperdicio_maquinas

    desperdicio_manual_total += desperdicio_manual
    desperdicio_maquinas_total += desperdicio_maquinas
    colheita_total += colheita
    colheita_maquinas_total += colheita_maquinas

    print(f'\nMês {mes}.....: {colheita}')
    print(f'Desperdício manual.....: {desperdicio_manual:.2f} toneladas')
    print(f'Desperdício com máquinas.....: {desperdicio_maquinas:.2f} toneladas')


print('\nRELATÓRIO CONSOLIDADO:')
print(f'\nColheita do ano.....: {colheita_total:.2f} toneladas')
print('Projeção de desperdício:')
print(f'Manual: {desperdicio_manual_total:.2f} toneladas')
print(f'Com máquina: {desperdicio_maquinas_total:.2f} toneladas')
