from flask import Flask, request, redirect, render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-link', methods=['GET'])

def gerar_link():
    matricula = request.args.get('matricula', 'matricula padrao')
    senha = request.args.get('senha', 'senha padrao')

    base_url = "https://forms.office.com/e/uNSqr31cfS"
    return redirect(f"{base_url}?matricula={matricula}&senha={senha}")


if __name__ == "__main__":
    app.run(debug=True)

