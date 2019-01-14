from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.db.models import Q
#from django.template import loader
from .models import Target, Country, PGAG

def welcome(request):
    return render(request, 'dataentry/welcome.html')

def country(request):
    countries = Country.objects.all().order_by("name")
    #groups = PGAG.objects.all()
    ctg = {}
    for c in countries:
        ctg[c] = set()

    #for g in groups:
    #    ctg[g.country].add(g)


    ctglist = []
    for c in countries:
        ctglist.append([c])

    return render(request, 'dataentry/countries.html', {'ctglist': ctglist}) 
    #return render(request, 'dataentry/countries.html')


def index(request):
    latest_target_list = Target.objects.order_by('target_name')[:5]
    #template = loader.get_template('dataentry/index.html')
    context = {'latest_target_list': latest_target_list}
    #output = ', '.join([t.target_name for t in latest_target_list])
    return render(request, 'dataentry/index.html', context)

def results(target, target_id):
    response = "You're looking at the results of Target %s."
    return HttpResponse(response % target_id)

def vote(request, target_id):
    return HttpResponse("You're voting on Target %s." % target_id)

def detail_country(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    groups = PGAG.objects.filter(country=country_id).order_by("name")
    grl = {}
    for g in groups:
        grl[g] = set()
    grlist = []
    for g in groups:
        grlist.append([g, grl[g]])
    
    groups2 = PGAG.objects.filter(country=country_id, finished="no").order_by("name")
    return render(request, 'dataentry/detail_country.html', {'country': country, 'groups': groups, 'grlist' : grlist, 'groups2' : groups2})

def detail_group(request, pgag_id):
    pgag = get_object_or_404(PGAG, pk=pgag_id)
    return render(request, 'dataentry/detail_group.html', {'pgag': pgag})
    #    for line in PGAG.GOVREL:
    #    if pgag.government_relation == line[0]:
    #        return render_to_response('pgag_detail.html', 
    #                                  {'pgag': pgag, 'pname': line[1]})

def datasets(request):
    return render(request, 'dataentry/datasets.html')

def imprint(request):
    return render(request, 'dataentry/imprint.html')

def privacy(request):
    return render(request, 'dataentry/privacy.html')

def about_us(request):
    return render(request, 'dataentry/about_us.html')

def more_info(request):
    return render(request, 'dataentry/more_info.html')

def regions(request):
    return render(request, 'dataentry/regions.html')

def groups(request):
    countries = Country.objects.all().order_by("name")
    groups = PGAG.objects.all()
    groups2 = PGAG.objects.filter(finished="yes")
    ctg = {}
    for c in countries:
        ctg[c] = set()

    for g in groups:
        if g in groups2:
            ctg[g.country].add(g)
        else:
            ctg[g.country].add("not finished yet")


    ctglist = []
    for c in countries:
        ctglist.append([c, ctg[c]])

    return render(request, 'dataentry/groups.html', {'ctglist': ctglist}) 

def region_asia(request):
    countries = Country.objects.filter(level1region="Asia").order_by("name")
    ctg = {}
    for c in countries:
        ctg[c] = set()

    ctglist = []
    for c in countries:
        ctglist.append([c, ctg[c]])

    return render(request, 'dataentry/region_asia.html', {'ctglist': ctglist}) 

def region_africa(request):
    countries = Country.objects.filter(level1region="Africa").order_by("name")
    ctg = {}
    for c in countries:
        ctg[c] = set()

    ctglist = []
    for c in countries:
        ctglist.append([c, ctg[c]])

    return render(request, 'dataentry/region_africa.html', {'ctglist': ctglist}) 

def region_americas(request):
    countries = Country.objects.filter(level1region="Americas").order_by("name")
    ctg = {}
    for c in countries:
        ctg[c] = set()

    ctglist = []
    for c in countries:
        ctglist.append([c, ctg[c]])

    return render(request, 'dataentry/region_americas.html', {'ctglist': ctglist}) 

def region_europe(request):
    countries = Country.objects.filter(level1region="Europe").order_by("name")
    ctg = {}
    for c in countries:
        ctg[c] = set()

    ctglist = []
    for c in countries:
        ctglist.append([c, ctg[c]])

    return render(request, 'dataentry/region_europe.html', {'ctglist': ctglist}) 

def region_oceania(request):
    countries = Country.objects.filter(level1region="Oceania").order_by("name")
    ctg = {}
    for c in countries:
        ctg[c] = set()

    ctglist = []
    for c in countries:
        ctglist.append([c, ctg[c]])

    return render(request, 'dataentry/region_oceania.html', {'ctglist': ctglist}) 

def search_country(request):
    #if not request.user.is_authenticated():
    #    return render_to_response('login_error.html')

    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query)
            )
        results = Country.objects.filter(qset).distinct().order_by('name')
    else:
        results = []
    # return render(request, 'dataentry/search_country.html')
    return render(request, 'dataentry/search_country.html', {
        "results": results,
        "query": query
        })

def search_pgag(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query)
            )
        results = PGAG.objects.filter(qset, finished="yes").distinct().order_by('name')

        country2pgag = {}
        for pgag in results:
            country2pgag[pgag.country] = []
        for pgag in results:
            country2pgag[pgag.country].append(pgag)

        ck = country2pgag.keys()
        #ck.sort(key=lambda x: x.name)
        results = []
        for el in ck:
            results.append( [el, country2pgag[el]] )

    else:
        results = []
    return render(request, 'dataentry/search_pgag.html', {
            "results": results,
            "query": query
            })
    # return render(request, 'dataentry/search_pgag.html')

def type(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    # return render_to_response("type.html", {'rels': PGAG.GOVREL})
    return render(request, 'dataentry/type.html')

def link(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    # govlink = GovernmentLink.objects.all().order_by("name")
    # return render_to_response("link.html", {'lin': govlink})
    return render(request, 'dataentry/link.html')

def support(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    # sup = Support.objects.all().order_by("type")
    # return render_to_response("support.html", {'supports': sup})
    return render(request, 'dataentry/support.html')

def member(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    # memberchar = MemberCharacteristic.objects.all().order_by("name")
    # return render_to_response("member.html", {'mc': memberchar})
    return render(request, 'dataentry/member.html')

def target(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    # targs = Target.objects.all().order_by("type")
    # return render_to_response("target.html", {'targets': targs})
    return render(request, 'dataentry/target.html')

def purpose(request):
    # if not request.user.is_authenticated():
    #     return render_to_response('login_error.html')

    # purp = Purpose.objects.all().order_by("name")
    # return render_to_response("purpose.html", {'purpose': purp})
    return render(request, 'dataentry/purpose.html')