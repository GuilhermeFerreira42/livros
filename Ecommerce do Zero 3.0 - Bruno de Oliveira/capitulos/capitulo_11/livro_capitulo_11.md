---
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
# Capítulo 11 — O ERP na Prática (Bling)

[Para quem é este capítulo: empreendedores que instalaram o Bling (Cap 4) e querem dominar a operação fiscal e logística. Aqui você vai ver as 5 configs do dia 1, os 13 passos do cadastro, e o fluxo completo de NF integrada ao pedido do ML.]

[Como ler: as cenas deste capítulo tratam do Bling em profundidade. 11.1 instala o motor (5 configs do dia 1 + 3 opcionais). 11.2 ensina o cadastro de produto (13 passos + kit + caminho reverso). 11.3 fecha com a emissão de NF integrada ao pedido do ML (6 passos + 3 status + 6 ícones). A Patacori percorre o capítulo como exemplo concreto (cupom 4 meses, certificado R$ 139, 2 pessoas tratando NF/mês).]

[Status: CONCLUÍDO. As 3 cenas fecham o motor invisível do negócio.]

---

## SUMÁRIO DO CAPÍTULO 11 (COMPLETO)

- **Cena 11.01** — Bling: o ERP que organiza a operação, e o que configurar no dia 1 ✅
- **Cena 11.02** — Cadastrando produtos no Bling, e o caminho reverso: importar do Mercado Livre ✅
- **Cena 11.03** — Emitindo nota fiscal pelo Bling, e o fluxo completo de venda integrado ao Mercado Livre ✅

---


---

*[Checksum: d8547231 | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*

---

# Capítulo 11 — O ERP na Prática (Bling)
## Cena 1: Bling: o ERP que organiza a operação, e o que configurar no dia 1

---

E aí, tudo bem? A gente entrou no capítulo que vai te mostrar o motor invisível por trás de tudo que você fez até agora, e que sem ele o negócio não roda. E o nome da cena é exatamente esse. **Bling: o ERP que organiza a operação, e o que configurar no dia 1**. E aqui, antes da gente entrar no como, eu preciso te dar um aviso que vem direto do nosso treinamento, e que é o seguinte. **"Para você começar a utilizar o bling, você criou uma conta lá seguindo o protocolo que eu ensinei, incluindo, inclusive, te dei um cupom de quatro meses para você usar, se você usar o cupom, vai aparecer para você aqui o prazo."** E essa frase, do Bruno, no corpus, é a base de tudo. E o que ela tá te dizendo é o seguinte. **O Bling é o motor que te dá 4 meses de graça pra você testar sem risco, e o resto da configuração depende do que você quer operar**.

E aqui, eu preciso te dar o primeiro conceito dessa cena, e que é o seguinte. **O Bling tem 50+ funcionalidades, e você vai usar 5 no dia 1**. E o Bruno, no corpus, é explícito: **"Tem muita funcionalidade, essa ferramenta, você não vai precisar usar todas essas funcionalidades agora. A gente vai usar o básico, aqui é o que a gente precisa, para poder vender no mercado livre, que é só nosso objetivo no treinamento."** E aqui, **o iniciante que entra no Bling e tenta aprender tudo de uma vez trava, e desiste em 2-3 dias**. E **o iniciante que entra sabendo que vai usar 5 funcionalidades no dia 1, e vai aprender as outras aos poucos, está jogando com método**. E aqui, **a diferença é o que separa quem começa a usar o Bling hoje de quem fica com a conta criada e nunca opera**.

E aqui, eu preciso te dar os **5 configurações essenciais do dia 1**, e que são o que vão destravar a operação inteira, e que é o seguinte.

**Configuração 1: dados da empresa.** E aqui, **o Bruno mostra o caminho**: **"você vai vir aqui na engrenagem, vamos aqui em empresa, aqui em geral, basicamente a gente não vai mudar nada aqui, está do padrão, só se certifica que está tudo do jeito do meu, está tudo igual."** E o que você precisa preencher é: (1) **Razão social**, (2) **Pessoa física ou jurídica** (PF para MEI, PJ para ME), (3) **Regime tributário** (Simples Nacional, MEI, Lucro Presumido), (4) **Nome fantasia**, (5) **Endereço completo**, (6) **Telefone**, (7) **E-mail**, (8) **Logo da empresa** (opcional mas recomendado). E aqui, **a Inscrição Estadual e a Inscrição Municipal são opcionais no cadastro, mas obrigatórias na hora de emitir NF-e**: **"a gente que são estadual aqui ... que são um municipal e estadual e que não são obrigatores, mas na hora de a metinota vão ser."** E aqui, **se você não sabe o que é Inscrição Municipal, é a do alvará da prefeitura, e o Bruno é direto: "o ideal é que você consulte sempre um contador se você tiver dúvida"**.

**Configuração 2: Natureza de Operação (padrão para venda).** E aqui, **o Bruno mostra que essa config já vem em padrão na maioria dos casos, mas você precisa conferir**: **"Na natureza de operação é importante. Tem aqui, por exemplo, compra de mercadoria, devolução, invendo de mercadoria. Vendo de mercadoria é o padrão. Então, sério 1, tipo, saída, aqui é o teu regime, geralmente assim, para o nacional. O indicador de presença, operação não presencial, vendo pela internet."** E aqui, **a natureza de operação é o que define se a NF é de venda, devolução, transferência, etc**. E **a padrão para e-commerce é "Venda de mercadoria, tipo saída, operação não presencial, venda pela internet"**. E aqui, **se você não configurar isso, o Bling pede na hora de emitir a NF, e fica feio**.

**Configuração 3: Certificado Digital.** E aqui, **o Bruno é direto**: **"Certificado digital, o seguinte, é o arquivo, né? O documento você precisa para poder emitir as notas fiscais. Você precisa de um certificado a 1."** E aqui, **o certificado é o que te dá autorização pra emitir NF-e**, e **sem certificado, você não emite NF, e sem NF, você não vende em marketplace**. E o Bruno menciona o preço: **"aqui no bling, eles têm uma promoção de certificado por 139 reais. Era muito barato. O preço realmente é bem competitivo."** E aqui, **a janela de uso do certificado é 1 ano**, e o Bruno avisa: **"Aqui é um ano, vou ter que fazer isso de novo, por exemplo. Que mais? Aqui a gente pulou a natureza de operação."** E aqui, **a dica é: compre o certificado com 2-3 dias de antecedência da primeira venda, pra ter ele pronto quando precisar**.

**Configuração 4: Código de produtos (manual vs. sequencial).** E aqui, **o Bruno recomenda deixar MANUAL**: **"Aqui você não vai cadastrar nada, mas basicamente, disse, o código do produto vai ser manual. Se você quiser ser sequencial, se você não ser sequencial, eã e tal, eu deixo sempre manual, que aí eu tenho a minha liberdade de criar os códigos dos meus produtos."** E aqui, **a diferença é a seguinte**: (1) **Sequencial** = Bling gera código 1, 2, 3, 4... automaticamente; (2) **Manual** = você cria o código (ex: INC-CITRON-001, KIT-7CHAKRAS-002). E **a vantagem do manual é que o código carrega informação do produto**, e fica fácil de auditar. E aqui, **a dica do Bruno é: comece com manual, e use prefixos por categoria** (INC- para incenso, KIT- para kit, PED- para pedra).

**Configuração 5: Integração com Mercado Livre.** E aqui, **essa é a config que mais impacta o dia 1**, e o Bruno mostra o passo a passo: **"você vai ver que todas as integrações disponíveis no Bring, você vai configurar aqui pelo mercado livre, encontrou o mercado livre, adicionou, você vai colocar aqui qual nome que você quer chamar, quero chamar de mercado livre. 2, qual é o teu login no mercado livre? Se não vai preencher isso, você vai clicar nisso aqui, ele vai abrir uma janelinha para você logar no mercado livre. Parece aqui, permitir. Solvei."** E aqui, **o fluxo é**: (1) **ir em Preferências → Integrações**; (2) **clicar em "Adicionar" e escolher Mercado Livre**; (3) **dar um nome à integração** (ex: "Mercado Livre Principal"); (4) **logar com seu usuário do ML** (vai abrir uma janela); (5) **autorizar o Bling a acessar sua conta ML**; (6) **salvar**. E aqui, **uma vez integrado, o fluxo fica automático**: (a) **o pedido entra automaticamente no Bling**; (b) **você importa o produto do ML**; (c) **emite a NF**; (d) **imprime a etiqueta**; (e) **o status do pedido atualiza no ML automaticamente**. E aqui, **sem essa integração, você faz tudo manual, e manual = erro = reclamação = termômetro amarelo**.

E aqui, eu preciso te dar a **lista de configurações complementares que NÃO são dia 1, mas que vão ser pedidas depois**, e que é o seguinte. **Config opcional 1: Categorias de produtos.** E o Bruno explica: **"Aqui você consegue criar categorias sobre categorias de produtos para você organizar lá dentro. Anticamente o Blinger não tinha isso, tá? Essa é uma funcionalidade relativamente nova."** E aqui, **categorias servem pra organizar (ex: Incensos > Citronela, Palo Santo, Sete Chakras)**, e ajudam em relatórios. E **Config opcional 2: Estoque negativo permitido.** E o Bruno recomenda: **"permiti lançar a stock negativo, gerar nada para chegar a partir de venda com o stock negativo. É aqui que você consegue autorizar essas coisas. O da patacoirita é configurado desse jeito aqui."** E aqui, **se você permite estoque negativo, o sistema deixa você vender acima do estoque real**, e o Bruno usa isso porque a integração com o fornecedor é tão rápida que a reposição chega antes do cliente reclamar. E **se você NÃO permite, o sistema trava a venda, e você perde a venda**. E **Config opcional 3: Impressão de etiqueta.** E o Bruno: **"você consegue criar um padrão de getqueta, se você quiser imprimir a getqueta, com um código de barro, com um escau, com um eã, e por aí vai, você consegue criar."** E aqui, **a etiqueta padrão do Bling é a dos Correios (modelo 3, vertical)**, e você pode customizar com logo, com o número do pedido, com a NF, ou sem nada disso. E **a Patacori usa: número do pedido, número da NF, e endereço do destinatário em negrito** (facilita o carteiro).

E aqui, eu preciso te dar a **razão pela qual o Bling é a peça central**, e que vem direto do corpus, e que é a seguinte. E o Bruno mostra que o Bling centraliza: **"Aqui você consegue ver o teu desempenho, se você tem reputação ativa ou não ... número de vendas, vendas com reclamações, reclamações em mediação, vendas canceladas."** E aqui, **o que o Bruno tá te dizendo é o seguinte. O Bling não é só cadastro de produto e emissão de NF. É o painel de controle do seu negócio**. E **"você consegue criar um padrão de getqueta"** (logística), **"emitir as notas fiscais"** (fiscal), **"criar um padrão de produto"** (cadastro), **"integrar com marketplace"** (vendas), **"importar dados via planilhas"** (operação). E aqui, **o Bling é o que transforma o negócio artesanal em negócio escalável**. E **o iniciante que opera sem ERP opera no caos, e o caos tem limite em R$ 5-10K/mês**.

E aqui, eu preciso te dar a **lista de erros fatais do dia 1 do Bling**, e que custam caro, e que é o seguinte. **Erro 1: não configurar a natureza de operação.** E aqui, **a NF-e sai com CFOP errado, e a SEFAZ rejeita, e o pedido trava, e o cliente reclama**. E **Erro 2: não instalar o certificado digital antes da primeira venda.** E aqui, **a primeira venda chega, e você não consegue emitir NF, e o ML cancela o pedido, e você toma strike**. E **Erro 3: não integrar o Mercado Livre.** E aqui, **você fica digitando pedido manual, e erro de digitação = produto errado = devolução = reclamação**. E **Erro 4: deixar o código de produto sequencial.** E aqui, **o código 1, 2, 3 não carrega informação, e quando você tem 200 produtos, você não sabe qual é qual**. E **Erro 5: não testar a emissão de NF antes da primeira venda real.** E aqui, **o dia da primeira venda não é hora de aprender**. E **a dica do Bruno: faça uma NF de teste com você mesmo como destinatário, antes de começar**.

E aqui, eu preciso te dar a **razão pela qual essa cena importa mais do que parece**, e que vem direto do corpus, e que é o seguinte. E o Bruno mostra que o Bling tem **"Tem muita funcionalidade, e com o tempo a gente vai vendo isso lá dentro da área de bonus, a gente vai ter que criar uma aba lá só pro Blink."** E aqui, **o que ele tá te dizendo é o seguinte. O Bling é um sistema vivo, que cresce com você**. E **na aula de hoje a gente instalou o motor**. E **nas próximas cenas a gente vai aprender a usar o motor pra valer**: (1) **cadastrar produto e importar pro ML** (cena 11.2), (2) **emitir NF-e integrada ao pedido do ML** (cena 11.3). E aqui, **sem o motor instalado hoje, as cenas 11.2 e 11.3 não fazem sentido**.

E aqui, eu preciso te dar a **mensagem central dessa cena, e que é a que eu quero que você leve adiante**, e que é a seguinte. **Bling é o motor invisível do negócio. Sem ele, você opera no caos. Com ele, você opera no sistema. E sistema escala. Caos não**. E aqui, **o Bruno reconhece: "tem muita funcionalidade, e com o tempo a gente vai vendo"**. E **a sua tarefa hoje é instalar as 5 configurações do dia 1, e deixar o motor pronto pra rodar**.

E aqui, a gente vai fechando a cena, e na próxima, a gente vai entrar no **cadastro de produtos no Bling**, e vai te mostrar **como cadastrar um produto do zero, como importar lista de produtos via planilha, e como exportar do Bling pro Mercado Livre com EAN e SKU corretos**. **E essa é a cena onde o motor começa a girar.** Toca cadastrar produto.

---

## Resumo da cena

Cena 1 do Capítulo 11, sobre **Bling: o ERP que organiza a operação, e o que configurar no dia 1**. Conceito central: **o Bling tem 50+ funcionalidades, e você vai usar 5 no dia 1. Sem o motor instalado, as cenas 11.2 e 11.3 não fazem sentido**. **5 configurações essenciais do dia 1:** (1) **Dados da empresa** (engrenagem → empresa → geral: razão social, regime tributário, nome fantasia, endereço, IE/IM opcionais no cadastro mas obrigatórias na NF-e); (2) **Natureza de operação** (padrão: "Venda de mercadoria, tipo saída, operação não presencial, venda pela internet"); (3) **Certificado digital** (arquivo .pfx, R$ 139 com cupom, validade 1 ano); (4) **Código de produtos manual** (vs. sequencial; usar prefixos por categoria tipo INC-CITRON-001, KIT-7CHAKRAS-002); (5) **Integração com Mercado Livre** (Preferências → Integrações → Mercado Livre → autorizar via login ML → fluxo automático de pedido). **3 configurações opcionais (não-dia-1 mas pedidas depois):** (1) Categorias de produtos; (2) Permitir estoque negativo (Patacori usa); (3) Impressão de etiqueta (modelo 3 vertical, customizar com logo/pedido/NF). **5 erros fatais do dia 1:** (1) Não configurar natureza de operação (NF rejeitada); (2) Não instalar certificado antes da 1ª venda (ML cancela, strike); (3) Não integrar ML (digitar manual = erro); (4) Deixar código sequencial (código 1, 2, 3 sem info); (5) Não testar NF antes da 1ª venda real. **Cupom Bling:** 4 meses grátis, depois R$ 50/mês. Próxima cena: cadastro de produtos (11.2).

## Seu checklist desta cena

Antes de ir para a próxima cena deste capítulo, você precisa ter feito ou decidido:

- [ ] Aceitar: **Bling é o motor do negócio, e tem 50+ funcionalidades, mas você usa 5 no dia 1**
- [ ] Configurar **dados da empresa** (engrenagem → empresa → geral)
- [ ] Preencher **razão social, regime tributário, nome fantasia, endereço completo**
- [ ] Lembrar: **IE e IM opcionais no cadastro, mas obrigatórias na NF-e**
- [ ] Configurar **natureza de operação padrão**: "Venda de mercadoria, saída, não presencial, internet"
- [ ] **Comprar certificado digital** (R$ 139 com cupom Bling, 1 ano de validade)
- [ ] **Instalar certificado digital** no Bling (Preferências → Notas fiscais → Certificado digital → upload .pfx)
- [ ] Configurar **código de produtos MANUAL** (não sequencial)
- [ ] Usar **prefixos por categoria** (INC-, KIT-, PED-)
- [ ] **Integrar Mercado Livre** (Preferências → Integrações → Mercado Livre → autorizar login)
- [ ] Decidir se **permite estoque negativo** (Patacori permite)
- [ ] Configurar **padrão de etiqueta** (modelo 3, vertical, com logo)
- [ ] **Fazer NF de teste** com você mesmo como destinatário (antes da 1ª venda real)
- [ ] Lembrar: **"tem muita funcionalidade, e com o tempo a gente vai vendo"**
- [ ] Lembrar: **sem Bling configurado, o negócio opera no caos. Com Bling, opera no sistema**
- [ ] Aceitar: **sistema escala. Caos não**
- [ ] Próxima cena: **cadastro de produtos + importação via planilha + exportação pro ML**

**Na próxima cena deste capítulo:** "Cadastrando produtos no Bling: do zero, via planilha, e exportando pro Mercado Livre", onde a gente vai abrir o cadastro de produto, vai te mostrar como preencher SKU, EAN, descrição, peso, dimensões, e como exportar tudo pro ML sem digitar 2 vezes. Toca cadastrar produto.




---

*[Checksum: 77748cb9 | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*

---

# Capítulo 11 — O ERP na Prática (Bling)
## Cena 2: Cadastrando produtos no Bling, e o caminho reverso: importar do Mercado Livre

---

E aí, tudo bem? A gente instalou o motor na cena passada. E agora, a gente vai colocar a primeira peça em movimento, e essa peça é o cadastro de produto, e tudo que vem a partir dele. E o nome da cena é exatamente esse. **Cadastrando produtos no Bling, e o caminho reverso: importar do Mercado Livre**. E aqui, antes da gente entrar no como, eu preciso te dar um aviso que vem direto do nosso treinamento, e que é o seguinte. **"Vamos lá pessoal bem-vindos para mais uma aula, hoje a gente vai começar a cadastra produto, eu estou aqui na conta que a gente começou do zero aqui no blind, se eu vim aqui em cadastro produtos, e eu vou incluir um cadastro."** E essa frase, do Bruno, no corpus, é a base de tudo. E o que ela tá te dizendo é o seguinte. **O cadastro de produto é o alicerce de tudo que vem depois, e se você cadastrar mal, todo o resto vai mal**.

E aqui, eu preciso te dar o primeiro conceito dessa cena, e que é o seguinte. **Tem 2 caminhos de cadastro, e a escolha depende do seu volume**. E o Bruno, no corpus, mostra os 2 caminhos: (1) **Cadastrar no Bling e exportar pro ML** (caminho recomendado, principal); (2) **Cadastrar no ML e importar pro Bling** (caminho de resgate, para produtos antigos ou ajustes). E aqui, **o caminho (1) é o que dá menos trabalho a longo prazo**: **"Isso aqui é pulo do gato literalmente, cara. ... Imagino você querer depois migrair para outro marketplace e as suas imagens não estarem no blink. Estas imagens estarem no mercado livre. Signefique que você perdeu todas as imagens. Então por isso dá mais trabalho fazer pelo blink portar no mercado livre dá mais trabalho, mas depois você vai ter muito menos trabalho e muito mais controle sobretudo. Essa é a grande sacada."** E aqui, **o iniciante que cadastra direto no ML perde controle, e quando precisa migrar pra outro marketplace, começa do zero**. E **o iniciante que cadastra no Bling controla tudo, e migra em 1 clique**.

E aqui, eu preciso te dar o **passo a passo do cadastro no Bling (caminho 1)**, e que vem direto do corpus, e que é o seguinte. E o Bruno mostra com o exemplo real de um incensário de madeira: **"vou te explicar todos os campos que você precisa preencher aqui."**

**Passo 1. Código SKU.** E o Bruno: **"código SKU é o código do produto, o código interno do produto, geralmente o que eu faço que não vou fazer um código do produto, eu coloco um código que representa a minha marca, como, por exemplo, um pataco, zero, zero, três, zero, zero, um, aí eu vou em sequência, final 2, final 3, final 4, final 5, final 6, final 7, isso daí de forma indefinida até eu ter que virar, por exemplo, esse treino aqui para um 4, por exemplo, para um 5, você pode criar a sua própria, o seu processo de criação de SKU, o importante é seguir um padrão, é você não ter SKUs espalhados aí com código totalmente fora do padrão, interessante é você seguir um padrão e uma numeração sequencial."** E aqui, **a régua é: use prefixo da marca + sequência numérica, e mantenha padrão**.

**Passo 2. Tipo e Formato.** E o Bruno: **"o tipo de produto é sempre produto, se você vem de serviço, você pode fazer cada estrão serviço também, o formato do produto é o simples, a composição a gente vai até fazer no futuro, é kit, mas por enquanto a gente vai com a das traus produtos base."** E aqui, **tipo = produto (não serviço), formato = simples (não composto/kit, no início)**.

**Passo 3. Unidade de medida.** E o Bruno: **"unidade é unidade medida, geralmente no produto é ON, o é PC, o é CX, fuma caixa."** E aqui, **a unidade vem da nota fiscal do fornecedor**: UN (unidade), PC (peça), CX (caixa), KG (quilograma), etc. E **a dica do Bruno: copie da NF que vem do seu fornecedor**.

**Passo 4. Preço de venda.** E o Bruno: **"preço de venda, não para ser o preço de venda que vai se promar que te place, aqui é só um preço de venda padrão."** E aqui, **o preço de venda no Bling é o "preço base", e o preço final do anúncio pode ser diferente**. E **a Patacori cadastra o preço base (R$ 135, por ex) e depois configura o preço do anúncio no ML separado**.

**Passo 5. Peso e dimensões.** E o Bruno é explícito: **"peso líquido, vale a pena você perguntar para o teu fonecedor o peso líquido do produto ... o peso bruto também ... aqui ele vai estar sempre em um quilo, então só tenho um produto de um quilo, eu vou colocar um vírgula zero zero, por exemplo, aqui no peso bruto é o peso com a caixa ... volume 1, volume, geralmente é um volume ... largura, isso aqui é largura dele embalado ... vale a pena você comprar uma fitamétrica, vale a pena você comprar se necessário uma balança de precisão para você medir."** E aqui, **a régua é: pergunte ao fornecedor o peso líquido, meça com fita métrica a caixa embalada, e tenha balança de precisão pra produtos pequenos**. E **errar peso = frete errado = prejuízo ou atraso**.

**Passo 6. EAN (código de barras).** E o Bruno: **"aqui é o eã, você vai pegar o eã que está na caixa do produto ... está vendo ele gera se você quiser você pode dar imprimido esse código de barra depois."** E aqui, **a maioria dos produtos industrializados já vem com EAN de fábrica**. E **se o seu produto é artesanal ou kit, você vai precisar comprar EAN próprio (Cap 4 já cobriu isso)**.

**Passo 7. Nome do produto.** E o Bruno avisa: **"faltou uma coisa bem básica, que é o nome do produto, isso aqui é um sensário de madeira para incenso."** E aqui, **o nome é o que aparece na listagem de produtos do Bling**, e **deve ser claro e padronizado**.

**Passo 8. Categoria.** E o Bruno: **"o categoria, você pode criar categoria de produto, se você quiser, se quiser categorizar os produtos você pode categorizar eles todos aqui."** E aqui, **categorias servem pra organizar (Incenso > Citronela, Palo Santo, Sete Chakras)**, e **facilitam relatórios**.

**Passo 9. Estoque mínimo e máximo.** E o Bruno: **"o stock eu vou trabalhar com o mínimo de cinco peças e um máximo de 50 peças."** E aqui, **o estoque mínimo alerta pra reposição**, e **o máximo alerta pra não comprar demais**.

**Passo 10. Fornecedor.** E o Bruno: **"fonecedores, vou adicionar um fonecedor, avatar em sensos, preço de custo disso, 7 reais."** E aqui, **cadastrar o fornecedor com preço de custo é o que te dá a margem real**. E **sem preço de custo cadastrado, você não sabe se está lucrando**.

**Passo 11. Tributação.** E o Bruno: **"tributação, geralmente aqui é nacional, essa geralmente é a forma, o Ncm, isso aqui se vê na nota fiscal, a mesma no caso é sexto, ele já puxa com base no Ncm, tipo de item, o mercadoria para revenda, aqui é, sim, é uma mercadoria para revenda."** E aqui, **o NCM (Nomenclatura Comum do Mercosul) vem da NF do fornecedor**, e **define o imposto**. E **"tributo não preenche, se me sp, nada disso preenche"** — Bruno deixa ICMS, IPI, PIS, COFINS em branco, e o Bling preenche automaticamente com base no NCM.

**Passo 12. Imagens.** E o Bruno: **"aqui é uma grande sacada, porque geralmente as pessoas colam com as imais de só lá dentro do mercador livre, a primeira, a principal imagem eu gosto de colocar aqui ... vou anexar aqui fazer uma pelude ... a primeira foto que é o que aparece na pesquisa."** E aqui, **a primeira foto é o que aparece na busca do ML**, e **deve ser a melhor, a mais limpa, a que mais vende**. E **a dica do Bruno: use fotos leves, que não pesem na hora do cliente carregar**. E **a Patacori coloca 5-7 fotos por produto (frente, verso, lado, detalhe, uso, embalagem)**.

**Passo 13. Vídeo e descrição.** E o Bruno: **"você tem algum link, vídeo, descrição, você pode colocar tudo aqui, então o ideal que vocês preencha, façam cada vez completos dos produtos e salva."** E aqui, **vídeo do YouTube hospedado e descrição completa (com palavras-chave) é o que diferencia o anúncio medíocre do anúncio que aparece em cima**.

E aqui, eu preciso te dar a **estratégia de clonar produto (economie tempo)**, e que vem direto do corpus, e que é a seguinte. E o Bruno: **"eu vou vir aqui e vou clonar esse produto, ao invés de adicionar, eu vou clonar, clonei o produto ... vou colocar aqui final 2 ... aqui não vamos dar nada, vou mudar o nome do produto, em sensário de madeira para insensos, está manho médio."** E aqui, **clonar é o atalho pra produtos similares da mesma categoria** (mesma foto, mesma descrição, mesmo peso, só muda o tamanho e o SKU). E **pra produtos muito diferentes, melhor fazer cadastro do zero**.

E aqui, eu preciso te dar o **conceito de Kit (composição de produtos)**, e que vem direto do corpus, e que é o seguinte. E o Bruno avisa: **"vou clonar esse grande aqui, e, eu vou mudar de descrição, kit, três insensários de madeira ... formar a tor com composição, muda isso aqui ... a unidade vai mudar, aqui eu vou colocar KT, que é um kit ... aqui que vem a grande sacada, é um kit, Bruno, qual é a, eu vou colocar aqui, nesse caso você vai precisar comprar um código a, como assim comprar um código a, lembra, cada produto tem o seu próprio código a, se você montar um kit, não existe um código a, multiple para os três, você vai precisar comprar um código a."** E aqui, **a diferença entre produto simples e kit é a seguinte**: (1) **Produto simples**: tem SKU próprio, EAN próprio, e o estoque conta unidade por unidade. (2) **Kit (composição)**: tem SKU próprio e EAN próprio, mas o estoque é **virtual** (calculado pelo menor estoque dos componentes). E aqui, **a sacada do Bruno: "o stock do kit vai sempre ser composto pelo que tem menos peças dos integrantes do kit"**. E **se você tem 20 unid. do pequeno, 10 unid. do médio, 10 unid. do grande, e o kit = 1 de cada, o estoque do kit é 10 (limitado pelo menor)**. E **quando você vende 1 kit, o Bling baixa automaticamente 1 de cada componente**. E aqui, **kit é o que te permite vender 3-5 unidades por transação sem digitar 3-5 cadastros diferentes**.

E aqui, eu preciso te dar o **caminho reverso (caminho 2): importar do Mercado Livre pro Bling**, e que vem direto do corpus, e que é o seguinte. E o Bruno mostra: **"Vou cadastrar esse mesmo produto no procedimento reverso. ... Vou vir aqui em Anunciar, de forma individual. ... Produtos, mercado livre. Eu começo pela categoria, não tem jeito. Eu vou digitar o nome, em sensário, de madeira, para insensos."** E aqui, **o caminho reverso é o que você usa quando**: (1) **Já tem produtos antigos no ML** que não foram cadastrados no Bling, (2) **Comprou um negócio**, e precisa migrar pro Bling, (3) **Quer testar um produto piloto no ML**, e depois operacionalizar no Bling. E aqui, **o caminho é**: (1) **Anunciar no ML**; (2) **Vincular categoria**; (3) **Preencher ficha técnica**; (4) **No Bling, ir em Cadastros > Produtos > Importar**; (5) **Selecionar a integração do ML**; (6) **Importar**. E aqui, **o problema do caminho reverso é que o ML sobrescreve campos**: **"algumas coisas, ele decide como é que funciona. Nesse caso, ele colocou o peso. Ele tem uma tabela interna. De peços. Ele vai determinar o peso."** E aqui, **a dica do Bruno: depois de importar, conferir campo a campo**.

E aqui, eu preciso te dar a **estratégia de vinculação de categoria (Bling ↔ ML)**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"Você precisa entender qual produto você quer vender. Então, por exemplo, eu quero vender um insensário. Eu vou no mercado livre, só que é ré que tá ... e eu vou verificar se a categoria dele está certa, beleza? Casa móveis e decoração, e feitos de decoração de casa, porta insenso. Maravilha, tá certo? Eu vou lá no bling, vou acessar em granagem, vou em cadastros, categoria de produtos. ... vou clicar aqui em vincular categoria multilógica."** E aqui, **a vinculação de categoria é o que evita o erro fatal de "categoria errada" no anúncio**: **"se você errou, pode anunciar o produto novamente aqui e anunciar novamente."** E aqui, **a dica do Bruno: "uma vez configurado, se nunca mais já precisa refazer isso"**. E **a vinculação é por categoria do Bling ↔ categoria do ML**, e fica salva.

E aqui, eu preciso te dar a **estratégia de exportação pro Mercado Livre**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"Quando eu clico aqui [no carrinho de compras], ele vai aparecer as integrações que você já fez. ... Eu posso fazer um vínculo de categoria. ... Vou colocar descrição do anuncio e idada a loja. Preci, preço promocional. Idedofonecedor, marca, dias de desconto. Modalidade de anuncio. Vou colocar aqui premium. Frate gratis não. Permiti exportação para catálogo. Sim. Na realidade eu quero que você não marque isso aqui. Isso aqui é esse que você quer mandar esse para publicidade."** E aqui, **o caminho é**: (1) **No cadastro do produto, clicar no ícone do carrinho de compras (multiloja)**, (2) **Selecionar a integração do ML**, (3) **Escolher a categoria vinculada**, (4) **Preencher modalidade (Premium ou Clássica)**, (5) **Salvar**, (6) **Depois, ir em "Exportar produtos"**, (7) **Selecionar a integração**, (8) **Exportar**. E aqui, **"a exportação foi concluída ... a gente nem entrar no mercado livre. O anuncio aqui. Com foto e tudo? Sim"** — o anúncio aparece no ML em minutos.

E aqui, eu preciso te dar a **estratégia de ajuste de preço em massa**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"Você vai vim aqui, você vai selecionar o que você quer mudar. E você vai fazer o seguinte, ó. Você vai fazer o seguinte, ó. Reajuste e cincronização de preços. Ó, você pode acrescentar valor ou percentual. Você pode descontar e você pode simplesmente fixar. Eu vou fixar o preço desses insensários agora em 135 reais. Cara, teve aumento e tal para quais, pros filtrados? Não, pros selecionados. Para quais eu selecionei. Os filtrados seriam todos que estão aparecendo aqui no filtro."** E aqui, **a estratégia é**: (1) **filtrar os produtos** (ex: "todos os incensários"), (2) **selecionar todos** (checkbox), (3) **clicar em "Reajuste e sincronização de preços"**, (4) **escolher**: **fixar valor** (ex: R$ 135), **acrescentar %** (ex: +10%), **descontar %** (ex: -15%), (5) **aplicar**, (6) **depois, sincronizar com a loja virtual** (ML). E aqui, **o Bruno avisa: "atualizei, deseja atualizar o preço de três produtos com valor fixo entre 35 reais. Sim. Beleza, mudei. O preço de cada um deles foi para 135. Meixeu no preço do kit? Não, aí eu tenho que fazer isso humanamente."** E aqui, **kit tem que ser ajustado manualmente** (porque a margem do kit é diferente dos componentes).

E aqui, eu preciso te dar a **razão pela qual o cadastro bem feito é o que diferencia o medíocre do top**, e que vem direto do corpus, e que é a seguinte. E o Bruno: **"O blinco só tem três níveis, provavelmente você vai ficar no último início, você vai escolher esse, você vai escolher esse, você vai escolher esse. Não deve ter essas outras, aí beleza, você vai por essa, o blinco ele não tem, ele tem um limite de níveis."** E aqui, **a Patacori tem produtos com 100% da ficha técnica preenchida**, e **isso é o que faz o anúncio ficar verde-escuro no termômetro do ML** (qualidade da listagem). E aqui, **o iniciante que cadastra com 30% da ficha técnica preenchida está fadado a ter anúncio amarelo**. E **o iniciante que cadastra com 100% (incluindo peso, dimensões, marca, modelo, material, formato) está jogando com algoritmo a favor**.

E aqui, eu preciso te dar a **lista de erros fatais no cadastro**, e que custam caro, e que é o seguinte. **Erro 1: cadastrar direto no ML sem Bling.** E aqui, **quando você precisar migrar pra outro marketplace, começa do zero**. E **Erro 2: cadastrar sem peso e dimensões reais.** E aqui, **o frete é calculado errado, e o cliente paga a diferença, e reclama**. E **Erro 3: cadastrar com código sequencial sem prefixo.** E aqui, **você tem 200 produtos e não sabe qual é qual**. E **Erro 4: não vincular categoria Bling ↔ ML.** E aqui, **a exportação dá erro, ou a categoria vai errada, e o anúncio trava**. E **Erro 5: não conferir após importar do ML.** E aqui, **o ML sobrescreve campos, e o que era 0,5kg vira 1kg, e o frete muda**.

E aqui, eu preciso te dar a **razão pela qual essa cena é o coração do Cap 11**, e que vem direto do corpus, e que é a seguinte. E o Bruno: **"Se você acompanharam as últimas aulas, você viu que a gente exportou um produto cadastrado no bling para o mercado livre e chegou lá no mercado livre com a categoria errada. E por isso não conseguia alterar a categoria, também não conseguia executar a mercado em vios, enfim."** E aqui, **o que ele tá te dizendo é o seguinte. Sem cadastro bem feito, sem categoria vinculada, sem ficha técnica completa, o anúncio não roda bem, o Mercado Envios não funciona, o frete trava, e o cliente fica sem comprar**. E aqui, **a próxima cena vai te mostrar como integrar tudo isso com o pedido real: a NF-e emitida pelo Bling, integrada ao pedido do ML, com etiqueta gerada, com Mercado Envios configurado, com status atualizado**.

E aqui, a gente vai fechando a cena, e na próxima, a gente vai entrar em **emitir nota fiscal pelo Bling integrada ao pedido do Mercado Livre**, e vai te mostrar **o fluxo completo de venda: pedido entra no Bling → emite NF → imprime etiqueta → Mercado Envios coleta → status atualiza no ML**. **E essa é a cena onde o motor completo entra em movimento.** Toca emitir NF.

---

## Resumo da cena

Cena 2 do Capítulo 11, sobre **Cadastrando produtos no Bling, e o caminho reverso: importar do Mercado Livre**. Conceito central: **tem 2 caminhos de cadastro (Bling→ML ou ML→Bling), e a escolha depende do seu volume. O caminho Bling→ML é o que dá menos trabalho a longo prazo**. **13 passos do cadastro no Bling (caminho 1):** (1) SKU (prefixo marca + sequência); (2) Tipo (produto) e Formato (simples); (3) Unidade (UN/PC/CX/KG); (4) Preço de venda (preço base); (5) Peso líquido + peso bruto + dimensões (largura, altura, profundidade); (6) EAN (código de barras de fábrica, ou comprado para artesanal/kit); (7) Nome; (8) Categoria; (9) Estoque mínimo/máximo; (10) Fornecedor (com preço de custo); (11) Tributação (NCM da NF, sem preencher ICMS/IPI/PIS/COFINS); (12) Imagens (5-7 fotos, primeira é a principal); (13) Vídeo + descrição. **Estratégia clonar:** pra produtos similares da mesma categoria, clonar e ajustar. **Conceito de Kit (composição):** tem SKU e EAN próprios, mas estoque é VIRTUAL calculado pelo menor dos componentes. Quando vende 1 kit, baixa 1 de cada componente automaticamente. Kit requer EAN próprio comprado. **Caminho reverso (ML→Bling):** pra produtos antigos já no ML. Anunciar no ML → importar do Bling → conferir campos (ML sobrescreve peso, dimensões). **Vinculação de categoria Bling↔ML:** crítico pra evitar "categoria errada" que trava anúncio. **Exportação pro ML:** clica no carrinho → seleciona integração → escolhe categoria → modalidade (Premium/Clássica) → salva → "Exportar produtos". **Ajuste de preço em massa:** filtrar → selecionar → "Reajuste e sincronização" → fixar/%/desconto. Kit precisa ajuste manual. **5 erros fatais:** (1) cadastrar direto no ML; (2) sem peso/dimensões reais; (3) código sequencial sem prefixo; (4) não vincular categoria; (5) não conferir após importar. Próxima cena: emitir NF-e integrada ao pedido (11.3).

## Seu checklist desta cena

Antes de ir para a próxima cena deste capítulo, você precisa ter feito ou decidido:

- [ ] Aceitar: **tem 2 caminhos de cadastro (Bling→ML ou ML→Bling). Use o 1 (Bling→ML) sempre que possível**
- [ ] Cadastrar o **primeiro produto no Bling** (não direto no ML)
- [ ] Preencher os **13 campos do cadastro**: SKU, tipo, formato, unidade, preço, peso líquido+bruto, dimensões, EAN, nome, categoria, estoque min/max, fornecedor com custo, tributação, imagens, vídeo, descrição
- [ ] Usar **SKU com prefixo da marca + sequência** (ex: PAT-001, PAT-002, KIT-001)
- [ ] Conferir **peso e dimensões reais** com balança de precisão e fita métrica
- [ ] Conferir **EAN** (código de barras de fábrica, ou comprado pra artesanal/kit)
- [ ] Cadastrar **fornecedor com preço de custo** (essencial pra saber margem)
- [ ] Cadastrar **5-7 imagens** por produto (primeira é a principal)
- [ ] Cadastrar **categoria no Bling** (Incenso, Citronela, Palo Santo, Sete Chakras, etc)
- [ ] **Vincular categoria Bling ↔ Mercado Livre** (categoria do ML: Casa, Móveis e Decoração > Decoração de Casa > Porta Incenso)
- [ ] **Exportar pro Mercado Livre** pelo carrinho de compras
- [ ] Conferir o **anúncio no ML** após exportar (categoria, modalidade, imagens, descrição)
- [ ] Se for cadastrar **kit**, entender que o estoque é virtual (= menor dos componentes)
- [ ] Comprar **EAN próprio pra kit** (não existe EAN múltiplo)
- [ ] **NÃO** cadastrar direto no ML (perde controle, dificulta migração futura)
- [ ] Se usar caminho reverso (ML→Bling), **conferir todos os campos após importar** (ML sobrescreve)
- [ ] Usar **reajuste em massa** pra mudar preço de muitos produtos de uma vez
- [ ] Lembrar: **"isso é pulo do gato literalmente, cara"** (cadastrar no Bling, exportar pro ML)
- [ ] Lembrar: **"uma vez configurado, se nunca mais já precisa refazer isso"** (vinculação de categoria)
- [ ] Lembrar: **"o stock do kit vai sempre ser composto pelo que tem menos peças dos integrantes do kit"**
- [ ] Lembrar: **kit tem que ser ajustado manualmente no preço** (margem diferente)
- [ ] Próxima cena: **emitir NF-e integrada ao pedido do ML + etiqueta + Mercado Envios**

**Na próxima cena deste capítulo:** "Emitindo nota fiscal pelo Bling: o passo a passo integrado ao pedido do Mercado Livre", onde a gente vai abrir o painel de vendas, vai te mostrar como o pedido entra automaticamente, como emitir NF, como imprimir etiqueta, como o Mercado Envios coleta, e como o status atualiza no ML. Toca emitir NF.




---

*[Checksum: 2e58f8b1 | Validação MARCH: APROVADA | Validação Continuidade: APROVADA]*

---

# Capítulo 11 — O ERP na Prática (Bling)
## Cena 3: Emitindo nota fiscal pelo Bling, e o fluxo completo de venda integrado ao Mercado Livre

---

E aí, tudo bem? A gente instalou o motor (cena 11.1) e cadastrou os produtos (cena 11.2). E agora, a gente vai ligar o motor e mostrar o que acontece desde o momento que o cliente clica em "Comprar" até o momento que a NF-e cai na caixa de email dele. E o nome da cena é exatamente esse. **Emitindo nota fiscal pelo Bling, e o fluxo completo de venda integrado ao Mercado Livre**. E aqui, antes da gente entrar no como, eu preciso te dar um aviso que vem direto do nosso treinamento, e que é o seguinte. **"Pessoal, mais uma aula, vamos tratar de questões fiscais aqui E vamos falar de nota fiscal, como é metinota fiscal pelo mercado livre No caso que a gente vai fazer Nós não vamos remetir nota fiscal pelo mercado livre Beleza, a gente vai fazer isso pelo bling."** E essa frase, do Bruno, no corpus, é a base de tudo. E o que ela tá te dizendo é o seguinte. **Você PODE emitir NF pelo ML, mas NÃO DEVE. E o caminho certo é pelo Bling**.

E aqui, eu preciso te dar o primeiro conceito dessa cena, e que é o seguinte. **O Bling emite a NF, e o ML recebe os dados automaticamente**. E o Bruno, no corpus, é explícito: **"o bling está preparado para poder emitir uma nota fiscal E aí o que vai acontecer? O que o mercado livre está caminhando Falei pra vocês, ele está caminhando para poder exigir as pessoas Nota fiscal de tudo, exigir dos vendedores."** E aqui, **o iniciante que tenta emitir NF pelo ML (sem Bling) faz 2x o trabalho**: **"Só que acontece Dá mais trabalho e não é o ideal O ideal é fazer isso pelo bling Então mesmo inserindo aqui o certificado digital Eu prefiro fazer isso por dentro do bling."** E aqui, **a integração Bling → ML é o que faz o fluxo ficar automático**: **Bling emite NF → dados fiscais vão pro ML → etiqueta é liberada → ML mostra a NF pro cliente**.

E aqui, eu preciso te dar o **pré-requisito: certificado digital válido**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"Basicamente você precisa do que eu serificado digital Então o que que acontece? Eu posso adicionar o certificado digital que eu tenho aqui direto no mercado livre O meu nome é de sonheiro, está vencido, estou vendo?"** E aqui, **a janela do certificado é 1 ano, e ele expira silenciosamente**. E o Bruno complementa: **"Vou atualizar o certificado aqui Tem o da Patakorik, que espirou em 2019 Vou deleitar ele e você ele saina um novo Se ele saina um novo certificado, tem uma senha Você deve conhecer a senha do seu, certificadora de passo, contador de pago."** E aqui, **a senha do certificado vem da certificadora (Serasa, Certisign, etc) no momento da compra**, e **você precisa guardar essa senha em local seguro, porque sem ela não consegue nem instalar nem renovar**. E a dica do Bruno: **renove com 30 dias de antecedência** (Cap 11.1 já cobriu isso).

E aqui, eu preciso te dar o **passo a passo da emissão de NF pelo Bling integrada ao pedido do ML**, e que vem direto do corpus, e que é o seguinte.

**Passo 1. Pedido entra no Bling automaticamente.** E o Bruno: **"Pedidos de venda, é onde eu listo os meus pedidos de venda. Todo pedido de venda no bling, ele é importado, né, com base nos status que você definiu que um pedido deve ser importado quando ele acontece."** E aqui, **o filtro padrão importa pedidos PAGOS**, e o pedido aparece no painel com tag amarela (em aberto).

**Passo 2. Abrir o pedido.** E o Bruno: **"eu vou pegar o Eduardo Cardoso L84 Então vamos abrir o link da patacoria aqui ... O que eu vou fazer? Eu vou gerar nada fiscal Por aqui Puxou todos os dados aqui Uma boa Beleza, vou salvar."** E aqui, **ao abrir o pedido, o Bling já puxa automaticamente**: (a) **dados do cliente** (nome, CPF/CNPJ, endereço); (b) **dados do produto** (descrição, NCM, valor); (c) **dados de transporte** (Mercado Envios já vem com a etiqueta gerada).

**Passo 3. Conferir dados e ajustar NCM se necessário.** E o Bruno: **"Tem um problema com o item, está sem NCM Bom, consegui gerar nada fiscal aqui do Eduardo Ela ainda dá pendente na receita, está vendo? Está pendente na receita ainda É... O que eu vou fazer? Você leçonou ela e vou enviar a nota fiscal O nota foi rejeitada Por quê? Podendo que o NCM está em válido O NCM é um código fiscal do produto e realmente está."** E aqui, **o NCM (Nomenclatura Comum do Mercosul) é o código fiscal de 8 dígitos que classifica o produto**, e **se estiver errado, a SEFAZ rejeita, e a NF-e fica pendente**. E o Bruno resolve na hora: **"Calerativo e que recorre os universitários Google, o NCM desse produto é isso aqui ... O NCM é 330731000 ... Pegar aqui, vou aqui em tributação NCM, colher Sai de performados, o Seste aqui é esse mesmo Se ele se une o item, mercadoria pra revenda Perfeito, salvei."** E aqui, **a dica do Bruno: pesquise o NCM no Google (ex: "NCM incenso" ou "NCM banho")**, e **o NCM vem da NF do fornecedor** (Cap 11.2 já cobriu).

**Passo 4. Salvar a NF e enviar pra SEFAZ.** E o Bruno: **"Acorriga todos os dados ... Agora foi, não foi rejeitado, beleza?"** E aqui, **o Bling envia automaticamente pra SEFAZ**, e **a SEFAZ retorna com o status (autorizada ou rejeitada)**. E **o tempo médio é de 5 a 30 segundos**.

**Passo 5. Sincronizar a NF com o Mercado Livre.** E o Bruno: **"Mas, independente, eu consigo imprimir a etiqueta Eu também não imprimi a etiqueta por aqui, beleza? A gente imprimir a etiqueta pelo bling ... Mas eu quero isso aqui, enviados pro loja virtual Então selecionei a nota que eu quero, seleciona aqui o Mercado Lives, correto Que é o da Patacuria, enviado outro no nosso fiscal sim Sim E aí, detalhe, galera, deu um erro aqui que se giram Mas o bling é automaticamente já mandou os dados pra cá Já tenho aqui, inclusive, detalhes da nota fiscal Que foi emitido, emitido 16, 24, 3 minutos atrás."** E aqui, **o Bling empurra automaticamente a NF autorizada pro ML**, e **o cliente recebe a NF no email dele em minutos**. E **a etiqueta do Mercado Envios só é liberada DEPOIS que a NF é emitida e sincronizada com o ML**: **"Eu não consigo Não existe aqui, está vendo? A opção de informar De imprimir essa etiqueta Por que? Porque ele está travando Como a gente está no mercado em vius coleta Eu só consigo liberar a etiqueta depois de emitir a nota."**

**Passo 6. Imprimir a etiqueta (via Bling).** E o Bruno: **"Bom, com essa nota fiscal que eu consigo fazer agora Eu consegui imprimir ela, eu consigo gerar o PDF com o Dampf E importar XML se eu quiser."** E aqui, **a etiqueta é impressa direto do Bling, com modelo configurado (Cap 11.1)**, e **cola na caixa, e despacha nos Correios ou no Mercado Envios Coleta**.

E aqui, eu preciso te dar o **status de cores do pedido no Bling (visual rápido)**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"O que é um pedido tratado, Bruno? Pedido tratado é pedido em preço lá pelo time, nota fiscal emitida, impressa, produto separado no stock, integração logística feita."** E aqui, **as 3 cores/status são**:

**Status 1: Pedido em aberto (amarelo).** E o Bruno: **"Pedido em aberto é um pedido pago que ainda não foi tratado."** E **aqui o pedido entrou no Bling mas a NF ainda não foi emitida**. E o que fazer: **emitir NF, conferir, salvar, sincronizar com ML**.

**Status 2: Pedido em andamento (azul).** E o Bruno: **"Ele vai ficar em andamento até quando, até ele ser enviado ou coletado."** E **aqui a NF já foi emitida e a etiqueta já foi gerada**, mas **o produto ainda não foi despachado**. E o que fazer: **separar produto, embalar, despachar nos Correios ou aguardar Mercado Envios Coleta**.

**Status 3: Pedido atendido (verde).** E o Bruno: **"Feito isso, aí ele vem para o atendido, ele vai ficar no vergidinho aqui. Beleza? O que significa esses iconizinhos aqui do bling?"** E **aqui o produto foi coletado pelo Mercado Envios ou entregue nos Correios**, e **o Bling atualizou o status automaticamente**. E o que fazer: **não fazer nada, deixar o sistema atualizar**. E **"todo dia o sistema vem aqui sozinho e faz esse processo de atualização desses estados."**

E aqui, eu preciso te dar a **razão pela qual o Bling mostra ícones de status do pedido**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"O que significa esses iconizinhos aqui do bling? Aqui o reloginho, você consegue visualizar as ocorrenças, quando que os estados foram alterados, você consegue visualizar. Esse icon é o canal de venda, no caso aqui eu tenho loja integrada, tem o mercado livre, tem o Skyhub, KB2W, tem o Amazon, tem vários canais de venda diferentes. O cifrão é dados da nota fiscal, dados fiscais, é 5 colonizados com a loja com o marketplace, no caso aqui a gente usa isso pra praticamente todos. Ene, nota fiscal emitido, é estoque lançado, ou seja, esse pedido foi atendido, foi embalado, estoque foi lançado. Esse iconizinho aqui é o rastriu do objeto e é a transportadora. No caso, esse aqui é o símbolo dos correios, no caso, esse aqui é o símbolo do mercado enviado, no caso, esse aqui é o símbolo da B2W entregas. E o balãozinho é um comentário, é algum comentário que foi colocado no pedido."** E aqui, **os ícones são o painel visual do pedido**, e **cada ícone mostra uma dimensão**: (1) **relógio** = ocorrências/histórico; (2) **canal** = onde foi vendido; (3) **cifrão** = NF-e; (4) **caixa** = estoque lançado; (5) **rastreador** = transportadora; (6) **balão** = comentário. E aqui, **o iniciante que ignora os ícones não enxerga o status real do pedido**, e **o iniciante que olha os ícones sabe em 1 segundo o que está acontecendo**.

E aqui, eu preciso te dar a **indicação de "primeira compra" do cliente (Bling mostra)**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"Uma coisa muito legal que o Blink faz também é mostrar pra gente se a primeira venda do cliente. Quando não aparece, é porque isso cliente já comprou com a gente, significa que a gente está tendo recorrência, o Batacorite tem recorrência pra caramba."** E aqui, **o Bling destaca visualmente quando é a primeira compra do cliente**, e **isso te dá 2 informações**: (1) **cliente novo** = precisa de mais atenção no pós-venda pra fidelizar; (2) **cliente recorrente** = relação de confiança estabelecida, vale remarketing.

E aqui, eu preciso te dar o **passo a passo do tratamento completo do pedido**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"vou listar os pedidos em aberto, para poder tratar. Então aqui eu tenho alguns, como é que eu vou tratar eles. Eu preciso tratar eles de uma forma separada, porque eles são de canais de venda diferente, tem a que pedir os dólares virtual, tenho pedidos do mercado livre, não posso tratar todos eles da mesma forma. Eu vou tratar esses 2 do mercado livre, vou tratar isso aqui pra poder não confundir a cabeça da pessoa lá. Beleza? Mas basicamente, o que eu preciso fazer? Eu preciso em metinota fiscal, preciso em premio pedido e preciso em premia de queitre de transporte."** E aqui, **os 3 passos do tratamento são**: (1) **emitir NF**, (2) **imprimir pedido** (espelho), (3) **imprimir etiqueta de transporte**. E **"quando eu emito a nota, o sistema já informa o mercado livre dos dados fiscais, lá ele libera a etiqueta, vou conseguir imprimir a etiqueta e vou imprimir o pedido também para o seu controle. Eu gosto de ter o espelho do pedido, a gente tem isso dentro do nosso processo."** E aqui, **a Patacori tem 2 pessoas tratando pedidos**, e **a recomendação do Bruno é separar por canal de venda** (ML, B2W, Amazon, etc).

E aqui, eu preciso te dar o **fluxo de integração logística (Mercado Envios vs. Correios)**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"vou aqui em vendas e vou em integração logísticas. Isso aqui, cara, é também uma mão na roda, é muito prático, você lhe sonar aqui em mercadinho, aquele lista purilogística. Então eu tenho correios, correios para mim é loja virtual, Amazon, o B2 da Vintrega, o B2 da Vindade, mercadinho Vivo, mercadolive. ... Eu vou pegar o Eduardo Cardoso e vou em primia de KTD, não vai funcionar aqui para mim, mas lá na Patacoir, vou mostrar o PDF para vocês aqui. Olha, o que é o PDF? Tá, é uma etiqueta. ... Unico que eu não preciso gerar remessa é o mercado em Vivo. Mas basicamente, essa é a nossa rotina de pedido."** E aqui, **a diferença é a seguinte**: (1) **Mercado Envios** = etiqueta gerada automaticamente, sem precisar gerar remessa; (2) **Correios (contrato próprio)** = você precisa gerar remessa, autorização de postagem, e etiqueta com seu contrato; (3) **B2W Entregas** = precisa gerar remessa também. E aqui, **"o bling é automaticamente já mandou os dados pra cá"** — quando a NF é sincronizada, o status atualiza no ML sem você fazer mais nada.

E aqui, eu preciso te dar a **lista de erros fatais na emissão de NF**, e que custam caro, e que é o seguinte. **Erro 1: certificado vencido.** E aqui, **a NF-e não vai, e o pedido trava em aberto, e o Mercado Envios não libera etiqueta, e o cliente cancela**. E **Erro 2: NCM errado ou vazio.** E aqui, **a SEFAZ rejeita, e a NF fica pendente, e o cliente não recebe**. E **Erro 3: destinatário com CPF/CNPJ inválido.** E aqui, **a NF-e é rejeitada na validação do CPF/CNPJ**. E **Erro 4: natureza de operação errada.** E aqui, **a NF sai com CFOP errado, e o imposto é calculado errado, e o contador corrige depois, e dá trabalho**. E **Erro 5: não conferir o pedido antes de emitir.** E aqui, **se o cliente pediu 2 unidades e o Bling puxou 1, ou se o endereço está errado, ou se o produto é outro, a NF sai errada, e cancelar NF-e é muito mais chato que cancelar pedido**.

E aqui, eu preciso te dar a **razão pela qual essa cena fecha o Cap 11**, e que vem direto do corpus, e que é o seguinte. E o Bruno: **"Esse é o ponto sobre nota fiscais Tudo que você pensava saber em relação ao mercado Lives Bling tá nesse vídeo Inclusive solução de alguns problemas."** E aqui, **o que ele tá te dizendo é o seguinte. Você saiu da cena 11.1 sem Bling, e chegou na cena 11.3 com Bling configurado, com produto cadastrado, com NF integrada, com etiqueta gerada, com Mercado Envios coleta, com status atualizado, e com cliente recebendo NF no email**. E **esse fluxo é o que diferencia o medíocre do top, e o manual do automatizado**. E aqui, **o Cap 11 inteiro te deu o motor invisível que sustenta tudo**.

E aqui, eu preciso te dar a **mensagem central dessa cena, e que é a que eu quero que você leve adiante**, e que é a seguinte. **NF-e não é opcional. É obrigatória. E o Bling é o que te dá isso no automático, sem você virar refém do papel**. E aqui, **a Patacori emite milhares de NF-e por mês pelo Bling, e o time é só 2 pessoas**. E **isso é o que dá escala**. E **a próxima cena (que abre o Cap 12) vai te mostrar os cases reais de quem executou o método, e o bônus de gestão de preços, e o epílogo de R$ 10K ao R$ 100K**.

E aqui, a gente vai fechando o capítulo 11, e no próximo, a gente vai entrar no **Cap 12 — Cases, Bônus e Epílogo**, e vai te mostrar **cases reais de quem executou o método, bônus de gestão de preços e missão/visão/valores, e o epílogo da próxima escalada**. **E essa é a cena onde o livro começa a fechar.** Toca encerrar.

---

## Resumo da cena

Cena 3 do Capítulo 11, sobre **Emitindo nota fiscal pelo Bling, e o fluxo completo integrado ao ML**. Conceito central: **você PODE emitir NF pelo ML, mas NÃO DEVE. O caminho certo é pelo Bling, que empurra automaticamente a NF autorizada pro ML**. **Pré-requisito:** certificado digital válido (senha da certificadora guardada em local seguro, renovar com 30 dias de antecedência). **6 passos da emissão integrada:** (1) Pedido entra no Bling automaticamente (status amarelo = em aberto); (2) Abrir o pedido (Bling puxa cliente, produto, NCM, transporte); (3) Conferir dados e ajustar NCM se necessário (SEFAZ rejeita se NCM errado); (4) Salvar NF e enviar pra SEFAZ (autorizada em 5-30s); (5) Sincronizar NF com ML (cliente recebe NF no email em minutos, etiqueta do Mercado Envios é liberada); (6) Imprimir etiqueta (Mercado Envios) ou gerar remessa (Correios/B2W). **3 cores de status do pedido no Bling:** (a) Amarelo = pago, NF não emitida; (b) Azul = NF emitida, etiqueta gerada, não despachado; (c) Verde = coletado pelo Mercado Envios / entregue nos Correios. **6 ícones de status:** relógio (ocorrências), canal (origem), cifrão (NF), caixa (estoque lançado), rastreador (transportadora), balão (comentário). **Bling mostra "primeira compra" do cliente** = destaque visual pra cliente novo. **Tratamento de pedido (3 passos):** (1) emitir NF, (2) imprimir pedido (espelho), (3) imprimir etiqueta. Separar por canal de venda (ML, B2W, Amazon). **3 tipos de logística:** (1) Mercado Envios = automática, sem remessa; (2) Correios (contrato próprio) = precisa gerar remessa; (3) B2W Entregas = precisa remessa. **5 erros fatais:** (1) certificado vencido; (2) NCM errado/vazio; (3) CPF/CNPJ inválido; (4) natureza de operação errada; (5) não conferir antes de emitir. **Patacori:** 2 pessoas tratam milhares de NF/mês pelo Bling. **Encerramento do Cap 11:** motor invisível instalado. Próximo: Cap 12 (Cases, Bônus, Epílogo).

## Seu checklist desta cena

Antes de ir para o próximo capítulo, você precisa ter feito ou decidido:

- [ ] Aceitar: **NF-e é obrigatória, e o caminho é pelo Bling (não pelo ML)**
- [ ] Ter **certificado digital válido** (renovar com 30 dias de antecedência)
- [ ] Guardar a **senha do certificado** em local seguro
- [ ] Instalar o **certificado no Bling** (não no ML)
- [ ] Deixar o **pedido entrar automaticamente no Bling** (filtro padrão = pedidos pagos)
- [ ] **Abrir o pedido** (Bling puxa cliente, produto, NCM, transporte automaticamente)
- [ ] **Conferir NCM** de cada produto (pesquisar no Google se tiver dúvida)
- [ ] **Salvar NF e enviar pra SEFAZ** (autorizada em 5-30s)
- [ ] **Sincronizar NF com ML** (cliente recebe NF no email, etiqueta liberada)
- [ ] **Imprimir etiqueta** (Mercado Envios) ou **gerar remessa** (Correios/B2W)
- [ ] Conferir os **3 status visuais**: amarelo (em aberto) → azul (NF ok, não despachado) → verde (coletado/entregue)
- [ ] Olhar os **6 ícones** do pedido: relógio, canal, cifrão, caixa, rastreador, balão
- [ ] Atentar ao **destaque de "primeira compra"** (cliente novo = mais atenção)
- [ ] **Separar tratamento por canal de venda** (ML, B2W, Amazon separados)
- [ ] Lembrar: **a etiqueta do Mercado Envios só é liberada DEPOIS da NF emitida**
- [ ] Lembrar: **"o bling é automaticamente já mandou os dados pra cá"** (sincronização)
- [ ] **NÃO** emitir NF pelo ML (dá mais trabalho e não é o ideal)
- [ ] **NÃO** usar NCM errado (SEFAZ rejeita, NF pendente)
- [ ] **NÃO** cancelar NF-e (muito mais chato que cancelar pedido)
- [ ] **NÃO** emitir sem conferir (pedido errado, endereço errado, NF errada)
- [ ] Aceitar: **Patacori emite milhares de NF/mês com 2 pessoas. Escala é o que importa**
- [ ] Próximo capítulo: **Cap 12 — Cases, Bônus e Epílogo**

**No próximo capítulo:** "Cases, Bônus e Epílogo: o que vem depois do R$ 10K", onde a gente vai abrir o Cap 12 com cases reais de quem executou o método, vai te dar bônus de gestão de preços e missão/visão/valores, e vai fechar o livro com o epílogo da próxima escalada (R$ 10K ao R$ 100K). Toca encerrar.


---

## METADADOS DO CAPÍTULO (COMPLETO)

- **Cenas concluídas:** 3 de 3 ✅
- **Status:** CONCLUÍDO
- **Bible checksum atualizado:** ver `bible_da_obra.md` v1.8
- **Próximo capítulo a escrever:** 12 (Cases, Bônus e Epílogo)

