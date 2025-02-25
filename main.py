from flask import Flask, request

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Javascript",
        "descricao": "Estudar Javascript para aprender a contruir eventos",
        "status": "Em andamento",
        "Local": "Vila Fátima",
        "Carga Horária": "60 horas",
        "Média necessaria": 7
    },

    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sobre Web Services",
        "status": "Não iniciado",
        "Local": "Santa Terezinha",
        "Carga Horaria": "90 horas",
        "Média necessaria": 8
    }

]

@app.route('/task', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa

    return 'Tarefa não encontrada'

@app.route('/task', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['Local'] = task_body.get('Local')
    task_search['Carga Horaria'] = task_body.get('Carga Horaria')
    task_search['Média necessaria'] = task_body.get('Média necessaria')


    return task_search

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)

    return 'Sua tarefa foi removida com sucesso!!!'

@app.route('/')
def index():
   return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

