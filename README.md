# FAQ Chatbot

![Block Diagram](block_diagram.png)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rlabconnect/NVIDIA-Jetson-Nano-RAG-Chatbot/
   cd chatbot
   ```

## Docker Deployment

1. Build the Docker image:

   ```bash
   docker build -t chatbot .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8501:8501 chatbot
   ```

## Access the Chatbot

Once the Docker container is running, you can access the chatbot by navigating to:

```bash
http://localhost:8501
```

## Format a bootable SD card:

1. Insert the bootable SD card into your computer's SD card slot.
2. Open the Command Prompt as an administrator.
3. Type 'diskpart' and press Enter to open the DiskPart utility.
4. In the DiskPart prompt, type 'list disk' and press Enter to view the list of available disks.
5. Identify the disk number associated with your SD card. Make sure to select the correct disk to avoid data loss.
6. Type 'select disk <disk_number>' and press Enter, replacing <disk_number> with the actual disk number of your SD card.
7. To clean the SD card, type 'clean' and press Enter. This will remove all partitions and data from the SD card.
8. Create a new primary partition by typing 'create partition primary' and pressing Enter.
9. To select the newly created partition, type 'select partition 1' and press Enter.
10. Format the partition by typing 'format fs=fat32 quick' and pressing Enter. This will format the partition as FAT32 with a quick format.
11. Assign a drive letter to the partition by typing 'assign letter=<drive_letter>' and pressing Enter, replacing <drive_letter> with the desired drive letter (e.g., E:).
12. To make the SD card bootable, type 'active' and press Enter.
13. Exit DiskPart by typing 'exit' and pressing Enter.

## Connect to WiFi on Jetson Nano

1. Run the following command to list the available WiFi networks:

   ```bash
   nmcli device wifi list
   ```

   This will display a list of available WiFi networks along with their SSID, mode, and signal strength.

2. Identify the SSID of the WiFi network you want to connect to.

3. Run the following command to connect to the WiFi network:
   ```bash
   nmcli device wifi connect <SSID> password <password>
   ```
4. You can verify the connection by running the following command:
   ```bash
   nmcli device status
   ```
