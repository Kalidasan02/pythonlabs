import random
apple_juice = 15.5;
orange_juice = 20;
grape_juice = 10.25;
total_volume = apple_juice+orange_juice+grape_juice;
print("Total volume of juice sold:", total_volume, "liters")
total_volume_int = int(total_volume)
print("Total volume (integer):", total_volume_int, "liters")
total_volume_str = str(total_volume)
print("The total volume of juice sold today is " + total_volume_str + " liters.")
bonus_litres = random.randrange(5,10)
final_total = total_volume + bonus_litres
print("Final total after adding bonus liters:", final_total, "liters")