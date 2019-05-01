from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem
from .forms import CodeSubmissionForm
from .modules.execute import execute
from operator import eq
# Create your views here.


def problemList(request):
    problemList = Problem.objects.all()
    return render(request, 'problem/problemList.html', {'problemList':problemList})


def detail(request, problem_id):
    if request.user.is_authenticated: # 로그인 안하면 로그인 사이트로 간다.
        problem = get_object_or_404(Problem, pk=problem_id)
        return render(request, 'problem/detail.html', {'problem': problem, 'form': CodeSubmissionForm})
    else:
        return HttpResponseRedirect('/')


def check(request, problem_id):
    if request.method == 'POST':
        SCodeSubmissionForm = CodeSubmissionForm(request.POST)
        if SCodeSubmissionForm.is_valid():
            lang = SCodeSubmissionForm.cleaned_data['lang']
            code = SCodeSubmissionForm.cleaned_data['code']
            userName = request.user.username

            # 코드 실행, 결과값 반환

            # output = execute(lang, code, userName).rstrip('\n')
            # answer = Problem.objects.get(pk=problem_id).serverTestCaseOutput.rstrip('\n')

            output = execute(lang, code, userName)
            output = output.splitlines()
            answer = Problem.objects.get(pk=problem_id).serverTestCaseOutput.rstrip().splitlines()

            isRight = output == answer
            print(isRight)

            print(output)


            print(answer)

            # 정답 확인




            # 회원별 문제 테이블에 코드 저장,



            # 문제모델에 문제 시도횟수, 정답횟수 변화

            return HttpResponse(isRight)
    else:
        user_form = CodeSubmissionForm()
    return HttpResponse('제대로 제출 되지 않았습니다.')