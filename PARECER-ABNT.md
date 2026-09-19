# Parecer de adequação ABNT e norma culta

Tradução educacional de *Think Python*, 3ª edição, de Allen B. Downey. Título adotado: *Pense em Python*. Revisão de 18 de setembro de 2026.

## 1. Escopo

Este parecer examina a adequação da citação, da autoria e da língua da tradução educacional depositada neste repositório. O objeto não é um TCC, dissertação, tese, artigo jurídico nem edição comercial. É obra derivada didática, sem fins lucrativos, em notebooks Jupyter, sob CC BY-NC-SA 4.0 (texto) e MIT (código).

Foram revistos e corrigidos, nesta passagem: `CITACAO.md`, `README.md` e o rodapé de autoria e licença em `jb/_config.yml`. `GLOSSARIO.md` foi lido por consistência e norma culta; não exigiu alteração. A amostragem de língua incidiu sobre `chapters/chap00.ipynb`, `chap01.ipynb`, `chap03.ipynb`, `chap10.ipynb`, `chap19.ipynb` e `chapters/jupyter_intro.ipynb`. Células de código não foram alteradas.

## 2. Normas aplicadas e não aplicadas

Aplicam-se, no que couber a este tipo de projeto:

- ABNT NBR 6023:2018, para fichas de referência (autoria, obra traduzida, recurso eletrônico, licença).
- ABNT NBR 10520:2023, para citação no texto no sistema autor-data, inclusive a indicação “tradução nossa”.
- A exigência de atribuição inequívoca da autoria original e do caráter de tradução, também imposta pela CC BY-NC-SA 4.0.

Não se aplicam, e não foram forçadas:

- ABNT NBR 14724 (estrutura de trabalhos acadêmicos). Notebooks didáticos não se convertem em monografia.
- Capa institucional, sumário ABNT, Times 12, recuo de 1,25 cm e demais requisitos gráficos de TCC.
- Linguagem impessoal de tese. O original fala com o leitor na segunda pessoa; essa voz é do livro e deve permanecer.

A NBR 6023 e a NBR 10520 regulam *como se cita e se referencia*. Não regulam o gênero literário do material citado. Sustentamos que a adequação, aqui, é a de uma tradução didática corretamente atribuída, não a de um trabalho de conclusão de curso.

## 3. Autoria (NBR 6023 e NBR 10520)

A entrada de responsabilidade é **DOWNEY, Allen B.** em todas as fichas. O repositório e a tradução não figuram como autor. O tradutor não está nominado; não se inventou nome, editora comercial, ISBN da tradução nem local de publicação.

O elemento de tradução, depois do título, usa a fórmula honesta “Tradução educacional para o português brasileiro”, admitida pela NBR 6023 quando há tradução e o tradutor não está identificado.

As datas ficam distintas e explícitas:

- **2024**: ano da 3ª edição original e, nesse sentido, das ideias do autor. Citação no texto: (DOWNEY, 2024) ou Downey (2024).
- **2026**: ano desta tradução como recurso eletrônico. Usa-se 2026 só quando a referência for a esta versão em português, não ao pensamento de Downey.

Essa distinção atende à NBR 10520 (ano da obra de cuja ideia se fala) e evita atribuir a Downey a data da tradução, ou à tradução a autoria do livro.

## 4. Fichas de referência (redação final)

### 4.1 Obra original (impressa)

DOWNEY, Allen B. *Think Python*: how to think like a computer scientist. 3. ed. Sebastopol: O’Reilly Media, 2024.

### 4.2 Obra original (recurso eletrônico)

DOWNEY, Allen B. *Think Python*: how to think like a computer scientist. 3. ed. [S. l.]: Green Tea Press, 2024. *E-book*. Disponível em: https://greenteapress.com/wp/think-python-3rd-edition. Acesso em: 18 set. 2026.

### 4.3 Tradução educacional (obra derivada)

DOWNEY, Allen B. *Pense em Python*: como pensar como um cientista da computação. Tradução educacional para o português brasileiro. 3. ed. [S. l.: s. n.], 2026. *E-book*. Disponível em: https://github.com/alexander-stack1/ThinkPython. Acesso em: 18 set. 2026.

Observações da ficha 4.3: subtítulo em minúscula após os dois-pontos; elemento de tradução imediatamente após o título; edição abreviada “3. ed.”; [S. l.: s. n.] por ausência de local e de editora; “Disponível em” e “Acesso em” com mês abreviado (set.).

### 4.4 Licença

CREATIVE COMMONS. *Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional*: CC BY-NC-SA 4.0. [S. l.]: Creative Commons, 2013. Disponível em: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pt_BR. Acesso em: 18 set. 2026.

### 4.5 Citação de trecho traduzido

Conforme a NBR 10520:2023, “tradução nossa” acompanha o trecho **já vertido**. Redação adotada:

“Aprender a programar significa aprender uma forma nova de pensar” (DOWNEY, 2024, cap. 1, tradução nossa).

Se o trecho for reproduzido em inglês, a indicação “tradução nossa” não se usa.

## 5. Achados de norma culta

### 5.1 Arquivos de frente

`CITACAO.md` trazia o exemplo de “tradução nossa” em inglês, o que invertia a regra da NBR 10520. A ficha da tradução usava “repositório didático sem fins lucrativos” no lugar de editora, o que inventava um responsável comercial inexistente. O elemento de tradução vinha depois da edição. Não havia ficha da licença nem distinção explícita 2024/2026. Essas falhas foram corrigidas.

`README.md` foi alinhado às fichas finais, à fórmula de tradutor não nominado e à distinção de datas. O tom didático foi mantido.

`jb/_config.yml` já atribuía a obra a Downey e declarava a CC BY-NC-SA 4.0. O rodapé e o campo `copyright` passaram a marcar 2024 (autoria) e 2026 (tradução).

`GLOSSARIO.md` está em norma culta aceitável e internamente consistente com a terminologia da tradução (inclusive escolhas já consagradas no Brasil, como *Pense em Python*, “função frutífera” e “função nula”). Não foi reescrito.

### 5.2 Notebooks amostrados (só erro real)

Foram alteradas **6 células markdown**, em 5 arquivos. `chap19.ipynb` não exigiu correção. Nenhuma célula de código foi tocada.

| Arquivo | Célula | Correção |
|---|---|---|
| `chapters/chap00.ipynb` | 5 | Concordância: “elas são ferramenta padrão” → “elas são ferramentas padrão”. |
| `chapters/chap01.ipynb` | 50 | Pontuação: período após “concatenação”. |
| `chapters/chap01.ipynb` | 88 | Ortografia no glossário: espaço indevido em `` ` float` ``. |
| `chapters/chap03.ipynb` | 5 | Concordância sujeito-verbo: “O corpo desta função são duas instruções” → “consiste em duas instruções”. |
| `chapters/chap10.ipynb` | 100 | Espaço indevido em `` ` n=3` ``. |
| `chapters/jupyter_intro.ipynb` | 15 | Ano de copyright 2023 alinhado a 2024, data da 3ª edição e das demais células de atribuição. |

A prosa didática em segunda pessoa, os enunciados de exercício, as letras de música em inglês e os *prompts* deliberadamente em inglês para assistentes virtuais foram preservados.

### 5.3 Risco residual

A amostragem não cobre o livro inteiro nem a pasta `blank/`. Calques leves e aceitáveis no tom do original permanecem (por exemplo, “deu um bom começo”, “verificação de sanidade”, “andaime” no sentido de *scaffolding*). A data de acesso das fichas eletrônicas envelhece e deve ser atualizada quando o material for citado de novo. Se no futuro houver tradutor nominado, o elemento “Tradução …” da NBR 6023 deve passar a trazer o nome, sem deslocar Downey da autoria.

## 6. Veredito

Depois das correções desta revisão, o projeto está **adequado** como tradução didática não comercial de obra de Allen B. Downey, com citação e referência compatíveis com a NBR 6023:2018 e a NBR 10520:2023 no recorte que se aplica a este gênero.

A autoria intelectual permanece de Downey (2024). A tradução (2026) está identificada como tal, sem usurpação de autoria, sem tradutor inventado e sem estrutura de monografia. A licença CC BY-NC-SA 4.0 e o uso não comercial estão declarados de forma inequívoca nos arquivos de frente e no rodapé do livro.

A língua da amostragem, após as seis correções pontuais, está em norma culta suficiente para uso educacional. Uma revisão integral dos demais capítulos ainda é recomendável, mas não é condição para o veredito de adequação da citação e da autoria.
