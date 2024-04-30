import asyncio
import aiohttp
import os
import aiofiles

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

async def download_file(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            filepath = f"downloads/{os.path.basename(url)}"
            async with aiofiles.open(filepath, "wb") as file:
                await file.write(await response.read())
            print(f"Successfully downloaded {os.path.basename(url)}")
        else:
            print(f"Failed to download {os.path.basename(url)} from {url}")



async def download_files(session):
    tasks = [download_file(session, url) for url in download_uris]
    await asyncio.gather(*tasks)



async def fetch_data():
    async with aiohttp.ClientSession() as session:
        await download_files(session)



async def main():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    await fetch_data()

    

if __name__ == "__main__":
    asyncio.run(main())
