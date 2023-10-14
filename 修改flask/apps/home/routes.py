# -*- encoding: utf-8 -*-
from flask import render_template, request
from jinja2 import TemplateNotFound

from apps.home import blueprint


@blueprint.route('/')
def index():
    return render_template('home/index.html', segment='index')


# @blueprint.route('/<template>')
# def route_template(template):
#     try:
#         if not template.endswith('.html'):
#             template += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/" + template, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500

@blueprint.route('/<template>')
def route_template(template):
    if not template.endswith('.html'):
        template += '.html'

    # Detect the current page
    segment = get_segment(request)
    
    print("Template:", template)  # 添加测试输出
    
    # Serve the file (if exists) from app/templates/home/FILE.html
    return render_template("home/" + template, segment=segment)


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
