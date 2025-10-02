# Veer Singh, COMP 1701 Fall 2025
# Oct 1 2025

import math

def getInputCoord(coord:str):
    print(f'Please Enter {coord} Coord:')
    degrees = int(input("Degrees: "))
    minutes = int(input("Minutes: "))
    seconds = float(input("Seconds(3 decimals): "))

    return degrees, minutes, seconds

def convertFromDMSToDD(degrees:int, minutes:int, seconds:float)->float:
    return degrees + (minutes/60) + (seconds/3600)

def haversine(deltaLong, deltaLat, startLat, endLat)->float:
    a = math.sin(deltaLat / 2.0) ** 2 + math.cos(startLat) * math.cos(endLat) * math.sin(deltaLong / 2.0) ** 2 # [2]
    return 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def reduceFare(fare:float, distance:float)->float:
    return fare - (1/(0.4 + math.e ** (3-distance))) # From assignment PDF


def tellUserResult(fare:float, distance:float, startLat:object, startLong:object)->None:
    startLatDegrees, startLatMinutes, startLatSeconds = startLat
    startLongDegrees, startLongMinutes, startLongSeconds = startLong

    print()
    print()
    print(f'Travelling from {startLatDegrees}\u00b0 {startLatMinutes}\' {startLatSeconds}" N, {startLongDegrees}\u00b0 {startLongMinutes}\' {startLongSeconds}" W')
    print("to the Homage statue on the MRU Campus")
    print(f'The distance is approx {distance} km')
    print(f'The fare would be reduced to ${fare}')