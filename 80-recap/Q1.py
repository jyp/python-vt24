# Assumption: parcel ids are always integers!
# Assumption: an exception will be raised if the user input for this parcel id is not an integer.

def deliverParcel(parcel):
    parcel_id = int(input("Please enter the parcel id (as an integer)"))
    if parcel_id not in parcels:
        print("Unknown parcel")
    else:
        customer_name = input("Customer name?")
        parcel_info = parcel[parcel_id]
        if customer_name == parcel_info[0]:
            print (parcel_info[1])
        else:
            print("This parcel is for a different recipient")

#############
# Test code
parcels = {4460: ("Byron Sully","Rack 1, blue package")
           ,1223: ("Dr. Quinn", "Rack 2, on the left, deliver today") }
deliverParcel(parcels)
