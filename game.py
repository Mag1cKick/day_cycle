from fsm import MyDay

fsm = MyDay()

print("How to survive:")
print("1) hunger under {100%, 80%, 60%, 40%}\
 and over {-50%, -20%, -10%, 0%} based on the difficulty")
print("2) tiredness under {100%, 80%, 60%, 40%} based on the difficulty")
print("3) emotional stability over {0%, 20%, 40%, 80%} based on the difficulty")
print("Time to survive")
print("You can: 'wake_up' or 'sleep':")

while not fsm.end:
    print("Current time: " + str(fsm.current_time))
    print("Hunger: " + str(fsm.hunger) + "%")
    print("Tiredness: " + str(fsm.tiredness) + "%")
    print("Emotional stability: " + str(fsm.e_stability) + "%")
    action = input(">>> ")
    print()
    fsm.send(action)

if fsm.win:
    print("You survived!")
else:
    print("WASTED")