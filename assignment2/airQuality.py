# Veer Singh, COMP 1701 FALL 2025
# Nov -6 2025

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
    sortedListOfMeasurements = sorted(listOfMeasurements)
    length = len(sortedListOfMeasurements)

    median = 0

    if((length / 2) % 2 == 0):
        medianIndex = (length / 2)
        medianIndexTwo = medianIndex + 1

        median = (sortedListOfMeasurements[medianIndex] + sortedListOfMeasurements[medianIndexTwo])/2
    else:
        medianIndex = (length // 2)

        median = sortedListOfMeasurements[medianIndex]     


    return median


def findWorstLocation(listOfMeasurements:list, locations:list):
    counter = 0
    greatestMeasurement = 0
    correspondingIndex = 0

    for measurement in listOfMeasurements:
        if measurement > greatestMeasurement:
            greatestMeasurement = measurement
            correspondingIndex = counter

        counter += 1

    return locations[correspondingIndex], listOfMeasurements[correspondingIndex]  