import yaml
import os
import re
from jinja2 import Environment, FileSystemLoader

# 1. LaTeX Escaping Filter (Essential for professional PDFs)
def tex_escape(text):
    """
        :param text: the mistake-prone text
        :return: the escaped text
    """
    if not isinstance(text, str):
        return text
    regex = re.compile(r'([&%$#_{}])')
    return regex.sub(r'\\\1', text)

# 2. Setup Jinja2 Environment
env = Environment(
    loader=FileSystemLoader('.'),
    block_start_string='((%',
    block_end_string='%))',
    variable_start_string='((*',
    variable_end_string='*))',
    comment_start_string='((#',
    comment_end_string='#))',
)
env.filters['te'] = tex_escape

def generate_cvs():
    data_dir = 'data'
    template_file = 'templates/cv.tex.j2'
    
    # Ensure the data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Directory '{data_dir}' not found.")
        return

    # 3. Process every YAML file in the data folder
    # This assumes files are named like 'cv_en.yml', 'cv_it.yml', etc.
    for filename in os.listdir(data_dir):
        if filename.startswith('cv_') and filename.endswith('.yml'):
            # Extract language code (e.g., 'en' from 'cv_en.yml')
            lang_code = filename.split('_')[1].replace('.yml', '')
            
            yaml_path = os.path.join(data_dir, filename)
            output_tex = f"cv_{lang_code}.tex"
            
            print(f"Processing {lang_code.upper()} version...")

            try:
                # Load the specific language data
                with open(yaml_path, 'r', encoding='utf-8') as f:
                    cv_data = yaml.safe_load(f)

                # Render the template
                template = env.get_template(template_file)
                rendered_tex = template.render(**cv_data)

                # Write the .tex file
                with open(output_tex, 'w', encoding='utf-8') as f:
                    f.write(rendered_tex)
                
                print(f"✅ Successfully generated {output_tex}")
                
            except Exception as e:
                print(f"❌ Failed to generate {output_tex}: {e}")

if __name__ == "__main__":
    generate_cvs()
