service_1 = 0.20
service_2 = 0.15
service_3 = 0.10


def tip_calc(big_cas,  big_ser):
    if big_ser == "great":
        print("Based on your bill amount and service quality, we recommend you leave a 20% tip in the amount of:","$",round(float(big_cas) * service_1, 2))
    elif big_ser == "fair":
        print("Based on your bill amount and service quality, we recommend you leave a 15% tip in the amount of:","$",round(float(big_cas) * service_2, 2))
    elif big_ser == "poor":
        print("Based on your bill amount and service quality, we recommend you leave a 10% tip in the amount of:","$",round(float(big_cas) * service_3, 2))
    else:
        print("Due to the lack of details provided we are unable to recommend a tip.")


big_cas = input("What was your bill amount?")
big_ser = input("Rate your service quality by entering great, fair, or poor.")
if big_ser == "great":
    tip_calc(big_cas, big_ser)
elif big_ser == "fair":
    tip_calc(big_cas, big_ser)
elif big_ser == "poor":
    tip_calc(big_cas, big_ser)
else:
    tip_calc(0,"none" )