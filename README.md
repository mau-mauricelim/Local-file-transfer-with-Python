# Local-file-transfer-with-Python

## Send files using Python on the same WIFI or Online

1) Run the server_send_file.py first and enter the [filename.type] to send.
2) Run the client_recv_file.py next and enter the Server's IP address as shown in the server_send_file cmd prompt


## 2 ways for online connectivity:
Single port forwarding (Insecure) or port triggering (More secure)

### Single port forwarding: 
"if a client comes looking for a configured port it will be forwarded to a configured machine (static IP address)"
---This port configured will always be open and vulnerable to possible attacks.

### Port triggering: 
"the port in the configured port range will only open when the host runs the server"
---This port will close when the server is terminated

##### For these methods, only the host can run the server as currently the client is the one looking for the port.
##### This can be improved by modifying the script to include sending and receiving inputs.
