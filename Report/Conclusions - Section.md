### What Design Choices where made along the way

1. Initial Ideas of IoT or Wi-Fi
2. Move to a Hybrid IoT Wi-Fi approach
3. Move again to Only Wi-Fi approach
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



### ---



---

---
### Why was it difficult 

- The limitations where difficult to navigate
	1. Unknowable topology
	2. Network range class (for scanning)
	3. Mac Address Rotation
	4. Real-time Analysis

### What was the cleverest part?
???
#continue-later 
### What did you discover / learn

- Unknowable topology
- Rediscovering the different network range classes and why they are useful
- 