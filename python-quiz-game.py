
import random

easy = [
{
"question":"Python me list ka syntax kya hai?",
"options":["A. {}","B. ()","C. []","D. <>"],
"answer":"C"
},

{
"question":"Python me dictionary kis bracket me banti hai?",
"options":["A. []","B. {}","C. ()","D. <>"],
"answer":"B"
},

{
"question":"List me element add karne ke liye kaunsa method use hota hai?",
"options":["A. add()","B. insert()","C. append()","D. push()"],
"answer":"C"
},

{
"question":"Python me loop ke liye kaunsa keyword use hota hai?",
"options":["A. repeat","B. loop","C. for","D. iterate"],
"answer":"C"
},

{
"question":"Function define karne ke liye kaunsa keyword use hota hai?",
"options":["A. function","B. define","C. fun","D. def"],
"answer":"D"
},

{
"question":"Python me comment likhne ke liye kya use karte hain?",
"options":["A. //","B. <!-- -->","C. #","D. **"],
"answer":"C"
},

{
"question":"len() function kya return karta hai?",
"options":["A. Sum","B. Length","C. Maximum","D. Minimum"],
"answer":"B"
},

{
"question":"Python kis type ki language hai?",
"options":["A. Low Level","B. High Level","C. Assembly","D. Machine"],
"answer":"B"
},

{
"question":"String ko uppercase me badalne ke liye kaunsa method hai?",
"options":["A. upper()","B. uppercase()","C. caps()","D. big()"],
"answer":"A"
},

{
"question":"Input lene ke liye kaunsa function use hota hai?",
"options":["A. get()","B. input()","C. read()","D. scan()"],
"answer":"B"
},

{
"question":"Output dikhane ke liye kaunsa function use hota hai?",
"options":["A. show()","B. print()","C. output()","D. display()"],
"answer":"B"
},

{
"question":"Python file extension kya hoti hai?",
"options":["A. .java","B. .cpp","C. .py","D. .txt"],
"answer":"C"
},

{
"question":"List ordered hoti hai?",
"options":["A. Yes","B. No","C. Sometimes","D. Never"],
"answer":"A"
},

{
"question":"Tuple kis bracket me banta hai?",
"options":["A. []","B. {}","C. ()","D. <>"],
"answer":"C"
},

{
"question":"Boolean me kitni values hoti hain?",
"options":["A. 1","B. 2","C. 3","D. 4"],
"answer":"B"
},

{
"question":"True aur False kis data type ke hain?",
"options":["A. int","B. str","C. bool","D. float"],
"answer":"C"
},

{
"question":"Python case sensitive language hai?",
"options":["A. Yes","B. No","C. Sometimes","D. Unknown"],
"answer":"A"
},

{
"question":"List ka first index kya hota hai?",
"options":["A. 1","B. 0","C. -1","D. 10"],
"answer":"B"
},

{
"question":"Dictionary me unique kya hoti hain?",
"options":["A. Values","B. Keys","C. Index","D. Lists"],
"answer":"B"
},

{
"question":"Random number ke liye kaunsa module use hota hai?",
"options":["A. math","B. random","C. os","D. time"],
"answer":"B"
},

{
"question":"Python me square root ke liye kaunsa module use hota hai?",
"options":["A. math","B. random","C. sys","D. os"],
"answer":"A"
},

{
"question":"List ki length nikalne ke liye kya use hota hai?",
"options":["A. count()","B. len()","C. size()","D. length()"],
"answer":"B"
},

{
"question":"Python interpreter line by line code execute karta hai?",
"options":["A. Yes","B. No","C. Sometimes","D. Unknown"],
"answer":"A"
},

{
"question":"Range banane ke liye kya use hota hai?",
"options":["A. loop()","B. range()","C. series()","D. list()"],
"answer":"B"
},

{
"question":"List se last element remove karne ke liye kya use hota hai?",
"options":["A. delete()","B. remove()","C. pop()","D. cut()"],
"answer":"C"
}
]
medium = [

{
"question":"Which data type is immutable in Python?",
"options":["A. List","B. Dictionary","C. Set","D. Tuple"],
"answer":"D"
},

{
"question":"Which keyword is used to handle exceptions?",
"options":["A. catch","B. try","C. except","D. Both B and C"],
"answer":"D"
},

{
"question":"Which function returns the length of an object?",
"options":["A. size()","B. length()","C. len()","D. count()"],
"answer":"C"
},

{
"question":"Which method adds an element at the end of a list?",
"options":["A. add()","B. insert()","C. append()","D. push()"],
"answer":"C"
},

{
"question":"Which keyword is used to create a class?",
"options":["A. object","B. class","C. define","D. struct"],
"answer":"B"
},

{
"question":"Which operator is used for exponentiation?",
"options":["A. ^","B. **","C. //","D. %"],
"answer":"B"
},

{
"question":"Which module is used to generate random numbers?",
"options":["A. math","B. random","C. os","D. numpy"],
"answer":"B"
},

{
"question":"What is the output type of input()?",
"options":["A. int","B. float","C. str","D. bool"],
"answer":"C"
},

{
"question":"Which data structure does not allow duplicate values?",
"options":["A. List","B. Tuple","C. Set","D. Dictionary"],
"answer":"C"
},

{
"question":"What does sorted() return?",
"options":["A. A new sorted list","B. Modifies original list","C. A tuple","D. None"],
"answer":"A"
},

{
"question":"Which loop is used when iterations are known?",
"options":["A. for","B. while","C. do while","D. repeat"],
"answer":"A"
},

{
"question":"Which keyword exits a loop immediately?",
"options":["A. stop","B. break","C. continue","D. return"],
"answer":"B"
},

{
"question":"Which keyword skips the current iteration?",
"options":["A. pass","B. break","C. continue","D. return"],
"answer":"C"
},

{
"question":"Which function converts a string to integer?",
"options":["A. str()","B. float()","C. int()","D. bool()"],
"answer":"C"
},

{
"question":"Which keyword creates an anonymous function?",
"options":["A. lambda","B. func","C. def","D. anon"],
"answer":"A"
},

{
"question":"What does range(5) produce?",
"options":["A. 0 to 4","B. 1 to 5","C. 0 to 5","D. 1 to 4"],
"answer":"A"
},

{
"question":"Which function opens a file?",
"options":["A. file()","B. open()","C. read()","D. create()"],
"answer":"B"
},

{
"question":"Which method converts a string to lowercase?",
"options":["A. lower()","B. down()","C. small()","D. casefold()"],
"answer":"A"
},

{
"question":"Which operator checks equality?",
"options":["A. =","B. ==","C. ===","D. !="],
"answer":"B"
},

{
"question":"Which data type stores key-value pairs?",
"options":["A. List","B. Set","C. Dictionary","D. Tuple"],
"answer":"C"
},

{
"question":"Which keyword imports a module?",
"options":["A. include","B. import","C. using","D. package"],
"answer":"B"
},

{
"question":"Which function returns the largest value?",
"options":["A. high()","B. max()","C. largest()","D. top()"],
"answer":"B"
},

{
"question":"Which function returns the smallest value?",
"options":["A. min()","B. low()","C. small()","D. least()"],
"answer":"A"
},

{
"question":"Which operator performs floor division?",
"options":["A. /","B. %","C. //","D. **"],
"answer":"C"
},

{
"question":"Which function returns the type of an object?",
"options":["A. object()","B. type()","C. class()","D. typeof()"],
"answer":"B"
}

]
hard = [

{
"question":"What is the average time complexity of dictionary lookup?",
"options":["A. O(n)","B. O(log n)","C. O(1)","D. O(n²)"],
"answer":"C"
},

{
"question":"Which keyword creates a generator?",
"options":["A. return","B. yield","C. async","D. pass"],
"answer":"B"
},

{
"question":"Which module provides deepcopy()?",
"options":["A. random","B. copy","C. os","D. collections"],
"answer":"B"
},

{
"question":"When is _init_() executed?",
"options":["A. Object creation","B. Object deletion","C. Function call","D. Program end"],
"answer":"A"
},

{
"question":"What does zip() do?",
"options":["A. Compresses files","B. Combines iterables","C. Sorts data","D. Removes duplicates"],
"answer":"B"
},

{
"question":"Which keyword is used in asynchronous functions?",
"options":["A. await","B. async","C. Both A and B","D. yield"],
"answer":"C"
},

{
"question":"Which decorator creates a static method?",
"options":["A. @classmethod","B. @staticmethod","C. @property","D. @decorator"],
"answer":"B"
},

{
"question":"Which statement about tuples is true?",
"options":["A. Mutable","B. Immutable","C. Unordered","D. Unique"],
"answer":"B"
},

{
"question":"What does enumerate() return?",
"options":["A. Index-value pairs","B. Keys","C. Values","D. Integers"],
"answer":"A"
},

{
"question":"What is Python's garbage collector for?",
"options":["A. Memory management","B. File handling","C. Networking","D. Sorting"],
"answer":"A"
},

{
"question":"Which function executes Python code from a string?",
"options":["A. run()","B. exec()","C. compile()","D. start()"],
"answer":"B"
},

{
"question":"Which function evaluates an expression string?",
"options":["A. eval()","B. exec()","C. parse()","D. compile()"],
"answer":"A"
},

{
"question":"What is the output of bool([])?",
"options":["A. True","B. False","C. Error","D. None"],
"answer":"B"
},

{
"question":"What is the output of bool({})?",
"options":["A. True","B. False","C. Error","D. None"],
"answer":"B"
},

{
"question":"Which module works with regular expressions?",
"options":["A. regex","B. re","C. string","D. pattern"],
"answer":"B"
},

{
"question":"What is the default return value of a function without return?",
"options":["A. 0","B. False","C. None","D. Empty string"],
"answer":"C"
},

{
"question":"Which operator checks object identity?",
"options":["A. ==","B. is","C. in","D. !="],
"answer":"B"
},

{
"question":"Which keyword is used to inherit a class?",
"options":["A. inherit","B. extends","C. Parent class in brackets","D. super"],
"answer":"C"
},

{
"question":"Which built-in function removes duplicates easily?",
"options":["A. set()","B. unique()","C. remove()","D. filter()"],
"answer":"A"
},

{
"question":"Which module is used for JSON?",
"options":["A. js","B. json","C. jsonify","D. parser"],
"answer":"B"
},

{
"question":"What is the output of 10 % 3?",
"options":["A. 0","B. 1","C. 2","D. 3"],
"answer":"B"
},

{
"question":"Which data structure uses hashing internally?",
"options":["A. List","B. Tuple","C. Dictionary","D. String"],
"answer":"C"
},

{
"question":"Which method removes and returns the last list element?",
"options":["A. delete()","B. remove()","C. pop()","D. discard()"],
"answer":"C"
},

{
"question":"Which module provides mathematical functions?",
"options":["A. calc","B. math","C. statistics","D. numbers"],
"answer":"B"
},

{
"question":"What is the output of type(None)?",
"options":["A. None","B. NoneType","C. null","D. object"],
"answer":"B"
}

]


def playquiz(name):

    level = input("Enter level (easy/medium/hard): ").lower()

    if level == "easy":
        questions = easy

    elif level == "medium":
        questions = medium

    elif level == "hard":
        questions = hard

    else:
        print(" Invalid level!")
        return

    random.shuffle(questions)

    score = 0

    print("\n===== QUIZ GAME =====")

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:

            print("Correct")

            score += 1

        else:

            print(" Wrong Answer")

            print("Correct answer:", q["answer"])

    print("\n===== RESULT =====")

    print("Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100

    print(f"Percentage: {percentage:.2f}%")
    
    # History save
    with open("Deepanshu.txt", "a") as file:
        file.write(f"{name} - {score}/{len(questions)}\n")
    # High score
    try:
        with open("highscore.txt","r") as file:
            high_score=int(file.read())

    except:
        high_score=0

    if score>high_score:
        with open("highscore.txt","w") as file:
            file.write(str(score))

        print("New high score")
    
    else:
        print("high_score",high_score)


name = input("Enter your name: ")

while True:

    playquiz(name)

    choice = input("\nPlay again? (Y/N): ").upper()

    if choice == "N":

        print(f"Thanks for playing, {name}!")

        break

