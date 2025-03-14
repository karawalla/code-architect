# Factory Pattern Example

This example demonstrates the Factory Pattern, a creational design pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created.

## Structure

- `Animal`: Abstract base class defining the interface
- `Dog`, `Cat`: Concrete implementations of the Animal interface
- `AnimalFactory`: Factory class that creates specific animal instances

## Benefits

1. Encapsulates object creation logic
2. Provides flexibility to add new types without modifying existing code
3. Promotes loose coupling between creator and concrete products

## Running the Example

```bash
python factory_example.py
```

## Expected Output

```
Dog says: Woof!
Cat says: Meow!
```
