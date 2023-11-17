from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This data is send from second app'
    d={'assumption':data}
    return render(request,'data_render2.html',context=d)