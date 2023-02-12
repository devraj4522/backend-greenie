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

from product.models import Product, Review, Category
from user.models import GreenieUser
from integeration.cloudnary.cloudnary_main import CloudnaryMain


def add_prod_image():
    products = Product.objects.filter(is_active=True)

    for product in products:
        cloudnary = CloudnaryMain()
        public_id = f'{product.name}_{product.category}_{product.id}'
        image = product.images[0]
        status, res = cloudnary.upload_to_cloudnary_folder(image, public_id, folder_name= "/product_image", )
        print("status: ", status)
        print("res: ", res)
        if status:
            product.images = [res,]
            product.save()
        else:
            print(res)
            continue

def add_category_image():
    categories = Category.objects.filter(active=True)

    for cat in categories:
        cloudnary = CloudnaryMain()
        public_id = f'{cat.name}_{cat.id}'
        image = cat.images['images'][0]
        status, res = cloudnary.upload_to_cloudnary_folder(image, public_id, folder_name= "/product_image", )
        print("status: ", status)
        print("res: ", res)
        if status:
            cat.images = [image,]
            cat.save()
        else:
            print(res)
            continue

if __name__=='__main__':
    file_path = str(ROOT_DIR / "scripts/add_review.json")
    add_prod_image()
    # add_category_image()