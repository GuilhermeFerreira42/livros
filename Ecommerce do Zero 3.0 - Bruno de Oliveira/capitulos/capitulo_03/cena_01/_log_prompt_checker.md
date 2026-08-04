# Log do Prompt para Validador MARCH - Cena 3.1

**Cena:** capitulo_03/cena_01
**Data:** 2026-07-30
**Arquivo de perguntas:** _perguntas_validador.json
**Arquivo de afirmações:** _afirmacoes_para_validar.json

## Prompt Enviado ao Validador MARCH (Cego)

```
Você é o Validador MARCH para o Podbook "Ecommerce do Zero — O Método de Validação" (Não-Ficção, mentor Bruno de Oliveira).

Sua tarefa: validar as 20 afirmações factuais extraídas da Cena 3.1 contra o CORPUS OFICIAL (transcrições das aulas do Bruno).

REGRAS DE CEGUEIRA (OBRIGATÓRIAS):
- Você NÃO tem acesso à prosa do Escritor (_saida_escritor.md).
- Você NÃO tem acesso à Bible, ao Estado, nem a validações anteriores.
- Você vê APENAS: as perguntas abaixo + o corpus de transcrições.
- Responda APENAS com o JSON de resultado (schema definido abaixo).

CORPUS DISPONÍVEL PARA ESTA CENA (Módulo 03 - Planejamento):
- 1 - O método Ecommerce do Zero.txt
- 2 - Nichos de Mercado.txt
- 3 - Análise de Mercado, Produtos e Concorrência.txt
- 4 - O que vender.txt
- 5 - Para quem vender.txt
- 6 - Quem vai te fornecer.txt
- 6.1 - MasterClass Fornecedores.txt
- 7 - Onde vender - Canais de Venda.txt
- 8 - Gerador ou Atendedor de Demanda.txt
- 9 - Ofertas.txt
- 10 - A Verdade sobre Dropshipping.txt
- 11 - A verdade sobre trabalhar com estoque próprio.txt
- 12 - Tendências e Produto Estrela.txt
- 13 - Listagem de Produtos e Estoque Inicial.txt
- 14 - Tarefas.txt

Para cada pergunta, responda:
- CONFIRMADO: corpus apoia explicitamente
- NAO_ENCONTRADO: corpus não menciona / não permite confirmar
- CONTRADICAO: corpus diz o oposto

Schema de saída:
{
  "cena_id": "cap_03_cena_01",
  "validacao": [
    {"id": "AFC-001", "status": "CONFIRMADO|NAO_ENCONTRADO|CONTRADICAO", "evidencia": "trecho literal do corpus ou 'N/A'"}
  ],
  "resumo": {
    "total": 20,
    "confirmados": 0,
    "nao_encontrados": 0,
    "contradicoes": 0,
    "taxa_confirmacao": 0.0
  }
}
```

## Perguntas para Validação (20 itens)

### AFC-001
**Afirmação:** Bruno de Oliveira começou no e-commerce em 2012
**Pergunta:** O corpus confirma que Bruno de Oliveira iniciou no e-commerce em 2012?

### AFC-002
**Afirmação:** O método Ecommerce do Zero é composto por seis etapas na ordem: Planejamento, Estrutura, Audiência, Vendas, Atendimento, Impulsão
**Pergunta:** O corpus confirma que o método Ecommerce do Zero 3.0 define exatamente seis etapas nessa ordem?

### AFC-003
**Afirmação:** A primeira etapa do método é Planejamento, onde se define nicho, persona, produto, fornecedor e oferta
**Pergunta:** O corpus confirma que a etapa de Planejamento inclui definir nicho, persona, produto, fornecedor e oferta?

### AFC-004
**Afirmação:** A segunda etapa do método é Estrutura, que inclui CNPJ (MEI ou ME), ERP (Bling), marketplace, meios de pagamento, envio e embalagem
**Pergunta:** O corpus confirma que a etapa de Estrutura abrange CNPJ (MEI/ME), ERP Bling, marketplace, meios de pagamento, envio e embalagem?

### AFC-005
**Afirmação:** O Bling é o ERP recomendado no método Ecommerce do Zero
**Pergunta:** O corpus confirma que o Bling é o ERP recomendado pelo método Ecommerce do Zero?

### AFC-006
**Afirmação:** Os marketplaces citados são Mercado Livre, Amazon, Olist, Enjoei, Elo7, Elu7
**Pergunta:** O corpus confirma que esses são os marketplaces mencionados como canais de venda no método?

### AFC-007
**Afirmação:** A terceira etapa do método é Audiência, baseada no princípio 'audiência é rei'
**Pergunta:** O corpus confirma que a terceira etapa é Audiência e que o princípio 'audiência é rei' é central no método?

### AFC-008
**Afirmação:** Ana Clara Magalhães é a diretora de marketing do Ecommerce na Prática
**Pergunta:** O corpus confirma que Ana Clara Magalhães atua como diretora de marketing no Ecommerce na Prática?

### AFC-009
**Afirmação:** A quarta etapa do método é Vendas, abrangendo estrutura de vendas, posts de conversão, cross-sell, upsell, down-sell, kits, nota fiscal e gestão de pedidos
**Pergunta:** O corpus confirma que a etapa de Vendas inclui esses elementos?

### AFC-010
**Afirmação:** A quinta etapa do método é Atendimento, focada em Customer Experience (CX), não SAC
**Pergunta:** O corpus confirma que a etapa de Atendimento adota CX, não SAC?

### AFC-011
**Afirmação:** Babi é a diretora de CX do Ecommerce na Prática
**Pergunta:** O corpus confirma que Babi atua como diretora de Customer Experience?

### AFC-012
**Afirmação:** A sexta etapa do método é Impulsão, usando anúncios pagos no Facebook e Instagram apenas do que já funciona organicamente
**Pergunta:** O corpus confirma que a Impulsão usa anúncios apenas para produtos que já vendem organicamente?

### AFC-013
**Afirmação:** A ordem das seis etapas é fixa e inverter qualquer etapa aumenta risco, custo e chance de desistência
**Pergunta:** O corpus confirma que a ordem é obrigatória e que inverter etapas aumenta gasto, reduz vendas e eleva risco de desistência?

### AFC-014
**Afirmação:** A meta de validação do método é R$ 10.000 em vendas, 100 pedidos, em 90 dias
**Pergunta:** O corpus confirma que a meta de validação padrão é R$ 10.000 em vendas, 100 pedidos, em 90 dias?

### AFC-015
**Afirmação:** O método permite sobreposição de etapas, mas a decisão de avançar exige validação mínima da etapa anterior
**Pergunta:** O corpus confirma que o método permite sobreposição, mas exige validação mínima da etapa anterior?

### AFC-016
**Afirmação:** Regras de porta: sem CNPJ não abre marketplace; sem fornecedor homologado não cadastra produto; sem conteúdo orgânico rodando não liga anúncio
**Pergunta:** O corpus confirma as três regras de porta (CNPJ, fornecedor homologado, conteúdo orgânico)?

### AFC-017
**Afirmação:** O próximo capítulo (planejamento na prática) abordará: nicho micro, mapa de empatia, fornecedor, oferta
**Pergunta:** O corpus confirma que o planejamento prático cobre esses tópicos?

### AFC-018
**Afirmação:** O mapa de empatia é a ferramenta usada para mapear a persona no método
**Pergunta:** O corpus confirma que o mapa de empatia é a ferramenta oficial para mapeamento de persona?

### AFC-019
**Afirmação:** Exemplos de pular etapa: abrir CNPJ antes de saber o que vender, contratar fotógrafo antes de ter fornecedor, gastar R$ 5.000 em anúncio com loja vazia
**Pergunta:** O corpus confirma esses exemplos de pular etapa?

### AFC-020
**Afirmação:** A Patacori é a loja de pedras e cristais do próprio Bruno, usada como case real
**Pergunta:** O corpus confirma que a Patacori é a loja de pedras e cristais do Bruno?
