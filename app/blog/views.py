import os

from django.http import HttpResponse
from django.template.loader import render_to_string


def post_list(request):
    # cur_file_path = os.path.abspath(__file__)
    # print(cur_file_path)
    # blog_file_path = os.path.dirname(cur_file_path)
    # print(blog_file_path)
    # app_file_path = os.path.dirname(blog_file_path)
    # print(app_file_path)
    # templates_file_path = os.path.join(app_file_path, 'templates')
    # print(templates_file_path)
    # blog__post_list_file_path = os.path.join(templates_file_path, 'blog', 'post_list.html')
    # html = open(blog__post_list_file_path, 'rt').read()

    # 경로에 해당하는 문자열을 로드해줌
    html = render_to_string('blog/post_list.html')
    # 가져온 문자열을 돌려주기
    return HttpResponse(html)
