def criar_e_armazenar_tarefas():
    #cria um arquivo txt para que possa armazenar as informações das tarefas diarias.
    with open('dados.txt', 'a') as arquivo:
        pass
    print("Arquivo 'dados.txt' pronto para adicionar novos registros.")
    
    #Adiciona uma tarefa ao arquivo para armazenamento. 
    
    nome = input ("Digite o nome da tarefa a ser adicionada: ")
    descricao = input ("Digite a descrição da Tarefa da tarefa: ")
    
    try: 
        while True:
            prioridade = int(input ('Digite o nivel de prioridade da Tarefa: \n sendo: \n 1 - para prioridade Alta\n 2 - para prioridade Média \n 3 - para prioridade Baixa '))
            
            if prioridade == 1:
                prioridade = 'alta'
                break
            elif prioridade == 2:
                prioridade = 'media'
                break
            elif prioridade == 3:
                prioridade = 'baixa'
                break
            else:
                print('Opção Invalida') 
    except ValueError:
        print("Por Favor, Insira um número Válido.")
    categoria = input ('Digite a Categoria da Tarefa: \n exemplo: Estudo, Trabalho, Lazer, Atividade a ser executada... ')

        # Adiciona as informações no txt criado.
    with open ('dados.txt', 'a') as arquivo:
        arquivo.write(f'\n{nome}, {descricao}, {prioridade}, {categoria}')
    print('Registro adicionado com sucesso!')

def listar_tarefas():
    #verifica se o arquivo não tem erros
    try:
        #abre o txt em modo leitura.
        with open ('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        # verifica se tem conteudo no txt, caso não tenha indica a opção de adicionar tarefas
        if len(linhas) == 0:
            print('O arquivo está vazio, escolha a opção adicionar tarefas')
        else:
            print('Lista de tarefas: \n')
            sequencia = 1
            for linha in linhas:
                print(f"{sequencia} - {linha.strip()}\n")
                sequencia += 1
    # retorna um erro caso o arquivo txt não foi craido
    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado, utilize a opção adicionar tarefa para criar um arquivo.")

def tarefa_concluida():
    try:
        #abre o arquivo pra leitura
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        # verifica se o arquivo está vazio
        if not linhas:
            print ('O arquivo se encontra vazio, escolha a opção adicionar tarefa para adicionar uma tarefas...')
            return
        # apresenta tarefas disponiveis
        print ("Tarefas disponíveis: ")
        for i, linha in enumerate(linhas):
            print(f"{i+1}. {linha.strip()}\n")
        
        #Solicita qual tarefa será marcada com concluida
        numero_tarefa = int(input("\n Digite o número da tarefa a ser marcada como concluido"))

        # caso não exista a tarefa, retorna para o usuario um informativo.
        if numero_tarefa < 1 or numero_tarefa > len(linhas):
            print ("Número de tarefa inválido.")
            return
        
        #Marca a tarefa como concluida
        tarefa = linhas[numero_tarefa -1]. strip()
        
        if "Concluida" in tarefa:
            print("Essa Tarefa já foi marcada como concluida. ")
        else:    
            tarefa_concluida = tarefa + " - Concluida"

            linhas[numero_tarefa -1] = tarefa_concluida + "\n"

            #Registra a atualização no arquivo
            with open('dados.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            print(f"tarefa '{tarefa}' marcada como concluída!")

    # Verifica se existem erros na execução
    except FileNotFoundError:
        print("O Arquivo 'dados.txt' não foi encontrado.")
    except ValueError:
        print("Por Favor, Insira um número Válido.")

def classifica_tarefas():
    tarefas = []
    prioridades = {"alta":1, "media": 2, "baixa": 3}

    try:
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                nome, descricao, prioridade, categoria = linha.strip().split(', ')
                tarefas.append((nome, descricao, prioridade, categoria))
                # o valor 99 garante que caso o usuario cadastre alguma prioridade incorreta ela sera salva no final da lista com default, assim o codigo continua sem erros de programação e exime a lista normalmente
            tarefas.sort(key=lambda x: prioridades.get(x[2].lower(), 99))
    except FileNotFoundError:
        print("Arquivo não localizado, acesse a opção 1 para criar a priemira tarefa")

    except Exception as e:
        print(f"Erro ao Ler o Arquivo: {e}")
        return
    if tarefas:
        print("Tarefas por ordem de prioridade: ")
        for tarefa in tarefas:
            nome, descricao, prioridade, categoria = tarefa
            print(f"- {nome}: {descricao} (Prioridade: {prioridade.capitalize()}, Categoria: {categoria})")
    else:
        print("Nenhuma tarefa encontrada ou erro ao ler o arquivo. ")
    return []

def menu():
    print("=-=" * 30)
    print(" Opção '1' Criar uma Tarefa:")
    print(" Opção '2' Listar Tarefas existentes:")
    print(" Opçao '3' Listar Tarefas por Prioridade:")
    print(" Opção '4' Marcar Tarefas como Concluida:")
    print(" Opçao '5' Sair do programa:")
    print("=-=" * 30)


while True:
    # Chama o menu da interação do usuario
    menu()
    try:
        #solicita que o usuario insira uma opção do menu
        usuario = int(input('Digite qual opção deseja utilizar:'))

        #Verifica o input do usuario e chama a função de acordo com o que o usuario digitou
        if usuario == 1:
            criar_e_armazenar_tarefas()
        elif usuario == 2:
            listar_tarefas()
        elif usuario == 3:
            classifica_tarefas()
        elif usuario == 4:
            tarefa_concluida()
        elif usuario == 5:
            print("Você Saiu da sua lista de Tarefas...")
            #sai do programa caso o usuario digite a opção 5
            break
        # retorna uma opção invalida caso o numero digitado não exista no menu
        else:
            print("Opção Invalida")
    #retorna mensagem de erro para o usuario, solicitando a opção correta.
    except ValueError:
        print("Por Favor, Insira um número Válido.")
