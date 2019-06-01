from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import ProblemsByUser

#.values('number').distinct()
#.annotate(total=Count('number'))
#annotate(total=Count('pUsername')).order_by('-total')
def rank(request):
                                        # 맞은 것 중에       pUsername에 대하여
    rankList = ProblemsByUser.objects.filter(rightOrNot=1).values("pUsername").annotate(total=Count('number', distinct=True))

    print(rankList)
    return render(request, 'rank/rank.html' ,{'rankList':rankList,})