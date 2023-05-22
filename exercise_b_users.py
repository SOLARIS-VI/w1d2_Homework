users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# Code Along Solution - 17/05/23

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers
eriks_numbers = users["Erik"]["lottery_numbers"]
eriks_numbers.sort()
eriks_numbers[0]

# 6. Return an list of Avril's lottery numbers that are even
avrils_numbers = users["Avril"]["lottery_numbers"]
even_numbers = []
for number in avrils_numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"
new_pet = {"name": "fluffy", "species": "dog"}
users["Erik"]["pets"].append(new_pet)
print(users["Erik"])

# 10. Add another person to the users dictionary

# My Solution

# # 1. Get Jonathan's Twitter handle
# jonathan_twitter = users["Jonathan"]["twitter"]
# print(jonathan_twitter)  # Output: "jonnyt"

# # 2. Get Erik's hometown
# erik_hometown = users["Erik"]["home_town"]
# print(erik_hometown)  # Output: "Linlithgow"

# # 3. Get the list of Erik's lottery numbers
# erik_lottery_numbers = users["Erik"]["lottery_numbers"]
# print(erik_lottery_numbers)  # Output: [18, 34, 8, 11, 24]

# # 4. Get the species of Avril's pet Monty
# avril_pet_species = users["Avril"]["pets"][0]["species"]
# print(avril_pet_species)  # Output: "snake"

# # 5. Get the smallest of Erik's lottery numbers
# smallest_lottery_number = min(users["Erik"]["lottery_numbers"])
# print(smallest_lottery_number)  # Output: 8

# # 6. Return a list of Avril's lottery numbers that are even
# avril_even_lottery_numbers = [num for num in users["Avril"]["lottery_numbers"] if num % 2 == 0]
# print(avril_even_lottery_numbers)  # Output: [12, 14, 38]

# # 7. Erik is one lottery number short! Add the number 7 to be included in his lottery numbers
# users["Erik"]["lottery_numbers"].append(7)
# print(users["Erik"]["lottery_numbers"])  # Output: [18, 34, 8, 11, 24, 7]

# # 8. Change Erik's hometown to Edinburgh
# users["Erik"]["home_town"] = "Edinburgh"
# print(users["Erik"]["home_town"])  # Output: "Edinburgh"

# # 9. Add a pet dog to Erik called "fluffy"
# new_pet = {"name": "fluffy", "species": "dog"}
# users["Erik"]["pets"].append(new_pet)
# print(users["Erik"]["pets"]) 

