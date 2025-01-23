#!/usr/bin/env python3

from manuever_functions import forwards,backwards,parallel_park, k_turn
action = 0
while action != 'e':
    action = input( "Use Keyboard to Select Manuever:\n Forward - 'f'             Backward - 'b'\n Parallel Park Left - 'pl'    Parallel Park Right - 'pr'\n K Turn Left = 'kl'           K Turn Right = 'kr'\n           Press e to exit\n")

    if action == 'f':
        forwards(0,40,1)
    elif action == 'b':
        backwards(0,40,1)

    elif action == 'pl':
        parallel_park("left")
    elif action == 'pr':
        parallel_park("right")
    elif action == 'kl':
        k_turn("left")
    elif action == 'kr':
        k_turn("right")

    





