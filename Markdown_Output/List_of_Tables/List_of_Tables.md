## **List of Tables**

| Table 2-1 Common Signals<br>47                                                                    |     |
|---------------------------------------------------------------------------------------------------|-----|
| Table 2-2 Request Channel Signals<br>50                                                           |     |
| Table 2-3 Read, ReqAttr Usage<br>53                                                               |     |
| Table 2-4 Atomic Request ReqAttr Usage<br>53                                                      |     |
| Table 2-5 Atomic OpSize Encoding<br>53                                                            |     |
| Table 2-6 Commands<br>54                                                                          |     |
| Table 2-7 UPLI Write Message Request Types57                                                      |     |
| Table 2-8<br>Read Response/Data Channel Signals58                                                 |     |
| Table 2-9 RdRspStatus [3:0] Encoding for Predefined Commands60                                    |     |
| Table 2-10 RdRspStatus[3:0] Encoding for Vendor Defined Command60                                 |     |
| Table 2-11 Write Response Channel Signals62                                                       |     |
| Table 2-12 WrRspStatus[3:0] Encoding<br>for Predefined Commands<br>64                             |     |
| Table 2-13 WrRspStatus[3:0] Encoding for Vendor Defined Commands64                                |     |
| Table 2-14 Originator Data Channel Signals<br>65                                                  |     |
| Table 5-1: TL Flit organization99                                                                 |     |
| Table 5-2: Control Half Flit Field Footprints and Sizes99                                         |     |
|                                                                                                   |     |
| Table 5-3: TL Flit with Message Indicator Bits102                                                 |     |
| Table 5-4: Message TL Half-Flit102                                                                |     |
| Table 5-5: An 8-sector Request (Read) followed by a Mandatory NOP Half Flit.<br>103               |     |
| Table 5-6: A 4 sector Request (WriteFull 256 bytes) followed by a Control Half Flit with Flow     |     |
| Control.<br>103                                                                                   |     |
| Table 5-7: A 4 sector Request (Write 192 bytes) followed by a Control Half Flit with Flow Control |     |
| 104                                                                                               |     |
| Table 5-8: A 2-sector Request (64 byte write), NOP, FC, and 4-sector AtomicR request104           |     |
| Table 5-9: A 2-sector Request (64 byte write), NOP, FC, and 4-sector AtomicR request105           |     |
| Table 5-10: A 2-sector Request (256 byte write), 2-sector Request (256-byte WriteFull), and a 4-  |     |
| sector AtomicNR105                                                                                |     |
| Table 5-11: Authentication mode example matching the prior example.<br>106                        |     |
| Table 5-12: Read Requests and Associated Read Responses107                                        |     |
| Table 5-13: 256-byte WriteFull with corrupt second 64-byte beat.<br>108                           |     |
| Table 5-14: An example illustrating corrupted Atomic Operand data108                              |     |
| Table 5-15 A single 4-sector Request (WriteFull 256 bytes) and a 2-sector Write Response109       |     |
| Table 5-16<br>Three 4 sector WriteFull 256 byte Requests and three Compressed Write Responses.110 |     |
| Table 5-17<br>Four 2 sector WriteFull 256-byte Requests and four Compressed Write Responses.      | 111 |
| Table 5-18: Five 2 sector WriteFull 256-byte Requests and Five Compressed Write Responses112      |     |
| Table 5-19: Two 2 sector WriteFull 256-byte Requests and Two Compressed Write Responses.          | 113 |
| Table 5-20: Five 2 sector Read 256-byte Requests and Five Compressed Read Responses114            |     |
| Table 5-21: Two 2-sector Read 256-byte Requests and Two Compressed Read Responses.<br>115         |     |
| Table 5-22 Three Write, Two Read Maximum Efficiency Example<br>116                                |     |
| Table 5-23 Address Cache Loading Request Availability121                                          |     |
| Table 5-24 Request Packing without Data Half-Flits123                                             |     |
| Table 5-25 Request Pacing with Data Half-Flits<br>123                                             |     |
| Table 5-26: Flow Control Field Signals127                                                         |     |
| Table 5-27: TL Control Half-Flit Message Type Values129                                           |     |
| Table 5-28: Legal TL Message Half-Flits<br>129                                                    |     |
| Table 5-29 Uncompressed Request Field Signals<br>130                                              |     |
| Table 5-30<br>Uncompressed Response Field Signals<br>131                                          |     |
| List of Tables                                                                                    | 13  |

| Table 5-31 Compressed Request Field Signals<br>133                                            |     |
|-----------------------------------------------------------------------------------------------|-----|
| Table 5-32 Compressed Request Usage Restrictions.<br>134                                      |     |
| Table 5-33 Compressed Request Command Encoding134                                             |     |
| Table 5-34<br>Compressed Response for Single Beat Read Field Signals135                       |     |
| Table 5-35 Compressed Response for Single-Beat Read Response Usage Restrictions.<br>135       |     |
| Table 5-36 Compressed Response for Write or Multi-Beat Read Field Signals136                  |     |
| Table 5-37 Compressed Response for Write or Multi-Beat Read Response Usage Restrictions.      | 136 |
| Table 5-38 Flow Control/NOP Field137                                                          |     |
| Table 6-1<br>Sector Allocation per Segment142                                                 |     |
| Table 6-2 Segment Header<br>144                                                               |     |
| Table 6-3 DL Message Types150                                                                 |     |
| Table 6-4 TL Rate Notification152                                                             |     |
| Table 6-5 Device ID Request153                                                                |     |
| Table 6-6 Port ID Request154                                                                  |     |
| Table 6-7 No-Op Message<br>154                                                                |     |
| Table 6-8 Channel Negotiation<br>159                                                          |     |
| Table 6-9 Vendor Defined Packet Type Length (TL) DWord<br>162                                 |     |
| Table 6-10 UART Stream Reset Request162                                                       |     |
| Table 6-11 UART Stream Reset Response163                                                      |     |
| Table 6-12 UART Stream transport message163                                                   |     |
| Table 6-13 UART Stream Credit Update<br>163                                                   |     |
| Table 6-14 Explicit Sequence Number Flit Header<br>167                                        |     |
| Table 6-15 Command Flit Header167                                                             |     |
| Table 7-1 100Gbps Serial Clauses182                                                           |     |
| Table 7-2 200Gbps Serial Clauses182                                                           |     |
| Table 7-3 Sequential Ordered Sets186                                                          |     |
| Table 7-4<br>Reduced Interleave FEC<br>189                                                    |     |
| Table 9-1 Possible attack types<br>210                                                        |     |
| Table 9-2 Threat model212                                                                     |     |
| Table 9-3 IV Format216                                                                        |     |
| Table 9-4 Request channel signals that are encrypted and authenticated217                     |     |
| Table 9-5 Read response channel signals that are authenticated and encrypted218               |     |
| Table 9-6 Write response channel signals that are authenticated and encrypted220              |     |
| Table 9-7 Originator data channel signals that are authenticated and encrypted220             |     |
| Table 9-8 Request Channel Fields for AAD and MSG -<br>Non Write or UPLI Write Message Request | 237 |
| Table 9-9 Originator Data Channel Fields for AAD and MSG (partial-word write or UPLI Write    |     |
| Message Request)237                                                                           |     |
| Table 9-10 Originator Data Channel Fields for AAD and MSG (Full Write)<br>237                 |     |
| Table 9-11 Read Response channel fields for AAD and MSG<br>238                                |     |
| Table 9-12 Write Response channel fields for AAD and MSG238                                   |     |
| Table 9-13 Mapping Request Channel AAD bits238                                                |     |
| Table 9-14 Mapping Request Channel MSG bits for non write and non UPLI Write Message          | 239 |
| Table 9-15 Mapping Request and Originator Data channels AAD bits for Wr Req or UPLI Write     |     |
| Message<br>239                                                                                |     |
| Table 9-16 Mapping MSG bits for Write Request w. Byte Enable or UPLI Write Message of the 1st |     |
| beat240                                                                                       |     |
| Table 9-17 Mapping MSG bits for Full-word Wr Req (w/o Byte Enable) of the 1st beat241         |     |
| Table 9-18 Mapping AAD bits for Originator data non 1st beat<br>242                           |     |
| Table 9-19 Mapping MSG bits for Full-word Wr Req (w. Byte Enable) non 1st beat242             |     |
| List of Tables                                                                                | 14  |

## Evaluation Copy

## **Ultra Accelerator Link Consortium Inc. (UALink) - UALink\_200 Rev 1.0 Specification**

| Table 9-20 Mapping MSG bits for Full-word Wr Req (w/o Byte Enable) non 1st beat243 |  |
|------------------------------------------------------------------------------------|--|
| Table 9-21 Mapping Read Response Channel AAD bits<br>244                           |  |
| Table 9-22<br>Mapping MSG bits for Read Response<br>244                            |  |
| Table 9-23 Mapping Read Response Channel AAD bits<br>246                           |  |
| Table 9-24 Mapping Write Response Channel MSG bits246                              |  |