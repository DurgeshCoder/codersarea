from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import *
import random

bg = ['rgba-black-strong']


def home(request):
    return render(request, "home.html", {"bg": bg[random.randrange(0, len(bg))]})


# managing and showing the topics
def topic_manager(request, technology_slug, topic_slug):
    tech = Technology.objects.filter(slug=technology_slug)[0]
    sub_topics = SubTopics.objects.filter(technology=tech)
    topic = Topic.objects.filter(slug=topic_slug)[0]
    next_previous_list = find_next_previous_topics(sub_topics, topic)
    return render(request, "show_topic.html", {'sub_topics': sub_topics, 'topic': topic, 'technology': tech, 'next_topic': next_previous_list[0], 'previous_topic': next_previous_list[1], 'current_topics': next_previous_list[2], 'current_subtopic': next_previous_list[3]})


# find next and previous
def find_next_previous_topics(sub_topics, topic):
    current_topic_index = -1
    topics_list = []
    next_subtopic = None
    next_topic = None
    previous_topic = None
    current_subtopic = None
    for subtopic in sub_topics:
        print(subtopic)
        if topic in subtopic.get_topics():
            print(True)
            current_subtopic = subtopic
            topics_list = list(subtopic.get_topics())
            current_topic_index = topics_list.index(topic)
            try:
                next_subtopic = list(sub_topics).__getitem__(
                    list(sub_topics).index(subtopic)+1)
            except:
                next_subtopic = None
            break
    print(current_topic_index)
    previous_topic = topics_list.__getitem__(
        ((current_topic_index-1)+len(topics_list)) % len(topics_list))
    try:
        next_topic = topics_list.__getitem__(
            (current_topic_index+1))
    except IndexError as e:
        # print("list index out of bound : next")
        if next_subtopic is not None:
            next_topic = next_subtopic.get_topics().__getitem__(0)

    # print(previous_topic)
    return [next_topic, previous_topic, topics_list, current_subtopic]


# uploading image
@csrf_exempt
def upload_image(request):
    print("testing")
    if request.method == 'POST':
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        print(file.name)
        print(uploaded_file_url)
        res = {'location': '' +
               str(uploaded_file_url)}
        return JsonResponse(res)
    else:
        return HttpResponse("error")
    return HttpResponse("error")

# delete image


@csrf_exempt
def delete_image(request):
    if request.method == 'POST':
        url = request.POST['url']
        if url.find('?') != -1:
            name = url[url.rindex('/') + 1: url.index('?'):]
        else:
            name = url[url.rindex('/') + 1::]
        import os
        full_path = os.path.join(settings.MEDIA_ROOT, name)
        os.remove(full_path)
        return JsonResponse({'msg': 'done'})
    return JsonResponse({"msg": "error"})

# show technology handler


def show_tech(request, tech_slug):
    print(tech_slug)
    tech = Technology.objects.filter(slug=tech_slug)[0]
    print(tech)
    print(tech.get_subtopics())
    return render(request, "technology.html", {'tech': tech})
