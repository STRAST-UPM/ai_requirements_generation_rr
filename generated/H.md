# Human Requirements for AI4I4 system (spec. version 2)

## 1. Help messages during the {log-on procedure} must not aid an unauthorized user, e.g., by indicating which {parts of the data} are correct or incorrect

1.1. During the Employee authentication process, no information should be disclosed to the user that would allow unautorized users to distinguish between a valid and invalid username, passwords or allocated roles.

1.2. During the Dealer authentication process, no information should be disclosed to the user that would allow unautorized users to distinguish between a valid and invalid username or password

## 2. A security incident must be raised if a potential attempted or successful breach of {log-on controls} is detected, and, when the risk of the incident warrants it, the account shall be temporarily restricted, plus an alert shall be sent to the {account owner}, and to the {organization's system administrators}.

2.1. When a pattern of abnormal behavior in the Employee login procedure is detected during or after a login attempt, a security incident must be raised, the Security Manager must be notified, and, if the risk of the incident warrants it, the affected Employees must be notified through an alternative verified communication channel, and their user accounts must be locked.

2.2. When a pattern of abnormal behavior in the Dealer login procedure is detected during or after a login attempt, a security incident must be raised, the Security Manager must be notified, and, if the risk of the incident warrants it, the affected Dealer must be notified through an alternative verified communication channel, and their user accounts must be locked.

## 3. Physical or logical access controls must be implemented to isolate {sensitive applications, data, or systems}.

3.1. Logical access controls must be implemented to isolate Access Control data (such as schedules and vehicle registration data; stored in the Requisitions Data Store) from Dock Management data (such as unloading confirmations; stored in the Supply Vehicles Registry) and from Warehouse Management data (such as material stock and movements; stored in the Warehouse Inventory).

3.2. Physical access controls must be implemented at the premises where the physical systems that support the services are located.

3.3. Controls must be implemented that prevent access to each system or registry except from the area where it is located or its usage is required

3.4. Controls must be implemented that prevent access to any system or registry through any means different from the dedicated end-user front-end or the subsystem designed for such purpose.

3.5. Controls must be implemented that prevent actuators to accept commands coming from anywhere except the area where they are located

## 4. {Access to data} must be controlled based on {user identity, group membership, and assigned roles}

4.1. Only the Employeed with the Access Control Manager role assigned will be authorized access to data related to incoming vehicles, schedules and requested materiales.

4.2. Only the Employees with the Access Control Manager role assigned will be authorized to access the Requisitions Data Store.

4.3. Only the Employees with the Access Control Manager or the Dock Manager role will be authorized to access the Transportation Vehicles Registry.

4.4. Only the Employees with the Dock Manager role assigned will be authorized to access data related to docked vehicles, material location and tagging, and unloading confirmations

4.5. Only the Employees with the Dock Manager role will be authorized to access the Warehouse Inventory

4.6. Only the Employees with the Access Control Manager or the Dock Manager role will be authorized to read the information in the AIDC carriers of Components.

4.7. Employees' access to data must be controlled based on user identity, assigned roles and allocated privileges, except for the data that, because of its physical nature, its observation is unavoidable to them in the warehouse, dock or access control areas (e.g. plates of the incoming vehicles, material tags, etc.).

4.8. The system shall implement a user management function supporting system availability for factory employees. This function shall manage the system users lifecycle: sign-up, user data update and recovery, role assignment, unsubscription, etc. System Admin is the Employee role in charge of the user management function.

## 5. The {organization} shall maintain a record of {all privileges allocated}

5.1. The system shall maintain a record of the privileges allocated to each Employee role, including reading and operative access to system functions, terminals, data stores, readers, interrogators, client applications, robots, machinery, automated vehicles, etc.

5.2. The System Admin shall maintain the record of allocated employee privileges.

## 6. The {organization} shall regularly review {users} with privileged access rights to ensure that their {duties}, {roles}, {responsibilities}, and {competence} still justify such access

6.1. A regular review of all employees and dealers with privileged access rights must be scheduled, in order to ensure that their duties, roles, responsibilities, and competence still justify such access. The review shall be conducted by the Operations Manager.

## 7. {Connection} of {systems} to the {network} must be restricted and filtered, e.g., using firewalls.

7.1. All devices and systems, including data stores, terminals, devices, robots and industrial machinery will be connected to trusted internal networks.

7.2. Connection to untrusted perimeter networks, in particular, Internet, will be screened by using firewalls

7.3. Connection to factory systems and resources from perimeter networks will only be allowed for two business entities: Dealer and Forwarder. Specific access control systems will secure the access from the Internet for theses two entities to specific sofware funcions related to the management of Dealer's orders and the Shipping process. The resto of factory systems and resources will remain unreachable

## 8. {Network administration channels} must be segregated from {other network traffic}

8.1. All maintenance and administration network traffic must be segregated from the overlay network traffic, by using a separate network segment, access method or technology solution which is only accessible to the System Admins and Security managers.

## 9. The system shall implement cryptographic measures to safeguard information saved in data stores, terminals, devices, robots and industrial machinery by authenticating Employees identity and roles.

9.1. The system shall implement cryptographic measures to safeguard information saved in data stores, terminals, devices, robots and industrial machinery by authenticating Employees identity and roles.

9.2. The system shall implement cryptographic measures to safeguard (encryption, device authentication and anti-cloning) information saved on RFID tags and other physical carriers and their linkage to physical assets, specifically considering the radio channel.

9.3. The system shall implement cryptographic measures to safeguard (confidentiality and integrity) information transmitted over networks by using TLS over Internet protocols both in the internal LAN(s) and in connections with untrusted perimeter networks.

## 10. Establish a comprehensive key management system, including procedures for generating and protecting {cryptographic keys} and recovering {encrypted data} in case of lost, compromised, or damaged {keys}

10.1. The system shall establish a comprehensive key management system, including procedures to generate cryptographic keys to store information at the AIDC carriers, protect the keys at the system, and regenerate the contents of the AIDC carriers in case the key is not usable anymore.

10.2. The system shall establish a comprehensive key management system, including procedures to generate Employees' access keys, protect them in the system, and regenerate them if the key becomes unusable.

10.3. The Security Manager shall be the employee role in charge of managing the key management system.

