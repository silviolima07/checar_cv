from pdfreader import SimplePDFViewer


def read_pdf(file_path):
    with open(file_path, "rb") as f:
        viewer = SimplePDFViewer(f)
        text_content = ""
        viewer.render()

        for canvas in viewer:
            text_content += "".join(canvas.strings)

    return text_content
        
def save_uploaded_pdf(uploaded_file, destination_path):
    with open(destination_path, "wb") as f:
        f.write(uploaded_file.read())
    return destination_path
        
    
    return text_content
    
