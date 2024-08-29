import subprocess
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='logs/remediation.log', level=logging.INFO)

# Function to automatically scale up the cluster in case of high CPU usage
def scale_up_cluster(namespace, deployment_name, scale_factor=2):
    try:
        current_replicas = int(subprocess.check_output(
            ["kubectl", "get", "deployment", deployment_name, "-n", namespace, "-o=jsonpath='{.spec.replicas}'"]
        ).decode('utf-8').strip("'"))
        
        new_replicas = current_replicas * scale_factor
        subprocess.run(["kubectl", "scale", "--replicas", str(new_replicas), "deployment", deployment_name, "-n", namespace], check=True)
        logging.info(f"{datetime.now()}: Scaled deployment {deployment_name} to {new_replicas} replicas in namespace {namespace}")
    except subprocess.CalledProcessError as e:
        logging.error(f"{datetime.now()}: Failed to scale deployment {deployment_name} in namespace {namespace}: {e}")

if __name__ == "__main__":
    scale_up_cluster("default", "example-deployment")
