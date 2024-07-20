# SMTP Protocol Analysis and SMTP Spoofing Cyberattack

This project is divided into three parts: identifying the network protocol and cyberattack, preparing the environment for simulation, and demonstrating the cyberattack.

## Part 1: Identifying the Network Protocol and Cyberattack

In this part, we focus on the Simple Mail Transfer Protocol (SMTP) and its associated cyberattack, SMTP spoofing. We explore both the normal and abnormal operations of SMTP.

### Normal Operation

In normal operation, SMTP is used for sending and receiving email messages. It follows a standard procedure to ensure the delivery of messages between email servers.

### Abnormal Operation (SMTP Spoofing)

SMTP spoofing involves forging the sender's email address to make it appear as though the email is coming from a trusted source. This can be used for various malicious activities such as phishing attacks.

## Part 2: Preparing the Environment for Simulation

To simulate and analyze the SMTP spoofing attack, we prepared the following environment:

- **Python 3.10.11**: Ensured compatibility with required libraries.
- **Libraries**: Utilized `smtpd` and `asyncore` for the simulation.
- **Operating System**: Set up on Windows 11.

### Environment Setup

1. **Python Environment**: Ensure you have Python 3.10.11 installed.
2. **Library Installation**: Install the required libraries using the following command:

    ```bash
    pip install smtpd asyncore
    ```

3. **System Configuration**: Configure Windows 11 to accommodate the experiment.

## Part 3: Demonstrating the Cyberattack

In this part, we demonstrate the SMTP spoofing attack using the prepared environment.

### Steps to Demonstrate SMTP Spoofing

1. **Environment Check**: Ensure the environment from Part 2 is correctly set up.
2. **SMTP Servers**: Use SMTP servers to perform the spoofing attack.
3. **Execution**: Execute the attack by forging the sender's email address and sending spoofed emails.

### Demonstration Code

Below is a simplified example of how SMTP spoofing can be demonstrated:

```python
import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Message from:', mailfrom)
        print('Message to  :', rcpttos)
        print('Message data:', data)
        return

server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()
