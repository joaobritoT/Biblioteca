import json
import customtkinter
from classe import Usuario
import webbrowser

customtkinter.set_appearance_mode("light")


def principal(usuario,senha):
    tela_principal = customtkinter.CTk()
    tela_principal.geometry("350x300")
    tela_principal.iconbitmap("livro.ico")
    tela_principal.title("Biblioteca do João")
    current_usuario = usuario
    password = senha
    lbl = customtkinter.CTkLabel(tela_principal,text="Bem-vindo(a) {}".format(usuario),font=("Arial",22,"bold"))
    lbl.pack(padx=5, pady=5)
    lbl2 = customtkinter.CTkLabel(tela_principal,text="Digite o livro que deseja cadastrar",font=("Arial",15,))
    lbl2.pack(padx=5, pady=5)
    entrada_livro = customtkinter.CTkEntry(tela_principal,placeholder_text="Nome do livro:",width=250,font=("Arial",15,"bold"),placeholder_text_color="#3b3b3b")
    entrada_livro.pack(padx=5,pady=5)
    def cadastrar_livro():
        def carregar_dados():
            with open('dados.json', 'r') as arquivo:
                dados = json.load(arquivo)
            return dados

# Função para salvar os dados no arquivo JSON
        

# Função para adicionar um livro ao usuário logado
        def adicionar_livro(usuario, livro):
            dados_atualizados = carregar_dados()
            def salvar_dados(dados_atualizadoss):
                with open('dados.json', 'w') as arquivo:
                    json.dump(dados_atualizados, arquivo, indent=2)
            for elemetos in dados_atualizados:

                if elemetos['nome'] == usuario:
                    if livro != "":
                        elemetos["livros"].append(livro)
                        dados_atualizadoss = dados_atualizados
                        salvar_dados(dados_atualizadoss)
                        print(f"Livro '{livro}' adicionado com sucesso para o usuário '{usuario}'.")
                        lbl_confirmacao_livro.configure(text="Livro adicionado com sucesso")
                        lbl_confirmacao_livro.configure(text_color="green",font=("Arial",18,"bold"))
                        lbl_confirmacao_livro.pack(padx=10,pady=10)
                    else:
                        lbl_confirmacao_livro.configure(text="Digite um livro valido")
                        lbl_confirmacao_livro.configure(text_color="red",font=("Arial",18,"bold"))
                        lbl_confirmacao_livro.pack(padx=10,pady=10)
                    break
                else:
                    print(f"Usuário '{usuario}' não encontrado.")
                    print(current_usuario)
                
        
        usuario_logado = current_usuario 
        livro_a_adicionar = entrada_livro.get()
        adicionar_livro(usuario_logado, livro_a_adicionar)
        entrada_livro.delete("0","end")


    def listagem():
            def carregar_dados():
                    with open('dados.json', 'r') as arquivo:
                        dados = json.load(arquivo)
                    return dados

            def ver_livros(usuario):
                dados_atualizados = carregar_dados()
                tela_listagem = customtkinter.CTk()
                tela_listagem.iconbitmap("livro.ico")
                tela_listagem.title("Biblioteca do João")
                frame = customtkinter.CTkScrollableFrame(tela_listagem,width=350,height=450,fg_color="white")
                frame.pack()
                tiuto = customtkinter.CTkLabel(frame,text="Meus livros: ",font=("Arial",25,"bold"))
                tiuto.pack(padx=10, pady=10)
                def mais_infos(livro):
                        print(livro)
                        new = 2
                        url ="https://www.goodreads.com/search?&query={}".format(livro.replace(' ','+').lower())
                        webbrowser.open(url,new=new)
                        print("livro que vou pesquisar: {}".format(livro))
                def deletar_livro(livro):
                    def carregar_dados():
                        with open('dados.json', 'r') as arquivo:
                            dados = json.load(arquivo)
                        return dados
                    dados_velhos = carregar_dados()
                    for elemetos in dados_velhos:
                        livross = elemetos['livros']
                        if elemetos['nome'] == current_usuario:
                            livross.remove(livro)
                            break
                    with open('dados.json','w') as file:
                        json.dump(dados_velhos,file,indent=2)
                    print("deletado")
                    tela_confirmacao_deletar_livro = customtkinter.CTk()
                    tela_confirmacao_deletar_livro.geometry("200x80")
                    tela_confirmacao_deletar_livro.iconbitmap("livro.ico")
                    tela_confirmacao_deletar_livro.title("Biblioteca do João")
                    lbl = customtkinter.CTkLabel(tela_confirmacao_deletar_livro,text="Livro deletado com sucesso!",wraplength=150,font=("Arial",16,"bold"),text_color="green")
                    lbl.pack(padx=10,pady=10)
                    tela_listagem.withdraw()
                    tela_confirmacao_deletar_livro.mainloop()
                for elemetos in dados_atualizados:
                    if elemetos['nome'] == usuario:
                        
                        for livros in elemetos['livros']:
                            linha = customtkinter.CTkLabel(frame, text="="*110,height=1,font=("Arial",5))
                            linha.pack(padx=10,pady=10)
                            label = customtkinter.CTkLabel(frame,text="{}".format(livros),font=("Arial",20,"bold"))
                            infos_livros = customtkinter.CTkButton(frame,text="Mais informações",command=lambda l=livros:mais_infos(l),font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=200,corner_radius=5,text_color="#DEEFE7")
                            btn_deletar_livro = customtkinter.CTkButton(frame,text="Deletar livro",command=lambda ll=livros:deletar_livro(ll),fg_color="#BD2A2E",text_color="white",width=200,corner_radius=5,font=("Arial",18,"bold"),hover_color="#FF4858")
                            label.pack()
                            infos_livros.pack(padx=5,pady=5)
                            btn_deletar_livro.pack(padx=5,pady=5)
                        break
                tela_listagem.mainloop()
            ver_livros(current_usuario)

    def Sair():
        current_usuario = None
        tela_principal.withdraw()
        main.deiconify()
 

    
          
    btn_cadastrar_livro = customtkinter.CTkButton(tela_principal,text="cadastrar livro", command=cadastrar_livro,font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_cadastrar_livro.pack(padx=5,pady=5)
    lbl_confirmacao_livro = customtkinter.CTkLabel(tela_principal,text="")
    btn_listar_livros = customtkinter.CTkButton(tela_principal,text="Ver meus livros",command=listagem,font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_listar_livros.pack(padx=5,pady=5)
    btn_sair = customtkinter.CTkButton(tela_principal,text="Sair",command=Sair,fg_color="#BD2A2E",text_color="white",width=210,corner_radius=20,font=("Arial",18,"bold"),hover_color="#FF4858")
    btn_sair.pack(padx=10,pady=10)


    tela_principal.mainloop()


def tela_login():
    tela_login = customtkinter.CTk()
    tela_login.geometry("300x250")
    tela_login.iconbitmap("livro.ico")
    tela_login.title("Biblioteca do João")
    lbllogin = customtkinter.CTkLabel(tela_login,text="Faça seu login",font=('Arial',20,"bold"),text_color="#002333")
    lbllogin.pack(padx=5, pady=5)
    entrada_user = customtkinter.CTkEntry(tela_login,placeholder_text="Nome:",width=250,font=("Arial",15,"bold"),placeholder_text_color="#3b3b3b")
    entrada_user.pack(padx=5,pady=5)
    entrada_senha_login = customtkinter.CTkEntry(tela_login,placeholder_text="Senha:",width=250,font=("Arial",15,"bold"),placeholder_text_color="#3b3b3b",show="*")
    entrada_senha_login.pack(padx=5,pady=5)
    def logar():
        usuario = entrada_user.get()
        senha = entrada_senha_login.get()

        def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
        nome_arquivo = "dados.json"
        dados_atualizados = carregar_dados(nome_arquivo)
        achei = False
        current_usuario = None
        for elemetos in dados_atualizados:
            if elemetos['nome'].lower() == usuario.lower() and elemetos['senha'].lower() == senha.lower():
                achei = True
                current_usuario = elemetos['nome']
                break
             
            else:
                achei = False
        if achei == True:
            tela_login.withdraw()
            principal(current_usuario,senha)
            
        else:
            print("nao achei")
            lbllogin_erro.configure(text='Usuario ou senha invalidos')
        
    def voltar():
        tela_login.withdraw()
        main.deiconify()

    main.withdraw()
    btn_login = customtkinter.CTkButton(tela_login,text="Entrar",command=logar,font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_login.pack(padx=10,pady=10)
    btn_voltar = customtkinter.CTkButton(tela_login,text="Voltar",command=voltar,font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_voltar.pack()
    lbllogin_erro = customtkinter.CTkLabel(tela_login,text='',font=("Arial",15,"bold"),text_color="red")
    lbllogin_erro.pack(padx=10,pady=10)

    tela_login.mainloop()

def tela_cadastro():
    cadastro = customtkinter.CTk()
    cadastro.geometry("300x250")
    cadastro.iconbitmap("livro.ico")
    cadastro.title("Biblioteca do João")
    lblcadastro = customtkinter.CTkLabel(cadastro,text ="Digite suas informacões",font=('Arial',20,"bold"),text_color="#002333")
    lblcadastro.pack(padx = 5, pady = 5)
    entrada_nome = customtkinter.CTkEntry(cadastro,placeholder_text="Nome:",width=250,font=("Arial",15,"bold"),placeholder_text_color="#3b3b3b")
    entrada_nome.pack(padx=5, pady=5)
    entrada_senha = customtkinter.CTkEntry(cadastro,placeholder_text="Senha:",width=250,font=("Arial",15,"bold"),placeholder_text_color="#3b3b3b",show="*")
    entrada_senha.pack(padx=5, pady=5)

    def cadastrar():
        nome = entrada_nome.get()
        senha = entrada_senha.get()

        user = Usuario(nome, senha)

        def carregar_dados(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
            except FileNotFoundError:
                dados = []
            return dados
        

        def salvar_dados(nome_arquivo, novos_dados):
            dados_existentes = carregar_dados(nome_arquivo)
            dados_existentes.append(novos_dados)

            with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados_existentes, arquivo, indent=2)
        nome_arquivo = "dados.json"
        dados_atualizados = carregar_dados(nome_arquivo)
        adiconado = False
        for elemetos in dados_atualizados:
            if elemetos['nome'].lower() == user.Nome.lower() or nome == '' or senha == '':
                adiconado = True
                break
                
            else:
                adiconado = False
        if adiconado == True:
            print("ja adicionado")
            lbl_ja_cadastrado.configure(text="Informações inválidas, tente novamente")
        else:

            salvar_dados(nome_arquivo,{
                "nome":user.Nome,
                "senha":user.Senha,
                "livros":user.Livros
            })
            tela_confirmacao_cadastro = customtkinter.CTk()
            tela_confirmacao_cadastro.geometry("200x80")
            tela_confirmacao_cadastro.title("Biblioteca do João")
            tela_confirmacao_cadastro.iconbitmap("livro.ico")
            lbl_confirmacao = customtkinter.CTkLabel(tela_confirmacao_cadastro,text="Usuario cadastrado com sucesso!",wraplength=150,font=("Arial",16,"bold"),text_color="green")
            lbl_confirmacao.pack(padx=10,pady=10)
            cadastro.withdraw()
            main.deiconify()
            tela_confirmacao_cadastro.mainloop()
    

    def voltar():
        cadastro.withdraw()
        main.deiconify()

    btn_cadastrar = customtkinter.CTkButton(cadastro,text="cadastrar",command=cadastrar,font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_cadastrar.pack(padx=5,pady=5)
    btn_voltar = customtkinter.CTkButton(cadastro,text="voltar",command=voltar,font=("Arial",18,"bold"),fg_color="#159A9C",hover_color="#002333",width=230,corner_radius=20,text_color="#DEEFE7")
    btn_voltar.pack(padx=5,pady=5)
    lbl_ja_cadastrado = customtkinter.CTkLabel(cadastro,text="",font=("Arial",15,"bold"),text_color="red")
    lbl_ja_cadastrado.pack(padx=10,pady=10)
    main.withdraw()
    cadastro.mainloop()

def acervo():
    new = 2
    url = "https://minhabiblioteca.com.br/"
    webbrowser.open(url,new=new)

main = customtkinter.CTk()
main.geometry("370x250")
main.title("Biblioteca do João")
main.iconbitmap("livro.ico")
lbl = customtkinter.CTkLabel(main,text ="Biblioteca do João",font=('Arial',26,"bold"))
lbl.pack(padx = 5, pady = 5)
lblcadastro = customtkinter.CTkLabel(main,text ="Cadastre-se ou entre",font=("Arial",16,"bold"),text_color="#3b3b3b")
lblcadastro.pack(padx=5, pady = 5)
btncadastro = customtkinter.CTkButton(main,text="Cadastre-se",command=tela_cadastro,font=("Arial",18,"bold"),fg_color="#002333",hover_color="#159A9C",width=270,corner_radius=20,text_color="white")
btncadastro.pack(padx= 5,pady=5)
btnlogin = customtkinter.CTkButton(main,text="Entrar",command=tela_login,font=("Arial",18,"bold"),fg_color="#002333",hover_color="#159A9C",width=270,corner_radius=20,text_color="white")
btnlogin.pack(padx=5,pady=5)
lbl_ou = customtkinter.CTkLabel(main, text="Ou",font=("Arial",16,"bold"),text_color="#3b3b3b")
lbl_ou.pack(padx=5,pady=5)
btn_acervo = customtkinter.CTkButton(main,text="Abrir acervo digital",command=acervo,font=("Arial",18,"bold"),fg_color="#B4BEC9",hover_color="#FFFFFF",width=270,corner_radius=20,text_color="#002333")
btn_acervo.pack()
main.mainloop()