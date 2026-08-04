#!/usr/bin/env python3
"""build_capitulo_06.py — consolida o Cap. 6 (COMPLETO, 5 cenas) em livro_capitulo_06.md."""
import hashlib
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira")
CAP = BASE / "capitulos/capitulo_06"

CENA_TITULOS = {
    1: "Atendimento: de SAC a CX (Customer Experience)",
    2: "Canais: marketplace, WhatsApp, Direct, Messenger e e-mail",
    3: "Pré-venda: conquistando antes do clique",
    4: "Pós-venda: encantamento, follow-up, recompra",
    5: "Solução de conflitos: quando o problema aparece",
}

CENA_CHECKSUMS = {
    1: "d6a78202",
    2: "e409c721",
    3: "fa7449d4",
    4: "52c6677a",
    5: "cf82d722",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 6 — Atendimento que Converte"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-07-31T21:00:00Z"
version: "1.0"
capitulo: 6
total_capitulos_estimados: 12
cena_count: 5
status: "CONCLUIDO"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.5 (atualizada após Cap 1 + Cap 2 + Cap 3 + Cap 4 + Cap 5 + Cap 6 completos — Cenas 1.1 a 6.5 CONCLUÍDAS, 32/50 cenas)"
validador_march: "TODAS_APROVADAS (5/5 cenas)"
validador_continuidade: "TODAS_APROVADAS (5/5 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "6.1: d6a78202"
  - "6.2: e409c721"
  - "6.3: fa7449d4"
  - "6.4: 52c6677a"
  - "6.5: cf82d722"
fios_narrativos_avancados:
  - "CX (Customer Experience) — Conceito Âncora do Cap 6, instalado em 6.1, operacionalizado em 6.2-6.4, FECHADO em 6.5"
  - "Atendimento = o que acontece sempre — tese central do Cap 6"
  - "Venda começa quando o Pix cai — tese central do pós-venda (6.4)"
  - "Conflito é normal, falta de solução não — tese central de 6.5"
  - "Case Fernando (prototípico com atrito: auge→queda→recuperação com CX) — instalado em 6.1"
  - "Case Nubank (literal: cachorro comeu cartão → brinquedo) — instalado em 6.1"
  - "Case Beatriz (cosmético, prototípico: R$30k→R$0→R$30k com pós-venda) — instalado em 6.4"
  - "Case Ain (literal: 2.774 recl, 100% resp, 92% sol, 77% voltariam) vs AliExpress (8.438 recl, 0% resp) — instalado em 6.5"
  - "Marketplace (hóspede) vs Canal próprio (dono) — instalado em 6.2"
  - "Regra 80-15-4-1 — instalado em 6.2"
  - "Resposta ativa vs Resposta passiva — instalado em 6.3"
  - "5 passos da pré-venda ativa — instalado em 6.3"
  - "4 momentos do pós-venda ativo — instalado em 6.4"
  - "6 níveis de conflito — instalado em 6.5"
  - "5 passos da solução de conflito (ouvir, validar, oferecer 3 op, executar, follow-up) — instalado em 6.5"
  - "Case Patacori 2019 (5 anúncios derrubados por desvio) — instalado em 6.2"
cases_citados:
  - "Fernando (loja decoração, 2019): R$ 18k/mês com 12% recompra → Queda 40% em 60 dias por 3 problemas combinados → NPS 65→18, recompra 12%→3% → 90 dias depois, com CX: NPS 70, recompra 18%, R$ 18k/mês com 30% mais margem [6.1]"
  - "Nubank (case real): cachorro comeu cartão → 2ª via + brinquedo → viralizou → equivalente a R$ 1 milhão em marketing [6.1]"
  - "Patacori 2019: vendedor desviou cliente do Mercado Livre pro WhatsApp → 5 anúncios derrubados em 48h [6.2]"
  - "Grupo Via Varejo Black Friday: 20% das vendas via WhatsApp [6.2]"
  - "Aluna tênis corrida: resposta passiva (30%) → resposta ativa (80%) [6.3]"
  - "Beatriz (cosmético natural, 2021): R$ 30k dez/2021 com 0% recompra → R$ 0 jan/2022 → pós-venda ativo → 28% recompra, R$ 25-30k/mês, LTV R$ 75 → R$ 280 em 6 meses [6.4]"
  - "Ain: 2.774 reclamações em 12 meses, 100% respondidas, 92% solução, 77% voltariam [6.5]"
  - "AliExpress: 8.438 reclamações em 12 meses, 0% respondidas [6.5]"
conceitos_definidos:
  - "Atendimento não é o que acontece quando dá errado. Atendimento é o que acontece sempre. (tese central Cap 6)"
  - "SAC vs CX: 3 diferenças — tempo, autonomia, visão"
  - "NPS = % Promotores - % Detratores, neutros descartados. Faixas -100/-1 a 75/100"
  - "3 camadas CX do MVP: responder rápido / resolver 1ª / encantar além da expectativa"
  - "Funil vira ampulheta com CX"
  - "Expectativa do cliente no e-commerce é baixa (produto inteiro, funcionando, no prazo). Quem entrega mais, encanta"
  - "Marketplace (hóspede) vs Canal próprio (dono)"
  - "Regra 80-15-4-1: 80% WhatsApp, 15% Direct, 4% Messenger, 1% e-mail"
  - "5 funcionalidades WhatsApp Business: cartão de visitas, respostas automáticas, etiquetas CRM, catálogo, listas de transmissão"
  - "Etiquetas do WhatsApp Business substituem CRM de R$ 100/mês"
  - "Não misturar chip pessoal com chip comercial"
  - "Rotina diária 9h-13h-18h = 2h/dia atende 100% dos canais com CX"
  - "Pedido de avaliação pós-venda dobra a taxa de 5 estrelas"
  - "Pré-venda tem objetivo único: conduzir à compra"
  - "Resposta passiva vs Resposta ativa (conecta dor na solução, devolve a bola)"
  - "5 passos da pré-venda ativa: ouvir, validar, conectar, oferecer, devolver bola"
  - "3 follow-ups quando 'vou pensar': 24h, 7d, 30d"
  - "Empatia = 'eu entendo o que você tá vivendo, e isso tem solução'"
  - "Consultor vende 3x mais que vendedor"
  - "Venda não acaba quando o Pix cai. Venda começa quando o Pix cai."
  - "4 momentos do pós-venda ativo: D+1, D+3-7, D+15-20, D+30-45"
  - "LTV é a métrica central do pós-venda. Cliente que faz 3-4 compras tem LTV 3-4x maior"
  - "3 erros clássicos do pós-venda: (1) Tratar como SAC; (2) Mensagem genérica; (3) Oferecer produto errado"
  - "Conflito é normal, falta de solução não é"
  - "6 níveis de conflito: N1 (silêncio) → N2 (reclama direto) → N3 (marketplace) → N4 (mediação) → N5 (Reclame Aqui) → N6 (Procon/juizado)"
  - "ML: máximo 1% das vendas em mediação (termômetro verde = até 1%)"
  - "Reclame Aqui = oportunidade de outdoor, não pesadelo (case Ain vs AliExpress)"
  - "5 passos da solução de conflito: ouvir, validar, oferecer 3 opções, executar, follow-up"
  - "3 opções clássicas: (A) reembolso total sem devolução; (B) reembolso parcial com devolução; (C) troca por novo com frete por conta da loja"
  - "3 casos negativos fatais: (1) Vender por fora sem NF e bloquear cliente; (2) Demorar mais de 24h; (3) Tratar cliente como número"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.400-3.100 palavras por cena (Cap. 6 está nesse range)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional, 'No próximo capítulo' (próximo cap) com gancho emocional"
  - "Diretriz editorial: caos antes da solução (Fernando 60 dias, Beatriz R$ 0, AliExpress 0% resposta)"
  - "Diretriz editorial: cases com atrito (Fernando, Beatriz, aluna tênis, AliExpress vs Ain)"
  - "Diretriz editorial: variar fechos (Bora/Toca/Te vejo/Vamos)"
  - "Persona Claudia da Patacori usada como ancora narrativa em todo o Cap. 6"
  - "Marketplaces canônicos da Bible v1.5: Mercado Livre, Amazon, Olist, Enjoei, Elo7, Elu7 (NÃO Shopee/Magalu)"
---
# Capítulo 6 — Atendimento que Converte

[Para quem é este capítulo: empreendedores que finalizaram o Cap. 5 com a máquina de audiência rodando. Agora é hora de fazer a audiência render. Este é o capítulo onde o cliente que chega vira cliente que volta, e onde a reputação vira ativo estratégico do negócio.]

[Como ler: as cenas deste capítulo tratam do atendimento como ativo estratégico (CX). A cena 6.1 instala o paradigma (de SAC a CX). A 6.2 entra nos canais (marketplace vs próprios). A 6.3 trata da pré-venda. A 6.4 trata da pós-venda. A 6.5 fecha com a solução de conflitos. A persona Claudia percorre o capítulo como exemplo concreto.]

[Status: ✅ CONCLUÍDO — 5 cenas escritas, fechadas, validadas. Cap. 6 entregue para revisão do usuário.]

---

## SUMÁRIO DO CAPÍTULO 6

- **Cena 6.01** — Atendimento: de SAC a CX (Customer Experience) ✅
- **Cena 6.02** — Canais: marketplace, WhatsApp, Direct, Messenger e e-mail ✅
- **Cena 6.03** — Pré-venda: conquistando antes do clique ✅
- **Cena 6.04** — Pós-venda: encantamento, follow-up, recompra ✅
- **Cena 6.05** — Solução de conflitos: quando o problema aparece ✅

---

"""

corpo = FRONT_MATTER
for n in [1, 2, 3, 4, 5]:
    cena_path = CAP / f"cena_0{n}" / "_saida_final.md"
    txt = cena_path.read_text(encoding="utf-8")
    checksum = CENA_CHECKSUMS[n]
    titulo = CENA_TITULOS[n]
    corpo += f"# Capítulo 6 — Atendimento que Converte\n## Cena 6.0{n}: {titulo}\n\n*[Checksum: {checksum} | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*\n\n---\n\n---\n\n{txt.split('---', 2)[-1].strip() if txt.count('---') >= 2 else txt}\n\n---\n\n\n"

metadados = """

---

## METADADOS DO CAPÍTULO

- **Checksum SHA256 (8 chars):** `PENDENTE`
- **Total de palavras:** ver `wc -w livro_capitulo_06.md`
- **Cenas:** 5 de 5 (COMPLETO)
- **Status:** ✅ CONCLUÍDO

### Resumo executivo do capítulo

**Paradigma instalado:** Atendimento é o que acontece sempre, não só quando dá errado. CX (Customer Experience) é o oposto do SAC em 3 dimensões (tempo, autonomia, visão). Canais organizados em marketplace (hóspede, segue regras) e próprios (dono, edita regras), com regra 80-15-4-1 (WhatsApp/Direct/Messenger/e-mail). Pré-venda com 5 passos (ouvir, validar, conectar, oferecer, devolver bola) e 3 follow-ups. Pós-venda com 4 momentos (D+1, D+3-7, D+15-20, D+30-45). Conflito é normal, falta de solução não é; 6 níveis de gravidade; protocolo 5 passos de solução.

**Cases oficiais reconstruídos literalmente do corpus:** Nubank (cachorro comeu cartão, brinquedo de brinde), Grupo Via Varejo Black Friday (20% via WhatsApp), Ain (2.774 recl, 100% resp) e AliExpress (8.438 recl, 0% resp). **Cases prototípicos com atrito:** Fernando (loja decoração, 60 dias de crise, NPS 18→70 com CX), Beatriz (cosmético, R$ 30k→R$ 0→R$ 30k com pós-venda), Patacori 2019 (5 anúncios derrubados por desvio), aluna tênis corrida (resposta passiva 30% → ativa 80%).

**Próximo capítulo (Cap. 7):** Estrutura de Vendas: o funil que não vaza — sem funil, a audiência vira cliente sem padrão; com funil, cada etapa tem objetivo, cada objetivo tem script, cada script tem métrica.

### Estado dos validadores (todas as 5 cenas)

| Cena | MARCH | Continuidade | Métrica |
|------|-------|--------------|---------|
| 6.1 | APROVADO | APROVADO | 10/10 afirmações + 20/20 perguntas |
| 6.2 | APROVADO | APROVADO | 12/12 afirmações + 20/20 perguntas |
| 6.3 | APROVADO | APROVADO | 11/11 afirmações + 18/18 perguntas |
| 6.4 | APROVADO | APROVADO | 10/10 afirmações + 18/18 perguntas |
| 6.5 | APROVADO | APROVADO | 10/10 afirmações + 20/20 perguntas |
| **Total** | **5/5** | **5/5** | **53/53 afirmações, 96/96 perguntas** |
"""

livro_path = CAP / "livro_capitulo_06.md"
livro_path.write_text(corpo + metadados, encoding="utf-8")
final_content = livro_path.read_text(encoding="utf-8")
checksum_final = hashlib.sha256(final_content.encode("utf-8")).hexdigest()[:8]
final_content = final_content.replace(
    "**Checksum SHA256 (8 chars):** `PENDENTE`",
    f"**Checksum SHA256 (8 chars):** `{checksum_final}`",
)
livro_path.write_text(final_content, encoding="utf-8")

final = livro_path.read_text(encoding="utf-8")
final_checksum = hashlib.sha256(final.encode("utf-8")).hexdigest()[:8]
words = len(final.split())

print(f"livro_capitulo_06.md gerado (COMPLETO)")
print(f"  Checksum: {final_checksum}")
print(f"  Tamanho: {len(final)} bytes")
print(f"  Palavras: {words}")
print(f"  Cenas: 5 de 5 (CAPÍTULO CONCLUÍDO)")
