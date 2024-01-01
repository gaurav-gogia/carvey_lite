# Set paths for source and destination files
src_file_path = ""
dst_file_path = ""

# Define header and footer for PNG files
PNG_HEADER = bytes([0x89, 0x50, 0x4e, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
PNG_FOOTER = bytes([0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE, 0x42, 0x60, 0x82])

# Read the source file into a byte array
src_data = open(src_file_path, "rb").read()

# Initialize position and counter for carved files
position = 0
count = 0

while True:
    # Find the next header starting from the current position
    header_index = src_data.find(PNG_HEADER, position)
    if header_index == -1:
        break  # Exit if no header is found

    # Find the next footer starting from the header
    footer_index = src_data.find(PNG_FOOTER, header_index)
    if footer_index == -1:
        break  # Exit if no footer is found for the current header

    # Calculate the end of the footer
    footer_end = footer_index + len(PNG_FOOTER)

    # Ensure the footer is after the header
    if header_index < footer_index:
        count += 1
        dst_data = src_data[header_index:footer_end]
        dst_file_name = f"{dst_file_path}_{count}.png"
        open(dst_file_name, "wb").write(dst_data)
        print("Carved:", dst_file_name)

    # Update position to search for the next PNG file
    position = footer_end

# Print the total number of carved files
print(f"Total carved files: {count}")
