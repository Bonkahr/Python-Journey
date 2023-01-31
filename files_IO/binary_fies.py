with open("binary", 'bw') as bin_file:
    bin_file.write(bytes(range(17)))

with open("binary", 'br') as my_bin_file:
    for b in my_bin_file:
        print(b)
