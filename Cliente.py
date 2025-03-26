import socket

HOST = "127.0.0.1"
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Handshake inicial
operacao = input("Digite:\n1 - Modo Seguro\n2 - Modo com perda de pacotes\n3 - Modo com erro nos pacotes\n--> ")

if operacao == "1":
    tamanho_max_mensagem = int(input("Digite o tamanho máximo da mensagem: "))
    mensagem = input("Digite a mensagem a ser enviada: ")

    if len(mensagem) > tamanho_max_mensagem:
        print("Erro: A mensagem excede o tamanho máximo permitido!")
    else:
        # Enviar handshake informando o tamanho fixo do pacote
        client_socket.sendall("SEGURO,3".encode())
        print(f"Resposta do servidor: {client_socket.recv(1024).decode()}")

        # Enviar mensagem dividida em pacotes
        tamanho_pacote = 3
        for i, carga in enumerate([mensagem[j:j+tamanho_pacote] for j in range(0, len(mensagem), tamanho_pacote)], start=1):
            pacote = f"{i:02d}S{carga}"
            client_socket.sendall(pacote.encode())
            print(f"Enviado pacote: {pacote}")

        client_socket.sendall("FIM".encode())  # Sinal de fim
    client_socket.close()

elif operacao in ["2", "3"]:
    print("Funcionalidade em desenvolvimento, volte mais tarde!")

else:
    print("Opção inválida!")