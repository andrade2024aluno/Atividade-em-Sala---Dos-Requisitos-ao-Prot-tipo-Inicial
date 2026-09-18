"""RF02 - Consulta de quantidade de vagas.

"Como usuário, eu quero visualizar a quantidade de vagas, para saber se o
estacionamento está lotado, principalmente no horário da manhã."
"""


def contar_vagas(vagas):
    """Retorna um dict com a contagem de vagas por status."""
    contagem = {"livre": 0, "ocupada": 0, "reservada": 0}
    for vaga in vagas:
        contagem[vaga["status"]] = contagem.get(vaga["status"], 0) + 1
    return contagem


def exibir_resumo_quantidade(vagas):
    """Imprime o resumo de quantidade de vagas e o total geral."""
    contagem = contar_vagas(vagas)
    total = len(vagas)
    print(f"Total de vagas: {total}")
    print(f"Livres: {contagem['livre']} | Ocupadas: {contagem['ocupada']} | Reservadas: {contagem['reservada']}")

    if contagem["livre"] == 0:
        print("Estacionamento lotado!")
