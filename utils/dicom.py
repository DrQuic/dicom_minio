from fastapi import UploadFile, File

async def verify_file(file: UploadFile = File(...)):
    # ir al header -> buscarm DICM
    print(file) 
    return "ok"