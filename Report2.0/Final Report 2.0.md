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

