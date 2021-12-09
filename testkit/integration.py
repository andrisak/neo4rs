import subprocess


def run(args):
    subprocess.run(
        args, universal_newlines=True, stderr=subprocess.STDOUT, check=True)


if __name__ == "__main__":
    print("TODO: Run integration tests")
    # run(["cargo", "test --doc"])
