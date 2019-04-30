from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Notice
# Create your views here.


def noticeList(request):
    noticeList = Notice.objects.all()
    return render(request, 'notice/noticeList.html', {'noticeList': noticeList})


def detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice/detail.html', {'notice': notice})
