# Veer Singh, COMP 1701 FALL 2025
#

import math

def askUserForMeasurement(location:str)->int:
    return int(input(f'please enter the measurement for {location}: '))

def enterAirQualityMeasurements(locations:list, listOfMeasurements:list)->None:
    for location in locations:
        listOfMeasurements.append(askUserForMeasurement(location))
    
def calculatePercentageOfGoodAirQaulityValues(listOfMeasurements:list)->int:
    amountOfMeasurements = len(listOfMeasurements);

    goodAirQualityMeasurements = [x for x in listOfMeasurements if x <= 50]

    amountOfGoodMeasurements = len(goodAirQualityMeasurements);

    return (amountOfGoodMeasurements/amountOfMeasurements) * 100

def calculateMeanAirQuality(listOfMeasurements:list)->float:
    return round(sum(listOfMeasurements)/len(listOfMeasurements), 1)

def calculateMedianAirQuality(listOfMeasurements:list)->float:
    listOfMeasurements.sort()
    length = len(listOfMeasurements)
    medianIndex = length/2 if length % 2 == 0 else math.ceil(length/2)

    return round(listOfMeasurements[medianIndex], 1)





def main()->None:
    airQualityMeasurements = []
    locations = []
    enterAirQualityMeasurements(locations, airQualityMeasurements)

    percentageOfGoodAirQualityValues = calculatePercentageOfGoodAirQaulityValues(airQualityMeasurements)

    print(f'{percentageOfGoodAirQualityValues} of the entered locations have air quality values of 50 or lower')



if(__name__ == "__main__"):
    main()