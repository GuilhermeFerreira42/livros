#!/usr/bin/env python3
"""
Gera _perguntas_continuidade.json retroativamente a partir de _resultado_continuidade.json
para as cenas que estão sem o arquivo de perguntas.
"""
import json
import os
import re

CENA_BASE = "/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_03"

# Templates de perguntas por categoria (genéricos, suficientes para revalidação)
PERGUNTAS_TEMPLATES = {
    "VOZ_NARRATIVA": "A cena mantém o padrão de voz narrativa definido na Bible (1ª do mentor com alternância para 2ª pessoa, presente, tom pragmático/encorajador, distância de mentor/consultor)?",
    "CONCEITO_DEFINICAO": "Os conceitos centrais da cena (validação, MVP, produto estrela, persona, etc.) estão definidos conforme a Bible da obra?",
    "CONCEITO_REGRA": "As regras de método/protocolo (ordem das 6 etapas, regras de porta, MVP, dropshipping homologado) estão corretamente aplicadas?",
    "CONCEITO_TECNICO": "Os termos técnicos da cena (SKU, EAN, ERP, Bling, MVP, marketplace) estão usados conforme glossário da Bible?",
    "PROTOCOLO": "O procedimento prático da cena (caça de produto, busca de fornecedor, homologação) segue o protocolo definido na Bible?",
    "MECANISMO": "O mecanismo operacional descrito (triangulação, conexão oferta-audiência, dropshipping nacional) está coerente com a Bible?",
    "REGRA_MERCADO": "As regras de mercado (CDC, imposto, MEI/ME, alfândega, marketplace) estão corretas conforme corpus?",
    "DADO_NUMERICO": "Os dados numéricos (R$ 10 mil, 100 pedidos, 90 dias, 1.400 unid/mês, R$ 65, 30 mil SKUs) estão corretos?",
    "NOME_PROPRIO": "Os nomes próprios (Bling, Mercado Livre, Amazon, Olist, Enjoei, Patacori, Ana Clara, Babi, Bruno) estão corretos?",
    "CASE_REFERENCIADO": "Os cases citados (Patrícia bolsa de bíblia, Vitor tapete de banheiro, John descascador de pinhão, Zappos, Carla) estão consistentes com a Bible e o corpus?",
    "CITACAO_CASE": "As citações a cases de alunos estão alinhadas com o que o corpus confirma?",
    "PERSONAGEM_ACAO": "As ações dos personagens (Ana Clara como diretora de marketing, Babi como diretora de CX) estão alinhadas com a Bible?",
    "FIO_NARRATIVO_SETUP": "Os fios narrativos (Validação R$ 10K, Audiência > Conteúdo, Estrutura Mínima Viável, Produto Estrela) estão sendo instalados corretamente?",
    "FIO_NARRATIVO_PAYOFF": "Os fios narrativos recebem payoff ou setup apropriado para esta cena?",
    "TIMELINE_CRONOLOGIA": "A timeline do método (Dias 1-7 Planejamento, 8-21 Estrutura, 22-35 Produtos, 36-60 Audiência, etc.) está sendo respeitada?",
    "MITO_DESCONTRUIDO": "Os mitos desconstruídos na cena (e-commerce fácil, dropshipping internacional, loja virtual obrigatória) estão sendo corretamente combatidos?",
    "TERMINOLOGIA_UNIFICADA": "A terminologia está unificada (MVP = estrutura mínima viável de validação, etc.)?",
}

def main():
    cenas = ["cena_02", "cena_03", "cena_04", "cena_05"]

    for cena in cenas:
        path_resultado = os.path.join(CENA_BASE, cena, "_resultado_continuidade.json")
        path_perguntas = os.path.join(CENA_BASE, cena, "_perguntas_continuidade.json")

        if os.path.exists(path_perguntas):
            print(f"{cena}: perguntas já existem, pulando")
            continue

        if not os.path.exists(path_resultado):
            print(f"{cena}: resultado não encontrado, pulando")
            continue

        with open(path_resultado, 'r', encoding='utf-8') as f:
            resultado = json.load(f)

        # Gera perguntas retroativas baseadas nas categorias
        perguntas = []
        for r in resultado.get("resultados", []):
            cid = r.get("id", "")
            categoria = r.get("categoria", "CONCEITO_DEFINICAO")
            template = PERGUNTAS_TEMPLATES.get(categoria, PERGUNTAS_TEMPLATES["CONCEITO_DEFINICAO"])

            perguntas.append({
                "id": cid,
                "categoria": categoria,
                "pergunta": template,
                "referencia_bible": f"Verificação de {categoria} conforme Bible da Obra (cap_03_cena_{cena[-1]})"
            })

        with open(path_perguntas, 'w', encoding='utf-8') as f:
            json.dump(perguntas, f, indent=2, ensure_ascii=False)

        print(f"{cena}: criado _perguntas_continuidade.json com {len(perguntas)} perguntas")

if __name__ == "__main__":
    main()
