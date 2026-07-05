## **List of Figures**

| Figure 0-1 UALink Connectivity Overview<br>18                                                 |    |
|-----------------------------------------------------------------------------------------------|----|
| Figure 1-1 UALink Based Multi-Accelerator System<br>22                                        |    |
| Figure 1-2 Accelerator communication over a direct link and over a Switch24                   |    |
| Figure 1-3 UALink Stack25                                                                     |    |
| Figure 1-4 UALink cross-domain address translation model27                                    |    |
| Figure 1-5 Translation Process28                                                              |    |
| Figure 2-1 UALink Protocol Level Interface30                                                  |    |
| Figure 2-2 Extending a UPLI interface through Intermediate UPLI Interfaces<br>31              |    |
| Figure 2-3 UALink Protocol Level Interface Channels and control signals<br>32                 |    |
| Figure 2-4 UALink Stack Component34                                                           |    |
| Figure 2-5 Connected UALink Stack Components<br>35                                            |    |
| Figure 2-6 End-to End UALink Connection Between two Accelerators36                            |    |
| Figure 2-7 UPLI Request and Response Flows37                                                  |    |
| Figure 2-8 Example system with 32 Accelerators with 32 x1 UALink Links38                      |    |
| Figure 2-9 Read Request end-to-end flow with Response39                                       |    |
| Figure 2-10 UALink Station with x1 bifurcation42                                              |    |
| Figure 2-11 Flow control loops<br>46                                                          |    |
| Figure 2-12 Four DoubleWorld Read Request Not Straddling a 64-Byte Boundary71                 |    |
| Figure 2-13 Four DoubleWord Read Request Straddling a 64-byte boundary<br>71                  |    |
| Figure 2-14 Single Byte Read72                                                                |    |
| Figure 2-15 Six Byte Read Access Not Straddling a 64-Byte Boundary72                          |    |
| Figure 2-16 Four Byte Read Access Straddling a 64-Byte Boundary73                             |    |
| Figure 2-17 Four Doubleword Write Request Not Straddling a 64 Byte Boundary74                 |    |
| Figure 2-18 Sixteen Doubleword Write Request Not Straddling a 64-Byte Bounday<br>74           |    |
| Figure 2-19 Three Doubleword Write Request Straddling a 64 Byte Boundary75                    |    |
| Figure 2-20 A 128 Byte Write Full Request (Requires Two Beats)75                              |    |
| Figure 2-21 Single Operand (Eight-Byte Operands) Atomic<br>77                                 |    |
| Figure 2-22 Single Operand (Four-Byte Operands) Atomic<br>77                                  |    |
| Figure 2-23 Double Operand (Eight-Byte Operands) Atomic, Data Returned in High 32 Bytes.      | 78 |
| Figure 2-24 Double Operand (Four-Byte Operands) Atomic, Data Returned in Low 32 Bytes79       |    |
| Figure 3-1 UALink End to End Data Protection<br>81                                            |    |
| Figure 3-2 UPLI Control Error detected at an Originator or Completer not on a UALink TL on an |    |
| Accelerators87                                                                                |    |
| Figure 3-3 UPLI Control Error detected at a UALink TL on an Accelerator<br>88                 |    |
| Figure 3-4 UPLI Interface Control Error detected at the UALink TL on the Switch89             |    |
| Figure 3-5 UPLI Control Error detected at the UPLI Completer on a Switch89                    |    |
| Figure 3-6 UPLI Control Error detected within the Switch Core at the UPLI Originator90        |    |
| Figure 3-7 UALink Link goes down91                                                            |    |
| Figure 3-8 PHYs Inform UALink TLs in Accelerator and Switch Which Enter Drop Mode91           |    |
| Figure 3-9 Placing the Accelerator UPLI Originator Into Isolation Mode<br>92                  |    |
| Figure 3-10 Other Accelerators Time Out92                                                     |    |
| Figure 3-11 Link Down Error Processing Complete93                                             |    |
| Figure 4-1 UPLI Interface Reset Requirements.<br>94                                           |    |
| Figure 4-2 UPLI Connection Handshake Protocol –<br>Originator connects first97                |    |
| Figure 4-3 UPLI Connection Handshake Protocol –<br>Completer connects first<br>97             |    |
| Figure 4-4 UPLI Connection Handshake Protocol –<br>Originator and Completer connecting        |    |
| concurrently<br>97                                                                            |    |
| List of Figures                                                                               | 10 |

## Ultra Accelerator Link Consortium Inc. (UALink) - UALink\_200 Rev 1.0 Specification

| 0  |
|----|
| O  |
|    |
|    |
|    |
| 0  |
| 7  |
| a  |
|    |
|    |
| (0 |
|    |
| Ш  |
|    |

| rigure 5-1: 1L filt connections to UPLI interfaces                                                                                   | 90  |
|--------------------------------------------------------------------------------------------------------------------------------------|-----|
| Figure 5-2: UALink TL Tx Dataflow                                                                                                    |     |
| Figure 5-3: UALink TL Rx Dataflow                                                                                                    |     |
| Figure 5-4: Indexing of Accelerator Tx Address Caches/Switch Rx Address Caches                                                       |     |
| Figure 5-5: Indexing of Switch Tx Address Caches/Accelerator Rx Address Caches                                                       |     |
| Figure 5-6 TL Receive Catch Buffer Dataflow                                                                                          |     |
| Figure 5-7: Flow Control Field Relation to Credit Channels.                                                                          | 126 |
| Figure 6-1 DL block Diagram                                                                                                          |     |
| Figure 6-2 UART                                                                                                                      |     |
| Figure 6-3 DL 640-Byte Flit Overview                                                                                                 |     |
| Figure 6-4 DL Flit with segment details                                                                                              |     |
| Figure 6-5 Flit packing flow chart                                                                                                   |     |
| Figure 6-6 TL Flit[0] example 1                                                                                                      |     |
| Figure 6-7 TL Flit[1] example 1                                                                                                      |     |
| Figure 6-8 TL Flit[0] example 2                                                                                                      |     |
| Figure 6-9 DL Flit to 64B/66B Encoding                                                                                               | 140 |
| Figure 6-10 Single Request Flow                                                                                                      |     |
| Figure 6-11 Two Requests Flow                                                                                                        |     |
| Figure 6-12 Single Successful Request Flow                                                                                           |     |
| Figure 6-13 Single Unsuccessful Request Flow                                                                                         |     |
| Figure 6-14 Single decision pending Request Flow                                                                                     |     |
| Figure 6-15 Conflicting request flow                                                                                                 |     |
| Figure 6-16 Identical Request Flow                                                                                                   |     |
| Figure 6-17 Vendor Defined Packet                                                                                                    |     |
| Figure 6-18 Pacing                                                                                                                   |     |
| Figure 6-19 Ack Replay Request valid range                                                                                           |     |
| Figure 6-20 Rx Flow Chart                                                                                                            | 17/ |
| Figure 6-21 Tx Flow Chart                                                                                                            |     |
| Figure 6-22 Round Trip Time                                                                                                          |     |
| Figure 6-23 DL Link State                                                                                                            |     |
| Figure 7-1 Physical Layer Block Diagram                                                                                              |     |
| Figure 7-2 64B/66B Block Codes                                                                                                       |     |
| Figure 7-3 100GBASE-R                                                                                                                |     |
| Figure 7-4 200GBASE-R & 400GBASE-R                                                                                                   |     |
| Figure 7-5 800GBASE-R                                                                                                                |     |
| Figure 7-6 200GBASE-KR1/CR1, 1-Way Interleave                                                                                        | 201 |
| Figure 8-1 UALink System Node                                                                                                        |     |
| Figure 8-2. A UALink Switch Platform                                                                                                 |     |
| Figure 8-3. A UALink Pod managed by a Pod Controller                                                                                 |     |
|                                                                                                                                      |     |
| Figure 8-4. A UALink Pod partitioned into three Virtual Pods                                                                         |     |
| Figure 9-1 System level view of confidential computing in a podFigure 9-2 Encryption and Authentication touch points in UALink stack |     |
|                                                                                                                                      |     |
| Figure 9-3 Example of UALink TL flit with the "Tag" half flit                                                                        |     |
| Figure 9-4 Security related state elements in UALink port TX for a 1024 accelerator system                                           |     |
| Figure 9-5 Security related state elements in UALink RX for a 1024 accelerator system                                                |     |
| Figure 9-6 Illustration of master keys maintained by UALink Port RX and TX in a UALink sy                                            |     |
| Figure 9-7 A 4 accelerator UALink system example                                                                                     |     |
| Figure 9-8 Stream-Key derivation flow in UALink port TX                                                                              |     |
| Figure 9-9 Key swap flow in UALink port TX                                                                                           |     |
| List of Figures                                                                                                                      | 11  |

| Figure 9-10 Key derivation flow in UALink Port RX<br>234                                             |  |
|------------------------------------------------------------------------------------------------------|--|
| Figure 9-11 Key switch flow in UALink port RX235                                                     |  |
| Figure 9-12<br>Source accelerator -<br>Destination accelerator interactions for key swap flow<br>236 |  |