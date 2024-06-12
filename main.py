import datetime
import random


def main():
    generate_random_dates(number_of_birthdays())


def number_of_birthdays():
    birthdays = int(input("How many birthdays should we generate?\n> "))
    return birthdays


def generate_random_dates(num_birthdays):
    birthdays = []
    start_date = datetime.date(2024, 1, 1)

    for i in range(num_birthdays):
        num_days = datetime.timedelta(random.randint(0, 364))

        random_date = start_date + num_days

        birthdays.append(random_date)
    return birthdays


if __name__ == "__main__":
    main()
