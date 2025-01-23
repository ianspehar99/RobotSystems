#!/usr/bin/env python3
from manuever_functions import forwards,backwards,parallel_park, k_turn

action = input("Use Keyboard to Select Manuever:\n Forward - 'f'\n Backward - 'b'\n Parallel Park Left - 'pl'\n Parallel Park Right - 'pr'\nK Turn Left = 'kl'\n K Turn Right = 'kr'\n")

if action == 'f':
    forwards(0,40,1)
elif action == 'b':
    forwards(0,40,1)

elif action == 'pl':
    parallel_park("left")
elif action == 'pr':
    parallel_park("right")
elif action == 'kl':
    k_turn("left")
elif action == 'kr':
    k_turn("right")



    





