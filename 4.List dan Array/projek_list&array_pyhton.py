import time

ingredient_list = ["telur", "tepung", "coklat", "minyak", "gula", "garam"]
score = 0

print("halo, tebak 3 bahan yang bakal digunakan yak, siapp!!")
time.sleep(3)

ingredient_1 = input("tebak bahan ke 1? ")
if ingredient_1 in ingredient_list:
    print("kamu berhasil menjawab " + ingredient_1)
    score += 1
else:
    print("maaf, jawaban kamu masih salah")

ingredient_2 = input("tebak bahan ke 2? ")
if ingredient_2 in ingredient_list:
    print("kamu berhasil menjawab " + ingredient_2)
    score += 1
else:
    print("maaf, jawaban kamu masih salah")

ingredient_3 = input("tebak bahan ke 3? ")
if ingredient_3 in ingredient_list:
    print("kamu berhasil menjawab " + ingredient_3)
    score += 1
else:
    print("maaf, jawaban kamu masih salah")

print("Game over, you have " + str(score) + " points")
print("The ingredient list was:")
print(ingredient_list)