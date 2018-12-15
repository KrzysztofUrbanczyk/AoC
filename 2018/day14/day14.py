with open('input') as f:
    _input = f.read()

first_elf = 0
second_elf = 1

recipe = "37"
while _input not in recipe[-7:]:
    first_elf_recipe = int(recipe[first_elf])
    second_elf_recipe = int(recipe[second_elf])
    recipe += str(first_elf_recipe + second_elf_recipe)
    first_elf = (first_elf + first_elf_recipe + 1) % len(recipe)
    second_elf = (second_elf + second_elf_recipe + 1) % len(recipe)

print(recipe[int(_input):int(_input)+10])
print(recipe.index(_input))
