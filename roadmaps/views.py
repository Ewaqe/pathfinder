import random
import markdown
from django.http import JsonResponse, HttpResponse
from .skill_generator import *
from .models import Skill, Topic
from .forms import SkillForm
from django.shortcuts import render, redirect


def create_skill(request):
    context = {}

    form = SkillForm(request.POST or None)
    if form.is_valid():
        try:
            skill = Skill.objects.get(name=form.data['name'])
            return redirect(f'/skill/{skill.id}')
        except Exception as e:
            pass

        skill = form.save()

        topics = generate_topics(skill.name)

        for topic_name in topics:
            topic = Topic()
            topic.skill = skill
            topic.name = topic_name
            topic.text = generate_topic_text(skill.name, topic_name)
            topic.save()

        return redirect(f'skill/{skill.id}')

    context['form'] = form
    return render(request, 'index.html', context)


def detail_view(request, skill_id):
    colors = ['beige', 'orange', 'red', 'blue']
    skill = Skill.objects.get(id=skill_id)
    context = {
        "skill": skill,
        'topics': []
    }
    for topic in Topic.objects.filter(skill=skill):
        topic = {
            'id': topic.id,
            'name': topic.name,
            'color': colors[random.randint(0, 3)]
        }
        context['topics'].append(topic)

    return render(request, 'detail_view.html', context)


def get_topic_text(request):
    topic = Topic.objects.get(id=request.GET.get('id'))
    response = {
        "name": topic.name,
        "text": markdown.markdown(topic.text)
    }
    return JsonResponse(response)


def search_skill(request):
    name = request.GET.get('q')
    return JsonResponse([{'name': skill.name, 'id': skill.id} for skill in Skill.objects.filter(name__startswith=name)], safe=False)
