# Calculadora com gRPC e Python

Atividade de Sistemas Distribuídos: um cliente de terminal envia três números
para um servidor gRPC e recebe o resultado da operação escolhida.

## Instalação

Requer Python 3.10 ou superior. Execute os comandos na pasta do projeto.

Crie um ambiente virtual:

```sh
python -m venv .venv
```

Ative no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Ou no Linux/macOS:

```sh
source .venv/bin/activate
```

Instale as dependências:

```sh
python -m pip install -r requirements.txt
```

## Gerar os arquivos do Protocol Buffers

```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
```

O comando gera `calculadora_pb2.py` (mensagens) e `calculadora_pb2_grpc.py`
(classes de comunicação gRPC). Execute-o novamente sempre que alterar o `.proto`.
Esses arquivos são gerados automaticamente e não devem ser editados manualmente.

## Executar

Em um terminal com o ambiente virtual ativo, inicie o servidor:

```sh
python servidor.py
```

Em outro terminal, na mesma pasta e com o ambiente virtual ativo, execute:

```sh
python cliente.py
```

O serviço usa `localhost:50051`. No cliente, escolha a operação e informe
`a`, `b` e `c` (use ponto para números decimais). Digite `0` no menu para sair.
Para encerrar o servidor, pressione `Ctrl+C`.

## Operações e verificação manual

Use `a = 24`, `b = 4` e `c = 2`:

| Opção | Operação | Resultado esperado |
| --- | --- | --- |
| 1 | `a + b + c` | `30.0` |
| 2 | `a - b - c` | `18.0` |
| 3 | `a * b * c` | `192.0` |
| 4 | `a / b / c` | `3.0` |

A subtração e a divisão são calculadas da esquerda para a direita.
Na divisão, se `b` ou `c` for zero, o servidor interrompe a chamada com
`grpc.StatusCode.INVALID_ARGUMENT` e o cliente exibe o erro recebido.
O valor `a = 0` é permitido.

## Estrutura

- `calculadora.proto`: contrato do serviço, com quatro métodos e mensagens com números `double`.
- `servidor.py`: implementação das operações e tratamento de divisão por zero.
- `cliente.py`: menu de terminal, envio dos números e exibição do resultado ou erro.
- `calculadora_pb2.py` e `calculadora_pb2_grpc.py`: código gerado pelo compilador.
- `requirements.txt`: dependências Python.
- `.gitignore`: exclui o ambiente virtual e os caches do controle de versão.

Referências: [guia Python do gRPC](https://grpc.io/docs/languages/python/quickstart/)
e [códigos de status do gRPC](https://grpc.io/docs/guides/status-codes/).
