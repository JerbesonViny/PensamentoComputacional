import math

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(f'({x}^2 + {y}^2 + {z}^2)^1/3 = {(x**2 + y**2 + z**2)**(1/3)}')
print(f'{x}^{y} + {y}^{z} = {x**y + y**z}')
print(f'cos({x}^2 + {y}^2) + sin({y}^2 + {z}^2) = {math.cos((x**2 + y**2)) + math.sin((y**2 + z**2))}')
print(f'(log {x} + log {y} + log {z}) ^ ({x} + {y} + {z}) = {(math.log(x) + math.log(y) + math.log(z))**(x+y+z)}')