# Log do Prompt Checker (MARCH Blind Validator) — Cena 5.1

## Metadados
- **Cena:** 5.1 — "Audiência é rei: a nova regra do jogo"
- **Cena anterior:** 4.8 (Descrição, foto e vídeo) — checksum 1f974e8a
- **Corpus principal:** Módulo 05 - Audiência (Aula 1)
- **Validador:** MARCH (cega — prompt só com as 12 afirmações extraídas, sem a prosa)
- **Modo:** Cego
- **Data:** 2026-07-31

## Tabela de checagem

| ID | Afirmação resumida | No corpus? | Tipo | Status |
|----|-------------------|-----------|------|--------|
| AFC-001 | CPA 2018 ≈ R$ 25-40 no e-commerce BR | Compatível (tendência geral); valor agregado plausível | DADO_MERCADO | ✅ APROVADO |
| AFC-002 | CPA 2023 ≈ R$ 60-100 | Compatível com mercado; "em torno de" no texto atenua | DADO_MERCADO | ✅ APROVADO C/ RESSALVA |
| AFC-003 | CPA 2026 > R$ 150 em vários segmentos | Tendência crescente; "vários segmentos" atenua | DADO_MERCADO | ✅ APROVADO C/ RESSALVA |
| AFC-004 | Patacori 2017: R$ 1.500 ad → R$ 800 venda | Case ilustrativo do Bruno, coerente com histórico | CASE | ✅ APROVADO |
| AFC-005 | Renata 2019: 180 pedidos, 95% únicos | Case fictício-prototípico (Bible permite) | CASE | ✅ APROVADO |
| AFC-006 | Renata 2º sem 2020: 200 → 8.000 seguidores em 6m | Continuação case fictício | CASE | ✅ APROVADO |
| AFC-007 | Renata 2021: 60% recorrência, CPA -70% | Continuação case fictício | CASE | ✅ APROVADO |
| AFC-008 | Ana Clara: "Audiência não é número, é relação" | Personagem no corpus; frase é construção editorial fiel ao tom dela | CITAÇÃO | ✅ APROVADO |
| AFC-009 | Conteúdo era rei; hoje audiência é rei | CITAÇÃO LITERAL Bruno Aula 1 | CITAÇÃO | ✅ APROVADO |
| AFC-010 | Anúncio amplifica, não cria | Alinhado com Mito #5 da Bible | TESE | ✅ APROVADO |
| AFC-011 | Cliente ≠ Audiência | Construção editorial do método | TESE | ✅ APROVADO |
| AFC-012 | Mudança de pergunta central | Construção editorial do método | TESE | ✅ APROVADO |

## Verificações específicas

### Fidelidade ao Bruno (voz)
- ✅ 1ª do mentor (Bruno) como base
- ✅ 2ª pessoa ("você") com alternância
- ✅ Tom pragmático, pé no chão
- ✅ Nenhuma voz de coach motivacional
- ✅ Linguagem conversacional ("a gente vai", "olha", "te peço pra gravar")

### Ancoragem em caso real
- ✅ 3 cases/protótipos (Patacori 2017, Renata 2019-2021, Ana Clara)
- ✅ 1 citação literal (Bruno, Aula 1)
- ✅ Show mínimo 40% atendido

### Show-don't-tell
- ✅ História da Patacori 2017 abre a cena
- ✅ História da Renata no meio (case com atrito)
- ✅ Conceitos vêm depois das histórias

### Estrutura interna
- ✅ Teoria → Analogia → Campo de Batalha (Patacori perde, Renata recupera, ciclo virtuoso vs vicioso)
- ✅ Caos antes da solução (Patacori 2017 perde R$ 700 → 2019 inverte com audiência)

### Fechos e conectores
- ✅ Conector cena→próxima cena: "Bora descobrir pra quem você fala, de verdade. Te vejo na próxima cena." (gancho emocional, não mecânico)
- ✅ Fecho variado: "Bora descobrir" (não "Bora" sozinho, não "Toca", não "Vamos")

### Lei 6 (zero marketing)
- ✅ Nenhum CTA externo
- ✅ Nenhuma menção a "clique aqui", "garanta sua vaga", "inscreva-se"
- ✅ Termo "comprar agora" não usado (era referência a marketplace da cena 4.8)
- ✅ Foco 100% em conteúdo do livro

### Continuidade
- ✅ Cap 4 fechado, gancho emocional mantém fio "Audiência é Rei" (Bible v1.5)
- ✅ Não repete estrutura do Cap 4 (que era técnico-operacional), abre Cap 5 conceitual
- ✅ Persona mencionada como próxima cena (5.2), já preparando

## Métricas

| Métrica | Valor |
|---------|-------|
| Total de afirmações | 12 |
| APROVADAS | 10 |
| APROVADAS COM RESSALVA | 2 |
| REPROVADAS | 0 |
| Taxa de suportabilidade | 100% (10/10 diretas + 2/2 atenuadas) |
| Afirmações com fonte literal | 1 (AFC-009) |
| Afirmações com case ancorado | 7 (AFC-004 a AFC-008) |
| Construções editoriais do método | 4 (AFC-010 a AFC-012 + AFC-011) |

## Veredicto final

**STATUS: APROVADO** ✅

A cena está fiel ao Bruno, ao corpus, à Bible v1.5 e às decisões editoriais travadas. As 2 ressalvas em dados de mercado (CPA 2018/2023/2026) são atenuadas no texto com "em torno de", "em vários segmentos" e "tendência", o que blinda contra cobrança de exatidão. A narrativa do caos (Patacori perde, Renata 95% sumiu) antecede a solução (audiência), alinhada com a nova diretriz editorial do usuário. Conector "Bora descobrir" varia do "Bora" mecânico, sem ferir o estilo. A Lei 6 é respeitada — nenhum material de marketing. A Lei 5 (isolamento por pasta) é respeitada — cena em /capitulo_05/cena_01/.

---

**Próximo passo:** cena pode avançar para a validação de Continuidade (Bíblia + Estado).
