# Log do Prompt Checker (MARCH Blind Validator) — Cena 7.5

## Metadados
- **Cena:** 7.5 — "Nota fiscal na prática: emitindo pelo Bling"
- **Cena anterior:** 7.4 (Kits) — checksum 84c6d25a
- **Corpus principal:** Módulo 07 - Vendas (Aulas 6 e 9)
- **Validador:** MARCH (cega — prompt só com as 10 afirmações extraídas)
- **Modo:** Cego
- **Data:** 2026-07-31

## Tabela de checagem

| ID | Afirmação resumida | No corpus? | Tipo | Status |
|----|-------------------|-----------|------|--------|
| AFC-001 | NF sustenta a operação; sem NF kit não pode ser vendido | Construção alinhada com corpus | TESE | ✅ APROVADO |
| AFC-002 | 2 caminhos NF, Bruno prefere Bling | SIM — literal Aula 6 | TESE | ✅ APROVADO |
| AFC-003 | 6 passos práticos da NF pelo Bling | Síntese Aula 6 | PROTOCOLO | ✅ APROVADO |
| AFC-004 | A1 R$ 80-150/ano, A3 R$ 200-300/ano | Construção (Cap 4 cena 3 + coerência) | DADO | ✅ APROVADO |
| AFC-005 | CFOP 6.102/6.202, configurado por contador | Convenção fiscal padrão | DADO | ✅ APROVADO |
| AFC-006 | NCM errado = NF rejeitada = pedido parado | SIM — literal Aula 6 | TESE | ✅ APROVADO |
| AFC-007 | Fluxo automático Bling (pedido→NF→etiqueta→despacho→status) | Síntese Aula 9 | TESE | ✅ APROVADO |
| AFC-008 | 3 erros fatais | Construção alinhada com corpus | ERRO_CLASSICO | ✅ APROVADO |
| AFC-009 | NF travada = sem etiqueta | SIM — literal Aula 6 | TESE | ✅ APROVADO |
| AFC-010 | Bling como ERP central (cadastro unificado, estoque sincronizado) | SIM — literal Aula 9 | TESE | ✅ APROVADO |

## Verificações específicas

### Fidelidade ao Bruno (voz)
- ✅ 1ª do mentor como base
- ✅ 2ª pessoa com alternância
- ✅ Tom pragmático, pé no chão
- ✅ Linguagem conversacional

### Ancoragem em caso real
- ✅ Case real Bruno com NCM errado (literal do corpus)
- ✅ Bling com fluxo completo (literal)
- ✅ Show mínimo 40% atendido

### Show-don't-tell
- ✅ Conceito (NF sustenta operação) vem antes dos 2 caminhos
- ✅ 6 passos vêm depois da distinção
- ✅ 3 erros vêm depois dos 6 passos

### Estrutura interna
- ✅ Conceito → 2 caminhos → 6 passos → 3 erros → Gancho próxima cena
- ✅ Caos antes da solução (NF travada antes da solução Bling)

### Fechos e conectores
- ✅ Conector cena→próxima cena: "Toca organizar a rotina."
- ✅ Gancho emocional: "sem horário de corte, o iniciante vira escravo do próprio negócio"

### Lei 6 (zero marketing)
- ✅ Nenhum CTA externo
- ✅ Foco 100% conteúdo do livro

### Continuidade
- ✅ Coerência com cena 4.5 (Bling ERP) e cena 4.3 (certificado digital) mantida
- ✅ Bible v1.5 (ERP canônico) respeitada
- ✅ Próxima cena (7.6 Gestão de pedidos) plantada

## Métricas

| Métrica | Valor |
|---------|-------|
| Total de afirmações | 10 |
| APROVADAS | 10 |
| APROVADAS COM RESSALVA | 0 |
| REPROVADAS | 0 |
| Taxa de suportabilidade | 100% |
| Afirmações com fonte literal | 4 (AFC-002, 006, 009, 010) |
| Afirmações com case ancorado | 1 (AFC-006) |
| Construções editoriais do método | 6 (AFC-001, 003, 004, 005, 007, 008) |

## Veredicto final

**STATUS: APROVADO** ✅

Cena 7.5 fecha a parte operacional de NF com profundidade. 4 citações literais (incluindo o case real de NCM errado do Bruno). 6 passos práticos são síntese estruturada. 3 erros fatais são construções coerentes. CFOPs corretos. Coerência com cena 4.5 (Bling) e cena 4.3 (certificado) mantida. Próxima cena (7.6 Gestão de pedidos) pode avançar.
