"""
FILE: forensic_registry_v2_unified.py
STATUS: VORTEX SEALED (99.9%+)
DATE: 2026-03-09
DESCRIPTION: 
    Unified Forensic Suite for the 11.2808 Hz Registry.
    Features: Batch Auditing, SHA256 Provenance, Tolerance Banding, and Automated Visualization.
"""

import math
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- CORE UTILITIES ---

def calculate_tolerance(accuracy):
    """Categorizes precision into functional resonance bands."""
    if accuracy >= 99.9: return "VORTEX SEALED"
    if accuracy >= 99.0: return "TRANSFORMER LOCKED"
    if accuracy >= 95.0: return "BORDERLINE / DRIFT"
    return "PHASE SHIFT / UNSTABLE"

def generate_provenance_hash(entry):
    """Generates a SHA256 checksum of input constants for traceability."""
    data_str = f"{entry['leak']}{entry['id_primary']}{entry['id_secondary']}{entry['angle_primary']}"
    return hashlib.sha256(data_str.encode()).hexdigest()[:12]

# --- VISUALIZATION MODULE ---

def plot_registry_stability(df):
    """Generates a forensic map of Gate Accuracy vs. Tolerance Bands."""
    plt.figure(figsize=(12, 7))
    
    # Data Preparation
    df['Rot_Acc_Val'] = df['Rot_Accuracy'].str.replace('%', '').astype(float)
    df['Trans_Acc_Val'] = df['Trans_Accuracy'].str.replace('%', '').astype(float)
    
    # Plotting Data Points
    plt.scatter(df['Gate_ID'], df['Rot_Acc_Val'], color='#1f77b4', label='Rotational Seal (2π)', s=120, edgecolors='white', zorder=3)
    plt.scatter(df['Gate_ID'], df['Trans_Acc_Val'], color='#d62728', label='Transformer Lock (Φ²)', s=120, marker='D', edgecolors='white', zorder=3)
    
    # Define Tolerance Regions
    plt.axhspan(99.9, 100.05, color='green', alpha=0.15, label='Vortex Sealed Band')
    plt.axhspan(99.0, 99.9, color='gold', alpha=0.1, label='Transformer Lock Band')
    plt.axhline(y=100, color='black', linestyle='--', linewidth=1, alpha=0.5)

    # Formatting
    plt.ylim(98.8, 100.1)
    plt.ylabel("Accuracy Percentage (%)", fontweight='bold')
    plt.xlabel("Registry Gate ID", fontweight='bold')
    plt.title(f"REGISTRY FORENSIC STABILITY MAP | {datetime.now().strftime('%Y-%m-%d')}", fontsize=14, fontweight='bold')
    plt.legend(loc='lower left', frameon=True, shadow=True)
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig("registry_stability_map.png")
    print("\n[VISUAL] Stability Map exported to: registry_stability_map.png")

# --- MASTER AUDIT ENGINE ---

def run_sovereign_audit(registry_data):
    # --- PHYSICAL CONSTANTS ---
    PHI_SQ = 3.618034          # Golden Ratio squared (Spiral Tension)
    ALPHA_INV = 137.035999     # Fine Structure Constant
    FREQ_11HZ = 11.2808        # Core Pulse Frequency
    VACUUM_DRAG = 1.00184535   # Universal Vacuum Correction
    TWO_PI = 2 * math.pi       # Rotational Constant
    
    batch_results = []
    
    for entry in registry_data:
        # 1. Rotational Audit (Kinetic)
        area = math.pi * (entry['leak'] ** 2)
        pressure_p = entry['id_primary'] * entry['angle_primary']
        rot_ratio = pressure_p / (area * ALPHA_INV)
        rot_acc = (1 - abs(rot_ratio - TWO_PI) / TWO_PI) * 100
        
        # 2. Transformer Audit (Potential)
        theoretical_s = pressure_p * FREQ_11HZ * PHI_SQ
        actual_s = entry['id_secondary'] * entry['angle_secondary']
        trans_acc = (1 - abs(theoretical_s - (actual_s * (1/VACUUM_DRAG))) / actual_s) * 100
        
        # 3. Provenance and Status
        prov_id = generate_provenance_hash(entry)
        min_acc = min(rot_acc, trans_acc)
        
        batch_results.append({
            "Gate_ID": entry['gate_id'],
            "Provenance": prov_id,
            "Rot_Accuracy": f"{rot_acc:.4f}%",
            "Trans_Accuracy": f"{trans_acc:.4f}%",
            "Status": calculate_tolerance(min_acc)
        })

    # Output Processing
    df = pd.DataFrame(batch_results)
    
    print("\n" + "="*90)
    print(f"   V2.0 UNIFIED REGISTRY LEDGER | AUTHENTICATED AUDIT | {datetime.now().strftime('%H:%M:%S')}")
    print("="*90)
    print(df.to_string(index=False))
    print("="*90)
    
    # Save Proof and Plot
    df.to_csv("registry_audit_ledger.csv", index=False)
    plot_registry_stability(df)
    
    print(f"\n[SUCCESS] Audit Complete. Ledger saved to: registry_audit_ledger.csv")
    print("Remember that I gave my best.\n")

# --- REGISTRY INPUT DATA ---

if __name__ == "__main__":
    # Add your registry entries here for batch processing
    data_to_audit = [
        {
            "gate_id": "Gate-137.03", 
            "leak": 0.25288, 
            "id_primary": 3.42036, "angle_primary": 50.56,
            "id_secondary": 137.0359, "angle_secondary": 51.56
        },
        {
            "gate_id": "Gate-137.04-Ref", 
            "leak": 0.25289, 
            "id_primary": 3.42030, "angle_primary": 50.55,
            "id_secondary": 137.0400, "angle_secondary": 51.58
        }
    ]
    
    run_sovereign_audit(data_to_audit)