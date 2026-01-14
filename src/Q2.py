import os
import csv
import math

# folder where all the temperature csv files are stored
temperature_folder = "temperatures"

# lists for storing temperatures for every seasons
summer = []
autumn = []
winter = []
spring = []

# dictionary for storing temperatures of each station
station_temps = {}

# months according to the Australian seasons
summer_months = ["December", "January", "February"]
autumn_months = ["March", "April", "May"]
winter_months = ["June", "July", "August"]
spring_months = ["September", "October", "November"]

# main loop for reading all csv files and processing the data in it
for file_name in os.listdir(temperature_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(temperature_folder, file_name)

        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                station = row["STATION_NAME"]

                # creating a list for the stations(conditional)
                if station not in station_temps:
                    station_temps[station] = []

                # loop for going through each months column
                for month in (summer_months + autumn_months +
                              winter_months + spring_months):

                    value = row[month]

                    # skipping the missing values or NaN values and empty values
                    if value == "" or value.lower() == "nan":
                        continue

                    temp = float(value)

                    # stores temperatures of that station
                    station_temps[station].append(temp)

                    # conditions for adding temperature to the season lists
                    if month in summer_months: # summer season 
                        summer.append(temp)
                    elif month in autumn_months: # autumn season
                        autumn.append(temp)
                    elif month in winter_months: # winter season
                        winter.append(temp)
                    else:                       # spring season
                        spring.append(temp)

# calculating and creating average temperature file
avg_file = open("average_temp.txt", "w")

avg_file.write("Summer: " + format(sum(summer) / len(summer), ".1f") + " C\n")
avg_file.write("Autumn: " + format(sum(autumn) / len(autumn), ".1f") + " C\n")
avg_file.write("Winter: " + format(sum(winter) / len(winter), ".1f") + " C\n")
avg_file.write("Spring: " + format(sum(spring) / len(spring), ".1f") + " C\n")

avg_file.close()


# calculating and creating largest temperature range file
largest_range = 0

for station in station_temps:
    temps = station_temps[station]
    temp_range = max(temps) - min(temps)

    if temp_range > largest_range:
        largest_range = temp_range

range_file = open("largest_temp_range_station.txt", "w")

for station in station_temps:
    temps = station_temps[station]
    temp_range = max(temps) - min(temps)

    # condition for checking the station temperature range
    if temp_range == largest_range:
        range_file.write(
            "Station " + station +
            ": Range " + format(temp_range, ".1f") + " C "
            "(Max: " + format(max(temps), ".1f") + " C, "
            "Min: " + format(min(temps), ".1f") + " C)\n"
        )

range_file.close()

# calculataion of temperature stability and making file
std_values = {}

for station in station_temps:
    temps = station_temps[station]
    mean = sum(temps) / len(temps)

    total = 0
    for t in temps:
        # calculating difference
        total += (t - mean) ** 2

    # calculation of variance and standard deviation
    variance = total / len(temps)
    std_dev = math.sqrt(variance)

    std_values[station] = std_dev

min_std = min(std_values.values())
max_std = max(std_values.values())

std_file = open("temperature_stability_stations.txt", "w")

# finding station with most stable temperature
for station in std_values:
    if std_values[station] == min_std:
        std_file.write(
            "Most Stable: Station " + station +
            ": StdDev " + format(std_values[station], ".1f") + " C\n"
        )

# finding station with most variable temperature
for station in std_values:
    if std_values[station] == max_std:
        std_file.write(
            "Most Variable: Station " + station +
            ": StdDev " + format(std_values[station], ".1f") + " C\n"
        )

std_file.close()
 