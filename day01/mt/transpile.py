import os

def transpile():
    input_path = "../input.txt"
    output_path = "data.go"

    # Handle symlink vs real file check
    if not os.path.exists(input_path):
        input_path = "input.txt"

    with open(input_path, "r") as f:
        # Filter empty lines
        raw_lines = [line.strip() for line in f if line.strip()]
    
    count = len(raw_lines)
    is_right = []
    distances = []

    # Parse logic: First char is direction, rest is int
    for line in raw_lines:
        # Convert directly to bool: True if 'R', False if 'L'
        is_right.append(line[0] == 'R')
        try:
            # Python's int() handles whitespace automatically
            distances.append(int(line[1:].strip()))
        except ValueError:
            distances.append(0)
    
    # BIT PACKING: Pack 64 booleans into one uint64
    bit_chunks = []
    current_chunk = 0
    for i, r in enumerate(is_right):
        if r:
            # Set the K-th bit in the current chunk
            current_chunk |= (1 << (i % 64))
        
        # If chunk is full (every 64th item), save and reset
        if (i + 1) % 64 == 0:
            bit_chunks.append(current_chunk)
            current_chunk = 0
            
    # Capture any remaining bits in the last partial chunk
    if count % 64 != 0:
        bit_chunks.append(current_chunk)

    chunk_count = len(bit_chunks)

    with open(output_path, "w") as f:
        f.write("package main\n\n")
        
        # EXPORT CONSTANTS so p01.go can loop exactly this many times
        f.write(f"const Count = {count}\n")
        f.write(f"const ChunkCount = {chunk_count}\n\n")

        f.write("// Structure of Arrays (SoA) layout\n")
        
        f.write("// 1. DirectionsBits: Packed bitset (1 bit per value)\n")
        f.write("// Access: (DirectionsBits[i/64] >> (i%64)) & 1\n")
        f.write(f"var DirectionsBits = [{chunk_count}]uint64{{\n") 
        for chunk in bit_chunks:
            # Write in Hex for cleaner bit representation
            f.write(f"\t0x{chunk:X},\n")
        f.write("}\n\n")

        f.write("// 2. Distances parsed as integers\n")
        f.write(f"var Distances = [{count}]int{{\n")
        for n in distances:
            f.write(f"\t{n},\n")
        f.write("}\n")

if __name__ == "__main__":
    transpile()
