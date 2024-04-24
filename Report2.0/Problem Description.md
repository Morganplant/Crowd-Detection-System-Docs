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