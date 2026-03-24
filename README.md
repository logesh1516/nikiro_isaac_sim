<div align="center">

```
███╗   ██╗██╗██╗  ██╗██╗██████╗  ██████╗ 
████╗  ██║██║██║ ██╔╝██║██╔══██╗██╔═══██╗
██╔██╗ ██║██║█████╔╝ ██║██████╔╝██║   ██║
██║╚██╗██║██║██╔═██╗ ██║██╔══██╗██║   ██║
██║ ╚████║██║██║  ██╗██║██║  ██║╚██████╔╝
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝
         × NVIDIA ISAAC SIM
```

### **Physics-Accurate AMR Simulation on NVIDIA Omniverse**
*USD · RTX Rendering · GPU Physics · ROS 2 Bridge · AI-Ready*

[![Isaac Sim](https://img.shields.io/badge/NVIDIA-Isaac%20Sim-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/isaac-sim)
[![Omniverse](https://img.shields.io/badge/Omniverse-Platform-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://www.nvidia.com/en-us/omniverse/)
[![ROS2](https://img.shields.io/badge/ROS2-Humble-blue?style=for-the-badge&logo=ros)](https://docs.ros.org/en/humble/)
[![USD](https://img.shields.io/badge/Format-USD-lightgrey?style=for-the-badge)](https://openusd.org/)

</div>

---

## 🧠 Why Isaac Sim?

Gazebo is great. Isaac Sim is a **different league**.

Nikiro's Isaac Sim integration brings **GPU-accelerated physics**, **RTX-quality sensor simulation**, and **AI training pipelines** to the same robot platform — letting you validate algorithms, generate synthetic datasets, and train real policies before a single wheel turns on real hardware.

> 🎯 **The goal:** Close the sim-to-real gap so tight it almost disappears.

---

## ✨ What Makes This Special

| Capability | Powered By |
|------------|------------|
| ⚡ GPU-Accelerated Physics | NVIDIA PhysX |
| 📷 Photorealistic Sensor Sim | RTX Ray Tracing |
| 🗺️ SLAM + Localization | Nav2 + ROS 2 Bridge |
| 🤖 AI Policy Training | Isaac Lab (RL / IL) |
| 🏭 Industrial Workflows | Conveyor + Manipulation |
| 📦 Synthetic Data Gen | Omniverse Replicator |
| 🔁 Sim-to-Real Transfer | Validated USD → Hardware |

---

## 📁 Repository Structure

```
nikiro_isaac_sim/
├── src/
│   ├── robot/              # Nikiro USD robot model files
│   ├── environments/       # World & warehouse scene USDs
│   └── sensors/            # LiDAR, camera, IMU configs
└── README.md
```

---

## 🚀 Getting Started

### Step 1 — Launch Isaac Sim

```bash
# Via pip install
isaacsim

# Via binary installation
cd isaacsim && ./isaac-sim.sh
```

### Step 2 — Open the Nikiro Scene

1. Go to **File → Open**
2. Navigate to the `src/` directory in this repo
3. Select the main Nikiro `.usd` scene file
4. Hit **▶ Play** in the toolbar

### Step 3 — Connect ROS 2 Bridge

```bash
ros2 launch nikiro_navigation nikiro_navigation.launch.py
```

Once the bridge is live:
- 📍 **Set an initial pose estimate** in RViz2
- 🎯 **Send a Nav2 goal** — watch Nikiro plan and navigate in real-time

---

## 🎮 Simulated Capabilities

### Navigation & Perception
- **Differential Drive** — test kinematics and odometry under realistic physics
- **LiDAR / Camera / IMU** — RTX-rendered sensor data, no approximations
- **SLAM Mapping** — build and localize against maps in real-time
- **Nav2 Path Planning** — full autonomous navigation with dynamic obstacle avoidance


### AI & Training Workflows
- **Reinforcement Learning** — train navigation/manipulation policies via Isaac Lab
- **Imitation Learning** — record and replay demonstrations
- **Synthetic Data Generation** — build perception training datasets at scale
- **Sim-to-Real Validation** — stress-test before any hardware deployment

---

## 📸 Simulation Preview

<div align="center">

| Isaac Sim Scene | Action Graph |
|:-:|:-:|
| ![Nikiro Isaac Sim Scene](https://raw.githubusercontent.com/logesh1516/nikiro_isaac_sim/ad7bf43bc10e9c9774a069e0233d69cbe3d79608/src/usd/scene.png) | ![Action Graph](https://raw.githubusercontent.com/logesh1516/nikiro_isaac_sim/ad7bf43bc10e9c9774a069e0233d69cbe3d79608/src/usd/action_graph.png) |

</div>

---

## 🌐 The Nikiro Ecosystem

Nikiro spans three interconnected repositories:

```
┌─────────────────────────────────────────────────────┐
│                  NIKIRO ECOSYSTEM                   │
│                                                     │
│  🧪 Nikiro_simulation   →  ROS2 + Gazebo + Nav2    │
│  🐳 Nikiro_docker       →  Containerized Deploy    │
│  🟢 Nikiro_isaac_sim    →  GPU Sim + AI Training   │
│                     
└─────────────────────────────────────────────────────┘
```

| Repo | Purpose | Link |
|------|---------|------|
| **Nikiro_simulation** | Full ROS 2 sim with SLAM, conveyor & arm | [→ View](https://github.com/logesh1516/Nikiro_simulation) |
| **Nikiro_docker** | One-command containerized deployment | [→ View](https://github.com/logesh1516/Nikiro_docker) |
| **Nikiro_isaac_sim** | NVIDIA Isaac Sim USD scenes & AI workflows | *you're here* |

---

<div align="center">

Built with 🟢 NVIDIA Isaac Sim + 🤖 ROS 2 by **Logesh S (Loki)**
*Because real robots deserve real physics.*

</div>
