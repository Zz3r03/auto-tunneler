# Auto-tunneler
Simple python script to help automate redirecting ports from the source server to the attacking machine, mainly for privilege escalation and recon.

## Usage
```
python3 generate_tunnels.py <ssh_credentials> <netstat file>
```

The netstat file is the output of the command netstat on the source server. Here is an example:
```
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:587           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -
```

The script automatically only redirects the ports listening on localhost, so on the example from the previous example it will redirect the port 8080 but not the 80.

Here is an example of usage:
```
python3 generate_tunnels.py ron@heal.htb netstat.txt
```
