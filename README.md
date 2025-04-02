Sistema de Gestão Posto de Gasolina (SGPG)
Equipe
Os desenvolvedores integrantes desse projeto são:

Elias da Costa Rodrigues
João Vitor Passos da Silva
José Fernando Bispo
Levi Ribeiro Santiago Mendonça
Pericles Maikon de Jesus Costa
Rafael Nascimento Andrade
Saula de Almeida

Instruções para desenvolvedores
Antes de inciar a instalação, certifique-se de ter o Python nas versões mais recentes instalados. Caso ainda não tenha instalado, abaixo estão os links para download: https://www.python.org/downloads/. Em seguida, basta clonar o repositório com git clone e seguir os passos seguintes.

Instalação do Backend
Para instalar todas as dependências do servidor use o com o comando no terminal:

python -m venv venv
Ative o ambiente virtual (Windows):

venv\Scripts\activate
O backend utiliza variáveis de ambiente para armazenar informações sensíveis ou específicas do ambiente. Crie um arquivo .env na pasta server com o seguinte conteúdo:

# Variáveis de ambiente para o banco de dados
DB_USER=<br/>
DB_PASSWORD=<br/>
DB_HOST=localhost<br/>
DB_PORT=5432<br/>
DB_NAME=<br/>

Observação: Certifique-se de preencher os valores pelas configurações adequadas ao seu ambiente.

Para iniciar o servidor Flask, execute o seguinte comando:

python api.py<br/>
Por padrão, o servidor estará disponível em http://localhost:5000.
