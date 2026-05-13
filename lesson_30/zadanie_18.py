import random
import threading


class BankAccount:
    def __init__(self, initial_balance: float = 0) -> None:
        self.balance = initial_balance
        self._lock = threading.Lock()

    def deposit(self, amount: float) -> None:
        with self._lock:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False


def deposit_many(account: BankAccount, amounts: list[float]) -> None:
    for amount in amounts:
        account.deposit(amount)


def withdraw_many(account: BankAccount, amounts: list[float]) -> None:
    for amount in amounts:
        account.withdraw(amount)


if __name__ == "__main__":
    random.seed(0)
    initial_balance = 10_000.0
    account = BankAccount(initial_balance)

    deposits = [[round(random.uniform(10, 100), 2) for _ in range(50)] for _ in range(5)]
    withdrawals = [[round(random.uniform(10, 100), 2) for _ in range(50)] for _ in range(5)]

    total_deposits = sum(sum(batch) for batch in deposits)
    total_withdrawals = sum(sum(batch) for batch in withdrawals)

    threads = []
    for batch in deposits:
        threads.append(threading.Thread(target=deposit_many, args=(account, batch)))
    for batch in withdrawals:
        threads.append(threading.Thread(target=withdraw_many, args=(account, batch)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Konto miało wystarczające środki, więc wszystkie wypłaty się powiodły.
    expected = initial_balance + total_deposits - total_withdrawals
    print(f"Saldo początkowe:   {initial_balance:.2f}")
    print(f"Suma wpłat:         {total_deposits:.2f}")
    print(f"Suma wypłat:        {total_withdrawals:.2f}")
    print(f"Saldo końcowe:      {account.balance:.2f}")
    print(f"Saldo oczekiwane:   {expected:.2f}")
    print(f"Zgodność: {abs(account.balance - expected) < 1e-6}")