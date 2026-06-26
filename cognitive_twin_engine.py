import websocket
import json
import numpy as np
import collections
import sys
import time

# Real-time streaming parameters
SEQ_LEN = 20
data_history = collections.deque(maxlen=SEQ_LEN)

print("🚀 Cognitive Twin Engine Script Initialized...")

def compute_watch_features(data):
    """
    Dynamically processes raw VR engine coordinates on the fly, 
    mimicking the low-power metrics tracked by an astronaut's smartwatch.
    """
    # Calculate Euclidean distance from hand tracker to the targeted panel console
    dist = np.sqrt(
        (data['hand_x'] - data['target_x'])**2 + 
        (data['hand_y'] - data['target_y'])**2 + 
        (data['hand_z'] - data['target_z'])**2
    )
    
    # Return features mapped to structural tracking configurations
    return [
        data['imu_roll_rate'],
        data['imu_pitch_rate'],
        dist,  # Hand trajectory drift
        data['heart_rate_bpm'],
        data['blink_rate_per_min'],
        data['fatigue_score']
    ]

def on_message(ws, message):
    payload = json.loads(message)
    
    # 1. Process Incoming Continuous VR Sensor Array Data
    if payload.get('type') == 'VR_TELEMETRY':
        features = compute_watch_features(payload)
        data_history.append(features)

        # Start evaluation as soon as our sliding telemetry history window fills up
        if len(data_history) == SEQ_LEN:
            current_distance = features[2]
            current_hr = features[3]
            fatigue = features[5]
            
            # --- REAL-TIME HARDWARE INFERENCE SIMULATION LOOP ---
            # Lightweight rule matrix running on the simulated Hexagon DSP chip
            risk_score = float(np.clip(current_distance * 0.65 + (current_hr - 72) * 0.01, 0.0, 1.0))
            
            # Dynamic Cooldown/Safety Threshold: Adjust sensitivity if astronaut is fatigued
            alert_threshold = 0.55 if fatigue < 0.5 else 0.42 
            
            if risk_score >= alert_threshold:
                # Disorientation or target drift detected! Choose context haptic pattern
                haptic_pattern = "LONG-short → Target alignment failure imminent!" if current_distance > 0.8 else "short-short-LONG → Roll illusion vector detected"
                print(f"⚠️ DISORIENTATION ANOMALY DETECTED! Risk Score: {risk_score:.2f} | Sending Emergency Alarm Payload...")
                
                # Push trigger payload back to server.js -> index.html to flash lights
                ws.send(json.dumps({
                    'type': 'DISORIENTATION_ALERT',
                    'riskScore': risk_score,
                    'hapticPattern': haptic_pattern,
                    'visualDanger': True  # Triggers high-intensity strobe
                }))
            else:
                # State normal: stand down warning indicators
                ws.send(json.dumps({
                    'type': 'DISORIENTATION_ALERT',
                    'riskScore': risk_score,
                    'hapticPattern': 'none',
                    'visualDanger': False
                }))

    # 2. Graceful Shutdown Signal to terminate process safely
    elif payload.get('type') == 'SYSTEM_SHUTDOWN':
        print("⏹ Received exit directive. Terminating background AI microservice...")
        ws.close()
        sys.exit(0)

def on_open(ws):
    print("🧠 Cognitive Twin Core successfully connected to the data pipeline network! ✓")
    ws.send(json.dumps({'type': 'IDENTIFY_AI'}))

def on_close(ws, close_status_code, close_msg):
    print(f"❌ Connection severed ({close_status_code}): {close_msg}. Reconnecting shortly...")

def on_error(ws, error):
    print(f"📡 Network communication error encountered: {error}")

# --- FAULT-TOLERANT INFINITE LISTENER LOOP ---
while True:
    try:
        ws_client = websocket.WebSocketApp(
            "ws://localhost:3000", 
            on_open=on_open, 
            on_message=on_message,
            on_close=on_close,
            on_error=on_error
        )
        ws_client.run_forever()
    except KeyboardInterrupt:
        print("\nProcess manually terminated by developer. Exiting safely.")
        sys.exit(0)
    except Exception as e:
        print(f"Connection dropped. Retrying socket engine instantiation in 3 seconds... (Error: {e})")
        time.sleep(3)