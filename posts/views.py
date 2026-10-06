from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
posts = [
    {
        'id':1,
        'title': 'Let\'s explore python',
        "content": 'Python is a high-level, interpreted programming language that has gained immense popularity in recent years. It was created by Guido van Rossum and first released in 1991. Python is known for its simplicity, readability, and versatility, making it an excellent choice for beginners and experienced developers alike.',

    },
    {
        'id':2,
        'title': 'Let\'s explore Django',
        "content": 'Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. It was created by Adrian Holovaty and Simon Willison in 2003 and released publicly under a BSD license in 2005. Django follows the "batteries-included" philosophy, providing developers with a wide range of built-in features and tools to streamline the web development process.',

    },
    {
        "id":3,
        "title": "Let's explore JavaScript",
        "content": "JavaScript is a versatile, high-level programming language that is primarily used",
    },
]



def home(request):
    html = ""
    for post in posts:
        html += f"""
            <div>
            <a href='/post/{post['id']}/'>

                <h1>{post['id']}-{post['title']}</h1></a>
                <p>{post['content']}</p>
            </div>
"""
    return render(request, 'posts/index.html', {'posts': posts})

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = f"""
                <h1>{post_dict['title']}</h1>
                <p>{post_dict['content']}</p>
            """
        return render(request, 'posts/post.html', {'post_dict': post_dict})
    else:
        raise Http404()





