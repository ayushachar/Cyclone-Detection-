import argparse, zipfile, os

def main():
    parser = argparse.ArgumentParser(description='Create zip of Task1, Task2, and final presentation')
    parser.add_argument('--name', required=True, help='Your name for the zip file')
    args = parser.parse_args()
    zip_name = f"{args.name}_DataScience.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for folder in ['Task1', 'Task2']:
            if os.path.isdir(folder):
                for root, _, files in os.walk(folder):
                    for f in files:
                        file_path = os.path.join(root, f)
                        arcname = os.path.relpath(file_path, '.')
                        z.write(file_path, arcname)
        pptx_path = 'Final_Presentation.pptx'
        if os.path.isfile(pptx_path):
            z.write(pptx_path, os.path.basename(pptx_path))
    print(f'Created {zip_name}')

if __name__ == '__main__':
    main()
