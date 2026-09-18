"""RF02 - Consulta de quantidade de vagas.

"Como usuário, eu quero visualizar a quantidade de vagas, para saber se o
estacionamento está lotado, principalmente no horário da manhã."
"""


def contar_vagas(vagas):
    """Retorna um dict com a contagem de vagas por status."""

    # Começamos com todos os contadores zerados.
    contagem = {
        "livre": 0,
        "ocupada": 0,
        "reservada": 0,
    }

    # Para cada vaga, descobrimos o status dela
    # e somamos 1 no contador correspondente.
    for vaga in vagas:
        status_da_vaga = vaga["status"]
        contagem[status_da_vaga] = contagem[status_da_vaga] + 1

    return contagem


def exibir_resumo_quantidade(vagas):
    """Imprime o resumo de quantidade de vagas e o total geral."""

    contagem = contar_vagas(vagas)
    total = len(vagas)

    quantidade_livres = contagem["livre"]
    quantidade_ocupadas = contagem["ocupada"]
    quantidade_reservadas = contagem["reservada"]

    print(f"Total de vagas: {total}")
    print(f"Livres: {quantidade_livres}")
    print(f"Ocupadas: {quantidade_ocupadas}")
    print(f"Reservadas: {quantidade_reservadas}")

    if quantidade_livres == 0:
        print("Estacionamento lotado!")
