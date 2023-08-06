import random
import json
import os
import sys
from pathlib import Path
import shortuuid


import django
from django.core.exceptions import ObjectDoesNotExist
from platformdirs import user_config_dir


# This allows easy placement of apps within the interior
# antler directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR))
sys.path.append(str(ROOT_DIR / "backend_greenie"))
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from product.models import Product, Review, Category
import random

all_categories = Category.objects.all()
with open('scripts/data_transfer.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)
    
# for item in data:
#     model = item['model'].split('.')[-1]
#     model = model.title()
    
    # if model == 'Category':
    #     Category.objects.create(**item['fields'])
    
    # if model == 'Product':
    #     item['fields']['category'] = random.choice(all_categories)
        # Product.objects.create(**item['fields'])
        
for product in Product.objects.all():
    images = product.images
    image = images[0]
    url = image['public_pk']
    del image['public_pk']
    image['public_id'] = url
    
    product.images[0] = image
    
    product.save()