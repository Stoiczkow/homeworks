import multiprocessing
import random
import time


IMAGE_COUNT = 10
IMAGE_SIZE = 300


def create_image(size):
    return [
        [random.randint(0, 255) for _ in range(size)]
        for _ in range(size)
    ]


def apply_filter(image):
    processed_image = []

    for row in image:
        processed_row = []

        for pixel in row:
            new_pixel = pixel * 1.1

            if new_pixel > 255:
                new_pixel = 255

            processed_row.append(new_pixel)

        processed_image.append(processed_row)

    return processed_image


if __name__ == "__main__":
    images = [create_image(IMAGE_SIZE) for _ in range(IMAGE_COUNT)]

    # Wersja sekwencyjna
    start = time.time()

    sequential_results = []

    for image in images:
        result = apply_filter(image)
        sequential_results.append(result)

    end = time.time()
    print(f"Sekwencyjnie: {end - start:.2f} sekund")

    # Wersja równoległa przez procesy
    start = time.time()

    with multiprocessing.Pool() as pool:
        parallel_results = pool.map(apply_filter, images)

    end = time.time()
    print(f"Procesy: {end - start:.2f} sekund")

    print(f"Liczba przetworzonych obrazów sekwencyjnie: {len(sequential_results)}")
    print(f"Liczba przetworzonych obrazów równolegle: {len(parallel_results)}")