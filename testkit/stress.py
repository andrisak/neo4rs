"""
Executed in Rust driver container.
Responsible for invoking Rust stress test suite.
The stress test might be invoked multiple times against different versions
of Neo4j.
Assumes driver has been built before.
"""
import subprocess
import os

if __name__ == "__main__":
    print("TODO: Execute stress tests")
