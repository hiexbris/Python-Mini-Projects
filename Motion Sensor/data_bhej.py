import serial
import json
import time

# Define the serial port and baud rate
serial_port = 'COM8'  # Adjust this to match your Arduino's serial port
baud_rate = 9600

# Initialize serial communication
ser = serial.Serial(serial_port, baud_rate)


# Function to send JSON data over serial
def send_data(int1, int2):
    data = {'int1': int1, 'int2': int2}
    json_data = json.dumps(data)  # Serialize data to JSON format
    ser.write(json_data.encode())


# Function to read JSON file and send data
def read_and_send_data():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    # Extract integers from the data
    int1 = data['int1']
    int2 = data['int2']

    # Send data over serial
    send_data(int1, int2)


while True:
    read_and_send_data()
    time.sleep(1)
