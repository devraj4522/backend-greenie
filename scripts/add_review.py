import random
import json
import os
import sys
from pathlib import Path


import django
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

from product.models import Product, Review
from user.models import GreenieUser


def add_review(file_name):
    users = GreenieUser.objects.all()
    products = Product.objects.filter(is_active=True)

    with open(file_name, 'r') as file:
        # Load the JSON data from the file
        reviews = json.load(file)

    for review in reviews:
        user = random.choice(users)
        product = random.choice(products)
        review['product'] = product
        review['user'] = user
        print(review)
        Review.objects.create(title= review['title'], description = review['description'], rating = review['rating'], product = review['product'], user=review['user'])

# if __name__=='__main__':
#     file_path = str(ROOT_DIR / "scripts/add_review.json")
#     add_review(file_path)