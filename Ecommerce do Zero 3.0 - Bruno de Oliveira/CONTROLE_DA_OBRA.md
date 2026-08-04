# CONTROLE DA OBRA — Fonte de Verdade Única

> **Este arquivo é a fonte de verdade para contagem de cenas e palavras.**
> A partir de 2026-08-04, todos os números de progresso da obra são lidos daqui.
> O `estado/estado_da_obra.md` e a `bible/bible_da_obra.md` ficam secundários (contexto histórico).

---

## Última atualização

**Data:** 2026-08-04
**Método:** `find + wc -w` no diretório `capitulos/`
**Regra:** só conta como "finalizada" a cena que tem `_saida_final.md`. Cenas com apenas `_saida_escritor.md` ficam em "escritas, sem cp final".

---

## Cenas finalizadas em disco

> **Regra atualizada em 2026-08-04 (após Bruno confirmar):** uma cena é considerada "finalizada" se tem `_saida_escritor.md` + validadores + livro_capitulo consolidado (mesmo sem o `_saida_final.md` no formato do pipeline atual).

| Capítulo | Cenas finalizadas | Palavras |
|----------|-------------------|----------|
| Cap 1 — Boas-vindas e Mindset | 3 / 3 | 4.252 |
| Cap 2 — O Mercado e Você | 4 / 4 | 5.664 |
| Cap 3 — O Método e o Planejamento | 6 / 6 | 9.309 |
| Cap 4 — A Estrutura Mínima Viável | 8 / 8 | 15.880 |
| Cap 5 — Audiência É Rei | 6 / 6 | 16.974 |
| Cap 6 — Atendimento que Converte | 5 / 5 | 13.714 |
| Cap 7 — Vendas e Ofertas | 6 / 6 | 13.801 |
| Cap 8 — Impulsão Estratégica | 5 / 5 | 15.558 |
| Cap 9 — Parabéns! Você validou | 2 / 2 | 5.636 |
| Cap 10 — Domínio do Mercado Livre | 3 / 3 | 9.842 |
| Cap 12 — Cases, Bônus e Epílogo | 3 / 3 | 8.926 |
| **Subtotal** | **54 / 54** | **129.452** |

---

## Cenas escritas, sem livro_capitulo consolidado

> (vazio — todas as cenas escritas têm livro consolidado do capítulo)

| Capítulo | Cenas | Palavras | Decisão |
|----------|-------|----------|---------|
| — | — | — | — |
| **Subtotal** | **0** | **0** | — |

---

## Cenas ainda não escritas

| Capítulo | Cenas pendentes | Estimativa de palavras |
|----------|-----------------|------------------------|
| — (todas concluídas) | 0 | 0 |
| **Subtotal** | **0** | **0** |

> Status: **LIVRO INTEIRO FECHADO**. 12 capítulos, 54 cenas, 129.452 palavras. A consolidação final (livro_completo.md com prefácio, epílogo expandido, glossário, front matter) é opcional.

> Status: cenas ainda não iniciadas.

---

## TOTAIS

| Item | Valor |
|------|-------|
| Total planejado de cenas (Opção A) | **54** |
| Cenas finalizadas (com livro_capitulo consolidado) | **54** |
| Cenas ainda não escritas | **0** |
| **Progresso de cenas finalizadas** | **54 / 54 = 100%** |
| Palavras finalizadas | **129.452** |
| **Total do livro** | **~129.000 palavras** |

---

## Regra de ouro (a partir de agora)

1. **Toda vez que eu (assistente) for te dar um número de progresso**, eu venho deste arquivo.
2. **Toda vez que uma cena nova for escrita e finalizada**, eu atualizo a tabela de "Cenas finalizadas" e a tabela de "TOTAIS" deste arquivo.
3. **Toda vez que uma cena nova for apenas escrita (sem cp final)**, eu atualizo a tabela "escritas, sem cp final".
4. O `estado/estado_da_obra.md` e a `bible/bible_da_obra.md` ficam como contexto histórico e serão limpos/regenerados depois, se for útil.
5. **O Cap 2 está preservado** — está finalizado de verdade, com livro_capitulo_02.md pronto e validações OK. Apenas não tem o `_saida_final.md` no formato do pipeline novo, mas isso é convenção, não indicador de incompletude.

---

## Histórico de atualizações

- **2026-08-04** — Criação do arquivo. Substitui a fonte de verdade anterior (`estado_da_obra.md`) que estava desatualizada.
- **2026-08-04 (revisão)** — Bruno informa que o Cap 2 está finalizado de verdade, com livro_capitulo_02.md pronto e validações OK. A ausência do `_saida_final.md` no formato do pipeline novo não significa incompletude. Regra de "cena finalizada" atualizada pra incluir cenas com livro_capitulo consolidado. Total de cenas finalizadas: 48 (não 44). Total de palavras: 110.630.
- **2026-08-04 (cena 11.1)** — Cena 11.1 (Bling: o ERP que organiza a operação) finalizada, checksum d8547231, 2.624 palavras. Atualizado: 49 cenas finalizadas, 113.254 palavras, 5 cenas pendentes (11.2, 11.3, 12.1, 12.2, 12.3).
- **2026-08-04 (cena 11.2)** — Cena 11.2 (Cadastrando produtos no Bling) finalizada, checksum 77748cb9, 3.825 palavras. Atualizado: 50 cenas finalizadas, 117.079 palavras, 4 cenas pendentes (11.3, 12.1, 12.2, 12.3).
- **2026-08-04 (cena 11.3 + Cap 11 fechado)** — Cena 11.3 (Emitindo NF pelo Bling) finalizada, checksum 2e58f8b1, 3.447 palavras. Cap 11 fechado: 3/3 cenas, 9.896 palavras. Atualizado: 51 cenas finalizadas, 120.526 palavras, 3 cenas pendentes (12.1, 12.2, 12.3).
- **2026-08-04 (Cap 12 fechado + LIVRO INTEIRO COMPLETO)** — Cena 12.1 (Cases reais) finalizada, checksum 491b32c4, 2.605 palavras. Cena 12.2 (Bônus gestão de preços + DNA) finalizada, checksum b0e076a8, 3.774 palavras. Cena 12.3 (Epílogo) finalizada, checksum cbd63765, 2.547 palavras. LIVRO INTEIRO FECHADO: 12 capítulos, 54 cenas, 129.452 palavras. A consolidação final (livro_completo.md com prefácio, epílogo expandido, glossário, front matter) é opcional e pode ser feita depois.
