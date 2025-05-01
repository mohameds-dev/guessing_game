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

- [ ] validate guess takes 'm' and 'm' and returns True
- [ ] validate guess takes 'M' and 'm' and returns True
- [ ] validate guess takes 'x' and 'y', and returns False

### Word shuffler

- [x] word shuffler takes a string "monkey" and returns it shuffled
- [x] word shuffler takes a string "donkey" and returns it shuffled

### Random word selection

- [x] Random word selector takes a list with word "monkey" and returns it
- [x] Random word selector takes a list of 2 strings and returns a random one
- [x] Random word selector takes an empty list and raises an exception saying "Invalid input: no words to select from."

### Guess evaluator

- [x] Guess evaluator takes the word "monkey" and the guessed word "monkey" and returns score of 10
- [x] Guess evaluator takes the word "monkey" and the guessed word "monk" and returns score of 7
- [x] Guess evaluator takes the word "monkey" and the guessed word "kom" and returns score of 0
- [x] Guess evaluator takes the word "monkey" and the guessed word "mono" and returns score of 5

### Reading input

- [x] Read input reads lines from words.txt file and returns a list of words
- [x] Read input reads empty file and returns empty list
