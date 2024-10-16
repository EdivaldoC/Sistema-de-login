usuarios = {}
tentativa = 0

def mostrar_menu():
    print("\n1. Cadastro")
    print("2. Mostrar")
    print("3. Login")
    print("4. Sair")
    return int(input("Selecione uma das opções: "))

def cadastrar_usuario():
    nomeUsuario = input("Nome do usuário: ")
    senhaUsuario = int(input("Senha do usuário: "))
    if nomeUsuario in usuarios:
        print("Esse nome de usuário já existe")
    else:
        usuarios[nomeUsuario] = senhaUsuario
        print("\nUsuário cadastrado com sucesso!")

def mostrar_usuarios():
    if not usuarios:
        print("\nNenhum usuário encontrado")
    else:
        for nome, senha in usuarios.items():
            print(f"\nUsuário: {nome}\nSenha: {senha}")

def login():
    global tentativa
    nomeUsuario = input("Nome do usuário: ")
    senhaUsuario = int(input("Senha do usuário: "))
    
    if nomeUsuario in usuarios and usuarios[nomeUsuario] == senhaUsuario:
        print("\nLogin efetuado com sucesso!")
        tentativa = 0
    elif nomeUsuario not in usuarios:
        print("\nUsuário não cadastrado")
    else:
        tentativa += 1
        print(f"\nSenha incorreta. Tentativa {tentativa} de 3.")
        if tentativa == 3:
            print("Conta bloqueada após 3 tentativas erradas.")
            return False
    return True

while True:
    menu = mostrar_menu()
    
    while menu < 1 or menu > 4:
        menu = int(input("Opção inválida.\nSelecione uma opção de 1 a 4: "))

    if menu == 1:
        cadastrar_usuario()
    elif menu == 2:
        mostrar_usuarios()
    elif menu == 3:
        if not login():
            break
    elif menu == 4:
        print("\nSaindo...")
        break
