from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = (
    b'gAAAAABcbdMdPLUYCT3RVg5rXsjfYahQkFITyYPu8JsOzh1ICn_fcHQvrj1wfQP3ZsfgE8tI'
    b'_V5mUOLDvOozi-aoqalq7KPv4KerCQVGNugSJSxWQupP6se0cQVdXriqK9T7lZRbMZvG6EBqx'
    b'UHJ_mRR51UoF70ZN2Ekb7YeUSs6Hb5wifs41IQ='
)

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
