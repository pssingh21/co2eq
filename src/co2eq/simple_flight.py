from meeting import Meeting, MeetingList, get_flight
# from meeting import IETFMeeting, IETFMeetingList, get_flight
from flight_utils import FlightDB
from conf import CONF

## For a single query, the simplest way to request a flight
origin = 'PAR'      # IATA city code
destination = 'LAX' # IATA airport code
flightDB = FlightDB( conf=CONF )
flight = flightDB.select_flight( origin, destination )

print( "The simplest way to retireve a flight!" )
print( flight )

## Retrieving a flight from origin to destination
## get_flight may perform requests at different dates in case, it does not get any response. 
## in this example, the databases are generated and passed to the requests as argument to avoid being instantiated for each request.
flight = get_flight( conf=CONF,  origin='PAR', destination='LAX' )
print( "A simple way to retrieve a flight!" )
print( flight )

