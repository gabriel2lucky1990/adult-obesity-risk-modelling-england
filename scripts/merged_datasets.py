#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 17:32:06 2026

@author: gabriellucky
"""

import pandas as pd
import os


folder_path = "/Users/gabriellucky/Downloads/mydataset/"

print("="*70)
print("MERGING FINGERTIPS DATASETS")
print("="*70)
print(f"\nLooking for files in: {folder_path}")


# CHECK IF FILES EXIST

files_needed = [
    'indicators-CountiesUAsfromApr2023_data.csv',
    'indicators-CountiesUAsfromApr2023_data__1_.csv',
    'indicators-CountiesUAsfromApr2023_data__2_.csv',
    'indicators-CountiesUAsfromApr2023_data__3_.csv'
]

print("\nChecking for files...")
missing_files = []
for file in files_needed:
    if os.path.exists(folder_path + file):
        print(f"   ✓ Found: {file}")
    else:
        print(f"   ✗ MISSING: {file}")
        missing_files.append(file)

if missing_files:
    print("\n❌ ERROR: Some files are missing!")
    print("   Please make sure all 4 CSV files are in your mydataset folder.")
    print("\n   Files in your mydataset folder:")
    for item in os.listdir(folder_path):
        if item.endswith('.csv'):
            print(f"      - {item}")
else:
    print("\n✅ All files found! Starting merge...")
    
    
    # LOAD THE FILES
    
    print("\n1. Loading files...")
    
    obesity = pd.read_csv(folder_path + 'indicators-CountiesUAsfromApr2023_data.csv', 
                          usecols=['Area Code', 'Area Name', 'Time period', 'Value'])
    print(f"   ✓ Obesity: {len(obesity)} rows")
    
    activity = pd.read_csv(folder_path + 'indicators-CountiesUAsfromApr2023_data__1_.csv',
                           usecols=['Area Code', 'Area Name', 'Time period', 'Value'])
    print(f"   ✓ Activity: {len(activity)} rows")
    
    diet = pd.read_csv(folder_path + 'indicators-CountiesUAsfromApr2023_data__3_.csv',
                       usecols=['Area Code', 'Area Name', 'Time period', 'Value'])
    print(f"   ✓ Diet: {len(diet)} rows")
    
    print("   Loading smoking data (filtering for adults)...")
    smoking_full = pd.read_csv(folder_path + 'indicators-CountiesUAsfromApr2023_data__2_.csv')
    smoking = smoking_full[(smoking_full['Sex'] == 'Persons') & 
                           (smoking_full['Age'] == '18+ yrs')].copy()
    smoking = smoking[['Area Code', 'Area Name', 'Time period', 'Value']]
    del smoking_full
    print(f"   ✓ Smoking (filtered): {len(smoking)} rows")
    
    
    # PROCESS VARIABLES
    
    print("\n2. Processing variables...")
    
    obesity['year'] = obesity['Time period'].str.split('/').str[0].astype(int)
    obesity = obesity.rename(columns={'Value': 'obesity_prevalence'})
    obesity = obesity[['Area Code', 'Area Name', 'year', 'obesity_prevalence']]
    
    activity['year'] = activity['Time period'].str.split('/').str[0].astype(int)
    activity = activity.rename(columns={'Value': 'physical_inactivity'})
    activity = activity[['Area Code', 'Area Name', 'year', 'physical_inactivity']]
    
    smoking['year'] = smoking['Time period'].astype(int)
    smoking = smoking.rename(columns={'Value': 'smoking_prevalence'})
    smoking = smoking[['Area Code', 'Area Name', 'year', 'smoking_prevalence']]
    
    diet['year'] = diet['Time period'].str.split('/').str[0].astype(int)
    diet = diet.rename(columns={'Value': 'diet_5_a_day_pct'})
    diet = diet[['Area Code', 'Area Name', 'year', 'diet_5_a_day_pct']]
    
    print("   ✓ All variables processed")
    
    # MERGE ALL 4 DATASETS
    
    print("\n3. Merging datasets...")
    
    merged = obesity.merge(activity, on=['Area Code', 'Area Name', 'year'], how='inner')
    print(f"   After obesity + activity: {len(merged)} rows")
    
    merged = merged.merge(smoking, on=['Area Code', 'Area Name', 'year'], how='inner')
    print(f"   After adding smoking: {len(merged)} rows")
    
    merged = merged.merge(diet, on=['Area Code', 'Area Name', 'year'], how='inner')
    print(f"   After adding diet: {len(merged)} rows")

    
    # CLEAN DATA
    
    print("\n4. Cleaning data...")
    
    # Remove England (national aggregate)
    merged = merged[merged['Area Name'] != 'England'].copy()
    
    # Remove any missing values
    merged = merged.dropna()
    
    print(f"   ✓ Final dataset: {len(merged)} rows")
    
    
    # SUMMARY STATISTICS
    
    print("\n" + "="*70)
    print("✅ MERGE COMPLETE!")
    print("="*70)
    
    print(f"\n📊 Dataset Summary:")
    print(f"   Total observations: {len(merged)}")
    print(f"   Local Authorities: {merged['Area Name'].nunique()}")
    print(f"   Years covered: {sorted(merged['year'].unique())}")
    
    print(f"\n📈 Variables:")
    print(f"   - obesity_prevalence")
    print(f"   - physical_inactivity")
    print(f"   - smoking_prevalence")
    print(f"   - diet_5_a_day_pct")
    
    print("\n📉 Summary Statistics:")
    print(merged[['obesity_prevalence', 'physical_inactivity', 
                  'smoking_prevalence', 'diet_5_a_day_pct']].describe().round(2))
    
    print("\n🔍 First 10 rows:")
    print(merged.head(10))
    
    
    # SAVE THE MERGED DATASET
    
    output_file = folder_path + 'FINGERTIPS_MERGED_COMPLETE.csv'
    merged.to_csv(output_file, index=False)
    
    print(f"\n💾 SAVED TO: {output_file}")
    print("\n🎉 YOUR DATASET IS READY FOR ANALYSIS!")
    print("="*70)
