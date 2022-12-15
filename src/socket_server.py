import random

from flask import session, request
from flask_socketio import emit, join_room, leave_room, rooms
from . import socketio

client_count = 0
a_count = 0
b_count = 0


def cb(data):
    print(data)
def task(sid):
    socketio.sleep(5)
    # socketio.emit('mult', {'numbers': [5, 3]}, callback=cb)
    result = socketio.call('mult', {'numbers': [5, 3]}, to=sid)
    print(result)

@socketio.on('connect')
def onConnect():
    global client_count
    global a_count
    global b_count
    client_count +=1
    sid = request.sid
    print(sid, 'connected')
    socketio.start_background_task(task, sid)
    socketio.emit('client_count', client_count)
    room = 'a'
    room2 = 'b'
    if random.random() >0.5:
        room
        join_room('a')
        a_count +=1
        socketio.emit('room_count', a_count, to='a')
    else:
        join_room('b')
        b_count += 1
        socketio.emit('room_count', b_count, to='b')


@socketio.on('disconnect')
def ondisconnect():
    global client_count
    global a_count
    global b_count
    client_count -= 1
    socketio.emit('client_count', client_count)
    if 'a' in rooms():
        a_count -= 1
        socketio.emit('room_count', a_count, to='a')
    else:
        b_count -= 1
        socketio.emit('room_count', b_count, to='b')

@socketio.event()
def sum(data):
    result = data['numbers'][0] + data['numbers'][1]
    socketio.emit('sum_result', {'result': result}, to=data['sid'])


@socketio.event()
def sum2(data):
    result = data['numbers'][0] + data['numbers'][1]
    return result
