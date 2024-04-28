# FAQ Chatbot

A NVIDIA Jetson Nano RAG Chatbot is an AI-powered conversational assistant designed to run on the NVIDIA Jetson Nano platform. It utilizes the Retrieval Augmented Generation (RAG) architecture, which combines the power of retrieval-based and generation-based language models. This chatbot is capable of retrieving relevant information from a knowledge base and generating fluent and contextual responses. It can be deployed on the energy-efficient and compact Jetson Nano, making it suitable for embedded and edge computing based applications.

1. AI-powered conversational assistant for university students, designed for the NVIDIA Jetson Nano.
2. Specialized in answering frequently asked questions related to university life, admissions, academics, and student services.
3. Utilizes Retrieval Augmented Generation (RAG) architecture to retrieve relevant information from a university FAQ knowledge base.
4. Generates contextual and fluent responses based on the retrieved knowledge, tailored for university students' needs.
5. Deployable on the energy-efficient Jetson Nano platform for embedded and edge computing applications on campus.

![image](https://github.com/rlabconnect/NVIDIA-Jetson-Nano-RAG-Chatbot/assets/166736790/53549051-a671-4776-9f10-bbb2d8fda3bc)

**Youtube Link for demo**
https://youtu.be/_bGodEZf23s

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rlabconnect/NVIDIA-Jetson-Nano-RAG-Chatbot/ chatbot
   cd chatbot
   ```

## Why Docker?

Docker is being used here to provide a consistent and isolated environment for running the chatbot application. It allows us to package all the necessary dependencies and configurations into a single container, making it easier to deploy and manage the application across different platforms and environments. Additionally, Docker provides a lightweight and efficient runtime, which is especially beneficial for resource-constrained devices like the NVIDIA Jetson Nano. By using Docker, we can ensure that the chatbot application runs smoothly and consistently, regardless of the underlying system setup.

2. Install Docker:

   - For Ubuntu, run the following commands:

     ```bash
     sudo apt-get update
     sudo apt-get install docker.io
     ```

   - For other operating systems, refer to the official Docker documentation: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

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
