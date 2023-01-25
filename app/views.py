from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views import View
from .models import rev

class ThankYouView(TemplateView):
    template_name='Thank_you.html'
    
    #to pass dynamic content in template in template_view

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["message"]="it will work!"
        #we have loaded all the objects and displayed it in the template
        return context

# class review_list_View(TemplateView):
#     template_name='review_list.html'
#     def get_context_data(self, **kwargs):
#         # through kwargs we can get url identifier ..suppose we pass id in url as url/<int:id> ... we can get it like kwargs['id']..and can 
#         context=super().get_context_data(**kwargs)
#         context["messages"]=rev.objects.get(id=kwargs['id'])
#         #we have loaded all the objects and displayed it in the template
#         # return context
#         return context

from .forms import Review_Form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView

class form_view(View):
    def get(self,request):
        form=Review_Form()
        return render(request,'dform.html',{'form':form})

    def post(self,request):
        form=Review_Form(request.POST)
        if form.is_valid():
            # user_name=form.cleaned_data['user_name']
            # rating=form.cleaned_data['rating']
            # obj=rev.objects.create(user_name=user_name,rating=rating)
            # obj.save()
            form.save()
            
            return HttpResponse("VALID FORM DATA") 
        else:
            return HttpResponse("INVALID FORM DATA") 

#Form_view 

class Form_View(FormView):

    #THIS IS EQUIVALENT TO GET METHID CODE 
    form_class=Review_Form 
    template_name='dform.html'
    success_url='/list'    
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
    #THIS IS EQUIVALENT TO POST METHID CODE 
    #This method will be executed only if the submitted form is valid and it is executed before the sucess_url
    def form_valid(self, form):
        print('ak')
        form.save()
        return super().form_valid(form)

#Create_View it will
from  django.views.generic.edit import CreateView
#NO need to have a Form,itself creates a Modelform from given model attr
# we can even point a form_class but that form must be a modelform(in which we can configure lables and error messages) 
class create_view(CreateView):
    model=rev
    # fields='__all__'
    form_class=Review_Form
    template_name='dform.html'
    success_url='/list'
    
#can use to display list 
#By default uses get method
class review_list_View(ListView):
    template_name='review_list.html'
    model=rev
    context_object_name='reviews' #we can access reviews in template instaed of object_list
    
    def get_queryset(self):
        base_query=super().get_queryset()
        data=base_query.filter(rating__lt=4)
        return data

    
    #we can access the model object with the name of object_list in template
    # we can even overrid the ordering of the objects we get by quering def get_oredering()
    # we can also add a custom queryset instaed of fetching all the databse records
    # we can even pass context to templatate using get_context_data..
    # 
    

from django.views.generic import DetailView
#DETAIL VIEW
class SingleReviewView(DetailView):
    template_name='single_review.html'
    model=rev
    context_object_name='message'
    # we can access the model object with the name of object in template / lower_case name of model in template 

