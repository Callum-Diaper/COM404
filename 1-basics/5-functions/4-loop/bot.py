def cross_bridge(bridge_distance):
    counter = 0
    for i in range (0, bridge_distance, 1):
        counter = counter + 1 
        print("Crossed step")
    if counter >= 5:
        print("The bridge is going to collapse!")
    else:
        print("We must keep going!")

    




cross_bridge(3)
cross_bridge(6)