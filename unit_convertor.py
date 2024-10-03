def length_converter(value, unit):
    if unit == 'cm_to_inch':
        return value / 2.54
    elif unit == 'inch_to_cm':
        return value * 2.54
    elif unit == 'km_to_mile':
        return value / 1.609
    elif unit == 'mile_to_km':
        return value * 1.609


def unit_converter():
    print("1. cm to inches\n2. inches to cm\n3. km to miles\n4. miles to km")
    choice = input("Choose a conversion: ")

    if choice in ['1', '2', '3', '4']:
        value = float(input("Enter value to convert: "))
        if choice == '1':
            print(f"{value} cm = {length_converter(value, 'cm_to_inch')} inches")
        elif choice == '2':
            print(f"{value} inches = {length_converter(value, 'inch_to_cm')} cm")
        elif choice == '3':
            print(f"{value} km = {length_converter(value, 'km_to_mile')} miles")
        elif choice == '4':
            print(f"{value} miles = {length_converter(value, 'mile_to_km')} km")
    else:
        print("Invalid choice.")


unit_converter()
