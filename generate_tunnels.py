import re
import sys
import subprocess

def extract_ports(text):
    return sorted(set(re.findall(r'127\.0\.0\.1:(\d+)', text)), key=int)

def build_ssh_command(ports, remote_host):
    ssh_cmd = ["ssh", "-N"]
    for port in ports:
        ssh_cmd.extend(["-L", f"{port}:localhost:{port}"])
    ssh_cmd.append(remote_host)
    return ssh_cmd

def main():
    if len(sys.argv) < 2:
        print("Usage: ./single_ssh_tunnel.py <user@host> [input_file]")
        print("Example: ./single_ssh_tunnel.py user@example.com ss_output.txt")
        sys.exit(1)

    remote_host = sys.argv[1]
    input_text = sys.stdin.read() if len(sys.argv) == 2 else open(sys.argv[2]).read()
    ports = extract_ports(input_text)

    if not ports:
        print("❌ No 127.0.0.1 ports found in input.")
        return

    ssh_cmd = build_ssh_command(ports, remote_host)
    print("🔗 SSH Command:")
    print(" ".join(ssh_cmd))

    try:
        subprocess.run(ssh_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ SSH failed: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Tunnel stopped.")

if __name__ == "__main__":
    main()
