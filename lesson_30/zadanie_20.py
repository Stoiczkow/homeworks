import random
import time
from multiprocessing import Pool

IMAGE_SIZE = 1000
IMAGE_COUNT = 10


def create_image(seed: int) -> list[list[float]]:
    rng = random.Random(seed)
    return [[rng.random() for _ in range(IMAGE_SIZE)] for _ in range(IMAGE_SIZE)]


def apply_filter(image: list[list[float]]) -> list[list[float]]:
    return [[pixel * 1.1 for pixel in row] for row in image]


if __name__ == "__main__":
    print("Generowanie obrazów...")
    images = [create_image(seed) for seed in range(IMAGE_COUNT)]

    start = time.time()
    sequential = [apply_filter(image) for image in images]
    sequential_time = time.time() - start
    print(f"Sekwencyjnie: {sequential_time:.2f} s")

    start = time.time()
    with Pool() as pool:
        parallel = pool.map(apply_filter, images)
    parallel_time = time.time() - start
    print(f"Równolegle:   {parallel_time:.2f} s")

    print(f"Przyspieszenie: {sequential_time / parallel_time:.2f}x")
    print(f"Wyniki identyczne: {sequential == parallel}")