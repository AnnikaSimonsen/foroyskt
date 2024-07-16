from foroyskt import Bin
b = Bin()

print("The following are the examples from BinPackage README but with Faroese usage.")

print("\n")

print(f'b.lookup("hava"): {b.lookup("hava")}')

print("\n")

print(f'Lemma of "hevur" using b.lookup() again: {b.lookup("hevur")}')
print(f'Lemma of "nøkur" using b.lookup() again: {b.lookup("nøkur")}')

print("\n")

print(f'All possible lemma for "í" using b.lookup_lemmas_and_cats(): {b.lookup_lemmas_and_cats("í")}')

print("\n")

print(f'Full entry given BÍN identifier 513763 using b.lookup_id(): {b.lookup_id(513763)}')

print("\n")

m = b.lookup_variants("maður", "kk", "ÞGF")
print(f'Convert "maður" to dative case singular using b.lookup_variants(): {m[0].bmynd}')

print("\n")

#n = b.lookup_variants("kettur", "kvk", "ÞF")

#noun = n[0].bmynd
#print(f"Eg sá nógvar {noun} í Reykjavík.")