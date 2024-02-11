---
tags:
  - G5038-Individual-Project
---

### What is the Problem that is being solved?

This Project `Crowd Pulse` aims to solve 3 problems; Crowd Monitoring, Effective Resource Allocation, and Security & safety concerns.

The problem being solved by the `Crowd Pulse` is the efficient monitoring of user presence and density across a university campus. This system addresses the challenge of effectively managing resource and space utilization by providing insights into crowd distribution. By utilizing based Wi-Fi technology and potentially IoT devices for data collection, the system offers flexibility in gathering user data. The primary objectives, including system development, data analysis, and user interface design, collectively tackle the problem of optimizing campus resources. In summary, the Crowd Detection System aims to mitigate challenges related to crowd monitoring and resource allocation on campus, thereby enhancing safety, security, and overall operational efficiency.

#### Crowd Monitoring - Primary Focus

Crowd monitoring serves as a crucial element in efficiently managing crowd dynamics across environments. The primary aim is to get valuable insights into crowd behaviour, using density and presence fluctuations. This comprehensive understanding empowers the campus staff, students and security to strengthen safety, space, time and resource allocation for enhanced efficiency. Moreover, crowd monitoring facilitates proactive decision-making in various scenarios, including event coordination, public safety initiatives, an individual's scheduling endeavours etc. Ultimately, the overarching objective is to gather data about the crowd density on a university campus the usage of that data can be used for many different things.

#### Resource Allocation Optimization - Secondary Focus

The integration of the University Crowd Detection System will significantly influence resource and space allocation across the campus. Providing real-time insights into crowd presence and density across various areas, the system empowers administrators to make informed decisions about resource distribution. During peak hours or events, the system identifies areas with high crowd density, prompting administrators to allocate additional resources like staff or facilities to effectively manage the surge in activity. Conversely, during periods of low activity, resources can be redirected to areas with higher demand, optimizing space utilization campus-wide. Additionally, visualizing real-time user data on a campus map enhances spatial planning, enabling administrators to identify underutilized areas that can be repurposed or consolidated for maximum efficiency. Integrating the Crowd Detection System enables universities to make more effective use of resources and space, ultimately enhancing the overall campus experience for students, faculty, and staff.

#### Safety and Security - Secondary Focus

Enhancing safety and security is a core aspect of this project. `Crowd Pulse` has the potential to significantly augment campus security infrastructure. By providing real-time updates on crowd activity across campus, the system empowers security personnel to swiftly identify and address potential security issues. Additionally, it facilitates proactive monitoring of high-traffic areas, enabling pre-emptive safety measures. With data visualization, security teams can strategically allocate resources, optimize patrol routes, and respond promptly to emergencies. Overall, integrating this system not only fortifies campus security but also cultivates a proactive safety culture, prioritizing the well-being of students, faculty, and staff.

### Does `Crowd Pulse` Build on anything?

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

### Why is this an "important" problem?

Addressing the pressing need to monitor crowd density on university campuses is of paramount importance for several compelling reasons. Firstly, it serves as a critical element in bolstering safety measures across campus grounds. By meticulously identifying high-density areas susceptible to potential safety hazards such as overcrowding, administrators can proactively mitigate risks, thereby fostering a secure environment conducive to the well-being of students, faculty, and visitors. Secondly, optimizing resource allocation is pivotal for universities striving for operational excellence. Implementing precise crowd density monitoring mechanisms enables institutions to judiciously allocate resources, including security personnel, maintenance teams, and facility usage, with heightened efficiency. This strategic resource management not only enhances operational efficacy but also streamlines the utilization of campus infrastructure. Additionally, providing insights into crowd density dynamics empowers decision-makers to navigate diverse scenarios, be it managing protests or responding to emergencies, with acumen and foresight. Such data-driven decision-making facilitates effective crowd management strategies and fosters seamless event planning protocols. In summary, resolving the crowd density monitoring challenge emerges as a linchpin in fortifying safety protocols, optimizing resource utilization, and empowering informed decision-making within university landscapes. Therefore, it is incumbent upon university stakeholders to invest in robust crowd density monitoring systems, as these systems play a pivotal role in ensuring the safety and well-being of all individuals within the academic community, while also enhancing the overall operational efficiency and resilience of the institution.

### Why it's interesting / worthwhile

Understanding the significance and value created with the Crowd pulse project is important to get a good grasp of its impact, as while this project only encompasses a university campus now, the project could be expanded to other universities, and other areas entirely. This project serves as a versatile solution to addressing challenges encountered by university campuses with crowd monitoring and the lack of data. The Goal of the system is to monitor the presence and density of users across campus with a proactive stance towards fortifying safety and security measures. Certain implementations could do this by pinpointing areas exhibiting high crowd density values, this allows campus administrators to strategies for crowd management, particularly during exigencies or unforeseen circumstances.

Furthermore, the overarching objectives and aspirations embodied within this project closely resonate with the broader missions of academic institutions, encompassing the promotion of student well-being, augmentation of operational efficiency, and cultivation of a conducive learning milieu. Through the creation of a user-friendly interface conducive to visualizing real-time data, Crowd pulse not only streamlines administrative tasks but also empowers students and faculty members to make well-informed decisions concerning their movements on campus. This empowerment engenders a palpable sense of community and collaboration, thereby fortifying the project's significance beyond its mere technical functionalities.

The main goals and aims of this project align closely with what academic institutions aim for, like promoting student well-being, improving operational efficiency, and creating an environment that fosters learning. By allowing anyone to see a the crowd density and presence values, Crowd pulse doesn't just make administrative work easier but also gives students and faculty the power to make smart choices about where they go on campus. This makes everyone feel more connected and collaborative, adding to the project's importance beyond just its technical side.

To sum up, Crowd pulse stands out as a solution that not only tackles the challenges faced by university campuses but also embodies the spirit of technological innovation and collaborative effort. Its ability to transform campus management practices and enhance the overall campus experience firmly establishes it as a project of significant interest and value within the realm of higher education.

### What does the reader / examiner need to know / understand

#continue-later

- Network-Classes
- CIDR
