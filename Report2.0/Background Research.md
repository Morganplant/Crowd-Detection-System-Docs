## Background Research
### What other Projects exist?

There are many ongoing projects exploring innovative, technologies for crowd monitoring. The tools mentioned below primarily utilize technologies like Wi-Fi tracking, Bluetooth signals, and video analytics. 
#### Existing Projects

##### TALLYFI
![[Pasted image 20240404172645.png]] [7]
TallyFi is a system designed to be an advanced people counting system, specifically designed for crowded areas, such as nightclubs, bars, and other larger venues. TallyFi's system aims to maximise capacity and give insights into customer throughput. [7]

The TallyFi System consists of a singular counting device as shown above with an OLED display, count keys, these devices can communicate to each other and a central server allowing for real-time data tracking. Viewable through the central server's dashboard as shown below:
![[Pasted image 20240404172759.png]] [7]
TallyFi can provide organizers with valuable data on crowd patterns, peak hours and popular event areas. it enables event planners to take a proactive measures such as adjusting the layout, redirect attendees to less crowded zones, or deploying additional staff to specific zones.
###### Pros
1. **Real-Time Data Access** - Users can access real-time crowd counts and monitor venue capacity through the online dashboard, enabling timely decision-making and resource allocation.
2. **User-Friendly Interface** - TALLYFI devices feature a simple and robust design with an OLED display and intuitive button controls, making them easy to operate even in busy environments.
###### Cons
1. **Wi-Fi Dependency**: The system relies on Wi-Fi connectivity, which may pose challenges in areas with poor signal strength or unreliable network conditions, potentially affecting data accuracy.
2. **Initial Setup Complexity**: Configuring devices and setting up venues may require a learning curve for users, especially those unfamiliar with the system, potentially delaying implementation.
3. **Hardware Reliability**: In cases of hardware malfunctions or unresponsiveness, troubleshooting may require technical expertise or contacting customer support, leading to potential downtime in crowd monitoring operations.

##### CROWDCONNECTED

CROWDCONNECTED specializes in providing location software for mobile tracking and analytics. Their solutions offer scalable and affordable people tracking capabilities, allowing businesses and organizations to efficiently monitor the whereabouts of individuals in real-time. They utilize mesh networking IoT technology from Wirepas to enable accurate tracking over entire buildings using low-cost battery-powered beacons[8].

![[Pasted image 20240404180114.png]] [8]
###### Pros:
1. **Real-Time Tracking:** CROWDCONNECTED's solution provides real-time tracking of people's locations, enabling safe and efficient operations.
2. **Versatile Applications:** It can be utilized across various sectors including healthcare, education, events, and security, making it suitable for a wide range of applications.
3. **Mesh Networking Technology:** The use of mesh IoT networking technology from Wirepas allows for accurate tracking over entire buildings using low-cost battery-powered beacons.
###### Cons:
1. **Dependency on Battery Power:** Since the solution relies on battery-powered beacons, there may be a need for regular maintenance to replace batteries, which could incur additional costs and effort.
2. **Limited Range of Mesh Networking:** While mesh networking technology offers advantages in coverage, it may still have limitations in extremely large or complex environments.
3. **Maintenance Requirements:** Regular maintenance and monitoring may be necessary to ensure the system operates effectively and remains up-to-date with evolving technology and security standards.
##### POINTR
POINTR is a location-based services platform that offers crowd-tracking and analytics capabilities for event organizers. It utilizes Bluetooth Low Energy (BLE) beacons and smartphone sensors to monitor attendee movement, generate heatmaps, and measure dwell times within the event venue. It works by using BLE beacons strategically placed throughout an event venue to capture attendee movement accurately. The platform then analyses the data collected to provide crowd behaviour, such as popular areas, engagement levels, etc. Additionally similar to CrowdConnected, it uses a heatmap to visualize the attendee behaviour, showing concentration and engagement in a venue [9].
![[Pasted image 20240404180422.png]] [9]
###### **Pros:**
1. **Real-time crowd monitoring and analysis:** Provides organizers with valuable insights into crowd patterns and behaviour in real-time.
2. **Indoor positioning technology:** Offers accurate data collection for crowd analysis, enabling better decision-making.
3. **Heatmap visualization:** Helps organizers visualize attendee behaviour and identify popular sections within the venue.
4. **Integration with event management systems:** Allows seamless integration with existing event management tools for efficient data management.
###### **Cons:**
1. **Potential complexity for setup and calibration:** May require technical expertise for setup and calibration of BLE beacons.
2. **Limited features specifically for crowd monitoring:** May lack advanced features compared to some other crowd monitoring tools.
3. **Potential limitations for very large-scale events:** Might face challenges in accurately monitoring and analysing crowd behaviour in extremely large events.
4. **Higher pricing compared to some other tools:** May have higher costs associated with its usage compared to alternative crowd monitoring solutions.
##### SIGHTCORP - CROWDSIGHT
![[Pasted image 20240405080947.png]] [10]
Crowd Sight is a cutting-edge facial analysis tool designed specifically for event crowd monitoring. Leveraging advanced AI-powered algorithms, Crowd Sight analyses real-time video feeds to extract valuable insights into crowd demographics, emotions, and behaviour. By tracking the faces of individuals within a crowd, Crowd Sight provides event organizers with crucial data on attendee engagement, sentiment, and crowd density, enabling them to optimize crowd management strategies and ensure a safe and memorable event experience [10].
##### **Pros**
1. **Real-time** - Crowd Sight offers real-time insights into attendee behaviour and crowd dynamics, allowing event organizers to make informed decisions on the spot.
2. **Facial Recognition** - With facial recognition capabilities, Crowd Sight provides detailed demographic profiling, including age ranges and gender distribution.
3. **Customizable Metrics** - Event organizers can tailor metrics and reporting according to their specific needs, enabling more personalized analysis.
4. **Integration with External Management Systems** - Crowd Sight seamlessly integrates with existing event management systems, facilitating streamlined data management and analysis processes.
###### **Cons**
1. **Privacy Concerns** - The use of facial recognition technology may raise privacy concerns among attendees, requiring careful consideration of data protection regulations.
2. **Limited Features** - While Crowd Sight excels in facial analysis, its features for crowd management may be comparatively limited when compared to other tools.
3. **Higher Pricing** - Crowd Sight may come with a higher price tag compared to some alternative crowd monitoring solutions, which could be a deterrent for budget-conscious event organizers.
4. **Complex Setup Process** - Implementing Crowd Sight may require some level of setup and configuration, which could pose challenges for users with limited technical expertise.

##### DIVA
DIVA stands for (Distributed Intelligent Video Analytics), which is a solution designed to streamline crowd management within railway stations and on-board trains. By leveraging the existing CCTV infrastructure, DIVA employs real-time video analysis, to measure passenger density. DIVA uses a color-coded system (red, yellow and green), DIVA guides passengers to areas with lower density, minimising congestion [11].

![[Pasted image 20240405081432.png]] [11]
###### **Pros**
1. **Enhanced Safety** - DIVA improves passenger safety by facilitating smooth movement and minimizing congestion.
2. **Optimized Flow** - By guiding passengers to less crowded areas, DIVA helps optimize passenger flow and reduce dwell times.
3. **Existing Infrastructure** - DIVA utilizes the existing CCTV network, minimizing the need for additional sensors and infrastructure.
4. **Real-time** The system offers real-time monitoring of passenger density and security threats, enabling prompt response to incidents.
5. **Security** - DIVA's ability to detect unattended luggage and trespassing enhances security within railway stations and trains.
###### **Cons**
1. **High Costs** - Implementing DIVA may involve initial costs for setup and integration with existing systems.
2. **Maintenance Requirements** - Regular maintenance and updates may be necessary to ensure optimal performance of the system.
3. **Privacy Concerns** - The use of video analytics for monitoring passengers may raise privacy concerns among some individuals.
4. **Technical Issues** - Like any technology, DIVA may encounter technical glitches or downtime, affecting its effectiveness.
5. **Training Needs** - Staff may require training to effectively utilize DIVA and interpret its data for decision-making.
##### Situate Project
The Situate project integrates Lidar-based crowd monitoring with AI technology to enhance safety and improve the passenger experience at Bristol Temple Meads train station. Using Lidar sensors, Situate tracks real-time potentially hazardous activities like individuals near platform edges, alerting operators swiftly. With wide coverage from a single sensor, it ensures comprehensive monitoring [12].

![[Pasted image 20240405082125.png]] [12] 
###### **Pros:**
1. Enhanced passenger safety: The Situate project employs AI and Lidar technology to proactively identify and address potential risks, thereby enhancing overall safety for passengers at Bristol Temple Meads train station.
2. Real-time incident detection: Utilizing AI, the system can detect incidents and concerning activities in real-time, enabling swift intervention by station operators to prevent accidents or escalations.
3. Comprehensive monitoring: With the ability of a single sensor to cover large distances, Situate ensures comprehensive monitoring of the station premises, reducing blind spots and enhancing security measures.
4. Improved passenger experience: By contributing to a safer and more secure environment, Situate aims to improve the overall passenger experience at the train station, potentially leading to increased satisfaction and loyalty among commuters.
###### **Cons:**
1. **Privacy concerns** - The use of AI-powered surveillance for crowd monitoring may raise privacy concerns among passengers, as it involves the collection and analysis of personal data, potentially infringing on individual privacy rights.
2. **Implementation challenges** - The implementation of the Situate project may pose challenges such as initial setup costs, system calibration, and ongoing maintenance requirements, which could impact its efficiency and effectiveness.
3. **Dependency on technology** - As the Situate system heavily relies on technology for crowd monitoring and incident detection, any technical glitches or malfunctions could compromise its ability to ensure passenger safety and security.
4. **Potential resistance or scepticism** - Some passengers or stakeholders may express resistance or scepticism towards the deployment of advanced surveillance technologies like Situate, citing concerns over surveillance culture or distrust in AI-based systems.

### What does Crowd Pulse do?

---
The Situate project integrates Lidar-based crowd monitoring with AI technology to enhance safety and improve the passenger experience at Bristol Temple Meads train station. Using Lidar sensors, Situate tracks real-time potentially hazardous activities like individuals near platform edges, alerting operators swiftly. With wide coverage from a single sensor, it ensures comprehensive monitoring [12].

---

Crowd Pulse utilizes the pre-existing Wi-Fi network to get the crowd density of particular areas, this is stored, so that users can see the historical data of 




---


Crowd Pulse uses the existing Wi-Fi infrastructure to capture data on high density locations, to help with campus security, day to day scheduling, as well as space and resource allocation. Despite the project's potential to enhance safety, security and efficiency, I encountered challenges such as, the privacy concerns of a system that monitors people, nonetheless the system holds promise for streamlining campus management processes and fostering a safer environment for students and staff.

The Crowd Pulse project aims to modernize the campus, by utilising WI-FI crowd detection, to create a solution to monitoring crowd presence and density on the university campus. Utilising this would be beneficial to the university, Staff, students, and administration.

Crowd Pulse Has Limitations, however without an exported network topology the system is heavily handicapped, and is only able to produce crowd density information for the entire network and not specific locations. This is due to how a network topology is unknowable and cannot be discovered by a "user device" (in this case a user device is a device connected to a network but does not have access to the network topology examples include; phones, laptops, Personal Computers, etc.)

Crowd Pulse if given the network structure, can identify "personal" devices in a much more refined way, meaning that instead of just generating a single crowd density for an entire campus, it can pinpoint Wireless Access points and use those to generate crowd density values, meaning that a much more localised crowd density value can be generated and used for analysis and historical data tracking.
##### Wide scanning technique
###### Pros

- Modernizes campus monitoring by leveraging advanced technology.
- Offers a comprehensive solution for monitoring crowd presence and density.
- Benefits various stakeholders including university staff, students, and administration.
###### Cons

- Limited by its status as a "user device," lacking knowledge of the network structure.
- Can only detect "personal" devices for the entire network, not individual areas.
##### Network Topology Access

###### Pros

- Enables a much more refined identification of "personal" devices.
- Allows pinpointing of Wireless Access Points for generating crowd density values.
- Provides a more localized crowd density value, enhancing accuracy and precision.
###### Cons
- Requires access to the network structure, potentially posing logistical challenges.
- May necessitate additional resources and permissions for implementation.
- Dependency on network structure for effectiveness, potentially limiting flexibility.