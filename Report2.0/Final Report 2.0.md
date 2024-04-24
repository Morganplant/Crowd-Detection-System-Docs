## Introduction
This project revolves around the concept, execution, and evaluation of a crowd density and presence detection system. Utilizing Wi-Fi technology the system aims to determine areas of high crowd density, providing users with information for making informed decision making. The name of this project is "Crowd Pulse".

Users will interact with the system in a way designed to be usable by anyone, this interface will be in the form of a web interface, allowing users, to locate the high density areas, to make informed decisions.

The Crowd Pulse System was designed to facilitate 3 major use cases:
1. Show Students where the busy areas on a university campus are.
2. Identify areas, with low resource allocation, for example a science lab that has low average usage.
3. locate potential security risks, and events such as protests, and gatherings.
### Project Description
This Project was designed to identify busy areas on a university campus, and to allow people to make informed decisions, based on the crowd presence in certain areas, and was specifically designed for the 3 major use cases mentioned above

Crowd Pulse works using two methods:
1. **Network Topology** - When given the Wi-Fi network Topology, Crowd Pulse will identify the areas, that are the busiest.
2. **Scanning** - Crowd Pulse can utilise network scanning techniques, to identify, the crowd density of the network as a whole, as well as identify network infrastructure devices, to avoid confusion.

> [!quote] Objective
The Overall goal of this project is to create a modern and efficient solution for monitoring crowd presence and density in a university campus setting.

Crowd Pulse offers the capability to monitor and analyse historical crowd density data for different locations, allowing users, to identify areas that are busy at certain times of day. This is done by utilising the existing Wi-Fi infrastructure, Other alternative discovery methods where considered, the benefits and drawbacks of which are talked about later in this report.

This Project was Guided by the Project Management Tools and workflows below, which are talked about in more detail in the design and management section of this report:
1. GitHub Project's [1]
2. SMART targets [2]
3. Weekly Project Log
4. Agile and Waterfall Methodologies [3][4]
5. Project Phases and Task Management
### Motivations
My reasoning for creating the Crowd Pulse project was threefold
1. I wanted to test my abilities and Problem Solving Skills in a meaningful and challenging way.
2. I wanted to minimize the impact of a potential Isolation incident after the wake of the COVID-19 pandemic.
3. I wanted to locate busy areas around the campus, either to avoid those areas for quiet study time, or to specifically seek them out to engage the people there.

I wanted to develop a system that would also be a great advantage to avoid queues in stores, cafes, and other areas. It would allow users to locate busy areas and then be able to plan around that new data, There is no such system that helps in this regard hence why I thought it might provide an interesting and challenging problem to solve.
### Ethics
During the development of Crowd Pulse it was important to me that I not cross any ethical boundaries, and made sure to keep this thought throughout the entirety of the project, I wanted to be mindful of the privacy and data security of those being monitored.

#### Privacy & Data Security
Due to the nature of the project I knew that it may involve the privacy of individuals and decided that I would only collect only the bare minimum amount of data to enable crowd pulse's functionality as I knew it might raise privacy concerns.

Given the nature of a system that collects and analyses user data, ensuring the security and integrity of the data is of utmost importance, as such Crowd Pulse will endeavour to use the minimal amount of user data possible to ensure there is no useful way for Crowd Pulse to be used to track individuals.

During the Project I decided that I would not use live public data, and would generate my own synthetic data, to avoid infringing on people's privacy and security.

### Things learned during the project

During the Project I learnt more about networking, how to manage a project, and efficiently manage my time.
- I discovered that network topology was unknowable as a "user device"
- I discovered that an easier way to implement this would be to change the specific network architecture to divide areas into different subnets, for example, the library building is on subnet 3 and the student union building is on subnet 4.
- I discovered that the process of MAC Address Swapping has changed in recent years [5]
- I realised that Scanning a network using a large network range class, requires more time or should be parallelized [6]
### Professional Considerations
Throughout the development and future deployment of a System such as Crowd Pulse, it is and was essential to uphold professional standards, best practices and ensuring the quality and reliability of the Crowd Pulse System.
### Project Scope
The scope of the Crowd Pulse project encompasses the design and development of a crowd density, presence detection system within a university campus settings.

Moreover, the project scope extends to considerations of scalability and adaptability, ensuring that the system can be tailored to different university areas and potentially extended to other public spaces. The project will also delve into the integration of security and privacy measures, ethical and legal compliance, and the potential for future enhancements and expansions of the system. Clear delineation of the project scope is fundamental to aligning expectations, resources, and deliverables throughout the development and implementation phases.
## Problem Description
### What is the Problem?

The Crowd Pulse Project aims to solve 3 problems; Crowd Monitoring, Effective Resource Allocation and Security of Campus Safety.

This Project's aim is to develop an efficient monitoring solution for crowd density, across a university campus. This System is capable of providing insight into, resource utilisation and Crowd Density. This is done by using the existing Wi-Fi infrastructure to show busy locations in a campus environment.
#### Project Focuses
The **Primary Focus** as Stated above is the Crowd Monitoring System. The Aim is to get valuable insights into the typical movements of crowd behaviour, using the crowd density variations throughout the day, this understanding would empower the campus staff, security and students to make informed proactive decisions such as:
- Deciding what time to get lunch, study etc.
- When to Go to bars and cafes to either maximise or minimize exposure to people
- Redirect equipment to areas with more use
- Event coordination
- Individual Time scheduling
- Correlation with lectures attendance
Ultimately, the overarching objective is to gather data about the crowd density on a university campus.

The **Secondary Focuses** are *Resource allocation* and *improvements to Safety*, which can be improved by first identifying areas that are busy and those that are not, with this data Staff can then make better decisions on what to do during events or where to allocate more resources. It could be used during open days to show where the most popular areas for new students is, or show the most popular university housing areas.

#### Safety and Security - Secondary Focus

Enhancing safety and security is a core aspect of this project. Crowd Pulse has the potential to significantly augment campus security infrastructure. By providing information on crowd activity across campus, the system empowers security personnel to quickly identify and address potential security issues. Additionally, it allows proactive monitoring of high-traffic areas, enabling pre-emptive safety measures. With data visualization, security teams can strategically allocate resources, optimize patrol routes. Overall, integrating this system not only fortifies campus security but also cultivates a proactive safety culture, prioritizing the well-being of students, faculty, and staff.
### How Does Crowd Pulse Solve this?
As explained earlier Crowd Pulse Aims to solve and improve the following:
- Crowd Monitoring
- Effective Resource Allocation
- Security of Campus Safety

Crowd Pulse Does this by utilising two methods:
1. Scanning method
2. Topology method

In the scanning method, crowd pulse scans the Wi-Fi network to identify the crowd density of the network which can then be down to the user.

In the topology methodology, crowd pulse uses it's knowledge of the Wi-Fi network topology to identify the crowd density of different locations, determined by the Wireless Access point.
### Has it been done before
Crowd Pulse is not the first in this project space, there are many projects that revolve around crowd monitoring and the analysis of that data. However these systems often use different methods to capture the crowd presence data, such as:
- Computer Vision
- Weight Monitoring (mostly used on trains)
- IoT Sensors
- Body Heat Detection

Using These methods can be inefficient as shown with the problems below:
- Computer vision requires that cameras be set up at all the exits and entrances, as well as expensive software to identify people and monitor when unique people enter and exit buildings.
- Weight monitoring requires that all people are of similar weights to identify how many people are in an area, this is not always the case as children do not weigh as much as adults, and the weight variability between adults is large, and so there is not an accurate way of measuring crowd density, this method also requires having weight sensors setup everywhere.
- IoT sensors, depending on the implementation it can be a good way of identifying people, but it requires lots of small devices to be placed around an area for monitoring, which all require power and a way to get that data out of the device.
- Body Heat systems, can be thrown off by large heat sources and so are not a good indication of crowd density, it is also hard to generate crowd density values if there is a large crowd if the crowd is packed tightly together, so heat sources are not easy to distinguish.
#### Why is Crowd Pulse Better?
Crowd Pulse utilises the existing network topology, supplemented with scanning techniques, that allow the system more accuracy than the techniques listed above, it uses the network topology available to determine areas based on active device counts. However that being said Crowd Pulse has it's own faults, such as if the network goes down, then there is no data to analyse.
### Why is this being solved?
After the COVID-19 pandemic there is a need to address the problem of crowd detection, this project is an important step towards a solution that can prevent another isolation period. It serves as a critical element in bolstering safety measures around campus grounds, by identifying high-density areas susceptible to potential safety hazards, like overcrowding.

The main goals and aims of this project align closely with what academic institutions aim for, such as:
- promoting student well-being
- improving operational efficiency
- creating an environment that fosters learning
By allowing anyone to see a the crowd density and presence values, Crowd pulse doesn't just make administrative work easier but also gives students and faculty the power to make smart choices about where they go on campus. This makes everyone feel more connected and collaborative, adding to the project's importance beyond just the technical side.

To sum up, Crowd pulse stands out as a solution that not only tackles the challenges faced by university campuses but also embodies the spirit of technological innovation and collaborative effort. Its ability to transform campus management practices and enhance the overall campus experience firmly establishes it as a project of interest and value within the realm of higher education.
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
Crowd Pulse utilizes the pre-existing Wi-Fi network to get the crowd density of particular areas, this is stored, so that users can see the historical data for locations around an area such as a university campus, to help with campus security, day to day scheduling, as well as space and resource allocation.

The Crowd Pulse project aims to modernize the campus, by utilising WI-FI crowd detection, to create a solution to monitoring crowd presence and density on the university campus. Utilising this would be beneficial to the university, Staff, students, and administration.
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
## Ethics
### Laws That May Apply

In this section I talk about the Laws that may or may not apply to the project, I outline which Laws and guidelines might provide issues with the project if any and which laws and guidelines may not apply, and what I did about it.
#### GDPR
The General Data Protection Regulation (GDPR) isa legislation by the EU and EEA aimed at protecting individuals' personal data rights, it was enacted in April of 2016. It governs data processing, protection, ensures transparency, and confidentiality.

GDPR, or the General Data Protection Regulation, is a set of laws designed to protect the privacy and personal data of individuals. It aims to ensure that personal data is processed transparently and fairly, while also giving individuals more control over their own data[13].

GDPR grants data subjects some of the following rights:
1. **Right of Access** - To know if your data is being processed and access to it.
2. **Right to Rectification** - Allows you to request the rectification of inaccurate or incomplete data.
3. **Right to Erasure** - Allows you to request the removal of your data.
These rights are designed to empower individuals to have more control over their own personal data and it's use. Essentially GDPR is about providing a better safeguard for people's personal information in today's digital age.

Due the the project's nature it could be speculated that the project uses, personal data to achieve the monitoring of people. However I made a conscious decision to avoid using as much personal information as possible, the only data collected is the number of devices under a specific wireless access point, and there is no use of personally identifiable data.

However, the Crowd pulse system does collect potentially identifiable data:
- MAC addresses - used only to identify the device vendor
- Device IP address - used to identify unique devices
- Device Name - used to check if the device is of a specific model / make
This data is only used to identify vendors, to disregard networking infrastructure devices.
#### DPA
The 2018 Data Protection Act or DPA serves to update and modernize data protection laws within the UK, aligning them with the GDPR of the EU. The act regulates the processing of personal data and lays down rules regarding how organizations collect, handle and store personal data[14].

The act applies to 'Personal Data' which refers to information that relates to individuals. It empowers individuals with rights similarly to how GDPR does so. The act establishes a regulatory framework for data protection enforcement and designates responsibilities to the ICO (information Commissioner's Office) to oversee compliance.

As Stated Earlier Crowd Pulse only collects identifying data, for the prepose of removing networking infrastructure devices from the crowd density.
#### ICO Guidance
As mentioned earlier the ICO or Information Commissioner's Office can provide guidance on data protection laws and regulations, including GDPR compliance.
These laws and regulations make sure that crowd monitoring projects involving Wi-Fi scanning techniques comply with legal requirements, respect individuals' privacy rights[15].
### BCS Code of Conduct
BCS stands for (British Computer Society), this section is about the BCS code of conduct and outlines the professional standards and guidelines that members of the BCS are expected to adhere to in their practice. It provides a framework for promoting and maintaining high standards of competence, integrity, and professionalism within the field of computing[16]. The code of conduct, addresses various aspects such as:
- confidentiality
- respect of privacy
- and responsible use of technology
#### Code of Conduct

> [!quote] Section 1 - Public Interest
> You shall:
> 1. have due regard for public health, privacy, security and wellbeing of others and the environment.
> 2. have due regard for the legitimate rights of Third Parties.
> 3. conduct your professional activities without discrimination on the grounds of sex, sexual orientation, marital status, nationality, colour, race, ethnic origin, religion, age or disability, or of any other condition or requirement.
> 4. promote equal access to the benefits of IT and seek to promote the inclusion of all sectors in society wherever opportunities arise.
[16]

> [!quote] Section 2 - Professional Competence and Integrity
> You shall:
> 1. only undertake to do work or provide a service that is within your professional competence.
> 2. NOT claim any level of competence that you do not possess.
> 3. develop your professional knowledge, skills and competence on a continuing basis, maintaining awareness of technological developments, procedures, and standards that are relevant to your field.
> 4. ensure that you have the knowledge and understanding of Legislation\* and that you comply with such Legislation, in carrying out your professional responsibilities.
> 5. respect and value alternative viewpoints and, seek, accept and offer honest criticisms of work.
> 6. avoid injuring others, their property, reputation, or employment by false or malicious or negligent action or inaction.
> 7. reject and will not make any offer of bribery or unethical inducement
> [16]

> [!quote] Section 3 - Duty to Relevant Authority
> You shall:
> 1.  carry out your professional responsibilities with due care and diligence in accordance with the Relevant Authority’s requirements whilst exercising your professional judgement at all times.
> 2.  seek to avoid any situation that may give rise to a conflict of interest between you and your Relevant Authority.
> 3.  accept professional responsibility for your work and for the work of colleagues who are defined in a given context as working under your supervision.
> 4.  NOT disclose or authorise to be disclosed, or use for personal gain, or to benefit a third party, confidential information except with the permission of your Relevant Authority, or as required by Legislation.
> 5.  NOT misrepresent or withhold information on the performance of products, systems or services (unless lawfully bound by a duty of confidentiality not to disclose such information), or take advantage of the lack of relevant knowledge or inexperience of others.
> [16]

> [!quote] Section 4 - Duty to the Profession
> You shall:
> 1. accept your personal duty to uphold the reputation of the profession and not take any action which could bring the profession into disrepute.
> 2. seek to improve professional standards through participation in their development, use and enforcement.
> 3. uphold the reputation and good standing of BCS, the Chartered Institute for IT.
> 4. act with integrity and respect in your professional relationships with all members of BCS and with members of other professions with whom you work in a professional capacity.
> 5. encourage and support fellow members in their professional development.
> [16]

I believe that I have upheld the BCS code of conduct during the development of Crowd Pulse. Once again the crowd pulse project only utilises the following data, to specifically remove networking infrastructure the crowd data:
- **MAC addresses** - used only to identify the device vendor to remove networking devices
- **Device IP address** - used to identify unique devices
- **Number of Devices** - used to create crowd density values
### Privacy Considerations / Concerns of the Project

#### Ethical Issues / Considerations

During the Crowd Pulse Project it was important to me that I consider the ethical implications and concerns before implementing a system like this. Due to the nature of the Crowd Pulse project it involved monitoring and analysing crowd presence and density in different locations, this could potentially raise privacy concerns among the individuals being monitored, therefore it was important to me that I decide on what is acceptable and what was not:
**Acceptable**
- Aggregated and anonymized data collection to ensure individual privacy is maintained
- Utilizing technology that focuses on crowd presence and density rather than individual identification
**Un-Acceptable**
- Collecting and storing personally identifiable data for the purpose of tracking individuals.
- Utilizing surveillance methods that infringe on privacy rights
- Using Live Data during the development process
##### Data Security
Given the nature of the system I wanted to ensure that the data being stored and used did not have any meaningful way of identifying individuals, Outlined below is the strategy I used to keep the data stored safe and secure.
1. **Data Minimization**: Crowd Pulse will limit the collection of personal data to only what is necessary for the system's functionality, ensuring that the least amount of identifiable information is gathered. This aligns with privacy principles and reduces the risk associated with unnecessary data storage.
2. **Encryption and Anonymization**: Any data that is collected will be encrypted and anonymized to prevent unauthorized access and to ensure that individual identities cannot be discerned from the stored information.
3. **Compliance with Data Protection Regulations**: Crowd Pulse will adhere to all relevant data protection regulations, ensuring that the handling and storage of user data complies with legal requirements to safeguard user privacy and security.
