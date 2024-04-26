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
## Design and Project Management
### Diagrams
> [!abstract]- User Flow Diagram
>![[Pasted image 20240405132323.png]]

> [!abstract]- Entity Relationship Diagram
> ![[Pasted image 20240405132406.png]]

> [!example]- Example Network Topology map
> ![[Pasted image 20240405132952.png]]
> ![[Pasted image 20240425021551.png]]

### How the Project is managed
I used a multitude of different ways to manage my project. For source control and backups, I used GitHub [1], my oracle cloud instance [17], and Google Drive [18]. Using GitHub allowed me to utilize GitHub issues and projects, which allowed me to track tasks easily, an example of which was the Kanban board below. I used my Google Drive as well as my own server to store backups periodically to avoid backup loss if something were to happen to GitHub. This way, I had a higher degree of redundancy baked into the project.
#### Kanban
![[Pasted image 20240405140730.png]]

#### Requirements Analysis
In the Following Section I will go through some of the functional and non-functional requirements, I though where important to Crowd Pulse during development. I will cover which requirements I viewed as mandatory, which I viewed as Desirable, and reasoning for not completing some of them.
##### Functional Requirements
###### Device Detection
1. The System must employ a method that relies on IoT Devices or Wi-Fi Functionality
2. It should be capable of monitoring the crowd density in multiple sub areas, or producing crowd density data for an entire area
###### Real-Time Data Collection & Analysis
- Implementing real-time data collection and analysis to provide immediate insights into crowd density, would be a great bonus to the project, but near real-time data would suffice
- Ideally the system should be responsive and provide timely information
###### Integration with Existing Infrastructure
- Seamless integration with the university's existing systems would be extremely useful in providing easy access to the users
- Compatibility with current systems would allow for a more efficient solution
###### User Experience & User Interface (UX and UI)
- Designing and developing a user-friendly interface (web app) for visualising the data would enhance the experience of the users greatly
###### Scalability and Historical Data
- The system must be easily expandable to cover multiple sub areas
- The System should store some historical data of some kind to draw from to do trend analysis
- The system should enable users to access historical insights
##### Non-Functional Requirements
###### Privacy and Security
- The system must adhere to the privacy principles set out by the university and the BCS, collecting and only aggregating anonymized data
###### Usability
- The user interface should have a design that is easy to understand and navigate
- Features should be logically organized for convenience
- Providing customizable views and filter options to cater to different user preferences
- Ensure that the interface is accessible to users with diverse needs
- Implementing a feedback mechanism for users to report issues or provide suggestions
#### Planning
##### Initial Proposal and Requirements Analysis
Crowd Pulse began with the creation of a comprehensive project proposal. This proposal outlined the project's objectives, scope, and deliverables. Following this, an analysis of requirements was done to identify the specific areas for successful completion. This initial phase laid the groundwork for the project's planning and execution.
##### Development of Project Plan
With a clear understanding of the project's goals, I developed a plan. This plan detailed the tasks, timelines and milestones, giving me a roadmap for the project's progression, though this was not always accurate, the initial project planning was outlined by the Gantt chart below:
![[Pasted image 20231123123439.png]]
##### Execution and Monitoring
Throughout the project, I followed the established project plan and when I encountered Limitations and unforeseen setbacks, changed the plan, timelines and milestones. I decided to have regular self-assigned checkpoints, where I would evaluate my progress and decide what was best for the project, these checkpoints often included talks with my academic advisor, but not always, as shown in the <mark style="background: #FF5582A6;">Project Log section in the appendences.</mark> This proactive approach ensured that the project remained on track toward successful completion, equipping me with valuable practical skills in project management.

> [!warning] Remove Highlighting
#### Kanban
![[Pasted image 20240405140730.png]]
#### Project Plan
During the initial Steps of the project it was important to establish a planned methodology. As I have worked with different methodologies before, namely agile, waterfall and scrum [3] initially I decided I would use a waterfall method, as described by the Gantt Chart shown previously, after the waterfall methodology did not work as well as I had hoped due to setbacks, I chose to implement the Agile methodology as shown by the diagram below:
![[Pasted image 20240405141209.png]]
[3]

After moving to the agile development process, the workflow became easier to manage, it allowed me to work on developing Crowd Pulse, and create sub prototypes (a prototype of a specific section), which greatly improved my efficiency.

The Crowd Pulse Project was guided by utilizing SMART targets / goals, these allowed me to have a more streamlined development workflow, in this instance SMART [2] refers to a way of setting objectives that are:
1. Specific
2. Measurable
3. Achievable
4. Relevant
5. Time-based
Some of these SMART targets included:
- Achieve 60% accuracy rate in identifying crowd density in testing data using scanning techniques.
- Identify and prioritize 3 high traffic areas within the test data.
- discover 4 low density areas, within the testing data.
- Identify and designate 3 campus zones with consistently high crowd density levels
##### Project Phases
As described above in the Gantt Chart of the initial project plan which I developed using Team Gantt [19] a reliable Gantt chart creation tool, the process of creating Crowd Pulse was done in phases, these phases are shown in the Gantt Chart, as well as the agile methodology example but to go over them again they are:
- **Ideas / Research Phase**
	- In this phase I was focused on generating ideas, backed by research, and developing those ideas rather than creating anything, this also held the start of the project planning.
- **Design Phase**
	- During This phase I was focused on furthering the ideas that held the most substance, and started to create diagrams of how these ideas would function and create the flow of the system. this is where the bulk of the planning, designing prototypes and diagrams happened.
- **Implementation / Coding**
	- During this Phase I started coding the prototype ideas, and picking which systems to use, using the agile methodology here has beneficial as it allowed me to refine my prototypes, and allowed my designs to become better.
- **Testing**
	- In this phase I tested the system, I was guided by my academic advisor as well as, my own targets, to avoid testing in a live environment, but create synthetic data that would simulate way a live environment would behave
- **Deployment**
	- This was a mostly theoretical project stage as I decided before that deployment into a live environment would pose security and privacy concerns already mentioned.
##### Source Control - GitHub & GiTea
I used GitHub, as well as my own self hosted version GiTea, on a VPS (Virtual Private Server on my oracle instance) on my cloud instance. GiTea, is a selfhosted alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in Go it works across all the platforms and architectures that are supported by Go[20]. For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down or corrupt in some way.
###### Project / Issue Management
GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be used it for this exact purpose, in The Planning Section I showed an image of the Kanban View of this tool.

## Implementation
### How Crowd Pulse Works

Crowd Pulse's Scanning Technique is built around a program named Nmap. Nmap (or Network Mapper) is a robust network auditing tool, that is used for network exploration and security auditing. It's functions by leveraging IP (internet Protocol) packets to identify hosts (devices on a network), then by analysing these packets it can provide information on these hosts [21], below are some examples of what kind of scans can be done:
- **Host Discovery** - This shows basic information about hosts on a network.
- **Port Scanning** - This shows information on the ports that different hosts have open.
- **OS Detection** - This shows information on the ports scanned, and uses probabilities to determine what OS the host devices are using.
By discovering devices, detecting OSes and scanning ports, we can identify which OS a device is likely to be using, which is useful in removing network architecture from our data.

Crowd Pulse Relies on the following 3 Assumptions:

> [!warning] Assumption 1 - All members of a crowd **will** have a discoverable device
> This is because if a crowd member does not have a discoverable device, then it is impossible to log their presence in the crowd using Crowd Pulse.

> [!warning] Assumption 2 - All members of a crowd will have their device connected to the local Wi-Fi
> This is a "safe" assumption because the Local Wi-Fi enables the Staff and Students to utilize university resources, such as Computer and Study Space booking, etc.

> [!warning] Assumption 3 - Members of a crowd will have only 1 device connected to the local Wi-Fi at a time
> This is due to the fact that there would be simply too many devices to sort through which, would inflate the crowd density artificially.

Crowd Pulse was designed with these assumptions in place, to allow me to develop a much simpler system than otherwise required. Without these assumptions It would require more work, to determine an accurate crowd density value for areas, where there are likely to be more devices per person, for example a lecture theatre in use.

Crowd Pulse Works by first checking the permissions it has
- If Crowd Pulse has access to the network topology then it is able to identify the areas with the highest crowd density values, this can then be applied to an interface in which a user would more easily understand this data.
- If Crowd Pulse does not have the network topology then it can only generate the crowd density for the entire area (Wi-Fi network) which significantly limits it's functionality.
The system captures data to pinpoint areas with high crowd density, facilitating optimal resource allocation and space management, on the administration side. As well as creating informed users, an example of this would be a student looking for a place to eat on campus, they would then check the Crowd Pulse System which provides the user with the crowd density information, allowing them to make an informed decision.

With access to the network structure, Crowd Pulse can significantly enhance its capability to identify "personal" devices with greater precision. This means that instead of merely generating crowd density values for the entire campus, it can pinpoint Wireless Access Points for more localized crowd density values.

> [!example]- Initial Design for User Interface
>
> > [!quote]- With Access to Network Topology
> > ![[Pasted image 20231123125302.png]]
>
> > [!quote]- Without Access to Network Topology
> > ![[Pasted image 20240228092302.png]]

### The Development Journey

#### Initial Ideas of IoT and Wi-Fi
At the onset of our project, I considered various approaches for monitoring crowd density on a campus network. The initial ideas revolved around two primary technologies - Internet of Things (IoT) and Wi-Fi. IoT referred to the use of connected devices such as sensors or beacons that could provide real-time data about device presence within their proximity. On the other hand, Wi-Fi offered a more comprehensive approach by either scanning the entire network for connected devices and estimating crowd density based on their numbers, or somehow utilising the existing network topology to "map" individual areas.

The rationale behind IoT was to set up a network of sensors or beacons across the campus that could detect the presence of devices within their range. By deploying these devices in strategic locations, I aimed to estimate the crowd density of different areas on the campus. However, this approach required significant investment in hardware and infrastructure. Moreover, there were many variables to consider: related to device placement, battery life, and ensuring network connectivity for the IoT devices.
##### IoT Approach:
The Internet of Things (IoT) approach for Crowd Pulse would have involved deploying a network of connected sensors throughout the target area (campus). These sensors would be responsible for detecting and reporting the presence of devices within their range. The benefits of this approach include:

1. **Fine-grained data collection**: IoT sensors can provide more accurate and detailed information about crowd density, as they are placed in specific locations and cover smaller areas.
2. **Real-time analysis**: With the IoT network, Crowd Pulse can perform real-time analysis of crowd density data, allowing for immediate action to be taken when necessary.

However, there are also downsides to this approach. Such as:

1. **Cost and infrastructure**: Setting up an IoT network requires significant investment in both hardware and maintenance costs. It also necessitates the installation of a robust communication infrastructure to enable seamless secure data transfer between sensors and a central server.
2. **Complexity**: Managing and maintaining a large number of sensors can be challenging, especially when it comes to updating firmware, troubleshooting issues, and ensuring their security.
##### Wi-Fi Approach:
The Wi-Fi approach for Crowd Pulse would have involved utilizing the Wi-Fi access points already present on campus to collect data on crowd density. This method does not require additional hardware beyond what is already installed. The benefits of this approach include:

1. **Reduced cost and infrastructure**: Since no additional hardware is required, there are no significant upfront costs or ongoing maintenance expenses for Crowd Pulse using the Wi-Fi approach.
2. **Widely available**: Wi-Fi networks are common in educational institutions, making it an easily deployable solution.

Despite its advantages, this approach also comes with its downsides:

1. **Limited accuracy and coverage**: Since crowd density data is collected based on the number of devices connected to a single access point, there may be inaccuracies or inconsistencies when it comes to crowd density measurements. Additionally, the Wi-Fi method may not provide detailed information about specific areas with high crowd density due to the larger coverage area of access points.
2. **Limitations for real-time analysis**: Since Crowd Pulse using this approach relies on the Wi-Fi access points for data collection, it may not be able to perform real-time analysis as the IoT approach due to potential network latencies or limitations in processing power at the access points.
#### Potential Hybrid IoT Wi-Fi approach
Considering the limitations of both IoT and Wi-Fi approaches, I decided a hybrid approach might be better. This method combined the benefits of both technologies - IoT's ability to provide real-time data from specific areas and Wi-Fi's comprehensive coverage of the entire network. Under this approach, IoT  devices would have been deployed in critical areas such as a campus library, lunch areas, cafes, shops, etc., to monitor crowd density in those particular spaces. In contrast, Wi-Fi was used to estimate the overall crowd density across the campus network by scanning for connected devices.

**Benefits of Hybrid Approach**:
1. Improved Accuracy: Combining data from both IoT devices and Wi-Fi access points can result in a more precise determination of crowd density.
2. Enhanced Flexibility: The hybrid approach would allow Crowd Pulse to adapt to various environments, as it could utilize available Wi-Fi networks when IoT devices are not an option.
3. Scalability: The hybrid system could expand its reach by integrating with existing campus Wi-Fi infrastructure and adding IoT devices where necessary.

**Downsides of Hybrid Approach**:
1. Increased Complexity: Managing and coordinating data from multiple sources, both IoT devices and Wi-Fi access points, can add complexity to the system design and implementation.
2. Cost: The hybrid approach would require a larger budget due to the additional cost of purchasing and deploying IoT devices alongside existing campus Wi-Fi infrastructure.
3. Privacy Concerns: Utilizing both technologies could potentially increase privacy concerns as more data is being collected from various sources.
#### Move to Only Wi-Fi approach
Despite the potential success of the hybrid IoT Wi-Fi approach, I foresaw some challenges related to the implementation, maintenance, and cost of IoT devices. The high cost, complex installation process, and intermittent connectivity issues made me reconsider the strategy. I decided to shift entirely to a Wi-Fi-based solution. 
**Benefits**:
- Utilizes existing Wi-Fi infrastructure
- No need for additional hardware installation (sensors)
- Reduced costs compared to IoT approach
- Less complicated setup and implementation process
**Downsides**:
- Lack of network topology information
- Limited crowd density precision, only able to provide overall density data
- Real-time analysis may be challenging due to data processing requirements

In this approach I envisioned the system utilise the existing Wi-Fi infrastructure to map out the devices connected to the Wi-Fi, due to the nature of a campus location, most people would be connected to the campus Wi-Fi, and so could be crowd data can be gathered. I initially wanted the system to scan the network, discover the topology of the network and then utilising that topology, generate crowd density data for each individual Wireless Access Point (WAP) on the network for each WAP I would be able to generate the crowd density, correlate that to the real-world location and display that information to users. 
#### Unknowable Topology
The Discovery that discovering / mapping topology as a "user device" was impossible, posed a significant challenge. In response, I reconsidered the initial IoT device approach, as well as an approach that utilised an exported topology to remove this challenge entirely. I noted that routers and other "management devices" had the network topology, I learned in some cases you can export the network topology [22]. And So I continued with the approach using an exported topology and supplementing that data with a scanning system.
#### Hybrid Topology and Scanning Approach
The Hybrid Topology and Scanning approach combines the usage of both network topology information, if available, and scanning techniques to generate crowd density and monitoring values. This method offers some benefits over the initially considered options. For instance, it provides more comprehensive data by utilizing both sources when possible. Additionally, it offers increased flexibility since it can function even when network topology information is not available. Furthermore, it may allow for real-time analysis of crowd density in specific areas, providing valuable insights to users.

Benefits of Hybrid Topology and Scanning approach:
- Comprehensive data collection (when topology is available)
- Increased flexibility (can function without network topology)
- Real-time analysis possible (in some cases)
### Project Extensions / Different Methods

In this section I'll go over some of the different methods that were considered for the implementation of the project.
#### Computer Vision
Using computer vision is an option, that could be explored by using some code to monitor the people who are entering and exiting buildings it would give a good indication on how many people are inside the building. This has the drawback of not being able to monitor people who are outside of areas with cameras, and so would be very difficult to get an accurate measurement for the crowd density.

This would also require some form of Machine Learning to identify people within a crowd and be able to distinguish the different people it comes across, similar to a facial recognition system which raises security concerns.
#### Subnet Sectioning
Implementing subnet sectioning for different areas of the campus within the Wi-Fi network infrastructure could significantly enhance the efficacy of crowd detection systems like Crowd Pulse. By allocating specific subnet addresses to distinct zones, devices connecting to wireless access points would automatically be assigned to their corresponding subnet based on their location. This approach streamlines the scanning process, enabling the system to pinpoint user devices more accurately and thereby provide more precise readings for crowd density in each designated area. Such precise localization of user devices within the network can greatly improve the effectiveness of crowd monitoring and management efforts on campus. Additionally, this method enhances crowd management, event safety, and infrastructure monitoring, ensuring comprehensive coverage and efficient resource allocation. This also means that Crowd Pulse would not require network topology privileges to work effectively.
#### Mac Address Swap Tracking using ML
Utilizing Machine Learning presents a promising avenue for addressing the MAS Problem most network scanning software encounters (Mac Address Swapping). A potentially viable strategy entails conducting multiple scans during off-peak hours to comprehensively map out the infrastructure. By meticulously filtering known devices, ML algorithms could hone in on outliers, specifically MAC address swaps, with greater precision. For instance, if a device suddenly disappears from the network while another device with a different MAC address emerges simultaneously, it could indicate a MAS event. Which could help in identifying "people"
#### Time Scanning
During the quieter hours of the night, we would conduct periodic network scans to establish a foundational baseline of the networking devices present. These scans encompass a comprehensive range of network components, including switches, routers, and access points, etc. Providing a detailed overview of our networking infrastructure. These initial scans serve as a foundational reference point for subsequent scans aimed at crowd detection. By identifying and cataloguing the devices present during these off-peak scans, I can effectively filter out known entities from our crowd detection algorithms, thereby augmenting the accuracy and reliability of our monitoring systems.
## Project Limitations
In the development phase of my project, I encountered several limitations that posed potential challenges to its functionality and effectiveness. These obstacles ranged from technical constraints like unpredictable network topologies to practical concerns such as overlapping IP addresses and vendor MAC rotations.
### Unknowable topology
One notable limitation was the unpredictable topology of the network, which complicated the accurate monitoring and management of network classes and devices. To address this issue, I implemented two methods, the first a dynamic discovery mechanism. This mechanism scans the network for new devices, ensuring updates to the database. The Second Method was allowing a user to supply the program with the network topology, allowing for enhanced functionality.
### Network range class
Another significant obstacle I faced involved the network range classes, which occasionally led to overlapping IP addresses and difficulties in device identification. To mitigate this challenge, I opted for CIDR notation. This allowed me to precisely define the IP address range for each network class, facilitating clear differentiation and accurate device tracking.
### Mac Address Rotation
Additionally, I grappled with the challenge posed by vendor MAC rotations, which jeopardized device identification due to the constant shuffling of MAC addresses. While considering potential solutions, I meticulously weighed the costs and benefits of implementing Machine Learning algorithms to automatically detect and adapt to MAC rotations. After thorough deliberation, I made a conscious decision not to pursue this particular problem. This determination stemmed from the realization that other facets of the project held greater significance, and diverting resources to address this issue would detract from those priorities. Instead, I chose to bolster the existing strategy by concentrating on consistently updating the database with known vendor MAC addresses and their corresponding device types. This proactive approach yielded positive results, ensuring steadfast and accurate device identification, even amidst MAC rotations.
### Real-Time-Analysis
Another Limitation that I ran into during development was the aspect of real-time data, initially the plan included real-time data analysis, however due to the time required for scanning or processing the network topology, real-time data became much harder to implement, due to this I decided, that it would be better to focus on the other aspects of the project and use timed intervals, much like other projects of this type, for example the Bridgton and Hove Bus app, which uses time intervals, to refresh the data, they use a time delay of 10s for a live map refresh, this allows time for the processing and provides the user with a relatively quick data refresh [23].

Despite facing a multitude of challenges, I effectively implemented solutions to mitigate their impact, ensuring the seamless operation of my network management system. Through meticulous planning, strategic decision-making, and diligent execution, I navigated through complexities and upheld the integrity of the network infrastructure. This accomplishment serves as a testament to my unwavering dedication and proficiency in overcoming obstacles and delivering optimal results.
### What does the project do vs initial plan for project
Crowd Pulse is a solution designed to monitor the presence and density of users across a large scale area. Initially the idea was to use scanning techniques to discover the network topology and then develop the data into usable metrics for crowd detection and monitoring, however due to some of the limitations that where encountered, the Project changed into what it is now. The Crowd Pulse Project, has developed into a system that can accept the network topology as an input, or use scanning techniques to generate crowd density and monitoring values, this differs from the initial desired implementation as the system is unable to get the network topology itself, in the case the network topology is not provided the system will only be able to generate crowd a singular crowd density value for the entire area, and not individual areas, like the initial design, however when crowd pulse is given the network topology, the system is able to identify areas that are busier than others, and show this to a user.
## Testing
Due to the nature of the Crowd Pulse project, I decided it would be best to use a blend of synthetic and real-world data. In accordance with the laws and regulations mentioned earlier in this report, I only used the crowd pulse system on network's I had direct authorization to do so.

Initially I tested the system a small home network, which did not accurately simulate the environment that the the project would be deployed in, i.e. large area networks that have high device counts. So to fix this I decided to use a python module named Faker,

Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service [24]. I utilized faker to create synthetic data, I created data that simulated network topologies.

I created a system that would allow the movement of devices between the different locations on a topology, I did this to simulate a more realistic environment, this showed that the crowd pulse project is capable of monitoring the network accurately.

##### How was it tested?
As stated before initially the project was tested on small home networks, that I had access to at the time. Due to the nature of the project, I decided that testing on small home networks was not the best way to test the project, as it was built for crowd monitoring on a larger scale.

I thought of a different way to test the project, without access to a large scale network due to potential privacy and security issues. Synthetic data, this would allow me to create much larger data that I could use to test the system.

Using the Faker library allowed me to simulate various network environments realistically, This synthetic data generation approach provided a controlled yet expansive testing environment without compromising actual user data. By generating data representative of real-world network behaviours, I could assess the project's performance, scalability, and accuracy under conditions akin to its intended deployment. This comprehensive testing approach helped identify and rectify issues early in the development cycle, ensuring a more robust and reliable final product.

Below Are some of the Smaller Example network topologies that were used to Test Crowd Pulse.

![[Pasted image 20240425093132.png]]
![[Pasted image 20240425093224.png]]
![[Pasted image 20240425093243.png]]
![[Pasted image 20240425093317.png]]
![[Pasted image 20240425093438.png]]
## Evaluation
### The Problem
The challenge we're facing centres around the need for a more effective monitoring of crowd presence across university campuses. At Present there is no system that is used to monitor the crowd density within campus grounds. This is an oversight that became apparent during the COVID-19 pandemic, a system like the one described in this report would help in day-to-day operations and would become critical during significant events, such as campus fairs, open days, protests and would be useful during another pandemic / epidemic. 
### The Solution
The proposed solution is Crowd Pulse, a system that utilizes the pre-existing Wi-Fi infrastructure to monitor the approximate location of "user devices", this means that when connected to the Wi-Fi the device's approximate location is logged, for historical data analysis to show where the busiest areas on the campus are. Crowd Pulse Works by using the existing Wi-Fi Access Points that are scattered around the campus by logging the devices that are connected to these Wi-Fi Access points we can correlate the number of devices connected to the crowd density in that location.

### Why This Matters
The significance of this Problem and the solution was of incredible importance only a couple of years ago, when the COVID-19 pandemic struck the world. A system of this type would have allowed users to have a lower chance of infection by avoiding the areas that this system would have identified.

Without a solution to this we are unable to identify the busiest locations of a campus, we are unable to locate areas where resources are not being used, and we are unable to locate potential crowd based security risks.

With a solution to this we would be able to identify all of these things, and have the historical data to make informed decisions, such as re-allocating unused resources such as computers, staff, etc. to more used areas.


### Why is this the best Solution 

Crowd Pulse Stands as the best solution to this problem for the following Reasons:
1. Crowd Pulse uses the pre-existing infrastructure
2. It has multiple applications
	- Locating busy areas and events
	- Locating under used areas and resources
	- Locating potential security risks
3. It can be used on a day-to-day basis
4. It it can easily be expanded on

### Does It work as Intended?
The answer to this question is more complex than you might think. Does Crowd Pulse Work as described by the Project Proposal, kind of, the project proposal stated the following:

The primary objectives:
1. develop a system for detecting using Wi-Fi or IoT
2. Real-Time Data analysis
3. Integration with existing university infrastructure
4. User Interface

The Current System, fulfils the first objective as the project utilizes the existing infrastructure.

The second objective I deemed to be too expensive in time and resources, when developing, I decided that having historical data would suffice for users, I think that it would not be hard to estimate the real-time crowd density, based on the existing historical data.

The third objective is more of a grey area, when I wrote the objective I wanted the system to be integrated into the university mobile app, so that anyone could access the information. However I was advised by my project supervisor that this would involve getting permissions and going through an extensive approval process. On the Other hand the system is integrated with the university infrastructure in the sense that the Wi-Fi infrastructure is used.

The forth objective I did implement but I believe it could have been done better, website and User interface design has never been a strong point for me, however I decided that a simple UI would be better than no UI at all.

So the Answer Remains does it function as intended? yes, it may not have met all the original aims and objectives, but I can say that the crowd pulse is functional and works how I currently intend it to.
#### How Well does it work?
Crowd Pulse demonstrates it's effectiveness in addressing the identified problem by accurately monitoring crowd density and presence. Through the data collection and analysis

Below is a graph showing the Crowd Density Values for the topology below it, it is just one instance in time and does not show the historical data but does show locations that are the busiest, as shown by the red coloration.
![[Pasted image 20240425121117.png]]
![[Pasted image 20240425121518.png]]
## Conclusion

Throughout this report, we have talked about the core challenges faced by university environments, the limitations of the project and how Crowd Pulse offers solutions to the following:
1. Crowd Monitoring
2. Effective Resource Allocation
3. Security and Campus Safety
In conclusion, the Crowd Pulse project stands as a solution to address the need for effective crowd monitoring across a university campus. 
### Project Impact
Through planning, and strategic decision-making, and execution, Crowd Pulse offers a solution that addresses critical issues faced by university campuses worldwide. By providing insights into crowd density, optimizing resource allocation, and enhancing safety measures, Crowd Pulse can empowered campus administrators and staff to make informed decisions and improve overall campus operations.

### Final Thoughts and Considerations:

As we conclude this report on the Crowd Pulse project, it's important to consider the larger implications and potential future directions of this project. Beyond university campuses, Crowd Pulse has the potential to transform crowd management strategies in various contexts, ranging from public events to commercial spaces.

Despite the achievements of the Crowd Pulse project, there are still areas that could be developed and enhanced further. With additional time and resources, the following project extensions could be pursued:
1. **Incorporating Machine Learning for Mac Address Swapping:** Addressing the challenge of MAC address swapping through machine learning algorithms could significantly enhance the accuracy and reliability of the Crowd Pulse scanning system. By training models to detect and adapt to MAC address rotations, we could improve device identification and provide more precise crowd monitoring data.
2. **Creating a Better User Interface (UI):** While the current UI serves its purpose, there is room for improvement in terms of user experience and aesthetics. Investing in the development of a more intuitive and visually appealing UI could enhance user engagement and satisfaction, making the Crowd Pulse system more accessible and user-friendly for a wider audience.
3. **Exploring Real-Time Data Analysis:** Although the decision was made to prioritize historical data analysis over real-time data processing, there is potential for incorporating real-time monitoring capabilities. By leveraging advanced data processing techniques, further enhancing the system's effectiveness and responsiveness.
4. **Enhancing Integration with Existing University Infrastructure:** While Crowd Pulse currently utilizes existing Wi-Fi infrastructure for crowd monitoring, there is an opportunity to deepen integration with other university systems and platforms. This could involve collaborating with IT departments to streamline data sharing and integration processes, ultimately creating a more seamless and interconnected campus ecosystem.

  
In conclusion, the Crowd Pulse project represents a significant step forward in addressing the challenges of crowd monitoring, resource allocation, and campus safety within university environments. By leveraging existing Wi-Fi infrastructure and innovative data analysis techniques, Crowd Pulse offers a powerful solution for enhancing situational awareness, optimizing resource utilization, and proactively managing security risks. While the project has achieved notable success in its current iteration, there remains ample potential for future development and refinement.

## Bibliography
[1] Github, “About Projects - GitHub Docs,” _GitHub Docs_, 2024. https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects (accessed Apr. 24, 2024).

[2] Smart Projects, “A Brief History of SMART Goals,” Project Smart, Dec. 13, 2014. https://www.projectsmart.co.uk/smart-goals/brief-history-of-smart-goals.php (accessed Apr. 24, 2024).

[3] Schnell, “Advantages and Disadvantages of Agile Methodology: Pros and Cons,” _Schnell Solutions_, Aug. 13, 2022. https://www.bespokesoftwaredevelopment.com/blog/agile-project-management-methodology-advantages-disadvantages/ (accessed Apr. 24, 2024).

[4] Adobe Communications Team, “Waterfall Methodology: Project Management | Adobe Workfront,” _Adobe.com_, 2022. https://business.adobe.com/blog/basics/waterfall#:~:text=The%20Waterfall%20methodology%20%E2%80%94%20also%20known,before%20the%20next%20phase%20begins. (accessed Apr. 24, 2024).
[5] “Development of a new sensor system to increase passenger safety on railway platforms | ALTPRO,” _ALTPRO_, Sep. 25, 2022. https://altpro.com/2022/09/26/development-of-a-new-sensor-system-to-increase-passenger-safety-on-railway-platforms/ (accessed Apr. 05, 2024).

[6] Apple, “Wi-Fi privacy,” _Apple Support_, 2017. https://support.apple.com/en-gb/guide/security/secb9cb3140c/web (accessed Apr. 24, 2024).

[7] TallyFi, “People Counters for Nightclubs by TallyFi - Support,” _Tallyfi.com_, 2018. https://www.tallyfi.com/support/manual (accessed Apr. 04, 2024).
[8] Crowd Connected, “People Tracking,” _CrowdConnected People-Tracking_, 2022. https://www.crowdconnected.com/solutions/people-tracking/ (accessed Apr. 04, 2024).

[9] Pointr, “Pointr - Deep Location® Company | Indoor Maps, Positioning & More,” _Pointr.tech_, 2024. https://www.pointr.tech/ (accessed Apr. 04, 2024).

[10] C. Preusler, “Sightcorp Delivers Computer Vision Technology for Real-Time Face Analysis Hosted at the Edge,” _HostingAdvice.com_, Sep. 22, 2020. https://www.hostingadvice.com/blog/sightcorp-delivers-real-time-face-analysis/ (accessed Apr. 05, 2024).
[11] S. Nair, “Thales introduces real-time crowd management solution for railway stations,” _Railway Technology_, Mar. 23, 2021. https://www.railway-technology.com/news/thales-real-time-crowd-management/?cf-view (accessed Apr. 05, 2024).

[12] Professional Engineering, “Lidar and AI to monitor crowds at Bristol train station,” _Imeche.org_, 2023. https://www.imeche.org/news/news-article/lidar-and-ai-to-monitor-crowds-at-bristol-train-station (accessed Apr. 05, 2024).

[13] Intersoft Coonsulting, “General Data Protection Regulation (GDPR) – Final text neatly arranged,” _General Data Protection Regulation (GDPR)_, Apr. 22, 2024. https://gdpr-info.eu/ (accessed Apr. 24, 2024).

[14] Government Digital Service, “Data protection,” _GOV.UK_, Nov. 15, 2011. https://www.gov.uk/data-protection#:~:text=The%20Data%20Protection%20Act%202018%20is%20the%20UK's%20implementation%20of,used%20fairly%2C%20lawfully%20and%20transparently (accessed Apr. 24, 2024).

[15] Information Commissioner's Office, “For organisations,” _Ico.org.uk_, Feb. 21, 2024. https://ico.org.uk/for-organisations/ (accessed Apr. 24, 2024).

[16] BCS, “BCS, THE CHARTERED INSTITUTE FOR IT CODE OF CONDUCT FOR BCS MEMBERS,” Jun. 2022. Available: https://www.bcs.org/media/2211/bcs-code-of-conduct.pdf

[17] Oracle, “Access Cloud Services for Free,” _Oracle.com_, 2024. https://www.oracle.com/uk/cloud/free/ (accessed Apr. 25, 2024).

[18] Google, “Google Drive,” _Google.com_, 2024. https://drive.google.com (accessed Apr. 25, 2024).

[19] Teamgantt, “TeamGantt FAQs,” _Teamgantt.com_, 2023. https://www.teamgantt.com/ (accessed Apr. 25, 2024).

[20] Gitea, “Gitea Official Website,” _Gitea.com_, 2024. https://about.gitea.com/ (accessed Apr. 25, 2024).

[21] Nmap, “Nmap: the Network Mapper - Free Security Scanner,” _Nmap.org_, 2017. https://nmap.org/ (accessed Apr. 25, 2024).

[22] Cisco , “Cisco DNA Center User Guide, Release 2.3.5 - Display Your Network Topology [Cisco Catalyst Center],” _Cisco_, Feb. 2024. https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/2-3-5/user_guide/b_cisco_dna_center_ug_2_3_5/b_cisco_dna_center_ug_2_3_5_chapter_0101.html (accessed Apr. 25, 2024).

[23] Brighton & Hove Buses, “Brighton & Hove Buses App,” _Buses.co.uk_, 2021. https://www.buses.co.uk/app (accessed Apr. 25, 2024).

[24] D. Faraglia, “joke2k/faker: Faker is a Python package that generates fake data for you.,” _GitHub_, Apr. 17, 2024. https://github.com/joke2k/faker (accessed Apr. 25, 2024).
## Appendices

### Appendix A: Project Proposal
By Morgan Plant
#### **Project Summary**
The aim of this project is to design and develop a University Crowd Detection System for monitoring the presence and density of users in different areas of the university. This system will have the flexibility to utilize either Wi-Fi technology or IoT devices to collect user data. In addition, we will create a user-friendly interface, either a web application or a mobile application, to visualize and interact with real-time data on a map of the campus.
##### Project Objective
- The primary objective of this project is to identify high crowd density locations on campus
##### Example Usage
- The project could be used during a pandemic / epidemic, to view the areas with the most people, this can be useful to a user as they can then avoid certain areas, to decrease the risk of infection.
- The project could be used to indicate whether a room / area is full and, which would save time on the part of the user
- This project could be used to help manage protests and other similar events
###### Aims
1. To create a University Crowd Detection System capable of monitoring and analysing crowed presence and density in university locations.
2. To optimize resource allocation and space utilization across the university.
3. To design and develop a user interface for visualizing real-time user data on a map of the campus.
4. To integrate this new resource with the existing infrastructure of the University
##### Objectives
###### **Primary Objectives**
1. **Design and Development**: Develop a flexible and scalable system for user detection using either Wi-Fi technology or IoT devices.
2. **Real-time Data**: Implement real-time data collection and analysis to provide immediate insights.
3. **Integration**: Ensure seamless integration with existing security and resource management infrastructure on campus.
4. **User Interface**: Design and develop a user-friendly interface (web or mobile application) for visualizing real-time user data on a map of the campus.
###### **Secondary Objectives**
1. **Scalability**: Ensure that the system can be easily expanded to cover various campus locations.
2. **Data Visualization**: Create interactive map-based visualizations for better understanding of user data.
3. **Historical Data**: Store historical data for trend analysis and decision-making.
4. **Resource Optimization**: Provide recommendations for resource allocation based on user data.
##### **Project Relevance**
This Project aims to address proper resource allocation, by allowing users to view the areas on campus, such as the library, university shop, etc. that are busy, or help manage crowd control during events, and provide useful data about said events, this project could also contribute to insights for space utilization, safety and security measures, which would make it a valuable tool for campus management. This relates to the degree I am studying for **Computer Science** because this project is centred on aspects of my studies such as, Human-Computer Interaction for creating the interface for users to check, Computer-Security, due to the nature of privacy featured in this project, Computer-Networks as this project will feature either a web-based interface or usage of Wi-Fi Systems to detect users. as well as Data Analysis aspects.

This project will test the skills I have learned in my studied modules, for instance this will test my Software Engineering capabilities, throughout the entire process, the GUI, web-based or not will test my Human-Computer Interaction skills, as the project is related to crowd density, this will involve data analytical skills, as well as Networking skills. as well as professional writing skills
##### **Resources Required**
1. Hardware:
   1. **Detection Devices**: Depending on the chosen technology (Wi-Fi or IoT), I'll need the necessary hardware, such access to Wi-Fi access points or IoT sensors. These devices will be responsible for collecting user data.
   2. **Dedicated Device**: To process and store data
2. Software:
   1. **Development Tools**: Software development tools, including integrated development environments (IDEs), programming languages, and development frameworks for creating the system.
   2. **Data Analysis Software**: Tools for real-time data analysis, data visualization, and data storage.
   3. **User Interface Development Tools**: Software for designing and developing the user-friendly interface, whether it's a web application or a mobile application.
3. Permissions
   1. Obtain the necessary approvals and permissions for installing monitoring equipment on the university campus. This may involve collaboration with university administrators and compliance with data privacy regulations.
##### **Expected Outcomes**
Upon completion of this project, I anticipate the following outcomes:
1. A functional University Crowd Detection System capable of utilizing either Wi-Fi or IoT technology or both.
2. Real-time user presence data.
3. Enhanced resource management and space utilization.
4. An intuitive and interactive user interface for viewing real-time user data featuring a map.
##### **Similar Projects**
- IETE Technical Review. (2021). _Crowd Monitoring: State-of-the-Art and Future Directions_. [online] Available at: https://www.tandfonline.com/doi/abs/10.1080/02564602.2020.1803152 [Accessed 15 Oct. 2023].
- Li, X. (2022). Crowd monitoring and detection. _Ntu.edu.sg_. [online] doi:https://hdl.handle.net/10356/158434.
- Mu, M. (2020). _WiFi-based Crowd Monitoring and Workspace Planning for COVID-19 Recovery_. [online] arXiv.org. Available at: https://arxiv.org/abs/2007.12250 [Accessed 15 Oct. 2023].
##### **Conclusion**
The "University Crowd Detection System" project aims to create a modern and effective solution for monitoring user presence on university campuses while providing a user-friendly interface for visualizing real-time user data on a campus map. It will contribute to the safety and security of students and staff while optimizing resource allocation.
### Appendix B Project Logs
#### B.1 Supervisor Log
1. 2023-10-24
2. 2023-10-31
3. 2023-11-07
4. 2023-11-28
5. 2024-02-20
6. 2024-03-05
7. 2024-03-15
8. 2024-04-20
#### B.2 Weekly Log
1. 2024-01-25
2. 2024-02-31
3. 2024-02-09
4. 2024-02-16
5. 2024-02-28
6. 2024-03-06
7. 2024-03-15
8. 2024-03-20
9. 2024-03-27
10. 2024-04-03
11. 2024-04-17
12. 2024-04-24





