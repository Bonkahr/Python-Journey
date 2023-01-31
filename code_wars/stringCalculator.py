def count_smileys(arr: list) -> int:
    smiley = [':D', ':)', ':-D', ':~D', ':-D', ':~)', ';D', ';)', ';-D',
              ';~D', ';-D', ';~)']
    return len([smile for smile in arr if smile in smiley])


print(count_smileys([':D', ':~)', ';~D', ':)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))


def zeros(n):
    x = n // 5
    return x + zeros(x) if x else 0


print(zeros(6))


def DNA_strand(dna):
    dna_comp = {
        'A': 'T',
        'C': 'G'
    }

    result = []
    for x in dna:
        if x in dna_comp.keys():
            result.append(dna_comp[x])
        elif x in dna_comp.values():
            pass
    return result


print(DNA_strand('ACTG'))
