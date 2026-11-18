#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Problem & Solution Recorder for Antigravity Expert Developer Brain
Allows any developer or agent to permanently record a solved problem so the brain
evolves and becomes smarter every day.
Dedicated to: Sudarsan Jena (Sudarsan Bhai)
"""

import os
import sys
import json
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
REGISTRY_PATH = os.path.join(KNOWLEDGE_DIR, "defect_registry.json")
LESSONS_PATH = os.path.join(KNOWLEDGE_DIR, "lessons_learned.md")

def record_lesson(title: str, symptom: str, permanent_solution: str, invariant_test: str, category: str = "GENERAL"):
    os.makedirs(KNOWLEDGE_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 1. Update JSON Registry
    registry = {"defects": []}
    if os.path.exists(REGISTRY_PATH):
        try:
            with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                registry = json.load(f)
        except Exception:
            registry = {"defects": []}
            
    def_id = f"DEF-{len(registry.get('defects', [])) + 1:03d}"
    new_entry = {
        "id": def_id,
        "title": title,
        "discovered": today,
        "invariant_test": invariant_test,
        "status": "PERMANENTLY_IMMUNIZED"
    }
    registry.setdefault("defects", []).append(new_entry)
    
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        
    # 2. Append to lessons_learned.md
    markdown_entry = f"""
- **Problem #{def_id}: {title}**
  - **Category:** {category}
  - **Symptom:** {symptom}
  - **Permanent Solution:** {permanent_solution}
  - **Automated Hard Gate:** `{invariant_test}`
  - **Recorded:** {today}
"""
    with open(LESSONS_PATH, "a", encoding="utf-8") as f:
        f.write(markdown_entry)
        
    print(f"✅ Successfully recorded {def_id}: {title} into Expert Developer Knowledge Base!")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        title = sys.argv[1]
        symptom = sys.argv[2]
        solution = sys.argv[3]
        test = sys.argv[4] if len(sys.argv) > 4 else "N/A"
        cat = sys.argv[5] if len(sys.argv) > 5 else "GENERAL"
        record_lesson(title, symptom, solution, test, cat)
    else:
        print("Usage: python record_solution.py <title> <symptom> <solution> [invariant_test] [category]")
