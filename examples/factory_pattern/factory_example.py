from abc import ABC, abstractmethod

# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage Example
def main():
    factory = AnimalFactory()
    
    # Create a dog
    dog = factory.create_animal("dog")
    print(f"Dog says: {dog.speak()}")
    
    # Create a cat
    cat = factory.create_animal("cat")
    print(f"Cat says: {cat.speak()}")

if __name__ == "__main__":
    main()
