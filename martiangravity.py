def main():

    print("-------------------")
    print("| codedrome.com   |")
    print("| Martian Gravity |")
    print("-------------------\n")

    planet = "mars"
    my_earth_weight_kg = 75  # 165lbs / 11.8st

    weights = calculate_weights(planet, my_earth_weight_kg)

    print(f"A person weighing {my_earth_weight_kg}kg on Earth would weigh:\n")
    print(f"  {weights['pounds']:>3.2f}lbs")
    print(f"  {weights['stones']:>2.2f}st")
    print(f"  {weights['kilograms']:>3.2f}kg")

    print(f"\non {planet.capitalize()}.")


def calculate_weights(planet, my_earth_weight_kg):

    planet_details = get_planet_details()

    G = 6.67408 * 10**-11

    Fg = G * ((planet_details[planet]["mass_kg"] * my_earth_weight_kg)
              / (planet_details[planet]["mean_radius_metres"] ** 2))

    weights = newtons_to_weights(Fg)

    return weights


def get_planet_details():

    planet_details = {}

    planet_details["mercury"] = {"mass_kg": 3.3011 * 10**23,
                                 "mean_radius_metres": 2439.7 * 1000}
    planet_details["venus"] = {"mass_kg": 4.8675 * 10**24,
                               "mean_radius_metres": 6051.8 * 1000}
    planet_details["earth"] = {"mass_kg": 5.97237 * 10**24,
                               "mean_radius_metres": 6371 * 1000}
    planet_details["mars"] = {"mass_kg": 6.4171 * 10**23,
                              "mean_radius_metres": 3389.5 * 1000}
    planet_details["jupiter"] = {"mass_kg": 1.8982 * 10**27,
                                 "mean_radius_metres": 69911 * 1000}
    planet_details["saturn"] = {"mass_kg": 5.6834 * 10**26,
                                "mean_radius_metres": 58232 * 1000}
    planet_details["uranus"] = {"mass_kg": 8.681 * 10**25,
                                "mean_radius_metres": 25362 * 1000}
    planet_details["neptune"] = {"mass_kg": 1.02413 * 10**26,
                                 "mean_radius_metres": 24622 * 1000}

    return planet_details


def newtons_to_weights(N):

    weights = {}

    weights["newtons"] = N
    weights["pounds"] = N / 4.4482216
    weights["stones"] = weights["pounds"] / 14
    weights["kilograms"] = N / 9.80665

    return weights


main()
