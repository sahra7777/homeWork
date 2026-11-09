# score=float(input("your score:"))
# score2=float(input("your score:"))
# avg= (score+score2)/2
# if avg >=17:
#     print("Level A")
# elif avg >=14:
#     print("Level B")
# elif avg >=10:
#     print("Level C")
# else:
#     print(f"""you are with {avg} cant accept it🙂☠""")

kharid=int(input("mablagh kharid:"))
ozv=input("ozviat froshgah? (y/n)") == "y"
kalabarg=input("pardakht ba kala barg? (y/n)") == "y"
if kharid >=1000000 or (ozv and kalabarg ):
    mablagh_kil=kharid/2
    print(f"""  mablagh pardakhty: {mablagh_kil} """)
else:
    print(kharid)
