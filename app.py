from flask import Flask, send_from_directory
from controllers import routes

app = Flask(__name__, 
            template_folder='views',
            static_folder='static')

# Rota para servir arquivos da pasta imgs
@app.route('/imgs/<path:filename>')
def serve_imgs(filename):
    return send_from_directory('imgs', filename)

routes.init_app(app)

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)