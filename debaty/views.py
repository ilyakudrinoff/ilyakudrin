from django.shortcuts import render, redirect, get_object_or_404
from .utils import paginator
from .models import Team, Speaker, News, ResultsTeam, ResultsSpeaker
from .forms import TeamForm, SpeakerForm


def debaty(request):
    form = TeamForm(request.POST or None)
    if form.is_valid() or request.POST:
        t = Team.objects.create(name=request.POST.get('name'), company=request.POST.get('company'))
        t.save()
        return redirect('debaty:createSpeaker')
    return render(request, 'debaty/debaty.html', {'form': form})


def results(request):
    resultsTeam = ResultsTeam.objects.all()
    resultsSpeaker = ResultsSpeaker.objects.all()
    context = {
        'resultsTeam': resultsTeam,
        'resultsSpeaker': resultsSpeaker,
    }
    return render(request, 'debaty/results.html', context)


def createSpeaker(request):
    form = SpeakerForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.save()
        return redirect('debaty:createSpeaker')
    return render(request, 'debaty/createSpeaker.html', {'form': form})