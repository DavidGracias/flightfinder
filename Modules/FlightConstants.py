import json
from Modules.Airport import Airport

class FlightConstants():
    min_layover_minutes = 15

    regions = {
        # ENUM: ["list of airports in ENUM category"]
        "US-NorthEast": [],
        "Non-US": ["BQN", "LIR", "SDQ", "STT", "MBJ", "NAS", "PSE", "PUJ", "SAL", "CUN", "GUA", "SYQ", "SJO", "SJU"],
        # "Anywhere": FlightFinder.get_all_airports_within_circle(0, 0, float('inf')),
    }

    ALL_AIRLINES = "ALL"
    airlines = {
        # ENUM: ["list of airlines in ENUM category"]
        "Frontier": ["FFT"],
        ALL_AIRLINES: ["FFT"],
    }

    city_to_city_by_airline = {
        # Airline ICAO Code: [ Tuple(from, to) ]

        # Frontier list up to date as of 11/9/23
        "FFT": [
            ("BQN", "MCO"),
            ("BQN", "TPA"),
            ("ATL", "BWI"),
            ("ATL", "BUF"),
            ("ATL", "CUN"),
            ("ATL", "ORD"),
            ("ATL", "MDW"),
            ("ATL", "CVG"),
            ("ATL", "CLE"),
            ("ATL", "DFW"),
            ("ATL", "DEN"),
            ("ATL", "DET"),
            ("ATL", "FLL"),
            ("ATL", "GUA"),
            ("ATL", "houston"),
            ("ATL", "LAS"),
            ("ATL", "LIR"),
            ("ATL", "MIA"),
            ("ATL", "MBJ"),
            ("ATL", "NY"),
            ("ATL", "ONT"),
            ("ATL", "MCO"),
            ("ATL", "PHL"),
            ("ATL", "PHX"),
            ("ATL", "RDU"),
            ("ATL", "SLC"),
            ("ATL", "SAT"),
            ("ATL", "SAN"),
            ("ATL", "SFO"),
            ("ATL", "SJO"),
            ("ATL", "SJU"),
            ("ATL", "SAL"),
            ("ATL", "SDQ"),
            ("ATL", "TPA"),
            ("ATL", "TTN"),
            ("AUS", "DEN"),
            ("AUS", "LAS"),
            ("BWI", "ATL"),
            ("BWI", "CUN"),
            ("BWI", "DFW"),
            ("BWI", "DEN"),
            ("BWI", "MIA"),
            ("BWI", "MCO"),
            ("BWI", "PHX"),
            ("BWI", "SJU"),
            ("BWI", "TPA"),
            ("FYV", "DEN"),
            ("BMI", "DEN"),
            ("BOS", "MCO"),
            ("BOS", "PHL"),
            ("BUF", "ATL"),
            ("BUF", "DEN"),
            ("BUF", "MCO"),
            ("BUF", "RDU"),
            ("BUF", "TPA"),
            ("CUN", "ATL"),
            ("CUN", "BWI"),
            ("CUN", "ORD"),
            ("CUN", "MDW"),
            ("CUN", "DFW"),
            ("CUN", "DEN"),
            ("CUN", "DET"),
            ("CUN", "houston"),
            ("CUN", "MIA"),
            ("CUN", "MSP"),
            ("CUN", "MCO"),
            ("CUN", "PHL"),
            ("CUN", "SJU"),
            ("CUN", "STL"),
            ("CUN", "TPA"),
            ("CID", "DEN"),
            ("CHS", "PHL"),
            ("CLT", "CLE"),
            ("CLT", "DEN"),
            ("CLT", "LAS"),
            ("CLT", "MCO"),
            ("CLT", "PHL"),
            ("CLT", "TTN"),
            ("ORD", "ATL"),
            ("ORD", "CUN"),
            ("ORD", "DFW"),
            ("ORD", "DEN"),
            ("ORD", "LAS"),
            ("ORD", "MIA"),
            ("ORD", "MCO"),
            ("ORD", "PHL"),
            ("ORD", "PHX"),
            ("ORD", "RDU"),
            ("ORD", "SFO"),
            ("ORD", "SJU"),
            ("ORD", "TPA"),
            ("MDW", "ATL"),
            ("MDW", "CUN"),
            ("MDW", "DFW"),
            ("MDW", "DEN"),
            ("MDW", "LAS"),
            ("MDW", "MIA"),
            ("MDW", "MCO"),
            ("MDW", "PHL"),
            ("MDW", "PHX"),
            ("MDW", "RDU"),
            ("MDW", "SFO"),
            ("MDW", "SJU"),
            ("MDW", "TPA"),
            ("CVG", "ATL"),
            ("CVG", "DFW"),
            ("CVG", "DEN"),
            ("CVG", "RSW"),
            ("CVG", "LAS"),
            ("CVG", "MIA"),
            ("CVG", "MCO"),
            ("CVG", "PHL"),
            ("CVG", "RDU"),
            ("CVG", "TPA"),
            ("CLE", "ATL"),
            ("CLE", "CLT"),
            ("CLE", "DFW"),
            ("CLE", "DEN"),
            ("CLE", "FLL"),
            ("CLE", "RSW"),
            ("CLE", "LAS"),
            ("CLE", "MCO"),
            ("CLE", "PHL"),
            ("CLE", "PHX"),
            ("CLE", "RDU"),
            ("CLE", "SAN"),
            ("CLE", "SJU"),
            ("CLE", "TPA"),
            ("CMH", "DEN"),
            ("CMH", "MCO"),
            ("DFW", "ATL"),
            ("DFW", "BWI"),
            ("DFW", "CUN"),
            ("DFW", "ORD"),
            ("DFW", "MDW"),
            ("DFW", "CVG"),
            ("DFW", "CLE"),
            ("DFW", "DEN"),
            ("DFW", "LAS"),
            ("DFW", "MIA"),
            ("DFW", "MBJ"),
            ("DFW", "NY"),
            ("DFW", "ONT"),
            ("DFW", "MCO"),
            ("DFW", "PHL"),
            ("DFW", "PHX"),
            ("DFW", "RDU"),
            ("DFW", "SAN"),
            ("DFW", "SFO"),
            ("DFW", "SJU"),
            ("DFW", "SNA"),
            ("DFW", "TPA"),
            ("DEN", "ATL"),
            ("DEN", "AUS"),
            ("DEN", "BWI"),
            ("DEN", "FYV"),
            ("DEN", "BMI"),
            ("DEN", "BUF"),
            ("DEN", "CUN"),
            ("DEN", "CID"),
            ("DEN", "CLT"),
            ("DEN", "ORD"),
            ("DEN", "MDW"),
            ("DEN", "CVG"),
            ("DEN", "CLE"),
            ("DEN", "CMH"),
            ("DEN", "DFW"),
            ("DEN", "DSM"),
            ("DEN", "DET"),
            ("DEN", "ELP"),
            ("DEN", "FAR"),
            ("DEN", "GRR"),
            ("DEN", "GRB"),
            ("DEN", "houston"),
            ("DEN", "IND"),
            ("DEN", "JAX"),
            ("DEN", "MCI"),
            ("DEN", "TYS"),
            ("DEN", "LAS"),
            ("DEN", "LIT"),
            ("DEN", "MSN"),
            ("DEN", "MEM"),
            ("DEN", "MIA"),
            ("DEN", " MKE"),
            ("DEN", "MSP"),
            ("DEN", "MYR"),
            ("DEN", "BNA"),
            ("DEN", "MSY"),
            ("DEN", "OKC"),
            ("DEN", "OMA"),
            ("DEN", "ONT"),
            ("DEN", "MCO"),
            ("DEN", "PNS"),
            ("DEN", "PHL"),
            ("DEN", "PHX"),
            ("DEN", "PIT"),
            ("DEN", "PWM"),
            ("DEN", "RDU"),
            ("DEN", "SMF"),
            ("DEN", "SLC"),
            ("DEN", "SAT"),
            ("DEN", "SAN"),
            ("DEN", "SFO"),
            ("DEN", "SNA"),
            ("DEN", "SEA"),
            ("DEN", "FSD"),
            ("DEN", "STL"),
            ("DEN", "SYR"),
            ("DEN", "TPA"),
            ("DEN", "WA"),
            ("DSM", "DEN"),
            ("DET", "ATL"),
            ("DET", "CUN"),
            ("DET", "DEN"),
            ("DET", "RSW"),
            ("DET", "LAS"),
            ("DET", "MCO"),
            ("DET", "PHX"),
            ("DET", "RDU"),
            ("DET", "SFO"),
            ("DET", "TPA"),
            ("ELP", "DEN"),
            ("ELP", "LAS"),
            ("FAR", "DEN"),
            ("FLL", "ATL"),
            ("FLL", "CLE"),
            ("FLL", "ISP"),
            ("FLL", "PHL"),
            ("FLL", "TTN"),
            ("RSW", "CVG"),
            ("RSW", "CLE"),
            ("RSW", "DET"),
            ("RSW", "MSP"),
            ("RSW", "PHL"),
            ("GRR", "DEN"),
            ("GRR", "MCO"),
            ("GRB", "DEN"),
            ("GUA", "ATL"),
            ("GUA", "MIA"),
            ("MDT", "MCO"),
            ("BDL", "MCO"),
            ("BDL", "RDU"),
            ("BDL", "SJU"),
            ("houston", "ATL"),
            ("houston", "CUN"),
            ("houston", "DEN"),
            ("houston", "LAS"),
            ("houston", "MCO"),
            ("houston", "PHX"),
            ("houston", "RDU"),
            ("IND", "DEN"),
            ("IND", "LAS"),
            ("IND", "MCO"),
            ("IND", "RDU"),
            ("ISP", "FLL"),
            ("ISP", "MYR"),
            ("ISP", "MCO"),
            ("ISP", "RDU"),
            ("ISP", "TPA"),
            ("JAX", "DEN"),
            ("JAX", "PHL"),
            ("MCI", "DEN"),
            ("TYS", "DEN"),
            ("LAS", "ATL"),
            ("LAS", "AUS"),
            ("LAS", "CLT"),
            ("LAS", "ORD"),
            ("LAS", "MDW"),
            ("LAS", "CVG"),
            ("LAS", "CLE"),
            ("LAS", "DFW"),
            ("LAS", "DEN"),
            ("LAS", "DET"),
            ("LAS", "ELP"),
            ("LAS", "houston"),
            ("LAS", "IND"),
            ("LAS", "MIA"),
            ("LAS", " MKE"),
            ("LAS", "BNA"),
            ("LAS", "OKC"),
            ("LAS", "OMA"),
            ("LAS", "ONT"),
            ("LAS", "MCO"),
            ("LAS", "PHL"),
            ("LAS", "PHX"),
            ("LAS", "PWM"),
            ("LAS", "RDU"),
            ("LAS", "SLC"),
            ("LAS", "SAT"),
            ("LAS", "SAN"),
            ("LAS", "SFO"),
            ("LAS", "SNA"),
            ("LAS", "SEA"),
            ("LAS", "STL"),
            ("LAS", "TPA"),
            ("LIR", "ATL"),
            ("LIT", "DEN"),
            ("MSN", "DEN"),
            ("MEM", "DEN"),
            ("MIA", "ATL"),
            ("MIA", "BWI"),
            ("MIA", "CUN"),
            ("MIA", "ORD"),
            ("MIA", "MDW"),
            ("MIA", "CVG"),
            ("MIA", "DFW"),
            ("MIA", "DEN"),
            ("MIA", "GUA"),
            ("MIA", "LAS"),
            ("MIA", "MBJ"),
            ("MIA", "PHL"),
            ("MIA", "PUJ"),
            ("MIA", "SJO"),
            ("MIA", "SJU"),
            (" MKE", "DEN"),
            (" MKE", "LAS"),
            (" MKE", "MCO"),
            ("MSP", "CUN"),
            ("MSP", "DEN"),
            ("MSP", "RSW"),
            ("MBJ", "ATL"),
            ("MBJ", "DFW"),
            ("MBJ", "MIA"),
            ("MBJ", "MCO"),
            ("MBJ", "PHL"),
            ("MYR", "DEN"),
            ("MYR", "ISP"),
            ("MYR", "PHL"),
            ("BNA", "DEN"),
            ("BNA", "LAS"),
            ("BNA", "MCO"),
            ("BNA", "PHL"),
            ("BNA", "PHX"),
            ("NAS", "MCO"),
            ("MSY", "DEN"),
            ("MSY", "MCO"),
            ("MSY", "PHL"),
            ("MSY", "RDU"),
            ("NY", "ATL"),
            ("NY", "DFW"),
            ("NY", "MCO"),
            ("ORF", "MCO"),
            ("OKC", "DEN"),
            ("OKC", "LAS"),
            ("OMA", "DEN"),
            ("OMA", "LAS"),
            ("ONT", "ATL"),
            ("ONT", "DFW"),
            ("ONT", "DEN"),
            ("ONT", "LAS"),
            ("ONT", "MCO"),
            ("ONT", "SFO"),
            ("MCO", "BQN"),
            ("MCO", "ATL"),
            ("MCO", "BWI"),
            ("MCO", "BOS"),
            ("MCO", "BUF"),
            ("MCO", "CUN"),
            ("MCO", "CLT"),
            ("MCO", "ORD"),
            ("MCO", "MDW"),
            ("MCO", "CVG"),
            ("MCO", "CLE"),
            ("MCO", "CMH"),
            ("MCO", "DFW"),
            ("MCO", "DEN"),
            ("MCO", "DET"),
            ("MCO", "GRR"),
            ("MCO", "MDT"),
            ("MCO", "BDL"),
            ("MCO", "houston"),
            ("MCO", "IND"),
            ("MCO", "ISP"),
            ("MCO", "LAS"),
            ("MCO", " MKE"),
            ("MCO", "MBJ"),
            ("MCO", "BNA"),
            ("MCO", "NAS"),
            ("MCO", "MSY"),
            ("MCO", "NY"),
            ("MCO", "ORF"),
            ("MCO", "ONT"),
            ("MCO", "PHL"),
            ("MCO", "PHX"),
            ("MCO", "PIT"),
            ("MCO", "PSE"),
            ("MCO", "PWM"),
            ("MCO", "PUJ"),
            ("MCO", "RDU"),
            ("MCO", "SAT"),
            ("MCO", "SAN"),
            ("MCO", "SFO"),
            ("MCO", "SJU"),
            ("MCO", "SDQ"),
            ("MCO", "STL"),
            ("MCO", "SYR"),
            ("MCO", "TTN"),
            ("PNS", "DEN"),
            ("PHL", "ATL"),
            ("PHL", "BOS"),
            ("PHL", "CUN"),
            ("PHL", "CHS"),
            ("PHL", "CLT"),
            ("PHL", "ORD"),
            ("PHL", "MDW"),
            ("PHL", "CVG"),
            ("PHL", "CLE"),
            ("PHL", "DFW"),
            ("PHL", "DEN"),
            ("PHL", "FLL"),
            ("PHL", "RSW"),
            ("PHL", "JAX"),
            ("PHL", "LAS"),
            ("PHL", "MIA"),
            ("PHL", "MBJ"),
            ("PHL", "MYR"),
            ("PHL", "BNA"),
            ("PHL", "MSY"),
            ("PHL", "MCO"),
            ("PHL", "PUJ"),
            ("PHL", "RDU"),
            ("PHL", "SJU"),
            ("PHL", "SDQ"),
            ("PHL", "SRQ"),
            ("PHL", "SAV"),
            ("PHL", "TPA"),
            ("PHL", "PBI"),
            ("PHX", "ATL"),
            ("PHX", "BWI"),
            ("PHX", "ORD"),
            ("PHX", "MDW"),
            ("PHX", "CLE"),
            ("PHX", "DFW"),
            ("PHX", "DEN"),
            ("PHX", "DET"),
            ("PHX", "houston"),
            ("PHX", "LAS"),
            ("PHX", "BNA"),
            ("PHX", "MCO"),
            ("PHX", "PWM"),
            ("PHX", "SLC"),
            ("PHX", "SAN"),
            ("PHX", "SFO"),
            ("PHX", "SNA"),
            ("PHX", "SEA"),
            ("PHX", "TPA"),
            ("PIT", "DEN"),
            ("PIT", "MCO"),
            ("PSE", "MCO"),
            ("PWM", "MCO"),
            ("PWM", "RDU"),
            ("PWM", "DEN"),
            ("PWM", "LAS"),
            ("PWM", "PHX"),
            ("PUJ", "MIA"),
            ("PUJ", "MCO"),
            ("PUJ", "PHL"),
            ("PUJ", "SJU"),
            ("PUJ", "TPA"),
            ("RDU", "ATL"),
            ("RDU", "BUF"),
            ("RDU", "ORD"),
            ("RDU", "MDW"),
            ("RDU", "CVG"),
            ("RDU", "CLE"),
            ("RDU", "DFW"),
            ("RDU", "DEN"),
            ("RDU", "DET"),
            ("RDU", "BDL"),
            ("RDU", "houston"),
            ("RDU", "IND"),
            ("RDU", "ISP"),
            ("RDU", "LAS"),
            ("RDU", "MSY"),
            ("RDU", "MCO"),
            ("RDU", "PHL"),
            ("RDU", "PWM"),
            ("RDU", "SJU"),
            ("RDU", "SYR"),
            ("RDU", "TTN"),
            ("SMF", "DEN"),
            ("SLC", "ATL"),
            ("SLC", "DEN"),
            ("SLC", "LAS"),
            ("SLC", "PHX"),
            ("SAT", "ATL"),
            ("SAT", "DEN"),
            ("SAT", "LAS"),
            ("SAT", "MCO"),
            ("SAN", "ATL"),
            ("SAN", "CLE"),
            ("SAN", "DFW"),
            ("SAN", "DEN"),
            ("SAN", "LAS"),
            ("SAN", "MCO"),
            ("SAN", "PHX"),
            ("SFO", "ATL"),
            ("SFO", "ORD"),
            ("SFO", "MDW"),
            ("SFO", "DFW"),
            ("SFO", "DEN"),
            ("SFO", "DET"),
            ("SFO", "LAS"),
            ("SFO", "ONT"),
            ("SFO", "MCO"),
            ("SFO", "PHX"),
            ("SJO", "ATL"),
            ("SJO", "MIA"),
            ("SJU", "ATL"),
            ("SJU", "BWI"),
            ("SJU", "CUN"),
            ("SJU", "ORD"),
            ("SJU", "MDW"),
            ("SJU", "CLE"),
            ("SJU", "DFW"),
            ("SJU", "BDL"),
            ("SJU", "MIA"),
            ("SJU", "MCO"),
            ("SJU", "PHL"),
            ("SJU", "PUJ"),
            ("SJU", "RDU"),
            ("SJU", "SDQ"),
            ("SJU", "STT"),
            ("SJU", "TPA"),
            ("SAL", "ATL"),
            ("SNA", "DFW"),
            ("SNA", "DEN"),
            ("SNA", "LAS"),
            ("SNA", "PHX"),
            ("SDQ", "ATL"),
            ("SDQ", "MCO"),
            ("SDQ", "PHL"),
            ("SDQ", "SJU"),
            ("SDQ", "TPA"),
            ("SRQ", "PHL"),
            ("SAV", "PHL"),
            ("SEA", "DEN"),
            ("SEA", "LAS"),
            ("SEA", "PHX"),
            ("FSD", "DEN"),
            ("STL", "CUN"),
            ("STL", "DEN"),
            ("STL", "LAS"),
            ("STL", "MCO"),
            ("STT", "SJU"),
            ("SYR", "DEN"),
            ("SYR", "MCO"),
            ("SYR", "RDU"),
            ("TPA", "BQN"),
            ("TPA", "ATL"),
            ("TPA", "BWI"),
            ("TPA", "BUF"),
            ("TPA", "CUN"),
            ("TPA", "ORD"),
            ("TPA", "MDW"),
            ("TPA", "CVG"),
            ("TPA", "CLE"),
            ("TPA", "DFW"),
            ("TPA", "DEN"),
            ("TPA", "DET"),
            ("TPA", "ISP"),
            ("TPA", "LAS"),
            ("TPA", "PHL"),
            ("TPA", "PHX"),
            ("TPA", "PUJ"),
            ("TPA", "SJU"),
            ("TPA", "SDQ"),
            ("TPA", "TTN"),
            ("TTN", "ATL"),
            ("TTN", "CLT"),
            ("TTN", "FLL"),
            ("TTN", "MCO"),
            ("TTN", "RDU"),
            ("TTN", "TPA"),
            ("WA", "DEN"),
            ("PBI", "PHL"),
        ],
    }


    DEFAULT_TRAVEL_DISTANCE = 80

    def get_all_airports():
        f = open('Modules/airports-code@public.json')
        airport_data = json.load(f)

        airports = []
        for airport in airport_data:
            airport_code = airport["column_1"]
            latitude = airport["latitude"]
            longitude = airport["longitude"]
            country_code = airport["country_code"]
            
            airports.append(
                Airport(airport_code, latitude, longitude, country_code)
            )
        return airports
    
    def get_airport_from_code(code):
        all_airports = FlightConstants.get_all_airports()
        for airport in all_airports:
            if airport == code: return airport
        exit(f"The given code \"{code}\" is not a valid airport code / was not found")
