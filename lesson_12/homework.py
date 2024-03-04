import os
import threading
import time
from dataclasses import dataclass
from multiprocessing import Process, Queue

import requests


@dataclass
class Path:
    path: str


# CPU-bound task (heavy computation)
def encrypt_file(path: str, queue: Queue):
    start_proc = time.perf_counter()
    print(f"Processing file from {path} in process {os.getpid()}")
    # Just simulate a heavy computation
    _ = [i for i in range(100_000_000)]
    global encryption_counter
    encryption_counter = time.perf_counter() - start_proc
    queue.put(encryption_counter)


# I/O-bound task (downloading image from URL)
def download_image(image_url: Path, image_path: Path, queue: Queue):
    start_thread = time.perf_counter()
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"  # noqa
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    global download_counter
    download_counter = time.perf_counter() - start_thread
    queue.put(download_counter)


file_path = Path(path="rockyou.txt")
image_path = Path(path="image.jpg")
url_path = Path(path="https://picsum.photos/1000/1000")


if __name__ == "__main__":
    try:
        queue_of_encryption = Queue()
        queue_of_download = Queue()

        proc_ = Process(
            target=encrypt_file,
            args=(file_path.path, queue_of_encryption),
        )
        tread_ = threading.Thread(
            target=download_image,
            args=(url_path.path, image_path.path, queue_of_download),
        )

        proc_.start()
        tread_.start()

        proc_.join()
        tread_.join()

        encryption_counter = queue_of_encryption.get()
        download_counter = queue_of_download.get()

        total = encryption_counter + download_counter

        print(
            f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds"  # noqa
        )

    except Exception as e:
        print(f"Error occurred: {e}")
