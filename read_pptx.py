import zipfile
import re
import sys
import xml.etree.ElementTree as ET

def extract_text_from_pptx(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as z:
            slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            
            # Sort slides numerically
            def slide_num(filename):
                m = re.search(r'slide(\d+)\.xml', filename)
                return int(m.group(1)) if m else 0
                
            slide_files.sort(key=slide_num)
            
            for idx, sf in enumerate(slide_files, 1):
                with z.open(sf) as f:
                    content = f.read().decode('utf-8')
                    # Find texts in <a:t>
                    texts = re.findall(r'<a:t>(.*?)</a:t>', content)
                    print(f"--- Slide {idx} ---")
                    for t in texts:
                        print(t)
                    print("\n")
    except Exception as e:
        print(f"Error reading pptx: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_text_from_pptx(sys.argv[1])
