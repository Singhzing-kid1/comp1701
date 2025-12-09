# Veer Singh, COMP 1701 FALL 2025
# Nov -6 2025

import airQuality as aq      

def main()->None:
    originalAirQualityMeasurements = [141, 53, 46, 142, 153, 136, 52, 55, 23, 73]
    airQualityMeasurements = []
    locations = ["Airdrie", "Ardrossan", "Banff South of Bow River", "Brooks Meadowplace", "Calgary Varsity", "Caroline", "Cold Lake South", "Conklin", "Cougar Point Road, Canmore", "Drayton Valley"]
    aq.enterAirQualityMeasurements(locations, airQualityMeasurements)

    originalMean = aq.calculateMeanAirQuality(originalAirQualityMeasurements)
    currentMean = aq.calculateMeanAirQuality(airQualityMeasurements)

    originalMedian = aq.calculateMedianAirQuality(originalAirQualityMeasurements)
    currentMedian = aq.calculateMedianAirQuality(airQualityMeasurements)

    originalWorstLocation, originalWorstMeasurement = aq.findWorstLocation(originalAirQualityMeasurements, locations)
    currentWorstLocation, currentWorstMeasuement = aq.findWorstLocation(airQualityMeasurements, locations)

    percentageOfGoodAirQualityValues = aq.calculatePercentageOfGoodAirQaulityValues(airQualityMeasurements)

    print(f'\nThe mean air quality measurement for the orignal measurements is: {originalMean}')
    print(f'The mean air quality measurement for the user entered measurements is: {currentMean}\n')

    print(f'The median air quality measurement for the orignal measurements is: {originalMedian}')
    print(f'The median air quality measurement for the user entered measurements is: {currentMedian}\n')

    print(f'The original location with the worst air quality is: {originalWorstLocation} with a measurement of {originalWorstMeasurement}')
    print(f'The user entered location with the worst air quality is: {currentWorstLocation} with a measurement of {currentWorstMeasuement}\n')

    print(f'{percentageOfGoodAirQualityValues} of the entered locations have air quality values of 50 or lower')



if(__name__ == "__main__"):
    main()