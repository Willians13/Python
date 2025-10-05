aluno = {}
aluno['nome'] = input('Nome : ')
aluno['media'] = float(input('Média do aluno : '))
if aluno['media'] >=7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >=5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print()
print(f'Nome : {aluno["nome"]}\nMedia : {aluno["media"]}\nSituacao : {aluno["situacao"]}')