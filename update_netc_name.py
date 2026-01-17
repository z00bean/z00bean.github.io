#!/usr/bin/env python3

import os
import re

# List of all project files
project_files = [
    "miso-rag-llm.html",
    "railroad-trespassing.html",
    "traffic-camera.html", 
    "edge-learning.html",
    "crosswalk-net.html",
    "thermal-uav.html",
    "work-zone-safety.html",
    "netc-ai-studies.html",
    "truck-rollover.html",
    "trip-generation.html",
    "bento.html"
]

def update_project_file(filename):
    filepath = f"projects/{filename}"
    
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist, skipping...")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace "NETC AI Studies" with "NETC Pilot AI Studies" in navigation links
    content = re.sub(
        r'>NETC AI Studies</a>',
        r'>NETC Pilot AI Studies</a>',
        content
    )
    
    # Replace in current page span (for the netc-ai-studies.html page itself)
    content = re.sub(
        r'<span>NETC AI Studies</span>',
        r'<span>NETC Pilot AI Studies</span>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

# Update all project files
for filename in project_files:
    update_project_file(filename)

print("All project files updated with new NETC name!")