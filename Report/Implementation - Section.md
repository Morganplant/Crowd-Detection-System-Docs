### How `Crowd Pulse` Works

`Crowd Pulse` Works by first checking the permissions it has

> [!error] Potentially **Inconsistent** With other sections - #continue-later

- If `Crowd Pulse` has access to the network topology then it is able to identify the areas with the highest crowd density values, this can then be applied to an interface in which a user would more easily understand this data.
- If `Crowd Pulse` does not have the network topology then it can only generate the crowd density for the entire area (Wi-Fi network) which significantly limits it's functionality.

The system captures data to pinpoint areas with high crowd density, facilitating optimal resource allocation and space management, on the administration side. As well as creating informed users, an example of this would be a student looking for a place to eat on campus, they would then check the `Crowd Pulse` System which provides the user with the crowd density information, allowing them to make an informed decision.

> [!section]

The `Crowd Pulse` initiative aims to modernize campus operations by utilizing Wi-Fi scanning techniques to develop a solution for monitoring crowd presence and density. This implementation stands to benefit the university, staff, students, and administration. Below are the limitations of `Crowd Pulse` as a "user device" (i.e., lacking knowledge of the network structure).

> [!warning] Constraints of `Crowd Pulse` as a "User Device"
> Given its limitations as a "user" device unable to perceive the network topology, `Crowd Pulse` can only detect "personal" devices across the entire network, not individual areas.

With access to the network structure, `Crowd Pulse` can significantly enhance its capability to identify "personal" devices with greater precision. This means that instead of merely generating crowd density values for the entire campus, it can pinpoint Wireless Access Points for more localized crowd density values.

### Prototypes

#### Prototype UI

> [!example]- Example Interface - With Access to Topology
>
> > [!quote]- With Access to Network Topology
> > ![[Pasted image 20231123125302.png]]
>
> > [!quote]- Without Access to Network Topology
> > ![[Pasted image 20240228092302.png]]

### Different Way of doing things?

In this section I'll go over some of the different ways that were considered for the implementation of the project

#### Computer Vision

#### Subnet Sectioning

#### Mac Address Swap Tracking using ML

#### Time Scanning
