from car import Car
from race import Race


def main():
    red_speed = input("Please select speed for the red car: ")
    blue_speed = input("Please select speed for the blue car: ")

    c1 = Car('red', red_speed)
    c2 = Car('blue', blue_speed)

    race = Race([c1, c2])
    print(f"And the winner is... {race.winner().color} car")


if __name__ == '__name__':
    main()
