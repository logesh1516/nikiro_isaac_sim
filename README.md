# Nikiro Isaac Sim

This repository contains NVIDIA Isaac Sim (USD) files for the Nikiro project - an autonomous mobile robot (AMR) platform designed for indoor navigation and manipulation tasks.

## Overview

Nikiro Isaac Sim provides the simulation environment and USD scene files needed to simulate the Nikiro robot platform within NVIDIA Isaac Sim. This enables physics-accurate simulation, sensor testing, and AI training workflows before deploying to real hardware.

## About Nikiro

Nikiro is a ROS 2-based Autonomous Mobile Robot (AMR) platform designed for indoor navigation using a differential drive system. The platform integrates:

- **SLAM (Simultaneous Localization and Mapping)**: Real-time environmental mapping and localization
- **Nav2 Navigation Stack**: Dynamic path planning and intelligent obstacle avoidance
- **Robot Manipulation**: Integration with robotic arms (like myCobot) for pick-and-place tasks
- **Industrial Workflows**: Support for conveyor systems and warehouse automation

For the complete ROS 2 simulation package, see the main [Nikiro Simulation repository](https://github.com/logesh1516/Nikiro_simulation).

## What is Isaac Sim?

NVIDIA Isaac Sim™ is a robotics simulation platform built on NVIDIA Omniverse that provides:

- **GPU-Accelerated Physics**: High-fidelity physics simulation powered by NVIDIA PhysX
- **RTX Rendering**: Physically accurate sensor simulation (cameras, LiDAR, etc.)
- **Robot Import**: Support for URDF, MJCF, and CAD formats
- **AI Training**: Integration with Isaac Lab for reinforcement learning
- **ROS Integration**: Seamless connection with ROS/ROS2 workflows
- **Synthetic Data Generation**: Tools for creating training datasets

## Repository Contents

This repository includes:

```
nikiro_isaac_sim/
└── src/
    └── USD scene files and assets for Nikiro robot simulation
```
## Usage

### Loading Nikiro in Isaac Sim

1. **Launch Isaac Sim**:
   ```bash
   # If installed via pip
   isaacsim
   
   # Or from binary installation
   cd isaacsim
   ./isaac-sim.sh
   ```

2. **Open the Nikiro Scene**:
   - Navigate to `File > Open`
   - Browse to the `src/` directory in this repository
   - Select the main Nikiro USD scene file

3. **Run Simulation**:
   - Click the "Play" button in the toolbar
   - Use the Isaac Sim controls to interact with the simulation

3. **ROS2 Bridge**:
```bash
    ros2 launch nikiro_navigation nikiro_navigation.launch.py
```
- Pose estimate the Robot.
- Give the location to navigate

## Features

### Simulated Capabilities

- **Differential Drive Navigation**: Test navigation algorithms in realistic physics
- **Sensor Simulation**: LiDAR, cameras, IMU, and contact sensors
- **SLAM Mapping**: Real-time map building and localization testing
- **Path Planning**: Nav2 integration for autonomous navigation
- **Manipulation**: Robot arm control and pick-and-place operations
- **Multi-Robot Scenarios**: Test fleet coordination and interaction

### Training Workflows

- **Reinforcement Learning**: Train navigation and manipulation policies
- **Imitation Learning**: Learn from demonstrations
- **Synthetic Data Generation**: Create training datasets for perception models
- **Sim-to-Real Transfer**: Validate algorithms before hardware deployment

## Project Structure

```
nikiro_isaac_sim/
├── src/                    # USD scene files and assets
│   ├── robot/             # Robot model USD files
│   ├── environments/      # Environment/world USD files
│   └── sensors/           # Sensor configuration files
└── README.md              # This file
```

**Note**: This repository contains the Isaac Sim USD files. For the complete ROS 2 simulation environment, visit the [Nikiro Simulation repository](https://github.com/logesh1516/Nikiro_simulation).
