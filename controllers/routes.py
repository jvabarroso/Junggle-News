from flask import render_template, request 

comentarios = [{'Nome':'',
                'Comentário':''}]

feedbacks = [{'Nome':'Igor',
             'DataNasc':'',
             'Sexo': '',
             'Email': '',
             'Comentário':''}]

noticias = [{'Título': '',
             'Autor':'',
             'Categoria':'',
             'Descrição':'',
             'Notícia':''}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html', method=['GET', 'POST'])
    
    @app.route('/baleias', methods=['GET', 'POST'])
    def noticia():
        dadosComentarios = comentarios[0]
        if request.method == 'POST':
            if request.form.get('comentario') and request.form.get('nome'):
                comentarios.append({'Nome': request.form.get('nome'),
                                    'Comentário': request.form.get('comentario')})
        return render_template('baleias.html', dadosComentarios=dadosComentarios, comentarios=comentarios)
    
    @app.route('/abelhas', methods=['GET', 'POST'])
    def abelhas():
        dadosComentarios = comentarios[0]
        if request.method == 'POST':
            if request.form.get('comentario') and request.form.get('nome'):
                comentarios.append({'Nome': request.form.get('nome'),
                                    'Comentário': request.form.get('comentario')})
        return render_template('abelhas.html', dadosComentarios=dadosComentarios, comentarios=comentarios)
    
    @app.route('/tigres', methods=['GET', 'POST'])
    def tigres():
        dadosComentarios = comentarios[0]
        if request.method == 'POST':
           if request.form.get('comentario') and request.form.get('nome'):
                comentarios.append({'Nome': request.form.get('nome'),
                                    'Comentário': request.form.get('comentario')})
        return render_template('tigres.html', dadosComentarios=dadosComentarios, comentarios=comentarios)
    
    @app.route('/lobo-terrivel', methods=['GET', 'POST'])
    def lobo_terrivel():
        dadosComentarios = comentarios[0]
        if request.method == 'POST':
           if request.form.get('comentario') and request.form.get('nome'):
                comentarios.append({'Nome': request.form.get('nome'),
                                    'Comentário': request.form.get('comentario')})
        return render_template('lobo-terrivel.html', dadosComentarios=dadosComentarios, comentarios=comentarios)
    
    @app.route('/feedback', methods=['GET', 'POST'])
    def feedback():
        dadosFeedbacks = feedbacks[0]
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('nascimento') and request.form.get('sexo') and request.form.get('email') and request.form.get('comentario'):
                feedbacks.append({'Nome': request.form.get('nome'),
                                 'DataNasc': request.form.get('nascimento'),
                                 'Sexo': request.form.get('sexo'),
                                 'Email': request.form.get('email'),
                                 'Comentário': request.form.get('comentario')})
        return render_template('feedback.html', dadosFeedbacks=dadosFeedbacks, feedbacks=feedbacks)
    
    @app.route('/addNoticia', methods=['GET', 'POST'])
    def addNoticia():
        dadosNoticias = noticias[0]
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('autor') and request.form.get('categoria') and request.form.get('descricao') and request.form.get('noticia'):
                noticias.append({'Título': request.form.get('titulo'),
                                 'Autor': request.form.get('autor'),
                                 'Categoria': request.form.get('Categoria'),
                                 'Descrição': request.form.get('descricao'),
                                 'Notícia': request.form.get('noticia'),
                                 })
        return render_template('addNoticia.html', dadosNoticias=dadosNoticias, noticias=noticias)