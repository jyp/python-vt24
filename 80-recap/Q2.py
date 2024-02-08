# Assumption: parcel ids are always integers!
# Assumption: an exception will be raised if the user input for this parcel id is not an integer.

def readParcels(filename):
    result = {}
    state = 0
    parcel_id = 0
    recipient = "No recipient"
    comment = "No comment"
    with open(filename) as file:
        for l in file:
            clean_line = l.strip()
            state = state + 1
            if state == 1:
                parcel_id = int(clean_line)
            elif state == 2:
                recipient = clean_line
            elif state == 3:
                comment = clean_line
            elif state == 4:
                result[parcel_id] = (recipient, comment)
                state = 0
            else:
                print("Wrong state!!!!")
    return result

#########
# Test code

print(readParcels("parcels.txt"))
