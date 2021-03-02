from docx import Document


def doc_converter():
    new = docx.Document("New Document")
    print(new)


if __name__ == "__main__":
    doc_converter()