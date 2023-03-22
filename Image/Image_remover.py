import os

# Listing all the items in the main folder
files = os.listdir('Webcam/')

# Creating a list for modified time
timelist = []


def abspath(i):
    abs_path = 'Webcam/' + i
    return abs_path


# Looping through each file in the folder
for i in files:
    # Absolute path as os module checks in the wrong dir
    path = abspath(i)

    # Append the timelist with the modification time of each file
    timelist.append(os.path.getmtime(path))

# Get the max value from timelist as it belongs to the latest file
latest_image = max(timelist)

# Looping through files again to delete the unrequired ones
for i in files:

    path = abspath(i)

    # Comparision of modification time
    if os.path.getmtime(path) == latest_image:
        print('Latest Image is ' + i)
        continue
    else:
        os.remove(path)
