import web

urls = [
    '/', 'mvc.controllers.index.Index',
    '/index', 'mvc.controllers.index.Index',
    '/vista', 'mvc.controllers.vista.Vista',
    '/registro', 'mvc.controllers.registro.Registro',
] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
