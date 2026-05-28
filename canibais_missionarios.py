TOTAL_CANIBAIS = 3
TOTAL_MISSIONARIOS = 3


OPERACOES = {
    "1MD": (0, 1, "D"),
    "2MD": (0, 2, "D"),
    "1CD": (1, 0, "D"),
    "2CD": (2, 0, "D"),
    "CMD": (1, 1, "D"),
    "1ME": (0, 1, "E"),
    "2ME": (0, 2, "E"),
    "1CE": (1, 0, "E"),
    "2CE": (2, 0, "E"),
    "CME": (1, 1, "E"),
}


def terminou(estado):
    canibais_esq, missionarios_esq, _ = estado
    return canibais_esq == 0 and missionarios_esq == 0


def estado_valido(estado):
    canibais_esq, missionarios_esq, _ = estado
    canibais_dir = TOTAL_CANIBAIS - canibais_esq
    missionarios_dir = TOTAL_MISSIONARIOS - missionarios_esq

    if not (0 <= canibais_esq <= TOTAL_CANIBAIS):
        return False
    if not (0 <= missionarios_esq <= TOTAL_MISSIONARIOS):
        return False

    if not (0 <= canibais_dir <= TOTAL_CANIBAIS):
        return False
    if not (0 <= missionarios_dir <= TOTAL_MISSIONARIOS):
        return False

    if missionarios_esq > 0 and canibais_esq > missionarios_esq:
        return False
    if missionarios_dir > 0 and canibais_dir > missionarios_dir:
        return False

    return True


def valida(estado, operacao):
    if operacao not in OPERACOES:
        return False, "operacao inexistente"

    canibais, missionarios, direcao = OPERACOES[operacao]
    canibais_esq, missionarios_esq, canoa_esq = estado
    canibais_dir = TOTAL_CANIBAIS - canibais_esq
    missionarios_dir = TOTAL_MISSIONARIOS - missionarios_esq
    passageiros = canibais + missionarios

    if passageiros < 1:
        return False, "a canoa precisa levar pelo menos 1 pessoa"
    if passageiros > 2:
        return False, "a canoa pode levar no maximo 2 pessoas"

    if direcao == "D" and not canoa_esq:
        return False, "a canoa nao esta no lado esquerdo"
    if direcao == "E" and canoa_esq:
        return False, "a canoa nao esta no lado direito"

    if direcao == "D":
        if canibais_esq < canibais or missionarios_esq < missionarios:
            return False, "nao ha pessoas suficientes no lado esquerdo"
        novo_estado = (
            canibais_esq - canibais,
            missionarios_esq - missionarios,
            False,
        )
    else:
        if canibais_dir < canibais or missionarios_dir < missionarios:
            return False, "nao ha pessoas suficientes no lado direito"
        novo_estado = (
            canibais_esq + canibais,
            missionarios_esq + missionarios,
            True,
        )

    if not estado_valido(novo_estado):
        return False, "o estado gerado deixa missionarios em desvantagem"

    return True, "operacao valida"


def mover(estado, operacao):
    valido, mensagem = valida(estado, operacao)

    if not valido:
        print(f"Operacao {operacao} invalida: {mensagem}")
        return estado

    canibais, missionarios, direcao = OPERACOES[operacao]
    canibais_esq, missionarios_esq, _ = estado

    if direcao == "D":
        return canibais_esq - canibais, missionarios_esq - missionarios, False

    return canibais_esq + canibais, missionarios_esq + missionarios, True


def imprimir_estado(passo, estado, operacao=None):
    canibais_esq, missionarios_esq, canoa_esq = estado
    canibais_dir = TOTAL_CANIBAIS - canibais_esq
    missionarios_dir = TOTAL_MISSIONARIOS - missionarios_esq
    canoa_dir = not canoa_esq
    status = "valido" if estado_valido(estado) else "invalido"
    objetivo = ", Objetivo Alcancado..." if terminou(estado) else ""
    texto_operacao = f" - {operacao}" if operacao else ""

    print(
        f"{passo:2}. "
        f"({canibais_esq}, {missionarios_esq}, {int(canoa_esq)}, "
        f"{canibais_dir}, {missionarios_dir}, {int(canoa_dir)})"
        f"{texto_operacao} | {status}{objetivo}"
    )


def executar_teste_de_mesa():
    estado = (3, 3, True)
    operacoes = [
        "CMD",
        "1ME",
        "2CD",
        "1CE",
        "2MD",
        "CME",
        "2MD",
        "1CE",
        "2CD",
        "1CE",
        "2CD",
    ]

    imprimir_estado(0, estado, operacoes[0])

    for passo, operacao in enumerate(operacoes, start=1):
        estado = mover(estado, operacao)
        proxima_operacao = operacoes[passo] if passo < len(operacoes) else None
        imprimir_estado(passo, estado, proxima_operacao)

    if terminou(estado):
        print("\nTodos os canibais e missionarios atravessaram com seguranca.")


def principal():
    executar_teste_de_mesa()


if __name__ == "__main__":
    principal()
