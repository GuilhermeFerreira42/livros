#!/usr/bin/env python3
"""build_capitulo_06.py — consolida o Cap. 6 (parcial, 2 cenas) em livro_capitulo_06.md."""
import hashlib
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira")
CAP = BASE / "capitulos/capitulo_06"

CENA_TITULOS = {
    1: "Atendimento: de SAC a CX (Customer Experience)",
    2: "Canais: marketplace, WhatsApp, Direct, Messenger e e-mail",
}

CENA_CHECKSUMS = {
    1: "d6a78202",
    2: "e409c721",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 6 — Atendimento que Converte"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-07-31T19:00:00Z"
version: "1.0-parcial"
capitulo: 6
total_capitulos_estimados: 12
cena_count: 2
status: "EM_ANDAMENTO (2/5 cenas)"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.5 (atualizada após Cap 1 + Cap 2 + Cap 3 + Cap 4 + Cap 5 completos; cenas 6.1 e 6.2 fechadas nesta parcial)"
validador_march: "TODAS_APROVADAS (2/2 cenas)"
validador_continuidade: "TODAS_APROVADAS (2/2 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "6.1: d6a78202"
  - "6.2: e409c721"
fios_narrativos_avancados:
  - "CX (Customer Experience) — Conceito Âncora, instalado em 6.1 (paradigma), operacionalizado em 6.2 (canais)"
  - "Atendimento = o que acontece sempre (não só quando dá errado) — tese central do Cap 6"
  - "Case Fernando (prototípico com atrito: auge→queda→recuperação com CX) — instalado em 6.1"
  - "Case Nubank (literal do corpus: cachorro comeu cartão → brinquedo como brinde) — instalado em 6.1"
  - "Marketplace (hóspede, segue regras) vs Canal próprio (dono, edita regras) — conceito operacional instalado em 6.2"
  - "Regra 80-15-4-1 (80% WhatsApp, 15% Direct, 4% Messenger, 1% e-mail) — instalado em 6.2"
  - "Case Patacori 2019 (5 anúncios derrubados por desvio de cliente) — instalado em 6.2"
cases_citados:
  - "Fernando (aluno, loja decoração, 2019): R$ 18k/mês com 12% recompra em 2020 → Queda 40% em 60 dias por 3 problemas combinados (atraso fornecedor, espelhos trincados, Reclame Aqui 38h sem resposta) → NPS 65→18, recompra 12%→3% → 90 dias depois, com CX: NPS 70, recompra 18%, R$ 18k/mês com 30% mais margem [6.1]"
  - "Nubank (case real, citado Aula 3 do corpus): cliente cujo cachorro comeu o cartão → 2ª via + brinquedo pro cachorro de brinde → viralizou nas redes (Exame, Globo, G1) → equivalente a R$ 1 milhão em marketing com custo de R$ 20-30 [6.1]"
  - "Patacori 2019: vendedor iniciante desviou cliente do Mercado Livre pro WhatsApp → 5 anúncios derrubados em 48h, notificação de punição, 30 dias pra recurso, iniciante foi despedido [6.2]"
  - "Grupo Via Varejo (Casas Bahia) Black Friday: 20% das vendas vieram do WhatsApp (case real citado na Aula 5) [6.2]"
conceitos_definidos:
  - "Atendimento não é o que acontece quando dá errado. Atendimento é o que acontece sempre. (tese central Cap 6)"
  - "SAC vs CX: 3 diferenças — (1) tempo: SAC adia vs CX resolve 1ª; (2) autonomia: SAC script vs CX decisão; (3) visão: SAC custo vs CX ativo"
  - "NPS = % Promotores (9-10) - % Detratores (0-6), neutros (7-8) descartados. Faixas: -100/-1 terrível, 0-49 razoável, 50-74 muito bom, 75-100 excelente"
  - "3 camadas CX do MVP: (1) Responder rápido (1h horário comercial, 4h fora, 24h máx); (2) Resolver na 1ª mensagem; (3) Encantar além da expectativa"
  - "Funil vira ampulheta com CX (cliente feliz vira recorrente, vira microinfluenciador)"
  - "Expectativa do cliente no e-commerce é baixa (produto inteiro, funcionando, no prazo). Quem entrega mais, encanta"
  - "Marketplace (hóspede, segue regras) vs Canal próprio (dono, edita regras)"
  - "Regra do Mercado Livre (Patacori 2019): desvio de cliente pra fora = derrubada de anúncios, banimento possível"
  - "3 pilares CX marketplace: (1) Resposta rápida pré-venda (1h horário comercial); (2) Resposta ativa pós-venda (rotina 2x/dia); (3) Avaliação 5 estrelas como meta, com pedido de avaliação"
  - "Regra 80-15-4-1: 80% WhatsApp, 15% Direct, 4% Messenger, 1% e-mail (da nossa experiência)"
  - "5 funcionalidades WhatsApp Business: (1) Cartão de visitas digital; (2) Respostas automáticas (saudação, ausência, rápidas); (3) Etiquetas como CRM (substitui CRM de R$ 100/mês); (4) Catálogo de produtos; (5) Listas de transmissão"
  - "Não misturar chip pessoal com chip comercial (misturar = atender cliente no meio do jantar da família)"
  - "Direct: 3 regras (1h resposta horário comercial, resposta rápida com atalhos, é audiência não só pré-venda)"
  - "E-mail: comunicação formal, registrada, com protocolo. Tempo de resposta bom: até 24h"
  - "Rotina diária de atendimento: 9h (1h) + 13h (30min) + 18h (30min) = 2h/dia atende 100% dos canais com CX"
  - "Pedido de avaliação pós-venda dobra a taxa de 5 estrelas (a maioria dos clientes satisfeitos não avalia por preguiça)"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.500-2.900 palavras por cena (Cap. 6 está nesse range)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional"
  - "Diretriz editorial: caos antes da solução (Fernando 60 dias de crise, Patacori 5 anúncios derrubados)"
  - "Diretriz editorial: cases com atrito (Fernando auge→queda→recuperação, Patacori 2019 punição)"
  - "Diretriz editorial: variar fechos ('Bora' em 6.1, 'Te vejo' em 6.2)"
  - "Persona Claudia da Patacori (citada literalmente do corpus) usada como ancora narrativa em todo o livro"
  - "Marketplaces canônicos da Bible v1.5: Mercado Livre, Amazon, Olist, Enjoei, Elo7, Elu7 (NÃO Shopee/Magalu)"
---
# Capítulo 6 — Atendimento que Converte

[Para quem é este capítulo: empreendedores que finalizaram o Cap. 5 com a máquina de audiência rodando (audiência-razão, persona-Claudia, canais focados, autoridade, jornada de compra, impulsão seletiva). Agora é hora de fazer a audiência render. Este é o capítulo onde o cliente que chega vira cliente que volta.]

[Como ler: as cenas deste capítulo tratam do atendimento como ativo estratégico (CX), e não como centro de custo (SAC). A cena 6.1 instala o paradigma. A 6.2 entra nos canais (marketplace vs próprios). As próximas (6.3, 6.4, 6.5) tratam de pré-venda, pós-venda e solução de conflitos. A persona Claudia percorre o capítulo como exemplo concreto.]

[Status atual: 2 de 5 cenas escritas (parcial). Fechamento do capítulo completo virá ao fim das cenas 6.3-6.5.]

---

## SUMÁRIO DO CAPÍTULO 6 (ATUAL)

- **Cena 6.01** — Atendimento: de SAC a CX (Customer Experience) ✅
- **Cena 6.02** — Canais: marketplace, WhatsApp, Direct, Messenger e e-mail ✅
- **Cena 6.03** — Pré-venda: conquistando antes do clique (PENDENTE)
- **Cena 6.04** — Pós-venda: transformando cliente em audiência fiel (PENDENTE)
- **Cena 6.05** — Solução de conflitos: quando o problema aparece (PENDENTE)

---

"""

# Monta o corpo
corpo = FRONT_MATTER
for n in [1, 2]:
    cena_path = CAP / f"cena_0{n}" / "_saida_final.md"
    txt = cena_path.read_text(encoding="utf-8")
    checksum = CENA_CHECKSUMS[n]
    titulo = CENA_TITULOS[n]
    corpo += f"# Capítulo 6 — Atendimento que Converte\n## Cena 6.0{n}: {titulo}\n\n*[Checksum: {checksum} | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*\n\n---\n\n---\n\n{txt.split('---', 2)[-1].strip() if txt.count('---') >= 2 else txt}\n\n---\n\n\n"

# Calcula checksum do livro_capitulo_06.md
livro_path = CAP / "livro_capitulo_06.md"
livro_path.write_text(corpo, encoding="utf-8")

# Metadados finais
metadados = """

---

## METADADOS DO CAPÍTULO (PARCIAL)

- **Checksum SHA256 (8 chars):** `PENDENTE_RECALCULO`
- **Total de palavras:** ver `wc -w livro_capitulo_06.md`
- **Cenas:** 2 de 5 (parcial)
- **Status:** EM_ANDAMENTO (Cap. 6 ainda em construção)
- **Próxima cena a escrever:** 6.3 (Pré-venda: conquistando antes do clique)

### Próximas cenas planejadas (6.3, 6.4, 6.5)

**Cena 6.3 — Pré-venda: conquistando antes do clique:** como responder perguntas de marketplace de forma que converte. Como usar o chat do WhatsApp como máquina de venda. Como qualificar a Claudia no Direct antes dela chegar no checkout. Cada mensagem pré-venda é uma Claudia com a mão no bolso.

**Cena 6.4 — Pós-venda: transformando cliente em audiência fiel:** encantamento, follow-up, recompra. Como o pedido de avaliação dobra 5 estrelas. A virada de "cliente sumido" pra "cliente recorrente".

**Cena 6.5 — Solução de conflitos: quando o problema aparece:** protocolo para crises, reembolsos, reclamações. Como recuperar um cliente insatisfeito. Quando não recuperar e seguir em frente.
"""

livro_path.write_text(corpo + metadados, encoding="utf-8")

# Reload e recalcula checksum
final_content = livro_path.read_text(encoding="utf-8")
import re
final_content = re.sub(
    r"\*\*Checksum SHA256 \(8 chars\):\*\* `PENDENTE_RECALCULO`",
    "**Checksum SHA256 (8 chars):** `PENDENTE`",
    final_content,
)
livro_path.write_text(final_content, encoding="utf-8")
checksum_final = hashlib.sha256(final_content.encode("utf-8")).hexdigest()[:8]
final_content = final_content.replace(
    "**Checksum SHA256 (8 chars):** `PENDENTE`",
    f"**Checksum SHA256 (8 chars):** `{checksum_final}`",
)
livro_path.write_text(final_content, encoding="utf-8")

# Stats
words = len(final_content.split())
print(f"livro_capitulo_06.md gerado")
print(f"  Checksum: {checksum_final}")
print(f"  Tamanho: {len(final_content)} bytes")
print(f"  Palavras: {words}")
print(f"  Cenas: 2 (parcial)")


CENA_TITULOS = {
    1: "Audiência é rei: a nova regra do jogo",
    2: "Persona: para quem você fala, de verdade",
    3: "Canais de conteúdo: onde sua persona está",
    4: "Autoridade: como virar referência",
    5: "A jornada de compra e a régua de conteúdo",
    6: "Impulsão de conteúdo: o que já funciona, amplifique",
}

CENA_CHECKSUMS = {
    1: "da664f9a",
    2: "ae72e290",
    3: "eee51da1",
    4: "675872f4",
    5: "b7a11439",
    6: "9c7788d5",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 5 — Audiência é Rei"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-07-31T18:00:00Z"
version: "1.0"
capitulo: 5
total_capitulos_estimados: 12
cena_count: 6
status: "CONCLUIDO"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.5 (atualizada após Cap 1 + Cap 2 + Cap 3 + Cap 4 + Cap 5 completos — Cenas 1.1 a 5.6 CONCLUÍDAS)"
validador_march: "TODAS_APROVADAS (6/6 cenas)"
validador_continuidade: "TODAS_APROVADAS (6/6 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "5.1: da664f9a"
  - "5.2: ae72e290"
  - "5.3: eee51da1"
  - "5.4: 675872f4"
  - "5.5: b7a11439"
  - "5.6: 9c7788d5"
fios_narrativos_avancados:
  - "Audiência é Rei — Conceito Âncora, instalado em 5.1 (paradigma conceitual), aprofundado em 5.2 (persona), 5.3 (canais), 5.4 (autoridade), 5.5 (jornada), 5.6 (impulsão) — FECHADO em 5.6"
  - "Ciclo virtuoso vs ciclo vicioso — diferenciação instalada em 5.1, operacionalizada em 5.5 e 5.6"
  - "Persona da Patacori (Claudia) — instalada em 5.2, usada como ancora narrativa em 5.3, 5.4, 5.5, 5.6"
  - "Cases com atrito (Padrão Bruno) — Renata (5.1), Marcos/Ricardo (5.2), Patacori 2020 + aluna TikTok 2022 (5.3), Patrícia Enrique (5.4), Cleid (5.5), Alisson (5.6)"
  - "Patrícia Enrique — case oficial reconstruído literalmente da Aula 5, instalado em 5.4 como case-âncora de autoridade"
  - "Patacori 2017 (R$ 1.500 Facebook Ads, R$ 800 vendas) — case de caos instalado em 5.1, ecoa como aviso em 5.6"
  - "Impulsão Seletiva (Bible v1.5) — conceito-âncora operacionalizado em 5.6 com case Alisson"
  - "Triângulo do Sucesso (Audiência × Estrutura × Ofertas) — Audiência completa neste cap, Ofertas antecipadas para Cap 7"
cases_citados:
  - "Patacori 2017: R$ 1.500 em Facebook Ads, R$ 800 em vendas, prejuízo (caos antes da virada conceitual) [5.1]"
  - "Renata 2019 (joias artesanais, 180 pedidos, 95% clientes únicos) → 2º sem 2020 (Instagram 200→8.000) → 2021 (60% recorrência, CPA -70%) [5.1]"
  - "Patacori 2019: persona 'Claudia' (32, advogada, mãe, espiritual) construída em 2h + 15 entrevistas com clientes; conteúdo pós-Claudia triplicou alcance em 4 meses [5.2]"
  - "Marcos (aluno, loja suplementos): persona 'Ricardo' (28, mora com mãe, assistente); 6 meses: 1.200→9.000 seguidores, R$ 3k→R$ 6k/mês [5.2]"
  - "Patacori 2020: tentativa de 5 canais (IG, TikTok, YouTube, Pinterest, FB, Twitter), 8 meses, resultado medíocre em todos; decisão de focar no IG [5.3]"
  - "Patacori 2019 (entrevistas): 13 de 15 clientes usavam IG diariamente, 11 descobriram a marca no IG, 0 mencionaram TikTok como canal de descoberta [5.3]"
  - "Aluna cosmético natural 2022: 0→80k seguidores no TikTok em 6 meses, 200 cliques/mês no link da bio, 5 vendas/mês, 2 recorrentes em 6 meses (alcance ≠ audiência qualificada) [5.3]"
  - "Patrícia Enrique: pré-2016 marca sem rosto, 5-10 pedidos/mês; pós-construção de autoridade 200-300 bolsas/mês, 60k seguidores, collabs, entrevistas, virou referência [5.4]"
  - "Reserva (Ron) e Arezzo (Birman): exemplos de marca forte representada por pessoa [5.4]"
  - "Cleid (Uberlândia, calçados): 15 pares/mês com só catálogo → 60 pares/mês em 4 meses com a régua topo/meio/fundo [5.5]"
  - "Alisson (utensílio cozinha aço inox, 2021): R$ 4.800 investidos em 6 meses anunciando produto de fundo (fracasso) → R$ 2.700 investidos no mês 1 com conteúdo de topo/meio (R$ 22.000 vendas, ROI 8x) → R$ 60k/mês em 6 meses [5.6]"
conceitos_definidos:
  - "Audiência ≠ Cliente (cliente é transação, audiência é relação)"
  - "Audiência é rei (paradigma substitui 'conteúdo é rei')"
  - "Custo de aquisição de cliente (CPA) — crescente de 2018 (R$ 25-40) a 2026 (R$ 150+ em vários segmentos)"
  - "Ciclo virtuoso (conteúdo bom → audiência → venda → recorrência → indicação) vs ciclo vicioso (conteúdo solto → audiência zero → anúncio frio → venda pontual → cliente some)"
  - "Persona ≠ público-alvo (persona = pessoa específica com nome, idade, profissão, rotina, dor, desejo, medo)"
  - "5 passos para construir persona: (1) demografia; (2) rotina; (3) dor, desejo, medo; (4) o que consome; (5) documento de 1 página"
  - "Rotina da persona = QUANDO postar; consumo da persona = O QUE postar; dor e medo da persona = gancho do conteúdo"
  - "Persona evolui (revisar a cada 6 meses) e é filtro de priorização, não de exclusão"
  - "4 papéis de canal: Instagram (identidade/relacionamento), TikTok (alcance/descoberta), YouTube (autoridade/profundidade), Blog/SEO (captura de intenção)"
  - "Regra dos 2 canais: 1 principal + 1 secundário no máximo no MVP"
  - "MVP 90 dias de audiência no IG: fundação (1-2 sem), consistência (3-6 sem), experimentação (7-10 sem), fechamento (11-13 sem)"
  - "TikTok dá alcance, mas não dá, necessariamente, audiência qualificada"
  - "Pessoas não compram de pessoas, compram de marcas representadas por pessoas"
  - "4 pilares da autoridade: (1) Posicionamento claro, (2) Consistência absurda, (3) Prova social visível, (4) Pessoa por trás da marca"
  - "1.500 posts em 3+ anos para virar referência no Instagram"
  - "Consistência > qualidade; algoritmo recompensa regularidade"
  - "Prova social é terceirização de autoridade (80% dos clientes satisfeitos aceitam depoimento)"
  - "Autoridade em 36-60 meses, não 90 dias"
  - "3 fases do funil: Topo (dor consciente, solução não descoberta) / Meio (dor consciente, solução em descoberta) / Fundo (dor consciente, solução e marca decididas)"
  - "Jornada instantânea (dor latente, solução conhecida) vs jornada estendida (dor consciente, solução em descoberta)"
  - "Régua semanal: 2-3 topo nos dias 1-2, 2-3 meio nos dias 3-5, 1-2 fundo nos dias 6-7"
  - "Impulsão Seletiva (Bible v1.5): anunciar SÓ o que já está funcionando organicamente"
  - "3 sinais reais de conteúdo campeão: salvamento, compartilhamento, comentário qualificado (like é vaidade)"
  - "5 passos da impulsão: (1) orgânico 7-14 dias; (2) R$ 30-50/dia por campeão; (3) medir cascata (salvamento < R$ 0,50, clique < R$ 1,50); (4) trocar quando cansar; (5) nunca anunciar produto de fundo sem base aquecida"
  - "Fórmula de bolso da impulsão: 2-3 campeões + R$ 30-50/dia + persona + 'saiba mais' + teste 7 dias + ROI 5x + rotação semanal"
  - "Efeito cascata da impulsão: 1.500 visitas → 400 seguidores → 80 cliques → 25 mensagens → 8 compras (R$ 180 ticket) = R$ 1.440 vendas com R$ 90 investidos = ROI 16x"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.300-3.200 palavras por cena (Cap. 5 está nesse range)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional, 'No próximo capítulo' (próximo cap) com gancho emocional"
  - "Diretriz editorial: caos antes da solução (Patacori 2017, Marcos R$3k, Patacori 2020 5 canais, Patrícia sem rosto, Cleid só catálogo, Alisson R$ 4.800 perdidos)"
  - "Diretriz editorial: cases com atrito (Renata, Marcos, aluna TikTok, Patrícia, Cleid, Alisson)"
  - "Diretriz editorial: variar fechos (Bora/Toca/Vamos/Te vejo/Te espero — rotação ao longo das 6 cenas)"
  - "Persona Claudia da Patacori (citada literalmente do corpus) usada como ancora narrativa em todo o Cap. 5"
  - "Ana Clara (diretora de marketing) e Babi (sócio do Bruno) podem ser citadas por papel, sem aprofundar personagens"
---
# Capítulo 5 — Audiência é Rei

[Para quem é este capítulo: empreendedores que finalizaram o Cap. 4 com a estrutura mínima viável (CNPJ, Bling, marketplace, catálogo, embalagem, vitrine) montada e rodando. Agora é hora de fazer essa estrutura render. Este é o capítulo onde o produto começa a se encontrar com as pessoas certas.]

[Como ler: as cenas deste capítulo acompanham a construção da audiência da perspectiva conceitual até a prática. A cena 5.1 instala o paradigma "audiência é rei". A 5.2 aprofunda persona. A 5.3 entra em canais. A 5.4 entra em autoridade. A 5.5 alinha conteúdo com a jornada de compra. A 5.6 fecha com a impulsão seletiva — anunciar só o que já funciona organicamente. A persona Claudia da Patacori percorre todo o capítulo como exemplo concreto.]

[Status: ✅ CONCLUÍDO — 6 cenas escritas, fechadas, validadas. Cap. 5 entregue para revisão do usuário.]

---

## SUMÁRIO DO CAPÍTULO 5

- **Cena 5.01** — Audiência é rei: a nova regra do jogo ✅
- **Cena 5.02** — Persona: para quem você fala, de verdade ✅
- **Cena 5.03** — Canais de conteúdo: onde sua persona está ✅
- **Cena 5.04** — Autoridade: como virar referência ✅
- **Cena 5.05** — A jornada de compra e a régua de conteúdo ✅
- **Cena 5.06** — Impulsão de conteúdo: o que já funciona, amplifique ✅

---

"""

# Monta o corpo
corpo = FRONT_MATTER
for n in [1, 2, 3, 4, 5, 6]:
    cena_path = CAP / f"cena_0{n}" / "_saida_final.md"
    txt = cena_path.read_text(encoding="utf-8")
    checksum = CENA_CHECKSUMS[n]
    titulo = CENA_TITULOS[n]
    corpo += f"# Capítulo 5 — Audiência é Rei\n## Cena 5.0{n}: {titulo}\n\n*[Checksum: {checksum} | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*\n\n---\n\n---\n\n{txt.split('---', 2)[-1].strip() if txt.count('---') >= 2 else txt}\n\n---\n\n\n"

# Calcula checksum do livro_capitulo_05.md
livro_path = CAP / "livro_capitulo_05.md"
livro_path.write_text(corpo, encoding="utf-8")

# Metadados finais
metadados = """

---

## METADADOS DO CAPÍTULO

- **Checksum SHA256 (8 chars):** `PENDENTE_RECALCULO`
- **Total de palavras:** ver `wc -w livro_capitulo_05.md`
- **Cenas:** 6 de 6 (COMPLETO)
- **Status:** ✅ CONCLUÍDO

### Resumo executivo do capítulo

**Paradigma instalado:** Audiência é rei (substitui "conteúdo é rei"). Construção de audiência é processo de anos (36-60 meses), não de 90 dias. Persona é o instrumento central — sem persona, conteúdo é tiro no escuro. Canais focados (1 principal + 1 secundário) superam dispersão em 5 canais. Autoridade é construída com posicionamento, consistência, prova social e pessoa por trás. Jornada de compra tem 3 fases (topo, meio, fundo) e a régua semanal (2-3/2-3/1-2) é o que prepara a Claudia pra comprar. Impulsão seletiva: anunciar SÓ o que já funciona organicamente, com 3 sinais reais (salvamento, compartilhamento, comentário qualificado).

**Cases oficiais reconstruídos literalmente do corpus:** Claudia (Patacori, persona), Patrícia Enrique (autoridade), Cleid (jornada/régua). **Cases prototípicos com atrito:** Renata (audiência), Marcos/Ricardo (persona), Patacori 2020 5 canais (canais), Aluna TikTok 2022 (alcance ≠ audiência), Alisson (impulsão).

**Próximo capítulo (Cap. 6):** Atendimento que converte — sem atendimento, a audiência vira cliente único e some. Com atendimento, vira cliente recorrente, indica, e fecha o ciclo. CX é o ativo mais valioso do negócio depois da audiência.

### Estado dos validadores (todas as 6 cenas)

| Cena | MARCH | Continuidade | Métrica |
|------|-------|--------------|---------|
| 5.1 | APROVADO | APROVADO | 10/10 afirmações + 12/12 perguntas |
| 5.2 | APROVADO | APROVADO | 10/10 afirmações + 17/17 perguntas |
| 5.3 | APROVADO | APROVADO | 10/10 afirmações + 17/17 perguntas |
| 5.4 | APROVADO | APROVADO | 13/13 afirmações + 18/18 perguntas |
| 5.5 | APROVADO | APROVADO | 10/10 afirmações + 18/18 perguntas |
| 5.6 | APROVADO | APROVADO | 10/10 afirmações + 20/20 perguntas |
| **Total** | **6/6** | **6/6** | **63/63 afirmações, 102/102 perguntas** |
"""

livro_path.write_text(corpo + metadados, encoding="utf-8")

# Reload e recalcula checksum
final_content = livro_path.read_text(encoding="utf-8")
final_checksum = hashlib.sha256(final_content.encode("utf-8")).hexdigest()[:8]

# Atualiza o checksum no próprio arquivo
import re
final_content = re.sub(
    r"\*\*Checksum SHA256 \(8 chars\):\*\* `PENDENTE_RECALCULO`",
    f"**Checksum SHA256 (8 chars):** `{final_checksum}`",
    final_content,
)
livro_path.write_text(final_content, encoding="utf-8")

# Stats
words = len(final_content.split())
print(f"livro_capitulo_05.md gerado (COMPLETO)")
print(f"  Checksum: {final_checksum}")
print(f"  Tamanho: {len(final_content)} bytes")
print(f"  Palavras: {words}")
print(f"  Cenas: 6 de 6 (CAPÍTULO CONCLUÍDO)")


