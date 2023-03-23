#!Python modules
import uuid


#!random_code
def random_code() -> str:
    generated_number = str(uuid.uuid4())[:12].replace("-", "").upper()
    return generated_number
