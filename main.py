from pet import Pet

def main():
    # Create a pet object
    my_pet = Pet("Fluffy")

    # Test the functionality
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("Roll Over")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
