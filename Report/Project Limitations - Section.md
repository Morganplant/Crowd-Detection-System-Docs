In the development phase of my project, I encountered several limitations that posed potential challenges to its functionality and effectiveness. These obstacles ranged from technical constraints like unpredictable network topologies to practical concerns such as overlapping IP addresses and vendor MAC rotations.

### Unknowable topology

One notable limitation was the unpredictable topology of the network, which complicated the accurate monitoring and management of network classes and devices. To address this issue, I implemented two methods, the first a dynamic discovery mechanism. This mechanism scans the network for new devices, ensuring updates to the database. The Second Method was allowing a user to supply the program with the network topology, allowing for enhanced functionality.

### Network range class

Another significant obstacle I faced involved the network range classes, which occasionally led to overlapping IP addresses and difficulties in device identification. To mitigate this challenge, I opted for CIDR notation. This allowed me to precisely define the IP address range for each network class, facilitating clear differentiation and accurate device tracking.

### Mac Address Rotation

Additionally, I grappled with the challenge posed by vendor MAC rotations, which jeopardized device identification due to the constant shuffling of MAC addresses. While considering potential solutions, I meticulously weighed the costs and benefits of implementing Machine Learning algorithms to automatically detect and adapt to MAC rotations. After thorough deliberation, I made a conscious decision not to pursue this particular problem. This determination stemmed from the realization that other facets of the project held greater significance, and diverting resources to address this issue would detract from those priorities. Instead, I chose to bolster the existing strategy by concentrating on consistently updating the database with known vendor MAC addresses and their corresponding device types. This proactive approach yielded positive results, ensuring steadfast and accurate device identification, even amidst MAC rotations.

### Real-time

Another Limitation that I ran into during development was the aspect of real-time data, initially the plan included real-time data analysis, however due to the time required for scanning or processing the network topology, real-time data became much harder to implement, due to this I decided, that it would be better to focus on the other aspects of the project and use timed intervals, much like other projects of this type, for example the Bridgton and Hove Bus app, which uses time intervals, to refresh the data, they use a time delay of 10s for a live map refresh, this allows time for the processing and provides the user with a relatively quick data refresh[22].

Despite facing a multitude of challenges, I effectively implemented solutions to mitigate their impact, ensuring the seamless operation of my network management system. Through meticulous planning, strategic decision-making, and diligent execution, I navigated through complexities and upheld the integrity of the network infrastructure. This accomplishment serves as a testament to my unwavering dedication and proficiency in overcoming obstacles and delivering optimal results.

### What does the project do vs initial plan for project
