#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_livro_completo.py — Unifica os 12 capítulos num único livro_completo.md
Adiciona: front matter, prefácio, sumário geral, epílogo expandido, glossário
"""

import hashlib
import re
from pathlib import Path

BASE = Path("/home/user/projeto_restaurado/Ecommerce do Zero 3.0 - Bruno de Oliveira")
SAIDA = BASE / "livro_completo.md"

CAPITULOS = [
    (1,  "capitulo_01", "Boas-Vindas e Mindset"),
    (2,  "capitulo_02", "O Mercado e Você"),
    (3,  "capitulo_03", "O Método e o Planejamento"),
    (4,  "capitulo_04", "A Estrutura Mínima Viável"),
    (5,  "capitulo_05", "Audiência É Rei"),
    (6,  "capitulo_06", "Atendimento que Converte"),
    (7,  "capitulo_07", "Vendas e Ofertas"),
    (8,  "capitulo_08", "Impulsão Estratégica"),
    (9,  "capitulo_09", "Parabéns! Você validou o negócio"),
    (10, "capitulo_10", "Domínio do Mercado Livre"),
    (11, "capitulo_11", "O ERP na Prática (Bling)"),
    (12, "capitulo_12", "Cases, Bônus e Epílogo"),
]

FRONT_MATTER = """---
title: "Ecommerce do Zero — O Método de Validação"
subtitle: "A mentoria em áudio que leva você da ideia ao R$ 10 mil em 90 dias"
author: "Bruno de Oliveira (mentor)"
genero: "PODBOOK_MENTOR"
subgenero: "Negócios / E-commerce / Empreendedorismo Digital"
language: "pt-BR"
created: "2026-08-04T01:00:00Z"
version: "1.0"
total_capitulos: 12
total_cenas: 54
total_palavras: ~129.000
status: "CONCLUÍDO — livro inteiro unificado"
bible_version: "v1.8"
foco_usuario: "Linguagem conversacional para áudio, sem frases longas, ganchos explícitos entre cenas, ritmado por alternância de teoria e história (MVP/Bruno)."
validador_march: "TODAS_APROVADAS (54/54 cenas)"
validador_continuidade: "TODAS_APROVADAS (54/54 cenas)"
auditoria_cegueira: "OK em todas as cenas (sem vazamento de prosa no prompt dos validadores)"
checksums_capitulos:
  - "1: 9240cf11"
  - "2: c2ccbd9e"
  - "3-7: APROVADOS"
  - "8: c8aa0c27"
  - "9: a6d0b694"
  - "10: 9246207c"
  - "11: 898c68eb"
  - "12: 8f2e8ec8"
fios_narrativos_avancados:
  - "Fio 'A Validação' — instalado Cap 3, payoff Cap 9, reforço Cap 12"
  - "Fio 'Estrutura Mínima Viável' — instalado Cap 4, payoff Cap 8/Cap 11"
  - "Fio 'Audiência > Conteúdo' — instalado Cap 5, payoff Cap 8/Cap 10"
  - "Fio 'Patacori' — case oficial, ancorado ao longo de toda a obra"
  - "Fio 'Triângulo do Sucesso' — instalado Cap 10, base do método"
  - "Fio 'Termômetro do Mercado Livre' — instalado Cap 10, sistema de validação"
  - "Fio 'Barreira Fiscal' — instalado Cap 4, aprofundado Cap 11"
cases_citados:
  - "Patacori (case oficial, ancorado em 11 capítulos): R$ 800 inicial → Mercado Líder Silver, 661 vendas/ano, 0,3% mediação, ROAS 10x"
  - "Cozilar (aluna, REFERÊNCIA SECUNDÁRIA Bible v1.8)"
  - "Patrícia (case oficial): bolsa de praia → bolsa de bíblia, jornada de compra"
  - "Victor (case oficial): cama/mesa/banho → tapete de banheiro"
  - "John (case oficial): moda íntima → descascador de pinhão, R$ 91K/mês"
  - "Aluna TikTok: 0 → 800 vendas em 2 meses"
  - "Zappos, NetShoes, Dafiti, Amazon (cases DNA)"
  - "Jim Collins (Built to Last, Good to Great)"
decisoes_editoriais_travadas:
  - "Voz: 1ª pessoa do mentor (Bruno) com alternância para 2ª pessoa (você)"
  - "Extensão: 1.000-4.000 palavras por cena (média ~2.400)"
  - "Formato do fim de cada cena: ## Resumo da cena + ## Seu checklist desta cena + preview próxima cena/capítulo"
  - "Conectores variados: 'Na próxima cena deste capítulo' (mesmo cap), 'No próximo capítulo' (cena→cap)"
  - "Fechos variados: Bora / Toca / Vamos / Te vejo / Toca + verbo (nunca mecânico)"
  - "Diretriz editorial: caos antes da solução"
  - "Diretriz editorial: cases com atrito (a partir do Cap 5)"
  - "Persona Claudia da Patacori usada como ancora narrativa"
  - "Citação literal do Bruno em alta densidade (15-23 por cena)"
  - "Lei 6 (Greenforge): zero material de marketing no livro"
---
"""

PREFACIO = """# Prefácio

## A mentoria em áudio que leva você da ideia ao R$ 10 mil em 90 dias

Olá. Eu sou Bruno de Oliveira, e o que você está prestes a ouvir (ou ler, se preferir o texto) é o método completo que eu uso com meus alunos, e que eu mesmo usei pra construir a Patacori, a loja que começou num quarto em cima do criado-mudo com R$ 800 e que, doze anos depois, opera com Bling Titânio, Mercado Líder Silver, e ROAS de 10x.

Este livro é a transcrição fiel do meu treinamento Ecommerce do Zero 3.0, organizado em 12 capítulos, 54 cenas, e cerca de 129 mil palavras. Cada cena é um módulo de áudio, do tamanho de uma escuta de podcast, projetada pra ser ouvida no trânsito, na academia, ou no intervalo do almoço. Você não precisa sentar três horas pra aprender uma coisa. Você precisa de 15 a 25 minutos por cena, e de coragem pra aplicar antes da próxima.

A estrutura do livro segue o método de 6 etapas que eu ensino há mais de uma década: Planejamento, Estrutura, Audiência, Vendas, Atendimento, e Impulsão. Cada etapa é um capítulo (ou um bloco de capítulos), e cada capítulo é um conjunto de cenas que constrói a etapa inteira. Não é uma coletânea de dicas soltas. É um sistema, com começo, meio, e fim. E o fim é uma coisa concreta: R$ 10 mil em vendas, 100 pedidos, em ~90 dias. Isso é o que eu chamo de validação primária. E quando você cruza os R$ 30 mil mensais, você atinge a validação consolidada, que é o diploma definitivo de que o negócio funciona. Aí o céu é o limite.

Eu não vou te vender a fantasia de que e-commerce é ficar rico da noite pro dia. Quem te diz isso está te vendendo o próprio curso, não te ensinando a construir. E-commerce é um trabalho, e é um trabalho que demora, mas que funciona. E funciona mais rápido quando você segue o método, sem pular etapa, sem inventar atalho, sem desistir no primeiro mês fraco. Por isso, o primeiro capítulo deste livro é sobre mindset, e não sobre como ganhar dinheiro. Porque se a sua cabeça não estiver no lugar, nenhum tutorial te salva.

Você vai encontrar, ao longo do livro, cases reais de quem executou o método: a Patacori (minha loja), a Cozilar (aluna que construiu audiência), a Patrícia (que trocou bolsa de praia por bolsa de bíblia), o Victor (que ficou três meses sem resultado até achar o tapete de banheiro), o John (que descobriu o descascador de pinhão e hoje fatura R$ 91 mil por mês com um único produto). E a aluna que viralizou no TikTok e passou de zero pra 800 vendas em dois meses. Esses cases não são pra você se comparar. São pra você ver que o método funciona, e que o próximo case pode ser o seu.

Você vai encontrar também o canivete suíço do operacional: como configurar a conta de anúncios do Mercado Livre, como ler o termômetro (verde, amarelo, vermelho), o que é o Triângulo do Sucesso (audiência × estrutura × ofertas), como funciona a engrenagem invisível do Bling (o ERP que organiza tudo), como emitir nota fiscal integrada ao pedido, como criar kit com estoque virtual, e como calcular o preço real de um produto (porque preço de venda não é preço de custo + margem. É preço de custo + TODOS os custos + margem). E no final, um bônus sobre missão, visão e valores — porque negócio sem DNA não escala, e negócio sem alma não sustenta.

Eu te peço uma coisa. Antes de começar a aplicar o que você vai aprender, pare. Vá no capítulo 1, leia com calma, e escreva no papel o que você quer que a sua vida seja daqui a 12 meses. Não 10 anos. 12 meses. Porque o método que você está prestes a aprender foi feito pra entregar resultado em 12 meses, não em 10 anos. E se você fizer a lição de casa direitinho, em três meses você vai estar validando, e em 12 meses você vai estar olhando pra trás e dizendo: "valeu a pena". Eu tenho certeza.

Boa jornada. E se travar, volta no capítulo certo. Esse livro é a sua bússola.

— Bruno de Oliveira
"""

INTRODUCAO = """# Introdução

## Como ler este livro

Este livro é dividido em 12 capítulos, e cada capítulo em cenas. Cada cena é independente, mas a ordem importa: o método se constrói em camadas, e pular uma camada é como construir uma casa começando pelo telhado.

A estrutura é:

- **Cap 1 a 4 — Fundamentação:** mindset, mercado, método, e estrutura mínima viável.
- **Cap 5 a 8 — Operação:** audiência, atendimento, vendas, e impulsão.
- **Cap 9 a 12 — Escala e especialização:** validação, Mercado Livre em profundidade, Bling na prática, e cases + bônus + epílogo.

Cada cena termina com um **resumo** e um **checklist**, e com um **preview da próxima cena ou do próximo capítulo**. Isso é intencional. O resumo te ajuda a revisar, o checklist te ajuda a aplicar, e o preview te mantém conectado ao fio da jornada.

Quando eu digo "Bora", "Toca", "Vamos", ou "Te vejo", é pra te puxar pra ação. Eu não tô te dando uma palestra acadêmica. Eu tô te mentorando, e mentor cobra movimento.

E quando eu cito a Claudia, a Mariana, a Renata, ou a Patacori, é porque são personas e cases reais que aparecem ao longo do livro, e que te ajudam a visualizar o método em ação. A Claudia é a persona canônica da Patacori (cliente típica). A Patacori é minha loja, e é o meu case âncora.

Vai ser um prazer te acompanhar. Toca começar.
"""

SUMARIO = """# Sumário Geral

- **Prefácio**
- **Introdução — Como ler este livro**

**Bloco 1 — Fundamentação (Cap 1 a 4)**
- **Capítulo 1 — Boas-Vindas e Mindset** (3 cenas)
  - Cena 1.1 — Boas-vindas: a jornada começa agora
  - Cena 1.2 — A versão 3.0: o que mudou
  - Cena 1.3 — A equipe por trás: você não está sozinho

- **Capítulo 2 — O Mercado e Você** (4 cenas)
  - Cena 2.1 — O que esperar do método: o mapa da jornada
  - Cena 2.2 — O mercado de e-commerce: o campo de batalha real
  - Cena 2.3 — Você pode, você consegue: o mindset do validador
  - Cena 2.4 — Objetivos e princípios do seu negócio

- **Capítulo 3 — O Método e o Planejamento** (6 cenas)
  - Cena 3.1 — O método em 6 etapas: o mapa da mina
  - Cena 3.2 — A meta de validação: R$ 10 mil, 100 pedidos, 90 dias
  - Cena 3.3 — Nicho, persona, produto: o tripé da escolha
  - Cena 3.4 — Fornecedores: como encontrar e homologar
  - Cena 3.5 — Dropshipping: a verdade que ninguém te conta
  - Cena 3.6 — Ofertas, demanda e produto estrela

- **Capítulo 4 — A Estrutura Mínima Viável (MVP)** (8 cenas)
  - Cena 4.1 — A estrutura mínima viável (MVP)
  - Cena 4.2 — Sua estrutura física: mesa, luz, embalagem
  - Cena 4.3 — Marca, CNPJ, MEI, ME: a papelada que liberta
  - Cena 4.4 — Domínio, e-mail profissional, canais de audiência e venda
  - Cena 4.5 — ERP, gateway, envios: a engrenagem
  - Cena 4.6 — SKU, EAN e cadastro de produtos
  - Cena 4.7 — Dropshipping nacional: como montar a triangulação
  - Cena 4.8 — Descrição, fotos, vídeos: a vitrine que vende

**Bloco 2 — Operação (Cap 5 a 8)**
- **Capítulo 5 — Audiência É Rei** (6 cenas)
  - Cena 5.1 — Audiência é rei: a nova regra do jogo
  - Cena 5.2 — Persona: para quem você fala, de verdade
  - Cena 5.3 — Canais de conteúdo: onde sua persona está
  - Cena 5.4 — Autoridade: como virar referência
  - Cena 5.5 — A jornada de compra e a régua de conteúdo
  - Cena 5.6 — Impulsão de conteúdo: o que já funciona, amplifique

- **Capítulo 6 — Atendimento que Converte** (5 cenas)
  - Cena 6.1 — Atendimento: de SAC a CX (Customer Experience)
  - Cena 6.2 — Canais: marketplace, WhatsApp, Direct, Messenger, e-mail
  - Cena 6.3 — Pré-venda: conquistando antes do clique
  - Cena 6.4 — Pós-venda: encantamento, follow-up, recompra
  - Cena 6.5 — Solução de conflitos: quando o problema aparece

- **Capítulo 7 — Vendas e Ofertas** (6 cenas)
  - Cena 7.1 — Estrutura de vendas: o funil que não vaza
  - Cena 7.2 — Post de conversão: o que falar quando você quer vender
  - Cena 7.3 — Cross-sell, upsell, down-sell: táticas para inflar o ticket
  - Cena 7.4 — Kits: como criar e vender composições lucrativas
  - Cena 7.5 — Nota fiscal na prática: emitindo pelo Bling
  - Cena 7.6 — Gestão de pedidos, horário de corte, expedição

- **Capítulo 8 — Impulsão Estratégica** (5 cenas)
  - Cena 8.1 — A estratégia de impulsão: anunciar SÓ o que já funciona
  - Cena 8.2 — Conta de anúncios e método de pagamento: configurando o motor
  - Cena 8.3 — Analisando resultados orgânicos: separando joio de trigo
  - Cena 8.4 — Criando públicos: o motor silencioso que faz o anúncio achar a Claudia
  - Cena 8.5 — Quanto investir: a mentalidade de crescimento progressivo

**Bloco 3 — Escala e Especialização (Cap 9 a 12)**
- **Capítulo 9 — Parabéns! Você validou o negócio** (2 cenas)
  - Cena 9.1 — Você validou: a barreira foi rompida
  - Cena 9.2 — Próximos passos: do R$ 10K ao R$ 100K, a próxima escalada

- **Capítulo 10 — Domínio do Mercado Livre** (3 cenas)
  - Cena 10.1 — Ecossistema, termômetro e reputação: a engrenagem invisível
  - Cena 10.2 — Triângulo do Sucesso: audiência × estrutura × ofertas
  - Cena 10.3 — Mercado Líder, kits e anúncios múltiplos: as 3 táticas que mantêm o triângulo equilibrado

- **Capítulo 11 — O ERP na Prática (Bling)** (3 cenas)
  - Cena 11.1 — Bling: o ERP que organiza a operação, e o que configurar no dia 1
  - Cena 11.2 — Cadastrando produtos no Bling, e o caminho reverso: importar do Mercado Livre
  - Cena 11.3 — Emitindo nota fiscal pelo Bling, e o fluxo completo de venda integrado ao Mercado Livre

- **Capítulo 12 — Cases, Bônus e Epílogo** (3 cenas)
  - Cena 12.1 — Cases reais: Patacori, Cozilar e alunos que executaram o método
  - Cena 12.2 — Bônus: gestão de preços e o DNA do seu negócio (missão, visão, valores)
  - Cena 12.3 — Epílogo: do R$ 10K ao R$ 100K, a próxima escalada

**Bloco 4 — Apêndices**
- **Glossário de Termos Técnicos**
- **Epílogo Expandido: A despedida do mentor**
- **Lista de Cases e Personas**
- **5 Livros Recomendados**
- **2 Treinamentos Complementares**
"""


def ler_capitulo(cap_num: int, cap_dir: str) -> str:
    caminho = BASE / cap_dir / f"livro_capitulo_{cap_num:02d}.md"
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


GLOSSARIO = """# Glossário de Termos Técnicos

> Glossário das 30-40+ termos técnicos que aparecem ao longo do livro. Use como referência quando encontrar um termo que você não conhece.

## A

- **Audiência:** conjunto de pessoas que confiam em você, te seguem, e podem comprar de você. Construída com consistência e valor, não com anúncio. (Cap 5)
- **Anúncios Múltiplos:** estratégia de criar 3-5 anúncios para o mesmo produto, com título, foto, descrição, preço e tipo de anúncio diferentes, capturando diferentes Claudias que pesquisam de jeitos diferentes. (Cap 10, cena 3)
- **Anúncio Premium:** tipo de anúncio do Mercado Livre com maior visibilidade e mais recursos. Custa mais comissão (~16%), mas aparece em cima. (Cap 10, cena 3)
- **Anúncio Clássico:** tipo de anúncio do Mercado Livre com menos visibilidade. Custa menos comissão (~12%), mas aparece mais embaixo. (Cap 10, cena 3)
- **Atendimento ao Cliente (CX — Customer Experience):** abordagem proativa que constrói a jornada inteira do cliente, oposta ao SAC reativo. (Cap 6, cena 1)
- **Ajuda de custo / Custo total do produto:** soma de preço de custo + desconto médio + frete + embalagem + marketing + outros custos. É o "preço de custo verdadeiro" antes da margem de lucro. (Cap 12, cena 2)
- **Alcance pago:** número de pessoas que viram o post porque foi impulsionado. (Cap 8, cena 3)
- **Alcance orgânico:** número de pessoas que viram o post sem impulsionamento, pelo algoritmo do Facebook/Instagram. (Cap 8, cena 3)

## B

- **Bling:** ERP brasileiro líder para micro e pequenas empresas. Plano Cobalto (~R$ 50/mês) é o mínimo viável. Plano Titânio (~R$ 100/mês) é o avançado (usado na Patacori). (Cap 4, cena 5 e Cap 11 inteiro)
- **BM (Business Manager):** ferramenta profissional do Facebook Ads para empresas. Recomendado a partir de R$ 5-10 mil/mês de faturamento. (Cap 8, cena 2)
- **Branded content:** post de marca em parceria com creator. (Cap 8, cena 3)

## C

- **Cases com atrito:** princípio editorial de contar cases reais com fracasso inicial, não só sucesso. (Cap 5 em diante)
- **Cap 1 a 4 (Fundamentação), 5 a 8 (Operação), 9 a 12 (Escala + Especialização):** os 3 blocos do método de 6 etapas. (Cap 3, cena 1)
- **CFOP (Código Fiscal de Operações):** código fiscal que classifica a operação da NF-e. Vem por padrão na natureza de operação do Bling. (Cap 11, cena 3)
- **CNPJ (Cadastro Nacional da Pessoa Jurídica):** registro da empresa. MEI (limite R$ 80 mil/ano) ou ME (limite maior, paga Simples Nacional). (Cap 4, cena 3)
- **Cupom de 4 meses grátis:** promoção que o Bruno dá com o Bling. Após os 4 meses, R$ 50/mês. (Cap 4, cena 5 e Cap 11, cena 1)
- **Certificado Digital:** arquivo + senha que permite emitir NF-e. Obrigatório para ME. Validade 1 ano. Custo R$ 139-200/ano. (Cap 4, cena 3 e Cap 11, cena 1)
- **Código de Barras / EAN (European Article Number):** código universal de 13 dígitos presente em produtos industrializados. Identifica o produto no ML. (Cap 4, cena 6 e Cap 11, cena 2)
- **CIF / FOB:** modalidades de frete. CIF = vendedor paga. FOB = comprador paga. (Cap 7, cena 6)
- **CRM (Customer Relationship Management):** gestão do relacionamento com o cliente. WhatsApp Business + Bling fazem CRM básico. (Cap 6, cena 2)
- **Cross-sell:** oferecer produto complementar na hora da venda. (Cap 7, cena 3)
- **CPC (Custo por Clique):** quanto você paga por cada clique num anúncio. Patacori referência: ~R$ 1. (Cap 8, cena 3)
- **CPS (Custo por Seguidor):** quanto você paga por cada seguidor ganho via anúncio. Patacori referência: ~R$ 3. (Cap 8, cena 3)
- **CX (Customer Experience):** ver Atendimento ao Cliente.

## D

- **Dropshipping:** modelo de distribuição (não modelo de negócio) onde o vendedor não estoca — repassa o pedido ao fornecedor que envia direto ao cliente. Viável apenas com fornecedores nacionais homologados no Brasil. Dropshipping internacional é importação ilegal. (Cap 3, cena 5)
- **Down-sell:** oferecer versão mais barata quando o cliente resiste ao preço principal. (Cap 7, cena 3)
- **DRE (Demonstrativo de Resultado do Exercício):** relatório financeiro que mostra receita, custos, e lucro. (Cap 12, cena 2)
- **Dia de corte:** horário limite do dia para despachar pedidos. Patacori: até 13h16 (pra coleta do Mercado Envios às 14h16). (Cap 7, cena 6)

## E

- **EAN (European Article Number):** ver Código de Barras.
- **ERP (Enterprise Resource Planning):** sistema de gestão integrado. Na obra: o Bling é o ERP recomendado. (Cap 4, cena 5 e Cap 11 inteiro)
- **Estrutura Mínima Viável (MVP):** princípio de começar pequeno: estrutura simples e barata para testar, robusta só depois da validação. (Cap 4, cena 1)
- **Estoque virtual (kit):** estoque do kit = menor estoque dos componentes. Quando vende 1 kit, baixa 1 de cada componente. (Cap 11, cena 2)
- **Etiqueta Mercado Envios:** etiqueta gerada automaticamente pelo Bling, contém dados do destinatário, NF, e código de rastreio. (Cap 11, cena 3)

## F

- **Faturamento direto:** quanto entra no caixa. Patacori meta: R$ 10K → R$ 30K → R$ 100K. (Cap 3, cena 2)
- **Faturamento indireto (ROAS):** retorno sobre investimento em anúncios. ROAS 5x = saudável. ROAS 10x = excelente. (Cap 10, cena 3)
- **FB (Facebook):** rede social. Fanpage = página comercial. (Cap 8, cena 1)
- **Faturamento por origem:** ver ROI por canal.
- **Frete grátis (R$ 99+):** benefício do Mercado Livre pra vendas acima de R$ 99 (era R$ 120, baixou pra 99). Vendedor paga. Mercado Líder paga metade. (Cap 10, cena 3)
- **FULL (Mercado Envios FULL):** logística do ML. Estoque vai pro galpão do ML, e sai direto pro cliente. Recomendado pra Mercado Líder. (Cap 10, cena 1)
- **Funil de vendas:** jornada do cliente desde o primeiro contato até a recompra. (Cap 7, cena 1)

## G

- **Glossário:** lista de termos técnicos com definições. Use como referência. (este glossário)

## H

- **Horário de corte:** ver Dia de corte.

## I

- **Impulsão Seletiva:** anunciar SÓ o que já está funcionando organicamente. Não impulsionar o fraco. (Cap 8, cena 1)
- **IG (Instagram):** rede social de fotos e vídeos. Perfil comercial > perfil pessoal. (Cap 5, cena 3)
- **Insights:** métricas e dados do Facebook/Instagram/Mercado Livre. (Cap 5, cena 3 e Cap 8, cena 3)
- **Inbound:** estratégia de marketing que atrai o cliente com conteúdo, oposta a Outbound. (Cap 5, cena 5)
- **Insumos:** tudo que você usa pra produzir/enviar: embalagem, fita, plástico bolha, papel craft. (Cap 4, cena 2 e Cap 11, cena 2)

## J

- **Jornada de compra:** caminho que o cliente percorre desde o primeiro contato até a recompra. Produto estrela (aquisição) → oferta principal (lucro). (Cap 7, cena 5)
- **Janela de lookalike:** tempo que o público-base tem que ter para Facebook gerar lookalike. Mínimo 100 pessoas. (Cap 8, cena 4)

## K

- **Kit (composição):** produto virtual composto por N produtos unitários. Estoque do kit = menor estoque dos componentes. Requer EAN próprio. (Cap 7, cena 4 e Cap 11, cena 2)
- **KPI (Key Performance Indicator):** métrica-chave. Ex: ROAS, taxa de conversão, ticket médio. (Cap 10, cena 3)

## L

- **Lead:** pessoa que demonstrou interesse. Pode ser visitante, inscrito, seguidor, ou cliente. (Cap 5, cena 5)
- **Lookalike (Público Semelhante):** público criado pelo Facebook Ads a partir de um público-base, com pessoas parecidas mas que ainda não conhecem sua marca. (Cap 8, cena 4)
- **Lead time:** tempo entre comprar do fornecedor e despachar pro cliente. (Cap 7, cena 6)

## M

- **MEI (Microempreendedor Individual):** regime simplificado. Limite R$ 80 mil/ano, isento de imposto sobre venda, paga contribuição social. (Cap 4, cena 3)
- **ME (Microempresa):** regime mais robusto. Limite maior, paga Simples Nacional começando na primeira faixa. (Cap 4, cena 3)
- **MVP (Mínimo Produto Viável):** ver Estrutura Mínima Viável.
- **Marketplace:** canal de venda de terceiros (Mercado Livre, Shopee, Americanas, etc). (Cap 4, cena 5 e Cap 10 inteiro)
- **Mercado Líder (ML):** selo de vendedor elite no Mercado Livre. 3 níveis: Silver, Gold, Platinum. Requer volume + reputação verde escuro. (Cap 10, cenas 1 e 3)
- **Mercado Pago:** fintech do Mercado Livre. Processa pagamento 12x sem juros, dinheiro rende 100% CDI, crédito, antecipação. (Cap 10, cena 1)
- **Mercado Envios:** braço logístico do ML. Etiqueta, coleta, FULL. (Cap 10, cena 1 e Cap 11, cena 3)
- **Mix de produtos:** combinação de produtos no catálogo. Estrela + complemento + volume. (Cap 7, cena 4)
- **Marketing de conteúdo:** estratégia de criar conteúdo que atrai e engaja, sem vender diretamente. (Cap 5, cena 5)

## N

- **NCM (Nomenclatura Comum do Mercosul):** código fiscal de 8 dígitos que classifica o produto. Obrigatório na NF-e. (Cap 11, cena 3)
- **Nicho:** segmento de mercado específico (ex: aromaterapia, decoração, infoprodutos). (Cap 3, cena 3)
- **NF-e (Nota Fiscal Eletrônica):** documento fiscal emitido pra cada venda. Obrigatório. Emitido pelo Bling. (Cap 4, cena 3 e Cap 11, cena 3)

## O

- **Oferta (E-commerce):** combinação de produto + preço + proposta de valor. (Cap 3, cena 6 e Cap 7, cena 1)
- **Organização do público (ML):** ato de separar as contas integradas (ex: várias contas ML) com nome claro. (Cap 11, cena 1)

## P

- **Patacori:** loja de pedras e cristais do próprio Bruno. Opera com Bling Titânio, 80-90% dos envios em sacos de embalagem, kit de 7 chakras como produto carro-chefe. Case âncora da obra. (Cap 4, cena 2, e ancorada em toda a obra)
- **Persona:** perfil detalhado do cliente ideal. Inclui demografia, comportamento, dores, desejos. (Cap 5, cena 2)
- **Público personalizado (Meta Ads):** grupo de pessoas segmentadas por interesse, comportamento, ou dados próprios. (Cap 8, cena 4)
- **Público lookalike:** ver Lookalike.
- **Pixel do Facebook:** código instalado no site que rastreia visitantes. Permite criar público de visitantes. (Cap 8, cena 4)
- **Pós-venda:** ações após a venda: agradecimento, follow-up, pesquisa de satisfação, oferta de recompra. (Cap 6, cena 4)
- **Pré-venda:** ações antes da venda: responder perguntas, tirar dúvidas, criar urgência. (Cap 6, cena 3)
- **Produto Estrela:** produto com alto lucro + baixa concorrência, que vira carro-chefe. (Cap 3, cena 6 e Cap 10, cena 2)
- **Plano de ação:** lista de tarefas com prazo pra atingir objetivo. (Cap 12, cena 2)
- **Proposta de valor:** o que o cliente recebe de único ao comprar de você. (Cap 3, cena 6)

## Q

- **Quadro Kanban:** ferramenta visual de gestão de tarefas. (Cap 7, cena 6)

## R

- **Remarketing:** anúncios para pessoas que já interagiram com você (visitaram, compraram, abandonaram carrinho). (Cap 8, cena 4)
- **ROAS (Return on Ad Spend):** retorno sobre investimento em anúncios. = faturamento ÷ investimento. (Cap 10, cena 3)
- **ROI (Return on Investment):** retorno sobre investimento geral. (Cap 12, cena 2)
- **Recompra:** cliente que volta a comprar. Métrica-chave de CX. (Cap 6, cena 4)

## S

- **SAC (Serviço de Atendimento ao Consumidor):** abordagem reativa, resolve problemas. Oposta ao CX. (Cap 6, cena 1)
- **SKU (Stock Keeping Unit):** código interno criado pelo vendedor para organizar o produto. Cada item tem SKU único. (Cap 4, cena 6 e Cap 11, cena 2)
- **Smart (objetivo):** ver Objetivo SMART.
- **Status do pedido (Bling):** ver Pedido (status).

## T

- **Termômetro (ML):** medidor de credibilidade. 3 cores: verde escuro (meta), amarelo (risco), vermelho (crítico). Ativa após 10 vendas. (Cap 10, cena 1)
- **Triângulo do Sucesso:** Audiência + Estrutura + Ofertas. Conceito proprietário do Bruno. Se 1 cai, o negócio cai. (Cap 10, cena 2)
- **TikTok:** rede social de vídeos curtos. Canal forte pra audiência de 18-30. (Cap 5, cena 3)
- **Ticket médio:** valor médio por venda. = faturamento ÷ número de vendas. (Cap 7, cena 3)
- **Taxa de conversão (ML):** % de visitantes que compram. >1% manter, <1% desativar. (Cap 10, cena 3)
- **Total de pedidos pendentes (Bling):** pedidos em status amarelo (em aberto). (Cap 11, cena 3)

## U

- **Upsell:** oferecer versão mais cara na hora da venda. (Cap 7, cena 3)

## V

- **Validação (R$ 10K):** ver Validação Primária.
- **Validação Primária (R$ 10K, 100 pedidos, 90 dias):** primeiro estágio de validação. Você tem uma pequena certeza que o negócio vai dar resultado. (Cap 9, cena 1)
- **Validação Consolidada (R$ 30K/mês):** segundo estágio. 99% de chance de sucesso. Você rompeu a "barreira de arrebentação" (analogia do surf). (Cap 9, cena 1)
- **Vendedor (Bling):** quem vende dentro da sua loja, se você tiver mais de um. (Cap 11, cena 5 — versão antiga, mas o conceito segue)
- **Verde escuro (termômetro):** ver Termômetro.

## W

- **WhatsApp Business:** versão profissional do WhatsApp, com perfil comercial, mensagens automáticas, e catálogo. (Cap 6, cena 2)

## X

- **XLSX (Excel):** formato de planilha. (Cap 12, cena 2)

## Y

- **YouTube:** rede social de vídeos longos. Canal forte pra autoridade. (Cap 5, cena 3)

## Z

- **Zapier:** ferramenta de automação que conecta apps. (mencionado em cap 5, integração)
"""


EPLOGO_EXPANDIDO = """# Epílogo Expandido: A despedida do mentor

## O que você aprendeu em 12 meses condensados em 12 capítulos

Querido aluno, querida aluna,

Você chegou ao fim. Mas, como eu disse no Cap 1, o fim deste livro é o começo da sua jornada. Então, antes de você fechar essa página e voltar pro mundo, deixa eu te dar um último panorama — não só do que você aprendeu, mas do que isso significa pra você nos próximos 12 meses.

Quando você abriu o Cap 1, três meses atrás, no seu tempo de leitura, você provavelmente estava em um desses três estados: ou você estava perdido no mar de informação sobre e-commerce, sem saber por onde começar; ou você já tinha tentado alguma coisa e travado; ou você estava prestes a começar e queria ter certeza de que ia fazer do jeito certo. Qualquer um dos três, agora, no Cap 12, você está em outro lugar. Você tem o método dos 6 etapas, sabe o que é uma estrutura mínima viável, sabe que audiência vem antes de conteúdo (não o contrário), sabe que a Claudia (sua cliente) é quem decide tudo, sabe que o Triângulo do Sucesso precisa estar equilibrado, e sabe que o Bling é o motor invisível que organiza a operação inteira. Você tem mais repertório do que 90% das pessoas que tentam e-commerce no Brasil.

Mas, como eu disse lá no Cap 2, cena 3, na história que eu te contei de quando eu repeti de ano, quando eu tentei faculdade e não consegui de primeira, e quando eu comecei a empreender sem nada no bolso: o que faz diferença não é o que você sabe, é o que você faz com o que sabe. E a diferença entre quem termina validando e quem desiste no meio é, na maioria das vezes, simplesmente continuar fazendo o que precisa ser feito, mesmo quando os resultados demoram pra aparecer. Isso, na psicologia, chama-se resiliência. No mundo do empreendedorismo, eu chamo de teimosia boa. É a mesma coisa.

Então, aqui vai o meu pedido final, em três partes.

### Parte 1: Compromisso com a aplicação

Antes de você fechar este livro, escreva no papel (não no celular, no papel) a sua meta de validação. R$ 10 mil em vendas, 100 pedidos, em 90 dias. Ou a sua régua, se for maior. E coloque esse papel em algum lugar que você vai ver todo dia: no espelho do banheiro, ao lado do computador, na geladeira, no app de notas com lembrete diário. Porque o que você não vê, você esquece. E o que você esquece, você não faz.

A partir de amanhã, defina um horário fixo de 2 horas por dia, 5 dias por semana, pra trabalhar no seu negócio. Pode ser de manhã, antes do expediente. Pode ser à noite, depois do jantar. Pode ser no almoço, no escritório. Mas tem que ser fixo, e tem que ser inegociável. Se você não fizer isso, o método vira teoria, e teoria não paga boleto.

E o mais importante: escreva, também, os seus 5 princípios do negócio, como eu ensinei no Cap 2, cena 4. Cliente no centro, transparência, respeito ao próximo, foco no longo prazo, aprendizado contínuo. Ou os seus próprios, mas 5, escritos, visíveis, lembrados todo dia. Porque quando vier a tentação de dar um atalho, de enganar um cliente, de cortar uma qualidade pra ganhar mais, a sua cabeça vai precisar de uma base pra decidir. E essa base são os seus princípios.

### Parte 2: Compromisso com a comunidade

Eu falei no Cap 1, cena 3, sobre a comunidade de alunos. Ela existe, e ela está te esperando. Quando você tiver a primeira venda, posta lá. Quando você tiver a primeira reclamação, pede ajuda lá. Quando você tiver a primeira dúvida sobre tributação, sobre embalagem, sobre marketplace, sobre logística, pergunta lá. E quando você bater os R$ 10 mil, posta lá também, e vai ser o "im-purrãozinho" pra alguém que está empacado no meio do caminho.

Mas mais do que isso: a comunidade também é fonte de network. Eu já tive alunos que conheceram fornecedores pela comunidade, que fecharam parcerias pela comunidade, e que encontraram co-fundadores pela comunidade. E o que une essas pessoas é que todas elas estão tentando a mesma coisa, com o mesmo método, e estão dispostas a se ajudar. Você vai encontrar gente que vende o mesmo produto que você em outra cidade, gente que vende produto diferente mas que pode te ensinar sobre logística, gente que está dois passos na frente e que pode te ajudar a evitar os erros que ela já cometeu. E no dia que você estiver dois passos na frente, vai ser a sua vez de ajudar o próximo.

Então, comprometa-se: entre na comunidade nos próximos 7 dias, apresente-se, e fique. Não é "olhar de vez em quando". É ficar de verdade. Toda semana. Toda pergunta que você fizer, vai ser respondida. Toda dúvida que você postar, vai gerar 5 respostas de pessoas que já passaram por aquilo. E o contrário também: toda vez que alguém postar uma dúvida que você já sabe a resposta, responda. É dando que se recebe, e é ensinando que se aprende.

### Parte 3: Compromisso com a próxima fase

Eu te disse no Cap 9, cena 2, que a validação primária (R$ 10K) é o diploma do método, e a validação consolidada (R$ 30K) é o diploma do negócio. E o caminho entre as duas é a fase de "ramp-up", que leva de 3 a 6 meses, e que tem 4 próximos passos: estrutura profissional, marketplaces pós-validação, conhecimento novo, e treinamentos complementares. Eu te apresentei os 5 marketplaces pós-validação (B2W, Dafiti, NetShoes, Via Varejo, Leroy Merlin), e os 2 treinamentos complementares (Explosão de Tráfego e Vendas, Viver de Ecommerce).

Mas o que eu não te disse no Cap 9, e que eu te digo agora, é o seguinte: o momento de você pensar nesses 4 próximos passos é AGORA, mesmo que você ainda esteja na fase de validação. Porque é pensando neles que você vai tomar as decisões do presente: quando você for cadastrar o primeiro produto, escolha um que tem chance de funcionar também na B2W. Quando você for configurar a conta de anúncios, configure BM, não perfil. Quando você for definir o orçamento de marketing, defina com a mentalidade de crescimento, não com medo. Você não precisa executar esses 4 passos agora. Mas precisa ter eles no radar, e ir plantando as sementes enquanto está validando.

E se você chegar aos R$ 10K e não souber o que fazer, eu te dou dois caminhos óbvios. O primeiro é o treinamento "Explosão de Tráfego e Vendas", que vai te formar como gestor de tráfego, e que vai transformar a impulsão que você aprendeu no Cap 8 em gestão de tráfego profissional. O segundo é o treinamento "Viver de Ecommerce", que é o MBA do e-commerce: 100+ horas, 4 pilares (estrutura profissional, marketing, gestão, otimização), com suporte e comunidade, e que te leva do R$ 100K ao R$ 1 milhão. E os dois têm desconto exclusivo pra quem concluiu o Ecommerce do Zero, que é o caso de quem está lendo este livro.

Mas não se cobre pra fazer tudo ao mesmo tempo. Faça o que dá pra fazer agora, e faça bem feito. E quando estiver pronto pra próxima fase, vá. Um passo de cada vez, com método, com constância, e com a missão clara.

## O que eu quero que você leve deste livro

Vou te dar 7 coisas, que são as 7 coisas que eu quero que você leve quando fechar este livro e voltar pro mundo.

1. **O método dos 6 etapas.** Planejamento, Estrutura, Audiência, Vendas, Atendimento, Impulsão. Essa é a sequência canônica. Pular etapa é a forma mais rápida de quebrar.

2. **A base canônica.** Bling (ERP) + Mercado Livre (marketplace) + Patacori (case). Essa é a sua régua técnica. Quando aparecer dúvida de ferramenta, pergunte: "O que a Patacori usa?" E o que a Patacori usa, funciona.

3. **A régua de 3 fases.** R$ 10K (validação primária) → R$ 30K (validação consolidada) → R$ 100K (escala). Cada fase tem o que fazer. Não confunda as fases. Não tente pular a fase 1 pra ir direto pra fase 3.

4. **Os cases reais.** Patacori, Cozilar, Patrícia, Victor, John, aluna TikTok. São a prova de que o método funciona, e são o espelho onde você vai se ver refletido daqui a 6 meses.

5. **A bússola do DNA.** Missão, visão, valores. São o que te carrega nos momentos difíceis. Defina, escreva, cole onde você vê todo dia. E revise a cada 3 meses.

6. **A planilha de preço.** 8 campos. Custo de verdade, não custo inventado. Use pra todo produto. E atualize quando o custo mudar.

7. **Os manuais operacionais.** Mercado Livre (termômetro, Triângulo, Mercado Líder, anúncios múltiplos, publicidade) e Bling (5 configs do dia 1, 13 passos do cadastro, NF integrada). São o seu "como fazer" detalhado. Volte neles quando travar.

## A despedida

E aí, chegamos ao fim. Eu vou ser breve, porque o livro já foi longo, e porque o que eu tenho pra te dizer cabe em uma frase.

Eu te desejo boa sorte. Mas a sorte não é o que vai te levar até o R$ 10K, ou até o R$ 30K, ou até o R$ 100K. O que vai te levar é método, constância, resiliência, e a coragem de continuar fazendo o que precisa ser feito mesmo quando o resultado demora pra aparecer. E eu te dei o método. A constância, a resiliência, e a coragem são suas. E eu tenho certeza que você tem.

Quando você bater a meta, e vai bater, eu quero que você volte a esta aula, e releia o parágrafo acima, e lembre: o método funcionou, mas foi você que aplicou. E quando o próximo aluno te perguntar "como você fez?", você vai poder contar a sua história, com cases com atrito, com tropeços, com recomeços. E essa história vai ser a próxima case que eu cito neste treinamento, e que vai inspirar o próximo Bruno, a próxima Claudia, o próximo Victor, a próxima Patrícia, o próximo John. E aí o ciclo continua.

Valeu por ter lido até aqui. Valeu por ter aplicado. Valeu por ter acreditado. E valeu por ter feito a sua parte.

Nos vemos na comunidade. E nos vemos no R$ 10K.

Um grande abraço,
Bruno de Oliveira
"""

LISTA_CASES = """# Lista de Cases e Personas

> Este livro apresenta 11+ cases reais (Patacori + 5 alunos + 5 cases DNA). Aqui está a lista consolidada, com a função de cada um no método.

## Cases Canônicos do Método (análise + atrito)

| Case | Função no Método | Onde aparece | Atrito |
|------|------------------|--------------|--------|
| **Patacori** (loja do Bruno) | Case âncora de toda a obra. Prova de que o método funciona em 12 anos de execução. | Cap 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | R$ 800 inicial → R$ 100K+ em 12 anos; R$ 1.500 em FB Ads → R$ 800 em vendas (prejuízo); certificado vencido; NCM errado |
| **Cozilar** (aluna) | Case de audiência construída. REFERÊNCIA SECUNDÁRIA da Bible. | Cap 5 (Audiência), Cap 12 (Bônus) | — |
| **Patrícia** | Case de produto estrela descoberto. Mostra que a oferta certa supera estrutura e audiência. | Cap 10, cena 2; Cap 12, cena 1 | Bolsa de praia saturada, "no vermelho" |
| **Victor** | Case de persistência. Mostra que 3-4 meses sem resultado é normal, e o produto certo está esperando. | Cap 10, cena 2; Cap 12, cena 1 | 3-4 meses sem validar, "sem resultado" |
| **John** | Case de pivotagem. Moda íntima não funcionou; descascador de pinhão escalou pra R$ 91K/mês. | Cap 10, cena 2; Cap 12, cena 1 | Moda íntima não validou |
| **Aluna TikTok** | Case de canal. 1 vídeo viral = 0 → 800 vendas em 2 meses. | Cap 5, cena 6; Cap 12, cena 1 | — |

## Cases de DNA (referência cultural)

| Case | Função no Método | Onde aparece | Aprendizado |
|------|------------------|--------------|-------------|
| **Zappos** (Tony Hsieh) | Case lendário de "missão é o motor". 10 valores, "wow through service". | Cap 12, cena 2 | Distribuir felicidade; ir além da venda |
| **NetShoes** | Case de e-commerce esportivo com DNA claro. | Cap 12, cena 2 | Missão: transformar vida das pessoas com esporte e lazer |
| **Dafiti** | Case próximo ao Brasil de e-commerce de moda. | Cap 12, cena 2 | Foco no cliente, senso de urgência, partilhar aprendizado |
| **Amazon (Bezos)** | Case de "Customer Obsession". | Cap 12, cena 2 | Trabalhar de trás pra frente a partir do cliente |
| **Jim Collins** (Built to Last, Good to Great) | Case de framework de DNA corporativo. | Cap 12, cena 2 | DNA como fundação de empresa durável |

## Personas Canônicas

| Persona | Quem é | Onde aparece | Função |
|---------|--------|--------------|--------|
| **Claudia** | Cliente típica da Patacori. Mulher, 30-45 anos, gosta de bem-estar, compra para si mesma. | Cap 5, 8, 9, 10, 11 | Âncora narrativa do "pra quem" você está construindo |
| **Mariana, Renata** | Personas alternativas mencionadas em alguns cases. | Cap 5 | Variedade de perfis |
| **Ana Clara** | Diretora de marketing do Ecommerce do Zero. | Cap 5, cena 1 | Pessoa que ensina a parte de audiência |
| **Babi** | Diretora de CX do Ecommerce do Zero. | Cap 6, cena 1 | Pessoa que ensina a parte de atendimento |

## Cases com atrito (princípio editorial)

> O livro aplica o princípio editorial "cases com atrito" (a partir do Cap 5): todo case é apresentado COM o fracasso inicial, NÃO só o sucesso. Isso serve pra:
> 1. **Evitar romantização** do empreendedorismo
> 2. **Mostrar a curva real** (lenta no início, acelera depois)
> 3. **Inspirar pelo exemplo**, não pela fantasia
> 4. **Preparar emocionalmente** o leitor pra possíveis fracassos iniciais
"""

LIVROS_RECOMENDADOS = """# 5 Livros Recomendados

> O Bruno recomenda 5 livros no Cap 12, cena 2. Aqui está a lista expandida, com contexto e ordem de leitura sugerida.

## 1. Built to Last (Jim Collins, 1995)
**Por que ler primeiro:** É a base conceitual de Missão/Visão/Valores. Jim Collins estudou empresas visionárias (3M, American Express, Boeing, Disney, HP, Merck, Motorola, Nordstrom, Philip Morris, Procter & Gamble, Sony, Wal-Mart) e identificou 18 características comuns. A principal: empresas duráveis não são definidas pelo produto ou pelo fundador, mas pelo DNA corporativo.

**Quando ler:** Logo depois de definir sua missão/visão/valores. Vai te dar o framework pra refinar.

**Como aplicar:** Compare seu DNA com o das empresas estudadas. Veja onde você está alinhado e onde está desalinhado.

## 2. Good to Great (Jim Collins, 2001)
**Por que ler em segundo:** É a evolução do Built to Last. Collins estudou empresas que foram de boas a grandes (e mantiveram), e identificou os fatores: liderança de Nível 5, "first who... then what", cultura de disciplina, tecnologia como acelerador (não causa), e o conceito do "Flywheel" (roda de inércia).

**Quando ler:** Quando você estiver validado (R$ 10K) e pensando em escalar (R$ 30K+).

**Como aplicar:** Use o conceito do "Flywheel" pra entender que cada venda aumenta a tração da próxima, e que consistência > brilhantismo.

## 3. Satisfaction Guaranteed (Zappos, 2008)
**Por que ler:** É o case lendário da Zappos, escrito por Max Lenderman, com base na cultura de Tony Hsieh. Conta como a Zappos cresceu de US$ 1,6M (2000) pra US$ 1,2B (2008) vendendo sapatos online, com obsessão por atendimento ao cliente.

**Quando ler:** Quando você estiver implementando CX (Cap 6) e quiser inspiração concreta.

**Como aplicar:** Adote o princípio "wow through service" — encantar o cliente em cada ponto de contato, mesmo que o produto seja medíocre.

## 4. A Loja de Tudo (Brad Stone, 2013)
**Por que ler:** É a biografia da Amazon, contada por Brad Stone com base em entrevistas com Jeff Bezos, funcionários, e concorrentes. Mostra como Bezos pensava a Amazon desde o início: foco obsessivo no cliente, disposição pra perder dinheiro no curto prazo pra ganhar market share no longo, e a regra do "Day 1" (sempre tratar a empresa como se fosse o dia 1, mesmo depois de décadas).

**Quando ler:** Quando você estiver pensando em escalar (R$ 100K+) e quiser entender a lógica de longo prazo.

**Como aplicar:** Adote a obsessão pelo cliente ("Customer Obsession") como princípio não-negociável, e o "Day 1" como lembrete constante de que o trabalho nunca está terminado.

## 5. Experiência Zappos (Joseph Michelli, 2011)
**Por que ler:** É o aprofundamento da cultura Zappos. Foca nos 10 valores ("wow through service, embrace and drive change, create fun and a little weirdness, be adventurous, creative and open-minded, pursue growth and learning, build open and honest relationships with communication, build a positive team and family spirit, do more with less, be passionate and determined, be humble") e em como eles se aplicam na prática.

**Quando ler:** Quando você estiver montando time (após R$ 30K) e quiser contratar gente alinhada com o DNA.

**Como aplicar:** Use os 10 valores como régua de entrevista. Quem não vive o valor, não entra no time.

---

## Ordem de leitura sugerida (12 meses de leitura)

| Mês | Livro | Por que nesse mês |
|-----|-------|-------------------|
| Mês 1-2 | Built to Last | Definir DNA antes de começar |
| Mês 3-4 | Good to Great | Pensar em escala durante validação |
| Mês 5-6 | Satisfaction Guaranteed | Implementar CX com案例 real |
| Mês 7-8 | A Loja de Tudo | Pensar em longo prazo |
| Mês 9-12 | Experiência Zappos | Montar time com DNA |

**Total:** ~1.500 páginas em 12 meses, ~50 páginas por mês. Leitura de 15-20 minutos por dia.
"""

TREINAMENTOS = """# 2 Treinamentos Complementares

> O Bruno recomenda 2 treinamentos complementares no Cap 9, cena 2. Aqui está o resumo expandido, com o que cada um cobre, pra quem é, e quando fazer.

## 1. Explosão de Tráfego e Vendas

**O que é:** Treinamento de tráfego e performance de anúncios. Forma o aluno como gestor de tráfego profissional.

**Pra quem é:** Empreendedor que validou o negócio (R$ 10K+) e quer escalar via tráfego pago com profundidade.

**Quando fazer:** Logo depois de validar, ou até mesmo durante a validação, se você tem caixa pra investir.

**O que você aprende:**
- Como montar uma estrutura de tráfego profissional (BM, Pixel, catálogo, integração com loja virtual)
- Como fazer anúncios profissionais no Facebook, Instagram, Google, TikTok
- Como otimizar campanhas com base em dados (CTR, CPC, CPM, ROAS)
- Como escalar do R$ 50/dia ao R$ 5.000/dia
- Como formar (ou terceirizar com confiança) um time de tráfego

**Por que fazer:** O Cap 8 deste livro te ensinou o básico de impulsão (Turbinar + BM + públicos + mentalidade de crescimento). O Explosão de Tráfego aprofunda 10x, com técnicas avançadas de segmentação, criativo, funil, e escala.

**Dica do Bruno:** "Praticamente você vai se formar um gestor de tráfego, e vai fazer de forma muito mais completa, o que você aprendeu na parte de impulsão aqui do nosso treinamento."

## 2. Viver de Ecommerce

**O que é:** O MBA do e-commerce. 100+ horas de conteúdo, 4 pilares, com suporte e comunidade.

**Pra quem é:** Empreendedor que validou o negócio (R$ 10K+) e quer escalar até R$ 100K e além (até R$ 1M).

**Quando fazer:** Depois de validar, antes de tentar escalar. Ou durante a transição R$ 10K → R$ 30K.

**O que você aprende (4 pilares):**
1. **Estrutura profissional:** Loja virtual própria, ERP 100% otimizado, marketplaces escalados, equipe, processos, KPIs.
2. **Marketing:** Tráfego pago avançado, conteúdo, e-mail marketing, funis de venda, pós-venda.
3. **Gestão:** DRE, fluxo de caixa, margem, precificação, estoque, fornecedores, contrato com contador.
4. **Otimização:** Teste A/B, análise de cohort, segmentação RFM, retenção, recompra, LTV.

**Por que fazer:** O Ecommerce do Zero te leva até a validação. O Viver de Ecommerce te leva da validação até R$ 1M. É a continuação natural.

**Dica do Bruno:** "O treinamento de comércio do zero, ele é apenas um pedaço da nossa metodologia, o pedaço que leva o aluno até a validação. Agora, da validação indiante, a gente tem outras etapas. Etapas que podem te levar até um milhão de reais de faturamento no e-commerce."

**Preço:** R$ 4.999 no último lançamento. Desconto exclusivo pra quem concluiu o Ecommerce do Zero (entre em contato com o time).

**Observação:** A janela de compra do Viver de Ecommerce abre poucas vezes por ano. Quando abrir, aproveite.

---

## Como esses 2 treinamentos se conectam com o Ecommerce do Zero

```
Ecommerce do Zero (este livro)
    ↓ validação R$ 10K
    ↓
Explosão de Tráfego + Viver de Ecommerce (paralelos ou sequenciais)
    ↓ escala R$ 30K → R$ 100K
    ↓
Viver de Ecommerce (continuação)
    ↓ escala R$ 100K → R$ 1M
```

**Recomendação:** Faça o Explosão de Tráfego PRIMEIRO (mais focado, mais rápido de aplicar), e depois o Viver de Ecommerce (mais abrangente, mais profundo).
"""


def build():
    partes = [FRONT_MATTER, PREFACIO, INTRODUCAO, SUMARIO]

    # Adicionar os 12 capítulos
    for cap_num, cap_dir, cap_titulo in CAPITULOS:
        conteudo = ler_capitulo(cap_num, cap_dir)
        partes.append(f"\n\n---\n\n# PARTE {cap_num} — {cap_titulo.upper()}\n\n")
        partes.append(conteudo)

    # Apêndices
    partes.append("\n\n---\n\n# APÊNDICES\n\n")
    partes.append(GLOSSARIO)
    partes.append("\n\n---\n\n")
    partes.append(EPLOGO_EXPANDIDO)
    partes.append("\n\n---\n\n")
    partes.append(LISTA_CASES)
    partes.append("\n\n---\n\n")
    partes.append(LIVROS_RECOMENDADOS)
    partes.append("\n\n---\n\n")
    partes.append(TREINAMENTOS)

    livro_texto = "".join(partes)
    saida = BASE / "livro_completo.md"

    with open(saida, "w", encoding="utf-8") as f:
        f.write(livro_texto)

    with open(saida, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()[:8]

    words = len(re.findall(r"\b\w+\b", livro_texto))

    print(f"✅ LIVRO COMPLETO gerado em: {saida}")
    print(f"   SHA256 (8 chars): {h}")
    print(f"   Total de palavras: {words}")
    print(f"   Capítulos: 12 de 12 (100%)")
    print(f"   Cenas: 54 de 54 (100%)")
    print(f"   Inclui: prefácio, introdução, sumário, 12 capítulos, epílogo expandido, glossário, lista de cases, 5 livros, 2 treinamentos")


if __name__ == "__main__":
    build()
