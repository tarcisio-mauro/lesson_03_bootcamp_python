### Exercícios com IF

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = 5
# preco = 30

# if quantidade > 0 and preco > 0:
#     print("Valid values")
# else:
#     print("Invalid values")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# try:
#     temperature = float(input("Insert the temperature reading in Celsius: "))
# except ValueError:
#     print("Temperature needs to be a number, please restart")
#     exit()

# if temperature < 18:
#     print("Low temperature")
# elif temperature >= 18 and temperature <= 26:
#     print("Normal temperature")
# else:
#     print("High temperature")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = int(input("Type your age: "))  # Exemplo de valor, substitua com input do usuário se necessário
# email = input("Type your email: ")  # Exemplo de valor, substitua com input do usuário se necessário

# if not 18 <= idade <= 65:
#     print("Idade fora do intervalo permitido")
# elif "@" not in email or "." not in email:
#     print("Email inválido")
# else:
#     print("Dados de usuário válidos")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transaction = {'value': 9000, 'time': 10}

# if transaction['value'] > 10000 and not 9 <= transaction['time'] <= 18:
#     print("Suspicious transaction (value and time)")
# elif not 9 <= transaction['time'] <= 18:
#     print("Suspicious transaction (outside commercial hours)")
# elif transaction['value'] > 10000:
#     print("Suspicious transaction (over 10k)")
# else:
#     print("Valid transaction")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# Example
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# texto = "a raposa marrom salta sobre o cachorro preguiçoso" #string
# palavras = texto.split() #list
# contagem_palavras = {} #dictionary 

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# total_palavras = len(contagem_palavras)
# print(f"O total de palavras no texto é {total_palavras}")

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros] # more direct use of the for structure, does the task for all numbers in the list

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Tarci", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_invalidos = [usuario for usuario in usuarios if usuario["email"] == ""]

# for usuario in usuarios_invalidos:
#     print(usuario["nome"])


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1,11)
# numeros_pares = [x for x in numeros if x % 2 == 0]

# print(numeros_pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Abaixo é uma lista de dicionários. Cada dicionário é como se fosse uma linha de uma tabela.
# Dessa forma, uma lista de dicionários é como se fosse uma tabela com várias linhas.
# Cada dicionário tem items, que são como colunas armazenando informações para cada linha da tabela
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {} # Cria um dicionário (linha de uma nova tabela) vazio que vai armazenar o total de vendas por categoria.

# for venda in vendas:                    # divide a tabela em linhas, e percorre todas as linhas
#     categoria = venda["categoria"]      # armazena a coluna categoria de cada linha (venda)
#     valor = venda["valor"]              # armazena a coluna valor de cada linha (venda)
    
#     if categoria in total_por_categoria:            # Checks if categoria is already on the new table categoria column   
#         total_por_categoria[categoria] += valor     # if yes than sums the value with the existing value for that category
#     else:
#         total_por_categoria[categoria] = valor     # if not then adds category and takes the first value

# print(total_por_categoria)     # prints the new one line table after the for, thus with the updated values


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# dados = []
# entrada = ""
# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = int(input("Digite um número entre 1 e 10: "))     # Receives number from user
# while numero < 1 or numero > 10:     # Check condition
#     print("Número fora do intervalo!")     # Action 1 if passes condition
#     numero = int(input("Por favor, digite um número entre 1 e 10: "))     # Action 2 if passes condition

# # Left the while or didn't enter

# print("Número válido!")     # Action after leaving while or if not entering

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Processando página {pagina_atual} de {paginas_totais}")
#     # Aqui iria o código para processar os dados da página
#     pagina_atual += 1

# print("Todas as páginas foram processadas.")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativa_atual = 1
# tentativas_totais = 5  # Limite

# while tentativa_atual <= tentativas_totais:
#     print(f"Tentando reconectar, tentativa {tentativa_atual} de {tentativas_totais}")
#     # Aqui iria o código para tentar reconectar com o serviço
#     tentativa_atual += 1

# print("Limite de tentativas alcançado.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# itens = [1, 2, 3, "parar", 4, 5]

# i = 0

# while itens[i] != "parar":
#     # Processa o item
#     print(f"Processando item: {itens[i]}")
#     i += 1

# print("Parada encontrada, encerrando o processamento.")