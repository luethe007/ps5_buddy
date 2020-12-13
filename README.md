# Amazon PS5 Buddy
## Automatize your PS5 availability checks

### Install

This project requires **Python 3.x** and the following Python libraries installed:

- [Selenium](https://selenium-python.readthedocs.io/)
- [webdriver manager](https://pypi.org/project/webdriver-manager/)
- [twilio](https://www.twilio.com/docs/libraries/python).

### Code

The code has been created as I wanted to automatize my availability checks for the PlayStation 5 from Sony. It automatically checks if the PS5 is available on Amazon and immediately sends a WhatsApp to your smartphone.

It switches between amazon and clearing the browser cache. It only stops when the availability status changes.

### Run

In a terminal or command window, run one the following command:

```bash
python ps5_buddy.py
```  
