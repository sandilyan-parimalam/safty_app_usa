from django.shortcuts import render, redirect
from django.urls import reverse

from tabulate import tabulate
from .config import API_CONFIG

def report_view(request):
    if request.method == 'GET':
        # Handle the initial page load (GET request)
        return render(request, 'reports/report.html', {
            'table': '',
            'error': None,
            'start_date': '',
            'start_time': '00:00',
            'end_date': '',
            'end_time': '00:00',
            'location': 'newyork',  # Default to New York
            'locations': API_CONFIG
        })
    
    elif request.method == 'POST':
        # Handle the form submission (POST request)
        location = request.POST.get('location', 'newyork')  # Default to New York City if not specified
        start_date = request.POST.get('start_date', '')
        start_time = request.POST.get('start_time', '00:00')
        end_date = request.POST.get('end_date', '')
        end_time = request.POST.get('end_time', '00:00')

        # Dynamically load the appropriate module based on the location
        if location in API_CONFIG:
            location_module = __import__(f'reports.{location}', fromlist=['*'])  # Corrected import statement
            api_url = API_CONFIG[location]['api_url']
            
            start_datetime = location_module.format_datetime(start_date, start_time)
            end_datetime = location_module.format_datetime(end_date, end_time)

            constructed_url = location_module.construct_api_url(api_url, start_datetime, end_datetime)
            data = location_module.fetch_data(constructed_url)
            
            if "error" in data:
                error = data["error"]
            else:
                rows = location_module.process_newyork_data(data)  # Adjust this method name to match your actual method
                table = tabulate(rows, headers=location_module.HEADERS, tablefmt="html")
                error = None
            
            return render(request, 'reports/report.html', {
                'table': table,
                'error': error,
                'start_date': start_date,
                'start_time': start_time,
                'end_date': end_date,
                'end_time': end_time,
                'location': location,
                'locations': API_CONFIG
            })
        
        return render(request, 'reports/report.html', {
            'error': 'Invalid location selected',
            'locations': API_CONFIG
        })
