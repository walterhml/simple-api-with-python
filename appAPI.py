from flask import Flask

app = Flask(__name__) 

@app.route('/')
def hello():
    return 'Criando minha primeira API com PYTHON'


if __name__ == '__main__':
    app.run(debug=True)
    
    
    