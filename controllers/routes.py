from flask import render_template, request 

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/noticia', methods=['GET', 'POST'])
    def noticia():
        return render_template('noticia.html')