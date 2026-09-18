"""RF03 - Sinalização de vagas reservadas.

"Como usuário, eu quero visualizar alertas e marcações claras sobre vagas
reservadas para funcionários (ex: biblioteca), para evitar estacionar em
locais não permitidos."
"""


def alertar_vagas_reservadas(vagas):
    """Imprime um alerta para cada vaga reservada, citando para quem é."""
    reservadas = [v for v in vagas if v["status"] == "reservada"]

    if not reservadas:
        print("Nenhuma vaga reservada nesta área.")
        return

    for vaga in reservadas:
        destino = vaga.get("reservada_para", "uso restrito")
        print(f"ALERTA: vaga {vaga['id']} ({vaga['local']}) é reservada para {destino}. Não estacione aqui.")
