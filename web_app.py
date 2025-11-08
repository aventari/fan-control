import subprocess
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Define the path to your compiled Go executable
# Assumes it's in the same directory and named "fan_control"
GO_EXECUTABLE = "./fan_control"

@app.route('/')
def index():
    """Serves the index.html frontend."""
    return send_from_directory('.', 'index.html')

@app.route('/api/fan_status', methods=['GET'])
def get_fan_status():
    """
    GET endpoint to retrieve the current fan status.
    Calls the Go program: ./fan_control get
    """
    try:
        # Run the Go program to get the status
        result = subprocess.run(
            [GO_EXECUTABLE, 'get'],
            capture_output=True,
            text=True,
            check=True,
            timeout=2
        )
        # The Go program prints the status to stdout
        status = result.stdout.strip()
        return jsonify({"status": status})
        
    except subprocess.CalledProcessError as e:
        # If the Go program returns an error code
        return jsonify({"error": "Failed to get status", "details": e.stderr.strip()}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/fan_speed', methods=['POST'])
def set_fan_speed():
    """
    POST endpoint to set a new fan speed.
    Expects JSON: {"speed": "low"}
    Calls the Go program: ./fan_control set [speed]
    """
    data = request.json
    speed = data.get('speed')

    if not speed or speed not in ['off', 'low', 'high']:
        return jsonify({"error": "Invalid speed. Must be 'off', 'low', or 'high'."}), 400

    try:
        # Run the Go program to set the speed
        result = subprocess.run(
            [GO_EXECUTABLE, 'set', speed],
            capture_output=True,
            text=True,
            check=True,
            timeout=2
        )
        # If successful, the Go program prints "OK"
        return jsonify({"success": True, "speed_set": speed, "details": result.stdout.strip()})

    except subprocess.CalledProcessError as e:
        # If the Go program returns an error code
        return jsonify({"error": "Failed to set speed", "details": e.stderr.strip()}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Runs the app on your Pi's local network IP
    app.run(host='0.0.0.0', port=5000, debug=True)