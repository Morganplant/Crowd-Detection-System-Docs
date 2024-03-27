### What is the Project 
---
### What Design Choices made along the way

1. Initial Ideas of IoT or Wi-Fi
2. Potential for a Hybrid IoT Wi-Fi approach
3. Move to Only Wi-Fi approach
4. Discovering that mapping Topology was not possible
5. Moving to Hybrid Topology given and Scanning approach
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
#### Discovery that mapping Topology as a "user device" is impossible

#reference 

In this approach I envisioned the system to instead of relying on dedicated IoT sensor devices, utilise the existing Wi-Fi infrastructure to map out the devices connected to the Wi-Fi, due to the nature of a campus location, **<mark style="background: #FFB86CA6;">most</mark>** people would be connected to the campus Wi-Fi, and thus could be crowd data can be gathered. I initially wanted the system to scan the network, discover the topology of the network and then utilising that topology, generate crowd density data for each individual Wireless Access Point (WAP) on the network for each WAP I would be able to generate the crowd density, correlate that to the real-world location and display that information to users. 

However during the development of this System I encountered a limitation, the unknowability of network topology as a "user device", meaning that I would be unable to identify which devices where connected to which WAP. This was until I noted that routers and other "management devices" had the network topology, I learned in some cases you can export the network topology. And So I continued with the approach using an exported topology in adition to 


### Why was it difficult 
##### How did you overcome these difficulties
- The limitations where difficult to navigate
	1. Unknowable topology
	2. Network range class (for scanning)
	3. Mac Address Rotation
	4. Real-time Analysis
---
### What did you discover / learn

- Unknowable topology
- Rediscovering the different network range classes and why they are useful
- 
