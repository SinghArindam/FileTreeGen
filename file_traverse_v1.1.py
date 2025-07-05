import os
import json
from datetime import datetime

def get_file_info(file_path):
    """Get comprehensive file information"""
    try:
        stat = os.stat(file_path)
        size = stat.st_size
        
        return {
            'size': get_size_in_units(size),
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
            'extension': os.path.splitext(file_path)[1].lower()
        }
    except (OSError, IOError):
        return {
            'size': get_size_in_units(0),
            'modified': None,
            'created': None,
            'extension': None,
            'error': 'Could not access file'
        }

def traverse_directory_enhanced(path, ignore_hidden=True):
    """Enhanced version with more file details"""
    structure = []
    
    for root, dirs, files in os.walk(path):
        # Filter out hidden directories if ignore_hidden is True
        if ignore_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        rel_root = os.path.relpath(root, path)
        
        for file in files:
            # Skip hidden files if ignore_hidden is True
            if ignore_hidden and file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.join(rel_root, file)
            
            file_info = get_file_info(file_path)
            structure.append({
                'relative_path': rel_path,
                **file_info
            })
    
    return structure

def get_size_in_units(size_bytes):
    """Convert bytes to KB, MB, GB with proper rounding"""
    kb = size_bytes / 1024
    mb = size_bytes / (1024 ** 2)
    gb = size_bytes / (1024 ** 3)
    return {
        'bytes': size_bytes,
        'kb': round(kb, 2),
        'mb': round(mb, 2),
        'gb': round(gb, 2)
    }

def traverse_directory(path, ignore_hidden=True):
    """Traverse directory and collect file information"""
    structure = []
    
    for root, dirs, files in os.walk(path):
        # Filter out hidden directories if ignore_hidden is True
        if ignore_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Get relative path from starting directory
        rel_root = os.path.relpath(root, path)
        
        # Process each file
        for file in files:
            # Skip hidden files if ignore_hidden is True
            if ignore_hidden and file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
            except (OSError, IOError):
                # Handle files that can't be accessed
                size = 0
            
            structure.append({
                'relative_path': os.path.join(rel_root, file),
                'size': get_size_in_units(size)
            })
    
    return structure

# Main execution
def main():
    # Configuration options
    ignore_hidden_files = True  # Set to False to include hidden files
    
    # Traverse current directory
    result = traverse_directory('.', ignore_hidden=ignore_hidden_files)
    # result = traverse_directory_enhanced('.', ignore_hidden=ignore_hidden_files)
    
    # Save to JSON file
    with open('file_structure.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Found {len(result)} files")
    print(f"Hidden files ignored: {ignore_hidden_files}")
    print("File structure saved to 'file_structure.json'")
    
    # Preview first few entries
    print("\nFirst 3 entries:")
    for entry in result[:3]:
        print(f"- {entry['relative_path']}: {entry['size']['mb']} MB")

if __name__ == "__main__":
    main()
