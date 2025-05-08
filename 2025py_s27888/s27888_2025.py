import random

def generate_dna_sequence(length, name, description, my_name):
    # Przechowywanie skladowych DNA
    nucleotides = ['A', 'C', 'G', 'T']
    # Tworzenie losowej sekwencji bazowanej na atrybutach
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    
    # ORGINAL
    #sequence = my_name + sequence

    # MODIFIED (Wstawienie imienia w losowe miejsce sekwencji, AI najwyrazniej postanowilo ze pozycja 0 jest losowa)
    insertion_index = random.randint(0, length - 1)
    sequence = sequence[:insertion_index] + my_name + sequence[insertion_index:]
    
    # Obliczanie ilosci poszczegolnych nukleotydow
    a_count = sequence.count('A')
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    t_count = sequence.count('T')
    
    # Obliczanie dlugosci z imieniem
    total_length = len(sequence)
    
    # Procentowa zawartość każdego nukleotydu
    a_percentage = (a_count / total_length) * 100
    c_percentage = (c_count / total_length) * 100
    g_percentage = (g_count / total_length) * 100
    t_percentage = (t_count / total_length) * 100
    
    # Stosunek zawartości C i G względem A i T
    # ORIGINAL
    #cg_at_ratio = ((c_count + g_count) / (a_count + t_count)) * 100 if (a_count + t_count) > 0 else 0
    # MODIFIED (Zadanie prosi o RATIO, a chat wyplul PERCENTAGE. Poprawione w celach zadania)
    cg_at_ratio = str(round(c_percentage + g_percentage, 2)) + "/" + str(round(a_percentage + t_percentage, 2))
    
    # Zapisywanie sekwencji do pliku FASTA
    fasta_filename = f"{name}.fasta"
    with open(fasta_filename, "w") as fasta_file:
        fasta_file.write(f">{name} {description}\n")
        fasta_file.write(sequence + "\n")
    
    # Wyświetlanie statystyk
    print(f"Zapisano sekwencję do pliku {fasta_filename}")
    print("Statystyki sekwencji:")

    # ORGINAL
    #print(f"A: {a_percentage:.1f}%")
    #print(f"C: {c_percentage:.1f}%")
    #print(f"G: {g_percentage:.1f}%")
    #print(f"T: {t_percentage:.1f}%")

    # MODIFIED (Biolodzy to tez ludzie, zasluguja na ladne kolorki)
    print(f"\033[34mA\033[0m: {a_percentage:.1f}%")
    print(f"\033[31mC\033[0m: {c_percentage:.1f}%")
    print(f"\033[32mG\033[0m: {g_percentage:.1f}%")
    print(f"\033[33mT\033[0m: {t_percentage:.1f}%")

    print("CG to AT ratio: " + cg_at_ratio)



# INTERAKCJA Z UŻYTKOWNIKIEM
length = int(input("Podaj długość sekwencji: "))
name = input("Podaj ID sekwencji: ")
description = input("Podaj opis sekwencji: ")
my_name = input("Podaj imię: ")

# Generowanie sekwencji
generate_dna_sequence(length, name, description, my_name)
