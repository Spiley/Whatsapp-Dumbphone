import subprocess
import sys

def run_deployment():
    try:
        # Build the container image
        subprocess.run(["docker", "build", "--no-cache", "-t", "nokia-wa", "."], check=True)

        # Start the container and capture its ID
        container_id = subprocess.check_output(
            ["docker", "run", "-d", "--env-file", ".env", "-p", "3000:3000", "nokia-wa"],
            text=True
        ).strip()

        print(f"Container started with ID: {container_id}")

        # Follow logs
        subprocess.run(["docker", "logs", "-f", container_id])

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting log stream.")

if __name__ == "__main__":
    run_deployment()