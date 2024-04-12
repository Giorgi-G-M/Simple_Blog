from django.shortcuts import render

# Create your views here.

blogs = [
    {'title': 'First Blog', 'text': 'This is the content of the first blog post.', 'author': 'John Doe'},
    {'title': 'Second Blog', 'text': 'This is the content of the second blog post.', 'author': 'Jane Smith'},
    {'title': 'Third Blog', 'text': 'This is the content of the third blog post.', 'author': 'Emily Johnson'},
]

def blog_view(request):
    context = {'blogs': blogs}
    return render(request, 'myapp/blog.html', context)
