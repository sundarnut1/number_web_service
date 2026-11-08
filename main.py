from fastapi import FastAPI, Path
from converter import NumberConverter

app = FastAPI(
    title="Number Converter API",
    description="An API that converts integers into their word representations.",
    version="1.0.0"
)

converter = NumberConverter()

@app.get("/convert/{number}", summary="Convert an integer to words")
def convert_number(
    number: int = Path(..., description="An integer between 0 and 10 to convert[cite: 1]", example=5)
):
    """
    Takes an integer input[cite: 1] and returns its string word equivalent.
    """
    result = converter.convert(number)
    return {"input": number, "result": result}
