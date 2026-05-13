import multiprocessing


def power(base: int, exponent: int) -> None:
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")


if __name__ == "__main__":
    process = multiprocessing.Process(target=power, args=(5, 3))
    process.start()
    process.join()
