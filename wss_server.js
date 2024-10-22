const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

// Function to handle incoming messages and send "200 OK" acknowledgment
wss.on('connection', (ws) => {
  console.log('New client connected');
    
    // Send JSON connected event to FREEswitch server
    const jsonData = {
        event: 'connected',
        message: 'Starting the process',
        timestamp: new Date()
    };
    ws.send(JSON.stringify(jsonData)); // Send JSON string

  // Listen for messages from the client
  ws.on('message', (message) => {
    console.log('Received:', message);

  });


});

console.log('WebSocket server is running on ws://localhost:8080');