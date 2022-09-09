# Trello_Progress_Tracker_Bot
Um bot para analisar o progresso das Tarefas da Matéria de Projeto Integrador I e gerar os Reports requisitados pelos professores

## O que será analisado
No trello existem 2 tipos de etiqueta: Dificuldade e Critério

- Dificuldade: uma tag com uma escala de 10 até 100
- Critério: Enumeração dos critérios especificados no PDF do problema a ser abordado

## Objetivo do Bot
Pegar os dados do trello atravez da API e gerar:
- Um gráfico da pontuação feita acumulada e da pontuação estimada acumulada (ambos em relação ao tempo)
- Uma lista de critérios e quais tarefas estão os abordando
