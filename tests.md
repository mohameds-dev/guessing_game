## Tests checklist 

### Consonants vs vowel scores

- [x] calculate score takes 'x' and returns 2
- [x] calculate score takes 'y' and returns 2
- [x] calculate score takes 'z' and returns 2
- [x] calculate score takes 'a' and returns 1
- [x] calculate score takes 'e' and returns 1
- [x] calculate score takes 'i' and returns 1
- [x] calculate score takes 'o' and returns 1
- [x] calculate score takes 'u' and returns 1

### Character guess validator

- [x] validate guess takes 'm' and 'm' and returns True
- [x] validate guess takes 'M' and 'm' and returns True
- [x] validate guess takes 'x' and 'y', and returns False

### Word shuffler

- [x] word shuffler takes a string "monkey" and returns it shuffled
- [x] word shuffler takes a string "donkey" and returns it shuffled

### Random word selection

- [x] random index generator takes 10 and is a random index between 0 and 9 inclusive
- [x] next index takes 1 and 10 and returns 5
- [x] next index takes 4 and 10 and returns 5
- [x] next index takes 9 and 10 and returns 0

### Guess evaluator

- [x] Guess evaluator takes the word "monkey" and the guessed word "monkey" and returns score of 10
- [x] Guess evaluator takes the word "monkey" and the guessed word "monk" and returns score of 7
- [x] Guess evaluator takes the word "monkey" and the guessed word "kom" and returns score of 0
- [x] Guess evaluator takes the word "monkey" and the guessed word "mono" and returns score of 5

### Reading input

- [x] Read input reads lines from words.txt file and returns a list of words
- [x] Read input reads empty file and returns empty list
