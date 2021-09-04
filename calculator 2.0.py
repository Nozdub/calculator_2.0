number_one = input("Type a number")
number_two = input("type a second number")

answer_1 = float(number_one) + float(number_two)
answer_2 = float(number_one) - float(number_two)
answer_3 = float(number_one) * float(number_two)
answer_4 = float(number_one) / float(number_two)
answer_5 = float(number_one) % float(number_two)
answer_6 = float(number_one) ** float(number_two)
answer_7 = float(number_one) // float(number_two)


print(f"Here are the answers:", ("Addition="),answer_1,
                                ("Subtraction="),answer_2,
                                ("Multiplication="),answer_3,
                                ("Division="),answer_4,
                                ("Modulus="), answer_5,
                                ("Exponentiation="), answer_6,
                                ("Floor division="),answer_7,)

# Calculator 2.0 laget etter forslag fra studassistent. Finner ikke en ryddig måte å få printet hvilke mattematisk
# løsning som blir brukt i stringformat.

