def check_vowels(string):
   # vowels
   vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
   # iterating over the string
   for char in string:
      if char not in vowels:
        print(f"{string}: Not accepted")
      break
   else:
      print(f"{string}: Accepted")
if __name__ == '__main__':
   # initializing strings
   string_1 = "tutorialspoint"
   string_2 = "AEiouaieeu"
   # checking the strings
   check_vowels(string_1)
   check_vowels(string_2)