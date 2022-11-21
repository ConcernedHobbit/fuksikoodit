# Game logic
def main():
  print("Gurula Adventure")
  step = 0

  while True:
    print()
    # Print the prompt corresponding to the current step
    print(tree[step]["prompt"])

    print()
    # List the choices taken from the current step
    choices = tree[step]["choices"]
    for i in range(len(choices)):
      print(f"[{i}] {choices[i][0]}")

    print()
    # Ask for a decision until we get a valid input
    decision = int(input("Choice > "))
    while decision not in range(0, len(choices)):
      print("Invalid choice.")
      decision = int(input("Choice > "))
    
    # Set the next step based on the user's decision
    step = choices[decision][1]

    # Hard-coded end point
    if step == 3:
      # Print the prompt for leaving Gurula
      print(tree[step]["prompt"])
      # Exit the loop
      break
  
  print("Thanks for playing!")

# Decision tree
tree = [
  {
    # The prompt given to the user at this step
    "prompt": "You arrive at Gurula. There's two people sitting by the table. A third one lounges on the sofa. They look at you with raised eyebrows.",
    # The choices available to the user
    "choices": [
      # The text of the prompt and the step it takes the user to
      ["Buy a NOCCO from RV", 1],
      ["Talk to the <Person on the Sofa>", 2],
      ["Leave", 3]
    ]
  },
  {
    "prompt": "You go to buy a NOCCO from RV. As you scan the barcode, the computer informs you your balance is -12.60€. The machine beeps angrily.",
    "choices": [
      ["Ask the <Person on the Sofa> for a loan", 4],
      ["Make a deposit from your bank account", 5],
      ["Run away", 3]
    ]
  },
  {
    "prompt": "You go to talk to the <Person on the Sofa>. They ask you why you're here.",
    "choices": [
      ["'Who the hell are you?'", 6],
      ["Ignore the person and go buy a NOCCO from RV", 1],
      ["Run away", 3]
    ],
  },
  {
    "prompt": "You escape Gurula... but at what cost?",
  },
  {
    "prompt": "You ask the <Person on the Sofa> for some money. They ask you who you think you are.",
    "choices": [
      ["'Who the hell are you?'", 6],
      ["Run away", 3]
    ]
  },
  {
    "prompt": "You try to make a deposit. Your cash account is empty. KELA benefits will arrive tomorrow.",
    "choices": [
      ["Leave Gurula shamefully", 3]
    ]
  },
  {
    "prompt": "I'm <The Gurula-goer>. Some people call me Charles. Before you can respond, they disappear in front of your eyes",
    "choices": [
      ["Leave Gurula confused", 3]
    ]
  }
]

# Start the game when running the program
if __name__ == "__main__":
  main()