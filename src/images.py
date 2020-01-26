from google_images_download import google_images_download
import os
import glob
import re
#instantiate the class

def  images(theme):
    imgDir = './downloads'

    for filename in os.listdir(os.path.abspath(imgDir)):
        os.remove(os.path.join(os.path.abspath(imgDir), filename))

    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":(str(theme)+','+str(theme)),"limit":2,"print_urls":True, "output_directory": '.', "image_directory": '/downloads'}
    paths = response.download(arguments)
    print(paths)
    
    for filename in os.listdir(os.path.abspath(imgDir)):
        try :
            with open(os.path.join(os.path.abspath(imgDir), filename)) as im:
                im = im
        except :
            os.remove(os.path.join(os.path.abspath(imgDir), filename))

    for filename in os.listdir(os.path.abspath(imgDir)):
        newName = re.sub(r'\..*?\.','.', filename)
        print(filename, newName)
        os.rename(os.path.join(os.path.abspath(imgDir),filename), os.path.join(os.path.abspath(imgDir), newName))

