import yaml
import re
from jinja2 import Environment, FileSystemLoader

def tex_escape(text):
    """
    Finds and escapes LaTeX special characters found in the YAML strings.
    """
    if not isinstance(text, str):
        return text
    
    # Map of LaTeX special characters to their escaped versions
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    
    # Create a regex pattern to match any of the keys in the conv dict
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key=lambda item: -len(item))))
    return regex.sub(lambda mo: conv[mo.group()], text)

def main():
    # 1. Load the single source of truth
    try:
        with open("data/cv.yml", "r") as f:
            cv_data = yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: data/cv.yml not found.")
        return

    # 2. Setup Jinja2 with LaTeX-friendly delimiters
    env = Environment(
        loader=FileSystemLoader('templates'),
        block_start_string='((%',
        block_end_string='%))',
        variable_start_string='((*',
        variable_end_string='*))',
        comment_start_string='((#',
        comment_end_string='#))',
        autoescape=False # LaTeX isn't HTML, so we handle escaping manually
    )

    # 3. Register our custom LaTeX escape filter
    # Usage in template: ((* variable | te *))
    env.filters['te'] = tex_escape

    # 4. Render the template
    try:
        template = env.get_template("cv.tex.j2")
        output = template.render(**cv_data)
        
        # 5. Write the resulting .tex file
        with open("cv.tex", "w") as f:
            f.write(output)
        print("🚀 Successfully generated cv.tex")
        
    except Exception as e:
        print(f"Error during rendering: {e}")

if __name__ == "__main__":
    main()
