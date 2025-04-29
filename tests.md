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

- [x] validate guess takes "monkey", index 0, and character 'm', and returns True
- [x] validate guess takes "monkey", index 0, and character 'k', and returns False
- [x] validate guess takes "monkey", index 5, and character 'y', and returns True

### Word shuffler

- [x] word shuffler takes a string "monkey" and returns it shuffled - use reverse as mock side effect
- [x] word shuffler takes a string "donkey" and returns it shuffled - use sort as mock side effect

### Random word selection

- [x] Random word selector takes a list with word "monkey" and returns it
- [x] Random word selector takes a list of 2 strings and returns a random one - return first one as mock side effect
- [ ] Random word selector takes a list of 3 strings and returns a random one - return second one as mock side effect
- [ ] Random word selector takes an empty list and raises an exception saying "Invalid input: no words to choose from
