"""
PLANO (Passo 1 - 5 minutos)

Requisitos escolhidos (ver requisitos.md para a descrição completa em forma
de user story, extraída do meu levantamento de requisitos):
  RF01 - Consulta de vagas disponíveis em tempo real
  RF02 - Consulta de quantidade de vagas
  RF03 - Sinalização de vagas reservadas

Ordem de implementação (do mais simples ao mais complexo):
  1) RF01  ~15 min  (listar vagas livres)
  2) RF02  ~15 min  (contar vagas por status)
  3) RF03  ~15 min  (alertar sobre vagas reservadas)
  (README e autoavaliação nos 15 min finais)

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
AUTOAVALIAÇÃO (Passo 3 - 5 minutos)

Critérios atingidos: 1, 2, 3, 4, 5 e 6 (lista de requisitos, um arquivo por
requisito, ponto de entrada único, mais de três commits identificando cada
etapa, README com até dez linhas, e saída no terminal comprovando cada
requisito).

Requisito mais difícil de traduzir em código: RF01, porque no meu
levantamento original "tempo real" e "horário da manhã" eram só menções em
texto livre, sem definição de dado. Precisei decidir, na hora de codificar,
que "tempo real" seria simulado como um snapshot fixo do estacionamento
(dict com status por vaga) e que "horário da manhã" seria só um parâmetro
de contexto, não uma integração com relógio de verdade — isso só ficou
claro quando fui escrever a função.

Uso de IA: não foi necessário para a lógica; usaria, se fosse o caso, para
revisar a redação das user stories.
"""
