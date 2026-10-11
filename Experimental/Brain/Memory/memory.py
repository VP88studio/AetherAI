
import json, os
startermem = {
    'closestlow': 0,
    'closesthigh': 12,
    'totalachived': False,
    'totalnum': ""
}
def save(startermem):
    try:
        with open('Brain/Memory/memory.json', 'w') as file:
            json.dump(startermem, file, indent=4)
    except json.decoder.JSONDecodeError:
        os.remove('Brain/Memory/memory.json')
        print('! JSONDECODE ERROR FILE REMOVED !')
        quit()
#render
try:
    with open('Brain/Memory/memory.json', 'r') as file:
        try:
            memory = json.load(file)
            print("Mem Load Success!")
            print(memory)
        except json.decoder.JSONDecodeError:
            os.remove('Brain/Memory/memory.json')
            print('! JSONDECODE ERROR FILE REMOVED !')
            quit()
except FileNotFoundError:
    memory = startermem
    save(memory)
    print("! ERROR Mem Not Found !")
    print(memory)
save(memory)
