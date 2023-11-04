number_of_guesses=5

secret_word='h e l l o'
show_word='_ _ _ _ _'
found=False
bufferString=""

print("Guess the word. You have 5 tries.")
print(show_word)

while (found==False and number_of_guesses>0):
    bufferString=""
    print(str(number_of_guesses) + " lives left")
    user_guess = (str(input(""))).lower()

    if len(user_guess)>1:
        print("Guess was more than one symbol")
    elif len(user_guess)==1:
        for i in range(0,len(secret_word)):
            
            if secret_word[i]==user_guess:
                bufferString=bufferString + secret_word[i]
            else:
                bufferString=bufferString + show_word[i]
        show_word=bufferString

        print(show_word)
        if show_word==secret_word:
            print("You found the word! Congratulations!")
            found=True
    number_of_guesses=number_of_guesses-1

    if number_of_guesses==0:
        print("No more lives")
        print("Secret word was")
        print(secret_word)


