from dict_challange import my_deepcopy
import copy

original = {
    'John': ['Doctor', ['Dental', 'Spinal']],
    'Daniel': ['Engineer', ['Electrical', 'Instrumentation']],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original['John'].append('Kenya')
original['Daniel'].append('USA')

original['Daniel'][1].append('Programming')
# original['John'][1].append('Legs')

john_list = original['John']
john_list[1].append('Sucked')

print(f'original: {original}')

print(f'copy 1:{copy_1}')

print(f'copy 2: {copy_2}')


