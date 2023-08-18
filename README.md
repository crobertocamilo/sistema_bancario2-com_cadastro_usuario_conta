## Desafio 3 do ***Potência Tech iFood* Ciência de Dados com Python**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio do [iFood](https://www.ifood.com.br/).

<div align="right">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/raw/main/assets/logo.webp" alt="logo bootcamp" width=30%/>
</div>

--- 
## Desafio - Criando um Sistema Bancário com Banco de Dados

### Objetivo

Desenvolver uma aplicação que em **Python** que possibilite o cadastramento de clientes e contas e que implemente as principais operações bancárias (depósito, saque, transferência entre contas, extrato de operações). As contas correntes devem ser vinculados ao CPF do cliente.

**Regras de negócio:**

- O sistema deve exibir um menu com as operações. 
- Clientes devem ser cadastrados com *CPF, nome, data de nascimento e endereço completo*; 
- Para **cadastrar uma conta corrente, é necessário vinculá-la ao CPF de um cliente já cadastrado**. O incremento no número da conta deve ser automático (número da última conta cadastrada + 1), a agência pode ser fixa em "0001", e outras informações pertinentes como saldo, limite diário de saques, etc. devem ser registradas;
- Deve ser possível depositar valores positivos (sem limite de valor ou número de operações);
- O sistema deve permitir até 3 saques por dia, sendo o valor máximo para cada saque R$ 500. Se o usuário não tiver saldo suficiente na conta, não permitir o saque;
- [ ] A opção extrato deve listar todas as operações de depósito e saque realizadas durante a seção, além do saldo da conta. O extrato pode ser solicitado a qualquer momento;
- [] As operações bancárias devem ser **implementadas como funções**, e deve-se explorar as diferentes formas de passagem de parâmetros em Python (`positional only`, `positional or keyword` e `keyword only`)

---
### Implementando a solução:

Para executar o [código](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/src/codigo_v2.py), baixe e extraia este repositório em sua máquina. Tendo o Python já instalado, digite no terminal (ou *prompt* de comando):

> `python codigo.py` ou `python3 codigo.py`

<br>

Será exibido o menu de operações e o usuário deve escolher uma das opções:
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/blob/main/assets/menu.png?raw=true" alt="Menu de operações" width=35%/>
</div>



<br>

Foi aplicada validação à todas as entradas de dados (*inputs*) utilizando **try... except**.

<br>

As operações de depósito e saque implementam as regras definidas nas *instruções* e solicitam a confirmação do usário para concluir a transação:

<br>
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/blob/main/assets/validacao.png?raw=true" alt="Exemplo confirmação saque" width=52%/>
</div>

<br>

A opção de extrato pode ser selecionada a qualquer momento (e várias vezes durante a seção) e exibe toda a movimentação financeira da conta:

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/blob/main/assets/extrato.png?raw=true" alt="Exemplo extrato" width=30%/>
</div>

