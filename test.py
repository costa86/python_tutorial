import asyncio
import random


async def download_file(file_name: str) -> None:
    print(f"Starting to download {file_name}")
    random_time_to_wait = random.randint(1, 5)
    await asyncio.sleep(random_time_to_wait)
    print(f"Finished downloading {file_name}")


async def perform_other_task(task_name: str) -> None:
    print(f"Starting {task_name}")
    random_time_to_wait = random.randint(1, 3)
    await asyncio.sleep(random_time_to_wait)
    print(f"Finished {task_name}")


async def main():
    download_task = asyncio.create_task(download_file("example_file.txt"))
    other_task = asyncio.create_task(perform_other_task("other_task"))

    await download_task
    await other_task


asyncio.run(main())
