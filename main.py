import hashlib
import getpass

ARQUIVO_USUARIOS = 'usuarios.txt'


def menu():
    print('\n' + '-' * 30)
    print('SISTEMA DE ACESSO')
    print('-' * 30)
    print('1 - cadastrar novo usuario')
    print('2 - acessar o sistema')
    print('3 - sair')
    print('-' * 30)
    return input('Escolha uma opção: ')


def cadastrar():
    usuario = input('Digite o nome do usuario: ').strip()
    senha = getpass.getpass('Digite a senha: ').strip()

    if not usuario or not senha:
        print('Usuario e senha não podem ser vazios.')
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    try:
        with open(ARQUIVO_USUARIOS, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(':')
                if len(partes) == 2:
                    usuario_arquivo, _ = partes

                    if usuario == usuario_arquivo:
                        print('Usuario já existe.')
                        return

    except FileNotFoundError:
        pass

    with open(ARQUIVO_USUARIOS, 'a') as arquivo:
        arquivo.write(f'{usuario}:{senha_hash}\n')

    print('Usuario cadastrado com sucesso!')


def login():
    usuario = input('Digite o nome do usuario: ').strip()
    senha = getpass.getpass('Digite a senha: ').strip()

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    encontrado = False

    try:
        with open(ARQUIVO_USUARIOS, 'r') as arquivo:

            for linha in arquivo:
                partes = linha.strip().split(':')

                if len(partes) == 2:
                    usuario_arquivo, senha_arquivo = partes

                    if (
                        usuario == usuario_arquivo
                        and senha_hash == senha_arquivo
                    ):
                        encontrado = True
                        break

    except FileNotFoundError:
        print('Nenhum usuario cadastrado ainda.')
        return

    if encontrado:
        print('Bem-vindo ao sistema!')
    else:
        print('Usuario ou senha incorretos.')


def iniciar():
    while True:
        opcao = menu()

        if opcao == '1':
            cadastrar()

        elif opcao == '2':
            login()

        elif opcao == '3':
            print('Saindo do sistema. Até logo!')
            break

        else:
            print('Opção inválida.')


if __name__ == '__main__':
    iniciar()


    


    