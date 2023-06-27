import random

def main():
    print("Sayı Tahmin Oyunu")
    print("1 ile 100 arasında bir sayıyı tahmin edin.")

    target_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != target_number:
        guess = get_guess_from_user()
        attempts += 1
        if guess < target_number:
            print("Daha yüksek bir sayı deneyin.")
        elif guess > target_number:
            print("Daha düşük bir sayı deneyin.")
        else:
            print("Tebrikler! Doğru tahmin!")
            print("Tahmin sayısı:", attempts)

    play_again = input("Tekrar oynamak ister misiniz? (Evet için 'E', Hayır için 'H'): ")
    if play_again.upper() == 'E':
        main()
    else:
        print("Oyun bitti. İyi günler!")

def get_guess_from_user():
    while True:
        try:
            guess = int(input("Tahmininizi girin: "))
            if guess < 1 or guess > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
            else:
                return guess
        except ValueError:
            print("Geçerli bir sayı girin.")

if __name__ == '__main__':
    main()
