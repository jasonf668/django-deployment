from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random
from string import digits
import math

class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""
    line  =  "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
    def get(self, request, *args, **kwargs):
        return HttpResponse(line)

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = {}
        category_list = []

        main_url = 'https://www.fuq.com'
        req = Request(f"{main_url}/a-z")
        html_page = urlopen(req)

        soup = BeautifulSoup(html_page, "lxml")

        for category in soup.findAll('a'):
            if '/category/' in category.get('href'):
                category_list.append(category.get('href')[10:])

        context['categories'] = category_list

        return context

def random_porn(request):
    main_url = 'https://www.fuq.com'
    req = Request(f"{main_url}/a-z")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        if '/category/' in link.get('href'):
            links.append(link.get('href'))
        
    rand_category = random.choice(links)

    req = Request(f"{main_url}{rand_category}")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    num_results = 0

    for line in soup.findAll(text=True):
        if 'results' in line:
            num_results = int(''.join(c for c in line if c in digits))
            break

    vid_count = []
    for vid in soup.findAll('a'):
        if 'report' not in vid.get('href') and 't=6000' not in vid.get('href') and '/out/' in vid.get('href'):
            vid_count.append(vid.get('href'))


    len_page = len(vid_count)
    num_pages = min(100, math.ceil(num_results / len_page))

    while True:
        try:
            req = Request(f"{main_url}{rand_category}?page={random.randint(1, num_pages)}")
            html_page = urlopen(req)
            break
        except:
            continue


    soup = BeautifulSoup(html_page, "lxml")

    vid_links = []
    for vid in soup.findAll('a'):
        if 'report' not in vid.get('href') and 't=6000' not in vid.get('href') and '/item/' in vid.get('href'):
            vid_links.append(vid.get('href'))

    while True:
        try:
            my_url = f"{vid_links[random.randint(1, len_page)]}"
            return HttpResponseRedirect(my_url)
        except:
            continue

def random_star(request):
    main_url = 'https://www.fuq.com'
    req = Request(f"{main_url}/pornstar")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        if '/pornstar/' in link.get('href'):
            links.append(link.get('href'))
        
    
    while True:
        try:
            rand_pornstar = random.choice(links)
            my_url = f"{main_url}{rand_pornstar}"
            return HttpResponseRedirect(my_url)
        except:
            continue

def from_category(request):
    #return HttpResponse(f'{request.POST["my_categories"]}')
    main_url = f'https://www.fuq.com/category/{request.POST["my_categories"]}'

    #### Get number of results, number of videos per page, total number of pages, address of random vid on random page ####
    req = Request(main_url)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    num_results = 0

    for line in soup.findAll(text=True):
        if 'results' in line:
            num_results = int(''.join(c for c in line if c in digits))
            break

    vid_count = []
    for vid in soup.findAll('a'):
        if 'report' not in vid.get('href') and 't=6000' not in vid.get('href') and '/out/' in vid.get('href'):
            vid_count.append(vid.get('href'))


    len_page = len(vid_count)
    num_pages = min(100, math.ceil(num_results / len_page))

    #rand_page = random.randint(1, num_pages)
    #rand_vid = random.randint(1, len_page)
    while True:
        try:
            req = Request(f"{main_url}?page={random.randint(1, num_pages)}")
            html_page = urlopen(req)
            break
        except:
            continue


    soup = BeautifulSoup(html_page, "lxml")

    vid_links = []
    for vid in soup.findAll('a'):
        if 'report' not in vid.get('href') and 't=6000' not in vid.get('href') and '/item/' in vid.get('href'):
            vid_links.append(vid.get('href'))

    while True:
        try:
            my_url = f"{vid_links[random.randint(1, len_page)]}"
            return HttpResponseRedirect(my_url)
        except:
            continue    
    
    

def fuq(request):
    return HttpResponseRedirect('http://fuq.com/a-z/')
