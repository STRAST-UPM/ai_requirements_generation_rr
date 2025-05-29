# Project AI4I4 – Automated Identification for Industry 4.0

AI4I4 (Automated Identification for Industry 4.0) is a project that applies Internet of Things technologies to Industry 4.0 (following the Industrial Internet of Things paradigm), stressing the relevance of cybersecurity properties. Specifically, the project will focus on the use of Automatic Identification and Data Capture (AIDC) technologies in the various movement processes of Parts, Materials and finished Cars at a car factory. This document presents a first version of the functional specification, which will be used as an artifact for the definition and validation of cybersecurity requirements.

Car manufacturing is a complex process that involves producing multiple Parts, assembling them on an Assembly Line, and delivering the finished Car for distribution. In this process, a series of external and internal logistic subprocesses are necessary for the reception of inbound Materials and Parts, the movement and storage thereof as well as of finished (manufactured) Cars within the different Assembly Lines involved in the manufacturing process, and the delivery of outbound finished Cars. These internal processes are carried out through an assortment of in-plant handling vehicles that combine automated equipment (e.g., loading robots, automated guided vehicles aka AGVs) and operator tasks (e.g., using forklifts, driving the finished Cars themselves); currently, a combination of both is most common, although the automatic component is increasingly significant.

The overall business process of Car manufacturing and distribution encompasses several entities related among them (including different agents, documents exchanged between one another, the Cars themselves, etc.) which address the overall flow from the incoming Parts and Materials, through the assembly process, to the eventual sale and delivery of the finished Car, namely:

- Factory: The overarching entity that encompasses the entire facility where the actual production of Cars takes place. The Factory comprises specialized areas for moulding and welding Materials, multiple Assembly Lines where Parts of a given Model are assembled into a finished Car whose quality is controlled, a Warehouse that stores a stock of Parts and Materials, unloading and loading Docks to receive Materials and Parts and deliver finished Cars, an Access Gate to control the access of Supply Vehicles bringing Parts and Materials to the Factory, and a Finished Car Yard to store finished Cars before they are shipped.
- Car Manufacturer: The primary entity responsible for Car production, owner of the Factory and holder of the rights for the Make and Model.
- Make: Represents the brand or a range of Cars produced by the Car Manufacturer.
- Model: Represents specific variants or designs implemented under the Make.
- Car: Each product unit (which implements a given Model) built in the Factory and delivered to a Dealer.
- Employee: Individuals hired by the Factory to perform the manufacturing work and various tasks associated with the production of Cars.
- Manager: An Employee in charge and in control of one or more processes in the Factory, who monitors the process and oversees other Employees.
- Worker: An Employee who executes manual tasks within one or more processes in the Factory, with the help of automated information or mechanical tools.
- Provider: This is a general classification that encompasses both OEMs (Original Equipment Manufacturers) and Material Providers.
- OEM (Original Equipment Manufacturer): A type of Provider that supplies specialized Parts integral to the Car manufacturing process.
- Material Provider: Another type of provider, which supplies the raw Materials necessary to produce Car Parts and the Cars themselves.
- Requisition: a request made by the Car Manufacturer to the Provider, indicating a need for Materials or Parts.
- Dealer: retail agent that orders Cars from the Factory to sell them to the end customer. They place Purchase Orders for Cars based on their stock needs and market demand.
- Purchase Order: a document issued by a Dealer to a Factory requesting a certain number and type of Cars (units of a given Model) for purchase and shipment, to be delivered at an expected delivery date and location.
- Forwarder: A logistic entity that delivers Cars, acting as an intermediary responsible for the transportation of Cars from the Factory to the Dealer.  
- Logistics Terminal: A facility where Cars are temporarily stored, handled, sorted and transferred to the car carriers (trains, trucks, ships…) that will deliver them to the Dealers. The Logistics Terminal intermediates between the Factory and the car carriers for the shipment of finished Cars. In our case, the Logistics Terminal is operated by the Forwarder and it’s physically located next to the Factory, but independent from it.
- Waybill: A document issued by the Forwarder for the shipment of Cars, which includes important details about the shipment.

For these processes to flow without interruptions and to maintain quality control of the manufacturing, it is necessary for the Parts, the Cars, and Supply Vehicles to have a specific, semantically unambiguous, and machine-readable identification attached to it. AI4I4 addresses this need through automatic identification and data capture (AIDC) technologies supported by an assortment of sensors, along with actuators that carry out different activities throughout the manufacturing process. These technologies may include the use of different physical data carriers, such as passive or active radio frequency identification (RFID) tags or two-dimensional optical codes (data matrix), as well as other technologies, such as general-purpose input/output (GPIO) sensors/actuators that can monitor and control physical actions within the manufacturing environment, physical alert signalling (andon), controlled barriers, etc. AI4I4 focuses on the identification processes that support manufacturing logistics, but it doesn’t address the detailed operations of the manufacturing process itself.

We will divide the process under study into three stages, each of which will be supported by a separate subsystem that address AIDC needs in the respective context: inbound logistics and reception of Components, Car assembly, and finished Car exit and outbound logistics.

## Inbound logistics and reception of Components

A Car is composed of multiple Components. Some are manufactured externally (in other manufacturing plants owned by the same Car Manufacturer or by external suppliers) and arrive at the Factory through provisioning logistic processes. In other cases, Parts are manufactured on a press line within the Factory (where the Part is moulded from raw Materials, such as metal or plastic). In either case, our system does not deal with the manufacturing or procurement processes of Parts. Instead, it is only interested in Components from the point of view of their movements since they arrived at the Factory to be stored, or when they are retrieved to be assembled onto a Car. For that aim, Parts or raw Materials must be taken delivery of once they arrive at the Factory in a Supply Vehicle (e.g. delivery van, cargo truck, freight wagon) that unloads the freight at a given Dock, as instructed by the signals available in the facility, which provide indications according to manual and automated rules. In the internal storage process, batches of the same type of Parts or Materials are loaded onto a rack or platform, from which they will move to the internal Warehouse. Both the Parts and the racks must be equipped with automatic identification mechanisms so that the inventory of Parts is always known and decisions about their movement can be made. Depending on the physical characteristics of each Part, the size of the rack, the combined weight (measured on a weighing line), and the use that will be made of the Parts in the Factory, an intelligent algorithm decides the specific place in the rack where the Part will be stored.

- The Access Gate represents the starting point for the inbound logistic process. The Access Gate enforces the authorization of all incoming and outgoing traffic into and out of the Factory premises. It is managed by an Access Control Manager, who verifies and registers the entry of Supply Vehicles.
- Access Control Manager: a Factory Employee responsible for managing the Access Gate. This individual validates the entry of Supply Vehicles, often by cross-checking the Delivery Notes shown by Supply Vehicle drivers, ensuring that only scheduled and permitted Supply Vehicles enter the Factory premises.
- Supply Vehicle: represents the various types of vehicles (delivery vans, freight trucks, etc.) that deliver Components to the Factory. A Supply Vehicle is driven by a driver that usually works for an external freight carrier company. Each Supply Vehicle is checked and registered upon entry by the Access Control Manager.
- Provider: source of the Components being delivered to the Factory. Each Supply Vehicle is associated with a Provider. Providers can be OEMs or Suppliers.
- Delivery Note: Accompanying each shipment is a Delivery Note, an essential document that typically lists the Components being delivered, quantities, and other relevant information such as Requisition identifiers and delivery schedules. It serves as a record for the transaction between the Provider and the Factory.
- Dock: physical location within the Factory where Components are unloaded from Supply Vehicles. It acts as an interface point between the external supply chain and the Factory's internal logistics.
- Dock Manager: a Factory Employee that oversees the operations at the Dock, managing the unloading of Components from the Supply Vehicles and their subsequent movement to storage in a Warehouse or directly to the production Assembly Lines.
- Warehouse: storage area within the Factory where Components are held until they are needed on the production floor. It serves as a buffer for stock and is crucial for maintaining the flow of Components for manufacturing processes.
- Component: each individual item that is delivered to the Factory and will be used in the manufacturing of Cars, e.g. engine parts, electronic modules, sheets of metal, or lubricant grease. They can be further categorized into Parts and Materials:
-- Parts refer to pre-manufactured items that will be assembled to create the finished Car.
-- Materials refer to the raw inputs that are processed within the Factory to create the Parts.
- Workers: individuals working in the Factory’s Warehouse and Dock, responsible for various tasks such as operating machinery to unload, store, and retrieve Components for use in the Factory.

Several use cases have been identified in the inbound logistic management subsystem, which address the movement of Components from arrival to storage and their eventual use in the manufacturing process.

**Control Access of Supply Vehicles**: This use case involves the initial check-in of Supply Vehicles when entering the Factory, including the access control and physical security measures to be enforced at the Access Gate. When a Supply Vehicle arrives at the Factory, it is first identified and logged into the system: this could include scanning RFID tags, reading barcodes, or using other AIDC technologies to ensure that only authorized Supply Vehicles enter the facility. This can be done by cross-checking Delivery Notes and Supply Vehicle identification against Requisitions. It involves an Access Control Manager, who oversees the process and ensures that all incoming Supply Vehicles are accounted for and registered appropriately.

1. Upon arrival at the facility of the Factory, the driver of the Supply Vehicle approaches the Access Gate, where a camera reads its license plate.
2. The Access Control Manager requests the driver their identification and the delivery documentation, outside the system.
3. The driver provides the necessary documents, which shall include a Delivery Note.
4. The Access Control Manager scans the documents and verifies them in the system against the scheduled Requisitions for Components.
5. The system checks the information, approves the entry, assigns an unloading Dock, and logs the arrival time, data of the Supply Vehicle and its driver, and details of the Delivery Note and a reference to the associated Requisition.

The gate opens, and the Supply Vehicle is allowed to enter. The signals on the Factory direct the Supply Vehicle driver to the unloading Dock. Internal barriers and gates in the way to the allocated Dock will open automatically after reading the license plate of the Supply Vehicle. License plate readers will also instruct the overhead door at the assigned Dock to open and signal that the Supply Vehicle is ready for unloading.

**Manage Unloading and Storage of Components**: After the access of Components and Supply Vehicles is controlled, the next step is the unloading and storage of these Components, which is performed at the Dock. The Dock Manager plays a crucial role in this use case, managing the unloading process from the Supply Vehicles, which possibly combines automated means with manual labour. Once unloaded, Components are checked into the system and stored in the Warehouse, with their location and status updated in the Warehouse Inventory. This ensures that Components are readily available and easily retrievable for the Assembly Line when needed.

1. The Supply Vehicle arrives at the designated Dock.
2. The Dock Manager meets the Supply Vehicle and oversees the unloading process.
3. Warehouse Workers, along with automated systems, begin unloading the Components from the Supply Vehicle.
4. Once the Components are unloaded, a Dock Manager scans their tags to register them in the system. In general, Factory Employees use a front-end application to interface with the Factory system in order to carry out tasks and manage processes and subprocesses. The interface application will implement different functions depending on the responsibilities and role of the current user.
5. The system updates the Warehouse Inventory and assigns storage locations based on the type of Component and the current layout of the Warehouse.
6. Workers transport the Components to the assigned locations and confirm in the system their placement, ensuring everything is correctly stored and ready for later retrieval.

**Control Exit of Supply Vehicles and Components**: This use case deals with the exit procedures for Supply Vehicles when leaving the inbound area, and potential Component returns. Once Components are logged and stored, the system needs to ensure that the exit of any Supply Vehicle or Component is also controlled and recorded, including the checkout of vehicles and freight (e.g. rejected and returned Materials or Parts) and the enforcement of physical security and access control measures at the Access Gate.

1. After unloading the Components, the Supply Vehicle is ready to leave the Dock.
2. The Dock Manager provides the system with a confirmation of successful unloading and receipt of Components. Materials and Parts may also be rejected upon arrival and sent back to the Provider upon damage detected, the received load not matching the requested Components, etc.
3. The system processes the confirmation and signals for an exit check.
4. The Access Control Manager conducts a final check, ensuring no Components are leaving with the Supply Vehicle (unless they go along a explicit authorization by the Dock Manager).
5. The system logs the departure time of the Supply Vehicle and updates the Dock's availability status.
6. The Access Gate opens, and the Supply Vehicle exits the Factory facility, completing the inbound process.

These use cases are supported by the following datastores, with the following interactions from actors and system:

- Requisitions Data Store. The Access Control Manager uses the Requisitions Data Store to cross-reference incoming shipments and check the Supply Vehicles against currently open Requisitions. The system updates the Requisitions Data Store as Components are checked in, reflecting the fulfilment of Requisitions for Components.
- Supply Vehicles Registry. This data store is used by both Access Control Manager and Dock Manager to log details of movements of Supply Vehicles (every time a Supply Vehicle enters or exits), including times, quantities, and conditions. Upon each unloading and action, traces are recorded that detail what Components were received, from whom, when, and where they were put to storage. The system processes the data to maintain an accurate and up-to-date record Components received, accessible to authorized personnel. Regular audits are conducted, with the system generating reports based on the recorded data to ensure accuracy and consistency.
- Warehouse Inventory. The Dock Manager utilizes this data store to track the location and status of Parts and Materials within the Warehouse. As Components are placed in their storage locations, their details are scanned by Warehouse Workers using handheld devices, ensuring that all movements are logged and recorded in real-time. This could involve updating the precise location, quantity, status, and special storage conditions of each item. The system keeps the data store current and adjusts the information about overall stock levels in real time, reflecting changes as Components are moved or used in the production process. This information is critical for efficient Warehouse operations and for the quick retrieval of Components as they are needed in the production process, and to provide insights for space optimization and future storage planning.

## Car assembly

Each time the Assembly Line needs Parts of a given type, a rack is transported from the internal Warehouse, using in-plant handling vehicles (usually robotized, e.g. AGVs). On the Assembly Line, the Car assembly takes place, requiring identification of the installed Parts. When the Assembly Line finishes assembling the Car, an event triggers the assignment of a new identifier to the Car, its recording on a physical AIDC carrier (e.g., RFID), and a robotized applicator arm places the carrier on the Car. Once assembled, it goes under a quality control process that is carried out by a Worker equipped with a handheld device where they register the various controls conducted and, eventually, approve its delivery.

The entities involved in the assembly process within the Car manufacturing facility include several entities that represent the flow of Components and their assembly and transformation process into finished Cars:

- Component: Components are the individual Parts or Materials that are assembled into the finished Car. They come from the inbound logistic process and are stored in the Warehouse before being used on the Assembly Line.
- Warehouse: it serves as the primary storage area for Components that will be used in the Car assembly process. who  
- Warehouse Manager: This role is responsible for managing the Warehouse operations, which includes organizing the storage of Components, maintaining stock levels, and coordinating the distribution of Components to the Assembly Line. The Warehouse Manager is responsible for overseeing the stock and making sure that the right Components are available when needed, ensuring that Components are supplied to the Assembly Line in accordance with the production plan.
- Workers: Workers represent the workforce in the Warehouse and on the Assembly Line. They are the individuals who perform various hands-on tasks in the Car assembly process, such as operating machinery, handling Materials, and placing Parts into Cars. Workers at the Assembly Line work along various Workstations, each with specific assembly procedures allocated.
- AGV (Automated Guided Vehicle): AGVs are used to transport Components from the Warehouse to the Assembly Line. They follow predefined paths and are an essential part of the logistics within the Factory, ensuring that Components move efficiently.
- Assembly Line: This is where the actual assembly of the Car takes place. Components are put together to form complete Cars. The Assembly Line is a sequence of Workstations where different steps of the assembly process are completed.
- Workstation: these are specific areas along the Assembly Line where particular assembly tasks are carried out. A conveyor belt transports a Car being manufacturing from one Workstation to the next along the Assembly Line. Each Workstation is equipped with the necessary tools and equipment, and Workers at these Workstations specialize in specific assembly tasks.
- Robot: In modern Assembly Lines, Robots are often used to perform precise or repetitive tasks that can be automated. They work alongside human Workers and are an integral part of the assembly process.
- Plant Manager: The Plant Manager is responsible for the overall management of the Factory. They oversee all operations and coordinate them between different departments, ensure that production targets are met, and maintain quality standards throughout the Car assembly process.

The Warehouse Manager, Plant Manager, and the Assembly Line Workers rely on the system to track the journey of each Part until it becomes a segment of a finished Car, through the following use cases:

**Manage Warehouse Output and Distribution of Components**:

- The day at the Car manufacturing Factory begins with the Warehouse Manager reviewing the day's production plan. It's a blueprint that that tells what Components are needed on the Assembly Line and when; thus, it dictates the rhythm of the movement of Components from the Warehouse to the Assembly Line. The Warehouse Manager must ensure that Components flow in sync with the production plan.
- The Warehouse Manager broadcasts their commands to the Warehouse Workers, allocating tasks and setting the day's priorities according to the day's demand as recorded in the day’s production plan. Inside the Warehouse, Workers start selecting the necessary Components following the Warehouse Manager's commands (e.g. "a batch of steering wheels, upholstery kits, and dashboards for the sedan line"), checking the list against the contents stored by the Warehouse.
- The system receives the distribution commands, and the AGVs are activated and begin to navigate around the Warehouse, each moving to its assigned location to pick up the required Components and transport them to the Assembly Line.
- The system logs each AGV's load, syncing with the Warehouse Inventory to keep everything up to date. The Parts are scanned when exiting the Warehouse, updating the Warehouse Inventory in real-time (confirming what has been distributed and what remains) and leaving digital breadcrumbs for traceability.

**Manage Assembly Line**:

- As a Car moves down the Assembly Line to a Workstation, the Worker that is operating the Workstation signals the need for Components there (e.g. station 4 is ready for an engine block). The AGV promptly arrives with the Components, and the system logs the provision.
- Next to the Assembly Line, the Plant Manager oversees the entire operation. Every so often, he or she checks in the system that the pace of incoming Components matches the cadence of assembly. Throughout the process, the system itself is vigilant, tracking progress and Component levels, ready to signal any discrepancies to the Plant Manager.

**Tag and Register Finished Cars**:

- At the final Workstation at the end of the Assembly Line, the finished Cars are ready for their final touches. The quality of each Car is meticulously inspected before receiving its unique identity (the VIN), which is carefully engraved by a Worker, recorded on a physical AIDC carrier (e.g. RFID), and affixed to the Car by a robotized applicator arm.
- A Worker stands ready with a scanning device. As each Car rolls off the Assembly Line, they scan the VIN, and the system acknowledges the new record. A green light signals the successful registration, and the Car is now ready for its journey beyond the Factory walls.
- The Plant Manager checks at the end of the working day that the production plan has been completed.

These uses cases rely on the following datastores:

- Production Plan Data Store. The Warehouse Manager uses the Production Plan Data Store to align daily activities with the manufacturing schedule and check its status during the day or at the end of it. The system uses this data to determine the flow of Components and to update task lists for the Warehouse Workers.
- Warehouse Inventory: this is crucial to track the flow of Components into and out of the Warehouse, ensuring that the Assembly Line has a steady supply of whatever Components it might need. The system uses these registries to keep an accurate account of stock and to alert the Warehouse Manager of any shortages or surpluses.
- Finished Car Registry. The system provides a database for tracking the final product, which is essential for sales, distribution, and service records. The Plant Manager uses this registry to ensure that all finished Cars are accounted for and ready for distribution.

## Finished Car exit and outbound logistics

Once a Car has passed the quality control checks and leaves the Assembly Line,, it must be transported to distribution points (e.g., car dealerships operated by Dealers), but this is not a direct process.,  Firstly, newly finished Cars must be taken to a Finished Car Yard, where they are temporarily stored. When the finished Car is delivered at the exit of the Assembly Line, an intelligent system decides through an algorithm in which spot of the Finished Car Yard it should be parked, a Yard Driver gets into the Car to move it to the indicated position using screens within the yard, and along the way, automatic barriers that segment the Finished Car Yard and only allow the passage of the identified Car must be opened. Later, Cars are moved to the Logistics Terminal, waiting to be loaded onto a car carrier (a freight transportation vehicle e.g. a train, ship, or truck especially conceived to carry finished Cars). Although the location of this Logistics Terminal is physically next to the Factory, the processes that take place there are managed by another company (a Forwarder) different from the Car Manufacturer. When the car carrier is ready to transport a load of Cars, the Car leaves the position and is taken to a loading dock, where it is handed over to a carrier company that operates the car carrier.

The following entities are involved in the process of moving finished Cars from the Factory to the Dealer:

- Factory: it represents the production facility where Cars are assembled. It's the starting point in the outbound logistic chain and is responsible for ensuring that finished Cars are ready for shipment.
- Finished Car Yard: a depot area within the Factory premises where finished Cars are stored before they are dispatched to Dealers. Cars are not directly shipped from the Finished Car Yard, but they are moved from there to the Logistics Terminal and transferred to the Forwarder.
- Finished Car Yard Manager: The Employee that manages the storage and retrieval and oversees the organization and allocation of Cars within the Finished Car Yard, coordinating with other members of the logistic team (to ensure that Cars are parked efficiently and are ready for dispatch according to Purchase Orders).
- Employee in the context of outbound logistics may include various roles such as logistic coordinators, Yard Drivers, and administrative staff who assist with the management of Car dispatch, paperwork, and other related tasks.
- Yard Driver: a worker that safely transports finished Cars through the Finished Car Yard, ensuring they are parked according to the plant’s logistics and organization system. First they drive the car to their temporary storage locations, and eventually to the Logistics Terminal when they are ready for dispatch to the Forwarder.  
- Logistics Terminal: the hub where all the logistic activities for the finished Cars are managed. This includes the management of Car storage, preparation for shipping, and coordination with transportation services. The Logistics Terminal includes its own yard as well where Cars are staged before being loaded in the car carrier.
- Dealer: retail agent that orders Cars from the Factory to sell them to the end customer. They receive deliveries of Cars from the Factory through the Forwarder.
- Transport Order: a directive by the Factory to the Forwarder for the transportation of Cars from the Factory to the Dealer. It details the logistics of who is responsible for shipping the cars, and when they shall be shipped.
- Shipping Manager: a role responsible for managing the shipping of Cars towards the Dealer. This includes arranging the Transport Order with the selected Forwarder.

In the outbound logistic management subsystem, the following use cases manage the journey of Cars from the end of the Assembly Line until they leave the Factory to be dispatched to the Dealer to meet their Purchase Orders (and ultimately reach the customer). The system acts as the central hub, tracking every Car’s location, status, and destination, providing real-time updates to all actors involved in the outbound logistic process.

**Manage Parking in Factory’s Finished Car Yard**: This use case involves organizing the storage of finished Cars in the Factory's Finished Car Yard before they are shipped to Dealers.

1. The Finished Car Yard Manager checks information about the new Cars from the Assembly Line in the Finished Car Registry.
2. The Finished Card Yard Manager assigns a parking spot in the Finished Car Yard for each Car, ensuring they're stored efficiently and ready for shipment.
3. Yard Drivers then drive the cars from the end of the Assembly Line to their designated spots in the Finished Car Yard.
4. The system updates the Finished Car Registry keeping track of the location and status of each Car.

**Manage Purchase Orders**: this use case manages the processing and fulfilment of Purchase Orders placed by Dealers for the delivery of finished Cars.

1. A Dealer places a Purchase Order for a batch of Cars, which is eventually received by the Shipping Manager.
2. The details of the Purchase Order are entered into a Purchase Order System, specifying models, quantities, and delivery schedules.
3. The Finished Car Yard Manager is notified of the Purchase Order and retrieves the specified Cars from the Finished Car Yard.
4. The Cars are checked and prepared for shipment, ensuring that they match the Dealer's Purchase Order specifications.
5. Employees then drive the Cars towards the Logistics Terminal.
6. The system updates to reflect that the cars are no longer in the Factory and are now allocated for shipment.

**Manage Shipping**: Once Cars are allocated to a Purchase Order, they need to be shipped to the Dealer; this use case covers the process of preparing and transporting Cars to their final destination.

1. The Shipping Manager checks the  outstanding Purchase Orders from the 'Purchase Order System', detailing which Cars need to be shipped, and matches them with finished cars in the Finished Car Registry.
2. The Shipping Manager plans the logistics and schedules  the shipment.
3. The system generates a Transport Order for the Forwarder, which includes details of the shipment and the destination.
4. A Yard Driver drives the Cars into the Logistics Terminal, where Cars will eventually be loaded onto the car carrier  (e.g. train, ship, truck), and supply the necessary documents to the Forwarder.
5. Once the shipment leaves the Factory and the Waybill is received from the Forwarder, the system logs the departure, updating the 'Transport Order Data Store with the details of the consignment.

The outbound logistic processes rely on the following datastores:

- Finished Car Registry: The Finished Car Yard Manager uses this registry to keep track of all finished Cars in the Finished Car Yard, ensuring they are ready for shipment. The system maintains an updated log of the Car status, facilitating quick retrieval for shipping.
- Logistics Terminal Car Registry: The Shipping Manager uses this registry to manage the logistics of Car dispatch, including space allocation and transport coordination in the Finished Car Yard. Changes in the Logistics Terminal are reflected in real time by the system to ensure that the data registered is current.
- Purchase Order and Transport Order Data Stores. Purchase orders are processed and matched with the available finished Cars stock, while Transport Orders are used to arrange the actual transport of the Cars. The system integrates these orders to streamline the outbound logistic process, from order receipt to Car dispatch.

## Other requirements

The system will rely on the use of generalist IoT middleware platforms (e.g. Thingsboard), to which the different sensors and actuators (and, where appropriate, their emulators) will be connected.

The system will implement administration and management procedures regarding user management, system operation, and security management. There are specific Employee roles that will be responsible for these procedures, namely:

- System admin: deals with the physical and logical IT infrastructure of the factory, ensuring that all Employees can perform their duties.
- Operations manager: oversees the production process, performing recurring tasks, optimizing inefficiencies and coordinating machinery like AGVs and robots.
- Security manager: implements and oversees security procedures and events, taking the necessary measures to handle them in a timely manner.
