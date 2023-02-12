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

from product.models import Product, Review
from user.models import GreenieUser
from backend_greenie.users.models import User
from integeration.cloudnary.cloudnary_main import CloudnaryMain

def create_all_users(file_name):

    with open(file_name, 'r') as file:
        # Load the JSON data from the file
        user_record = json.load(file)

    for user_detail in user_record:
        phone = user_detail['phone']
        email = user_detail['email']
        name = user_detail['name']
        gender = user_detail['gender']
        avatar_url = user_detail['avatar_url']

        try:
            user = User.objects.get(username=phone)
        except ObjectDoesNotExist:
            user = User.objects.create(username=phone, password=phone, email=email)
        
        try:
            user.greenie_user
            print(f"This user is already added: {phone}, {name}")
            continue
        except:
            pass
        cloudnary = CloudnaryMain()
        public_id = f'{name}_{phone}_{user.id}'
        status, res = cloudnary.upload_to_cloudnary_folder(avatar_url, public_id, folder_name= "/user_profile", )
        # print("status: ", status)
        # print("res: ", res)
        if status:
            greenie_user = GreenieUser.objects.create(user=user, name=name, phone=phone, gender=gender, email=email, images = res)
        else:
            print(res)
            continue

# if __name__=='__main__':
#     file_path = str(ROOT_DIR / "scripts/add_greenie_users.json")
#     create_all_users(file_path)