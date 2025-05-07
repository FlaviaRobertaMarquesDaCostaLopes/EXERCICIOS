from exercicios_04 import calcular_media

def cadastrar_aluno(nome, email, serie, nota01, nota02, nota03):
    alunos = []

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": [nota01, nota02, nota03]
    }

    alunos.append(aluno)
    
    return alunos

print(cadastrar_aluno("Flavia", "flavinha29@.com", "2tb", 7, 10, 10))