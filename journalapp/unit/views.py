from django.shortcuts import render
from .forms import UnitForm, EditUnitForm, URLForm
from .models import Unit, UnitTag


from bs4 import BeautifulSoup
import requests

import ollama

    
def get_text(url: str) -> str:

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    body = soup.find("div", {"id": "post-content-body"})

    text = body.text
    return text

def get_summary(text:str) -> str:

    clean_text = text.replace('\n', ';').replace(';;', ';').replace('\"', '').replace('\'', '')

    stream = ollama.chat(
    model='llama3.1',
    messages=[{
        'role': 'user',
        'content': f'Сделай краткий пересказ статьи. Выдели десять основных пунктов: "{clean_text}"',
    }],
    stream=True,
    )

    summary = ''
    for chunk in stream:
        summary += chunk['message']['content']
    return summary



# Create your views here.


def knowledges_page(request):
    queryset_units = Unit.objects.all().filter(user=request.user)
    queryset_tags = UnitTag.objects.all()
    context = {'units': queryset_units, 'tags': queryset_tags}
    return render(request, 'knowledges.html', context)


def create_unit(request):
    message = 'Error'

    if request.method == 'POST':

        form = URLForm(request.POST)
        message = 'OK'
        if form.is_valid():
            return render(request, 'edit_unit.html', { 'message': message })
    
    else:
        
        form = URLForm()
        message = 'Fill out form'
        
        return render(request, 'unit.html', { 'form': form, 'message': message })

                
def edit_unit(request, unit_id=None):
    message = 'Error'

    if request.method == 'POST':
        
        if 'download' in request.POST:
            
            form = URLForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['url']

                text = get_text(url)

                summary = get_summary(text)
                
                data = {
                    'url': url,
                    'unit': text,
                    'text': summary
                    }
                
                next_form = UnitForm(data)

                context = { 'form': next_form, 'message': message }
                return render(request, 'edit_unit.html', context)
        
        if unit_id:
                
            unit = Unit.objects.get(pk=unit_id)

            form = EditUnitForm(request.POST, instance=unit)

            if form.is_valid():
                
                text = form.cleaned_data['text']
                unit = form.cleaned_data['unit']
                url = form.cleaned_data['url']

                unit = Unit(pk=unit_id, user=request.user, text=text, unit=unit, url=url)
                unit.save()

                message = 'Unit saved'

        else:
            
            form = UnitForm(request.POST)
            
            if form.is_valid():
                
                text = form.cleaned_data['text']
                unit = form.cleaned_data['unit']
                url = form.cleaned_data['url']
                
                unit = Unit(user=request.user, text=text, unit=unit, url=url)
                unit.save()

                message = 'Unit saved'
                
        queryset = Unit.objects.all().filter(user=request.user)
        context = {'units': queryset, 'message': message }
        return render(request, 'knowledges.html', context)
    
    else:

        if unit_id:

            unit = Unit.objects.get(pk=unit_id)
            form = EditUnitForm(instance=unit)

            message = 'Edit form'

    return render(request, 'edit_unit.html', { 'form': form, 'message': message })