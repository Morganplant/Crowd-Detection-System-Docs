### How `Crowd Pulse` Works

`Crowd Pulse` Works by first checking the permissions it has
> [!warning] Go back and Cover how you export the network topology

> [!error] Potentially **Inconsistent** With other sections - #continue-later

- If `Crowd Pulse` has access to the network topology then it is able to identify the areas with the highest crowd density values, this can then be applied to an interface in which a user would more easily understand this data.
- If `Crowd Pulse` does not have the network topology then it can only generate the crowd density for the entire area (Wi-Fi network) which significantly limits it's functionality.

The system captures data to pinpoint areas with high crowd density, facilitating optimal resource allocation and space management, on the administration side. As well as creating informed users, an example of this would be a student looking for a place to eat on campus, they would then check the `Crowd Pulse` System which provides the user with the crowd density information, allowing them to make an informed decision.

> [!section]

The `Crowd Pulse` initiative aims to modernize campus operations by utilizing Wi-Fi scanning techniques to develop a solution for monitoring crowd presence and density. This implementation stands to benefit the university, staff, students, and administration. Below are the limitations of `Crowd Pulse` as a "user device" (i.e., lacking knowledge of the network structure).

> [!warning] Constraints of `Crowd Pulse` as a "User Device"
> Given its limitations as a "user" device unable to perceive the network topology, `Crowd Pulse` can only detect "personal" devices across the entire network, not individual areas.

With access to the network structure, `Crowd Pulse` can significantly enhance its capability to identify "personal" devices with greater precision. This means that instead of merely generating crowd density values for the entire campus, it can pinpoint Wireless Access Points for more localized crowd density values.

> [!example]- Example Interface - With Access to Topology
>
> > [!quote]- With Access to Network Topology
> > ![[Pasted image 20231123125302.png]]
>
> > [!quote]- Without Access to Network Topology
> > ![[Pasted image 20240228092302.png]]

### Different Way of doing things?

> [!error] Title change to Extension / add ons #continue-later

In this section I'll go over some of the different ways that were considered for the implementation of the project

#### Computer Vision

Using computer vision is an option, that could be explored by using some code to monitor the people who are entering and exiting buildings it would give a good indication on how many people are inside the building. This has the drawback of not being able to monitor people who are outside of areas with cameras, and so would be very difficult to get an accurate measurement for the crowd density.

This would also require some form of Machine Learning to identify people within a crowd and be able to distinguish the different people it comes across, similar to a facial recognition system which raises security concerns.

#### Subnet Sectioning

Implementing subnet sectioning for different areas of the campus within the Wi-Fi network infrastructure could significantly enhance the efficacy of crowd detection systems like Crowd Pulse. By allocating specific subnet addresses to distinct zones, devices connecting to wireless access points would automatically be assigned to their corresponding subnet based on their location. This approach streamlines the scanning process, enabling the system to pinpoint user devices more accurately and thereby provide more precise readings for crowd density in each designated area. Such precise localization of user devices within the network can greatly improve the effectiveness of crowd monitoring and management efforts on campus. Additionally, this method enhances crowd management, event safety, and infrastructure monitoring, ensuring comprehensive coverage and efficient resource allocation. This also means that Crowd Pulse would not require network topology privileges to work effectively.

#### Mac Address Swap Tracking using ML

Utilizing Machine Learning presents a promising avenue for addressing the MAS Problem most network scanning software encounters (Mac Address Swapping). A potentially viable strategy entails conducting multiple scans during off-peak hours to comprehensively map out the infrastructure. By meticulously filtering known devices, ML algorithms could hone in on outliers, specifically MAC address swaps, with greater precision. For instance, if a device suddenly disappears from the network while another device with a different MAC address emerges simultaneously, it could indicate a MAS event. Which could help in identifying "people"

#### Time Scanning

During the quieter hours of the night, we would conduct periodic network scans to establish a foundational baseline of the networking devices present. These scans encompass a comprehensive range of network components, including switches, routers, and access points, etc. Providing a detailed overview of our networking infrastructure. These initial scans serve as a foundational reference point for subsequent scans aimed at crowd detection. By identifying and cataloguing the devices present during these off-peak scans, I can effectively filter out known entities from our crowd detection algorithms, thereby augmenting the accuracy and reliability of our monitoring systems.

### What did happen vs what could have

#continue-later
