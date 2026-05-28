# Traffic Signal Optimization at Macapagal Avenue – Tubod Intersection

[![SUMO](https://img.shields.io/badge/SUMO-1.26.0-blue.svg)](https://eclipse.dev/sumo/)
[![NetEdit](https://img.shields.io/badge/Netedit-1.26.0-red.svg)](https://eclipse.dev/netedit/)
[![Python](https://img.shields.io/badge/Python-3.14%2B-green.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-yellow.svg)](https://pandas.pydata.org/)

## Background
This repository contains the files for the traffic simulation models and data analysis scripts for evaluating signal timing performance at the **Macapagal Avenue – Tubod Intersection** in Iligan City, Philippines. 

The study utilizes **SUMO (Simulation of Urban MObility)** to compare the existing static (fixed-time) traffic signal configuration against a proposed **Actuated (Dynamic) Signal Control** system. Performance is evaluated across three distinct time-of-day scenarios using real-world AADT (Annual Average Daily Traffic), K-factors, and directional splits.

## Study Area
The  Macapagal Avenue - Tubod Intersection junction 
consists of four main lanes–the northbound lanes (Roxas Avenue 
in Tubod Bridge), southbound lanes (Roxas Avenue in Tubod 
Bridge), Talipapa lanes (Lanao del Norte Interior Circumferential 
Road), and Caltex lanes (President Diosdado Macapagal Avenue 
Road).

### Simulated Scenarios
The study analyzes three peak periods, modeled to reflect actual commuter tidal flows:
1. **Morning Peak (7:00 - 8:00 AM):** K-Factor 0.09 | 80% Northbound / 20% Southbound
2. **Midday Off-Peak (12:00 - 1:00 PM):** K-Factor 0.06 | 60% Northbound / 40% Southbound
3. **Afternoon Peak (4:00 - 5:00 PM):** K-Factor 0.085 | 30% Northbound / 70% Southbound

## File Structure

```text
├── baseline_cases/                 # Static traffic signal configurations (control group)
│   ├── morning_baseline_case/
│      ├── outputs_morning
│          ├── edge_data.xml
│          ├── queues.xml
│          ├── tripinfo.xml
│          ├── parse_results.py
│      ├── morning_baseline.sumocfg
│      ├── detectors.add.xml
│      ├── inital8_network.net.xml
│      ├── routes_morning.rou.xml
│   ├── midday_baseline_case/
│   └── afternoon_baseline_case/
├── modified_cases/                # Actuated (dynamic) signal configurations
│   ├── modified_morning/
│      ├── outputs_morning
│          ├── edge_data.xml
│          ├── queues.xml
│          ├── tripinfo.xml
│          ├── parse_results.py
│      ├── morning_baseline.sumocfg
│      ├── detectors.add.xml
│      ├── inital8_network.net.xml
│      ├── routes_morning.rou.xml
│   ├── modified_midday/
│   └── modified_afternoon/
