from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from accounts.models import ProblemsByUser, CustomUser
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




            # 문제 확인
            problem = Problem.objects.get(pk=problem_id)
            output, runtime = execute(lang, code, userName, problem_id)


            output = output.splitlines()
            answer = problem.serverTestCaseOutput.rstrip().splitlines()
            isRight = output == answer

            # 사용자별 문제 갱신
            problemsByUser = ProblemsByUser()
            problemsByUser.pUsername = CustomUser.objects.get(username=userName)
            problemsByUser.number = problem_id
            problemsByUser.code = code
            problemsByUser.rightOrNot = isRight
            problemsByUser.lang = lang
            problemsByUser.runTime = float(runtime)
            problemsByUser.save()


            if isRight ==True:
                # 문제 상태 갱신
                problem.numOfTry += 1
                problem.numOfRight += 1
                problem.ratio = 100*problem.numOfRight//(problem.numOfTry+problem.numOfRight)
                # 사용자 상태 갱신

            else:
                problem.numOfTry += 1
                problem.ratio = 100*problem.numOfRight//(problem.numOfTry+problem.numOfRight)


            problem.save()

            print(isRight)

            print(output)

            print(answer)

            # 정답 확인

            resultList = ProblemsByUser.objects.filter(Q(pUsername_id=CustomUser.objects.get(username=userName))&Q(number=problem_id))


            # 회원별 문제 테이블에 코드 저장,



            # 문제모델에 문제 시도횟수, 정답횟수 변화

            return render(request,'problem/result.html',{'resultList':resultList})
    else:
        user_form = CodeSubmissionForm()
    return HttpResponse('제대로 제출 되지 않았습니다.')

def code(request,code_id):
    if request.user.is_authenticated: # 로그인 안하면 로그인 사이트로 간다.
        code = get_object_or_404(ProblemsByUser, pk=code_id)
        code = code.code
        return render(request, 'problem/code.html', {'code': code})
    else:
        return HttpResponseRedirect('/')

