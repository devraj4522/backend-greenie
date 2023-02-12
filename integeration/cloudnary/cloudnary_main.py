import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import os
from dotenv import load_dotenv
import logging

error_logger = logging.getLogger('error_logger')
load_dotenv()

class CloudnaryException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg
    
    def __str__(self) -> str:
        return self.error_msg

class CloudnaryMain():
    def __init__(self):
        self.cloud_name = os.environ.get("CLOUDNARY_CLOUD_NAME")
        self.api_key = os.environ.get("CLOUDNARY_API_KEY")
        self.api_secret = os.environ.get("CLOUDNARY_API_SECRET")
        self.secure = True

        try:
            cloudinary.config(
            cloud_name = self.cloud_name,
            api_key = self.api_key,
            api_secret = self.api_secret,
            secure = True
            )
        except Exception as e:
            print(e)
            raise CloudnaryException(f'{e}')
    def upload_to_cloudnary_folder(self, media_url, public_id, folder_name):
        """
        `media_url`: file_url
        `public_id`: file_name
        `folder_name`: where to upload on cloud
        """
        try:
            # response = upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", public_id="olympic_flag", folder="delete/")
            response = upload(media_url, public_id=public_id, folder=folder_name)
            if (response.get('error')):
                print("Cloudnary upload media exception: ", response.get("error"))
                raise CloudnaryException(f'{response.error}')
            else:
                error = f"Image: {media_url} uploaded successfully!"
                print(error)

        except Exception as e:
            print("Cloudnary upload media exception", e)
            raise CloudnaryException(f'{e}')
        try:
            image = cloudinary.CloudinaryImage(public_id)
            if (response.get('error')):
                print("Media uploaded to cloudiarny could not read: ", response.get("error"))
                raise CloudnaryException(response.error)
            image.public_id = f'{folder_name}/{image.public_id}'
            return True, vars(image)
        except Exception as e:
            print("Media uploaded but could not read", e)
            raise CloudnaryException(f'{e}')

if __name__ == "__main__":
    cloudinary_obj = CloudnaryMain()
    status, res = cloudinary_obj.upload_to_cloudnary_folder('https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg',"123sadf", "/delete", )
    print("status: ", status)
    print("res: ", res)