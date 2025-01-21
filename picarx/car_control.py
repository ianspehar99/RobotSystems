#!/usr/bin/env python3
from manuever_functions import forwards,backwards,parallel_park

action = input("Use Keyboard to Select Manuever:\n Forward - 'f'\n Backward - 'b'\n Parallel Park Left - 'pl'\n Parallel Park Right - 'pr'\nK Turn Left = 'kl'\n K Turn Right = 'kr'\n")

if action == 'f':
    forwards(0,10,1)
if action == 'b':
    forwards(0,10,1)
