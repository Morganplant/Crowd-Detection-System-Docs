### How `Crowd Pulse` Works

`Crowd Pulse` Works by first checking the permissions it has

> [!error] **Inconsistent** - With other sections - #continue-later

- If `Crowd Pulse` has access to the network topology then it is able to identify the areas with the highest crowd density values, this can then be applied to an interface in which a user would more easily understand this data.
- If `Crowd Pulse` does not have the network topology then it can only generate the crowd density for the entire area (Wi-Fi network) which significantly limits it's functionality.

The system captures data to pinpoint areas with high crowd density, facilitating optimal resource allocation and space management, on the administration side. As well as creating informed users, an example of this would be a student looking for a place to eat on campus, they would then check the `Crowd Pulse` System which provides the user with the crowd density information, allowing them to make an informed decision.

> [!section]

The `Crowd Pulse` initiative aims to modernize campus operations by utilizing Wi-Fi scanning techniques to develop a solution for monitoring crowd presence and density. This implementation stands to benefit the university, staff, students, and administration. Below are the limitations of `Crowd Pulse` as a "user device" (i.e., lacking knowledge of the network structure).

> [!warning] Constraints of `Crowd Pulse` as a "User Device"
> Given its limitations as a "user" device unable to perceive the network topology, `Crowd Pulse` can only detect "personal" devices across the entire network, not individual areas.

With access to the network structure, `Crowd Pulse` can significantly enhance its capability to identify "personal" devices with greater precision. This means that instead of merely generating crowd density values for the entire campus, it can pinpoint Wireless Access Points for more localized crowd density values.

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

### Prototypes

#### Prototype UI

### How the Project is managed

#### Planning

#### Backups

##### GitHub

##### GitTea

##### Cloud Backups

##### Source Control
