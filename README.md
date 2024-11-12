# Email and Phone Number Extractor

This program extracts email addresses and phone numbers from text copied to the clipboard. It identifies multiple formats, including international phone numbers and U.S.-formatted numbers with optional extensions.

## How It Works

1. The program captures text from the clipboard.
2. It uses regex patterns to find:
   - Emails.
   - International and Nigerian phone numbers.
   - American phone numbers with or without extensions.
3. Extracted email addresses and phone numbers are displayed in the console.

## Getting Started

### Prerequisites

- **Python** (3.7+)
- **pyperclip** library for clipboard interaction
- **re** module (standard Python regex module)

Install `pyperclip` with:
```bash
pip install pyperclip
```

### Usage

1. Copy the text containing emails and phone numbers to your clipboard.
2. Run the script:
    ```bash
    python email_phone_extractor.py
    ```
3. The extracted emails and phone numbers will appear in the console.

### Example

Given this input:

```
Reach us at support@example.com or (123) 456-7890 ext. 123. For international inquiries, call +1234567890123.
```

The program will output:

```
support@example.com
123-456-7890 x123
+2348567890123
```
