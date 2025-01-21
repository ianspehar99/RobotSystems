#!/usr/bin/env python3
from manuever_functions import forwards,backwards,parallel_park

action = input("Use Keyboard to Select Manuever:\n Forward - 'f'\n Backward - 'b'\n Parallel Park - 'p'\n K Turn = 'k'\n")

if action == 'f':
    speed = float(input("Speed:"))
    angle = float(input("Angle:"))
    time = (input("Time:"))
    forwards(angle, speed, time)

