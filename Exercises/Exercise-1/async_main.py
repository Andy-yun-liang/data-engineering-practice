import os
import aiohttp
import asyncio

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
                        print(f"Downloading zip file: {os.path.basename(uri)}")
                        file.write(await response.read())
                else:
                    print(f"Zip file: {os.path.basename(uri)} cannot be downloaded")

async def unZippingFiles():
    await downloading_uris(download_uris)

async def main():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    await unZippingFiles()

if __name__ == "__main__":
    asyncio.run(main())
