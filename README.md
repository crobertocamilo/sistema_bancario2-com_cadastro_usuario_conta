## Desafio 3 do ***Potência Tech iFood* Ciência de Dados com Python**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio do [iFood](https://www.ifood.com.br/).

<div align="right">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/raw/main/assets/logo.webp" alt="logo bootcamp" width=30%/>
</div>

--- 
## Desafio - Criando um Sistema Bancário com Banco de Dados

### Objetivo

Desenvolver uma aplicação que em **Python** que possibilite o cadastramento de clientes e contas e que implemente as principais operações bancárias (depósito, saque, transferência entre contas, extrato de operações). As contas correntes devem ser vinculados ao CPF do cliente.

<br>  

**Regras de negócio:**

- O sistema deve exibir um menu com as operações;
  
- Clientes devem ser cadastrados com *CPF, nome, data de nascimento e endereço completo*;
   
- Para **cadastrar uma conta corrente, é necessário vinculá-la ao CPF de um cliente já cadastrado**. O incremento no número da conta deve ser automático (número da última conta cadastrada + 1), a agência pode ser fixa em "0001", e outras informações pertinentes como saldo, limite diário de saques, etc. devem ser registradas;
  
- Deve ser possível depositar valores positivos (sem limite de valor ou número de operações);
  
- O sistema deve permitir até 3 saques por dia, sendo o valor máximo para cada saque R$ 500. Se o usuário não tiver saldo suficiente na conta, não permitir o saque;
  
- A opção extrato deve listar todas as operações de depósito e saque realizadas durante a seção, além do saldo da conta. O extrato pode ser solicitado a qualquer momento;
  
- As operações bancárias devem ser **implementadas como funções**, e deve-se explorar as diferentes formas de passagem de parâmetros em Python (`positional only`, `positional or keyword` e `keyword only`)

---
### Desenvolvimento:

O código desenvolvido está na pasta [src](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/tree/main/src) e utiliza **funções em Python** para implementar tanto os serviços principais (cadastrar cliente ou conta, depósito, saque, etc.) quanto ações secundárias, como validar uma data de nascimento.

A utilização de funções permite uma melhor estruturação do código, deixando-o mais organizado, e reduz a redundância de linhas de código pois uma mesma função pode ser invocada diversas vezes ao longo do programa. No bloco abaixo, são apresentadas as funções criadas para a solução (apenas sua chamada, o [código interno] foi omitido - ver o [arquivo completo](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/src/codigo_v2.py) para detalhes).

```Python
def carregar_dados():
def salvar_dados(clientes, contas):
def cadastrar_cliente(clientes):
def listar_clientes(clientes):
def cadastrar_conta(contas,clientes):
def listar_contas(contas,clientes):
def imprimir_detalhes_conta(conta_corrente,nro_conta,clientes):
def login_conta(clientes, contas):
def depositar(nro_conta, contas, extrato):  #positional only
def sacar(*, contas, extrato, nro_conta):   #keyword only           
def imprimir_extrato(nro_conta, /, contas, extrato):  #positional and keyword
def transferir(nro_conta, contas, clientes, extrato):
def validar_data_nascimento():
def calcular_idade(data_nascimento):
def confirmar_operacao():

```  
<br>  

Utilizando as funções:

```Python  

#Sem passagem de parâmetros
clientes, contas = carregar_dados()

#Argumentos passados pela posição (positional only)
depositar(nro_conta, contas, extrato)  

#Argumentos passados com identificação explícita da variável (keyword only)
#Se a posição dos argumentos for alterada, não é necessário corrigir no código da função
sacar(contas = contas, extrato = extrato, nro_conta = nro_conta)
```
<br>  

A partir dos dados dos clientes e contas corrente cadastradas é criado um banco de dados a partir de arquivos em formato **JSON**.

Exemplo de registro de clientes (arquivo [clientes.json](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/clientes.json)) com o CPF sendo a chave e um dicionário interno para nome, data de nascimento e endereço:

```json
{
    "12345678910": {
        "nome": "Arthur Silva",
        "data_nascimento": "30/06/1999",
        "endereco": "Rua Um, 1250 - Jardins - Sao Paulo/SP"
    }
}
```  
<br>  

Para as contas correntes, a chave é o número da conta (que é auto incrementado pelo programa e sequencial), e o CPF do cliente é vinculado a um cliente já cadastrado, implementando uma integridade de chave estrangeira via aplicação. Exemplo de registro de contas (arquivo [contas.json](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/contas.json)):

```json
{
    "1": {
        "agencia": "0001",
        "cpf_titular": "12345678910",
        "saldo": 735.0,
        "limite_diario_saques": 3,
        "limite_valor_por_saque": 500,
        "qtd_saques_dia": 3,
        "valor_sacado_dia": 1225.0
    },
    "2": {
        "agencia": "0001",
        "cpf_titular": "12345678910",
        "saldo": 1320.0,
        "limite_diario_saques": 3,
        "limite_valor_por_saque": 500,
        "qtd_saques_dia": 1,
        "valor_sacado_dia": 390.0
    }
}
```

---
### Implementação da solução:

Para executar o [código](https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/src/codigo_v2.py), baixe e extraia este repositório em sua máquina. Tendo o Python já instalado, digite no terminal (ou *prompt* de comando):

<center> `python src/codigo.py` ou `python3 src/codigo.py` </center>  

<br>
O sistema exibirá o menu de opções, conforme mostrado abaixo. Caso o usuário já esteja logado, no cabeçalho serão exibidas as informações sobre a conta corrente.  

<br>  
<br>  

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/menu_operacoes.png?raw=true" alt="Menu de operações" width=39%/>
</div>
<div align="center">  

##### Figura 1 - Menu de opções 
</div>
  
<br>

Antes de realizar operações bancárias (depósito, saque, extrato, transferência), o usuário precisa:

1. **Cadastrar um cliente**;
2. **Cadastar uma conta vinculando-a ao CPF de um cliente já cadastrado**;
3. **Selecionar uma conta já cadastrada (fazer *login*)**.  
   
<br>  

Foi aplicada validação à todas as entradas de dados (*inputs*) de dados utilizando a estrutura `try... except`.

<br>  

### Cadastrando um cliente:  

Ao cadastrar um cliente, é necessário informar um CPF com 11 dígitos e uma data de nascimento válida:  

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/validacao_data_nascimento.png?raw=true" alt="Cadastrando um cliente" width=48%/>
</div>
<div align="center">  

##### Figura 2 - Validações no cadastro de um cliente 
</div>

<br>

Uma verificação adicional é que o sistema não permite o cadastro de dois usuários com o mesmo número de CPF, garantindo que ele possa ser utilizado como chave primária do cadastro de clientes:

<br>
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/cadastro_cliente_erro.png?raw=true" alt="Validação CPF" width=42%/>
</div>
<div align="center">  

##### Figura 3 - Dois clientes não podem ter o mesmo CPF. 
</div>

<br>

A opção de listar clientes mostra todos os clientes cadastrados, utilizando a biblioteca `datetime` para o cálculo da idade:

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/clientes_cadastrados.png?raw=true" alt="Lista de clientes cadastrados" width=60%/>
</div>
<div align="center">  

##### Figura 4 - Listando os cliente cadastrados.
</div>

<br></br>

### Cadastrando uma conta corrente:

O número das contas correntes cadastradas é **sequencial e auto incrementado**. Por padrão, todas as contas estão vinculadas à Agência 0001. Para criar uma nova conta é necessário informar o CPF de um cliente já cadastrado no sistema (chave estrangeira):

<br>
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/cadastrar_conta_erro.png?raw=true" alt="Erro cadastro conta" width=56%/>
</div>
<div align="center">  

##### Figura 5 - Erro ao cadastrar a conta antes de cadastrar o cliente.
</div>

<br>

Informado um CPF válido, o sistema mostra o nome cliente e solicita a confirmação da criação da conta. As demais definições da conta (número de saques por dia, limite de valor por saque, etc.) seguem o padrão definido nas regra de negócio.

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/cadastro_conta.png?raw=true" alt="Cadastrando nova conta" width=48%/>
</div>
<div align="center">  

##### Figura 6 - Confirmação de cadastro de conta corrente.
</div>

<br></br>

### Realizando operações:

Para realizar qualquer operação bancária, é necessário estar logado numa conta corrente (ter selecionado uma conta). Ao fim de cada operação é solicitada a confirmação da transação. Caso o usuário selecione *NÃO*, nenhuma modifição é aplicada à conta.  

Para transferir valor entre contas também é necessário informar uma conta da destino válida:

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/tranferencia.png?raw=true" alt="Transferência entre contas" width=58%/>
</div>
<div align="center">  

##### Figura 7 - Transferindo valores entre contas.
</div>

<br>  

A transferência terá efeito sobre o saldo das duas contas, o que pode ser visualizado listando as contas cadastradas:

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/contas_cadastradas.png?raw=true" alt="Lista de contas cadastradas" width=48%/>
</div>
<div align="center">  

###### Figura 8 - Listando as contas cadastradas.
</div>

<br> 

O extrato reflete todas operações realizadas durante a seção, e pode ser solicitado a qualquer momento:

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario2-com_cadastro_usuario_conta/blob/main/assets/extrato.png?raw=true" alt="Extrato" width=40%/>
</div>
<div align="center">  

###### Figura 9 - Extrato de operações.
</div>

<br>  

---
### Autor
[Carlos Roberto de Souza Camilo](https://www.linkedin.com/in/carlos-roberto-camilo/)  
Ago. 23


