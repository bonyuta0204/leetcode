# Compiler and flags
ASM = nasm
ASM_FLAGS = -f elf64
CC = gcc
LINKER_FLAGS = -no-pie -o

# Directories
SRC_DIR = src
BIN_DIR = bin

# Sources and targets
SRCS = $(wildcard $(SRC_DIR)/*.s)
OBJS = $(patsubst $(SRC_DIR)/%.s, $(BIN_DIR)/%.o, $(SRCS))
BINS = $(patsubst $(SRC_DIR)/%.s, $(BIN_DIR)/%, $(SRCS))

# Default target
all: $(BINS)

# Rule for creating binary executables
$(BIN_DIR)/%: $(BIN_DIR)/%.o
	@mkdir -p $(BIN_DIR)
	$(CC) $(LINKER_FLAGS) $@ $<

# Rule for assembling source files
$(BIN_DIR)/%.o: $(SRC_DIR)/%.s
	@mkdir -p $(BIN_DIR)
	$(ASM) $(ASM_FLAGS) -o $@ $<

# Clean up build artifacts
clean:
	rm -rf $(BIN_DIR)

# Utility targets
.PHONY: all clean