from flask import Flask, render_template

app = Flask(__name__)

tarefas = [
    {'id': 1, 'nome': 'Comprar leite', 'descricao': 'Ir ao supermercado e comprar leite'},
    {'id': 2, 'nome': 'Estudar Flask', 'descricao': 'Ler a documentação do Flask'},
    {'id': 3, 'nome': 'Ler um livro', 'descricao': 'Ler o livro "1984 de George Orwell"'},
]

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/tarefa/<int:tarefa_id>')
def tarefa_detail(tarefa_id):
    tarefa = next(t for t in tarefas if t['id'] == tarefa_id)
    return render_template('task_detail.html', tarefa=tarefa)

if __name__ == '__main__':
    app.run(debug=True)
