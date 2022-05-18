from trackr import create_app
from multiprocessing import cpu_count
from gunicorn.app.base import BaseApplication
from os import environ

def get_number_of_workers():
    return (cpu_count() * 2) + 1

class MyGunicornServer(BaseApplication):
    def __init__(self, app, options = None):
        self.app = app
        self.options = options or {}
        super().__init__()

    def load(self):
        return self.app

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

if __name__ == "__main__":
    trackr = create_app()
    host = environ.get("HOST") or "0.0.0.0"
    port = environ.get("PORT") or 8000
    options = {
        "bind": f"{host}:{port}",
        "workers": get_number_of_workers(),
    }
    MyGunicornServer(trackr, options).run()
    