import json
import os

data1 = {
  "figure": {
    "id": "Figure 1-1",
    "title": "UALink Based Multi-Accelerator System",
    "page": 0,
    "type": "BLOCK DIAGRAM",
    "purpose": "Illustrates an example system with multiple nodes connecting Hosts, Accelerators and Switches"
  },
  "technical_summary": [
    "System has M Accelerators and each Accelerator has N Ports.",
    "A single OS image controls and manages each System Node (OS Domain).",
    "UALink Switches connect the Accelerators together.",
    "UALink connection has 2 lanes @ 212.5G."
  ],
  "components": [
    {
      "name": "OS Domain",
      "type": "System Node",
      "description": "Boundary containing HOST and Accelerators"
    },
    {
      "name": "HOST",
      "type": "Processor",
      "description": "Host processor connected to Accelerators"
    },
    {
      "name": "ACC",
      "type": "Accelerator",
      "description": "Accelerator with multiple ports"
    },
    {
      "name": "Switch",
      "type": "Switch",
      "description": "UALink Switch"
    }
  ],
  "interfaces": [
    {
      "name": "Host-ACC Link",
      "from": "HOST",
      "to": "ACC",
      "direction": "bidirectional",
      "signals": []
    },
    {
      "name": "UALink",
      "from": "ACC",
      "to": "Switch",
      "direction": "bidirectional",
      "signals": []
    }
  ],
  "signals": [],
  "registers": [],
  "packet_layout": [],
  "state_machine": {
    "initial_state": "",
    "states": [],
    "transitions": []
  },
  "timing": {
    "signals": [],
    "events": [],
    "ordering": [],
    "constraints": []
  },
  "pipeline": {
    "ordered_flow": []
  },
  "algorithm": {
    "steps": []
  },
  "tables": [],
  "equations": [],
  "constraints": [],
  "rules": [],
  "assumptions": [],
  "important_constants": [],
  "cross_references": [],
  "keywords": ["UALink", "Accelerator", "Switch", "OS Domain"],
  "entities": [],
  "relationships": [
    {
      "source": "HOST",
      "relation": "connects_to",
      "target": "ACC"
    },
    {
      "source": "ACC",
      "relation": "connects_to",
      "target": "Switch"
    }
  ],
  "knowledge_triples": [],
  "llm_notes": {
    "critical_facts": ["Accelerators connect to Switches via UALink with 2 lanes @ 212.5G"],
    "potential_ambiguities": [],
    "missing_information": []
  },
  "confidence": 0.95
}

data2 = {
  "figure": {
    "id": "Figure 1-2",
    "title": "Accelerator communication over a direct link and over a Switch",
    "page": 2,
    "type": "BLOCK DIAGRAM",
    "purpose": "Shows Direct Connected vs Switch Connected topologies"
  },
  "technical_summary": [
    "Direct connected topology links two Acc units via UALink.",
    "Switch connected topology links multiple Acc units via a ULS (UALink Switch).",
    "Hosts connect to Ethernet Switch Fabric via NICs.",
    "Hosts connect to Accelerators via PCIe."
  ],
  "components": [
    {"name": "Ethernet Switch Fabric", "type": "Switch", "description": "Ethernet network connecting nodes"},
    {"name": "NIC", "type": "Network Interface", "description": "Connects host to Ethernet"},
    {"name": "Host", "type": "Processor", "description": "Host processor"},
    {"name": "Acc", "type": "Accelerator", "description": "Accelerator device"},
    {"name": "OS-Domain", "type": "Domain", "description": "OS boundary containing Host and Acc"},
    {"name": "ULS", "type": "Switch", "description": "UALink Switch"}
  ],
  "interfaces": [
    {"name": "Ethernet", "from": "NIC", "to": "Ethernet Switch Fabric", "direction": "bidirectional", "signals": []},
    {"name": "PCIe", "from": "Host", "to": "NIC", "direction": "bidirectional", "signals": []},
    {"name": "Host-Acc", "from": "Host", "to": "Acc", "direction": "bidirectional", "signals": []},
    {"name": "UALink (Direct)", "from": "Acc", "to": "Acc", "direction": "bidirectional", "signals": []},
    {"name": "UALink (Switched)", "from": "Acc", "to": "ULS", "direction": "bidirectional", "signals": []}
  ],
  "signals": [],
  "registers": [],
  "packet_layout": [],
  "state_machine": {"initial_state": "", "states": [], "transitions": []},
  "timing": {"signals": [], "events": [], "ordering": [], "constraints": []},
  "pipeline": {"ordered_flow": []},
  "algorithm": {"steps": []},
  "tables": [],
  "equations": [],
  "constraints": [],
  "rules": [],
  "assumptions": [],
  "important_constants": [],
  "cross_references": [],
  "keywords": ["PCIe", "Ethernet", "UALink", "ULS", "OS-Domain"],
  "entities": [],
  "relationships": [
    {"source": "Host", "relation": "connects_to", "target": "Acc"},
    {"source": "Host", "relation": "connects_to", "target": "NIC"},
    {"source": "Acc", "relation": "connects_to", "target": "ULS"}
  ],
  "knowledge_triples": [],
  "llm_notes": {"critical_facts": [], "potential_ambiguities": [], "missing_information": []},
  "confidence": 0.95
}

data3 = {
  "figure": {
    "id": "Figure 1-3",
    "title": "UALink Stack",
    "page": 3,
    "type": "BLOCK DIAGRAM",
    "purpose": "Illustrates the UALink stack layers"
  },
  "technical_summary": [
    "UALink200 Stack contains Protocol, Transaction, Data, and PHY layers.",
    "UPLI interface is between Functional/Protocol Layer and Transaction Layer.",
    "Transaction Layer interfaces with Data Layer using TL Flit (64B).",
    "Data Layer interfaces with Ethernet PHY Layer using DL Flit (640B).",
    "PHY layer connects via 200G Serial Link / SerDes."
  ],
  "components": [
    {"name": "Accelerator Functional/Protocol Layer", "type": "Layer", "description": ""},
    {"name": "Switch/Accelerator Functional/Protocol Layer", "type": "Layer", "description": ""},
    {"name": "Transaction Layer Protocol FLITs", "type": "Layer", "description": ""},
    {"name": "Data Layer DL FLITs", "type": "Layer", "description": ""},
    {"name": "Ethernet PHY Layer", "type": "Layer", "description": ""}
  ],
  "interfaces": [
    {"name": "UPLI", "from": "Protocol Layer", "to": "Transaction Layer", "direction": "bidirectional", "signals": []},
    {"name": "Transaction Layer Interface", "from": "Transaction Layer", "to": "Data Layer", "direction": "bidirectional", "signals": []},
    {"name": "Data Link Layer Interface", "from": "Data Layer", "to": "Ethernet PHY Layer", "direction": "bidirectional", "signals": []},
    {"name": "Serial Link SerDes", "from": "Ethernet PHY Layer", "to": "Ethernet PHY Layer", "direction": "bidirectional", "signals": []}
  ],
  "signals": [],
  "registers": [],
  "packet_layout": [],
  "state_machine": {"initial_state": "", "states": [], "transitions": []},
  "timing": {"signals": [], "events": [], "ordering": [], "constraints": []},
  "pipeline": {"ordered_flow": []},
  "algorithm": {"steps": []},
  "tables": [],
  "equations": [],
  "constraints": [],
  "rules": [],
  "assumptions": [],
  "important_constants": ["TL Flit (64B)", "DL Flit (640B)", "200G"],
  "cross_references": [],
  "keywords": ["UPLI", "TL", "DL", "PHY", "FLIT"],
  "entities": [],
  "relationships": [],
  "knowledge_triples": [],
  "llm_notes": {"critical_facts": [], "potential_ambiguities": [], "missing_information": []},
  "confidence": 0.95
}

data4 = {
  "figure": {
    "id": "Figure 1-4",
    "title": "UALink cross-domain address translation model",
    "page": 5,
    "type": "BLOCK DIAGRAM",
    "purpose": "Shows how GVA translates to NPA and then SPA across the UALink Network"
  },
  "technical_summary": [
    "Source Accelerator translates Guest Virtual Address (GVA) to Network Physical Address (NPA) using Acc MMU.",
    "NPA traverses the UALink Network through UALink Switches.",
    "Destination Accelerator translates NPA to System Physical Address (SPA) using Link MMU.",
    "SPA accesses local HBM on Destination Accelerator."
  ],
  "components": [
    {"name": "CU", "type": "Compute Unit", "description": ""},
    {"name": "Acc MMU", "type": "MMU", "description": "Translates GVA to NPA"},
    {"name": "UALink", "type": "Interface", "description": ""},
    {"name": "UALink Switches", "type": "Switch", "description": ""},
    {"name": "Link MMU", "type": "MMU", "description": "Translates NPA to SPA"},
    {"name": "HBM", "type": "Memory", "description": "High Bandwidth Memory"}
  ],
  "interfaces": [
    {"name": "GVA -> NPA", "from": "CU", "to": "Acc MMU", "direction": "unidirectional", "signals": []},
    {"name": "NPA -> SPA", "from": "Link MMU", "to": "HBM", "direction": "unidirectional", "signals": []}
  ],
  "signals": [],
  "registers": [],
  "packet_layout": [],
  "state_machine": {"initial_state": "", "states": [], "transitions": []},
  "timing": {"signals": [], "events": [], "ordering": [], "constraints": []},
  "pipeline": {"ordered_flow": []},
  "algorithm": {"steps": []},
  "tables": [],
  "equations": [],
  "constraints": [],
  "rules": [],
  "assumptions": [],
  "important_constants": [],
  "cross_references": [],
  "keywords": ["GVA", "NPA", "SPA", "MMU", "HBM"],
  "entities": [],
  "relationships": [],
  "knowledge_triples": [],
  "llm_notes": {"critical_facts": [], "potential_ambiguities": [], "missing_information": []},
  "confidence": 0.95
}

data5 = {
  "figure": {
    "id": "Figure 1-5",
    "title": "Translation Process",
    "page": 6,
    "type": "BLOCK DIAGRAM",
    "purpose": "Details the address translation bits and process"
  },
  "technical_summary": [
    "Process VA goes through Source translate (ACC MMU).",
    "AT=b1 selects Network PA (Cross Domain).",
    "AT=b0 selects Local Host SPA.",
    "NPA[51:42] = DstAccID[9:0], NPA[41:0] = Address[41:0].",
    "Destination LNK MMU translates NPA to SPA[51:0]."
  ],
  "components": [
    {"name": "Process VA", "type": "Process", "description": ""},
    {"name": "Source translate", "type": "Translation Logic", "description": ""},
    {"name": "Dest. Translate", "type": "Translation Logic", "description": ""}
  ],
  "interfaces": [],
  "signals": [
    {"name": "AT", "description": "Address Type", "direction": "internal", "width": 1},
    {"name": "NPA", "description": "Network Physical Address", "direction": "cross-domain", "width": 52},
    {"name": "SPA", "description": "System Physical Address", "direction": "internal", "width": 52}
  ],
  "registers": [],
  "packet_layout": [
    {"field": "DstAccID", "bits": "51:42", "description": "Destination Accelerator ID in NPA", "valid_values": []},
    {"field": "Address", "bits": "41:0", "description": "Address bits in NPA", "valid_values": []}
  ],
  "state_machine": {"initial_state": "", "states": [], "transitions": []},
  "timing": {"signals": [], "events": [], "ordering": [], "constraints": []},
  "pipeline": {"ordered_flow": []},
  "algorithm": {"steps": []},
  "tables": [],
  "equations": [],
  "constraints": [],
  "rules": [],
  "assumptions": [],
  "important_constants": [],
  "cross_references": [],
  "keywords": ["AT", "GVA", "NPA", "SPA"],
  "entities": [],
  "relationships": [],
  "knowledge_triples": [],
  "llm_notes": {"critical_facts": [], "potential_ambiguities": [], "missing_information": []},
  "confidence": 0.95
}

with open("_page_0_Figure_6.json", "w") as f:
    json.dump(data1, f, indent=2)

with open("_page_2_Figure_4.json", "w") as f:
    json.dump(data2, f, indent=2)

with open("_page_3_Figure_9.json", "w") as f:
    json.dump(data3, f, indent=2)

with open("_page_5_Figure_4.json", "w") as f:
    json.dump(data4, f, indent=2)

with open("_page_6_Figure_3.json", "w") as f:
    json.dump(data5, f, indent=2)

# Update MD file
md_file = "1_Introduction.md"
with open(md_file, "r") as f:
    content = f.read()

replacements = {
    "![](_page_0_Figure_6.jpeg)": "![](_page_0_Figure_6.jpeg)\\n\\n[JSON Extraction](_page_0_Figure_6.json)",
    "![](_page_2_Figure_4.jpeg)": "![](_page_2_Figure_4.jpeg)\\n\\n[JSON Extraction](_page_2_Figure_4.json)",
    "![](_page_3_Figure_9.jpeg)": "![](_page_3_Figure_9.jpeg)\\n\\n[JSON Extraction](_page_3_Figure_9.json)",
    "![](_page_5_Figure_4.jpeg)": "![](_page_5_Figure_4.jpeg)\\n\\n[JSON Extraction](_page_5_Figure_4.json)",
    "![](_page_6_Figure_3.jpeg)": "![](_page_6_Figure_3.jpeg)\\n\\n[JSON Extraction](_page_6_Figure_3.json)"
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(md_file, "w") as f:
    f.write(content)

print("Done generating JSONs and updating MD")
