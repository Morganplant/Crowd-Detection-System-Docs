## Ethics
### Laws That May Apply

In this section I talk about the Laws that may or may not apply to the project, I outline which Laws and guidelines might provide issues with the project if any and which laws and guidelines may not apply, and what I did about it.
#### GDPR
The General Data Protection Regulation (GDPR) isa legislation by the EU and EEA aimed at protecting individuals' personal data rights, it was enacted in April of 2016. It governs data processing, protection, ensures transparency, and confidentiality.

GDPR, or the General Data Protection Regulation, is a set of laws designed to protect the privacy and personal data of individuals. It aims to ensure that personal data is processed transparently and fairly, while also giving individuals more control over their own data[13].

GDPR grants data subjects some of the following rights:
1. **Right of Access** - To know if your data is being processed and access to it.
2. **Right to Rectification** - Allows you to request the rectification of inaccurate or incomplete data.
3. **Right to Erasure** - Allows you to request the removal of your data.
These rights are designed to empower individuals to have more control over their own personal data and it's use. Essentially GDPR is about providing a better safeguard for people's personal information in today's digital age.

Due the the project's nature it could be speculated that the project uses, personal data to achieve the monitoring of people. However I made a conscious decision to avoid using as much personal information as possible, the only data collected is the number of devices under a specific wireless access point, and there is no use of personally identifiable data.

However, the Crowd pulse system does collect potentially identifiable data:
- MAC addresses - used only to identify the device vendor
- Device IP address - used to identify unique devices
- Device Name - used to check if the device is of a specific model / make
This data is only used to identify vendors, to disregard networking infrastructure devices.
#### DPA
The 2018 Data Protection Act or DPA serves to update and modernize data protection laws within the UK, aligning them with the GDPR of the EU. The act regulates the processing of personal data and lays down rules regarding how organizations collect, handle and store personal data[14].

The act applies to 'Personal Data' which refers to information that relates to individuals. It empowers individuals with rights similarly to how GDPR does so. The act establishes a regulatory framework for data protection enforcement and designates responsibilities to the ICO (information Commissioner's Office) to oversee compliance.

As Stated Earlier Crowd Pulse only collects identifying data, for the prepose of removing networking infrastructure devices from the crowd density.
#### ICO Guidance
As mentioned earlier the ICO or Information Commissioner's Office can provide guidance on data protection laws and regulations, including GDPR compliance.
These laws and regulations make sure that crowd monitoring projects involving Wi-Fi scanning techniques comply with legal requirements, respect individuals' privacy rights[15].
### BCS Code of Conduct
BCS stands for (British Computer Society), this section is about the BCS code of conduct and outlines the professional standards and guidelines that members of the BCS are expected to adhere to in their practice. It provides a framework for promoting and maintaining high standards of competence, integrity, and professionalism within the field of computing[16]. The code of conduct, addresses various aspects such as:
- confidentiality
- respect of privacy
- and responsible use of technology
#### Code of Conduct

> [!quote] Section 1 - Public Interest
> You shall:
> 1. have due regard for public health, privacy, security and wellbeing of others and the environment.
> 2. have due regard for the legitimate rights of Third Parties.
> 3. conduct your professional activities without discrimination on the grounds of sex, sexual orientation, marital status, nationality, colour, race, ethnic origin, religion, age or disability, or of any other condition or requirement.
> 4. promote equal access to the benefits of IT and seek to promote the inclusion of all sectors in society wherever opportunities arise.
[16]

> [!quote] Section 2 - Professional Competence and Integrity
> You shall:
> 1. only undertake to do work or provide a service that is within your professional competence.
> 2. NOT claim any level of competence that you do not possess.
> 3. develop your professional knowledge, skills and competence on a continuing basis, maintaining awareness of technological developments, procedures, and standards that are relevant to your field.
> 4. ensure that you have the knowledge and understanding of Legislation\* and that you comply with such Legislation, in carrying out your professional responsibilities.
> 5. respect and value alternative viewpoints and, seek, accept and offer honest criticisms of work.
> 6. avoid injuring others, their property, reputation, or employment by false or malicious or negligent action or inaction.
> 7. reject and will not make any offer of bribery or unethical inducement
> [16]

> [!quote] Section 3 - Duty to Relevant Authority
> You shall:
> 1.  carry out your professional responsibilities with due care and diligence in accordance with the Relevant Authority’s requirements whilst exercising your professional judgement at all times.
> 2.  seek to avoid any situation that may give rise to a conflict of interest between you and your Relevant Authority.
> 3.  accept professional responsibility for your work and for the work of colleagues who are defined in a given context as working under your supervision.
> 4.  NOT disclose or authorise to be disclosed, or use for personal gain, or to benefit a third party, confidential information except with the permission of your Relevant Authority, or as required by Legislation.
> 5.  NOT misrepresent or withhold information on the performance of products, systems or services (unless lawfully bound by a duty of confidentiality not to disclose such information), or take advantage of the lack of relevant knowledge or inexperience of others.
> [16]

> [!quote] Section 4 - Duty to the Profession
> You shall:
> 1. accept your personal duty to uphold the reputation of the profession and not take any action which could bring the profession into disrepute.
> 2. seek to improve professional standards through participation in their development, use and enforcement.
> 3. uphold the reputation and good standing of BCS, the Chartered Institute for IT.
> 4. act with integrity and respect in your professional relationships with all members of BCS and with members of other professions with whom you work in a professional capacity.
> 5. encourage and support fellow members in their professional development.
> [16]

I believe that I have upheld the BCS code of conduct during the development of Crowd Pulse. Once again the crowd pulse project only utilises the following data, to specifically remove networking infrastructure the crowd data:
- **MAC addresses** - used only to identify the device vendor to remove networking devices
- **Device IP address** - used to identify unique devices
- **Number of Devices** - used to create crowd density values
### Privacy Considerations / Concerns of the Project

#### Ethical Issues / Considerations

During the Crowd Pulse Project it was important to me that I consider the ethical implications and concerns before implementing a system like this. Due to the nature of the Crowd Pulse project it involved monitoring and analysing crowd presence and density in different locations, this could potentially raise privacy concerns among the individuals being monitored, therefore it was important to me that I decide on what is acceptable and what was not:
**Acceptable**
- Aggregated and anonymized data collection to ensure individual privacy is maintained
- Utilizing technology that focuses on crowd presence and density rather than individual identification
**Un-Acceptable**
- Collecting and storing personally identifiable data for the purpose of tracking individuals.
- Utilizing surveillance methods that infringe on privacy rights
- Using Live Data during the development process
##### Data Security
Given the nature of the system I wanted to ensure that the data being stored and used did not have any meaningful way of identifying individuals, Outlined below is the strategy I used to keep the data stored safe and secure.
1. **Data Minimization**: Crowd Pulse will limit the collection of personal data to only what is necessary for the system's functionality, ensuring that the least amount of identifiable information is gathered. This aligns with privacy principles and reduces the risk associated with unnecessary data storage.
2. **Encryption and Anonymization**: Any data that is collected will be encrypted and anonymized to prevent unauthorized access and to ensure that individual identities cannot be discerned from the stored information.
3. **Compliance with Data Protection Regulations**: Crowd Pulse will adhere to all relevant data protection regulations, ensuring that the handling and storage of user data complies with legal requirements to safeguard user privacy and security.
