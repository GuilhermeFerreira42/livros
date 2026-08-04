#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_capitulo_11.py — Construtor do Capítulo 11 (O ERP na Prática - Bling) consolidado
3 cenas: 11.1, 11.2, 11.3 (CAPÍTULO COMPLETO)
"""

import hashlib
import re
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_11")
SAIDAS = {
    1: BASE / "cena_01" / "_saida_final.md",
    2: BASE / "cena_02" / "_saida_final.md",
    3: BASE / "cena_03" / "_saida_final.md",
}
CHECKSUMS = {
    "11.1": "d8547231",
    "11.2": "77748cb9",
    "11.3": "2e58f8b1",
}
CHECKSUMS_VALIDACAO = {
    "11.1": "APROVADA",
    "11.2": "APROVADA",
    "11.3": "APROVADA",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 11 — O ERP na Prática (Bling)"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-08-04T01:00:00Z"
version: "1.0"
capitulo: 11
total_capitulos_estimados: 12
cena_count: 3
status: "CONCLUÍDO (3/3 cenas)"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.8 (Cap 1-11 completos; Cap 11 fechou com 3/3 cenas)"
validador_march: "TODAS_APROVADAS (3/3 cenas)"
validador_continuidade: "TODAS_APROVADAS (3/3 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "11.1: d8547231"
  - "11.2: 77748cb9"
  - "11.3: 2e58f8b1"
fios_narrativos_avancados:
  - "Fio 'A Barreira Fiscal e a Nota Fiscal' (Bible v1.0) — instalado em Cap 4, aprofundado em Cap 11"
  - "Fio 'MVP → estrutura' — Bling é peça central do MVP"
  - "5 configs do dia 1 do Bling (11.1): dados empresa, natureza operação, certificado digital, código manual, integração ML"
  - "13 passos do cadastro no Bling (11.2)"
  - "Kit com estoque virtual (= menor dos componentes) (11.2)"
  - "Caminho reverso ML→Bling pra resgate de produtos antigos (11.2)"
  - "Vinculação de categoria Bling↔ML, crítica pra evitar categoria errada (11.2)"
  - "6 passos da emissão de NF integrada ao pedido do ML (11.3)"
  - "3 status visuais (amarelo/azul/verde) e 6 ícones do pedido no Bling (11.3)"
cases_citados:
  - "Patacori (case oficial, Cap 11): configurações (estoque negativo, etiqueta modelo 3, certificado R$ 139), cadastros (kit incensário 3 tamanhos), Patacori 2 pessoas tratando milhares de NF/mês [11.1, 11.2, 11.3]"
conceitos_definidos:
  - "Bling: ERP canônico da obra, cupom 4 meses grátis, R$ 50/mês pós-cupom"
  - "5 configs dia 1: dados empresa, natureza operação, certificado digital, código manual, integração ML"
  - "Certificado digital: arquivo .pfx com senha, R$ 139, validade 1 ano, renovar com 30 dias antecedência"
  - "Natureza de operação padrão: 'Venda de mercadoria, saída, não presencial, internet'"
  - "Código de produtos MANUAL com prefixos por categoria"
  - "13 passos do cadastro: SKU, tipo, formato, unidade, preço, peso, dimensões, EAN, nome, categoria, estoque min/max, fornecedor, tributação, imagens, vídeo, descrição"
  - "Kit (composição): SKU e EAN próprios, estoque virtual (= menor dos componentes)"
  - "2 caminhos de cadastro: Bling→ML (recomendado) e ML→Bling (resgate)"
  - "Vinculação de categoria Bling↔ML: configurar uma vez só"
  - "Exportação pro ML: clica no carrinho → modalidade Premium/Clássica → 'Exportar produtos'"
  - "Ajuste de preço em massa: filtrar → selecionar → fixar/%/desconto"
  - "Emissão de NF: pelo Bling (não pelo ML), pré-requisito certificado digital válido"
  - "6 passos: pedido entra → abrir pedido → conferir NCM → salvar e enviar SEFAZ → sincronizar com ML → imprimir etiqueta"
  - "3 status visuais: amarelo (em aberto), azul (NF ok, não despachado), verde (coletado/entregue)"
  - "6 ícones: relógio (ocorrências), canal (origem), cifrão (NF), caixa (estoque), rastreador (transportadora), balão (comentário)"
  - "Bling destaca primeira compra do cliente"
  - "3 tipos de logística: Mercado Envios (automática), Correios (gera remessa), B2W (gera remessa)"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.600-3.800 palavras por cena (Cap. 11 está nesse range, 9.896 com 3 cenas)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional; 'No próximo capítulo' (cena→cap) com gancho"
  - "Diretriz editorial: caos antes da solução (NF rejeitada → ajusta NCM → reenvia)"
  - "Diretriz editorial: cases com atrito (Patacori certificado vencido, NCM errado)"
  - "Diretriz editorial: variar fechos ('Toca cadastrar produto', 'Toca emitir NF', 'Toca encerrar')"
  - "Persona Claudia da Patacori usada como ancora narrativa"
  - "Citação literal do Bruno em alta densidade (15-20 citações por cena)"
---
"""

INTRO = """# Capítulo 11 — O ERP na Prática (Bling)

[Para quem é este capítulo: empreendedores que instalaram o Bling (Cap 4) e querem dominar a operação fiscal e logística. Aqui você vai ver as 5 configs do dia 1, os 13 passos do cadastro, e o fluxo completo de NF integrada ao pedido do ML.]

[Como ler: as cenas deste capítulo tratam do Bling em profundidade. 11.1 instala o motor (5 configs do dia 1 + 3 opcionais). 11.2 ensina o cadastro de produto (13 passos + kit + caminho reverso). 11.3 fecha com a emissão de NF integrada ao pedido do ML (6 passos + 3 status + 6 ícones). A Patacori percorre o capítulo como exemplo concreto (cupom 4 meses, certificado R$ 139, 2 pessoas tratando NF/mês).]

[Status: CONCLUÍDO. As 3 cenas fecham o motor invisível do negócio.]

---

## SUMÁRIO DO CAPÍTULO 11 (COMPLETO)

- **Cena 11.01** — Bling: o ERP que organiza a operação, e o que configurar no dia 1 ✅
- **Cena 11.02** — Cadastrando produtos no Bling, e o caminho reverso: importar do Mercado Livre ✅
- **Cena 11.03** — Emitindo nota fiscal pelo Bling, e o fluxo completo de venda integrado ao Mercado Livre ✅

---
"""

METADADOS_FINAIS = """---

## METADADOS DO CAPÍTULO (COMPLETO)

- **Cenas concluídas:** 3 de 3 ✅
- **Status:** CONCLUÍDO
- **Bible checksum atualizado:** ver `bible_da_obra.md` v1.8
- **Próximo capítulo a escrever:** 12 (Cases, Bônus e Epílogo)

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
        ch = CHECKSUMS[f"11.{n}"]
        val = CHECKSUMS_VALIDACAO[f"11.{n}"]

        partes.append("\n\n---\n\n")
        partes.append(f"*[Checksum: {ch} | Validação MARCH: {val} | Validação Continuidade: {val}]*\n\n---\n\n")
        partes.append(cena_texto)
        partes.append("\n\n")

    partes.append(METADADOS_FINAIS)

    livro_texto = "".join(partes)
    saida = BASE / "livro_capitulo_11.md"

    with open(saida, "w", encoding="utf-8") as f:
        f.write(livro_texto)

    with open(saida, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()[:8]

    words = len(re.findall(r"\b\w+\b", livro_texto))

    print(f"✅ Livro do Cap. 11 (COMPLETO — 3/3 cenas) gerado em: {saida}")
    print(f"   SHA256 (8 chars): {h}")
    print(f"   Total de palavras: {words}")
    print(f"   Cenas: 3 de 3 (capítulo fechado)")


if __name__ == "__main__":
    build()
