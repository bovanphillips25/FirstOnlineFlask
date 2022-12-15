from flask import render_template
# this import is needed to find the controller module
from . controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
        name = "Bovan Phillips"
        return render_template('index.html', name=name)
