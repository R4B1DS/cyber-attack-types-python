"""
Cyberattack Types
Santander Bootcamp x DIO - Python challenge

Reads a cyberattack name from input and prints its description.
"""

attack_input = input().strip()


def describe_attack(attack):
    if attack == "Phishing":
        return "Tricking users into giving away sensitive information"

    elif attack == "DDoS":
        return "Attacking a service with massive traffic to take it down"

    elif attack == "Malware":
        return "Malicious software designed to cause damage"

    elif attack == "Social Engineering":
        return "Psychological manipulation to gain access or data"


print(describe_attack(attack_input))
