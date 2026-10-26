from concurrent import futures

import grpc

import calculadora_pb2
import calculadora_pb2_grpc


class Calculadora(calculadora_pb2_grpc.CalculadoraServicer):
    def Somar(self, request, context):
        return calculadora_pb2.Resultado(valor=request.a + request.b + request.c)

    def Subtrair(self, request, context):
        return calculadora_pb2.Resultado(valor=request.a - request.b - request.c)

    def Multiplicar(self, request, context):
        return calculadora_pb2.Resultado(valor=request.a * request.b * request.c)

    def Dividir(self, request, context):
        if request.b == 0 or request.c == 0:
            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Divisão por zero: b e c devem ser diferentes de zero.",
            )
        return calculadora_pb2.Resultado(valor=request.a / request.b / request.c)


def main():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(Calculadora(), servidor)
    servidor.add_insecure_port("localhost:50051")
    servidor.start()
    print("Servidor gRPC iniciado em localhost:50051. Encerre com Ctrl+C.")
    try:
        servidor.wait_for_termination()
    except KeyboardInterrupt:
        servidor.stop(0).wait()


if __name__ == "__main__":
    main()
