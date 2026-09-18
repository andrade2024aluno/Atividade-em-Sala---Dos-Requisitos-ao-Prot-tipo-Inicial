"""RF01 - Consulta de vagas disponíveis em tempo real.

"Como usuário, eu quero visualizar a localização de vagas disponíveis em
tempo real, para encontrar um lugar para estacionar rapidamente."
"""


def listar_vagas_disponiveis(vagas, horario=None):
    """Imprime as vagas com status 'livre', com destaque se for horário de pico.

    `vagas` é uma lista de dicts: {"id": str, "local": str, "status": str}.
    `horario` é opcional, ex.: "manha", usado apenas para o aviso de contexto.
    """
    livres = [v for v in vagas if v["status"] == "livre"]

    if horario == "manha":
        print("(Horário de manhã - período de maior procura)")

    if not livres:
        print("Nenhuma vaga disponível no momento.")
        return

    print("Vagas disponíveis agora:")
    for vaga in livres:
        print(f"- {vaga['id']} ({vaga['local']})")
