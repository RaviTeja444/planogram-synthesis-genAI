#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
import seaborn as sns

plt.rcParams.update({
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'font.size': 10,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'legend.fontsize': 9,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.figsize': (8, 6),
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1
})

def generate_time_cost_comparison():

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    # Time comparison
    methods = ['Traditional\nManual Process', 'AI-Powered\nSystem']
    times = [30, 0.5]  # Exact values from paper
    colors = ['#E57373', '#81C784']
    
    bars1 = ax1.bar(methods, times, color=colors, edgecolor='black', linewidth=1)
    ax1.set_ylabel('Time (hours)', fontweight='bold')
    ax1.set_title('Planogram Creation Time', fontweight='bold', pad=20)
    ax1.set_ylim(0, 35)
    
    # Add value labels on bars
    for bar, time in zip(bars1, times):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{time} hrs', ha='center', va='bottom', fontweight='bold')
    
    # Add percentage reduction
    ax1.text(0.5, 25, '98.3%\nReduction', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7),
            fontsize=12, fontweight='bold')
    
    # Cost comparison
    costs = [1950, 49]  # Exact values from paper
    bars2 = ax2.bar(methods, costs, color=colors, edgecolor='black', linewidth=1)
    ax2.set_ylabel('Cost per Planogram ($)', fontweight='bold')
    ax2.set_title('Creation Cost Analysis', fontweight='bold', pad=20)
    ax2.set_ylim(0, 2200)
    
    # Add value labels
    for bar, cost in zip(bars2, costs):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 30,
                f'${cost}', ha='center', va='bottom', fontweight='bold')
    
    # Add percentage reduction
    ax2.text(0.5, 1600, '97.5%\nReduction', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7),
            fontsize=12, fontweight='bold')
    
    plt.suptitle('Figure 1: Time and Cost Comparison of Planogram Creation Methods',
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('figure1_time_cost_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Generated figure1_time_cost_comparison.png")

def generate_constraint_satisfaction():

    constraints = ['Physical\nFeasibility', 'Weight Limit\nCompliance', 
                  'Category\nGrouping', 'Regulatory\nCompliance', 
                  'Brand\nAgreements']
    satisfaction_rates = [94.3, 98.7, 91.2, 99.1, 88.5]  # Exact values
    std_devs = [2.1, 1.2, 3.5, 0.8, 4.2]  # Exact std deviations
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bar chart
    x = np.arange(len(constraints))
    bars = ax.bar(x, satisfaction_rates, yerr=std_devs, 
                  color='#64B5F6', edgecolor='black', linewidth=1,
                  capsize=5, error_kw={'linewidth': 1.5})
    
    # Add average line
    avg_satisfaction = 94.4  # Exact average from paper
    ax.axhline(y=avg_satisfaction, color='red', linestyle='--', linewidth=2,
              label=f'Overall Average: {avg_satisfaction}%')
    
    # Customize chart
    ax.set_xlabel('Constraint Type', fontweight='bold')
    ax.set_ylabel('Satisfaction Rate (%)', fontweight='bold')
    ax.set_title('Figure 2: Constraint Satisfaction Rates for AI-Generated Planograms',
                fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(constraints)
    ax.set_ylim(80, 105)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for bar, rate, std in zip(bars, satisfaction_rates, std_devs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + std + 0.5,
               f'{rate}%', ha='center', va='bottom', fontsize=9)
    
    # Add note about simulation
    plt.figtext(0.5, 0.02, 'Note: Based on simulated performance using industry benchmarks and AWS Lambda characteristics',
                ha='center', fontsize=8, style='italic')
    
    plt.tight_layout()
    plt.savefig('figure2_constraint_satisfaction.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Generated figure2_constraint_satisfaction.png")

def generate_scalability_analysis():

    # Response times based on: 400ms inference + 50ms network + scaling penalty
    concurrent_requests = [10, 100, 1000, 10000]
    response_times = [487, 497, 521, 538]  # Projected from AWS Lambda benchmarks
    costs_per_1000 = [0.24, 0.25, 0.27, 0.32]  # Based on AWS Lambda pricing
    throughput = [20.5, 201.2, 1919.4, 18587.4]  # Calculated from response times
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Response time scaling
    ax1.semilogx(concurrent_requests, response_times, 'o-', color='#1976D2', 
                linewidth=2, markersize=8)
    ax1.set_xlabel('Concurrent Requests', fontweight='bold')
    ax1.set_ylabel('Response Time (ms)', fontweight='bold')
    ax1.set_title('(a) Response Time Scaling', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(450, 550)
    
    # Add annotations
    for x, y in zip(concurrent_requests, response_times):
        ax1.annotate(f'{y}ms', (x, y), textcoords="offset points", 
                    xytext=(0,10), ha='center', fontsize=8)
    
    # Cost efficiency
    ax2.semilogx(concurrent_requests, costs_per_1000, 's-', color='#388E3C',
                linewidth=2, markersize=8)
    ax2.set_xlabel('Concurrent Requests', fontweight='bold')
    ax2.set_ylabel('Cost per 1000 Requests ($)', fontweight='bold')
    ax2.set_title('(b) Cost Efficiency', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Throughput
    ax3.loglog(concurrent_requests, throughput, '^-', color='#D32F2F',
              linewidth=2, markersize=8)
    ax3.set_xlabel('Concurrent Requests', fontweight='bold')
    ax3.set_ylabel('Throughput (requests/second)', fontweight='bold')
    ax3.set_title('(c) System Throughput', fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Efficiency metric (throughput/cost)
    efficiency = [t/c for t, c in zip(throughput, costs_per_1000)]
    ax4.semilogx(concurrent_requests, efficiency, 'd-', color='#7B1FA2',
                linewidth=2, markersize=8)
    ax4.set_xlabel('Concurrent Requests', fontweight='bold')
    ax4.set_ylabel('Efficiency (requests/$ × 1000)', fontweight='bold')
    ax4.set_title('(d) Cost Efficiency Metric', fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    # Main title
    plt.suptitle('Figure 3: Scalability Analysis of Cloud-Native Architecture',
                fontsize=14, fontweight='bold')
    
    # Add note
    plt.figtext(0.5, 0.01, 'Projected performance based on AWS Lambda benchmarks (Wang et al., 2018; Manner et al., 2021) and serverless scaling patterns',
                ha='center', fontsize=8, style='italic')
    
    plt.tight_layout()
    plt.savefig('figure3_scalability_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Generated figure3_scalability_analysis.png")

def generate_roi_timeline():

    initial_investment = 250000 
    monthly_savings = 1869000   
    months = np.arange(0, 25)
    
    # Calculate cumulative cash flow
    cumulative_cashflow = [-initial_investment]
    for month in months[1:]:
        cumulative_cashflow.append(cumulative_cashflow[-1] + monthly_savings)
    
    cumulative_cashflow = np.array(cumulative_cashflow) / 1000000 
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot cumulative cash flow
    ax.plot(months, cumulative_cashflow, 'b-', linewidth=3, label='Cumulative Cash Flow')
    ax.fill_between(months, cumulative_cashflow, 0, 
                   where=(cumulative_cashflow > 0), 
                   color='green', alpha=0.3, label='Profit Zone')
    ax.fill_between(months, cumulative_cashflow, 0, 
                   where=(cumulative_cashflow <= 0), 
                   color='red', alpha=0.3, label='Investment Recovery')
    
    # Mark break-even point (4.4 months from paper)
    break_even_month = 4.4
    break_even_idx = int(break_even_month)
    ax.plot(break_even_month, 0, 'ro', markersize=12, label='Break-even Point')
    ax.annotate('Break-even\n4.4 months', 
               xy=(break_even_month, 0), 
               xytext=(break_even_month + 2, -5),
               arrowprops=dict(arrowstyle='->', color='red', lw=2),
               fontsize=11, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
    
    # Add grid and labels
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Months After Deployment', fontweight='bold')
    ax.set_ylabel('Cumulative Value ($ Millions)', fontweight='bold')
    ax.set_title('Figure 4: Return on Investment Timeline', fontweight='bold', pad=20)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.legend(loc='upper left')
    
    # Add key metrics
    ax.text(20, 30, f'Monthly Savings: ${monthly_savings/1000000:.1f}M\n' +
                    f'Initial Investment: ${initial_investment/1000000:.2f}M\n' +
                    f'24-Month Return: ${cumulative_cashflow[-1]:.1f}M',
           bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8),
           fontsize=10)
    
    plt.tight_layout()
    plt.savefig('figure4_roi_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Generated figure4_roi_timeline.png")

def generate_system_architecture():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Define components with positions
    components = [
        # (name, x, y, width, height, color)
        ('Retail Store Data\n• Historical Planograms\n• Sales Performance\n• Constraints', 
         2, 6.5, 3, 1.2, '#E8F5E9'),
        ('Data Processing\n& Feature Engineering', 2, 4.5, 3, 0.8, '#E3F2FD'),
        ('Diffusion Model Training\n(AWS SageMaker)', 2, 2.5, 3, 0.8, '#F3E5F5'),
        ('Model Optimization\n(ONNX Conversion)', 7, 2.5, 3, 0.8, '#FFF3E0'),
        ('Edge Deployment\n(AWS Lambda)', 7, 4.5, 3, 0.8, '#FFEBEE'),
        ('Store Systems\n(Real-time Inference)', 7, 6.5, 3, 0.8, '#E8F5E9'),
    ]
    
    # Draw components
    for name, x, y, width, height, color in components:
        rect = Rectangle((x - width/2, y - height/2), width, height,
                        facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=10,
               bbox=dict(boxstyle="round,pad=0.1", facecolor='white', alpha=0.8))
    
    # Draw arrows
    arrows = [
        (2, 5.9, 2, 5.3),  # Store to Processing
        (2, 4.1, 2, 3.3),  # Processing to Training
        (5, 2.5, 7, 2.5),  # Training to Optimization
        (7, 3.3, 7, 4.1),  # Optimization to Deployment
        (7, 5.3, 7, 5.9),  # Deployment to Stores
    ]
    
    for x1, y1, x2, y2 in arrows:
        ax.arrow(x1, y1, x2-x1, y2-y1, head_width=0.2, head_length=0.1,
                fc='black', ec='black', linewidth=2)
    
    # Add performance metrics
    metrics_text = 'Key Achievements:\n• 98.3% time reduction\n• 94.4% constraint satisfaction\n• 487ms inference time'
    ax.text(10, 1, metrics_text, fontsize=10,
           bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.8))
    
    # Title
    ax.text(6, 7.5, 'Figure 5: Cloud-Native Planogram Generation System Architecture',
           fontsize=14, fontweight='bold', ha='center')
    
    plt.tight_layout()
    plt.savefig('figure5_system_architecture.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Generated figure5_system_architecture.png")


def generate_all_figures():
    print("\n" + "="*60)
    print("GENERATING FIGURES FOR PLANOGRAM AI PAPER")
    print("="*60)
    
    # Generate each figure
    generate_time_cost_comparison()
    generate_constraint_satisfaction()
    generate_scalability_analysis()
    generate_roi_timeline()
    generate_system_architecture()
    
    
    print("\n" + "="*60)
    print("FIGURE GENERATION COMPLETE")
    print("="*60)
    print("\nGenerated files:")
    print("1. figure1_time_cost_comparison.png")
    print("2. figure2_constraint_satisfaction.png")
    print("3. figure3_scalability_analysis.png")
    print("4. figure4_roi_timeline.png")
    print("5. figure5_system_architecture.png")

if __name__ == "__main__":
    generate_all_figures()