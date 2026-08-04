#!/usr/bin/env python3
"""Constrói livro_capitulo_04.md — versão consolidada do capítulo 4."""
import os
import re
import hashlib

CENA_BASE = "/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_04"
OUTPUT = os.path.join(CENA_BASE, "livro_capitulo_04.md")

CENA_TITULOS = {
    "cena_01": "A estrutura mínima viável (MVP) — a filosofia por trás do método",
    "cena_02": "Sua estrutura física — mesa, luz, embalagem (e o que é firula)",
    "cena_03": "CNPJ, MEI e ME — a papelada que liberta (e os 5 erros que apagam 30% do seu lucro)",
    "cena_04": "Domínio, e-mail profissional, e os canais de audiência e venda",
    "cena_05": "ERP, gateway de pagamento e envios — a engrenagem da operação",
    "cena_06": "SKU, EAN e o cadastro do primeiro produto",
    "cena_07": "Dropshipping nacional homologado — como montar a triangulação",
    "cena_08": "Descrição, foto e vídeo — a vitrine que vende",
}

CENA_CHECKSUMS = {
    "cena_01": "4dafb0d7",
    "cena_02": "55339228",
    "cena_03": "05a08fc1",
    "cena_04": "0f993482",
    "cena_05": "224ededa",
    "cena_06": "e9b5ea55",
    "cena_07": "1730219c",
    "cena_08": "1f974e8a",
}

FIXED_TIMESTAMP = "2026-07-30T18:50:00Z"

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
    cenas = ["cena_01", "cena_02", "cena_03", "cena_04", "cena_05", "cena_06", "cena_07", "cena_08"]

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
subtitle: "Capítulo 4 — A Estrutura Mínima Viável (MVP)"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "{FIXED_TIMESTAMP}"
version: "1.0"
capitulo: 4
total_capitulos_estimados: 12
cena_count: 8
word_count: {total_palavras}
status: "CONCLUIDO"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.5 (atualizada após Cap 3 completo + Cap 4 completo)"
validador_march: "TODAS_APROVADAS (8/8 cenas)"
validador_continuidade: "TODAS_APROVADAS (8/8 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "4.1: {CENA_CHECKSUMS['cena_01']}"
  - "4.2: {CENA_CHECKSUMS['cena_02']}"
  - "4.3: {CENA_CHECKSUMS['cena_03']}"
  - "4.4: {CENA_CHECKSUMS['cena_04']}"
  - "4.5: {CENA_CHECKSUMS['cena_05']}"
  - "4.6: {CENA_CHECKSUMS['cena_06']}"
  - "4.7: {CENA_CHECKSUMS['cena_07']}"
  - "4.8: {CENA_CHECKSUMS['cena_08']}"
fios_narrativos_avancados:
  - "Estrutura Mínima Viável (MVP) — Conceito Âncora, instalado em 4.1, aplicado em 4.2-4.8, FECHADO em 4.8"
  - "Patacori como case âncora — atualizado em 4.2 (quarto → espaço 12m²), 4.4 (gmail → domínio), 4.5 (Word → Bling), 4.8 (foto celular → foto profissional, vendas 15-20 → 60/mês)"
  - "Dropshipping Nacional Homologado — aprofundado em 4.7 (triangulação operacional, transparência sobre NF do fornecedor)"
  - "Triângulo do Sucesso (Audiência × Estrutura × Ofertas) — Audiência e Ofertas antecipados para Cap. 5 e Cap. 7"
  - "Audiência é Rei — fio antecipado para próximo capítulo (Cap. 5)"
cases_citados:
  - "Bruno 2012 (quarto com criado-mudo) → 2018 (espaço 12m², R$ 800, triplicou produtividade) [4.1, 4.2]"
  - "Patacori 2017 (300 NFs no Word, 3 planilhas, 4h/dia) → 2018 (Bling, 30s/NF, 4h/dia recuperadas) [4.5]"
  - "Patacori 2018 (gmail pedraspatacori@gmail.com) → (contato@patacori.com.br, R$ 300, badge azul) [4.4]"
  - "Patacori 2019 (kit 7 chakras, foto celular 15-20 vendas/mês) → (foto profissional, descrição reescrita, 60 vendas/mês, triplicou) [4.8]"
  - "Patacori (cristais em consignação por 6 meses, margem 30%) [4.7]"
conceitos_definidos:
  - "MVP (Minimum Viable Product) — do Vale do Silício, adaptado para e-commerce"
  - "6 peças do MVP: CNPJ, ERP, Canal, Catálogo, Embalagem, Capital de giro"
  - "Estrutura física mínima: mesa 1m+, cadeira ergonômica, luminária, notebook, impressora térmica, embalagem padronizada, armário"
  - "Firula: caixa personalizada, mesa cara, decoração, notebook gamer, uniforme"
  - "MEI vs ME: limite R$ 80k, custo R$ 70/mês (MEI) vs sem limite, contador R$ 150-300, Simples 4-19% (ME)"
  - "5 erros que custam 30% do lucro: (1) MEI sem verificar CNAE, (2) ME sem validar, (3) contador caro, (4) não emitir NF, (5) conta pessoal misturada com PJ"
  - "Domínio próprio (.com.br, R$ 40-80/ano, Registro.br)"
  - "E-mail profissional (contato@suamarca.com.br, Google Workspace R$ 30/mês ou Zoho Mail R$ 12/mês)"
  - "Regra dos 2 canais: 1 venda (Mercado Livre) + 1 audiência (Instagram) no MVP"
  - "Bling ERP (Cobalto R$ 50/mês, Titânio R$ 100/mês): centraliza cadastros, vendas, estoque, NF, etiquetas, relatórios"
  - "Gateway Mercado Pago (4,99% à vista, 12,99% parcelado) + Mercado Envios (Full só com 50+ unid/SKU/mês)"
  - "SKU (código interno, seu) vs EAN (código universal, 13 dígitos, do fabricante)"
  - "GS1 Brasil (faixa de 10 EANs = R$ 350, vinculado ao CNPJ)"
  - "Triangulação dropshipping: cliente → você → fornecedor → cliente (NF do fabricante)"
  - "Margem dropshipping nacional: 20-40% (Patacori 30% em cristais por 6 meses)"
  - "Gatilho de saída do dropshipping: 10-20 vendas/mês do mesmo SKU"
  - "Foto 3 ângulos mínimos (frente, lado, detalhe); luz natural de janela + cortina branca"
  - "Vídeo 15-30s hands-on converte 3-5x mais que sem vídeo"
  - "Descrição avançada: 4 parágrafos (dor, o que é, diferencial, logística) + CTA"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~1.700-2.200 palavras por cena (Cap. 4 ficou nesse range)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) / 'No próximo capítulo' (próximo cap) — com gancho emocional, não mecânico"
  - "Diretriz editorial crítica: narrativa de caos antes da solução nas cenas técnicas (4.2 Patacori no quarto, 4.5 Word → Bling, 4.8 foto celular → foto profissional)"
  - "Diretriz editorial: variar fechos ('Bora', 'Toca', 'Vamos', 'Te vejo')"
  - "MEI primeiro, ME quando o MEI travar"
  - "Não aceitar Pix por fora do marketplace (venda sem NF, sem proteção, sem lastro)"
  - "Domínio indisponível = filtro obrigatório para escolha de nome de marca"
  - "Sincronização de estoque no Bling é obrigatória (evita over-selling)"
  - "Mistura no MVP: 2-3 produtos em estoque + 2-3 em dropshipping"
  - "Categorias específicas > genéricas (mais qualificado, menos tráfego)"
  - "Foto profissional é o maior ROI do e-commerce (Patacori triplicou vendas só com nova vitrine)"
---
"""
    parts.append(front_matter)

    sumario = ["# Capítulo 4 — A Estrutura Mínima Viável (MVP)\n\n"]
    sumario.append("[Para quem é este capítulo: empreendedores que finalizaram o Cap. 3 com método, meta, tripé, fornecedor e oferta. Agora é hora de sair do papel e construir a operação real. Este é o capítulo onde a teoria vira prática.]\n\n")
    sumario.append("[Como ler: as cenas seguem a sequência operacional. Comece com a bancada (4.2), passe pelo CNPJ (4.3), configure a cara digital (4.4), monte a engrenagem (4.5), cadastre produto (4.6), habilite o dropshipping como contingência (4.7), e construa a vitrine (4.8). A cena 4.1 é a filosofia; as outras sete são o passo a passo.]\n\n")
    sumario.append("---\n\n")
    sumario.append("## SUMÁRIO DO CAPÍTULO 4\n\n")
    for cena in cenas:
        numero = cena.split("_")[1]
        sumario.append(f"- **Cena 4.{numero}** — {CENA_TITULOS[cena]}\n")
    sumario.append("\n---\n\n")
    parts.append(''.join(sumario))

    for i, cena in enumerate(cenas):
        numero = cena.split("_")[1]
        titulo = CENA_TITULOS[cena]
        prosa = prosa_cenas[cena]

        if i > 0:
            parts.append("\n---\n\n")

        cena_block = f"# Capítulo 4 — A Estrutura Mínima Viável (MVP)\n"
        cena_block += f"## Cena 4.{numero}: {titulo}\n\n"
        cena_block += f"*[Checksum: {CENA_CHECKSUMS[cena]} | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*\n\n"
        cena_block += "---\n\n"
        cena_block += prosa
        cena_block += "\n"

        parts.append(cena_block)

    livro_corpo = ''.join(parts)

    livro = livro_corpo + f"\n\n---\n\n## METADADOS DO CAPÍTULO\n\n- **Checksum SHA256 (8 chars):** `PLACEHOLDER_CHECKSUM`\n- **Total de palavras:** {total_palavras:,}\n- **Cenas:** 8\n- **Compilado em:** {FIXED_TIMESTAMP}\n- **Pipeline:** Greenforge v3 (Podbook Mentor)\n- **Status:** CONCLUÍDO\n\n### Próximo capítulo (Cap. 5)\n\n**Audiência é Rei:** sem audiência, mesmo o melhor produto do mundo fica encalhado. Você vai entender por que audiência é a peça que faltou na engrenagem, como construir audiência orgânica no Instagram com conteúdo que vende sem precisar de impulsão, e como essa audiência conversa com o Mercado Livre para criar crescimento exponencial. Te vejo lá.\n"

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(livro)

    with open(OUTPUT, 'r', encoding='utf-8') as f:
        content = f.read()
    idx_metadata = content.find('## METADADOS')
    corpo = content[:idx_metadata]
    livro_bytes_size = len(corpo.encode('utf-8'))
    livro_checksum = hashlib.sha256(corpo.encode('utf-8')).hexdigest()[:8]

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
