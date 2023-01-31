# farm_animals = {'sheep', 'goat', 'dog', 'cow', 'cat'}
# wild_animals = {'lion', 'elephant', 'giraffe', 'panther'}
#
# all_animals = farm_animals.union(wild_animals)  # Any way same result
# print(all_animals)
#
# # union operator '|'
#
# all_animals = wild_animals | farm_animals
# print(all_animals)
#
from prescription_data import adverse_interactions
# extracting all drugs from the set

meds_to_watch = set()

for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction) #creating new set
    # meds_to_watch.update(interaction)   # updating the set
    meds_to_watch |= interaction    # same as update above
print(sorted(meds_to_watch))

# real update method in use
meds_to_watch.update(*adverse_interactions)  # the * iterates inserting the set
# with the each item

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
