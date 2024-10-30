'''
- Kyozho (Chase)
- Date: 29/10/24
- Context: 
-   You meet a group of aliens, and their language is just like English except that they say every word backwards.
- How will you learn to communicate with them?
- *Question by Sololearn*
'''

def Aliens():
    alien_input = input("Word: ")
    output = alien_input[::-1]

    print(f"Translation: {output}")
    print("\nKyozho (Chase)")
    input("Press 'Enter' to exit program")

Aliens()