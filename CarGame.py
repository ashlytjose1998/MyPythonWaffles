command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car started! Ready to Go!!")
    elif command == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car stopped!!")
    elif command == "quit":
        print("Thanks for playing!")
        exit(0)
    elif command == "help":
        print("""
        start - start the car.
        stop - stop the car.
        quit - exit the game.        
        """)
    else:
        print("I don't understand :( ")