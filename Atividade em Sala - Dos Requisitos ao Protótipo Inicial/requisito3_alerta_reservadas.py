"""RF03 - Sinalização de vagas reservadas.

"Como usuário, eu quero visualizar alertas e marcações claras sobre vagas
reservadas para funcionários (ex: biblioteca), para evitar estacionar em
locais não permitidos."
"""


def alertar_vagas_reservadas(vagas):
    """Imprime um alerta para cada vaga reservada, citando para quem é."""

    # Passo 1: separar só as vagas marcadas como reservadas.
    reservadas = []
    for vaga in vagas:
        if vaga["status"] == "reservada":
            reservadas.append(vaga)

    # Passo 2: se não tem nenhuma vaga reservada, só avisa e sai.
    if not reservadas:
        print("Nenhuma vaga reservada nesta área.")
        return

    # Passo 3: para cada vaga reservada, monta e imprime o alerta.
    for vaga in reservadas:
        identificador = vaga["id"]
        local = vaga["local"]

        # Nem toda vaga reservada tem o campo "reservada_para" preenchido,
        # então usamos um valor padrão caso ele não exista.
        destino = vaga.get("reservada_para", "uso restrito")

        print(
            f"ALERTA: vaga {identificador} ({local}) "
            f"é reservada para {destino}. Não estacione aqui."
        )
