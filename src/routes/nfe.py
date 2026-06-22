from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import tempfile
import shutil
from datetime import datetime

nfe_bp = Blueprint('nfe', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xml'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@nfe_bp.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'files' not in request.files:
            return jsonify({'error': 'Nenhum arquivo foi enviado'}), 400
        
        files = request.files.getlist('files')
        
        if not files or files[0].filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        # Criar diretório temporário para os uploads
        temp_dir = tempfile.mkdtemp()
        uploaded_files = []
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(temp_dir, filename)
                file.save(file_path)
                uploaded_files.append(file_path)
        
        if not uploaded_files:
            return jsonify({'error': 'Nenhum arquivo XML válido foi enviado'}), 400
        
        # Processar os arquivos XML
        from src.nfe_processor import NFEProcessor
        processor = NFEProcessor()
        excel_path = processor.process_files(uploaded_files)
        
        # Limpar arquivos temporários
        shutil.rmtree(temp_dir)
        
        return jsonify({
            'success': True,
            'message': f'Processados {len(uploaded_files)} arquivos XML com sucesso',
            'download_url': f'/api/nfe/download/{os.path.basename(excel_path)}'
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao processar arquivos: {str(e)}'}), 500

@nfe_bp.route('/download/<filename>')
def download_file(filename):
    try:
        downloads_dir = os.path.join(os.path.dirname(__file__), '..', 'downloads')
        return send_file(
            os.path.join(downloads_dir, filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': f'Erro ao baixar arquivo: {str(e)}'}), 500

