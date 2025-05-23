# ------------------- MAIN MENU -------------------

from pathlib import Path
from hufmann import *
from red_black_tree import *
from b_tree import *

def main_menu():
    print("\n--- File Management System ---")
    print("1. Compress File (Huffman)")
    print("2. Decompress File")
    print("3. Insert File (Indexing)")
    print("4. Search File (RBT)")
    print("5. List Files (B-Tree)")
    print("6. Search File (B-Tree)")
    print("7. Display RBT Structure in Terminal")
    print("0. Exit")

def print_rbtree(node, indent="", last=True, NIL=None):
    if node is None or node == NIL:
        return
    print(indent, end="")
    if last:
        print("└──", end="")
        indent += "    "
    else:
        print("├──", end="")
        indent += "│   "
    color = "R" if node.color == 'red' else "B"
    print(f"{node.key} ({color})")
    print_rbtree(node.left, indent, False, NIL)
    print_rbtree(node.right, indent, True, NIL)

def run_system():
    rbtree = RedBlackTree()
    btree = BTree(t=2)

    while True:
        main_menu()
        secim = input("Your choice: ")

        if secim == "1":
            filename = input("Enter the name of the file to compress (e.g., input.txt): ")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    text = f.read()
                huffman_tree = build_huffman_tree(text)
                code_map = generate_codes(huffman_tree)
                encoded = compress(text, code_map)
                base_name = Path(filename).stem
                save_compressed(base_name, encoded, code_map)
                print(f"File compressed: {base_name}.huff and {base_name}.meta")
            except FileNotFoundError:
                print("File not found!")

        elif secim == "2":
            filename = input("Enter the name of the file to decompress (name only, without extension): ")
            try:
                encoded, tree = load_compressed(filename)
                decoded = decompress(encoded, tree)
                output_file = filename + "_decoded.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(decoded)
                print(f"File decompressed and saved as: {output_file}")
            except FileNotFoundError:
                print(".huff or .meta file not found!")

        elif secim == "3":
            filename = input("Enter the filename to insert (e.g., file1.txt): ")
            rbtree.insert(filename)
            btree.insert(filename)
            print(f"{filename} has been added to the system.")

        elif secim == "4":
            name = input("Enter the filename to search: ")
            found = rbtree.search(name)
            print(f"{name} found." if found else "File not found.")

        elif secim == "5":
            print("File list (ordered by B-Tree):")
            btree.traverse()

        elif secim == "6":
            name = input("Enter the filename to search in B-Tree: ")
            found = btree.search(name)
            print(f"{name} found in B-Tree." if found else "File not found in B-Tree.")

        elif secim == "7":
            print("Red-Black Tree:")
            print_rbtree(rbtree.root, NIL=rbtree.NIL)

        elif secim == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run_system()