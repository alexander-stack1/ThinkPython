#!/usr/bin/env python3
"""Traduz comentários de código, sem alterar o programa."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Frases inteiras de comentário, incluindo o # inicial.
# Código comentado, magics e identificadores não entram aqui.
REPLACEMENTS: list[tuple[str, str]] = [
    ("# Solution goes here", "# A solução vai aqui"),
    (
        "# This cell tells Jupyter to provide detailed debugging information",
        "# Esta célula pede ao Jupyter informações detalhadas de depuração",
    ),
    (
        "# when a runtime error occurs. Run it before working on the exercises.",
        "# quando ocorre um erro em tempo de execução. Execute-a antes dos exercícios.",
    ),
    (
        "# when a runtime error occurs, including a traceback.",
        "# quando ocorre um erro em tempo de execução, inclusive um traceback.",
    ),
    ("# should be True", "# deve ser True"),
    ("# should be False", "# deve ser False"),
    ("# should return False", "# deve devolver False"),
    ("# should return True", "# deve devolver True"),
    ("# should be Yes", "# deve ser Yes"),
    ("# should be No", "# deve ser No"),
    (
        "# this cell initializes the random number generator so it",
        "# esta célula inicializa o gerador de números aleatórios para que",
    ),
    (
        "# starts at the same point in the sequence each time this",
        "# comece no mesmo ponto da sequência cada vez que este",
    ),
    ("# notebook runs.", "# notebook for executado."),
    ("# INCORRECT!", "# INCORRETO!"),
    ("# INCORRECT", "# INCORRETO"),
    ("# WRONG!", "# ERRADO!"),
    ("# number of seconds in 42:42", "# número de segundos em 42:42"),
    ("# 10 kilometers in miles", "# 10 quilômetros em milhas"),
    ("# assign 8 to v", "# atribui 8 a v"),
    ("# velocity in miles per hour", "# velocidade em milhas por hora"),
    ("# x is not equal to y", "# x não é igual a y"),
    ("# x is greater than y", "# x é maior que y"),
    ("# x is less than to y", "# x é menor que y"),
    ("# x is greater than or equal to y", "# x é maior ou igual a y"),
    ("# x is less than or equal to y", "# x é menor ou igual a y"),
    (
        "# TODO: need to handle negative values!",
        "# TODO: é preciso tratar valores negativos!",
    ),
    ("# should be 29", "# deve ser 29"),
    ("# should be 61", "# deve ser 61"),
    ("# should be 125", "# deve ser 125"),
    ("# should be 4", "# deve ser 4"),
    ("# should be 1", "# deve ser 1"),
    ("# should be 55", "# deve ser 55"),
    ("# should be 6765", "# deve ser 6765"),
    ("# should be 210", "# deve ser 210"),
    (
        "# Here's what I got from ChatGPT 4o December 26, 2024",
        "# Eis o que obtive do ChatGPT 4o em 26 de dezembro de 2024",
    ),
    (
        "# It's correct, but it makes multiple calls to uses_any",
        "# Está correto, mas faz várias chamadas a uses_any",
    ),
    (
        "# I used this function to search for lines to use as examples",
        "# Usei esta função para buscar linhas que servissem de exemplo",
    ),
    (
        "# Here's the pattern I used (which uses some features we haven't seen)",
        "# Eis o padrão que usei (ele usa alguns recursos que ainda não vimos)",
    ),
    (
        "# generates the same sequence each time the notebook runs.",
        "# gera a mesma sequência cada vez que o notebook for executado.",
    ),
    (
        "# I used this cell to find a predecessor with a good number of possible successors",
        "# Usei esta célula para achar um predecessor com um bom número de sucessores possíveis",
    ),
    (
        "# and at least one repeated word.",
        "# e pelo menos uma palavra repetida.",
    ),
    (
        "# This cell downloads an archive file that contains the the files we'll",
        "# Esta célula baixa um arquivo compactado com os arquivos que",
    ),
    (
        "# use for the examples in this chapter.",
        "# usaremos nos exemplos deste capítulo.",
    ),
    (
        "# WARNING: This cell removes the photos/ directory if it already exists.",
        "# AVISO: esta célula remove o diretório photos/ se ele já existir.",
    ),
    (
        "# Any files already in the photos/ directory will be deleted.",
        "# Qualquer arquivo já existente em photos/ será apagado.",
    ),
    (
        "# this cell replaces `os.cwd` with a function that returns a fake path",
        "# esta célula substitui `os.cwd` por uma função que devolve um caminho falso",
    ),
    (
        "# this cell installs the pyyaml package, which provides the yaml module",
        "# esta célula instala o pacote pyyaml, que fornece o módulo yaml",
    ),
    (
        "# When you open a shelve file, a backup file is created that has the suffix `.bak`.",
        "# Ao abrir um arquivo shelve, cria-se um backup com o sufixo `.bak`.",
    ),
    (
        "# If you run this notebook more than once, you might see that file left behind.",
        "# Se executar este notebook mais de uma vez, esse arquivo pode ficar para trás.",
    ),
    (
        "# This cell removes it so the output shown in the book is correct.",
        "# Esta célula o remove para que a saída mostrada no livro fique correta.",
    ),
    ("# read the contents of the source file", "# lê o conteúdo do arquivo de origem"),
    ("# replace the old string with the new", "# substitui a string antiga pela nova"),
    (
        "# write the result into the destination file",
        "# grava o resultado no arquivo de destino",
    ),
    (
        "# This cell initializes the random number generator so we",
        "# Esta célula inicializa o gerador de números aleatórios para que",
    ),
    ("# always get the same results.", "# sempre obtenhamos os mesmos resultados."),
    (
        "# This cell makes a fresh Deck and",
        "# Esta célula cria um Deck novo e",
    ),
    (
        "# initializes the random number generator",
        "# inicializa o gerador de números aleatórios",
    ),
    (
        "# this cell creates a small example so we can run the following",
        "# esta célula cria um exemplo pequeno para podermos executar a célula",
    ),
    (
        "# cell without loading the actual data",
        "# seguinte sem carregar os dados reais",
    ),
    # thinkpython.py
    (
        "# the functions that define cell magic commands are only defined",
        "# as funções que definem comandos mágicos de célula só são definidas",
    ),
    ("# if we're running in Jupyter.", "# se estivermos rodando no Jupyter."),
    (
        "# get the name of the function defined in this cell",
        "# obtém o nome da função definida nesta célula",
    ),
    ("# get the class we're adding it to", "# obtém a classe à qual vamos adicioná-la"),
    (
        "# save the old version of the function if it was already defined",
        "# guarda a versão antiga da função, se ela já estava definida",
    ),
    (
        "# Execute the cell to define the function",
        "# Executa a célula para definir a função",
    ),
    ("# get the newly defined function", "# obtém a função recém-definida"),
    (
        "# add the function to the class and remove it from the namespace",
        "# adiciona a função à classe e a remove do namespace",
    ),
    (
        "# restore the old function to the namespace",
        "# restaura a função antiga no namespace",
    ),
    # Turtle.py (texto; código comentado e alias ficam)
    (
        "# Module for drawing classic Turtle figures on Google Colab notebooks.",
        "# Módulo para desenhar figuras clássicas de tartaruga em notebooks do Google Colab.",
    ),
    (
        "# It uses html capabilites of IPython library to draw svg shapes inline.",
        "# Usa os recursos HTML da biblioteca IPython para desenhar formas SVG no próprio documento.",
    ),
    (
        "# Looks of the figures are inspired from Blockly Games / Turtle (blockly-games.appspot.com/turtle)",
        "# O visual das figuras é inspirado no Blockly Games / Turtle (blockly-games.appspot.com/turtle)",
    ),
    (
        "# all 140 color names that modern browsers support. taken from https://www.w3schools.com/colors/colors_names.asp",
        "# os 140 nomes de cores que os navegadores modernos aceitam. fonte: https://www.w3schools.com/colors/colors_names.asp",
    ),
    (
        "# helper function that maps [1,13] speed values to ms delays",
        "# função auxiliar que mapeia valores de velocidade [1,13] para atrasos em ms",
    ),
    ("# construct the display for turtle", "# monta a exibição da tartaruga"),
    (
        "# helper function for generating svg string of the turtle",
        "# função auxiliar que gera a string SVG da tartaruga",
    ),
    (
        "# helper function for generating the whole svg string",
        "# função auxiliar que gera a string SVG inteira",
    ),
    (
        "# helper functions for updating the screen using the latest positions/angles/lines etc.",
        "# funções auxiliares para atualizar a tela com as posições, ângulos e linhas mais recentes.",
    ),
    (
        "# helper function for managing any kind of move to a given 'new_pos' and draw lines if pen is down",
        "# função auxiliar para qualquer movimento até 'new_pos' e para desenhar linhas se a caneta estiver abaixada",
    ),
    (
        "# rounding the new_pos to eliminate floating point errors.",
        "# arredonda new_pos para eliminar erros de ponto flutuante.",
    ),
    (
        "# makes the turtle move forward by 'units' units",
        "# faz a tartaruga avançar 'units' unidades",
    ),
    (
        "# makes the turtle move backward by 'units' units",
        "# faz a tartaruga recuar 'units' unidades",
    ),
    (
        "# makes the turtle move right by 'degrees' degrees (NOT radians)",
        "# faz a tartaruga girar 'degrees' graus à direita (NÃO radianos)",
    ),
    (
        "# makes the turtle face a given direction",
        "# faz a tartaruga apontar para uma direção dada",
    ),
    (
        "# makes the turtle move right by 'degrees' degrees (NOT radians, this library does not support radians right now)",
        "# faz a tartaruga girar 'degrees' graus à direita (NÃO radianos; esta biblioteca ainda não aceita radianos)",
    ),
    (
        "# raises the pen such that following turtle moves will not cause any drawings",
        "# levanta a caneta para que os movimentos seguintes não desenhem",
    ),
    (
        "# TODO: decide if we should put the timout after lifting the pen",
        "# TODO: decidir se o timeout deve vir depois de levantar a caneta",
    ),
    (
        "# lowers the pen such that following turtle moves will now cause drawings",
        "# abaixa a caneta para que os movimentos seguintes passem a desenhar",
    ),
    (
        "# TODO: decide if we should put the timout after releasing the pen",
        "# TODO: decidir se o timeout deve vir depois de abaixar a caneta",
    ),
    ("# update the speed of the moves, [1,13]", "# atualiza a velocidade dos movimentos, [1,13]"),
    (
        "# if argument is omitted, it returns the speed.",
        "# se o argumento for omitido, devolve a velocidade.",
    ),
    (
        "# TODO: decide if we should put the timout after changing the speed",
        "# TODO: decidir se o timeout deve vir depois de mudar a velocidade",
    ),
    (
        "# move the turtle to a designated 'x' x-coordinate, y-coordinate stays the same",
        "# move a tartaruga para a coordenada x indicada; y permanece o mesmo",
    ),
    (
        "# move the turtle to a designated 'y' y-coordinate, x-coordinate stays the same",
        "# move a tartaruga para a coordenada y indicada; x permanece o mesmo",
    ),
    ("# this will handle updating the drawing.", "# isto cuida de atualizar o desenho."),
    (
        "# retrieve the turtle's currrent 'x' x-coordinate",
        "# obtém a coordenada x atual da tartaruga",
    ),
    (
        "# retrieve the turtle's currrent 'y' y-coordinate",
        "# obtém a coordenada y atual da tartaruga",
    ),
    (
        "# retrieve the turtle's current position as a (x,y) tuple vector",
        "# obtém a posição atual da tartaruga como vetor (x, y)",
    ),
    ("# retrieve the turtle's current angle", "# obtém o ângulo atual da tartaruga"),
    (
        "# move the turtle to a designated 'x'-'y' coordinate",
        "# move a tartaruga para a coordenada x-y indicada",
    ),
    (
        "# jump to a given location without leaving a trail",
        "# salta para um lugar dado sem deixar rastro",
    ),
    ("# switch turtle visibility to ON", "# torna a tartaruga visível"),
    ("# switch turtle visibility to OFF", "# torna a tartaruga invisível"),
    ("# 140 predefined html color names", "# 140 nomes de cores HTML predefinidos"),
    ("# 3 or 6 digit hex color code", "# código hexadecimal de 3 ou 6 dígitos"),
    ("# rgb color code", "# código de cor RGB"),
    (
        "# change the background color of the drawing area",
        "# muda a cor de fundo da área de desenho",
    ),
    (
        "# if no params, return the current background color",
        "# sem parâmetros, devolve a cor de fundo atual",
    ),
    ("# change the color of the pen", "# muda a cor da caneta"),
    (
        "# if no params, return the current pen color",
        "# sem parâmetros, devolve a cor atual da caneta",
    ),
    (
        "# change the width of the lines drawn by the turtle, in pixels",
        "# muda a largura das linhas desenhadas pela tartaruga, em pixels",
    ),
    (
        "# if the function is called without arguments, it returns the current width",
        "# se a função for chamada sem argumentos, devolve a largura atual",
    ),
    (
        "# TODO: decide if we should put the timout after changing the pen_width",
        "# TODO: decidir se o timeout deve vir depois de mudar pen_width",
    ),
    ("# pensize is an alias for width", "# pensize é um alias de width"),
    ("# clear any text or drawing on the screen", "# apaga texto e desenho da tela"),
    ("# return turtle window width", "# devolve a largura da janela da tartaruga"),
    ("# return turtle window height", "# devolve a altura da janela da tartaruga"),
    (
        "# vX.X.X Updated at by Allen Downey for Think Python 3e",
        "# vX.X.X Atualizado por Allen Downey para Think Python 3e",
    ),
    # structshape.py
    ("# handle sequences", "# trata sequências"),
    ("# handle dictionaries", "# trata dicionários"),
    ("# handle other types", "# trata outros tipos"),
    # diagram.py
    ("# Set figure size", "# Define o tamanho da figura"),
    ("# Set axes position", "# Define a posição dos eixos"),
    ("# Set x and y limits", "# Define os limites de x e y"),
    (
        "# Remove the spines, ticks, and labels",
        "# Remove as bordas, os ticks e os rótulos",
    ),
    ("# Remove the spines", "# Remove as bordas"),
    ("# Remove the axis labels", "# Remove os rótulos dos eixos"),
    ("# Remove the tick marks", "# Remove as marcas de escala"),
    (
        "# only include the arrow if we drew the value",
        "# só inclui a seta se desenhamos o valor",
    ),
    (
        "# Note for the future about dotted arrows",
        "# Nota para o futuro sobre setas pontilhadas",
    ),
    ("# draw the bindings", "# desenha as ligações"),
    ("# draw the frames", "# desenha os frames"),
    (
        "# TODO: dpi in the notebook should be 100, in the book it should be 300 or 600",
        "# TODO: o dpi no notebook deve ser 100; no livro, 300 ou 600",
    ),
]


def apply_text(text: str) -> tuple[str, int]:
    count = 0
    for old, new in REPLACEMENTS:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            count += n
    return text, count


def apply_notebook(path: Path) -> int:
    nb = json.loads(path.read_text(encoding="utf-8"))
    total = 0
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        new, n = apply_text(src)
        if n:
            # preservar formato Jupyter de source
            if src == new:
                continue
            parts = new.split("\n")
            source = []
            for i, part in enumerate(parts):
                if i < len(parts) - 1:
                    source.append(part + "\n")
                elif part:
                    source.append(part)
            cell["source"] = source
            total += n
    if total:
        path.write_text(
            json.dumps(nb, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return total


def apply_py(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    new, n = apply_text(text)
    if n:
        path.write_text(new, encoding="utf-8")
    return n


def main() -> None:
    print("notebooks:")
    for folder in ("chapters", "blank"):
        for path in sorted((ROOT / folder).glob("*.ipynb")):
            n = apply_notebook(path)
            if n:
                print(f"  {folder}/{path.name}: {n}")
    print("py:")
    for name in ("thinkpython.py", "Turtle.py", "structshape.py", "diagram.py"):
        path = ROOT / name
        if path.exists():
            n = apply_py(path)
            print(f"  {name}: {n}")


if __name__ == "__main__":
    main()
