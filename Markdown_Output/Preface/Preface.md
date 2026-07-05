# **Preface**

### **About This Specification**

This specification is intended to define a set of protocols and interfaces that enable the creation of systems comprised of multiple System Nodes targeting AI applications. A System Node typically contains one or more Host CPUs and one or more Accelerators connected within the System Node utilizing an implementation specific set of interconnects such as CXL ®, PCIe ®, XGMI, CHI c2c, AMD Infinity Fabric ®, etc. These System Nodes can be and often are coherent within the System Node, meaning that each Accelerator and each Host CPU can directly and coherently access all Host and Accelerator memory within the given System Node though this is not required. The exact configuration and number of Accelerators and Hosts within a System Node and the nature of the coherence and accessibly to memory within the node is implementation specific and is not mandated by this specification. Each System Node is typically managed under the control of a single OS image (System Nodes are also referred to as "OS Domains").

The protocols and interfaces defined in this specification are intended to support low latency Accelerator-to-Accelerator communication across System Nodes using direct read, write, and atomics transactions. These protocols and interfaces do not, however, allow for Host CPU accesses to memory attached to device or host in another remote System Node.

The interfaces described in this specification are the UALink Protocol Level Interface (UPLI) and the Ultra Accelerator Link (UALink) interface. The UALink Protocol Level Interface is a point-to-point, on-chip interface comprised of various channels that transfer UPLI transactions consisting of Requests, Read data, Write data, and Request Responses between an Originator and a Completer. The Ultra Accelerator Link is a high-bandwidth point-to-point serial interface providing a connection between Accelerators and Switches that allows UPLI transactions to be transferred between Originators and Completers in Accelerators within and across System Nodes. This specification is primarily intended to create a switching ecosystem for Accelerators.

The figure below Figure 0-1 [UALink Connectivity Overview,](#page-0-0) illustrates a portion of a simple example system illustrating two (of possibly many) System Nodes (SN0 and SN1) each illustrating one (of possibly many) Host/Acc pairs in each of the System Nodes.

![](_page_0_Figure_8.jpeg)

**Figure 0-1 UALink Connectivity Overview**

<span id="page-0-0"></span>The illustrated Host and Accelerator (Acc) in each of the system nodes are connected using an implementation chosen interconnect such as CXL, PCIe, AMD Infinity Fabric, XGMI, CHI c2c, etc. (red) that can and often allows for Host and Acc access to all memory within the node or at least on the connected Host and Accelerator. The Accelerator is further attached to a set of UALink Links (blue) that connect to a Switch and then on to another set of UALink links to the remote Accelerator allowing UPLI transactions to be routed between Accelerators in different System Nodes (accesses can also be routed between Accelerators in the same System Node).

*Preface* 18

#### **Ultra Accelerator Link Consortium Inc. (UALink) - UALink\_200 Rev 1.0 Specification**

In a typical system, Requests from a given Accelerator in one System Node to a remote Accelerator in a different System Node may access any Accelerator memory or Host Memory in the Remote System node. This is illustrated above by red arrows above showing each Accelerator accessing the remote Accelerator's memory (Host and Accelerator accesses to local Host and Accelerator memory are not shown). Hosts accessing any memory in any remote System Nodes shall not be supported.

This version of the specification does not define or enable attaching devices to the Switches. It does not define or enable how to perform in-network, in-memory, or near-memory compute.

*Preface* 19

## **Terminology**

The following terms are used in this specification:

| Term                    | Definition                                                                                                                                                                                                     |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UALink                  | Ultra Accelerator Link                                                                                                                                                                                         |
| UPLI                    | UALink Protocol Level Interface                                                                                                                                                                                |
| DL                      | Data Link Layer                                                                                                                                                                                                |
| DL Channel              | Logical channels with in DL, one for TL Flits, one for DL UART messages                                                                                                                                        |
| SH                      | Segment header, used with in a DL Flit                                                                                                                                                                         |
| FH                      | Flit Header, for DL Flit                                                                                                                                                                                       |
| DL alternative sector   | Sectors in a DL Flit that are sued for non TL Flits                                                                                                                                                            |
| DL message              | Message that starts and terminates at the DL                                                                                                                                                                   |
| CRC                     | Cyclic redundancy check                                                                                                                                                                                        |
| RS                      | Reconciliation Layer, interface between PCA and DL                                                                                                                                                             |
| AM                      | Alignment marker, used for alignment of PCS lanes                                                                                                                                                              |
| PCS                     | Physical Coding Sublayer                                                                                                                                                                                       |
| FEC                     | Forward error correction                                                                                                                                                                                       |
| PMA                     | Physical Medium Attachment Interface                                                                                                                                                                           |
| GAUI                    | Gigabit unit attachment                                                                                                                                                                                        |
| VDCI                    | Voltage Domain Crossing Interface                                                                                                                                                                              |
| SPA                     | System Physical Address                                                                                                                                                                                        |
| Field                   | A group of one or more signals that share a name and encode a specific piece of information. Signals                                                                                                           |
|                         | within a field are numbered according to binary significance.                                                                                                                                                  |
| SOC                     | System on Chip.                                                                                                                                                                                                |
| SPC                     | Symbols Per Clock                                                                                                                                                                                              |
| Word                    | Two Bytes                                                                                                                                                                                                      |
| Doubleword              | Four Bytes                                                                                                                                                                                                     |
| UART                    | Universal Anonymous Receiver Transmitter. A DL mechanism for F/W on either end of the link to                                                                                                                  |
|                         | exchange information.                                                                                                                                                                                          |
| Pod                     | The collection of all the Accelerators and Switches physically connected though UALink via Switches.                                                                                                           |
| Virtual Pod             | A non-overlapping partition of a Pod where the Acclerators within the Virtual Pod may communicate                                                                                                              |
|                         | with other Accelerators in the Virtual Pod, but no other Accelerators in the Pod.                                                                                                                              |
| Availability            | Security objective ensuring a resource (e.g., network) is functioning and data is accessible when needed                                                                                                       |
| UALink Network          | The physical network of UALink Links and Switches connecting the Accelerators in a Pod.                                                                                                                        |
| CC                      | Confidential Computing                                                                                                                                                                                         |
| Confidentiality         | Security objective ensuring data are only readable by an authorized party                                                                                                                                      |
| Front end network       | Network used by OS domains to communicate and establish a Tenant TCB.                                                                                                                                          |
| Infrastructure provider | An organization that maintains computing resources such as servers, storage, networking and                                                                                                                    |
| Integrity               | virtualization and provides them to the users on demand.<br>Security objective ensuring data are only writeable and modifiable by an authorized party                                                          |
|                         |                                                                                                                                                                                                                |
| Pod Controller          | Central controller software responsible for managing the lifecycle of the Pod including topology<br>discovery, configuration, resource management, virtual pod creation and management and Pod health          |
|                         | monitoring. The Pod Controller is typically owned by the Infrastructure provider.                                                                                                                              |
| Port encryption engine  | A port encryption engine has at least one association (key, IV/count/sequence #, etc.) and enough                                                                                                              |
|                         | encryption/decryption capability to keep up with line rates. Additionally, based on implementation, the                                                                                                        |
|                         | port encryption engine may have buffering associated with each association such that it can pre                                                                                                                |
|                         | compute counter encryption values. An accelerator requires a port encryption engine per port.                                                                                                                  |
| Switch                  | An entity that can switch UALink traffic between a set of Ports equal in number to the number of                                                                                                               |
|                         | Accelerators in the Pod.                                                                                                                                                                                       |
| Physical Switch         | A physical hardware entity that can be used to implement a Switch and which can have Ports equal to                                                                                                            |
|                         | he number of Accelerators in the Pod or Ports equal to an integer multiple greater than one of the                                                                                                             |
|                         | number of Accelerators in the Pod.                                                                                                                                                                             |
| TCB                     | Trusted Computing Base – The set of hardware and software components that are trusted to meet the                                                                                                              |
|                         | security objectives of a feature.                                                                                                                                                                              |
| TEE                     | Trusted Execution Environment. It is responsible for bringing an accelerator into the TCB and for                                                                                                              |
|                         | UALsec configuration (e.g., key establishment). In the context of CC, TEE examples include Intel TDX,                                                                                                          |
|                         | AMD SEV and ARM CCA).                                                                                                                                                                                          |
| Tenant                  | User of the infrastructure computing resources such as AI Cluster. In an AI cluster, the Tenant is                                                                                                             |
|                         | typically assigned a set of accelerators (i.e., a Virtual Pod) to run its workload.                                                                                                                            |
| TVM                     | Trusted Execution Environment Virtual Machine. This is a confidential computing VM running in a TEE.                                                                                                           |
|                         | One or more accelerators are assigned to a TVM which is responsible for secure configuration and                                                                                                               |
|                         | management of those accelerators.                                                                                                                                                                              |
| Virtual Pod             | The logical subset of a physical pod connected over UAL. A virtual pod belongs to one user (aka Tenant).<br>A physical pod can be partitioned into multiple, concurrent virtual pods, each presumably owned by |
|                         |                                                                                                                                                                                                                |

*Preface* 20

#### **Ultra Accelerator Link Consortium Inc. (UALink) - UALink\_200 Rev 1.0 Specification**

|                            | distinct Tenants. One virtual pod can be created and torn down without impacting other running virtual<br>pods in the physical pod                                                                                                                      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TSM                        | TEE Security Manager. This is SW/FW component on the host which establishes secure interface with<br>the device and is responsible for configuring and helping enfoce TEE IO security policies on the host<br>side. It is in the TCB of all TVMs        |
| DSM                        | Device Security Manager. This is a FW component on the device that enforces device security policies. It<br>communicates with the TSM over a secure channel and receives commands from TSM for configuring<br>and enforcing device security policies.   |
| System Node                | Hardware platform that hosts Accelerators, alongside one or more Central Processing Unit(s) (CPU(s))<br>and one or more network interface(s). The System Node is the boundary of an OS Domain, and UALink<br>System Nodes host a Node Management Agent. |
| Switch Platform            | Hardware platform that hosts Switches, a Switch Management Agent, and a network interface. When<br>present, Switch Platforms are distinct from System Nodes.                                                                                            |
| Node Management<br>Agent   | Firmware/Software component that manages Accelerators in a System Node under the direction of the<br>Pod Controller.                                                                                                                                    |
| Switch Management<br>Agent | Firmware/Software component that manages Switches under the direction of the Pod Controller.                                                                                                                                                            |

In addition to the hardware requirements laid out by this specification, the complementary *Ultra Accelerator Link Manageability Specification* documents the requirements for firmware and software to manage and operate an Ultra Accelerator Link Pod.