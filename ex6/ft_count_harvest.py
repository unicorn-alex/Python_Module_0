def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")


def recursive_harvest(day: int) -> None:
    if day == 0:
        return
    if day > 0:
        recursive_harvest(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive_harvest(days)
    print("Harvest time!")
