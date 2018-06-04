import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from blog.models import Post


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

    # # 경로에 해당하는 문자열을 로드해줌
    # html = render_to_string('blog/post_list.html')
    # # 가져온 문자열을 돌려주기
    # return HttpResponse(html)
    # 위 두 과정을 한줄로 바꿔줄 수 있다
    # return render(request, 'blog/post_list.html')

    # Post인스턴스에서 title 속성에 접근가능
    # HttpResponse에
    # 글 목록
    # - 글제목..
    # - 글제목..
    # ...
    # 위 텍스트를 넣어서 리턴
    # posts = Post.objects.all()
    # print(posts)
    #
    # result = '글 목록<br>'
    # for post in Post.objects.all():
    #     result += '{}<br>'.format(post.title)
    #
    # # po = ['글 목록', ]
    # # for post in Post.objects.all():
    # #     po.append(f'<br> - {post.title}')
    #
    # # result = '\n'.join([post for post in Post.objects.all()])
    #
    # return HttpResponse(result)

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    # render는 주어진 1,2번째 인수를 사용해서
    #     1번째 인수: httpresponse인스턴스
    #     2번째 인수: 문자열(TEMPLATES['DIRS']를 기준으로 탐색 할 템플릿 파일의 경로)
    #     3번째 인수: 템플릿을 렌더링할때 사용할 객체 모음
    return render(request, 'blog/post_list.html', context)