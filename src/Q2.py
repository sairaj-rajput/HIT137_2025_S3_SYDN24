import os
import csv
import math

# folder where all the temperature csv files is stored
temperature_folder = "temperatures"

# list for storing temperatures according to the seasons
summer = []
autumn = []
winter = []
spring = []

# empty dictionary for storing temprature of each station
station_temps = {}

# months according to the australia season
summer_months = ["December","January","February"]
autumn_months = ["March","April","May"]
winter_months = ["June","July","August"]
spring_months = ["September","October","November"]

# main function to read all csv files and process data

for file_name in os.listdir(temperature_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(temperature_folder, file_name)

        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                station = row["STATION_NAME"]

                
                if station not in station_temps:
                    station_temps[station] = []

            
                for month in (summer_months + autumn_months +
                              winter_months + spring_months):

                    value = row[month]

                
                    if value == "" or value.lower() == "nan":
                        continue

                    temp = float(value)

                
                    station_temps[station].append(temp)

                
                    if month in summer_months:
                        summer.append(temp)
                    elif month in autumn_months:
                        autumn.append(temp)
                    elif month in winter_months:
                        winter.append(temp)
                    else:
                        spring.append(temp)
