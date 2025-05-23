# File Management System with Huffman Coding and Tree-Based Indexing

This project implements a simplified file compression and indexing system as part of a computer algorithms course. The system provides the following key functionalities:

## 🔧 Features

- **Huffman Coding** for compressing and decompressing text files
- **Red-Black Tree** for efficient filename searching
- **B-Tree** for alphabetically indexing and listing files
- **Terminal-based CLI** to manage compression, decompression, insertion, and search operations
- **.huff** and **.meta** output files for compressed binary data and Huffman code maps
- Visualization support for Red-Black Tree structure in the terminal

##  Technologies

- Python 3
- `heapq`, `collections.Counter`, `json`
- No external dependencies required for core functionality

##  Folder Structure

- `main.py`: CLI interface
- `hufmann.py`: Huffman compression logic
- `red_black_tree.py`: Red-Black Tree structure
- `b_tree.py`: B-Tree implementation
- `sample.txt`: Example file for compression testing
