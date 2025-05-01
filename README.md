# guessing_game

Simple guessing game using python. Practice for my Software Design class with Dr. Venkat Subramaniam. This is a past exam problem in his class.

### Problem statement:

Write a program, using test first development, for the problem described below. Your work will be evaluated based on code quality, design quality, test quality, test coverage, and of course, the program working to solve the given problem.

---

Create a guessing game for a single user to play. The game will read a file which has a list of words. For example, the file may contain:

monkey
fruit
banana
apple
cosmopolitan

The program will pick a random word from the file, scramble it (for example, monkey may be scrambled to oekmny, emknoy, etc.), and present to the user the scrambled word.

Then it will ask the user to guess. The user gets partial points for their guess. They get one point for each vowel and two points for each consonant. For example, if the user enters monk (when the selected word is monkey), then they get 7 points. If a letter they enter is not in the word, they don't get any points for that letter. For example, if they enter mop, they get 3 points and not 5. If the spelling of the word is wrong, they get zero points. For example, if they enter kom, even though each letter there is in the selected word, they get 0 points.

The program will present the user with a scrambled word, cycle through asking the user for a guess, print their score, and repeat. It will stop when the user has made the perfect guess, that is, entered the original word (monkey, for example).
