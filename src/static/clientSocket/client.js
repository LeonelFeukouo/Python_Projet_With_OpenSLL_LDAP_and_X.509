const sio = io();

sio.on('connect',() =>{
    console.log('client connected'+ sio.id);
    sio.emit('sum', {sid: sio.id, numbers: [1, 2]});
    sio.emit('sum2', {sid: sio.id, numbers: [6, 2]}, (result) =>{
        console.log(result)
    });
});

sio.on('disconnect',() =>{
    console.log('client disconnected')
});

sio.on('sum_result', (data)=>{
    console.log(data)
})

sio.on('mult', (data, callback)=>{
    console.log(data);
    const result = data.numbers[0] * data.numbers[1];
    callback(result)

})

sio.on('client_count', (count)=>{
    console.log('There are '+ count + ' connected clients.');
})

sio.on('room_count', (count)=>{
    console.log('There are '+ count + ' clients in my room.');
})