class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, no):
        no.next = self.top
        self.top = no
        self.size += 1

    def __str__(self):
        if self.top is not None:
            no = self.top
            pilha_listagem = []
            while no is not None:
                pilha_listagem.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(pilha_listagem)
        else:
            return "a pilha está vazia"

    def pop(self):
        if self.size > 0:
            no = self.top
            self.top = self.top.next
            self.size -= 1
            return no
        else:
            return None

    def topo(self):
        if self.top is not None:
            return self.top.valor
        else:
            return None
        
    def tamanho(self):
        return self.size


def calcular_posfixa_com_pilha_ligada(expressao):
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    pilha = Pilha()
    tokens = expressao.split()

    for token in tokens:
        if token in operadores:
            b = pilha.pop()
            a = pilha.pop()
            if a is None or b is None:
                raise ValueError("Expressão inválida: operandos insuficientes")
            resultado = operadores[token](a.valor, b.valor)
            pilha.push(No(resultado))
        else:
            try:
                pilha.push(No(float(token)))
            except ValueError:
                raise ValueError(f"Valor inválido: {token}")

    if pilha.tamanho() != 1:
        raise ValueError("Expressão inválida: operandos ou operadores sobrando")

    return pilha.pop().valor


# Programa principal
if __name__ == "__main__":
    print("\nCalculadora de Notação Polonesa\n")
    print("Digite com espaço entre os caracteres")
    print("Digite 'sair' para encerrar.\n")

    while True:
        expressao = input("Digite a expressão: ")
        if expressao.lower() == "sair":
            print("Encerrando...")
            break
        try:
            resultado = calcular_posfixa_com_pilha_ligada(expressao)
            print("Resultado:", resultado)
        except Exception as e:
            print("Erro:", e)
