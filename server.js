const express = require('express');
const http = require('http');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Track connected hardware/software nodes
let vrClient = null;
let aiEngine = null;

wss.on('connection', (ws) => {
    console.log('🔄 A system node has linked to the network hub');

    ws.on('message', (message) => {
        let data;
        try {
            data = JSON.parse(message);
        } catch (e) {
            console.log('Malformed JSON packet received');
            return;
        }

        // 1. Identify who is connecting
        if (data.type === 'IDENTIFY_VR') {
            vrClient = ws;
            console.log('🎮 VR Simulator Stream successfully linked! ✓');
        } else if (data.type === 'IDENTIFY_AI') {
            aiEngine = ws;
            console.log('🧠 Cognitive Twin AI Engine successfully linked! ✓');
        }

        // 2. Route real-time VR telemetry data over to Python
        if (data.type === 'VR_TELEMETRY' && aiEngine) {
            aiEngine.send(JSON.stringify(data));
        }

        // 3. Route the AI warning decisions straight back to the flashing VR screen
        if (data.type === 'DISORIENTATION_ALERT' && vrClient) {
            vrClient.send(JSON.stringify({
                type: 'ALARM_TRIGGER',
                riskScore: data.riskScore,
                hapticPattern: data.hapticPattern,
                visualDanger: data.visualDanger // True triggers the bright flashing strobe
            }));
        }
    });

    ws.on('close', () => { 
        console.log('❌ A node has disconnected from the network hub'); 
    });
});

// Run everything on Port 3000
server.listen(3000, () => {
    console.log('🚀 Cognitive Twin Streaming Router active on http://localhost:3000');
});