
import json
startermem = {
    'closestlow': 0,
    'closesthigh': 12,
    'totalachived': False,
    'totalnum': ""
}
def save(startermem):
    with open('Brain/Memory/memory.json', 'w') as file:
        json.dump(startermem, file, indent=4)
#render
try:
    with open('Brain/Memory/memory.json', 'r') as file:
        memory = json.load(file)
        print("Mem Load Success!")
except FileNotFoundError:
    memory = startermem
    print("! ERROR Mem Not Found !")
save(startermem)
