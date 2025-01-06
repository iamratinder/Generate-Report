from flask import Flask, request, render_template, send_file, url_for
import os, subprocess
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No File Uploaded'
    
    file = request.files['file']
    
    if file.filename == '':
        return "No Selected File"
    
    upload_folder = './upload/'
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    result = subprocess.run(['python', 'main.py', file_path], capture_output=True, text=True)

    if result.returncode != 0:
        return f"Error generating report: {result.stderr}"
    
    report_file_path = os.path.join(upload_folder, file.filename.replace('.csv', '_report.html'))
    return render_template('report.html', report_file=url_for('view_report', filename=os.path.basename(report_file_path)))

    



@app.route('/view_report/<filename>', methods=['GET'])
def view_report(filename):
    report_path = os.path.join('./upload/', filename)
    
    if not os.path.exists(report_path):
        return "File not found", 404
    
    return send_file(report_path, as_attachment=False, mimetype='text/html')

@app.route('/download_report/<filename>', methods=['GET'])
def download_report(filename):
    report_path = os.path.join('./upload/', filename)
    
    if not os.path.exists(report_path):
        return "File not found", 404
    
    return send_file(report_path, as_attachment=True, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)