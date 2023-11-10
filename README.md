# README - Landing Page Customizável com Python, Flask e MySQL

## Sumário

- [Visão Geral](#visão-geral)
- [Requisitos](#requisitos)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Executando o Projeto](#executando-o-projeto)
- [Personalização da Landing Page](#personalização-da-landing-page)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

Este projeto tem como objetivo criar uma Landing Page personalizável que permite a coleta de dados de um formulário e a exibição desses dados em uma página HTML. O desenvolvimento é baseado em Python, utilizando o microframework Flask para criar o servidor web e a biblioteca mysql-connection para se comunicar com um banco de dados MySQL.

## Requisitos

Para executar este projeto, você precisará ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.x
- Flask
- MySQL
- mysql-connection
- Um navegador da web moderno

## Configuração do Ambiente

1. **Instalar o Python 3.x:** Se ainda não tiver o Python instalado, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. **Instalar o Flask:** Use o gerenciador de pacotes pip para instalar o Flask com o seguinte comando:

```
pip install flask
```
3. **Instalar o MySQL:** Instale o MySQL no seu sistema. Você pode usar o [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) ou um serviço de banco de dados MySQL hospedado na nuvem.

4. **Instalar o mysql-connection:** Você pode instalá-lo usando pip:

```
pip install mysql-connector-python
```
5. **Configurar o banco de dados MySQL:** Crie um banco de dados e uma tabela para armazenar os dados do formulário. Atualize as informações de configuração no arquivo `TCC.py` com as credenciais do seu banco de dados.

## Executando o Projeto

Para executar o projeto, siga estas etapas:

1. Navegue até o diretório raiz do projeto:


2. Inicie o servidor Flask executando o seguinte comando:


3. Abra seu navegador e acesse `http://localhost:5000` para visualizar a Landing Page personalizável.

## Personalização da Landing Page

Você pode personalizar a Landing Page editando o arquivo `templates/site.html`. Você pode adicionar HTML, CSS e JavaScript para personalizar a aparência e o comportamento da página. Os dados do formulário serão exibidos onde você definir as tags apropriadas no arquivo HTML.

## Estrutura de Arquivos

A estrutura de arquivos do projeto é organizada da seguinte maneira:

seu-diretorio-do-projeto/
├── app.py
├── templates/
│ └── site.html
├── static/
│ └── (arquivos estáticos, como CSS e JavaScript)
└── README.md


## Contribuição

Se você deseja contribuir para o projeto ou relatar problemas, sinta-se à vontade para criar um pull request ou abrir uma issue no repositório do projeto.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes sobre os termos da licença.

---

Aproveite o desenvolvimento do seu TCC e não hesite em entrar em contato caso precise de ajuda adicional ou esclarecimento de dúvidas. Boa sorte com o seu trabalho!
