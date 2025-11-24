import pyjokes
import pyquotegen
def random_joke():
    lng=input("""
choose language
 en	English
 de	German
 es	Spanish
 it	Italian
 gl	Galician
 eu 	Basque
Enter language code : """)
            
    cat=input("""
choose category
 neutral --> Neutral geeky jokes
 chuck --> Chuck-style jokes
 all --> All types of joke
Enter category code : """)
    my_joke=pyjokes.get_joke(language=lng, category=cat)
    print(my_joke)

    
def random_quote():
    cat=input("""
choose category
*motivational
*inspirational
*attitude
*success
*technology
*coding
*friendship
*funny
*nature
Write your choice : """)
    my_quote=pyquotegen.get_quote(category=cat)
    print(my_quote)
    
def main():
    print("""
__________________________________________
          
     RANDOM QUOTE AND JOKE GENERATOR
        
__________________________________________
""")
    while True:
        print('''

''')
        choice=int(input("""
Choose your option
1. Joke
2. Quote
3. quit
Enter your choice : """))
        if choice==1:
            
            random_joke()  

        elif choice==2:

            random_quote()
        
        elif choice==3:
            print("Thanks for using random quote and joke generator")
            break
        else:
            print("Please enter a valid choice...")
main()