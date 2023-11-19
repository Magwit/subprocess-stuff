import subprocess
from icecream import ic


def test_reverse():
    cypher_app = subprocess.run(
        "python cypher.py reverse Test123", shell=True, capture_output=True, text=True
    )
    assert cypher_app.returncode == 0
    assert "321tseT" in cypher_app.stdout


def test_shuffle():
    cypher_app = subprocess.run(
        "python cypher.py shuffle Test123", shell=True, capture_output=True, text=True
    )
    assert cypher_app.returncode == 0
    assert "3" in cypher_app.stdout


def test_reverse_and_shuffle():
    reverse_invocation = subprocess.run(
        "python cypher.py reverse Test123", shell=True, capture_output=True, text=True
    )
    reverse_output = reverse_invocation.stdout
    dynamic_command = f"python cypher.py shuffle {reverse_output}"
    ic(reverse_output)
    assert reverse_invocation.returncode == 0

    shuffle_invocation = subprocess.run(
        dynamic_command,
        shell=True,
        capture_output=True,
        text=True,
    )
    assert shuffle_invocation.returncode == 0
    assert "3" in shuffle_invocation.stdout


# def test_output():
#     assert "This is the app!" in the_app.stdout


# ic(the_app.args)

# Capture output from one command and have that be input to another LIKE A TOKEN!

# aLL content of drivel.txt
crawler1 = subprocess.run("cat drivel.txt", shell=True, capture_output=True, text=True)

# Grep by 'lines' as text match
crawler2 = subprocess.run(
    "grep -n lines", shell=True, capture_output=True, text=True, input=crawler1.stdout
)
ic(crawler2.stdout)
