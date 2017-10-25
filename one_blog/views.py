from django.shortcuts import render,render_to_response
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    allComment = Comment.objects.all()
    template=get_template('index.html')
    html=template.render(locals())
    return HttpResponse(html)
def myblog(request):
    template=get_template('blog.html')
    html=template.render(locals())
    return HttpResponse(html)
def mydata(request):
    template = get_template('about.html')
    html = template.render(locals())
    return HttpResponse(html)
def management(request):

    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        user=User.objects.filter(username=username,password=password)
        if user:
            template = get_template('manage.html')
            html = template.render(locals())
            return HttpResponse(html)
        else:
            message="该页面只有管理员才能登陆"
            template1 = get_template('index.html')
            html1 = template1.render(locals())
            return HttpResponse(html1)
    else:
        message="请先登录！"
        template1 = get_template('index.html')
        html1 = template1.render(locals())
        return HttpResponse(html1)
    return  HttpResponse(message)

def blogpost(request):#博客提交
    template=get_template('blog.html')
    if request.POST:
        title = request.POST['title']
        body = request.POST['editor1']
        Post.objects.create(title=title, body=body)
        # p = Post(title=title, body=body)
        # p.save()
    else:
        message = "您提交了空的表单"
    allarticle=Post.objects.all()
    html=template.render(locals())
    return HttpResponse(html)
def postcomment(request):
    template = get_template('index.html')
    if request.POST:
        comment=request.POST['comment']
        Comment.objects.create(comment=comment)
    else:
        message="您提交了空的评论"
    allComment=Comment.objects.all()
    html=template.render(locals())
    return HttpResponse(html)
def blog_detail(request,slug):
    template=get_template('blog_detail.html')
    article = Post.objects.get(slug=slug)
    html=template.render(locals())
    return HttpResponse(html)
