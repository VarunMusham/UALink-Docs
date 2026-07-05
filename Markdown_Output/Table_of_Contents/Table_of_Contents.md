# <span id="page-0-0"></span>**Table of Contents**

| Legal Not   | ice                                                                          | 2  |
|-------------|------------------------------------------------------------------------------|----|
| Table of 0  | Contents                                                                     | 4  |
| List of Fig | gures                                                                        | 10 |
| List of Ta  | bles                                                                         | 13 |
| Revision    | History                                                                      | 16 |
| Preface     |                                                                              | 18 |
| About       | This Specification                                                           | 18 |
| Termin      | ology                                                                        | 20 |
| 1 Intro     | duction                                                                      | 22 |
| 1.1         | Multi-Node Accelerator System                                                | 22 |
| 1.2         | Accelerator System Node                                                      | 24 |
| 1.3         | UALink Stack Interface Layers                                                | 25 |
| 1.3.1       | Protocol Layer                                                               | 25 |
| 1.3.2       | Transaction Layer                                                            | 25 |
| 1.3.3       | Data Link Layer                                                              | 26 |
| 1.3.4       | Physical Layer                                                               | 26 |
| 1.4         | UALink Address Translation Model                                             | 27 |
| 1.4.1       | Remote Memory Access (RMA)                                                   | 27 |
| 1.5         | UALink Coherency                                                             | 29 |
| 2 UPLI      | Interface Definition and Operation Rules                                     | 30 |
| 2.1         | UPLI Interface                                                               | 30 |
| 2.2         | UALink Stack Component                                                       | 34 |
| 2.3         | UALink UPLI Request and Response Paths                                       | 36 |
| 2.4         | Routing a Transaction from End-to-End                                        | 38 |
| 2.5         | UPLI Channel Time Division Multiplexing (TDM)                                | 42 |
| 2.6         | UALink Protocol Level Interface Flow Control and overall UALink Flow control | 44 |
| 2.7         | Interface Signals                                                            | 47 |
| 2.7.1       | Signal Groups                                                                | 47 |
| 2.7.2       | Common Signals                                                               | 47 |
| 2.7.3       | UPLI Transactions/Channel usage                                              | 47 |
| 2.7.4       | Request Channel                                                              | 50 |
| 2.7.5       | Read Response/Data Channel                                                   | 58 |
| 2.7.6       | Write Response Channel                                                       | 62 |
| 2.7.7       | Originator Data Channel                                                      | 65 |
|             | Table of Contents                                                            | 4  |

|   | 2.7.8  | Relationships between UPLI Channels and requirements within the Channels66 |  |
|---|--------|----------------------------------------------------------------------------|--|
|   | 2.7.9  | UPLI Request, Read Response, and Write Response ordering68                 |  |
|   | 2.7.10 | UPLI Request Single-Copy Atomicity69                                       |  |
|   | 2.8    | Data/Atomic Operands Transfer<br>69                                        |  |
| 3 |        | Reliability, Availability, and Serviceability (RAS)80                      |  |
|   | 3.1    | RAS Requirements<br>80                                                     |  |
|   | 3.1.1  | End to End Data Protection81                                               |  |
|   | 3.1.2  | RAS Error Types<br>82                                                      |  |
|   | 3.1.3  | RAS Error Handling Mechanisms<br>83                                        |  |
|   | 3.1.4  | UALink RAS Error Handling86                                                |  |
| 4 |        | UPLI Interface Reset, Signaling, and Connection94                          |  |
|   | 4.1    | UPLI Interface Reset94                                                     |  |
|   | 4.2    | UPLI Interface Signaling Requirements<br>95                                |  |
|   | 4.3    | UPLI Interface Control96                                                   |  |
| 5 |        | Transaction Layer (TL)98                                                   |  |
|   | 5.1    | TL Flit and Half Flit formats<br>98                                        |  |
|   | 5.1.1  | TL Flit and TL Control and Data Half-Flit formats and Sequencing<br>98     |  |
|   | 5.1.2  | TL Message Flit Format and Sequencing101                                   |  |
|   | 5.2    | TL Flit Sequencing and Packing Examples102                                 |  |
|   | 5.3    | Indicating Data Corruption in TL Data Half-Flits.<br>107                   |  |
|   | 5.4    | TL Write Flit Sequence Encoding Efficiency Examples108                     |  |
|   | 5.4.1  | Single WriteFull Request and Single WriteFull Response109                  |  |
|   | 5.4.2  | WriteFull Requests and Compressed WriteFull Responses<br>109               |  |
|   | 5.4.3  | Compressed WriteFull Requests and Compressed WriteFull Responses110        |  |
|   | 5.4.4  | Maximum Efficiency WriteFulls111                                           |  |
|   | 5.4.5  | Maximum Efficiency WriteFulls with Authentication112                       |  |
|   | 5.4.6  | Maximum Efficiency Reads.<br>113                                           |  |
|   | 5.4.7  | Maximum Efficiency Reads with Authentication.<br>114                       |  |
|   | 5.4.8  | Maximum Efficiency With Mixed Reads and Writes115                          |  |
|   | 5.5    | TL Tx and Rx Dataflow and Tx and Rx Compression Caches117                  |  |
|   | 5.6    | TL Tx and Rx Address Cache Synchronization.<br>120                         |  |
|   | 5.6.1  | CLOAD and CWAY control signals121                                          |  |
|   | 5.6.2  | Address Cache sequencing at the Tx Address Cache and Rx Address Cache121   |  |
|   | 5.7    | TL Control Half-Flit Request/Response Field packing limits122              |  |
|   | 5.8    | TL Flow Control126                                                         |  |
|   |        |                                                                            |  |

|   | >        |  |
|---|----------|--|
|   | 0        |  |
|   | C        |  |
|   |          |  |
| • | ati      |  |
|   |          |  |
|   | <u>a</u> |  |
|   | Ú        |  |

|   | 5.9   | TL Control Field Bit Assignments and Legal TL Message Flit Types  | 129 |
|---|-------|-------------------------------------------------------------------|-----|
|   | 5.9.1 | Uncompressed Request Field                                        | 130 |
|   | 5.9.2 | Uncompressed Response Field                                       | 131 |
|   | 5.9.3 | Compressed Request Field                                          | 133 |
|   | 5.9.4 | Compressed Response Field for Single Beat Read Response           | 135 |
|   | 5.9.5 | Compressed Response Field for a Write or Multi-Beat Read Response | 136 |
|   | 5.9.6 | Flow Control/NOP Field                                            | 137 |
|   | 5.10  | Recommended TL backoff modes                                      | 138 |
| 6 | Data  | Link                                                              | 139 |
|   | 6.1   | Overview                                                          | 139 |
|   | 6.2   | Data Link Features                                                | 140 |
|   | 6.2.1 | Packing Flits                                                     | 140 |
|   | 6.2.2 | DL message service                                                | 140 |
|   | 6.2.3 | UART                                                              | 140 |
|   | 6.2.4 | Tx Pacing, Rx Rate Adaptation                                     | 141 |
|   | 6.3   | Flit Format                                                       | 142 |
|   | 6.3.1 | DL Flit Overview                                                  | 142 |
|   | 6.3.2 | Flit Header                                                       | 143 |
|   | 6.3.3 | Segment Header                                                    | 143 |
|   | 6.3.4 | Flit packing rules                                                | 144 |
|   | 6.3.5 | TL Flit to DL Flit Mapping                                        | 147 |
|   | 6.3.6 | DL Flit to 64B/66B encoding                                       | 149 |
|   | 6.3.7 | CRC                                                               | 149 |
|   | 6.4   | DL messages                                                       | 150 |
|   | 6.4.1 | Message Overview                                                  | 150 |
|   | 6.4.2 | Basic Messages                                                    | 150 |
|   | 6.4.3 | Control Messages                                                  | 154 |
|   | 6.4.4 | UART Messages                                                     | 159 |
|   | 6.5   | Transmitter Pacing                                                | 164 |
|   | 6.5.1 | Overview                                                          | 164 |
|   | 6.5.2 | Switch                                                            | 164 |
|   | 6.5.3 | Accelerator                                                       | 165 |
|   | 6.5.4 | Sequence                                                          | 165 |
|   | 6.6   | Link Level Replay                                                 | 165 |
|   | 6.6.1 | Overview                                                          | 165 |
|   |       |                                                                   |     |

|   | _ |   |  |
|---|---|---|--|
|   |   |   |  |
|   |   | 3 |  |
|   | " |   |  |
|   |   | 7 |  |
|   |   |   |  |
|   |   |   |  |
|   |   |   |  |
|   |   |   |  |
|   |   |   |  |
|   |   |   |  |
| _ |   |   |  |
|   |   |   |  |
|   |   |   |  |
|   |   |   |  |

|   | 6.6.2 | Flit Header                       | 166 |
|---|-------|-----------------------------------|-----|
|   | 6.6.3 | Term Definitions                  | 167 |
|   | 6.6.4 | Rx Flags and Counters             | 168 |
|   | 6.6.5 | Tx Flags and Counters             | 169 |
|   | 6.6.6 | General Rules                     | 170 |
|   | 6.6.7 | Round Trip Time                   | 176 |
|   | 6.7   | Link State and Errors             | 177 |
|   | 6.7.1 | DL Link States                    | 177 |
|   | 6.7.2 | Correctable Errors                | 178 |
|   | 6.7.3 | Uncorrectable Errors              | 178 |
|   | 6.7.4 | Error Containment                 | 178 |
| 7 | Physi | cal Layer                         | 180 |
|   | 7.1   | Introduction                      | 180 |
|   | 7.2   | Reconciliation Sublayer (RS)      | 183 |
|   | 7.2.1 | Introduction                      | 183 |
|   | 7.2.2 | Data Flow                         | 183 |
|   | 7.2.3 | DL Flits                          | 183 |
|   | 7.2.4 | Control Flits                     | 184 |
|   | 7.2.5 | Data and Control Blocks and Codes | 185 |
|   | 7.2.6 | Link fault signaling              | 186 |
|   | 7.2.7 | Flit and Lane Alignment           | 187 |
|   | 7.2.8 | Receive State Machine             | 188 |
|   | 7.3   | PCS/PMA modifications             | 188 |
|   | 7.3.1 | Introduction                      | 188 |
|   | 7.3.2 | DL Flit to PCS codeword alignment | 188 |
|   | 7.3.3 | Reduced FEC interleave            | 189 |
|   | 7.3.4 | Decode Encode                     | 189 |
|   | 7.3.5 | Rate Matching                     | 189 |
|   | 7.3.6 | Back-to-Back DL Flits             | 190 |
|   | 7.4   | PCS and FEC for 100GBASE-R        | 191 |
|   | 7.4.1 | Removed functional Blocks         | 191 |
|   | 7.4.2 | Transmit Function                 | 192 |
|   | 7.4.3 | Receive Function                  | 192 |
|   | 7.5   | PCS for 200GBASE-R and 400GBASE-R | 194 |
|   | 7.5.1 | Transmit Function                 | 194 |
|   |       |                                   |     |

|   |   | 1 |
|---|---|---|
|   |   |   |
|   | _ |   |
|   |   |   |
|   |   |   |
| 1 |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
| - |   |   |
|   | 1 |   |
| " |   |   |
|   | 7 |   |
|   |   |   |
|   |   |   |
|   | 1 |   |
| " |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |

|   | 7.5.2  | Receive Function                                                          | 195 |
|---|--------|---------------------------------------------------------------------------|-----|
|   | 7.6    | PCS for 800GBASE-R                                                        | 196 |
|   | 7.6.1  | Transmit Function                                                         | 197 |
|   | 7.6.2  | Receive Function                                                          | 198 |
|   | 7.7    | Low Latency FEC Interleave                                                | 199 |
|   | 7.7.1  | 400GBASE-KR2/CR2 (2-way interleave)                                       | 199 |
|   | 7.7.2  | 200GBASE-KR1/CR1 (2-way interleave)                                       | 199 |
|   | 7.7.3  | 200GBASE-KR1/CR1 (1-way interleave)                                       | 199 |
| 8 | Mana   | geability Requirements                                                    | 203 |
|   | 8.1    | UALink Accelerators and System Nodes                                      | 203 |
|   | 8.2    | UALink Switches and Switch Platforms                                      | 203 |
|   | 8.3    | UALink Pod Controller                                                     | 204 |
|   | 8.4    | UALink Virtual Pods                                                       | 205 |
|   | 8.5    | Manageability Workflows                                                   | 206 |
| 9 | Secur  | ity                                                                       | 208 |
|   | 9.1    | References                                                                | 208 |
|   | 9.2    | System Overview                                                           | 208 |
|   | 9.3    | Security model                                                            | 209 |
|   | 9.3.1  | Security objectives:                                                      | 209 |
|   | 9.3.2  | Trusted Computing Base (TCB)                                              | 210 |
|   | 9.3.3  | Adversary profile and capabilities                                        | 210 |
|   | 9.3.4  | Security Assumptions                                                      | 211 |
|   | 9.3.5  | Threat model                                                              | 211 |
|   | 9.4    | UALink System Security                                                    | 212 |
|   | 9.5    | Encryption and authentication scheme for UALink                           | 215 |
|   | 9.5.1  | AES-GCM IV format                                                         | 216 |
|   | 9.5.2  | Control Half-Flit field encryption                                        | 217 |
|   | 9.5.3  | Control Half-Flit field authentication                                    | 217 |
|   | 9.5.4  | Data authentication and encryption                                        | 221 |
|   | 9.5.5  | Poisoned data handling with security enabled                              | 221 |
|   | 9.5.6  | ISOLATE response handling                                                 | 222 |
|   | 9.5.7  | Modes of operation                                                        | 222 |
|   | 9.5.8  | Ordering requirements imposed due to AES-GCM                              | 222 |
|   | 9.5.9  | Authentication and Encryption/Decryption Implementation in an UALink port | 223 |
|   | 9.5.10 | Initializing encrypted and authenticated transmission and reception       | 247 |
|   |        |                                                                           |     |

# Evaluation Copy

| (  | 9.5.1 | 1     | Refreshing an expired key                                                 | 248 |
|----|-------|-------|---------------------------------------------------------------------------|-----|
| (  | 9.5.1 | 2     | Safeguarding UALink configuration to ensure confidentiality and integrity | 249 |
| (  | 9.5.1 | 3     | Integrity failure handling                                                | 249 |
| (  | 9.5.1 | 4     | Switch requirements                                                       | 249 |
| (  | 9.5.1 | 5     | Key Derivation Function Requirements                                      | 249 |
| 10 | U     | ALinl | s Switch Requirements                                                     | 250 |
| 10 |       |       | rview                                                                     |     |
| 10 | .2    | Bifu  | rcation support                                                           | 250 |
| 10 | .3    | Loss  | eless Request and Response delivery                                       | 250 |
| 10 | .4    | Non   | -blocking architecture                                                    | 251 |
| 10 | .5    | Forv  | vard progress guarantee                                                   | 251 |
| 10 | .6    | Ord   | ering and Virtual Channels                                                | 251 |
| 10 | .7    | Rou   | ting Table Structure                                                      | 251 |
|    | 10.7. | 1     | Routing Table Instances                                                   | 252 |
|    | 10.7. | 2     | Egress port reachability                                                  | 252 |
| 10 | .8    | Con   | figuration                                                                | 252 |
| 10 | .9    | UAL   | ink Switch Recommendations and Goals                                      | 252 |
|    | 10.9. | 1     | Debug                                                                     | 252 |
|    | 10.9. | 2     | Latency goals                                                             | 253 |
|    | 10.9. | 3     | Performance goals                                                         | 253 |