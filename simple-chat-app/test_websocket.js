const WebSocket = require('ws');
const ws = new WebSocket('ws://localhost:3000');
ws.on('open', () => {
    ws.send('Test message');
});
ws.on('message', (message) => {
    console.log(`Received: ${message}`);
    process.exit(0);
});
