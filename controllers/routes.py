from flask import render_template, request 

comentarios = [{'Comentário':''}]

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
    
    @app.route('/noticia')
    def noticia():
        dadosComentarios = comentarios[0]
        if request.method == 'POST':
            if request.form.get('comentario'):
                comentarios.append({'Comentário': request.form.get('comentario')})
        return render_template('noticia.html', dadosComentarios=dadosComentarios, comentarios=comentarios)
    
    @app.route('/feedback', methods=['GET', 'POST'])
    def feedback():
        dadosFeedbacks = feedbacks[0]
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('nascimento') and request.form.get('sexo') and request.form.get('email') and request.form.get('comentario'):
                feedbacks.append({'Nome': request.form.get('nome'),
                                 'dataNasc': request.form.get('nascimento'),
                                 'Sexo': request.form.get('sexo'),
                                 'Email': request.form.get('email'),
                                 'Comentário': request.form.get('comentario')})
        return render_template('feedback.html', dadosFeedbacks=dadosFeedbacks, feedback=feedbacks)
    
    @app.route('/addNoticia', methods=['GET', 'POST'])
    def addNoticia():
        dadosNoticias = noticias[0]
        if request.form == 'POST':
            if request.form.get('titulo') and request.form.get('autor') and request.form.get('categoria') and request.form.get('descricao') and request.form.get('noticia'):
                noticias.append({'Título': request.form.get('titulo'),
                                 'Autor': request.form.get('Autor'),
                                 'Categoria': request.form.get('Categoria'),
                                 'Descrição': request.form.get('descricao'),
                                 'Título': request.form.get('noticia'),
                                 })
        return render_template('addNoticia.html', dadosNoticias=dadosNoticias, noticias=noticias)