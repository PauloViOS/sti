import csv


class Aluno:
	def __init__(self, nome, matricula, telefone, email, uffmail, status):
		self.nome = nome
		self.matricula = matricula
		self.telefone = telefone
		self.email = email
		self.uffmail = uffmail
		self.status = status


def criar_lista_de_objetos():
	lista = []
	with open('alunos.csv') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			instance = Aluno(row[0], row[1], row[2], row[3], row[4], row[5])
			lista.append(instance)
	file.close()
	return lista


def acha_instancia(lista, matricula):
	instancia = next((aluno for aluno in lista if aluno.matricula == matricula), None)
	while instancia is None or instancia.status != 'Ativo':
		if instancia is None:
			matricula = input("Matrícula não encontrada na base de dados. Insira uma matrícula válida: ")
		else:
			matricula = input("Matrícula inativa. Insira uma matrícula ativa: ")
		instancia = next((aluno for aluno in lista if aluno.matricula == matricula), None)
	return instancia


def definir_uffmail(nome, lista):
	email = input(f"Olá, {nome}! Por favor, insira um nome de usuário para a criação do email: ")
	email += '@id.uff.br'
	resposta = input(f"Seu email será {email}. Gostaria de confirmar a criação deste email? (s/n)")
	repetido = next((email for aluno in lista if aluno.uffmail == email), False)
	print(repetido)
	while resposta != 's'.lower() or repetido:
		if resposta != 's'.lower():
			email = input("Por favor, insira um nome de usuário para a criação do email: ")
			email += '@id.uff.br'
			resposta = input(f"Seu email será {email}. Gostaria de confirmar a criação deste email? (s/n)")
		if repetido:
			email = input(f"Esse email já existe na base de dados! Por favor, insira outro email: ")
			email += '@id.uff.br'
			resposta = input(f"Seu email será {email}. Gostaria de confirmar a criação deste email? (s/n)")
			repetido = next((email for aluno in lista if aluno.uffmail == email), False)

	return email


def criar_uffmail():
	lista = criar_lista_de_objetos()
	matricula = input("Digite sua matrícula: ")
	instancia = acha_instancia(lista, matricula)
	nome = instancia.nome.split()[0]
	uffmail = definir_uffmail(nome, lista)
	instancia.uffmail = uffmail
	print(f"A criação de seu e-mail ({uffmail}) será feita nos próximos minutos.")
	print(f"Um SMS foi enviado para {instancia.telefone} com a sua senha de acesso.")

criar_uffmail()
