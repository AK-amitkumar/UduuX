# -*- coding: utf-8 -*-
from odoo import http


class UniteToolsDrawerFrame(http.Controller):
	@http.route('/drawer', auth='public')
	def index(self):
		return '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">' \
			   '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>' \
			   '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>' \
			   '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>' \
			   '<a class="btn btn-primary btn-lg btn-block" href="/web">Back to UNITE ERP</a>' \
			   '<p>' \
			   '<iframe src="https://uniteit.github.io/models/war/index.html" frameborder="0" height="1080" width="1920"></iframe>' \
			   '</p>'