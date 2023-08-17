import os
from datetime import datetime
import re


def cadastrar_cliente(clientes):

    print('Informe os dados do cliente: \n')
    nome = input('Nome: ')
    
    while True:
        cpf = input('CPF (somente números, 11 dígitos): ')

        #O CPF informado é válido?
        if cpf.isdigit() == False or len(cpf) != 11:
            print('Número de CPF inválido! \n')
            continue
        
        else:

            #O cliente já está cadastrado?
            if cpf in clientes:
                print('\nErro! O CPF informado já consta na base de dados.\nFaça uma consulta dos clientes já cadastrados.\n')
                return 0
            
            else:
                break
    

    data_nascimento = validar_data_nascimento()
    endereco = input('Endereço (logradouro, número, complemento): \n')
    bairro = input('Bairro: ')
    municipio = input('Cidade: ')
    uf = input('UF: ')

    endereco_completo = f'{endereco} - {bairro} - {municipio}/{uf}'

    print('\nConfirma o cadastro do cliente?')
    if (confirmar_operacao() == True):
        clientes[cpf] = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'endereco': endereco_completo
        }

        print('\nCliente cadastrado com sucesso!\n')
        return 1
    else:
        print('Operação cancelada!\n')


def listar_clientes(clientes):

    if len(clientes) == 0:
        print('Ainda não há clientes cadastrados.\n')
    else:
        print('Lista de clientes cadastrados:')

        # clientes.items() gera tuplas onde o primeiro item é a chave do dicionário (o CPF do cliente), 
        #     e o segundo item o conteúdo do dicionário interno (os dados do cliente).
        for cpf, dados in clientes.items():
            print(f'\nCPF: {cpf}')
            print(f'Nome: {dados["nome"]}')
            print(f'Data de Nascimento: {dados["data_nascimento"]}')
            print(f'Idade: {calcular_idade(dados["data_nascimento"])} anos')
            print(f'Endereço: {dados["endereco"]}\n')


def cadastrar_conta(contas,clientes):

    if (len(clientes) < 1):
        print('Não é possível criar uma conta. Não há nenhum cliente cadastrado!')
        print('Cadastre um cliente primeiro para depois criar sua conta.\n')
        return 0
    
    #Gera o número da nova conta somando 1 ao número da última conta cadastrada ou inicia em 1 se não houver nenhuma conta.
    nro_conta = (max(contas.keys()) + 1) if (len(contas) > 0) else 1
    agencia = '0001'

    print(f'Agência: {agencia}')
    print(f'Conta Corrente: {nro_conta}')

    while True:
        cpf = input('CPF do titular (somente números, 11 dígitos): ')

        #O CPF informado é válido?
        if cpf.isdigit() == False or len(cpf) != 11:
            print('Número de CPF inválido! \n')
            continue
        
        else:

            #O cliente já está cadastrado?
            if cpf not in clientes:
                print('\nErro! O CPF informado não consta entre os clientes cadastrados!\nPrimeiro cadastre o cliente para depois criar sua conta.\n')
                return 0
            
            else:                
                break

    print(f'Nome do Cliente: {clientes[cpf]["nome"]}')
    
    conta = {
        'agencia': agencia,
        'cpf_titular': cpf,
        'saldo': 0.0,
        'limite_diario_saques': 3,
        'limite_valor_por_saque': 500,
        'qtd_saques_dia': 0,
        'valor_sacado_dia': 0.0
    }

    print('\nConfirma o cadastro da conta corrente?')
    if (confirmar_operacao() == True):
        contas[nro_conta] = conta

        os.system('clear')
        print('Conta corrente criada com sucesso!\n')
        print('Detalhes da Conta corrente:\n')
        imprimir_detalhes_conta(contas[nro_conta],nro_conta,clientes)
    else:
        print('Operação cancelada!\n')


def listar_contas(contas,clientes):

    if len(contas) == 0:
        print('Ainda não há conta corrente cadastrada.\n')
    else:
        print('Lista de contas corrente cadastradas:\n')
        for nro_conta in contas:
            imprimir_detalhes_conta(contas[nro_conta],nro_conta,clientes)


def imprimir_detalhes_conta(conta_corrente,nro_conta,clientes):
    print(f'Agência: {conta_corrente["agencia"]}')
    print(f'Conta Corrente: {nro_conta}')
    cpf = conta_corrente["cpf_titular"]
    print(f'CPF do Titular: {cpf}')
    print(f'Nome do Titular: {clientes[cpf]["nome"]}')
    print(f'Saldo: R$ {conta_corrente["saldo"]:0.2f}')
    print(f'Limite Diário de Saques: {conta_corrente["limite_diario_saques"]}')
    print(f'Limite de Valor por Saque: R$ {conta_corrente["limite_valor_por_saque"]:0.2f}')
    print(f'Número de Saques Efetuados Hoje: {conta_corrente["qtd_saques_dia"]}')
    print(f'Total Sacado Hoje: R$ {conta_corrente["valor_sacado_dia"]:0.2f}\n')


def login_conta(clientes, contas):

    if len(contas) == 0:
        print('Ainda não há conta corrente cadastrada.\n')
    else:
        print('Agência: 0001')
        nova_conta = input('Conta Corrente: ')
        
        if nova_conta.isdigit() == True:
            if int(nova_conta) in contas:
                cpf = contas[int(nova_conta)]["cpf_titular"]
                print(f'Nome do Titular: {clientes[cpf]["nome"]}\n')

                print(f'Deseja selecionar esta conta?\n')
                if (confirmar_operacao() == True):
                    print('Login efetuado com sucesso!\n')
                    return nova_conta
                else:
                    print('Operação cancelada!\n')
                    return None
                
        print('\nNúmero de conta inválido!\nCadastre-a ou consulte a lista de contas já cadastradas.\n')
    

def depositar(nro_conta, contas, extrato):
        while True:
            try:
                valor = float(input('Informe o valor a ser depositado: '))
                break
            except:
                print('Valor de depósito inválido! \n')
                continue

        if valor <= 0:
            print('Valor de depósito inválido! \n')
        else:

            print(f'\nConfirma o depósito de R$ {valor:.2f}?')            
            if (confirmar_operacao() == True):
                contas[nro_conta]["saldo"] += valor
                print(f'\nDepósito confirmado! \n')
                print(f'Novo saldo da conta: R$ {contas[nro_conta]["saldo"]:.2f} \n')
                extrato.append(f'Depósito........R$  {valor:0.2f}') 
                return True
            else:
                return False
                                   

def sacar(nro_conta, contas, extrato):
        
        #Cliente já excedeu o limite de saques no dia?
        if (contas[nro_conta]["qtd_saques_dia"] >= contas[nro_conta]["limite_diario_saques"]):
            print(f'Limite de saque diário ({contas[nro_conta]["qtd_saques_dia"]}) excedido!')
            print('Não é possível fazer a operação! Por favor, tente novamente amanhã.\n')
            return False

        else:

            while True:
                try:
                    valor = float(input('Informe o valor a ser sacado: '))
                    break
                except:
                    print('Valor de saque inválido! \n')
                    continue
            
            if valor <= 0:
                print('Valor de saque inválido! \n')
            elif valor > contas[nro_conta]["limite_valor_por_saque"]:
                print(f'Valor inválido! O limite de saque por operação é de R$ {contas[nro_conta]["limite_valor_por_saque"]:0.2f} \n')           
            else:

                print(f'\nConfirma o saque de R$ {valor:.2f}?')
                if (confirmar_operacao() == True):
                    
                    #O cliente tem saldo suficiente para o saque?
                    if (contas[nro_conta]['saldo'] - valor) >= 0:
                        contas[nro_conta]['saldo'] -= valor
                        contas[nro_conta]['qtd_saques_dia'] += 1
                        contas[nro_conta]['valor_sacado_dia'] += valor
                        print(f'\nSaque efetuado! \n')
                        print(f'Novo saldo da conta: R$ {contas[nro_conta]["saldo"]:.2f} \n')
                        extrato.append(f'Saque...........R$  {valor:0.2f}')
                        return True

                    else:
                        print('\nNão é possível efetuar o saque: Saldo insuficiente!')
                        print(f'Saldo da conta: R$ {contas[nro_conta]["saldo"]:.2f} \n')
                        return False
                else:
                    return False
                

def imprimir_extrato(nro_conta, contas, extrato):
        print('==== Extrato da Sessão ====\n')

        #Houve alguma movientação durante a seção?
        if len(extrato) == 1:
            print(extrato[0])
            print('Não foram realizadas movimentações.')
        
        else:
            for item in range(len(extrato)):
                print(extrato[item])
            print(f'Saldo atual:    R$ {contas[nro_conta]["saldo"]:0.2f}\n')
        print('===========================\n\n')


def transferir(nro_conta, contas, clientes, extrato):

    if len(contas) == 1:
        print('Erro: Apenas a sua conta está cadastrada! \nÉ necessário haver uma outra conta para ser possível a transferência.\n')
    else:
        print('\nInfome os dados da conta de destino:')
        print('Agência: 0001')
        outra_conta = input('Conta Corrente: ')
        
        if outra_conta.isdigit() == True:

            outra_conta = int(outra_conta)
            #Confirma se a conta de destino está cadastrada e se é diferente da própria conta do usuário.
            if (outra_conta in contas) and (outra_conta != nro_conta):
                outro_cpf = contas[outra_conta]["cpf_titular"]
                print(f'Nome do Titular: {clientes[outro_cpf]["nome"]}\n')

                while True:
                    try:
                        valor = float(input('Valor a ser transferido R$: '))
                        break
                    except:
                        print('Valor inválido! \n')
                        continue

                print(f'\nConfirma a transferência de R$ {valor:0.2f} para a conta informada acima? \n')                
                if (confirmar_operacao() == True):

                    #O cliente tem saldo suficiente para a transferência?
                    if (contas[nro_conta]['saldo'] - valor) >= 0:
                        contas[nro_conta]['saldo'] -= valor
                        contas[outra_conta]['saldo'] += valor

                        print(f'\nTransferência efetuada com sucesso! \n')
                        print(f'Novo saldo de sua conta: R$ {contas[nro_conta]["saldo"]:.2f} \n')
                        extrato.append(f'Transferência ..R$  {valor:0.2f}')
                        return True
                    
                    else:
                        print('\nNão foi possível realizar a transferência: Saldo insuficiente!')
                        print(f'Saldo em sua conta: R$ {contas[nro_conta]["saldo"]:.2f} \n')
                        return False

                else:
                    print('Operação cancelada!\n')
                    return False
                
        print('\nNúmero de conta inválido!\nConsulte a lista de contas já cadastradas.\n')

def validar_data_nascimento():

    #Regex para a data. O "r" informa ao python que é uma string bruta, evitando que ele trate "\d" ou "\n" como marcadores especiais.
    padrao = r'^\d{2}/\d{2}/\d{4}$'    
    while True:
        data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ')

        #re.math(padrao, string) só retorna algum valor caso haja alguma correspondência do padrão na string.
        if re.match(padrao, data_nascimento) is not None:

            #A função map() desempacota os três valores da lista gerada pelo split('/'), antes aplicando a função int() a cada valor.
            dia,mes,ano = map(int, data_nascimento.split('/'))
            if (1 <= dia <= 31) and (1 <= mes <= 12) and (1900 <= ano <= datetime.now().year):
                return data_nascimento
            else:
                print('\nValor de data inválido!')
        else:
            print('\nValor inválido! Utilize o formato de data especificado.')


def calcular_idade(data_nascimento):
    hoje = datetime.now()

    #Converter a data de nascimento para um objeto da classe datetime, de acordo com o formato de data especificado.
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    
    #Calcula a data de nascimento subtraindo os anos, e depois verificando se a pessoa já fez aniversário no ano atual (subtrai 1 se ainda não).
    #    Numa expressão numérica, True = 1 e False = 0.
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade


def confirmar_operacao():

    print(f'''
     [1] Sim
     [0] Não

  ''')
    
    while True:
        resposta = input('Confirmação: ')

        if resposta == '1':
            print('Opção selecionada: SIM \n')
            return True
        elif resposta == '0':
            print('Opção selecionada: NÃO \n')
            return False
        else:
            print('Opção inválida! \n')
            continue


menu = '''
 ======== Menu de Operações ========

   [1] Selecionar/Trocar de Conta     
   [2] Depósito
   [3] Saque
   [4] Extrato
   [5] Transferência
   [6] Cadastrar Conta
   [7] Listar Contas
   [8] Cadastrar Cliente
   [9] Listar Clientes
   [0] Sair
        
 ===================================      
    '''
    
clientes = {}
contas = {}

#Zero indica que o usuário não fez o login numa conta
nro_conta = 0

#Limpa a tela do terminal
os.system('clear')

#O menu deve ser exibido até que o usuário digite 0 (zero)
while True:

    if nro_conta != 0:     
        print(cabecalho)

    print(menu)
    opcao = input('Selecione a operação desejada: ')
    os.system('clear')

    if opcao == '1':
        print('Opção selecionada: SELECIONAR CONTA CORRENTE - FAZER LOGIN \n')
        
        nova_conta = login_conta(clientes, contas)

        if nova_conta is not None:
            nro_conta = int(nova_conta)
            
            #Os registros em extrato são resetados ao trocar de conta - troca de sessão.
            extrato = [f'Saldo anterior: R$ {contas[nro_conta]["saldo"]:0.2f}']

            cpf = contas[nro_conta]["cpf_titular"]
            cabecalho = f'Agência: 0001    Conta Corrente: {nro_conta}    \nTitular: {clientes[cpf]["nome"]}\n'
       
    elif opcao == '2':

        if nro_conta != 0:      
            while True:
                print(cabecalho)
                print('Opção selecionada: DEPÓSITO \n')

                #Operação é repetida até que o usuário digite um valor válido e confirme (return True) ou não o depósito (return False)
                if depositar(nro_conta, contas, extrato) is not None:
                    break
        else:
            print('\nErro: É necessário selecionar uma conta corrente antes de efetuar um depósito!\n')

    elif opcao == '3':

        if nro_conta != 0:
            while True:
                print(cabecalho)
                print('Opção selecionada: SAQUE \n')

                #Operação é repetida até que o usuário digite um valor válido e confirme (return True) ou não o saque (return False)
                if sacar(nro_conta, contas, extrato) is not None:
                    break
        else:
            print('\nErro: É necessário selecionar uma conta corrente antes de efetuar um saque!\n')
                
    elif opcao == '4':

        if nro_conta != 0:

            print(cabecalho)
            print('Opção selecionada: EXTRATO \n')
            imprimir_extrato(nro_conta, contas, extrato)
        else:
            print('\nErro: É necessário selecionar uma conta corrente antes de visualizar um extrato!\n')

    elif opcao == '5':

        if nro_conta != 0:

            print(cabecalho)
            print('Opção selecionada: TRANSFERIR VALORES ENTRE CONTAS \n')
            transferir(nro_conta, contas, clientes, extrato)
        else:
            print('\nErro: É necessário fazer o login em sua conta corrente para fazer uma transferência!\n')

    elif opcao == '6':

        print('Opção selecionada: CADASTRAR CONTA \n')
        cadastrar_conta(contas,clientes)

    elif opcao == '7':

        print('Opção selecionada: LISTAR CONTAS CORRENTE CADASTRADAS \n')
        listar_contas(contas,clientes)

    elif opcao == '8':

        print('Opção selecionada: CADASTRAR CLIENTE \n')
        cadastrar_cliente(clientes)

    elif opcao == '9':

        print('Opção selecionada: LISTAR CLIENTES \n')
        listar_clientes(clientes)

    elif opcao == '0':
        print('\nAgradecemos por utilizar os nossos serviços! Tenha um bom dia! \n')
        print('=== Sessão Encerrada === \n')
        break

    else:
        print('Opção inválida!\n')

    input('Pressione qualquer tecla para continuar...')

    print('\nDeseja realizar outra operação?\n')


        

        


            


        

        
      