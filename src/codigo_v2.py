import os

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
                print('O CPF informado já consta na base de dados. Faça uma consulta dos clientes já cadastrado.')
                return 0
            
            else:
                break
    
    data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ')
    endereco = input('Endereço (logradouro, número, complemento): \n')
    bairro = input('Bairro: ')
    municipio = input('Cidade: ')
    uf = input('UF: ')

    endereco_completo = f'{endereco} - {bairro} - {municipio}/{uf}'

    clientes[cpf] = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco_completo
    }

    print('\nCliente cadastrado com sucesso!')
    return 1

def confirmacao (operacao, valor):

    print(f'''
  Confirma o {operacao} de R$ {valor:.2f}?

     [1] Sim
     [0] Não

  ''')
    
    while True:

        resposta = input('Confirmação: ')

        if resposta in ['0','1']:
            return resposta
        else:
            print('Opção inválida! \n')
            continue


# Recebe os dados do cliente a partir de seu login no sistema
CLIENTE = {
    'nome': 'Arthur',
    'agencia': 1234,
    'conta': '0001-1',
    'saldo': 400,
    'limite_diario_saques': 3,
    'limite_valor_por_saque': 500,
    'qtd_saques_dia': 0,
    'valor_sacado_dia': 0
}

menu = '''
  === Menu de Operações ===
        
      [1] Depósito
      [2] Saque
      [3] Extrato
      [4] Cadastrar Conta
      [5] Cadastrar Cliente
      [0] Sair
        
  =========================      
    '''
    
clientes = {}
extrato = [f'Saldo anterior: R$ {CLIENTE["saldo"]:0.2f}']

#Limpa a tela do terminal
os.system('clear')

#O menu deve ser exibido até que o usuário digite 0 (zero)
while True:
        
    print(menu)
    opcao = input('Selecione a operação desejada: ')
    os.system('clear')

    if opcao == '1':
        
        while True:
            print('Opção selecionada: DEPÓSITO \n')

            while True:
                try:
                    valor = float(input('Informe o valor a ser depositado: '))
                    break
                except:
                    print('Valor de depósito inválido! \n')
                    continue

            if valor <= 0:
                print('Valor de depósito inválido! \n')
                continue
            else:
                
                if (confirmacao('depósito',valor) == '1'):
                    CLIENTE['saldo'] += valor
                    os.system('clear')
                    print('Opção selecionada: SIM \n')
                    print(f'Depósito confirmado! \n')
                    print(f'Novo saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                    extrato.append(f'Depósito........R$  {valor:0.2f}') 

                else:
                    print('\nOpção selecionada: NÃO \n')
                           
                break

    elif opcao == '2':
        
        #Cliente já excedeu o limite de saques no dia?
        if (CLIENTE['qtd_saques_dia'] >= CLIENTE['limite_diario_saques']):
            print(f'Limite de saque diário ({CLIENTE["qtd_saques_dia"]}) excedido!')
            print('Não é possível fazer a operação! Por favor, tente novamente amanhã.')

        else:
            while True:
                print('Opção selecionada: SAQUE \n')

                while True:
                    try:
                        valor = float(input('Informe o valor a ser sacado: '))
                        break
                    except:
                        print('Valor de saque inválido! \n')
                        continue
                
                if valor <= 0:
                    print('Valor de saque inválido! \n')
                    continue
                elif valor > CLIENTE['limite_valor_por_saque']:
                    print('Valor inválido! O limite de saque por operação é de R$ 500 \n')
                    continue            
                else:

                    if (confirmacao('saque',valor) == '1'):
                        
                        #O cliente tem saldo suficiente para o saque?
                        if (CLIENTE['saldo'] - valor) >= 0:
                            CLIENTE['saldo'] -= valor
                            CLIENTE['qtd_saques_dia'] += 1
                            os.system('clear')
                            print('Opção selecionada: SIM \n')
                            print(f'Saque efetuado! \n')
                            print(f'Novo saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                            input('Pressione qualquer tecla para continuar.')
                            extrato.append(f'Saque...........R$  {valor:0.2f}')

                        else:
                            print('\nNão é possível efetuar o saque: Saldo insuficiente!')
                            print(f'Saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                            input('Pressione qualquer tecla para continuar.')
                    
                    else:
                        print('\nOpção selecionada: NÃO \n')
                
                    break
            

    elif opcao == '3':
        print('Opção selecionada: EXTRATO \n')
        print('==== Extrato da Sessão ====\n')

        #Houve alguma movientação durante a seção?
        if len(extrato) == 1:
            print(extrato[0])
            print('Não foram realizadas movimentações.')
        
        else:
            for item in range(len(extrato)):
                print(extrato[item])
            print(f'Saldo atual:    R$ {CLIENTE["saldo"]:0.2f}\n')
        print('===========================\n\n')
        input('Pressione qualquer tecla para continuar.')

    elif opcao == '5':

        print('Opção selecionada: CADASTRAR CLIENTE \n')

        if cadastrar_cliente(clientes) == 1:
            print('Cliente cadastrado com sucesso!')
        
        input('Pressione qualquer tecla para continuar...')

        print(clientes)

    elif opcao == '0':
        print('\nAgradecemos por utilizar os nossos serviços! Tenha um bom dia! \n')
        print('=== Sessão Encerrada === \n')
        break

    else:
        print('Opção inválida!')
        input('Pressione qualquer tecla para continuar.')

    print('\nDeseja realizar outra operação?\n')


        

        


            


        

        
      