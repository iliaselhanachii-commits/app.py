from flask import Flask, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "cle_secrete_ultra_securisee" # Nécessaire pour les sessions

# --- CONFIGURATION ---
PASSWORD = "2893" # MODIFIE TON MOT DE PASSE ICI
# ---------------------

G = "\033[92m"
R = "\033[0m"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus Secure Terminal</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono&display=swap' );
        body { margin: 0; background: #050505; color: #00ff41; font-family: 'Orbitron', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        body::before { content: " "; display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06)); z-index: 2; background-size: 100% 2px, 3px 100%; pointer-events: none; }
        .terminal-box { position: relative; background: rgba(0, 20, 0, 0.9); border: 2px solid #00ff41; padding: 40px; border-radius: 15px; box-shadow: 0 0 20px rgba(0, 255, 65, 0.2); width: 90%; max-width: 500px; z-index: 3; text-align: center; }
        h1 { font-size: 1.2rem; margin-bottom: 30px; letter-spacing: 5px; text-shadow: 0 0 10px #00ff41; }
        input[type="text"], input[type="password"] { width: 100%; background: transparent; border: none; border-bottom: 2px solid #00ff41; padding: 10px 0; font-family: 'JetBrains Mono', monospace; font-size: 24px; color: #00ff41; text-align: center; outline: none; margin-bottom: 20px; }
        button { width: 100%; background: #00ff41; color: #000; border: none; padding: 15px; font-weight: bold; cursor: pointer; transition: 0.3s; text-transform: uppercase; }
        button:hover { background: #000; color: #00ff41; box-shadow: 0 0 20px #00ff41; }
        .error { color: #ff003c; font-size: 12px; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="terminal-box">
        {% if not authorized %}
            <h1>AUTHENTICATION REQUIRED</h1>
            <form method="POST" action="/login">
                <input type="password" name="password" placeholder="[ ENTER ACCESS KEY ]" required>
                <button type="submit">Unlock System</button>
            </form>
            {% if error %}<div class="error">INVALID ACCESS KEY</div>{% endif %}
        {% else %}
            <h1>SYSTEM ACCESS GRANTED</h1>
            <form id="cyberForm" method="POST" action="/search">
                <input type="text" name="query" id="query" placeholder="[ ENTER NUMBERS ]" autocomplete="off" required>
                <button type="submit">Execute Transmission</button>
            </form>
            <div id="js-error" class="error" style="display:none;">ERROR: NUMERIC_ONLY_PROTOCOL</div>
            <a href="/logout" style="color:#00ff41; font-size:10px; text-decoration:none; margin-top:20px; display:block; opacity:0.5;">LOGOUT</a>
        {% endif %}
    </div>
    <script>
        const form = document.getElementById('cyberForm');
        if(form) {
            form.onsubmit = function(e) {
                const input = document.getElementById('query');
                if (!/^[0-9]+$/.test(input.value)) {
                    e.preventDefault();
                    document.getElementById('js-error').style.display = 'block';
                    return false;
                }
            };
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    authorized = session.get('authorized', False)
    return render_template_string(HTML_TEMPLATE, authorized=authorized)

@app.route('/login', methods=['POST'])
def login():
    if request.form.get('password') == PASSWORD:
        session['authorized'] = True
        return redirect(url_for('index'))
    return render_template_string(HTML_TEMPLATE, authorized=False, error=True)

@app.route('/logout')
def logout():
    session.pop('authorized', None)
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    if not session.get('authorized'):
        return redirect(url_for('index'))
    query = request.form.get('query')
    if query:
        print(f"\\n{G}[SYSTEM] DATA RECEIVED: {query}{R}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
