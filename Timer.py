#Python Program to Timer
import time
import datetime
import os
import sys

#countdown timer

def main():
    print("This is a timer")
    print("Enter the time in seconds")
    time = int(input())
    print("Enter the message")
    message = input()
    print("Enter the file name")
    fileName = input()
    print("Enter the number of times to repeat")
    repeat = int(input())
    print("Enter the time interval in seconds")
    interval = int(input())
    for i in range(repeat):
        print(message)
        time.sleep(time)
        print("Time is up")
        time.sleep(interval)
        os.system("clear")
    print("End of program")

    