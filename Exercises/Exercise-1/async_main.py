import os
import aiohttp
import asyncio
import zipfile



download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

async def downloading_uris(download_uris):
    async with aiohttp.ClientSession() as session:
        for uri in download_uris:
            async with session.get(uri) as response:
                if response.status == 200:
                    filepath = f"downloads/{os.path.basename(uri)}"
                    with open(filepath, "wb") as file:
                        print(f"Downloaded {os.path.basename(uri)}")
                        file.write(await response.read())
                else:
                    print(f"Download failed: {os.path.basename(uri)}")



async def unzip_files():
    for root, dirs, files in os.walk("downloads"):
        for file in files:
            if file.endswith(".zip"):
                filepath = os.path.join(root, file)
                with zipfile.ZipFile(filepath, 'r') as ref:
                    ref.extractall(root)
                print(f"Extracted {file} into csv")


async def deleting_zipped_version():
    for root, dirs,files, in os.walk("downloads"):
        for file in files:
            if file.endswith("zip"):
                filepath = os.path.join(root,file)
                os.remove(filepath)
                print(f"Deleted {file}")
    

async def processing_data():
    await downloading_uris(download_uris)
    await unzip_files()
    await deleting_zipped_version()



async def main():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    await processing_data()



if __name__ == "__main__":
    asyncio.run(main())
    print("Process is done!")
