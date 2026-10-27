livros = []
usuarios = []
 
opcao  = 0
while opcao != 3:
    print("""
    -----------------------------
       SISTEMA DA BIBLIOTECA
 
       [1] Gerenciar livros
       [2] Gerenciar usuários
       [3] Sair
    -----------------------------
    """)
 
    try:
        opcao = int(input("Escolha uma opção: "))
 
        if opcao == 1:
            print("Você escolheu o menu de livros!")
            while opcao != 5:
                try:
                    print(f"""
                    -----------------------------
                    Cadastro de livros e alugúeis
           
                    [1] Cadastro
                    [2] Listar
                    [3] Atualização de Cadastro
                    [4] Remover
                    [5] Sair
                    -----------------------------
                    """)
                    opcao = int(input("Digite uma opção: "))
                    print("--"*20)
                except:
                    print("\033[31mOPÇÃO INVALIDA\033[m")
               
                if opcao == 1:
                    try:
                        nomeLivro = input("Digite o nome do livro: ").upper
                        descricaolirvo = input("Digite uma descrição do livro: ")
                        precolivro = float(input("digite o Valor do livro: "))
                        quantidadelivro = int(input("Digite a Quantidade que possui deste livro: "))
                        generolivro = input("Digite o genero do livro: ").upper
                        Idade = int(input("Digite a idade recomendada do livro: "))
           
                        livro = {
                        "nome":nomeLivro,
                        "descricao":descricaolirvo,
                        "Preco":precolivro,
                        "quantidade":quantidadelivro,
                        "Genero":generolivro,
                        "Idade":Idade
                        }
               
                        livros.append(livro)
           
                    except:
                        print("\033[31mOPÇÃO INVALIDA\033[m")
                elif opcao == 2:
                    for x in livros:
                        print(f"""
                            Nome:{x["nome"]}
                            Descrição do livro:{x["descricao"]}
                            Preço:{x["Preco"]}
                            Quantidade:{x["quantidade"]}
                            Gênero:{x["Genero"]}
                            Idade recomendada:{x["Idade"]}""")
                elif opcao == 3:
                    try:
                   
                        nomebusca = input("Digite o livro a ser atualizado: ")
 
                        listadelivros = []
 
                        for x, i in enumerate(livros):
                            livroaservalidado = livros[x]["nome"]
                            listadelivros.append(livroaservalidado)
 
                        if nomebusca in listadelivros:
 
                            opcaoatt = 0
 
                            while opcaoatt != 7:
                                print("""
                                O que deseja atualizar?
 
                                [1] Nome
                                [2] Descrição
                                [3] Preço
                                [4] Quantidade
                                [5] Gênero
                                [6] Idade recomendada
                                [7] Sair
                                """)
 
                                opcaoatt = int(input("Escolha uma opção: "))
 
                                for x, i in enumerate(livros):
                                    if livros[x]["nome"] == nomebusca:
 
                                        if opcaoatt == 1:
                                            novonome = input("Digite o novo nome: ").upper
                                            livros[x]["nome"] = novonome
                                            nomebusca = novonome
 
                                        elif opcaoatt == 2:
                                            novadescricao = input("Digite a nova descrição: ")
                                            livros[x]["descricao"] = novadescricao
 
                                        elif opcaoatt == 3:
                                            novopreco = float(input("Digite o novo preço: "))
                                            livros[x]["Preco"] = novopreco
 
                                        elif opcaoatt == 4:
                                            novaquantidade = int(input("Digite a nova quantidade: "))
                                            livros[x]["quantidade"] = novaquantidade
 
                                        elif opcaoatt == 5:
                                            novogenero = input("Digite o novo gênero: ").upper
                                            livros[x]["Genero"] = novogenero
 
                                        elif opcaoatt == 6:
                                            novaidade = int(input("Digite a nova idade recomendada: "))
                                            livros[x]["Idade"] = novaidade
 
                                        elif opcaoatt == 7:
                                            print("Saindo da atualização...")
 
                                        else:
                                            print("\033[31mOPÇÃO INVALIDA\033[m")
 
                                        break
                    except:
                        print("\033[31mOPÇÃO INVALIDA\033[m")
                       
                elif opcao == 4:
                    for x, i in enumerate(livros):
                        print(f"{x} {livros[x]["nome"]}")
           
                    deletarlivro = int(input("Digite O livro a ser deletado: "))
                    livros.pop(deletarlivro)
 
        elif opcao == 2:
            print("Você escolheu o menu de usuários!")
 
            opcao = 0
 
            while opcao != 5:
                print("""
                -----------------------------
                CADASTRO DE USUÁRIOS
 
                [1] Cadastrar
                [2] Listar
                [3] Atualizar
                [4] Remover
                [5] Voltar ao menu principal
                -----------------------------
                """)
                try:
                    opcao = int(input("Escolha uma opção: "))
 
                    if opcao == 1:
                        nome = input("Digite o nome: ").lower
                        idade = int(input("Digite a idade: "))
                        telefone = input("Digite o telefone: ").strip
 
                        usuario = {
                            "nome": nome,
                            "idade": idade,
                            "telefone": telefone
                        }
 
                        usuarios.append(usuario)
 
                        print("Usuário cadastrado com sucesso!")
 
                    elif opcao == 2:
                        try:
                            for x, i in enumerate(usuarios):
                                print(f"""
                                Usuário: {x + 1}
                                Nome: {i["nome"]}
                                Idade: {i["idade"]}
                                Telefone: {i["telefone"]}
                                """)
                        except:
                            print("\033[31mOPÇÃO INVALIDA\033[m")
                    elif opcao == 3:
                        try:
                            nomebusca_usuario = (input("Digite o usuario a ser atualizado: "))

                            lista_de_usuario = []
    
                            for x, i in enumerate(usuarios):
                                usuariovalidado = usuarios[x]["nome"]
                                lista_de_usuario.append(usuariovalidado)

                                if nomebusca_usuario in lista_de_usuario:

                                    opcaoattusuario = 0

                                    while opcaoattusuario != 4:
                                        print("""
                                        O que deseja atualizar?

                                        [1] Nome
                                        [2] Idade
                                        [3] Telefone
                                        [4] sair
                                        """)

                                        opcaoattusuario = int(input("Escolha uma opção: "))

                                        for x, i in enumerate(usuarios):
                                            if usuarios[x]["nome"] == nomebusca_usuario:

                                                if opcaoattusuario == 1:
                                                    novonomeusuario = input("Digite o novo nome usuario: ").lower
                                                    usuarios[x]["nome"] = novonomeusuario
                                                    nomebusca_usuario = novonomeusuario

                                                elif opcaoattusuario == 2:
                                                    novaidade = input("Digite a nova idade: ")
                                                    usuarios[x]["idade"] = novaidade

                                                elif opcaoattusuario == 3:
                                                    novotelefone = float(input("Digite o novo telefone: "))
                                                    usuarios[x]["telefone"] = novotelefone

                                                else:
                                                    print("Saindo da atualização...")

                                                break
                        except:
                            print("\033[31mOPÇÃO INVALIDA\033[m")
 
                    elif opcao == 4:
                         for x, i in enumerate(usuarios):
                            print(f"{x} {usuarios[x]["nome"]}")
           
                            deletarusuario = int(input("Digite O usuário a ser deletado: "))
                            usuarios.pop(deletarusuario)
 
                    elif opcao == 5:
                        print("Voltando ao menu principal...")
 
                    
                except:
                    print("\033[31mOPÇÃO INVALIDA\033[m")    
        elif opcao == 3:
            print("Encerrando o sistema...")
    except:
        print("\033[31mOPÇÃO INVALIDA\033[m")