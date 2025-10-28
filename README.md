🏦 Desafio: Sistema Bancário em Python

Projeto desenvolvido como parte do Bootcamp Luizalabs na DIO (Digital Innovation One).
O objetivo é criar um sistema de conta bancária simples, totalmente em Python, que permite realizar operações básicas como cadastro de usuários, criação de contas, depósitos, saques e emissão de extratos.


💡 Contexto do Projeto
O foco está em desenvolver funções bem estruturadas e um fluxo de controle claro, simulando o funcionamento básico de um banco.
O sistema foi construído com base em boas práticas de código, legibilidade e uso de funções com parâmetros posicionais e nomeados, além de documentação linha a linha para facilitar o entendimento.

⚙️ Funcionalidades

✅ Criar novos usuários (com nome, CPF, data de nascimento e endereço)
✅ Criar contas bancárias associadas a um usuário existente
✅ Realizar depósitos
✅ Efetuar saques com limite de valor e quantidade de operações
✅ Exibir o extrato completo com histórico das movimentações
✅ Menu interativo com controle de opções
✅ Mensagens claras de erro e sucesso

💻 Estrutura do Código

O sistema é dividido em funções independentes:
menu() → Exibe o menu principal e coleta a opção do usuário
criar_usuario() → Cadastra um novo usuário no sistema
validar_cpf() → Verifica se o CPF informado já existe
criar_conta() → Cria uma nova conta bancária vinculada a um usuário existente
depositar() → Realiza depósitos e atualiza o extrato
sacar() → Executa saques com controle de limites
mostrar_extrato() → Exibe o saldo e todas as movimentações
main() → Controla o fluxo principal do programa

🧠 Conceitos Aplicados

Estruturas de dados: listas e dicionários
Controle de fluxo: condicionais e laços de repetição
Funções com parâmetros posicionais, nomeados e somente posicionais (/, *)
Boas práticas de código (PEP8, comentários explicativos e organização funcional)
Simulação de operações bancárias reais
