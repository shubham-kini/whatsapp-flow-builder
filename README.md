# WhatsApp Flow Builder

A modular approach to building WhatsApp Flows.  
Instead of editing one giant JSON in WhatsApp Manager IDE, you can split it into smaller files (`screens/`, `version.json`, `routing_model.json`) and compile them back into one `flow.json`.

---

## 🚀 Features

- Modular JSON structure
- Easy to extend with more screens
- Demo screens included (`demo_services.json`, `demo_summary.json`)

---

## 📂 Project Structure

---

## 🔧 Usage

1. Clone this repository:

   ````bash
   git clone https://github.com/YOUR_USERNAME/whatsapp-flow-builder.git
   cd whatsapp-flow-builder```

   ````

2. Add/edit your screen JSON files inside the screens/ folder.

   1. Start from the provided demo screens.
   2. Add as many screens as needed.

3. Run the builder:
   `python builder.py`

4. The compiled flow.json will be generated inside /output.

5. Copy-paste this into the WhatsApp Manager IDE.
