# Assumption: parcel ids are always integers!
# Assumption: an exception will be raised if the user input for this parcel id is not an integer.
# Assumption: We do not check if every 4th line is empty

def deliverParcel(parcel):
    parcel_id = int(input("Please enter the parcel id (as an integer)"))
    if parcel_id not in parcel:
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
# parcels = {4460: ("Byron Sully","Rack 1, blue package")
#            ,1223: ("Dr. Quinn", "Rack 2, on the left, deliver today") }
other_parcels = {445460: ("Byron Sully","Rack 1, blue package")
                 ,1223: ("Dr. Quinn", "Rack 2, on the left, deliver today") }
deliverParcel(other_parcels)
