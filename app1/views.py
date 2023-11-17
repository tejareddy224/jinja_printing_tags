from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This Data is our Assumption'
    d={'assumption':data}
    return render(request,'data_render1.html',context=d)