#!/usr/bin/env python3
"""Constrói livro_capitulo_03.md — versão consolidada do capítulo 3."""
import os
import re
import hashlib
from datetime import datetime

CENA_BASE = "/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_03"
OUTPUT = os.path.join(CENA_BASE, "livro_capitulo_03.md")

CENA_TITULOS = {
    "cena_01": "O método em 6 etapas — o mapa da mina",
    "cena_02": "A meta de validação — R$ 10 mil, 100 pedidos, 90 dias",
    "cena_03": "Nicho, persona, produto — o tripé da escolha",
    "cena_04": "Fornecedores — como encontrar e homologar",
    "cena_05": "Dropshipping — a verdade que ninguém te conta",
    "cena_06": "Ofertas, demanda e produto estrela",
}

CENA_CHECKSUMS = {
    "cena_01": "a33eeef9",
    "cena_02": "0607dae5",
    "cena_03": "87dbb362",
    "cena_04": "23869428",
    "cena_05": "7fbe9fe7",
    "cena_06": "1cc50b04",
}

FIXED_TIMESTAMP = "2026-07-30T17:50:00Z"

def extract_prosa(cena):
    path = os.path.join(CENA_BASE, cena, "_saida_final.md")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    if lines[0].startswith("# Capítulo"):
        lines = lines[1:]
    if lines and lines[0].strip() == "":
        lines = lines[1:]
    if lines and lines[0].startswith("## "):
        lines = lines[1:]
    if lines and lines[0].strip() == "":
        lines = lines[1:]
    return '\n'.join(lines).rstrip()

def count_words(text):
    return len(text.split())

def main():
    cenas = ["cena_01", "cena_02", "cena_03", "cena_04", "cena_05", "cena_06"]

    total_palavras = 0
    prosa_cenas = {}
    for cena in cenas:
        prosa = extract_prosa(cena)
        palavras = count_words(prosa)
        prosa_cenas[cena] = prosa
        total_palavras += palavras

    parts = []

    front_matter = f"""---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 3 — O Método e o Planejamento"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "{FIXED_TIMESTAMP}"
version: "1.0"
capitulo: 3
total_capitulos_estimados: 12
cena_count: 6
word_count: {total_palavras}
status: "CONCLUIDO"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Zappos/Bruno)."
bible_version: "v1.5 (atualizada após Cap 3 completo — Cenas 1.1 a 1.3 + 2.1 a 2.4 + 3.1 a 3.6 CONCLUÍDAS)"
validador_march: "TODAS_APROVADAS (6/6 cenas)"
validador_continuidade: "TODAS_APROVADAS (6/6 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "3.1: {CENA_CHECKSUMS['cena_01']}"
  - "3.2: {CENA_CHECKSUMS['cena_02']}"
  - "3.3: {CENA_CHECKSUMS['cena_03']}"
  - "3.4: {CENA_CHECKSUMS['cena_04']}"
  - "3.5: {CENA_CHECKSUMS['cena_05']}"
  - "3.6: {CENA_CHECKSUMS['cena_06']}"
fios_narrativos_avancados:
  - "Validação (R$ 10K / 100 pedidos / 90 dias) — Tema Central, instalado em 3.1, aprofundado em 3.2, reforçado em 3.6"
  - "Estrutura Mínima Viável (MVP) — Conceito Âncora, instalado em 3.1, aprofundado em 3.4, contextualizado em 3.5/3.6"
  - "Audiência > Conteúdo — Mudança de Paradigma, antecipada em 3.1, payoff em Cap. 5"
  - "Dropshipping Nacional Homologado — Solução de Nicho, instalado em 3.4, desmascarado em 3.5"
  - "Triângulo do Sucesso (Audiência × Estrutura × Ofertas) — Conceito-chave, instalado em 3.6"
  - "Produto Estrela (alto lucro + baixa competição) — Conceito Âncora, instalado em 3.6"
cases_citados:
  - "Patrícia (bolsa de praia → bolsa de bíblia para evangélicas → adquire cliente → vende bolsa de praia na jornada)"
  - "Vitor (cama/mesa/banho → testou lençol/toalha/mesa sem resultado → tapete de banheiro virou produto estrela, alavancou o portfólio)"
  - "John (moda íntima sem resultado → descascador de pinhão 1.400 unid/mês a R$ 65 → estrela → parceria com fabricante 30k SKUs para jornada de compra)"
  - "Zappos (MVP histórico: site simples, foto de shopping, enviava se vendesse)"
  - "Bruno/Patacori (cartucho em consignação, cristais em consignação)"
personagens_reais:
  - "Bruno (mentor, narrador em 1ª pessoa)"
  - "Ana Clara (diretora de marketing de embalagem)"
  - "Babi (diretora de produtos e customer experience)"
conceitos_definidos:
  - "Método de validação (6 etapas: Planejamento → Estrutura → Audiência → Vendas → Atendimento → Impulsão)"
  - "Meta de validação (R$ 10 mil + 100 pedidos em ~90 dias, parâmetro flexível)"
  - "Curva de validação (lenta no começo, acelera depois; quem desiste no começo lento nunca vê a subida)"
  - "Barreira da incerteza (99% de chance de dar certo quando rompida; correr risco → gerenciar risco)"
  - "MVP (Estrutura Mínima Viável, adaptado do Vale do Silício)"
  - "Tripé do planejamento (Nicho micro-verticalizado + Persona com Mapa de Empatia + Produto)"
  - "Mapa de Empatia (ferramenta de persona com gente real)"
  - "Fornecedor homologado (checklist 6 itens: CNPJ, NF, prazo, qualidade, comunicação, parceria)"
  - "Contingência de fornecedor (1 principal + 2 backups)"
  - "Dropshipping Nacional Homologado (fornecedor BR + NF do fabricante + você no suporte + consignação)"
  - "Triângulo do Sucesso (Audiência × Estrutura × Ofertas)"
  - "Produto Estrela (alto lucro + baixa competição, 'agulha no palheiro')"
  - "Anatomia da oferta (10 elementos: produto, preço, parcelamento, frete, garantia, urgência, prova social, cross/upsell, kits, NF)"
  - "Regra orgânica primeiro (só impulsiona o que já vende)"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: 1.000-2.000 palavras por cena (Cap. 3 ficou entre 1.282 e 1.715 — dentro do range)"
  - "Formato do fim: ## Resumo + ## Seu checklist + **Próxima cena/capítulo:**"
  - "Ordem das 6 etapas é fixa — inverter aumenta risco"
  - "Marketplaces: Mercado Livre, Amazon, Olist, Enjoei, Elo7, Elu7 (sem Shopee/Magalu na lista canônica)"
  - "Bling é o ERP recomendado (não outro)"
  - "Pular etapa = queima dinheiro (aula prática com 3 exemplos)"
  - "Não usar dropshipping internacional (importação ilegal, viola CDC)"
  - "Testa no orgânico primeiro, só impulsiona o que converte"
  - "1 fornecedor principal + 2 backups (contingência)"
  - "5 motivos contra dropshipping internacional (importação ilegal, sem aviso ao cliente, viola CDC, sem CNPJ/NF/SAC, financia cadeia ilegal)"
---
"""
    parts.append(front_matter)

    sumario = ["# Capítulo 3 — O Método e o Planejamento\n\n"]
    sumario.append("[Para quem é este capítulo: empreendedores que já entenderam o mindset (Caps 1-2) e agora precisam colocar a mão na massa. O capítulo mais denso do treinamento — o Bruno avisa logo na abertura.]\n\n")
    sumario.append("[Como ler: cada cena é autocontida, mas a ordem importa. A cena 1 dá o mapa geral (as 6 etapas), as cenas 2-6 destrincham cada peça do planejamento. Pode pular cena 2 se já está firme na meta de validação.]\n\n")
    sumario.append("---\n\n")
    sumario.append("## SUMÁRIO DO CAPÍTULO 3\n\n")
    for cena in cenas:
        numero = cena.split("_")[1]
        sumario.append(f"- **Cena 3.{numero}** — {CENA_TITULOS[cena]}\n")
    sumario.append("\n---\n\n")
    parts.append(''.join(sumario))

    for i, cena in enumerate(cenas):
        numero = cena.split("_")[1]
        titulo = CENA_TITULOS[cena]
        prosa = prosa_cenas[cena]

        if i > 0:
            parts.append("\n---\n\n")

        cena_block = f"# Capítulo 3 — O Método e o Planejamento\n"
        cena_block += f"## Cena 3.{numero}: {titulo}\n\n"
        cena_block += f"*[Checksum: {CENA_CHECKSUMS[cena]} | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*\n\n"
        cena_block += "---\n\n"
        cena_block += prosa
        cena_block += "\n"

        parts.append(cena_block)

    livro_corpo = ''.join(parts)

    # Salva versão com placeholder primeiro
    livro = livro_corpo + f"\n\n---\n\n## METADADOS DO CAPÍTULO\n\n- **Checksum SHA256 (8 chars):** `PLACEHOLDER_CHECKSUM`\n- **Total de palavras:** {total_palavras:,}\n- **Cenas:** 6\n- **Compilado em:** {FIXED_TIMESTAMP}\n- **Pipeline:** Greenforge v3 (Podbook Mentor)\n- **Status:** CONCLUÍDO\n\n### Próximo capítulo (Cap. 4)\n\n**Estrutura Mínima Viável (MVP):** CNPJ (MEI vs ME), Bling, Mercado Livre/Shopee/Magalu, pagamentos, envios, embalagem, SKU/EAN, cadastro de produtos. É a hora de botar a mão na massa na operação. Bora construir.\n"

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(livro)

    # Calcula checksum do corpo
    with open(OUTPUT, 'r', encoding='utf-8') as f:
        content = f.read()
    idx_metadata = content.find('## METADADOS')
    corpo = content[:idx_metadata]
    livro_bytes_size = len(corpo.encode('utf-8'))
    livro_checksum = hashlib.sha256(corpo.encode('utf-8')).hexdigest()[:8]

    # Substitui placeholder
    content_final = content.replace('PLACEHOLDER_CHECKSUM', livro_checksum)
    content_final = content_final.replace(
        f"- **Tamanho:** {livro_bytes_size:,} bytes\n",
        f"- **Tamanho:** {livro_bytes_size:,} bytes (corpo) / {len(content_final.encode('utf-8')):,} bytes (com rodapé)\n"
    )

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(content_final)

    print(f"Livro salvo em: {OUTPUT}")
    print(f"Checksum do corpo: {livro_checksum}")
    print(f"Tamanho do corpo: {livro_bytes_size:,} bytes")
    print(f"Tamanho final: {len(content_final.encode('utf-8')):,} bytes")
    print(f"Palavras: {total_palavras:,}")
    print(f"Cenas consolidadas: {len(cenas)}")

    with open(OUTPUT, 'r', encoding='utf-8') as f:
        content_check = f.read()
    idx_check = content_check.find('## METADADOS')
    corpo_check = content_check[:idx_check]
    rt_checksum = hashlib.sha256(corpo_check.encode('utf-8')).hexdigest()[:8]
    if rt_checksum == livro_checksum:
        print(f"Round-trip OK ✓ ({livro_checksum})")
    else:
        print(f"Round-trip FALHOU ✗")

if __name__ == "__main__":
    main()
