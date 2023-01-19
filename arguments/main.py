# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name : str, message : str = "Hello, <name>!"):
    return message.replace("<name>", name)

print(greet("Ulrike"))
print(greet("Ulrike", "Guten Morgen, <name>!"))

def force(mass : float, body : str = "earth"):
    bodies = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    gravity = bodies[body]
    return mass * gravity

print(force(50))
print(force(50, "sun"))
print(force(50, "mars"))

def pull(m1: float, m2: float, d: float):

    g = 6.674 * 10 ** -11
    return  g * ((m1 * m2) / d ** 2)

print(pull(800, 1500, 3))

