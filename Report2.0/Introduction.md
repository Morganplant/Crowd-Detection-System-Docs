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

During the Project I learnt more about networking, how to manage a project, and effeciently manage my time.
- I discovered that network topology was unknowable as a "user device"
- I discovered that an easier way to implement this would be to change the specific network architecture to divide areas into different subnets, for example, the library building is on subnet 3 and the student union building is on subnet 4.
- I discovered that the process of MAC Address Swapping has changed in recent years [5]
- I realised that Scanning a network using a large network range class, requires more time or should be parallelized [6]
### Professional Considerations
Throughout the development and future deployment of a System such as Crowd Pulse, it is and was essential to uphold professional standards, best practices and ensuring the quality and reliability of the Crowd Pulse System.
### Project Scope
The scope of the Crowd Pulse project encompasses the design and development of a crowd density, presence detection system within a university campus settings.

Moreover, the project scope extends to considerations of scalability and adaptability, ensuring that the system can be tailored to different university areas and potentially extended to other public spaces. The project will also delve into the integration of security and privacy measures, ethical and legal compliance, and the potential for future enhancements and expansions of the system. Clear delineation of the project scope is fundamental to aligning expectations, resources, and deliverables throughout the development and implementation phases.