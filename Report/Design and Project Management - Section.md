### Diagrams

> [!abstract]- User Flow Diagram
>
> ```mermaid
> flowchart TD
> A[Start]
> B[User Chooses to View Crowd Density]
> C{Crowd Pulse Has Topology Access}
>  C_1[Get Network Topology]
>  C_2[Filter out Networking Devices]
>  C_3[Map Connected Devices to Access Points]
>  C_4[Generate Crowd Density Values for individual Access Points]
>
>  D_1[Scan Entire Network]
>  D_2[Filter out Networking Devices]
>  D_3[Generate Crowd Density for Entire Network]
> E[Display Data To User]
> F[End]
> A --> B
> B --> C
> C --"Yes"--> C_1
> C --"No"--> D_1
>     C_1 --> C_2 --> C_3 --> C_4 --> E
>     D_1 --> D_2 --> D_3 --> E
> E --> F
> ```

> [!abstract]- Entity Relationship Diagram
>
> ```mermaid
> erDiagram
>     NETWORK {
>         string network_id
>         string network_name
>     }
>     DEVICE {
>         string device_id
>         string device_name
>         string device_type
>     }
>     ACCESS_POINT {
>         string access_point_id
>         string access_point_name
>     }
>     USER {
>         string user_id
>         string user_name
>         string user_role
>     }
>     INTERFACE {
>         string interface_id
>         string interface_type
>     }
>     MAPPING {
>         string mapping_id
>         string access_point_id
>         string device_id
>     }
>
>     NETWORK ||--o{ DEVICE : "exists in"
>     DEVICE ||--o{ ACCESS_POINT : "connected to"
>     NETWORK }|--|| ACCESS_POINT : "exists in"
>     DEVICE }|--|| MAPPING : "mapped to"
>     ACCESS_POINT }|--|| MAPPING : "mapped to"
>     INTERFACE }|--|| MAPPING : "views"
>     USER }|--|| INTERFACE : "views"
> ```

> [!example]- Example Network Topology map
>
> ```mermaid
> graph TD
>     A[Network] --> B[Router]
>     A --> C[Switch1]
>     A --> D[Switch2]
>     A --> E[Switch3]
>     A --> F[Wireless AP1]
>     A --> G[Wireless AP2]
>     A --> H[Wireless AP3]
>     B --> R1[Desktop1]
>     B --> R2[Laptop1]
>     B --> R3[Printer1]
>     C --> S1[Desktop2]
>     C --> S2[Laptop2]
>     C --> S3[Printer2]
>     D --> T1[Desktop3]
>     D --> T2[Laptop3]
>     D --> T3[Printer3]
>     E --> U1[Desktop4]
>     E --> U2[Laptop4]
>     E --> U3[Printer4]
>     F --> V1[Desktop5]
>     F --> V2[Laptop5]
>     F --> V3[Printer5]
>     G --> W1[Desktop6]
>     G --> W2[Laptop6]
>     G --> W3[Printer6]
>     H --> X1[Desktop7]
>     H --> X2[Laptop7]
>     H --> X3[Printer7]
>     B --> Y1[Smartphone1]
>     B --> Y2[Tablet1]
>     B --> Y3[Smartwatch1]
>     C --> Z1[Smartphone2]
>     C --> Z2[Tablet2]
>     C --> Z3[Smartwatch2]
> ```

### How the Project is managed

I used a multitude of different ways to manage my project. For source control and backups, I used GitHub [11], my own self-hosted server [12], and Google Drive [13]. Using GitHub allowed me to utilize GitHub issues and projects, which allowed me to track tasks easily, an example of which was the Kanban board below. I used my Google Drive as well as my own server to store backups periodically to avoid backup loss if something were to happen to GitHub. This way, I had a higher degree of redundancy baked into the project.

#### Planning

##### Initial Proposal and Requirements Analysis

`Crowd Pulse` began with the creation of a comprehensive project proposal. This proposal outlined the project's objectives, scope, and deliverables. Following this, a thorough analysis of requirements was conducted to identify the specific technologies, tools, and skills necessary for successful completion. This initial phase laid the groundwork for the project's planning and execution.

##### Development of Project Plan

With a clear understanding of the project's parameters, a detailed project plan was developed. This plan delineated tasks, timelines, and milestones, providing a roadmap for the project's progression. Emphasis was placed on time management and self-discipline, with the creation of a personalized schedule to ensure steady progress. Contingency plans were also formulated to address potential roadblocks, ensuring adaptability in the face of challenges.

##### Execution and Monitoring

Throughout the project, I followed the established project plan and when I encountered Limitations, changed the plan, timelines and milestones. Regular self-assigned checkpoints were integrated into the process to evaluate progress and adjust strategies as needed. This was accompanied regular meetings with my supervisor. This proactive approach ensured that the project remained on track toward successful completion, equipping me with valuable practical skills and academic achievement.

#### Kanban

![[Pasted image 20240228085556.png]]

#### Project Plan

In undertaking the crowd pulse project, it is important to establish a planned methodology, therefore I have come up with the following diagrams and graphs to show how I will proceed with the Crowd Pulse Project.

I have worked with different methodologies before namely agile and waterfall, so I will use a combined approach in the following way, due to the nature of the fixed timeline of the project believe that a waterfall methodology would suite the project well, however I will be using an agile methodology when it comes to the Designing and Coding Phases, this is due to the nature of these phases, the design phases is one that requires rapid development in short amounts of time with a high quality return, in this case using an agile methodology makes sense as it allows me to rapidly prototype designs and evaluate them in a much more efficient way than using a waterfall method. The Same applies to the coding phase of the project it greatly hinder my abilities, so I will be focused on the agile cycle of development when entering the Coding phase.

> [!abstract]- Initial Project Gantt Chart
> ![[Pasted image 20231123123439.png]]

##### Project Phases

As described above in the Gantt Chart which I developed using Team Gantt[14] The Process of creating Crowd Pulse will be done in phases, these phases are shown in the Gantt Chart, but to go over them again they are:

- <span style="color:#92d050">Ideas / Research Phase</span>
  - In this phase I will be generating ideas looking for similar projects and completing documentation, I will also be more focused on how I will create the end goal rather than what I do to create it.
- <span style="color:#00b0f0">Design Phase</span>
  - During this phase I will be using the agile methodology to generate designs of how the product will look from a user experience point of view, as well as working on the designs for how other parts of the System will function, e.g. Diagrams and prototyping.
- <span style="color:#ffc000">Implementation / Coding</span>
  - During this Phase I will again be using the agile methodology to rapidly produce code that will follow the designs and prototypes developed in the design phase, during this phase I will also be testing as and when required although there will be an entire phase dedicated to testing these tests will be focused on the code specifics.
- <span style="color:#7030a0">Testing</span>
  - In this phase I will test all aspects of the product and work out any bugs that need to be fixed. I also hope to be able to test my product using a group of my peers that way I will be able to replicate the environment it would be used in, I will then be fixing issues that arise due to the testing done by the group of peers.
- <span style="color:#ff0000">Deployment</span>
  - This Phase is dedicated to deploying the product into the wild, in this phase the product is ready, as been thoroughly tested, and is now ready for the users to have access, I will be focused on implementing the code as well as potentially integrating it with the existing systems available.

##### Source Control - GitHub & GiTea

As discussed earlier I will be using GitHub, as well as my own self hosted server, on my server I run a self hosted version of GitHub named GiTea [15]. GiTea, is an alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in go it works across all the platforms and architectures that are supported by Go which is a lot). For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down.

###### Project / Issue Management

GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be using it for this exact purpose.

#### Backups and Source Control

As discussed earlier I will be using GitHub, as well as my own self hosted server, on my server I run a self hosted version of GitHub named GiTea [15]. GiTea, is an alternative of GitHub, the primary goal of GiTea is to make an easy, fast, painless self hosted git service, and as GiTea is written in go it works across all the platforms and architectures that are supported by Go which is a lot). For this project I will only be using GiTea as an extra level of protection or redundancy, This is so that I will always have some form of the project available to me that is under source control, allowing me to have a backup of the project available even if GitHub where to go down.

GitHub has a feature called projects, these are things that can be synced to a repo to allow you to manage it's issues and track your progress I will be using it for this exact purpose.
