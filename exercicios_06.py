def cadastrar_filmes(nome, descricao_do_filme,classificacao, categoria01, categoria02, categoria03,categoria04, categoria05 ):
    filmes = []

    filme = {
        "nome": nome,
        "descricao do filme": descricao_do_filme,
        "classifificacao": classificacao,
        "categorias": [categoria01, categoria02, categoria03, categoria04, categoria05]
    }
    filmes.append(filme)

    return filmes

print(cadastrar_filmes("Harry Potter e o Prisioneiro de azkaban","É o início do terceiro ano na escola de bruxaria Hogwarts. Harry, Ron e Hermione têm muito o que aprender. Mas uma ameaça ronda a escola e ela se chama Sirius Black. Após doze anos encarcerado na prisão de Azkaban, ele consegue escapar e volta para vingar seu mestre, Lord Voldemort. Para piorar, os Dementores, guardas supostamente enviados para proteger Hogwarts e seguir os passos de Black, parecem ser ameaças ainda mais perigosas", "10 anos", "Fantasia", "Ficcao", "Sobrenatural", "Drama", "Misterio"))
