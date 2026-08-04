#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_capitulo_08.py — Construtor do Capítulo 8 (Impulsão Estratégica) consolidado
5 cenas: 8.1, 8.2, 8.3, 8.4, 8.5 (CAPÍTULO COMPLETO)
"""

import os
import hashlib
import re
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_08")
SAIDAS = {
    1: BASE / "cena_01" / "_saida_final.md",
    2: BASE / "cena_02" / "_saida_final.md",
    3: BASE / "cena_03" / "_saida_final.md",
    4: BASE / "cena_04" / "_saida_final.md",
    5: BASE / "cena_05" / "_saida_final.md",
}
CHECKSUMS = {
    "8.1": "d834eccb",
    "8.2": "375eb2d3",
    "8.3": "7b1eceae",
    "8.4": "1ab2f172",
    "8.5": "5afa54ca",
}
CHECKSUMS_VALIDACAO = {
    "8.1": "APROVADA",
    "8.2": "APROVADA",
    "8.3": "APROVADA",
    "8.4": "APROVADA",
    "8.5": "APROVADA",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 8 — Impulsão Estratégica"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-08-04T01:00:00Z"
version: "1.0"
capitulo: 8
total_capitulos_estimados: 12
cena_count: 5
status: "CONCLUÍDO (5/5 cenas)"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.6 (Cap 1-8 completos; Cap 8 fechou com 5/5 cenas)"
validador_march: "TODAS_APROVADAS (5/5 cenas)"
validador_continuidade: "TODAS_APROVADAS (5/5 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "8.1: d834eccb"
  - "8.2: 375eb2d3"
  - "8.3: 7b1eceae"
  - "8.4: 1ab2f172"
  - "8.5: 5afa54ca"
fios_narrativos_avancados:
  - "Impulsão Seletiva (Bible v1.5 Conceito Âncora) — instalado em 8.1: anunciar SÓ o que já funciona"
  - "Tese central: orgânico e anúncio = mesmo canal, escalas diferentes"
  - "2 tipos de conteúdo pra impulsionar: audiência (Cap. 5) e conversão (Cap. 7)"
  - "Estratégia inicial sem dados: turbinar todas por 3 dias R$ 6/dia, sem pausar nenhuma"
  - "2 caminhos: Turbinar/Promover (iniciante) vs Gerenciador Meta Ads (avançado)"
  - "2 públicos atalho: curtidores+amigos (FB) e automático (IG)"
  - "Investimento inicial R$ 150/semana (4 posts × R$ 40/7 dias)"
  - "Conta de anúncios bem configurada = proteção contra bloqueio por 'atividade incomum'"
  - "2 caminhos de conta: perfil pessoal (MVP) vs BM (escala, a partir de R$ 5-10k/mês)"
  - "7 passos de configuração: fuso BR, moeda BRL, dados reais, método pagamento, limites, vinculação IG"
  - "4 cuidados de segurança: dispositivo único, usuário único, não misturar contas, dados reais"
  - "Análise de resultados: 5-10x acima da média = candidato a turbinar (8.3)"
  - "2 caminhos de análise: Facebook (granular) vs Instagram (complementar) [8.3]"
  - "CPC e CPS: Patacori R$ 1/clique, R$ 3/seguidor, 87% mulher 13% homem [8.3]"
  - "4 tipos de público personalizado: Pixel site, Instagram, Facebook, Lookalike (8.4)"
  - "Audience Insights: azul vs cinza, Patacori 25-54, casado, faculdade (8.4)"
  - "8 públicos para Mês 1: visitantes 30/180, carrinho 30, engajados IG 14/180, FB 30, lookalike visitantes 1%, lookalike compradores 1%"
  - "Público > criativo: 'melhor criativo do mundo com público errado vai dar ruim'"
  - "Mentalidade de crescimento progressivo: hoje X, amanhã 2X, depois 3X (8.5)"
  - "R$ 50/dia como ponto de partida (não orçamento mensal fixo)"
  - "Orçamento consolidado: R$ 50/dia total distribuído entre 3-5 posts"
  - "Cálculo do 'comprometido amanhã'"
  - "4 gatilhos de escalar / 4 motivos de pausar / 4 durações de campanha"
  - "Cap 8 não é módulo de anúncios, é módulo de impulsão"
cases_citados:
  - "Patacori (case oficial do corpus, Aula 4): 11.000 fãs × 300 amigos = 3,3 milhões de público para lookalike. [8.1]"
  - "Patacori (case oficial do corpus, Aula 2): conta BM com R$ 8.000+ gastos, limite R$ 3.000, cobrança por faixa. [8.2]"
  - "Patacori (case oficial do corpus, Aula 3): Bruno usa cartão virtual Nubank/Inter/Bradesco por segurança. [8.2]"
  - "Patacori (case oficial do corpus, Aula 4): 4 posts analisados — Palo Santo 10x, incenso 3.5K, incenso+produto 513, cinzas 1.867. [8.3]"
  - "Patacori (case oficial do corpus, Aula 4): dados demográficos 87% mulher 13% homem, 18-54 anos, R$ 1/clique, R$ 3/seguidor. [8.3]"
  - "Patacori (case oficial do corpus, Aula 4): post de incenso de jardim 50.000 alcance (parte pago), uncienso séculos 2.660 likes 39 salvamentos. [8.3]"
  - "Patacori (case oficial do corpus, Aula 5): 11.000 fãs, 345 dias de janela, lookalike de visitantes e compradores. [8.4]"
  - "Patacori (case oficial do corpus, Aula 5): Audience Insights 1-1,5M (mulher, 18-54, Brasil, incenso, aromaterapia), 25-54, casado, faculdade. [8.4]"
  - "Patacori (case oficial do corpus, Aula 6): distribuição de orçamento entre posts ativos. [8.5]"
conceitos_definidos:
  - "Sem impulsão estratégica, o sistema trava no orgânico (citação literal Bruno)"
  - "Impulsão é escala, não descoberta: 'A gente não vai impulsionar tudo. A gente vai impulsionar só o que já está gerando o resultado'"
  - "Orgânico e anúncio = mesmo canal, escalas diferentes"
  - "2 tipos de conteúdo pra impulsionar: (1) audiência (Cap. 5, construir audiência); (2) post de conversão (Cap. 7, gerar venda)"
  - "Estratégia inicial sem dados: turbinar TODAS as publicações por 3 dias, com R$ 6/dia, sem pausar nenhuma"
  - "Por que 3 dias (iniciante) e 7 dias (avançado): 'dias da semana diferente' (Bruno literal)"
  - "2 caminhos: botão Turbinar/Promover (iniciante, MVP) vs Gerenciador de Anúncios Meta Ads (avançado, escala)"
  - "2 públicos atalho do iniciante: 'Pessoas que curtiram a página e amigos' (FB) + público automático do Instagram"
  - "Investimento padrão Bruno: R$ 5,71/dia (R$ 40/7 dias, mínimo Facebook) por post, 2 FB + 2 IG = R$ 21,40/dia = R$ 150/semana"
  - "Erro fatal: anunciar produto que não vende organicamente, esperando que o anúncio 'descubra' o público"
  - "2 caminhos de conta: perfil pessoal (MVP) vs BM Business Manager (escala, R$ 5-10k/mês)"
  - "7 passos de configuração: (1) acessar gerenciador, (2) fuso Brasil, (3) moeda BRL, (4) dados reais, (5) método pagamento, (6) limite cobrança + limite gastos, (7) vincular Instagram"
  - "Fuso horário: ajustar para Brasil. Padrão vem Costa Oeste americana (Bruno literal)"
  - "Moeda: BRL. 'Não dá para mudar depois' (Bruno literal)"
  - "Dados pessoais: CPF real, nome real, endereço real. 'CPF de uma outra pessoa = indicativo de fraude' (Bruno literal)"
  - "Cartão virtual (Nubank/Inter/Bradesco) é mais seguro que cartão real (cancelamento imediato)"
  - "SuperDigital + PayPal para quem não tem cartão de crédito. Facebook não aceita pré-pago, mas aceita PayPal"
  - "Faixas de cobrança Facebook: R$ 80 → R$ 160 → R$ 240 → R$ 800 → R$ 1.600 → R$ 2.400 → R$ 3.000. Bruno recomenda R$ 800"
  - "Limite de gastos absoluto = teto do mês (sangria)"
  - "4 cuidados de segurança: (1) não logar em dispositivos desconhecidos, (2) usuário único no computador, (3) não misturar contas, (4) perfil com dados reais"
  - "Bloqueio por 'atividade incomum' é feito por robô que analisa padrões. Prevenção 100x melhor que correção (que demora 7-30 dias)"
  - "Análise prévia: orgânico é espelho do que audiência quer. Você não vai adivinhar o que funciona. Você vai medir"
  - "1 dado pode ser acaso, 3-5 dados é padrão"
  - "2 caminhos de análise: Facebook (granular, alcance pago separado) e Instagram (complementar)"
  - "Régua do Bruno: 5-10x acima = turbinar / 3-5x = observar / dentro = não mexer / abaixo = deixar morrer"
  - "Padrão de impulsionamento sem público: 3 dias R$ 6/dia, todas as publicações, sem pausar"
  - "Mínimo Facebook: R$ 6/dia × 7 dias = R$ 40 total (R$ 5,71/dia)"
  - "CPC e CPS Patacori: R$ 1/clique, R$ 3/seguidor. Tendência importa mais que absoluto"
  - "5 erros da análise: (1) olhar curtidas não alcance; (2) não separar pago de orgânico; (3) decidir com 1 dado; (4) audiência como venda; (5) não anotar"
  - "Público > criativo: 'O melhor criativo do mundo, com o público errado, vai dar ruim'"
  - "2 famílias de público: comportamento (Pixel, engajamento) vs dados Facebook (interesse, demografia)"
  - "4 tipos de público: (1) Pixel site (visitantes 30-180d, carrinho, checkout, produto); (2) Instagram (14d oferta, 180d audiência); (3) Facebook (14-365d); (4) Lookalike (1-10%, mín. 100 pessoas)"
  - "Audience Insights: ferramenta analítica Facebook, mostra azul (seu público) vs cinza (média Facebook)"
  - "Patacori Audience Insights: 1-1,5M (mulher, 18-54, Brasil, incenso, aromaterapia), 25-54, casado, faculdade, menos 18-24 que média"
  - "8 públicos para Mês 1: visitantes 30d, visitantes 180d, carrinho 30d, engajados IG 14d, engajados IG 180d, engajados FB 30d, lookalike 1% visitantes 30d, lookalike 1% compradores 180d"
  - "5 erros do público: (1) criar e nunca usar; (2) público de 10 pessoas; (3) não atualizar; (4) misturar quente com frio; (5) não testar interesse"
  - "Mentalidade de crescimento progressivo: hoje X, amanhã 2X, depois 3X"
  - "Antigamente Bruno dava orçamento mensal fixo. Hoje mudou porque engessava"
  - "R$ 50/dia é ponto de partida (não R$ 1.500/mês)"
  - "Orçamento consolidado: R$ 50/dia é o bolo total, não 1 post com R$ 50"
  - "Cálculo do 'comprometido amanhã': somar campanhas ativas para saber o que cabe hoje"
  - "4 gatilhos de escalar: ROI 2x+, CPC caindo, público crescendo, criativo novo performando"
  - "4 motivos de pausar: ROI negativo, CPC subindo, criativo queimado, post off da régua"
  - "4 durações: 3d (teste), 7d (público personalizado), 14-30d (lookalike), 5-7d (remarketing)"
  - "5 erros do orçamento: mensal fixo, R$ 50/dia em 1 post, não calcular comprometido amanhã, escalar prejuízo, parar de investir por uma campanha ruim"
  - "5 boas práticas: valor diário, céu é o limite, só investir no que gera resultado, orgânico vendeu → impulsionar vende mais, orgânico não vendeu → não impulsionar"
  - "Cap 8 não é módulo de anúncios, é módulo de impulsão"
  - "Da série de 10-15-20% das campanhas acertam, e esse percentual banca os custos das que erraram"
  - "Resultado é diretamente proporcional ao investimento"
  - "A diferença é o método, não o dinheiro"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.300-3.700 palavras por cena (Cap. 8 está nesse range, 13.368 com 4 cenas; completo ~17.000)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional; 'No próximo capítulo' (cena→cap) com gancho"
  - "Diretriz editorial: caos antes da solução (conta mal configurada → 7 passos)"
  - "Diretriz editorial: cases com atrito (Patacori R$ 8k vs iniciante R$ 150/semana)"
  - "Diretriz editorial: variar fechos ('Toca configurar a máquina de anúncios', 'Toca analisar resultados', 'Te vejo construindo público', 'Bora calcular orçamento', 'Te vejo no R$ 10K')"
  - "Persona Claudia da Patacori usada como ancora narrativa"
  - "Citação literal do Bruno em quase toda cena (alta densidade: 15-23 citações por cena)"
---
"""

INTRO = """# Capítulo 8 — Impulsão Estratégica

[Para quem é este capítulo: empreendedores que finalizaram o Cap. 7 com a máquina de vendas rodando. Agora é hora de pegar o que já funciona organicamente, e dar o empurrão final com Impulsão Seletiva — anunciar SÓ o que a Claudia já está validando.]

[Como ler: as cenas deste capítulo tratam da impulsão estratégica. 8.1 instala a tese (anunciar só o que já funciona). 8.2 entra na configuração da conta de anúncios. 8.3 mostra como analisar resultados orgânicos antes de gastar. 8.4 ensina a criar públicos personalizados. 8.5 fecha com a mentalidade de crescimento progressivo de orçamento. A persona Claudia percorre o capítulo como exemplo concreto.]

[Status: CONCLUÍDO. As 5 cenas formam a tese central do capítulo: a diferença é o método, não o dinheiro.]

---

## SUMÁRIO DO CAPÍTULO 8 (COMPLETO)

- **Cena 8.01** — A estratégia de impulsão: anunciar SÓ o que já funciona ✅
- **Cena 8.02** — Conta de anúncios e método de pagamento: configurando o motor ✅
- **Cena 8.03** — Analisando resultados orgânicos: separando joio de trigo ✅
- **Cena 8.04** — Criando públicos: o motor silencioso que faz o anúncio achar a Claudia ✅
- **Cena 8.05** — Quanto investir: a mentalidade de crescimento progressivo ✅

---
"""

METADADOS_FINAIS = """---

## METADADOS DO CAPÍTULO (COMPLETO)

- **Cenas concluídas:** 5 de 5 ✅
- **Status:** CONCLUÍDO
- **Bible checksum atualizado:** ver `bible_da_obra.md` v1.6
- **Próximo capítulo a escrever:** 9 (Parabéns! Você validou o negócio)

"""


def ler_cena(numero: int) -> str:
    caminho = SAIDAS[numero]
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def build():
    partes = [FRONT_MATTER, INTRO]

    for n in [1, 2, 3, 4, 5]:
        cena_texto = ler_cena(n)

        ch = CHECKSUMS[f"8.{n}"]
        val = CHECKSUMS_VALIDACAO[f"8.{n}"]

        # Anotação de checksum/validação
        partes.append("\n\n---\n\n")
        partes.append(f"*[Checksum: {ch} | Validação MARCH: {val} | Validação Continuidade: {val}]*\n\n---\n\n")
        partes.append(cena_texto)
        partes.append("\n\n")

    partes.append(METADADOS_FINAIS)

    livro_texto = "".join(partes)
    saida = BASE / "livro_capitulo_08.md"

    with open(saida, "w", encoding="utf-8") as f:
        f.write(livro_texto)

    # Calcula checksum
    with open(saida, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()[:8]

    # Conta palavras
    words = len(re.findall(r"\b\w+\b", livro_texto))

    print(f"✅ Livro do Cap. 8 (COMPLETO — 5/5 cenas) gerado em: {saida}")
    print(f"   SHA256 (8 chars): {h}")
    print(f"   Total de palavras: {words}")
    print(f"   Cenas: 5 de 5 (capítulo fechado)")


if __name__ == "__main__":
    build()
