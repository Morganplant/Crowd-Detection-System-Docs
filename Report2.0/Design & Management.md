## Design and Project Management
### Diagrams
> [!abstract]- User Flow Diagram
>![[Pasted image 20240405132323.png]]

> [!abstract]- Entity Relationship Diagram
> ![[Pasted image 20240405132406.png]]

> [!example]- Example Network Topology map
> ![[Pasted image 20240405132952.png]]
> ![[Pasted image 20240425021551.png]]


( #insert-reference actual topology json mapping)
### How the Project is managed
I used a multitude of different ways to manage my project. For source control and backups, I used GitHub #insert-reference, my own self-hosted server #insert-reference, and Google Drive #insert-reference. Using GitHub allowed me to utilize GitHub issues and projects, which allowed me to track tasks easily, an example of which was the Kanban board below. I used my Google Drive as well as my own server to store backups periodically to avoid backup loss if something were to happen to GitHub. This way, I had a higher degree of redundancy baked into the project.

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

The Following Requirements where not met during the development of Crowd Pulse:
- Real-Time Analysis
- Integration with existing Infrastructure
- Scalability
- Usability
I made a conscious decision to focus my time and resources on completing other aspects of the project that enabled me to create a working prototype.
#### Planning
##### Initial Proposal and Requirements Analysis
Crowd Pulse began with the creation of a comprehensive project proposal. This proposal outlined the project's objectives, scope, and deliverables. Following this, an analysis of requirements was done to identify the specific areas for successful completion. This initial phase laid the groundwork for the project's planning and execution.
##### Development of Project Plan
With a clear understanding of the project's goals, I developed a plan. This plan detailed the tasks, timelines and milestones, giving me a roadmap for the project's progression, though this was not always accurate, the initial project planning was outlined by the Gantt chart below:
![[Pasted image 20231123123439.png]]
##### Execution and Monitoring
Throughout the project, I followed the established project plan and when I encountered Limitations and unforeseen setbacks, changed the plan, timelines and milestones. I decided to have regular self-assigned checkpoints, where I would evaluate my progress and decide what was best for the project, these checkpoints often included talks with my academic advisor, but not always, as shown in the <mark style="background: #FF5582A6;">Project Log section in the appendences.</mark> This proactive approach ensured that the project remained on track toward successful completion, equipping me with valuable practical skills in project management.
#### Kanban
![[Pasted image 20240405140730.png]]
#### Project Plan
During the initial Steps of the project it was important to establish a planned methodology. As I have worked with different methodologies before, namely agile, waterfall and scrum #insert-reference initially I decided I would use a waterfall method, as described by the Gantt Chart shown previously, after the waterfall methodology did not work as well as I had hoped due to setbacks, I chose to implement the Agile methodology as shown by the diagram below:
![[Pasted image 20240405141209.png]]
#insert-img-reference 

After moving to the agile development process, the workflow became easier to manage, it allowed me to work on developing Crowd Pulse, and create sub prototypes (a prototype of a specific section), which greatly improved my efficiency.

The Crowd Pulse Project was guided by utilizing SMART targets / goals, these allowed me to have a more streamlined development workflow, in this instance SMART #insert-reference refers to a way of setting objectives that are:
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
As described above in the Gantt Chart of the initial project plan which I developed using Team Gantt #insert-reference a reliable Gantt chart creation tool, the process of creating Crowd Pulse was done in phases, these phases are shown in the Gantt Chart, as well as the agile methodology example but to go over them again they are:
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
I used GitHub, as well as my own self hosted version GiTea, on a VPS (Virtual Private Server) I run a self hosted version of GitHub named GiTea #insert-reference. GiTea, is an alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in Go it works across all the platforms and architectures that are supported by Go. For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down.
###### Project / Issue Management
GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be used it for this exact purpose, in The Planning Section I showed an image of the Kanban View of this tool.

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
The Discovery that discovering / mapping topology as a "user device" was impossible, posed a significant challenge. In response, I reconsidered the initial IoT device approach, as well as an approach that utilised an exported topology to remove this challenge entirely. I noted that routers and other "management devices" had the network topology, I learned in some cases you can export the network topology. #insert-reference And So I continued with the approach using an exported topology and supplementing that data with a scanning system.
#### Hybrid Topology and Scanning Approach
The Hybrid Topology and Scanning approach combines the usage of both network topology information, if available, and scanning techniques to generate crowd density and monitoring values. This method offers some benefits over the initially considered options. For instance, it provides more comprehensive data by utilizing both sources when possible. Additionally, it offers increased flexibility since it can function even when network topology information is not available. Furthermore, it may allow for real-time analysis of crowd density in specific areas, providing valuable insights to users.

Benefits of Hybrid Topology and Scanning approach:
- Comprehensive data collection (when topology is available)
- Increased flexibility (can function without network topology)
- Real-time analysis possible (in some cases)

