"""RF01 - Consulta de vagas disponíveis em tempo real.

"Como usuário, eu quero visualizar a localização de vagas disponíveis em
tempo real, para encontrar um lugar para estacionar rapidamente."
"""


def listar_vagas_disponiveis(vagas, horario=None):
    """Imprime as vagas com status 'livre', com destaque se for horário de pico.

    `vagas` é uma lista de dicts: {"id": str, "local": str, "status": str}.
    `horario` é opcional, ex.: "manha", usado apenas para o aviso de contexto.
    """

    # Passo 1: separar só as vagas que estão livres.
    # Em vez de fazer isso em uma linha só, vamos com um laço explícito
    # pra ficar mais fácil de ler.
    livres = []
    for vaga in vagas:
        if vaga["status"] == "livre":
            livres.append(vaga)

    # Passo 2: se for horário de manhã, mostrar um aviso extra.
    if horario == "manha":
        print("(Horário de manhã - período de maior procura)")

    # Passo 3: se não sobrou nenhuma vaga livre, avisar e parar por aqui.
    if not livres:
        print("Nenhuma vaga disponível no momento.")
        return

    # Passo 4: se sobrou vaga livre, listar cada uma.
    print("Vagas disponíveis agora:")
    for vaga in livres:
        identificador = vaga["id"]
        local = vaga["local"]
        print(f"- {identificador} ({local})")
