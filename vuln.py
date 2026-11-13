from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <h1>Flask App 1</h1>
    <form action="/change-email" method="post">
        <label for="new-email">New Email:</label>
        <input type="email" id="new-email" name="new-email" required>
        <input type="submit" value="Change Email">
    </form>
    """)

@app.route('/change-email', methods=['POST'])
def change_email():
    new_email = request.form.get('new-email')
    return f"<p>Email changed to: {new_email}</p>"

if __name__ == '__main__':
    app.run(port=5000)
