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
