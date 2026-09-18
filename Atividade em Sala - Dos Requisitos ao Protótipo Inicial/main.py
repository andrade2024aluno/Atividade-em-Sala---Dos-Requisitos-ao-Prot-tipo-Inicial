"""
PLANO 
Requisitos escolhidos (ver requisitos.md para a descrição completa em forma
de user story, extraída do meu levantamento de requisitos):
  RF01 - Consulta de vagas disponíveis em tempo real
  RF02 - Consulta de quantidade de vagas
  RF03 - Sinalização de vagas reservadas

Uso de IA: opcional. Não utilizada na geração da lógica; usada apenas para
organizar a estrutura de arquivos e revisar o texto do README.
"""

from requisito1_vagas_disponiveis import listar_vagas_disponiveis
from requisito2_quantidade_vagas import exibir_resumo_quantidade
from requisito3_alerta_reservadas import alertar_vagas_reservadas


def main():
    # Simula o estado do estacionamento no horário de maior procura (manhã)
    vagas = [
        {"id": "A1", "local": "Bloco A - térreo", "status": "livre"},
        {"id": "A2", "local": "Bloco A - térreo", "status": "ocupada"},
        {"id": "B1", "local": "Biblioteca", "status": "reservada", "reservada_para": "Funcionários"},
        {"id": "B2", "local": "Biblioteca", "status": "livre"},
        {"id": "C1", "local": "Bloco C - subsolo", "status": "ocupada"},
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
até agora na faculdade nao foi ensinada, foi apenas mostra mas nao cobrado, 
entao eu meio que fui largado as traças pra ver oque poderia fazer, 
eu fiz usando os meu 3 requisitos da atividade passada.
Testei o codigo e funcionou .
"""
