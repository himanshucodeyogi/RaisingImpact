import zipfile
import re
import json

def extract_theme_colors(file_path):
    with zipfile.ZipFile(file_path, 'r') as z:
        # List all files
        print("=== ALL FILES IN PPTX ===")
        for f in sorted(z.namelist()):
            if 'theme' in f.lower() or 'slide' in f.lower() or 'master' in f.lower() or 'layout' in f.lower():
                print(f)
        
        # Read theme files
        theme_files = [f for f in z.namelist() if 'theme' in f.lower() and f.endswith('.xml')]
        for tf in theme_files:
            print(f"\n=== {tf} ===")
            with z.open(tf) as f:
                content = f.read().decode('utf-8')
                # Extract color scheme
                # Find srgbClr values
                srgb_colors = re.findall(r'<a:srgbClr val="([A-Fa-f0-9]{6})"\s*/?>', content)
                print(f"sRGB Colors found: {srgb_colors}")
                
                # Find color scheme names and values
                color_scheme = re.findall(r'<a:(dk1|dk2|lt1|lt2|accent\d|hlink|folHlink)>(.*?)</a:\1>', content, re.DOTALL)
                print(f"\nColor Scheme Elements:")
                for name, inner in color_scheme:
                    srgb = re.findall(r'val="([A-Fa-f0-9]{6})"', inner)
                    sys_clr = re.findall(r'lastClr="([A-Fa-f0-9]{6})"', inner)
                    color = srgb[0] if srgb else (sys_clr[0] if sys_clr else "unknown")
                    print(f"  {name}: #{color}")
                
                # Find font scheme
                fonts = re.findall(r'<a:(latin|ea|cs)\s+typeface="([^"]+)"', content)
                print(f"\nFonts:")
                seen = set()
                for ftype, fname in fonts:
                    if fname not in seen:
                        print(f"  {ftype}: {fname}")
                        seen.add(fname)
        
        # Check slide master for additional styling
        master_files = [f for f in z.namelist() if 'slideMaster' in f and f.endswith('.xml')]
        for mf in master_files:
            print(f"\n=== {mf} (colors) ===")
            with z.open(mf) as f:
                content = f.read().decode('utf-8')
                srgb_colors = set(re.findall(r'val="([A-Fa-f0-9]{6})"', content))
                print(f"Unique colors: {sorted(srgb_colors)}")
        
        # Check slide layouts
        layout_files = [f for f in z.namelist() if 'slideLayout' in f and f.endswith('.xml')]
        for lf in layout_files:
            with z.open(lf) as f:
                content = f.read().decode('utf-8')
                srgb_colors = set(re.findall(r'srgbClr val="([A-Fa-f0-9]{6})"', content))
                if srgb_colors:
                    print(f"\n{lf} colors: {sorted(srgb_colors)}")
        
        # Check individual slides for colors
        slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        for sf in sorted(slide_files):
            with z.open(sf) as f:
                content = f.read().decode('utf-8')
                srgb_colors = set(re.findall(r'srgbClr val="([A-Fa-f0-9]{6})"', content))
                if srgb_colors:
                    print(f"\n{sf} colors: {sorted(srgb_colors)}")

        # Check for images
        print("\n=== IMAGES ===")
        for f in z.namelist():
            if any(ext in f.lower() for ext in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.emf', '.wmf']):
                info = z.getinfo(f)
                print(f"  {f} ({info.file_size} bytes)")

if __name__ == "__main__":
    extract_theme_colors(r"RaisingImpact_sample slides.pptx")
