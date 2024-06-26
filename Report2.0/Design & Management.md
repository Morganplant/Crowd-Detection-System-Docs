## Design and Project Management
### Diagrams
> [!abstract]- User Flow Diagram
>![[Pasted image 20240405132323.png]]

> [!abstract]- Entity Relationship Diagram
> ![[Pasted image 20240405132406.png]]

> [!example]- Example Network Topology map
> ![[Pasted image 20240405132952.png]]
> ![[Pasted image 20240425021551.png]]

### How the Project is managed
I used a multitude of different ways to manage my project. For source control and backups, I used GitHub [1], my oracle cloud instance [17], and Google Drive [18]. Using GitHub allowed me to utilize GitHub issues and projects, which allowed me to track tasks easily, an example of which was the Kanban board below. I used my Google Drive as well as my own server to store backups periodically to avoid backup loss if something were to happen to GitHub. This way, I had a higher degree of redundancy baked into the project.
#### Kanban
![[Pasted image 20240405140730.png]]

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
During the initial Steps of the project it was important to establish a planned methodology. As I have worked with different methodologies before, namely agile, waterfall and scrum [3] initially I decided I would use a waterfall method, as described by the Gantt Chart shown previously, after the waterfall methodology did not work as well as I had hoped due to setbacks, I chose to implement the Agile methodology as shown by the diagram below:
![[Pasted image 20240405141209.png]]
[3]

After moving to the agile development process, the workflow became easier to manage, it allowed me to work on developing Crowd Pulse, and create sub prototypes (a prototype of a specific section), which greatly improved my efficiency.

The Crowd Pulse Project was guided by utilizing SMART targets / goals, these allowed me to have a more streamlined development workflow, in this instance SMART [2] refers to a way of setting objectives that are:
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
As described above in the Gantt Chart of the initial project plan which I developed using Team Gantt [19] a reliable Gantt chart creation tool, the process of creating Crowd Pulse was done in phases, these phases are shown in the Gantt Chart, as well as the agile methodology example but to go over them again they are:
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
I used GitHub, as well as my own self hosted version GiTea, on a VPS (Virtual Private Server on my oracle instance) on my cloud instance. GiTea, is a selfhosted alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in Go it works across all the platforms and architectures that are supported by Go[20]. For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down or corrupt in some way.
###### Project / Issue Management
GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be used it for this exact purpose, in The Planning Section I showed an image of the Kanban View of this tool.