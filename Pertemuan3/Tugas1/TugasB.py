from functools import reduce

def arithmetic_geometric_sequence(a, d, r, n):
    if n == 1:
        return [a] 
    else:
        prev_sequence = arithmetic_geometric_sequence(a, d, r, n - 1)
        an = (a + (n - 1) * d) * (r ** (n - 1))
        prev_sequence.append(an)
        return prev_sequence 

a = 2  # Suku pertama
d = 3  # Beda aritmetika
r = 2  # Rasio geometri
n = 5  # Menghitung suku hingga ke-5

sequence = arithmetic_geometric_sequence(a, d, r, n)
print("Baris aritmetika-geometri:", sequence)

total_sum = sum(sequence)
print("Jumlah deret:", total_sum)
