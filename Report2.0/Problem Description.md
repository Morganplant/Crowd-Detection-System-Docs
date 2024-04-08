## Problem Description
### What is the Problem?

The Crowd Pulse Project aims to solve 3 problems; Crowd Monitoring, Effective Resource Allocation and Security of Campus Safety.

This Project's aim is to develop an efficient monitoring solution for crowd density, across a university campus. This System is capable of providing insight into, Space utilisation and Crowd Density. This is done by utilising the existing Wi-Fi Architecture to show the busy locations in a campus environment.
#### Project Focuses
The **Primary Focus** as Stated above is the Crowd Monitoring System. The Aim is to get valuable insights into the typical movements of crowd behaviour, using the crowd density variations throughout the day, this understanding would empower the campus staff, security and students to make informed proactive decisions such as:
- Deciding what time to get lunch, study etc.
- When to Go to bars and cafes
- Redirect equipment to areas with more use
- Event coordination
- Individual Time scheduling
- Correlation with lectures attendance 
Ultimately, the overarching objective is to gather data about the crowd density on a university campus the usage of that data can be used for many different things.

The **Secondary Focuses** are *Resource allocation* and *improvements to Safety*, which can be improved by first identifying areas that are busy and those that are not, with this data Staff can then make better decisions on what to do during events or where to allocate more resources. It could be used during open days to show where the most popular areas for new students is, or show the most popular university housing areas.

#### Safety and Security - Secondary Focus

Enhancing safety and security is a core aspect of this project. `Crowd Pulse` has the potential to significantly augment campus security infrastructure. By providing real-time updates on crowd activity across campus, the system empowers security personnel to swiftly identify and address potential security issues. Additionally, it facilitates proactive monitoring of high-traffic areas, enabling pre-emptive safety measures. With data visualization, security teams can strategically allocate resources, optimize patrol routes, and respond promptly to emergencies. Overall, integrating this system not only fortifies campus security but also cultivates a proactive safety culture, prioritizing the well-being of students, faculty, and staff.


> [!warning]- Move to Implementation Section
Crowd Pulse uses the Wi-Fi to show where the busy areas of a university campus are, with this data, it could be used to improve those areas.
>
As Explained earlier Crowd Pulse uses the existing Wi-Fi to locate busy areas. The Scanning Technique uses A Large Network Class #continue-later 

### How Does Crowd Pulse Solve this?
As explained earlier Crowd Pulse Aims to solve and improve the following:
- Crowd Monitoring
- Effective Resource Allocation
- Security of Campus Safety

Crowd Pulse's Scanning Technique is build around a program named `Nmap`. Nmap (or Network Mapper) is a robust network auditing tool, that is used for network exploration and security auditing. It's functions by leveraging IP (internet Protocol) packets to identify hosts (devices on a network), then by analysing these packets it can provide information on these hosts #insert-reference, below are some examples of what kind of scans can be done:
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
### Has it been done before
Crowd Pulse is not the first in this project space, there are many projects that revolve around crowd monitoring and the analysis of that data. However these systems often use different methods to capture the crowd presence data, such as:
- Computer Vision
- Weight Monitoring (mostly used on trains)
- IoT Sensors
- Body Heat Detection
Using These methods can be inefficient as shown with the problems below:
- Computer vision requires that cameras be set up at all the exits and entrances, as well as expensive software to identify people and monitor when specific people enter and exit buildings.
- Weight monitoring requires that all people are of similar weights to identify how many people are in an area, this is not always the case as children do not weigh as much as adults, and the weight variability between adults is large, and so there is not an accurate way of measuring crowd density
- IoT sensors, depending on the implementation it can be a good way of identifying people, but it requires lots of small devices to be placed around an area for monitoring.
- Body Heat systems, can be thrown off by large heat sources and so are not a good indication of crowd density, it is also hard to generate crowd density values if there is a large crowd if the crowd is packed tightly together, so heat sources are not easy to distinguish.
#### Why is Crowd Pulse Better?

Crowd Pulse utilises the existing network topology, supplemented with scanning techniques, that allow the system more accuracy than the techniques listed above, it uses the network topology available to determine areas based on active device counts. However that being said Crowd Pulse has it's own faults, such as if the network goes down, then there is no crowd data to use.
### Why is this being solved?
After the COVID-19 pandemic there is a need to address the problem of crowd detection, this project is an important step towards a solution that can prevent another isolation period. It serves as a critical element in bolstering safety measures around campus grounds, by identifying high-density areas susceptible to potential safety hazards, like overcrowding.

The main goals and aims of this project align closely with what academic institutions aim for, like promoting student well-being, improving operational efficiency, and creating an environment that fosters learning. By allowing anyone to see a the crowd density and presence values, Crowd pulse doesn't just make administrative work easier but also gives students and faculty the power to make smart choices about where they go on campus. This makes everyone feel more connected and collaborative, adding to the project's importance beyond just its technical side.

To sum up, Crowd pulse stands out as a solution that not only tackles the challenges faced by university campuses but also embodies the spirit of technological innovation and collaborative effort. Its ability to transform campus management practices and enhance the overall campus experience firmly establishes it as a project of significant interest and value within the realm of higher education.