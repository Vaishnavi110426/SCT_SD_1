class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9/5 + 32


def main():
    print("\n🌡️  Welcome to the Temperature Converter 🌡️")
    print("-" * 45)
    print("1️⃣  Convert Celsius → Fahrenheit & Kelvin")
    print("2️⃣  Convert Fahrenheit → Celsius & Kelvin")
    print("3️⃣  Convert Kelvin → Celsius & Fahrenheit")
    print("0️⃣  Exit")
    print("-" * 45)

    while True:
        try:
            choice = int(input("\nEnter your choice (0/1/2/3): "))

            if choice == 1:
                c = float(input("Enter temperature in Celsius: "))
                print(f"{c}°C = {TemperatureConverter.celsius_to_fahrenheit(c):.2f}°F")
                print(f"{c}°C = {TemperatureConverter.celsius_to_kelvin(c):.2f}K")

            elif choice == 2:
                f = float(input("Enter temperature in Fahrenheit: "))
                print(f"{f}°F = {TemperatureConverter.fahrenheit_to_celsius(f):.2f}°C")
                print(f"{f}°F = {TemperatureConverter.fahrenheit_to_kelvin(f):.2f}K")

            elif choice == 3:
                k = float(input("Enter temperature in Kelvin: "))
                print(f"{k}K = {TemperatureConverter.kelvin_to_celsius(k):.2f}°C")
                print(f"{k}K = {TemperatureConverter.kelvin_to_fahrenheit(k):.2f}°F")

            elif choice == 0:
                print("✅ Exiting Temperature Converter. Stay cool ❄️🔥")
                break

            else:
                print("⚠️ Invalid choice! Please enter 0, 1, 2, or 3.")

        except ValueError:
            print("⚠️ Please enter a valid number!")


if __name__ == "__main__":
    main()
