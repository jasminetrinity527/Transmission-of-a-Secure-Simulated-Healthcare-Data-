import time
import random #added for random numbers
import json
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet #add fernet for cryptography

#secret key for encryption (added)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#def function for the bp readings randoms numbers as 70 150
def simulate_bp_readings(encrypt_data=False): #added for encryption
    bp_readings = []
    timestamps = []
    for _ in range(120):  # 2 minutes
        bp = random.randint(70, 150) #the random number that was in the project tasks
        if encrypt_data:
            encrypted_bp = cipher_suite.encrypt(str(bp).encode())
            bp_readings.append(encrypted_bp)
        else:
            bp_readings.append(bp)
        timestamps.append(time.time())
        time.sleep(1) #added time sleep 1 instead of 4
    return timestamps, bp_readings

#def function to dcrypt #added
def decrypt_data(encrypted_data):
    return [int(cipher_suite.decrypt(data).decode()) for data in encrypted_data] #dcryption

#encryption
timestamps_encrypted, bp_readings_encrypted = simulate_bp_readings(encrypt_data=True)
decrypted_bp_readings = decrypt_data(bp_readings_encrypted)

#dcryption
timestamps_unencrypted, bp_readings_unencrypted = simulate_bp_readings(encrypt_data=False)

#plots for the bp reading #added
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(timestamps_encrypted, decrypted_bp_readings, label='Encrypted BP Readings', color='pink')
plt.plot(timestamps_unencrypted, bp_readings_unencrypted, label='Unencrypted BP Readings', color='blue')
plt.title('Blood Pressure Reading')
plt.xlabel('Time')
plt.ylabel('Blood Pressure')
plt.legend()

#byte sizes for the bp readings #added
byte_sizes_encrypted = [len(data) for data in bp_readings_encrypted]
byte_sizes_unencrypted = [len(str(data).encode()) for data in bp_readings_unencrypted]

#plots for sizes for dcryption and encyprtion
plt.subplot(2, 1, 2)
plt.plot(timestamps_encrypted, byte_sizes_encrypted, label='Encrypted Data Size', color='yellow')
plt.plot(timestamps_unencrypted, byte_sizes_unencrypted, label='Unencrypted Data Size', color='purple')
plt.title('Data Size')
plt.xlabel('Time')
plt.ylabel('Data Size (bytes)')
plt.legend()

plt.tight_layout()
plt.show()
