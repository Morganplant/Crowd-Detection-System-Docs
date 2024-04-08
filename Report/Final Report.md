## Introduction
This project revolves around the concept, execution, and evaluation of a crowd density and presence detection system. Utilizing Wi-Fi technology the system aims to determine areas of high crowd density, providing users with information for making informed decision making. The name of this project is "Crowd Pulse".

Users will interact with the system in a way designed to be usable by anyone, This interface will be in the form of a web interface, allowing users, to locate the high density areas, to make informed decisions.


The Crowd Pulse System was designed to facilitate 3 major use cases:
1. Show Students where the busy areas on a university campus are.
2. Identify areas, with low resource allocation, for example A computer Science lab that has low average usage.
3. locate potential security risks, and events such as protests.
### Project Description
The Overall goal of this project is to fashion a modern and efficient solution for monitoring crowd presence and density in a university campus setting. 

The system offers the capability to monitor and analyse crowd density across various university campus locations. This is done by utilising the existing Wi-Fi architecture, Other alternative discovery methods where considered the benefits and drawbacks of which are talked about later in this report.

The Crowd Pulse Project was guided by utilizing SMART targets / goals, these allowed me to have a more streamlined development workflow, in this instance SMART [8] refers to a way of setting objectives that are:
1. Specific
2. Measurable
3. Achievable
4. Relevant
5. Time-based

These SMART targets included:
- Achieve 70% accuracy rate in identifying crowd density in testing data.
- Identify and prioritize 3 high traffic areas within the test data.
- discover 4 low density areas, within the testing data.
- Identify and designate 3 campus zones with consistently high crowd density levels
### Motivations
My reason for creating the Crowd Pulse project was threefold
1. I wanted to test my abilities and Problem Solving Skills
2. I wanted to minimize another Isolation incident after the wake of the COVID-19 pandemic
3. I wanted to locate busy areas around the campus, either to avoid those areas, or to specifically seek them out

I wanted to develop a system would also be a great advantage to avoid queues in stores / cafes / other areas, it would allow the user to locate busy areas and then be able to plan around that new data, currently there is no such system that helps with this hence why I thought it would be an interesting and challenging problem to solve.
### Ethics
During the development of Crowd Pulse it was important to me that I not cross any ethical boundaries, and made sure to keep this throughout the entirety of the project, I wanted to be mindful of the privacy and data security of those being monitored.

#### Privacy
Due to the nature of the project I knew that it may involve the privacy of individuals and decided that I would only collect only the bare minimum amount of data to enable crowd pulse's functionality as I knew it might raise privacy concerns.
#### Data Security
Given the nature of a system that collects and analyses user data, ensuring the security and integrity of the data is of utmost importance, as such Crowd Pulse will endeavour to use the minimal amount of user data possible to ensure there is no useful way for Crowd Pulse to be used to track individuals.

### Things learned during the project

#continue-later

### Professional Considerations
Throughout the development and future deployment of a System such as Crowd Pulse, it is and was essential to uphold professional standards, best practices and ensuring the quality and reliability of the Crowd Pulse System.
### Project Scope
The scope of the Crowd Pulse project encompasses the design, development, and deployment of a crowd density, presence detection system within a university campus settings.

Moreover, the project scope extends to considerations of scalability and adaptability, ensuring that the system can be tailored to different university areas and potentially extended to other public spaces. The project will also delve into the integration of security and privacy measures, ethical and legal compliance, and the potential for future enhancements and expansions of the system. Clear delineation of the project scope is fundamental to aligning expectations, resources, and deliverables throughout the development and implementation phases.
## Problem Description

### What is the Problem that is being solved?
This Project Crowd Pulse aims to solve 3 problems; Crowd Monitoring, Effective Resource Allocation, and Security & safety concerns.

The problem being solved by the `Crowd Pulse` is the efficient monitoring of user presence and density across a university campus. This system addresses the challenge of effectively managing resource and space utilization by providing insights into crowd distribution. By utilizing based Wi-Fi technology and potentially IoT devices for data collection, the system offers flexibility in gathering user data. The primary objectives, including system development, data analysis, and user interface design, collectively tackle the problem of optimizing campus resources. In summary, the Crowd Detection System aims to mitigate challenges related to crowd monitoring and resource allocation on campus, thereby enhancing safety, security, and overall operational efficiency.

#### Crowd Monitoring - Primary Focus
Crowd monitoring serves as a crucial element in efficiently managing crowd dynamics across environments. The primary aim is to get valuable insights into crowd behaviour, using density and presence fluctuations. This comprehensive understanding empowers the campus staff, students and security to strengthen safety, space, time and resource allocation for enhanced efficiency. Moreover, crowd monitoring facilitates proactive decision-making in various scenarios, including event coordination, public safety initiatives, an individual's scheduling endeavours etc. Ultimately, the overarching objective is to gather data about the crowd density on a university campus the usage of that data can be used for many different things.

#### Resource Allocation Optimization - Secondary Focus
The integration of the University Crowd Detection System will significantly influence resource and space allocation across the campus. Providing real-time insights into crowd presence and density across various areas, the system empowers administrators to make informed decisions about resource distribution. During peak hours or events, the system identifies areas with high crowd density, prompting administrators to allocate additional resources like staff or facilities to effectively manage the surge in activity. Conversely, during periods of low activity, resources can be redirected to areas with higher demand, optimizing space utilization campus-wide. Additionally, visualizing real-time user data on a campus map enhances spatial planning, enabling administrators to identify underutilized areas that can be repurposed or consolidated for maximum efficiency. Integrating the Crowd Detection System enables universities to make more effective use of resources and space, ultimately enhancing the overall campus experience for students, faculty, and staff.

#### Safety and Security - Secondary Focus
Enhancing safety and security is a core aspect of this project. `Crowd Pulse` has the potential to significantly augment campus security infrastructure. By providing real-time updates on crowd activity across campus, the system empowers security personnel to swiftly identify and address potential security issues. Additionally, it facilitates proactive monitoring of high-traffic areas, enabling pre-emptive safety measures. With data visualization, security teams can strategically allocate resources, optimize patrol routes, and respond promptly to emergencies. Overall, integrating this system not only fortifies campus security but also cultivates a proactive safety culture, prioritizing the well-being of students, faculty, and staff.

### Does Crowd Pulse Build on anything?
`Crowd Pulse` utilizes Nmap[17] as the cornerstone for it's network scanning capabilities.

Nmap (or Network Mapper) is a robust network auditing tool, that's used for network exploration and security auditing[18]. It functions by leveraging IP packets to identify active hosts and IPs on a network, then analysing these packets to provide detailed information about each host, IP and the OS that it might be running on. the tool operates with two fundamental protocols TCP and UDP using ports to establish connections, where each connection is uniquely identified.

### Has it been done before
`Crowd Pulse` is not the first system to attempt such a thing, there are a multitude of other projects that revolve around crowd monitoring and analysis of the data. However these systems often use different methods to capture the crowd presence data, such as:

- Computer Vision
- Weight Monitoring System (used on trains mostly)
- IoT sensors
- Body Heat

  However using these methods can be inefficient, as shown below:

  - Computer vision requires that cameras be set up at all the exits and entrances, as well as expensive software to identify people and monitor when specific people enter and exit buildings.
  - Weight monitoring requires that all people are of similar weights to identify how many people are in an area, this is not always the case as children do not weigh as much as adults, and the weight variability between adults is large, and so there is not an accurate way of measuring crowd density
  - IoT sensors, depending on the implementation it can be a good way of identifying people, but it requires lots of small devices to be placed around an area for monitoring.
  - Body head systems, can be thrown off by large heat sources and so are not a good indication of crowd density, it is also hard to generate crowd density values if there is a large crowd if the crowd is packed tightly together, so heat sources are not easy to determine.

`Crowd Pulse` uses a form of WIFI tracking, which allows tracking crowd density on the following assumptions, which are talked about in more depth later in this report:

> [!warning] Assumption 1 - Each member of the crowd will have a device

> [!warning] Assumption 2 - The device a crowd member has will be on the local WIFI network

> [!warning] Assumption 3 - Crowd members will have no more than 1 device actively connected to the network
### Why it's interesting / worthwhile
Understanding the significance and value created with the Crowd pulse project is important to get a good grasp of its impact, as while this project only encompasses a university campus now, the project could be expanded to other universities, and other areas entirely. This project serves as a versatile solution to addressing challenges encountered by university campuses with crowd monitoring and the lack of data. The Goal of the system is to monitor the presence and density of users across campus with a proactive stance towards fortifying safety and security measures. Certain implementations could do this by pinpointing areas exhibiting high crowd density values, this allows campus administrators to strategies for crowd management, particularly during exigencies or unforeseen circumstances.

Furthermore, the overarching objectives and aspirations embodied within this project closely resonate with the broader missions of academic institutions, encompassing the promotion of student well-being, augmentation of operational efficiency, and cultivation of a conducive learning milieu. Through the creation of a user-friendly interface conducive to visualizing real-time data, Crowd pulse not only streamlines administrative tasks but also empowers students and faculty members to make well-informed decisions concerning their movements on campus. This empowerment engenders a palpable sense of community and collaboration, thereby fortifying the project's significance beyond its mere technical functionalities.

The main goals and aims of this project align closely with what academic institutions aim for, like promoting student well-being, improving operational efficiency, and creating an environment that fosters learning. By allowing anyone to see a the crowd density and presence values, Crowd pulse doesn't just make administrative work easier but also gives students and faculty the power to make smart choices about where they go on campus. This makes everyone feel more connected and collaborative, adding to the project's importance beyond just its technical side.

To sum up, Crowd pulse stands out as a solution that not only tackles the challenges faced by university campuses but also embodies the spirit of technological innovation and collaborative effort. Its ability to transform campus management practices and enhance the overall campus experience firmly establishes it as a project of significant interest and value within the realm of higher education.

### What does the reader / examiner need to know / understand
#continue-later

- Network-Classes
- CIDR

## Background Research

### What other Projects exist?
There are many ongoing projects exploring innovative technologies for crowd monitoring. One notable project is the Situate Project, which focuses on leveraging advanced technologies to enhance event safety and attendee experience. While the tools mentioned below primarily utilize technologies like Wi-Fi tracking, Bluetooth signals, and video analytics, there is increasing interest in utilizing LiDAR (Light Detection and Ranging) technology for crowd monitoring. LiDAR-based systems offer the potential for highly accurate spatial mapping and movement tracking, presenting exciting opportunities for improving crowd management strategies and ensuring event safety.
#### Existing Projects
##### TALLYFI
TallyFi is an event crowd monitoring tool, it is described as a crowd monitoring tool that utilizes wireless sensors to track attendee movement and density in-real time. TallyFi can provide organizers with valuable data on crowd patterns, peak hours and popular event areas. it enables event planners to take a proactive measures such as adjusting the layout, redirect attendees to less crowded zones, or deploying additional staff to specific zones[20].
##### Pros
1. **Real-Time** - TallyFi provides real-time data on attendee movement and density, enabling event organizers to make timely decisions on managing the crowd effectively
2. **Wireless and portable** - The wireless sensors used by TallyFi are convenient to deploy throughout an event venue, allowing for flexibility in monitoring different areas.
3. **Accurate data collection** - TallyFi's sensors capture accurate data, providing organizers with valuable insights into crowd patterns, peak hours, and popular event areas.
4. **Integration with management systems** TallyFi can integrate with existing event management systems, allowing organizers to streamline data collection and analysis processes.
##### Cons:
1. **Limited advanced features** - While TallyFi offers real-time monitoring and basic crowd counting functionalities, it may lack some advanced features available in other crowd monitoring tools.
2. **limitations for large-scale events** TallyFi's effectiveness may diminish in large-scale events where managing crowd flow and density becomes more complex, suggesting it may not be as suitable for such occasions compared to other tools designed for these environments.
##### CROWDCONNECTED
CrowdConnected utilizes Wi-Fi and Bluetooth signals to monitor attendee movement and behaviour in real-time during events. It offers valuable insights into crowd density, wait times, and popular areas within the event venue. It offers real-time monitoring and analysis, with a heatmap for visualisation, that seamlessly integrates with the predictive analysis and other management systems[20].
##### Pros:
1. **Real-Time** - Provides real-time insights into crowd density, wait times, and popular areas.
2. **Heatmap visualization** - Heatmap visualization facilitates easy identification of crowded zones.
3. **Integration with external tools** - with event management systems streamlines data collection and analysis.
4. **Predictive analytics** - Predictive analytics capabilities help organizers anticipate crowd-related issues.
##### Cons:
1. **Complex Setup Process** - Potential complexity for setup and configuration due to the reliance on Wi-Fi and Bluetooth signals, setting up CrowdConnected may require technical expertise.
2. **Higher pricing** - compared to some other tools while CrowdConnected offers advanced features, it may come at a higher cost compared to other crowd monitoring tools.
##### POINTR
POINTR is a location-based services platform that offers crowd-tracking and analytics capabilities for event organizers. It utilizes Bluetooth Low Energy (BLE) beacons and smartphone sensors to monitor attendee movement, generate heatmaps, and measure dwell times within the event venue. It works by using BLE beacons strategically placed throughout an event venue to capture attendee movement accurately. The platform then analyses the data collected to provide crowd behaviour, such as popular areas, engagement levels, etc. Additionally similar to CrowdConnected, it uses a heatmap to visualize the attendee behaviour, showing concentration and engagement in a venue[20].
##### **Pros:**
1. **Real-time crowd monitoring and analysis:** Provides organizers with valuable insights into crowd patterns and behaviour in real-time.
2. **Indoor positioning technology:** Offers accurate data collection for crowd analysis, enabling better decision-making.
3. **Heatmap visualization:** Helps organizers visualize attendee behavior and identify popular sections within the venue.
4. **Integration with event management systems:** Allows seamless integration with existing event management tools for efficient data management.
##### **Cons:**
1. **Potential complexity for setup and calibration:** May require technical expertise for setup and calibration of BLE beacons.
2. **Limited features specifically for crowd monitoring:** May lack advanced features compared to some other crowd monitoring tools.
3. **Potential limitations for very large-scale events:** Might face challenges in accurately monitoring and analysing crowd behaviour in extremely large events.
4. **Higher pricing compared to some other tools:** May have higher costs associated with its usage compared to alternative crowd monitoring solutions.
##### SIGHTCORP - CROWDSIGHT
Crowd Sight is a cutting-edge facial analysis tool designed specifically for event crowd monitoring. Leveraging advanced AI-powered algorithms, Crowd Sight analyses real-time video feeds to extract valuable insights into crowd demographics, emotions, and behaviour. By tracking the faces of individuals within a crowd, Crowd Sight provides event organizers with crucial data on attendee engagement, sentiment, and crowd density, enabling them to optimize crowd management strategies and ensure a safe and memorable event experience[20].
##### **Pros:**
1. **Real-time** - Crowd Sight offers real-time insights into attendee behaviour and crowd dynamics, allowing event organizers to make informed decisions on the spot.
2. **Facial Recognition** - With facial recognition capabilities, Crowd Sight provides detailed demographic profiling, including age ranges and gender distribution.
3. **Customizable Metrics** - Event organizers can tailor metrics and reporting according to their specific needs, enabling more personalized analysis.
4. **Integration with External Management Systems** - Crowd Sight seamlessly integrates with existing event management systems, facilitating streamlined data management and analysis processes.
##### **Cons:**
1. **Privacy Concerns** - The use of facial recognition technology may raise privacy concerns among attendees, requiring careful consideration of data protection regulations.
2. **Limited Features** - While Crowd Sight excels in facial analysis, its features for crowd management may be comparatively limited when compared to other tools.
3. **Higher Pricing** - Crowd Sight may come with a higher price tag compared to some alternative crowd monitoring solutions, which could be a deterrent for budget-conscious event organizers.
4. **Complex Setup Process** - Implementing Crowd Sight may require some level of setup and configuration, which could pose challenges for users with limited technical expertise.
##### DIVA
DIVA stands for (Distributed Intelligent Video Analytics), which is a solution designed to streamline crowd management within railway stations and on-board trains. By leveraging the existing CCTV infrastructure, DIVA employs real-time video analysis, to measure passenger density. DIVA uses a color-coded system (red, yellow and green), DIVA guides passengers to areas with lower density, minimising congestion[9].
##### **Pros**
1. **Enhanced Safety** - DIVA improves passenger safety by facilitating smooth movement and minimizing congestion.
2. **Optimized Flow** - By guiding passengers to less crowded areas, DIVA helps optimize passenger flow and reduce dwell times.
3. **Existing Infrastructure** - DIVA utilizes the existing CCTV network, minimizing the need for additional sensors and infrastructure.
4. **Real-time** The system offers real-time monitoring of passenger density and security threats, enabling prompt response to incidents.
5. **Security** - DIVA's ability to detect unattended luggage and trespassing enhances security within railway stations and trains.
##### **Cons**
1. **High Costs** - Implementing DIVA may involve initial costs for setup and integration with existing systems.
2. **Maintenance Requirements** - Regular maintenance and updates may be necessary to ensure optimal performance of the system.
3. **Privacy Concerns** - The use of video analytics for monitoring passengers may raise privacy concerns among some individuals.
4. **Technical Issues** - Like any technology, DIVA may encounter technical glitches or downtime, affecting its effectiveness.
5. **Training Needs** - Staff may require training to effectively utilize DIVA and interpret its data for decision-making.
##### Situate Project
The Situate project integrates Lidar-based crowd monitoring with AI technology to enhance safety and improve the passenger experience at Bristol Temple Meads train station. Using Lidar sensors, Situate tracks real-time potentially hazardous activities like individuals near platform edges, alerting operators swiftly. With wide coverage from a single sensor, it ensures comprehensive monitoring[10].
##### **Pros:**
1. Enhanced passenger safety: The Situate project employs AI and Lidar technology to proactively identify and address potential risks, thereby enhancing overall safety for passengers at Bristol Temple Meads train station.
2. Real-time incident detection: Utilizing AI, the system can detect incidents and concerning activities in real-time, enabling swift intervention by station operators to prevent accidents or escalations.
3. Comprehensive monitoring: With the ability of a single sensor to cover large distances, Situate ensures comprehensive monitoring of the station premises, reducing blind spots and enhancing security measures.
4. Improved passenger experience: By contributing to a safer and more secure environment, Situate aims to improve the overall passenger experience at the train station, potentially leading to increased satisfaction and loyalty among commuters.
##### **Cons:**
1. **Privacy concerns** - The use of AI-powered surveillance for crowd monitoring may raise privacy concerns among passengers, as it involves the collection and analysis of personal data, potentially infringing on individual privacy rights.
2. **Implementation challenges** - The implementation of the Situate project may pose challenges such as initial setup costs, system calibration, and ongoing maintenance requirements, which could impact its efficiency and effectiveness.
3. **Dependency on technology** - As the Situate system heavily relies on technology for crowd monitoring and incident detection, any technical glitches or malfunctions could compromise its ability to ensure passenger safety and security.
4. **Potential resistance or scepticism** - Some passengers or stakeholders may express resistance or scepticism towards the deployment of advanced surveillance technologies like Situate, citing concerns over surveillance culture or distrust in AI-based systems.
### What does `Crowd Pulse` do?
Utilizing cutting-edge technologies such as Wi-Fi and IoT devices, the system captures real-time data to identify areas of high crowd density, thereby aiding in optimizing resource allocation and space utilization. Stakeholders can easily access this data through an intuitive interface via web or mobile applications, enabling them to make well-informed decisions. Despite the project's potential to enhance safety, security, and efficiency, it may encounter challenges such as privacy concerns regarding data collection and the initial investment required for hardware and software setup. Nonetheless, the system holds promise for streamlining campus management processes and fostering a safer, more efficient environment for both students and staff.

The `Crowd Pulse` project aims to modernize the campus, by utilising WI-FI scanning techniques, to create a solution to monitoring crowd presence and density on the university campus. Utilising this would be beneficial to the university, Staff, students, and administration, below is the limitations of `Crowd Pulse` as a "user device" (i.e. it has no knowledge of the network structure)

> [!warning] Limits of a crowd pulse as a `user device `
> Due to the Limitations of a "user" device, not being able to see the network topology, crowd pulse is only able to detect "personal" devices for the entire network and not individual areas.

`Crowd Pulse` if given the network structure, can identify "personal" devices in a much more refined way, it means that instead of just generating crowd density values for the entire campus, it can pinpoint Wireless Access points and use those to generate crowd density values, meaning that a much more localised crowd density value can be generated.
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
### Design Choices
#continue-later

## Project Ethics
### Laws That May Apply
In this section I talk about the Laws that may or may not apply to the project, I outline which Laws and guidelines might provide issues with the project if any and which laws and guidelines may not apply.

#### GDPR
The General Data Protection Regulation (GDPR) is a legislation by the EU and EEA aimed at protecting individuals' personal data rights. Enacted in 2016 and effective since 2018, it governs data processing and protection, ensuring transparency, accuracy, and confidentiality. GDPR grants data subjects rights like access, rectification, and erasure. Organizations must appoint Data Protection Officers (DPOs), report breaches, and comply with strict fines for violations. Its global influence has prompted widespread compliance efforts and impacted data protection laws worldwide.

Since this project involves crowd detection using Wi-Fi scanning which is affected by GDPR, due to the strict regulations set out by GDPR the following apply to the project:

- **Data Collection** - This often involves, gathering potentially identifiable information, such as:
  - MAC Addresses
  - Device Names
  - Personal information
  - Location data
  - etc …
    These count as Identifiable information and as such are protected by GDPR.
- **Transparent Communication** - Anyone affected by this system needs to be properly informed.
- **Anonymity** - This system will not use personally identifiable information, it only monitors the number of "devices" in the area, not specific devices
#### DPA 2018 (Data Protection Act)
This is the UK's implementation of GDPR, providing additional specifications and exemptions. It regulates how personal data should be handled, processed, and stored, including provisions regarding the processing of special categories of personal data

> [!warning] Which may include data collected through WiFi scanning.
#### RIPA 2000 (Regulation of Investigatory Powers Act)
RIPA regulates the use of surveillance techniques by public bodies. It outlines the legal procedures for conducting surveillance and intercepting communications
#continue-later

> [!warning] Which may be applicable depending on the nature of the crowd monitoring project.
#### Human Rights Act 1998
This Act incorporates the European Convention on Human Rights into UK law. It protects fundamental rights and freedoms, including the right to privacy and the right to freedom of expression, which may intersect with the operation of crowd monitoring projects.
#continue-later

#### Information Commissioner's Office (ICO) Guidance
The ICO provides guidance on data protection laws and regulations, including GDPR compliance.

> [!warning] A crowd monitoring project should adhere to ICO guidelines to ensure lawful and ethical data processing practices.

These laws and regulations aim to ensure that crowd monitoring projects involving Wi-Fi scanning techniques comply with legal requirements, respect individuals' privacy rights, and maintain data security. It's essential for organizations undertaking such projects to carefully assess and adhere to these legal frameworks to avoid potential legal liabilities and ensure ethical conduct.

### Sussex University Code of ethics
### BCS Code of Conduct
BCS stands for (British Computer Society), this section is about the BCS code of conduct and outlines the professional standards and guidelines that members of the BCS are expected to adhere to in their practice. It provides a framework for promoting and maintaining high standards of competence, integrity, and professionalism within the field of computing. The code of conduct, addresses various aspects such as:
- confidentiality
- respect of privacy
- and responsible use of technology
#### Code of Conduct
> [!quote] Section 1 - Public Interest [21]
> You shall:
>
> 1. have due regard for public health, privacy, security and wellbeing of others and the environment.
> 2. have due regard for the legitimate rights of Third Parties.
> 3. conduct your professional activities without discrimination on the grounds of sex, sexual orientation, marital status, nationality, colour, race, ethnic origin, religion, age or disability, or of any other condition or requirement.
> 4. promote equal access to the benefits of IT and seek to promote the inclusion of all sectors in society wherever opportunities arise.

I believe I have help up this aspect of the BCS code of conduct, as In this project I have never compromised the **public health**, **privacy**, **security** and **wellbeing** of others. Third party work has properly been referenced and legitimate rights acknowledged.

> [!quote] Section 2 - Professional Competence and Integrity [21]
> You shall:
>
> 1. only undertake to do work or provide a service that is within your professional competence.
> 2. NOT claim any level of competence that you do not possess.
> 3. develop your professional knowledge, skills and competence on a continuing basis, maintaining awareness of technological developments, procedures, and standards that are relevant to your field.
> 4. ensure that you have the knowledge and understanding of Legislation\* and that you comply with such Legislation, in carrying out your professional responsibilities.
> 5. respect and value alternative viewpoints and, seek, accept and offer honest criticisms of work.
> 6. avoid injuring others, their property, reputation, or employment by false or malicious or negligent action or inaction.
> 7. reject and will not make any offer of bribery or unethical inducement

I think that I have adhered to this section of the BCS code of conduct. As I have not claimed to do work that is outside of my professional competence, I have not claimed any level of competence that I do not possess. I have ensured that I have a thorough understanding of the Legislation and have complied with such legislation.

> [!quote] Section 3 - Duty to Relevant Authority [21]
> You shall:
>
> 1.  carry out your professional responsibilities with due care and diligence in accordance with the Relevant Authority’s requirements whilst exercising your professional judgement at all times.
> 2.  seek to avoid any situation that may give rise to a conflict of interest between you and your Relevant Authority.
> 3.  accept professional responsibility for your work and for the work of colleagues who are defined in a given context as working under your supervision.
> 4.  NOT disclose or authorise to be disclosed, or use for personal gain, or to benefit a third party, confidential information except with the permission of your Relevant Authority, or as required by Legislation.
> 5.  NOT misrepresent or withhold information on the performance of products, systems or services (unless lawfully bound by a duty of confidentiality not to disclose such information), or take advantage of the lack of relevant knowledge or inexperience of others.

I have carried out this project in a professional way with care and diligence with the Relevant Authority being the University of Sussex, and have exercised professional judgement

> [!warning] I will not use Live data that may compromise individuals' privacy
> I will generate fake data to complete my testing #continue-later

I accept professional responsibility for my work on this project and have not disclosed any information for personal gain. I have not misrepresented or withheld information on the performance of the system.

> [!quote] Section 4 - Duty to the Profession [21]
> You shall:
>
> 1. accept your personal duty to uphold the reputation of the profession and not take any action which could bring the profession into disrepute.
> 2. seek to improve professional standards through participation in their development, use and enforcement.
> 3. uphold the reputation and good standing of BCS, the Chartered Institute for IT.
> 4. act with integrity and respect in your professional relationships with all members of BCS and with members of other professions with whom you work in a professional capacity.
> 5. encourage and support fellow members in their professional development.

I believe I have upheld this section of the BCS standards, as I have not taken any action that could bring the profession into disrepute. I Sought to improve my own abilities as much as I have professional standards. I believe I have upheld the representation of the BCS and acted with integrity and respect through my professional relationships.

### Privacy Considerations / Concerns of the Project
#### Ethical Issues / Considerations
During development of `Crowd Pulse` it is important to consider the ethical concerns and implement strategies to address these concerns.

##### Privacy
Due to the nature of the Crowd Pulse project it involves monitoring and analysing crowd presence and density in different locations, this could potentially raise privacy concerns among the individuals being monitored, therefore it is crucial to establish what is acceptable and what is not:

- Acceptable
  - Aggregated and anonymized data collection to ensure individual privacy is maintained.
  - Utilizing technology that focuses on crowd presence and density rather than individual identification.
- Not-Acceptable
  - Monitoring or collecting personally identifiable information[7] without explicit consent.
  - Utilizing surveillance methods that infringe upon individuals’ privacy rights.

##### Data Security
Given the nature of a system that collects and analyses user data, ensuring the security and integrity of the data is of utmost importance, as such Crowd Pulse will endeavour to use the minimal amount of user data possible to ensure there is no useful way for Crowd Pulse to be used to track individuals. In addition to holding as little identifiable data as possible, the data which is required will be thoroughly protected. Outlined below is the strategy I will be implementing to keep the minimal user data stored safe:

1. **Data Minimization**: Crowd Pulse will limit the collection of personal data to only what is necessary for the system's functionality, ensuring that the least amount of identifiable information is gathered. This aligns with privacy principles and reduces the risk associated with unnecessary data storage.
2. **Encryption and Anonymization**: Any data that is collected will be encrypted and anonymized to prevent unauthorized access and to ensure that individual identities cannot be discerned from the stored information.
3. **Compliance with Data Protection Regulations**: Crowd Pulse will adhere to all relevant data protection regulations, ensuring that the handling and storage of user data complies with legal requirements to safeguard user privacy and security.

##### Informed Consent
It is crucial to consider the issue of informed consent. Users and individuals affected by the system's monitoring should be informed about the purpose and scope of data collection and analysis. Clear communication and transparency regarding the utilization of their data, including the option to opt out, are essential ethical considerations.

This means that when / if this system is rolled out and used on the campus of a university, people who are affected by this system should be informed about the use of their data before hand.

> [!warning] This is Crucial for not infringing on the Laws outlined earlier in this section of the report

## Design And Project Management
### Diagrams
> [!abstract]- User Flow Diagram
>
> ```mermaid
> flowchart TD
> A[Start]
> B[User Chooses to View Crowd Density]
> C{Crowd Pulse Has Topology Access}
>  C_1[Get Network Topology]
>  C_2[Filter out Networking Devices]
>  C_3[Map Connected Devices to Access Points]
>  C_4[Generate Crowd Density Values for individual Access Points]
>  D_1[Scan Entire Network]
>  D_2[Filter out Networking Devices]
>  D_3[Generate Crowd Density for Entire Network]
> E[Display Data To User]
> F[End]
> A --> B
> B --> C
> C --"Yes"--> C_1
> C --"No"--> D_1
>     C_1 --> C_2 --> C_3 --> C_4 --> E
>     D_1 --> D_2 --> D_3 --> E
> E --> F
> ```

> [!abstract]- Entity Relationship Diagram
>
> ```mermaid
> erDiagram
>     NETWORK {
>         string network_id
>         string network_name
>     }
>     DEVICE {
>         string device_id
>         string device_name
>         string device_type
>     }
>     ACCESS_POINT {
>         string access_point_id
>         string access_point_name
>     }
>     USER {
>         string user_id
>         string user_name
>         string user_role
>     }
>     INTERFACE {
>         string interface_id
>         string interface_type
>     }
>     MAPPING {
>         string mapping_id
>         string access_point_id
>         string device_id
>     }
>
>     NETWORK ||--o{ DEVICE : "exists in"
>     DEVICE ||--o{ ACCESS_POINT : "connected to"
>     NETWORK }|--|| ACCESS_POINT : "exists in"
>     DEVICE }|--|| MAPPING : "mapped to"
>     ACCESS_POINT }|--|| MAPPING : "mapped to"
>     INTERFACE }|--|| MAPPING : "views"
>     USER }|--|| INTERFACE : "views"
> ```

> [!example]- Example Network Topology map
>
> ```mermaid
> graph LR
>     A[Network] --> B[Wireless AP4]
>     A --> C[Switch1]
>     A --> D[Switch2]
>     A --> E[Switch3]
>     A --> F[Wireless AP1]
>     A --> G[Wireless AP2]
>     A --> H[Wireless AP3]
>     B --> R1[Desktop1]
>     B --> R2[Laptop1]
>     B --> R3[Printer1]
>     C --> S1[Desktop2]
>     C --> S2[Laptop2]
>     C --> S3[Printer2]
>     D --> T1[Desktop3]
>     D --> T2[Laptop3]
>     D --> T3[Printer3]
>     E --> U1[Desktop4]
>     E --> U2[Laptop4]
>     E --> U3[Printer4]
>     F --> V1[Desktop5]
>     F --> V2[Laptop5]
>     F --> V3[Printer5]
>     G --> W1[Desktop6]
>     G --> W2[Laptop6]
>     G --> W3[Printer6]
>     H --> X1[Desktop7]
>     H --> X2[Laptop7]
>     H --> X3[Printer7]
>     B --> Y1[Smartphone1]
>     B --> Y2[Tablet1]
>     B --> Y3[Smartwatch1]
>     C --> Z1[printer8]
>     C --> Z2[Tablet2]
>     C --> Z3[Smartwatch2]
> ```

### How the Project is managed
I used a multitude of different ways to manage my project. For source control and backups, I used GitHub [11], my own self-hosted server [12], and Google Drive [13]. Using GitHub allowed me to utilize GitHub issues and projects, which allowed me to track tasks easily, an example of which was the Kanban board below. I used my Google Drive as well as my own server to store backups periodically to avoid backup loss if something were to happen to GitHub. This way, I had a higher degree of redundancy baked into the project.

#### Planning
##### Initial Proposal and Requirements Analysis
`Crowd Pulse` began with the creation of a comprehensive project proposal. This proposal outlined the project's objectives, scope, and deliverables. Following this, a thorough analysis of requirements was conducted to identify the specific technologies, tools, and skills necessary for successful completion. This initial phase laid the groundwork for the project's planning and execution.

##### Development of Project Plan
With a clear understanding of the project's parameters, a detailed project plan was developed. This plan delineated tasks, timelines, and milestones, providing a roadmap for the project's progression. Emphasis was placed on time management and self-discipline, with the creation of a personalized schedule to ensure steady progress. Contingency plans were also formulated to address potential roadblocks, ensuring adaptability in the face of challenges.
##### Execution and Monitoring
Throughout the project, I followed the established project plan and when I encountered Limitations, changed the plan, timelines and milestones. Regular self-assigned checkpoints were integrated into the process to evaluate progress and adjust strategies as needed. This was accompanied regular meetings with my supervisor. This proactive approach ensured that the project remained on track toward successful completion, equipping me with valuable practical skills and academic achievement.

#### Kanban
![[Pasted image 20240228085556.png]]

#### Project Plan
In undertaking the crowd pulse project, it is important to establish a planned methodology, therefore I have come up with the following diagrams and graphs to show how I will proceed with the Crowd Pulse Project.

I have worked with different methodologies before namely agile and waterfall, so I will use a combined approach in the following way, due to the nature of the fixed timeline of the project believe that a waterfall methodology would suite the project well, however I will be using an agile methodology when it comes to the Designing and Coding Phases, this is due to the nature of these phases, the design phases is one that requires rapid development in short amounts of time with a high quality return, in this case using an agile methodology makes sense as it allows me to rapidly prototype designs and evaluate them in a much more efficient way than using a waterfall method. The Same applies to the coding phase of the project it greatly hinder my abilities, so I will be focused on the agile cycle of development when entering the Coding phase.

> [!abstract]- Initial Project Gantt Chart
> ![[Pasted image 20231123123439.png]]

##### Project Phases
As described above in the Gantt Chart which I developed using Team Gantt[14] The Process of creating Crowd Pulse will be done in phases, these phases are shown in the Gantt Chart, but to go over them again they are:

- <span style="color:#92d050">Ideas / Research Phase</span>
  - In this phase I will be generating ideas looking for similar projects and completing documentation, I will also be more focused on how I will create the end goal rather than what I do to create it.
- <span style="color:#00b0f0">Design Phase</span>
  - During this phase I will be using the agile methodology to generate designs of how the product will look from a user experience point of view, as well as working on the designs for how other parts of the System will function, e.g. Diagrams and prototyping.
- <span style="color:#ffc000">Implementation / Coding</span>
  - During this Phase I will again be using the agile methodology to rapidly produce code that will follow the designs and prototypes developed in the design phase, during this phase I will also be testing as and when required although there will be an entire phase dedicated to testing these tests will be focused on the code specifics.
- <span style="color:#7030a0">Testing</span>
  - In this phase I will test all aspects of the product and work out any bugs that need to be fixed. I also hope to be able to test my product using a group of my peers that way I will be able to replicate the environment it would be used in, I will then be fixing issues that arise due to the testing done by the group of peers.
- <span style="color:#ff0000">Deployment</span>
  - This Phase is dedicated to deploying the product into the wild, in this phase the product is ready, as been thoroughly tested, and is now ready for the users to have access, I will be focused on implementing the code as well as potentially integrating it with the existing systems available.

##### Source Control - GitHub & GiTea
As discussed earlier I will be using GitHub, as well as my own cloud instance, on my instance I run a self hosted version of GitHub named GiTea [15]. GiTea, is an alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in go it works across all the platforms and architectures that are supported by Go which is a lot). For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down.

###### Project / Issue Management
GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be using it for this exact purpose.
#### Backups and Source Control
As discussed earlier I will be using GitHub, as well as my own self hosted server, on my server I run a self hosted version of GitHub named GiTea [15]. GiTea, is an alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in go it works across all the platforms and architectures that are supported by Go which is a lot). For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down.

GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be using it for this exact purpose.

## Implementation
### How Crowd Pulse Works
Crowd Pulse Works by first checking the permissions it has

> [!error] Potentially **Inconsistent** With other sections - #continue-later

- If `Crowd Pulse` has access to the network topology then it is able to identify the areas with the highest crowd density values, this can then be applied to an interface in which a user would more easily understand this data.
- If `Crowd Pulse` does not have the network topology then it can only generate the crowd density for the entire area (Wi-Fi network) which significantly limits it's functionality.

The system captures data to pinpoint areas with high crowd density, facilitating optimal resource allocation and space management, on the administration side. As well as creating informed users, an example of this would be a student looking for a place to eat on campus, they would then check the `Crowd Pulse` System which provides the user with the crowd density information, allowing them to make an informed decision.

> [!section]

The `Crowd Pulse` initiative aims to modernize campus operations by utilizing Wi-Fi scanning techniques to develop a solution for monitoring crowd presence and density. This implementation stands to benefit the university, staff, students, and administration. Below are the limitations of `Crowd Pulse` as a "user device" (i.e., lacking knowledge of the network structure).

> [!warning] Constraints of `Crowd Pulse` as a "User Device"
> Given its limitations as a "user" device unable to perceive the network topology, `Crowd Pulse` can only detect "personal" devices across the entire network, not individual areas.

With access to the network structure, `Crowd Pulse` can significantly enhance its capability to identify "personal" devices with greater precision. This means that instead of merely generating crowd density values for the entire campus, it can pinpoint Wireless Access Points for more localized crowd density values.

> [!example]- Example Interface - With Access to Topology
>
> > [!quote]- With Access to Network Topology
> > ![[Pasted image 20231123125302.png]]
>
> > [!quote]- Without Access to Network Topology
> > ![[Pasted image 20240228092302.png]]

### Different Way of doing things?
> [!error] Title change to Extension / add ons #continue-later

In this section I'll go over some of the different ways that were considered for the implementation of the project

#### Computer Vision
Using computer vision is an option, that could be explored by using some code to monitor the people who are entering and exiting buildings it would give a good indication on how many people are inside the building. This has the drawback of not being able to monitor people who are outside of areas with cameras, and so would be very difficult to get an accurate measurement for the crowd density.

This would also require some form of Machine Learning to identify people within a crowd and be able to distinguish the different people it comes across, similar to a facial recognition system which raises security concerns.

#### Subnet Sectioning
Implementing subnet sectioning for different areas of the campus within the Wi-Fi network infrastructure could significantly enhance the efficacy of crowd detection systems like Crowd Pulse. By allocating specific subnet addresses to distinct zones, devices connecting to wireless access points would automatically be assigned to their corresponding subnet based on their location. This approach streamlines the scanning process, enabling the system to pinpoint user devices more accurately and thereby provide more precise readings for crowd density in each designated area. Such precise localization of user devices within the network can greatly improve the effectiveness of crowd monitoring and management efforts on campus. Additionally, this method enhances crowd management, event safety, and infrastructure monitoring, ensuring comprehensive coverage and efficient resource allocation. This also means that Crowd Pulse would not require network topology privileges to work effectively.

#### Mac Address Swap Tracking using ML
Utilizing Machine Learning presents a promising avenue for addressing the MAS Problem most network scanning software encounters (Mac Address Swapping). A potentially viable strategy entails conducting multiple scans during off-peak hours to comprehensively map out the infrastructure. By meticulously filtering known devices, ML algorithms could hone in on outliers, specifically MAC address swaps, with greater precision. For instance, if a device suddenly disappears from the network while another device with a different MAC address emerges simultaneously, it could indicate a MAS event. Which could help in identifying "people"
#### Time Scanning
During the quieter hours of the night, we would conduct periodic network scans to establish a foundational baseline of the networking devices present. These scans encompass a comprehensive range of network components, including switches, routers, and access points, etc. Providing a detailed overview of our networking infrastructure. These initial scans serve as a foundational reference point for subsequent scans aimed at crowd detection. By identifying and cataloguing the devices present during these off-peak scans, I can effectively filter out known entities from our crowd detection algorithms, thereby augmenting the accuracy and reliability of our monitoring systems.
### What did happen vs what could have
#continue-later

## Limitations Discovered
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
Crowd Pulse is a solution designed to monitor the presence and density of users across a large scale area. Initially the idea was to use scanning techniques to discover the network topology and then develop the data into usable metrics for crowd detection and monitoring, however due to some of the limitations that where encountered, the Project changed into what it is now. The Crowd Pulse Project, has developed into a system that can accept the network topology as an input, or use scanning techniques to generate crowd density and monitoring values, this differs from the initial desired implementation as the system is unable to get the network topology itself, in the case the network topology is not provided the system will only be able to generate crowd a singular crowd density value for the entire area, and not individual areas, like the initial design, however when crowd pulse is given the network topology, the system is able to identify areas that are busier than others, and show this to a user.

## Testing

> [!warning] Mention `Faker` to generate fake data

During the testing phase of the project, I used a blend of real-world data, and simulated data, to test that the system was working correctly. In accordance with the laws and regulations mentioned earlier in this report, I only used the crowd pulse system on network's I had authorization to do so. 

Initially I was using the system on relatively small networks, which did not simulate the environment that the system would be deployed in, i.e. large area networks, that have a much higher device count. So to fix this, I decided to use `Faker`. Faker is a Python module that allows you to quickly generate fake information, such as companies, names, and most importantly for this project, Network information. Using the faker module I was able to create large networks, that would simulate the environment that the crowd pulse system would be deployed in.
### How was it tested?
Initially the project was tested on small home networks, as that was what I had access to at the time. Due to the nature of the project, testing on small home networks was not the best way to test the project, as it was built for crowd monitoring, on larger scale networks. 

I had to think of a different way to test the project without access to larger scale networks due to the potential data security issues. I landed on Faker, a library for generating synthetic data.

Using the Faker library allowed me to simulate various network environments realistically, This synthetic data generation approach provided a controlled yet expansive testing environment without compromising actual user data. By generating data representative of real-world network behaviours, I could assess the project's performance, scalability, and accuracy under conditions akin to its intended deployment. This comprehensive testing approach helped identify and rectify issues early in the development cycle, ensuring a more robust and reliable final product.
### What did you test it on?
As mentioned earlier the project underwent exhaustive testing across an extensive array of synthetic networks, meticulously crafted utilizing the sophisticated functionalities offered by the Faker library. These simulated environments spanned a broad spectrum of complexity, encompassing everything from modest home-based configurations to expansive networks mirroring the intricate infrastructure typically observed within university campuses or corporate enterprises.
### How did you get the data?
The data acquisition process began with an in-depth analysis of my personal home network, serving as the initial testing ground for the project. Subsequently, the methodology evolved towards the generation of intricate synthetic data sets crafted to accurately emulate real-world scenarios. This sophisticated approach involved meticulously fine-tuning data parameters to ensure a seamless integration Through these iterative steps, a comprehensive data framework was established, enabling exhaustive testing and refinement to drive the project's development forward.
## Evaluation
### Explain the Problem:
The challenge we're facing centres on the need for more effective monitoring and analysis of crowd density and presence across university campuses. It's a multifaceted issue with far-reaching implications. At present, we're grappling with the absence of a robust system to accurately track the ebb and flow of people within campus grounds. This deficit in oversight not only impacts routine day-to-day operations but becomes particularly critical during significant events such as protests, campus fairs, or when implementing safety protocols during public health crises like the COVID-19 pandemic. Addressing this issue necessitates a comprehensive approach by developing and implementing a monitoring systems tailored to the unique dynamics of university settings, we can significantly enhance our ability to anticipate and respond to fluctuations in crowd density. This will serve to reduce risks and empower campus authorities to make informed decisions, thereby safeguarding the welfare of the entire university community.
### Explain the Solution:
The proposed solution named "Crowd Pulse." This is a system that utilises the pre-existing infrastructure of the Wi-Fi, as an example the Wireless Access points that are scattered around could be used, This would allow you to correlate the device numbers to density of people in that area. Through data collection and analysis, Crowd Pulse will provide insights into crowd density across various campus locations.

### Explain Why It Matters:
The significance of this Problem and the solution was of incredible importance only a couple of years ago, when the COVID-19 pandemic struck the world. A system of this type would have allowed users to have a lower chance of infection by avoiding the areas that this system would have identified. During a pandemic this system becomes indispensable, and during day to day activities, this system, would provide a way for the Staff and Security to enhance the safety and security of the Students, and Staff. It would also be able locate areas, that are not being utilized properly for redistribution. An example of this could be A computer lab being under used, i.e. only half of the computers are being used, and so the system could be used to locate these types of areas.
### Why Is This Solution Best:
Crowd Pulse Stands as the best solution to this problem, for the following reasons;
- Flexibility
- Scalability
- Capabilities
This is because the, Crowd Pulse System is able to utilise the pre-existing Wi-Fi infrastructure, this is already a large reason as to why this system is better than others, For instance, a Computer Vision based system, you would need a new camera infrastructure, as well as some form of facial recognition software for the ability to count how many unique individuals are in an area, as well as the privacy violations that such a system would cause. Crowd Pulse bypasses these restrictions, by identifying people based on how many devices are connected to individual Wireless Access points or by identifying people utilising a network scanning variation. Which allows Crowd Pulse the previously stated benefits.
### What Other Things Could Be Done Better:
While Crowd Pulse presents a comprehensive solution, there are areas for potential improvement. Enhancements in privacy measures, such as implementing advanced encryption techniques and providing clearer communication on data usage, could further bolster user trust. Moreover, refining the system's scalability to seamlessly integrate with existing campus infrastructure and expanding compatibility with different devices would enhance its adaptability.
#continue-later 

### How Well Does It Work:
Crowd Pulse demonstrates effectiveness in addressing the identified problem by accurately monitoring crowd density and presence. Through its data collection and analysis, it provides insights, allowing authorities to take proactive measures. The user-friendly interface enhances usability, ensuring accessibility for all stakeholders. Overall, Crowd Pulse effectively fulfils its primary objective of enhancing safety and resource management within university campuses.

### Does It Work in the Desired Way:
Yes, Crowd Pulse functions as intended by effectively monitoring crowd density, providing insights, and offering a user-friendly interface for visualization. Its implementation of either Wi-Fi topology or Wi-Fi scanning ensures adaptability to different campus environments, while its capabilities enable proactive decision-making. Thus, Crowd Pulse aligns with the desired outcome of enhancing safety, security, and resource utilization within a university campus environment.

## Conclusion

### What is the Project 
#continue-later 

### What Design Choices made along the way
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

---
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
#### Unknowable Topology Limitation
The Discovery that discovering / mapping topology as a "user device" was impossible, posed a significant challenge. In response, I reconsidered the initial IoT device approach, as well as an approach that utilised an exported topology to remove this challenge entirely. I noted that routers and other "management devices" had the network topology, I learned in some cases you can export the network topology. #insert-reference And So I continued with the approach using an exported topology and supplementing that data with a scanning system.
#### Hybrid Topology and Scanning Approach
The Hybrid Topology and Scanning approach combines the usage of both network topology information, if available, and scanning techniques to generate crowd density and monitoring values. This method offers some benefits over the initially considered options. For instance, it provides more comprehensive data by utilizing both sources when possible. Additionally, it offers increased flexibility since it can function even when network topology information is not available. Furthermore, it may allow for real-time analysis of crowd density in specific areas, providing valuable insights to users.

Benefits of Hybrid Topology and Scanning approach:

- Comprehensive data collection (when topology is available)
- Increased flexibility (can function without network topology)
- Real-time analysis possible (in some cases)



---
#to-continue
### Why was it difficult 
##### How did you overcome these difficulties
- The limitations where difficult to navigate
	1. Unknowable topology
	2. Network range class (for scanning)
	3. Mac Address Rotation
	4. Real-time Analysis
---
### Further work / Extensions
### What did you discover / learn

- Unknowable topology
- Rediscovering the different network range classes and why they are useful
- 

