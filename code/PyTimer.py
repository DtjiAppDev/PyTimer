"""
This file contains implementation of a timer using Python programming language.
Author: CreativeCloudAppDev2020
"""


import time
import sys


class Timer:
    """
    This class contains attributes of a timer.
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours: int = hours if 0 <= hours <= 23 else 0
        self.minutes: int = minutes if 0 <= minutes <= 59 else 0
        self.seconds: int = seconds if 0 <= seconds <= 59 else 0

    def to_seconds(self) -> int:
        return 3600 * self.hours + 60 * self.minutes + self.seconds

    def tick(self) -> None:
        if self.seconds > 0:
            self.seconds -= 1
        elif self.seconds == 0 and self.minutes > 0:
            self.minutes -= 1
            self.seconds = 59
        elif self.seconds == 0 and self.minutes == 0 and self.hours == 0:
            self.hours = 23
            self.minutes = 59
            self.seconds = 59
        else:
            self.hours -= 1
            self.minutes = 59
            self.seconds = 59

    def countdown(self) -> None:
        if self.to_seconds() == 0:
            print(self.__str__())
            print("FINISHED!")
        else:
            print(self.__str__())
            time.sleep(1)
            self.tick()
            self.countdown()

    def __str__(self) -> str:
        return "(" + str(self.hours) + ", " + str(self.minutes) + ", " + str(self.seconds) + ")"


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'PyTimer' by 'CreativeCloudAppDev2020'.")
    print("This application works like a normal timer.")

    print("Please enter the amount of time interval to be measured by the timer.")
    hours: int = int(input("How many hours? "))
    minutes: int = int(input("How many minutes? "))
    seconds: int = int(input("How many seconds? "))
    t: Timer = Timer(hours, minutes, seconds)
    t.countdown()

    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using the timer? ")
    if continue_using == "Y":
        main()
    sys.exit()


if __name__ == '__main__':
    main()
