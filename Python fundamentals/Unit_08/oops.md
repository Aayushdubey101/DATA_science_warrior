# Classes and Objects in Python

Python is an object-oriented programming language, which means it allows you to model real-world entities as objects. Everything in Python is an object, with properties (attributes) and behaviors (methods). For example, numbers, strings, lists, and even functions are objects of their respective classes.

## What is a Class?

A class is a blueprint or template for creating objects. It defines a set of attributes and methods that the created objects will have. Think of a class as a recipe, and objects as the dishes made from that recipe.

## What is an Object?

An object is an instance of a class. When you create an object, you are creating a specific realization of the class with actual values.

## Creating a Class

To create a class in Python, use the `class` keyword followed by the class name (usually in CamelCase), and a colon. The class body contains attributes and methods.

```python
class Vehicle:
    pass  # An empty class
```

## Creating an Object

You create an object by calling the class as if it were a function.

```python
car = Vehicle()
print(car)
```

## Class Constructor (`__init__` method)

The constructor method `__init__` is a special method that is called when an object is created. It is used to initialize the object's attributes.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make  # Instance attribute
        self.model = model
        self.year = year

car = Vehicle('Toyota', 'Corolla', 2020)
print(car.make)   # Output: Toyota
print(car.model)  # Output: Corolla
print(car.year)   # Output: 2020
```

## Object Methods

Methods are functions defined inside a class that describe the behaviors of an object.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

car = Vehicle('Toyota', 'Corolla', 2020)
print(car.description())  # Output: 2020 Toyota Corolla
```

## Default Parameter Values

You can provide default values for constructor parameters to make them optional.

```python
class Vehicle:
    def __init__(self, make='Unknown', model='Unknown', year=0):
        self.make = make
        self.model = model
        self.year = year

car1 = Vehicle()
car2 = Vehicle('Honda', 'Civic', 2018)
print(car1.description())  # Output: 0 Unknown Unknown
print(car2.description())  # Output: 2018 Honda Civic
```

## Modifying Object Attributes

You can add or modify attributes of an object after it has been created.

```python
car = Vehicle('Ford', 'Mustang', 1967)
car.color = 'Red'  # Adding a new attribute dynamically
print(car.color)   # Output: Red
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class (parent class).

```python
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  # Call parent constructor
        self.battery_size = battery_size

    def battery_info(self):
        return f"This vehicle has a {self.battery_size}-kWh battery."

ev = ElectricVehicle('Tesla', 'Model S', 2021, 100)
print(ev.description())     # Output: 2021 Tesla Model S
print(ev.battery_info())    # Output: This vehicle has a 100-kWh battery.
```

## Method Overriding

A child class can override methods of the parent class to provide specialized behavior.

```python
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def description(self):
        parent_desc = super().description()
        return f"{parent_desc} with a {self.battery_size}-kWh battery"

ev = ElectricVehicle('Tesla', 'Model 3', 2022, 75)
print(ev.description())  # Output: 2022 Tesla Model 3 with a 75-kWh battery
```



## Getter and Setter Methods

In Python, getter and setter methods are used to access and update the values of private attributes in a controlled way. Python provides the `@property` decorator to define getters, and the `@<property_name>.setter` decorator to define setters.

### Example: Using Getter and Setter

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute by convention

    @property
    def name(self):
        """Getter method"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method with validation"""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

p = Person("Alice")
print(p.name)  # Access using getter

p.name = "Bob"  # Update using setter
print(p.name)

# p.name = 123  # This will raise ValueError
```

Using getter and setter methods allows you to add validation logic and encapsulate the internal representation of attributes.
 
 ## Summary

- Classes define the structure and behavior of objects.
- Objects are instances of classes.
- The `__init__` method initializes object attributes.
- Methods define object behaviors.
- Inheritance allows code reuse and extension.
- Method overriding customizes behavior in subclasses.

Practice creating your own classes and objects to get comfortable with these concepts!