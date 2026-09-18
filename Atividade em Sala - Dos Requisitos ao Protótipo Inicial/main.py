"""
PLANO

Requisitos escolhidos (ver requisitos.md para a descrição completa em forma
de user story, extraída do meu levantamento de requisitos):
  RF01 - Consulta de vagas disponíveis em tempo real
  RF02 - Consulta de quantidade de vagas
  RF03 - Sinalização de vagas reservadas

"""


from requisito1_vagas_disponiveis import listar_vagas_disponiveis
from requisito2_quantidade_vagas import exibir_resumo_quantidade
from requisito3_alerta_reservadas import alertar_vagas_reservadas


def main():
    # Simula o estado do estacionamento no horário de maior procura (manhã)
    vagas = [
        {
            "id": "A1",
            "local": "Bloco A - térreo",
            "status": "livre",
        },
        {
            "id": "A2",
            "local": "Bloco A - térreo",
            "status": "ocupada",
        },
        {
            "id": "B1",
            "local": "Biblioteca",
            "status": "reservada",
            "reservada_para": "Funcionários",
        },
        {
            "id": "B2",
            "local": "Biblioteca",
            "status": "livre",
        },
        {
            "id": "C1",
            "local": "Bloco C - subsolo",
            "status": "ocupada",
        },
    ]

    print("=== RF01: Consulta de vagas disponíveis em tempo real ===")
    listar_vagas_disponiveis(vagas, horario="manha")

    print("\n=== RF02: Consulta de quantidade de vagas ===")
    exibir_resumo_quantidade(vagas)

    print("\n=== RF03: Sinalização de vagas reservadas ===")
    alertar_vagas_reservadas(vagas)


if __name__ == "__main__":
    main()

"""
AutoAvaliação:

Esse codigo e foi basicamente feito na base da ia, Eu nunca usei python na vida, 
até agora na faculdade não foi ensinada, foi apenas mostra em poucos exemplos não cobrado, 
entao eu meio que fui largado as traças pra ver oque poderia fazer,
talves se fosse pedido para usar c/c++ eu até teria feito o codigo bem mais na moral ,
eu fiz usando os meu 3 requisitos da atividade passada então não foi nada tão bem feito,
a atividade da aula passada ja foi muito na pressa e essa mais ainda tentando aprender coisas que eu não sabia.
Testei o codigo e funcionou mas talvez tenha commitado meinho errado porque eu tambem uso bem pouco o git.
"""
