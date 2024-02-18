### Laws That May Apply

In this section I talk about the Laws that may or may not apply to the project, I outline which Laws and guidelines might provide issues with the project if any and which laws and guidelines may not apply.

#### GDPR

The General Data Protection Regulation (GDPR) is a legislation by the EU and EEA aimed at protecting individuals' personal data rights. Enacted in 2016 and effective since 2018, it governs data processing and protection, ensuring transparency, accuracy, and confidentiality. GDPR grants data subjects rights like access, rectification, and erasure. Organizations must appoint Data Protection Officers (DPOs), report breaches, and comply with strict fines for violations. Its global influence has prompted widespread compliance efforts and impacted data protection laws worldwide.

Since this project involves crowd detection using Wi-Fi scanning which is affected by GDPR, due to the strict regulations set out by GDPR the following apply to the project:

- **Data Collection** - This often involves, gathering potentially identifiable information, such as:
  - MAC Addresses
  - Device Names
  - Personal information
  - Location data
  - etc …
    These count as Identifiable information and as such are protected by GDPR.
- **Transparent Communication** - Anyone affected by this system needs to be properly informed.
- **Anonymity** - This system will not use personally identifiable information, it only monitors the number of "devices" in the area, not specific devices

#### DPA 2018 (Data Protection Act)

This is the UK's implementation of GDPR, providing additional specifications and exemptions. It regulates how personal data should be handled, processed, and stored, including provisions regarding the processing of special categories of personal data

> [!warning] Which may include data collected through WiFi scanning.

#### RIPA 2000 (Regulation of Investigatory Powers Act)

RIPA regulates the use of surveillance techniques by public bodies. It outlines the legal procedures for conducting surveillance and intercepting communications
#continue-later

> [!warning] Which may be applicable depending on the nature of the crowd monitoring project.

#### Human Rights Act 1998

This Act incorporates the European Convention on Human Rights into UK law. It protects fundamental rights and freedoms, including the right to privacy and the right to freedom of expression, which may intersect with the operation of crowd monitoring projects.
#continue-later

#### Information Commissioner's Office (ICO) Guidance

The ICO provides guidance on data protection laws and regulations, including GDPR compliance.

> [!warning] A crowd monitoring project should adhere to ICO guidelines to ensure lawful and ethical data processing practices.

These laws and regulations aim to ensure that crowd monitoring projects involving Wi-Fi scanning techniques comply with legal requirements, respect individuals' privacy rights, and maintain data security. It's essential for organizations undertaking such projects to carefully assess and adhere to these legal frameworks to avoid potential legal liabilities and ensure ethical conduct.

### Sussex University Code of ethics

### BCS Code of Conduct

BCS stands for (British Computer Society), this section is about the BCS code of conduct and outlines the professional standards and guidelines that members of the BCS are expected to adhere to in their practice. It provides a framework for promoting and maintaining high standards of competence, integrity, and professionalism within the field of computing. The code of conduct, addresses various aspects such as:

- confidentiality
- respect of privacy
- and responsible use of technology

#### Code of Conduct

> [!quote] Section 1 - Public Interest [21]
> You shall:
>
> 1. have due regard for public health, privacy, security and wellbeing of others and the environment.
> 2. have due regard for the legitimate rights of Third Parties.
> 3. conduct your professional activities without discrimination on the grounds of sex, sexual orientation, marital status, nationality, colour, race, ethnic origin, religion, age or disability, or of any other condition or requirement.
> 4. promote equal access to the benefits of IT and seek to promote the inclusion of all sectors in society wherever opportunities arise.

I believe I have help up this aspect of the BCS code of conduct, as In this project I have never compromised the **public health**, **privacy**, **security** and **wellbeing** of others. Third party work has properly been referenced and legitimate rights acknowledged.

> [!quote] Section 2 - Professional Competence and Integrity [21]
> You shall:
>
> 1. only undertake to do work or provide a service that is within your professional competence.
> 2. NOT claim any level of competence that you do not possess.
> 3. develop your professional knowledge, skills and competence on a continuing basis, maintaining awareness of technological developments, procedures, and standards that are relevant to your field.
> 4. ensure that you have the knowledge and understanding of Legislation\* and that you comply with such Legislation, in carrying out your professional responsibilities.
> 5. respect and value alternative viewpoints and, seek, accept and offer honest criticisms of work.
> 6. avoid injuring others, their property, reputation, or employment by false or malicious or negligent action or inaction.
> 7. reject and will not make any offer of bribery or unethical inducement

I think that I have adhered to this section of the BCS code of conduct. As I have not claimed to do work that is outside of my professional competence, I have not claimed any level of competence that I do not possess. I have ensured that I have a thorough understanding of the Legislation and have complied with such legislation.

> [!quote] Section 3 - Duty to Relevant Authority [21]
> You shall:
>
> 1.  carry out your professional responsibilities with due care and diligence in accordance with the Relevant Authority’s requirements whilst exercising your professional judgement at all times.
> 2.  seek to avoid any situation that may give rise to a conflict of interest between you and your Relevant Authority.
> 3.  accept professional responsibility for your work and for the work of colleagues who are defined in a given context as working under your supervision.
> 4.  NOT disclose or authorise to be disclosed, or use for personal gain, or to benefit a third party, confidential information except with the permission of your Relevant Authority, or as required by Legislation.
> 5.  NOT misrepresent or withhold information on the performance of products, systems or services (unless lawfully bound by a duty of confidentiality not to disclose such information), or take advantage of the lack of relevant knowledge or inexperience of others.

I have carried out this project in a professional way with care and diligence with the Relevant Authority being the University of Sussex, and have exercised professional judgement

> [!warning] I will not use Live data that may compromise individuals' privacy
> I will generate fake data to complete my testing #continue-later

I accept professional responsibility for my work on this project and have not disclosed any information for personal gain. I have not misrepresented or withheld information on the performance of the system.

> [!quote] Section 4 - Duty to the Profession [21]
> You shall:
>
> 1. accept your personal duty to uphold the reputation of the profession and not take any action which could bring the profession into disrepute.
> 2. seek to improve professional standards through participation in their development, use and enforcement.
> 3. uphold the reputation and good standing of BCS, the Chartered Institute for IT.
> 4. act with integrity and respect in your professional relationships with all members of BCS and with members of other professions with whom you work in a professional capacity.
> 5. encourage and support fellow members in their professional development.

I believe I have upheld this section of the BCS standards, as I have not taken any action that could bring the profession into disrepute. I Sought to improve my own abilities as much as I have professional standards. I believe I have upheld the representation of the BCS and acted with integrity and respect through my professional relationships.

### Privacy Considerations / Concerns of the Project

#### Ethical Issues / Considerations

During development of `Crowd Pulse` it is important to consider the ethical concerns and implement strategies to address these concerns.

##### Privacy

Due to the nature of the Crowd Pulse project it involves monitoring and analysing crowd presence and density in different locations, this could potentially raise privacy concerns among the individuals being monitored, therefore it is crucial to establish what is acceptable and what is not:

- Acceptable
  - Aggregated and anonymized data collection to ensure individual privacy is maintained.
  - Utilizing technology that focuses on crowd presence and density rather than individual identification.
- Not-Acceptable
  - Monitoring or collecting personally identifiable information[7] without explicit consent.
  - Utilizing surveillance methods that infringe upon individuals’ privacy rights.

##### Data Security

Given the nature of a system that collects and analyses user data, ensuring the security and integrity of the data is of utmost importance, as such Crowd Pulse will endeavour to use the minimal amount of user data possible to ensure there is no useful way for Crowd Pulse to be used to track individuals. In addition to holding as little identifiable data as possible, the data which is required will be thoroughly protected. Outlined below is the strategy I will be implementing to keep the minimal user data stored safe:

1. **Data Minimization**: Crowd Pulse will limit the collection of personal data to only what is necessary for the system's functionality, ensuring that the least amount of identifiable information is gathered. This aligns with privacy principles and reduces the risk associated with unnecessary data storage.
2. **Encryption and Anonymization**: Any data that is collected will be encrypted and anonymized to prevent unauthorized access and to ensure that individual identities cannot be discerned from the stored information.
3. **Compliance with Data Protection Regulations**: Crowd Pulse will adhere to all relevant data protection regulations, ensuring that the handling and storage of user data complies with legal requirements to safeguard user privacy and security.

##### Informed Consent

It is crucial to consider the issue of informed consent. Users and individuals affected by the system's monitoring should be informed about the purpose and scope of data collection and analysis. Clear communication and transparency regarding the utilization of their data, including the option to opt out, are essential ethical considerations.

This means that when / if this system is rolled out and used on the campus of a university, people who are affected by this system should be informed about the use of their data before hand.

> [!warning] This is Crucial for not infringing on the Laws outlined earlier in this section of the report
