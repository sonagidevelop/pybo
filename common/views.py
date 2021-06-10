from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
# from .forms import QuestionForm, AnswerForm, CommentForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# @login_required(login_url='common:login')
# def comment_create_question(request, question_id):
#     """
#     pybo 질문댓글등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
