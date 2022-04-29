
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sport
from .models import Comment
from .models import Champions
from .models import Registration
from .form import CommentForm
from .form import AddRegistrationForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.

def main(request):
   sport = Sport.objects.all()
   sport_info = {'sports': sport}
   return render(request, 'main.html', sport_info) 

def football(request):
   sport = Sport.objects.get(pk=4)
   sport_info = {'sports': sport}
   return render(request, 'football.html', sport_info) 

def wrestling(request):
   sport = Sport.objects.get(pk=1)
   sport_info = {'sports': sport}
   return render(request, 'football.html', sport_info) 

def createComment(request):
   form = CommentForm()

   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/sport')

   context = {'form':form}
   return render(request, 'comment_form.html', context)

def updateComment(request, pk):
   comment = Comment.objects.get(id=pk)
   form = CommentForm(instance=comment)
   if request.method == 'POST':
      form = CommentForm(request.POST, instance=comment)
      if form.is_valid():
         form.save()
         return redirect('/sport')
   context = {'form': form}
   return render(request, 'comment_form.html', context)

def deleteComment(request, pk):
   comment = Comment.objects.get(id=pk)
   if request.method == 'POST':
      comment.delete()
      return redirect('/sport')
   context = {'item': comment}
   return render(request, 'delete_comment.html', context)

def Comments(request):
   comment = Comment.objects.all()
   com = {'comments': comment}
   return render(request, 'comments.html', com)

def Football_comments(request):
   comment = Comment.objects.filter(Sport='football')
   com = {'comments':comment}
   return render(request, 'football_comments.html', com)

def Wrestling_comments(request):
   comment = Comment.objects.filter(Sport='wrestling')
   com = {'comments':comment}
   return render(request, 'wrestling_comments.html', com)

def Boxing_comments(request):
   comment = Comment.objects.filter(Sport='boxing')
   com = {'comments':comment}
   return render(request, 'boxing_comments.html', com)

def Weightlifting_comments(request):
   comment = Comment.objects.filter(Sport='weightlifting')
   com = {'comments':comment}
   return render(request, 'weightlifting_comments.html', com)

def Hockey_comments(request):
   comment = Comment.objects.filter(Sport='hockey')
   com = {'comments':comment}
   return render(request, 'hockey_comments.html', com)


def Champs(request):
   cpns = Champions.objects.all()
   champions = {'champions':cpns}
   return render(request, 'champions.html', champions)

def AddRegistration(request):
   if request.method == 'POST':
      form = AddRegistrationForm(request.POST)
      if form.is_valid():
          try:
             form.save()
             return redirect('/sport/user_info')
          except:
             form.add_error(None, 'Error occured')
   else:
      form = AddRegistrationForm()
   return render(request, 'registration.html', {'form':form})

def user_info(request):
   registration = Registration.objects.last()
   return render(request, 'user_info.html', {'registrations': registration})

"""
def send_message(request):
   send_mail("Backend", "Some message", "alyara.erleskyzy@gmail.com", ["alyara.erleskyzy@gmail.com","200103282@stu.sdu.edu.kz"],
             fail_silently=False)
   return render(request, "mail.html")
"""
def send_file(request):
   email = EmailMessage(
      'Subject',
      'Content',
      'alyara.erleskyzy@gmail.com',
      ['200103282@stu.sdu.edu.kz'],
      headers = {'Message_ID': 'f'}
   )

   email.attach_file('C:/Users/alyar/Downloads/12-дәріс.pptx')
   email.send(fail_silently=False)
   return render(request, "mail.html")
