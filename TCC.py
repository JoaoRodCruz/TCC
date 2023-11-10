from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Função para estabelecer uma conexão com o banco de dados MySQL
def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1253',
            database='tcc'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o banco de dados: {err}")
        return None


# Ligação das respostas recebidas no formulário com o banco de dados MySQL
@app.route('/tcc', methods=['GET', 'POST'])
def processar_formulario():
    if request.method == 'POST':
        # Obtenha os dados do formulário
        frase_inicial = request.form['frase-inicial']
        frase_secundaria = request.form['frase-secundaria']
        sobre_empresa = request.form['sobre_empresa']
        sobre_produto = request.form['sobre_produto']
        produto1 = request.form['produto1']
        preco1 = request.form['preco1']
        produto2 = request.form['produto2']
        preco2 = request.form['preco2']
        produto3 = request.form['produto3']
        preco3 = request.form['preco3']

        conn = conectar_bd()

        if conn:
            cursor = conn.cursor()

            insert_query = "INSERT INTO formulario (frase_inicial, frase_sec, sobre_empresa, sobre_produto, produto1, preco1, produto2, preco2, produto3, preco3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (frase_inicial, frase_secundaria, sobre_empresa, sobre_produto, produto1, preco1, produto2, preco2, produto3, preco3))

            conn.commit()
            conn.close()

            return "Dados inseridos com sucesso!"

        return "Erro no envio do formulário."
    else:
        # Retornar um formulário HTML para preenchimento
        return render_template('forms.html')


# Função para recuperar dados do banco de dados MySQL
def recuperar_dados_do_banco():
    try:
        connection = conectar_bd()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT frase_inicial, frase_sec, sobre_empresa, sobre_produto, produto1, preco1, produto2, preco2, produto3, preco3 FROM formulario")
            dados = cursor.fetchone()  # Supondo que você deseja apenas um registro
            connection.close()
            return dados
        return None
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o banco de dados: {err}")
        return None

# Ligação dos dados recuperados no banco de dados MySQL com a Landing Page finalizada
@app.route('/visualizar_informacoes', methods=['GET'])
def visualizar_informacoes():
    dados = recuperar_dados_do_banco()
    if dados:
        return render_template('index.html', dados=dados)
    else:
        return "Dados não encontrados."

if __name__ == '__main__':
    app.run()
