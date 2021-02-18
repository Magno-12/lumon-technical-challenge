import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


TASKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Descargar reporte de datos',
        'description': 'Se debe descargar el reporte de Google Analytics en formato CSV',
        'priority': 'low',
        'author': 'Jack Kerouac',
        'worker': 'Evert Moreno',
        'isCompleted': True,
        'tags': 'google, analytics, dashboard'
    },
    {
       'id': uuid.uuid4().hex,
        'title': 'Descargar reporte de datos',
        'description': 'Se debe descargar el reporte de Google Analytics en formato CSV',
        'priority': 'low',
        'author': 'Jack Kerouac',
        'worker': 'Evert Moreno',
        'isCompleted': True,
        'tags': 'google, analytics, dashboard'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Descargar reporte de datos',
        'description': 'Se debe descargar el reporte de Google Analytics en formato CSV',
        'priority': 'low',
        'author': 'Jack Kerouac',
        'worker': 'Evert Moreno',
        'isCompleted': True,
        'tags': 'google, analytics, dashboard'
    }
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_task(task_id):
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
            return True
    return False


@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TASKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'isCompleted': post_data.get('isCompleted'),
            'description': post_data.get('description'),
            'priority': post_data.get('priority'),
            'worker': post_data.get('worker'),
            'tags': post_data.get('tags'),
        })
        response_object['message'] = 'task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)


@app.route('/tasks/<task_id>', methods=['PUT', 'DELETE'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_task(task_id)
        TASKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'isCompleted': post_data.get('isCompleted'),
            'description': post_data.get('description'),
            'priority': post_data.get('priority'),
            'worker': post_data.get('worker'),
            'tags': post_data.get('tags'),
        })
        response_object['message'] = 'task updated!'
    if request.method == 'DELETE':
        remove_task(task_id)
        response_object['message'] = 'task removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
