# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Photo, User, Comment, Guest
import uuid
import boto3

# Create your views here.


class EventCreate(CreateView):
    model = Event
    fields = ['title', 'date', 'time', 'location',
              'description', 'capacity', 'infolink', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        return super().form_valid(form)


def category_index(request, event_category):
    events = Event.objects.filter(category=event_category)
    return render(request, 'events/index.html', {'category': event_category})


def events_index(request):
    #   events = Event.objects.filter()
    #   events = request.user.event_set.all()
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})


def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    post_form = PostForm()
    return render(request, 'events/detail.html', context={
        'event': event

    })


def events_comment(request, event_id):
    event = Event.objects.get(id=event_id)
    comment_text = request.POST.__getitem__('comment')
    user = request.user
    new_comment = Comment(event=event, user=user, text=comment_text)
    new_comment.save()
    return redirect('events_detail', event_id=event_id)


def events_rsvp(request, event_id):
    event = Event.objects.get(id=event_id)
    # event.users.all(user)
    is_attending = request.POST.__getitem__('is_attending')
    user = request.user
    new_guest = Guest(event=event, user=user, is_attending=is_attending)
    # new_guest = Event(users=user)
    # new_guest.is_attending = True
    new_guest.save()
    return redirect('events_detail', event_id=event_id)


def landing(request):
    return render(request, 'index.html', {'arr': ['Outdoors', 'Music', 'Food', 'Tech', 'Education']})

# def add_event(request):
#     form = PostForm(request.POST)
#     print(form)
#     if form.is_valid():
#         new_event = form.save(commit=False)
#         new_event.save()
#     return render(request, 'events/upload_photo.html', {'form': form})


def user(request):
    events = Event.objects.all()
    guest = Guest.objects.all()
    return render(request, 'user/profile.html', {})


def events(request):
    return render(request, 'events/index.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign up - Try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def add_photo(request, event_id):
    event = Event.objects.get(id=event_id)
    S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
    BUCKET = 'catcollector-dt'
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, event_id=event_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('events_detail', event_id=event_id)


def upload_photo(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/upload_photo.html', {
        # Pass the cat and feeding_form as context
        'event': event
    })


class EventUpdate(UpdateView):
    model = Event
    fields = ['title', 'date', 'time', 'location',
              'description', 'capacity', 'infolink', 'category']


class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'
