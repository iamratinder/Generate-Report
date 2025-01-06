import pandas as pd
from ydata_profiling import ProfileReport
import sys

def generate_profile_report(file_path):
    df = pd.read_csv(file_path)
    profile = ProfileReport(
        df,
        title="Pandas Profiling Report",
        explorative=True  # Enables an explorative mode with additional visualizations and insights
    )
    report_file_path = file_path.replace('.csv', '_report.html')
    profile.to_file(report_file_path)

    return report_file_path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    report_path = generate_profile_report(input_file_path)
    print(f"Report generated: {report_path}")
