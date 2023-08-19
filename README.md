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

- O sistema deve exibir um menu com as operações;
  
- Clientes devem ser cadastrados com *CPF, nome, data de nascimento e endereço completo*;
   
- Para **cadastrar uma conta corrente, é necessário vinculá-la ao CPF de um cliente já cadastrado**. O incremento no número da conta deve ser automático (número da última conta cadastrada + 1), a agência pode ser fixa em "0001", e outras informações pertinentes como saldo, limite diário de saques, etc. devem ser registradas;
  
- Deve ser possível depositar valores positivos (sem limite de valor ou número de operações);
  
- O sistema deve permitir até 3 saques por dia, sendo o valor máximo para cada saque R$ 500. Se o usuário não tiver saldo suficiente na conta, não permitir o saque;
  
- A opção extrato deve listar todas as operações de depósito e saque realizadas durante a seção, além do saldo da conta. O extrato pode ser solicitado a qualquer momento;
  
- As operações bancárias devem ser **implementadas como funções**, e deve-se explorar as diferentes formas de passagem de parâmetros em Python (`positional only`, `positional or keyword` e `keyword only`)

---
### Implementação da solução:

Para executar o [código](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/src/codigo_v2.py), baixe e extraia este repositório em sua máquina. Tendo o Python já instalado, digite no terminal (ou *prompt* de comando):

<center> `python src/codigo.py` ou `python3 src/codigo.py` </center>

<br>
O sistema exibirá o menu de opções, conforme mostrado abaixo. Caso o usuário já esteja logado, no cabeçalho serão exibidas as informações sobre a conta corrente.  


<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/menu_operacoes.png?raw=true" alt="Menu de operações" width=40%/>
</div>

<div align="center">
Figura 1 - Menu de opções 
</div>
  

<br>

Para realizar operações bancárias (depósito, saque, extrato, transferência), o usuário deve:

1. **Cadastrar um cliente**;
2. **Cadastar uma conta vinculando-a ao CPF de um cliente já cadastrado**;
3. **Selecionar uma conta já cadastrada (fazer *login*)**.  
   
<br>
Foi aplicada validação à todas as entradas de dados (*inputs*) de dados utilizando a estrutura `try... except`.

<br>  

#### Cadastrando um cliente  

Ao cadastrar um cliente, é necessário informar um CPF com 11 dígitos e uma data de nascimento válida:  

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/validacao_data_nascimento.png?raw=true" alt="Cadastrando um cliente" width=45%/>
</div>
<div align="center">
Figura 2 - **Validações no cadastro de um cliente** 
</div>

<br>

Uma verificação adicional é que o sistema não permite o cadastro de dois usuários com o mesmo número de CPF, garantindo que ele possa ser utilizado como chave primária do cadastro de clientes:

<br>
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/cadastro_cliente_erro.png?raw=true" alt="Validação CPF" width=45%/>
</div>
<div align="center">
Figura 3 - Dois clientes não podem ter o mesmo CPF. 
</div>

<br>

A opção de listar clientes mostra todos os clientes cadastrados, utilizando a biblioteca `datetime` para o cálculo da idade:

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/clientes_cadastrados.png?raw=true" alt="Lista de clientes cadastrados" width=60%/>
</div>
<div align="center">
Figura 4 - Listando os cliente cadastrados.
</div>

#### Cadastrando uma conta corrente

O número das contas correntes cadastradas é **sequencial e auto incrementado**. Por padrão, todas as contas estão vinculadas à Agência 0001. Para criar uma nova conta é necessário informar o CPF de um cliente já cadastrado no sistema (chave estrangeira):

<br>
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/cadastrar_conta_erro.png?raw=true" alt="Erro cadastro conta" width=48%/>
</div>
<div align="center">
Figura 5 - Erro ao cadastrar a conta antes de cadastrar o cliente.
</div>

<br>

Informado um CPF válido, o sistema mostra o nome cliente e solicita a confirmação da criação da conta. As demais definições da conta (número de saques por dia, limite de valor por saque, etc.) seguem o padrão definido nas regra de negócio.

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/cadastro_conta.png?raw=true" alt="Cadastrando nova conta" width=48%/>
</div>
<div align="center">
Figura 6 - Confirmação de cadastro de conta corrente.
</div>

