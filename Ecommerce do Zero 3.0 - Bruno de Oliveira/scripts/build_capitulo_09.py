#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_capitulo_09.py — Construtor do Capítulo 9 (Parabéns! Você validou o negócio) consolidado
2 cenas: 9.1, 9.2 (CAPÍTULO COMPLETO)
"""

import hashlib
import re
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira/capitulos/capitulo_09")
SAIDAS = {
    1: BASE / "cena_01" / "_saida_final.md",
    2: BASE / "cena_02" / "_saida_final.md",
}
CHECKSUMS = {
    "9.1": "18869e08",
    "9.2": "c9bf80cb",
}
CHECKSUMS_VALIDACAO = {
    "9.1": "APROVADA",
    "9.2": "APROVADA",
}

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "Capítulo 9 — Parabéns! Você validou o negócio"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-08-04T01:00:00Z"
version: "1.0"
capitulo: 9
total_capitulos_estimados: 12
cena_count: 2
status: "CONCLUÍDO (2/2 cenas)"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
bible_version: "v1.7 (Cap 1-9 completos; Cap 9 fechou com 2/2 cenas)"
validador_march: "TODAS_APROVADAS (2/2 cenas)"
validador_continuidade: "TODAS_APROVADAS (2/2 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_cenas:
  - "9.1: 18869e08"
  - "9.2: c9bf80cb"
fios_narrativos_avancados:
  - "Fio central 'A Validação' tem payoff em 9.1 (R$ 10K primária / R$ 30K consolidada)"
  - "Régua de 3 fases: ramp-up (10K→30K), salto (30K→100K), cruising (100K+)"
  - "4 próximos passos do Bruno: (1) estrutura profissional; (2) marketplaces pós-validação; (3) conhecimento novo; (4) treinamentos complementares"
  - "5 marketplaces pós-validação: B2W, Dafiti, NetShoes, Via Varejo, Leroy Merlin (massa + nicho)"
  - "2 treinamentos complementares: Explosão de Tráfego e Vendas + Viver de Ecommerce (100+ horas, R$ 4-5 mil, R$ 100K → R$ 1M)"
  - "Analogie do surf/jet ski: romper a arrebentação = R$ 30K (99% chance de sucesso)"
  - "Conexão com Cap 10 (Mercado Livre): 'pistas de alta velocidade' pós-validação"
cases_citados:
  - "Patacori (case oficial do corpus, Cap 9): MVP bem feito, ERP 100%, loja virtual a construir"
  - "Bruno: recomenda manual de loja virtual (bônus do curso), fotógrafo profissional, redator"
conceitos_definidos:
  - "Validação primária (R$ 10K) vs Validação consolidada (R$ 30K) — 99% de chance de sucesso"
  - "Analogia do surf: arrebentação = R$ 30K, mar adentro = depois de R$ 30K"
  - "Comemoração tem 3 funções: (1) ancora feito na memória, (2) inspira outros, (3) constrói rede"
  - "Manual de uso do curso: fonte de consulta, não prova de leitura"
  - "Acesso ao conteúdo por 1 ano + suporte renovável"
  - "Estrutura profissional tem 4 subfrentes: (1) loja virtual própria; (2) ERP 100%; (3) outros marketplaces; (4) fotógrafo/redator"
  - "Bônus: manual de construção de loja virtual própria, sem agência, plataforma renomada"
  - "Marketplaces pós-validação: B2W, Dafiti, NetShoes, Via Varejo, Leroy Merlin (massa + nicho)"
  - "Pistas de alta velocidade: marketplaces pós-validação. 'Não é ideal pra quem está validando, é ideal pra quem está no pós-validação'"
  - "Curva de 3 fases: ramp-up (10K→30K gradual), salto (30K→100K exponencial), cruising (100K+ consolidação)"
  - "Gastar tempo na estruturação profissional não tem como evitar. Quem pula trava em R$ 20-25K"
  - "Conhecimento novo, não quantidade do mesmo. 'Coisas que fazem sentido agora e que antes não faziam'"
  - "Explosão de Tráfego e Vendas: forma gestor de tráfego, anúncios profissionais, BM, catálogo"
  - "Viver de Ecommerce: 100+ horas, 4 pilares (estrutura, marketing, gestão, otimização), R$ 100K → R$ 1M, R$ 4-5 mil"
  - "Janela de oportunidade: Viver abre poucas vezes/ano, condição de aluno é exclusiva"
  - "Time de orientadores para quem não está pronto pro upgrade"
  - "5 comportamentos que separam quem escala: estrutura antes de travar, marketplaces pós-validação, aprender tráfego, tratar como negócio, aceitar que a régua muda"
  - "5 erros do pós-validação: escalar fazendo mais do mesmo, pular estruturação, esperar travar pra buscar conhecimento, marketplaces como atalho, não investir em time"
  - "Mensagem central: validação primária = diploma do método / validação consolidada = diploma do negócio"
  - "Antes da validação, ninguém te dá nada. Depois, o mercado te dá tudo"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor como base, 2ª pessoa pontual"
  - "Extensão: ~2.400-3.200 palavras por cena (Cap. 9 está nesse range, 5.636 com 2 cenas)"
  - "Formato do fim: ## Resumo + ## Seu checklist + preview próxima cena/capítulo"
  - "Conectores: 'Na próxima cena deste capítulo' (mesmo cap) com gancho emocional; 'No próximo capítulo' (cena→cap) com gancho"
  - "Diretriz editorial: caos antes da solução (celebração com preparação pra próxima fase)"
  - "Diretriz editorial: cases com atrito (reconhece que 'ainda tem coisas para implementar')"
  - "Diretriz editorial: variar fechos ('Te vejo no próximo passo', 'Toca dominar o Mercado Livre')"
  - "Persona Claudia percorre como ancora narrativa (implícita, foco é celebratório)"
  - "Citação literal do Bruno em alta densidade (18-19 citações por cena)"
---
"""

INTRO = """# Capítulo 9 — Parabéns! Você validou o negócio

[Para quem é este capítulo: empreendedores que finalizaram o Cap. 8 com a máquina de impulsão rodando. Agora é hora de parar, respirar, e reconhecer o que você acabou de fazer. Você validou o negócio.]

[Como ler: as cenas deste capítulo tratam da validação e dos próximos passos. 9.1 celebra a barreira rompida, e mostra a régua de 2 estágios (R$ 10K primária, R$ 30K consolidada). 9.2 abre o mapa da próxima fase (estrutura profissional, marketplaces pós-validação, treinamentos complementares, R$ 100K). A persona Claudia percorre o capítulo como exemplo concreto de quem rompeu a arrebentação.]

[Status: CONCLUÍDO. As 2 cenas fecham o ciclo da validação e abrem o ciclo da escala.]

---

## SUMÁRIO DO CAPÍTULO 9 (COMPLETO)

- **Cena 9.01** — Você validou: a barreira foi rompida ✅
- **Cena 9.02** — Próximos passos: do R$ 10K ao R$ 100K, a próxima escalada ✅

---
"""

METADADOS_FINAIS = """---

## METADADOS DO CAPÍTULO (COMPLETO)

- **Cenas concluídas:** 2 de 2 ✅
- **Status:** CONCLUÍDO
- **Bible checksum atualizado:** ver `bible_da_obra.md` v1.7
- **Próximo capítulo a escrever:** 10 (Mercado Livre: termômetro, triângulo, kits)

"""


def ler_cena(numero: int) -> str:
    caminho = SAIDAS[numero]
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def build():
    partes = [FRONT_MATTER, INTRO]

    for n in [1, 2]:
        cena_texto = ler_cena(n)

        ch = CHECKSUMS[f"9.{n}"]
        val = CHECKSUMS_VALIDACAO[f"9.{n}"]

        partes.append("\n\n---\n\n")
        partes.append(f"*[Checksum: {ch} | Validação MARCH: {val} | Validação Continuidade: {val}]*\n\n---\n\n")
        partes.append(cena_texto)
        partes.append("\n\n")

    partes.append(METADADOS_FINAIS)

    livro_texto = "".join(partes)
    saida = BASE / "livro_capitulo_09.md"

    with open(saida, "w", encoding="utf-8") as f:
        f.write(livro_texto)

    with open(saida, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()[:8]

    words = len(re.findall(r"\b\w+\b", livro_texto))

    print(f"✅ Livro do Cap. 9 (COMPLETO — 2/2 cenas) gerado em: {saida}")
    print(f"   SHA256 (8 chars): {h}")
    print(f"   Total de palavras: {words}")
    print(f"   Cenas: 2 de 2 (capítulo fechado)")


if __name__ == "__main__":
    build()
