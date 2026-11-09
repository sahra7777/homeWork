score=float(input("your score:"))
score2=float(input("your score:"))
avg= (score+score2)/2
if avg >=17:
    print("Level A")
elif avg >=14:
    print("Level B")
elif avg >=10:
    print("Level C")
else:
    print(f"""you are with {avg} cant accept it🙂☠""")
