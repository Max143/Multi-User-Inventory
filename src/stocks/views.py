from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def StocksView(request):
    return render(request, 'stocks/stocks_unit.html')

