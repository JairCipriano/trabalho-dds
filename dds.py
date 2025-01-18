from flask import Flask, Request, redirect, render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-link', methods=['get'])

def gerar_link():
    matricula = Request.args.__get__('matricula', 'matricula padrao')
    senha = Request.args.__get__('senha', 'senha padrao')

    base_url = "https://forms.office.com/e/uNSqr31cfS"
    return redirect(f"{base_url}?matricula={matricula}&senha={senha}")


if __name__ == "__main__":
    app.run(debug=True)

