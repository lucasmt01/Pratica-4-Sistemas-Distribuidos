import grpc

import calculadora_pb2
import calculadora_pb2_grpc


def main():
    with grpc.insecure_channel("localhost:50051") as canal:
        calculadora = calculadora_pb2_grpc.CalculadoraStub(canal)
        operacoes = {
            "1": calculadora.Somar,
            "2": calculadora.Subtrair,
            "3": calculadora.Multiplicar,
            "4": calculadora.Dividir,
        }

        while True:
            print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair")
            opcao = input("Escolha a operação: ").strip()
            if opcao == "0":
                break
            if opcao not in operacoes:
                print("Opção inválida.")
                continue

            try:
                a = float(input("Informe a: "))
                b = float(input("Informe b: "))
                c = float(input("Informe c: "))
            except ValueError:
                print("Entrada inválida. Use números e ponto como separador decimal.")
                continue

            try:
                resposta = operacoes[opcao](
                    calculadora_pb2.Numeros(a=a, b=b, c=c), timeout=5
                )
                print(f"Resultado: {resposta.valor}")
            except grpc.RpcError as erro:
                print(f"Erro gRPC ({erro.code().name}): {erro.details()}")


if __name__ == "__main__":
    main()
