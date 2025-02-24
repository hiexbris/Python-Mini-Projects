from flask import Flask, request, Response
import mysql.connector
from mysql.connector import Error
import requests
import json
import time
import string
import random

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'user': 'owa',
    'password': ')mn-bkrp35XFBzp-',
    'host': '',
    'database': 'nexus'
}

# Proxmox API Configuration
proxmox_config = {
    'host': '38.46.222.215',
    'user': 'root@pam',
    'password': 'Paradox_8008164715',
    'verify_ssl': False
}

# List of VM IDs for each tier
vm_ids = {
    'Lite - Classic': 123,
    'Standard - Classic': 124,
    'tier3': 102
}

def get_ticket():
    url = f"https://{proxmox_config['host']}:8006/api2/json/access/ticket"
    payload = {
        "username": proxmox_config['user'],
        "password": proxmox_config['password']
    }
    
    try:
        response = requests.post(url, data=payload, verify=False)  # verify=False to skip SSL verification
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        if 'data' in data and 'ticket' in data['data'] and 'CSRFPreventionToken' in data['data']:
            return data['data']['ticket'], data['data']['CSRFPreventionToken']
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None

def get_next_id(ticket, csrf_token):
    url = f"https://{proxmox_config['host']}:8006/api2/json/cluster/nextid"
    headers = {
        "Cookie": f"PVEAuthCookie={ticket}",
        "CSRFPreventionToken": csrf_token
    }
    
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data:
            return data['data']
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def clone_vm(ticket, csrf_token, vmid, newid, new_ip, new_name, password):
    url = f"https://{proxmox_config['host']}:8006/api2/json/nodes/pve/qemu/{vmid}/clone"
    headers = {
        "Cookie": f"PVEAuthCookie={ticket}",
        "CSRFPreventionToken": csrf_token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "newid": newid,
        "name": new_name
    }
    
    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data:
            clone_task = data['data']
            return monitor_clone_status(ticket, csrf_token, newid, new_ip, password)
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def monitor_clone_status(ticket, csrf_token, newid, new_ip, password):
    url = f"https://{proxmox_config['host']}:8006/api2/json/nodes/pve/qemu/{newid}/status/current"
    headers = {
        "Cookie": f"PVEAuthCookie={ticket}",
        "CSRFPreventionToken": csrf_token
    }
    
    try:
        while True:
            response = requests.get(url, headers=headers, verify=False)  # verify=False to skip SSL verification
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()
            
            if 'data' in data and 'lock' in data['data'] and data['data']['lock'] == 'clone':
                print("VM is still being cloned...")
                time.sleep(3)  # Wait for 3 seconds before checking again
            else:
                print("VM clone completed.")
                return start_vm(ticket, csrf_token, newid, new_ip, password)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def start_vm(ticket, csrf_token, newid, new_ip):
    url = f"https://{proxmox_config['host']}:8006/api2/json/nodes/pve/qemu/{newid}/status/start"
    headers = {
        "Cookie": f"PVEAuthCookie={ticket}",
        "CSRFPreventionToken": csrf_token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        response = requests.post(url, headers=headers, verify=False)  # verify=False to skip SSL verification
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        if 'data' in data:
            print("VM started successfully.")
            set_network_properties(ticket, csrf_token, newid, new_ip, password)
            return data['data']
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def set_network_properties(ticket, csrf_token, newid, new_ip, password):
    ping_url = f"https://{proxmox_config['host']}:8006/api2/json/nodes/pve/qemu/{newid}/agent/ping"
    exec_url = f"https://{proxmox_config['host']}:8006/api2/json/nodes/pve/qemu/{newid}/agent/exec"
    headers = {
        "Cookie": f"PVEAuthCookie={ticket}",
        "CSRFPreventionToken": csrf_token,
        "Content-Type": "application/json"
    }
    payload_ping = {}  # Empty payload for the ping request
    payload_exec = {
        "command": ["netsh", "interface", "ipv4", "set", "address", "name=Ethernet", "static", new_ip, "255.255.255.0", "172.98.54.1"]
    }
    
    try:
        while True:
            response = requests.post(ping_url, headers=headers, json=payload_ping, verify=False)  # verify=False to skip SSL verification
            print(f"Ping response status: {response.status_code}")
            print(f"Ping response content: {response.content}")
            if response.status_code == 200:
                print("Guest agent is up, setting network properties...")
                break
            else:
                print("Waiting for guest agent to be available...")
                time.sleep(3)  # Wait for 3 seconds before checking again
        
        response = requests.post(exec_url, headers=headers, json=payload_exec, verify=False)  # verify=False to skip SSL verification
        print(f"Exec response status: {response.status_code}")
        print(f"Exec response content: {response.content}")
        response.raise_for_status()  # Raise an error for bad status codes
        
        if response.status_code == 200:
            print("Network properties set successfully.")
            set_user_password(ticket, csrf_token, newid, "Administrator", password)
        else:
            print("Failed to set network properties.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def get_available_ip():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT server_ip FROM servers")
        used_ips = {row[0] for row in cursor.fetchall()}
        cursor.close()
        conn.close()
        print(f"Used IPs: {used_ips}")

        for i in range(1, 256):
            ip = f"172.98.54.{i}"
            if ip not in used_ips:
                return ip
    except Error as e:
        print(f"Error fetching used IPs: {e}")
        return None


def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(random.randint(12, 18)))

def set_user_password(ticket, csrf_token, newid, username, password):
    url = f"https://{proxmox_config['host']}:8006/api2/json/nodes/pve/qemu/{newid}/agent/set-user-password"
    headers = {
        "Cookie": f"PVEAuthCookie={ticket}",
        "CSRFPreventionToken": csrf_token,
        "Content-Type": "application/json"
    }
    payload = {
        "username": username,
        "password": password
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, verify=False)  # verify=False to skip SSL verification
        print(f"Set password response status: {response.status_code}")
        print(f"Set password response content: {response.content}")
        response.raise_for_status()  # Raise an error for bad status codes
        
        if response.status_code == 200:
            print(f"Password {password} set successfully.")
        else:
            print("Failed to set password.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


@app.route('/callback', methods=['POST'])
def sellix_callback():
    rawdata = request.json
    data = rawdata['data']
    
    if not data or 'recurring_billing_id' not in data or 'product_title' not in data:
        return Response("Invalid callback data", status=400)
    
    subscription_id = str(data['recurring_billing_id']).replace('rec_', '')
    if 'Lite' in data['product_title'] and 'Classic' in data['product_title']:
        tier = 'Lite - Classic'
    if 'Standard' in data['product_title'] and 'Classic' in data['product_title']:
        tier = 'Standard - Classic'
    
    if tier not in vm_ids:
        return Response("Invalid tier", status=400)
    
    available_ip = get_available_ip()

    if not available_ip:
        return Response("No available IP addresses", status=500)
    
    vmid = vm_ids[tier]

    ticket, csrf_token = get_ticket()
    if ticket and csrf_token:
        nextid = get_next_id(ticket, csrf_token)
        password = generate_random_password()
        if nextid:
            clone_result = clone_vm(ticket, csrf_token, vmid, nextid, available_ip, subscription_id, password)
            if clone_result:
                print(f"Clone Result: {clone_result}")
                try:
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO servers (sub_id, server_ip, password, proxmox_ip, email, tier) VALUES (%s, %s, %s, %s, %s, %s)",
                        (subscription_id, available_ip, password, proxmox_config['host'], data.get('customer_email', ''), tier)
                    )
                    conn.commit()
                    cursor.close()
                    conn.close()
                    print(f"Inserted server info into database: {subscription_id}, {available_ip}, {proxmox_config['host']}, {data.get('customer_email', '')}, {tier}")
                except Error as e:
                    print(f"Database error: {e}")
                    return Response(f"Database error: {e}", status=500)

                return Response("Server setup completed successfully.", status=200)
            else:
                print("Failed to clone the VM.")
                return Response("Failed to clone the VM.", status=500)
        else:
            print("Failed to obtain next ID.")
            return Response("Failed to obtain next ID.", status=500)
    else:
        print("Failed to obtain ticket and CSRF token.")
        return Response("Failed to obtain ticket and CSRF token.", status=500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
