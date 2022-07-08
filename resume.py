def say_hi(name):
    print("\nHi " + name + ", I'm Phil Campbell\n")


contact = {
    "name": "Pxxx Cxxxxxx",
    "address": "Hxxxxxxxxx, XXX",
    "email": "cxxxxxxxxxxxxxx@protonmail.com",
    "mobile": "04xxxxxxxx",
}

responses = {
    1: "Creative, Customer Focused, Solution Orientated and Passionate about Learning.",
    2: "Fun, Family and Work/Life Balance.",
    3: "Banking, Solar Power, Businesses, Hospitality and Government.",
    4: "Python Coding Language & Blockchain Technology now and NET+, SEC+ and CEH in the near future.",
    5: "Blockchain, Help Desk, Ethical Hacking, NFT's, Software Development and Crypto Trading.",
    0: f"Thank you for considering me! {contact.get('name')} - {contact.get('email')} - {contact.get('mobile')}",
}

say_hi(input("What's your name? "))

print(
    """Please select a number to know more... 
1. Who am I?
2. What's important to me?
3. What experience do I have?
4. What am I learning?
5. What else am I interested in?
0. That's all I need to know Phil."""
)

while True:
    know = int(input("Number... "))

    if not know in responses:
        print("select correct number")
        continue

    if know == 0:
        print(responses.get(know))
        break
    else:
        print(responses.get(know))
