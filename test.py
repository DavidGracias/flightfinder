from bs4 import BeautifulSoup

from_to = [
("aguadilla", "orlando"),
("aguadilla", "tampa"),
("atlanta", "baltimore"),
("atlanta", "buffalo"),
("atlanta", "cancun"),
("atlanta", "chicago"),
("atlanta", "cincinnati"),
("atlanta", "cleveland"),
("atlanta", "dallas"),
("atlanta", "denver"),
("atlanta", "detroit"),
("atlanta", "fort lauderdale"),
("atlanta", "guatemala city"),
("atlanta", "houston"),
("atlanta", "las vegas"),
("atlanta", "liberia 1"),
("atlanta", "miami"),
("atlanta", "montego bay"),
("atlanta", "new york"),
("atlanta", "ontario ca"),
("atlanta", "orlando"),
("atlanta", "philadelphia"),
("atlanta", "phoenix"),
("atlanta", "raleigh"),
("atlanta", "salt lake city"),
("atlanta", "san antonio"),
("atlanta", "san diego"),
("atlanta", "san francisco"),
("atlanta", "san jose 3"),
("atlanta", "san juan"),
("atlanta", "san salvador"),
("atlanta", "santo domingo"),
("atlanta", "tampa"),
("atlanta", "trenton"),
("austin", "denver"),
("austin", "las vegas"),
("baltimore", "atlanta"),
("baltimore", "cancun"),
("baltimore", "dallas"),
("baltimore", "denver"),
("baltimore", "miami"),
("baltimore", "orlando"),
("baltimore", "phoenix"),
("baltimore", "san juan"),
("baltimore", "tampa"),
("fayetteville", "denver"),
("bloomington", "denver"),
("boston", "orlando"),
("boston", "philadelphia"),
("buffalo", "atlanta"),
("buffalo", "denver"),
("buffalo", "orlando"),
("buffalo", "raleigh"),
("buffalo", "tampa"),
("cancun", "atlanta"),
("cancun", "baltimore"),
("cancun", "chicago"),
("cancun", "dallas"),
("cancun", "denver"),
("cancun", "detroit"),
("cancun", "houston"),
("cancun", "miami"),
("cancun", "minneapolis"),
("cancun", "orlando"),
("cancun", "philadelphia"),
("cancun", "san juan"),
("cancun", "st louis"),
("cancun", "tampa"),
("cedar rapids", "denver"),
("charleston", "philadelphia"),
("charlotte", "cleveland"),
("charlotte", "denver"),
("charlotte", "las vegas"),
("charlotte", "orlando"),
("charlotte", "philadelphia"),
("charlotte", "trenton"),
("chicago", "atlanta"),
("chicago", "cancun"),
("chicago", "dallas"),
("chicago", "denver"),
("chicago", "las vegas"),
("chicago", "miami"),
("chicago", "orlando"),
("chicago", "philadelphia"),
("chicago", "phoenix"),
("chicago", "raleigh"),
("chicago", "san francisco"),
("chicago", "san juan"),
("chicago", "tampa"),
("cincinnati", "atlanta"),
("cincinnati", "dallas"),
("cincinnati", "denver"),
("cincinnati", "fort myers"),
("cincinnati", "las vegas"),
("cincinnati", "miami"),
("cincinnati", "orlando"),
("cincinnati", "philadelphia"),
("cincinnati", "raleigh"),
("cincinnati", "tampa"),
("cleveland", "atlanta"),
("cleveland", "charlotte"),
("cleveland", "dallas"),
("cleveland", "denver"),
("cleveland", "fort lauderdale"),
("cleveland", "fort myers"),
("cleveland", "las vegas"),
("cleveland", "orlando"),
("cleveland", "philadelphia"),
("cleveland", "phoenix"),
("cleveland", "raleigh"),
("cleveland", "san diego"),
("cleveland", "san juan"),
("cleveland", "tampa"),
("columbus", "denver"),
("columbus", "orlando"),
("dallas", "atlanta"),
("dallas", "baltimore"),
("dallas", "cancun"),
("dallas", "chicago"),
("dallas", "cincinnati"),
("dallas", "cleveland"),
("dallas", "denver"),
("dallas", "las vegas"),
("dallas", "miami"),
("dallas", "montego bay"),
("dallas", "new york"),
("dallas", "ontario ca"),
("dallas", "orlando"),
("dallas", "philadelphia"),
("dallas", "phoenix"),
("dallas", "raleigh"),
("dallas", "san diego"),
("dallas", "san francisco"),
("dallas", "san juan"),
("dallas", "orange county"),
("dallas", "tampa"),
("denver", "atlanta"),
("denver", "austin"),
("denver", "baltimore"),
("denver", "fayetteville"),
("denver", "bloomington"),
("denver", "buffalo"),
("denver", "cancun"),
("denver", "cedar rapids"),
("denver", "charlotte"),
("denver", "chicago"),
("denver", "cincinnati"),
("denver", "cleveland"),
("denver", "columbus"),
("denver", "dallas"),
("denver", "des moines"),
("denver", "detroit"),
("denver", "el paso"),
("denver", "fargo"),
("denver", "grand rapids"),
("denver", "green bay"),
("denver", "houston"),
("denver", "indianapolis"),
("denver", "jacksonville"),
("denver", "kansas city"),
("denver", "knoxville"),
("denver", "las vegas"),
("denver", "little rock"),
("denver", "madison"),
("denver", "memphis"),
("denver", "miami"),
("denver", "milwaukee"),
("denver", "minneapolis"),
("denver", "myrtle beach"),
("denver", "nashville"),
("denver", "new orleans"),
("denver", "oklahoma city"),
("denver", "omaha"),
("denver", "ontario ca"),
("denver", "orlando"),
("denver", "pensacola"),
("denver", "philadelphia"),
("denver", "phoenix"),
("denver", "pittsburgh"),
("denver", "portland"),
("denver", "raleigh"),
("denver", "sacramento"),
("denver", "salt lake city"),
("denver", "san antonio"),
("denver", "san diego"),
("denver", "san francisco"),
("denver", "orange county"),
("denver", "seattle"),
("denver", "sioux falls"),
("denver", "st louis"),
("denver", "syracuse"),
("denver", "tampa"),
("denver", "washington"),
("des moines", "denver"),
("detroit", "atlanta"),
("detroit", "cancun"),
("detroit", "denver"),
("detroit", "fort myers"),
("detroit", "las vegas"),
("detroit", "orlando"),
("detroit", "phoenix"),
("detroit", "raleigh"),
("detroit", "san francisco"),
("detroit", "tampa"),
("el paso", "denver"),
("el paso", "las vegas"),
("fargo", "denver"),
("fort lauderdale", "atlanta"),
("fort lauderdale", "cleveland"),
("fort lauderdale", "long island"),
("fort lauderdale", "philadelphia"),
("fort lauderdale", "trenton"),
("fort myers", "cincinnati"),
("fort myers", "cleveland"),
("fort myers", "detroit"),
("fort myers", "minneapolis"),
("fort myers", "philadelphia"),
("grand rapids", "denver"),
("grand rapids", "orlando"),
("green bay", "denver"),
("guatemala city", "atlanta"),
("guatemala city", "miami"),
("harrisburg", "orlando"),
("hartford", "orlando"),
("hartford", "raleigh"),
("hartford", "san juan"),
("houston", "atlanta"),
("houston", "cancun"),
("houston", "denver"),
("houston", "las vegas"),
("houston", "orlando"),
("houston", "phoenix"),
("houston", "raleigh"),
("indianapolis", "denver"),
("indianapolis", "las vegas"),
("indianapolis", "orlando"),
("indianapolis", "raleigh"),
("long island", "fort lauderdale"),
("long island", "myrtle beach"),
("long island", "orlando"),
("long island", "raleigh"),
("long island", "tampa"),
("jacksonville", "denver"),
("jacksonville", "philadelphia"),
("kansas city", "denver"),
("knoxville", "denver"),
("las vegas", "atlanta"),
("las vegas", "austin"),
("las vegas", "charlotte"),
("las vegas", "chicago"),
("las vegas", "cincinnati"),
("las vegas", "cleveland"),
("las vegas", "dallas"),
("las vegas", "denver"),
("las vegas", "detroit"),
("las vegas", "el paso"),
("las vegas", "houston"),
("las vegas", "indianapolis"),
("las vegas", "miami"),
("las vegas", "milwaukee"),
("las vegas", "nashville"),
("las vegas", "oklahoma city"),
("las vegas", "omaha"),
("las vegas", "ontario ca"),
("las vegas", "orlando"),
("las vegas", "philadelphia"),
("las vegas", "phoenix"),
("las vegas", "portland"),
("las vegas", "raleigh"),
("las vegas", "salt lake city"),
("las vegas", "san antonio"),
("las vegas", "san diego"),
("las vegas", "san francisco"),
("las vegas", "orange county"),
("las vegas", "seattle"),
("las vegas", "st louis"),
("las vegas", "tampa"),
("liberia 1", "atlanta"),
("little rock", "denver"),
("madison", "denver"),
("memphis", "denver"),
("miami", "atlanta"),
("miami", "baltimore"),
("miami", "cancun"),
("miami", "chicago"),
("miami", "cincinnati"),
("miami", "dallas"),
("miami", "denver"),
("miami", "guatemala city"),
("miami", "las vegas"),
("miami", "montego bay"),
("miami", "philadelphia"),
("miami", "punta cana"),
("miami", "san jose 3"),
("miami", "san juan"),
("milwaukee", "denver"),
("milwaukee", "las vegas"),
("milwaukee", "orlando"),
("minneapolis", "cancun"),
("minneapolis", "denver"),
("minneapolis", "fort myers"),
("montego bay", "atlanta"),
("montego bay", "dallas"),
("montego bay", "miami"),
("montego bay", "orlando"),
("montego bay", "philadelphia"),
("myrtle beach", "denver"),
("myrtle beach", "long island"),
("myrtle beach", "philadelphia"),
("nashville", "denver"),
("nashville", "las vegas"),
("nashville", "orlando"),
("nashville", "philadelphia"),
("nashville", "phoenix"),
("nassau", "orlando"),
("new orleans", "denver"),
("new orleans", "orlando"),
("new orleans", "philadelphia"),
("new orleans", "raleigh"),
("new york", "atlanta"),
("new york", "dallas"),
("new york", "orlando"),
("norfolk", "orlando"),
("oklahoma city", "denver"),
("oklahoma city", "las vegas"),
("omaha", "denver"),
("omaha", "las vegas"),
("ontario ca", "atlanta"),
("ontario ca", "dallas"),
("ontario ca", "denver"),
("ontario ca", "las vegas"),
("ontario ca", "orlando"),
("ontario ca", "san francisco"),
("orlando", "aguadilla"),
("orlando", "atlanta"),
("orlando", "baltimore"),
("orlando", "boston"),
("orlando", "buffalo"),
("orlando", "cancun"),
("orlando", "charlotte"),
("orlando", "chicago"),
("orlando", "cincinnati"),
("orlando", "cleveland"),
("orlando", "columbus"),
("orlando", "dallas"),
("orlando", "denver"),
("orlando", "detroit"),
("orlando", "grand rapids"),
("orlando", "harrisburg"),
("orlando", "hartford"),
("orlando", "houston"),
("orlando", "indianapolis"),
("orlando", "long island"),
("orlando", "las vegas"),
("orlando", "milwaukee"),
("orlando", "montego bay"),
("orlando", "nashville"),
("orlando", "nassau"),
("orlando", "new orleans"),
("orlando", "new york"),
("orlando", "norfolk"),
("orlando", "ontario ca"),
("orlando", "philadelphia"),
("orlando", "phoenix"),
("orlando", "pittsburgh"),
("orlando", "ponce"),
("orlando", "portland me"),
("orlando", "punta cana"),
("orlando", "raleigh"),
("orlando", "san antonio"),
("orlando", "san diego"),
("orlando", "san francisco"),
("orlando", "san juan"),
("orlando", "santo domingo"),
("orlando", "st louis"),
("orlando", "syracuse"),
("orlando", "trenton"),
("pensacola", "denver"),
("philadelphia", "atlanta"),
("philadelphia", "boston"),
("philadelphia", "cancun"),
("philadelphia", "charleston"),
("philadelphia", "charlotte"),
("philadelphia", "chicago"),
("philadelphia", "cincinnati"),
("philadelphia", "cleveland"),
("philadelphia", "dallas"),
("philadelphia", "denver"),
("philadelphia", "fort lauderdale"),
("philadelphia", "fort myers"),
("philadelphia", "jacksonville"),
("philadelphia", "las vegas"),
("philadelphia", "miami"),
("philadelphia", "montego bay"),
("philadelphia", "myrtle beach"),
("philadelphia", "nashville"),
("philadelphia", "new orleans"),
("philadelphia", "orlando"),
("philadelphia", "punta cana"),
("philadelphia", "raleigh"),
("philadelphia", "san juan"),
("philadelphia", "santo domingo"),
("philadelphia", "sarasota"),
("philadelphia", "savannah"),
("philadelphia", "tampa"),
("philadelphia", "west palm beach"),
("phoenix", "atlanta"),
("phoenix", "baltimore"),
("phoenix", "chicago"),
("phoenix", "cleveland"),
("phoenix", "dallas"),
("phoenix", "denver"),
("phoenix", "detroit"),
("phoenix", "houston"),
("phoenix", "las vegas"),
("phoenix", "nashville"),
("phoenix", "orlando"),
("phoenix", "portland"),
("phoenix", "salt lake city"),
("phoenix", "san diego"),
("phoenix", "san francisco"),
("phoenix", "orange county"),
("phoenix", "seattle"),
("phoenix", "tampa"),
("pittsburgh", "denver"),
("pittsburgh", "orlando"),
("ponce", "orlando"),
("portland me", "orlando"),
("portland me", "raleigh"),
("portland", "denver"),
("portland", "las vegas"),
("portland", "phoenix"),
("punta cana", "miami"),
("punta cana", "orlando"),
("punta cana", "philadelphia"),
("punta cana", "san juan"),
("punta cana", "tampa"),
("raleigh", "atlanta"),
("raleigh", "buffalo"),
("raleigh", "chicago"),
("raleigh", "cincinnati"),
("raleigh", "cleveland"),
("raleigh", "dallas"),
("raleigh", "denver"),
("raleigh", "detroit"),
("raleigh", "hartford"),
("raleigh", "houston"),
("raleigh", "indianapolis"),
("raleigh", "long island"),
("raleigh", "las vegas"),
("raleigh", "new orleans"),
("raleigh", "orlando"),
("raleigh", "philadelphia"),
("raleigh", "portland me"),
("raleigh", "san juan"),
("raleigh", "syracuse"),
("raleigh", "trenton"),
("sacramento", "denver"),
("salt lake city", "atlanta"),
("salt lake city", "denver"),
("salt lake city", "las vegas"),
("salt lake city", "phoenix"),
("san antonio", "atlanta"),
("san antonio", "denver"),
("san antonio", "las vegas"),
("san antonio", "orlando"),
("san diego", "atlanta"),
("san diego", "cleveland"),
("san diego", "dallas"),
("san diego", "denver"),
("san diego", "las vegas"),
("san diego", "orlando"),
("san diego", "phoenix"),
("san francisco", "atlanta"),
("san francisco", "chicago"),
("san francisco", "dallas"),
("san francisco", "denver"),
("san francisco", "detroit"),
("san francisco", "las vegas"),
("san francisco", "ontario ca"),
("san francisco", "orlando"),
("san francisco", "phoenix"),
("san jose 3", "atlanta"),
("san jose 3", "miami"),
("san juan", "atlanta"),
("san juan", "baltimore"),
("san juan", "cancun"),
("san juan", "chicago"),
("san juan", "cleveland"),
("san juan", "dallas"),
("san juan", "hartford"),
("san juan", "miami"),
("san juan", "orlando"),
("san juan", "philadelphia"),
("san juan", "punta cana"),
("san juan", "raleigh"),
("san juan", "santo domingo"),
("san juan", "st thomas"),
("san juan", "tampa"),
("san salvador", "atlanta"),
("orange county", "dallas"),
("orange county", "denver"),
("orange county", "las vegas"),
("orange county", "phoenix"),
("santo domingo", "atlanta"),
("santo domingo", "orlando"),
("santo domingo", "philadelphia"),
("santo domingo", "san juan"),
("santo domingo", "tampa"),
("sarasota", "philadelphia"),
("savannah", "philadelphia"),
("seattle", "denver"),
("seattle", "las vegas"),
("seattle", "phoenix"),
("sioux falls", "denver"),
("st louis", "cancun"),
("st louis", "denver"),
("st louis", "las vegas"),
("st louis", "orlando"),
("st thomas", "san juan"),
("syracuse", "denver"),
("syracuse", "orlando"),
("syracuse", "raleigh"),
("tampa", "aguadilla"),
("tampa", "atlanta"),
("tampa", "baltimore"),
("tampa", "buffalo"),
("tampa", "cancun"),
("tampa", "chicago"),
("tampa", "cincinnati"),
("tampa", "cleveland"),
("tampa", "dallas"),
("tampa", "denver"),
("tampa", "detroit"),
("tampa", "long island"),
("tampa", "las vegas"),
("tampa", "philadelphia"),
("tampa", "phoenix"),
("tampa", "punta cana"),
("tampa", "san juan"),
("tampa", "santo domingo"),
("tampa", "trenton"),
("trenton", "atlanta"),
("trenton", "charlotte"),
("trenton", "fort lauderdale"),
("trenton", "orlando"),
("trenton", "raleigh"),
("trenton", "tampa"),
("washington", "denver"),
("west palm beach", "philadelphia"),
]

print(len(from_to))

html = '<tbody><tr bgcolor="#d1d1d1"> <td><span>Alabama</span></td> <td><span>AL</span></td> </tr><tr> <td>Birmingham International Airport</td> <td>BHM</td> </tr><tr> <td>Dothan Regional Airport</td> <td>DHN</td> </tr><tr> <td>Huntsville International Airport</td> <td>HSV</td> </tr><tr> <td>Mobile</td> <td>MOB</td> </tr><tr> <td>Montgomery</td> <td>MGM</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Alaska</span></td> <td><span>AK</span></td> </tr><tr> <td>Anchorage International Airport</td> <td>ANC</td> </tr><tr> <td>Fairbanks  International Airport</td> <td>FAI</td> </tr><tr> <td>Juneau  International Airport  </td> <td>JNU</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Arizona</span></td> <td><span>AZ</span></td> </tr><tr> <td>Flagstaff</td> <td>FLG</td> </tr><tr> <td>Phoenix, <i>Phoenix Sky Harbor International Airport</i></td> <td>PHX</td> </tr><tr> <td>Tucson  International Airport</td> <td>TUS</td> </tr><tr> <td>Yuma  International Airport</td> <td>YUM</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Arkansas</span></td> <td><span>AR</span></td> </tr><tr> <td>Fayetteville</td> <td>FYV</td> </tr><tr> <td>Little Rock National Airport</td> <td>LIT</td> </tr><tr> <td>Northwest Arkansas Regional Airport</td> <td>XNA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>California</span></td> <td><span>CA</span></td> </tr><tr> <td>Burbank</td> <td>BUR</td> </tr><tr> <td>Fresno</td> <td>FAT</td> </tr><tr> <td>Long Beach</td> <td>LGB</td> </tr><tr> <td>Los Angeles International Airport</td> <td>LAX</td> </tr><tr> <td>Oakland</td> <td>OAK</td> </tr><tr> <td>Ontario</td> <td>ONT</td> </tr><tr> <td>Palm Springs</td> <td>PSP</td> </tr><tr> <td>Sacramento</td> <td>SMF</td> </tr><tr> <td>San Diego</td> <td>SAN</td> </tr><tr> <td>San Francisco International Airport</td> <td>SFO</td> </tr><tr> <td>San Jose</td> <td>SJC</td> </tr><tr> <td>Santa Ana</td> <td>SNA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Colorado</span></td> <td><span>CO</span></td> </tr><tr> <td>Aspen</td> <td>ASE</td> </tr><tr> <td>Colorado Springs</td> <td>COS</td> </tr><tr> <td>Denver International  Airport</td> <td>DEN</td> </tr><tr> <td>Grand Junction</td> <td>GJT</td> </tr><tr> <td>Pueblo</td> <td>PUB</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Connecticut</span></td> <td><span>CT</span></td> </tr><tr> <td>Hartford</td> <td>BDL</td> </tr><tr> <td>Tweed New Haven</td> <td>HVN</td> </tr><tr bgcolor="#d1d1d1"> <td><span>District of Columbia</span></td> <td><span>DC</span></td> </tr><tr> <td>Washington, <i>Dulles International Airport</i></td> <td>IAD</td> </tr><tr> <td>Washington National  Airport</td> <td>DCA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Florida</span></td> <td><span>FL</span></td> </tr><tr> <td>Daytona Beach</td> <td>DAB</td> </tr><tr> <td>Fort Lauderdale-Hollywood International Airport</td> <td>FLL</td> </tr><tr> <td>Fort Meyers</td> <td>RSW</td> </tr><tr> <td>Jacksonville</td> <td>JAX</td> </tr><tr> <td>Key West International Airport</td> <td>EYW</td> </tr><tr> <td>Miami International Airport</td> <td>MIA</td> </tr><tr> <td>Orlando</td> <td>MCO</td> </tr><tr> <td>Pensacola</td> <td>PNS</td> </tr><tr> <td>St. Petersburg</td> <td>PIE</td> </tr><tr> <td>Sarasota</td> <td>SRQ</td> </tr><tr> <td>Tampa</td> <td>TPA</td> </tr><tr> <td>West Palm Beach</td> <td>PBI</td> </tr><tr> <td>Panama City-Bay County International Airport </td> <td>PFN</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Georgia</span></td> <td><span>GA</span></td> </tr><tr> <td>Atlanta Hartsfield International Airport</td> <td>ATL</td> </tr><tr> <td>Augusta</td> <td>AGS</td> </tr><tr> <td>Savannah</td> <td>SAV</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Hawaii</span></td> <td><span>HI</span></td> </tr><tr> <td>Hilo</td> <td>ITO</td> </tr><tr> <td>Honolulu International Airport</td> <td>HNL</td> </tr><tr> <td>Kahului</td> <td>OGG</td> </tr><tr> <td>Kailua</td> <td>KOA</td> </tr><tr> <td>Lihue</td> <td>LIH</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Idaho</span></td> <td><span>ID</span></td> </tr><tr> <td>Boise</td> <td>BOI</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Illinois</span></td> <td><span>IL</span></td> </tr><tr> <td>Chicago Midway Airport</td> <td>MDW</td> </tr><tr> <td>Chicago, <i>OHare International Airport  Airport</i></td> <td>ORD</td> </tr><tr> <td>Moline</td> <td>MLI</td> </tr><tr> <td>Peoria</td> <td>PIA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Indiana</span></td> <td><span>IN</span></td> </tr><tr> <td>Evansville</td> <td>EVV</td> </tr><tr> <td>Fort Wayne</td> <td>FWA</td> </tr><tr> <td>Indianapolis International Airport</td> <td>IND</td> </tr><tr> <td>South Bend</td> <td>SBN</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Iowa</span></td> <td><span>IA</span></td> </tr><tr> <td>Cedar Rapids</td> <td>CID</td> </tr><tr> <td>Des Moines</td> <td>DSM</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Kansas</span></td> <td><span>KS</span></td> </tr><tr> <td>Wichita</td> <td>ICT</td> </tr><tr> <td><span>Kentucky</span></td> <td><span>KY</span></td> </tr><tr> <td>Lexington</td> <td>LEX</td> </tr><tr> <td>Louisville</td> <td>SDF</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Louisiana</span></td> <td><span>LA</span></td> </tr><tr> <td>Baton Rouge</td> <td>BTR</td> </tr><tr> <td>New Orleans International Airport</td> <td>MSY</td> </tr><tr> <td>Shreveport</td> <td>SHV</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Maine</span></td> <td><span>ME</span></td> </tr><tr> <td>Augusta</td> <td>AUG</td> </tr><tr> <td>Bangor</td> <td> BGR</td> </tr><tr> <td>Portland</td> <td>PWM</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Maryland</span></td> <td><span>MD</span></td> </tr><tr> <td>Baltimore</td> <td>BWI</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Massachusetts</span></td> <td><span>MA</span></td> </tr><tr> <td>Boston, Logan International Airport</td> <td>BOS</td> </tr><tr> <td>Hyannis</td> <td>HYA</td> </tr><tr> <td>Nantucket</td> <td>ACK</td> </tr><tr> <td>Worcester</td> <td>ORH</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Michigan</span></td> <td><span>MI</span></td> </tr><tr> <td>Battlecreek</td> <td>BTL</td> </tr><tr> <td>Detroit Metropolitan Airport</td> <td> DTW</td> </tr><tr> <td>Detroit</td> <td>DET</td> </tr><tr> <td>Flint</td> <td>FNT</td> </tr><tr> <td>Grand Rapids</td> <td>GRR</td> </tr><tr> <td>Kalamazoo-Battle Creek International Airport</td> <td>AZO</td> </tr><tr> <td>Lansing</td> <td>LAN</td> </tr><tr> <td>Saginaw</td> <td>MBS</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Minnesota</span></td> <td><span>MN</span></td> </tr><tr> <td>Duluth</td> <td>DLH</td> </tr><tr> <td>Minneapolis/St.Paul International Airport</td> <td>MSP</td> </tr><tr> <td>Rochester</td> <td>RST</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Mississippi</span></td> <td><span>MS</span></td> </tr><tr> <td>Gulfport</td> <td>GPT</td> </tr><tr> <td>Jackson</td> <td>JAN</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Missouri</span></td> <td><span>MO</span></td> </tr><tr> <td>Kansas City</td> <td>MCI</td> </tr><tr> <td>St Louis, Lambert International Airport </td> <td>STL</td> </tr><tr> <td>Springfield</td> <td>SGF</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Montana</span></td> <td><span>MT</span></td> </tr><tr> <td>Billings</td> <td>BIL</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Nebraska</span></td> <td><span>NE</span></td> </tr><tr> <td>Lincoln</td> <td>LNK</td> </tr><tr> <td>Omaha</td> <td>OMA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Nevada</span></td> <td><span>NV</span></td> </tr><tr> <td>Las Vegas, <i>Las Vegas McCarran International Airport</i></td> <td>LAS</td> </tr><tr> <td>Reno-Tahoe International Airport</td> <td>RNO</td> </tr><tr bgcolor="#d1d1d1"> <td><span>New Hampshire</span></td> <td><span>NH</span></td> </tr><tr> <td>Manchester</td> <td>MHT</td> </tr><tr bgcolor="#d1d1d1"> <td><span>New Jersey</span></td> <td><span>NJ</span></td> </tr><tr> <td>Atlantic City International Airport</td> <td>ACY</td> </tr><tr> <td>Newark International Airport</td> <td>EWR</td> </tr><tr> <td>Trenton</td> <td>TTN</td> </tr><tr bgcolor="#d1d1d1"> <td><span>New Mexico</span></td> <td>NM</td> </tr><tr> <td>Albuquerque International Airport</td> <td>ABQ</td> </tr><tr> <td>Alamogordo</td> <td>ALM</td> </tr><tr bgcolor="#d1d1d1"> <td><span>New York</span></td> <td><span>NY</span></td> </tr><tr> <td>Albany International Airport</td> <td>ALB</td> </tr><tr> <td>Buffalo</td> <td>BUF</td> </tr><tr> <td>Islip</td> <td>ISP</td> </tr><tr> <td>New York, <i>John F Kennedy International Airport</i></td> <td>JFK</td> </tr><tr> <td>New York, <i>La Guardia  Airport</i></td> <td>LGA</td> </tr><tr> <td>Newburgh</td> <td>SWF</td> </tr><tr> <td>Rochester</td> <td>ROC</td> </tr><tr> <td>Syracuse</td> <td>SYR</td> </tr><tr> <td>Westchester</td> <td>HPN</td> </tr><tr bgcolor="#d1d1d1"> <td><span>North Carolina </span></td> <td><span>NC</span></td> </tr><tr> <td>Asheville</td> <td>AVL</td> </tr><tr> <td>Charlotte/Douglas International Airport</td> <td>CLT</td> </tr><tr> <td>Fayetteville</td> <td>FAY</td> </tr><tr> <td>Greensboro</td> <td>GSO</td> </tr><tr> <td>Raleigh</td> <td>RDU</td> </tr><tr> <td>Winston-Salem</td> <td>INT</td> </tr><tr bgcolor="#d1d1d1"> <td><span>North Dakota</span></td> <td><span>ND</span></td> </tr><tr> <td>Bismark</td> <td>BIS</td> </tr><tr> <td>Fargo</td> <td>FAR</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Ohio</span></td> <td><span>OH</span></td> </tr><tr> <td>Akron</td> <td>CAK</td> </tr><tr> <td>Cincinnati</td> <td>CVG</td> </tr><tr> <td>Cleveland</td> <td>CLE</td> </tr><tr> <td>Columbus</td> <td>CMH</td> </tr><tr> <td>Dayton</td> <td>DAY</td> </tr><tr> <td>Toledo</td> <td>TOL</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Oklahoma</span></td> <td><span>OK</span></td> </tr><tr> <td>Oklahoma City</td> <td>OKC</td> </tr><tr> <td>Tulsa</td> <td>TUL</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Oregon</span></td> <td><span>OR</span></td> </tr><tr> <td>Eugene</td> <td>EUG</td> </tr><tr> <td>Portland International Airport</td> <td>PDX</td> </tr><tr> <td>Portland, Hillsboro Airport</td> <td>HIO</td> </tr><tr> <td>Salem</td> <td>SLE</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Pennsylvania</span></td> <td><span>PA</span></td> </tr><tr> <td>Allentown</td> <td>ABE</td> </tr><tr> <td>Erie</td> <td>ERI</td> </tr><tr> <td>Harrisburg</td> <td>MDT</td> </tr><tr> <td>Philadelphia</td> <td>PHL</td> </tr><tr> <td>Pittsburgh</td> <td>PIT</td> </tr><tr> <td>Scranton</td> <td>AVP</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Rhode Island</span></td> <td>RI</td> </tr><tr> <td>Providence - T.F. Green Airport</td> <td>PVD</td> </tr><tr bgcolor="#d1d1d1"> <td><span>South Carolina</span></td> <td><span>SC</span></td> </tr><tr> <td>Charleston</td> <td>CHS</td> </tr><tr> <td>Columbia</td> <td>CAE</td> </tr><tr> <td>Greenville</td> <td>GSP</td> </tr><tr> <td>Myrtle Beach</td> <td>MYR</td> </tr><tr bgcolor="#d1d1d1"> <td><span>South Dakota</span></td> <td><span>SD</span></td> </tr><tr> <td>Pierre</td> <td>PIR</td> </tr><tr> <td>Rapid City</td> <td>RAP</td> </tr><tr> <td>Sioux Falls</td> <td>FSD</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Tennessee</span></td> <td><span>TN</span></td> </tr><tr> <td>Bristol</td> <td>TRI</td> </tr><tr> <td>Chattanooga</td> <td>CHA</td> </tr><tr> <td>Knoxville</td> <td>TYS</td> </tr><tr> <td>Memphis</td> <td>MEM</td> </tr><tr> <td>Nashville</td> <td>BNA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Texas</span></td> <td><span>TX</span></td> </tr><tr> <td>Amarillo</td> <td>AMA</td> </tr><tr> <td>Austin Bergstrom International Airport</td> <td>AUS</td> </tr><tr> <td>Corpus Christi</td> <td>CRP</td> </tr><tr> <td>Dallas Love Field Airport</td> <td>DAL</td> </tr><tr> <td>Dallas/Fort Worth International Airport</td> <td>DFW</td> </tr><tr> <td>El Paso</td> <td>ELP</td> </tr><tr> <td>Houston, William B Hobby  Airport</td> <td>HOU</td> </tr><tr> <td>Houston, George Bush Intercontinental Airport</td> <td>IAH</td> </tr><tr> <td>Lubbock</td> <td>LBB</td> </tr><tr> <td>Midland</td> <td>MAF</td> </tr><tr> <td>San Antonio International Airport</td> <td>SAT</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Utah</span></td> <td>UT</td> </tr><tr> <td>Salt Lake City</td> <td>SLC</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Vermont</span></td> <td><span>VT</span></td> </tr><tr> <td>Burlington</td> <td>BTV</td> </tr><tr> <td>Montpelier</td> <td>MPV</td> </tr><tr> <td>Rutland</td> <td>RUT</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Virginia</span></td> <td><span>VA</span></td> </tr><tr> <td>Dulles</td> <td>IAD</td> </tr><tr> <td>Newport News</td> <td>PHF</td> </tr><tr> <td>Norfolk</td> <td>ORF</td> </tr><tr> <td>Richmond</td> <td>RIC</td> </tr><tr> <td>Roanoke</td> <td>ROA</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Washington</span></td> <td>WA</td> </tr><tr> <td>Pasco, Pasco/Tri-Cities Airport</td> <td>PSC</td> </tr><tr> <td>Seattle, Tacoma International Airport</td> <td>SEA</td> </tr><tr> <td>Spokane International Airport</td> <td>GEG</td> </tr><tr bgcolor="#d1d1d1"> <td><span>West Virginia</span></td> <td><span>WV</span></td> </tr><tr> <td>Charleston</td> <td>CRW</td> </tr><tr> <td>Clarksburg</td> <td>CKB</td> </tr><tr> <td>Huntington Tri-State Airport</td> <td>HTS</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Wisconsin</span></td> <td><span>WI</span></td> </tr><tr> <td>Green Bay</td> <td>GRB</td> </tr><tr> <td>Madison</td> <td>MSN</td> </tr><tr> <td>Milwaukee</td> <td> MKE</td> </tr><tr bgcolor="#d1d1d1"> <td><span>Wyoming</span></td> <td><span>WY</span></td> </tr><tr> <td>Casper</td> <td>CPR</td> </tr><tr> <td>Cheyenne</td> <td>CYS</td> </tr><tr> <td>Jackson Hole</td> <td>JAC</td> </tr><tr> <td>Rock Springs</td> <td>RKS</td> </tr> </tbody>'


parsed_html = BeautifulSoup(html)

leonardscities = [
    # hardcoded values
("dallas", "DFW"),
("portland me", "PWM"),
# ("chicago", "replacethistextwithairportcode"),
("ponce", "PSE"),
("aguadilla", "BQN"),
("fort myers", "RSW"),
("nassau", "NAS"),
# ("houston", "replacethistextwithairportcode"),
("ontario ca", "ONT"),
("bloomington", "BMI"),
("santo domingo", "SDQ"),
("san juan", "SJU"),
("punta cana", "PUJ"),
("st thomas", "STT"),
("guatemala city", "GUA"),
("san jose 3", "SJO"),
("liberia 1", "LIR"),
("orange county", "SNA"),
("montego bay", "MBJ"),
("long island", "ISP"),
("cancun", "CUN"),
("san salvador", "SAL"),
]
c = parsed_html.findAll('tr')
for child in c:
    city = child.findAll("td")[0].text.lower()
    code = child.findAll("td")[1].text.upper()

    leonardscities.append( (city, code) )



def isCity(leonardstext, city):
    if leonardstext == city: return True
    if len(leonardstext) < len(city): return False
    spliced = leonardstext[:len(city)]
    return spliced == city

dups = {}
for (city, code) in leonardscities:
    for i, (o, d) in enumerate(from_to):
        if isCity(city, o):
            if not o in dups:
                dups[o] = set()
            dups[o].add(city)
        if isCity(city, d):
            if not d in dups:
                dups[d] = set()
            dups[d].add(city)

def isRefinedCity(leonardstext, city):
    global dups
    if leonardstext == city: return True

    num_airports_in_city = 1 if not city in dups else len(dups[city])
    return isCity(leonardstext, city) and num_airports_in_city == 1



for (city, code) in leonardscities:
    for i, (o, d) in enumerate(from_to):
        if isRefinedCity(city, o):
            from_to[i] = (code, from_to[i][1])
        if isRefinedCity(city, d):
            from_to[i] = (from_to[i][0], code)
print(len(from_to))

# print(from_to)

# print(dups["detroit"])

frontier_cities = set()
print("[")
for o, d in from_to:
    if o.lower() == o:
        frontier_cities.add(o)
    if d.lower() == d:
        frontier_cities.add(d)

    print(f"    (\"{o}\", \"{d}\"),")

print("]")