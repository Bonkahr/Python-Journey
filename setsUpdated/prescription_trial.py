from prescription_data import *

trial_patient = ["Denise", 'Eddie', 'Frank', 'George', 'Kenny']

# remove Warfarin and add Edoxabin

for patient in trial_patient:
    prescription = patients[patient]
    print(f'{patient} -> {prescription}')
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        pass
    print(f'{patient} -> {prescription}')
    print('#' * 150)
