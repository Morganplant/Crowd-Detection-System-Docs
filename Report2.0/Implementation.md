## Implementation
### How Crowd Pulse Works

Crowd Pulse's Scanning Technique is built around a program named Nmap. Nmap (or Network Mapper) is a robust network auditing tool, that is used for network exploration and security auditing. It's functions by leveraging IP (internet Protocol) packets to identify hosts (devices on a network), then by analysing these packets it can provide information on these hosts [22], below are some examples of what kind of scans can be done:
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
The Discovery that discovering / mapping topology as a "user device" was impossible, posed a significant challenge. In response, I reconsidered the initial IoT device approach, as well as an approach that utilised an exported topology to remove this challenge entirely. I noted that routers and other "management devices" had the network topology, I learned in some cases you can export the network topology [21]. And So I continued with the approach using an exported topology and supplementing that data with a scanning system.
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
