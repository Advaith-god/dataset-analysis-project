"""
Dataset Analysis Project
Author: Intern Project
Description: Analyzes student performance dataset and generates an automatic report.
"""

import pandas as pd
import os
from datetime import datetime


def load_dataset(filepath):
    """Load the student dataset from CSV file."""
    df = pd.read_csv(filepath)
    print(f"[INFO] Dataset loaded successfully. Total records: {len(df)}")
    return df


def calculate_totals_and_averages(df):
    """Calculate total marks and average for each student."""
    subject_cols = ['Math', 'Science', 'English', 'History', 'Computer']
    df['Total'] = df[subject_cols].sum(axis=1)
    df['Average'] = df[subject_cols].mean(axis=1).round(2)
    df['Grade'] = df['Average'].apply(assign_grade)
    return df


def assign_grade(avg):
    """Assign grade based on average marks."""
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'


def find_top_student(df):
    """Find the top-performing student."""
    top_idx = df['Total'].idxmax()
    return df.loc[top_idx]


def department_wise_analysis(df):
    """Perform department-wise analysis."""
    subject_cols = ['Math', 'Science', 'English', 'History', 'Computer', 'Total', 'Average']
    dept_analysis = df.groupby('Department')[subject_cols].mean().round(2)
    dept_count = df.groupby('Department')['StudentID'].count().rename('Student Count')
    dept_analysis = dept_analysis.join(dept_count)
    return dept_analysis


def generate_report(df, top_student, dept_analysis, output_path):
    """Generate a text analysis report and save it."""
    subject_cols = ['Math', 'Science', 'English', 'History', 'Computer']
    lines = []
    lines.append("=" * 60)
    lines.append("       STUDENT PERFORMANCE ANALYSIS REPORT")
    lines.append("=" * 60)
    lines.append(f"Generated on : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Dataset      : students_performance.csv")
    lines.append(f"Total Records: {len(df)}")
    lines.append("")

    # Overall Stats
    lines.append("-" * 60)
    lines.append("OVERALL STATISTICS")
    lines.append("-" * 60)
    lines.append(f"Highest Average Score : {df['Average'].max()}")
    lines.append(f"Lowest Average Score  : {df['Average'].min()}")
    lines.append(f"Class Average Score   : {df['Average'].mean().round(2)}")
    lines.append(f"Highest Total Marks   : {df['Total'].max()}")
    lines.append(f"Lowest Total Marks    : {df['Total'].min()}")
    lines.append("")

    # Subject-wise averages
    lines.append("-" * 60)
    lines.append("SUBJECT-WISE CLASS AVERAGES")
    lines.append("-" * 60)
    for subject in subject_cols:
        lines.append(f"  {subject:<12}: {df[subject].mean().round(2)}")
    lines.append("")

    # Top Student
    lines.append("-" * 60)
    lines.append("TOP PERFORMING STUDENT")
    lines.append("-" * 60)
    lines.append(f"  Name       : {top_student['Name']}")
    lines.append(f"  Student ID : {top_student['StudentID']}")
    lines.append(f"  Department : {top_student['Department']}")
    lines.append(f"  Total Marks: {top_student['Total']}")
    lines.append(f"  Average    : {top_student['Average']}")
    lines.append(f"  Grade      : {top_student['Grade']}")
    lines.append("")

    # Department-wise analysis
    lines.append("-" * 60)
    lines.append("DEPARTMENT-WISE ANALYSIS")
    lines.append("-" * 60)
    for dept, row in dept_analysis.iterrows():
        lines.append(f"\n  Department: {dept}")
        lines.append(f"    Student Count  : {int(row['Student Count'])}")
        lines.append(f"    Average Total  : {row['Total']}")
        lines.append(f"    Average Score  : {row['Average']}")
        for subject in subject_cols:
            lines.append(f"    Avg {subject:<10}: {row[subject]}")
    lines.append("")

    # Grade Distribution
    lines.append("-" * 60)
    lines.append("GRADE DISTRIBUTION")
    lines.append("-" * 60)
    grade_dist = df['Grade'].value_counts().sort_index()
    for grade, count in grade_dist.items():
        lines.append(f"  Grade {grade}: {count} student(s)")
    lines.append("")

    # All students summary
    lines.append("-" * 60)
    lines.append("ALL STUDENTS SUMMARY")
    lines.append("-" * 60)
    lines.append(f"  {'ID':<6} {'Name':<18} {'Dept':<20} {'Total':<8} {'Avg':<8} {'Grade'}")
    lines.append("  " + "-" * 68)
    for _, row in df.sort_values('Total', ascending=False).iterrows():
        lines.append(f"  {row['StudentID']:<6} {row['Name']:<18} {row['Department']:<20} {row['Total']:<8} {row['Average']:<8} {row['Grade']}")
    lines.append("")
    lines.append("=" * 60)
    lines.append("              END OF REPORT")
    lines.append("=" * 60)

    # Save report
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))

    print(f"[INFO] Report saved to: {output_path}")
    return '\n'.join(lines)


def main():
    # File paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, 'data', 'students_performance.csv')
    report_path = os.path.join(base_dir, 'output', 'analysis_report.txt')

    print("\n==============================")
    print("  DATASET ANALYSIS PROJECT")
    print("==============================\n")

    # Step 1: Load dataset
    df = load_dataset(dataset_path)

    # Step 2: Calculate totals and averages
    df = calculate_totals_and_averages(df)
    print("[INFO] Totals and averages calculated.")

    # Step 3: Find top student
    top_student = find_top_student(df)
    print(f"[INFO] Top student identified: {top_student['Name']}")

    # Step 4: Department-wise analysis
    dept_analysis = department_wise_analysis(df)
    print("[INFO] Department-wise analysis completed.")

    # Step 5: Generate report
    report = generate_report(df, top_student, dept_analysis, report_path)
    print("[INFO] Analysis complete!\n")
    print(report)


if __name__ == "__main__":
    main()
