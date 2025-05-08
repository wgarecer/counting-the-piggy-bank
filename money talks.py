fives = int(input("Enter how many fives you have: "))
tens = int(input("Enter how many tens you have: "))
fifties = int(input("Enter how many fifties you have: "))
hundreds = int(input("Enter how many hundreds you have: "))
two_hundreds = int(input("Enter how many two hundreds you have: "))
five_hundreds = int(input("Enter how many five hundreds you have: "))
thousands = int(input("Enter how many thousands you have: "))
five_thousands = int(input("Enter how many five thousands you have: "))

fives_total = fives * 5
tens_total = tens * 10
fifties_total = fifties * 50
hundreds_total = hundreds * 100
two_hundreds_total = two_hundreds * 200
five_hundreds_total = five_hundreds * 500
thousands_total = thousands * 1000
five_thousands_total = five_thousands * 5000

total_money = (
    fives_total + tens_total + fifties_total + hundreds_total +
    two_hundreds_total + five_hundreds_total +
    thousands_total + five_thousands_total
)

print("\nHere is what you have:")
print(f"5s: {fives} → {fives_total} rubles")
print(f"10s: {tens} → {tens_total} rubles")
print(f"50s: {fifties} → {fifties_total} rubles")
print(f"100s: {hundreds} → {hundreds_total} rubles")
print(f"200s: {two_hundreds} → {two_hundreds_total} rubles")
print(f"500s: {five_hundreds} → {five_hundreds_total} rubles")
print(f"1000s: {thousands} → {thousands_total} rubles")
print(f"5000s: {five_thousands} → {five_thousands_total} rubles")

print(f"\nTotal money you have: {total_money} rubles")
