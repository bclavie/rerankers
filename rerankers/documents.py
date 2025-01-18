from typing import Optional, Union, Literal


class Document:
    def __init__(
        self,
        text: Optional[str] = None,
        doc_id: Optional[Union[str, int]] = None,
        metadata: Optional[dict] = None,
        document_type: Literal["text", "image"] = "text",
        image_path: Optional[str] = None,
        base64: Optional[str] = None,
    ):
        self.document_type = document_type
        self.text = text
        self.base64 = base64
        self.image_path = image_path
        self.doc_id = doc_id
        self.metadata = metadata if metadata is not None else {}
        
        # Validation
        if self.document_type == "text" and self.text is None:
            raise ValueError("text field is required when document_type is 'text'")
