from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            if content.startswith("# "):
                return f"<h1>{content[2:]}</h1>"

        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"

        case (DocFormat.HTML, DocFormat.MD):
            if content.startswith("<h1>") and content.endswith("</h1>"):
                inner_text = content[4:-5]  # remove <h1> and </h1>
                return f"# {inner_text}"

        case _:
            raise Exception("invalid type")

