const sio = io();

sio.on('connect',() =>{
    console.log('client connected')
});

sio.on('disconnect',() =>{
    console.log('client disconnected')
});