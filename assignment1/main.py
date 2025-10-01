import math
import haversine as hs


def main()->None:
    latDegrees, latMinutes, latSeconds = hs.getInputCoord("Latitude")
    longDegrees, longMinutes, longSeconds = hs.getInputCoord("Longitude")

    ddLatitude = hs.convertFromDMSToDD(latDegrees, latMinutes, latSeconds)
    ddLongitude = hs.convertFromDMSToDD(longDegrees, longMinutes, longSeconds)

    ddEndingLat = 51.01376194
    ddEndingLong = 114.13369889
    avgEarthRadius = 6371008

    ddRadLatitude = math.radians(ddLatitude)
    ddRadLongitude = math.radians(ddLongitude)
    ddRadEndingLat = math.radians(ddEndingLat)
    ddRadEndingLong = math.radians(ddEndingLong)

    ddRadDeltaLat = ddRadEndingLat - ddRadLatitude
    ddRadDeltaLong = ddRadEndingLong - ddRadLongitude

    distanceToMRU = round((hs.haversine(ddRadDeltaLong, ddRadDeltaLat, ddRadLatitude, ddRadEndingLat) * avgEarthRadius) / 1000.0, 1)

    transitFareAdult = 3.80

    reducedFare = round(hs.reduceFare(transitFareAdult, distanceToMRU), 2)

    hs.tellUserResult(reducedFare, distanceToMRU, [latDegrees, latMinutes, latSeconds], [longDegrees, longMinutes, longSeconds])



if(__name__ == "__main__"):
    main()