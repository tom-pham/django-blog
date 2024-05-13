from django.shortcuts import render
from polling.models import Poll
from django.http import Http404


# Create your views here.
def list_view(request):
    context = {"polls": Poll.objects.all()}
    return render(request, "polling/list.html", context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
    context = {"poll": poll}
    return render(request, "polling/detail.html", context)
