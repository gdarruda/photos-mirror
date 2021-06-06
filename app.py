from async_download import save_file
from pyicloud import PyiCloudService
from config import settings

import logging
import sys

api = PyiCloudService(settings.icloud.user, 
                      settings.icloud.password)

if api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = api.validate_2fa_code(code)
    print("Code validation result: %s" % result)

    if not result:
        print("Failed to verify security code")
        sys.exit(1)

logging.basicConfig(format='%(levelname)s:%(asctime)s - %(message)s', 
                    level=logging.INFO)

download_path = 'downloads/'

for photo in api.photos.all:
    
    logging.info(f"Photo {photo.filename} processing...")

    if save_file.delay(photo.versions['original']['url'], photo.filename):
        logging.info(f"Photo {photo.filename} queued!")

    if 'alternative' in photo.versions:
        
        alternative = photo.versions['alternative']
        filename = photo.filename

        if alternative['type'] == 'com.fuji.raw-image':
            filename =  filename.split(".")[0] + ".RAF"
        elif alternative['type'] == 'com.canon.cr2-raw-image':
            filename =  filename.split(".")[0] + ".cr2"
        else:
            logging.warn(f"Extension not identified: {alternative['type']}")

        if save_file.delay(alternative['url'], filename):
            logging.info(f"RAW Photo {filename} queued!")

logging.info(f"Process finished!")