from flask import Flask, jsonify, abort, make_response, request, url_for
import connexion

tasks = [
    {
        'id': 1,
        'title': u'Completer Tronc Commun',
        'description': u'AdWords Certification, Install Python 3, Read team guidelines, Understand Git',
        'done': True
    },
    {
        'id': 2,
        'title': u'Tuto Microservices',
        'description': u'Flask, framework connexion, Adscale Architecture',
        'done': False
    }
]

# def make_public_task(task):
#     new_task = {}
#     for field in task:
#         if field == 'id':
#             new_task['uri'] = url_for('get_task_2', task_id= task['id'], _external=True)
#         else:
#             new_task[field] = task[field]
#     return new_task

def create_task():
    if not request.json or not 'title' in request.json:
        abort(404)

    task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description',""),
            'done': False
        }
    tasks.append(task)
    return jsonify({'task': task}), 201

def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(404)
    if 'title'  in request.json and type(request.json['title']) is not str:
        abort(404)
    if 'description' in request.json and type(request.json['description']) is not str: 
        abort(404)
    if 'done' in request.json and type(request.json['done']) != bool: 
        abort(404)

    task[0]['title'] = request.json.get('title', task[0]['title']) 
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task)==0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

def get_tasks():
    return jsonify([{'tasks': task for task in tasks}]), 200

def get_task_2(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)

    return jsonify({'task': task[0]})

def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)
