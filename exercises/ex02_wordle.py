"""My own wordle game! Wahoo!"""

__author__: str = "730469212"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False
    while (
        turn <= 6 and not won
    ):  # starts a loop to create a new turn in the game as long as the word has not been solved and 6 tries have not be expended
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # calls the secret word inside of the call for input guess, setting the number of characters allowed per guess
        print(
            emojified(guess, secret)
        )  # calls emojified to analyze and present approiate colors based of guess and secret word
        if guess == secret:
            won = True  # stops the while loop because the game has been won and the word solved!
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    else:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(search: str, single_character: str) -> bool:
    """Looks for character in word guess"""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    index: int = 0  # sets index to 0
    while index < len(
        search
    ):  # ensures that the index values searched does not exceed the length of the word
        if (
            search[index] == single_character
        ):  # checks to see if the character at the index value in the guess is the same as the index value in the secret word
            return True
        index += 1  # increases index value by one to search the rest of the word
    return False


WHITE_BOX: str = (
    "\U00002B1C"  # assigns string variables for emojified function to reference
)
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(search: str, secret: str) -> str:
    """return an emoji to color code the results of a word guess"""
    assert len(search) == len(secret), "Guess must be same length as secret"
    index: int = 0
    result = ""  # sets an empty string to add the emojis assigned to each index"
    while index < len(
        search
    ):  # creates a loop to assess all the indices in a given word, since index values start at 0 the index associated with the last character will inhereently be lower than the length of the word, thus the need to have the index be lower than the length of the word.
        if search[index] == secret[index]:
            result += GREEN_BOX  # adds a green emoji to the string, if the characters match at this index
        elif contains_char(secret, search[index]):
            result += YELLOW_BOX  # adds a yellow emoji to the string, if the character is in the secret word but not at this given index
        else:
            result += WHITE_BOX  # adds a white emoji to the string if the character is not present in the secret word
        index += 1  # increases index value to search the whole word
    return result


def input_guess(n: int) -> str:
    """sets expected length for guess based on length of secret word."""
    guess: str = input(
        f"Enter a {n} character word: "
    )  # creates a guess parameter and prompts user to enter a word of a certain length
    while len(guess) != n:
        guess = input(
            f"That wasn't {n} chars! Try again: "
        )  # if guess is not the designated length, reminds user of correct length and prompts them to enter a new word
    return guess


if __name__ == "__main__":
    main(secret="tevye")  # sets the secret word to my cats name!
