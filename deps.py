#!/usr/bin/python3

requirements_path = "requirements.txt"
dependencies = []

with open(requirements_path, "r") as file:
    for line in file:
        dependencies.append(line.strip())

# Now, print them out or append directly to your pyproject.toml
for dep in dependencies:
    print(f'"{dep}",')
