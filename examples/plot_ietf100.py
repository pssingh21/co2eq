from co2eq.meeting import Meeting, MeetingList, get_flight
from conf import CONF

## Ploting a single IETF meeting
ietf_meeting = Meeting( name='IETF100', location={'iata':"BER"}, conf = CONF ) 
for cluster_key in [ None, 'country', 'organization', 'presence', 'flight_segment_number' ]:
  ietf_meeting.plot_co2eq( mode=[ 'flight', 'distance' ], cluster_key=cluster_key, cluster_nbr=15)
  ietf_meeting.plot_co2eq( mode='attendee', cluster_key=cluster_key, cluster_nbr=15)

## generating md page
ietf_meeting.md()
