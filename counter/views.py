from django.shortcuts import render
import json
import requests


# Create your views here.
def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        # USDA Food Data Central API
        api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
        params = {
            'api_key': 'AyzLwaHsTj5iwPUZIlu96gi13BPMXviTSDU14MCt',  # Replace with your USDA API key
            'query': query,
            'pageSize': 1,
            'dataType': ['Survey (FNDDS)']  # This gives us detailed nutritional data
        }
        try:
            api_request = requests.get(api_url, params=params)
            data = json.loads(api_request.content)
            
            if data.get('foods') and len(data['foods']) > 0:
                food = data['foods'][0]
                nutrients = food.get('foodNutrients', [])
                
                # Extract relevant nutritional information
                api = [{
                    'name': food.get('description', ''),
                    'calories': next((n['value'] for n in nutrients if n['nutrientName'] == 'Energy'), 0),
                    'serving_size_g': 100,  # USDA data is typically per 100g
                    'protein_g': next((n['value'] for n in nutrients if n['nutrientName'] == 'Protein'), 0),
                    'fat_total_g': next((n['value'] for n in nutrients if n['nutrientName'] == 'Total lipid (fat)'), 0),
                    'carbohydrates_total_g': next((n['value'] for n in nutrients if n['nutrientName'] == 'Carbohydrate, by difference'), 0),
                }]
            else:
                api = []
                
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
