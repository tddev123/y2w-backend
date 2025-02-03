from flask import Blueprint, request, jsonify, send_file
from ..services.downloader import download_from_url
import os

download_bp = Blueprint('download', __name__)

@download_bp.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')
    format = data.get('format')
    
    if not url or not format:
        return jsonify({'error': 'No URL or format provided'}), 400

    try:
        file_path, title, size, file_type = download_from_url(url, format)
        size_mb = size / (1024 * 1024)  # Convert size to megabytes
        return jsonify({'file_path': file_path, 'title': title, 'size': size_mb, 'type': file_type}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@download_bp.route('/download-file', methods=['GET'])
def download_file():
    file_path = request.args.get('file_path')
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    return send_file(file_path, as_attachment=True)
