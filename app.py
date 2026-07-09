from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

# Codes de couleur pour le terminal
G = "\\033[92m" # Vert
R = "\\033[0m"  # Reset

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Terminal Access</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono&display=swap');

        body {
            margin: 0;
            padding: 0;
            background-color: #050505;
            color: #00ff41;
            font-family: 'Orbitron', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        /* Scanline effect */
        body::before {
            content: " ";
            display: block;
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            z-index: 2;
            background-size: 100% 2px, 3px 100%;
            pointer-events: none;
        }

        .terminal-box {
            position: relative;
            background: rgba(0, 20, 0, 0.9);
            border: 2px solid #00ff41;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.2), inset 0 0 20px rgba(0, 255, 65, 0.1);
            width: 90%;
            max-width: 500px;
            z-index: 3;
        }

        h1 {
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 30px;
            text-transform: uppercase;
            letter-spacing: 5px;
            text-shadow: 0 0 10px #00ff41;
        }

        .input-container {
            position: relative;
            margin-bottom: 20px;
        }

        input[type="text"] {
            width: 100%;
            background: transparent;
            border: none;
            border-bottom: 2px solid #00ff41;
            padding: 10px 0;
            font-family: 'JetBrains Mono', monospace;
            font-size: 24px;
            color: #00ff41;
            text-align: center;
            outline: none;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            background: #00ff41;
            color: #000;
            border: none;
            padding: 15px;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
            text-transform: uppercase;
            margin-top: 10px;
        }

        button:hover {
            background: #000;
            color: #00ff41;
            box-shadow: 0 0 20px #00ff41;
        }

        .status {
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            margin-top: 20px;
            text-align: center;
            opacity: 0.7;
        }

        .error-msg {
            color: #ff003c;
            font-size: 12px;
            text-align: center;
            margin-top: 10px;
            display: none;
            text-shadow: 0 0 5px #ff003c;
        }
    </style>
</head>
<body>
    <div class="terminal-box">
        <h1>System Access</h1>
        <form id="cyberForm" method="POST" action="/search">
            <div class="input-container">
                <input type="text" name="query" id="query" placeholder="[ ENTER NUMBERS ]" autocomplete="off" required>
            </div>
            <button type="submit">Execute Transmission</button>
            <div id="error" class="error-msg">ERROR: NUMERIC_ONLY_PROTOCOL</div>
        </form>
        <div class="status">> CONNECTION: STABLE<br>> ENCRYPTION: ACTIVE</div>
    </div>

    <script>
        const form = document.getElementById('cyberForm');
        const input = document.getElementById('query');
        const error = document.getElementById('error');

        form.onsubmit = function(e) {
            if (!/^[0-9]+$/.test(input.value)) {
                e.preventDefault();
                error.style.display = 'block';
                return false;
            }
        };
        input.oninput = () => error.style.display = 'none';
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if query:
        print(f"\\n{G}[SYSTEM] DATA RECEIVED: {query}{R}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    # On utilise 0.0.0.0 pour permettre les connexions réseau
    app.run(host='0.0.0.0', port=5000)
