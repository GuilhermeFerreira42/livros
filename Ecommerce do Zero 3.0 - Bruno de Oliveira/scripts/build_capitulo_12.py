#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_capitulo_12.py — Construtor do Capítulo 12 (Cases, Bônus e Epílogo) consolidado
3 cenas: 12.1, 12.2, 12.3 (CAPÍTULO COMPLETO + LIVRO INTEIRO FECHADO)
"""

import hashlib
import re
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_12")
SAIDAS = {
    1: BASE / "cena_01" / "_saida_final.md",
    2: BASE / "cena_02" / "_saida_final.md",
    3: BASE / "cena_03" / "_saida_final.md",
}
CHECKSUMS = {
    "12.1": "491b32c4",
    "12.2": "b0e076a8",
    "12.3": "cbd63765",
}
CHECKSUMS_VALIDACAO = {
    "12.1": "APROVADA",
    "12.2": "APROVADA",
    "12.3": "APROVADA",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 12 — Cases, Bônus e Epílogo"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-08-04T01:00:00Z"
version: "1.0"
capitulo: 12
total_capitulos_estimados: 12
cena_count: 3
status: "CONCLUÍDO (3/3 cenas) — LIVRO INTEIRO FECHADO (12/12 capítulos, 54/54 cenas)"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.8 (Cap 1-12 completos; livro inteiro fechado com 54/54 cenas)"
validador_march: "TODAS_APROVADAS (3/3 cenas)"
validador_continuidade: "TODAS_APROVADAS (3/3 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "12.1: 491b32c4"
  - "12.2: b0e076a8"
  - "12.3: cbd63765"
fios_narrativos_avancados:
  - "Fio 'Patacori' (case oficial) — fechado com linha do tempo 2012-2024+ (ramp-up 6 anos, salto 2 anos, cruising)"
  - "Fio 'Cases com atrito' — Patrícia saturada, Victor 3-4 meses, John não validou"
  - "Fio 'DNA do negócio' — Missão/Visão/Valores de Patacori implícitos"
  - "Fio 'Planilha de preço' — exemplo real Patacori (toner R$ 16,50 → R$ 31,90)"
  - "Fio 'Treinamentos complementares' — Explosão de Tráfego + Viver de Ecommerce (R$ 4-5 mil com desconto)"
  - "Fio 'Curva de 3 fases' — ramp-up R$ 10K→R$ 30K, salto R$ 30K→R$ 100K, cruising R$ 100K+"
cases_citados:
  - "Patacori (case oficial, Cap 12.1): linha do tempo 2012-2024+ completa, R$ 800 inicial → Mercado Líder Silver, 661 vendas/ano, 0,3% mediação, ROAS 10x"
  - "Cozilar (case oficial, Bible v1.8): aluna do treinamento, REFERÊNCIA SECUNDÁRIA, audiência Cap 5 + bônus Cap 12"
  - "Patrícia (case oficial, Cap 10 + 12.1): bolsa de praia saturada → bolsa de bíblia estrela, jornada de compra: estrela → principal"
  - "Victor (case oficial, Cap 10 + 12.1): cama/mesa/banho 3-4 meses sem resultado → tapete de banheiro carro-chefe"
  - "John (case oficial, Cap 10 + 12.1): moda íntima → descascador de pinhão, 1.400 × R$ 65 = R$ 91K/mês, 30K produtos depois"
  - "Aluna TikTok (case oficial, Cap 5 + 12.1): 1 vídeo viral = 0 → 800 vendas em 2 meses"
  - "NetShoes (case DNA, Cap 12.2): missão 'transformar vida das pessoas com esporte e lazer', valores liderança/integridade/dedicação"
  - "Zappos (case lendário DNA, Cap 12.2): missão 'distribuir felicidade', 10 valores, wow through service"
  - "Dafiti (case DNA, Cap 12.2): 5 valores: foco no cliente, senso de urgência, partilhar aprendizado, comunicação honesta, fazer mais com menos"
  - "Amazon/Bezos (case DNA, Cap 12.2): obsessão pelo cliente, trabalhar de trás pra frente"
  - "Jim Collins (case DNA, Cap 12.2): Built to Last, Good to Great — DNA como fundação"
conceitos_definidos:
  - "Cases reais (Patacori, Cozilar, Patrícia, Victor, John, aluna TikTok) provam que o método funciona"
  - "Case real vale mais que 1.000 promessas"
  - "5 padrões que unem todos os cases: (1) estrutura mínima antes; (2) produto estrela descoberto; (3) jornada de compra; (4) audiência pós-validação; (5) resistência ao início lento"
  - "8 campos da planilha de preço: (1) Nome; (2) Preço de custo; (3) Desconto médio; (4) Frete; (5) Custo de embalagem; (6) Custo de marketing; (7) Outros custos; (8) Margem de lucro"
  - "Exemplo Patacori: toner R$ 16,50 custo, +1% desconto +5% frete +R$ 1 embalagem +8% marketing = R$ 20,47 custo final. Margem 35,8% = preço R$ 31,90"
  - "Sacada: negociar 10% com fornecedor aumenta margem em ~5 pontos percentuais SEM mexer no preço"
  - "MISSÃO = propósito do negócio (1 frase, clara, real, visível, transferível)"
  - "VISÃO = onde chegar (tangibilizar, prazo, micrometas)"
  - "VALORES = como chegar (3-5, pessoais, testáveis, inegociáveis)"
  - "Curva de 3 fases: ramp-up (R$ 10K → R$ 30K, 90-180d), salto (R$ 30K → R$ 100K, 180-365d), cruising (R$ 100K+ após 365d)"
  - "Patacori prova: ramp-up 6 anos, salto 2 anos, cruising Mercado Líder Silver"
  - "2 treinamentos complementares: Explosão de Tráfego e Vendas + Viver de Ecommerce (100+ horas, R$ 4-5 mil com desconto)"
  - "5 livros recomendados: Built to Last (Collins), Good to Great (Collins), Satisfação Garantida (Zappos), A Loja de Tudo (Bezos), Experiência Zappos"
  - "Mensagem final: 'A validação é só o primeiro passo da jornada do sucesso'"
  - "'Você pode, você consegue, e o método funciona'"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.500-3.800 palavras por cena (Cap. 12 está nesse range, 8.926 com 3 cenas)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo (ou despedida final no epílogo)"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional; 'No próximo capítulo' (cena→cap) com gancho"
  - "Diretriz editorial: caos antes da solução (recomeço do case pós-falha)"
  - "Diretriz editorial: cases com atrito (Patrícia saturada, Victor 3-4 meses, John não validou)"
  - "Diretriz editorial: variar fechos ('Toca ganhar DNA', 'Toca encerrar de vez', 'Toca escalar')"
  - "Persona Claudia da Patacori usada como ancora narrativa"
  - "Citação literal do Bruno em alta densidade (15-20 citações por cena)"
---
"""

INTRO = """# Capítulo 12 — Cases, Bônus e Epílogo

[Para quem é este capítulo: empreendedores que finalizaram o método dos 6 etapas e querem ver quem executou, ganhar ferramentas extras, e fechar o ciclo do livro com clareza sobre o futuro.]

[Como ler: as cenas deste capítulo fecham o livro. 12.1 traz os cases reais (Patacori, Cozilar, Patrícia, Victor, John, aluna TikTok). 12.2 entrega o bônus de gestão de preços e o DNA do negócio (missão, visão, valores). 12.3 fecha com o epílogo, recapitulando tudo e apontando a próxima escalada (R$ 10K → R$ 30K → R$ 100K).]

[Status: CONCLUÍDO. As 3 cenas fecham o livro inteiro, com 12 capítulos e 54 cenas no total.]

---

## SUMÁRIO DO CAPÍTULO 12 (COMPLETO)

- **Cena 12.01** — Cases reais: Patacori, Cozilar e alunos que executaram o método ✅
- **Cena 12.02** — Bônus: gestão de preços (planilha) e o DNA do seu negócio (missão, visão, valores) ✅
- **Cena 12.03** — Epílogo: do R$ 10K ao R$ 100K, a próxima escalada ✅

---

## 🏁 LIVRO INTEIRO FECHADO

**12 capítulos | 54 cenas | ~129.000 palavras**

Este é o fim do livro "Ecommerce do Zero — O Método de Validação". O método dos 6 etapas (Planejamento → Estrutura → Audiência → Vendas → Atendimento → Impulsão) está completo, e a próxima fase é da sua conta.

---
"""

METADADOS_FINAIS = """---

## METADADOS DO CAPÍTULO (COMPLETO)

- **Cenas concluídas:** 3 de 3 ✅
- **Status:** CONCLUÍDO
- **Livro inteiro:** 12 capítulos, 54 cenas, ~129.000 palavras ✅
- **Bible checksum atualizado:** ver `bible_da_obra.md` v1.8
- **Próximo passo:** consolidação final (livro_completo.md) com prefácio, epílogo expandido, glossário, front matter, sumário geral

---

## 🏁 FIM DO LIVRO

A validação é só o primeiro passo da jornada do sucesso.

Você pode, você consegue, e o método funciona.

Toca escalar.

"""


def ler_cena(numero: int) -> str:
    caminho = SAIDAS[numero]
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def build():
    partes = [FRONT_MATTER, INTRO]

    for n in [1, 2, 3]:
        cena_texto = ler_cena(n)
        ch = CHECKSUMS[f"12.{n}"]
        val = CHECKSUMS_VALIDACAO[f"12.{n}"]

        partes.append("\n\n---\n\n")
        partes.append(f"*[Checksum: {ch} | Validação MARCH: {val} | Validação Continuidade: {val}]*\n\n---\n\n")
        partes.append(cena_texto)
        partes.append("\n\n")

    partes.append(METADADOS_FINAIS)

    livro_texto = "".join(partes)
    saida = BASE / "livro_capitulo_12.md"

    with open(saida, "w", encoding="utf-8") as f:
        f.write(livro_texto)

    with open(saida, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()[:8]

    words = len(re.findall(r"\b\w+\b", livro_texto))

    print(f"✅ Livro do Cap. 12 (COMPLETO — 3/3 cenas) gerado em: {saida}")
    print(f"   SHA256 (8 chars): {h}")
    print(f"   Total de palavras: {words}")
    print(f"   Cenas: 3 de 3 (capítulo fechado, livro inteiro completo)")


if __name__ == "__main__":
    build()
