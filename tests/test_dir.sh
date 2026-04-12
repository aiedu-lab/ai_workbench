#!/usr/bin/env bash

TEST_DIR = "../.tmp/test_dir"
mkdir -p $TEST_DIR
cd $TEST_DIR

# Create dummy files of different types and sizes
truncate -s 1K very_small_file_tom.txt
truncate -s 1K very_small_file_alice.pdf
truncate -s 2K small_file_susan.jpg
truncate -s 2K small_file_charlie.mp4
truncate -s 4K medium_file_bob.pdf
truncate -s 4K medium_file_lisa.jpg
truncate -s 8K large_file_harry.txt
truncate -s 8K large_file_david.mp4
