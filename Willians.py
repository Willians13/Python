
class Aluno:
    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade

def ordenar_alunos(alunos):
    alunos.sort(key=lambda x: x.nome)


def buscar_aluno(alunos, nome):
    for aluno in alunos:
        if aluno.nome == nome:
            return aluno
    return None


def listar_alunos(alunos):
    ordenar_alunos(alunos)
    print("Lista de Alunos:")
    for aluno in alunos:
        print(f"""Nome: {aluno.nome} == Matrícula: {aluno.matricula} == Idade: {aluno.idade}""")

def programa_principal():
    
    alunos = [
        Aluno("Willians", 1 , 18),
        Aluno("Allyson", 2, 17),
        Aluno("Gabriel", 3, 18),
        Aluno("Lucas", 4, 18),
        Aluno("Jean", 5, 19),
        Aluno("Enzo", 6, 21),
        Aluno("Gabriela", 7, 20),
        Aluno("Andreia", 8, 18),
        Aluno("David", 9, 18),
        
    ]
    while True:
        print("\nOpções:")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula do aluno: ")
            idade = int(input("Idade do aluno: "))
            aluno = Aluno(nome, matricula, idade)
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == 2:
            listar_alunos(alunos)

        elif opcao == 3:
            nome = input("Digite o nome do aluno a ser buscado: ")
            aluno_encontrado = buscar_aluno(alunos, nome)
            if aluno_encontrado:
                print(f"\033[32mAluno encontrado\033[m - Nome: {aluno_encontrado.nome} == Matrícula: {aluno_encontrado.matricula} == Idade: {aluno_encontrado.idade}")
            else:
                print("Aluno não encontrado.")

        elif opcao == 4:
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Digite novamente.")

programa_principal()