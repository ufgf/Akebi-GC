# pylint: disable=C0114:missing-docstring, C0301:line-too-long, C0103:invalid-name, R1727:condition-evals-to-constant, W1514:unspecified-encoding, W0703:broad-except

print("- Making some small changes to sources...")

try:
    with open('cheat-library/cheat-library.vcxproj', 'r+', newline="") as f:
        print("- commenting out CustomBuildStep sections... ", end="")
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            if '<CustomBuildStep>' or '</CustomBuildStep>' in line:
                line = line.replace('<CustomBuildStep>', '<!-- <CustomBuildStep>').replace('</CustomBuildStep>', '</CustomBuildStep> -->')
                f.write(line)

except Exception as e:
    print(f"unsuccessful ({e.__class__}: {e}).")

print("done.")
