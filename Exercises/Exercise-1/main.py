import requests
import os
import zipfile
from urllib.parse import urlparse

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]



def verify_url_and_download():

 if not os.path.exists("downloads"):
    os.makedirs("downloads")
        
    for url in download_uris: 
            
        response = requests.get(url)
        uri = urlparse(url).path

        if response.status_code == 200:

            filepath = f"downloads/{uri}"

            with open(filepath,"wb") as f:
                f.write(response.content)
            
            print(f"Successfully saved zip file '{uri}' into 'downloads'")

            extract_zip_dl_csv(filepath)
            
            
        else:
            print(f"Failed to download zip file '{uri}': {response.status_code}")


def extract_zip_dl_csv(filepath):

    #extracting csv
    with zipfile.ZipFile(filepath,"r") as ref:
      ref.extractall("downloads")

    print(f"Successfully extracted csv from zip file at {filepath}")
    
    #deleting zipfile
    os.remove(filepath)
    print(f"Successfully deleted {filepath}")

def main():
   
   verify_url_and_download()
    


if __name__ == "__main__":
    main()
