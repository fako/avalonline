from django.shortcuts import render_to_response, RequestContext


def start_avalonline(request):
    return render_to_response('start_avalonline.html', {}, RequestContext(request))